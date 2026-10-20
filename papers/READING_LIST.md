# Reading list — papers to download

Updated 2026-10-20. Download each PDF and save it in `papers/inbox/` **using the file name shown** (or attach it in chat). The next run reads the full paper and replaces the partial summary.

## 1. Couldn't get the full text — please download

| Paper | Why it matters | Where to get it | Save as |
|---|---|---|---|
| Market Intraday Momentum (2018) — *abstract only* | transcript 01 - opening range breakout (open preprint may exist on author pages) | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2440866 | `market_intraday_momentum.pdf` |
| Volume Weighted Average Price (VWAP): The Holy Grail for Day Trading Systems (2023) — *partial* | transcript 01 - VWAP trend | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4631351 | `volume_weighted_average_price_vwap_the_holy_grail_for_day_tr.pdf` |

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

### P1 · Do S&P500 Options Increase Market Volatility? Evidence from 0DTEs (2025)
*Greg Adams, Chukwuma Dim, Bjorn Eraker, Jean-Sebastien Fontaine, Chayawat Ornthanalai, Grigory Vilkov* · instruments: ES, S&P 500 index · access: open_pdf · testable on our data: partial

- **Why:** Complements the gamma-exposure study already in the method notes (video 04, where crossings continued) with an academic counter-view: net-positive dealer gamma makes hedging counter-directional (dealers trade against the move), which damps volatility and produces reversals in ES; negative gamma does the opposite. Structural WHY = execution mechanics of big players (delta-hedging by market makers) plus limited liquidity in the underlying. Tells us the regime switch: reversion when dealers are long gamma, continuation when short. Edge killers: change in dealer positioning (retail 0DTE selling flipping dealer gamma sign), CME/Cboe product changes. Decay risk: very new (2023-2025), so little crowding evidence yet. Related finding worth cross-checking in the same list: Cboe's paper 'gammasqueezes' estimates the maximum impact of dealer gamma on S&P volatility.
- **Should contain:** Intraday evidence that on days with expiring 0DTE contracts, 10-minute realized S&P 500 volatility is lower; that market makers' net gamma (built from option data) predicts lower volatility over the next ~10 minutes, fading after about an hour; and that higher net gamma predicts stronger order-flow REVERSAL and weaker momentum in E-mini futures. Needs SPX option volume/open interest to build gamma (we do not have it); the volatility/reversal behaviour on 0DTE-era vs pre-0DTE days can be tested on our ES data (ES ticks 2021-06 to 2023-06, 1-min to 2026-09; NQ ticks 2021-07 onward).
- **Get it:** Free PDF from author site: https://www.jean-sebastienfontaine.com/papers/0dte-options-volatility.pdf . Also SSRN abstract page https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5641974 -> 'Download This Paper'. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5641974
- **Save as:** `papers/inbox/do_s_p500_options_increase_market_volatility_evidence_from_0.pdf`

### P1 · Hedging Demand and Market Intraday Momentum (2021)
*Guido Baltussen, Zhi Da, Sten Lammers, Martin Martens* · instruments: ES, NQ, 60+ futures · access: open_pdf · testable on our data: yes

- **Why:** Return from prior close to 15:30 predicts the last 30 minutes in 60+ futures, 1974-2020. WHY: option dealers and leveraged-ETF managers who are short gamma must buy into rallies and sell into drops near the close.
- **Should contain:** Last-30-min predictability by asset class and by gamma level; reversal over following days; strategy returns
- **Get it:** Free PDF on Erasmus University repository (pure.eur.nl, 'Hedging Demand and Market Intraday Momentum') https://doi.org/10.1016/j.jfineco.2021.04.029
- **Save as:** `papers/inbox/hedging_demand_and_market_intraday_momentum.pdf`

### P1 · Market Return Around the Clock: A Puzzle (2022)
*Oleg Bondarenko, Dmitriy Muravyev* · instruments: ES · access: ssrn_free_download · testable on our data: yes

- **Why:** Directly extends the 'overnight drift' idea Conti uses but is not in our already-known list. Finding: the overnight premium is concentrated in a ~4-hour window around the European open (roughly 02:00-06:00 ET). Structural WHY (risk/liquidity premium + information accumulated while the US is closed): uncertainty builds during Asian hours and is resolved when European investors process it. That gives a precise clock-time window we can turn into a simple long-only 'European-open' ES rule and a 'different session' angle. What would kill it: 24h participation by US desks / Asian-session price discovery, or the VIX-uncertainty pattern vanishing. Decay risk: published 2020, so check the 2019-2026 out-of-sample portion of our ES data (our ES 1-min covers 2013-2026 in UTC; remember DST handling for European open).
- **Should contain:** Average E-mini S&P 500 excess return by time of day over a ~24h session, 2006-2018 (plus 2020 COVID check). Main claim: the four hours around the European open account for the entire average return, with a 1.6 Sharpe that stays high after costs and positive returns every year; the other 20 hours are a noisy zero. Also VIX-futures evidence (uncertainty rises overnight, falls at the European open). Needs only ES intraday bars, which we have.
- **Get it:** SSRN abstract page https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3596245 -> click 'Download This Paper' (70 pages, free with SSRN login). Published version: JFQA 58(2022/23). https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3596245
- **Save as:** `papers/inbox/market_return_around_the_clock_a_puzzle.pdf`

### P1 · The Overnight Drift (2023)
*Nina Boyarchenko, Lars C. Larsen, Paul Whelan* · instruments: ES, NQ, YM · access: open_pdf · testable on our data: yes

- **Why:** E-mini returns concentrated around 2-3 a.m. ET (European open), explained by dealers' inventory risk from end-of-day order imbalances. Their July 2026 follow-up (Liberty Street Economics, 'The Disappearing Overnight Drift') says the effect has been near zero since 2021 - a direct test of Conti's overnight claim.
- **Should contain:** Hour-by-hour E-mini returns 1998-2020, link to closing order imbalance; timing rules for an overnight window
- **Get it:** Free NY Fed Staff Report 917 PDF: https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr917.pdf (journal version: https://doi.org/10.1093/rfs/hhad020)
- **Save as:** `papers/inbox/the_overnight_drift.pdf`

### P2 · Assessing the Profitability of Timely Opening Range Breakout on Index Futures Markets (2019)
*Yi-Cheng Tsai, Mu-En Wu, Jia-Hao Syu, Chin-Laung Lei, Chung-Shu Wu, Jan-Ming Ho, Chuan-Ju Wang* · instruments: ES, NQ, DJIA futures, HSI futures, TAIEX futures · access: open_pdf · testable on our data: yes

- **Why:** The only index-futures-specific ORB paper found, and it carries a structural WHY that fits the Conti method: the opening/closing minutes of the underlying cash market carry peak volume and volatility, and breakout signals line up with institutional order flow. We can replicate the idea on ES (1-min, 2013-2026) and test long-only vs both sides, volatility-scaled stops and time exits. Caveats: sample ends in 2013 (alpha-decay risk, check 2014+ out-of-sample), costs and slippage assumptions need checking, and the profits are strongest in Asian markets. A companion working paper by Holmberg, Lonnbark and Lundstrom (Finance Research Letters; crude oil futures only, profits concentrated in 2000-2011) is a cautionary read; a 2026 arXiv paper on MNQ ('Structural Limits of OHLCV-Based Intraday Momentum Signals in MNQ Futures', arXiv 2605.04004) tests ORB and gap signals and reports falsification results, useful as a sceptical benchmark.
- **Should contain:** One-minute data on DJIA, S&P 500, NASDAQ, HSI and TAIEX index futures, 2003-2013. Timely ORB (TORB): align the strategy's 'active hours' with when the underlying stock market is open, use a short opening probing window, and trade breakouts. Reports annual returns above 8% in all five markets (p-values below 3%), best probing time per market (short in the US, longer in Asia), and a TAIEX transaction-level check that TORB signals are in the same direction as institutional (especially foreign) traders.
- **Get it:** IEEE Access is open access: https://ieeexplore.ieee.org/document/8641124/ -> click 'PDF'. DOI 10.1109/ACCESS.2019.2899177. Alternate PDF copies: the scispace link above, or the ResearchGate copy (CC BY-NC-ND). https://ieeexplore.ieee.org/document/8641124/
- **Save as:** `papers/inbox/assessing_the_profitability_of_timely_opening_range_breakout.pdf`

### P2 · Dash for Cash: Monthly Market Impact of Institutional Liquidity Needs (2020)
*Erkko Etula, Kalle Rinne, Matti Suominen, Lauri Vaittinen* · instruments: S&P 500, ES · access: open_pdf · testable on our data: yes

- **Why:** Equity prices fall into the days before month end and rise after, because institutions must raise cash for monthly payments (pensions, payroll). Classic forced-flow WHY.
- **Should contain:** Daily return pattern around turn of month, size of the effect in S&P 500 futures, which days to be long/short
- **Get it:** Free working-paper PDF on orbilu.uni.lu or aalto.fi https://academic.oup.com/rfs/article/33/1/75/5494694
- **Save as:** `papers/inbox/dash_for_cash_monthly_market_impact_of_institutional_liquidi.pdf`

### P2 · Overnight Returns of Stock Indexes: Evidence from ETFs and Futures (2017)
*Qingfu Liu, Yiuman Tse* · instruments: ES, S&P 500 ETF · access: unknown · testable on our data: yes

- **Why:** A directly testable, rule-ready ES pattern: gap/overnight move -> fade in the first half hour, then continuation into the final half hour. Complements (and partly contradicts) the already-known 'Market Intraday Momentum' (first half-hour predicts last), so it is a useful conflict to resolve in our own data. Structural WHY: market-maker inventory management at the close/open (Branch and Ma are cited as attributing overnight gains and daytime losses to market-maker trading) rather than retail attention. Edge killers: faster inventory unwind (24h liquidity, European-open offloading), or overnight and intraday returns becoming positively correlated. Decay risk: sample ends 2014, so our 2013-2026 ES data gives a genuine out-of-sample test of the 2015+ period.
- **Should contain:** Using TAQ and S&P (E-mini) futures trades, 1999-2014: overnight returns of the S&P 500 and sector ETFs and most international index futures are significantly positive while daytime returns are negative; overnight return predicts the first-30-minute return NEGATIVELY (open reversal) and the last-30-minute return POSITIVELY, with no relation for 10:00-15:30; and the first-30-minute return does not predict the last-30-minute return. Includes in- and out-of-sample forecasts and volatility-sorted subsamples.
- **Get it:** SSRN abstract page https://www.ssrn.com/abstract=2921758 -> look for 'Download This Paper' (check whether a free PDF is offered; if not, the journal version is on ScienceDirect, DOI 10.1016/j.iref.2017.01.005, probably paywalled; author preprint may be on ResearchGate). https://www.ssrn.com/abstract=2921758
- **Save as:** `papers/inbox/overnight_returns_of_stock_indexes_evidence_from_etfs_and_fu.pdf`

### P2 · Price Drift before U.S. Macroeconomic News: Private Information about Public Announcements? (2019)
*Alexander Kurov, Alessio Sancetta, Georg Strasser, Marketa Halova Wolfe* · instruments: ES, 10-year Treasury note futures · access: open_pdf · testable on our data: partial

- **Why:** Adds a different WHY to the pre-FOMC drift we already know: informed traders and information leakage/proprietary data collection push futures prices before 08:30 ET releases (NFP, CPI etc.), so the early move can be traded in ES with a short time exit. Edge killers: tighter release security/lock-up procedures (the same authors' later paper 'Drift Begone!' shows drift disappears when procedures change) and faster algos pricing the leak. Decay risk is high: sample ends 2014; companion evidence from Kurov, Wolfe and Gilbert, 'The Disappearing Pre-FOMC Announcement Drift' (SSRN 3134546), shows the pre-FOMC drift essentially vanished after 2015, so this should be read together with it to avoid over-trusting old results. Treat as an event-study design to rebuild on ES 1-min with a hand-built release calendar.
- **Should contain:** Second-by-second E-mini S&P 500 and 10-year Treasury futures around 21-30 U.S. macro announcements (about 2003/2008-2014; versions differ on exact counts). Finds a pre-announcement drift in the 'correct' direction starting roughly 30 minutes before the release, accounting for about 40% (earlier version: half) of the total price adjustment, in only some announcements, with an estimated profit of about USD 20 million a year; explanations tested are leakage and proprietary data; stricter release procedures (e.g. PFEI guidelines) make the drift less likely. Testing the signal needs announcement surprises (consensus vs actual) and release times, which we do not have; a surprise-free version can only test ES volatility and the 30-minute run-up on release days.
- **Get it:** Free ECB working paper PDF: https://www.ecb.europa.eu/pub/pdf/scpwps/ecbwp1901.en.pdf . SSRN abstract page https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2637528 -> 'Download This Paper'. Journal DOI 10.1017/S0022109018000625. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2637528
- **Save as:** `papers/inbox/price_drift_before_u_s_macroeconomic_news_private_informatio.pdf`

### P2 · The Pre-FOMC Announcement Drift (2015)
*David O. Lucca, Emanuel Moench* · instruments: ES, S&P 500 · access: unknown · testable on our data: yes

- **Why:** S&P 500 rose a large share of its total return in the 24 hours before scheduled FOMC announcements. Later work (SSRN 'The Disappearing Pre-FOMC Announcement Drift') says it faded - test both on ES.
- **Should contain:** Return in the 24h before 14:00 ET FOMC releases, 1994-2011; needs a list of FOMC dates (public)
- **Get it:** NY Fed Staff Report 512 (free on newyorkfed.org) - search 'Lucca Moench pre-FOMC announcement drift staff report' https://libertystreeteconomics.newyorkfed.org/2012/07/the-puzzling-pre-fomc-announcement-drift
- **Save as:** `papers/inbox/the_pre_fomc_announcement_drift.pdf`

### P2 · The Unintended Consequences of Rebalancing (2026)
*Campbell R. Harvey, Michele G. Mazzoleni, Alessandro Melone* · instruments: ES, 10-year Treasury note futures · access: open_pdf · testable on our data: partial

- **Why:** Gives a modern, quantified WHY for month-end and quarter-end ES flows that is better than the generic 'turn of the month' story: institutional mandate/constraint (pension funds, target-date funds, balanced funds must rebalance to fixed weights on known schedules), so their trades are mechanical and predictable. Tradable idea: fade or front-run equity weakness after strong stock-vs-bond outperformance into month-end, long-only/short-only variants. Edge killers: funds randomising or smoothing rebalancing, front-runners (some pensions reportedly trade it themselves) crowding the trade. Decay risk: moderate; widely discussed by sell-side desks (month-end pension rebalance estimates) since before this paper. Needs a ZN (10-year note) series, which is not in our inventory, so mark data as partial.
- **Should contain:** Sample 1997-2023 using S&P 500 and 10-year Treasury note futures returns. 'Calendar' and 'Threshold' rebalancing signals built from a 60/40 portfolio drifting from target; when stocks are overweight, funds sell equities and buy bonds, and next-day equity returns fall by about 17 bps. Predictability concentrated around month-end, robust to momentum/reversal/macro controls, with Sharpe ratios for a front-running rule and robustness tables (including end-of-month reversal). Needs 10-year note futures/Treasury returns to build the stock-vs-bond signal; ES alone only lets us test the month-end calendar part.
- **Get it:** Free PDF (AFA conference copy): https://afajof.org/management/viewp.php?n=144452 . SSRN abstract page https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5122748 -> 'Download This Paper'. NBER version: https://www.nber.org/system/files/working_papers/w33554/w33554.pdf (may need a subscription). https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5122748
- **Save as:** `papers/inbox/the_unintended_consequences_of_rebalancing.pdf`

### P3 · Does Overnight News Explain Overnight Returns? (2025)
** · instruments: US stocks, index · access: open_pdf · testable on our data: partial

- **Why:** Tests whether news flow, rather than a risk premium, drives overnight returns - helps decide which WHY behind the overnight effect is real.
- **Should contain:** Overnight return decomposition by news vs no-news nights
- **Get it:** Free on arXiv https://arxiv.org/abs/2507.04481
- **Save as:** `papers/inbox/does_overnight_news_explain_overnight_returns.pdf`


## 3. Recommended research — Stocks

### P1 · A Profitable Day Trading Strategy For The U.S. Equity Market (2024)
*Carlo Zarattini, Andrea Barbon, Andrew Aziz* · instruments: - · access: ssrn_free_download · testable on our data: partial

- **Why:** Finding: ORB works far better when limited to stocks with unusually high volume, usually because of company news. WHY (Conti pattern 1, news digested slowly after the close): news piles up overnight and opening orders collide, so the imbalance carries through the day. Heavy relative volume marks the stocks where that imbalance is largest. What would kill it: institutions allowed to trade pre-market, or a fast-moving price discovery process at the open. Decay risk: published 2024 and sits on the retail ORB bandwagon, so check the post-2023 half. Angle for us: the single-stock data is missing, but the 'abnormal volume at the open' filter can be tested as a conditioning variable on ES opening-range breakouts (first-30-minute volume vs a 20-day average) as a proxy for 'index in play'.
- **Should contain:** 5-minute ORB tested on 7,000+ US stocks, 2016-2023. Net performance, Sharpe and alpha for portfolios of the top-N Stocks in Play, ranked by relative volume at the open. ORB variants on 15/30/60-minute ranges. Per-stock best/worst tables. Transaction-cost assumptions. 1R-style stop based on a per-share loss. Reported result: top-20 portfolio, Sharpe about 2.8, net return above 1,600%.
- **Get it:** Open the SSRN abstract page (abstract_id=4729284) and click 'Download This Paper'. Free, no login needed for the PDF. Backup copies: the Concretum Group papers page (concretumgroup.com/papers/, 'Download PDF') or the PDF mirror at tradewithpat.com. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4729284
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

### P1 · Intraday Patterns in the Cross-section of Stock Returns (2010)
*Steven L. Heston, Robert A. Korajczyk, Ronnie Sadka* · instruments: - · access: open_pdf · testable on our data: partial

- **Why:** Finding: a stock's return in a given half hour predicts its return in the same half hour on following days, for about two months. WHY (Conti pattern 'liquidity constraints on large orders / execution mechanics'): big funds split a parent order over many days and trade at similar times of day, so flow is persistent and predictable. What would kill it: faster, randomized execution algorithms (VWAP/TWAP with randomization, dark pools), and lower trading costs. Decay risk: published 2010, and algorithmic execution has changed a lot since, so the out-of-sample half matters. Angle: apply to ES/NQ time-of-day returns, plus use it as a timing guide for entries.
- **Should contain:** Cross-sectional regressions of each stock's half-hour return on its own past returns at lags that are exact multiples of one trading day. Result: continuation that lasts about 40 trading days, stronger in the first and last half-hours, and not explained by volume, spreads or the Keim (1989) bid-ask effect. Separate result: short-term reversal is driven by temporary liquidity imbalances lasting under an hour. Stock-level intraday data needed, but the time-of-day structure can be partly tested on ES 1-minute bars (same half-hour of yesterday predicting today's same half-hour) 2013-2026.
- **Get it:** Free: arXiv abs/1005.3535 ('View PDF'). Also on SSRN abstract 1107590 ('Download This Paper') and on the University of Houston Bauer site (PDF). https://arxiv.org/abs/1005.3535
- **Save as:** `papers/inbox/intraday_patterns_in_the_cross_section_of_stock_returns.pdf`

### P1 · The Disappearing Index Effect (2022)
*Robin Greenwood, Marco Sammon* · instruments: - · access: open_pdf · testable on our data: no

- **Why:** Finding: the S&P 500 inclusion pop has declined sharply and is close to zero on average. The effect survives only where the net demand shock is still large (direct additions, large weights). WHY (Conti pattern 'institutional constraint / mandate' plus 'liquidity constraint on large orders'): index funds must buy on the effective date, but liquidity providers and front-runners now absorb the flow in advance. That tells us exactly what to test: condition on the size of net passive demand. What would kill it: front-running capacity, midcap-fund offsets, and rule changes in S&P announcement timing. Decay risk: already high, and the paper documents it. Use as a template for deciding which forced-flow edges are still alive. Single-stock and event-date data not in our inventory.
- **Should contain:** S&P 500 addition/deletion abnormal returns from 1980 to 2020, by decade (about 10% in the mid-1990s falling to near zero). Split between 'migrations' from S&P MidCap and direct additions (direct additions about 5.4% vs migrations about -1.8% in the 2010s). Passive-fund net demand, evidence on front-running and shrinking trading costs, and a short section on Russell index changes (weaker, not significant). Data: S&P addition/deletion dates (Siblis), CRSP, fund holdings.
- **Get it:** Free PDF on the HBS research page (hbs.edu/ris/download.aspx?name=ssrn-4294297.pdf), or the NBER version w30748 (nber.org/system/files/working_papers/w30748/w30748.pdf), or SSRN abstract 4294297 with 'Download This Paper'. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4294297
- **Save as:** `papers/inbox/the_disappearing_index_effect.pdf`

### P1 · The Earnings Announcement Premium and Trading Volume (2007)
*Andrea Frazzini, Owen A. Lamont* · instruments: - · access: ssrn_free_download · testable on our data: no

- **Why:** Finding: stocks earn an abnormal return around scheduled earnings dates, strongly tied to volume surges. WHY: attention-driven retail buying. The announcement draws small investors, who are net buyers of attention-grabbing stocks, and the order flow is predictable because the dates are known in advance. That fits the 'someone is predictably forced or likely to trade' test. What would kill it: retail attention shifting away from earnings dates, or arbitrage capital pre-positioning earlier and earlier. Decay risk: published 2007 and widely known (also shown in 46 countries by Barber et al., SSRN 1872183, a good follow-up for the Europe angle). Angle: long-only, buy about 5-10 days before the known earnings date and exit before or at the print, avoiding the surprise risk. Needs earnings dates and single-stock prices, which we do not have.
- **Should contain:** Stocks rise on average around scheduled earnings dates. Calendar-time portfolio returns for stocks in or out of their predicted announcement month. Volume surges around announcement dates. Link between high past announcement-period volume and the highest premium. Imputed small-investor buying (from trade size). Needs CRSP, earnings dates (Compustat/IBES) and trade-size data.
- **Get it:** SSRN abstract page abstract_id=986940, click 'Download This Paper'. The NBER version is Working Paper w13090 on nber.org, usually a free PDF there too. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=986940
- **Save as:** `papers/inbox/the_earnings_announcement_premium_and_trading_volume.pdf`

### P2 · Decoding Inside Information (2012)
*Lauren Cohen, Christopher J. Malloy, Lukasz Pomorski* · instruments: - · access: open_pdf · testable on our data: no

- **Why:** Finding: almost all the predictive power of insider trades sits in the irregular, 'opportunistic' trades, mostly purchases. WHY (slow information diffusion): insiders know about upcoming news, they must report with a lag, and the market under-weights a signal that is hidden among routine trades. What would kill it: more attention on Form 4 filings (already automated screens), or insiders shifting to less visible trading. Decay risk: published 2012 and since widely replicated in commercial insider-trading screens; a robustness check by independent users gave mixed results. Angle: long-only, small and mid caps, cluster of buys by several insiders, hold 20-60 days with a time exit. Needs single stocks and insider filing data, so 'no' on our data.
- **Should contain:** Classification of insiders as 'routine' (same calendar-month trades year after year) or 'opportunistic'. Calendar-time portfolios, 1989-2007: opportunistic trades earned about 82 bp/month value-weighted abnormal return and routine trades roughly zero. Fama-MacBeth regressions on the number of opportunistic buys/sells in a firm-month. Evidence that opportunistic trades predict later news at the firm. Data: Thomson Reuters insider filings (Form 4), CRSP.
- **Get it:** Free NBER PDF (nber.org/system/files/working_papers/w16454/w16454.pdf) or SSRN abstract 1692517 with 'Download This Paper'. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1692517
- **Save as:** `papers/inbox/decoding_inside_information.pdf`

### P2 · The 52-Week High and Momentum Investing (2004)
*Thomas J. George, Chuan-Yang Hwang* · instruments: US stocks · access: unknown · testable on our data: partial

- **Why:** Stocks near their 52-week high keep outperforming. WHY: traders anchor on the 52-week high and under-react to good news near it. Also tested on index level in later work.
- **Should contain:** Ranking by price / 52-week high, holding periods, comparison with classic momentum.
- **Get it:** Free PDF copy: http://basehitinvesting.com/wp-content/uploads/2013/01/52-Week-High-and-Momentum-Investing.pdf (the Alpha Architect page is only a blog summary). Journal of Finance 2004, George & Hwang.
- **Save as:** `papers/inbox/the_52_week_high_and_momentum_investing.pdf`

### P2 · The Russell Reconstitution Effect (2001)
** · instruments: Russell 2000 stocks · access: ssrn_free_download · testable on our data: no

- **Why:** Index funds must trade every addition/deletion on reconstitution day, creating order imbalances and price pressure. The 2007 follow-up says the effect has weakened - check what survives.
- **Should contain:** Abnormal returns from rank day to reconstitution day for additions vs deletions; reversal afterwards. Needs Russell membership lists.
- **Get it:** SSRN abstract 278000; follow-up 'Russell Reconstitution Effect Revisited' is SSRN 960727 https://papers.ssrn.com/sol3/papers.cfm?abstract_id=278000
- **Save as:** `papers/inbox/the_russell_reconstitution_effect.pdf`

### P2 · Understanding Returns to Short Selling Using Option-Implied Stock Borrowing Fees (Is There a Risk Premium in the Stock Lending Market? Evidence from Equity Options) (2017)
*Dmitriy Muravyev, Neil D. Pearson, Joshua M. Pollet* · instruments: - · access: open_pdf · testable on our data: no

- **Why:** Finding: short-interest and borrow-based signals predict poor returns, but after borrow costs most of the edge is gone, and what remains is predicted by option-implied fees. WHY (Conti pattern 'risk premium / constraint'): short sales are limited by lending supply, so overpricing persists only where borrowing is costly or scarce, and borrow fee is the price of that constraint. What would kill it: more lendable supply, lower fees, or short-sale restrictions being lifted. Decay risk: moderate; the finding is about cost, not a new signal. Angle: long-only tests (avoid heavily shorted stocks) or squeeze-risk filters avoid paying fees. Data needed is outside our inventory, so 'no'.
- **Should contain:** Portfolio sorts on short interest, lending supply, utilization and borrow fees. Result: returns to short selling net of borrowing costs are less than one-third of the gross returns and not significant. Option-implied borrowing fee (from put-call parity) equals quoted fee on average, and predicts returns at 1-week and 1-month horizons, including in hard-to-borrow stocks. Needs data: stock-lending data (Markit/IHS), OptionMetrics, CRSP.
- **Get it:** Free PDFs: the UNC finance site (jhfinance.web.unc.edu ... 2017JH_MuravyevPearsonPollet.pdf) or the AEA 2018 conference program page for the 'Understanding Returns to Short Selling Using Option-Implied Stock Borrowing Fees' draft. Search the title on SSRN for the latest version. https://www.aeaweb.org/conference/2018/preliminary/paper/EKFHFi58
- **Save as:** `papers/inbox/understanding_returns_to_short_selling_using_option_implied.pdf`

