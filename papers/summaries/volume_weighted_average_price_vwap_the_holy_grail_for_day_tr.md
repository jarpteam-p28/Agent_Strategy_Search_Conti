# Volume Weighted Average Price (VWAP) The Holy Grail for Day Trading Systems

**Authors:** Carlo Zarattini, Andrew Aziz  
**Year:** 2023  **Type:** industry  **Read:** full_pdf  
**Source:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4631351

> On QQQ, 2018-2023, the intraday trend continued in the direction of price versus session VWAP, so a long-above/short-below-VWAP day-trading system flipping on 1-minute closes beat buy-and-hold on paper, but about 22,000 trades with a 17% hit rate and no slippage make the result highly cost-sensitive.

## Findings
- Price location versus RTH-only VWAP predicts the direction of the next 1-minute moves. When the prior 1-minute close was above VWAP, QQQ repriced about +$320 per share (2018-2023, RTH only). When it was below VWAP, it repriced about -$280. — *Fig. 2. QQQ rose about $202 in total, with about $98 in RTH and about $104 outside RTH. About 56% of 1-minute closes were above VWAP. Sample: QQQ 1-minute data, 2 Jan 2018 to 28 Sep 2023 (IQFeed/IB).*
- Trading that signal (long above VWAP, short below, always in the market during RTH, flat overnight) beat buy-and-hold on QQQ. Beta to QQQ was about zero, so the paper reports it was not just market exposure. — *Starting from $25k, QQQ version ended at $192,656 (+671%, 43%/yr, vol 18%, Sharpe 2.1, MDD 9.4%). Buy-and-hold QQQ: +126%, Sharpe 0.7, MDD about 36%. Annualized alpha 38% (t>5), beta about 0. Costs: $0.0005/share, no slippage.*
- The same rules on TQQQ (3x) gave 8,242% total return (116%/yr), 54% vol, Sharpe 1.7 and MDD 36.1%. Commissions were large at about $400k. — *Table 2/3. Alpha 93% (t>4), beta about 0. Worst day -22.7%, worst trade -4.1%.*
- It is a classic low-hit-rate trend profile. About 22,000 trades (roughly 15 per day) with a 17% hit ratio and a gain:loss ratio of about 5.5-5.7. The average gross profit is only about $0.027 per share per trade ($600 total per share traded over about 22k trades). — *Tables 3-4 and Fig. 7. The per-trade figure is our arithmetic from the paper's numbers. The authors flag that higher commission rates hurt the strategy.*
- VWAP beat simple moving-average versions of the same trend system. SMA9 made 202% with about 107k trades and 41% MDD. SMA20 made 49%. SMA100 made 83%. SMA200 made 135%. VWAP made 671% with 9% MDD. — *Table 5. Fast MAs churn commissions. Slow MAs are polluted by pre-market prices and react slowly to reversals.*
- The profit is concentrated by time of day: 9:30-12:00 and the last hour (15:00-16:00). Midday (12:00-15:00) is roughly flat. — *Fig. 7, cumulative per-minute PnL of a 1-share strategy. The authors say a cheaper version could skip 12-3pm but did not test it.*

## The WHY
**Pattern:** Execution mechanics of big players (VWAP algos and benchmark-driven order splitting), combined with liquidity constraints on large orders

Institutions slice large parent orders and are judged against the day's VWAP. A desk that sees the market moving away from VWAP early has an incentive to finish the order quickly. This adds flow in the direction of the imbalance and keeps price on the same side of VWAP. A desk that waits and sees no pullback to VWAP is forced to complete late, which pushes the last hour in the same direction. The paper's time-of-day chart (morning and last hour carry the profit, midday does not) is consistent with this story. VWAP is also a visible, widely used reference level, so crossing it makes flow more predictable, as with the VWAP-crossing amplification Conti describes. The paper cites a figure that VWAP-benchmarked orders are about 50% of institutional trading.

- **Who is forced / predictable:** Execution desks and algos benchmarked to VWAP, which can't build or unwind a full position in one print. Their schedule is partly front-loaded and partly forced into the close. Retail and prop traders who watch VWAP add to the flow.
- **Why it persists:** As long as VWAP remains the standard execution benchmark and parent orders are larger than what the book can absorb in one go, the order-splitting footprint remains. This is a structural feature of how funds execute, not a behavioural quirk. It is also related to the better-documented intraday momentum effect, where early-session direction predicts later-session direction.
- **What would kill it:** (1) Execution benchmarks moving away from VWAP (arrival price/implementation shortfall, randomised or dark execution) so orders no longer leave a directional footprint. (2) So many traders trading VWAP crosses that the signal is arbitraged into chop. (3) Transaction costs: with about 15 flips a day and an edge of about 3 cents per share per trade, any real spread, slippage or higher commission can erase the result. (4) Regimes with persistent mean-reverting days and many false VWAP crosses (the authors' own worst day was -5.1% on QQQ).
- **Paper's view vs ours:** The authors give almost no causal analysis. They say the economic reasons for the time-of-day pattern are 'outside the scope' and offer two speculative order-execution stories. The rest of the paper is performance reporting. They also describe the signal as 'imbalance detection' without evidence. Their WHY is therefore weak. The execution-mechanics WHY above is the best defensible one, but it is a hypothesis the paper does not test. For example, it never shows that the effect is stronger in high-volume or high-institutional-flow days.

## Setting
- Markets: 
- Instruments: 
- Period:   Frequency:   Holding: 

## Reported results
QQQ: $25k to $192,656 (+671%, 43%/yr), Sharpe 2.1, MDD 9.4% versus buy-and-hold +126%, Sharpe 0.7, MDD about 36%. TQQQ: +8,242% (116%/yr), Sharpe 1.7, MDD 36.1%. Period 2 Jan 2018 to 28 Sep 2023.
- About 22,000 trades (about 15 per day); hit ratio 17%; gain:loss about 5.5-5.7
- Annualized alpha 38% on QQQ (t>5) and 93% on TQQQ (t>4); beta not different from zero
- Per-share profit: about $600 on a 1-share strategy versus $200 for 1 share of QQQ; roughly $0.027 per trade
- Worst day -5.1% (QQQ version) and -22.7% (TQQQ version); best day +6.5% / +20.9%
- Moving-average controls (SMA9/20/100/200) returned 202% / 49% / 83% / 135%, all below VWAP
- Commissions $6.5k (QQQ) and $400k (TQQQ) on 13M and 800M shares traded
- Costs: Commission only: $0.0005 per share. No slippage and no bid-ask spread were modelled. The authors admit higher commissions hurt the strategy and say the system is not suited to multi-million accounts.

## Tradable edge (our framing)
Price relative to the running RTH VWAP is a free, real-time read on which way big benchmark-driven orders are leaning. A systematic day trader can take the side of that lean after the opening minutes and stay with it until price closes back through VWAP or the session ends, especially in the first 2.5 hours and the last hour. The paper's version flips on every 1-minute close through VWAP, producing about 15 trades a day at a 17% hit rate and about 3 cents of gross profit per trade. That means the idea may be real, but a net-of-cost edge only exists if trades are cut with filters. The filters are a minimum distance or buffer from VWAP, a VWAP-slope and recent-speed condition, a lockout after exits, no trading 12:00-15:00, and a cap on trades per day. These are the same level/direction/speed conditions Conti used in the later VWAP pullback strategy.

## Angles to test
- Different instrument: ES 1-minute (we have 2013-12 to 2026-09) with RTH-only VWAP computed from 09:30 ET. NQ from ticks (2021-07 to 2026-09, with gaps) could be rebuilt into 1-minute bars. Futures spreads are tighter in % terms, but a one-tick cost on every flip is still heavy.
- Reduce trade count: test a buffer band (e.g. 0.05-0.1% or a fraction of the 15-session ATR) around VWAP before flipping. Also test a lockout after each exit (cluster filter, per method note 04), and a trade cap per day.
- Different session: trade only 09:30-12:00 and 15:00-16:00, per the paper's Fig. 7. Or the reverse: skip the first 60 minutes so VWAP has formed (Conti note 02). Compare to a 'long above VWAP only' version.
- One side only: the paper's own numbers show the above-VWAP side gaining $320 and below-VWAP side losing $280 in a rising market, so the long side carries a beta. Test long-only versus short-only, and the short side in down years (2022).
- Combine with other findings: add the opening-range breakout direction, the overnight gap/news (stocks-in-play) and the VWAP-slope condition. Alternatively use VWAP-side as a regime filter for the ORB or VWAP-pullback strategies already in the repo.
- Vol-target the sizing (risk-parity by ATR) instead of 100% of equity, and run daily-P&L correlation with the existing ORB and overnight strategies for the portfolio.
- Leveraged-ETF variant (TQQQ/SQQQ) cannot be tested with our data but futures with vol-target sizing are the equivalent leverage.

## Decay risk: high
Published Nov 2023 with about 45k downloads, and VWAP trend-following is among the best-known retail and institutional rules. The paper's edge is thin per trade (about 3 cents per share per trade on about 22k trades) and assumes zero slippage and no spread. The sample (2018-2023) is a single in-sample run with no out-of-sample split, no parameter robustness table, and was chosen as a QQQ-only study. Real-world costs plus crowding at the VWAP line are the most likely killers; the underlying order-splitting mechanism is more durable than the exact rules.

## Data fit
Partial to good. ES 1-minute data (RTH and ETH, 2013-12 to 2026-09, UTC timestamps) lets us compute an RTH-only VWAP and test a futures version over about 12 years, which includes a true out-of-sample period beyond the paper's 2018-2023. Convert UTC to ET (handle DST) and anchor VWAP at 09:30 ET. The paper's HLC-weighted-by-volume VWAP is easy to replicate. NQ is tick data only from mid-2021 with missing contracts, so there is no continuous 1-minute series yet and nothing before 2021. QQQ/TQQQ ETF data is not in our inventory, so the exact paper test cannot be reproduced; ES is a proxy. Costs must be modelled explicitly (commission plus at least one tick of slippage per side), because the paper used none. We cannot test the order-flow/VWAP-algo explanation directly, only its footprint in price.

## Caveats
- Zero slippage and zero spread on about 15 flips a day. At an average gross of about 3 cents per share per trade, even a 1-cent round-trip cost would remove a large part of the profit. Our estimate; the authors do not give a cost sensitivity table.
- No out-of-sample split, no parameter sensitivity and no Monte Carlo. The authors call it exploratory and 'not a fully developed trading system'. The title ('Holy Grail') overstates it.
- Stop at the close of a 1-minute bar below/above VWAP, and fills at the next open (entry at 9:31). Their exact fill assumption for stops is not fully specified. Check execution timing for look-ahead.
- Sample 2018-2023 is mostly a bull market with a 2020 crash and a 2022 bear. The effect of one or two big trend days (the best-day gain is +6.5% on QQQ) on the equity curve is not shown. A 17% hit rate means outlier dependence.
- TQQQ results are driven by 3x leverage with compounding at 100% of equity; a Sharpe of 1.7 is below the QQQ version's 2.1. The 8,242% headline is leverage, not extra edge.
- Minor inconsistencies in the paper: buy-and-hold MDD is quoted as 35.6%, 36% and 37%; buy-and-hold average yearly return is 15% in Table 1 and 17% in Table 5.
- The WHY (VWAP algos) is asserted, not tested. A simple intraday-momentum effect would give the same price pattern.

## Cited papers worth reading
- Equilibrium effects of intraday order-splitting benchmarks (2021)
- Improving VWAP strategies: A dynamic volume approach (2008)
- Can Day Trading Really Be Profitable? Evidence of sustainable long-term profits from opening range breakout (ORB) day trading strategy vs. benchmark in the US stock market (2023)
- On-line VWAP trading strategies (2010)
- Beat the Market: An Effective Intraday Momentum Strategy for S&P500 ETF (SPY) (2024)
