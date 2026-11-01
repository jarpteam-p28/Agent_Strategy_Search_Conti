# The Overnight Drift

**Authors:** Nina Boyarchenko, Lars C. Larsen, Paul Whelan  
**Year:** 2023  **Type:** academic  **Read:** abstract_only  
**Source:** https://ideas.repec.org/p/fip/fednsr/87539.html

> US equity index futures earn large positive returns around the European open, linked to the previous US close's order imbalance: selloffs are followed by strong overnight reversals, rallies by much smaller ones.

## Findings
- Returns on US equity index futures are large and positive during the opening hours of European markets. — *Abstract: 'pervasive, economically large, and highly statistically significant'. Blog follow-up: the 2-3am ET window earned ~3.7%/yr of a 5.9%/yr close-to-close ES return, 1998-2020.*
- The overnight return is related to the order imbalance at the previous US close. — *Consistent with dealer inventory-risk models.*
- The response is asymmetric: market selloffs generate robust positive overnight reversals; reversals after rallies are much more modest. — *Abstract (Review of Financial Studies 36(9), 2023).*

## The WHY
**Pattern:** Execution mechanics / liquidity provision: dealers absorb closing order imbalances and demand compensation for carrying that inventory overnight.

Sell imbalances at the US close leave dealers long; they offload when European liquidity arrives, earning a premium; the premium is larger after selloffs because risk-bearing capacity is lower then.

- **Who is forced / predictable:** End-of-day sellers (closing auctions, rebalancers) who must trade at the close; dealers with limited capacity.
- **Why it persists:** Compensation for risk-bearing, not a free lunch — unless the closing imbalances themselves shrink.
- **What would kill it:** Smaller closing imbalances (finer algorithmic slicing) — which the 2026 follow-up says has happened since 2021.

## Setting
- Markets: US equity index futures
- Instruments: ES, NQ, YM
- Period: 1998-2020  Frequency: intraday  Holding: overnight hours around the European open

## Reported results
2-3am ET window ≈ 3.7%/yr of ES's 5.9%/yr (1998-2020, from the authors' 2026 blog post).
- Selloff days → strong overnight reversal; rally days → weak

## Tradable edge (our framing)
Long ES around the European open (02:00-03:00 ET), sized up after a down US session / large closing sell imbalance. Combine with Bondarenko & Muravyev's window; must survive the post-2021 decay.

## Angles to test
- Condition the overnight long on a down RTH day (proxy for sell imbalance)
- Condition on a down last 30 minutes (closer proxy for the closing auction imbalance)

## Decay risk: high
Authors' own 2026 update: ~0 since 2021.

## Data fit
ES 1-min (ETH + RTH) Dec 2013 → Sep 2026 in clean_ES_master.parquet; NQ 1-min Jul 2021 → Sep 2026. 2024+ is protected in the backtest project.

## Caveats
- Abstract and the authors' 2026 blog only; the full PDF was not reachable from this session.
- Read by Claude in a chat session (manual run), not by the weekly pipeline.
