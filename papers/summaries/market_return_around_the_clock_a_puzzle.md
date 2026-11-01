# Market Return Around the Clock: A Puzzle

**Authors:** Oleg Bondarenko, Dmitriy Muravyev  
**Year:** 2023  **Type:** academic  **Read:** web_fetch  
**Source:** https://ideas.repec.org/a/cup/jfinqa/v58y2023i3p939-967_1.html

> On E-mini S&P futures 2004-2018, essentially the whole average return was earned in the 'EU-open' window (23:30-03:30 ET): 7.6% a year, Sharpe 1.67, t = 6.4; the other ~20 hours averaged about zero.

## Findings
- The EU-open window (11:30 pm to 3:30 am ET) accounts for essentially all of the E-mini S&P 500's average return. — *7.6% annualised, Sharpe 1.67, t = 6.4; rest of the day about -0.8% a year. Tick data 2004-2018.*
- The pattern is positive in every year, calendar month and weekday, and similar in both halves of the sample. — *Trade-price and mid-quote returns nearly identical; Bonferroni-type tests reported.*
- A buy-before / sell-after EU-open rule is profitable after conservative costs, and better when VIX and Asian-session volatility are rising. — *Timing version: Sharpe about 1.2 after costs, high out-of-sample R2; capacity about $50m a year (as reported in the Alpha Architect summary).*
- VIX futures rise during Asian hours and fall sharply around the European open. — *Used as evidence for uncertainty resolution.*

## The WHY
**Pattern:** Risk premium for bearing uncertainty, paid when information that built up while the US was closed is resolved by European investors.

Uncertainty accumulates during Asian hours (VIX futures rise); European participants process it at their open; the uncertainty premium is realised in that window.

- **Who is forced / predictable:** Holders of equity exposure through the Asian session bear unresolved uncertainty and are paid when it resolves.
- **Why it persists:** Thin, operationally awkward window for most US investors; capacity is limited (~$50m/yr).
- **What would kill it:** Overnight trading becoming crowded (ETFs/24h trading), or the uncertainty pattern in VIX disappearing. See Boyarchenko et al. (2026): the 2-3am drift has averaged ~0 since 2021.
- **Paper's view vs ours:** Authors favour uncertainty resolution and reject inventory risk; Boyarchenko, Larsen & Whelan argue for dealer inventory risk from closing imbalances. Both predict the same window, different conditioning variables.

## Setting
- Markets: CME E-mini S&P 500 futures
- Instruments: ES
- Period: 2004-2018  Frequency: tick  Holding: 4 hours (23:30-03:30 ET)

## Reported results
EU-open window: 7.6%/yr, Sharpe 1.67, t = 6.4; rest of day ~0.
- Timing rule Sharpe ~1.2 after costs
- Positive every year/month/weekday 2004-2018
- Costs: Conservative estimates (not detailed in the summary read).

## Tradable edge (our framing)
Hold ES only in the European-open window (about 23:30-03:30 ET, or the tighter 02:00-03:00 ET), flat otherwise. Condition on rising Asian-session volatility. Must be checked post-2021, when the related 2-3am drift reportedly vanished.

## Angles to test
- Long ES 23:30→03:30 ET every night vs 02:00→03:00 ET
- Only when the prior US session closed down (Boyarchenko asymmetry) or Asian-session range is above its 15-day average
- Split 2014-2020 vs 2021-2023 (decay test)

## Decay risk: high
Published 2020-2023; the same authors' window (2-3am) has averaged ~0 since 2021 per Boyarchenko et al. (2026).

## Data fit
ES 1-min (ETH + RTH) Dec 2013 → Sep 2026 in clean_ES_master.parquet; NQ 1-min Jul 2021 → Sep 2026. 2024+ is protected in the backtest project. ETH bars cover the window.

## Caveats
- Read via the Alpha Architect summary and the abstract listing, not the full PDF; numbers are as reported there.
- Sample ends 2018; ES overnight volume roughly doubled in 2020.
- Read by Claude in a chat session (manual run), not by the weekly pipeline.
