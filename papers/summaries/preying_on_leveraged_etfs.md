# Preying on Leveraged ETFs

**Authors:** Yinhong Zhao  
**Year:** 2026  **Type:** academic  **Read:** full_pdf  
**Source:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7229918

> When leveraged-ETF rebalancing is large relative to the closing auction that clears it, the close overshoots overnight news and about 75% of the first-day move reverses by the next close, in a damped oscillation over several days (shown only for Samsung and SK Hynix after the May 2026 Korean launch).

## Findings
- Leveraged ETFs must trade A(L²−L)r into the close in the direction of the day's move. This holds for inverse funds too, so long and inverse funds add up. The order is predictable, cannot be postponed, and is sized by the closing price it moves, so demand slopes upward. — *Equation (1). Worked example: SK Hynix −9.9% on 5 Jun 2026 forced a KRW 4.3tn sale, 36% of daily volume, into a window that normally trades about 10% of the day's value.*
- A single 'loop gain' ℓ = (closing-auction price impact) × (total rebalancing capital of all leveraged products on the stock) decides whether the effect appears. Korean SK Hynix (avg 0.51–0.58) and Samsung (0.22–0.25) are far above US index complexes. MicroStrategy (0.22) is the US outlier; other US single stocks sit at 0.03–0.10. — *Figure 3. Worldwide mandated rebalance in SK Hynix averaged 22.4% of daily traded value, peaking at 50.4%.*
- In treated Korean stocks after launch, the next-day close-to-close return loads negatively on the pre-open US return (SMH/QQQ/SPY). About 80%/75%/68% of the first-day news response reverses by the next close; 32–45% of it comes overnight. The response then oscillates and is back near its first-day level by day 3. — *Table 1 triple differences −0.79, −1.55, −2.29 (p<0.01), only 82 treated-post stock-days (two stocks, about 41 days each). No reversal in any control cell: US index and single-stock complexes (incl. NVDA, AMD), pre-launch treated, other Korean stocks (Tables A4, A8).*
- The overshoot is already in the price at the open and stays flat through the session. The closing auction adds nothing. The mandated order's impact is therefore front-loaded by speculators who pre-position, not delivered at the close. — *Figure 4(a); Table A2 auction-leg loading −0.03; calibrated session share of overshoot S≈0.93.*
- The reversal scales with shock size (large-shock days −0.81, small-shock days null) and is stronger after down-shocks. Retail was a dip-buyer (net purchase vs fund return −0.30), so the cause is not retail momentum. — *Table A6, Table A7. The up/down sign difference is only partly significant (z 1.17 SMH, 2.48 QQQ).*
- News-conditional volatility rose after launch, and annualised vol was 136.7% for SK Hynix against a model counterfactual of 100%. The model attributes about KRW 1.4tn (17.6% of initial investment per unit) of transfer from LETF holders to counterparties over nine weeks. Pre-positioning accounts for roughly a quarter of the overshoot. — *Section 5.2, Fig 5 (pre-launch parallel trends p=0.78 and 0.71). Counterfactual and welfare numbers are model-derived and weakly identified (arbitrage-capacity scale spans a very wide range; reversal share CI [0.17,1.32]).*
- Policy counterfactuals: dispersing the rebalance across the day backfires, and a two-auction rebalance (open and close), flexible leverage with a capacity cap, and a 3-day moving-average reference price all reduce losses. — *Tables 3-5. Averaging prices over 3 days cuts the holder loss to KRW 237bn from 1,380bn.*

## The WHY
**Pattern:** Execution mechanics of big players, combined with a liquidity constraint on large orders. The mandated, price-insensitive closing rebalance is a known demand curve; speculators front-run it (the paper calls this predatory), and the displacement reverses once outside capital arrives overnight. It also has an information-arrives-while-closed flavour, because the US session closes before Korea opens.

Overnight US news fixes most of the day's LETF rebalance size, and anyone can compute the closing order from the current price. Speculators buy or sell at the open in the direction of the news, which pushes the open and the close beyond fundamental value. The fund then buys high or sells low at the reference close, and its larger order is sized on the overshot price (the feedback loop). Deeper capital corrects the error overnight, so the next day gives back most of the move and rebounds again in a damped oscillation. Each atomistic speculator is rational and none manipulates; the effect is non-linear in loop gain and only bites when the complex is large relative to the auction depth.

- **Who is forced / predictable:** LETF managers and swap counterparties must trade A(L²−L)r at the reference close; they are contractually inelastic and cannot delay or resize. Retail LETF holders (92% of holders) bear the cost. Market makers and speculators are not forced. They are the predictable side, paid for warehousing overnight risk.
- **Why it persists:** The prospectus-mandated daily reset is structural. The effect only needs a big complex relative to venue depth, and Korean complexes grew by leveraged compounding (63% of SK Hynix's growth). Regulatory fixes proposed so far (dispersing the trades, flexible multiple) either backfire or are partial.
- **What would kill it:** Regulators or issuers move to a two-auction rebalance, a multi-day averaged reference, a capacity cap on the order, or a flexible multiple. Funds shrink through outflows or the listing freeze, so loop gain falls below the oscillation threshold. Speculators crowd the pre-position and compress the overshoot. Dispersing trades only moves timing, so on its own it will not kill the effect.
- **Paper's view vs ours:** The authors frame it as predatory trading, but they say themselves that the behaviour cannot be told apart from benign liquidity provision or an intraday momentum trade. The tradable content is simpler: a known inelastic closing flow plus overnight news produces an overshoot that reverses the next day. The causal identification rests on two treated stocks and one launch, about 82 treated-post observations over roughly 9 weeks. The welfare and counterfactual numbers depend on a weakly identified calibration, and the paper's own appendix says as much. A paper dated August 2026 and written with AI-assisted coding should be treated as preliminary.

## Setting
- Markets: Korea (KOSPI), US (comparison cells)
- Instruments: Samsung Electronics, SK Hynix, 10 Korean large-cap controls, 10 Korean tech peers, US single stocks with 2x ETFs (MSTR, NVDA, TSLA, PLTR, AMD), US index complexes (S&P 500, Nasdaq-100)
- Period: Daily panel Jan 2024 – Jul 2026; 1-min KRX data May–Jul 2026 (61 cash days); launch 27 May 2026  Frequency: Daily panel plus 1-min intraday and auction data  Holding: Close-to-close next day (reversal over days 1-3)

## Reported results
After the May 2026 Korean LETF launch, treated stocks reverse about 75% of the first-day response to pre-open US news by the next close. Model attributes 36.7 pp of SK Hynix annualised volatility (136.7% vs 100.0%) and KRW 1.38tn (17.6% of initial investment) of holder losses to the mechanism.
- Triple-difference next-day loading: −0.79 (SMH), −1.55 (QQQ), −2.29 (SPY), all p<0.01; treated-post cell has only 82 observations
- Overshoot factor Πg=1.66 (CI 0.84–3.27); measured loop gain SK Hynix 0.58, Samsung 0.22
- Closing-return autocorrelation −0.16 (SK Hynix), −0.08 (Samsung); pre-launch ~0
- Closing-auction share of futures traded value rose from 0.3% to 1.4%; cash-side share 7.3% to 9.8%
- Policy: 3-day averaged reference cuts holder loss from KRW 1,380bn to 237bn; 2-auction rebalance to about 592bn; staggered intraday prints worsen it (vol 146.9–155.7%)
- Costs: No trading strategy is backtested, so no transaction costs. This is an event-study and structural-model paper. The holder-loss figures include futures-leg execution cost on an assumed impact curve.

## Tradable edge (our framing)
Where one mandated, price-insensitive closing rebalance is large relative to what the closing auction can absorb, the stock overshoots overnight news (pre-open foreign market moves) from the open, and about two-thirds to three-quarters of that overshoot reverses by the next close, partly overnight. For us the idea is to fade, next day, a large pre-open news move in a name or product whose closing-flow pressure is abnormally large. The Korean stocks are not in our data. The mechanism is only testable in a diluted form on index futures, where the scale is much smaller and the paper's own evidence says reversal is null at US-index loop gains (0.03-0.10). Treat this mostly as a regime-monitoring signal. The strategy only exists where a fund complex such as a leveraged ETF is big against venue depth, in effect single-stock or thematic products. A direct conversion to ES/NQ futures is likely to find nothing.

## Angles to test
- Other instruments: US single stocks and ETFs with extreme leveraged-ETF AUM relative to closing-auction volume, for example MicroStrategy (loop gain 0.22), Tesla, and Nvidia, which was null in the paper. Needs stock data we lack.
- Other universes: Hong Kong, Taiwan and Japan products referencing a single domestic stock. Also any new single-stock leveraged ETF launches in Europe, where closing-auction depth is thinner.
- Different session: test whether the open-to-close move after large overnight (US-close to Asia-open) gaps is followed by a next-day reversal, on index futures only. Prior: null in the paper at US index loop gains, so a falsification test.
- Scheduled-flow framing on ES/NQ 1-min data: compute K×return, the implied late-day mandated flow, and test last-30-min and next-day continuation or reversal. Report pre/post-2022 and by size of the day's move, per our regime notes. Expect small effects.
- One side only: the paper finds the reversal stronger after down-shock days, so test long-only buys after large down-gaps.
- Combine with a vol-management lens: the paper's loop-gain idea generalises to other mandated flows such as volatility-targeting funds, portfolio insurers and 0DTE dealer hedging (compare the gamma exposure study already in our notes).
- Use as a risk filter: when a leveraged-ETF complex is huge, expect higher next-day |return| per unit of overnight news (the news-conditional vol result).

## Decay risk: high
Published August 2026, one episode (Korea, 9 weeks), and the regulators already acted: a listing freeze on 16 July, the Hong Kong flexible multiple, and the Korean guidance on dispersing rebalancing. Authors themselves note the effect is nonlinear and absent at US scale. Under McLean-Pontiff post-publication shrinkage, plan for the effect to be smaller than reported even if it persists.

## Data fit
Poor. The core tests need Korean single-stock closing-auction data, leveraged-ETF AUM, and intraday quotes, none of which we hold. We have ES (2013-2026) and NQ (2021-2026) 1-min and tick data, so we can only run a diluted test. At US index loop gains (0.03–0.10 in the paper), reversal is null, so this would mostly be a falsification test. Missing: leveraged-ETF AUM and leverage multiples (to compute K), the US-close to Asia-open overnight shock for Korean names, single stocks, and the Korean futures. Futures roll and the 15:45 index-futures close add complications. NQ before mid-2021 is not available.

## Caveats
- Single episode, two treated stocks, one launch date, about 82 treated-post stock-days over roughly 9 weeks; clustered standard errors are unreliable with two treated units, and the paper leans on randomization inference.
- Confounded with a massive AI-memory bull-then-crash regime and market-wide circuit breakers; the paper says the LETFs mainly changed the path, not the destination, of the decline.
- Loop gain and the structural calibration are only weakly identified: the arbitrage-capacity scale τ ranges from 1,605 to 4e5 in the bootstrap, the reversal share CI is [0.17, 1.32], and the model reversal share (0.31) is below the data (0.75). The paper itself calls the loop gain an upper bound.
- The Samsung overshoot is not distinguishable from SK Hynix (data 1.75 vs 1.60), but the model predicts 1.18 for Samsung.
- Welfare transfer and the policy counterfactuals are model outputs, not observed. The 'predatory' label is not established; the authors state they cannot rule out benign liquidity provision.
- Preliminary preprint (v4, 29 Aug 2026), with AI-assisted coding and appendix, not peer reviewed.
- No trading rule or P&L is tested; any strategy conversion is our own and would be an untested extrapolation.
- Only first 95 of 106 pages read.

## Cited papers worth reading
- Do Leveraged ETFs Really Amplify Late-Day Returns and Volatility? (2018)
- Liquidity Provision to Leveraged ETFs and Equity Options Rebalancing Flows: Evidence from End-of-Day Stock Prices (2022)
- Predatory Trading (2005)
- Returns to Constant Leverage Strategies: General Principles and Application to Levered Single-Stock ETFs (2025)
- Positive Feedback Investment Strategies and Destabilizing Rational Speculation (1990)
