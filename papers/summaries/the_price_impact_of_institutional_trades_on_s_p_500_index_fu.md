# Large Trades and Intraday Futures Price Behavior (indexed as: The Price Impact of Institutional Trades on S&P 500 Index Futures)

**Authors:** Alex Frino, Johan Bjursell, George H. K. Wang, Andrew Lepone  
**Year:** 2008  **Type:** academic  **Read:** abstract_only  
**Source:** https://ideas.repec.org/a/wly/jfutmk/v28y2008i12p1147-1181.html

> In CME futures, large customer BUYS have bigger permanent (information) price impact than large sells, while sells have bigger temporary (liquidity) impact that reverses; the asymmetry flips with market state (sells matter more in bear markets).

## Findings
- Permanent impact: buys > sells; temporary impact: sells > buys. — *JFM 28(12), CME customer large trades.*
- Bear markets: large sells carry more information; bull markets: buys.

## The WHY
**Pattern:** Liquidity-driven selling partly reverses; information-driven buying persists.




## Setting
- Markets: US index futures
- Instruments: CME futures
- Period: -  Frequency: trade-level  Holding: minutes

## Reported results
In CME futures, large customer BUYS have bigger permanent (information) price impact than large sells, while sells have bigger temporary (liquidity) impact that reverses; the asymmetry flips with market state (sells matter more in bear markets).

## Tradable edge (our framing)
No strategy (needs trade-level customer flags). Context for forced_selling_flush_fade_es: liquidity selling reverses, but less so in bear regimes.

## Angles to test

## Decay risk: low
Descriptive.

## Data fit
ES 1-min Dec 2013 → Sep 2026, NQ 1-min Jul 2021 → Sep 2026 (2024+ protected in the backtest project).

## Caveats
- Only the abstract / a secondary summary was reachable (SSRN is blocked from chat sessions); numbers not verified against the full paper.
- Read by Claude in a chat session (manual run 6, 2026-11-16), not by the weekly pipeline.
