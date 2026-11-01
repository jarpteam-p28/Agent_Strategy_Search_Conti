# Overnight Returns of Stock Indexes: Evidence from ETFs and Futures

**Authors:** Qingfu Liu, Yiuman Tse  
**Year:** 2017  **Type:** academic  **Read:** abstract_only  
**Source:** https://ideas.repec.org/a/eee/reveco/v48y2017icp440-451.html

> In US index ETFs and most international index futures (1999-2014), overnight returns are positive and daytime returns negative; the overnight return predicts the first half hour NEGATIVELY and the last half hour POSITIVELY, in and out of sample.

## Findings
- Overnight returns significantly positive, trading-hours returns negative; overnight volatility lower. — *US ETFs and most international index futures, 1999-2014 (IREF 48).*
- Overnight return predicts the first-half-hour return negatively (open reversal) and the last-half-hour return positively. — *In-sample and out-of-sample; no magnitudes in the abstract.*
- Not consistent with the usual risk-return tradeoff; trading hours carry most of the risk. — *Copula VaR/ES.*

## The WHY
**Pattern:** Liquidity provision / inventory: overnight moves partly reverse at the open, then the day's direction carries into the close.

Market makers unwind overnight inventory at the open (reversal); close-related flows follow the day (last half-hour continuation).


## Setting
- Markets: US ETFs, international index futures
- Instruments: SPY and sector ETFs, index futures
- Period: 1999-2014  Frequency: intraday (half-hour)  Holding: first and last 30 minutes

## Reported results
Overnight return → first 30 min (−), last 30 min (+).

## Tradable edge (our framing)
Supports two specs already on file: overnight_reversal_first_hour_es (fade the overnight move early) and noise_area_last_half_hour_es (last-30-minute continuation).

## Angles to test
- Use the overnight return as an extra predictor/filter in both specs

## Decay risk: medium
Sample ends 2014; our ES 2015-2023 is out-of-sample.

## Data fit
ES 1-min Dec 2013 → Sep 2026, NQ 1-min Jul 2021 → Sep 2026 (2024+ protected in the backtest project).

## Caveats
- Read by Claude in a chat session (manual run 2), not by the weekly pipeline.
