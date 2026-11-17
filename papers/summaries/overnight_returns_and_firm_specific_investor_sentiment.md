# Overnight Returns and Firm-Specific Investor Sentiment

**Authors:** David Aboody, Omri Even-Tov, Reuven Lehavy, Brett Trueman  
**Year:** 2018  **Type:** academic  **Read:** full_pdf  
**Source:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2554010

> A US stock's close-to-open return keeps going the same way for the next 1-4 weeks (overnight returns persist), but stocks with the highest overnight returns underperform over the next 12 months; the authors read this as retail sentiment, strongest in small, hard-to-value, low-institutional-ownership names.

## Findings
- Overnight (close-to-open) returns persist in the short run. Stocks ranked by a week's average overnight return keep the same ordering in overnight returns over the following 4 weeks. — *CRSP, all stocks with price >$5 and market cap >$10M, Jul 1992-Dec 2013, more than 1,000 weeks. Week w+1 overnight return: -0.90% in the lowest decile, +0.86% in the highest. Spread 1.76 pp (t=46). Spreads for w+2, w+3, w+4: 1.48, 1.33, 1.21 pp. Monotonic across deciles. Gross, equal-weighted, no costs.*
- Ordinary close-to-close returns show much weaker persistence, so the effect sits in the overnight leg. Extreme overnight returns are partly reversed during the day (intraday reversal). — *Close-to-close spread for w+1..w+4: 0.26%, 0.11%, 0.15%, 0.06%. Only w+1 and w+3 are significant, and the pattern is not monotonic. In 8 of 10 deciles the overnight return has the same sign as, and a larger magnitude than, the weekly total return (Table 1).*
- Persistence is not explained by bid-ask bounce, beta, size, book-to-market or momentum. — *The result holds with quote-midpoint overnight returns (untabulated). Within each decile of beta, size, B/M and momentum, the w+1 spread stays significant: 1.29-1.90 pp across beta deciles, 0.98-2.50 pp across size deciles, 1.34-1.80 pp across B/M deciles, 1.27-1.87 pp across momentum deciles.*
- Persistence is stronger for harder-to-value and less institutionally held firms. — *w+1 spread, top vs bottom quartile: volatility 1.99 vs 1.04 pp; size (smallest vs largest) 2.32 vs 0.72 pp; age (youngest vs oldest) 1.94 vs 1.25 pp; profitability (least vs most profitable) 2.13 vs 1.30 pp; E/P 1.93 vs 0.82 pp. By institutional ownership: 2.36 pp (lowest quartile) vs 1.07 pp (highest quartile).*
- Long-run reversal: stocks with high December average overnight returns underperform stocks with low ones over the next 12 months. This is a once-a-year (December) formation, equal-weighted. — *Long decile 1, short decile 10, Dec 1992-Dec 2012. Four-factor alpha 0.62%/month (about 7.4%/yr, t=3.54). Decile 1 alpha +0.40%/month; decile 10 alpha -0.23%/month (not significant). The long-short loads negatively on market, SMB and WML, and positively on HML. Alpha is significant in all hard-to-value subsamples (4.4%/yr for the smallest firms to 9.7%/yr for the highest-growth firms) and in only one easy-to-value subsample (the most profitable firms, 5.3%).*
- Firms with high pre-announcement overnight returns react less positively to earnings news (price already embeds optimism). — *Regression on top/bottom two deciles of overnight return over days -20 to -2. The SENT x AF coefficient is -0.082 (t=-2.93). The 3-day abnormal return rises with earnings E (0.32, t=7.5) and falls with the analyst forecast AF (-0.19).*

## The WHY
**Pattern:** Retail attention and order-flow (sentiment) demand that hits at the open, combined with slow information diffusion/limits to arbitrage. It also overlaps with the playbook's 'information arrives while the market is closed, digested slowly at the open' and 'overnight risk/liquidity premium' patterns, but here the driver is retail behaviour, not news.

Retail investors tend to place orders outside market hours. These are executed at the next open. Attention-grabbing events (big moves, strong retail net buying) raise retail demand, which is concentrated at the open and creates temporary price pressure, so the overnight return is inflated. Retail order imbalances persist for weeks (Barber et al. 2009), so the open-price pressure repeats and overnight returns persist. Part of the pressure is reversed intraday. Over months the sentiment-driven overpricing mean-reverts, which gives the long-run underperformance. Both effects are stronger where valuation is hard and arbitrage is costly (small, young, volatile, low-institutional names).

- **Who is forced / predictable:** Retail investors who place orders while the market is closed and buy at the open. Institutions and market makers absorb the flow, but arbitrage capital is limited and short-selling is costly in small, hard-to-value names. Also anyone buying at the open pays a hidden cost.
- **Why it persists:** Retail behaviour (after-hours order placement, attention-driven buying) is structural. The limit to arbitrage in small illiquid names is a real cost, and the stocks where the effect is strongest are the ones where trading it is hardest and most expensive. This is why the anomaly can survive in the data while still being hard to harvest.
- **What would kill it:** Retail orders being spread through the session or routed away from the open (e.g. extended-hours retail trading, zero-commission fractional execution at random times). Opening auctions or market makers pricing the retail imbalance in. Retail trading mostly migrating to options. Heavier institutional/arbitrage participation in small caps. Also, note the authors' own sentiment reading is untested directly: overnight persistence could reflect other things (news flow, attention clustering, overnight risk premia) that are not retail.
- **Paper's view vs ours:** The authors only argue that the pattern is consistent with sentiment, and treat overnight return as a measure of it. They do not observe retail orders, run no trading strategy, report no costs and no post-2013 data. Our view: the retail-order-at-the-open story is plausible and supported by Berkman et al. (2012), but the paper itself does not prove it. We should treat it as a plausible WHY that still needs testing, especially after 2013 when 0DTE, commission-free retail and extended hours changed the picture.

## Setting
- Markets: US equities (CRSP universe)
- Instruments: US common stocks (price >$5, market cap >$10M)
- Period: Jul 1992 - Dec 2013  Frequency: Daily (CRSP open and close prices), aggregated to weekly and monthly  Holding: Persistence measured over 1-4 weeks; long-run portfolio held 12 months

## Reported results
Top-minus-bottom decile of weekly overnight return gives +1.76 pp in next week's overnight return (t=46), decaying to 1.21 pp by week 4; a December-ranked long-short earns 7.4%/yr four-factor alpha over the next 12 months (t=3.54).
- Next-week overnight spread 1.76 pp; weeks 2-4: 1.48, 1.33, 1.21 pp
- Close-to-close spread next week 0.26 pp (t=4.1); weeks 2-4 smaller and mostly insignificant
- Lowest institutional ownership quartile 2.36 pp vs highest 1.07 pp; smallest size quartile 2.32 pp vs largest 0.72 pp
- Long-run long-short alpha 0.62%/month (7.4%/yr), t=3.54; range 4.4%-9.7%/yr in hard-to-value subsamples
- Earnings reaction interaction coefficient SENT x AF = -0.082 (t=-2.93)
- Costs: None. Gross equal-weighted portfolio returns; no spreads, commissions, borrow costs or capacity analysis.

## Tradable edge (our framing)
Retail demand placed while the market is closed pushes individual stocks' opening prices away from the prior close, and that pressure persists for weeks in the same direction (and partly reverses intraday), then the overpricing unwinds over months. Our framing is a cross-sectional single-stock tilt: rank small/mid, hard-to-value, low-institutional-ownership stocks by recent average close-to-open return. In the short horizon, hold the overnight leg (buy close / sell open) of last week's high-overnight names, and avoid or fade it intraday; in the long horizon, underweight recent extreme-high overnight names and favour extreme-low ones. The index-level version (NQ/ES overnight vs intraday) is a different, weaker use of the same idea: this paper provides no index-level evidence.

## Angles to test
- Overnight leg only: long names with last-week's highest average overnight return, hold close-to-open each day for 1-4 weeks; compare to the always-long-overnight baseline and size by volatility. Test where the effect is strongest (small, young, volatile, low institutional ownership) and after costs, since the 1.76pp weekly gross spread is likely mostly eaten by spreads and open-auction impact in microcaps.
- Intraday leg: for the top overnight-return decile, test a short/fade from open to close (intraday reversal) vs the paper's finding that overnight returns are larger than total returns.
- Long-horizon version: long lowest / short highest decile of average overnight return (monthly, rolled, not just December), restricted to hard-to-value names; check borrow cost and shorting limits; long leg only is likely more tradable.
- Index-futures adaptation: ES/NQ overnight return of the prior N days as a persistence signal for the next overnight session, in the Conti 'trade the overnight session' spirit. Weak support: the paper is cross-sectional single-stock, so this is a hypothesis, not a replication. Test pre/post 2022 and conditional on retail attention (volatility, big down/up days).
- Combine with PEAD: skip or underweight names with high pre-earnings overnight returns (the paper finds a smaller earnings reaction, i.e. optimism is already priced); use overnight sentiment as an extra filter on earnings-drift longs.
- Other markets: Europe/Asia small caps with retail-heavy ownership; crypto or single-stock futures with distinct overnight/intraday sessions.

## Decay risk: high
Published 2018 on 1992-2013 data and builds on Berkman et al. (2012) and Lehmann-style weekly reversals/persistence. The overnight/intraday split is widely known, and retail trading changed a lot after 2013 (commission-free apps, extended-hours trading, options). The strongest effects sit in small, illiquid, costly-to-short stocks where gross spreads are likely eaten by costs. McLean-Pontiff suggests roughly half of the published edge survives, less after costs. No out-of-sample or post-2013 evidence is given.

## Data fit
Poor for the paper's actual test. It needs a single-stock cross-section (CRSP open/close prices, institutional ownership, size, age, profitability), none of which we have. Our NinjaTrader inventory holds only ES (2013-2026) and NQ (2021-2026) futures and no single stocks. We can run only an index-futures analog: ES/NQ overnight (ETH close to RTH open) return persistence over the next days, and the intraday reversal after extreme overnight moves, which is not what the paper tests. Missing: single stocks, ownership data, small-cap universe, NQ before 2021.

## Caveats
- All results are gross, equal-weighted decile spreads from CRSP open and close prices. No transaction costs, spreads, shorting costs or capacity are considered, and microcaps (price >$5, cap >$10M) dominate the extremes.
- Overnight returns computed from CRSP open prices can include opening-auction noise and bid-ask bounce; the quote-midpoint check is untabulated.
- The sentiment interpretation is indirect: no retail order data is used. The persistence could partly reflect other overnight drivers (news, attention clustering).
- The long-run result uses only December formation (one portfolio a year, about 20 observations) with overlapping 12-month holds; the t-statistic of 3.54 comes from monthly returns of overlapping portfolios. The short leg (decile 10) alpha is not significant on its own.
- Sample ends in 2013. There is no check on whether it still works in the retail/0DTE era.
- Earnings-announcement test is a regression, not a strategy, and the SENT dummy uses only the extreme two deciles.
- Persistence in weekly overnight return is strong but close-to-close persistence is small, so a long-only buy-and-hold of the same stocks captures little. The edge exists only if you can capture the overnight leg specifically, which means daily turnover.

## Cited papers worth reading
- Paying Attention: Overnight Returns and the Hidden Cost of Buying at the Open (2012)
- Do Retail Trades Move Markets? (2009)
- Return Differences between Trading and Non-Trading Hours: Like Night and Day (2008)
- Overnight Return, the Invisible Hand behind Intraday Returns (2012)
- Investor Sentiment and the Cross-Section of Stock Returns (2006)
