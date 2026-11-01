# Gamma Fragility

**Authors:** Andrea Barbon, Andrea Buraschi  
**Year:** 2021  **Type:** academic  **Read:** abstract_only  
**Source:** https://abarbon.com/papers/gamma-fragility

> Across a large panel of equity options, dealers' aggregate gamma imbalance shapes intraday returns: negative gamma → intraday momentum, positive gamma → intraday reversal, both stronger when the underlying is illiquid; gamma imbalance also relates to flash crashes.

## Findings
- Negative ex-ante dealer gamma → intraday momentum; positive → intraday reversal. — *Delta-hedging feedback.*
- Effects stronger with higher illiquidity; strongest in the least liquid stocks.
- Gamma imbalance linked to frequency and size of flash crashes.

## The WHY
**Pattern:** Execution mechanics: dealers' delta hedging amplifies (short gamma) or dampens (long gamma) price moves.

Short-gamma dealers buy rallies and sell drops; long-gamma dealers do the opposite.


## Setting
- Markets: US equity options
- Instruments: stocks
- Period: to 2021  Frequency: intraday  Holding: intraday

## Reported results
Gamma sign decides momentum vs reversal.

## Tradable edge (our framing)
A regime switch for our momentum strategies: favour Noise Area / last-30-minute momentum when dealers are short gamma (proxy: after market drops / high volatility), and expect reversals when long gamma (quiet, rising markets).

## Angles to test
- Gamma proxy (prior-day return < 0 or AvgRange above median) as a filter on momentum specs

## Decay risk: medium
0DTE changed dealer positioning after 2022.

## Data fit
ES 1-min Dec 2013 → Sep 2026, NQ 1-min Jul 2021 → Sep 2026 (2024+ protected in the backtest project).

## Caveats
- Abstract only; we have no dealer-gamma data, only proxies.
- Read by Claude in a chat session (manual run 2), not by the weekly pipeline.
