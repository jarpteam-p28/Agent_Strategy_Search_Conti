# The Pre-FOMC Announcement Drift

**Authors:** David O. Lucca, Emanuel Moench  
**Year:** 2015  **Type:** academic  **Read:** full_pdf  
**Source:** https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr512.html

> The S&P 500 rose ~49 bps on average in the 24 hours before scheduled FOMC announcements (t > 4.5); since 1994 these windows earned ~80% of annual excess stock returns; holding the index only then had a Sharpe of ~1.1.

## Findings
- Average 49 bps in the 2pm-to-2pm window ending 15 minutes before the announcement. — *t > 4.5; other 2pm-to-2pm windows < 0.5 bps.*
- Since 1994 about 80% of realized annual excess returns came in pre-FOMC windows (3.89%/yr vs 0.88% on other days). — *Jan 1980-Mar 2011: about half.*
- No reversal afterwards; just-before-announcement to close ≈ 0.
- Holding only in the window: Sharpe ~1.14 post-1994, 0.92 for 1980-2011.
- European indices show 29-52 bps pre-FOMC returns; Nikkei none; nothing before other central banks.

## The WHY
**Pattern:** Unexplained premium ahead of US monetary-policy news (risk reallocation / inattention partly).

Authors find no single adequate explanation; volatility and liquidity declines explain only part.


## Setting
- Markets: US equities, global indices
- Instruments: S&P 500, ES
- Period: 1980-2011 (strongest 1994-2011)  Frequency: intraday  Holding: 24 hours before FOMC

## Reported results
≈49 bps in 24h before FOMC; ~80% of excess returns since 1994.
- Sharpe ~1.14 (1994-2011)

## Tradable edge (our framing)
Long ES from 14:00 ET the day before a scheduled FOMC decision to 13:45 ET on decision day — but see Kurov et al. (2021): gone after 2015 except when uncertainty (VIX) is high.

## Angles to test
- Condition on high volatility (AvgRange or VIX proxy) before the meeting
- Press-conference meetings only

## Decay risk: high
Kurov, Wolfe & Gilbert (2021) show it disappeared for 2016-2019.

## Data fit
ES 1-min Dec 2013 → Sep 2026, NQ 1-min Jul 2021 → Sep 2026 (2024+ protected in the backtest project).

## Caveats
- FOMC calendar needed (official dates).
- Read by Claude in a chat session (manual run 2), not by the weekly pipeline.
