# Method notes from transcripts

## 02_drift_vwap_pullback_prop_firms.txt — How a Quant Hedge Fund Exploits the Math of Prop Firms

- **Design for the objective, not just for profit.** A strategy can be built to maximize the chance of
  passing a prop-firm challenge rather than long-run profit. A high win rate with a low reward/risk
  (risk 80 to make 40-50) suits challenge rules even when the average trade is too thin for a personal account.
- **Prop-firm pass simulation.** Export the backtest trade list, resample it 20,000 times against the
  firm's rules (profit target, drawdown, daily loss limit, time limit), and report: single-challenge pass
  rate, average days to pass, and probability of passing at least one within N attempts
  (≈ 1 − (1 − p)^N). Treat challenges as a business: cost per attempt vs probability of getting funded.
- **How he builds the prop simulation (from his notebook):** resample whole trading DAYS (daily P&L,
  including zero-trade days) rather than single trades, so intraday guard rails and clustering are kept.
  Walk each simulated challenge day by day: pass when cumulative P&L ≥ target, fail when it breaches the
  drawdown limit (end-of-day for an EOD account), fail on time after the max days. Report pass rate with a
  confidence interval, failure mode split (drawdown vs time), days to pass, average and 95th-percentile max
  drawdown, expected challenges per pass, and a sweep over position size (number of MNQ).
- **Three conditions = level, direction, speed.** A trend filter should say where price is versus a key
  level (above/below VWAP), which way that level is moving (VWAP slope), and how fast price is moving
  (minimum % move over the last hour).
- **Guard rails make a strategy mechanical.** One position at a time, a max number of trades per day,
  stop after N losses in a day, no new entries late in the session, flatten before the close.
- **Let the key level form first.** Skip the first hour (09:30-10:30 ET) so VWAP reflects where real
  volume traded.
- **Split rule used here:** develop on the first half of the data (2020-2024), run frozen on the rest
  (2024-2026). Rising equity in both halves → low chance of overfitting.
- **Optimize only the few parameters that matter, in-sample only** (here: the 0.1% move threshold and
  max trades per day), choosing values that minimize overfitting risk rather than the single best result.
- **Even if trading manually, encode the signal.** Let the code raise the trigger and decide to click
  yourself; otherwise you have no statistics backing the decision.
- **Trust the machine.** After the research is done, don't move stops/targets or add trades by feel.
- **Monte Carlo yardsticks decide when to stop.** If live drawdown over N trades exceeds what the
  simulation gave only a 5% chance of, stop the strategy and investigate.
- **Run a portfolio of 3-4 automated strategies**, for prop firms or your own capital.
- **Institutional job split:** 90% research, development and validation; 10% monitoring risk and performance.

## 03_three_prop_strategies.txt — A Hedge Fund Manager Just CRACKED Prop Trading

- **Run a small portfolio, not one strategy.** Three strategies with daily-P&L correlation below 0.25 on
  one challenge pass more often than any single one (each alone ≈ 40%). His sizing: ~5 MNQ each,
  ≈ 5 trading days to pass on average.
- **Evaluation and funded phases are different problems.** Evaluation: reach the target before the
  drawdown → high win rate, reward/risk below 1, enough trade frequency to finish inside ~20 days.
  Funded: maximize payouts → higher reward/risk strategies (e.g. overnight bias, 3:1) become useful.
- **The prop edge comes from geometry, not edge strength.** These strategies have modest positive
  expectancy; what makes them work in a challenge is win rate, frequency and payoff shape vs the rules.
- **Only run strategies at or near an equity high-water mark.** Losing (and winning) streaks cluster, so a
  strategy in drawdown keeps failing challenges. Bench it; bring it back only when its equity curve makes a
  new all-time high.
- **When to bench:** two failed challenges in a row → investigate; current drawdown above the 75th
  percentile of the Monte Carlo drawdown distribution → bench. (Monte Carlo: export trades from
  MultiCharts, run in Python/Colab.)
- **Don't marry a strategy.** Keep at least three live so a benched one can be replaced.
- **Every strategy spec = WHY + entry + exit (+ sizing, 1 contract while developing).**
- **Low-frequency strategies need care in challenges** — they can run out of time before hitting target or stop.
- **Build custom indicators that draw the rules** so you can check visually that the code does what the rules say.
- **Development split used:** develop 2018-2022, out-of-sample 2023 onward.
- **Volatility-scaled levels:** use a fraction (e.g. 30%) of the 15-session average daily ATR to set
  noise barriers and stops, so levels adapt to the regime; trade-off between the fraction and trade frequency.
- **When the talk and the code disagree, trust the code.** In video 03 he said "one trade per day" for the
  overnight bias strategy, but the code allows up to 4; the VWAP/ADX exit is 15:55 CT (whiteboard), not ET.
  Specs record both and flag the difference.
- **His code hygiene (MultiCharts headers):** state the time zone of every time input, use a 1-minute bar
  magnifier for intrabar fills, document warm-up length (ATR look-back) so early sessions don't trade with
  filters silently off, set realistic costs (~$13 round turn for NQ), and print the IS/OOS stats in the header.
- **His long IS/OOS split for the overnight bias:** in-sample 2006-2019, out-of-sample 2020-2026, zero-cost.

## 04_gamma_exposure_study.txt — Gamma exposure from an Ex Market Maker

- **Test beliefs with one master signal.** To judge an entry idea, hold every trade a fixed time (here
  15 min) with no stop and no target, so the exit can't flatter the entry.
- **Always beat a zero-intelligence baseline.** Measure the same bars with "just own the market" (here:
  always long NQ in 15-min slices = +$4.71/trade). A signal below the baseline is worthless.
- **Events beat states.** "Which side of the level are we on" was a coin flip; "the moment price crosses
  the level" carried the edge. Test the change, not just the state.
- **Continuation first, reversion later.** At gamma levels, every touch/cross continued; faders are early,
  and early means losing. Check the return profile over time after the event to pick the holding period
  (here a second plateau out to ~50 min).
- **Cluster filter.** Signals arrive in clusters; only the first one carries information. A lockout after
  each exit (35 min) nearly doubled the edge.
- **Outlier dependence decides how you trade it.** If the top 20 trades are 90% of profit, you must take every
  signal - automate or don't trade it.
- **Build your own data when the edge depends on it.** He built gamma levels minute by minute from raw 0DTE
  option volume, using only volume traded inside each minute to avoid look-ahead bias.
- **Report the ugly parts:** losing year, worst months, cost drag ($19 round trip), half-by-half and side-by-side results.
