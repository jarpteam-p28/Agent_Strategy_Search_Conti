# Running Conti's NQ strategies on ES — PROPOSED (decide at A1)

**Pablo's decision (2026-10-20): run it exactly like Conti does.** Base = his code unchanged on ES. For Vault Break
his exits are in DOLLARS (TakeProfitDollars 800, StopLossDollars 1500), so on ES the base is **$800 / $1,500 per
contract = 16 / 30 ES points**. The volatility translations below are logged variants only, not the base.

Why ES: Pablo's ES 1-minute data is complete from Dec 2013 to Sep 2026; the NQ tick files miss five contracts
(12-21, 03-22, 03-25, 06-25, 09-25). Conti himself says to run the same code on ES.
Consequence: his NQ numbers can no longer be reconciled one-to-one — they become a rough guide only.

## Data
- Longest series: `Backtest Github/data/clean_ES_master.parquet` — ES 1-minute, 2013-12-08 → 2026-09-02, timestamps
  UTC (see its MANIFEST: NinjaTrader contract files 2013–2021 + Joshua's clean series 2021–2026). Reading it is fine;
  copy it into `Backtest_Conti_Research/data/` rather than writing to the other project.
- Fill checks at tick level: ES tick files 2021-06 → 2023-06 only.
- Re-verify timestamps, time zone and rolls (A4 / Part B) — don't trust the manifest alone.

## What scales and what doesn't
NQ moves far more points than ES. Measured on TradingView daily bars (median daily range NQ ÷ ES):
2018 3.4 · 2019 3.5 · 2020 3.8 · 2021 4.8 · 2022 4.1 · 2023 4.5 · 2024 5.0 · 2025 4.7 · 2026 5.8.
Median over his test periods (2021-07 → 2026-09): **4.7**. The ratio drifts, so fixed points are a poor translation
over 2013–2026 (an ES day ranged ~33 points in 2019 and ~92 in 2026).

| Rule | On NQ (his) | ES translation — **proposed base** | ES variant to log |
|---|---|---|---|
| Vault Break noise level | 0.30 × 15-session avg range | unchanged (already volatility-scaled) | — |
| Vault Break TP / SL | $800 / $1,500 per contract (= 40 / 75 NQ pts) | **$800 / $1,500 = 16 / 30 ES points (his code as written)** | 8.5 / 16 ES points (÷ 4.7, same shape as on NQ); 0.10 / 0.20 × avg range |
| Drift VWAP min 1-hour move | 0.10 % | 0.10 % | 0.075 % (ES moves ~1.35× less in % terms) |
| Drift VWAP TP long / TP short / SL | 40 / 50 / 80 NQ points (code not shown) | **same dollars: $800 / $1,000 / $1,600 = 16 / 20 / 32 ES points** | 8.5 / 10.75 / 17 ES points; 0.10 / 0.13 / 0.21 × avg range |
| Overnight Bias stop / target | 0.30 × avg range, 3R | unchanged (already volatility-scaled) | — |
| Overnight thirds, opening range, ADX > 20 | — | unchanged | — |
| Session times | CT / ET as in each sheet | unchanged (ES and NQ trade the same hours) | — |

Caution: on ES the $800 / $1,500 bracket is about 4.7x wider relative to ES's daily range than it was on NQ, so expect
fewer target hits and more 14:30 time exits than his NQ report. That is what 'his code on ES' really does.

## Closest possible copy of his own test: NQ on the months we have
His Vault Break report is NQ 1/2022 → 9/2026. Pablo's NQ files miss the front months 12-21, 03-22, 03-25, 06-25,
09-25 (≈ Sep 2021–Mar 2022 and Dec 2024–Sep 2025), so roughly Mar 2022 → Nov 2024 and Sep 2025 → Sep 2026 are
usable (check whether back-month ticks in neighbouring files fill any of it). Running his rules there and comparing
month by month with his report is the most direct replication; ES is the long-history test.

## Costs and sizing
- ES: $50 per point, tick 0.25 = $12.50. Use real commission + slippage from the start (1 tick ≈ 1.6% of the
  16-point base target; ≈ 3% of the 8.5-point variant).
- With his dollar bracket, 1 ES risks the same $1,500 per trade as his 1 NQ - so 1 ES is directly comparable in
  dollars. Prop simulation: his settings, size sweep in MES (10 MES = 1 ES).

## Extra benefit of ES
2013–2026 gives a real in-sample period before his out-of-sample years, e.g. in-sample 2014–2020, out-of-sample
2021–2025-09, holdout 2025-10 → 2026-09 (to confirm at A3). NQ can still be the "second instrument" test (C12)
on the months that exist.
