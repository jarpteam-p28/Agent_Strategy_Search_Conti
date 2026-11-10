# ORB / IVB target statistics — 15, 30, 60-minute opening ranges (Pablo, 2026-11-10)

Pre-registered. Follow `CONTI_REVISED_BACKTEST_CHECKLIST.md`. Part 1 is a DESCRIPTIVE study (no P&L, no tuning);
Part 2 turns it into a small set of fixed strategies.

## Where this comes from
- **Deepcharts "Deep-M IVB"** (shown by a Deepcharts trader in a video, Jan 2026 NQ replays): opening range of 15, 30 or
  60 minutes (30 recommended) with High / Mid (IB_M) / Low, and after the break: **Protection** ("highest probability
  target of the day"), **Ext. Avg** (second target) and **Ext. Std-1** (third). The help page says the levels are
  "statistically derived … from historical probability models" but gives no formulas.
  - Reading the video's NQ chart (27 Jan 2026): IVB low ≈ 25,922, high ≈ 26,057 (range ≈ 135 pts); Protection 26,146
    (≈ **0.66 × range** above the high); Ext. Avg 26,280 (≈ **1.65 × range**). Pablo's notes: Protection ≈ 50% of the
    range, extension ≈ 1.5×. The names suggest Ext. Avg = **average past breakout extension**, Ext. Std-1 = average + 1
    standard deviation, Protection = a high-hit-rate (median-type) extension. We rebuild these from our own data.
- **Toby Crabel (1990)**, *Day Trading with Short Term Price Patterns and Opening Range Breakout*: entry a "stretch"
  away from the open, stretch = 10-day average of the smaller of (high − open) and (open − low).
- **Research already summarized**: Holmberg, Lönnbark & Lundström (2013), Tsai et al. (2019, best ES/NQ range = 1 min,
  in-sample), Lundström (breakouts pay in high volatility), Zarattini et al. (2023, 5-min ORB), Mesfin (2026, MNQ ORB not
  significant after costs).

## Data
ES 1-min `clean_ES_master.parquet` 2014-01 → 2023-12 and NQ 1-min `clean_NQ/continuous_1min.parquet` 2021-07 → 2023-12
(complete months). **Never touch 2024+.** New York time; close-stamped bars (09:31 bar = first RTH minute).
Regular session 09:30-16:00 ET. Skip half days.

## Definitions
- **Opening range (OR):** high/low of 09:30 → 09:45 (OR15), → 10:00 (OR30), → 10:30 (OR60). Mid = (high + low) / 2.
  Width R = high − low (points). Also record R ÷ AvgRange (Conti 15-session range) and R ÷ its own 20-day average.
- **Breakout:** the first 1-minute CLOSE above the OR high (up) or below the OR low (down) after the OR ends, before
  15:00 ET. Record its time. (Also count days with no break, and days that break both sides.)
- **Extension:** after an up-break, the highest high from the break to 16:00, minus the OR high, in units of R (down:
  mirror). **Retrace:** the deepest move back against the break before the extension high, in units of R.
- **Crabel stretch:** 10-day average of min(high − open, open − low) of the full RTH day, using the 10 previous days.

## Part 1 — descriptive statistics (per OR length × instrument × direction)
1. % of days with a break; % up vs down; % breaking both sides; median break time.
2. Extension distribution in R: mean, median, 25/75/90th percentiles, SD. **This rebuilds the Deepcharts levels:**
   Ext. Avg = mean, Ext. Std-1 = mean + 1 SD, and the "Protection" candidate = the level reached on ~70% of break days.
3. **Hit-probability table:** P(reach X × R beyond the broken side before 16:00) for X = 0.25, 0.5, 0.66, 1.0, 1.5, 2.0,
   AND P(reach X before the price returns to (a) the OR mid, (b) the opposite OR side). This is the key table.
4. Same table with the **rolling, out-of-sample** version: levels computed from the PREVIOUS 60 break days only (as a live
   indicator would), then checked on the next day.
5. Splits: volatility regime (AvgRange terciles, cutoffs from 2014-2018), R small/medium/large vs its 20-day average,
   break time (before/after 11:00), weekday, pre/post 2022 (0DTE), and Crabel stretch vs R.
6. Crabel check: P(price trades 1 × stretch beyond the open) and what happens next (continuation in R).

## Part 2 — fixed strategies (pre-registered; N = 3 OR lengths × 4 exits = 12 per instrument)
- Entry: first 1-minute close beyond the OR (both directions), enter next bar open; one trade per day; until 15:00.
- Stop: OR mid (base). Variant noted below.
- Exits (4): (a) target = 0.5 R, (b) target = Protection level from Part 1 step 4 (rolling, no look-ahead),
  (c) scale out half at Protection and the rest at Ext. Avg (rolling), (d) hold to 16:00.
- Baselines: same entry times with random direction (100 runs); always-long same times.
- Report per config: trades, win rate, avg win/loss, net $, PF, max DD, gross points per trade vs costs, without top
  5%/10% winners, 2x slippage, by year.
- Crabel version (1 extra config): buy stop at open + stretch / sell stop at open − stretch, first touch only, exit 16:00,
  stop at the opposite stretch level.
- Expect: high hit rates on small targets come from the payoff shape (small target vs larger stop) — judge on net
  expectancy and the random-direction baseline, not win rate (checklist A1c).

## Output
`results/ORB_TARGET_STATS/` with the hit-probability tables (CSV + one PNG per OR length), the rolling Protection /
Ext. Avg / Ext. Std-1 values per day (so a TradingView indicator can be built from them), Part 2 summary table, and a
plain-English summary first: "On ES/NQ, after a 30-min OR breaks, price reaches 0.5 R X% of the time before the mid…".
