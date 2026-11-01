# Price Drift before U.S. Macroeconomic News: Private Information about Public Announcements?

**Authors:** Alexander Kurov, Alessio Sancetta, Georg Strasser, Marketa Halova Wolfe  
**Year:** 2019  **Type:** academic  **Read:** full_pdf  
**Source:** https://www.skidmore.edu/economics/documents/KSSW2017-PriceDriftBeforeUSMacroeconomicNews.pdf

> For 9 of 20 market-moving US releases (2008-2014), ES and Treasury futures start moving the 'right' way ~30 minutes before the release, about 40% of the total move on average — consistent with leakage or proprietary nowcasting.

## Findings
- Pre-release drift for 9 of 20 market-moving announcements, starting ~30 minutes before. — *Second-by-second ES and ZN, Jan 2008-Mar 2014.*
- Drift ≈ 49% of the total move for stocks, 36% for bonds; significant for ES on pending home sales, ISM non-manufacturing, ISM manufacturing, existing home sales. — *S&P coefficients ≈ 0.05-0.10 (t ≈ 2.6-6.1).*
- Stronger for non-government releasers and pre-released/embargoed data.
- Weaker or absent in 2003-2007.

## The WHY
**Pattern:** Informed trading before public releases (leakage / superior proprietary forecasting).

Some traders know or predict the number and trade before release; prices drift toward the outcome.


## Setting
- Markets: US futures
- Instruments: ES, ZN
- Period: 2008-2014  Frequency: second-level  Holding: 30 minutes before release

## Reported results
Pre-release drift ≈ 40% of the total move for 9 of 20 releases.

## Tradable edge (our framing)
Not directly tradable (the direction is the surprise, unknown in advance). Possible angle: trade WITH a strong 30-minute pre-release move into ISM/home-sales releases — speculative; also a warning to avoid entries just before those releases.

## Angles to test
- Event filter: avoid new entries 30 minutes before ISM / home-sales releases

## Decay risk: high
Release procedures tightened after 2013 (pre-release lock-ups ended).

## Data fit
ES 1-min Dec 2013 → Sep 2026, NQ 1-min Jul 2021 → Sep 2026 (2024+ protected in the backtest project).

## Caveats
- Strategy would need second-level data and a release calendar.
- Read by Claude in a chat session (manual run 2), not by the weekly pipeline.
