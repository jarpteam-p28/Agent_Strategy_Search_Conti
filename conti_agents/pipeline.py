"""Weekly pipeline: transcripts -> paper queue -> read -> strategize -> critique -> report."""
from __future__ import annotations

import hashlib
import logging
import traceback
from dataclasses import dataclass, field

from . import agents
from .store import Repo, slugify, today

log = logging.getLogger(__name__)
MAX_ATTEMPTS = 3


@dataclass
class RunReport:
    transcripts: list[dict] = field(default_factory=list)
    papers: list[dict] = field(default_factory=list)
    strategies: list[dict] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    scouted: int = 0
    librarian: int = 0


def _file_hash(path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()[:16]


# ---------------------------------------------------------------------------------------------
def process_transcripts(repo: Repo, llm, report: RunReport) -> None:
    idx = repo.transcript_index()
    for t in repo.transcript_files():
        h = _file_hash(t)
        if idx.get(t.name, {}).get("hash") == h:
            continue
        log.info("mining transcript %s", t.name)
        try:
            out = agents.mine_transcript(repo, llm, t)
        except Exception as e:  # keep the weekly run going
            report.errors.append(f"transcript {t.name}: {e}")
            continue
        n = len([p for p in repo.path("strategies/conti").glob("*.yaml")])
        ids = []
        for i, st in enumerate(out.get("strategies", []), start=1):
            repo.save_strategy(st, folder="strategies/conti", prefix=f"{n + i:02d}_")
            ids.append(st["id"])
            report.strategies.append({"id": st["id"], "name": st.get("name"), "origin": t.name,
                                      "verdict": "(from Conti - not reviewed)"})
        added = repo.add_seeds(out.get("papers_referenced", []))
        if out.get("method_notes"):
            notes = repo.read_text("knowledge/method_notes.md", "# Method notes from transcripts\n")
            notes += f"\n## {t.name} — {out.get('title', '')}\n\n" + "\n".join(f"- {m}" for m in out["method_notes"]) + "\n"
            repo.write_text("knowledge/method_notes.md", notes)
        idx[t.name] = {"hash": h, "title": out.get("title"), "summary": out.get("summary"),
                       "strategies": ids, "processed": today()}
        report.transcripts.append({"file": t.name, "strategies": ids, "papers_added": added})
    repo.save_transcript_index(idx)


# ---------------------------------------------------------------------------------------------
def build_queue(repo: Repo, llm, report: RunReport, limit: int, scout: bool) -> list[dict]:
    idx = repo.paper_index()

    def pending(slug):
        e = idx.get(slug)
        return e is None or (e["status"] in ("queued", "failed") and e.get("attempts", 0) < MAX_ATTEMPTS)

    # 1. PDFs dropped in papers/inbox (full text guaranteed). A PDF named after a paper's id
    #    (e.g. the file name shown in READING_LIST.md) upgrades that paper to a full read.
    for pdf in repo.inbox_pdfs():
        if pdf.stem in idx and idx[pdf.stem].get("read_mode") != "full_pdf":
            e = idx[pdf.stem]
            if e.get("local_pdf") != str(pdf.relative_to(repo.root)):
                e.update(local_pdf=str(pdf.relative_to(repo.root)), status="queued", attempts=0)
            continue
        slug = "inbox_" + _file_hash(pdf)
        if pending(slug):
            idx.setdefault(slug, {"title": pdf.stem, "origin": "inbox", "status": "queued", "attempts": 0})
            idx[slug]["local_pdf"] = str(pdf.relative_to(repo.root))
    # 2. Papers Conti named
    for s in repo.seeds():
        slug = slugify(s["title"])
        if pending(slug):
            idx.setdefault(slug, {**s, "origin": "seed", "status": "queued", "attempts": 0})
    queue = [dict(v, slug=k) for k, v in idx.items() if pending(k)]
    origin_rank = {"inbox": 0, "seed": 1, "librarian": 2, "scout": 3}
    queue.sort(key=lambda p: (0 if p.get("local_pdf") else 1, origin_rank.get(p.get("origin"), 4),
                              p.get("priority", 3), p.get("attempts", 0)))

    # 3. Scout for new papers if there's room this week
    if scout and len(queue) < limit:
        try:
            lim = repo.settings().get("limits", {})
            found = agents.scout(repo, llm, [v.get("title", "") for v in idx.values()],
                                 lim.get("max_new_candidates", 8))
            for c in found:
                slug = slugify(c["title"])
                if slug not in idx:
                    idx[slug] = {**c, "origin": "scout", "status": "queued", "attempts": 0}
                    queue.append(dict(idx[slug], slug=slug))
                    report.scouted += 1
        except Exception as e:
            report.errors.append(f"scout: {e}")
    repo.save_paper_index(idx)
    return queue[:limit]


# ---------------------------------------------------------------------------------------------
def process_paper(repo: Repo, llm, paper: dict, report: RunReport) -> None:
    idx = repo.paper_index()
    slug = paper["slug"]
    entry = idx[slug]
    entry["attempts"] = entry.get("attempts", 0) + 1
    try:
        if not paper.get("local_pdf") and not (paper.get("url") or paper.get("pdf_url")):
            paper = agents.resolve(repo, llm, paper)
            entry.update({k: paper.get(k) for k in ("url", "pdf_url", "venue") if paper.get(k)})
        summary = agents.read_paper(repo, llm, paper, cache_path=repo.path(f"papers/pdfs/{slug}.pdf"))
        if paper.get("origin") == "inbox" and summary.get("title"):
            entry["title"] = summary["title"]
        ref = f"papers/summaries/{slug}.md"
        repo.save_json(f"papers/summaries/{slug}.json", summary)
        repo.write_text(ref, agents.summary_markdown(summary))
        entry.update(status="summarized", read_mode=summary.get("read_mode"), summary=ref, updated=today())
        repo.save_paper_index(idx)
        repo.add_seeds(summary.get("referenced_papers_worth_reading", [])[:3])

        out = agents.strategize(repo, llm, summary, ref)
        ids = []
        for st in out.get("strategies", []):
            try:
                st["review"] = agents.critique(repo, llm, st, summary)
                verdict = st["review"].get("verdict")
                if verdict == "reject":
                    st["status"] = "rejected"
                elif verdict == "park":
                    st["status"] = "parked"
            except Exception as e:
                report.errors.append(f"critic {st['id']}: {e}")
                verdict = "(review failed)"
            repo.save_strategy(st)
            ids.append(st["id"])
            report.strategies.append({"id": st["id"], "name": st.get("name"), "origin": entry.get("title"),
                                      "verdict": verdict, "scores": st.get("review", {}).get("scores")})
        entry.update(strategies=ids, skipped_reason=out.get("skipped_reason"))
        report.papers.append({"title": entry.get("title"), "read_mode": summary.get("read_mode"),
                              "summary": ref, "one_line": summary.get("one_line"),
                              "why": summary.get("why", {}).get("pattern"), "strategies": ids,
                              "skipped_reason": out.get("skipped_reason")})
    except Exception as e:
        entry.update(status="failed", error=str(e)[:300], updated=today())
        report.errors.append(f"paper '{entry.get('title')}': {e}")
        log.debug(traceback.format_exc())
    idx[slug] = entry
    repo.save_paper_index(idx)


# ---------------------------------------------------------------------------------------------
def reading_list_tracks(repo: Repo) -> dict:
    tracks = (repo.load_yaml("config/search_topics.yaml", {}) or {}).get("librarian_tracks") or {}
    return tracks or {"index_futures": {"label": "ES / NQ / index futures"}}


def update_reading_list(repo: Repo, llm, report: RunReport, search: bool) -> None:
    """Ask the librarian for new papers on each track, then write papers/READING_LIST.md.

    Part 1: papers the agents could not read in full (download these and drop them in
    papers/inbox/ under the shown file name). Then one section of recommendations per track.
    """
    idx = repo.paper_index()
    tracks = reading_list_tracks(repo)
    if search:
        n = repo.settings().get("limits", {}).get("max_reading_list", 8)
        for track in tracks:
            try:
                for p in agents.librarian(repo, llm, [v.get("title", "") for v in idx.values()], n, track):
                    slug = slugify(p["title"])
                    if slug not in idx:
                        idx[slug] = {**p, "origin": "librarian", "status": "queued", "attempts": 0, "added": today()}
                        report.librarian += 1
            except Exception as e:
                report.errors.append(f"librarian ({track}): {e}")
        repo.save_paper_index(idx)

    need_pdf = [(k, v) for k, v in idx.items()
                if v.get("status") == "failed" or v.get("read_mode") in ("abstract_only", "web_fetch")]
    L = ["# Reading list — papers to download", "",
         f"Updated {today()}. Download each PDF and save it in `papers/inbox/` **using the file name shown** "
         "(or attach it in chat). The next run reads the full paper and replaces the partial summary.", ""]
    L += ["## 1. Couldn't get the full text — please download", ""]
    if need_pdf:
        L += ["| Paper | Why it matters | Where to get it | Save as |", "|---|---|---|---|"]
        for k, v in need_pdf:
            why = v.get("note") or v.get("why_promising") or ""
            where = v.get("where_to_get_it") or v.get("url") or "search the title on ssrn.com / Google Scholar"
            got = "abstract only" if v.get("read_mode") == "abstract_only" else ("partial" if v.get("read_mode") else "failed")
            L.append(f"| {v.get('title')} ({v.get('year') or '?'}) — *{got}* | {why} | {where} | `{k}.pdf` |")
    else:
        L.append("Nothing pending.")

    for i, (track, cfg) in enumerate(tracks.items(), start=2):
        recs = sorted([(k, v) for k, v in idx.items()
                       if v.get("origin") == "librarian" and v.get("status") == "queued"
                       and v.get("track", "index_futures") == track],
                      key=lambda kv: (kv[1].get("priority", 3), kv[0]))
        L += ["", f"## {i}. Recommended research — {cfg.get('label', track)}", ""]
        if not recs:
            L.append("No open recommendations yet.")
        for k, v in recs:
            L += [f"### P{v.get('priority', 3)} · {v.get('title')} ({v.get('year') or '?'})",
                  f"*{', '.join(v.get('authors') or [])}* · instruments: {', '.join(v.get('instruments') or []) or '-'} · "
                  f"access: {v.get('access', 'unknown')} · testable on our data: {v.get('testable_on_our_data', '?')}", "",
                  f"- **Why:** {v.get('why_promising', '')}",
                  f"- **Should contain:** {v.get('what_it_should_contain', '')}",
                  f"- **Get it:** {v.get('where_to_get_it', '')} {v.get('url') or ''}",
                  f"- **Save as:** `papers/inbox/{k}.pdf`", ""]
    repo.write_text("papers/READING_LIST.md", "\n".join(L) + "\n")


# ---------------------------------------------------------------------------------------------
def write_report(repo: Repo, report: RunReport, usage) -> str:
    rel = f"reports/{today()}.md"
    L = [f"# Weekly research run — {today()}", ""]
    L += [f"Papers read: **{len(report.papers)}** · New strategies: **{len(report.strategies)}** · "
          f"Scouted: **{report.scouted}** · Added to reading list: **{report.librarian}** · "
          f"Errors: **{len(report.errors)}**", "",
          "Papers to download by hand: see [papers/READING_LIST.md](../papers/READING_LIST.md).", ""]
    if report.transcripts:
        L += ["## Transcripts mined"] + [f"- {t['file']}: strategies {', '.join(t['strategies']) or 'none'}; "
                                        f"{t['papers_added']} papers added to seeds" for t in report.transcripts] + [""]
    if report.papers:
        L += ["## Papers", "", "| Paper | Read | WHY | Strategies |", "|---|---|---|---|"]
        for p in report.papers:
            strat = ", ".join(p["strategies"]) or f"none ({p.get('skipped_reason') or '-'})"
            L.append(f"| [{p['title']}]({'../' + p['summary']}) | {p['read_mode']} | {p['why']} | {strat} |")
        L.append("")
    if report.strategies:
        L += ["## Strategies", "", "| Strategy | From | Critic verdict | Scores (why/persist/simple/test/overfit) |",
              "|---|---|---|---|"]
        for s in report.strategies:
            sc = s.get("scores") or {}
            scores = "/".join(str(sc.get(k, "-")) for k in
                              ("why_strength", "persistence", "simplicity", "testability", "overfit_resistance"))
            L.append(f"| `{s['id']}` {s.get('name') or ''} | {s.get('origin')} | {s.get('verdict')} | {scores if sc else '-'} |")
        L.append("")
    if report.errors:
        L += ["## Errors"] + [f"- {e}" for e in report.errors] + [""]
    if usage is not None:
        L += ["## API usage", f"{usage.calls} calls · {usage.input_tokens:,} input tokens · {usage.output_tokens:,} output tokens", ""]
        L += [f"- {a}: {u['calls']} calls, {u['input_tokens']:,} in / {u['output_tokens']:,} out" for a, u in usage.by_agent.items()]
    repo.write_text(rel, "\n".join(L) + "\n")
    return rel


def run(repo: Repo, llm, max_papers: int | None = None, scout: bool = True,
        transcripts: bool = True, library: bool = True) -> tuple[RunReport, str]:
    report = RunReport()
    limit = max_papers or repo.settings().get("limits", {}).get("max_papers_per_run", 4)
    if transcripts:
        process_transcripts(repo, llm, report)
    for paper in build_queue(repo, llm, report, limit, scout):
        log.info("reading: %s", paper.get("title"))
        process_paper(repo, llm, paper, report)
    update_reading_list(repo, llm, report, search=library)
    rel = write_report(repo, report, getattr(llm, "usage", None))
    return report, rel
