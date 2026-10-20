# Hand-off to the backtest project (Backtest_Conti_Research)

This repo only researches and writes specs. These sheets are the bridge: each one is a **proposed rule set**
written to match `BACKTEST_VALIDATION_CHECKLIST.md` (step A1 "lock the rules in writing and get the user's OK").
Nothing here is locked until Pablo approves it in the backtest chat.

| Sheet | Strategy | Instrument | His reported period |
|---|---|---|---|
| `VAULT_BREAK_RULES_PROPOSED.md` | Vault Break (30-min noise breakout, long only) | NQ | 2022-01 → 2026-09 |
| `DRIFT_VWAP_PULLBACK_RULES_PROPOSED.md` | Drift VWAP Pullback (5-min, 15-min VWAP drift, long/short) | NQ | 2021-01 → 2026-07 |
| `OVERNIGHT_BIAS_ORB_RULES_PROPOSED.md` | Overnight Bias ORB (15-min, long/short) | NQ | 2006 → 2026-08 |
| `EVALUATION_WINDOWS.md` | Conti window + full history, each split 80/20 in time (reporting views, not variants) | ES | — |
| `ES_ADAPTATION.md` | **How to run these NQ strategies on ES** (Pablo's choice: ES data is complete 2013-2026) | ES | — |
| `reference/vwap_mtf.py` | Python 15-min VWAP on 5-min + drift state (tested, no look-ahead) | — | — |

Instrument: **ES** (see `ES_ADAPTATION.md`). Data: `Backtest Github/data/clean_ES_master.parquet`, ES 1-minute 2013-12 → 2026-09.
NQ (`clean_NQ/continuous_1min.parquet`, Jul 2021 → Sep 2026, five contracts missing) only as a second-instrument check. Confirm its timestamp convention (A4) and roll handling (Part B)
before anything else.

## How to use
1. Open the backtest chat (the one working in `Backtest_Conti_Research`).
2. Paste `PROMPT_FOR_BACKTEST_CHAT.md`.
3. Answer the "decide before locking" questions in the sheet, approve, and let it run the checklist.
