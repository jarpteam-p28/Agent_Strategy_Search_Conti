# The Dynamics of Leveraged and Inverse Exchange-Traded Funds

**Authors:** Minder Cheng, Ananth Madhavan  
**Year:** 2009  **Type:** academic  **Read:** abstract_only  
**Source:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1539120

> Leveraged and inverse ETFs must rebalance at the close in the same direction as the day's market move, which creates predictable late-day order flow that pushes the market further the way it already went.

## Findings
- I could not open the SSRN page or the PDF. The notes below come from my memory of the paper and of the literature that cites it, not from reading the text. Check the numbers before relying on them. — *Fetch of the SSRN URL failed. No quantitative results were read.*
- Leveraged ETFs (2x, 3x) and inverse ETFs (-1x, -2x, -3x) promise a multiple of the index's daily return. To keep that promise they have to rebalance their derivative exposure every day. When the index rises they must buy more exposure, and when it falls they must sell. This holds for leveraged and inverse funds alike. The size of the flow is about AUM × L(L-1) × the day's return. — *Mathematical derivation in the paper. The required rebalancing grows with leverage squared, fund AUM and the size of the day's return.*
- The rebalancing happens near the close, so it adds to the closing-period volume and can move prices in the last part of the day. The authors argue that in volatile markets (e.g. late 2008, financial-sector funds) the flow is large compared with the underlying market's closing liquidity. — *Recalled from the paper's illustrative calculations on sector and index funds around 2008-2009. Exact magnitudes not verified.*
- Path dependence: over periods longer than a day, a leveraged fund's return is not the leverage multiple of the index's return. Volatility drag erodes returns, and with high volatility and a choppy path even the sign can differ. This is a product-design point, not a trading signal in itself. — *Analytical and numerical examples in the paper.*

## The WHY
**Pattern:** {"pattern":"Execution mechanics of big players, plus an institutional constraint (a mandate). This is like the VWAP-algo pattern: a rule-bound participant trades in a predictable direction at a predictable time.","mechanism":"A leveraged or inverse ETF is contractually bound to hold a constant multiple of the index's return each day. After the index moves, its leverage drifts away from the target. The fund (or its swap counterparties, who hedge in futures and stocks) must trade to restore it. The trade is in the direction of the day's move and is sized by the day's return. It is executed late, because the NAV is struck at the close and the exact day return is only known then. This adds buying pressure into the close on up days and selling pressure on down days. Momentum into the close is the result. The effect is bigger when the day's move is large and when the funds' AUM is large relative to the underlying's closing liquidity.","who_is_forced":"The ETF sponsors and their swap dealers have to rebalance. They cannot choose to skip it, and they have to do it in the last minutes before the NAV is set. Market makers and arbitrageurs who understand the schedule can trade ahead of it, and that amplifies the move.","why_it_persists":"It comes from how the product is built (a daily-reset constant-leverage promise), not from market inefficiency. Flows scale with AUM, which has grown since 2009 (TQQQ, SQQQ, SPXL, SPXU, etc.). The direction of the flow is known in advance once the day's return is known. Late-day momentum has also been documented in later work on intraday momentum (Gao-Han-Li-Zhou) and on ETF rebalancing, which is consistent with this.","what_would_kill_it":"Regulation or products that remove the daily reset. Sponsors moving rebalancing into the closing auction or spreading it over the day. Front-running arbitrageurs who trade the flow earlier and shrink the late-day move. Dealers netting offsetting flow across funds. Closing-auction liquidity growing faster than LETF AUM. Dealers being long gamma and absorbing the flow in the 0DTE era (Adams et al., 2025)","authors_explanation_vs_ours":"The authors write about the size of the rebalancing flow and the market-quality risk (possible volatility at the close). They do not present a tested trading strategy. Turning it into a signal is our work. In practice other late-day effects (rebalancing by other participants, MOC imbalances, 0DTE hedging) overlap with LETF flows, so the effect cannot be cleanly attributed to LETFs alone."}}




## Setting
- Markets: US equity ETFs
- Instruments: Leveraged and inverse ETFs, Underlying index/sector futures and swaps
- Period: Around 2008-2009 (not verified)  Frequency: Daily fund data and illustrative calculations (from memory; unverified)  Holding: Intraday, last part of the trading day (implied)

## Reported results
Not read. Paper is analytical; no trading strategy is reported to my knowledge.
- Costs: Not applicable (no strategy backtest recalled).

## Tradable edge (our framing)
Trade the forced close-of-day rebalancing flow. After a big up day in the index, be long into the final 30-60 minutes of the cash session. After a big down day, be short or stay out. The signal is the day's return so far, from open or prior close to about 15:00 ET. It is stronger when the move is large (the flow scales with the return and with LETF leverage, L²−L). Exit at the cash close, or at the start of the closing auction. The edge is the late-session continuation of the day's direction, which comes from mandated rebalancing. It is not a general momentum bet.

## Angles to test
- Different instrument: test ES versus NQ. NQ should show a stronger effect because of the Nasdaq LETFs (TQQQ, SQQQ). Compare with the other futures once data exist (RTY, financials).
- Different session: last 30 minutes versus last 60 minutes of RTH. Entry at 15:00 or 15:30 ET, exit at 16:00 ET. Also check the 15:30-16:15 futures window.
- One side only: test longs after up days and shorts after down days separately. Up-days may be stronger (buyers absorb, and the dip-buying bias is stronger).
- Signal strength: only trade when the day's absolute return is above a volatility-scaled threshold (e.g. a multiple of ATR), since the flow scales with the return. Also test on high-vol days, when the flow is bigger.
- Combine with intraday momentum (first half-hour return predicting the last half-hour) and with the 0DTE gamma regime. The effect should be strongest when dealers are short gamma.
- Regime split: before and after 2022 (0DTE growth), and across days with FOMC or other scheduled events.
- Fade the other way: if the move reverses the next morning (the overnight reversal of price pressure), test an open-to-first-hour reversal trade after large flow days.

## Decay risk: medium
The paper was published in 2009. Late-day momentum and LETF rebalancing are well known (Tuzun 2013, Bessembinder 2015, Shum et al. 2016, Gao et al. 2018), and arbitrageurs front-run the flow. But the flow is structural and LETF AUM has grown. Expect a smaller, regime-dependent effect (McLean & Pontiff: about half the published size, less after costs), likely weaker since 0DTE options changed dealer gamma around 2022.

## Data fit
"Partly testable. ES 1-min bars (2013-12 to 2026-09, ETH and RTH) cover the full test: day return to 15:00 ET versus the 15:00-16:00 return. NQ 1-min covers 2021-07 onward only, which is shorter but includes the most relevant index for TQQQ/SQQQ. Costs: a hold of 30-60 min is fine against the ~2-point NQ friction hurdle. Missing: LETF AUM and flow data (use the absolute day return as a proxy, and AUM growth as a time trend), closing-auction imbalance data, ETF prices. Report results pre/post 2022 and by signal strength. Timestamps are in UTC, so convert to ET and handle DST carefully."

## Caveats
- I could not fetch the paper. Every statement about its content is from memory and general knowledge, so the findings carry no quoted evidence or exact numbers.
- The paper is mostly an analysis of flows and market-quality risk. It does not test a trading strategy, so there is no reported performance, no costs and no sample-period Sharpe to cite.
- The flow formula is for the index-return day. Real rebalancing is spread over several funds and swap counterparties, and dealers may already hedge intraday. Net flow is not directly observable.
- The effect may be mixed up with the general late-day momentum documented in other work and with MOC imbalances. It cannot be cleanly attributed to LETFs without the AUM data.

## Cited papers worth reading
- Are Leveraged and Inverse ETFs the New Portfolio Insurers? (2013)
- Market Timing and Return Prediction under Model Instability / Market Intraday Momentum (2018)
- Predictable ETF Order Flow and Market Quality (2015)
- Intraday Share Price Volatility and Leveraged ETF Rebalancing (2016)
- Do ETFs Increase Volatility? (2018)
