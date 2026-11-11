# Nonlinear Time Series Momentum

**Authors:** Tobias Moskowitz, Riccardo Sabbatucci, Andrea Tamoni, Björn Uhl  
**Year:** 2025  **Type:** academic  **Read:** secondary  
**Source:** https://www.cxoadvisory.com/momentum-investing/s-shaped-time-series-momentum

> Across 53 futures (1980-2024), time-series momentum works better when position size flattens or reverses for EXTREME past returns (an S-shaped signal) than with linear weights; higher out-of-sample gross Sharpe for 21/62/260-day lookbacks.

## Findings
- S-shaped weights beat linear TSMOM out of sample, gross. — *53 futures incl. 8 equity index futures.*
- Signal = past return ÷ 260-day volatility, 12% vol target.

## The WHY
**Pattern:** Small/moderate trends persist; extreme moves partly reverse.




## Setting
- Markets: global futures
- Instruments: 53 futures
- Period: 1980-2024  Frequency: daily  Holding: weeks-months

## Reported results
Across 53 futures (1980-2024), time-series momentum works better when position size flattens or reverses for EXTREME past returns (an S-shaped signal) than with linear weights; higher out-of-sample gross Sharpe for 21/62/260-day lookbacks.

## Tradable edge (our framing)
Variant for trend_risk_timing_overlay_es: cap the trend signal at ±1.5 SD and reduce exposure beyond ±2.5 SD. Daily, ES only (single asset ⇒ weak test).

## Angles to test

## Decay risk: medium
Gross only; multi-asset result.

## Data fit
ES 1-min Dec 2013 → Sep 2026, NQ 1-min Jul 2021 → Sep 2026 (2024+ protected in the backtest project).

## Caveats
- Only the abstract / a secondary summary was reachable (SSRN is blocked from chat sessions); numbers not verified against the full paper.
- Read by Claude in a chat session (manual run 5, 2026-11-10), not by the weekly pipeline.
