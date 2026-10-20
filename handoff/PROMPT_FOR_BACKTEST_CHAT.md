Paste this into the backtest chat:

---
New strategies to test in Backtest_Conti_Research, from Matteo Conti's videos. The proposed rules are in
`/Volumes/Lexar Armor 700 Media/Backtest_Conti_Research/incoming_specs/`.

Source of truth = these written specs (not TradingView, not Joshua's PD-Array work, which stays read-only reference).

Instrument: **ES**, not NQ - my NQ tick data is missing five contracts. Conti built these on NQ, so read
ES_ADAPTATION.md first: it says which rules carry over unchanged and how the fixed NQ-point stops/targets are
translated to ES (proposed base: fractions of the 15-session average range; fixed ES points as a logged variant).

Data: my own ES 1-minute bars, `/Volumes/Lexar Armor 700 Media/Backtest Github/data/clean_ES_master.parquet`
(2013-12 → 2026-09, UTC per its MANIFEST) - copy it into this project's data/ folder, don't write to Backtest Github.
ES tick files (2021-06 → 2023-06) for tick-level fill checks. No TradingView or web data. Verify timestamps, time
zone and rolls yourself (A4 / Part B).

TradingView only for the reconciliation step: the Pine versions are in GitHub jarpteam-p28/Agent_Strategy_Search_Conti,
folder indicators/tradingview/ (run them on ES1! with the ES-translated inputs). The written spec wins any disagreement.

Monte Carlo: your standard 10,000 trade-resampling sims, plus Conti's prop simulation as written in the sheets
(resample whole trading days 20,000 times; 50K account, $2,500 end-of-day drawdown, $3,000 target, 20 days),
sized in MES to the same dollar risk.

Start with VAULT_BREAK_RULES_PROPOSED.md + ES_ADAPTATION.md. Follow BACKTEST_VALIDATION_CHECKLIST.md from A1 in
order: show me the ES rules in plain words plus every "decide before locking" question, and wait for my OK.
---
