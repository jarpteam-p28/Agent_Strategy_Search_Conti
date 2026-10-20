# Indicators

| Indicator | TradingView (Pine v6) | Python (for backtests) | Used by |
|---|---|---|---|
| Drift VWAP 15m on 5m | `tradingview/drift_vwap_15m_on_5m.pine` | `conti_indicators/vwap_mtf.py` → `drift_vwap_15_on_5()` | `strategies/conti/06_drift_vwap_pullback.yaml` |

## Drift VWAP 15m on 5m — how to add it in TradingView
1. Open a **5-minute NQ1! (or ES1!) chart**. Keep extended hours on (the 1-hour move looks back before 10:30).
2. Pine Editor → new indicator → paste the file → **Save** → **Add to chart**.
3. Optional: right-click a trigger → **Add alert** → "Drift VWAP long/short trigger".

What you see:
- **Crosses** = session VWAP built from 15-minute bars, anchored 09:30 ET, updating every 15 minutes.
- **Colour** = VWAP direction vs 15 minutes ago (green rising, red falling) — as on Conti's chart.
  Setting "Cross colour → All 3 conditions" shows green/red only when the full drift is on (grey otherwise).
- **Triangles** = first pullback candle during a full 3-condition drift, 10:30–15:30 ET
  (red candle in a long drift / green candle in a short drift); entry is the next bar's open.

The Python and Pine versions use the same rules: 15-minute bars from the chart's own bars, typical price,
values used only after the 15-minute bar closes (no repainting, no look-ahead).
