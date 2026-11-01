# The Unintended Consequences of Rebalancing

**Authors:** Campbell R. Harvey, Michele G. Mazzoleni, Alessandro Melone  
**Year:** 2026  **Type:** academic  **Read:** full_pdf  
**Source:** https://www.edhec.edu/sites/default/files/2026-03/Scientific%20paper.%20ssrn-5122748.pdf

> Predictable pension/balanced-fund rebalancing (calendar month-end and threshold) moves prices: a 1-SD signal is followed by ~16-17 bps lower next-day equity returns; a long/short S&P vs 10-year note futures strategy front-running it earned ~10%/yr, Sharpe 1.11 (1997-2023).

## Findings
- Threshold signal: 1 SD → about −16 bps next-day equity excess return, +4 bps bonds; gone within two weeks. — *Simulated 60/40 ES/ZN portfolio, 1997-2023.*
- Calendar signal: 1 SD → about −17 bps equities; only significant around month end; peaks in the last four trading days; stronger into quarter end. — *Last-week interaction ≈ −0.30 (t ≈ −3.8).*
- Front-running long/short ES vs ZN: ~10.2%/yr excess, vol 9.2%, Sharpe 1.11; alphas ~9.5% (t > 4); Sharpe ~1 after costs, ~0.90 excluding crises.
- Cost to funds ~8 bps/yr ≈ $16bn; random rebalancing dates would cut it to ~0.6 bps.

## The WHY
**Pattern:** Institutional constraint: funds rebalance back to fixed weights on a calendar and when drift exceeds thresholds, at predictable times.

After equities outperform bonds during a month, 60/40 funds must sell equities in the last days of the month (and buy after underperformance).


## Setting
- Markets: US equity and Treasury futures
- Instruments: ES, ZN
- Period: 1997-2023  Frequency: daily  Holding: last ~4 days of the month, reverses within ~6 days

## Reported results
1 SD rebalancing signal → −16/−17 bps next-day equities; ES/ZN long-short Sharpe 1.11.

## Tradable edge (our framing)
ES-only version: in the last 4 trading days of the month, short ES if equities strongly outperformed bonds month-to-date (expected rebalancing sales), long if they underperformed. Needs bond returns — we have no ZN data, so use a proxy or add ZN data.

## Angles to test
- ES side only, signal from ES month-to-date return vs a bond proxy
- Interaction with Dash for Cash month-end long

## Decay risk: medium
Published 2025-2026 with press coverage; the effect only appeared after the late 1990s.

## Data fit
ES 1-min Dec 2013 → Sep 2026, NQ 1-min Jul 2021 → Sep 2026 (2024+ protected in the backtest project). Treasury futures (ZN) are NOT in the inventory — the full signal needs bond returns.

## Caveats
- Rebalancing activity is estimated from proxies, not observed trades.
- Read by Claude in a chat session (manual run 2), not by the weekly pipeline.
