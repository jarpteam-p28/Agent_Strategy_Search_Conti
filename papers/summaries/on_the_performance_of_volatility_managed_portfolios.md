# On the Performance of Volatility-Managed Portfolios

**Authors:** Scott Cederburg, Michael S. O'Doherty, Feifei Wang, Xuemin (Sterling) Yan  
**Year:** 2020  **Type:** academic  **Read:** secondary  
**Source:** https://alphaarchitect.com/does-portfolio-timing-based-on-volatility-signals-outperform-buy-and-hold/

> Across 103 equity strategies, volatility-managed versions show in-sample alphas but do NOT beat the unmanaged originals in real time: out of sample they earn lower Sharpe ratios and certainty-equivalent returns (only momentum, ROE and BAB avoid significant degradation) because the scaling coefficients are unstable.

## Findings
- 75% of in-sample alphas positive, 23 significant. — *JFE 138(1) 2020.*
- Real-time: volatility management generally lowers Sharpe vs the original strategy, market factor included.
- Robust to window length, rolling samples and leverage limits.

## The WHY
**Pattern:** In-sample spanning regressions overstate the benefit of scaling by inverse variance.




## Setting
- Markets: US equities
- Instruments: 103 factor portfolios
- Period: 1926-2017  Frequency: monthly  Holding: monthly

## Reported results
Across 103 equity strategies, volatility-managed versions show in-sample alphas but do NOT beat the unmanaged originals in real time: out of sample they earn lower Sharpe ratios and certainty-equivalent returns (only momentum, ROE and BAB avoid significant degradation) because the scaling coefficients are unstable.

## Tradable edge (our framing)
No new strategy. Confirms our rule: volatility sizing is a sizing VIEW, not a source of edge — judge strategies at 1 contract first.

## Angles to test

## Decay risk: low
Methodological.

## Data fit
ES 1-min Dec 2013 → Sep 2026, NQ 1-min Jul 2021 → Sep 2026 (2024+ protected in the backtest project).

## Caveats
- Read by Claude in a chat session (manual run 5, 2026-11-10), not by the weekly pipeline.
