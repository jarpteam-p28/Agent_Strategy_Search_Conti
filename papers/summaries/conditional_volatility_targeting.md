# Conditional Volatility Targeting

**Authors:** Dion Bongaerts, Xiaowei Kang, Mathijs van Dijk  
**Year:** 2020  **Type:** academic  **Read:** secondary  
**Source:** https://alphaarchitect.com/conditional-volatility-targeting/

> Scaling exposure only when last month's volatility is in its top quintile (cut) or bottom quintile (raise), and staying unscaled otherwise, reduces drawdowns and tail risk in all 10 major equity markets with ~1/3 less turnover than conventional volatility targeting, which raised drawdowns in several markets.

## Findings
- Conventional vol targeting raised max drawdown 4-34% in UK, Canada, Australia, Hong Kong. — *FAJ 76(4), 10 markets 1972-2019.*
- Conditional rule lowers drawdowns everywhere; Sharpe gains clearer for momentum than for market factors.
- Turnover 1.6×/yr (US) vs 2.4× conventional; leverage cap 200%.

## The WHY
**Pattern:** Volatility is persistent mainly at the extremes; scaling in between adds noise.




## Setting
- Markets: global equities
- Instruments: market and factor portfolios
- Period: 1972-2019  Frequency: monthly  Holding: monthly

## Reported results
Scaling exposure only when last month's volatility is in its top quintile (cut) or bottom quintile (raise), and staying unscaled otherwise, reduces drawdowns and tail risk in all 10 major equity markets with ~1/3 less turnover than conventional volatility targeting, which raised drawdowns in several markets.

## Tradable edge (our framing)
Variant for liquidity_stress_overlay_es and for VOLATILITY_SIZING: scale only in the top/bottom quintile of prior volatility. Consistent with Cederburg et al.: plain vol targeting doesn't add edge.

## Angles to test

## Decay risk: low
Risk-management result.

## Data fit
ES 1-min Dec 2013 → Sep 2026, NQ 1-min Jul 2021 → Sep 2026 (2024+ protected in the backtest project).

## Caveats
- Only the abstract / a secondary summary was reachable (SSRN is blocked from chat sessions); numbers not verified against the full paper.
- Read by Claude in a chat session (manual run 6, 2026-11-16), not by the weekly pipeline.
