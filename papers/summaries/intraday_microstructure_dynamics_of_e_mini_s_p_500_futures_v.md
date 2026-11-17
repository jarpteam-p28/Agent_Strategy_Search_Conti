# Intraday Microstructure Dynamics of E-mini S&P 500 Futures: Volatility Regimes, Liquidity Decay, and Long Memory in Realized Volatility

**Authors:** Max Brown  
**Year:** 2026  **Type:** academic  **Read:** abstract_only  
**Source:** https://papers.ssrn.com/abstract=6847024

> On ES 1-min data (Apr 2024-May 2026, 529 sessions), activity and bar range decay through the day (−44% from the first to the last 30 minutes), realized volatility is highly persistent (lag-1 autocorrelation 0.71, still positive at 21 days), and mean bar range tracks realized volatility almost perfectly (r = 0.975).

## Findings
- Mean 1-min bar range 4.78 pts in the first 30 min vs 2.69 in the last. — *ES, 2024-2026.*
- Four volatility regimes; April 2025 tariff shock 33.9% annualized vs 9.3% normal.
- Daily RV autocorrelation 0.71 at lag 1, significant to lag 21.

## The WHY
**Pattern:** Volatility clustering / long memory.




## Setting
- Markets: US index futures
- Instruments: ES
- Period: 2024-04 to 2026-05  Frequency: 1-minute  Holding: -

## Reported results
On ES 1-min data (Apr 2024-May 2026, 529 sessions), activity and bar range decay through the day (−44% from the first to the last 30 minutes), realized volatility is highly persistent (lag-1 autocorrelation 0.71, still positive at 21 days), and mean bar range tracks realized volatility almost perfectly (r = 0.975).

## Tradable edge (our framing)
No strategy. Supports our use of range-based volatility (AvgRange) and regime splits. Sample is entirely in our protected 2024+ period — do NOT use it to choose parameters.

## Angles to test

## Decay risk: low
Descriptive.

## Data fit
ES 1-min Dec 2013 → Sep 2026, NQ 1-min Jul 2021 → Sep 2026 (2024+ protected in the backtest project).

## Caveats
- Only the abstract / a secondary summary was reachable (SSRN is blocked from chat sessions); numbers not verified against the full paper.
- Sample overlaps the protected 2024+ data.
- Read by Claude in a chat session (manual run 6, 2026-11-16), not by the weekly pipeline.
