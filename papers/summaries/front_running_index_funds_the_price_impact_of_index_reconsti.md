# Index Changes and Losses to Index Fund Investors

**Authors:** Honghui Chen, Gregory Noronha, Vijay Singal  
**Year:** 2006  **Type:** academic  **Read:** abstract_only  
**Source:** https://ssrn.com/abstract=922296

> Stocks added to (or dropped from) the S&P 500 are pushed up (or down) between the announcement and the day index funds trade, and the move partly reverses afterward, so index funds that buy or sell at the effective date lose money.

## Findings
- I could not open the paper. SSRN and the other URLs failed, so this summary comes from memory of the paper's topic and not from the text. Every number needs checking against the paper. — *Fetch of the SSRN abstract page failed. No PDF was available.*
- As I remember it, the paper looks at S&P 500 additions and deletions. Added stocks gain between the announcement and the effective date, when index funds must buy. Deleted stocks fall over the same window. Part of the move reverses after the effective date, so the price pressure is partly temporary. — *Recalled, not verified. Sample and period (probably the 1990s into the early 2000s) and effect sizes are not confirmed.*
- As I remember it, the paper estimates the cost to index fund investors of trading at the effective-date close. It also notes that the permanent, demand-curve part of the S&P price effect has shrunk in recent years. The earlier literature is Shleifer 1986 and Harris & Gurel 1986. — *Recalled, not verified.*

## The WHY
**Pattern:** Institutional constraint / mandate, plus execution mechanics and liquidity constraints of big players

Index funds must hold the index and are judged on tracking error, so they all buy additions and sell deletions at the same close, the effective date. Arbitrageurs front-run that demand after the announcement. This pushes prices away from fair value in the window. Once the forced demand is over, prices partly revert.

- **Who is forced / predictable:** Index funds and ETFs trade at the effective-date close because tracking error is what they are measured on. Event-driven arbitrageurs and hedge funds take the other side by front-running, and they exit into the index funds' demand.
- **Why it persists:** The tracking-error mandate remains. The announcement-to-effective-date gap is still predictable and the volume at the close is still huge. Competition among arbitrageurs has made the effect smaller and faster, but the forced flow itself persists.
- **What would kill it:** Index providers could announce changes and make them effective almost at once. They could phase changes in over several days. Funds could be allowed to trade at other times or to sample the index. Arbitrage capital could grow enough to move prices on the announcement itself, leaving nothing to capture afterwards. S&P has already moved toward shorter gaps and after-close announcements.
- **Paper's view vs ours:** The authors frame the result as a cost to index fund investors. I read the same facts as a forced-flow, predictable-trader story: the price-pressure explanation fits the partial reversal, while the information explanation does not. The permanent part of the effect is contested.

## Setting
- Markets: US equities
- Instruments: S&P 500 constituent stocks
- Period: Not verified  Frequency: Daily (event study)  Holding: From announcement to a few days after the effective date

## Reported results
Not verified. The paper reports price run-ups for additions between announcement and effective date, partial reversal afterward, and resulting losses to index funds.
- Costs: Unknown

## Tradable edge (our framing)
Index-change events create forced, scheduled buying or selling. An index addition lifts the stock from the announcement to the effective-date close. After that the forced buyers are gone and part of the move reverses. The edge is to ride, or fade, the pressure window. A simpler version is to trade the reversal in the days after the effective date. The strongest version is to trade the index-level equivalent: the quarterly rebalance and futures-expiry flow around the close, which ES and NQ can capture without stock data. The single-stock event trade is the cleanest test, but we lack the stock and event data for it.

## Angles to test
- Different universe: Nasdaq-100, Russell reconstitution (late June), MSCI and FTSE rebalances, and European or Asian indices. Small-cap and less liquid names should show stronger pressure.
- Different session: the effective-date closing auction. Test a fade after the close, or the next day's open.
- One side only: additions have historically been the stronger leg. Deletions are weaker and short-sale constrained.
- Index-level proxy on ES/NQ: look at returns and volume in the last 30 minutes on quarterly triple-witching and rebalance days against ordinary days. The NQ data starts in 2021-07, so it covers only that period. ES has 2013 onward.
- Combine with the PEAD or short-term reversal literature: after the effective date, buy deleted names or short added names as a reversal trade.
- Check whether the effect has weakened since announcements moved to after the close and since ETFs grew.

## Decay risk: high
The S&P 500 addition effect has been known since the 1980s and the paper is from 2006. Later studies find the effect smaller and faster, with the gains now arriving mostly on the announcement day. Index funds have also moved to trading earlier, and arbitrage capital is heavy. The published edge is probably mostly gone for the large caps.

## Data fit
"The core single-stock test cannot be run. We have no single-stock prices, no index membership change dates and no announcement or effective dates. Only an ES or NQ proxy is possible: check closing-auction flow, volume and returns on rebalance and triple-witching days with the 1-minute data. NQ covers 2021-07 on and ES covers 2013-12 on. Those proxies test a related idea, not this paper's finding."

## Caveats
- read_mode is abstract_only and the paper itself was not read. The findings are from memory and the numbers are not reported here because I cannot verify them.
- The paper's emphasis is on losses to index funds, not on a trading strategy. The tradable framing is ours.
- Published edges shrink after publication, so plan on well under the paper's numbers (McLean & Pontiff).

## Cited papers worth reading
- Demand Curves for Stocks Do Slope Down (1986)
- Price and Volume Effects Associated with Changes in the S&P 500 List (1986)
- The Price Effects of S&P 500 Index Changes: Is the Demand for Stocks Perfectly Elastic? (2004)
