# How Much Do Investors Care About Macroeconomic Risk? Evidence from Scheduled Economic Announcements

**Authors:** Pavel Savor, Mungo Wilson  
**Year:** 2013  **Type:** academic  **Read:** full_pdf  
**Source:** https://faculty.wharton.upenn.edu/wp-content/uploads/2012/04/Draft20111128p_edited.pdf

> Excess market returns averaged 11.4 bp on CPI/PPI, employment and FOMC announcement days vs 1.1 bp on other days (difference t = 3.77, 1958-2009): over 60% of the equity premium is earned on ~13% of days, with volatility only ~5% higher.

## Findings
- Announcement days 11.4 bp vs 1.1 bp other days; difference 10.3 bp, t = 3.77; non-announcement returns not different from zero. — *JFQA 48(2), 1958-2009.*
- Sharpe ratio on announcement days ≈ 10× other days.
- Effect holds for each announcement type and survives controls for the size of the surprise.
- T-bill yields fall and long bonds earn more on announcement days (precautionary demand).

## The WHY
**Pattern:** Risk premium for bearing macro 'state variable' risk that is resolved on announcement days.




## Setting
- Markets: US equities
- Instruments: CRSP VW index
- Period: 1958-2009  Frequency: daily  Holding: 1 day

## Reported results
Excess market returns averaged 11.4 bp on CPI/PPI, employment and FOMC announcement days vs 1.1 bp on other days (difference t = 3.77, 1958-2009): over 60% of the equity premium is earned on ~13% of days, with volatility only ~5% higher.

## Tradable edge (our framing)
New spec macro_announcement_day_long_es: hold ES on CPI/PPI/NFP/FOMC days (prior close → day close, plus RTH-only variant). Complements pre_macro_overnight_es (the night before) and pre_fomc_drift_uncertainty_es.

## Angles to test

## Decay risk: medium
Old sample; part of the FOMC piece is the pre-FOMC drift that weakened after 2015.

## Data fit
ES 1-min Dec 2013 → Sep 2026, NQ 1-min Jul 2021 → Sep 2026 (2024+ protected in the backtest project).

## Caveats
- Read by Claude in a chat session (manual run 5, 2026-11-10), not by the weekly pipeline.
