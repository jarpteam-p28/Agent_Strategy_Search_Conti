# Intra-Day Momentum

**Authors:** Oleg Komarov  
**Year:** 2017  **Type:** academic  **Read:** secondary  
**Source:** https://cxoadvisory.com/?p=29509

> In US stocks (1993-2010) the 15:30-16:00 return is positively related to the 9:30-12:00 return, while the 13:30-15:30 return reverses the morning; the last half-hour is the strongest intraday slot (+8.9%/yr) and the first hour the weakest; all gross.

## Findings
- Last half-hour annualized +8.9%, overnight +20.1%, 09:30-10:00 −9.2%, 10:00-10:30 −5.9%. — *US stocks ex-microcaps, 1993-2010.*
- 9:30-12:00 winners/losers both positive in 15:30-16:00; 13:30-15:30 return negatively related to the morning.
- Morning winner/loser spread flipped sign after 2001 decimalization.

## The WHY
**Pattern:** Institutional order splitting and end-of-day rebalancing.




## Setting
- Markets: US equities
- Instruments: stocks
- Period: 1993-2010  Frequency: 30-minute  Holding: 30 minutes

## Reported results
In US stocks (1993-2010) the 15:30-16:00 return is positively related to the 9:30-12:00 return, while the 13:30-15:30 return reverses the morning; the last half-hour is the strongest intraday slot (+8.9%/yr) and the first hour the weakest; all gross.

## Tradable edge (our framing)
Covered by noise_area_last_half_hour_es; adds a variant signal (09:30-12:00 return instead of the first half-hour) and the mid-afternoon reversal as a descriptive check.

## Angles to test

## Decay risk: high
Gross; stock-level.

## Data fit
Single-stock study — not testable on our ES/NQ data.

## Caveats
- Only the abstract / a secondary summary was reachable (SSRN is blocked from chat sessions); numbers not verified against the full paper.
- Read by Claude in a chat session (manual run 6, 2026-11-16), not by the weekly pipeline.
