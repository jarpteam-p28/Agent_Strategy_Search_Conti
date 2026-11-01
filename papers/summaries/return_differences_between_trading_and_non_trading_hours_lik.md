# Return Differences between Trading and Non-Trading Hours: Like Night and Day

**Authors:** Michael Cliff, Michael J. Cooper, Huseyin Gulen  
**Year:** 2008  **Type:** academic  **Read:** full_pdf  
**Source:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1004081

> From 1993 to 2006 essentially all of the US equity premium was earned overnight (close to open), while open-to-close returns were zero or negative, with much of the daytime weakness coming in the first hour after the open.

## Findings
- Night (close-to-open) returns are positive and day (open-to-close) returns are about zero or negative for S&P 500 stocks, 1993-2006. — *Night 2.8 to 4.8 bp per night (t 3.9-17.8). Day -2.85 to +0.22 bp. Night minus day spread 2.6 to 7.6 bp. Pooled trade-price spread 5.25 bp (t 3.48). Sample: 843 stocks, TAQ data.*
- For SPY, $1 compounded in night returns only grows to $6.54 over 1993-2006. $1 compounded in day returns only falls to $0.61 (no transaction costs). — *Figure 1, SPY, Feb 1993 to Dec 2006.*
- The effect appears across asset types and venues: Internet stocks (night +17 bp, day -14 bp), 14 ETFs (spread 8.5 bp, t 3.8), and E-mini S&P futures (night +4.79 bp, day -4.53 bp, spread 9.3 bp, t 2.98, 1997-2004). — *Table 1 Panels B-D. Night return is above day return for all 14 ETFs, and the spread is significant in 8 of them.*
- Night is less volatile than day, so risk does not explain the premium. — *SD of night returns is 124 bp vs 203 bp for day (S&P 500 stocks). For E-minis, 54 bp vs 116 bp.*
- Most of the negative day return comes from the first hour after the open (AM, 9:30-10:30). Mid-day is about zero, and the last hour is slightly positive for S&P 500 stocks. — *S&P 500 stocks AM -1.2 to -3.6 bp (t up to -13). SPY AM -1.89 bp (t -2.64). E-minis AM (8:30-9:30) -2.84 bp (t -3.81).*
- The effect is not a calendar artifact. It holds on every weekday, on days outside the turn of the month, in 11 of 12 months, and in 12 of 14 years for SPY (spread positive). The weekend (Friday close to Monday open) return is positive, the reverse of the classic weekend effect. — *Tables 2-5. SPY weekend return +8.9 bp (t 3.62). SPY spread outside turn-of-month 7.08 bp (t 2.78). Strongest in 1997-2000 (8.5 bp), but 3.9 bp (t 3.19) in other years.*
- Earnings news timing, ECNs, decimalization, and liquidity or size do not explain the effect. The spread is stable pre- and post-1998 and weaker (not significantly) after 2001 for SPY. It persists excluding earnings days. It is not concentrated in illiquid stocks. It is larger for high-volatility stocks. — *Table 6: spread 4.40 bp on all days vs 4.44 bp excluding earnings days. Table 7: spread 17.4 bp for the high-SD quintile vs -0.7 bp for the low-SD quintile.*
- There is a reversal pattern. A high night return predicts a lower next-morning (AM) return. Intraday returns are negatively related to the next night's spread. — *Table 8: AM return on lagged night return t = -54.6. Night-minus-day spread on lagged night return t = 17.6. R-squared only about 8-10%.*

## The WHY
**Pattern:** {"pattern":"Information arrives while the market is closed, and is digested slowly once it opens, combined with a risk/liquidity premium for carrying positions through the closed period. Overnight overreaction then corrects intraday.","mechanism":"The paper has no firm explanation and says so. It rules out risk, earnings timing, ECNs, decimalization and liquidity. It points to Longstaff (1995), where holders are paid for non-marketability while the market is closed, and to price pressure from algorithmic trading. The best defensible WHY: positive overnight drift pays holders for carrying risk while the market is shut and illiquid. Early buying pressure at the open pushes the opening price too high, and this reverses in the first hour. That gives positive night returns, a negative first hour, and a negative correlation between the night return and the next AM return. Part of the story is also a one-way structural bias. Passive and retail demand and institutional accumulation orders are queued to the open, and they pay up at the auction. Market makers and short-term traders then fade this into the first hour.","who_is_forced":"Participants who must or prefer to buy at the open (index and ETF creation, retail orders placed overnight, funds that can only trade in regular hours, algos that start at the open). Liquidity providers who carry inventory overnight are compensated. Reversal traders sell the high open in the first hour.","why_it_persists":"It holds across assets, exchanges and subperiods (1993-2006). Later evidence (not in this paper) suggests the overnight premium persists in index futures and ETFs. The risk-premium and order-flow-at-the-open reasons are structural and not arbitraged away, because holding overnight is risky and capital-intensive to hedge. The paper stresses that the premium is a close-to-open vs intraday split, so it needs no stock selection.","what_would_kill_it":"Pre-open and overnight liquidity becoming deep enough that opening prices fully reflect overnight information (24h trading by most institutions). Large players executing at the open stopping. Overnight risk premia being competed away by capital flowing into overnight holding strategies. The authors note a weak decline after decimalization and ECNs, and the higher opening price fading."},
"authors_explanation_vs_ours":"The authors do not give a conclusive explanation. They call the day results puzzling. They tested earnings timing, risk, liquidity and ECNs, and found each explains little. They float the Longstaff non-marketability story, but note it conflicts with their results, because the discount should appear at the close and not at the open. They speculate on algorithmic price pressure. Our WHY (overnight risk and illiquidity premium plus open-auction buying pressure that mean-reverts in the first hour) fits the first-hour reversal and the negative night-to-AM autocorrelation, but it is a hypothesis, not proven."}




## Setting
- Markets: US equities (NYSE, Nasdaq, AMEX), CME E-mini S&P 500 futures
- Instruments: S&P 500 constituent stocks (843), AMEX Internet index stocks (44), 14 ETFs including SPY, QQQ, DIA, E-mini S&P 500 futures
- Period: 1993-2006 (E-mini futures Sept 1997-Sept 2004)  Frequency: Transaction-level TAQ trades and quotes (open, 10:30, 15:00, close prices); 15-min E-mini bars  Holding: Overnight (close to open) vs intraday (open to close); intraday sub-windows AM 9:30-10:30, Mid 10:30-15:00, PM 15:00-16:00

## Reported results
For SPY 1993-2006, $1 held only overnight grew to $6.54 while $1 held only intraday shrank to $0.61. For S&P 500 stocks the night-minus-day spread was about 2.6-7.6 bp per day.
- S&P 500 stocks pooled: night 4.14 bp (t 5.81), day -1.11 bp (t -0.83), spread 5.25 bp (t 3.48)
- E-mini S&P futures 1997-2004: night +4.79 bp, day -4.53 bp, spread 9.32 bp (t 2.98)
- 14 ETFs: spread 8.47 bp (t 3.77)
- Night SD 124 bp vs day SD 203 bp (S&P 500 stocks)
- Negative returns: 39.5% of nights vs 50.5% of days (S&P 500 stocks)
- SPY spread positive in 12 of 14 years and 11 of 12 months
- First-hour (AM) return -1.2 to -3.6 bp for S&P 500 stocks
- Costs: No. The authors explicitly exclude transaction costs from the Figure 1 compounding and report none.

## Tradable edge (our framing)
Own the index (ES/NQ or the corresponding ETF) only during the close-to-open window. Enter at or near the cash close and exit at or shortly after the next open. Skip holding through the RTH session, particularly the first hour, which has been the weak part of the day. The edge is a structural split of the equity premium into a paid overnight carry and an unpaid daytime period. Two variants exist: pure overnight long, and an overnight long plus a first-hour fade that exits (or shorts) the high open, using the high negative correlation between night return and next AM return. Raise or keep size on high-volatility names or periods, where the spread was strongest. Position sizing in live trading would be volatility-targeted: dollars at risk divided by recent overnight volatility. Costs matter, as the effect is only a few bp per night, so use futures with low round-turn costs and test net of costs.

## Angles to test
- Different instrument: ES and NQ overnight-only long; test YM/RTY/CL/GC if data is added (the NQ overnight history before 2021 is missing in our inventory).
- Different session: split the globex session (Asia, Europe, pre-open) to find where the overnight return is earned, then use the Conti-style 'trade the overnight session' ORB or hold during the paid window only.
- One side only: long-only overnight (breakdowns at night are absorbed). Test whether the daytime short, especially first-hour (09:30-10:30) short or fade, adds anything on top.
- Combine: overnight long plus first-hour fade (night return is negatively related to the next AM return). Use a large overnight gap up as a stronger fade signal, and a large gap down as a long signal.
- Volatility conditioning: the effect grows with stock-level volatility (high-SD quintile spread 17 bp vs ~0). Scale size by volatility regime (e.g. VIX or ATR) or test high-beta instruments such as NQ.
- Day-of-week and weekend: the Friday-close to Monday-open return is positive in this sample. Test the weekend hold separately on ES for the 2013-2026 period.
- Prop-firm and portfolio use: overnight bias is low-frequency with a higher reward/risk profile, suited to the funded phase and uncorrelated with intraday VWAP-pullback strategies.

## Decay risk: medium
Published in 2008 (SSRN), and widely known since, with many follow-up papers and retail strategies on 'overnight drift'. The effect was stronger in 1997-2000 and weaker after 2001 (SPY spread 6.5 bp before vs 3.6 bp after, not significant). Overnight returns in index futures stayed positive for years afterwards, and the risk-premium explanation is structural, so it has not obviously vanished. Still, the edge is only a few bp per night, so costs and decay can erase it. The paper itself has no costs.

## Data fit
Good for the ES test: ES 1-min data (ETH and RTH, Dec 2013 to 2026) lets us compute close-to-open (RTH close 16:00 ET to next 09:30 ET open, or 16:15 globex) versus open-to-close returns, plus the first-hour (09:30-10:30) return, the weekday split, and the night-to-AM reversal. Out-of-sample use is natural: the paper's sample ends 2006, so all our data is post-publication. NQ 1-min is only available from mid-2021 (NQ before 2021 is missing, as the inventory notes). No data for single stocks, other futures (YM, RTY, CL, GC), or earnings dates, so we cannot replicate the stock-level cross-section (high-volatility stocks, Internet stocks). We can use ES ETH bars to proxy volatility regimes. Time zone is UTC in the files, so careful ET conversion with DST is needed. Futures rollover gaps must be handled when computing overnight returns (use continuous back-adjusted series or exclude roll days).

## Caveats
- Sample ends 2006 and includes the Internet bubble years (1997-2000), where the effect was strongest. Everything we test will be out of sample.
- No transaction costs. Effects are 3-10 bp per night, small against slippage and fees except in liquid futures.
- The cash-session close and open are used for stocks. For E-minis the authors used 8:30 CT open (full-size pit open), which is a different definition from the RTH 09:30 ET open. Results depend on the open and close definitions.
- The futures sample is short (Sept 1997 to Sept 2004), and the E-mini day return is not significant (t -1.6) on its own.
- Opening price uses the first trade after 9:30, which can be noisy. Part of the 'negative first hour' could reflect opening-print bias and bid-ask effects. Mid-quote results are weaker: S&P 500 pooled spread 2.61 bp, t 1.74.
- The authors do not establish a causal explanation. The Longstaff model implies the opposite timing of the discount.
- Effect is not significant every year or month (September negative for SPY, 2001-2002 negative night returns).
- Authors suggest the effect is a puzzle, not a ready strategy. No portfolio results, drawdowns, or Sharpe ratios are reported.

## Cited papers worth reading
- How Much Can Marketability Affect Security Values? (1995)
- Equity Returns at the Turn of the Month (2008)
- A Transaction Day Study of Weekly and Intradaily Patterns in Stock Returns (1986)
- Price Discovery and Trading After Hours (2003)
- Stock Market Structure and Volatility (1990)
