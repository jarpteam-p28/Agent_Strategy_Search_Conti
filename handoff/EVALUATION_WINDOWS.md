# Evaluation windows — Conti window + full history, each with an 80/20 split (Pablo, 2026-10-20)

These are REPORTING views of the same locked rules. They are not variants: they do not add to the A2 count / C9 N.
Parameters are Conti's, fixed — nothing is tuned in-sample, so in-sample vs out-of-sample here checks CONSISTENCY,
not overfitting of our own choices.

| Strategy | Window | Dates (ES 1-min) | In-sample (first ~80%) | Out-of-sample (last ~20%) |
|---|---|---|---|---|
| Vault Break | **Conti window** (his report) | 2022-01-21 → 2026-09-24* | 2022-01-21 → 2025-09-30 | 2025-10-01 → end of data |
| Vault Break | **Full history** | 2014-01-02 → end of data | 2014-01-02 → 2023-12-31 | 2024-01-01 → end of data |
| Drift VWAP Pullback | **Conti window** (his report) | 2021-01-04 → 2026-07-31 | 2021-01-04 → 2025-05-31 | 2025-06-01 → 2026-07-31 |
| Drift VWAP Pullback | **Full history** | 2014-01-02 → end of data | 2014-01-02 → 2023-12-31 | 2024-01-01 → end of data |

*ES data ends 2026-09-02.

Also show his own splits for comparison: Vault Break developed 2018–2022 / out-of-sample 2023+;
Drift VWAP developed 2020–2024 / out-of-sample 2024-08+.

## Rules
- The out-of-sample slices fall inside the checklist's protected data (2024 and the 2025+ UNSEEN DATA). They follow
  A3d exactly: written in RULES_<period>.md before loading, run once, nothing changed after, quarter by quarter,
  only with Pablo's explicit yes. Running them IS the one-time unseen-data test for this strategy.
- Report in-sample and out-of-sample side by side (trades, win rate, avg trade, PF, net $, max DD, with and without
  the top 5% / 10% winners), plus the ratio out-of-sample avg / in-sample avg.
- Dates are calendar cut-offs; trades still open at a cut-off are reported separately (A3c rule e).
