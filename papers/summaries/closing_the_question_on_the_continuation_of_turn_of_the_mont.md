# Closing the Question on the Continuation of Turn-of-the-Month Effects: Evidence from the S&P 500 Index Futures Contract

**Authors:** Edwin D. Maberly, Daniel F. Waggoner  
**Year:** 2000  **Type:** academic  **Read:** abstract_only  
**Source:** https://www.atlantafed.org/research/publications/wp/2000/11.aspx

> The classic turn-of-the-month effect (last trading day + first three days of the month) disappeared from S&P 500 futures and the spot index after 1990.

## Findings
- Turn-of-the-month effects in S&P 500 futures disappear after 1990; same for the spot index. — *Atlanta Fed WP 2000-11; TOTM = last trading day + next three trading days.*
- Calendar patterns are tied to market microstructure and can change without notice. — *Authors' caution on out-of-sample conclusions.*

## The WHY
**Pattern:** Institutional constraint / payment cycles (classic TOTM) — weakened as retail moved to mutual funds.

Authors conjecture the shift from direct stock buying to mutual funds changed month-end cash flows.

- **What would kill it:** Already reported dead post-1990 in futures (pre-2000 data).

## Setting
- Markets: S&P 500 futures and spot
- Instruments: SP (big S&P futures)
- Period: to ~2000  Frequency: daily  Holding: 4 days around month end

## Reported results
TOTM effect gone after 1990 in S&P futures.

## Tradable edge (our framing)
No new strategy — a warning for month_end_rebalance_es: the naive TOTM window failed in futures after 1990, so any month-end spec needs the settlement-timed version (Dash for Cash) and must beat this naive window as a baseline.

## Angles to test
- Use the naive TOTM window (T-1 to T+3) as a required baseline in month-end tests

## Decay risk: high
Documents the decay.

## Data fit
ES 1-min (ETH + RTH) Dec 2013 → Sep 2026 in clean_ES_master.parquet; NQ 1-min Jul 2021 → Sep 2026. 2024+ is protected in the backtest project.

## Caveats
- Abstract-level only; no return figures recorded.
- Read by Claude in a chat session (manual run), not by the weekly pipeline.
