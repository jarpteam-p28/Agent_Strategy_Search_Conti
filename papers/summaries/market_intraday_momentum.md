# Market Intraday Momentum

**Authors:** Lei Gao, Yufeng Han, Sophia Zhengzi Li, Guofu Zhou  
**Year:** 2018  **Type:** academic  **Read:** full_pdf  
**Source:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2440866

> The return from the prior close to 10:00 ET (and, to a lesser extent, the 15:00–15:30 half-hour) predicts the direction of the last half-hour (15:30–16:00) return in SPY and ten other ETFs. The effect is much stronger on volatile, high-volume, recession and news days.

## Findings
- The first half-hour return (prior close to 10:00 ET, so it includes the overnight gap) positively predicts the last half-hour return of SPY. Sample: Feb 1993 to Dec 2013, TAQ data, 13 half-hour bars per day. — *Slope 6.94 (x100), Newey-West t = 4.08, R² = 1.6%. Out-of-sample recursive R² = 1.4% (start 1998).*
- The twelfth half-hour (15:00–15:30) return is an independent second predictor. Combining the two gives R² 2.6% in-sample and 2.0% out-of-sample. The r12 effect is less stable: it is mostly driven by the 2008 crisis and is not significant in the pre-crisis and post-crisis subsamples alone. The r1 effect is the robust one. — *r12 slope 11.8, t = 2.62; joint R² 2.6%. Table 13: in a regression on all 12 half-hours, only r1 and r12 are consistently significant for SPY.*
- Simple timing rule: go long at 15:30 if r1 > 0, short if r1 <= 0, and exit at the close. It beats the buy-and-hold and 'always long last 30 min' benchmarks while being in the market only 30 minutes a day. — *Avg return 6.67%/yr, std 6.19%, Sharpe 1.08, skew 0.90, success rate 54.4%. 'Always long last half-hour' gave -1.11%/yr and buy-and-hold had Sharpe 0.29. Trading only when r1 and r12 agree gives a 77% success rate but a lower return (4.39%/yr) because it is in the market less often.*
- The predictability is stronger when volatility or volume is high, in recessions and on macro news days. In low-volatility days the r1 coefficient is not significant. — *R² by first-half-hour volatility tercile: 0.6% / 1.0% / 3.3%. Expansion R² 1.0% vs recession 6.6%. Crisis period (Dec 2007–Jun 2009) R² 6.9%, but 1.1% excluding the crisis. Timing return on FOMC-minutes release days was 20.0%/yr vs 6.2% on other days; MCSI 19.1%, CPI 18.0%, GDP 14.4% on release days.*
- The effect survives bid-ask costs and is not specific to SPY. It appears in ten other liquid ETFs and is often larger in less liquid ones. — *After costs: 4.46%/yr post-2001 and 6.52%/yr post-2005 (spread about 1.2bp). Out-of-sample R² for r1 alone ranges from 0.70% (QQQ) to 6.53% (EEM). CER gains reach 17.7%/yr for FXI, and IYR, XLF, IWM, EEM and VWO are all above 10%. TLT also shows it. The paper says SPX futures give similar results (internet appendix).*
- Results by liquidity and institutional ownership. The r1 effect is similar across liquid and illiquid stocks and across high and low institutional ownership. The r12 effect is stronger in illiquid stocks, stocks with high institutional ownership, and days with high institutional order imbalance. Momentum is weaker in the T-3 to T+3 month-end window. — *Amihud-sorted portfolios: r1 slope about 7.3 vs 7.7, but r12 slope 12.3 vs 27.0. Low-ownership r1 slope 9.7 vs high-ownership 6.3.*

## The WHY
**Pattern:** Information arrives while the market is closed, and is digested slowly once it opens (overnight news and the opening gap), combined with Institutional constraint / close-oriented execution (late rebalancing and late-informed flows at the close).

Most earnings and macro news come out before the open, so the first 30 minutes (prior close to 10:00) contain the overnight information shock. Some participants cannot or do not trade in the first 30 minutes: slow-moving or infrequently rebalancing institutions, late-informed or slow-processing investors, and mutual fund flows that are priced at the close. They trade in the same direction in the last half-hour, which is the second most liquid period. Market makers also want to unload inventory before the overnight session. Those late flows push the close in the direction of the morning move. The authors cite Bogousslavsky (2016) on infrequent rebalancing and a late-informed-trader model.

- **Who is forced / predictable:** Mutual funds, index and benchmark-tracking funds, and other institutions whose performance is marked at the closing price. These participants are pushed into the close by mandate, NAV and settlement timing, and by the wish to avoid overnight risk. They split orders across the day (rebalancing delays). Market makers also unwind inventory before the close, and slow-information investors wait for the high-liquidity close.
- **Why it persists:** It rests on structural features of how institutions trade: NAV is struck at the close, execution is spread out, rebalancing is infrequent, and the close is a liquidity magnet. None of these are arbitraged away by faster traders because the late flow is mandated, not discretionary. The stronger effect on volatile days, news days and recessions fits more dispersed, slower digestion of larger shocks and harder arbitrage when liquidity is thin.
- **What would kill it:** Participants would need to move their rebalancing or execution into the morning (for example, all-day or open-weighted algos replacing close-targeted ones). The effect would also fade if the close became less central (no NAV or benchmark marking at the close), or if enough capital front-runs the last-half-hour order flow (many traders already trade this signal). The authors' own explanations (infrequent rebalancing, late-informed traders) are theoretical and untested here; the paper has no direct data on who trades in the last half-hour (ANcerno timestamps were unreliable). Treat the WHY as plausible but not proven.
- **Paper's view vs ours:** The authors offer two models (infrequent rebalancing and late-informed trading) and admit there are probably others. They cannot identify who trades, because the ANcerno timestamps are unreliable. Our added angle is the close-targeted execution mechanics of big players: end-of-day marking and NAV, and market-maker inventory unwinds. This predicts the effect is stronger when more institutional flow is in play (high volume, FOMC days), and the data agree. The paper's weak spot is that the sample ends in 2013 and says nothing about post-publication decay, which also matters because the large 2008 crisis drives part of the r12 effect.

## Setting
- Markets: US equities (ETFs)
- Instruments: SPY (S&P 500 ETF), QQQ, DIA, IWM, XLF, IYR, EEM, FXI, EFA, VWO, TLT
- Period: Feb 1993 to Dec 2013 (SPY); each other ETF from inception to Dec 2013  Frequency: Intraday trade prices (TAQ), aggregated to 13 half-hour returns per day; first-half-hour volatility from 1-minute returns  Holding: 30 minutes (15:30 to 16:00 ET), one trade per day

## Reported results
Sign-of-first-half-hour timing strategy on SPY earned 6.67%/yr (Sharpe 1.08) by holding only the last 30 minutes of each day, versus Sharpe 0.29 for buy-and-hold and -1.11%/yr for 'always long last half-hour'. After bid-ask costs it still earned 4.46%/yr (post-2001) and 6.52%/yr (post-2005).
- In-sample R² 1.6% (r1), 2.6% (r1 + r12); out-of-sample R² 1.4% and 2.0%
- Timing return 6.67%/yr, std 6.19%, Sharpe 1.08, skew 0.90, kurtosis 15.65, success rate 54.37%
- Joint r1/r12 rule: 4.39%/yr, Sharpe 0.98, success rate 77.05%, in the market only part of the time
- Utility CER gain 6.02%/yr (r1) and 6.18%/yr (r1+r12) for a mean-variance investor (risk aversion 5)
- FOMC-minutes days: R² 11.0%, timing return 20.04%/yr; recession R² 6.6%; high-volatility tercile R² 3.3%
- Other ETFs: out-of-sample R² 0.70% (QQQ) to 6.53% (EEM); CER up to 17.71%/yr (FXI)
- Costs: Bid-ask spread only (long at ask, short at bid at 15:30; exit at the closing auction price with no spread). Commissions ignored. After July 2001 and again after Jan 2005 only.

## Tradable edge (our framing)
Each day, read the direction of the market from the prior close (including the overnight gap) to 10:00 ET. Take that direction through the final half-hour of the session (enter around 15:30 ET, exit at or just before the close), because late institutional rebalancing and close-oriented flows tend to push the close the same way. Treat it as a one-sided-per-day, 30-minute holding trade on index futures. Make the position bigger or only take trades when conditions favour the effect: high first-half-hour volatility or volume, and scheduled macro-news days (especially FOMC), where the paper's gains were three to four times larger. Optionally require the 15:00–15:30 return to agree with the morning direction (higher win rate, fewer trades). Use volatility targeting for live size, and judge the signal against the 'always long last 30 minutes' baseline rather than against zero.

## Angles to test
- Different instrument: ES first (our data), then NQ (tick data from 2021 only; partial), and later YM, RTY and TLT/bond futures if we get the data. The paper found it in IWM, EEM, FXI and IYR (stronger in less liquid ETFs), so Russell 2000 futures (RTY) or emerging-market proxies may be stronger than ES.
- Filter by regime: only trade on high first-half-hour volatility (top tercile) or high volume days, and on FOMC, CPI, GDP and Michigan sentiment release days; test whether skipping low-volatility days improves expectancy per trade (paper: low-vol days R² 0.6%, r1 not significant).
- Conti 'different session' angle: test the same logic with other windows (e.g. overnight-session open to US open, or first hour to last hour) and with the first-half-hour measured from the Globex open instead of the prior RTH close.
- Combine with the r12 signal: take trades only if r1 and r12 agree (higher win rate, fewer trades, good for prop-firm style challenges), or size up when both agree. Combine with overnight drift or ORB signals as a separate, low-correlation sleeve.
- One side only: test long-only (buy last 30 minutes when the morning was up) vs short-only, because breakdowns may be absorbed differently. Test the effect of skipping month-end days (T-3 to T+3), where the paper found it weaker.
- Test exit variations: a fixed time exit at 15:55 or 16:00 ET vs 16:15 for futures settlement; a time-only exit is the paper's design, so keep it as the baseline and test stops only as an add-on.
- Use it as a prop-firm challenge component: high-frequency (every day), small stops, and low correlation to the VWAP-pullback and overnight-bias strategies; run the daily-P&L bootstrap from the method notes.

## Decay risk: medium
The paper has circulated since 2014 (SSRN first draft; published version in the Journal of Financial Economics, 2018) and has several thousand downloads, so it is well known. The signal is a tiny edge (about 6–7%/yr gross, around 4.5–6.5% after costs on a ~1bp spread asset) that was strongest in 2008 and weaker in calm periods. The WHY (close-targeted institutional flow) is structural, so it may persist in a weaker form, but out-of-sample strength after 2013 is untested here and must be checked with our own data. Later replications are mixed in strength.

## Data fit
Good for ES. We have ES 1-minute bars from 2013-12-08 to 2026-09-02 (ETH and RTH, UTC timestamps). This covers 2014 to 2026, which is entirely after the paper's 1993–2013 sample, so it is a clean out-of-sample test of publication decay. We can compute r1 (prior 16:00 ET close, or the 15:59 ET bar close, to 10:00 ET), r12 (15:00–15:30 ET), first-half-hour realized volatility from 1-minute bars, and the 15:30–16:00 return. Need to handle UTC to ET conversion with daylight-saving changes, and the ES RTH close at 16:00 ET (futures close at 16:00 vs. the 16:15 index cash close detail; use consistent bars). NQ is only available as tick data from mid-2021 to 2026 with gaps and no continuous series, so NQ testing is partial. Missing: macro-news release calendars (FOMC minutes, CPI, GDP, Michigan sentiment) would have to be sourced separately, though FOMC and CPI dates are public and easy to hand-build. No ETF data (SPY, IWM, TLT, EEM etc.), no other futures (YM, RTY, CL, GC), and no stock data. Split: develop on about 2014–2022 (80%), freeze and test on the remaining 20%. Check 2022 and other down years, since the strategy is long and short and should have little beta.

## Caveats
- The paper's trades are SPY with ~1bp spread and no commission; futures costs (about $13+ round turn for NQ, ~$5-10 for ES plus slippage) matter for a trade that earns a few bp on average. Need to check net expectancy per contract.
- A large share of the predictability comes from 2008–2009 (R² 6.9% in the crisis vs 1.1% outside). The out-of-sample window in the paper (starting 1998) includes the crisis. Performance in calm regimes is much weaker (about 0.8% R² for r1).
- The signal is a regression with R² of 1–3%; the edge per trade is small and the return distribution is fat-tailed (kurtosis 15–60) with positive skew. Outlier dependence may mean you must take every signal.
- Sample ends December 2013; it says nothing about decay after publication. Our 2014–2026 ES data will answer that.
- The first half-hour return in the paper is prior close (16:00) to 10:00 ET, so it includes the overnight gap. A version that measures only 09:30–10:00 would be a different signal. ES trades overnight, so the 'prior close' is the 16:00 ET RTH close or the 16:15 futures cash-index convention; define it exactly.
- Statistical results use Newey-West t-stats on overlapping, annualized daily returns; Sharpe ratios reflect only the time in the market (30 minutes), so annualized return is not comparable to a full-day strategy; it uses daily-notional exposure of 100%.
- The mean-variance utility results use leverage between -0.5 and 1.5 and are not directly tradable rules; the market timing sign rule is the simplest tradable form.
- Explanations are theoretical; the paper has no direct evidence on who creates the last-half-hour flow.

## Cited papers worth reading
- Infrequent Rebalancing, Return Autocorrelation, and Seasonality (2016)
- Intraday Patterns in the Cross-Section of Stock Returns (2010)
- The Pre-FOMC Announcement Drift (2015)
- A Tug of War: Overnight Versus Intraday Expected Returns (2019)
- Dash for Cash: Month-End Liquidity Needs and the Predictability of Stock Returns (2016)
