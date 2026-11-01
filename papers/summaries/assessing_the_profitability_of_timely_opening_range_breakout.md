# Assessing the Profitability of Timely Opening Range Breakout on Index Futures Markets

**Authors:** Yi-Cheng Tsai, Mu-En Wu, Jia-Hao Syu, Chin-Laung Lei, Chung-Shu Wu, Jan-Ming Ho, Chuan-Ju Wang  
**Year:** 2019  **Type:** academic  **Read:** full_pdf  
**Source:** https://scispace.com/pdf/assessing-the-profitability-of-timely-opening-range-breakout-1elg30dvq5.pdf

> A 'timely' opening range breakout — range from the start of the stock market's active hours to a probe time, trade the first break, exit at the end of active hours — earned > 8%/yr after 0.01% costs on E-mini DJIA, S&P 500, Nasdaq-100, HSI and TAIEX (2001-2013); best probe times were 1 minute for ES and NQ, 4 for YM.

## Findings
- All five index futures: annual returns > 8%, one-tailed p < 3%, after 0.01% per-trade costs. — *1-minute data, E-mini S&P/NQ 2001-2013, YM 2003-2013.*
- Best probe times: S&P 500 1 min, Nasdaq 1 min, DJIA 4 min, HSI 151 min, TAIEX 37 min; Nasdaq best ≈ 17.5%/yr. — *Probe time picked on the full sample (in-sample selection).*
- Classic Brock et al. trading-range breakouts (10-day holds) were not significant on most markets.
- On TAIEX, the breakout direction lines up with institutional (especially foreign) net buying. — *Non-public TAIEX transaction data 2006-2013.*

## The WHY
**Pattern:** Execution mechanics / informed institutional order flow concentrated at the open.




## Setting
- Markets: US and Asian index futures
- Instruments: ES, NQ, YM, HSI, TAIEX
- Period: 2001-2013  Frequency: 1-minute  Holding: intraday (to session end)

## Reported results
A 'timely' opening range breakout — range from the start of the stock market's active hours to a probe time, trade the first break, exit at the end of active hours — earned > 8%/yr after 0.01% costs on E-mini DJIA, S&P 500, Nasdaq-100, HSI and TAIEX (2001-2013); best probe times were 1 minute for ES and NQ, 4 for YM.

## Tradable edge (our framing)
Covered by T5 (opening range breakout) in VOLATILITY_BREAKOUT_RESEARCH_TESTS.md; adds a 1-minute opening-range variant for ES/NQ. Note the 0.01% cost assumption (~1 ES point at 6,000+) and in-sample probe selection; the 2026 MNQ falsification study found ORB not significant after costs.

## Angles to test
- Add 1-minute opening range to T5

## Decay risk: high
Ends 2013; recent MNQ study found ORB long not significant (t = 0.88).

## Data fit
ES 1-min Dec 2013 → Sep 2026, NQ 1-min Jul 2021 → Sep 2026 (2024+ protected in the backtest project).

## Caveats
- Read by Claude in a chat session (manual run 4), not by the weekly pipeline.
