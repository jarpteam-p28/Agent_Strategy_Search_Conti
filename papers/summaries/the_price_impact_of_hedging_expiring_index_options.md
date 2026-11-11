# The Price Impact of Hedging Expiring Index Options

**Authors:** Pedro Angel Garcia-Ares, Aurelio Vasquez, Neil D. Pearson, Diego Amaya  
**Year:** 2026  **Type:** academic  **Read:** abstract_only  
**Source:** https://algoseek.com/research/market-microstructure/the-price-impact-of-hedging-expiring-index-options/

> Delta hedges of expiring cash-settled S&P 500 options are unwound at expiration; using proprietary market-maker positions, the authors find these unwinds move index-futures returns and volatility in the 30 minutes before expiration.

## Findings
- Hedge unwinding concentrated in the last 30 minutes before expiration. — *Proprietary market-maker positions; AEA 2026.*
- Also documents volatility effects of hedge rebalancing.

## The WHY
**Pattern:** Cash settlement means hedges must be traded away at expiry, creating predictable flow.




## Setting
- Markets: US index futures
- Instruments: ES, SPX options
- Period: recent (0DTE era)  Frequency: 1-minute  Holding: last 30 min

## Reported results
Delta hedges of expiring cash-settled S&P 500 options are unwound at expiration; using proprietary market-maker positions, the authors find these unwinds move index-futures returns and volatility in the 30 minutes before expiration.

## Tradable edge (our framing)
Supports a last-30-minutes look on PM-expiration days (third_friday_spike_es / expiration_pin_es descriptive check: 15:30-16:00 range and drift on expiration vs non-expiration days). Direction needs dealer positions we do not have.

## Angles to test

## Decay risk: medium
Depends on 0DTE volumes.

## Data fit
ES 1-min Dec 2013 → Sep 2026, NQ 1-min Jul 2021 → Sep 2026 (2024+ protected in the backtest project). Needs options positioning / open-interest data we do not have; ES/NQ price data only allows proxies.

## Caveats
- Only the abstract / a secondary summary was reachable (SSRN is blocked from chat sessions); numbers not verified against the full paper.
- Read by Claude in a chat session (manual run 5, 2026-11-10), not by the weekly pipeline.
