# A Profitable Day Trading Strategy For The U.S. Equity Market

**Authors:** Carlo Zarattini, Andrea Barbon, Andrew Aziz  
**Year:** 2024  **Type:** academic  **Read:** web_fetch  
**Source:** https://www.cxoadvisory.com/individual-investing/intraday-trading-of-overactive-stocks-via-opening-range-breakout/

> A 5-minute opening range breakout restricted to 'stocks in play' (top-20 relative volume at the open, price > $5, ADV ≥ 1m, ATR > $0.50), stop at 10% of ATR, exit at the close, 1% risk per trade, 2016-2023.

## Findings
- Universe: all US stocks; daily screen for top-20 relative volume (opening-range volume vs 14-day average ≥ 100%). — *Jan 2016-Dec 2023, $0.0035/share commission.*
- Entry: stop order at the 5-minute range high (if the first 5 minutes were up) or low (if down); stop 10% of 14-day ATR; exit at the close. — *Size so a stop loses 1% of capital, max 4x leverage.*
- Authors report ORB works far better on stocks in play than on all stocks. — *Results not visible in the summary read.*

## The WHY
**Pattern:** News/attention: unusually high opening volume marks stocks with fresh information and order imbalances that persist through the day.




## Setting
- Markets: US equities
- Instruments: stocks in play
- Period: 2016-2023  Frequency: 1-minute  Holding: intraday

## Reported results
Stocks-in-play ORB beats ORB on all stocks (per authors).

## Tradable edge (our framing)
Stocks only — not testable on our data. Index angle: use 'relative opening volume' on ES as an 'index in play' filter for ORB tests (T5 in the volatility study).

## Angles to test
- ES relative-volume filter on the 5-minute ORB

## Decay risk: medium
Published 2024 with a large retail following.

## Data fit
No single-stock data in the inventory.

## Caveats
- Results section not reached.
- Read by Claude in a chat session (manual run 2), not by the weekly pipeline.
