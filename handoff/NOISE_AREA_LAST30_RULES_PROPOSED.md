# Noise Area — last 30 minutes only (ES/NQ) — PROPOSED rules (needs A1 OK)

Follow `CONTI_REVISED_BACKTEST_CHECKLIST.md`. Source spec (agents, critic verdict "backtest", 2026-10-26):
`strategies/candidates/noise_area_last_half_hour_es.yaml`. Builds on Zarattini, Aziz & Barbon (2024) "Beat the Market"
(trend P&L builds from 14:00 into the close, FAQ Q18), Gao, Han, Li & Zhou (2018) "Market intraday momentum" (JFE) and
Baltussen, Da, Lammers & Martens (2021) "Hedging demand and market intraday momentum" (JFE).

## Part 0
Objectives: PERSONAL + PROP EVALUATION + PROP FUNDED. Mode: FULL VALIDATION. Headline = the pre-registered run below,
reported first, unchanged.

## Why it should work
Several players MUST trade near the close in the direction of the day's move: option dealers who are short gamma re-hedge
(bigger hedge on bigger moves), leveraged/inverse ETFs rebalance into the close, VWAP/close-benchmark algos finish their
orders, and market-on-close imbalances follow the day's direction. A day that is still outside its normal time-of-day
range (the noise band) at 15:30 is the day those forced flows are largest. This isolates the part of the full-day Noise
Area / Dual Noise Zone trade that the forced-flow WHY explains best — if it fails here, that WHY is weak on ES.

## A1 — Rules (headline, pre-registered)
- **Data:** ES `clean_ES_master.parquet` 1-min, regular hours 09:30–16:00 ET (UTC → New York with DST; close-stamped:
  the 09:31-stamped bar is the first RTH minute). NQ `clean_NQ/continuous_1min.parquet` as the second market.
- **Bands:** reuse `scripts/noise_area_engine.py`, unchanged: sigma(t) = mean of |close(t) / 09:30 open − 1| over the
  previous 14 sessions; Upper = max(open, prior 16:00 close) × (1 + 1.0 × sigma); Lower = min(...) × (1 − 1.0 × sigma).
- **VWAP:** session VWAP from 09:30 ET (same engine).
- **Decision:** at the close of the 15:30 ET bar only (one decision per day).
  - close > Upper(15:30) AND close > VWAP → **buy 1 contract** at the next bar's open.
  - close < Lower(15:30) AND close < VWAP → **sell 1 contract** at the next bar's open.
  - otherwise no trade.
- **Exit:** at the close of the 16:00 ET bar (the cash close). **No stop** in the headline (a pure 30-minute signal).
- **Skip:** half days (13:00 close), the first 14 sessions (warm-up), roll days if the roll isn't handled cleanly.
- **Costs:** real ES commission round trip + 1 tick slippage each way. (Average 30-min move is small — check gross vs costs.)

## Required baselines (same bars, same costs)
- **B1 always long** 15:30 → 16:00 every day.
- **B2 Gao-style rule:** direction of the day's 09:30 → 15:30 return, no band, no VWAP.
- **B3 random direction** on the same signal days (100 runs).
The strategy only counts if it beats B1 AND B2 on both ES and NQ.

## Variants (pre-registered; N = 1 headline + 5 = 6)
1. Stop: exit on a 1-min close back through max(Upper, VWAP) for longs / min(Lower, VWAP) for shorts.
2. Decision at 15:00 (60-minute hold).
3. Band only (no VWAP confirmation).
4. Long only.
5. Exit at 16:15 ET instead of 16:00 (includes the futures-only minutes after the cash close).
Lookback / multiplier sweeps are NOT in this set (in-sample only, later, plateau rule — Part O) — only if the headline
beats both baselines.

## Windows (A3e)
- ES development 2014-01 → 2023-12; report 2014–2021 and 2022–2023 (post-0DTE options era) separately.
- NQ 2021-07 → 2023-12, complete months.
- **2024+ is protected / UNSEEN DATA (A3d) — do not touch** (the agent spec's "out-of-sample to 2026-09" is overridden).

## Report
Trades, % of days with a signal, win rate, avg trade gross and net (and gross as a fraction of the average |15:30–16:00|
move), net $, PF, max DD, year by year, long vs short, real − B1 / B2 / B3, and without top 5% / 10% winners.
Dose-response check (supports the WHY): split signal days by distance from the band at 15:30 (in sigma units, terciles) —
bigger distance should mean bigger follow-through. Daily P&L correlation with Dual Noise Zone.
