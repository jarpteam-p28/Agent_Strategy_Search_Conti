# Short-term market reversals and the S&P 500 index option returns (earlier draft: Implied Variance and Market Index Reversal)

**Authors:** Christopher S. Jones, Sung June Pyun, Tong Wang  
**Year:** 2025  **Type:** academic  **Read:** full_pdf  
**Source:** https://sjpyun.github.io/Rev.pdf

> When implied variance is high, the S&P 500 index, futures and SPY show strong daily reversals, mainly after DOWN moves, strongest around the close and open; a futures rule that bets against the last 30 minutes of the day and holds until 30 minutes after the next open earned slightly over 12 bp/day gross.

## Findings
- Negative serial covariance rises with implied variance and is driven by reversals of negative returns. — *S&P 500 index, futures and SPY 1990-2015.*
- Reversal strongest in prices just after the open; very short-term reversal of the last 20-60 minutes most sensitive to high implied variance.
- Futures strategy: position opposite to (and sized by) the last-N-minute return, close → N minutes after the next open; best N = 20-60; ≈ 12 bp/day for N = 30, gross.
- Reversal stronger when S&P 500 option open interest is high (hedging flows).

## The WHY
**Pattern:** Liquidity / fire-sale pressure at the close and option-hedging flows that unwind overnight.




## Setting
- Markets: US index
- Instruments: S&P 500 index, ES futures, SPY
- Period: 1990-2015  Frequency: intraday/daily  Holding: close → next-day 10:00

## Reported results
When implied variance is high, the S&P 500 index, futures and SPY show strong daily reversals, mainly after DOWN moves, strongest around the close and open; a futures rule that bets against the last 30 minutes of the day and holds until 30 minutes after the next open earned slightly over 12 bp/day gross.

## Tradable edge (our framing)
New spec close_reversal_overnight_es: fade the 15:30-16:00 move, hold to 10:00 next day; condition on high volatility (AvgRange top tercile as VIX proxy).

## Angles to test

## Decay risk: medium
Gross of costs; ~12 bp/day ≈ 0.7 ES points at 6,000 — cost hurdle is close.

## Data fit
ES 1-min Dec 2013 → Sep 2026, NQ 1-min Jul 2021 → Sep 2026 (2024+ protected in the backtest project).

## Caveats
- Read the 2016 working-paper version; the 2025 published title differs.
- Read by Claude in a chat session (manual run 5, 2026-11-10), not by the weekly pipeline.
