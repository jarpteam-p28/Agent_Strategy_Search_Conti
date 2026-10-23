# Volatility contraction → breakout: what the research says, and how to test each idea (Pablo, 2026-10-23)

Follow `CONTI_REVISED_BACKTEST_CHECKLIST.md`. Everything below is written BEFORE any result (pre-registered).
**Data:** NQ 5-min built from `clean_NQ/continuous_1min.parquet` 2021-07 → 2023-12 (complete months only) and ES 5-min from
`clean_ES_master.parquet` 2014-01 → 2023-12. **2024+ is protected — never touch it.** Times New York. 1 contract, real
commission + 1 tick slippage. Shared volatility yardstick: **AvgRange** = Conti 15-session average range (midnight CT →
16:00 CT, skip most recent; reuse `vault_break_engine.py`).

---------------------------------------------------------------------------------------------------------------------
## Part 1 — The research (source → finding → what it predicts)

| # | Source | Finding | Testable claim |
|---|---|---|---|
| R1 | Engle (1982) ARCH; Bollerslev (1986) GARCH; Andersen & Bollerslev (1997) intraday volatility | Volatility clusters: big moves follow big moves, quiet follows quiet. Very strong evidence. | Range SIZE is predictable; direction is not. A tight range predicts a smaller next range in the short run. |
| R2 | Christoffersen & Diebold (2006), *Management Science* / NBER w10009 | Volatility changes can create direction predictability only when the expected return is not zero. | Any direction edge on NQ/ES may be the upward drift → must beat always-long. |
| R3 | Toby Crabel (1990), *Day Trading with Short Term Price Patterns and Opening Range Breakout* | NR4 / NR7 (narrowest range of 4 / 7 days) days are followed by expansion; trade the next day's opening-range break. Practitioner, no peer review. | Next-day ORB pays more after NR4/NR7 days than after normal days. |
| R4 | Zarattini, Aziz & Barbon (2024), *Beat the Market* (Tables 5–6) | Intraday momentum had its best average P&L on NR4 days (22 bps, t = 5.1); many patterns tested. | NR4 as a filter for the Noise Area / Dual Noise Zone strategy. |
| R5 | John Bollinger (2001); John Carter, *Mastering the Trade* (2005, TTM Squeeze); Leung & Chong (2002/03) | Squeeze = Bollinger Bands inside Keltner Channels; practitioner claims. Academic test: Bollinger Bands no better than simple envelopes. | Squeeze release → move in the release direction beats random. |
| R6 | Crabel (1990); Holmberg, Lönnbark & Lundström (2013), *Finance Research Letters* 10(1); Zarattini et al. (2023) 5-min ORB in stocks | ORB returns significantly above zero (futures). | ORB (5-min and 30-min) is profitable after costs. |
| R7 | Lundström, *Day trading returns across volatility states* (Umeå, 2013/2017) | ORB returns much higher in the HIGHEST volatility state (S&P futures ≈ 150 bps/day difference vs lowest). | Breakouts pay in high volatility — the OPPOSITE of "trade after contraction". |
| R8 | Steidlmayer & Koy (1986) *Markets and Market Logic*; Dalton, *Mind Over Markets* (1990); Chen & Chen (2015, TAIEX) | Market Profile value area (70% of volume); "80% rule"; breakout/acceptance outside value. Mostly practitioner. | Open outside value and re-enter → travels to the other side of value; or acceptance outside value → continuation. |
| P | Pablo's idea | Tight intraday range (fraction of ATR) then breakout predicts the next move. | T4 below. |

---------------------------------------------------------------------------------------------------------------------
## Part 2 — Tests (run every test on NQ and ES; report both)

Every P&L test gets the SAME baselines and splits (required, Part C2/C2b/C8):
- **B1 always-long** with the same entry times, stop and exit; **B2 random direction** at the same times (100 runs);
  **B3 random time** same day, same stop/exit (100 runs). Edge = real minus baseline.
- **Volatility-state split (R7):** AvgRange quintiles, cutoffs from the first 60% of each instrument's data only.
- Long vs short; year by year; without top 5% / 10% winners; 2x slippage.

### T1 — Clustering / size (R1) — DESCRIPTIVE, no P&L
On 5-min bars: rolling range of the last 6 bars (30 min) ÷ AvgRange. Bucket into quintiles. For each bucket report the
range of the NEXT 6, 12, 24 bars ÷ AvgRange (median, 75th, 90th) and the share of next-hour moves > 0.25 × AvgRange.
Answers: does a tight 30 minutes predict a bigger or smaller next hour?

### T2 — NR4 / NR7 + next-day ORB (R3)
Daily RTH range (09:30–16:00). NR4 = narrowest of last 4 days; NR7 = narrowest of last 7. Next day: opening range = first
30 min; buy on a 5-min close above the OR high / sell below the OR low (first break only, 10:00–15:00); stop = other side
of the OR; exit 16:00. Compare: after NR7 / after NR4 / after all other days. Variants: OR 5 min vs 30 min. (4 configs)

### T3 — Squeeze release (R5), 5-min bars
Squeeze ON when BB(20, 2.0) is inside KC(20 EMA, 1.5 × ATR(20)). Signal = first bar squeeze turns OFF after ≥ 6 bars ON,
09:45–15:00. Direction = close vs the 20-bar mean (above = long). Enter next bar open; stop 1 × ATR(20) of 5-min;
exit after 12 bars (1 h) or 16:00. Variant: KC 1.5 vs 2.0. (2 configs)

### T4 — Pablo's tight-range breakout (P), 5-min bars
Box = high/low of the last K bars (K = 6, i.e. 30 min). Tight when box height ≤ 0.10 × AvgRange (variant 0.15).
Breakout = first 5-min CLOSE above the box high (long) or below the box low (short), 10:00–15:00, one trade per box.
Enter next bar open; stop = other side of the box; exits: 2R target, or 1-hour time exit, or 16:00 (3 exit variants).
(2 thresholds × 3 exits = 6 configs.) Also report the same rule on NON-tight boxes as the comparison group.

### T5 — Opening range breakout (R6)
OR = first 5 min and first 30 min after 09:30. Long on a close above OR high, short below OR low (first break, until 15:00);
stop = other side of the OR; exit 16:00. (2 configs.) Report by volatility state (R7) — this is the Lundström test.

### T6 — NR4 filter on the Noise Area strategy (R4)
Run the existing Dual Noise Zone / Noise Area base (`noise_area_engine.py`) only on days after an NR4 day vs all days.
(1 config, no re-tuning.)

### T7 — Market Profile value area (R8)
Prior day RTH volume profile from 1-min bars (volume at each bar's typical price, 1-tick bins for ES, 1-point for NQ);
value area = 70% of volume around the point of control. Two rules:
- **80% rule:** open outside the prior value area, then two consecutive 30-min closes back inside → trade toward the
  opposite edge of value; stop = the 09:30 open's side extreme of the day so far; exit at the far edge or 16:00.
- **Acceptance breakout:** two consecutive 30-min closes outside value → trade in that direction; stop = back inside
  value by 0.25 × AvgRange; exit 16:00.
(2 configs.)

---------------------------------------------------------------------------------------------------------------------
## Part 3 — Counting and verdicts
- Variant count: T2 4 + T3 2 + T4 6 + T5 2 + T6 1 + T7 2 = **17 configurations per instrument** (T1 descriptive, not counted).
  DSR / PBO use N = 17 per instrument (34 if a pick is made by comparing both).
- An idea counts only if it: beats B1 AND B2 on BOTH instruments, is positive after 2x slippage, and does not depend on
  one year. Expect most to fail — that is the point of checking the research first.
- Output: one summary table (rows = configs, columns = NQ / ES: trades, win rate, avg R, net $, PF, max DD, real − B1,
  real − B2, by volatility quintile), plus T1 tables. Plain-English summary first.
