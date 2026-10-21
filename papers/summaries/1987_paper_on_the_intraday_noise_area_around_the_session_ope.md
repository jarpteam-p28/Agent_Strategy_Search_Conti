# Beat the Market: An Effective Intraday Momentum Strategy for S&P500 ETF (SPY)

**Authors:** Carlo Zarattini, Andrew Aziz, Andrea Barbon  
**Year:** 2024  **Type:** industry  **Read:** full_pdf  
**Source:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4824172

> When SPY moves further from the open than its own 14-day average move at that time of day (a time-varying "Noise Area"), the move tends to keep going into the close; trading it with VWAP/band trailing stops and volatility-targeted size returned about 19.6% a year with a Sharpe of 1.33 in the backtest.

## Findings
- A time-of-day-specific noise band gives a usable trend signal. The band is the open (or prior close if that is further out) plus or minus the average absolute move from the open over the last 14 days, computed separately for each HH:MM. Going long above the band and short below it, checked only on the half-hour, beats buy-and-hold on a risk-adjusted basis. — *SPY 1-min data, May 2007 to Apr 2024. Base version (stop at the opposite band): total return 178%, 6.2% a year, Sharpe 0.61, skew -1.24, worst day -10.3%.*
- A tighter trailing stop turns the base version into a convex trend-follower. The stop is the current band (upper band for longs) combined with VWAP, whichever is nearer. Hit rate falls but skew turns positive. — *Sharpe rises from 0.61 to 1.24, volatility falls from 10.9% to 7.7%, max drawdown from 21% to 12%, hit rate 43%. Trades rise from 5,494 to 7,668. Skew goes from -1.24 to +1.29.*
- Volatility targeting (2% daily, leverage capped at 4x, 14-day realised vol) raises returns a lot. Sharpe barely moves. — *Total return 1,985%, 19.6% a year, volatility 14.3%, Sharpe 1.33, max drawdown 25%, alpha 19.6%, beta about -0.07. Trade-level: 7,668 trades, 37% hit rate, about $0.09 gross per share.*
- Performance is stronger in high-VIX regimes and after recent market declines. Sharpe is roughly 1.5 when VIX at the open is above 6 and about 3.5 when above 40. Yesterday's 5-day RSI has a negative coefficient on strategy return (beta -3.25 bps per RSI point, p=0.001). — *Section 4.1, 4.5. In the 10 worst S&P quarters the strategy was positive every time (Q7 FAQ).*
- Conditioning by daily candle pattern and weekday shows differences. NR4 days have the best average PnL (22 bps, t=5.1, Sharpe 3.2). Triangle and NR7 days are also good. Trend days after a big move and inside/outside days show no edge. Wednesday is best (18 bps, t=3.4). Monday is weakest. — *Tables 5 and 6, 2,620 days in sample. Many patterns were tested, so this is data-mining prone.*
- The result is not very sensitive to the two parameters, and costs are survivable. Volatility multiplier 1.5 gives a Sharpe of about 1.5. A 90-day lookback gives a Sharpe of 1.50, against 1.35 for 14 days. With the I-Star impact model the Sharpe falls from 1.33 to 1.17. — *Figure 9, FAQ Q6, Q14, Q15. Costs used: $0.0035 per share commission and $0.001 slippage (measured on more than 1,000 live market orders). Total return falls toward zero as commission approaches $0.04 per share (Figure 10).*
- The signal appears to carry over to other instruments, according to the authors' FAQs. Liquid ETFs and stocks since 2018 give a diversified Sharpe above 2. On 33 futures markets (2007-2024), only 2 had negative total return, the average Sharpe was 0.60, and the portfolio Sharpe was 1.65. S&P500 index futures had a Sharpe of 1.32 and Nasdaq 1.23. Performance is also reported post-publication (FAQ Q24). — *FAQ Q12, Q13, Q24. These are authors' own unaudited tables. Most contract names are masked.*
- Both legs contribute. The short leg works regardless of VIX level, and filtering shorts to bear markets (below the 100/150/200-day SMA) hurts total return a lot. — *FAQ Q5, Q19-Q21.*

## The WHY
**Pattern:** Execution mechanics of big players, combined with slow information diffusion (under-reaction) and a possible dealer-hedging flow

When price moves further from the open than is typical for that time of day, it signals a buy/sell imbalance too large for liquidity providers to absorb. Large orders are worked gradually, which pushes the move further. Under-reaction to news also contributes (slow-moving capital, limited attention, disposition effect). In negative-gamma conditions, option dealers hedge in the direction of the move and amplify it. That fits the stronger results at high VIX and after a market drop. VWAP is a level that execution algos and institutions benchmark against, so it works as a regime boundary and a natural trailing stop.

- **Who is forced / predictable:** Institutions executing large orders with VWAP/participation algos who cannot fill in one go. Dealers who delta-hedge short-gamma books and must buy rallies and sell dips. Slow-moving capital and mandates that cannot trade intraday or leverage up.
- **Why it persists:** These are structural flows, not a mispricing. The signal uses a very liquid instrument and trend-following has historically decayed less. The authors argue that few institutions can run intraday, high-turnover, leveraged strategies. Post-publication results through early 2025 reportedly remain strong (self-reported). It works across many markets, which supports a generic mechanism.
- **What would kill it:** A fall in volatility and trend days. A shift to dealer long-gamma regimes (heavier 0DTE selling or overwriting). Crowding of the same band/VWAP signal, which would produce fake-outs around the bands. Higher costs or slippage at larger size (the edge is only about $0.09 per share gross). More algos fading breakouts early. Mean reversion becoming the dominant intraday behaviour in SPY.
- **Paper's view vs ours:** The authors lean on generic under-reaction and the Jegadeesh-Titman momentum literature, plus a loose gamma story tested with a crude RSI proxy. They do not test the flow mechanism directly. We think the better WHY is large-order execution plus dealer hedging amplifying imbalances. The Noise Area is a statistical, not causal, definition of imbalance. Their claim that alpha decay is minimal is a claim, not a test.

## Setting
- Markets: US equity (SPY), VIX for regime analysis, FAQ extends to 33 global futures, ETFs and stocks
- Instruments: SPY (S&P 500 ETF)
- Period: May 2007 to April 2024 (updates to Jan 2025 in FAQ)  Frequency: 1-minute OHLCV (IQFeed); decisions on half-hour marks  Holding: Intraday, flat at 16:00 ET close, 1.8 trades a day on average

## Reported results
Intraday momentum on SPY, May 2007 to Apr 2024: 1,985% total return, 19.6% annualised, 14.3% volatility, Sharpe 1.33, max drawdown 25%, net of costs, using vol-targeted size with leverage capped at 4x.
- Unlevered band+VWAP version: 380% total, 9.7% a year, volatility 7.7%, Sharpe 1.24, MDD 12%, hit rate 43%, skew +1.29
- Base version (stop at opposite band): 178% total, Sharpe 0.61, skew -1.24, worst day -10.3%
- SPY buy-and-hold: 227% total, 7.2% a year, volatility 20.2%, Sharpe 0.45, MDD 56%
- Beta about -0.07 against SPY, alpha 19.6% a year
- 7,668 trades, 1.8 trades per day, hit rate 37% by trade, avg $0.09 per share, worst trade -2.9%
- Sharpe with I-Star impact model 1.17; volatility multiplier 1.5 gives Sharpe about 1.55
- FAQ: 2008 +63%, 2018 +61%, 2016 -12.8%, 2017 -6.9%, 2024 +32.2%; authors' updated table to Jan 2025 (self-reported)
- Costs: $0.0035 per share commission (IB entry-level, lower tier on about 20% of days) plus $0.001 per share slippage, estimated from over 1,000 live market orders worth more than $50m. An alternative impact model is also tested in the FAQ.

## Tradable edge (our framing)
Trade SPY (or ES/NQ futures) in the direction of the day once price moves outside the typical time-of-day move from the open. That means a move beyond the 14-day average absolute move from the open at the same clock time, widened by the overnight gap. Decide only at the half-hour marks. Hold until the close, but exit if price comes back to the current band or VWAP, and reverse on the opposite band. The exit is the essential part. It makes payoffs convex (low hit rate of about 40%, big winners). Size by volatility so that every day carries roughly the same risk. The edge is concentrated on trending days. Those days are more common in stressed or falling markets, so it can hedge long equity exposure. Both long and short legs are worth keeping.

## Angles to test
- Run on ES and NQ 1-min bars with fixed 1 contract in development, then volatility-target (e.g. risk fixed dollars divided by recent average move) in live. ES is available 2013-2026.
- Test the long-only and short-only legs separately, because the playbook notes that one side often works better. The paper says both legs help.
- Test band lookback (14 to 90 days) and volatility multiplier (1.0 to 1.5) in-sample only, then run frozen on the last 20%.
- Compare exits: current band + VWAP, VWAP only, opposite band. Confirm the convex payoff (low hit rate, positive skew) holds on futures.
- Add a gamma/regime filter instead of RSI: use realised vol at the open, VIX proxy, or prior-day drawdown to size up on stressed days.
- Use NR4/NR7/Triangle days only to scale size, not as entry filters. Check this in-sample before trusting it.
- Check an event-based version in the style of the gamma study: take only the first band crossing of the day and apply a lockout after the first stop-out to avoid clusters of whipsaws.
- Combine with an opening range breakout or overnight-drift strategy as uncorrelated sleeves, and check the daily P&L correlation. Evaluate as a prop-firm challenge strategy (daily-P&L Monte Carlo).
- Try an overnight-session version: band built from the Globex session opening, which fits the information-while-closed WHY.
- Extend to other liquid futures when data is available (CL, GC, YM, RTY), and to ETFs/stocks. Authors claim it works across assets.

## Decay risk: medium
Published May 2024 (updated Feb 2025). It is built on well-known ideas (opening range breakout, VWAP, momentum) and the authors have a large public following. Their Matlab/Python code and TradingView indicator are free, so many people can run exactly this. Some of the gain comes from compounding at high leverage. Per-share profit is small and sensitive to costs. Much of the equity curve was made in 2008 and 2018, and 2016-2017 were negative years. Authors report positive post-publication performance, but only a short and unaudited sample.

## Data fit
Good for ES: 1-min bars from 2013-12 to 2026, both ETH and RTH, which covers the 9:30-16:00 ET session the paper uses. That gives about 11 years against the paper's 17, so 2007-2013 (including 2008) is missing. NQ 1-min data covers 2021-07 onward, enough for a short test. SPY itself and VIX are not in the inventory. VIX at the open could be proxied by a realised-volatility measure. Everything needed (bands, VWAP, vol targeting) can be computed from OHLCV. There is no data for the multi-asset futures or stock tests (no CL, GC, YM, RTY, stocks). Cost assumptions would need converting from per-share to per-contract (about $13 round turn for NQ per method notes). Careful session handling is needed, because data is in UTC and the paper's clock is ET (watch DST).

## Caveats
- Backtest is from the authors, who sell research/software and are tied to a trading education brand. It is not independently verified.
- The headline 19.6% a year needs up to 4x leverage. The unlevered version has a Sharpe of 1.24 and about 9.7% a year.
- Different versions of the paper report different numbers (Sharpe 1.33 vs 1.35, trade counts 7,668 vs 7,964).
- Several choices were picked after looking at results (VWAP + band stop, vol target, half-hour decisions). Parameter robustness is shown only for lookback and multiplier, with no out-of-sample split.
- The gamma test uses RSI as a proxy and is weak evidence for the mechanism.
- Daily pattern and weekday tables test many conditions, which increases the chance of false positives.
- Per-share profit before costs is only about $0.09. Costs matter, and a more conservative impact model cuts the Sharpe from 1.33 to 1.17.
- Equity curve is uneven: 2016-2017 lost money, and most of the early gain came in 2008-2009.
- The paper's trades check the signal at HH:00 and HH:30 on closes. Fill timing assumptions (next-bar open) need care.
- The multi-market table in the FAQ hides most asset names, so it cannot be checked.

## Cited papers worth reading
- Hedging demand and market intraday momentum (2021)
- Market intraday momentum (2018)
- Understanding intraday momentum strategies (2022)
- Volume Weighted Average Price (VWAP) the holy grail for day trading systems (2023)
- Gamma fragility (2020)
