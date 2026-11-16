# The Dynamics of Leveraged and Inverse Exchange-Traded Funds

**Authors:** Minder Cheng, Ananth Madhavan  
**Year:** 2009  **Type:** industry  **Read:** abstract_only  
**Source:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1539120

> Leveraged and inverse ETFs must rebalance at the close in the same direction as the day's market move, so they add buying pressure after up days and selling pressure after down days, concentrated in the last minutes of trading.

## Findings
- Leveraged ETFs (2x, 3x) and inverse ETFs (-1x, -2x, -3x) reset leverage daily. To do that, they must trade in the direction of the day's index return. After an up day, bull funds buy and inverse funds also buy. After a down day, both sell. The paper derives the required flow as roughly L×(L−1)×AUM×(daily return), where L is the leverage multiple. This is positive for any |L|>1 and for any inverse fund. — *Mathematical derivation, from my knowledge of the paper. I could not open the full text, so details are unverified.*
- The rebalancing is a mechanical, non-discretionary flow. It is largest on big-move days and in high-volatility periods, such as late 2008. For narrow sector funds, for example financials, it can be a large share of closing-period volume and of the underlying market cap. — *From memory of the paper's sector examples in 2008-09. The exact figures are not verified.*
- Because of daily compounding, multi-day returns of these ETFs do not equal the stated multiple of the index return. They are path-dependent and suffer volatility drag. — *Standard result discussed in the paper. It is not directly tradable on our data.*

## The WHY
**Pattern:** Execution mechanics of big players (mandated end-of-day rebalancing flows, a form of institutional constraint).

The fund's prospectus promises a fixed daily leverage multiple. Fund managers and their swap counterparties must therefore buy or sell exposure in proportion to the day's return. They do it at or near the close, so the NAV calculation is accurate. The flow has the same sign as the day's return and rises with AUM, leverage and the size of the move. This adds late-day momentum or closing-auction pressure that other participants can anticipate. The flow is partly absorbed by swap dealers, who hedge in futures and the underlying.

- **Who is forced / predictable:** Leveraged and inverse ETF issuers (ProShares, Direxion and others) and their swap counterparties. They trade in the last 15-30 minutes and have no discretion about size or timing.
- **Why it persists:** The product structure is the cause. Daily-reset funds are still large and popular. The flow grows when volatility is high and when AUM is large. Arbitrageurs front-run it, so the effect is partly competed away, but the mandate cannot change.
- **What would kill it:** Leveraged ETF AUM shrinking, or funds moving rebalancing to swaps settled earlier or spread over the day. A regulatory change to the daily-reset structure. Wide front-running that shifts the move earlier, to 15:00-15:30. In the index futures the flow is small relative to total volume unless it is a high-volatility, large-move day.
- **Paper's view vs ours:** The authors only quantify the size of the rebalancing flow and warn about its potential market impact, especially for narrow sector funds. They do not offer a backtested trading rule. The trading edge, a last-30-minute continuation after a large day, is our extension. Later literature supports it, but with modest effect sizes and doubts about how much it is driven by gamma and 0DTE dealer hedging.

## Setting
- Markets: 
- Instruments: 
- Period:   Frequency:   Holding: 

## Reported results
Not a backtest. The paper quantifies the size of the daily rebalancing flow of leveraged and inverse ETFs, which is large on big-move days and for narrow sectors.
- Rebalancing flow ≈ L(L−1)×AUM×daily return, same direction as the day's move (from memory).
- The flow is concentrated near the close.
- No Sharpe, win rate or drawdown results.
- Costs: Not applicable.

## Tradable edge (our framing)
On days when the S&P or Nasdaq has moved a lot by about 15:30 ET, go with the direction of the day's move into the last 30 minutes, and exit at the close. The leveraged-ETF rebalance flow, together with other late-day momentum, should push that way. The edge should grow with the size of the day's move, the level of volatility and the estimated leveraged-ETF AUM. It should be absent on quiet days. It is a time-boxed intraday continuation trade, tied to a known forced flow, not a free-standing indicator. It would need to be tested against a simple baseline of always being long in that window, and by volatility and year, including the post-2022 0DTE regime.

## Angles to test
- Instrument: ES and NQ in the last 30 minutes; NQ has higher-AUM leveraged ETFs (TQQQ/SQQQ), so test the signal there too and compare effect sizes.
- Signal strength: condition on |day return at 15:30| above a threshold (for example 1 sigma, or 1.5% for ES). Test unconditional against conditional, and by pre/post-2022 (0DTE regime).
- Session: test windows 15:30-16:00, 15:45-16:00 and the last 5 minutes. Check the return profile to see where the flow shows up.
- One side only: long after up days may work better than short after down days. Test both sides separately.
- Combine with other findings: the first-half-hour-predicts-last-half-hour intraday momentum paper and the gamma-exposure cross findings. Check that the leveraged-ETF signal adds information beyond them.
- Use as a filter: skip fading end-of-day trends on big-move days.
- Reversal side: next-morning reversal of large close moves, if the closing flow is price pressure that reverses overnight.

## Decay risk: medium
The paper was published in 2009 and the flow is widely known to dealers and quants. Later work (for example Tuzun 2013, Shum et al. 2016, and Gao et al. 2018 on market intraday momentum) found similar late-day momentum, but the effect is partly arbitraged. On NQ and ES the net edge per trade after costs is likely small, so it should only work on large-move days.

## Data fit
"Partly testable. ES 1-min data from 2013 and NQ 1-min from mid-2021 let us build the signal (the return from the prior close to 15:30 ET) and the outcome (the return from 15:30 to 16:00 ET, or the 15:50 and 16:00 ET windows). Missing: leveraged ETF AUM and the exact daily flow estimates. We would need public ETF AUM series (not in inventory) to build the estimated rebalance flow as a share of volume. Without that, test with the day's return magnitude and realised volatility as a proxy. NQ has only about 5 years, so ES is the main test; NQ is a robustness check."

## Caveats
- I could not access the paper. The SSRN page and other URLs failed, so this summary is based on the abstract and my own knowledge of the paper and later literature. Numbers are not verified.
- The paper is a descriptive study of rebalancing flow, not a backtest. There is no tested trading rule, costs or sample results.
- Our rules and edge are an extension and have not been verified. The mapping from the ETF flow to ES or NQ futures return is indirect, since the flow is mostly in swaps and stocks.
- The 2008-09 sample and the sector funds studied are unlike today's market. The flow relative to futures volume is probably small.
- Later intraday-momentum evidence is regime-dependent. Dealers have been long gamma on expiry days since 0DTE, so test pre and post 2022.

## Cited papers worth reading
- Market Intraday Momentum (2018)
- Are Leveraged and Inverse ETFs the New Portfolio Insurers? (2013)
- Path-Dependence of Leveraged ETF Returns (2010)
- Leveraged ETF Rebalancing and Intraday Momentum (Shum, Hejazi, Haryanto, Rodier) (2016)
