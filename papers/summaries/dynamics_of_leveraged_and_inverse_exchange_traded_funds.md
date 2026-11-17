# The Dynamics of Leveraged and Inverse Exchange-Traded Funds

**Authors:** Minder Cheng, Ananth Madhavan  
**Year:** 2009  **Type:** academic  **Read:** abstract_only  
**Source:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1539120

> Leveraged and inverse ETFs must buy after the market rises and sell after it falls, in size and near the close, so the day's direction can feed into the last-hour move, most visibly in volatile periods and narrow sectors.

## Findings
- Daily-reset leveraged ETFs (long and inverse) must rebalance their index exposure every day. The required trade is roughly (L²−L) × fund assets × the day's index return, where L is the leverage multiple. For both +2x/+3x and −1x/−2x/−3x funds the trade goes in the same direction as the day's return: buy after up days, sell after down days. — *Mathematical derivation in the paper. I could not open the full text, so this is from memory of the paper and its widely known result, not checked against the PDF.*
- Rebalancing demand grows with leverage squared, fund assets and the size of the day's move. It is concentrated at the close, because the funds target the closing NAV and swap or futures hedges are reset then. — *From memory. The authors estimated rebalancing amounts for the late-2008 crisis period (high volatility, big daily moves). The amounts were small against total S&P 500 volume but large against closing-auction volume in narrower areas such as financials. I am not certain of the exact figures.*
- Returns over multi-day horizons do not equal L times the index return. They are path-dependent (compounding and volatility drag), so these products are poor buy-and-hold vehicles. — *Analytical result, illustrated with leveraged ETF data from 2008–2009. Exact numbers not verified.*

## The WHY
**Pattern:** {"pattern":"Execution mechanics of big players (plus an institutional constraint: a fixed daily leverage mandate)","mechanism":"A fund promising a constant 2x or 3x daily return must hold exposure equal to L times its closing NAV. After an up day its NAV rises, so it must add exposure. After a down day it must cut exposure. The inverse funds also have to move the same way, because their short exposure is proportional to NAV. Every product therefore adds to the day's direction, and the trade has to be done by the close. That adds same-direction flow late in the session, a bit like a portfolio-insurance trade.","who_is_forced":"Leveraged and inverse ETF sponsors and their swap counterparties or authorised participants. They have no discretion over size or timing, since both are fixed by the fund's prospectus and the day's return. Market makers on the other side absorb the flow or front-run it.","why_it_persists":"It comes from the product's contractual design. Assets under management in leveraged ETFs stayed large or grew after 2009, and the rebalance rule is mechanical. Volatility on big-move days also scales the flow up.","what_would_kill_it":"Smaller leveraged-ETF assets, or a switch to intraday rebalancing. Other participants front-running the flow earlier in the day, so it is priced before the final minutes. Market makers or closing-auction liquidity growing enough to absorb it. For indices as deep as ES and NQ the flow is small relative to total volume, so the effect may be too small to survive costs. It is probably strongest in narrower sector indices.","authors_explanation_vs_ours":"The authors' point is mostly about market-impact and systemic risk: whether the rebalancing could destabilise closing prices, especially in sectors. They do not offer a trading strategy. Our framing treats it as a same-day momentum prediction for the last 30–60 minutes. The paper does not demonstrate this directly, and later work (e.g. Gao et al. on intraday momentum) points to other contributors such as hedgers and dealer gamma."},"tradable_edge":"The day's move (open or prior close to about 15:00 ET) produces a predictable same-direction flow into the close from leveraged and inverse ETF rebalancing. This is a late-day continuation (last 30–60 minutes) on index futures. Candidates are NQ and ES, with entry after a large absolute day move and exit at the close or just before it, and possibly a filter on how large the day move is. The prediction is strongest when volatility is high and the day's move is large, because the flow scales with the return. The test is whether this beats a plain 'always long the last half hour' baseline.","decay_risk":{"level":"high","reason":"Published in 2009 and widely cited. The closing-flow link is well known to dealers and quant desks, and later papers (Tuzun 2013, Shum et al. 2016) cover it. The last-half-hour momentum effect has also been documented and traded. The effect is probably small on ES and NQ relative to total volume. Treat it as a regime-dependent tilt, not a standalone edge."},"data_fit":"Partly testable. ES 1-min from 2013-12 and NQ 1-min from 2021-07 are enough to build day-return-to-close-return tests: the return from open or prior close to 15:00 or 15:30 ET against the 15:30 or 15:45 to 16:00 return. Test it by absolute day move, by volatility regime, and pre/post 2022. The 0DTE era is a confound, since dealers have been net long gamma on expiry days. Missing: leveraged-ETF AUM and daily rebalance estimates (needed to scale the signal; the day-return size is a proxy), sector indices and sector futures (the paper's strongest case is in narrow sectors), and closing-auction volume. NQ history before 2021-07 is also missing, so NQ has no crisis-period test. Open at 09:30 ET and the 16:00 ET close should be handled as RTH sessions in UTC.","angles":["Instrument: ES and NQ futures, because the Nasdaq-100 has large 2x and 3x ETF assets (QLD, TQQQ, SQQQ). Compare the two for the size of the effect.","Session: trade only the last 30 minutes (15:30–16:00 ET), or the 15:45–16:00 window, with a time exit at the close.","Conditioning: take trades only when the absolute day return exceeds a threshold (for example 1% or 1.5×ATR), or when VIX or realised volatility is high, since the flow scales with the move and with L²−L.","Side: test long-only after up days versus short after down days. Dip-buying and short-covering may make the two sides asymmetric.","Combination: pair with the intraday momentum literature (first half-hour return predicts last half-hour) and with dealer gamma levels as filters.","Reversal angle: test whether the closing push is followed by an overnight or next-open reversal when the flow was large (possible overreaction that reverses). Risk-premium-style overnight pattern."]




## Setting
- Markets: 
- Instruments: 
- Period:   Frequency:   Holding: 

## Reported results
No trading-strategy performance is reported. The contribution is a formula for daily leveraged-ETF rebalancing flow, plus estimates of that flow against market volume.
- Rebalancing ≈ (L²−L) × AUM × daily index return, in the direction of the day's move. Exact empirical estimates not verified.
- Costs: Not applicable

## Tradable edge (our framing)


## Angles to test

## Decay risk: None


## Data fit


## Caveats
- I could not access the SSRN page or PDF, so this summary rests on my memory of the paper and on the published literature. Numbers, sample details and any empirical claim should be verified before use.
- The paper is mainly theoretical and descriptive. It does not test a trading rule, and the late-day momentum link is our inference.
- The effect size for broad indices like ES/NQ is likely small against closing volume. The paper's strongest cases are narrower sector funds.
- The sample covers the 2008–2009 crisis, an unusual high-volatility, high-flow period. Leveraged ETF assets are much larger now, but so is the 0DTE options volume that can mask or offset the flow.

## Cited papers worth reading
- Are Leveraged and Inverse ETFs the New Portfolio Insurers? (2013)
- Intraday Share Price Volatility and Leveraged ETF Rebalancing (2016)
- Market Intraday Momentum (2018)
- Path-Dependence of Leveraged ETF Returns (2010)
