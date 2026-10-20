"""Offline tests: a fake LLM stands in for Claude so the whole pipeline runs without an API key."""
import shutil
from pathlib import Path

import jsonschema
import pytest
import yaml

from conti_agents import agents, pipeline
from conti_agents.schemas import STRATEGY_SCHEMA
from conti_agents.store import Repo

ROOT = Path(__file__).resolve().parent.parent

SUMMARY = {
    "title": "Fake Paper on Month-End Flows", "authors": ["A. Author"], "year": 2025,
    "read_mode": "abstract_only", "paper_type": "academic",
    "one_line": "Index futures rise into month end.",
    "findings": [{"statement": "Last 3 days of the month earn most returns", "evidence": "ES 2000-2024"}],
    "why": {"pattern": "Institutional constraint / mandate", "mechanism": "Pension rebalancing buys at month end.",
            "what_would_kill_it": "Funds rebalancing earlier"},
    "tradable_edge": "Be long ES into month end.",
    "decay_risk": {"level": "medium", "reason": "Known since 2010s"},
    "data_fit": "Needs ES daily - available.",
    "referenced_papers_worth_reading": [{"title": "Cited Classic Paper", "year": 1999}],
}


def strategy(sid="month_end_long_es"):
    return {
        "id": sid, "name": "Month-end long ES", "status": "spec",
        "source": {"kind": "paper", "ref": "x"},
        "finding": "f", "why": "w",
        "market": {"instruments": ["ES"], "bar_size": "1 day", "session": "RTH America/New_York"},
        "direction": "long_only",
        "entry": {"long": "Buy close T-3", "short": None, "filters": []},
        "exit": {"stop_loss": None, "take_profit": None, "time_exit": "Sell close T+1", "other": []},
        "position_sizing": {"development": "1 contract", "live": "vol target"},
        "parameters": [{"name": "days_before", "default": 3, "test_range": "2-5", "source": "paper"}],
        "open_questions": [], "validation": {"in_sample_pct": 80},
    }


class FakeLLM:
    def __init__(self):
        self.calls = []
        self.usage = None

    def structured(self, *, agent, tool_name, **kw):
        self.calls.append(agent)
        if agent == "scout":
            return {"candidates": [{"title": "Scouted Paper", "url": "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=123",
                                    "why_promising": "flows"}]}
        if agent == "librarian":
            return {"papers": [{"title": "ES Last Half Hour Momentum", "year": 2024, "access": "ssrn_free_download",
                                "where_to_get_it": "SSRN abstract page, Download This Paper", "priority": 1,
                                "why_promising": "dealer hedging into the close", "instruments": ["ES"]}]}
        if agent == "resolver":
            return {"title": "resolved", "url": "https://ssrn.com/abstract=999"}
        if agent == "reader":
            return dict(SUMMARY)
        if agent == "strategist":
            return {"strategies": [strategy()], "skipped_reason": None}
        if agent == "critic":
            return {"scores": {"why_strength": 4, "persistence": 3, "simplicity": 5, "testability": 5,
                               "overfit_resistance": 4}, "verdict": "backtest", "reasons": ["clear WHY"],
                    "copies_the_paper": False}
        if agent == "transcript_miner":
            return {"title": "T2", "summary": "s", "strategies": [strategy("new_transcript_strategy")],
                    "papers_referenced": [{"title": "A Paper Conti Named", "year": 2020}],
                    "method_notes": ["Always check results by year."]}
        raise AssertionError(agent)


@pytest.fixture
def repo(tmp_path, monkeypatch):
    for d in ("config", "knowledge", "papers", "strategies"):
        shutil.copytree(ROOT / d, tmp_path / d, ignore=shutil.ignore_patterns("*.pdf", "index.json"))
    (tmp_path / "transcripts").mkdir()
    (tmp_path / "reports").mkdir()
    monkeypatch.setattr(agents, "download_pdf", lambda urls, max_mb: None)   # no network
    monkeypatch.setattr(agents, "arxiv_recent", lambda cats, n: [])
    return Repo(tmp_path)


def test_committed_strategies_match_schema():
    strategies = Repo(ROOT).strategies()
    assert len(strategies) >= 5
    for s in strategies:
        s.pop("_file")
        jsonschema.validate(s, STRATEGY_SCHEMA)


def test_full_run(repo):
    (repo.root / "transcripts" / "02_new.txt").write_text("Conti talks about a new strategy")
    llm = FakeLLM()
    report, rel = pipeline.run(repo, llm, max_papers=2, scout=True)

    assert report.errors == []
    assert report.transcripts and report.transcripts[0]["strategies"] == ["new_transcript_strategy"]
    assert (repo.root / "knowledge/method_notes.md").read_text().count("results by year") == 1
    assert any(s["title"] == "A Paper Conti Named" for s in repo.seeds())

    # two seeds read, each produced one strategy; ids made unique
    assert len(report.papers) == 2
    files = sorted(p.name for p in (repo.root / "strategies/candidates").glob("*.yaml"))
    assert files == ["month_end_long_es.yaml", "month_end_long_es_2.yaml"]
    st = yaml.safe_load((repo.root / "strategies/candidates/month_end_long_es.yaml").read_text())
    assert st["review"]["verdict"] == "backtest" and st["source"]["kind"] == "paper"
    jsonschema.validate({k: v for k, v in st.items()}, STRATEGY_SCHEMA)

    idx = repo.paper_index()
    assert sum(e["status"] == "summarized" for e in idx.values()) == 2
    assert (repo.root / rel).read_text().startswith("# Weekly research run")

    # second run: same transcript is not mined again, already-read seeds are not re-read
    report2, _ = pipeline.run(repo, FakeLLM(), max_papers=2, scout=False)
    assert report2.transcripts == []
    assert {p["title"] for p in report2.papers}.isdisjoint({p["title"] for p in report.papers}) or len(report2.papers) == 0


def test_failed_paper_is_retried_then_dropped(repo, monkeypatch):
    def boom(*a, **k):
        raise RuntimeError("fetch blocked")
    monkeypatch.setattr(agents, "read_paper", boom)
    for _ in range(4):
        pipeline.run(repo, FakeLLM(), max_papers=1, scout=False, transcripts=False)
    first = repo.paper_index()[sorted(repo.paper_index())[0]]
    attempts = [e["attempts"] for e in repo.paper_index().values()]
    assert max(attempts) <= pipeline.MAX_ATTEMPTS
    assert first["status"] == "failed"


def test_ssrn_pdf_urls():
    urls = agents.pdf_candidates({"url": "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2659431"})
    assert urls == ["https://papers.ssrn.com/sol3/Delivery.cfm?abstractid=2659431&mirid=1"]
    assert agents.pdf_candidates({"url": "https://arxiv.org/abs/2401.00001"}) == ["https://arxiv.org/pdf/2401.00001"]
    assert agents.ssrn_id("https://ssrn.com/abstract=3175538") == "3175538"


def test_summary_markdown_renders():
    md = agents.summary_markdown(SUMMARY)
    assert "## The WHY" in md and "Pension rebalancing" in md


def test_reading_list(repo, monkeypatch):
    # reader can only see abstracts -> those papers land in the "please download" section
    def abstract_only(repo_, llm, paper, cache_path=None):
        return dict(SUMMARY, title=paper["title"], read_mode="abstract_only")
    monkeypatch.setattr(agents, "read_paper", abstract_only)
    report, _ = pipeline.run(repo, FakeLLM(), max_papers=1, scout=False, transcripts=False)
    rl = (repo.root / "papers/READING_LIST.md").read_text()
    assert report.librarian == 1
    assert "ES Last Half Hour Momentum" in rl and "papers/inbox/es_last_half_hour_momentum.pdf" in rl
    first_read = report.papers[0]["title"]
    assert first_read in rl.split("## 2.")[0]          # needs a manual PDF

    # Pablo drops the PDF under the suggested name -> it is re-queued first, as a full read
    slug = next(k for k, v in repo.paper_index().items() if v.get("title") == first_read)
    (repo.root / "papers/inbox").mkdir(exist_ok=True)
    (repo.root / f"papers/inbox/{slug}.pdf").write_bytes(b"%PDF-1.4 fake")
    monkeypatch.setattr(agents, "read_paper", lambda r, l, p, cache_path=None: dict(SUMMARY, title=p["title"], read_mode="full_pdf"))
    report2, _ = pipeline.run(repo, FakeLLM(), max_papers=1, scout=False, transcripts=False, library=False)
    assert report2.papers[0]["title"] == first_read and report2.papers[0]["read_mode"] == "full_pdf"
    assert first_read not in (repo.root / "papers/READING_LIST.md").read_text().split("## 2.")[0]
