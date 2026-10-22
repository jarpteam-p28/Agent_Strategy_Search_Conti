# Can Day Trading Really Be Profitable? Evidence of sustainable long-term profits from opening range breakout (ORB) day trading strategy vs. benchmark in the US stock market

**Authors:** Carlo Zarattini, Andrew Aziz  
**Year:** 2023  **Type:** industry  **Read:** abstract_only  
**Source:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4416622

> A rules-based opening range breakout on QQQ, traded intraday and flat every close, beat buy-and-hold in 2016-2023 (abstract: 33% annualised alpha net of commissions), and TQQQ lifted the return to 1,484% against 169% for QQQ.

## Findings
- An opening range breakout (ORB) day-trading strategy on QQQ, 2016-2023, beat passive QQQ. The period includes two bear markets and several abnormal-volatility events. — *Abstract: annualised alpha of about 33% net of commissions versus buy-and-hold QQQ.*
- Broker leverage limits capped how much of the ORB edge a trader could capture with QQQ alone. — *Abstract. The authors say leverage constraints capped the upside.*
- Running the same strategy through TQQQ (3x leveraged QQQ) removes the leverage constraint. Because positions are flat overnight, the daily-reset decay of a leveraged ETF matters less. — *Abstract: 1,484% total return for the ORB-in-TQQQ portfolio versus 169% for QQQ, 2016-2023.*
- The strategy is described as an uncorrelated, long-term-consistent source of return, in contrast with the usual claim that day trading loses money. — *Abstract only. I could not check drawdowns, Sharpe, trade counts or yearly breakdowns.*
- From my memory of the paper, not verified here: the rule uses the first 5-minute bar. Go long if it closes up and short if it closes down. The stop is a fraction of ATR, with a risk-based position size, and the trade exits at the close. — *Not verified. The full text was inaccessible. Treat these details as unconfirmed.*

## The WHY
**Pattern:** Information arrives while the market is closed, and is digested slowly once it opens (primary). Institutional constraint / mandate is secondary.

News, earnings and global positioning build up overnight. At the open, orders collide and the imbalance is too big to absorb in the first minutes. The direction of the first bar shows which side is overwhelmed, and that flow carries through the day because it is absorbed slowly and large orders get worked over hours. Intraday momentum from the open to the close is the observable result.

- **Who is forced / predictable:** Funds and pension mandates that can only trade in regular hours. Index and ETF arbitrageurs and market makers, who hedge or rebalance into the move. Leveraged-ETF rebalancing flows into the close add to momentum on big days.
- **Why it persists:** The overnight information gap and the regular-hours mandates are structural. Intraday momentum also appears to be strongest on high-volatility days, and those days will keep occurring.
- **What would kill it:** Pre-market and 24-hour trading becoming the norm for large funds, so overnight information gets digested before the open. A flood of ORB capital that front-runs the first bar. Lower volatility regimes. The authors' explanation is mostly empirical, so a mechanism like the one above is my own framing. The paper's own WHY is weak as far as the abstract shows.
- **Paper's view vs ours:** The abstract gives no mechanism. It argues from the performance numbers and the benchmark comparison. Our WHY is the overnight-information and flow-imbalance story. We would also reject the 3x leverage figure as evidence of edge, because it comes from scaling a sample that includes the 2020-2021 bull run.

## Setting
- Markets: US equities (Nasdaq-100 ETF)
- Instruments: QQQ, TQQQ
- Period: 2016-2023  Frequency: Intraday (my recollection is 5-minute bars, unverified)  Holding: Intraday, flat by the close

## Reported results
ORB portfolio in TQQQ returned 1,484% over 2016-2023 versus 169% for passive QQQ. The QQQ ORB portfolio earned 33% annualised alpha net of commissions.
- Annualised alpha of 33%, net of commissions (QQQ ORB)
- 1,484% total return (TQQQ ORB) versus 169% (QQQ buy and hold), 2016-2023
- Sample covers two bear markets
- Costs: Commissions are included in the alpha figure according to the abstract. Slippage assumptions are unknown.

## Tradable edge (our framing)
Use the first minutes of the cash session as an information signal. After the overnight news pile-up, the direction of the opening range shows which side's flow could not be absorbed. Trade that direction with a stop beyond the range and a hard time exit at the close, so there is no overnight risk. Size by volatility (the range or ATR), not by a fixed number of shares. Develop on unlevered fixed size, then add leverage only at the sizing layer. Test long-only against long-short, because dips get absorbed by buyers in equity indices. The abstract's headline return is a leverage story, so judge the edge on risk-adjusted returns and on the per-trade expectancy before leverage.

## Angles to test
- Different instrument: run the same rules on ES (2014-2026) and NQ (2021-2026) instead of QQQ. Compare with the paper's QQQ result as a sanity check.
- Different session: an ORB on the overnight (Globex) session, or the Asian/European opens in ES, using the same 'information pile-up then open' logic.
- One side only: long-only ORB against long-short, and a down-year check (2022) to separate the edge from market beta.
- Volatility-managed sizing: risk a fixed dollar amount divided by range or ATR, and compare with fixed 1-contract size. This is the Conti live-sizing approach.
- Opening-range length sweep (1, 5, 15, 30 minutes) in-sample, with a cluster/time filter and one trade per day.
- Combine with a VWAP trend filter or a gamma-level cross as a second strategy, and check that daily P&L correlation is under 0.25 for prop-firm portfolio use.
- Regime filter: trade only when the overnight gap or the prior-day range is large, to target the high-information days.

## Decay risk: medium
The paper was posted in April 2023 and is very widely downloaded (about 51k downloads). ORB is among the best-known intraday strategies, and the QQQ and TQQQ version is easy for retail to copy. The sample includes the 2020-2021 high-volatility, bull-market regime. The WHY is structural, but returns after 2023 are untested and the edge is probably thinner. A fixed 5-minute rule is crowded, so the WHY is better exploited in futures with volatility-scaled levels.

## Data fit
Partial. ES 1-minute bars (ETH and RTH, 2013-12 to 2026) and NQ 1-minute bars (2021-07 to 2026) cover the opening-range logic well. QQQ and TQQQ are not in the inventory. ES or NQ futures are the natural proxies for the QQQ signal, and 5 minutes can be built from the 1-minute bars. The TQQQ leverage test cannot be replicated directly, but it can be approximated by scaling NQ position size. NQ data before mid-2021 is missing, so 2016-2021 cannot be tested on NQ. ES covers 2014-2026 and includes the paper's period. We don't have the paper's exact rules, so we would build ours from the WHY.

## Caveats
- I read only the SSRN abstract page. The PDF could not be fetched, so I have not seen the rules, statistics, drawdowns, trade counts, cost assumptions or robustness checks.
- The rule details in the findings come from memory and are marked unverified.
- Leveraged returns of 1,484% versus 169% are not comparable: one side is levered and the other is not. They also depend heavily on the 2016-2023 sample.
- Testing a single ticker (QQQ) over about 7 years has a data-mining risk, and the authors say it was chosen 'without loss of generality'.
- The 'alpha' is measured against QQQ. Because the strategy is intraday, it's more meaningful to look at the risk-adjusted return and at correlation with the market.
- TQQQ liquidity and slippage at the open are not the same as in futures.

## Cited papers worth reading
- A Profitable Day Trading Strategy For The U.S. Equity Market (2024)
- Market Intraday Momentum (2018)
- Volatility-Managed Portfolios (2017)
- The Impact of Volatility Targeting (2018)
