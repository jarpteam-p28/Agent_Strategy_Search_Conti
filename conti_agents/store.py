"""File-based storage. Everything the agents learn lives in the repo as plain files."""
from __future__ import annotations

import datetime as dt
import json
import re
from pathlib import Path
from typing import Any

import yaml


def slugify(text: str, max_len: int = 60) -> str:
    s = re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")
    return s[:max_len].rstrip("_") or "untitled"


def today() -> str:
    return dt.date.today().isoformat()


class _Dumper(yaml.SafeDumper):
    pass


def _str_presenter(dumper, data):
    style = ">" if len(data) > 100 and "\n" not in data else ("|" if "\n" in data else None)
    return dumper.represent_scalar("tag:yaml.org,2002:str", data, style=style)


_Dumper.add_representer(str, _str_presenter)


def dump_yaml(obj: Any) -> str:
    return yaml.dump(obj, Dumper=_Dumper, sort_keys=False, allow_unicode=True, width=100)


class Repo:
    def __init__(self, root: str | Path):
        self.root = Path(root).resolve()

    # -- generic ---------------------------------------------------------------------------
    def path(self, rel: str) -> Path:
        return self.root / rel

    def read_text(self, rel: str, default: str = "") -> str:
        p = self.path(rel)
        return p.read_text(encoding="utf-8") if p.exists() else default

    def write_text(self, rel: str, text: str) -> Path:
        p = self.path(rel)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")
        return p

    def load_yaml(self, rel: str, default: Any = None) -> Any:
        text = self.read_text(rel)
        return yaml.safe_load(text) if text.strip() else default

    def save_yaml(self, rel: str, obj: Any) -> Path:
        return self.write_text(rel, dump_yaml(obj))

    def load_json(self, rel: str, default: Any = None) -> Any:
        text = self.read_text(rel)
        return json.loads(text) if text.strip() else default

    def save_json(self, rel: str, obj: Any) -> Path:
        return self.write_text(rel, json.dumps(obj, indent=2, ensure_ascii=False) + "\n")

    # -- config & knowledge ----------------------------------------------------------------
    def settings(self) -> dict:
        return self.load_yaml("config/settings.yaml", {})

    def method_text(self) -> str:
        core = self.read_text("knowledge/conti_method.md")
        notes = self.read_text("knowledge/method_notes.md")
        return core + ("\n\n# Additional method notes from later transcripts\n\n" + notes if notes.strip() else "")

    def data_inventory_text(self) -> str:
        return self.read_text("config/data_inventory.yaml", "(no data inventory file)")

    # -- papers ----------------------------------------------------------------------------
    def paper_index(self) -> dict:
        return self.load_json("papers/index.json", {})

    def save_paper_index(self, idx: dict) -> None:
        self.save_json("papers/index.json", dict(sorted(idx.items())))

    def seeds(self) -> list[dict]:
        return self.load_yaml("papers/seeds.yaml", []) or []

    def add_seeds(self, papers: list[dict]) -> int:
        seeds = self.seeds()
        known = {slugify(s["title"]) for s in seeds}
        added = 0
        for p in papers:
            if p.get("title") and slugify(p["title"]) not in known:
                seeds.append({k: v for k, v in p.items() if v not in (None, "", [])})
                known.add(slugify(p["title"]))
                added += 1
        if added:
            self.save_yaml("papers/seeds.yaml", seeds)
        return added

    def inbox_pdfs(self) -> list[Path]:
        return sorted(self.path("papers/inbox").glob("*.pdf"))

    # -- strategies ------------------------------------------------------------------------
    def strategy_files(self) -> list[Path]:
        return sorted(self.path("strategies").rglob("*.yaml"))

    def strategies(self) -> list[dict]:
        out = []
        for f in self.strategy_files():
            data = yaml.safe_load(f.read_text(encoding="utf-8"))
            if isinstance(data, dict):
                data["_file"] = str(f.relative_to(self.root))
                out.append(data)
        return out

    def strategy_brief(self) -> str:
        lines = [f"- {s['id']}: {s.get('name', '')} | finding: {' '.join(str(s.get('finding', '')).split())[:200]}"
                 for s in self.strategies()]
        return "\n".join(lines) or "(none yet)"

    def unique_strategy_id(self, wanted: str) -> str:
        existing = {s["id"] for s in self.strategies()}
        sid, n = slugify(wanted, 50), 2
        base = sid
        while sid in existing:
            sid, n = f"{base}_{n}", n + 1
        return sid

    def save_strategy(self, strategy: dict, folder: str = "strategies/candidates", prefix: str = "") -> Path:
        clean = {k: v for k, v in strategy.items() if not k.startswith("_")}
        return self.save_yaml(f"{folder}/{prefix}{clean['id']}.yaml", clean)

    # -- transcripts -----------------------------------------------------------------------
    def transcript_index(self) -> dict:
        return self.load_json("transcripts/index.json", {})

    def save_transcript_index(self, idx: dict) -> None:
        self.save_json("transcripts/index.json", idx)

    def transcript_files(self) -> list[Path]:
        d = self.path("transcripts")
        return sorted([*d.glob("*.txt"), *d.glob("*.md")]) if d.exists() else []
