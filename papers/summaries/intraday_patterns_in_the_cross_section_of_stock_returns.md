# Intraday Patterns in the Cross-section of Stock Returns

**Authors:** Steven L. Heston, Robert A. Korajczyk, Ronnie Sadka  
**Year:** 2010  **Type:** academic  **Read:** full_pdf  
**Source:** https://arxiv.org/pdf/1005.3535.pdf

> A stock's return in a given half hour predicts its return in the SAME half hour on later days (≈3 bps next day, significant for ~40 days), strongest at the open and close, but the effect is smaller than trading costs in stocks.

## Findings
- Same-half-hour returns persist at daily lags (13, 26, 39 half-hours...), significant for ~40 trading days. — *NYSE stocks 2001-2005, 1,715 firms.*
- Winners-minus-losers spread ≈ 3.01 bps at the same time next day. — *Smallest t at daily lags in week 1: 9.62.*
- Strongest in the first and last half hours; relatively stronger at the close for S&P 500 stocks.
- After paying spreads the strategies lose money (e.g. −14 to −24 bps).

## The WHY
**Pattern:** Predictable demand for immediacy at particular times of day (fund flows, algorithms).




## Setting
- Markets: US equities
- Instruments: NYSE stocks
- Period: 2001-2005  Frequency: half-hour  Holding: one half hour

## Reported results
≈3 bps same-slot persistence; unprofitable after spreads.

## Tradable edge (our framing)
Basis for same_slot_seasonality_es; for ES the cost per trade is much lower than for single stocks, but ~3 bps is still below ES round-trip costs — expect it to fail unless the index-level effect is bigger.

## Angles to test
- Gross vs cost check for same_slot_seasonality_es

## Decay risk: medium
Sample 2001-2005.

## Data fit
ES 1-min Dec 2013 → Sep 2026, NQ 1-min Jul 2021 → Sep 2026 (2024+ protected in the backtest project).

## Caveats
- Read by Claude in a chat session (manual run 2), not by the weekly pipeline.
