# Evaporating Liquidity

**Authors:** Stefan Nagel  
**Year:** 2012  **Type:** academic  **Read:** full_pdf  
**Source:** https://nber.org/papers/w17653

> Short-term reversal returns (a proxy for paid liquidity provision) are predictable with the VIX: expected returns and Sharpe ratios spike when VIX rises in turmoil (e.g. 2007-09), even for industry portfolios that earn little on average.

## Findings
- Reversal-strategy returns (liquidity provision) rise ~0.22 pp/day per normalized VIX point (≈ 0.014 pp per annualized VIX point); expected returns rose ~10× in 2007-09, Sharpe doubled. — *Nagel, NBER w17653, CRSP stocks 1998-2010.*
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
Supports conditioning every ES/NQ reversal spec (close_reversal_overnight_es, forced_selling_flush_fade_es, liquidity_recovery_long_es) on high volatility — use AvgRange top tercile as the VIX proxy.

## Angles to test
- Condition overnight_reversal_first_hour_es on high AvgRange

## Decay risk: medium
Regime-dependent.

## Data fit
Cross-sectional; the ES version would be a regime filter only.

## Caveats
- Read by Claude in a chat session (manual run 3), not by the weekly pipeline.
- Full NBER text read (2026-11-17, manual run 7).
