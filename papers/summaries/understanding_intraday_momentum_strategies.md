# Understanding Intraday Momentum Strategies

**Authors:** C. Rosa  
**Year:** 2022  **Type:** academic  **Read:** abstract_only  
**Source:** https://ideas.repec.org/a/wly/jfutmk/v42y2022i12p2218-2234.html

> Intraday momentum predictability disappears in the out-of-sample period; a Markov-switching model finds two regimes, and predictability depends on signal strength — calendar-time tests can mislead when anomalies have time-varying returns.

## Findings
- Predictability disappears out of sample. — *Journal of Futures Markets 42(12), 2022.*
- Two regimes; predictability depends on the strength of the signal. — *Markov-switching model.*

## The WHY
**Pattern:** Regime-dependent momentum (works in strong-signal / volatile regimes).




## Setting
- Markets: futures (journal)
- Instruments: not stated
- Period: not stated  Frequency: intraday  Holding: last half hour

## Reported results
Intraday momentum gone out of sample, except in strong-signal regimes.

## Tradable edge (our framing)
Warning for noise_area_last_half_hour_es and Dual Noise Zone: test strength-dependence (dose-response by band distance) and regimes, not just the unconditional average.

## Angles to test
- Dose-response by signal strength
- Volatility-regime split

## Decay risk: high
Out-of-sample failure reported.

## Data fit
ES 1-min Dec 2013 → Sep 2026, NQ 1-min Jul 2021 → Sep 2026 (2024+ protected in the backtest project).

## Caveats
- Read by Claude in a chat session (manual run 2), not by the weekly pipeline.
