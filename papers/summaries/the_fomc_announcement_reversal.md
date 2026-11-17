# The FOMC Announcement Reversal

**Authors:** Tommaso Baglioni, Ruy Ribeiro  
**Year:** 2022  **Type:** academic  **Read:** secondary  
**Source:** https://cxoadvisory.com/calendar-effects/stock-market-return-reversal-after-fomc-announcements

> On scheduled FOMC days, the S&P 500 reverses the prior 24 hours: buying E-mini at 13:50 ET after a negative prior-24h return (selling after a positive one) and exiting at the close earned ~0.18% per announcement net of spreads, Sharpe ≈ 0.36 (180 announcements, Oct 1997-Jan 2020).

## Findings
- Rule: sign = −sign(prior 24h return), enter 13:50 ET (10 min before the release), exit at the day's close; buys at ask / sells at bid. — *E-mini S&P 500, 180 scheduled FOMC announcements.*
- ≈ +0.18% per announcement net; Sharpe ≈ 0.36. — *Subperiods 1997-2011 and 2011-2020 studied; varies with VIX and policy uncertainty (details behind paywall).*

## The WHY
**Pattern:** Pre-announcement positioning (and the pre-FOMC drift) unwinds once the decision resolves uncertainty.




## Setting
- Markets: US index futures
- Instruments: ES
- Period: 1997-2020  Frequency: intraday  Holding: 13:50 → close

## Reported results
On scheduled FOMC days, the S&P 500 reverses the prior 24 hours: buying E-mini at 13:50 ET after a negative prior-24h return (selling after a positive one) and exiting at the close earned ~0.18% per announcement net of spreads, Sharpe ≈ 0.36 (180 announcements, Oct 1997-Jan 2020).

## Tradable edge (our framing)
New spec fomc_announcement_reversal_es — fully testable on ES/NQ 1-min with the public FOMC calendar.

## Angles to test

## Decay risk: medium
≈ 8 trades/yr; few observations, but our 2014-2023 window is mostly out of sample.

## Data fit
ES 1-min Dec 2013 → Sep 2026, NQ 1-min Jul 2021 → Sep 2026 (2024+ protected in the backtest project).

## Caveats
- Only the abstract / a secondary summary was reachable (SSRN is blocked from chat sessions); numbers not verified against the full paper.
- Read by Claude in a chat session (manual run 6, 2026-11-16), not by the weekly pipeline.
