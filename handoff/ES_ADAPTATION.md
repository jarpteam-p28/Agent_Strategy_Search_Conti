# Running Conti's NQ strategies on ES — PROPOSED translation (decide at A1)

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
| Vault Break TP / SL | 40 / 75 points fixed | **0.10 / 0.20 × 15-session avg range** (what 40/75 were vs NQ's ~380-pt avg range in 2022-26) | fixed 8.5 / 16 ES points (÷ 4.7) |
| Drift VWAP min 1-hour move | 0.10 % | 0.10 % | 0.075 % (ES moves ~1.35× less in % terms) |
| Drift VWAP TP long / TP short / SL | 40 / 50 / 80 points fixed | **0.10 / 0.13 / 0.21 × 15-session avg range** | fixed 8.5 / 10.75 / 17 ES points |
| Overnight Bias stop / target | 0.30 × avg range, 3R | unchanged (already volatility-scaled) | — |
| Overnight thirds, opening range, ADX > 20 | — | unchanged | — |
| Session times | CT / ET as in each sheet | unchanged (ES and NQ trade the same hours) | — |

The ATR-scaled base is a change from his fixed-point rules — it keeps the same *shape* (small target, wide stop,
high win rate) across 13 years of different volatility. It must be logged as a deliberate translation (A1/A2).

## Costs and sizing
- ES: $50 per point, tick 0.25 = $12.50. Costs bite harder relative to the target: ~1 tick of slippage is ~3% of an
  8.5-point target, vs ~0.6% of a 40-point NQ target. Use real commission + slippage from the start.
- Prop simulation: size to the same dollar risk as his NQ test (≈ $1,500 per trade for Vault Break, ≈ $1,600 for
  Drift VWAP), using MES (micro, $5/point) to get close — e.g. a 16-point ES stop = $80 per MES → ~19 MES.
  Or run his size sweep in MES.

## Extra benefit of ES
2013–2026 gives a real in-sample period before his out-of-sample years, e.g. in-sample 2014–2020, out-of-sample
2021–2025-09, holdout 2025-10 → 2026-09 (to confirm at A3). NQ can still be the "second instrument" test (C12)
on the months that exist.
