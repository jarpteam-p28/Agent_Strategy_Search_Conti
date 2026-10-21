# Drift VWAP Pullback — PROPOSED rules (not locked; needs Pablo's OK — checklist A1)

Source: Matteo Conti, "Ex-Market Maker Shows the Exact VWAP Setup That Gets Traders Funded" (IQ Capital, 2026-08-07,
youtu.be/wm4A6qo0g3I) and screenshots of his chart, MultiCharts report and Colab prop notebook.
Full spec: `strategies/conti/06_drift_vwap_pullback.yaml`. Python reference for the 15-min VWAP + drift:
`reference/vwap_mtf.py` (tested; values only used after the 15-min bar closes).
TradingView indicator: `indicators/tradingview/drift_vwap_15m_on_5m.pine`.

## A1 — Rules
- **Instrument / bars:** NQ continuous, 5-minute execution bars + 15-minute bars for the trend check, both built
  from 1-minute data. Long and short. 1 contract.
- **Time zone:** New York (ET). Note: his chart and trade list are in Chicago time (09:45 on his list = 10:45 ET).
- **VWAP:** session VWAP computed on **15-minute bars** from 09:30 ET (typical price × volume). It only updates when a
  15-min bar closes; on the 5-min chart it steps every 15 minutes.
- **Trend check (every 15-min close):**
  - Long drift = close15 > VWAP **and** VWAP > VWAP 15 minutes earlier **and** close15 ≥ 0.1% above the close
    four 15-min bars (1 hour) earlier.
  - Short drift = mirror (below, falling, ≤ −0.1%).
- **Trigger:** during a long drift, the **first red 5-min candle** (pullback; it does not need to touch VWAP) →
  buy at market, filled at the **next 5-min bar's open**. Short: first green 5-min candle in a short drift.
- **Re-entry:** after a trade closes, the next counter-colour candle in the same drift is a new trigger (his trade
  list: three shorts in one downtrend on 08/03/2021).
- **Exits:** long TP **40 points**, short TP **50 points**, SL **80 points** both sides on NQ = $800 / $1,000 / $1,600
  per contract; on ES the same dollars = **16 / 20 / 32 ES points** (base, 'exactly like him'). Intrabar on 1-minute data.
  Flatten at **15:55 ET**.
- **Guard rails:** no entries 09:30–10:30 ET; no new entries after 15:30 ET; one position at a time; max **4 trades per
  day**; stop for the day after **2 losses**.
- **Costs:** his report looks zero-commission with ~2 ticks slippage on stops. Use real costs (≈ $13 round turn)
  plus the project's slippage — the average trade is only $74, so costs matter a lot.

## Decide before locking
1. **2-loss rule:** any 2 losses in a day, or 2 in a row? (He said both.)
2. **Must the drift still be on when the pullback candle closes?** Proposed: yes (drift state at the last 15-min close).
3. **"First" pullback:** proposed = first counter-colour candle after the drift turns on or after the previous trade
   closes; consecutive counter candles only trigger once.
4. **Same-minute TP and SL:** stop first, or resolve with ticks.
5. **Holdout (A3):** proposed 2025-10-01 → end of data.

## A1b — Why the edge should exist
Bank and broker execution desks fill most institutional orders with VWAP algorithms. Those algos trade hardest near
VWAP, so a pullback toward VWAP during an established drift reveals which side the algos are on, and price moves
sharply that way. The three conditions = level (price vs VWAP), direction (VWAP slope), speed (1-hour move).

## A1c — Red-flag check
64% winners at roughly 1:2 (win/loss 0.65). Profit factor 1.15 — thin. High win rate comes from the payoff shape.

## A4 / A5 — When each value is known
| Value | Known at |
|---|---|
| 15-min VWAP, slope, 1-hour move, drift state | close of each 15-min bar; carried until the next 15-min close |
| Candle colour of the 5-min trigger bar | close of that 5-min bar → order fills next bar open |
| TP / SL | intrabar after entry (1-min path) |

## Reconciliation targets (do NOT tune to these)
His MultiCharts report, NQ 5-min, 1 contract, **04/01/2021 → 31/07/2026**: 4,130 trades (2,156 long / 1,974 short),
64.09% winners (long 66.51%, short 61.45%), net $306,590 on $100k, profit factor 1.15, Sharpe 0.46, max drawdown
$29,055, average trade $74.23, average win $866.42, average loss $1,340.63, largest win $3,040, largest loss
$2,815, avg 14.9 bars per trade. Developed 2020–2024, out-of-sample 2024 → 2026. Our NQ data starts Jul 2021.

## Variants to log (A2)
Base; 2-loss rule "in a row" vs "any"; VWAP on 5-min bars instead of 15-min; min move 0.05% / 0.15% (sensitivity only).

## Part D — Monte Carlo and prop simulation (his notebook "PropFirm_MonteCarlo_The_Protocol")
50K account, end-of-day drawdown −$2,500, target +$3,000, max 20 trading days, 1 NQ (10 MNQ); bootstrap daily P&L
(pool of all weekdays incl. zero-trade days), 20,000 runs. His result: pass 49.8% (95% CI 49.1–50.5%), drawdown
fail 50.2%, time fail 0%, 3.4 days to pass, avg max DD $2,078, P95 max DD $4,661, pass ≥ 1 in 2/3/4 attempts =
74.8% / 87.3% / 93.6%. Also run a position-size sweep in MNQ.

## Volatility sizing (sizing view, not a variant)
Apply `VOLATILITY_SIZING.md`: contracts (MES) = floor(Risk$ / (0.30 × 15-session AvgRange × $5 + 2 ticks)), capped, skip if 0. Headline stays 1 contract.
