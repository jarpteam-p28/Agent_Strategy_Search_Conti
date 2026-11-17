# The Limits of Arbitrage

**Authors:** Andrei Shleifer, Robert W. Vishny  
**Year:** 1997  **Type:** academic  **Read:** full_pdf  
**Source:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=8043

> Arbitrageurs who run other people's money get capital pulled after losses, so they cut positions exactly when mispricing is widest. Prices can therefore overshoot in extreme conditions, and volatile anomalies persist because betting against them is risky.

## Findings
- Real arbitrage needs capital and carries interim risk. Even a near-riskless trade can move against you before it converges, and the arbitrageur must post more margin. — *Bund futures example, LIFFE vs DTB: DM6,500 of capital needed, and a further DM5,000 margin call if the gap widens.*
- When investors judge arbitrageurs on past returns (performance-based arbitrage), funds under management fall after losses, which is when expected returns are highest. Arbitrageurs get most constrained at the best opportunities. — *Three-period model with a funds-flow function F2 = F1 − aD1(1 − p2/p1). Calibrated example: V=1, F1=0.2, a=1.2, S1=0.3, S2=0.4.*
- In extreme circumstances (fully invested arbitrageurs, mispricing deepens), arbitrageurs liquidate. Prices fall more than one-for-one with the noise shock (dp2/dS < −1), so the market loses resilience, and more so as fund-flow sensitivity rises. — *Propositions 3 and 4. Numerical example: price 0.9 → 0.7636 with forced selling, versus the 0.6 floor that would apply with no arbitrage at all.*
- Specialized, undiversified arbitrageurs care about total (idiosyncratic) risk. They avoid volatile, long-horizon mispricings, so those anomalies persist, e.g. glamour stocks stay overpriced and carry low returns despite high variance. — *Qualitative argument. The value strategy beat the S&P 500 only about 60% of the time over a 1-year horizon, with much better odds over 5 years. Bank stocks in 1990–91 were an anecdote: value funds were forced to liquidate and missed the later recovery.*
- Young funds with short track records are more sensitive to past returns than established funds. Established funds therefore earn more in the long run because they have capital available at the extremes. — *Theoretical implication, not tested.*
- Anomalies that last are noisy, hard to hedge and long-horizon. Clean, short-horizon anomalies (e.g. the January effect) get accepted and arbitraged faster. As anomalies become widely known, the return shrinks. — *Discussion in Section IV.B.*

## The WHY
**Pattern:** Institutional constraint / mandate, plus liquidity constraints on large orders. This is a funding-liquidity version: the marginal liquidity provider is forced to sell by investor redemptions and margin calls.

Fund investors cannot observe strategies, so they judge managers by past returns. A mispricing that deepens makes the arbitrageur lose money, triggering withdrawals, margin calls and risk-limit breaches. He liquidates just as the expected return is highest, and the forced selling pushes prices further from value. This creates fire-sale dislocations that are followed by recovery once the forced selling is exhausted. It also explains why volatile, hard-to-hedge mispricings are never fully arbitraged away.

- **Who is forced / predictable:** Levered hedge funds and arbitrage funds with redeemable capital, prime-broker margin calls, and managers with short track records. Creditors can demand repayment when collateral falls. Risk managers inside the firm can force a cut, and risk-averse managers pre-emptively de-risk.
- **Why it persists:** Agency frictions between money and expertise are structural. Investors cannot cheaply evaluate complex strategies, and redemption and margin rules are built into fund structure. Idiosyncratic volatility cannot be diversified by specialists. Each crisis (1998, 2008, March 2020) shows the same forced-liquidation dynamic.
- **What would kill it:** Capital that is locked up or insensitive to past performance (long lockups, permanent capital, closed-end structures) would remove forced selling. So would investors who judge arbitrageurs against accurate peer benchmarks, or contracts that let managers raise fees or insure investors after drawdowns. Deep outside capital that enters when specialists leave would also kill it, as would widespread understanding of the anomaly.
- **Paper's view vs ours:** The paper is a theory paper with no tests. Its own mechanism is performance-based capital withdrawal in a stylised 3-period model, and it admits no robust conclusions about ex-ante efficiency. For us the usable part is the empirical implication: forced-liquidation events produce temporary, partly predictable overshoots, and volatile anomalies persist. The model is not evidence that any particular trade works. We have to supply the measurable trigger ourselves (extreme move plus stress).

## Setting
- Markets: General financial markets; examples from Bund futures, value/glamour equities, 1990-91 bank stocks
- Instruments: Conceptual: any arbitrage or convergence trade (bonds, FX, equities, futures spreads)
- Period: No empirical sample; theoretical model with anecdotes through 1996  Frequency: n/a  Holding: n/a (three-period model; discussion of 1-year vs 5-year horizons)

## Reported results
Theoretical only, no trading performance reported.
- Numerical example: with a=1.2 and full investment, price at t=1 is 0.9 and falls to 0.7636 if sentiment worsens, with fund size shrinking from 0.2 to 0.1636.
- Value/glamour arbitrage outperformed the S&P 500 only about 60% of the time over 1 year.
- Costs: n/a

## Tradable edge (our framing)
This is a framing paper, not a ready signal. After sharp, fast, one-directional moves that coincide with market stress (volatility spike, liquidity vacuum, deleveraging), forced selling by capital-constrained players can push futures well past fair value. Once the forced flow is exhausted, price tends to snap back. The idea is to fade extreme index-futures dislocations on a time exit, with small volatility-targeted size, and to stand aside or follow the trend in the early, still-accelerating phase of a liquidation. The dislocation itself must be measured (e.g. multiple of ATR, multi-day drop, VIX or realized-vol spike). Entry should be a reversal trigger (the event, not the state) rather than a catch of the falling knife. Reversion-first versus continuation-first must be settled in-sample.

## Angles to test
- ES/NQ: after an extreme down move of several ATRs on a spike in realized vol, go long for a 1-5 day time exit; test the long side only, since forced selling tends to be downside and buyers absorb it.
- Separate the phases: first-day continuation (liquidation still running) versus later reversion; add a lockout so only the first signal in a cluster is taken.
- Intraday: flush days in the final hour or at the open, where margin-driven liquidations are concentrated, tested on 1-min ES/NQ data.
- Expiry and quarter-end windows when funding is tight, to see if dislocations are larger.
- Conditioning variable: realized-vol percentile or drawdown depth, as a proxy for the paper's 'extreme circumstances'. Test pre/post 2022 and with volatility regimes, as in the playbook method notes.
- Pair with volatility-managed sizing: arbitrage risk scales with volatility, so cut size when vol is high and use fixed risk dollars.
- Other universes (not in our data): closed-end fund discounts, high-idiosyncratic-vol overpriced stocks, convertible bonds.

## Decay risk: low
This is not an anomaly with one published rule. It is a structural mechanism (agency-based funding fragility), 1997 theory that crises have repeatedly confirmed. The risk is that the framework yields no specific rules and any concrete implementation is a weak, noisy signal. A concrete dislocation-fade will also decay as more capital chases it, and recent high-frequency liquidity provision may shrink windows.

## Data fit
Partial. ES 1-min from 2013 and NQ from mid-2021 cover several stress episodes (Dec 2018, Feb 2018 volatility spike, Mar 2020, 2022, Apr 2025) so we can test extreme-move reversion on index futures. Missing: VIX and other vol or funding-stress indicators (we only have realized vol from our bars), NQ before mid-2021, other futures (CL, GC, YM, RTY), single stocks and closed-end fund data. A 2013+ ES sample contains few true crisis events, so statistics will be thin and outlier-dependent. Treat the result as a handful of episodes, not 100+ independent trades."

## Caveats
- The paper is pure theory: no data, no backtest, no trading rule, and no numbers on returns.
- The model is stylised: 3 periods, exogenous noise shocks, and prices that either revert fully or get worse. The authors admit no robust prediction about ex-ante efficiency or about how intensity of fund-flow sensitivity affects volatility.
- The ideas are broad, so turning them into a rule involves our own choices that may not reflect the mechanism.
- Catching dislocations is dangerous because the model itself says they can deepen. Drawdowns can be large and the signal is rare.
- The authors themselves note that well-understood anomalies should fade as more investors learn about them.
- Evidence cited is anecdotal (banks 1990-91, Orange County).

## Cited papers worth reading
- Noise Trader Risk in Financial Markets (1990)
- Contrarian Investment, Extrapolation, and Risk (1994)
- Costly Arbitrage: Evidence from Closed-End Funds (1996)
- Aggregate Mutual Fund Flows and Security Returns (1995)
- Liquidation Values and Debt Capacity: A Market Equilibrium Approach (1992)
