# Market Intraday Momentum

**Authors:** Lei Gao, Yufeng Han, Sophia Zhengzi Li, Guofu Zhou  
**Year:** 2018  **Type:** academic  **Read:** abstract_only  
**Source:** https://doi.org/10.1016/j.jfineco.2018.05.009

> The market's return in the first half-hour of the day, measured from the prior close, predicts the sign of the return in the last half-hour, and the 11:30–12:00 half-hour adds to that signal.

## Findings
- On SPY and S&P 500 futures, the first half-hour return (prior day's close to 10:00 ET) positively predicts the last half-hour return (15:30–16:00). The paper reports this in-sample and out-of-sample. — *From memory, not verified against the text: about 1993–2013, in-sample R² of roughly 1–2%, statistically significant. Treat the exact numbers as unconfirmed.*
- The second-to-last half-hour return (about 11:30–12:00, the 12th half-hour) is a second, smaller predictor of the last half-hour. Using it together with the first half-hour raises explanatory power. — *From memory: both coefficients are positive and significant. Exact values unconfirmed.*
- The effect is stronger on high-volatility days, high-volume days, recession days and days with major macro news releases. — *From memory. The paper has subsample splits, and the effect is stronger in these regimes.*
- The pattern holds across many assets, including other equity ETFs and futures on bonds, FX and commodities. A simple timing rule (go long or short in the last half-hour according to the sign of the morning signal) earns a meaningful economic gain. — *From memory: the paper reports an annualised timing gain of several percent and a Sharpe ratio well above buy-and-hold. Exact numbers and costs unconfirmed.*

## The WHY
**Pattern:** {"pattern":"Execution mechanics of big players, plus slow information diffusion. Information that arrives overnight or in the morning is only partly traded on early, so the rest comes in late in the day.","mechanism":"The authors point to two channels. (1) Infrequent portfolio rebalancing: investors don't act on the morning's information at once, so informed demand is deferred and clusters near the close (Bogousslavsky 2016). (2) Late-day informed trading, where informed traders delay trades because of liquidity and price impact. A related, separate channel is dealers and levered products rebalancing at the close. This is my reading and I did not confirm it in the paper. Heavy closing-auction and benchmark-driven flow also makes the last 30 minutes a predictable time to trade.","who_is_forced":"Institutions with benchmark or closing-price mandates. Rebalancers and levered/inverse ETF issuers, whose hedges must be traded near the close in the direction of the day's move. Dealers hedging gamma. Large funds that spread orders across the day.","why_it_persists":"The constraints are structural: closing-price benchmarks, daily rebalancing of levered ETFs, and the spreading of large orders to limit impact. Rising volatility amplifies them, which fits the paper's regime results.","what_would_kill_it":"Faster digestion of overnight news, so less is left for the close. Dealers being net long gamma on 0DTE expiry days, which can turn flow mean-reverting. Close-time flow becoming crowded or arbitraged by HFT. Changes to closing-auction mechanics or ETF rebalancing. Later literature finds the effect is regime-dependent (Rosa 2022; the 0DTE work in our notes)."},
"authors_explanation_vs_ours":"The paper stresses infrequent rebalancing and late-informed trading, which are behavioural or information stories. I think the most defensible WHY for trading is mechanical: the close is where mandated and forced flow concentrates. That also tells us the signal should be strongest on high-volatility days and on days when the market moved a lot. I could not read the full text, so I may have missed parts of the authors' reasoning."}




## Setting
- Markets: US equity (main), multi-asset (robustness)
- Instruments: SPY, S&P 500 futures, other equity ETFs, Treasury, FX and commodity futures
- Period: About 1993–2013 (from memory, unverified)  Frequency: 1-minute, aggregated to 30-minute intervals  Holding: Last 30 minutes of the RTH session (15:30–16:00 ET), flat at the close

## Reported results
A last-half-hour timing strategy based on the first-half-hour (and 12th half-hour) return beats buy-and-hold on a risk-adjusted basis, with significant R² in-sample and out-of-sample.
- Unverified, from memory: SPY sample about 1993–2013; in-sample R² about 1.6%.
- Unverified: effect is larger on volatile and recession days and on news days.
- The full text was not accessed, so no figures here are confirmed.
- Costs: Unknown. I believe the paper's economic-gain figures are largely gross of transaction costs, so confirm this before relying on them.

## Tradable edge (our framing)
When the market has moved strongly since yesterday's close, with the same sign in the first half-hour and optionally the 11:30–12:00 window, the late-day demand for that direction is predictable and still unfilled. Take the last 30 minutes in that direction with a time exit at the close. This is one side of a day-trading portfolio that holds almost no overnight exposure. Filter on signal size and volatility regime, because the edge depends on both. Test it by pre/post 2022 period. Any gross edge in points per trade has to clear friction (about 2 points on NQ, about $19 round trip) and the net t-stat must be 2 or higher.

## Angles to test
- ES, and NQ for 2021+: signal = prior RTH close (16:00 ET) to 10:00 ET return; trade 15:30→16:00 or 15:30→close.
- Use ES as the main test, since it has 2013+ history. Run NQ only post-2021.
- Long-only vs short-only. Check whether the long side drives the result, which would mean it is partly equity beta.
- Condition on signal strength (e.g. |signal| above X% or above a multiple of ATR) and on VIX or realised volatility. Add a no-trade filter for small signals.
- Add the 11:30–12:00 return as a second signal, and test them separately and together.
- Event days: FOMC, NFP and CPI days, where the paper says the effect is stronger. Also test on expiry days to see the 0DTE effect.
- Different session: use the same logic on the overnight or Asia/Europe close (an ETH 'last half-hour' for each session).
- Combine with the Zarattini et al. noise-area intraday momentum approach, or with the ORB strategy.
- Hold-time sweep: start at 15:00, 15:15 or 15:30 and exit at 15:55, 16:00 or the following open, so there is a longer hold to beat friction.
- Size by volatility target, not fixed contracts, for live trading.

## Decay risk: high
The paper has been public since 2018 and is widely cited. Follow-up papers report weaker or regime-dependent results after 2014 or 2022, and 0DTE dealer gamma may now dampen it. A 30-minute hold is also vulnerable to costs, and McLean & Pontiff suggest expecting about half the published effect.

## Data fit
"Good for ES. We have 1-minute ES from 2013-12 to 2026-09 in ETH and RTH, which covers the signal windows and the last half-hour. NQ 1-minute is available from 2021-07, so a test fits there too, with a shorter history. We lack the paper's 1993–2013 history, so this is an out-of-sample re-test, not a replication. We also lack the macro-news calendar (FOMC, NFP, CPI dates) and VIX, which would have to be added for the conditioning tests. Check the UTC time zone and the daylight-saving shift when mapping to 09:30–16:00 ET."

## Caveats
- I could not access the paper (the DOI, SSRN and ScienceDirect fetches all failed). This summary comes from prior knowledge plus the abstract-level facts, so all numbers are unverified.
- I am not sure whether the paper's economic-gain numbers include costs. I assume they are mostly gross.
- The paper's own sample ends in 2013, so it says nothing about the 0DTE era.
- The long-only part of the signal may mostly be market drift in the last half-hour, so beat an 'always long 15:30–16:00' baseline.

## Cited papers worth reading
- Intraday Momentum: The First Half-Hour Return Predicts the Last Half-Hour Return (working paper, earlier version of this paper) (2014)
- Infrequent Rebalancing, Return Autocorrelation, and Seasonality (2016)
- Beat the Market: An Effective Intraday Momentum Strategy for S&P500 ETF (SPY) (2024)
- Intraday Momentum: The Role of Market Regimes / Intraday momentum and 0DTE (Rosa 2022; Adams et al. 2025) (2022)
- Intraday Patterns in the Cross-section of Stock Returns (2010)
