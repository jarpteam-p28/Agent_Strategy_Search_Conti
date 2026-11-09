# Liquidity Provision to Leveraged ETFs and Equity Options Rebalancing Flows: Evidence from End-of-Day Stock Prices

**Authors:** Andrea Barbon, Heiner Beckmeyer, Andrea Buraschi, Mathis Moerke  
**Year:** 2022  **Type:** academic  **Read:** abstract_only  
**Source:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3925725

> Leveraged-ETF rebalancing and options delta-hedging create predictable late-day order flow that pushes prices in the direction of the day's move (end-of-day momentum) and then partly reverses; the gamma effect persists while the LETF effect has faded.

## Findings
- Leveraged-ETF rebalancing and dealer delta-hedging of equity options are two separate, large sources of liquidity demand. Both produce end-of-day momentum and later mean reversion in stock returns. — *Abstract only. The specific numbers, sample and universe were not available to me.*
- The gamma (options hedging) effect is persistent across the whole sample. The LETF effect has weakened over time. — *Abstract only.*
- LETF flows attract more liquidity provision, and their price impact is shorter-lived. Intermediaries can choose when to delta-hedge, which makes their flows less predictable. — *Abstract only. The authors read this as showing that disclosing information improves liquidity.*

## The WHY
**Pattern:** Execution mechanics of big players, plus liquidity constraints on large orders. The flows are forced by mandate and by hedging.

A leveraged ETF has to hold a fixed leverage multiple each day. After a big up day it must buy more of the underlying, and after a big down day it must sell. It does this near the close, so it can match the closing NAV. Option dealers who are short gamma must also buy into rising markets and sell into falling ones to stay delta-neutral. Both flows point the same way as the day's move, and they land in a short window. Liquidity providers take the other side and demand a price concession. That gives continuation into the close, then partial reversal afterwards.

- **Who is forced / predictable:** LETF issuers, whose rebalancing size is mechanical and can be computed from the day's return and assets under management. Short-gamma option dealers, who have to hedge. Liquidity providers and market makers absorb the flow and are paid for it.
- **Why it persists:** The hedging flows follow from option exposure and are structural. Where gamma is concentrated is partly observable. The LETF effect is fading because the flow is public and predictable, so more liquidity providers compete for it. The gamma effect persists because dealers can time their hedges and the exposure is harder to estimate.
- **What would kill it:** More liquidity providers front-running the flow, as has happened with LETFs. Dealers spreading hedges across the day. A regime where dealers are net long gamma, which flips the sign to mean reversion. Changes to the closing auction or to LETF rebalancing practice, such as rebalancing earlier. Very low LETF assets.
- **Paper's view vs ours:** The authors' account is the same in substance. They stress information disclosure and competition among liquidity providers as the reason the LETF effect decays. Our addition is that the sign depends on the dealers' gamma sign. This links to the playbook note that 0DTE dealers are long gamma on expiry days, so the effect could change sign or weaken. I could not check the details in the full text.

## Setting
- Markets: 
- Instruments: 
- Period:   Frequency:   Holding: 

## Reported results
End-of-day momentum followed by mean reversion from LETF and option hedging flows. The gamma effect is persistent. The LETF effect declines over time.
- Costs: Unknown, I could not read the paper beyond the abstract.

## Tradable edge (our framing)
Late in the session, trade in the direction of the day's move, because forced hedging and LETF rebalancing flows keep pushing the index the same way into the close. Then consider fading the move in the next session's open or the following hours, when the liquidity concession reverses. We test this on ES and NQ as a time-boxed continuation trade, for example from about 15:00 to 15:45 ET, and use size of the day's move (or an approximate leverage-ETF rebalance estimate) as the signal strength. The gamma-linked version should work better on days with large moves. Treat it as a flow-driven drift, not a free lunch, and compare it with the always-long baseline for the same window.

## Angles to test
- ES and NQ: signal is the return from the prior close (or from the open) to 15:00 ET. Hold from 15:00 or 15:30 to a time exit at 15:55 or 16:00. Report gross points against costs.
- Split by pre-2022 and post-2022. Split by signal strength, since the effect should be stronger after large moves. Compare NQ with ES, because LETF assets are larger on Nasdaq-linked products.
- Long-only versus short-only: test whether strong up days continue more than strong down days.
- Reversal leg: fade the late-day move at the next open or in the first 30 minutes. This is the 'mean reversion later' part of the claim.
- Add an expiry filter such as monthly opex, Fridays or 0DTE days, as a proxy for gamma regime. Then try to build gamma levels from tick data, along the lines of the gamma-exposure study.
- Combine with the overnight-drift and opening-range ideas. The late-day move can predict the overnight return and the next open.

## Decay risk: medium
The paper was published in 2021–22 and the authors already report that the LETF effect has decreased. The gamma effect persisted in their sample. The late-day momentum is also known from Gao et al. (2018) on intraday momentum. 0DTE growth may have changed dealer positioning.

## Data fit
Partly testable. The paper uses stocks, but the same logic applies to index futures. ES 1-minute data runs 2013–2026 and NQ 1-minute data runs 2021–2026. That is enough to test late-day momentum (the return from open to about 15:00 as the signal, the last 30 to 60 minutes as the outcome), split pre- and post-2022, and by day-move size. The LETF rebalance can be approximated from the daily index return times leverage squared, but there is no AUM data, so the size is not scaled. We have no option open interest or gamma exposure data, so the gamma-signed version can't be tested directly. We have no single-stock data. The result for ES and NQ as a proxy for the paper's stock-level evidence is unproven.

## Caveats
- I could only read the SSRN abstract page. I did not read the full paper, so every sample, universe, size, t-stat and cost number is missing.
- The explanation of the mechanism is partly inferred from the abstract and from the general literature on LETF rebalancing and dealer gamma hedging. Check it against the full text.
- The paper's evidence is on individual stocks. Transfer to index futures is a hypothesis.
- Expect the effect to be small after costs, as in the Mesfin cost hurdle note.

## Cited papers worth reading
- Market Intraday Momentum (2018)
- Leveraged ETFs and market quality / Leveraged Funds and the Shadow Cost of Leverage (2009)
- Do Leveraged ETFs Rebalance at the Close? / Leveraged ETFs and Volatility (Tuzun) (2013)
