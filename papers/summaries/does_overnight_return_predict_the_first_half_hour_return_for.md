# Does Overnight Return Predict the First Half-Hour Return for U.S. Market Indices?

**Authors:** Yasuhiro Iwanaga, Ryuta Sakemoto  
**Year:** 2025  **Type:** academic  **Read:** secondary  
**Source:** https://github.com/talalmalikllc-debug/nq-post-open-rebound

> Per an independent pre-registered NQ replication: the overnight return predicts the 09:30-10:00 return NEGATIVELY (β×100 = −4.15, t = −2.42, about half the paper's SPY strength), mostly in the first ~5 minutes, and it does not survive costs; trading with the overnight move fails; a narrowed version (buy NQ 09:35-10:00 after an extreme overnight drop that bounces at 09:35) was positive out of sample on 18 trades.

## Findings
- Replication on NQ: overnight return → first-half-hour return negative, β×100 = −4.15 (t = −2.42). — *NQ futures 2016-2026 (replicator's data); paper studies SPY/US indices.*
- Most of the reversal happens in the first ~5 minutes and does not survive costs.
- Momentum (same direction as overnight) failed in every holding window.
- Narrowed rule (overnight z ≤ −2 vs 60-day SD, 09:35 above 09:30 open, buy 09:35 → exit 10:00): out-of-sample 2022-2026 +50.9 pts/trade net, t = 2.49, 18 trades; train 2016-2021 +7.9 pts, t = 1.86. — *Pre-registered; 9 candidates chosen on training data.*

## The WHY
**Pattern:** Overnight overreaction corrected when full liquidity returns at the open.




## Setting
- Markets: US index futures/ETFs
- Instruments: SPY (paper), NQ (replication)
- Period: 2016-2026 (replication)  Frequency: 1-minute  Holding: 09:30/09:35 → 10:00

## Reported results
Per an independent pre-registered NQ replication: the overnight return predicts the 09:30-10:00 return NEGATIVELY (β×100 = −4.15, t = −2.42, about half the paper's SPY strength), mostly in the first ~5 minutes, and it does not survive costs; trading with the overnight move fails; a narrowed version (buy NQ 09:35-10:00 after an extreme overnight drop that bounces at 09:35) was positive out of sample on 18 trades.

## Tradable edge (our framing)
Supports overnight_reversal_first_hour_es; new spec nq_extreme_overnight_drop_rebound tests the narrowed version on our NQ/ES data.

## Angles to test

## Decay risk: medium
Tiny sample; non-monotonic effect.

## Data fit
ES 1-min Dec 2013 → Sep 2026, NQ 1-min Jul 2021 → Sep 2026 (2024+ protected in the backtest project).

## Caveats
- The paper itself (SSRN 5807282) was not reachable; content comes from an independent replication on GitHub that cites it — treat paper-level numbers as unverified.
- Read by Claude in a chat session (manual run 4), not by the weekly pipeline.
