# Pinning in the S&P 500 Futures

**Authors:** Benjamin Golez, Jens Carsten Jackwerth  
**Year:** 2012  **Type:** academic  **Read:** abstract_only  
**Source:** https://ideas.repec.org/a/eee/jfinec/v106y2012i3p566-585.html

> S&P 500 futures are pulled toward the at-the-money strike on days when serial options on the futures expire ('pinning'), and pushed away from it just before S&P 500 index options expire ('anti-cross-pinning'); the hedging-driven shift is at least $115 million notional per expiration.

## Findings
- Pinning toward the nearest strike on futures-option expiration days. — *JFE 106(3) 2012.*
- Anti-cross-pinning before index-option expiration.
- Mechanism: delta-hedge rebalancing by market makers as hedges decay, and retail reselling of in-the-money options.

## The WHY
**Pattern:** Dealer delta-hedge decay into expiration pulls price toward heavily-held strikes.




## Setting
- Markets: US index futures
- Instruments: ES
- Period: 1990s-2000s  Frequency: intraday  Holding: afternoon of expiration

## Reported results
S&P 500 futures are pulled toward the at-the-money strike on days when serial options on the futures expire ('pinning'), and pushed away from it just before S&P 500 index options expire ('anti-cross-pinning'); the hedging-driven shift is at least $115 million notional per expiration.

## Tradable edge (our framing)
New quick-screen spec expiration_pin_es: on monthly/weekly ES option expiration afternoons, does price close nearer a round strike (25-pt multiple) than on other days, and does a fade-toward-strike rule pay? Strike open interest is not available — round numbers are the proxy.

## Angles to test

## Decay risk: medium
0DTE growth changed expiration dynamics after 2022.

## Data fit
ES 1-min Dec 2013 → Sep 2026, NQ 1-min Jul 2021 → Sep 2026 (2024+ protected in the backtest project). Needs options positioning / open-interest data we do not have; ES/NQ price data only allows proxies.

## Caveats
- Only the abstract / a secondary summary was reachable (SSRN is blocked from chat sessions); numbers not verified against the full paper.
- Read by Claude in a chat session (manual run 5, 2026-11-10), not by the weekly pipeline.
