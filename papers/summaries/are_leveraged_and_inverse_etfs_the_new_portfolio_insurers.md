# Are Leveraged and Inverse ETFs the New Portfolio Insurers?

**Authors:** Tugkan Tuzun  
**Year:** 2013  **Type:** academic  **Read:** full_pdf  
**Source:** https://www.federalreserve.gov/pubs/feds/2013/201348/201348abs.html

> Leveraged and inverse ETFs must buy after the market rises and sell after it falls, mostly in the last hour. That pushes prices from 3pm to the close in the direction of the day's move, and the move partly reverses the next day.

## Findings
- Leveraged and inverse ETF (LETF) rebalancing always points the same way as the index move. The required trade is r×δ×(δ−1)×NAV. It is positive for both 2x/3x long funds and negative-multiple inverse funds, so the two groups add together instead of netting out. — *Derived analytically. Table I: 108 US equity LETFs, $20.1B in assets (Dec 15, 2011). A 1% index move forces about $1.04B of stock-equivalent trading, roughly 0.8% of US daily stock volume.*
- The flow is large for the average financial and small-cap stock, and larger still relative to last-hour volume. Flow is scaled to 1% of the index move and assumes the trading happens in the last hour. — *About 2% of daily volume for financials. Small caps rise from 2% to 6% of daily volume by 2011. Last-hour share is 2-3% for large, mid and tech, 4-8% for financials, and up to 18% for small caps.*
- The 15:00-16:00 ET return moves in the direction of LETF flow. LETF flow is defined from the index return between the prior close and 15:00, scaled by stock ADV. The result holds for every category and survives controls for the 15:00 return and the index and S&P intraday returns. — *Daily panel of US stocks, June 2006 to Dec 2011, TAQ data, standard errors clustered by day. Coefficients on flow/ADV: financials 3.1, large 3.8-4.3, mid 4.2, small 0.8, tech 2.7-3.8. Adj-R² is only 0.5-6%. Implied move for a 1% index move: about 6.9bp in an average large cap, 13bp in financials, 12.7bp in small caps.*
- The reaction is stronger on up days than on down days in every category except small caps. — *Table V. Large caps: 4.46 on up days vs 3.60 on down days. Tech: 4.66 vs 2.93. Small caps: 0.63 vs 0.80. The author suggests short-sale constraints on anticipators.*
- The late-day move partly reverses the next day. The reversal is measured from the close to 15:00 the following day. — *Table VI. Lagged-flow coefficients are negative in every category: -1.7 financials, -3.5 large, -2.5 mid, -0.35 small, -4.2 tech. These are similar in size to the same-day coefficients. The reversal R² is tiny, about 0.1-0.25%.*
- Late-day volatility is higher when the absolute flow is large. — *Table VII. Coefficients on |flow|/ADV are positive and significant: 0.6 for small caps to 2.6 for tech. Effects are stronger in 2006-2009 than in 2010-2011. Extra close volatility for a 1% index move is about 23bp for a large cap.*
- The price impact implied by the Kyle-Obizhaeva formula grows sharply when volatility is high. The 1% implied impact is the paper's own critical level. — *Financials exceed 1% in summer 2008 and peak near 2.5% in H1 2009. Small caps and financials are above 1% again in Aug-Sep 2011. Large and tech approach 1% in late 2008. Calm periods are around 0.1-0.3%.*
- On financial-index days that already moved 1% by 3pm, the share that moved another 1% in the same direction in the last hour was zero before the first financial LETF launched in 2007. It rose to 0.6-0.8 in the crisis months. — *Figure 4, monthly frequency of an amplified move. This is descriptive, with no controls and few observations per month.*
- LETFs deliver their promised daily multiple closely, so the rebalancing really does happen. — *Table II. Asset-weighted beta is about 0.95-1.05, alpha is near zero, and adj-R² is 0.90-0.996.*

## The WHY
**Pattern:** {"pattern":"Execution mechanics of big players, combined with an institutional mandate. The funds are contractually bound to hold a constant multiple of the index each day. The flow is therefore forced, one-directional and known in advance, and it is concentrated near the close. It is the same kind of flow as VWAP-algo amplification or 1987 portfolio insurance.","mechanism":"A fund promising a daily multiple δ must reset its exposure at the close. After the index moves by r it must trade r×δ×(δ−1)×NAV in the same direction as the move. Long and inverse funds both trade with the move. The trade is executed through futures or swaps, mainly in the last hour, and arbitrageurs pass it through to stocks. Liquidity providers are not fully compensating the price pressure. Other traders also front-run the flow, which pulls the effect earlier into the afternoon. Since the flow carries no information, prices partly revert the next day.","who_is_forced":"The LETF issuers and their swap counterparties, who must rebalance at the close every day regardless of price. The other participants are anticipators and arbitrageurs who trade ahead of that flow. They are predictable, not forced.","why_it_persists":"The daily-multiple promise is contractual. Flow size scales with LETF assets, which have grown a lot since 2011, and with the square of leverage times index move, so volatile days make it larger. The rebalancing flow is known to everyone, so competition from front-runners may have pulled the effect earlier in the afternoon.","what_would_kill_it":"Funds rebalancing earlier or spreading the trades across the day, or moving to closing-auction or MOC execution that absorbs it. LETF assets shrinking. Arbitrageurs and market makers becoming good enough at absorbing the flow. A change to the daily-reset product design. Front-runners moving the effect earlier, so that 15:00 already contains the move.","authors_explanation_vs_ours":"The author frames this as a financial-stability study: LETFs as new portfolio insurers that could cause a cascade. His evidence is thin for that claim. He admits LETFs 'have not been proven to disrupt' markets, and the R² values are very small. The implied-impact and Figure 4 results are descriptive and use a calibrated formula. For trading, the useful part is the narrower claim: forced, predictable closing flow that grows with the day's move and with volatility, and partly reverses the next day. This is a flow-timing edge, not a crash story."},
"tradable_edge":"The edge is a late-session continuation, followed by a next-morning fade, driven by forced LETF rebalancing. Go with the day's move into the close when the index is already far from the prior close at about 15:00 ET and estimated LETF flow is large. The flow estimate is Σ δ(δ−1)×AUM×return, as a share of market volume. The trade is held through the closing hour only. A second leg fades that same move at the next day's open or morning, because the flow has no information and tends to reverse. Both legs scale with the size of the day's move and with the volatility regime. Position size should follow the estimated flow relative to liquidity, not a fixed count. The paper gives per-stock R² of only 0.5-6%, and the extra late-day move is roughly 7bp in a large-cap stock for a 1% index day. Expect a modest gross edge per trade in index futures, so costs and decay matter. Test both legs on index futures, where the effect aggregates.","decay_risk":{"level":"medium","reason":"The mechanism is structural and contractual, and LETF assets have grown since 2011. But the paper was circulated in 2013 and was followed by other work on LETF end-of-day momentum. The edge is small relative to cost: the 15:00-16:00 effect is a few bp per stock. Efficiency of closing-auction handling has improved. The flow estimate needs data we do not have, and the front-running the paper describes would move the effect earlier. It still bites on large-move days, but it is conditional on volatility."},
"data_fit":"Partly testable, as a proxy only. ES 1-minute ETH/RTH from Dec 2013 and NQ 1-minute from mid-2021 allow the index-level test: the 15:00-16:00 ET return conditional on the prior-close-to-15:00 return, and the next-day reversal. This can be split by size of move, by volatility regime and by year (pre/post 2022). It also fits the playbook rule that intraday momentum should be reported by regime. The data does not contain actual LETF AUM or flows, so the flow-scaled version cannot be built. The AUM history would have to be taken from outside (fund assets for SPXL/SPXU/SPXS/TQQQ/SQQQ/UPRO and others). Only index futures can be tested. Single-stock, financial-sector and small-cap results, where the paper's effect is strongest, cannot be tested. There is no YM, RTY or sector-ETF data. The effect also uses a 15:00 ET cutoff, so the UTC timestamps have to be converted with DST handled."},
"referenced_papers_worth_reading">[
{"title":"Dynamics of Leveraged and Inverse Exchange-Traded Funds","authors":["Minder Cheng","Ananth Madhavan"],"venue":"Journal of Investment Management","year":2009,"url":null,"pdf_url":null,"note":"Derives the rebalancing formula and shows aggregate LETF flow pressure on end-of-day S&P 500 returns. This is the key source for an index-level close-momentum test."},
{"title":"Large Bets and Stock Market Crashes","authors":["Albert S. Kyle","Anna Obizhaeva"],"venue":"University of Maryland working paper","year":2012,"url":null,"pdf_url":null,"note":"Source of the implied-price-impact formula used here. Useful for sizing flow-driven impact in a volatility-scaled way."},
{"title":"The Impact of Leveraged and Inverse ETFs on Underlying Stock Returns","authors":["Qianqiu Bai","Shaun A. Bond","Brian Hatch"],"venue":"University of Cincinnati working paper","year":2012,"url":null,"pdf_url":null,"note":"Finds end-of-day price pressure and extra volatility from LETF rebalancing in real-estate stocks. It is a separate sector-level check on the closing-hour effect."},
{"title":"ETFs, Arbitrage, and Shock Propagation","authors":["Itzhak Ben-David","Francesco Franzoni","Rabih Moussawi"],"venue":"Working paper (later Journal of Finance, 2018 as 'Do ETFs Increase Volatility?')","year":2012,"url":null,"pdf_url":null,"note":"Shows that ETF arbitrage passes non-fundamental flow shocks to underlying stocks. This supports the mechanism that futures flow transfers into stocks."}
]




## Setting
- Markets: US equities (TAQ), US equity LETFs, index futures only through the mechanism
- Instruments: US stocks in the S&P 500, Russell 2000, Russell Mid Cap, Russell 1000 Financial Services and Nasdaq 100, 108 equity LETFs
- Period: June 19, 2006 to Dec 31, 2011  Frequency: Daily LETF assets and returns, with intraday stock returns split at 15:00 and 16:00 ET  Holding: Last hour of trading (15:00-16:00 ET), with a next-day reversal tested from the close to 15:00

## Reported results
No trading performance is reported. The paper reports price-pressure coefficients, implied price impact and frequencies, not strategy returns.
- A 1% index rise creates $1.04B of rebalancing flow, which is 0.79-0.84% of daily US stock volume.
- End-of-day price reaction to a 1% index move: 6.9bp for large caps, 13bp for financials, 12.7bp for small caps, 6.3bp for tech, 5.5bp for mid caps.
- Extra close volatility: 22.7bp for large caps, 31bp for financials, 50.5bp for small caps.
- Next-day reversal coefficients are similar in size to the same-day effect but opposite in sign.
- Implied price impact in financials reaches 1.5% after Lehman and about 2.5% in H1 2009.
- Costs: No. There are no transaction costs because no strategy is tested.

## Tradable edge (our framing)


## Angles to test
- Index-futures proxy: on ES (2013 onward) and NQ (2021 onward), long if the prior-close-to-15:00 ET return is above a threshold, short if below, exit at the close. Test across thresholds scaled by trailing volatility.
- Overnight/next-morning fade: take the opposite side at the close and exit at the next open or at 10:30 ET, using the next-day reversal result.
- Flow-scaled version using external AUM for SPXL/SPXU/SPXS/UPRO/SPXU/TQQQ/SQQQ and so on. Compute δ(δ−1)×AUM×return as a share of ES or NQ closing volume, and trade only when the share is high.
- Volatility-conditioned: use only days with a large 15:00 move or VIX above a level, as flow scales with the move and the paper's effect sits in high-volatility periods.
- Report pre- and post-2022 and by signal strength, as the playbook requires for intraday momentum.
- Long-only vs short-only: the up-day effect is stronger than the down-day effect in most categories.
- Other instruments or universes: Russell 2000 futures, financial sector ETFs and small-cap stocks (the paper's largest relative flows), and more recently the 3x single-stock ETFs. This needs data we lack.
- Combine with VWAP or ORB intraday trend filters: only follow the late-day move when the day is already trending relative to VWAP.
- Last-30-minutes momentum variants (15:30-16:00) to check whether the effect has moved later or earlier.

## Decay risk: None


## Data fit


## Caveats
- Effect sizes are small: R² is 0.5-6%, and a 1% index day gives only about 7bp of extra late-day move in an average large cap.
- The flow is hypothetical. The paper never observes actual LETF trades. It assumes rebalancing happens in the last hour, and that assumption comes from other papers.
- The causal link is hard to prove. The 15:00-16:00 return could also reflect ordinary end-of-day momentum, closing-auction imbalances or other flow. The paper's design does not separate these.
- The sample ends in 2011 and covers a crisis period. Coefficients are higher in 2006-2009 than in 2010-2011, so the effect may be concentrated in high-volatility regimes.
- The Kyle-Obizhaeva impact and the Figure 4 frequency are suggestive, not tested. Figure 4 has no controls or standard errors.
- Working-paper draft from 2013 with no trading rules, no costs and no out-of-sample test.
- Flow depends on AUM, which was $20B in 2011 and has grown since, so past coefficients cannot be applied directly.
