# Comparing the Post–Earnings Announcement Drift for Surprises Calculated from Analyst and Time Series Forecasts

**Authors:** Joshua Livnat, Richard R. Mendenhall  
**Year:** 2006  **Type:** academic  **Read:** abstract_only  
**Source:** https://doi.org/10.1111/j.1475-679X.2006.00196.x

> Post-earnings drift is stronger when the surprise is measured against analyst consensus than against a time-series (seasonal random walk) forecast, and it is largest in stocks that are costly to trade.

## Findings
- PEAD exists for both surprise definitions, but the drift after surprises measured against analyst forecasts (I/B/E/S consensus) is larger than the drift after time-series surprises (same quarter last year, seasonal random walk). — *US quarterly announcements, roughly 1987–2003, hedge portfolios long top-decile / short bottom-decile surprise. Written from memory of the paper. I could not open the full text, so I have no exact figures.*
- The analyst-based surprise carries information beyond the time-series surprise and beyond the announcement-window price reaction. The two measures can be combined. — *Cross-sectional regressions of post-announcement abnormal returns on both surprise types. From memory, not verified.*
- The drift is bigger and more persistent in stocks with higher trading costs: low price, low volume, small size. This points to limits to arbitrage. The drift is not explained by standard risk factors. — *Sub-sample and transaction-cost analyses. From memory, not verified.*
- Trade-size data suggest that small traders react more to time-series surprises, and larger traders react more to analyst surprises. Small traders therefore seem to under-use the more informative analyst-based signal. — *Trade-size-based investor-class analysis in the paper. From memory, not verified.*

## The WHY
**Pattern:** Slow information diffusion + liquidity constraints on large orders (PEAD)

Investors under-react to earnings news. Part of the market anchors on a naive benchmark, last year's EPS. The more informative benchmark is the analyst consensus. Price converges slowly toward the analyst-based surprise over the next 60 days or so. Institutions cannot build full positions in one day in thinly traded stocks, so their buying is spread over days or weeks. That creates the drift.

- **Who is forced / predictable:** Small, naive investors trade on the simple benchmark. Institutions are slowed by size and trading costs. Arbitrageurs are limited by costs in low-price, low-volume stocks.
- **Why it persists:** Trading costs and capacity limits stop arbitrage in small and mid caps. Coverage is thin, and costs scale with size, so the structural reason is still there.
- **What would kill it:** Cheaper trading and wider analyst coverage in small caps. Firms pre-announcing bad news, which weakens the short side. Crowding by quant funds. Consensus data becoming fully priced within the announcement window.
- **Paper's view vs ours:** The authors lean on transaction costs and limits to arbitrage, and on investors' differing sophistication. Our WHY is the same, with the addition that institutions must work large orders slowly. I could not check the details against the full text.

## Setting
- Markets: 
- Instruments: 
- Period:   Frequency:   Holding: 

## Reported results


## Tradable edge (our framing)
After an earnings release, rank stocks by surprise against analyst consensus. Combine that with the announcement-window price reaction, and optionally the time-series surprise. Buy the strongly positive group and hold for about 60 days, since institutions and slow-reacting investors keep pushing prices in that direction. The effect is strongest in small and mid caps with low coverage and higher trading costs. Mega caps carry little edge. The long side is the more reliable. Size positions by dollars or percent per name, and watch costs, because the stocks with the biggest drift are also the most expensive to trade.

## Angles to test
- Small/mid-cap universe only. Test Europe or other markets with thinner analyst coverage.
- Long-only version, since the short side has weakened as companies pre-announce bad news.
- Combine three signals: announcement-window return (Ball-Brown), the 60-day horizon (Bernard-Thomas), and the analyst-consensus surprise (this paper).
- Condition on trading cost and volume buckets and keep only names where the drift survives costs.
- Index-futures proxy: aggregate earnings-season surprise breadth in the Nasdaq-100/S&P 500 constituents as a signal for NQ/ES drift over the following weeks. Needs outside data.
- Use the first-day price reaction as a proxy when EPS data is missing, and hold for 60 days.

## Decay risk: high
PEAD has been known since 1968, and this paper has been out since 2006. The literature reports that the drift has shrunk in liquid stocks. It persists mainly in costly-to-trade small caps, and the short side has weakened.

## Data fit
"Not testable with the current inventory. It needs single-stock prices, earnings dates, actual EPS, and I/B/E/S analyst consensus, and we have none of these. We hold only ES and NQ futures minute and tick data. A rough index-level proxy, the ES/NQ drift after earnings-heavy weeks, is possible but only loosely related. Missing: stock-level OHLC data, an earnings calendar, EPS actuals and estimates, and market-cap and volume data for the universe."

## Caveats
- I could not open the paper, because the DOI and publisher access were blocked. Everything here comes from memory of the abstract and the paper. Specific numbers are omitted on purpose and the details may be imperfect.
- The sample is US stocks, roughly 1987–2003. That is old, and decay has probably occurred since.
- The returns are gross of realistic transaction costs in the stocks where the drift is largest.

## Cited papers worth reading
- Post-Earnings-Announcement Drift: Delayed Price Response or Risk Premium? (1989)
- An Empirical Evaluation of Accounting Income Numbers (1968)
- Post-Earnings Announcement Drift: The Role of Revenue Surprises (2006)
- Post-Earnings-Announcement Drift and the Dispersion of Analyst Forecasts / Trading Costs and PEAD (Chordia, Goyal, Sadka, Sadka, Shivakumar) (2009)
