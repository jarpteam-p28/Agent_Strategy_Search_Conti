# Overnight Bias ORB — PROPOSED rules (not locked; needs Pablo's OK — checklist A1)

Source: Matteo Conti, "A Hedge Fund Manager Just CRACKED Prop Trading" (2026-10-06), whiteboard and on-screen code
"OFB_OvernightBiasORB_Signal - NQ 15-min, one data stream, 1 contract". Full spec: `strategies/conti/09_overnight_bias_orb.yaml`.
TradingView indicator: `indicators/tradingview/overnight_bias_orb.pine`.

## A1 — Rules
- **Instrument / bars:** NQ continuous, 15-minute bars from 1-minute data, Globex session. Long and short. 1 contract.
- **Time zone:** his code inputs are **ET** (SessStart 0930, OREnd 0945, LastEntry 1300, FlatTime 1530, SessEnd 1600).
- **Overnight range:** high/low of the overnight session up to 09:30 ET (his code: the RTH open "ends the overnight
  range"). Start: Globex open 18:00 ET (proposed; the talk also says 23:00 CT and his chart suggests midnight CT).
- **Bias at 09:30:** open ≥ 0.67 of the overnight range → long-only day (BiasLongMin 0.67); open ≤ 0.33 → short-only;
  middle → no trade. The bias stays valid all day.
- **Opening range:** high/low of 09:30–09:45 ET.
- **Entry:** after 09:45 and up to 13:00 ET, a 15-min bar closes above the OR high (long day) / below the OR low
  (short day) with ADX > 20 (any slope) → market order, next bar open.
- **Re-entry:** code MaxTradesPerDay(4), one position at a time (he SAID one trade per day — code wins; log 1 as a variant).
- **Exits:** stop = 0.30 × 15-session average range; target = 3 × stop; flat at 15:30 ET.
- **Filter not explained:** an opening-range SIZE band (needs 20 days of history: "under 15 days nothing trades;
  between 15 and 20 it trades with the OR-size band silently off").

## Decide before locking
1. Overnight start (18:00 ET / 00:00 ET / 01:00 ET).
2. OR-size band: unknown thresholds — run without, or define one as a logged variant.
3. ADX period (likely 14, on 15-min bars).
4. Average-range definition: same as Vault Break (high−low, 15 completed sessions) but his code says the 16:00 ET RTH
   close "bounds the ATR reference's day" — confirm the window.

## Reconciliation targets (zero-cost, from his code header)
In-sample 01-01-2006 → 31-12-2019: n = 1,112, PF 1.35, net $50,445, max DD $6,160.
Out-of-sample 01-01-2020 → 31-08-2026: n = 599, PF 1.66, net $257,615, max DD $20,195.
In the talk: ~53% winners, avg win / avg loss ≈ 1.4. **Our NQ data only covers Jul 2021 → Sep 2026**, so we can
only check part of his out-of-sample period.
