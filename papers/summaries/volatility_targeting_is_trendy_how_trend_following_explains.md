# Volatility Targeting Is Trendy: How Trend Following Explains Alpha in Volatility-Managed Strategies

**Authors:** Benjamin Hood, Cameron Raughtigan  
**Year:** 2024  **Type:** academic  **Read:** web_fetch  
**Source:** https://mrzepczynski.blogspot.com/2024/07/volatility-targetting-is-trend.html?m=1

> Volatility targeting beats buy-and-hold in equities mainly because of the leverage effect (prices fall when volatility rises); controlling for trend following removes about two-thirds of its alpha across 14 stock indices, and the effect is absent in bonds, commodities and FX.

## Findings
- Controlling for trend following cuts volatility-targeting alpha by about two-thirds (14 stock indices).
- The leverage effect and trend link are equity-specific.

## The WHY
**Pattern:** Volatility targeting in equities behaves like trend following (de-risks in falling, volatile markets).

Leverage effect.


## Setting
- Markets: Equity indices
- Instruments: 14 stock indices
- Period: not stated  Frequency: daily  Holding: n/a

## Reported results
~2/3 of vol-targeting alpha is trend exposure.

## Tradable edge (our framing)
For our VOLATILITY_SIZING view: expect smoother results and smaller drawdowns, not a new edge; on ES it partly duplicates trend exposure.

## Angles to test
- Compare vol-sized vs fixed size on every strategy (already in the sizing view)

## Decay risk: low
Methodological.

## Data fit
ES 1-min Dec 2013 → Sep 2026, NQ 1-min Jul 2021 → Sep 2026 (2024+ protected in the backtest project).

## Caveats
- Read via a blog summary.
- Read by Claude in a chat session (manual run 2), not by the weekly pipeline.
