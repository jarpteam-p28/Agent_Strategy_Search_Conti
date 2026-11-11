# ADDENDUM to ALL_STRATEGIES_BUNDLE_2026-11-06 — updated 2026-11-10 (all 125 papers read)

Same rules as the main bundle (quick screen first, scoreboard line after each, ES 2014-2023 / NQ 2021-07-2023-12, never 2024+). Public FOMC/BLS release calendars are approved.

## TIER 4 — studies already written (run after Tiers 1-3)
- A) `incoming_specs/ORB_TARGET_STATS_STUDY.md` — ORB 15/30/60-min hit-probability tables, rebuilt Deepcharts Protection / Ext. Avg / Ext. Std-1 levels, Crabel stretch, 13 fixed strategies per instrument.
- B) `incoming_specs/VOLATILITY_BREAKOUT_RESEARCH_TESTS.md` — T1-T7 (NR4/NR7, squeeze, tight-range breakout, ORB by volatility regime, Market Profile value area).
- C) Dual Noise Zone (`noise_area_momentum_es`) FULL VALIDATION on NQ 2021-07-2023-12 — it works on NQ, not ES (independent replication: NQ t = 2.74). ALSO run the Chuk (2026) executable NQ build: 5-min bars; entries only at :00/:30 from 10:00 to 15:30 (long if close > upper band AND > VWAP, short mirror); fill next bar open; resting trailing stop = the nearer of band or VWAP, recomputed every 5 minutes at the bar close and active from the next bar; flat at 15:55; 1 MNQ, $2 per round trip. Paper: +$10.26/day net 2020-Jul 2026, Sharpe 1.14, flat 2014-2019. Report the +1-point stop-slippage stress and the 3-year bootstrap max drawdown vs a $2,500 EOD limit. Our NQ window sits in the paper's best years — not independent confirmation.
- D) `incoming_specs/pd_rejection/PD_REJECTION_FILTER_STUDY.md` — only if not already finished in results/.
- E) Overnight Bias ORB — confirm all 3 overnight start times (18:00, 00:00, 01:00 ET) were run.

- Not testable (no data): megacap_earnings_overnight_split_nq, dividend payment-day effect (needs S&P pay-date calendar), 0DTE/gamma-flow ideas, single-stock specs.

---
## TIER 5 — new research ideas from the 2026-11-09 agent run (quick screen)

### 25. `deleveraging_rebound_es_daily` — Multi-Day Deleveraging Rebound (ES daily, long only, N-day time exit)
- **Spec:** `strategies/candidates/deleveraging_rebound_es_daily.yaml` · verdict: refine · data: yes
- **Finding:** This is a model result, from memory and not verified. Forced liquidation by levered holders, spreading through crowded positions, pushes prices below fundamental value over several days. Prices recover once the liquidation is complete.
- **Why:** Margin calls, vol-target and risk-parity de-risking, and CTA stop-outs force sales spread over several days, because large positions cannot be dumped in one session (liquidity constraints on large orders). Predators front-run, which deepens the drop. Once realised volatility stops rising, the mechanical selling ends and the price partly recovers. The proxy for 'forced selling is over' is a large multi-day drop on heavy volume followed by the first up close.
- **Market:** instruments: ES; NQ; bar_size: daily built from 1-min (RTH close 16:00 ET; also volume); session: Daily, RTH close-to-close 16:00 America/New_York · direction: long_only
- **Entry long:** Setup: the 3-day RTH close-to-close return is at or below -K × σ_daily × sqrt(3), where σ_daily is the 60-day standard deviation of daily returns. The average volume over the 3 days must also be at least V × the 60-day average. Entry: buy at the RTH close of the first day after the setup that closes up (the exhaustion signal). The setup expires after 5 days.
- **Entry short:** —
- **Filters:** No new setup while a position is open.; Variant: require that 20-day realised volatility rose by at least 50% over the last 10 days (a deleveraging regime).
- **Exit:** stop: Close below the lowest close of the selloff minus 0.5 × the 15-day ATR · target: None in the base test · time: Exit at the RTH close N=5 trading days after entry
- **Parameters:** K_sigma=2.5 (test 2.0, 2.5, 3.0); volume_multiple_V=1.3 (test 1.0, 1.3, 1.6); hold_days_N=5 (test 3, 5, 10); lookback_days=60 (test 40, 60, 120)
- **Variants (pre-registered):** Hold 3 vs 10 days; Enter at the next RTH open instead of the close; Realised-volatility jump gate only
- **Extra checks:** Compare with being long N days from a random entry, and from any day after a down close.; Long-only beta check: report 2022 separately.; Remove the top 3 trades and re-check sign.
- **Data needs:** ES 1-min 2013-2026 aggregated to daily RTH bars with volume (have); NQ 2021+ (have, short)
- **Notes:** Status is idea because the rules are speculative and the event sample is small.

### 26. `forced_selling_flush_fade_es` — Forced-Selling Flush Fade (ES/NQ intraday, long only, time exit)
- **Spec:** `strategies/candidates/forced_selling_flush_fade_es.yaml` · verdict: refine · data: partial
- **Finding:** This is a theory result with no empirical sample, and it was read from the abstract and memory only. When a large trader is forced to sell and others can see it, rivals sell first. The price is pushed below fundamental value and recovers once the forced flow is finished. The overshoot is bigger when liquidity is thin, the position is large and the seller is near its margin limits.
- **Why:** The WHY is liquidity constraints on large orders combined with an institutional constraint. Margin calls, risk limits and vol-target de-risking force sales that do not depend on price. Liquidity providers must be paid to absorb them, and predators sell ahead, so the price overshoots. When the forced flow stops, nothing keeps the price down and it partly recovers. We cannot see who is distressed. Our proxy is the footprint of forced flow: an abnormally fast, high-volume drop compared with the normal move at that time of day, followed by a sign that selling is exhausted (no new low for a few minutes). The test is reversion after the flow ends. We do not fade into the flow itself, because the playbook's gamma study found that faders who come in early lose.
- **Market:** instruments: ES; NQ; bar_size: 1min (signals on rolling 30-min windows); session: RTH 09:30-16:00 America/New_York (data stored in UTC, convert with DST); signals allowed 10:00-15:00 ET · direction: long_only
- **Entry long:** Flush trigger: during 10:00-15:00 ET, the trailing 30-minute return is at or below -K × σ30. σ30 is the 20-day standard deviation of 30-minute returns ending at the same clock time. Trailing 30-minute volume must also be at least V × the 20-day average volume for the same clock window. After the trigger, wait for exhaustion: go long at the close of the first 1-minute bar that completes X consecutive minutes without a new low below the flush low. If no exhaustion occurs by 15:15 ET, there is no trade.
- **Entry short:** —
- **Filters:** One trade per day. After a trigger, take the first event only (cluster lockout).; Do not use the first 30 minutes after the open, so overnight-gap dynamics are excluded. Those are covered by nq_extreme_overnight_drop_rebound.; Skip the 08:30/10:00 ET macro release minutes and FOMC 14:00-14:30 ET, where the drop is news repricing rather than forced flow.; Variant filter: regime gate where 20-day realised volatility is above its 1-year median, i.e. a stress regime where deleveraging is likely.
- **Exit:** stop: Flush low minus 0.25 × the 15-session average daily ATR · target: Optional: retrace of R × the flush size (default 0.5, i.e. 50% of the drop). Test with no target as well. · time: Flat at 15:59 ET. Variant: hold to the next 09:35 ET. · other: Master-signal test first: fixed holds of 60 and 120 minutes and to the close, with no stop and no target, compared with an always-long baseline over the same clock windows.
- **Parameters:** K_sigma_threshold=3 (test 2.0, 2.5, 3.0, 3.5); volume_multiple_V=2 (test 1.5, 2.0, 3.0); window_minutes=30 (test 15, 30, 60); exhaustion_minutes_X=5 (test 3, 5, 10); lookback_days=20 (test 10, 20, 40); stop_atr_fraction=0.25 (test 0.15, 0.25, 0.4); retrace_target_R=0.5 (test none, 0.38, 0.5, 0.75)
- **Variants (pre-registered):** Hold to the next RTH open at 09:35 ET to capture the overnight recovery.; Regime-gated only (realised volatility above the median).; Stop-free master signal with fixed 60/120-min holds.
- **Extra checks:** Must beat the always-long baseline over the same clock windows on gross points per trade. Report gross vs net with about $5 round trip ES and $13 NQ.; Net t ≥ 2 and the same sign in every out-of-sample year (Mesfin note).; Report 2020, 2022 and Aug 2024 separately, plus results with the top 10 trades removed (outlier dependence).; Split results by regime (high vs low realised volatility) and before/after 2022.; Falsification: run the mirror case (a high-volume spike up followed by a fade short). The theory predicts weaker or no reversion there.
- **Data needs:** ES 1-min OHLCV 2013-2026 (have); NQ 1-min 2021-2026 (have); Macro and FOMC release calendar (must build)
- **Notes:** This differs from nq_extreme_overnight_drop_rebound, which trades the overnight gap at the open. This spec trades intraday RTH flushes after the open window.; This differs from letf_rebalance_day_reversal_nq, which trades close to next close by mechanical rebalancing. Here the trigger is a volume/speed footprint at any time of day.

### 27. `letf_close_rebalance_continuation_nq` — LETF/Gamma Close-Rebalance Continuation, signed by close-to-close move (NQ/ES, 15:30-16:00 ET, long/short)
- **Spec:** `strategies/candidates/letf_close_rebalance_continuation_nq.yaml` · verdict: refine · data: partial
- **Finding:** Abstract only, with no sample numbers. In individual stocks, leveraged-ETF rebalancing and the hedging of short-gamma option dealers create order flow late in the day in the direction of the day's move. Prices continue into the close and then partly reverse. The options (gamma) part held up across the authors' whole sample. The LETF part has weakened because the flow is public and liquidity providers compete to absorb it.
- **Why:** Execution mechanics of big players, forced by mandate and by hedging. A leveraged ETF must reset its exposure every day to L times NAV. The trade it needs is proportional to (L² − L) × the close-to-close return, and it is done near the close so it matches NAV. Short-gamma dealers must also buy into rallies and sell into declines. Both flows point the same way as the day's close-to-close move and arrive in the same late window. Liquidity providers demand a price concession, so price drifts in the move's direction into 16:00. Our angle, not the paper's rule: (1) sign the signal by the CLOSE-TO-CLOSE return (prior 16:00 to 15:30), because that is what LETFs rebalance on. Our existing noise-area strategies use the move from the open. (2) Expect the edge to be larger on NQ, because TQQQ/SQQQ dominate LETF assets. (3) Expect it only where dealers are likely short gamma: high-volatility regimes and non-expiry days. Since 0DTE, dealers are often long gamma, which dampens or reverses the effect.
- **Market:** instruments: NQ; ES; bar_size: 1min; session: RTH 09:30-16:00 America/New_York (data stored in UTC; convert with DST) · direction: long_short
- **Entry long:** At the close of the 15:29 ET bar (entry 15:30 ET), compute S = (price_15:30 / prior RTH close at 16:00 ET) − 1. If S > +k × A, where A = the 14-day average absolute close-to-close RTH return, buy 1 contract.
- **Entry short:** Under the same computation, if S < −k × A, sell 1 contract.
- **Filters:** One trade per day at most; no re-entry.; Skip half-day sessions (early 13:00 ET closes) and days with fewer than 14 days of warm-up.; Main run: all days. Report results separately for monthly opex (3rd Friday), quarterly opex and non-expiry days. The hypothesis is that the edge is weaker or reversed on opex days.; Report results separately by volatility regime. Regime proxy: realized vol of the trailing 5 days divided by trailing 60 days. If above 1, treat it as a likely short-gamma regime with a stronger edge.; Report results separately before and after 2022, the 0DTE era (ES only, since NQ starts in 2021-07).
- **Exit:** stop: Master-signal test: no stop, so the exit cannot flatter the entry. Tradable version: stop at 0.3 × the 15-session average daily ATR from entry. · target: — · time: Close at the 15:59 ET bar close (flat before the 16:00 settlement). Never hold overnight. The overnight reversal leg is covered by letf_rebalance_day_reversal_nq. · other: Benchmark: always long 15:30-15:59 on all days and on the same signal days. Also benchmark against the open-signed noise_area_last_half_hour_es signal on the same days.
- **Parameters:** entry_time_et=15:30 (test 15:00, 15:15, 15:30, 15:45); k_threshold=1 (test 0, 0.5, 1.0, 1.5, 2.0); avg_move_lookback_days=14 (test 10-30); stop_atr_fraction=0.3 (test none, 0.2, 0.3, 0.5); vol_regime_ratio=1 (test 0.8-1.5)
- **Variants (pre-registered):** Rebalance-weighted signal: (L² − L) × S with L = 3, which only changes scaling. Test a convex threshold instead.; Window 15:50-15:59 only (after the closing-imbalance publication).; Fade version on opex/low-vol days: trade against S from 15:30 to 15:59.; Long-only variant, in case strong up-days continue more than down-days.
- **Extra checks:** Chronological 80/20 split. ES 2013-2026 is the long test. NQ 2021-2026 is short, so it gets fewer trades; report its t-stat.; Report gross points per trade vs costs (about $13 per NQ round turn plus 1 tick of slippage). Require net t ≥ 2 and the same sign in each out-of-sample year.; Long side vs short side separately.; Results by signal-strength quintile of |S|/A. The edge should be monotonic.; Pre-2022 vs post-2022, opex vs non-opex, high vs low vol regime.; NQ vs ES on overlapping dates. The hypothesis says NQ is stronger.; Correlation of daily P&L with noise_area_last_half_hour_es and with letf_rebalance_day_reversal_nq.
- **Data needs:** ES 1-min 2013-2026 (have); NQ 1-min 2021-07 to 2026 (have); Exchange holiday and early-close calendar; Monthly and quarterly opex calendar (derivable); Optional: TQQQ/SQQQ/UPRO/SPXU AUM history; NDX/SPX option open interest for gamma
- **Notes:** New angle versus the existing late-day strategies: the signal is signed by the close-to-close return (the quantity LETFs rebalance on) rather than the move from the open, and it is conditioned on a gamma-regime proxy.; Abstract-only source. Expect about half the paper's effect or less (McLean & Pontiff).

---
## TIER 6 — from the last 27 papers read 2026-11-10 (quick screen)

### 28. `fomc_cycle_even_weeks_es` — FOMC-cycle even weeks (hold ES only in weeks 0, 2, 4, 6)
- **Spec:** `strategies/candidates/fomc_cycle_even_weeks_es.yaml` · verdict: refine · data: yes
- **Finding:** 1994-2013: the whole equity premium came in even FOMC-cycle weeks; staying out in odd weeks doubled the Sharpe ratio (0.4 → 0.8).
- **Why:** Fed information flow and policy news cluster bi-weekly after each scheduled meeting.
- **Market:** instruments: ES; NQ; bar_size: 1min; session: America/New_York; universe: ES 2014-2023, NQ 2021-07-2023-12 (2024+ protected) · direction: long_only
- **Entry long:** Day 0 = scheduled FOMC decision day. Hold ES from the 16:00 close of day −2 to the 16:00 close of day 3 (week 0), and likewise for weeks 2 (days 9-13), 4 (19-23), 6 (29-33), counting TRADING days. Flat otherwise.
- **Entry short:** —
- **Filters:** Scheduled meetings only (public FOMC calendar); If the next meeting arrives before week 6 ends, restart the count
- **Exit:** stop: — · target: — · time: End of each even week (16:00 ET).
- **Parameters:** weeks_held=0,2,4,6 (test fixed (paper))
- **Variants (pre-registered):** long even weeks; long even / short odd
- **Extra checks:** Development data only; 2024+ protected; Baseline: buy-and-hold ES and odd-weeks-only; Report each even week separately and by year; Variant: short odd weeks (paper's Strategy D)
- **Data needs:** ES/NQ daily closes from 1-min; FOMC scheduled-meeting dates (public calendar)

### 29. `macro_announcement_day_long_es` — Macro announcement days long (CPI, PPI, NFP, FOMC)
- **Spec:** `strategies/candidates/macro_announcement_day_long_es.yaml` · verdict: refine · data: yes
- **Finding:** 1958-2009: market excess return 11.4 bp on CPI/PPI/employment/FOMC days vs 1.1 bp on other days (t = 3.77).
- **Why:** Premium for bearing macro risk resolved on announcement days.
- **Market:** instruments: ES; NQ; bar_size: 1min; session: America/New_York; universe: ES 2014-2023, NQ 2021-07-2023-12 (2024+ protected) · direction: long_only
- **Entry long:** Buy at the 16:00 ET close the day before a scheduled CPI, PPI, Employment Situation (NFP) or FOMC decision day; sell at the 16:00 close on the announcement day.
- **Entry short:** —
- **Filters:** Official release calendars (BLS, Fed); Variant A: RTH only (09:30 → 16:00 on the day); Variant B: by announcement type
- **Exit:** stop: — · target: — · time: 16:00 ET on the announcement day.
- **Parameters:** window=close-to-close (test close-to-close, overnight only, RTH only)
- **Variants (pre-registered):** close-to-close; overnight only; RTH only
- **Extra checks:** Development data only; 2024+ protected; Baseline: all non-announcement days; Split by announcement type and by year; Without the best 5 days
- **Data needs:** ES/NQ 1-min; BLS/Fed release dates (public calendars)

### 30. `close_reversal_overnight_es` — Close reversal overnight (fade the last 30 minutes, hold to 10:00)
- **Spec:** `strategies/candidates/close_reversal_overnight_es.yaml` · verdict: refine · data: yes
- **Finding:** S&P futures reverse the last 20-60 minutes of the session overnight, strongly when implied variance is high and after down moves; 30-min version ≈ 12 bp/day gross (1990-2015).
- **Why:** Closing liquidity pressure and option-hedging flows revert once fresh liquidity arrives.
- **Market:** instruments: ES; NQ; bar_size: 1min; session: America/New_York; universe: ES 2014-2023, NQ 2021-07-2023-12 (2024+ protected) · direction: long_short
- **Entry long:** If the 15:30-16:00 ET return is negative, buy at the 16:00 close.
- **Entry short:** If it is positive, sell at the 16:00 close (variant: long side only, per the paper's asymmetry).
- **Filters:** Base: all days; Conditioned: only when AvgRange (15-session) is in its top tercile (cutoffs from 2014-2018) — VIX proxy; Size filter: |last-30 return| above its 20-day median
- **Exit:** stop: None in base; variant 1 × the last-30 move beyond the 16:00 close. · target: — · time: 10:00 ET next session. · other: Variant exit 09:35 and 09:30
- **Parameters:** formation_minutes=30 (test 20, 30, 60); exit_time=10:00 (test 09:30, 09:35, 10:00)
- **Variants (pre-registered):** 3 formation × 3 exits × 2 filters (pre-registered)
- **Extra checks:** Development data only; 2024+ protected; Random-direction baseline (100 runs); Split by volatility tercile, by sign, pre/post 2022; 2x slippage
- **Data needs:** ES/NQ 1-min
- **Notes:** Opposite of the last-half-hour momentum idea: momentum INTO the close, reversal AFTER it — test both on the same days.

### 31. `expiration_pin_es` — Expiration-day pinning (descriptive + fade toward the round strike)
- **Spec:** `strategies/candidates/expiration_pin_es.yaml` · verdict: refine · data: partial
- **Finding:** S&P futures are pulled toward the at-the-money strike on futures-option expiration days; hedge unwinding moves index futures in the 30 minutes before expiration.
- **Why:** Dealer delta-hedge decay and unwinding into expiration.
- **Market:** instruments: ES; NQ; bar_size: 1min; session: America/New_York; universe: ES 2014-2023, NQ 2021-07-2023-12 (2024+ protected) · direction: long_short
- **Entry long:** Monthly ES-option expiration days (3rd Friday; variant: every weekly Friday). At 14:30 ET, find the nearest 25-point strike K. If price is more than 0.15 × AvgRange BELOW K, buy.
- **Entry short:** If more than 0.15 × AvgRange ABOVE K, sell.
- **Filters:** Step 1 (descriptive, no P&L): distribution of |16:00 close − nearest 25-pt strike| on expiration vs non-expiration days, and 15:30-16:00 range
- **Exit:** stop: 0.30 × AvgRange · target: Touch of K · time: 16:00 ET
- **Parameters:** strike_grid=25 (test 25 (ES); 100 (NQ))
- **Variants (pre-registered):** monthly vs weekly expirations
- **Extra checks:** Development data only; 2024+ protected; Placebo: same rule on non-expiration Fridays and on random strike offsets (e.g., K + 12.5); Pre/post 2022
- **Data needs:** ES/NQ 1-min; Expiration calendar
- **Notes:** Proxy strikes only; real pinning studies use open interest.
