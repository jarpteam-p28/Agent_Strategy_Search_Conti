# Predatory Trading

**Authors:** Markus K. Brunnermeier, Lasse Heje Pedersen  
**Year:** 2005  **Type:** academic  **Read:** abstract_only  
**Source:** https://doi.org/10.1111/j.1540-6261.2005.00781.x

> When a big trader is forced to sell and others know it, rivals sell ahead of the forced flow, push the price below fundamental value, and then buy it back as it recovers.

## Findings
- Theory paper (Journal of Finance 2005). It is a model with no empirical sample. A distressed large trader must liquidate. Other strategic traders know this. They find it profitable to trade in the same direction first (sell or short), which pushes the price down. They then buy back at the depressed price once the forced seller has finished. — *From my memory of the paper. The PDF could not be fetched, so I did not verify this against the text.*
- Predation causes price overshooting. Prices fall below fundamental value and later recover. The distressed trader's losses are larger than they would be if the others only supplied liquidity. — *Model result as I recall it. I did not read the full text.*
- Predation is stronger when the forced seller's position is large and publicly known, when the market is illiquid, and when the seller is near its funding or margin limits. Several predators competing makes it worse, because each wants to sell before the others do. That produces a race to sell early. — *Model result as I recall it. I did not read the full text.*
- Even a trader who is not distressed can lose if many traders hold similar positions. Liquidation can then spill over into other assets and funds. The paper links this to episodes such as LTCM in 1998 and to the risk of disclosing positions. — *Discussion section as I recall it. I did not read the full text.*

## The WHY
**Pattern:** Liquidity constraints on large orders, combined with an institutional constraint or mandate (margin calls, risk limits, index-tracking rules). This also has an execution-mechanics flavour, because forced flows are predictable.

A large player's forced order cannot be absorbed at the current price, because liquidity providers need to be paid. If its schedule or its distress is known, rivals trade ahead of it. This pushes the price past fundamental value, and the move reverses once the forced flow ends. The edge is early continuation in the direction of the forced flow, followed by mean reversion after the flow stops.

- **Who is forced / predictable:** Levered funds facing margin calls, index funds and ETFs that must rebalance on fixed dates, and large traders with disclosed positions. They trade by rule, not by choice. Their price impact is predictable, and others can front-run it.
- **Why it persists:** Leverage, margin constraints and mechanical rebalancing are structural. Liquidity is finite relative to size. Fund positions overlap, so distress spreads. Arbitrage capital is itself limited, which keeps the dislocations from closing instantly.
- **What would kill it:** Position and flow opacity (dark pools, randomised or slow execution). Deep liquidity providers who lean against forced flows. Regulation or rule changes that remove forced selling, such as lower leverage, or the removal of known rebalance or roll schedules. Crowding by many predators, which compresses the reversal profit.
- **Paper's view vs ours:** The authors give a clean, strategic-trading model, but it needs a known distressed position. In our data we cannot observe who is distressed. Our proxy has to be the footprint of forced flow: a fast, high-volume one-directional move around known mechanical events. The paper makes no claim about a retail-tradable intraday rule.

## Setting
- Markets: Theoretical
- Instruments: Generic risky asset in a model
- Period: n/a. Motivating episodes include LTCM in 1998.  Frequency: n/a (theoretical model)  Holding: Multi-period: the predator sells during the forced liquidation, then buys back afterwards

## Reported results
No backtest. This is a theory paper whose results are model propositions about overshooting and profitable predation.
- Costs: n/a (theory paper)

## Tradable edge (our framing)
We cannot see anyone's distress directly. The idea is to trade the footprint of forced or mechanical flow in ES and NQ. First, join the move early, when volume and speed are abnormal and one-directional in a window where forced flow is known to exist: the last 30 minutes of the session, the quarterly roll and expiry windows, and month-end or index rebalance days. Second, fade the overshoot after the flow window ends, expecting a partial recovery over the next session open or the next day. The test is whether continuation during the forced-flow window and reversion afterward both beat a "just be long" baseline, after costs. This is a hypothesis built from the WHY. The paper itself offers no rules.

## Angles to test
- Different session: split into a continuation leg during the forced-flow window and a reversion leg at the next open, and test each separately.
- Event days: quarterly expiry and roll days, Russell reconstitution (ES/NQ proxies), month-end, and days with big VIX spikes (forced deleveraging).
- Stress overshoot fade: after an N-sigma 15-60 minute drop on high volume, go long for a time-exit holding period and compare to the always-long baseline. Report 2022 and the 2020 and 2024 crashes separately.
- Long-only: forced selling creates overshoots below fair value, and forced buying overshoots are less reliable, so test long-only.
- Volatility-conditioned: condition on VIX or realised volatility, as in the playbook's note on scheduled-event drifts.
- Cross-instrument: run the same code on NQ and ES and check whether the larger overshoot appears in the more levered, thinner instrument.

## Decay risk: medium
The paper was published in 2005 and is widely cited, so the general mechanism is known. Specific front-running of mechanical flows (roll and rebalance days) is crowded. The underlying structure, finite liquidity plus forced flows, persists. Expect only a small residual edge in liquid index futures after costs.

## Data fit
Partial. ES 1-minute data from 2013 and NQ 1-minute data from 2021 let us test intraday continuation and reversion around the close, expiry and roll days, and around volume-spike drops. ES tick data (2021-2023) and NQ ticks allow a finer look at order-flow footprints. Missing: any data on fund positions, margin stress or flows, and single stocks and ETFs. We would have to build a calendar of roll, expiry and rebalance dates ourselves. NQ before 2021 is not available. The paper is theory, so there are no parameters to start from. We would set everything in-sample.

## Caveats
- I could not fetch the paper. The doi.org domain was blocked and no PDF was available. This summary comes from memory of the paper and from general knowledge, not from reading the text. Details need checking before anyone relies on them.
- It is a theory paper with no tested trading rule and no costs. It does not tell us how to identify distressed traders in real time.
- Any rule we build from it is our own hypothesis, and it is a hard one to test. Event samples are small, and results will depend heavily on outliers such as 2020.
- Net-of-cost hurdles for intraday NQ signals are high (see the Mesfin 2026 note in the playbook). Prefer holds of 60+ minutes and demand net t >= 2.

## Cited papers worth reading
- Market Liquidity and Funding Liquidity (2009)
- The Limits of Arbitrage (1997)
- Front-Running Index Funds / The Price Impact of Index Reconstitution (Russell rebalancing) (2006)
- Leveraged ETFs and market-close rebalancing flows (2009)
