# Night Moves: Is the Overnight Drift the Grandmother of All Market Anomalies?

**Authors:** Nina Boyarchenko, Lars C. Larsen, Paul Whelan  
**Year:** 2022  **Type:** academic  **Read:** full_pdf  
**Source:** https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr917.pdf

> ES futures earn a large, very significant return between 02:00 and 03:00 ET as European cash markets open (1.48 bp/day, t = 7.1, 1998-2020), larger after US closing sell imbalances; long-only the hour loses to the spread, but a 'buy-the-dip' version (only after a negative closing imbalance) keeps a post-cost Sharpe ≈ 1.1.

## Findings
- 02:00-03:00 ET mean 1.48 bp/day (≈ 3.7%/yr), t = 7.1; the only hour surviving multiple-testing adjustment. — *ES mid-quotes 1998-2020.*
- Negative signed volume 15:15-16:15 predicts the drift (coefficient −17.5); reversal after sell-offs much stronger than after rallies; larger when VIX is high. — *Volume data 2007-2020.*
- Long the hour: pre-cost Sharpe 1.1, post-cost ≈ −0.5; 01:30-03:30 window ≈ 0.3 post-cost; buy-the-dip ≈ 1.1 post-cost. — *Strategies 2004-2020.*
- Positive in 20 of 23 years; shifts with daylight-saving time differences between US and Europe.

## The WHY
**Pattern:** Dealer inventory: US-close selling leaves dealers long; they need compensation until European liquidity arrives.




## Setting
- Markets: US index futures
- Instruments: ES
- Period: 1998-2020  Frequency: 1-minute  Holding: 1 hour overnight

## Reported results
ES futures earn a large, very significant return between 02:00 and 03:00 ET as European cash markets open (1.48 bp/day, t = 7.1, 1998-2020), larger after US closing sell imbalances; long-only the hour loses to the spread, but a 'buy-the-dip' version (only after a negative closing imbalance) keeps a post-cost Sharpe ≈ 1.1.

## Tradable edge (our framing)
Already covered by europe_open_long_es (its conditioned 'after a down session' and 'large last-30-min move' variants are the buy-the-dip version). Added the DST note to that spec.

## Angles to test

## Decay risk: high
Same authors later documented the drift disappearing after 2021 ('The Disappearing Overnight Drift').

## Data fit
ES 1-min Dec 2013 → Sep 2026, NQ 1-min Jul 2021 → Sep 2026 (2024+ protected in the backtest project).

## Caveats
- Read by Claude in a chat session (manual run 5, 2026-11-10), not by the weekly pipeline.
