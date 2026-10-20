"""JSON schemas for everything the agents produce.

The same schemas are used (a) as the input_schema of the "submit" tool each agent must call,
so Claude returns structured output, and (b) to validate files committed to the repo.
"""

STR = {"type": "string"}
STR_LIST = {"type": "array", "items": {"type": "string"}}

PAPER_REF = {
    "type": "object",
    "properties": {
        "title": STR,
        "authors": STR_LIST,
        "year": {"type": ["integer", "null"]},
        "url": {"type": ["string", "null"], "description": "SSRN abstract page, arXiv abs page, DOI or journal URL"},
        "pdf_url": {"type": ["string", "null"]},
        "venue": {"type": ["string", "null"]},
        "note": {"type": ["string", "null"], "description": "Why this paper matters / how it was referenced"},
    },
    "required": ["title"],
}

# ---------------------------------------------------------------------------------------------
# Scout: candidate papers to read
# ---------------------------------------------------------------------------------------------
CANDIDATES_SCHEMA = {
    "type": "object",
    "properties": {
        "candidates": {
            "type": "array",
            "items": {
                **PAPER_REF,
                "properties": {
                    **PAPER_REF["properties"],
                    "topic": STR,
                    "why_promising": {"type": "string", "description": "The likely finding AND a plausible structural WHY, in one or two sentences"},
                },
                "required": ["title", "url", "why_promising"],
            },
        }
    },
    "required": ["candidates"],
}

# ---------------------------------------------------------------------------------------------
# Librarian: reading list for Pablo to download by hand
# ---------------------------------------------------------------------------------------------
READING_LIST_SCHEMA = {
    "type": "object",
    "properties": {
        "papers": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    **PAPER_REF["properties"],
                    "instruments": {"type": "array", "items": STR, "description": "ES, NQ, S&P 500 index, etc."},
                    "access": {"type": "string", "enum": ["open_pdf", "ssrn_free_download", "paywalled", "unknown"]},
                    "where_to_get_it": {"type": "string", "description": "Exact page to download from and what to click"},
                    "why_promising": {"type": "string", "description": "Likely finding + structural WHY"},
                    "what_it_should_contain": {"type": "string", "description": "Tables/rules/data we expect: e.g. intraday return by half hour on ES 2000-2023"},
                    "testable_on_our_data": {"type": "string", "enum": ["yes", "partial", "no"]},
                    "priority": {"type": "integer", "minimum": 1, "maximum": 3, "description": "1 = read first"},
                },
                "required": ["title", "where_to_get_it", "why_promising", "access", "priority"],
            },
        }
    },
    "required": ["papers"],
}

# ---------------------------------------------------------------------------------------------
# Reader: paper summary (finding + WHY + tradable edge)
# ---------------------------------------------------------------------------------------------
PAPER_SUMMARY_SCHEMA = {
    "type": "object",
    "properties": {
        "title": STR,
        "authors": STR_LIST,
        "year": {"type": ["integer", "null"]},
        "source_url": {"type": ["string", "null"]},
        "read_mode": {"type": "string", "enum": ["full_pdf", "web_fetch", "abstract_only"],
                      "description": "How much of the paper you actually read"},
        "paper_type": {"type": "string", "enum": ["academic", "industry", "review"]},
        "one_line": {"type": "string", "description": "The finding in one plain sentence"},
        "findings": {
            "type": "array",
            "items": {"type": "object",
                      "properties": {"statement": STR, "evidence": STR},
                      "required": ["statement"]},
        },
        "why": {
            "type": "object",
            "properties": {
                "pattern": {"type": "string", "description": "Which WHY pattern from the playbook (or 'new: ...')"},
                "mechanism": {"type": "string", "description": "The economic reason the finding exists"},
                "who_is_forced": {"type": "string", "description": "Which participants are constrained or predictable, and how"},
                "why_it_persists": STR,
                "what_would_kill_it": STR,
                "authors_explanation_vs_ours": {"type": "string", "description": "Where the paper's own explanation differs from or is weaker than this WHY"},
            },
            "required": ["pattern", "mechanism", "what_would_kill_it"],
        },
        "setting": {
            "type": "object",
            "properties": {
                "markets": STR_LIST,
                "instruments": STR_LIST,
                "sample_period": STR,
                "data_frequency": STR,
                "holding_period": STR,
            },
        },
        "reported_results": {
            "type": "object",
            "properties": {
                "headline": STR,
                "key_stats": STR_LIST,
                "costs_included": STR,
            },
        },
        "tradable_edge": {"type": "string", "description": "OUR framing of the edge in one paragraph — not the paper's rules copied"},
        "angles": {"type": "array", "items": STR, "description": "Ways to adapt it: other instruments, universes, sessions, one side only, combinations"},
        "decay_risk": {
            "type": "object",
            "properties": {"level": {"type": "string", "enum": ["low", "medium", "high"]}, "reason": STR},
            "required": ["level", "reason"],
        },
        "data_fit": {"type": "string", "description": "Can it be tested with the data inventory? What's missing?"},
        "caveats": STR_LIST,
        "referenced_papers_worth_reading": {"type": "array", "items": PAPER_REF},
    },
    "required": ["title", "read_mode", "one_line", "findings", "why", "tradable_edge", "decay_risk", "data_fit"],
}

# ---------------------------------------------------------------------------------------------
# Strategy spec (the three boxes + validation plan)
# ---------------------------------------------------------------------------------------------
PARAMETER = {
    "type": "object",
    "properties": {
        "name": STR,
        "default": {"type": ["string", "number", "boolean"]},
        "test_range": {"type": ["string", "null"], "description": "Values to try IN-SAMPLE only"},
        "source": {"type": ["string", "null"], "description": "paper / transcript / assumption"},
    },
    "required": ["name", "default"],
}

STRATEGY_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "string", "pattern": "^[a-z0-9][a-z0-9_]*$"},
        "name": STR,
        "status": {"type": "string", "enum": ["idea", "spec", "coded", "backtested", "validated", "live", "parked", "rejected"]},
        "source": {
            "type": "object",
            "properties": {
                "kind": {"type": "string", "enum": ["transcript", "paper", "agent_idea"]},
                "ref": STR,
                "papers": {"type": "array", "items": PAPER_REF},
            },
            "required": ["kind", "ref"],
        },
        "finding": STR,
        "why": STR,
        "what_would_kill_it": STR,
        "market": {
            "type": "object",
            "properties": {
                "instruments": STR_LIST,
                "bar_size": STR,
                "session": {"type": "string", "description": "Session and timezone, e.g. 'RTH 09:30-16:00 America/New_York'"},
                "universe": {"type": ["string", "null"]},
            },
            "required": ["instruments", "bar_size", "session"],
        },
        "direction": {"type": "string", "enum": ["long_only", "short_only", "long_short"]},
        "entry": {"type": "object", "properties": {"long": {"type": ["string", "null"]}, "short": {"type": ["string", "null"]}, "filters": STR_LIST}},
        "exit": {
            "type": "object",
            "properties": {
                "stop_loss": {"type": ["string", "null"]},
                "take_profit": {"type": ["string", "null"]},
                "time_exit": {"type": ["string", "null"]},
                "other": STR_LIST,
            },
        },
        "position_sizing": {
            "type": "object",
            "properties": {"development": STR, "live": STR},
            "required": ["development", "live"],
        },
        "parameters": {"type": "array", "items": PARAMETER},
        "variants": {"type": "array", "items": STR},
        "expectations": {"type": "array", "items": STR, "description": "What the source says we should see, to confirm or refute in backtest"},
        "data_requirements": STR_LIST,
        "data_available": {"type": "string", "enum": ["yes", "partial", "no", "unknown"]},
        "open_questions": STR_LIST,
        "validation": {
            "type": "object",
            "properties": {
                "in_sample_pct": {"type": "number"},
                "monte_carlo_reshuffle_runs": {"type": "integer"},
                "monte_carlo_bootstrap_runs": {"type": "integer"},
                "kill_switch": STR,
                "extra_checks": STR_LIST,
            },
            "required": ["in_sample_pct"],
        },
        "related_strategies": STR_LIST,
        "notes": STR_LIST,
        "review": {"type": "object"},
    },
    "required": ["id", "name", "status", "source", "finding", "why", "market", "direction",
                 "entry", "exit", "position_sizing", "parameters", "open_questions", "validation"],
}

STRATEGIES_OUTPUT_SCHEMA = {
    "type": "object",
    "properties": {
        "strategies": {"type": "array", "items": STRATEGY_SCHEMA, "maxItems": 3},
        "skipped_reason": {"type": ["string", "null"], "description": "If no strategy: why the paper gives no tradable edge for us"},
    },
    "required": ["strategies"],
}

# ---------------------------------------------------------------------------------------------
# Critic review
# ---------------------------------------------------------------------------------------------
SCORE = {"type": "integer", "minimum": 1, "maximum": 5}
REVIEW_SCHEMA = {
    "type": "object",
    "properties": {
        "scores": {
            "type": "object",
            "properties": {
                "why_strength": SCORE,
                "persistence": SCORE,
                "simplicity": SCORE,
                "testability": SCORE,
                "overfit_resistance": SCORE,
            },
            "required": ["why_strength", "persistence", "simplicity", "testability", "overfit_resistance"],
        },
        "verdict": {"type": "string", "enum": ["backtest", "refine", "park", "reject"]},
        "reasons": STR_LIST,
        "required_changes": STR_LIST,
        "copies_the_paper": {"type": "boolean", "description": "True if the rules just replicate the paper instead of framing around the WHY"},
    },
    "required": ["scores", "verdict", "reasons", "copies_the_paper"],
}

# ---------------------------------------------------------------------------------------------
# Transcript miner
# ---------------------------------------------------------------------------------------------
TRANSCRIPT_EXTRACT_SCHEMA = {
    "type": "object",
    "properties": {
        "title": STR,
        "summary": STR,
        "strategies": {"type": "array", "items": STRATEGY_SCHEMA},
        "papers_referenced": {"type": "array", "items": PAPER_REF},
        "method_notes": {"type": "array", "items": STR,
                         "description": "New or sharper rules of the method (research, WHY, rules, validation, sizing, portfolio) not already in the playbook"},
    },
    "required": ["title", "summary", "strategies", "papers_referenced", "method_notes"],
}
