# Nasdaq-100 Index Futures: Intraday Momentum or Reversal?

**Authors:** Susana Yu, Joel Rentzler, Avner Wolf  
**Year:** 2005  **Type:** academic  **Read:** abstract_only  
**Source:** https://joim.com/downloads/nasdaq-100-index-futures-intraday-momentum-reversal

> In Nasdaq-100 futures, today's intraday returns show both momentum and reversal depending on the signs of yesterday's and last night's returns; last night's return is mainly followed by reversal.

## Findings
- Last night's (overnight) return is mainly associated with intraday reversal. — *Multiple regression of intraday returns on yesterday's and overnight returns (Journal of Investment Management).*
- Yesterday's return is associated with both momentum and reversal, depending on signs, bull/bear state and Mondays. — *'A simplistic view of momentum and reversal proves untenable.'*
- A forecast model is favoured in four intraday periods, suggesting structure in the opening hours. — *No magnitudes in the abstract.*

## The WHY
**Pattern:** Overnight overreaction corrected when the regular session opens (liquidity returns).

Thin overnight trading pushes prices too far; full-session liquidity at the open reverses part of the move.


## Setting
- Markets: CME Nasdaq-100 futures
- Instruments: NQ
- Period: not stated in abstract  Frequency: intraday  Holding: intraday periods

## Reported results
Overnight return → intraday reversal; sign- and day-dependent.

## Tradable edge (our framing)
Fade the overnight move in the first hour of the regular session (see spec overnight_reversal_first_hour_es, which combines this with Cliff, Cooper & Gulen 2008).

## Angles to test
- Fade the overnight return 09:30→10:30 ET, ES and NQ
- Only after large overnight moves (top tercile vs AvgRange)
- Mondays separately

## Decay risk: high
Old sample; MNQ falsification study found gap-fill fades unprofitable after costs 2021-2025.

## Data fit
ES 1-min (ETH + RTH) Dec 2013 → Sep 2026 in clean_ES_master.parquet; NQ 1-min Jul 2021 → Sep 2026. 2024+ is protected in the backtest project.

## Caveats
- Abstract only; no sample period or magnitudes.
- Read by Claude in a chat session (manual run), not by the weekly pipeline.
