# Noise Area Intraday Momentum (ES) — PROPOSED rules (not locked; needs Pablo's OK — checklist A1)

Follow `CONTI_REVISED_BACKTEST_CHECKLIST.md`. Source: Zarattini, Aziz & Barbon (2024), "Beat the Market: An Effective
Intraday Momentum Strategy for S&P500 ETF (SPY)", SSRN 4824172 (published May 2024, updated Feb 2025).
Summary: `papers/summaries/beat_the_market_intraday_momentum_spy_zarattini.md` · spec: `strategies/candidates/noise_area_momentum_es.yaml`
TradingView picture of the bands: `indicators/tradingview/noise_area_bands.pine`.

## Part 0 — Setup
- **Objectives:** PERSONAL ACCOUNT + PROP EVALUATION + PROP FUNDED (separate verdicts).
- **Mode:** FULL VALIDATION. Base = the paper's rules exactly (0.4), translated from SPY to ES only where unavoidable.
- **Parameters:** SOURCE-FIXED (lookback 14, multiplier 1.0) → C6b and C9b are N/A unless Pablo asks to optimize.
  If he asks: Part O grid = lookback {14, 30, 60, 90} × multiplier {1.0, 1.25, 1.5} (the two dials the paper itself varies).

## A1 — Rules (base)
- **Instrument / data:** ES continuous front month, 1-minute bars, `clean_ES_master.parquet` (UTC → convert to New York
  time with DST). Regular hours only: bars closing 09:31 → 16:00 ET. 1 ES contract (headline).
- **Today's open (O):** open of the 09:30 ET 1-minute bar. **Prior close (C₋₁):** close of the previous session's 16:00 ET bar.
- **Noise (sigma) at minute t:** average over the **previous 14 sessions** of |close at minute t ÷ that day's 09:30 open − 1|,
  one value per minute of the day, prior sessions only (today never included).
- **Bands at minute t:**
  Upper = max(O, C₋₁) × (1 + 1.0 × sigma(t)) · Lower = min(O, C₋₁) × (1 − 1.0 × sigma(t)).
- **VWAP:** session VWAP anchored at 09:30 ET, typical price × volume, regular hours only.
- **Decision times:** only at the closes of the 10:00, 10:30, … 15:30 ET bars (HH:00 and HH:30).
  - Flat and close > Upper → **buy**. Flat and close < Lower → **sell short**.
  - Long and close < Lower → **reverse to short** (and vice versa).
  - Fill at the **next 1-minute bar's open** (A6: never inside the signal bar).
- **Exit (paper's band + VWAP trailing stop):** long → exit when close < max(Upper, VWAP); short → exit when close > min(Lower, VWAP).
  After an exit, a new entry is allowed at a later decision time if the rule fires again.
- **Time exit:** flat at the 16:00 ET close (market-on-close: use the 16:00 bar close).
- **Costs:** real ES commission round turn + 1 tick slippage on every market entry and exit (B4). Paper used SPY costs
  ($0.0035/share + $0.001 slippage); do not copy those.

## Decide before locking (proposed answers)
1. **When is the stop checked?** Proposed base = at the **half-hour closes only**, like the entries (paper's
   description: positions are re-evaluated only at HH:00 / HH:30). Variant = checked on every 1-minute close.
   Confirm from the paper's code/FAQ (authors published Matlab/Python code) before locking.
2. **Half days** (13:00 close): no decisions after the early close; sigma for missing minutes uses the sessions that have them
   (need ≥ 11 of 14).
3. **Sizing:** base 1 ES fixed. Paper's volatility targeting (2% daily vol target, 14-day realised vol, max 4× leverage) is a
   logged variant, shown with capped contracts (D5).
4. **Same-minute ambiguity:** not relevant to entries/exits on closes; the 16:00 time exit is at the close.
5. **First trade of the day:** earliest 10:00 (no decision at 09:30/09:31).

## A1b — Why the edge should exist
A move bigger than the usual distance from the open for that time of day means a buy/sell imbalance too large for
liquidity providers to absorb. Institutions work large orders through VWAP/participation algos over the rest of the
day, and short-gamma option dealers hedge in the direction of the move, so it keeps going. Losing VWAP or re-entering
the band means the imbalance is gone, which is why that is the exit. Should be stronger on high-volatility days and after
market drops (more negative gamma).

## A1c — Red-flag check
Paper: hit rate 37–43%, positive skew, Sharpe 1.24 unlevered on SPY. A low win rate with big winners is the expected
shape, not a red flag. A win rate above ~55% here would be suspicious (check look-ahead in sigma first).

## A4 / A5 — When each value is known
| Value | Known at |
|---|---|
| sigma(t) | before today's session (previous 14 sessions only) |
| O, C₋₁ | O at the 09:30 bar open; C₋₁ at yesterday's 16:00 close |
| Upper / Lower at t | at the open of minute t (O, C₋₁, sigma(t) all known) |
| VWAP | close of each 1-minute bar |
| Signal / stop | close of the HH:00 / HH:30 bar → fill next 1-minute bar's open |

## A3e — Evaluation windows (reporting views, not variants)
1. **Source window:** paper's sample is SPY May 2007 → Apr 2024; our ES overlap is **2014-01 → 2024-04**.
   80/20: in-sample 2014-01 → ~2022-04, out-of-sample ~2022-05 → 2024-04.
2. **Full history:** 2014-01 → end, 80/20 as in the checklist (IS 2014–2023, OOS 2024 → end).
3. **Post-publication** (extra view, valuable here): **2024-05 → end** — the paper did not exist yet, so this is true
   out-of-sample for the idea. It sits inside protected 2024 + UNSEEN DATA → A3d rules (written first, run once, quarter by quarter, Pablo's yes).
Warm-up: first 14 sessions of the data produce no bands.

## Reconciliation targets (do NOT tune to these)
SPY 2007-05 → 2024-04, band + VWAP stop, unlevered: 9.7%/yr, volatility 7.7%, Sharpe 1.24, max DD 12%, hit rate 43%,
skew +1.29, ~1.8 trades/day. Base version with stop at the opposite band: Sharpe 0.61. Year signs from the FAQ:
2016 −12.8%, 2017 −6.9%, 2018 +61%, 2024 +32.2% (levered). Authors' FAQ: S&P 500 futures Sharpe 1.32, Nasdaq 1.23
(unaudited). Expect lower on ES 2014+ (no 2008 in our data; a 2022 study says intraday momentum weakened after 2013).

## Variants to log (A2)
Base; stop checked every minute; stop at the opposite band only (paper's base version); VWAP-only stop; long only;
short only; volatility-targeted sizing; no gap widening (bands from O only); first signal of the day only + lockout after
the first stop-out; NQ second instrument (C11, 2021-07+ months that exist); **DOUBLE-NOISE ENTRY** (Pablo, 2026-10-20,
see below). **Total: 1 base + 10 variants = 11** (C9 uses 11).

### Variant: DOUBLE-NOISE ENTRY (Pablo, added 2026-10-20, written before any results)
Entry needs the half-hour close to be outside BOTH noise zones; everything else = base.
- **Conti level (Vault Break):** session = bars from midnight CT to 16:00 CT (MultiCharts close-time dating, so the
  23:30 CT 30-min bar opens it). SessOpen = open of that first 30-min bar. AvgRange = average session high − low
  of the last 15 completed sessions, skipping the most recent one. NoiseUp = SessOpen + 0.30 × AvgRange,
  NoiseDown = SessOpen − 0.30 × AvgRange. Fixed for the whole session; known at its start (no look-ahead).
  Reuse the Vault Break engine's code for this; do not rebuild it.
- **Long:** at a half-hour decision close (10:00 … 15:30 ET), close > Upper(t) (Zarattini) **AND** close > NoiseUp (Conti).
- **Short:** close < Lower(t) **AND** close < NoiseDown.
- **Reversal:** a reverse only when the opposite side meets BOTH conditions; otherwise the base exits apply.
- **Exits, time exit, sizing, costs:** identical to the base (band + VWAP trailing stop checked at half hours, flat at 16:00, 1 ES).
- Report it next to the base on every slice, plus how many base trades the extra filter removed and what those
  removed trades made (so we see whether the filter removes losers or winners).
- It is a filter on the base, so expect fewer trades; check the trade count against C1 / C9c.
Regime splits (VIX proxy, NR4/NR7, weekday, after a down day) are C8 reporting only, not variants.

## Part P — Prop notes
Low win rate + uneven years = long losing streaks; expect EOD-drawdown failures on a 50K / −$2,500 account at 1 ES
(an average ES day range of 40–90 points). Run the P4 size sweep in MES (1–10). Daily-P&L correlation with Vault Break
(E7 / P5) — likely high on trend days, both are momentum.

## Volatility sizing (sizing view, not a variant)
Apply `VOLATILITY_SIZING.md`: contracts (MES) = floor(Risk$ / (0.30 × 15-session AvgRange × $5 + 2 ticks)), capped, skip if 0. Headline stays 1 contract.
