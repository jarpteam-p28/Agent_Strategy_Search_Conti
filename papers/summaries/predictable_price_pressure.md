# Predictable Price Pressure

**Authors:** Samuel M. Hartzmark, David H. Solomon  
**Year:** 2025  **Type:** academic  **Read:** full_pdf  
**Source:** https://nber.org/system/files/working_papers/w30688/w30688.pdf

> Days with large aggregate dividend PAYMENTS (cash reinvested by funds) earn higher market returns: +1 SD payout yield → +3.2 bp that day vs a 4.1 bp mean; above-median payment days earned 7.7%/yr vs 3.5% on other days (1926-2018), effect larger when VIX/illiquidity is high, absent in December.

## Findings
- Payout-yield coefficient 67 (t = 3.47) with year-month fixed effects; days t and t−1 only, placebo on future payments null. — *CRSP 1926-2018; 58 countries 1986-2017.*
- Top-quarter payment days +7.1 bp (t = 4.27).
- Strongest in Q1; no effect in Q4/December.
- Survives day-of-week, turn-of-month, FOMC and macro-announcement controls. — *AER 115(9) 2025.*

## The WHY
**Pattern:** Predictable uninformed buying (dividend reinvestment) moves prices — inelastic markets.




## Setting
- Markets: US equities
- Instruments: CRSP VW index
- Period: 1926-2018  Frequency: daily  Holding: 1-2 days

## Reported results
Days with large aggregate dividend PAYMENTS (cash reinvested by funds) earn higher market returns: +1 SD payout yield → +3.2 bp that day vs a 4.1 bp mean; above-median payment days earned 7.7%/yr vs 3.5% on other days (1926-2018), effect larger when VIX/illiquidity is high, absent in December.

## Tradable edge (our framing)
Testable on ES only with an aggregate S&P 500 dividend PAYMENT-date calendar, which we do not have (needs per-stock pay dates). Parked: dividend_payment_day_long_es would be the spec if a free pay-date calendar is approved.

## Angles to test

## Decay risk: medium
Requires dividend calendar data.

## Data fit
Index-level effect, but needs S&P 500 dividend payment dates (not in Lexar data).

## Caveats
- Read by Claude in a chat session (manual run 5, 2026-11-10), not by the weekly pipeline.
