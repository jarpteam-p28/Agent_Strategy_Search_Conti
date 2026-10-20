# Reading list — papers to download

Updated 2026-10-20. Download each PDF and save it in `papers/inbox/` **using the file name shown** (or attach it in chat). The next run reads the full paper and replaces the partial summary.

## 1. Couldn't get the full text — please download

| Paper | Why it matters | Where to get it | Save as |
|---|---|---|---|
| Market Intraday Momentum (2018) — *partial* | transcript 01 - opening range breakout (open preprint may exist on author pages) | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2440866 | `market_intraday_momentum.pdf` |
| Volume Weighted Average Price (VWAP): The Holy Grail for Day Trading Systems (2023) — *abstract only* | transcript 01 - VWAP trend | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4631351 | `volume_weighted_average_price_vwap_the_holy_grail_for_day_tr.pdf` |

## 2. Recommended research — ES / NQ / index futures

### P1 · Beat the Market: An Effective Intraday Momentum Strategy for S&P500 ETF (SPY) (2024)
*Carlo Zarattini, Andrea Barbon, Andrew Aziz* · instruments: SPY, ES · access: open_pdf · testable on our data: yes

- **Why:** Intraday momentum on SPY: trade breakouts of a 'noise area' built from past intraday moves, trail with VWAP. WHY ties to dealer gamma hedging (same mechanism as Baltussen et al.).
- **Should contain:** Noise-band definition, entry every 30 min, VWAP trailing stop, vol-targeted sizing, 2007-2024 results
- **Get it:** Free PDF on the University of St. Gallen repository (alexandria.unisg.ch) or via SSRN / SFI https://ideas.repec.org/p/chf/rpseri/rp2497.html
- **Save as:** `papers/inbox/beat_the_market_an_effective_intraday_momentum_strategy_for.pdf`

### P1 · Can Day Trading Really Be Profitable? (2023)
*Carlo Zarattini, Andrew Aziz* · instruments: QQQ, TQQQ · access: ssrn_free_download · testable on our data: yes

- **Why:** Opening range breakout on QQQ 2016-2023, 33% annual alpha net of commissions - same authors as the VWAP paper, directly maps onto our ORB spec on NQ. An independent replication (MQL5 blog) reports gross results reproduce but net of costs it is about zero - worth checking ourselves.
- **Should contain:** Exact ORB rules (5-min range, stop, sizing by ATR), stock-in-play filter, yearly results
- **Get it:** SSRN abstract 4416622 -> 'Download This Paper' (free, may ask for a free SSRN login) https://papers.ssrn.com/abstract=4416622
- **Save as:** `papers/inbox/can_day_trading_really_be_profitable.pdf`

### P1 · Hedging Demand and Market Intraday Momentum (2021)
*Guido Baltussen, Zhi Da, Sten Lammers, Martin Martens* · instruments: ES, NQ, 60+ futures · access: open_pdf · testable on our data: yes

- **Why:** Return from prior close to 15:30 predicts the last 30 minutes in 60+ futures, 1974-2020. WHY: option dealers and leveraged-ETF managers who are short gamma must buy into rallies and sell into drops near the close.
- **Should contain:** Last-30-min predictability by asset class and by gamma level; reversal over following days; strategy returns
- **Get it:** Free PDF on Erasmus University repository (pure.eur.nl, 'Hedging Demand and Market Intraday Momentum') https://doi.org/10.1016/j.jfineco.2021.04.029
- **Save as:** `papers/inbox/hedging_demand_and_market_intraday_momentum.pdf`

### P1 · Market Return Around the Clock: A Puzzle (2020)
*Oleg Bondarenko, Dmitriy Muravyev* · instruments: ES · access: ssrn_free_download · testable on our data: yes

- **Why:** Finding: the whole average ES return comes in a 4-hour window around the European open (roughly 2:00-6:00 ET). The paper says it is positive every year and survives costs. WHY: this is the 'information arrives while the market is closed' pattern. Uncertainty builds overnight while the US is absent and is resolved when European investors process it, which is also a risk and liquidity premium. It gives us a new angle: trade the overnight session by clock window instead of the usual close-to-open. It is not the already-known Overnight Drift paper. It is a separate, more granular study with a different mechanism (uncertainty resolution) and a conditional rule (buy after a large US selloff). What would kill it: European investors becoming less central, the overnight VIX pattern disappearing, or 24h liquidity equalising. Decay risk is high because it was published in 2020 and the Boyarchenko overnight drift paper is widely known. Out-of-sample 2020-2026 is a clean decay test.
- **Should contain:** Average E-mini S&P 500 return by time of day over a near-24-hour session. About 4 hours around the European open account for the whole average market return, and the other 20 hours are a noisy zero. It should report a Sharpe ratio near 1.6 after costs, and results by year, around daylight-saving shifts, and in the 2020 COVID period. It should also link overnight VIX-futures uncertainty to the European open. Our ES 1-min ETH data (2013-12 to 2026-09, UTC) can rebuild the hour-by-hour return profile. Convert UTC to Europe/US clock time carefully because of the DST mismatch weeks.
- **Get it:** Open the SSRN abstract page (ssrn.com/abstract=3596245) and click 'Download This Paper' (free, SSRN login may be needed). The JFQA version (DOI 10.1017/S0022109022000783) is paywalled. The 70-page SSRN PDF is the better copy. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3596245
- **Save as:** `papers/inbox/market_return_around_the_clock_a_puzzle.pdf`

### P1 · The Overnight Drift (2023)
*Nina Boyarchenko, Lars C. Larsen, Paul Whelan* · instruments: ES, NQ, YM · access: open_pdf · testable on our data: yes

- **Why:** E-mini returns concentrated around 2-3 a.m. ET (European open), explained by dealers' inventory risk from end-of-day order imbalances. Their July 2026 follow-up (Liberty Street Economics, 'The Disappearing Overnight Drift') says the effect has been near zero since 2021 - a direct test of Conti's overnight claim.
- **Should contain:** Hour-by-hour E-mini returns 1998-2020, link to closing order imbalance; timing rules for an overnight window
- **Get it:** Free NY Fed Staff Report 917 PDF (newyorkfed.org) https://doi.org/10.1093/rfs/hhad020
- **Save as:** `papers/inbox/the_overnight_drift.pdf`

### P2 · Dash for Cash: Monthly Market Impact of Institutional Liquidity Needs (2020)
*Erkko Etula, Kalle Rinne, Matti Suominen, Lauri Vaittinen* · instruments: S&P 500, ES · access: open_pdf · testable on our data: yes

- **Why:** Equity prices fall into the days before month end and rise after, because institutions must raise cash for monthly payments (pensions, payroll). Classic forced-flow WHY.
- **Should contain:** Daily return pattern around turn of month, size of the effect in S&P 500 futures, which days to be long/short
- **Get it:** Free working-paper PDF on orbilu.uni.lu or aalto.fi https://academic.oup.com/rfs/article/33/1/75/5494694
- **Save as:** `papers/inbox/dash_for_cash_monthly_market_impact_of_institutional_liquidi.pdf`

### P2 · Do S&P500 Options Increase Market Volatility? Evidence from 0DTEs (2025)
*Greg Adams, Chukwuma Dim, Bjorn Eraker, Jean-Sebastien Fontaine, Chayawat Ornthanalai, Grigory Vilkov* · instruments: ES, S&P 500 index, SPX options · access: open_pdf · testable on our data: partial

- **Why:** Finding: when 0DTE contracts expire, intraday index volatility is lower on average. Higher dealer net gamma predicts reversal and negative momentum at high frequency, and the effect fades in about an hour. WHY: this is the 'execution mechanics of big players' pattern. Dealers who are long gamma must sell rallies and buy dips, which is forced and predictable. It complements our transcript-04 gamma study, which found continuation at gamma levels. This paper gives the reversal side and the time scale (about 1 hour), so it helps decide when to fade and when to follow. What would kill it: dealer positioning flipping to net short gamma, retail flow dominating, or a change in how the 0DTE calendar works. Decay risk is moderate because the topic is hot and new. Read it together with Baltussen et al. (already known) for the negative-gamma momentum side.
- **Should contain:** Evidence that 0DTE days have lower 10-minute realised S&P 500 volatility. It explains this through market-maker net-gamma hedging needs that come from positions built earlier in longer-dated options. It also predicts intraday order-flow reversal in E-mini futures, lower momentum returns, and effects that fade after about an hour. It needs SPX/0DTE option data to rebuild the net-gamma proxy, and we don't have that. We can test the reduced-form part on ES 1-min bars: volatility, reversal versus momentum at 10-60 minute horizons, expiration versus non-expiration days, and before versus after the daily-expiry era.
- **Get it:** Direct PDF from the author site (link above, free). The SSRN abstract page (ssrn.com/abstract=5641974) also has 'Download This Paper'. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5641974
- **Save as:** `papers/inbox/do_s_p500_options_increase_market_volatility_evidence_from_0.pdf`

### P2 · Intraday price reversals in the US stock index futures market: A 15-year study (2004)
** · instruments: ES, S&P 500 futures · access: paywalled · testable on our data: yes

- **Why:** Finding: after large opening gaps in index futures, price continues for roughly the first 10 minutes and then reverses. The reversal is stronger after up-gaps. This is the opposite of the 'ORB carries through' story, so it is a useful stress test of the gap and opening-range ideas. WHY: this is the 'information arrives while the market is closed' pattern, but with overreaction. Overnight order imbalances and liquidity needs at the open push prices too far, and liquidity providers pull them back. It matches the playbook idea of overnight overreaction correcting intraday. Pair it with Bondarenko-Muravyev (the overnight gain is concentrated at the European open) to separate gaps caused by Europe from gaps caused by the US open. What would kill it: faster algorithmic opening auctions that absorb imbalances, or a stronger continuation regime. Decay risk is high because the sample ends in 2002 and is well known. The 2013-2026 re-test is the real value.
- **Should contain:** Event study on S&P 500 and other index futures, Nov 1987 to Sep 2002. Event days are those where the opening gap is at least a filter size (0.10%, 0.20%, 0.30%). It finds about 10 minutes of significant continuation after the open and then a long series of reversals. Reversals are stronger after large positive open gaps. It should include year-by-year and day-of-week tables. We can replicate this directly on ES 1-min data for 2013-2026 by defining gap as RTH open versus prior RTH close and measuring the return path every minute.
- **Get it:** ScienceDirect abstract page (link above). The full text is paywalled, so use a university or library login, or ask the authors for a copy. A working-paper version may exist on SSRN or an author site, so search the title there first. https://www.sciencedirect.com/science/article/abs/pii/S0378426604000949
- **Save as:** `papers/inbox/intraday_price_reversals_in_the_us_stock_index_futures_marke.pdf`

### P2 · Pinning in the S&P 500 Futures (2010)
*Benjamin Golez, Jens Carsten Jackwerth* · instruments: ES, S&P 500 futures, options on S&P 500 futures · access: ssrn_free_download · testable on our data: partial

- **Why:** Finding: ES is pulled toward the nearest strike on option expiry days, and index-option expiry creates the opposite push. WHY: market makers hedging delta against time decay, plus individuals reselling in-the-money options. This is forced hedging flow tied to a calendar, so we can predict when it happens. Related to our gamma work but at the strike and expiry level, and it covers the 'futures roll and settlement effects' and 'option expiration' areas. What would kill it: market makers' inventory shrinking, expiries becoming daily (the pin gets diluted across every day), or exchange settlement rules changing. Decay risk is high. The paper is old, and weekly and daily expiries since 2016 and 2022 change the setting a lot. Use it for the mechanism and expect a weaker effect.
- **Should contain:** Evidence that S&P 500 futures are pulled towards the at-the-money strike on days when serial options on the futures expire. They are pushed away from the cost-of-carry-adjusted at-the-money strike just before S&P 500 index options expire ('anti-cross-pinning'). It gives the dealer delta-hedging mechanism and an estimate of at least $115 million shifted per expiration day. The sample is old, so we should rebuild it on 2013-2026 ES 1-min bars. We need the option expiration calendar (monthly, serial and weekly) and the nearest strikes, which we can compute but we don't have it as data. Test the distance of the ES close to the nearest strike on expiry days versus other days, and the drift in the last hour before the expiry settlement.
- **Get it:** SSRN abstract page (ssrn.com/abstract=1664261), click 'Download This Paper'. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1664261
- **Save as:** `papers/inbox/pinning_in_the_s_p_500_futures.pdf`

### P2 · The Pre-FOMC Announcement Drift (2015)
*David O. Lucca, Emanuel Moench* · instruments: ES, S&P 500 · access: unknown · testable on our data: yes

- **Why:** S&P 500 rose a large share of its total return in the 24 hours before scheduled FOMC announcements. Later work (SSRN 'The Disappearing Pre-FOMC Announcement Drift') says it faded - test both on ES.
- **Should contain:** Return in the 24h before 14:00 ET FOMC releases, 1994-2011; needs a list of FOMC dates (public)
- **Get it:** NY Fed Staff Report 512 (free on newyorkfed.org) - search 'Lucca Moench pre-FOMC announcement drift staff report' https://libertystreeteconomics.newyorkfed.org/2012/07/the-puzzling-pre-fomc-announcement-drift
- **Save as:** `papers/inbox/the_pre_fomc_announcement_drift.pdf`

### P2 · The Unintended Consequences of Rebalancing (2025)
*Campbell R. Harvey, Michele G. Mazzoleni, Alessandro Melone* · instruments: ES, S&P 500 futures, 10-year Treasury note futures · access: open_pdf · testable on our data: partial

- **Why:** Finding: predictable pension and balanced-fund rebalancing flows move US equity and bond returns, mostly at month-end and quarter-end, and the signal became significant in the early 2000s. WHY: this combines an institutional constraint or mandate (calendar and threshold rules, tracking error versus benchmarks) with liquidity needs. The flow is forced and the timing is known. For ES the angle is to condition month-end and quarter-end behaviour on the prior month's equity-versus-bond performance, then test the last days of the month and the first day of the next month. What would kill it: pension funds randomising rebalancing dates, or front-running arbitrage capital crowding it out (the authors themselves argue it should stop). Decay risk is moderate: it is very recent, and the turn-of-month effect is old and known. It extends the already-known 'Dash for Cash' idea with a clean mechanism. Also compare it with the turn-of-the-month paper on infrequent rebalancing in the Journal of International Financial Markets (ScienceDirect S1042443126000259), which I did not list because it is paywalled and I could not confirm its authors.
- **Should contain:** Two rule-based rebalancing signals: Threshold (portfolio weights drift past a band) and Calendar (month-end and quarter-end). It shows they predict equity and bond returns with opposite signs. When stocks are overweight, funds sell stocks, with about a 17 bp lower next-day equity return. The pressure is mostly gone within about 2 weeks. Calendar predictability is strong at month-end and builds toward quarter-end. It includes an S&P 500 vs 10-year Treasury futures long-short strategy with a Sharpe above 1 and high skew. We can test the equity side on ES using prior-month stock-versus-bond performance as a proxy for pension overweight, but we have no Treasury futures or pension weight data. It needs ZN/bond futures to test the full long-short trade.
- **Get it:** Free NBER PDF (link above, NBER working-paper w33554). A copy is also on the AFA site. The version I found lists Harvey among the authors, and I did not see the other two names in the search results, so check the author list on the PDF. https://www.nber.org/system/files/working_papers/w33554/revisions/w33554.rev0.pdf
- **Save as:** `papers/inbox/the_unintended_consequences_of_rebalancing.pdf`

### P3 · Does Overnight News Explain Overnight Returns? (2025)
** · instruments: US stocks, index · access: open_pdf · testable on our data: partial

- **Why:** Tests whether news flow, rather than a risk premium, drives overnight returns - helps decide which WHY behind the overnight effect is real.
- **Should contain:** Overnight return decomposition by news vs no-news nights
- **Get it:** Free on arXiv https://arxiv.org/abs/2507.04481
- **Save as:** `papers/inbox/does_overnight_news_explain_overnight_returns.pdf`

### P3 · Price Drift before U.S. Macroeconomic News: Private Information about Public Announcements? (2019)
** · instruments: ES, E-mini S&P 500 futures, 10-year Treasury note futures · access: open_pdf · testable on our data: partial

- **Why:** Finding: ES (and Treasury futures) drift in the direction of the coming macro surprise before the release, for a subset of announcements. This is a broader version of the already-known Pre-FOMC drift paper. WHY: informed or well-connected traders position before public news and large players adjust risk ahead of events. The WHY is shakier than in the other papers, so treat it as a lower-priority idea. What would kill it: stricter release controls (lock-ups, embargo rules), faster information dissemination, or more trading ahead of releases that arbitrages away the drift. Decay risk is high; the sample ends in 2014. Useful mostly for event-window design (which releases, what time before, what holding period) and for the 'event not state' lesson from the gamma study.
- **Should contain:** Second-by-second E-mini S&P 500 and 10-year note futures, Jan 2008 to Mar 2014. It covers 21 market-moving announcements out of 30 US macro releases (for example GDP Advance, ISM, consumer confidence, nonfarm payrolls, CPI). It shows that 11 of the 21 have a pre-announcement drift in the direction of the later surprise, with a table of drift size by announcement, a profit estimate (about $262,000 per release across seven drift announcements), and the proposed explanation (informed trading ahead of public news, mostly in the stock market). We can test the direction-agnostic parts on ES 1-min bars: volatility and returns in windows before and after release times. We need an economic calendar with release times, and the later-surprise direction needs consensus forecasts, which we don't have.
- **Get it:** Free PDF from the ECB (link above). The 2015 draft is also at pages.stern.nyu.edu/~jh4/SternMicroMtg/Old/SternMicroMtg2015/Papers/Preannouncement_042015Strasser.pdf. https://www.ecb.europa.eu/pub/pdf/scpwps/ecbwp1901.en.pdf
- **Save as:** `papers/inbox/price_drift_before_u_s_macroeconomic_news_private_informatio.pdf`


## 3. Recommended research — Stocks

### P1 · A Profitable Day Trading Strategy For The U.S. Equity Market (2024)
*Carlo Zarattini, Andrea Barbon, Andrew Aziz* · instruments: US single stocks (7,000+ names), applicable by analogy to ES, applicable by analogy to NQ · access: ssrn_free_download · testable on our data: partial

- **Why:** Finding: the 5-minute ORB works far better only on days a stock is 'in play' (abnormal relative volume, usually on company news), including after costs. WHY (our framing): a news catalyst forces institutions to build or unwind large positions over the day. Their orders cannot be absorbed in the first minutes, so the imbalance continues. Without abnormal volume the catalyst is already priced in and there is no forced flow. Same pattern as Conti's ORB WHY (info arrives while closed, order imbalance at the open). What would kill it: institutions fully pre-positioning before the open, or retail and HFT crowding the opening range. Decay risk: published 2024 and a widely followed trader community, so check the post-2023 period.
- **Should contain:** Opening Range Breakout on more than 7,000 US stocks, 2016-2023. Focus is a 'Stocks in Play' filter based on relative volume (today's volume vs. prior-day average). Reported results: top-20 Stocks in Play portfolio, over 1,600% net, Sharpe 2.81, annualized alpha 36%, versus 198% for passive S&P 500. Also a comparison of 5/15/30/60-minute opening ranges, and best/worst 25 stock tables. Data needed to replicate: intraday single-stock bars and relative volume (we don't have these). Our ES 1-min data can only test the ORB logic and the 'abnormal-volume days' idea at index level.
- **Get it:** SSRN abstract page above, click 'Download This Paper' (free). Same PDF is on the author's site abarbon.com (link 'Download PDF' on the paper page). https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4729284
- **Save as:** `papers/inbox/a_profitable_day_trading_strategy_for_the_u_s_equity_market.pdf`

### P1 · A Tug of War: Overnight versus Intraday Expected Returns (2019)
*Dong Lou, Christopher Polk, Spyros Skouras* · instruments: US stocks · access: open_pdf · testable on our data: no

- **Why:** Momentum profits are earned almost entirely overnight; most other anomalies (value, size, etc.) are earned intraday and reverse overnight. WHY: different clienteles - individuals trade at the open, institutions during the day - push in opposite directions.
- **Should contain:** Overnight vs intraday decomposition of 10+ stock anomalies; a strategy that holds momentum overnight only.
- **Get it:** Free PDF on Christopher Polk's LSE page https://researchonline.lse.ac.uk/id/eprint/87481
- **Save as:** `papers/inbox/a_tug_of_war_overnight_versus_intraday_expected_returns.pdf`

### P1 · Asset Fire Sales (and Purchases) in Equity Markets (2007)
*Joshua Coval, Erik Stafford* · instruments: US stocks · access: open_pdf · testable on our data: no

- **Why:** Mutual funds with big outflows are forced to sell their holdings, pushing prices below value; prices recover over the following months. Classic forced-seller WHY - buy what distressed funds must dump.
- **Should contain:** How to identify forced sellers from fund flows/holdings, size and timing of the price drop and rebound. Needs mutual fund holdings/flows data.
- **Get it:** Free NBER working paper w11357 PDF https://www.nber.org/papers/w11357
- **Save as:** `papers/inbox/asset_fire_sales_and_purchases_in_equity_markets.pdf`

### P1 · Famous Firms, Earnings Clusters, and the Stock Market (2020)
*Yixin Chen, Randolph B. Cohen, Zixuan (Kevin) Wang* · instruments: US mega caps, S&P 500, ES · access: ssrn_free_download · testable on our data: partial

- **Why:** A large part of the yearly market return comes in the 24 hours before days when several famous firms report together after the close - days known in advance. WHY: optimists buy into the attention spike while short-sale limits keep pessimists out. Tradable on ES as well as the stocks.
- **Should contain:** How clusters are defined, return close-to-close before post-close clusters, results by year. Needs a mega-cap earnings calendar (public).
- **Get it:** SSRN abstract 3685452 -> 'Download This Paper' https://papers.ssrn.com/abstract=3685452
- **Save as:** `papers/inbox/famous_firms_earnings_clusters_and_the_stock_market.pdf`

### P1 · The Earnings Announcement Premium and Trading Volume (2007)
*Andrea Frazzini, Owen A. Lamont* · instruments: US single stocks · access: open_pdf · testable on our data: no

- **Why:** Finding: prices drift up into and around scheduled earnings dates, strongest for stocks with high past announcement-period volume. This is the pre-earnings run-up. WHY: the authors link it to small-investor buying when the announcement catches their attention, with limits to arbitrage stopping institutions from fully trading against it. That is a predictable-flow reason: attention-driven retail demand on a known calendar date. A risk-premium reading is also in the literature (the Savor-Wilson / Liu et al. papers cited in the search results). What would kill it: attention-driven retail buying fading, or the premium being arbitraged through earnings-date calendar trades. Decay risk: published 2007 and well known. Test the post-2010 period before trusting it.
- **Should contain:** Evidence that stocks rise on average around scheduled earnings announcement dates, with volume surging. Monthly long-short strategies (long expected announcers, short non-announcers) earning 7%-18% per year with high Sharpe ratios. Includes the link to past announcement-period volume and imputed small-investor buying. Data needed to replicate: single-stock returns and the scheduled earnings calendar (we don't have these).
- **Get it:** NBER PDF link above (direct, free). SSRN abstract page also has 'Download This Paper'. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=986940
- **Save as:** `papers/inbox/the_earnings_announcement_premium_and_trading_volume.pdf`

### P2 · Decoding Inside Information (2012)
*Lauren Cohen, Christopher Malloy, Lukasz Pomorski* · instruments: US single stocks · access: open_pdf · testable on our data: no

- **Why:** Finding: after removing routine insider trades (more than half of all trades), the remaining opportunistic trades carry all the predictive power. WHY: insiders hold private information, and the information reaches prices slowly (slow diffusion). The paper adds a filter that removes calendar-driven noise. What would kill it: tighter SEC enforcement. The paper shows opportunistic insiders cut trading after enforcement waves. A later study found smaller profits after Dodd-Frank (66 bp over 12 months in the high-enforcement regime, per a citing summary), so check the post-2010 period. Decay risk: published 2012 and widely followed. Insider buy data is free from EDGAR, so this is a cheap one to acquire data for.
- **Should contain:** A rule for separating routine from opportunistic insider trades: an insider who traded in the same calendar month in prior consecutive years is routine. A portfolio of opportunistic trades only, with value-weighted abnormal returns of about 82 bp per month, while routine trades earn about zero. Tests of what opportunistic trades predict (news and events), and of which insiders are most informed (local, non-executive, poorly governed firms). Data needed: SEC Form 4 insider filings (free from EDGAR) plus stock prices (we have no single-stock prices).
- **Get it:** NBER PDF link above (free). A free Harvard copy is also on dash.harvard.edu (search the title). SSRN abstract page lists the NBER paper. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1692517
- **Save as:** `papers/inbox/decoding_inside_information.pdf`

### P2 · Retail Investors' Contrarian Behavior Around News, Attention, and the Momentum Effect (2025)
*Patrick (Cheng) Luo, Enrichetta Ravina, Marco C. Sammon, Luis M. Viceira* · instruments: US single stocks · access: open_pdf · testable on our data: no

- **Why:** Finding: extreme returns or surprises alone do not produce PEAD or momentum. The drift depends on retail contrarian trading pushing against the news. Small caps with low institutional ownership drift most; large caps show little PEAD. WHY: retail counter-trading slows the price adjustment to the news (slow information diffusion plus a flow constraint). This matches the Conti rule 'PEAD works in small/mid caps, not mega caps'. It also gives a concrete filter, retail flow imbalance, to combine with surprise size. What would kill it: retail flow turning momentum-following (for example the post-2020 retail boom), or low-coverage small caps becoming better covered. Decay risk: recent (2025), so low for now.
- **Should contain:** A US brokerage-account panel showing retail investors trade as contrarians after large earnings surprises, especially in loser stocks. PEAD and momentum are stronger where retail contrarian flow is heaviest. Sorts by firm size, institutional ownership and analyst coverage. Small caps show stronger PEAD than large caps. Data needed: earnings surprises, retail flow data, institutional ownership (we have none).
- **Get it:** nber.org/papers/w34086, then use the PDF link (the system/files PDF above). If the NBER page asks for payment, the earlier 2021 draft is free at marcosammon.com/images/lrsv.pdf. SSRN charges $5 for the NBER version. https://www.nber.org/papers/w34086
- **Save as:** `papers/inbox/retail_investors_contrarian_behavior_around_news_attention_a.pdf`

### P2 · The 52-Week High and Momentum Investing (2004)
*Thomas J. George, Chuan-Yang Hwang* · instruments: US stocks · access: unknown · testable on our data: partial

- **Why:** Stocks near their 52-week high keep outperforming. WHY: traders anchor on the 52-week high and under-react to good news near it. Also tested on index level in later work.
- **Should contain:** Ranking by price / 52-week high, holding periods, comparison with classic momentum.
- **Get it:** Journal of Finance 2004; search the title on Google Scholar for a free author copy https://alphaarchitect.com/the-secret-to-momentum-is-the-52-week-high/
- **Save as:** `papers/inbox/the_52_week_high_and_momentum_investing.pdf`

### P2 · The Loan Fee Anomaly: A Short Seller's Best Ideas (2020)
*Joseph E. Engelberg, Richard B. Evans, Greg Leonard, Adam V. Reed, Matthew C. Ringgenberg* · instruments: US single stocks · access: open_pdf · testable on our data: no

- **Why:** Finding: high borrow fees predict low future returns. A short-sale constraint means mispricing persists in those names, and the anomalies concentrate there. WHY: an institutional constraint. Shorting costs, recall risk and fee variance limit arbitrage. The related Short-Selling Risk paper (Engelberg, Reed, Ringgenberg; SSRN 2312625) shows stocks with more short-selling risk have lower returns and less price efficiency. Squeeze angle: when loans are recalled, forced covering can cause sharp up-moves (see 'Short Squeezes and Their Consequences', Cambridge). What would kill it: cheaper, more liquid securities lending, or fee data becoming public enough to be arbitraged. Decay risk: moderate. Its practical use is as a filter (do not short high-fee names, and beware squeezes) more than a standalone signal.
- **Should contain:** Evidence that stock-loan fees predict returns better than 102 other anomalies over 2006-2019 (this comparison is described in a later paper that cites it, the Journal of Financial and Quantitative Analysis article 'Short Squeezes and Their Consequences'). Also that other anomalies live almost entirely in high-loan-fee stocks. Data needed: stock loan fee and utilization data (a paid securities-lending feed such as IHS Markit/S&P Global; we have none).
- **Get it:** Free PDF at the uncipc.org link above. SSRN abstract page: ssrn.com/abstract=3707166, click 'Download This Paper'. https://ssrn.com/abstract=3707166
- **Save as:** `papers/inbox/the_loan_fee_anomaly_a_short_seller_s_best_ideas.pdf`

### P2 · The Russell Reconstitution Effect (2001)
** · instruments: Russell 2000 stocks · access: ssrn_free_download · testable on our data: no

- **Why:** Index funds must trade every addition/deletion on reconstitution day, creating order imbalances and price pressure. The 2007 follow-up says the effect has weakened - check what survives.
- **Should contain:** Abnormal returns from rank day to reconstitution day for additions vs deletions; reversal afterwards. Needs Russell membership lists.
- **Get it:** SSRN abstract 278000; follow-up 'Russell Reconstitution Effect Revisited' is SSRN 960727 https://papers.ssrn.com/sol3/papers.cfm?abstract_id=278000
- **Save as:** `papers/inbox/the_russell_reconstitution_effect.pdf`

### P3 · The Disappearing Index Effect (2025)
*Robin Greenwood, Marco Sammon* · instruments: S&P 500 constituents (additions/deletions), US single stocks · access: open_pdf · testable on our data: no

- **Why:** Finding: index inclusion/deletion abnormal returns have almost vanished. WHY it existed: forced index-fund buying and selling on predictable dates, with limited liquidity supply. WHY it faded: the paper reports that the market's liquidity-provision capacity improved a lot (by about a factor of 20), as other institutions stand ready to sell to indexers. This is a clear case study of a forced-flow edge being competed away, and it tells us which index events might still be inefficient. What would kill any index-event strategy: more anticipation and more liquidity providers. Decay risk: already decayed in the S&P 500. Better used as a warning than as a signal.
- **Should contain:** The abnormal return on S&P 500 additions fell from about 7.4% in the 1990s to under 1% in the most recent decade. Deletions show a similar decline. Decomposition into drivers (migrations from the S&P MidCap index, anticipation, increased liquidity provision). The effect also declines in other index families. Data needed: S&P 500 change announcement/effective dates and single-stock prices (we have neither).
- **Get it:** Free PDF at the hbs.edu link above, or the NBER PDF (nber.org/system/files/working_papers/w30748/w30748.pdf). SSRN abstract page also has 'Download This Paper'. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4294297
- **Save as:** `papers/inbox/the_disappearing_index_effect.pdf`

