# 0DTEs: Trading, Gamma Risk and Volatility Propagation

**Authors:** Chukwuma Dim, Bjorn Eraker, Grigory Vilkov  
**Year:** 2024  **Type:** academic  **Read:** secondary  
**Source:** https://harbourfrontquant.substack.com/p/impact-of-zero-dte-options-on-the

> No evidence that 0DTE gamma raises S&P volatility: higher 0DTE and short-dated open-interest gamma goes with LOWER intraday realized volatility, does not carry overnight, and 0DTE volume shocks have only tiny, short-lived effects; 0DTEs carry the largest volatility risk premium.

## Findings
- Higher 0DTE open-interest gamma → lower same-day realized volatility. — *SPX options.*
- 0DTE volume shocks raise underlying volume briefly; economically insignificant.
- Largest volatility risk premium among maturities.

## The WHY
**Pattern:** Dealers net long gamma dampen moves by trading against them.




## Setting
- Markets: US index options
- Instruments: SPX 0DTE
- Period: 2016-2023  Frequency: intraday  Holding: -

## Reported results
No evidence that 0DTE gamma raises S&P volatility: higher 0DTE and short-dated open-interest gamma goes with LOWER intraday realized volatility, does not carry overnight, and 0DTE volume shocks have only tiny, short-lived effects; 0DTEs carry the largest volatility risk premium.

## Tradable edge (our framing)
No strategy (needs options data). Context for gamma_flip_cross and for post-2022 regime splits.

## Angles to test

## Decay risk: low
Descriptive.

## Data fit
Needs options positioning / open-interest data we do not have; ES/NQ price data only allows proxies.

## Caveats
- Only the abstract / a secondary summary was reachable (SSRN is blocked from chat sessions); numbers not verified against the full paper.
- Read by Claude in a chat session (manual run 5, 2026-11-10), not by the weekly pipeline.
