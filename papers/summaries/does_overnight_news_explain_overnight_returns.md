# Does Overnight News Explain Overnight Returns?

**Authors:** Paul Glasserman, Kriste Krstovski, Paul Laliberte, Harry Mamaysky  
**Year:** 2025  **Type:** academic  **Read:** full_pdf  
**Source:** https://arxiv.org/html/2507.04481v1

> In S&P 500 stocks (2000-2022) overnight returns exceed intraday by ~2.75 bps/day (~7%/yr); news topics explain much of it — removing the stocks the news model selects makes the gap small and insignificant, out of sample 2011-2022.

## Findings
- Overnight minus intraday ≈ 2.75 bps/day (~7.2%/yr) since 2000. — *2.4m Reuters articles, 887 firms.*
- Without the news-selected stocks the gap is small and insignificant (out of sample 2011-2022).
- Topic exposures persistent (year-to-year ≈ 0.94).

## The WHY
**Pattern:** Information arrival: news released outside trading hours drives the overnight premium.




## Setting
- Markets: US equities
- Instruments: S&P 500 stocks
- Period: 1996-2022  Frequency: daily open/close  Holding: overnight vs intraday

## Reported results
News explains much of the overnight-intraday gap.

## Tradable edge (our framing)
No index-futures strategy; supports the information-flow WHY behind the overnight specs (vs the inventory WHY).

## Angles to test
- None for ES/NQ

## Decay risk: low
Explanatory.

## Data fit
ES 1-min Dec 2013 → Sep 2026, NQ 1-min Jul 2021 → Sep 2026 (2024+ protected in the backtest project).

## Caveats
- Read by Claude in a chat session (manual run 2), not by the weekly pipeline.
