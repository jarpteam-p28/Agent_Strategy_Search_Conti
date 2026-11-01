# Market Intraday Momentum

**Authors:** Lei Gao, Yufeng Han, Sophia Zhengzi Li, Guofu Zhou  
**Year:** 2018  **Type:** academic  **Read:** web_fetch  
**Source:** https://cxoadvisory.com/calendar-effects/first-and-last-half-hours-of-trading-linked

> The first half-hour return (from the previous close) predicts the last half-hour return on SPY (R² ≈ 2%, up to 4.8% on high-volatility days); timing the last half hour on that sign earned 6.3%/yr gross vs -0.5% always-in, before costs.

## Findings
- The first half-hour return explains ~2% of the variance of the last half-hour return; adding the 12th half-hour raises R² to ~3.5%, ~4.8% when first half-hour volatility is high. — *SPY from 1999 and QQQ from 1999 to 2012 (working-paper version).*
- Stronger in recessions and on macro-news days (2006-2009 R² 0.043 / 0.071).
- Out-of-sample R² up to 1.8% (first half-hour) and 2.7% (combined).
- Holding SPY in the last half hour only when the first half hour was up: 6.3%/yr gross; always holding the last half hour: -0.5%/yr. — *Before costs.*
- Independent replication Aug 2012-May 2014: correlation 0.12, R² 1.4%, driven by extreme first-hour moves. — *CXO Advisory.*

## The WHY
**Pattern:** Late-informed traders and short-gamma hedging push the close in the direction of the morning move.

Information digested slowly; forced hedgers trade near the close (see Baltussen et al. 2021).


## Setting
- Markets: US equity ETFs
- Instruments: SPY, QQQ
- Period: 1999-2012 (working paper); published JFE 2018  Frequency: half-hour  Holding: last 30 minutes

## Reported results
R² ≈ 2% (higher on volatile days); timing strategy 6.3%/yr gross.
- OOS R² up to 2.7%
- Costs: No — costs would 'swamp returns' per the replication.

## Tradable edge (our framing)
Covered by noise_area_last_half_hour_es (baseline B2 = direction of the day's move into 15:30). Costs are the main risk.

## Angles to test
- Already a baseline in the last-30-minutes sheet

## Decay risk: medium
Published 2018; small R²; cost-sensitive.

## Data fit
ES 1-min (ETH + RTH) Dec 2013 → Sep 2026 in clean_ES_master.parquet; NQ 1-min Jul 2021 → Sep 2026. 2024+ is protected in the backtest project.

## Caveats
- Read via the CXO Advisory summary of the working-paper version, not the JFE PDF.
- Upgraded from the earlier abstract-only summary.
- Read by Claude in a chat session (manual run), not by the weekly pipeline.
