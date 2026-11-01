# Famous Firms, Earnings Clusters, and the Stock Market

**Authors:** Yixin Chen, Randolph B. Cohen, Zixuan (Kevin) Wang  
**Year:** 2020  **Type:** academic  **Read:** web_fetch  
**Source:** https://www.cxoadvisory.com/calendar-effects/three-high-attention-earnings-announcement-clusters-drive-market/

> E-mini S&P futures rose ~0.34% in the 24 hours before the most prominent after-close earnings clusters of famous firms (vs 0.02% on a typical day; Sharpe ~4.5, 1999-2018); holding only ~12 such days a year captured nearly two-thirds of the annual excess return.

## Findings
- Market +0.34% in the 24h before prominent PM (after-close) earnings clusters vs +0.02% typical; normal volatility; annualized Sharpe ~4.5. — *E-mini minute data 1999-2018; 3 most prominent PM clusters in each of Jan/Apr/Jul/Oct, ranked by prior-year Dow Jones news count.*
- ~0.11% the evening before, ~0.23% during the pre-announcement trading day.
- Only after-close clusters; pre-open clusters show no effect.
- No correlation between pre- and post-announcement returns (not leakage).
- ~12 days a year ≈ two-thirds of the annual excess return.

## The WHY
**Pattern:** Attention + short-sale constraints: differences of opinion before high-attention news push prices up.




## Setting
- Markets: US
- Instruments: ES, S&P 500 stocks
- Period: 1999-2018  Frequency: minute  Holding: 24 hours

## Reported results
E-mini S&P futures rose ~0.34% in the 24 hours before the most prominent after-close earnings clusters of famous firms (vs 0.02% on a typical day; Sharpe ~4.5, 1999-2018); holding only ~12 such days a year captured nearly two-thirds of the annual excess return.

## Tradable edge (our framing)
Long ES for the 24 hours before the three most-watched after-close mega-cap earnings clusters each earnings month — see spec famous_earnings_cluster_es.

## Angles to test
- Long ES 16:00 two days before → 16:00 on the announcement day for top PM clusters

## Decay risk: medium
Published 2020; 12 events a year.

## Data fit
ES 1-min covers it; needs a mega-cap earnings calendar (public).

## Caveats
- Read by Claude in a chat session (manual run 3), not by the weekly pipeline.
