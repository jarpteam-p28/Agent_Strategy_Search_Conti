# Noise-Band Intraday Momentum in Nasdaq-100 Futures

**Authors:** Justin Chuk  
**Year:** 2026  **Type:** academic  **Read:** full_pdf  
**Source:** https://ssrn.com/abstract=7609644

> The Zarattini noise-band momentum rule rebuilt for 1 MNQ with an unattended-execution design (5-min bars, entries only at :00/:30 10:00-15:30, resting trailing stop at the nearer of band/VWAP moved every 5 min, flat 15:55) earns +$10.26/day net (95% CI +$3.27 to +$17.25), daily Sharpe 1.14, 2020-Jul 2026; 2014-2019 was flat; one point of stop slippage removes 22% of the edge.

## Findings
- Frozen build: +$10.26/day net of $2/RT, 2,184 trades, trades ~60% of sessions, positive every year 2020-2026 but 2020 (+$49) and 2025 (+$835) near flat. — *Databento NQ 1-min, 2020-07/2026; Table 2.*
- Published 1-min rule +$12.16/day → 5-min +$11.57 → resting stop +$10.05 → with VWAP-side filter +$10.26. — *Table 3.*
- Stress: stop one bar late +$9.52; +1 pt slippage on every stop +$7.98; both +$7.39 (2024-26 only +$5.87). — *Table 4.*
- 3-year bootstrap max drawdown at 1 MNQ: median $1,926, 95th pct $3,406 ($4,081 stressed) ⇒ needs $150K prop account (breaches $3,000 limit in 10-21% of paths). — *Table 5.*
- 2014-2019 flat on NQ — behaviour changed around 2020; one of 2 survivors among 144 pre-registered tests (in-sample); companion 30-min ORB rule correlated 0.34.

## The WHY
**Pattern:** Large investors executing through the day + option-hedging demand push late-morning breaks further (Gao et al. 2018; Baltussen et al. 2021).




## Setting
- Markets: US index futures
- Instruments: NQ / MNQ
- Period: 2020-2026 (2014-2019 checked)  Frequency: 1-min / 5-min  Holding: intraday

## Reported results
The Zarattini noise-band momentum rule rebuilt for 1 MNQ with an unattended-execution design (5-min bars, entries only at :00/:30 10:00-15:30, resting trailing stop at the nearer of band/VWAP moved every 5 min, flat 15:55) earns +$10.26/day net (95% CI +$3.27 to +$17.25), daily Sharpe 1.14, 2020-Jul 2026; 2014-2019 was flat; one point of stop slippage removes 22% of the edge.

## Tradable edge (our framing)
Strongly relevant: same rule family as noise_area_momentum_es (our ES result PF 1.08; NQ is where it works). Adds an executable NQ variant to run in the Dual Noise Zone NQ full validation (Tier 4-C): 5-min bars, resting stop moved every 5 min, 1 MNQ, $2/RT, 15:55 flat, plus the 1-pt stop-slippage stress.

## Angles to test

## Decay risk: medium
Edge concentrated 2021-2024; 2025 near flat; in-sample from 144 tests.

## Data fit
ES 1-min Dec 2013 → Sep 2026, NQ 1-min Jul 2021 → Sep 2026 (2024+ protected).

## Caveats
- Companion paper (Chuk 2026, regime-dependent 30-min ORB on NQ with a complete negative-result registry) not yet read — worth getting.
- Read by Claude in a chat session (manual run 5, 2026-11-10) from a file Pablo supplied.
