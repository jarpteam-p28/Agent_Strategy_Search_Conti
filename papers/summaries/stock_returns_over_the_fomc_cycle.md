# Stock Returns over the FOMC Cycle

**Authors:** Anna Cieslak, Adair Morse, Annette Vissing-Jorgensen  
**Year:** 2019  **Type:** academic  **Read:** full_pdf  
**Source:** https://stern.nyu.edu/sites/default/files/assets/documents/cycle_paper_cieslak_morse_vissingjorgensen.pdf

> From 1994 to 2013 the whole US equity premium was earned in even weeks of FOMC cycle time (weeks 0, 2, 4, 6 counted from the scheduled meeting); odd weeks were flat or negative. Staying out in odd weeks doubled the Sharpe ratio (≈0.4 → 0.8).

## Findings
- Week 0 = days −1..3, week 2 = days 9..13, week 4 = 19..23, week 6 = 29..33 (day 0 = scheduled FOMC decision day). — *Published JF 74(5) 2019; 2015 draft read.*
- Average 5-day excess returns: week 0 +0.57%, week 2 +0.30%, week 4 +0.42%, week 6 +0.61%; odd weeks −0.17% to 0. — *1994-2013 CRSP value-weighted.*
- Even-week days earn 10-13.6 bp/day more than odd-week days (1% significance); pattern in all three sub-periods and in international markets.
- Strategy 'out of the market in odd weeks': Sharpe ≈ 0.8 vs ≈ 0.4 buy-and-hold, ~3 pp more return, ~1/3 less volatility.

## The WHY
**Pattern:** Fed information flow: board meetings and Fed communication cluster in even weeks; stock gains follow news of easier policy.




## Setting
- Markets: US equities, international
- Instruments: CRSP VW index, MSCI
- Period: 1994-2013 (+1982-1993)  Frequency: daily  Holding: 5 trading days

## Reported results
From 1994 to 2013 the whole US equity premium was earned in even weeks of FOMC cycle time (weeks 0, 2, 4, 6 counted from the scheduled meeting); odd weeks were flat or negative. Staying out in odd weeks doubled the Sharpe ratio (≈0.4 → 0.8).

## Tradable edge (our framing)
New spec fomc_cycle_even_weeks_es: hold ES only in even FOMC weeks (daily close-to-close). Public FOMC calendar (approved for the bundle).

## Angles to test

## Decay risk: high
Widely publicized since 2015; later evidence suggests the pattern weakened after 2016.

## Data fit
ES 1-min Dec 2013 → Sep 2026, NQ 1-min Jul 2021 → Sep 2026 (2024+ protected in the backtest project).

## Caveats
- Read by Claude in a chat session (manual run 5, 2026-11-10), not by the weekly pipeline.
