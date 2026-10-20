# Indicators

| Indicator | TradingView (Pine v6) | Python (for backtests) | Used by |
|---|---|---|---|
| Drift VWAP 15m on 5m | `tradingview/drift_vwap_15m_on_5m.pine` | `conti_indicators/vwap_mtf.py` → `drift_vwap_15_on_5()` | `strategies/conti/06_drift_vwap_pullback.yaml` |
| Vault Break (strategy, Strategy Tester) | `tradingview/vault_break_strategy.pine` | not yet | `strategies/conti/07_vault_break.yaml` |
| Overnight Bias ORB (overnight range thirds) | `tradingview/overnight_bias_orb.pine` | not yet | `strategies/conti/09_overnight_bias_orb.yaml` |

## Drift VWAP 15m on 5m — how to add it in TradingView
1. Open a **5-minute NQ1! (or ES1!) chart**. Keep extended hours on (the 1-hour move looks back before 10:30).
2. Pine Editor → new indicator → paste the file → **Save** → **Add to chart**.
3. Optional: right-click a trigger → **Add alert** → "Drift VWAP long/short trigger".

What you see:
- **Crosses** = session VWAP built from 15-minute bars, anchored 09:30 ET, updating every 15 minutes.
- **Colour** = VWAP direction vs 15 minutes ago (green rising, red falling) — as on Conti's chart.
  Settings → Inputs → "Colour only when ALL 3 conditions are met" shows green/red only when the full drift is on (grey otherwise).
- **Triangles** = first pullback candle during a full 3-condition drift, 10:30–15:30 ET
  (red candle in a long drift / green candle in a short drift); entry is the next bar's open.

The Python and Pine versions use the same rules: 15-minute bars from the chart's own bars, typical price,
values used only after the 15-minute bar closes (no repainting, no look-ahead).

## Overnight Bias ORB — how to add it in TradingView
1. Open a **15-minute NQ1! (or ES1!) chart** with **extended hours ON** (the overnight range needs the Globex session).
2. Pine Editor → new indicator → paste `overnight_bias_orb.pine` → Save → Add to chart.

What you see:
- **Grey lines** = overnight high and low (default 18:00 ET Globex open → 09:30 ET), locked at the open.
- **Green shaded band** = top third (≥ 67%), **red band** = bottom third (≤ 33%), clear middle third.
- **Label at 09:30** = today's bias: LONG ONLY / SHORT ONLY / NO TRADE, and where the open sat in the range.
- **Orange lines** = opening range (09:30–09:45).
- **Triangle + label** = breakout close beyond the opening range in the bias direction with ADX > 20,
  between 09:45 and 13:00 ET; enter at the next bar's open. The label shows stop / target in points
  (30% of the 15-day average RTH daily range, target 3×). Flat by 15:30 ET.
- **Status box** (top right) = bias, open %, ADX, stop/target, signals used today.

Overnight start is an input: 18:00 ET (his code, default), 00:00 ET (= 23:00 CT, as said in the talk) or 01:00 ET (= midnight CT, his chart).
