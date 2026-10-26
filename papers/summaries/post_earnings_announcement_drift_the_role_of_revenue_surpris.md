# Post-Earnings-Announcement Drift: The Role of Revenue Surprises

**Authors:** Narasimhan Jegadeesh, Joshua Livnat  
**Year:** 2006  **Type:** academic  **Read:** abstract_only  
**Source:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=903767

> Post-earnings drift is better predicted when you combine the earnings surprise with the revenue surprise, because revenue is harder to manipulate and tells you whether an earnings beat is likely to persist.

## Findings
- Revenue surprise (actual quarterly sales vs. a seasonal-random-walk expectation, scaled by its volatility) predicts subsequent stock returns. It does this even after controlling for the earnings surprise (SUE). — *From memory of the paper, not verified. The sample is US stocks from roughly the late 1980s to early 2000s, using Compustat quarterly data. I could not access the text, so no exact numbers are given.*
- Stocks with both a strong earnings surprise and a strong revenue surprise drift more than stocks with only an earnings surprise. A long-short strategy on the joint signal beats one that uses earnings alone. — *From memory, not verified. I recall the drift lasting about 6 months after the announcement, but I could not check the figures.*
- Revenue surprises carry information about the quality and persistence of earnings. Earnings beats driven by cost cuts or accruals are less persistent than beats backed by sales growth. — *From memory, not verified. I believe the paper also finds that revenue surprise predicts later earnings surprises, but I could not confirm this.*

## The WHY
**Pattern:** Slow information diffusion (primary), plus liquidity constraints on large orders (secondary).

Investors anchor on the headline EPS number and under-react to the less visible revenue component. Revenue is a cleaner signal of demand and is harder to manage than earnings, so it says more about whether the beat will persist. Investors update only slowly. Institutions also build positions over days or weeks, which stretches the price adjustment.

- **Who is forced / predictable:** Small and mid-cap stocks have thin analyst coverage and limited arbitrage capital. Large funds can't build full positions on announcement day, so they buy gradually. Many investors and screens focus on EPS only.
- **Why it persists:** Limits to arbitrage remain in small caps, such as costs, thin liquidity and short-sale constraints. The cause is behavioural and structural, not a one-off mispricing. Revenue is also now widely reported, so the effect may be partly arbitraged away in large caps.
- **What would kill it:** Faster and wider adoption of revenue-surprise screens by quant funds. Better analyst coverage of small caps. Companies pre-announcing bad news, which weakens the short side. Higher liquidity or lower costs that let arbitrageurs trade the drift away.
- **Paper's view vs ours:** As I recall, the authors frame this as market under-reaction to the information in revenue, and they show revenue surprise is a distinct signal. That matches our WHY. I couldn't verify the details, so check the original text before relying on this.

## Setting
- Markets: 
- Instruments: 
- Period:   Frequency:   Holding: 

## Reported results


## Tradable edge (our framing)
After a quarterly report, go long stocks where both the earnings and the revenue surprise are strongly positive. Hold them for about 60 trading days with volatility-scaled sizing. The revenue confirmation screens out low-quality EPS beats and leaves announcements the market is likely to keep digesting. Small and mid-caps and the long side are where this should work best. Use consensus-based surprises where available, because the original paper's seasonal random-walk revenue expectation is the weaker version.

## Angles to test
- Different universe: small and mid-cap stocks in the US and Europe, where coverage and liquidity are lower. Skip mega-caps.
- One side only: long-only on joint positive earnings and revenue surprises. Check it still works in a down year such as 2022.
- Combine signals (the Conti PEAD recipe): price reaction on announcement day, a 60-day hold, and the consensus-based earnings and revenue surprise together.
- Use revenue-surprise divergence as a filter. An EPS beat with a revenue miss means a low-quality beat, so skip it or fade it.
- Index proxy: for ES and NQ, test whether aggregate revenue surprise or aggregate earnings breadth predicts index drift over the following weeks. This needs outside data.

## Decay risk: medium
The paper was published in 2006 and the PEAD family is very well known. Revenue surprise is easy to compute and widely used by quants. Large caps have lost most of the drift. The structural cause (slow diffusion, small-cap frictions) remains, so some effect probably survives in small and mid-caps and outside the US.

## Data fit
We can't test it directly. We have no single-stock data, earnings dates, actual EPS or revenue, or analyst consensus estimates. We only have ES and NQ futures. A rough index-level proxy would be to trade ES and NQ around mega-cap earnings clusters, but that is a different effect and very weak. We would need a stock universe (small and mid-caps, ideally including Europe) with fundamentals and consensus data.

## Caveats
- I could not access the SSRN page or the PDF, so this summary comes from memory of the paper and not from the text. The numbers are deliberately left out. Verify before use.
- The original revenue surprise uses a seasonal random walk with drift, not analyst revenue consensus. Consensus-based versions may behave differently.
- Published results often exclude trading costs, and PEAD is concentrated in small and illiquid stocks. Net returns may be much lower.
- The short side has probably weakened because of pre-announcements and borrow costs.

## Cited papers worth reading
- Post-Earnings-Announcement Drift: Delayed Price Response or Risk Premium? (1989)
- The Information Content of Revenue Surprises / Revenue surprises and stock returns (2006)
- Market Underreaction to Open Market Share Repurchases / Post-earnings drift literature by Ball and Brown (1968)
