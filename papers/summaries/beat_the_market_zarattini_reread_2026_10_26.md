# Beat the Market: An Effective Intraday Momentum Strategy for S&P500 ETF (SPY)

**Authors:** Carlo Zarattini, Andrew Aziz, Andrea Barbon  
**Year:** 2024  **Type:** academic  **Read:** full_pdf  
**Source:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4824172

> When SPY moves further from the open than its typical 14-day move at that time of day, it tends to keep going into the close, and a long/short strategy trading that with VWAP/band trailing stops and volatility-targeted size shows a net Sharpe of 1.33 over 2007–2024.

## Findings
- Base model: compute a time-of-day-specific 'Noise Area' around the open (widened by the overnight gap) from the average absolute move-from-open over the last 14 days. Go long above it and short below it, checking only on the half-hour. Exit at the close or on a cross of the opposite band. This gives a total return of 178% and a Sharpe of 0.61, about the same as buy-and-hold (SPY 227%, Sharpe 0.45). It has negative skew and a worst day of -10.3%. — *SPY 1-min data (IQFeed), May 2007–Apr 2024; commission $0.0035/share + $0.001 slippage; Table 1*
- Replacing the opposite-band stop with a tighter trailing stop at max(current band, VWAP) for longs (min for shorts) doubles the Sharpe. Skew turns positive, the worst day improves from -10.3% to -4.8%, and the hit rate falls to 43%. Trades rise from 5,494 to 7,668. — *Table 2: IRR 9.7%, vol 7.7%, Sharpe 1.24, MDD 12%, alpha 9.9%, beta -0.03. A later FAQ shows a VWAP-only stop is worse (Sharpe 1.17 vs 1.35).*
- Volatility-targeted sizing (2% daily target on 14-day SPY vol, leverage capped at 4x) lifts return to 19.6% a year, vol 14.3%, Sharpe 1.33, max drawdown 25%. The paper reports alpha vs SPY of 19.6% a year with beta of about -0.07. — *Table 3; total return 1,985%. The Sharpe falls to 1.17 under the Kissell I-Star impact model (FAQ Q15).*
- The edge is larger when VIX is higher. Sharpe is about 1.5 for VIX above 6 and about 3.5 for VIX above 40. The strategy made money in all 10 of the S&P's worst quarters. — *Fig 8; FAQ Q7 (e.g. Q4 2008 +16% vs -22%, Q1 2020 +7%, Q4 2018 +31%)*
- The edge is bigger after narrow-range days (NR4: 22 bps/day, t=5.1; NR7: 16 bps; Triangle: 14 bps). Inside/outside days and trend days show no significant edge. Wednesday has the best day-of-week result (18 bps, t=3.4). Monday is weak. — *Tables 5 and 6; 2,620 trading days. Only the unconditional result is the headline; the subsets are data-mined.*
- A higher 5-day RSI at the prior close predicts lower strategy returns (beta -3.25 bps per RSI point, p=0.001). The authors read this as a proxy for dealer long-gamma (mean-reverting) versus short-gamma (trend-amplifying) regimes. — *Section 4.5 regression of daily strategy return on lagged RSI(5); this is only an RSI proxy, not real gamma data.*
- The parameters are not tightly tuned. Sharpe is flat across lookbacks of 5–90 days (1.23–1.50). A volatility multiplier of about 1.5 is best (Sharpe about 1.5), and returns fall at very high multipliers. Long and short legs both contribute, and shorting only in bear markets or high-VIX conditions hurts. — *Fig 9; FAQ Q6, Q14, Q19–Q21*
- The same rules work on other ETFs, single stocks and 33 futures markets. Only 2 of 33 futures lost money, the average Sharpe was 0.60, and the diversified portfolio had a Sharpe of 1.65 (S&P 500 index 1.32, Nasdaq 1.23). Post-publication results (to Jan 2025) are reported as still positive (2024: +32%). — *FAQ Q12, Q13, Q24. These are author-reported, with no costs detailed for the futures.*
- Intraday trend returns accumulate mostly from 10:00 to noon and from 14:00 to the close, with a pause at lunch. — *FAQ Q18 chart*

## The WHY
**Pattern:** Mix: slow information diffusion / under-reaction, plus execution mechanics of big players (dealer delta-hedging and institutional order-splitting)

Imbalances between buyers and sellers are sticky. When price leaves the range it normally covers by that time of day, it signals an abnormal flow. This comes from overnight news and gaps, large institutions that cannot fill in one go and so spread orders through the day, and dealers who are short gamma and must buy into rallies and sell into dips. The imbalance is absorbed slowly, so the move continues into the close. The edge is stronger on high-VIX days and after sell-offs (low RSI), which fits the short-gamma story. Trailing stops at VWAP and the band cut off the days when a trend fails and reverses.

- **Who is forced / predictable:** Options dealers who delta-hedge (when short gamma they trade with the move). Institutional desks working large parent orders via VWAP-type algos over the day. Fund mandates and slow-moving capital that can't react at once. Late-day rebalancers (levered ETFs, hedgers) add to the move into the close.
- **Why it persists:** These flows come from structural constraints (dealer hedging, order-slicing, mandates), not from an anomaly that can be arbitraged away. SPY and ES are very liquid, so the trade can be done at scale. The strategy keeps working across other instruments, which points to a general mechanism. Gao et al. found that intraday momentum weakened after 2013, and the paper's own average profit per share before 2018 was close to zero, so the edge is regime-dependent and not constant.
- **What would kill it:** A drop in intraday volatility and trend days (a permanently calm, mean-reverting market). Dealers moving structurally to long gamma, for example through very heavy call overwriting or 0DTE flows that dampen intraday moves. Faster absorption of imbalances because so many traders use the same noise-band and VWAP rules. Higher slippage once sized up. Note that the 2016–2017 losses (-12.8%, -6.9%) came in quiet, low-VIX years.
- **Paper's view vs ours:** The authors cite under-reaction to news (disposition effect, inattention, slow-moving capital) and a gamma-hedging link, but the gamma link is only tested with a crude RSI proxy. They say alpha decay is minimal because momentum decays less after publication, which is asserted and not tested. The dealer-hedging and order-splitting explanation is the more defensible one, and it tells us to condition on volatility and gamma regime.

## Setting
- Markets: US equities (SPY), US equity index and commodity futures (FAQ only)
- Instruments: SPY, VIX (for regime tests), QQQ, single stocks, 33 futures (FAQ only)
- Period: May 2007 – April 2024 (FAQ updates to Jan 2025)  Frequency: 1-minute OHLCV bars (IQFeed); decisions at HH:00 and HH:30  Holding: Intraday: enter after 10:00 ET on a band break, exit at the 16:00 close or on a stop

## Reported results
Net of costs: 19.6% annualised return, Sharpe 1.33, max drawdown 25%, 1,985% total return, alpha 19.6% a year with beta -0.07, on SPY 2007–Apr 2024 (vs buy-and-hold Sharpe 0.45).
- Base model with opposite-band stop: Sharpe 0.61, 178% total return, worst day -10.3%
- With band+VWAP stop at 100% size: Sharpe 1.24, IRR 9.7%, vol 7.7%, MDD 12%, hit ratio 43%
- With vol-targeting (2% daily target, max 4x): Sharpe 1.33, IRR 19.6%, vol 14.3%, MDD 25%
- 7,668 trades over 17 years (about 1.8 per traded day); avg PnL $0.09 per share; trade hit ratio 37%
- Sharpe 1.17 with Kissell I-Star impact model; alpha still above 15% (FAQ Q15)
- Sharpe about 3.5 on days with VIX above 40; 10 of 10 worst S&P quarters positive
- Futures: average Sharpe 0.60 across 33 markets, portfolio Sharpe 1.65; S&P 500 index 1.32, Nasdaq 1.23
- 2024: +32.2% (self-reported post-publication)
- Costs: Yes: $0.0035/share commission (IB entry tier) and $0.001/share slippage from a live test of 1,000+ market orders on SPY. Sensitivity chart shows the return falls quickly as commission rises. Alternative impact model reduces Sharpe from 1.33 to 1.17.

## Tradable edge (our framing)
Trade the intraday trend only when price leaves a time-of-day-specific noise band, which is the average move from the open over the same period on recent days, widened by the overnight gap. We read an exit from the band as evidence of a real flow imbalance, either dealers hedging with the move or institutions still working orders. Enter in the direction of the break on a half-hour check. Hold to the close. Exit early if price falls back through the band or VWAP, which keeps the right tail and cuts reversal days. Size by volatility so risk per day is constant. The trade is long and short, and is most useful in volatile or stressed regimes, where it also offsets long equity exposure. Quiet, low-VIX regimes are the weak spot.

## Angles to test
- ES futures (we have 1-min data from 2013): build the bands from the 09:30 ET RTH open. Test with $12–13 round-turn costs, 1 contract in development, then volatility-targeted sizing live. This directly tests whether the edge survives on futures.
- NQ 1-min (2021–2026 only): same rules; the Nasdaq result in the futures table (Sharpe 1.23) is the second strongest equity index.
- Different session: build the bands on the overnight/Globex session, or on a London/Europe open, and trade continuation. The same sticky-imbalance logic applies.
- Long-only version: the shorts add diversification but have lower payoff in bull years. Test whether long-only ES keeps most of the edge, and long-only above the band only when VIX is above a threshold.
- Regime filters (in-sample only): lagged RSI(5) below 50 or a VIX floor to proxy short-gamma. Also NR4/NR7 day filters, which are data-mined, so treat them cautiously. Compare against an actual gamma or VIX-term-structure filter, since we could build GEX-style levels from our data.
- Combine with the VWAP-pullback, ORB, and overnight bias strategies from other papers and check daily-P&L correlation (below 0.25 is the target). This one is a trend/breakout type with negative market beta.
- Prop-firm application: the hit rate of about 43% with a positive-skew payoff doesn't suit evaluation geometry on its own. Test the Monte Carlo pass rate by resampling days; it may be better in the funded phase.
- Parameter ranges to test in-sample: lookback 10–90 days, volatility multiplier 0.8–1.5, decision interval 15 vs 30 min, stop = band/VWAP/both, vol target 1–2%.

## Decay risk: medium
The paper was released in May 2024 (updated Feb 2025). It comes with public code, a free TradingView indicator and a heavy trader following, so the exact rules may crowd. The underlying mechanism (dealer hedging, order-splitting) is structural, and the authors' post-publication update (2024 +32%) is positive but self-reported and short. Earlier literature shows intraday momentum weakened after 2013, and the paper's own gross profit per share was near zero in 2016–2017, so the edge is regime-dependent. Backtested returns also assume tiny slippage; the more cautious impact model cuts the Sharpe from 1.33 to 1.17.

## Data fit
Good for ES: we have 1-min ES bars from 2013-12 to 2026 (ETH and RTH), which is enough for the noise-area bands, VWAP and the half-hour decision grid. That covers about 12 years including 2018, 2020 and 2022, and it is long enough for an 80/20 split. NQ 1-min exists but only from mid-2021. The paper's own SPY test starts in 2007, so we can't check 2007–2012 or the 2008 crisis (the biggest return years). VIX data isn't in the inventory and would be needed for the VIX-regime filter; RSI can be computed from ES itself. We can't test the other stocks, ETFs or other futures (CL, GC, YM, RTY not available). Assumptions to settle: ES RTH open time is 09:30 ET and the data timezone is UTC; the paper uses the prior 16:00 close for the gap, while the ES futures close is 16:15 or 17:00 ET, which we need to choose; contract roll handling; the cost per round turn.

## Caveats
- The headline 1,985% return uses volatility-targeted leverage of up to 4x. The unlevered Sharpe is 1.24 and the gross return is about 380%. Max drawdown is 25% with leverage.
- The backtest runs on SPY ETF shares with $0.0035 commission + $0.001 slippage. Slippage was measured on small orders in April 2024 and may not hold at size or on futures.
- Almost all the profit per share was made in a few years (2008, 2018, 2021–2023). 2016–2017 were negative, and the full period had long flat stretches (2010–2017).
- The study is a single-instrument, 17-year in-sample backtest with no out-of-sample split and no Monte Carlo. The FAQ parameter sweeps show some stability (lookback, VM), but the paper picked 14/1.0 and the FAQ itself shows 90/1.5 does better.
- Conditional results (NR4, Wednesday, RSI regression) are data-mined subgroups, so treat them as hypotheses.
- The gamma explanation is only tested with an RSI proxy.
- Authors' own interest: they run the strategy, sell tools and a TradingView indicator, and the FAQ claims on futures and stocks (names hidden as ***) are not verifiable.
- Paper figures differ slightly between versions (e.g. 7,668 vs 7,964 trades; Sharpe 1.33 vs 1.35).
- The code uses the SPY 09:30 open and 16:00 close; applying it to ES (nearly 24-hour trading) changes the 'overnight gap' definition.

## Cited papers worth reading
- Hedging demand and market intraday momentum (2021)
- Market intraday momentum (2018)
- Understanding intraday momentum strategies (2022)
- Volume Weighted Average Price (VWAP) the Holy Grail for Day Trading Systems (2023)
- Gamma fragility (2020)
