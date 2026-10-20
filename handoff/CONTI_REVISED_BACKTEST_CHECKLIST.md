CONTI REVISED — MASTER BACKTEST VALIDATION CHECKLIST — PASTE AT THE START OF EVERY BACKTEST
==========================================================================================
Revision 2026-10-20 of the family checklist (original: BACKTEST_VALIDATION_CHECKLIST.md, kept unchanged).
Everything from the original is kept. Changes are marked [REVISED]; additions are marked [NEW]. Main additions:
two objectives (PERSONAL ACCOUNT and PROP FIRM) with their own pass bars and verdicts, an N/A rule, a QUICK SCREEN
mode, an optimization protocol (Part O), evaluation windows with an 80/20 split (A3e), a full prop-firm track
(Part P), and a standard results package so every option is shown side by side.

Follow every step in order. Do NOT show me win rates, profits, Monte Carlos, compounding or prop-firm results
until Part A (audit) passes. If any step fails, stop and tell me first, in plain words. A strategy only counts as
REAL if it passes every PASS/FAIL line below.

-----------------------------------------------------------------------------------------------------------------
PART 0 — SETUP (fill this in and get my OK before anything else) [NEW]
-----------------------------------------------------------------------------------------------------------------
0.1 OBJECTIVE — pick one or more. It decides which pass bars and which verdict apply (see HOW TO JUDGE):
      [ ] PERSONAL ACCOUNT  - trade my own money; needs a real edge after costs.
      [ ] PROP EVALUATION   - pass a funded-account challenge (reach the target before the drawdown).
      [ ] PROP FUNDED       - keep a funded account alive and collect payouts.
    If more than one is ticked, report each verdict separately. A strategy can be PROP-VIABLE and still have
    NO EDGE for a personal account (Conti's Drift VWAP Pullback is designed exactly that way).
0.2 MODE:
      [ ] QUICK SCREEN      - is it worth a full test? Runs only: A1, A1b, A1c, A3, A4, A5, A6, A11, A16, A16b,
                              B1, B3, B4, C1, C2b, C4 (short), D1, and P2 (if a prop objective is ticked). Ends with
                              WORTH FULL TEST / DROP. Never a verdict of PROMISING or PROP-VIABLE.
      [ ] FULL VALIDATION   - every step A1 to E7 (plus O and P where they apply).
0.3 STRATEGY CARD (write it out):
      Source (paper / video / own idea), instrument(s), data file(s) and date range, bar sizes, time zone of every
      rule, session window, costs (commission per round turn + slippage in ticks), sizing (headline = 1 contract),
      parameters and where each came from (SOURCE-FIXED = taken from the author unchanged, or TO-OPTIMIZE),
      holdout / protected data, evaluation windows (A3e), prop firm(s) to simulate (P1).
0.4 SOURCE-FAITHFUL FIRST: if the strategy comes from someone else (paper, Conti, a video), the base test is the
    author's rules and numbers EXACTLY, translated only where unavoidable (e.g. another instrument), with every
    translation written down. Any change is a logged variant (A2). Optimize only if I ask (Part O).

-----------------------------------------------------------------------------------------------------------------
DATA [REVISED - real paths and ranges]
-----------------------------------------------------------------------------------------------------------------
Use ONLY my own data on the Lexar drive (mounted as "/Volumes/Lexar Armor 700 Media/"):
- ES 1-minute, longest series: "Backtest Github/data/clean_ES_master.parquet" (2013-12 → 2026-09, UTC per its MANIFEST;
  NinjaTrader contract files 2013-2021 + cleaned series 2021-2026). Copy it into the current project's data/ folder;
  never write into another project's folders.
- ES 1-minute raw contract files: "Pablo backtest data from ninjatrader/ES files/" (2013-12 → 2021-06).
- ES ticks: "Joshua Backtest data copy of drive/2023 june-2021 september/" (2021-06 → 2023-06) and
  "Joshua Backtest data copy of drive/ES BACKTEST , VISUAL STUDIO CODE /".
- NQ ticks: "Joshua Backtest data copy of drive/NQ 2026 september-2021 september/" (2021-07 → 2026-09; front-month
  files 12-21, 03-22, 03-25, 06-25, 09-25 are MISSING).
- Cleaned 1-minute bars: "Joshua Backtest data copy of drive/claude python trading scripts/clean_ES/" and "clean_NQ/".
Never download or substitute other data (no Yahoo Finance, no web data) unless I explicitly ask. TradingView is
allowed only for the A15 reconciliation and B8 spot checks.

-----------------------------------------------------------------------------------------------------------------
NO SKIPPING — WITH A REAL N/A [REVISED]
-----------------------------------------------------------------------------------------------------------------
The final scorecard must list EVERY step ID (0.1 through E7, plus O and P when they apply) with its result.
A step marked "not run" or missing counts as a FAIL until it's done.
N/A is allowed ONLY when the step cannot apply to this strategy, with a one-line written reason that I approve, e.g.:
  - C6b walk-forward OPTIMIZATION when every parameter is SOURCE-FIXED and I did not ask to optimize
    (C7 walk-forward stability still runs);
  - A7 swing points when the strategy uses none; A14/A15 before a live script exists (then they block going live);
  - Part P when no prop objective is ticked.
N/A is never allowed for: any Part A audit that applies, any Part B step, C1, C2/C2b, C4, C5, C6, C9, D1, E2b.

-----------------------------------------------------------------------------------------------------------------
HOW TO JUDGE THE RESULTS (two kinds of checks) [REVISED - per objective]
-----------------------------------------------------------------------------------------------------------------
1) HARD RULES — must ALL pass for EVERY objective, no exceptions. A failure here means a bug or an untradeable
   result; stop and fix it:
   - All of Part A (audit, look-ahead, 0% early fills, independent rebuild, hand checks, live-code parity,
     TradingView reconciliation, reverse test, random-data test, 1-bar signal-delay test, reproducibility)
   - The adversarial final review (E2b) must come back clean
   - All of Part B (data, gaps, rolls, real costs + slippage, strict fills, bot delay)
2) EVIDENCE TESTS — weigh them TOGETHER, don't kill a strategy for one narrow miss:
   - Part C (placebo, sensitivity, concentration, cost stress, holdout, walk-forward, regimes, Deflated Sharpe, PBO,
     sample size, bootstrap, second instrument), Part D (Monte Carlo and stress tests), and Part P for prop objectives.
   - Score each as PASS / NARROW MISS / CLEAR FAIL, with the actual number next to the bar.
   - Where a bar differs by objective, the table in C1 and P10 says which one applies.
3) VERDICTS — one per ticked objective:
   PERSONAL ACCOUNT
     * PROMISING: all hard rules + clearly passes most evidence tests, at most 1-2 narrow misses -> Part E paper trading.
     * NO EDGE: clear fail on placebo, holdout or random-data; OR clear fail on Deflated Sharpe TOGETHER WITH a weak
       or failed holdout. [REVISED: a DSR miss alone with a strong holdout and passing placebo = UNPROVEN, not NO EDGE.]
     * UNPROVEN: several narrow misses because the sample is small -> collect more data or paper trade; don't size up.
   PROP EVALUATION / PROP FUNDED (see Part P)
     * PROP-VIABLE: all hard rules + the P10 bars for that objective + no clear fail on placebo, holdout or
       random-data. A low profit factor is allowed if the prop economics (P3, P6) are clearly positive.
     * PROP-UNPROVEN: hard rules pass, pass-rate / payout numbers positive but uncertain (wide CI, few days, one regime).
     * NOT PROP-VIABLE: expected value per challenge or per funded account is negative, or a clear fail on
       placebo, holdout or random-data.
   - Why: with ~15 statistical tests, even a genuinely real edge fails at least one by chance about half the time.
     Real edges are usually small (+0.1R to +0.2R per trade) and need many trades to prove. Prop strategies can
     work through payoff shape (high win rate, small target, wide stop) rather than a large edge — judge them on
     the challenge economics, never on win rate alone.

-----------------------------------------------------------------------------------------------------------------
PART A — AUDIT FIRST (this is what exposed the fake 77% win rate)
-----------------------------------------------------------------------------------------------------------------
A1. Lock the rules in writing (entry, stop, target, timeframes, session, filters) and get my OK before running.
A1b. Write down WHY the edge should exist (who is on the other side, what behavior it exploits). No reason = extra suspicion.
A1c. Red-flag rule: win rate above 70% at 1:1, profit factor above 3, or a very smooth equity curve = assume a bug
     until a deeper audit proves otherwise. [REVISED note: a high win rate with reward/risk well below 1 (e.g. 65%
     at 0.5:1) is expected from the payoff shape - not a red flag by itself, but still audit fully.]
A2. Keep a log of EVERY variant/parameter tried. This number is needed for the multiple-testing check (C9).
    [REVISED] Evaluation windows (A3e), objectives and reporting views are NOT variants. Every optimization grid
    point (Part O) IS a variant.
A3. Set aside an untouched holdout period BEFORE testing. Never look at it until C6.
A3b. TRAIN-CONFIRM-HOLDOUT PROTOCOL (default process for every strategy, confirmed 2026-10-14):
     split the dev period into two pieces up front -- an EXPLORATION slice (e.g. 2021-2023) and a
     CONFIRMATION slice (e.g. 2024) the exploration never touches -- on top of the separate sealed
     holdout from A3 (e.g. Oct 2025-Sep 2026).
       1. Test ONE pre-chosen favorite variant alone on the exploration slice first (true N=1).
          Passes -> go to step 3. Fails -> go to step 2.
          [REVISED] For a source strategy, the favorite is the author's exact rules (0.4).
       2. Only if step 1 fails: run the full batch/grid of variants (however many) on the SAME
          exploration slice. This is discovery, not validation -- no correction illusion here.
          Take the top candidate(s) forward, carrying the REAL count tried into C9's N. (Use Part O.)
       3. Confirm whatever survived step 1 or 2 on the untouched confirmation slice, using that
          step's real N for DSR/PBO. This is the step that actually filters fakes -- an overfit
          step-2 winner usually falls apart here even if it looked great on the exploration slice.
       4. Only what survives step 3 goes to the sealed A3 holdout, run once, no retuning after.
     Key rule: DSR's N must always equal however many variants were ACTUALLY tried before the
     candidate being evaluated was picked -- a step-1 single-shot test's honesty does NOT transfer
     to a later step-2 big-search winner just because step 1 was tried first.
     This does not make passing more likely in any absolute sense -- most ideas still fail, usually
     at step 3. It makes a pass or fail TRUSTWORTHY, because each step's statistical correction
     matches data that step's search never saw.
A3c. CHUNKED CONFIRMATION (added 2026-10-15; user's preferred way to qualify candidates without spending all the
     real data -- use it by default for every strategy). Step 3 and step 4 of A3b are run in CHUNKS, never all at once:
       1. Fresh data in SECTIONS, newest first (example: 2018-2021 first with ALL finalists; then ONLY the survivors on
          2015-2017; then ONLY the survivors on the oldest section, e.g. Dec 2013-2014). After the last section, compute
          one POOLED verdict over the whole fresh sample (pooled avg R, t, PF, bootstrap, DSR at N = every variant ever
          looked at). If the user asks, also show all finalists on every section "just to see" -- that is descriptive only.
       2. The final untouched data in QUARTERS (example: 2024 Q1, then Q2 ...), for the surviving candidate only. Run one
          quarter at a time and STOP as soon as the candidate fails (INCONSISTENT); remaining quarters and the sealed
          holdout stay untouched.
     Rules for EVERY chunk: (a) write the exact rules, the finalist list and the pass bars into a RULES_<chunk>.md file BEFORE
     loading that chunk; (b) load ONLY that chunk (pyarrow/read-time filter on the date, never read the whole file first);
     (c) run it ONCE, unchanged -- no re-tuning after seeing a result; (d) check the chunk's data first (duplicates, bad bars,
     DST/timezone, holes, contract rolls: force-close at a roll, no FVG across a roll) and print no price levels; (e) trades
     still open at the end of a chunk are NOT counted in the official result (report them separately, marked to the last
     close, information only); (f) report the chunk's result plainly next to the in-sample numbers, with the one-position
     headline AND the overlapping-positions version; (g) only survivors continue, and ask the user before the next chunk;
     (h) a quarter is too small to prove an edge -- score it CONSISTENT / INCONSISTENT against rules written in advance and
     against the candidate's own quarterly history, and rely on the pooled DSR for the formal verdict.
A3d. UNSEEN-DATA RULES (added 2026-10-19; the ES data from 2025 onward is called the "UNSEEN DATA" - always use that name):
     1. GATE: never touch the unseen data (or 2024) unless the user physically says yes AND the strategy has EARNED it by getting through the
        earlier stages (development data, then the fresh older chunks). Never initiate it myself.
     2. REMINDER (say it once, briefly, BEFORE loading 2024 and again BEFORE loading the unseen data): "From here on the strategy must be FINALIZED -
        rules written down, no more tuning - because this is the actual walk-forward / out-of-sample test."
     3. THE THREE CONDITIONS that make an unseen-data result valid: (a) the rules are WRITTEN DOWN BEFORE running (RULES_<period>.md, before any data
        is loaded); (b) each period is run ONCE; (c) NOTHING is changed afterward. If any is broken, say the result no longer counts as out-of-sample.
     4. Run it in pieces, ONE QUARTER (or half) at a time, stopping at the first clear FAIL or at the user's stopping rule. Timestamp-only count of
        trading days per quarter first (no prices) so the user knows what is usable.
     5. Score each piece with a pre-registered battery: avg R > 0; beats the ALWAYS-LONG baseline; positive after 2x slippage and a $35 round trip;
        profit > 0 without the single biggest winner; beats the RANDOM-DAY PLACEBO (200 runs, same time-of-day and stop distance, 95th pct);
        late entry 1-3 min still > 0; >= 20 counted trades. All 7 = ROBUST PASS, >= 5 = PARTIAL, else FAIL; < 20 trades = INSUFFICIENT DATA (no
        conclusion, rules unchanged). Template script: orb_unseen_test.py (verified against earlier runs).
        [REVISED] For a PROP objective add an 8th item: prop pass rate on that piece (P7 rolling challenges) not
        clearly below the in-sample pass rate.
     6. Once the user says yes: run it with NO warnings or lectures, ONE short reminder line that the data is important and is now used, and ONE line
        saying whether the strategy was chosen on that data or not. Independent audit agents confirm the numbers are real (correctness); an unseen test
        of a pre-registered, run-once, unchanged strategy is valid out-of-sample evidence for THAT strategy; its only cost is that the data can no longer
        be a clean final exam for a LATER strategy.
     7. Every result shown: also without the top 5% and 10% of winners (see C4), always-long/always-short baselines, long vs short, and the day-trade
        (flat at 16:00) version of the same signals.
A3e. EVALUATION WINDOWS + 80/20 (Conti's split) [NEW]. Report the locked rules on these REPORTING VIEWS (not variants):
     1. SOURCE WINDOW: the exact period the author tested (e.g. Conti Vault Break NQ 2022-01 → 2026-09), with the author's own
        in-sample / out-of-sample split if known.
     2. FULL HISTORY: all usable data (ES 2014-01 → end).
     3. Each window split CHRONOLOGICALLY 80/20: in-sample = first ~80% of the window, out-of-sample = last ~20%.
        (ES full history: in-sample 2014-01 → 2023-12, out-of-sample 2024-01 → end, which is the protected 2024 + UNSEEN DATA.)
     4. Show in-sample and out-of-sample side by side (trades, win rate, avg trade, PF, net $, max DD, with and without the
        top 5%/10% winners) and the ratio out-of-sample avg / in-sample avg (ideally above 0.5).
     5. Any out-of-sample slice inside protected data follows A3d exactly (written first, run once, quarter by quarter, my yes).
     6. When every parameter is SOURCE-FIXED, in-sample vs out-of-sample checks CONSISTENCY, not our own overfitting; say so.
A4. Timestamps: prove whether each bar is stamped at its OPEN or CLOSE, for every timeframe used.
    [REVISED] If a series mixes conventions (e.g. a seam between data sources), prove the seam with the opening-volume
    bar on days either side, normalize into a NEW file (keep the original), and re-check the seam for duplicate/missing minutes.
    Match the convention the strategy's author used (MultiCharts / NinjaTrader = close-stamped).
A5. Look-ahead check: for every value used (candle high/low/close, wick, FVG, order block, rejection block, swing
    point, level, indicator), state the exact moment it's known in real time. Nothing may be used before then.
A5b. Indicator traps (common in AI-written code): no zero-phase / two-way filters (scipy filtfilt — use a one-way
     filter like lfilter), no centered rolling windows (center=True), no scaling/normalizing/z-scores using the
     whole dataset's mean or std, no pandas shift(-1) or anything that reads a later row, no "fit on everything" ML.
     Every indicator value at time t must be computable using only data up to t.
A6. Entries only after the signal candle CLOSES. No fills inside the candle that creates the entry price.
    PASS/FAIL: report % of trades filled before the signal was fully known. Must be 0%.
A7. Swing highs/lows with K candles each side only count after the K right-hand candles have CLOSED.
A8. "Level broken / zone invalidated" only counts when the breaking candle CLOSES (not at its open).
A9. Higher-timeframe data on a lower chart: only use the last CLOSED higher-timeframe candle (no repainting).
A10. Daily selections (e.g. at 9:30) use only candles fully closed by that time.
A11. Same-bar ambiguity: if a bar touches both stop and target, count the STOP. If the fill bar also touches the
     target, do not count it as a win. [REVISED] Where tick data exists, MEASURE how often it happens and its effect
     (diagnostic only, not a variant).
A12. Independent rebuild: a separate agent rebuilds the strategy from the written rules without reusing the code.
     PASS/FAIL: setups and trades must match; every difference explained.
A13. Hand-check 5 trades minute by minute (setup candle, entry price, fill time, exit time and price).
A14. Live-code parity: compare the live script (Pine/bot) to the backtest line by line — session window, candle
     alignment (TradingView 4H starts 6 PM ET), one-position-at-a-time vs overlapping trades, order types. List
     every difference.
A15. Third-engine check: run the live script in TradingView's Strategy Tester over a period both cover and
     reconcile trade by trade with the Python backtest. PASS/FAIL: same trades and similar win rate.
     [REVISED] TradingView intraday history is short - reconcile on the overlapping recent months and say how many.
A16. Reverse test: flip every trade to the opposite side. It must LOSE about what the original makes (minus costs).
     If both directions win, something is broken.
A16b. Random-data test: run the exact strategy on synthetic random-walk price data (same volatility, no pattern).
      PASS/FAIL: must show NO edge. Profit on random data = guaranteed bug (usually look-ahead).
A16c. Signal-delay test: delay every signal by one full bar of its own timeframe. A real edge weakens gradually;
      an edge that collapses almost entirely after a 1-bar delay was likely using information too early.
A17. Reproducibility: save the code version, settings, random seeds and full trade list so any result can be re-run exactly.

-----------------------------------------------------------------------------------------------------------------
PART B — DATA AND EXECUTION REALISM
-----------------------------------------------------------------------------------------------------------------
B1. Data check: duplicates, bad ticks, missing minutes, timezone and daylight-saving handling, holidays/half days.
B2. List every data gap. No zone/swing/trade may be built across a gap.
B3. Contract rolls: is the series back-adjusted? Count trades open across a roll and check roll price jumps.
B4. Costs: real commission + at least 1 tick slippage on market entries and stop exits.
B5. Strict fills: price must trade 1 and 2 ticks THROUGH a limit to fill. PASS/FAIL: still profitable at 1 tick.
B6. Overnight/weekend gaps: stops filled at the gap price, not the stop price.
B7. Position limits: overlapping trades and max contracts the market and account can really hold; margin.
B8. Second data source: spot-check prices and a sample of signals against another feed (e.g. TradingView vs tick files).
B9. Alert/bot delay: measure the real delay from signal to order (webhook, broker) and re-run with that delay added.
B10. Overfitting check: count the rules/filters vs the number of trades. Many filters on few trades = likely curve-fit.

-----------------------------------------------------------------------------------------------------------------
PART O — OPTIMIZATION (only when I ask, or when A3b step 2 is reached) [NEW]
-----------------------------------------------------------------------------------------------------------------
O1. Write the grid BEFORE running (RULES_optimization.md): which dials (at most 3), the exact values for each, the
    data slice (exploration slice only), and ONE objective metric chosen in advance:
      PERSONAL -> avg R after costs (or PF after costs);  PROP EVALUATION -> P2 pass rate;  PROP FUNDED -> P6 expected payouts.
    Prefer dials the author also optimized (e.g. Conti: noise %, max trades/day, minimum move).
O2. Run every grid point on the exploration slice only. No confirmation, protected or unseen data.
O3. Output the full table (every grid point: trades, win rate, avg trade, PF, net $, max DD, objective metric) and a
    heat map for each pair of dials.
O4. PICK A PLATEAU, NOT A PEAK: choose the setting at the centre of the best region whose neighbours are all within
    ~10-20% of it. A lone spike with poor neighbours = luck; say so and do not pick it.
O5. Count every grid point into A2 / C9's N, and feed the grid to C9b (PBO).
O6. Freeze the chosen setting, write it down, then continue with A3b step 3 (confirmation slice) and A3c / A3d.
O7. Walk-forward optimization (C6b) re-uses this same grid and objective on each training window.
O8. Always show the SOURCE-FIXED (author's) setting next to the optimized one, on every slice, so I can see what
    optimizing actually bought.

-----------------------------------------------------------------------------------------------------------------
PART C — VALIDATION TESTS (only after Parts A and B pass)
-----------------------------------------------------------------------------------------------------------------
C1. Headline: trades, win rate vs break-even win rate, avg R/trade, total R, profit factor, net $, max drawdown
    ($ and R), longest losing streak, losing months, best/worst month, year-by-year. All net of costs.
    PASS/FAIL [REVISED - by objective]:
      PERSONAL ACCOUNT : at least 300 trades; profit factor at least 1.3 after costs.
      PROP (either)    : at least 300 trades; profit factor at least 1.05 after costs AND still positive after 2x
                         slippage (C5); the real bar is in Part P (P10).
C2. Placebo: same days, same stop/target, RANDOM entry times AND RANDOM direction (100+ runs). Also report a
    same-direction version, but don't judge on it (random entries in the setup's direction can be biased).
    PASS/FAIL: the real strategy beats at least 95 of 100 random-direction runs.
    [REVISED] For PROP, also run the placebo through P2: the real strategy's pass rate must beat the 95th percentile
    of random-entry pass rates with the same stop/target/time rules (payoff shape alone can pass challenges).
C2b. DRIFT CHECK FIRST (added 2026-10-19; do this BEFORE detailed testing): compare with (i) ALWAYS-LONG and ALWAYS-SHORT using the same entry bars, stop
     distance and target, (ii) the RANDOM-DAY placebo (same time-of-day and stop distance, random day), (iii) buy-and-hold scaled to the strategy's average
     exposure, (iv) the same signals as a DAY TRADE (flat at the close). If the profit is about what the passive exposure earns, call it "drift, no edge".
     Define "long-only" honestly: a filtered subset of a both-sides stacked stream is NOT a standalone long-only run; also run the true long-only version.
C3. Parameter sensitivity: nudge every setting (threshold +/-1, R-multiple +/-0.5, stop size, distances).
    PASS/FAIL: performance degrades gradually, no single sharp peak.
C4. Trade concentration: % of profit from the top 5% and top 10% of trades; result without the best 5/10 months.
    PASS/FAIL (only for strategies with variable-size wins, e.g. trailing stops): still profitable without the top
    10% of trades. For fixed-target strategies the top 10% are all identical full winners, so report it as a NOTE
    and judge concentration by best months instead (still profitable without the best 5 months).
    ALWAYS REPORT (added 2026-10-14, every backtest, no need to ask): the total after removing the top 5% and top 10%
    of WINNING trades (in R and dollars, flat 1 contract), the same count of RANDOM trades removed for comparison,
    the number of winners needed to wipe out all profit, and the same removals under compounding / fixed-risk-%
    sizing. State which sizing every number uses. Reusable helper: concentration_check.py in the scripts folder.
    BREAKDOWN POINT (added 2026-10-15, user request, every backtest): keep removing winners, biggest first, and report
    the total after removing 5/10/15/20/25/30% of winners AND the % of winners at which total profit hits zero.
    Reading: breakdown at 25%+ of winners = robust; 10-25% = mixed; under 10% = fragile (a strategy that falls
    apart at ~5% is far more suspicious than one that only turns negative after losing 25%+). Note that for fixed-R
    targets every winner is about the same size, so also compare with the mechanical drag (a zero-edge strategy loses
    about the same R from the removal). concentration_report() prints this automatically.
    EVERY-STAT RULE (user, 2026-10-19): with EVERY performance number shown (any table row, variant, period, side, quarter) also show it without the top 5%
    and top 10% of winners (R and $, number of trades removed, winners to zero), plus removing the same count of RANDOM trades. Reason: if a couple of trades
    make a strategy, missing them in real life loses money. State the sizing (flat 1 contract) with every number.
C5. Cost stress: 2x and 3x slippage, plus $35 and $50 round-trip commissions. Report how much edge survives.
C6. Out-of-sample holdout: run the locked rules unchanged on the holdout from A3. Compare to in-sample.
    PASS/FAIL: holdout profitable after costs and not significantly worse than in-sample. No re-tuning after.
C6b. Walk-forward OPTIMIZATION: on each rolling window, pick the settings using ONLY the past training months,
     then trade those settings on the next unseen test months; roll forward by the test length and repeat across all
     data. Stitch the test months together and report them as the real result. [REVISED] Uses the Part O grid and
     objective. N/A (with reason) when every parameter is SOURCE-FIXED and I did not ask to optimize.
     DEFAULT FOR MY ES DATA [REVISED]: full history 2014-01 → 2026-09. Development 2014-01 → 2023-12, walk-forward
     12-month train / 3-month test, rolling 3 months, inside development; 2024 = confirmation (protected), 2025+ =
     UNSEEN DATA, final holdout Oct 2025 - Sep 2026 run ONCE at the very end. For a strategy that only uses the
     2021+ series, the old default applies: development Jun 2021 - Jun 2025, same holdout (data hole Jul-Oct 2025 skipped).
     Window sizes by data length:
       - 3+ years of data: train 12 months / test 3 months.
       - About 1.5 years (18 months): train 6 months / test 2 months, rolling -> about 6 test windows = 12 unseen
         months. Also run an "anchored" version (training always starts at the first month and grows).
       - Under 1 year: not enough for walk-forward; say so and rely on paper trading.
     Each test window should have at least ~20 trades; if not, lengthen the test window and say so.
     Note: with only 1.5 years, all results are low-confidence by nature — more data or forward testing is needed.
     PASS/FAIL: stitched out-of-sample result profitable after costs, and not far worse than the in-sample windows
     (walk-forward efficiency = out-of-sample avg / in-sample avg, ideally above 0.5).
C6c. INDEPENDENT HOLDOUT VERIFICATION (added 2026-10-12): after the one holdout run, launch a separate agent that did
     NOT run it. Give it the locked rules, the data paths and the saved trade list. It must (1) rebuild the holdout trades
     itself from the raw price files with its own plain code (not the backtest engine), (2) check that every trade in the
     list exists: entry bar, entry price, stop, target, exit bar, exit price, dollars, (3) check that no trade is missing
     or invented (scan every night in the holdout window for signals), and (4) recompute the totals (profit, % return,
     drawdown, profit without the best trade). PASS = identical trade list and totals. Report its findings unedited next
     to the holdout result. This proves the holdout numbers are REAL; it does not make the data unseen again.
     Also record in the scorecard when the holdout was used and for which strategy; for later strategies, treat the same
     slice as "used once" (lower weight) and prefer data that did not exist when the strategy was designed.
C7. Walk-forward stability: split into quarters and years; rolling 100-trade and 12-month windows.
    PASS/FAIL: most quarters profitable; no rolling 12-month window deeply negative.
C8. Regime segmentation: trending vs choppy, high vs low volatility, long vs short, setup type, time of day, day of
    week, FOMC/CPI days (official dates). Report where the money actually comes from.
C9. Multiple-testing correction: Deflated Sharpe Ratio using the REAL variant count from A2.
    PASS/FAIL: at least 0.95. [REVISED] Evidence test: a miss weighs heavily but is decided together with the
    holdout and placebo (see VERDICTS).
C9b. Probability of Backtest Overfitting (PBO): split the data into many chunks and check how often the best variant
     in-sample turns out below median out-of-sample. PASS/FAIL: PBO below 20%. [REVISED] Uses the Part O grid;
     N/A (with reason) when only one SOURCE-FIXED configuration exists.
C9c. Sample-size check: calculate how many trades are needed to tell the claimed edge apart from break-even (95%
     confidence). PASS/FAIL: the backtest AND the holdout each have at least that many trades.
C9d. Purged cross-validation: when splitting into train/test periods, drop trades that overlap the boundary (plus a
     short gap) so a trade can't leak information across the split.
C10. Bootstrap: 95% confidence ranges (single trades and 15-trade blocks) for avg R and total R.
     PASS/FAIL: lower bound of avg R above 0.
C11. Second instrument (e.g. NQ for ES): identical rules, sizes scaled by a rule fixed BEFORE seeing results.
     PASS/FAIL: still profitable after costs. [REVISED] If the second instrument's data has holes (e.g. NQ front
     months missing), use only complete months and say how many.

-----------------------------------------------------------------------------------------------------------------
PART D — MONTE CARLO AND STRESS TESTS
-----------------------------------------------------------------------------------------------------------------
D1. Trade-sequence resampling: reshuffle trade order 10,000 times; drawdown distribution (median/95th/worst),
    losing-streak distribution, recovery time. [REVISED] QUICK SCREEN uses D1 only; FULL VALIDATION uses D1b.
D1b. MONTE CARLO RESAMPLING (added 2026-10-19): run 100,000 simulations by (a) reshuffle, (b) bootstrap with replacement, (c) BLOCK bootstrap (blocks of 10
     trades; the most realistic, keeps streaks). Report % of runs ending below the start, % blown ($0), deepest drawdown (median/95th/worst, in $ and % of the
     account), lowest balance reached, and the profit distribution (worst, median, best, where the middle 50%/80% land; and separately for runs that end above
     the start). Run it on the full list AND without the top 5% and 10% of winners AND on the window that excludes the selection period. For position-size
     questions run 1-5% risk per trade (compounding, micro-contract sizing) and check margin: contracts x current margin vs the account.
D2. Monte Carlo with entry-timing / parameter noise: random small delays and price noise on every entry (enter 0-5
    minutes late at market) to see if the logic is fragile.
D3. Equity-high stress table: effect of 1-10 losses in a row at each account size.
D4. Prop-firm sims -> now fully specified in PART P [REVISED]. Keep the original warning:
     D4 WARNING (2026-10-19): prop-firm evaluations require positions to be FLAT at the daily close (verify on the firm's rule page and record the date); a
     strategy that holds trades for days cannot be simulated there. Closed-trade equity is optimistic; monthly start dates overlap (one path).
D5. Compounding: always show a capped, realistic version (max contracts the market can fill). Uncapped
    compounding is a math demo only, never a forecast.

-----------------------------------------------------------------------------------------------------------------
PART P — PROP-FIRM TRACK (required when PROP EVALUATION or PROP FUNDED is ticked in 0.1) [NEW]
-----------------------------------------------------------------------------------------------------------------
P1. RULES, CHECKED ONLINE: for each firm/account write down, with the date checked and the page: account size, profit
    target, drawdown type (end-of-day / intraday trailing / static) and size, daily loss limit, minimum trading days,
    maximum days (if any), consistency rule, max contracts, flat-by-close / news rules, whether automation (bots) is
    allowed, evaluation fee, activation fee, payout rules (buffer, minimum days, split, caps, consistency).
    Default comparison account (Conti's notebook): 50K, END-OF-DAY drawdown -$2,500, target +$3,000, 20 trading days.
P2. PASS-RATE MONTE CARLO (Conti's method): bootstrap WHOLE TRADING DAYS (daily P&L, including zero-trade days) 20,000
    times; walk each simulated challenge day by day: PASS when equity >= target, FAIL when the drawdown rule is broken,
    FAIL on time at the day limit. For INTRADAY trailing drawdown use each day's worst intraday equity (open-trade
    low point), not the close. Also run a BLOCK bootstrap (5-day blocks) to keep streaks.
P3. REPORT: pass rate with 95% confidence range; failure split (drawdown / daily loss / time); median and average days
    to pass; average and 95th-percentile max drawdown during the challenge; expected challenges per pass (1 / pass
    rate); probability of at least one pass in 1, 2, 3, 4 attempts; COST PER FUNDED ACCOUNT = fees / pass rate.
P4. SIZE SWEEP: repeat P2 for 1 to N micro contracts (e.g. 1-20 MES / MNQ) and show pass rate and days to pass for each.
    Pick a size from the plateau, not the single best.
P5. PORTFOLIO: if several strategies run on one account, simulate them together on the same days (daily P&L summed),
    report their daily-P&L correlation (E7) and the combined pass rate vs each alone.
P6. FUNDED PHASE: simulate the funded account with the payout rules: probability of reaching the first payout before
    breaching, expected number and size of payouts, expected life of the account, EXPECTED VALUE PER FUNDED ACCOUNT
    = expected payouts - activation/monthly fees.
P7. ROLLING HISTORICAL CHALLENGES (real order, no resampling): start a challenge on EVERY trading day in the data and
    run it forward with the real sequence. Report the pass rate by year and by quarter - is it only one regime?
    (Real order is one path; overlapping starts are not independent - say so.)
P8. PLACEBO FOR PROP: the C2 random-entry placebo pushed through P2 with the same stop/target/time rules. The strategy's
    pass rate must beat the 95th percentile of the placebo pass rates; otherwise the payoff shape alone is passing.
P9. BENCH RULES (Conti): bench a strategy when its current drawdown is above the 75th percentile of the Monte Carlo
    drawdown, or after 2 failed challenges in a row; bring it back only at a new equity high. Write these as numbers.
P10. PROP PASS BARS (write the numbers in 0.3 before running; defaults below):
     PROP EVALUATION: P2 pass rate lower 95% bound >= 35% AND beats the P8 placebo AND expected value per challenge
       > 0, where EV = pass rate x (P6 expected value per funded account) - evaluation fee AND P7 pass rate not near
       zero in any full year.
     PROP FUNDED: P6 expected value per funded account > 0 with probability of a first payout >= 50%.
     Hard rules (Parts A, B, E2b) still apply in full.

-----------------------------------------------------------------------------------------------------------------
PART R — STANDARD RESULTS PACKAGE (so every option is visible) [NEW]
-----------------------------------------------------------------------------------------------------------------
R1. One results folder per strategy run: rules file, code version, settings, seed, trade list (CSV), daily P&L (CSV).
R2. RESULTS_SUMMARY.md with ONE comparison table: rows = base (author's exact rules), every logged variant, every
    optimized setting (Part O); column groups = evaluation windows (A3e: source window / full history, each in-sample and
    out-of-sample); for each cell: trades, win rate, avg trade $, PF, net $, max DD, and without top 5% / 10% winners.
R3. A second table per objective: PERSONAL (C1, C9, C10 key numbers) and PROP (P3 pass rate + CI, days to pass, cost per
    funded account, EV) for every row of R2.
R4. Charts: equity curve with in-sample / out-of-sample shading, drawdown curve, Monte Carlo fan, prop pass-rate by
    size (P4), rolling-challenge pass rate by year (P7), optimization heat maps (O3).
R5. The one-page scorecard (E2c) at the top, with the verdict for EACH objective ticked in 0.1.

-----------------------------------------------------------------------------------------------------------------
PART E — VERDICT
-----------------------------------------------------------------------------------------------------------------
E1. Lead with the bad news if the edge is gone. Show the before-audit vs after-audit numbers side by side.
E2. Give an honest confidence level and a scorecard: every hard rule (PASS/FAIL) and every evidence test
    (PASS / NARROW MISS / CLEAR FAIL / N/A with reason, with the number), then the verdict for EACH objective:
    PERSONAL: PROMISING / UNPROVEN / NO EDGE;  PROP: PROP-VIABLE / PROP-UNPROVEN / NOT PROP-VIABLE.
E2b. ADVERSARIAL FINAL REVIEW (required, hard rule): after the scorecard, launch a separate agent that did NOT run the
     backtest. Give it the written rules, the code, the data paths and the results, and one job: try to prove the
     edge is FAKE — hunt for look-ahead, bugs, data problems, overfitting, unrealistic fills/costs, and anything the
     scorecard got wrong. It must re-run at least the key numbers itself. Report its findings to me unedited, next to
     the scorecard. If it finds a real problem: fix it, re-run, and repeat the review. No verdict of PROMISING or
     PROP-VIABLE until a review comes back clean. [REVISED] For PROP it also re-runs P2 independently.
E2c. FINAL REVIEW PACKAGE (added 2026-10-19): (1) an INDEPENDENT AUDIT agent rebuilds the trades from raw data + the written rules WITHOUT reading the original code and
     compares every reported number (per chunk and per window; state the chunk/stacking/hole conventions explicitly; true timestamps for concurrency, not row
     indices); (2) a FRESH ADVERSARIAL REVIEW agent attacks the exact version to be traded (look-ahead, selection bias, walk-forward purging by EXIT time, hindsight
     candidate sets, DSR with the real variance, prop/margin modelling); (3) ONE-PAGE FINAL SCORECARD listing every step 0.1-E7; (4) a written kill-switch rule (E4).
     Walk-forward: purge training trades by EXIT time, fix the candidate list before looking, compare with buy-and-hold per unit of exposure.
E3. Real money only after 3-6 months of forward paper trading that matches the backtest. [REVISED] For PROP: paper
    trade or run on a demo of the same firm's platform with the same automation (B9) before paying for evaluations.
E4. Write the kill switch BEFORE going live: stop trading if drawdown exceeds the Monte Carlo 95th-percentile
    drawdown, or if the live win rate after 50+ trades falls below the backtest's 95% confidence range.
    [REVISED] For PROP add the P9 bench rules.
E5. Live tracking: log every live trade next to what the backtest says should have happened that day; review monthly.
E6. Scale slowly: paper -> 1 micro contract -> larger size, only while live results stay inside the backtest's ranges.
E7. If running more than one strategy, check how correlated they are so they don't all lose on the same days.
