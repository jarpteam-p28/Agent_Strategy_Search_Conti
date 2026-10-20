"""The five agents: scout, resolver, reader, strategist, critic, transcript miner."""
from __future__ import annotations

import base64
import io
import json
import logging
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlparse

import httpx

from . import prompts
from .llm import web_fetch_tool, web_search_tool
from .schemas import (CANDIDATES_SCHEMA, PAPER_REF, PAPER_SUMMARY_SCHEMA, READING_LIST_SCHEMA,
                      REVIEW_SCHEMA, STRATEGIES_OUTPUT_SCHEMA, TRANSCRIPT_EXTRACT_SCHEMA)
from .store import Repo, dump_yaml

log = logging.getLogger(__name__)
UA = "conti-strategy-research/0.1 (academic research pipeline)"


def fill(template: str, **values: str) -> str:
    for k, v in values.items():
        template = template.replace("{" + k + "}", v)
    return template


def _model(repo: Repo, agent: str) -> str:
    return repo.settings().get("models", {}).get(agent, "claude-sonnet-5-5")


def _limits(repo: Repo) -> dict:
    return repo.settings().get("limits", {})


# =============================================================================================
# 1. Scout - find new candidate papers
# =============================================================================================
def arxiv_recent(categories: list[str], count: int) -> list[dict]:
    """Latest submissions in arXiv quantitative-finance categories (free public API)."""
    query = " OR ".join(f"cat:{c}" for c in categories)
    try:
        r = httpx.get("https://export.arxiv.org/api/query",
                      params={"search_query": query, "sortBy": "submittedDate", "sortOrder": "descending",
                              "max_results": count},
                      headers={"User-Agent": UA}, timeout=30)
        r.raise_for_status()
    except httpx.HTTPError as e:
        log.warning("arXiv listing failed: %s", e)
        return []
    ns = {"a": "http://www.w3.org/2005/Atom"}
    out = []
    for entry in ET.fromstring(r.text).findall("a:entry", ns):
        abs_url = entry.findtext("a:id", default="", namespaces=ns)
        out.append({
            "title": " ".join(entry.findtext("a:title", default="", namespaces=ns).split()),
            "authors": [a.findtext("a:name", default="", namespaces=ns) for a in entry.findall("a:author", ns)],
            "year": int(entry.findtext("a:published", default="0000", namespaces=ns)[:4] or 0) or None,
            "url": abs_url,
            "pdf_url": abs_url.replace("/abs/", "/pdf/"),
            "abstract": " ".join(entry.findtext("a:summary", default="", namespaces=ns).split())[:1200],
        })
    return out


def scout(repo: Repo, llm, known_titles: list[str], n: int) -> list[dict]:
    s, lim = repo.settings(), _limits(repo)
    topics = repo.read_text("config/search_topics.yaml")
    arxiv = arxiv_recent(s.get("sources", {}).get("arxiv_categories", []),
                         s.get("sources", {}).get("arxiv_recent_count", 25))
    arxiv_block = "\n".join(f"- {p['title']} ({p['url']}): {p['abstract'][:400]}" for p in arxiv) or "(none)"
    content = (
        f"Find up to {n} NEW papers to read this week.\n\n"
        f"Search guidance:\n<search_topics>\n{topics}\n</search_topics>\n\n"
        f"Recent arXiv q-fin submissions you may also pick from (only if they fit):\n<arxiv>\n{arxiv_block}\n</arxiv>\n\n"
        f"Already known - skip these:\n<known>\n" + "\n".join(f"- {t}" for t in known_titles) + "\n</known>"
    )
    out = llm.structured(
        agent="scout", model=_model(repo, "scout"),
        system=fill(prompts.SCOUT, method=repo.method_text()),
        content=content, tool_name="submit_candidates", schema=CANDIDATES_SCHEMA,
        server_tools=[web_search_tool(lim.get("scout_max_searches", 12),
                                      s.get("sources", {}).get("web_search_domains"))],
    )
    return out.get("candidates", [])[:n]


# =============================================================================================
# 1b. Librarian - reading list of ES/NQ research for Pablo to download by hand
# =============================================================================================
def librarian(repo: Repo, llm, known_titles: list[str], n: int) -> list[dict]:
    lim = repo.settings().get("limits", {})
    focus = repo.load_yaml("config/search_topics.yaml", {}).get("librarian_focus", [])
    content = (f"Find up to {n} papers for the reading list.\n\nFocus areas:\n"
               + "\n".join(f"- {f}" for f in focus)
               + "\n\nAlready known - skip these:\n" + "\n".join(f"- {t}" for t in known_titles))
    out = llm.structured(
        agent="librarian", model=_model(repo, "librarian"),
        system=fill(prompts.LIBRARIAN, method=repo.method_text(), data_inventory=repo.data_inventory_text()),
        content=content, tool_name="submit_reading_list", schema=READING_LIST_SCHEMA,
        server_tools=[web_search_tool(lim.get("librarian_max_searches", 15))],
    )
    return out.get("papers", [])[:n]


# =============================================================================================
# 2. Resolver - find a URL for a paper we only know by title
# =============================================================================================
def resolve(repo: Repo, llm, paper: dict) -> dict:
    content = f"Locate this paper:\n{json.dumps(paper, indent=2)}"
    out = llm.structured(
        agent="resolver", model=_model(repo, "scout"),
        system=fill(prompts.RESOLVE, method=repo.method_text()),
        content=content, tool_name="submit_paper", schema=PAPER_REF,
        server_tools=[web_search_tool(5)], max_tokens=4000,
    )
    return {**paper, **{k: v for k, v in out.items() if v}}


# =============================================================================================
# 3. Reader - read the full paper and extract finding + WHY + edge
# =============================================================================================
def ssrn_id(url: str | None) -> str | None:
    if not url:
        return None
    m = re.search(r"abstract(?:_?id)?=(\d+)", url) or re.search(r"ssrn\.com/abstract=(\d+)", url)
    return m.group(1) if m else None


def pdf_candidates(paper: dict) -> list[str]:
    urls = [paper.get("pdf_url")]
    url = paper.get("url") or ""
    if "arxiv.org/abs/" in url:
        urls.append(url.replace("/abs/", "/pdf/"))
    sid = ssrn_id(url) or ssrn_id(paper.get("pdf_url"))
    if sid:
        urls.append(f"https://papers.ssrn.com/sol3/Delivery.cfm?abstractid={sid}&mirid=1")
    if url.lower().endswith(".pdf"):
        urls.append(url)
    return [u for i, u in enumerate(urls) if u and u not in urls[:i]]


def download_pdf(urls: list[str], max_mb: float) -> bytes | None:
    for u in urls:
        try:
            r = httpx.get(u, headers={"User-Agent": UA}, follow_redirects=True, timeout=60)
            if r.status_code == 200 and r.content[:5] == b"%PDF-" and len(r.content) <= max_mb * 1e6:
                return r.content
            log.info("no PDF from %s (status %s, %d bytes)", u, r.status_code, len(r.content))
        except httpx.HTTPError as e:
            log.info("download failed %s: %s", u, e)
    return None


def trim_pdf(data: bytes, max_pages: int) -> tuple[bytes, int, bool]:
    from pypdf import PdfReader, PdfWriter
    reader = PdfReader(io.BytesIO(data))
    pages = len(reader.pages)
    if pages <= max_pages:
        return data, pages, False
    w = PdfWriter()
    for p in reader.pages[:max_pages]:
        w.add_page(p)
    buf = io.BytesIO()
    w.write(buf)
    return buf.getvalue(), pages, True


def read_paper(repo: Repo, llm, paper: dict, cache_path: Path | None = None) -> dict:
    s, lim = repo.settings(), _limits(repo)
    system = fill(prompts.READER, method=repo.method_text(), data_inventory=repo.data_inventory_text())
    meta = json.dumps({k: paper.get(k) for k in ("title", "authors", "year", "url", "pdf_url")}, indent=2)

    data = None
    if paper.get("local_pdf"):
        local = Path(paper["local_pdf"])
        data = (local if local.is_absolute() else repo.path(paper["local_pdf"])).read_bytes()
    elif cache_path and cache_path.exists():
        data = cache_path.read_bytes()
    else:
        data = download_pdf(pdf_candidates(paper), lim.get("max_pdf_mb", 30))
        if data and cache_path:
            cache_path.parent.mkdir(parents=True, exist_ok=True)
            cache_path.write_bytes(data)

    if data:
        data, pages, trimmed = trim_pdf(data, lim.get("max_pdf_pages", 95))
        note = f"\n(Only the first {lim.get('max_pdf_pages', 95)} of {pages} pages are attached.)" if trimmed else ""
        content = [
            {"type": "document", "source": {"type": "base64", "media_type": "application/pdf",
                                            "data": base64.standard_b64encode(data).decode()}},
            {"type": "text", "text": f"Paper metadata:\n{meta}{note}\n\nRead the full paper and submit the summary."},
        ]
        out = llm.structured(agent="reader", model=_model(repo, "reader"), system=system, content=content,
                             tool_name="submit_summary", schema=PAPER_SUMMARY_SCHEMA)
        out["read_mode"] = "full_pdf"
        if trimmed:
            out.setdefault("caveats", []).append(f"Only first {lim.get('max_pdf_pages', 95)} of {pages} pages read.")
    else:
        # Couldn't download it ourselves: let Claude fetch the page/PDF server-side.
        domains = set(s.get("sources", {}).get("web_search_domains", []))
        for u in pdf_candidates(paper) + [paper.get("url")]:
            if u:
                host = urlparse(u).hostname or ""
                domains.add(".".join(host.split(".")[-2:]))
        content = (f"Paper metadata:\n{meta}\n\nOur direct PDF download failed. Use web_fetch on the "
                   f"pdf_url / SSRN or arXiv page to read as much of the paper as you can (the full PDF if "
                   f"possible), then submit the summary. Be honest in read_mode.")
        out = llm.structured(agent="reader", model=_model(repo, "reader"), system=system, content=content,
                             tool_name="submit_summary", schema=PAPER_SUMMARY_SCHEMA,
                             server_tools=[web_fetch_tool(lim.get("reader_max_fetches", 4), sorted(domains))])
    out.setdefault("source_url", paper.get("url"))
    return out


def summary_markdown(sm: dict) -> str:
    why = sm.get("why", {})
    lines = [f"# {sm.get('title')}", "",
             f"**Authors:** {', '.join(sm.get('authors') or [])}  ",
             f"**Year:** {sm.get('year')}  **Type:** {sm.get('paper_type', '?')}  **Read:** {sm.get('read_mode')}  ",
             f"**Source:** {sm.get('source_url')}", "",
             f"> {sm.get('one_line')}", "", "## Findings"]
    lines += [f"- {f.get('statement')}" + (f" — *{f['evidence']}*" if f.get("evidence") else "") for f in sm.get("findings", [])]
    lines += ["", "## The WHY", f"**Pattern:** {why.get('pattern')}", "", why.get("mechanism", ""), ""]
    for k, label in [("who_is_forced", "Who is forced / predictable"), ("why_it_persists", "Why it persists"),
                     ("what_would_kill_it", "What would kill it"), ("authors_explanation_vs_ours", "Paper's view vs ours")]:
        if why.get(k):
            lines.append(f"- **{label}:** {why[k]}")
    st, rr = sm.get("setting", {}), sm.get("reported_results", {})
    lines += ["", "## Setting", f"- Markets: {', '.join(st.get('markets', []))}",
              f"- Instruments: {', '.join(st.get('instruments', []))}",
              f"- Period: {st.get('sample_period', '')}  Frequency: {st.get('data_frequency', '')}  Holding: {st.get('holding_period', '')}",
              "", "## Reported results", rr.get("headline", "")]
    lines += [f"- {x}" for x in rr.get("key_stats", [])]
    if rr.get("costs_included"):
        lines.append(f"- Costs: {rr['costs_included']}")
    lines += ["", "## Tradable edge (our framing)", sm.get("tradable_edge", ""), "", "## Angles to test"]
    lines += [f"- {a}" for a in sm.get("angles", [])]
    dr = sm.get("decay_risk", {})
    lines += ["", f"## Decay risk: {dr.get('level')}", dr.get("reason", ""), "", "## Data fit", sm.get("data_fit", "")]
    if sm.get("caveats"):
        lines += ["", "## Caveats"] + [f"- {c}" for c in sm["caveats"]]
    if sm.get("referenced_papers_worth_reading"):
        lines += ["", "## Cited papers worth reading"]
        lines += [f"- {p.get('title')} ({p.get('year')})" for p in sm["referenced_papers_worth_reading"]]
    return "\n".join(lines) + "\n"


# =============================================================================================
# 4. Strategist - finding + WHY -> strategy specs
# =============================================================================================
def strategize(repo: Repo, llm, summary: dict, summary_ref: str) -> dict:
    system = fill(prompts.STRATEGIST, method=repo.method_text(),
                  data_inventory=repo.data_inventory_text(), existing=repo.strategy_brief())
    content = f"Paper summary ({summary_ref}):\n{json.dumps(summary, indent=2, ensure_ascii=False)}"
    out = llm.structured(agent="strategist", model=_model(repo, "strategist"), system=system,
                         content=content, tool_name="submit_strategies", schema=STRATEGIES_OUTPUT_SCHEMA)
    for st in out.get("strategies", []):
        st["id"] = repo.unique_strategy_id(st.get("id") or st.get("name", "strategy"))
        st["source"] = {**st.get("source", {}), "kind": "paper", "ref": summary_ref}
        if st.get("status") not in ("spec", "idea"):
            st["status"] = "spec"
    return out


# =============================================================================================
# 5. Critic - independent review
# =============================================================================================
def critique(repo: Repo, llm, strategy: dict, summary: dict | None) -> dict:
    system = fill(prompts.CRITIC, method=repo.method_text(), data_inventory=repo.data_inventory_text())
    content = f"Strategy spec:\n{dump_yaml(strategy)}"
    if summary:
        content += f"\n\nSource paper summary:\n{json.dumps(summary, indent=2, ensure_ascii=False)}"
    return llm.structured(agent="critic", model=_model(repo, "critic"), system=system, content=content,
                          tool_name="submit_review", schema=REVIEW_SCHEMA, max_tokens=4000)


# =============================================================================================
# 6. Transcript miner - new Conti transcripts -> strategies, papers, method notes
# =============================================================================================
def mine_transcript(repo: Repo, llm, transcript: Path, max_images: int = 20) -> dict:
    content: list[dict] = []
    shots = repo.path(f"transcripts/screenshots/{transcript.stem}")
    for img in sorted([*shots.glob("*.png"), *shots.glob("*.jpg"), *shots.glob("*.jpeg")])[:max_images] if shots.exists() else []:
        media = "image/png" if img.suffix == ".png" else "image/jpeg"
        content.append({"type": "image", "source": {"type": "base64", "media_type": media,
                                                    "data": base64.standard_b64encode(img.read_bytes()).decode()}})
    content.append({"type": "text", "text": f"Transcript ({transcript.name}):\n<transcript>\n"
                                            f"{transcript.read_text(encoding='utf-8')}\n</transcript>"})
    system = fill(prompts.TRANSCRIPT_MINER, method=repo.method_text(), existing=repo.strategy_brief())
    out = llm.structured(agent="transcript_miner", model=_model(repo, "transcript_miner"), system=system,
                         content=content, tool_name="submit_extraction", schema=TRANSCRIPT_EXTRACT_SCHEMA,
                         max_tokens=32000)
    for st in out.get("strategies", []):
        st["id"] = repo.unique_strategy_id(st.get("id") or st.get("name", "strategy"))
        st["source"] = {**st.get("source", {}), "kind": "transcript", "ref": f"transcripts/{transcript.name}"}
    return out
