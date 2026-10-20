# Vault Break — PROPOSED rules (not locked; needs Pablo's OK — checklist A1)

Source: Matteo Conti, "A Hedge Fund Manager Just CRACKED Prop Trading (Live On Chart)" (IQ Capital, 2026-10-06,
youtu.be/A0G14JYYVTk), whiteboard, and his on-screen MultiCharts code "VaultBreak NQ - v8 - Longs Only".
Full spec: `strategies/conti/07_vault_break.yaml`. TradingView version: `indicators/tradingview/vault_break_strategy.pine`.

## A1 — Rules
- **Instrument / bars:** NQ continuous front month, 30-minute bars built from 1-minute data. Long only. 1 contract.
- **Time zone:** all times **Chicago (CT)**, as in his code ("ALL TIME INPUTS ARE CT").
- **Session:** a bar belongs to the date of its **close** time (MultiCharts convention). Session = bars closing from
  00:00 CT through 16:00 CT. On 30-min bars the first bar is 23:30–00:00 CT.
- **Session open (SessOpen):** open of the first bar of the session.
- **Average range (BoundaryATR):** simple average of the **high − low** of the last **15 completed sessions**
  (same session window), **excluding the session that just ended** (see reconciliation below). His code stores
  session ranges in a ring buffer `RngBuf[250]`; "LegacyATR" in his code is "diagnostic only, drives nothing".
  No trades until 16 sessions of history exist.
- **Noise level:** `NoiseUp = SessOpen + 0.30 × BoundaryATR`, fixed for the session.
- **VWAP:** from the session start, typical price (H+L+C)/3 × volume, cumulative.
- **Entry:** when a 30-min bar **closes** above NoiseUp **and** above VWAP, with bar close time ≥ 10:00 CT and
  < 14:30 CT → buy at market, filled at the **next bar's open**.
- **Re-entry:** max **3 trades per session**, one position at a time. After TP or SL, a new entry fires on the next
  bar that again closes above NoiseUp and VWAP.
- **Exits:** take profit **40 points** ($800 on 1 NQ), stop loss **75 points** ($1,500), limit/stop orders checked
  intrabar on 1-minute data (he uses a 1-minute bar magnifier). Time exit: flat at **14:30 CT** (15:30 ET).
- **Costs:** his header says set commission + slippage, "realistic NQ round turn is near $13". Use $13 round turn
  plus the project's standard slippage.

## Decide before locking
1. **VWAP exit:** his inputs include `VWAPExitBars(7)` and a counter `BarsBelowVW`, never shown or mentioned.
   Proposed: base test WITHOUT it; test "exit after 7 consecutive 30-min closes below VWAP" as a logged variant.
2. **Session start variant (Pablo's idea):** midnight **New York** (23:00 CT) instead of midnight Chicago — log as a variant.
3. **Same-minute TP and SL:** assume stop first (conservative), or resolve with ticks.
4. **Holdout (A3):** proposed last 12 months (2025-10-01 → end of data), untouched until C6.

## A1b — Why the edge should exist
Most intraday moves are noise. A move bigger than 30% of the recent average daily range, with price above the
volume-weighted average (buyers in control of where volume traded), signals real directional pressure; long only
exploits the structural upward drift of the Nasdaq. His source: a 1987 paper on the intraday "noise area"
(title not given). Related: Zarattini, Barbon & Aziz (2024) "Beat the Market" noise-area strategy on SPY.

## A1c — Red-flag check
67.7% winners with TP 40 / SL 75 (win/loss ratio 0.61) — the high win rate comes from the payoff shape, not a 1:1
setup, so the >70%-at-1:1 rule doesn't apply directly. Still audit it fully.

## A4 / A5 — When each value is known
| Value | Known at |
|---|---|
| BoundaryATR | at session start — uses only completed sessions (and skips the latest one) |
| SessOpen, NoiseUp | open of the first session bar (23:30 CT bar on 30-min) |
| VWAP | close of each bar (cumulative to that bar) |
| Signal (close > NoiseUp and > VWAP) | close of the 30-min bar → order fills next bar open |
| TP / SL | intrabar after entry (1-min path) |

## Reconciliation targets (do NOT tune to these)
- **On-screen value, 9/22/2026:** NoiseUp 30,945.39, SessOpen 30,836.25 → his average = 363.8 points.
  Checked with TradingView NQ1! data: the rules above give 364.1 (NoiseUp 30,945.48). Including the most recent
  session instead gives 403.0, so "skip the latest session" is needed to match.
- **His MultiCharts report (1/21/2022 → 9/24/2026, 1 NQ, costs unclear):** 1,151 trades (all long), 779 winners =
  67.68%, average trade $112.48, average win $739.92, average loss $1,204.69, largest win $800, largest loss
  $1,500, avg 2.7 bars per trade, max 11 winners / 6 losers in a row, largest consecutive loss $7,965; equity
  $100k → ~$225k.
- Developed 2018–2022, out-of-sample 2023 onward (his split). Our NQ data starts Jul 2021.

## Variants to log (A2)
Base; VWAP exit 7; session from midnight NY; noise multiplier 0.2 / 0.5 (sensitivity only); max trades 1 / 2;
**ES fixed points 8.5 / 16** (ES test); **average range including the most recent session**. Total on ES: 1 base + 7 variants = 8.

Note for the split: Conti chose 0.30 / 3 trades / 40-75 on NQ 2018-2022, so on any instrument 2018-2022 is not fully
unseen for these parameters. Cleanest test of his rules as given: 2023 onward + the holdout.

## Part D — Monte Carlo and prop simulation (his settings)
- Trade reshuffle 10,000 and bootstrap 20,000; bench rule: drawdown above the 75th percentile of the Monte Carlo
  distribution, or 2 failed challenges in a row.
- Prop sim like his notebook: 50K account, end-of-day drawdown −$2,500, target +$3,000, 20 trading days, bootstrap
  whole trading days (incl. zero-trade days), 20,000 runs; report pass rate (CI), fail modes, days to pass, P95 max
  drawdown, pass-in-N attempts; position-size sweep in MNQ.
- He runs it together with VWAP Pullback + ADX and Overnight Bias at ~5 MNQ each (daily P&L correlation < 0.25,
  each alone ≈ 40% pass rate) — combined sim once all three exist.
