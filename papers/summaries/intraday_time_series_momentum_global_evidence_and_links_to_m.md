# Intraday time series momentum: Global evidence and links to market characteristics

**Authors:** Zhuo Li, Athanasios Sakkas, Andrew Urquhart  
**Year:** 2022  **Type:** academic  **Read:** full_pdf  
**Source:** https://reading-9.eprints-hosting.org/95566/1/Accepted-Version.pdf

> The first half-hour return predicts the last half-hour return in 12 of 16 developed markets (2005-2017); the effect is stronger in crises, recessions and illiquid periods; out-of-sample it beats the historical mean in 14 of 16 markets but R² is positive in only 5; returns are before costs.

## Findings
- Pooled first-half-hour coefficient 2.86 (t = 7.53); significant in 12 of 16 markets in-sample. — *Index data, JFM 57, 2022.*
- US predictability concentrated in the financial crisis (scaled coefficient 18.3 vs 4.3 outside).
- Strategy returns roughly double in low-liquidity periods; stronger when information arrives smoothly (frog-in-the-pan).
- Country strategies alpha 2.7-7.5%/yr gross; no transaction costs deducted.

## The WHY
**Pattern:** Late-informed traders and hedgers rebalancing near the close; liquidity-dependent.




## Setting
- Markets: 16 developed equity markets
- Instruments: S&P 500 index and others
- Period: 2005-2017  Frequency: 30-minute  Holding: last 30 minutes

## Reported results
The first half-hour return predicts the last half-hour return in 12 of 16 developed markets (2005-2017); the effect is stronger in crises, recessions and illiquid periods; out-of-sample it beats the historical mean in 14 of 16 markets but R² is positive in only 5; returns are before costs.

## Tradable edge (our framing)
Already covered by the Gao et al. first-half-hour → last-half-hour logic inside noise_area_last_half_hour_es; adds a split to run: by volatility regime (crisis-type days) — the effect may live only in high-volatility tercile.

## Angles to test
- Report last-30 strategy by AvgRange tercile

## Decay risk: high
US effect mostly 2008-2009; gross returns only.

## Data fit
ES 1-min Dec 2013 → Sep 2026, NQ 1-min Jul 2021 → Sep 2026 (2024+ protected in the backtest project).

## Caveats
- Read by Claude in a chat session (manual run 5, 2026-11-10), not by the weekly pipeline.
