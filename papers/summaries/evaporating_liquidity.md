# Evaporating Liquidity

**Authors:** Stefan Nagel  
**Year:** 2012  **Type:** academic  **Read:** abstract_only  
**Source:** https://nber.org/papers/w17653

> Short-term reversal returns (a proxy for paid liquidity provision) are predictable with the VIX: expected returns and Sharpe ratios spike when VIX rises in turmoil (e.g. 2007-09), even for industry portfolios that earn little on average.

## Findings
- Reversal strategy returns vary strongly over time and are predicted by VIX. — *RFS 25(7), 2012.*
- Industry-level reversal earns little on average but a lot when VIX is high.

## The WHY
**Pattern:** Liquidity provision is paid more when intermediaries withdraw (high VIX).




## Setting
- Markets: US equities
- Instruments: stocks, industry portfolios
- Period: to 2010  Frequency: daily/weekly  Holding: days

## Reported results
Short-term reversal returns (a proxy for paid liquidity provision) are predictable with the VIX: expected returns and Sharpe ratios spike when VIX rises in turmoil (e.g. 2007-09), even for industry portfolios that earn little on average.

## Tradable edge (our framing)
Index angle (speculative): short-term reversal in ES works mainly in high-volatility regimes — a regime filter for the overnight-reversal spec.

## Angles to test
- Condition overnight_reversal_first_hour_es on high AvgRange

## Decay risk: medium
Regime-dependent.

## Data fit
Cross-sectional; the ES version would be a regime filter only.

## Caveats
- Read by Claude in a chat session (manual run 3), not by the weekly pipeline.
