# Reading list — papers to download

Updated 2026-10-19. Download each PDF and save it in `papers/inbox/` **using the file name shown** (or attach it in chat). The next run reads the full paper and replaces the partial summary.

## 1. Couldn't get the full text — please download

Nothing pending.

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

### P2 · The Pre-FOMC Announcement Drift (2015)
*David O. Lucca, Emanuel Moench* · instruments: ES, S&P 500 · access: unknown · testable on our data: yes

- **Why:** S&P 500 rose a large share of its total return in the 24 hours before scheduled FOMC announcements. Later work (SSRN 'The Disappearing Pre-FOMC Announcement Drift') says it faded - test both on ES.
- **Should contain:** Return in the 24h before 14:00 ET FOMC releases, 1994-2011; needs a list of FOMC dates (public)
- **Get it:** NY Fed Staff Report 512 (free on newyorkfed.org) - search 'Lucca Moench pre-FOMC announcement drift staff report' https://libertystreeteconomics.newyorkfed.org/2012/07/the-puzzling-pre-fomc-announcement-drift
- **Save as:** `papers/inbox/the_pre_fomc_announcement_drift.pdf`

### P3 · Does Overnight News Explain Overnight Returns? (2025)
** · instruments: US stocks, index · access: open_pdf · testable on our data: partial

- **Why:** Tests whether news flow, rather than a risk premium, drives overnight returns - helps decide which WHY behind the overnight effect is real.
- **Should contain:** Overnight return decomposition by news vs no-news nights
- **Get it:** Free on arXiv https://arxiv.org/abs/2507.04481
- **Save as:** `papers/inbox/does_overnight_news_explain_overnight_returns.pdf`


## 3. Recommended research — Stocks

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

### P2 · The 52-Week High and Momentum Investing (2004)
*Thomas J. George, Chuan-Yang Hwang* · instruments: US stocks · access: unknown · testable on our data: partial

- **Why:** Stocks near their 52-week high keep outperforming. WHY: traders anchor on the 52-week high and under-react to good news near it. Also tested on index level in later work.
- **Should contain:** Ranking by price / 52-week high, holding periods, comparison with classic momentum.
- **Get it:** Journal of Finance 2004; search the title on Google Scholar for a free author copy https://alphaarchitect.com/the-secret-to-momentum-is-the-52-week-high/
- **Save as:** `papers/inbox/the_52_week_high_and_momentum_investing.pdf`

### P2 · The Russell Reconstitution Effect (2001)
** · instruments: Russell 2000 stocks · access: ssrn_free_download · testable on our data: no

- **Why:** Index funds must trade every addition/deletion on reconstitution day, creating order imbalances and price pressure. The 2007 follow-up says the effect has weakened - check what survives.
- **Should contain:** Abnormal returns from rank day to reconstitution day for additions vs deletions; reversal afterwards. Needs Russell membership lists.
- **Get it:** SSRN abstract 278000; follow-up 'Russell Reconstitution Effect Revisited' is SSRN 960727 https://papers.ssrn.com/sol3/papers.cfm?abstract_id=278000
- **Save as:** `papers/inbox/the_russell_reconstitution_effect.pdf`

