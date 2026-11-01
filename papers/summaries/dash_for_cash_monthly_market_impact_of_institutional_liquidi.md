# Dash for Cash: Monthly Market Impact of Institutional Liquidity Needs

**Authors:** Erkko Etula, Kalle Rinne, Matti Suominen, Lauri Vaittinen  
**Year:** 2020  **Type:** academic  **Read:** full_pdf  
**Source:** https://academic.oup.com/rfs/article/33/1/75/5494694

> Institutions sell to raise month-end cash (peak at T-4 under 3-day settlement, pushing prices down T-8 to T-4) and buy back from T-1 to T+3; US stocks earned about +25 bps in the T-3 to T-1 reversal and ~+48 bps T-3 to T+3 (1995-2013).

## Findings
- Monthly cycle around the last trading day T: T-8..T-4 'selling pressure' (avg daily -0.03%, abnormal ≈ -37 bps/month); T-3..T-1 'positive reversal' (avg daily +0.12%, ≈ +25 bps); T..T+3 buying pressure (T-3..T+3 ≈ +48 bps); T+4..T+8 negative reversal. — *CRSP value-weighted, Jul 1995-Dec 2013.*
- 2003-2013: cumulative excess returns in the T-3..T-1 window were 103%, about 73% of the market's total excess return. — *Correlation between the two windows -0.54.*
- Timing follows settlement: 3-day settlement pushes month-end selling to T-4; Europe's move to 2-day settlement (Oct 2014) shifted the pattern (T-2 autocorrelation fell by 0.78, t ≈ -3.2 to -3.7). — *Quasi-natural experiment.*
- Reversals are 2-3x larger when the month ends on a Friday (pension + weekly salary cycles coincide).
- Present in 20 of 23 developed markets; strongest in large, liquid stocks. — *All 23 correlations negative.*

## The WHY
**Pattern:** Institutional constraint / payment cycles: funds must raise cash for month-end payouts and do it at predictable, settlement-determined times.

Pension and fund payouts at month end → selling timed by settlement lag (T-4 under T+3) → price pressure, then reversal and re-investment buying T-1..T+3.

- **Who is forced / predictable:** Mutual funds, pensions and other institutions meeting month-end cash obligations.
- **Why it persists:** Payment calendars and settlement rules are fixed; agency concerns delay selling to the last moment.
- **What would kill it:** Settlement changes (US moved to T+2 in Sept 2017 and T+1 in May 2024 — the window should shift accordingly), spreading of payouts across the month.
- **Paper's view vs ours:** Agree; key for us is that the window must be shifted with each US settlement change.

## Setting
- Markets: US and 22 developed equity markets, bonds
- Instruments: CRSP VW index, national indices
- Period: 1995-2013 (some from 1980)  Frequency: daily  Holding: 3-7 trading days

## Reported results
T-3..T-1 ≈ +25 bps/month, T-3..T+3 ≈ +48 bps; T-8..T-4 ≈ -37 bps.
- 2003-2013: T-3..T-1 window = 73% of market excess return
- Friday month-ends 2-3x stronger
- Costs: No trading strategy backtested.

## Tradable edge (our framing)
Long ES from the close of the peak-selling day to month end (+3 days); flat (or short) during the selling window. Settlement-adjusted timing: T+3 era (to Sept 2017) buy at close T-4; T+2 era (Sept 2017-May 2024) buy at close T-3; T+1 era buy at close T-2. Exit at close T+3.

## Angles to test
- Settlement-adjusted long window vs the naive TOTM window (baseline)
- Friday month-ends separately
- Short leg T-8..T-4 (shifted)

## Decay risk: medium
Published 2020; structural cash cycle, but settlement changes shift the timing.

## Data fit
ES 1-min (ETH + RTH) Dec 2013 → Sep 2026 in clean_ES_master.parquet; NQ 1-min Jul 2021 → Sep 2026. 2024+ is protected in the backtest project. Daily closes from 1-min bars; ~120 months in 2014-2023.

## Caveats
- Several results 'available on request'; mutual fund flow data only 2007-2013.
- Sample ends before the US T+2 (2017) and T+1 (2024) changes.
- Read by Claude in a chat session (manual run), not by the weekly pipeline.
