# PD-Array Rejection + noise / CVD filters — PROPOSED (Pablo, 2026-10-21; needs A1 OK)

Follow `CONTI_REVISED_BACKTEST_CHECKLIST.md`. Objectives: PERSONAL + PROP EVALUATION + PROP FUNDED. Mode: FULL VALIDATION
for the base re-run; the filters are a pre-registered variant set (written before any result).

## Permission and source files
Pablo gives explicit permission for this task to READ (read-only, never write) Joshua's locked strategy:
- Spec: `Joshua Backtest data copy of drive/ES BACKTEST 2/results_combined/PINE_SCRIPT_SPEC.md`
- Python reference: `Joshua Backtest data copy of drive/ES BACKTEST 2/src/pd_setups.py`
- Live TradingView script: `Backtest Github/pine/pd_array_rejection_signal.pine`
Copies of the spec and the Pine script are in `incoming_specs/pd_rejection/` — work from those copies.
Rebuild the base strategy in THIS project from the spec (do not import Joshua's code), then match it to his Python on
the overlapping period as the A12 independent-rebuild check.

## Base strategy (Joshua's locked rules, unchanged — summary; the spec is the authority)
4H FVG + Rejection-Block zones (formed at the 4H bar CLOSE; invalidated by a 4H close through the far side) → at 09:30 ET
keep zones formed before 09:30, still valid, within 50 pts of the 09:30 open → scan 15-min bars 09:30–16:00 ET; first
bar that overlaps a zone, CLOSES outside it in the zone's direction and is not a doji (|C−O| ≥ 0.15 × range) triggers
(oldest zone first) → limit entry at 50% of that candle's wick, filled only after the trigger bar closes, same day →
stop 10 pts, targets 1R and 2R (two parallel legs, reported separately) → same-bar stop+target = stop. Max one setup
per day. 1 ES headline; real commission + 1 tick slippage (B4).

## The three filters (all evaluated at the CLOSE of the 15-min trigger bar — known at that moment, no look-ahead)
**C — Conti noise level (Vault Break level)**
- Session = midnight CT → 16:00 CT, MultiCharts close-time dating (the 23:30–00:00 CT 30-min bar opens it).
- SessOpen = open of that first 30-min bar. AvgRange = average session high − low of the last 15 COMPLETED sessions,
  skipping the most recent one. NoiseUp = SessOpen + 0.30 × AvgRange; NoiseDown = SessOpen − 0.30 × AvgRange.
- Reuse `scripts/vault_break_engine.py` (`compute_session_table`, `boundary_atr`).
- **Long passes if trigger close > NoiseUp; short passes if trigger close < NoiseDown.**

**Z — Zarattini noise area (bands that widen through the day)**
- sigma(t) = average over the previous 14 sessions of |close at minute t ÷ that day's 09:30 open − 1| (per minute of day).
- Upper(t) = max(open 09:30, prior 16:00 close) × (1 + sigma(t)); Lower(t) = min(...) × (1 − sigma(t)).
- Reuse `scripts/noise_area_engine.py`. t = the trigger bar's close minute.
- **Long passes if trigger close > Upper(t); short passes if trigger close < Lower(t).**

**D — Cumulative volume delta (CVD)**
- Per 1-minute bar: delta = volume × sign(close − open); if close = open, use the previous bar's sign.
  (Same rule as the TradingView indicator `cvd_15m.pine`, so the backtest matches what Pablo sees live — A14.)
- CVD = running sum of delta from the 09:30 ET bar (bar stamped 09:31 in close-stamped data) to the trigger bar's close.
- **Long passes if CVD > 0; short passes if CVD < 0.**
- A4/B8 check: on ES tick data 2021-06 → 2023-06, compute true CVD (aggressor side, or tick rule if the side is
  missing) and report how often its sign agrees with the bar estimate at the trigger times. Report only; don't switch.

## How a filter is applied — VETO (primary)
The base setup of the day is found exactly as in the spec. If the filter fails at the trigger bar's close, that day's
trade is SKIPPED (no re-scan for a later trigger). So every variant's trades are a subset of the base trades, and the
removed trades can be scored. (A "keep scanning for the next trigger that passes" version is NOT part of this set;
it would be a new pre-registered set.)

## The variant set (written before any result; N = 10 for DSR/PBO, plus any count from Joshua's original search)
| # | Rule | Long passes when | Short passes when |
|---|---|---|---|
| 0 | Base (no filter) | — | — |
| 1 | C | > NoiseUp | < NoiseDown |
| 2 | Z | > Upper(t) | < Lower(t) |
| 3 | D | CVD > 0 | CVD < 0 |
| 4 | C AND Z | both | both |
| 5 | C OR Z | either | either |
| 6 | C AND D | both | both |
| 7 | Z AND D | both | both |
| 8 | C AND Z AND D | all three | all three |
| 9 | (C OR Z) AND D | (C or Z) and D | (C or Z) and D |
Each row for the 1R leg and the 2R leg separately.

## Data and windows
- ES `clean_ES_master.parquet`, development **2014-01 → 2023-12 only**. 2024+ = protected / UNSEEN DATA (A3d gate).
- Report two windows side by side: **2014-01 → 2020-12** (never used in Joshua's work → fresh for this strategy) and
  **2021-01 → 2023-12** (Joshua's development/holdout period → already seen for the base).
- NQ (C11) later, complete months only.

## Report per variant (Part R table)
Trades, trades removed vs base and the P&L of the removed trades (win rate, avg R, net $), win rate, avg R, total R,
net $, PF, max DD, longest losing streak, year by year, long vs short, and every number again without the top 5% / 10% of
winners (C4 every-stat rule). Then C2 placebo for the best-looking rows (same days, random direction), cost stress
(2x slippage), DSR at the real N, and prop pass rate (Part P, 50K EOD −$2,500 / +$3,000, MES size sweep).
Warning to state up front: 10 variants on one dataset — expect at least one to look good by chance; only a variant that
holds on BOTH windows, beats the placebo and survives costs counts.

## Decide at A1 (proposed answers)
1. "Above the noise" = above the UPPER line (NoiseUp / Upper band) for longs, below the LOWER line for shorts. (Alternative
   reading "above the session open / band midline" is not in this set.)
2. Filters checked at the trigger bar's close (proposed) rather than at the fill.
3. VETO mode only (above).

## EXPANDED GRID (Pablo, 2026-10-21 12:57 — written before any result; replaces "N = 10")
Pablo is away: run everything end to end without waiting, using the A1 answers below. Never touch 2024+.
- **A1 answers (approved):** "above the noise" = above the UPPER line for longs / below the LOWER line for shorts;
  filters checked at the trigger bar's close; VETO mode.
- **Instruments:** ES 2014-01 → 2023-12 and NQ (`clean_NQ/continuous_1min.parquet`) 2021-07 → 2023-12, complete
  months only (list any gaps). NQ translation of Joshua's fixed-point inputs (ratio 4.7, ES_ADAPTATION.md):
  base stop 10 → 47 NQ pts, proximity 50 → 235 NQ pts. Volatility stops need no translation.
- **Stops (6):** base 10 pts (Joshua) + volatility stops k × AvgRange with k = **0.20, 0.22, 0.27, 0.28, 0.33**
  (AvgRange = Conti 15-session average range, skip most recent; known before the session).
- **Targets (5):** **1R, 1.5R, 2R, 2.5R, 3R**, where R = that row's stop distance.
- **Filters (10):** the table above (#0–#9).
- **Grid:** 10 × 6 × 5 = **300 configurations per instrument**. Run and report it as a SENSITIVITY GRID (C3) — no
  "pick the best cell". DSR / PBO use N = 300 per instrument (600 if any cell is chosen by comparing both).
- **Output:** one summary table per instrument (rows = filter × stop, columns = target: trades, win rate, avg R, net $,
  PF, max DD, net without top 10% winners), heat maps, and the removed-trades report for each filter at Joshua's base
  (10 pts / 1R and 2R). Then run the full robustness set (placebo, 2x slippage, concentration, year by year, prop pass rate)
  ONLY on: Joshua's base, plus at most 3 cells that hold up on BOTH windows (2014–2020 and 2021–2023) and on BOTH
  instruments, from a plateau (neighbouring stops/targets also positive), not single peaks.
- Finish with E2 scorecard + E2b adversarial review, and a plain-English summary for Pablo at the top.
