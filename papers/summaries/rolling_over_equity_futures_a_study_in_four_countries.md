# Rolling Over Equity Futures: A Study in Four Countries

**Authors:** Ronald T. Slivka, Han Qin, Kai Ye  
**Year:** 2020  **Type:** academic  **Read:** full_pdf  
**Source:** https://www.indianjournalofcapitalmarkets.com/index.php/IJF/article/download/123688/99703/340937

> For ES (and FTSE, Nifty, A50) 2016 expirations, ~90% of calendar-spread volume falls in the last 5 days before expiry (ES peak on day 12 of a 15-day window); ES spread volatility rises through the roll window, so rolling earlier lowers risk; spreads stay within a 0.5% no-arbitrage band.

## Findings
- Spread volume > 10% of futures volume from roll-window day 8-11; peaks 40-70% on days 12-14. — *2016 expirations, daily data.*
- Volatility-minimizing roll beats even and stack rolls in US, India, China.

## The WHY
**Pattern:** Execution mechanics of the quarterly roll.




## Setting
- Markets: index futures
- Instruments: ES, FTSE, Nifty, A50
- Period: 2016  Frequency: daily  Holding: -

## Reported results
For ES (and FTSE, Nifty, A50) 2016 expirations, ~90% of calendar-spread volume falls in the last 5 days before expiry (ES peak on day 12 of a 15-day window); ES spread volatility rises through the roll window, so rolling earlier lowers risk; spreads stay within a 0.5% no-arbitrage band.

## Tradable edge (our framing)
No strategy. Backtest hygiene: our continuous ES series should switch on volume (as the data already does) and roll-week days can be flagged as a split.

## Angles to test

## Decay risk: low
Descriptive.

## Data fit
ES 1-min Dec 2013 → Sep 2026, NQ 1-min Jul 2021 → Sep 2026 (2024+ protected in the backtest project).

## Caveats
- Read by Claude in a chat session (manual run 6, 2026-11-16), not by the weekly pipeline.
