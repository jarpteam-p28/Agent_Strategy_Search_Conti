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
