# Market Liquidity and Funding Liquidity

**Authors:** Markus K. Brunnermeier, Lasse Heje Pedersen  
**Year:** 2009  **Type:** academic  **Read:** abstract_only  
**Source:** https://doi.org/10.1093/rfs/hhn098

> A theory paper showing that when traders' funding gets tight, market liquidity dries up across assets at once and prices become fragile, which creates a feedback loop between market liquidity and funding liquidity (margin spirals).

## Findings
- Theory model: speculators (dealers, hedge funds) provide market liquidity, and their capacity depends on the funding they can get. Funding depends on the margins their lenders require, and margins depend on the volatility of the asset and the asset's market liquidity. — *Theoretical model (RFS 2009). I could not open the paper and am writing from memory of it. I did not read the full text and the model details are not verified.*
- Market liquidity and funding liquidity reinforce each other through two spirals. In the loss spiral, losses erode capital and force sales. In the margin spiral, higher margins force deleveraging. Both push prices further from fundamentals. — *Model result. It is an equilibrium analysis, not an empirical backtest.*
- Market liquidity has a common component across securities, and it co-moves with funding conditions and volatility. Liquidity can suddenly drop (be fragile) when funding gets tight, so it behaves non-linearly. — *Model propositions. The paper cites empirical support from the 1998 LTCM crisis, the 2007-08 crisis and the 1987 crash. I did not verify the figures.*
- Securities with higher margins are more sensitive to funding shocks. Their prices should show higher required returns, and their margins should go up when volatility rises. Liquidity risk has a premium: assets whose liquidity co-moves with funding conditions earn higher expected returns. — *Model predictions. The paper states them as testable implications. It does not run a trading test.*

## The WHY
**Pattern:** Institutional constraint / mandate, plus liquidity constraints on large orders. This is a forced-seller version: margin calls and capital limits force leveraged players to deleverage in a predictable way. It is also a liquidity risk premium.

Leveraged liquidity providers fund their positions with collateralised short-term borrowing. When volatility rises or they take losses, lenders raise margins and their capital shrinks. They must cut positions and stop providing liquidity. Spreads widen, prices move against them, and the cycle repeats. Because the same funders and the same traders are active in many assets, the stress hits many assets at once, so correlations and liquidity commonality jump together.

- **Who is forced / predictable:** Levered hedge funds, prop desks and dealers facing margin calls or risk limits. Their lenders (prime brokers, repo desks) are also forced to raise haircuts when volatility rises. Their forced selling is mechanical and tends to follow volatility spikes.
- **Why it persists:** Leverage, collateral rules and VaR-based margin are structural features of financial markets. The paper argues that margins tend to rise in bad times, so the spiral is built into the system. Crises since 2009 (2020 March, repo/Treasury basis stress, Aug 2024) fit the pattern.
- **What would kill it:** Central bank backstops, fixed or counter-cyclical margin rules, or much lower leverage. Any of these would dampen the spirals. In futures, exchanges could stop raising margin when volatility spikes. The edge can also die if everyone anticipates the spiral and crowds into the same liquidity-provision trade early.
- **Paper's view vs ours:** The authors' explanation is the WHY itself. The weakness is that this is a theory paper and gives no trading rules, thresholds or estimated effect sizes. Turning it into a strategy takes our own proxies, such as realised volatility, VIX, or bid-ask spreads.

## Setting
- Markets: General, with no specific market
- Instruments: Theoretical risky securities, Applied to equities, bonds and futures in the discussion
- Period: None (theory). Illustrative episodes: 1987, 1998, 2007-08  Frequency: Not applicable  Holding: Not applicable

## Reported results
No trading backtest. The paper is a theory paper with testable predictions about liquidity co-movement, margins and the cross-section of returns.
- No Sharpe ratio, return or sample statistics are reported, because the paper is theoretical.
- Costs: Not applicable

## Tradable edge (our framing)
Treat funding stress as a regime state. When volatility spikes sharply and market depth falls, forced deleveraging pushes prices past fundamentals and spreads widen. Two uses follow. First, defensive: cut size or stand aside in index futures when volatility and depth deteriorate, because moves are nonlinear and continuation is likely while the spiral is running. This is volatility targeting with a liquidity add-on. Second, opportunistic: after the stress peaks (volatility has peaked and starts to fall, intraday range or depth recovers), take long reversion trades in ES/NQ, since the liquidity providers who were forced out are coming back and the price overshoot unwinds. Both are regime filters or overlays on other strategies, not a standalone signal. Costs matter, and holding periods should be hours to days.

## Angles to test
- Use ES 1-min data to build a liquidity-stress proxy: realised volatility, range per unit of volume, and volume spikes. Condition existing intraday momentum and reversion tests on that proxy.
- Test fade-the-panic: after a large one-day or intraday drop with volume at 3x normal and the stress proxy at a high percentile, go long ES for hours to days. Compare against the always-long baseline.
- Use the stress proxy as a vol-targeting overlay to reduce size on days when volatility is rising faster than a threshold, to avoid the margin spiral. Compare drawdown with and without it.
- Check pre/post 2022 and by volatility regime, as the playbook requires for intraday momentum.
- Compare ES with NQ (NQ only from 2021-07). Do NQ stress episodes lead or lag ES?
- Long-side only, since forced selling produces the overshoots that reverse upward. Short squeezes are less reliable.
- Combine with scheduled-event findings: quad-witching, month-end and the VIX expiry are times when margin and deleveraging flows are concentrated.

## Decay risk: medium
The mechanism is structural and has been widely known since 2009. It is cited in thousands of papers. Central bank backstops and the faster response of vol-targeting funds change the timing. As a regime filter it is likely to persist. Crisis events are rare, so a direct trading edge has few observations and is hard to validate.

## Data fit
Only partly testable. ES 1-min bars (2013-2026) and NQ 1-min bars (2021-2026) let us build volatility, range and volume proxies for stress, and we can test the overlay and the post-stress reversion on index futures. We lack funding data (repo spreads, TED/FRA-OIS, VIX, margin rates), bid/ask depth for the earlier years (ticks cover only ES 2021-06 to 2023-06 and NQ 2021 onward), and cross-asset data (bonds, credit, CL, GC). We also have few stress episodes: March 2020, Feb 2018, Aug 2015, plus 2022. The sample has too few independent events for strong significance.

## Caveats
- I could not open the paper. Fetching failed (domain not allowed), so this summary comes from memory of the paper and its abstract. Details and numbers could be wrong.
- The paper is a theory paper with no strategy rules, backtest or estimated effect sizes.
- Any tradable rule is our own construct on proxies, so it needs full in-sample/out-of-sample validation.
- Stress episodes are rare. Results may rest on just a few events (2015, 2018, 2020, 2022).

## Cited papers worth reading
- Liquidity Risk and Expected Stock Returns (2003)
- Liquidity and Market Crashes / Leverage Cycle and the Economy (Geanakoplos) (2002)
- Betting Against Beta (2014)
- Volatility-Managed Portfolios (2017)
