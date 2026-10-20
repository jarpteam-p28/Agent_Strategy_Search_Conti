"""15-minute session VWAP shown on a 5-minute chart (Conti's 'DriftPullback VWAP Indicator').

How it works (matches the Drift VWAP Pullback rules, strategies/conti/06_drift_vwap_pullback.yaml):

* Build 15-minute bars from the session anchor (default 09:30 America/New_York).
* VWAP is computed on those 15-minute bars:  sum(price_15 * volume_15) / sum(volume_15) since the anchor,
  where price_15 is the bar's typical price (H+L+C)/3 by default.
* The value is only known when a 15-minute bar CLOSES. On the 5-minute chart it is placed on the 5-minute
  bar that closes at the same time and carried forward until the next 15-minute close. So it moves in steps
  every 15 minutes, exactly like the crosses on his chart - and it never uses future data.
* Drift state, evaluated at each 15-minute close (his 'every 15 minutes we ask: is there a trend?'):
      long  = close15 > VWAP  and  VWAP > VWAP 15 minutes ago  and  close15 / close15 one hour ago - 1 >=  +0.1%
      short = close15 < VWAP  and  VWAP < VWAP 15 minutes ago  and  close15 / close15 one hour ago - 1 <= -0.1%
  (+1 = long drift, -1 = short drift, 0 = none.)
* Cross colour on his chart = VWAP slope only ('when the cross is green the VWAP over the past 15 minutes
  is increasing'): column `slope` = +1 rising (green), -1 falling (red); a flat step keeps the last colour.

Input: a DataFrame of 1-minute (or 5-minute) OHLCV bars with a tz-aware DatetimeIndex marking each bar's
CLOSE time (NinjaTrader convention). Bars are resampled to 5 and 15 minutes here.
"""
from __future__ import annotations

import pandas as pd

ET = "America/New_York"


def load_ninjatrader_minute(path: str, source_tz: str = "UTC") -> pd.DataFrame:
    """Read a NinjaTrader 'Last' minute export: 'yyyyMMdd HHmmss;open;high;low;close;volume'.

    Timestamps are bar close times. Our Lexar exports are in UTC (the clean_ES_master manifest says so);
    pass source_tz if a file was exported in another zone. Returns bars indexed in New York time.
    """
    df = pd.read_csv(path, sep=";", header=None, names=["ts", "open", "high", "low", "close", "volume"])
    idx = pd.to_datetime(df.pop("ts"), format="%Y%m%d %H%M%S").dt.tz_localize(source_tz).dt.tz_convert(ET)
    df.index = pd.DatetimeIndex(idx, name="time")
    return df.sort_index()


def resample_bars(bars: pd.DataFrame, minutes: int) -> pd.DataFrame:
    """Resample close-stamped bars to N minutes, keeping close-time stamps (a 09:35 bar covers 09:30-09:35)."""
    out = bars.resample(f"{minutes}min", label="right", closed="right").agg(
        {"open": "first", "high": "max", "low": "min", "close": "last", "volume": "sum"})
    return out.dropna(subset=["close"])


def session_vwap(bars: pd.DataFrame, anchor: str = "09:30", end: str = "16:00",
                 price: str = "typical") -> pd.Series:
    """Session VWAP on the given bars, reset every day at `anchor` (New York time). NaN outside the session."""
    b = bars.tz_convert(ET) if bars.index.tz is not None else bars.tz_localize(ET)
    t = b.index.time
    a, e = pd.Timestamp(anchor).time(), pd.Timestamp(end).time()
    in_sess = (t > a) & (t <= e)  # close-stamped: the first bar of the session closes after the anchor
    px = (b["high"] + b["low"] + b["close"]) / 3 if price == "typical" else b["close"]
    day = pd.Series(b.index.date, index=b.index)
    pv = (px * b["volume"]).where(in_sess, 0.0)
    vol = b["volume"].where(in_sess, 0.0)
    cum_pv = pv.groupby(day).cumsum()
    cum_v = vol.groupby(day).cumsum()
    vwap = (cum_pv / cum_v).where(in_sess & (cum_v > 0))
    vwap.name = "vwap"
    return vwap


def drift_vwap_15_on_5(bars: pd.DataFrame, anchor: str = "09:30", end: str = "16:00",
                       min_hour_move: float = 0.001, price: str = "typical") -> pd.DataFrame:
    """Return 5-minute bars with the 15-minute VWAP and Conti's drift state carried onto them.

    Columns added:
      vwap15        15-min session VWAP, stepped (value of the last CLOSED 15-min bar)
      vwap15_prev   VWAP at the previous 15-min close (slope reference)
      close15       close of the last closed 15-min bar
      ret_1h        close15 vs close15 one hour (four 15-min bars) earlier
      drift         +1 long drift, -1 short drift, 0 none (all three conditions at the last 15-min close)
      slope         +1 VWAP rising (green cross), -1 falling (red cross), 0 unknown (first 15-min bar)
    """
    b5 = resample_bars(bars, 5)
    b15 = resample_bars(bars, 15)

    v15 = session_vwap(b15, anchor, end, price)
    t15 = b15.index.time
    in_sess = (t15 > pd.Timestamp(anchor).time()) & (t15 <= pd.Timestamp(end).time())
    day = pd.Series(b15.index.date, index=b15.index)

    s = pd.DataFrame({"vwap15": v15, "close15": b15["close"]})
    s = s[in_sess]
    g = s.groupby(day[in_sess])
    s["vwap15_prev"] = g["vwap15"].shift(1)                     # slope within the same session
    s["ret_1h"] = s["close15"] / b15["close"].shift(4).reindex(s.index) - 1  # may reach back before the open

    long_ = (s["close15"] > s["vwap15"]) & (s["vwap15"] > s["vwap15_prev"]) & (s["ret_1h"] >= min_hour_move)
    short = (s["close15"] < s["vwap15"]) & (s["vwap15"] < s["vwap15_prev"]) & (s["ret_1h"] <= -min_hour_move)
    s["drift"] = 0
    s.loc[long_, "drift"] = 1
    s.loc[short, "drift"] = -1
    sl = pd.Series(0.0, index=s.index)
    sl[s["vwap15"] > s["vwap15_prev"]] = 1
    sl[s["vwap15"] < s["vwap15_prev"]] = -1
    flat = (s["vwap15"] == s["vwap15_prev"])
    sl[flat] = float("nan")
    s["slope"] = sl.groupby(day[in_sess]).ffill().fillna(0)

    # Carry the 15-min values onto 5-min bars: each 5-min bar sees the last 15-min bar that closed at or
    # before its own close. Restrict to the same session day so values never leak across days.
    out = b5.copy()
    t5 = out.index.time
    sess5 = (t5 > pd.Timestamp(anchor).time()) & (t5 <= pd.Timestamp(end).time())
    joined = pd.merge_asof(out.reset_index(), s.reset_index().rename(columns={"time": "t15"}),
                           left_on="time", right_on="t15", direction="backward")
    joined.index = out.index
    same_day = joined["t15"].dt.date == pd.Series(out.index.date, index=out.index)
    cols = ["vwap15", "vwap15_prev", "close15", "ret_1h", "drift", "slope"]
    for c in cols:
        out[c] = joined[c].where(same_day & sess5)
    out["drift"] = out["drift"].fillna(0).astype(int)
    out["slope"] = out["slope"].fillna(0).astype(int)
    return out
