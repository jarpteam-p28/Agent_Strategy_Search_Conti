"""Command line entry point.

    python -m conti_agents run                 # full weekly run
    python -m conti_agents run --max-papers 1  # cheaper test run
    python -m conti_agents run --no-scout      # only seeds + inbox PDFs
    python -m conti_agents transcripts         # only mine new transcripts
    python -m conti_agents validate            # check every strategy YAML against the schema
"""
from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

from .store import Repo


def validate(repo: Repo) -> int:
    import jsonschema
    from .schemas import STRATEGY_SCHEMA
    bad = 0
    for s in repo.strategies():
        f = s.pop("_file")
        try:
            jsonschema.validate(s, STRATEGY_SCHEMA)
            print(f"ok   {f}")
        except jsonschema.ValidationError as e:
            bad += 1
            print(f"FAIL {f}: {e.message} at {'/'.join(map(str, e.absolute_path))}")
    return 1 if bad else 0


def main(argv=None) -> int:
    p = argparse.ArgumentParser(prog="conti_agents")
    p.add_argument("--root", default=str(Path(__file__).resolve().parent.parent))
    p.add_argument("-v", "--verbose", action="store_true")
    sub = p.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run")
    r.add_argument("--max-papers", type=int)
    r.add_argument("--no-scout", action="store_true")
    r.add_argument("--no-transcripts", action="store_true")
    sub.add_parser("transcripts")
    sub.add_parser("validate")
    a = p.parse_args(argv)
    logging.basicConfig(level=logging.DEBUG if a.verbose else logging.INFO, format="%(levelname)s %(name)s: %(message)s")
    repo = Repo(a.root)

    if a.cmd == "validate":
        return validate(repo)

    from .llm import ClaudeLLM
    from . import pipeline
    llm = ClaudeLLM()
    if a.cmd == "transcripts":
        report = pipeline.RunReport()
        pipeline.process_transcripts(repo, llm, report)
        print(report)
        return 0
    report, rel = pipeline.run(repo, llm, max_papers=a.max_papers, scout=not a.no_scout,
                               transcripts=not a.no_transcripts)
    print(f"report: {rel}")
    print(repo.read_text(rel))
    return 0


if __name__ == "__main__":
    sys.exit(main())
