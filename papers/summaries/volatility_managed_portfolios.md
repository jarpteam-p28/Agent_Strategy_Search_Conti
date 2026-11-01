# Volatility-Managed Portfolios

**Authors:** Alan Moreira, Tyler Muir  
**Year:** 2017  **Type:** academic  **Read:** abstract_only  
**Source:** https://www.nber.org/papers/22208

> Scaling factor exposure down when recent volatility is high (and up when low) produces large alphas and higher Sharpe ratios for the market, value, momentum and other factors, because volatility changes are not matched by changes in expected returns.

## Findings
- Volatility-managed versions of market, value, momentum, profitability, ROE, investment and carry factors produce large alphas and higher Sharpe ratios. — *Journal of Finance 72(4), 2017.*
- Takes less risk in recessions/crises yet keeps high average returns.

## The WHY
**Pattern:** Volatility doesn't predict returns proportionally, so risk-scaling raises Sharpe.




## Setting
- Markets: US equities, FX carry
- Instruments: factor portfolios
- Period: long history  Frequency: monthly  Holding: monthly rebalance

## Reported results
Large alphas from inverse-variance scaling.

## Tradable edge (our framing)
The academic basis Conti cites for volatility sizing — already applied as the sizing view (VOLATILITY_SIZING.md).

## Angles to test
- Already in the sizing view

## Decay risk: low
Widely replicated; later work debates out-of-sample gains.

## Data fit
ES 1-min Dec 2013 → Sep 2026, NQ 1-min Jul 2021 → Sep 2026 (2024+ protected in the backtest project).

## Caveats
- Read by Claude in a chat session (manual run 2), not by the weekly pipeline.
