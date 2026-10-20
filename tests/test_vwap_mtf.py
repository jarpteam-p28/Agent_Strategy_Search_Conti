import numpy as np
import pandas as pd
import pytest

from conti_indicators import drift_vwap_15_on_5, resample_bars, session_vwap

ET = "America/New_York"


def at(obj, t, col=None):
    ts = pd.Timestamp(t, tz=ET)
    return obj.at[ts, col] if col else obj.at[ts]


def minute_bars(day="2024-03-05", start="09:00", end="16:30", seed=0, trend=0.0):
    idx = pd.date_range(f"{day} {start}", f"{day} {end}", freq="1min", tz=ET)[1:]  # close-stamped
    rng = np.random.default_rng(seed)
    close = 18000 + np.cumsum(rng.normal(trend, 2, len(idx)))
    df = pd.DataFrame({"close": close}, index=idx)
    df["open"] = df["close"].shift(1).fillna(df["close"].iloc[0])
    df["high"] = df[["open", "close"]].max(axis=1) + 1
    df["low"] = df[["open", "close"]].min(axis=1) - 1
    df["volume"] = rng.integers(50, 500, len(idx))
    df.index.name = "time"
    return df[["open", "high", "low", "close", "volume"]]


def test_vwap15_matches_hand_calculation():
    m = minute_bars()
    b15 = resample_bars(m, 15)
    sess = b15.between_time("09:45", "16:00")
    tp = (sess.high + sess.low + sess.close) / 3
    expected = (tp * sess.volume).cumsum() / sess.volume.cumsum()
    got = session_vwap(b15).dropna()
    pd.testing.assert_series_equal(got, expected, check_names=False)


def test_steps_on_5min_and_no_lookahead():
    m = minute_bars()
    out = drift_vwap_15_on_5(m)
    v15 = session_vwap(resample_bars(m, 15))
    # 09:35 and 09:40 bars: no 15-min bar has closed yet in the session
    assert pd.isna(at(out, "2024-03-05 09:35", "vwap15"))
    assert pd.isna(at(out, "2024-03-05 09:40", "vwap15"))
    # 09:45, 09:50, 09:55 all show the 09:45 value; 10:00 steps to the 10:00 value
    for t in ("09:45", "09:50", "09:55"):
        assert at(out, f"2024-03-05 {t}", "vwap15") == pytest.approx(at(v15, "2024-03-05 09:45"))
    assert at(out, "2024-03-05 10:00", "vwap15") == pytest.approx(at(v15, "2024-03-05 10:00"))
    # changing data AFTER 10:05 must not change any value up to 10:05
    m2 = m.copy()
    m2.loc[m2.index > pd.Timestamp("2024-03-05 10:05", tz=ET), ["close", "high", "low"]] += 500
    out2 = drift_vwap_15_on_5(m2)
    a = out.loc[:"2024-03-05 10:05", ["vwap15", "drift"]]
    b = out2.loc[:"2024-03-05 10:05", ["vwap15", "drift"]]
    pd.testing.assert_frame_equal(a, b)


def test_no_values_outside_session_or_across_days():
    m = pd.concat([minute_bars("2024-03-05"), minute_bars("2024-03-06", seed=1)])
    out = drift_vwap_15_on_5(m)
    assert out.between_time("16:05", "09:30")["vwap15"].isna().all()
    assert (out.between_time("16:05", "09:30")["drift"] == 0).all()
    # first values of day 2 restart from day 2 data only
    d2 = m.loc["2024-03-06"]
    v = session_vwap(resample_bars(d2, 15)).dropna().iloc[0]
    assert at(out, "2024-03-06 09:45", "vwap15") == pytest.approx(v)


def test_drift_long_and_short():
    up = drift_vwap_15_on_5(minute_bars(trend=1.5, seed=3))
    down = drift_vwap_15_on_5(minute_bars(trend=-1.5, seed=3))
    late = slice("2024-03-05 11:00", "2024-03-05 16:00")
    assert (up.loc[late, "drift"] == 1).mean() > 0.8
    assert (down.loc[late, "drift"] == -1).mean() > 0.8


def test_slope_colour_follows_vwap_direction():
    out = drift_vwap_15_on_5(minute_bars(seed=5))
    sess = out.dropna(subset=["vwap15_prev"])
    rising = sess["vwap15"] > sess["vwap15_prev"]
    falling = sess["vwap15"] < sess["vwap15_prev"]
    assert (sess.loc[rising, "slope"] == 1).all()
    assert (sess.loc[falling, "slope"] == -1).all()
    # every in-session bar after the first 15-min close is coloured (no grey), like his chart
    assert (sess["slope"] != 0).all()
