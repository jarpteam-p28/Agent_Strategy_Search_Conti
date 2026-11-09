# Do Leveraged ETFs Really Amplify Late-Day Returns and Volatility?

**Authors:** Ivan T. Ivanov, Stephen L. Lenkey  
**Year:** 2018  **Type:** academic  **Read:** abstract_only  
**Source:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2504012

> The SSRN page and the PDF both failed to load, so this is not read from the paper; from memory, the authors argue that leveraged-ETF rebalancing is too small and too poorly timed to explain the late-day momentum and volatility seen in the last 30 minutes, so a trade built on 'LETF rebalancing flow' is a weak WHY.

## Findings
- Earlier work (Cheng & Madhavan 2009, Tuzun 2013 and others) said daily rebalancing by leveraged and inverse ETFs pushes prices in the same direction as the day's move into the close, and so adds to late-day returns and volatility. Ivanov & Lenkey test this and, as I recall, find the evidence much weaker than claimed. — *Not verified. The paper could not be fetched. This is my recollection of the paper's framing, not a quote or a figure from it.*
- As I recall, the rebalancing demand implied by LETF assets is small next to normal closing-period volume and market depth for most underlyings. Late-day momentum also shows up where LETF effects should be absent, or before LETFs existed, and it can be explained by other forces. — *Not verified. No sample, period or statistics could be read, so none are given here.*
- Anyone using this paper should check the exact claims, sample and numbers directly. I did not read them. — *Access failed for the SSRN abstract page. The Fed and ScienceDirect URLs were blocked because they had not appeared in earlier results.*

## The WHY
**Pattern:** Execution mechanics of big players / institutional constraint (the LETF-rebalancing story). This paper is a critique of that story, not a confirmation of it.

Leveraged ETFs must rebalance daily to hold their target leverage, which means buying after up days and selling after down days, in the same direction as the day's move. The trades happen near the close, so they could amplify the day's move over the last 30 minutes. This paper (as I recall) argues the flow is too small to matter, which weakens this as the WHY. A better-supported WHY for last-30-minute continuation is broader: late-day trading by institutions and hedgers, dealer gamma hedging, and information arriving slowly during the day.

- **Who is forced / predictable:** LETF issuers and their swap counterparties are forced to rebalance at the close. The paper argues the amounts are small. Other forced flows at the close include index funds, MOC order imbalances and dealer hedging.
- **Why it persists:** If the LETF effect exists at all, it persists because the rebalancing mandate is contractual. The broader late-day momentum persists because of institutional execution patterns. Persistence is not established by this paper.
- **What would kill it:** A trade premised on LETF rebalancing would die if LETF assets shrank or if the flow was never material. A late-day momentum trade would die if dealers' gamma positions flipped, as in the post-2022 0DTE regime, or if MOC liquidity absorbed the flow.

## Setting
- Markets: US equities (reported); not verified
- Instruments: Leveraged and inverse ETFs and their underlyings (reported); not verified
- Period: Unknown  Frequency: Intraday (unverified)  Holding: Last ~30 minutes of the session (unverified)

## Reported results
Not verified. The paper could not be read.
- Costs: Unknown

## Tradable edge (our framing)
Treat last-30-minute continuation as a separate question from LETF flow. Test whether the return from the open, or from the last full session, up to 15:30 ET predicts the 15:30–16:00 return on ES and NQ. Hold it for a fixed time with no stop, and compare it to a long-always baseline. Split the results by volatility, by year before and after 2022, and by signal strength. Use this paper mainly as a warning: the LETF rebalancing WHY is contested, so size the trade as a modest, regime-dependent drift and not as a forced-flow edge.

## Angles to test
- ES and NQ: signal = return from the prior close or the open to 15:30 ET. Enter at 15:30 in the signal's direction and exit at 15:59, with fixed size and no stop.
- Condition on signal size, using only strong-move days, and on volatility regime.
- Run pre-2022 versus post-2022 separately, since 0DTE dealer gamma may have changed the late-day flow.
- Compare ES with NQ. NQ should be more exposed to LETF effects, since Nasdaq-linked leveraged products are large. That is a test of the LETF WHY, but we only have NQ from 2021.
- Use as a conditional filter on other end-of-day strategies, not as a standalone one.
- Test one side only: late-day long continuation after up days versus short continuation after down days.

## Decay risk: medium
The late-day momentum and LETF-rebalancing idea has been public since 2009, and this paper (2018) argues it is overstated. Intraday momentum is regime-dependent, and 0DTE dealer positioning since 2022 changes the late-day flow. Expect roughly half of any published number, and less after costs.

## Data fit
{"text":"Partly testable. ES 1-minute data from 2013 and NQ 1-minute data from mid-2021 are enough to test late-day continuation, with the last 30 minutes conditioned on the return so far that day. We lack ETF AUM or LETF rebalancing-demand data, and we lack single stocks, so the paper's cross-sectional LETF tests cannot be reproduced. NQ has no history before mid-2021, so a pre/post-LETF-growth split is only possible on ES."}

## Caveats
- Not read: the full paper and the abstract were inaccessible, and the summary is from memory.
- All findings above are unverified and the paper's actual numbers are unknown.
- If this paper is used further, a fresh reader should fetch the real text, for example from the Journal of Financial Markets version (2018), before relying on it.
- The paper is skeptical of the LETF mechanism, so it does not itself supply a tradable edge.

## Cited papers worth reading
- Leveraged and Inverse ETF Rebalancing and Market Close (2009)
- Trading Volume Predictions and Intraday Momentum / Market Intraday Momentum (2018)
- Leveraged ETF rebalancing and late-day returns (Tuzun) (2013)
