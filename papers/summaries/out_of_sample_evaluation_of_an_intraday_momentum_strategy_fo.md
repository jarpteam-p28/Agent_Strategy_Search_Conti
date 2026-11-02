# Out-of-Sample Evaluation of an Intraday Momentum Strategy for the S&P 500 ETF (SPY)

**Authors:** Sheimy Paz  
**Year:** 2026  **Type:** academic  **Read:** abstract_only  
**Source:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7290621

> I could not open this paper, so I have no verified result. From the title alone, it appears to be an out-of-sample test of a SPY intraday momentum (noise-area breakout) strategy. The strategy is probably the one from Zarattini, Aziz and Barbon (2024), but that is an inference.

## Findings
- NOT VERIFIED. Both SSRN fetch attempts failed (the abstract page and a shortened link), and I saw no abstract text or PDF text. I can report no findings from this paper. The title says it is an out-of-sample evaluation of an intraday momentum strategy on SPY. It most likely re-tests the Zarattini-Aziz-Barbon 'Beat the Market' noise-area breakout (trade when price leaves a volatility-based band around the open, with VWAP as the trailing stop and volatility-targeted sizing). This is my guess from the title and the literature. — *None from the paper. The only basis is the title and my background knowledge of the original 2024 paper.*

## The WHY
**Pattern:** Likely 'Institutional constraint / execution mechanics' plus 'information arrives while market closed'. This is a hypothesis about the underlying strategy family, not drawn from this paper.

Intraday momentum (Gao et al. 2018; Zarattini et al. 2024) is usually explained by imbalances that big players cannot absorb at once. These come from overnight news, the demand for hedging and rebalancing late in the day, and dealer gamma hedging. A move beyond the normal daily range (the noise area) shows that demand is one-sided and persists into the close.

- **Who is forced / predictable:** Institutions that must spread large orders over the day (VWAP/TWAP algos), dealers hedging options exposure, and leveraged-ETF rebalancers near the close.
- **Why it persists:** Order-splitting and hedging mechanics are structural. The playbook, however, says intraday momentum depends on the regime, especially after 0DTE growth, when dealers have been net long gamma on expiry days. That would weaken it.
- **What would kill it:** Dealers staying long gamma, so their hedging dampens moves. Crowding of the published strategy. Costs and slippage above the gross edge. Any rule change that lets funds trade the overnight session freely.

## Setting
- Markets: US equities ETF
- Instruments: SPY (per title)
- Period: Unknown  Frequency: Unknown (probably intraday)  Holding: Probably intraday

## Reported results
Not read. No verified results.
- Costs: Unknown

## Tradable edge (our framing)
Unverified, based on the strategy family and not on this paper. Trade an intraday breakout only when price leaves a band around the open that is sized from recent volatility. Go long above the upper band and short below the lower band. Use VWAP or the opposite band as the trailing stop, and flatten at the close. Size positions by volatility targeting. Test it on ES, and on NQ from mid-2021. Report results before and after 2022, by signal strength, and net of costs. Read this paper's own out-of-sample numbers before relying on any of this.

## Angles to test
- Test the same noise-area breakout on ES and NQ 1-minute data. Split results into pre- and post-2022 (0DTE regime).
- Go long only, since breakdowns are often absorbed by buyers.
- Condition on signal strength and on volatility (VIX or ATR).
- Try a late-day momentum variant (last 30 minutes) using the gamma-hedging explanation.
- Add a cost hurdle check: gross points per trade against 2 points of friction on NQ.

## Decay risk: medium
The original strategy was published in 2024 and is widely discussed. McLean and Pontiff suggest roughly half of an edge disappears after publication. I could not see what this out-of-sample paper actually found.

## Data fit
If the paper is the noise-area SPY strategy, ES 1-minute data (2013-2026, RTH and ETH) fits well, and NQ 1-minute data fits from 2021-07. That would allow a long out-of-sample window, including pre- and post-0DTE periods. Missing: SPY itself and dividends (not needed for futures). The exact rules in this paper are unknown until the full text is read.

## Caveats
- The paper's content was not accessed, so every statement here comes from the title and my background knowledge.
- The strategy identification (Zarattini-Aziz-Barbon noise-area breakout) is an inference.
- Someone must re-fetch the full PDF and re-run this summary before any rules are written.
- The author's out-of-sample result, either confirming or failing to confirm the edge, is unknown.

## Cited papers worth reading
- Beat the Market: An Effective Intraday Momentum Strategy for S&P500 ETF (SPY) (2024)
- Market Intraday Momentum (2018)
