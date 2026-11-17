# Large Bets and Stock Market Crashes

**Authors:** Albert S. Kyle, Anna A. Obizhaeva  
**Year:** 2012  **Type:** academic  **Read:** full_pdf  
**Source:** https://pages.nes.ru/aobizhaeva/Kyle-Obizhaeva-crashes.pdf

> Market-microstructure 'invariance' predicts price impact of large forced sales far better than conventional wisdom: e.g., 1987 portfolio insurance sales (67% of ADV) → predicted −16.8% vs actual −32%; SocGen 2008 −10.8% vs −9.4%; aggregate-market demand elasticity ≈ 0.01, so even ~1-3% of daily volume sold quickly moves index markets materially.

## Findings
- Impact ∝ (dollar volume)^(1/3) × (vol)^(4/3) × order size / volume; k = 5 calibrated on 400k portfolio transitions. — *Full paper.*
- 1929 −46% predicted vs −25% actual; 1987 −17% vs −32%; 2010 flash crash −0.6% vs −5.1% (speed amplified).
- Faster execution increases temporary impact → V-shaped moves.

## The WHY
**Pattern:** Forced, fast selling relative to market depth creates outsized temporary impact that partly reverses.




## Setting
- Markets: US/European equities
- Instruments: indices
- Period: 1929-2010 events  Frequency: event  Holding: -

## Reported results
Market-microstructure 'invariance' predicts price impact of large forced sales far better than conventional wisdom: e.g., 1987 portfolio insurance sales (67% of ADV) → predicted −16.8% vs actual −32%; SocGen 2008 −10.8% vs −9.4%; aggregate-market demand elasticity ≈ 0.01, so even ~1-3% of daily volume sold quickly moves index markets materially.

## Tradable edge (our framing)
No strategy. Supports the flow-to-depth logic of letf_flow_to_depth_last_hour_es and the V-shaped reversal logic of forced_selling_flush_fade_es.

## Angles to test

## Decay risk: low
Theory + case studies.

## Data fit
ES 1-min Dec 2013 → Sep 2026, NQ 1-min Jul 2021 → Sep 2026 (2024+ protected in the backtest project).

## Caveats
- Read by Claude in a chat session (manual run 6, 2026-11-16), not by the weekly pipeline.
