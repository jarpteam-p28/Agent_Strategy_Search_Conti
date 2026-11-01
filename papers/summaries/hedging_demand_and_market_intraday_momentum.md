# Hedging Demand and Market Intraday Momentum

**Authors:** Guido Baltussen, Zhi Da, Sten Lammers, Martin Martens  
**Year:** 2021  **Type:** academic  **Read:** abstract_only  
**Source:** https://pure.eur.nl/en/publications/hedging-demand-and-market-intraday-momentum/

> Across 60+ futures (equities, bonds, commodities, FX) 1974-2020, the return from the previous close to the last half hour predicts the last 30 minutes' return, and the effect reverts over the next days; the authors link it to short-gamma hedging by option dealers and leveraged ETFs.

## Findings
- The return from the previous close up to the last half hour positively predicts the last-30-minute return. — *Economically and statistically significant across 60+ futures, 1974-2020 (Journal of Financial Economics 142(1), 2021).*
- The effect reverts over the following days. — *Abstract.*
- Intraday momentum is linked to hedging of short-gamma positions by option market makers and leveraged ETFs. — *Hedging short gamma requires trading in the direction of the price move.*

## The WHY
**Pattern:** Execution mechanics of forced players (short-gamma dealers, leveraged-ETF rebalancing) near the close.

Short-gamma hedgers must buy after rallies and sell after drops, mostly near the close; the push scales with the day's move.

- **Who is forced / predictable:** Option dealers net short gamma; leveraged/inverse ETFs rebalancing daily.
- **Why it persists:** Mandatory, size-dependent flows.
- **What would kill it:** Dealers moving net long gamma (heavy overwriting, 0DTE dynamics), shrinking leveraged-ETF AUM.

## Setting
- Markets: Global futures
- Instruments: 60+ futures incl. equity index futures
- Period: 1974-2020  Frequency: intraday  Holding: last 30 minutes

## Reported results
Rest-of-day return predicts the last 30 minutes; reverts over the next days.

## Tradable edge (our framing)
Covered by the existing spec noise_area_last_half_hour_es (this paper is its WHY) — its baseline B2 (direction of the day's move into 15:30, no band) is exactly this paper's signal.

## Angles to test
- Already in the last-30-minutes sheet as baseline B2
- Split by a gamma proxy (prior-day move / volatility) if the base works

## Decay risk: medium
Long sample, structural flows; but 0DTE since 2022 may change dealer gamma near the close.

## Data fit
ES 1-min (ETH + RTH) Dec 2013 → Sep 2026 in clean_ES_master.parquet; NQ 1-min Jul 2021 → Sep 2026. 2024+ is protected in the backtest project.

## Caveats
- Abstract only — the full PDF links were blocked from this session; no coefficients recorded.
- Read by Claude in a chat session (manual run), not by the weekly pipeline.
