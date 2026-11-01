# Post-Earnings-Announcement Drift: Delayed Price Response or Risk Premium?

**Authors:** Victor L. Bernard, Jacob K. Thomas  
**Year:** 1989  **Type:** academic  **Read:** abstract_only  
**Source:** https://ideas.repec.org/a/bla/joares/v27y1989ip1-36.html

> After a company reports earnings far above or below expectations, its stock keeps moving the same way for about 60 days. Bernard and Thomas find this is mostly because investors react slowly, not because of a hidden risk premium.

## Findings
- The JSTOR PDF was blocked and the IDEAS page has no abstract, so I could not read the paper. The findings below come from my memory of this well-known paper and are not verified against the text. Check the numbers before relying on them. — *web_fetch of the JSTOR PDF returned a JavaScript client challenge. The IDEAS page returned only metadata and keywords: post-earnings drift, risk premium, delayed market reaction, incomplete risk adjustment.*
- Stocks sorted on standardized unexpected earnings (SUE, a time-series surprise measure) keep drifting in the direction of the surprise for roughly 60 trading days after the announcement. A long-top-decile, short-bottom-decile hedge earns a few percent over that window (recalled as about 4% before costs). — *Recalled: NYSE/AMEX firms, roughly 1974-1986, quarterly earnings, SUE deciles. Not verified.*
- The drift is concentrated around the next quarters' earnings announcements. Part of the post-announcement return comes in the 3-day windows around later announcements, and those returns have the same sign as the earlier surprise. This pattern suggests the market misjudges how seasonal earnings changes persist. Earnings surprises are positively autocorrelated over the next three quarters and negatively correlated at the fourth lag. — *Recalled from the paper's main argument. Not verified.*
- The risk-premium story does not fit well. Drift does not line up with betas or size-based risk measures, and it shows up as surprises when later earnings arrive, which a rational risk premium would not predict. The authors also note that transaction costs and thin trading in small firms may limit how much arbitrage can remove it. — *Recalled. Not verified.*

## The WHY
**Pattern:** Slow information diffusion, plus liquidity constraints on large orders. This is the PEAD pattern from playbook §4.

Investors do not fully see what a quarterly surprise implies for later quarters, because earnings changes tend to persist. Prices therefore adjust step by step, with another jump at each later announcement. Low coverage of small firms, and funds that spread out their buying to avoid moving the price, stretch the adjustment further.

- **Who is forced / predictable:** Analysts and investors who anchor on the last seasonal earnings change and update slowly. Institutions that cannot build a full position in a day and so buy or sell over days or weeks. Arbitrageurs who find trading small, illiquid stocks too costly to remove the mispricing.
- **Why it persists:** Frictions remain: transaction costs, limited coverage of small and mid caps, and capacity limits on large positions. Behavioural anchoring on past earnings also remains. The drift has weakened in large caps since publication.
- **What would kill it:** Better and faster analyst coverage. Cheaper, faster trading in small caps. Firms pre-announcing bad news, which weakens the short side. Strategy crowding. In mega caps the edge is already gone.
- **Paper's view vs ours:** The authors compare delayed price response against a risk premium and favour delayed response, based on drift clustering at later announcements. We agree. I add an execution-mechanics layer: large investors splitting orders, and the cost of arbitrage in small caps. I cannot confirm how much of that the paper discusses.

## Setting
- Markets: US equities (NYSE/AMEX)
- Instruments: Individual stocks
- Period: About 1974-1986 (recalled, unverified)  Frequency: Quarterly earnings, daily returns  Holding: About 60 trading days

## Reported results
Unverified recall: the extreme-SUE hedge portfolio earned a few percent over about 60 days after the announcement. The effect was strongest in small firms, and part of it arrived at later earnings announcements.
- Not verified: roughly 4% hedge return over 60 days.
- Not verified: drift clustered in the 3-day windows around the next three quarterly announcements.
- Costs: Unknown. The paper discusses transaction costs as a limit on arbitrage, but I could not verify net results.

## Tradable edge (our framing)
Rank stocks on how far the latest quarterly earnings beat or missed a surprise benchmark. Hold the extreme surprises in the direction of the surprise for about 60 days, which is the horizon at which the slow reaction plays out. Focus on small and mid caps where coverage is thin, and consider the long side first because the short side has weakened. The 1989 paper provides the horizon and the idea of a time-series surprise. In our framework, newer analyst-consensus surprises and price reaction around the announcement would be added.

## Angles to test
- Different universe: small and mid caps, or European stocks with lower coverage and liquidity. Skip mega caps.
- One side only: long positive surprises, since the short side is weaker now.
- Combine findings: price reaction at the announcement (Ball and Brown 1968), the 60-day horizon (this paper), and analyst-consensus surprise (Livnat and Mendenhall 2006).
- Time entry or exit around the next quarter's announcement, where much of the drift arrives.
- Index-futures proxy: after mega-cap earnings clusters, test continuation in NQ or ES over several days. This is speculative and has weak links to the stock-level WHY.
- Size positions by volatility or as a percentage of portfolio. Keep each position small because of capacity limits in small caps.

## Decay risk: high
Published in 1989 and one of the most replicated anomalies. It has faded in large caps and weakened with cheaper trading and wider coverage. Some residual effect remains in small and mid caps and in less-covered markets.

## Data fit
We cannot test it with the current inventory. The inventory has only ES and NQ futures bars and ticks. It has no single-stock prices, earnings dates, actual EPS, or analyst consensus estimates, which PEAD needs. The inventory lists these as not available. A possible proxy is the ES/NQ reaction on large-cap earnings days, but the data does not identify which stocks reported.

## Caveats
- I could not read the paper. The numbers are from memory and unverified.
- The drift is weaker and more expensive to capture after costs, especially on the short side of small illiquid stocks.
- The original sample is 1974-1986 and is long outdated.
- Our inventory lacks the required data.

## Cited papers worth reading
- Post-Earnings-Announcement Drift: The Role of Revenue Surprises / Analyst-based surprise measures (Livnat and Mendenhall: Comparing the Post-Earnings Announcement Drift for Surprises Calculated from Analyst and Time Series Forecasts) (2006)
- An Empirical Evaluation of Accounting Income Numbers (1968)
- The Post-Earnings-Announcement Drift and Liquidity Risk / Trading frictions and PEAD (e.g., Sadka 2006; Chordia et al. 2009) (2009)
