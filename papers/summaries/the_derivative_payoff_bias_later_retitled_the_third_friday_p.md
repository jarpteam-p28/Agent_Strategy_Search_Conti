# The Derivative Payoff Bias (3rd Friday Price Spike)

**Authors:** Guido Baltussen, Julian Terstegge, Paul Whelan  
**Year:** 2024  **Type:** academic  **Read:** web_fetch  
**Source:** https://www.aeaweb.org/conference/2025/program/paper/N7rsBN2N

> Since 2003, S&P 500 prices drift up from Thursday's close into the 3rd-Friday morning settlement (SOQ, +18.2 bps, t = 4.5) and revert by midday; a long-Thursday-close / short-at-SOQ trade earned ~24 bps per expiry after costs.

## Findings
- On monthly expiration (3rd Friday), the opening settlement price (SOQ) is on average 18.2 bps above Thursday's close since 2003; no effect before 2003. — *t = 4.5.*
- E-mini futures rise overnight, peak around the SOQ calculation, and revert; the reversal completes by midday. — *Overnight futures gain ~14 bps (t ≈ 3.5); SPX open-to-close on 3rd Fridays averages -16.4 bps.*
- A buy-Thursday-close, short-at-SOQ, close-at-Friday-close strategy grew $1 to ~$2.18 by 2021, Sharpe often above 2; mean 27 bps → 24 bps after costs (t ≈ 3.5). — *Backtest on the index via the SOQ (2003-2021), not on ES directly.*
- Appears in DJIA and Nasdaq-100 too; absent for p.m.-settled expiries.
- Call payoffs inflated ~$214m/month, puts deflated ~$80m/month (~$3.5bn/yr lower bound).

## The WHY
**Pattern:** Execution mechanics: option dealers' 'charm' hedging (delta decaying into expiry) forces predictable buying into the settlement.

As expiry nears, dealers' hedges must be adjusted; the net adjustment is buying into the SOQ, which then reverts once settlement is fixed.

- **Who is forced / predictable:** Option dealers hedging expiring a.m.-settled SPX options.
- **Why it persists:** Tied to the expiry calendar and settlement design; published 2023-2024, so crowding is possible.
- **What would kill it:** Changes to SOQ settlement, shift of open interest to p.m.-settled / 0DTE contracts, or arbitrageurs front-running the overnight leg.
- **Paper's view vs ours:** Authors favour charm hedging and leave manipulation untested.

## Setting
- Markets: S&P 500 index and futures
- Instruments: SPX, ES, NQ, YM
- Period: 2003-2021  Frequency: intraday  Holding: Thursday 16:00 → Friday 09:30 (long), 09:30 → 16:00 (short leg)

## Reported results
+18.2 bps Thursday close → SOQ (t = 4.5); ~24 bps per expiry after costs.
- Futures overnight ~14 bps, t ≈ 3.5
- SPX open-to-close on 3rd Fridays -16.4 bps
- Costs: Yes, in the index backtest (27 → 24 bps).

## Tradable edge (our framing)
Monthly ES trade: buy at the Thursday 16:00 ET close before the 3rd-Friday expiry, sell at the Friday 09:30 open (the SOQ); optional second leg short from 09:30 to the close/midday. ~12 trades a year.

## Angles to test
- Long leg only vs long + short legs
- Quarterly (witching) vs monthly expiries
- Pre/post 2022 (0DTE era)
- NQ as second market

## Decay risk: medium
Published 2023-2024 with press coverage ('manipulation talk'); small capacity; settlement-structure dependent.

## Data fit
ES 1-min (ETH + RTH) Dec 2013 → Sep 2026 in clean_ES_master.parquet; NQ 1-min Jul 2021 → Sep 2026. 2024+ is protected in the backtest project. The overnight ETH bars capture the Thursday-close → Friday-open leg.

## Caveats
- Small sample: ~12 trades a year → ~120 in ES 2014-2023.
- The paper backtests the index SOQ, not ES fills; ES 09:30 open is a proxy for the SOQ.
- Read via the AEA program page abstract/details, not the full PDF.
- Read by Claude in a chat session (manual run), not by the weekly pipeline.
