# Overnight-Intraday Reversal Everywhere (Market Closure and Short-Term Reversal)

**Authors:** Pasquale Della Corte, Robert Kosowski, Tianyu Wang  
**Year:** 2016  **Type:** academic  **Read:** web_fetch  
**Source:** https://www.cxoadvisory.com/technical-trading/overnightintraday-return-reversal-trading/

> A cross-sectional strategy buying overnight losers and selling overnight winners for the next day session earned huge gross returns in US stocks (1.68%/day gross, 1993-2014), much weaker in futures including index futures, and it depends on trading right at the open.

## Findings
- CO-OC reversal (overnight losers beat winners intraday): 1.68%/day gross, Sharpe 24 (US stocks). — *1993-2014; gross, ~100% daily turnover.*
- Holds across futures asset classes including index futures, but much weaker. — *Futures 1982-2014.*
- Most profit right after the open; a one-minute delay sharply reduces returns.

## The WHY
**Pattern:** Liquidity provision: market closure concentrates order imbalances that reverse when trading resumes.

Overnight price pressure from imbalances reverses once liquidity returns at the open.


## Setting
- Markets: US/global stocks, futures
- Instruments: stocks, index futures
- Period: 1982-2014  Frequency: daily open/close  Holding: open to close

## Reported results
Overnight-to-intraday reversal everywhere, strongest in stocks.

## Tradable edge (our framing)
Supports overnight_reversal_first_hour_es; the cross-sectional stock version needs stock data we don't have.

## Angles to test
- Single-instrument version on ES/NQ = existing spec

## Decay risk: medium
Gross results; extremely sensitive to execution speed and costs.

## Data fit
ES 1-min Dec 2013 → Sep 2026, NQ 1-min Jul 2021 → Sep 2026 (2024+ protected in the backtest project).

## Caveats
- Read by Claude in a chat session (manual run 2), not by the weekly pipeline.
