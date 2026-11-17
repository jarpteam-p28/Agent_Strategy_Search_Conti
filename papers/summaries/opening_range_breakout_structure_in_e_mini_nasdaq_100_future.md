# Opening Range Breakout Structure in E-Mini NASDAQ-100 Futures

**Authors:** Georgi Yordanov  
**Year:** 2026  **Type:** industry  **Read:** web_fetch  
**Source:** https://researchpaperfilteropen.vercel.app/

> On NQ (Sep 2025-Apr 2026, 159 days, MBO data), with a 09:30-10:05 ET range defined by its 70% volume value area, 71% of breakout days reach 0.5 × the range beyond the break; if price first falls back through the range mid before reaching 0.5×, follow-through drops to 23%; second breakouts reach 0.5× 77% of the time.

## Findings
- Base rate: 71.1% of breakout days reach 0.5× the filter range (stable as the sample grew 78 → 159 days). — *NQ MBO, 159 days.*
- 'Cross + miss': falling back through the range mid before 0.5× → only 22.7% follow-through (−48 pp).
- Second breakout of the day reaches 0.5× 76.5%.
- Positive opening delta 75% vs negative 67.5% (gap narrowing); down-breaks reach 2.0× more often than up-breaks (numbers inconsistent in the paper).
- No costs, entries, stops or sizing modelled; single short period, no out-of-sample.

## The WHY
**Pattern:** Opening-range breakouts carry short continuation; a failed retest of the mid signals the break has no follow-through.




## Setting
- Markets: US index futures
- Instruments: NQ
- Period: 2025-09 to 2026-04  Frequency: tick/MBO  Holding: intraday

## Reported results
71% reach 0.5R; 23% after a cross-and-miss of the mid

## Tradable edge (our framing)
No new spec. Adds two pre-registered checks to ORB_TARGET_STATS_STUDY Part 1: (a) P(reach 0.5R | price closed back through the OR mid first) vs unconditional, (b) second-breakout hit rates. Note his 0.5R hit rate (71%) matches the Deepcharts 'Protection' level idea.

## Angles to test

## Decay risk: medium
Short sample inside our protected period.

## Data fit
ES/NQ 1-min allow the price version (not the volume-profile range or delta). Sample lies in the protected 2024+ period — use only as an idea, never to set parameters.

## Caveats
- Practitioner study, internally inconsistent numbers in places.
- Read by Claude in a chat session (manual run 7, 2026-11-17).
