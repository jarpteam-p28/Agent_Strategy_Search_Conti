# Do S&P500 Options Increase Market Volatility? Evidence from 0DTEs

**Authors:** Greg Adams, Jean-Sébastien Fontaine, Chayawat Ornthanalai, Chukwuma Dim  
**Year:** 2025  **Type:** academic  **Read:** web_fetch  
**Source:** https://quantpedia.com/do-sp500-0dtes-options-increase-market-volatility/

> 0DTE options did not raise S&P 500 volatility — index volatility was ~60 bps (annualized) lower on 0DTE days; dealers are net LONG gamma on expiration days, which predicts lower 10-minute volatility and stronger short-term reversal in E-mini order flow.

## Findings
- Index volatility ≈ 60 bps annualized lower on days with 0DTE trading (before daily expiries, May 2022). — *Tue/Thu natural experiment.*
- Each 1 bp rise in hedging needs ≈ 4 bp lower realized volatility. — *Two-stage estimate.*
- Dealers net long gamma on expiration days; higher net gamma predicts lower volatility over ~10 minutes (fades within an hour), stronger E-mini order-flow reversals and negative high-frequency momentum.

## The WHY
**Pattern:** Execution mechanics: long-gamma dealer hedging dampens moves and produces short-term reversal.

Dealers holding positive gamma sell into rallies and buy dips while hedging.


## Setting
- Markets: S&P 500 options and E-mini futures
- Instruments: SPX 0DTE, ES
- Period: to 2025  Frequency: intraday (minutes)  Holding: 10-60 minutes

## Reported results
0DTE dampens volatility; long dealer gamma → short-term reversal.

## Tradable edge (our framing)
Context: since 2022 the close and intraday may be more mean-reverting; every momentum spec must report pre/post 2022 separately.

## Angles to test
- Pre/post May 2022 split in all intraday momentum tests

## Decay risk: low
Structural observation.

## Data fit
ES 1-min Dec 2013 → Sep 2026, NQ 1-min Jul 2021 → Sep 2026 (2024+ protected in the backtest project).

## Caveats
- Read by Claude in a chat session (manual run 2), not by the weekly pipeline.
