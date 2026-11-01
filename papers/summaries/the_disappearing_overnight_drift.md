# The Disappearing Overnight Drift

**Authors:** Nina Boyarchenko, Lars C. Larsen, Paul Whelan  
**Year:** 2026  **Type:** industry  **Read:** web_fetch  
**Source:** https://libertystreeteconomics.newyorkfed.org/2026/07/the-disappearing-overnight-drift/

> The 2-3am ET ES drift that earned ~3.7%/yr in 1998-2020 has averaged close to zero in 2021-2025 (also NQ and YM); the authors trace it to closing order imbalances becoming much less dispersed.

## Findings
- The 2:00-3:00 am ET window earned ~3.7% a year (more than 60% of ES's 5.9% close-to-close return) in 1998-2020, and close to zero since 2021. — *Post-publication sample Jan 2021-Dec 2025, 1,245 trading days; same in NQ and YM.*
- The dispersion of closing order imbalances fell by more than half. — *SD of end-of-day relative signed volume 6.5% → 2.9%; VIX mean 20.4 → 19.4; overnight share of volume 15% → 16%.*
- The closing-imbalance → overnight-return link is much weaker in 2021-25. — *Spread between imbalance-sorted return bins much narrower.*
- NightShares overnight ETFs (NSPY, NIWM), launched June 2022, closed after ~14 months. — *Authors call this consistent with the weakened pattern (ETF costs also played a part).*

## The WHY
**Pattern:** Inventory risk premium that depends on closing imbalances; it fades when any of imbalance dispersion, variance or dealer capacity collapses.

Closing limit orders became smaller (finer algorithmic slicing), so dealers carry less overnight inventory and earn less premium.

- **What would kill it:** Already weakened; it could return if closing-imbalance dispersion widens again (authors' prediction).

## Setting
- Markets: CME equity index futures
- Instruments: ES, NQ, YM
- Period: 1998-2020 vs 2021-2025  Frequency: intraday  Holding: 1 hour (02:00-03:00 ET)

## Reported results
Pre-2021 ~3.7%/yr in the 2-3am window; 2021-2025 ~0.
- Imbalance SD 6.5% → 2.9%

## Tradable edge (our framing)
Not a strategy on its own — a kill/regime switch for any overnight-drift strategy: trade the European-open long only when closing-imbalance proxies are large (e.g. a big last-30-minute move), otherwise stay flat.

## Angles to test
- Regime switch: trade overnight long only after days with an unusually large last-30-minute move (imbalance proxy)
- Report every overnight strategy pre/post 2021

## Decay risk: high
This paper documents the decay.

## Data fit
ES 1-min (ETH + RTH) Dec 2013 → Sep 2026 in clean_ES_master.parquet; NQ 1-min Jul 2021 → Sep 2026. 2024+ is protected in the backtest project. Our ES data covers both regimes (2014-2020 vs 2021-2023 in development).

## Caveats
- Authors' blog summary of the SSRN paper; full PDF not reached.
- Read by Claude in a chat session (manual run), not by the weekly pipeline.
