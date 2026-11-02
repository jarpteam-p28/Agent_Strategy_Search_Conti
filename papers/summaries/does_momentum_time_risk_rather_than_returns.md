# Does Momentum Time Risk Rather Than Returns?

**Authors:** Valeriy Zakamulin  
**Year:** 2026  **Type:** academic  **Read:** abstract_only  
**Source:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6910478

> I could not open the paper, so I have no verified finding. The title suggests momentum signals may work by predicting risk (volatility or drawdown) more than returns. That is an untested guess.

## Findings
- NOT VERIFIED. The SSRN page failed to load and I found no other copy, so I read nothing beyond the title. I have no sample, market, period or numbers. The title suggests the paper asks whether time-series momentum (trend) signals earn their benefit by timing risk rather than by forecasting returns. — *Title only. Do not cite any numbers from this entry.*

## The WHY
**Pattern:** Unverified. The title points to a risk-timing mechanism, which would be volatility clustering plus leverage/risk-management constraints. Treating it as a new pattern, 'risk-state timing', is my inference and not something the paper says.

Hypothesis only. A trend signal (price above or below its moving average, or a positive or negative past return) may mostly mark low-volatility, calm regimes and high-volatility, drawdown regimes. Volatility is persistent, so an exposure rule based on it can improve risk-adjusted return even if the mean return forecast is weak. This is consistent with the volatility-managed portfolios literature (Moreira & Muir) in our playbook. I have not confirmed that the paper argues this.

- **Who is forced / predictable:** Not verified. Plausibly risk-targeting funds, which de-lever when volatility rises, and loss-limit or margin-driven sellers in drawdowns. These are the participants who make volatility persistent and predictable.
- **Why it persists:** Volatility clustering is a structural feature of markets, so a risk-timing benefit would last longer than a return-prediction anomaly. This is an inference.
- **What would kill it:** If the paper's claim holds, it would break when volatility stops being persistent or when trend signals stop separating calm regimes from stressed ones. Another risk is sharp V-shaped reversals, where de-risking after a drop misses the rebound. This is unverified.
- **Paper's view vs ours:** I don't know the authors' explanation, because I did not read the paper.

## Setting
- Markets: 
- Instruments: 
- Period: unknown  Frequency: unknown  Holding: unknown

## Reported results
Not available. The paper was not read.
- Costs: Unknown

## Tradable edge (our framing)
Unverified, and it should not be treated as an edge until someone reads the paper. If the title's thesis is right, the practical version is to use trend or momentum conditions as a volatility and exposure filter, not as a directional return forecast. For example, size an ES or NQ position by realised volatility and trend state, then compare it against a plain volatility-targeted buy-and-hold baseline. The thing to test is whether the trend filter adds anything once volatility targeting is already applied.

## Angles to test
- Run a baseline comparison on ES: a volatility-targeted long position, a trend-filtered long position, and the two combined. This shows whether trend adds anything beyond volatility.
- Measure whether a trend signal predicts next-period realised volatility or drawdown on ES, and separately whether it predicts the return.
- Run the same test on NQ for 2021-2026 and compare against ES.
- Try long-only trend as a regime filter on our intraday strategies, switching them off in high-volatility or downtrend regimes.
- Report all results before and after 2022, and by volatility regime.

## Decay risk: medium
Not assessed from the paper. Trend and momentum are widely known, but volatility persistence is robust. The paper was published in 2026, so no post-publication decay can be measured yet.

## Data fit
ES 1-minute data from 2013 to 2026 can test any daily or intraday trend-versus-volatility timing rule, including pre/post-2022 splits and the 2022 down year. NQ data starts only in 2021. Multi-asset or cross-sectional momentum tests are not possible because we have no other futures and no single stocks. I can't say what data the paper itself needs.

## Caveats
- I could not read the paper. The SSRN page was inaccessible and no PDF URL was available. Everything here except the title is hypothesis.
- The WHY and the tradable edge are inferred from the title only and may be wrong or even opposite to the paper's conclusion.
- Someone should re-run this reader pass once the paper text is available.

## Cited papers worth reading
- Volatility-Managed Portfolios (2017)
