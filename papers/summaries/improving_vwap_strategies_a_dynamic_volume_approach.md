# Improving VWAP strategies: A dynamic volume approach

**Authors:** Jędrzej Białkowski, Serge Darolles, Gaëlle Le Fol  
**Year:** 2008  **Type:** academic  **Read:** full_pdf  
**Source:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=932699

> Splitting intraday volume into a common (market/seasonal U-shape) part and a stock-specific part, and forecasting the specific part with ARMA/SETAR models, cuts VWAP execution tracking error by roughly 10-20% versus a plain historical-average volume curve. This is an execution paper, not a return-prediction paper.

## Findings
- Intraday turnover can be split by PCA across CAC40 stocks into a common seasonal component (U-shape, shared across stocks) and a stationary stock-specific component with short memory. — *39 CAC40 stocks, 20-min bars (25 per day, 9:20-17:20), Sep 2003-Aug 2004. First 3 PCs explain 48.5% of variance on a 1-month window but only 35.6% on a 1-year window. Unit-root tests reject non-stationarity at 1% for the specific part.*
- Volume forecasts built on the decomposition beat the classical rolling-average-volume forecast. SETAR (regime-switching) beats ARMA, which beats classical. — *Table 11, weighted-average MAPE of volume: SETAR 7.5bp, ARMA 8.3bp, classical 9.1bp. 95% quantile of error: 2.0e-2 vs 2.3e-2 vs 2.5e-2.*
- VWAP tracking error falls with the better volume curve. The gain is mostly theoretical, because the 'theoretical' execution uses the unknown full-day volume. The implementable dynamic execution keeps part of it. — *Table 28, mean abs. VWAP prediction error, Sep-Dec 2003. In-sample: SETAR 7.1bp, ARMA 7.7bp, classical 11.4bp. Out-of-sample (20-day rolling window): theoretical SETAR 7.7bp, dynamic SETAR 9.0bp, dynamic ARMA 9.2bp, classical 10.1bp. Basket of CAC40: classical ~10bp, theoretical ~8bp (-20%), dynamic ~8bp (-10%).*
- Static execution (forecasting the whole day once at the open) does worse than the classical method. The ARMA forecast decays to zero within a few steps, so the specific component adds nothing. — *Stated by the authors; results 'available upon request', not shown.*
- The improvement is largest where the classical method tracks worst (names with volume surprises such as CAP GEMINI and EADS). It is negligible where classical error is already small. — *Figure 4 scatter. CAP GEMINI dynamic gain about -8bp, EADS about -5bp. Out-of-sample, 30 of 39 stocks improve, 14 improve by more than 1bp, and 2 get significantly worse (Lagardere +1.3bp, Schneider +1.6bp).*
- The result holds in other sub-periods. The model does not by itself beat the VWAP, i.e. it does not produce a directional price edge. — *Jan-Apr 2004 out-of-sample: dynamic SETAR 11.2bp vs classical 12.0bp. The sign of the predicted-minus-actual VWAP error is about 50/50 (Table 30). The authors say a joint volume-and-price model is needed to beat VWAP.*
- Rough scale of the benchmark: VWAP-type orders are about 50% of institutional trading, per the authors' introduction. This is the main reason the intraday volume profile is predictable and the VWAP is a 'magnet' for algo flow. — *Introduction claim, not tested in the paper.*

## The WHY
**Pattern:** Execution mechanics of big players (VWAP algos). Secondary: new: predictable intraday volume seasonality (U-shape) as a structural liquidity clock.

Institutions slice large orders by a forecast volume curve so that their average price tracks the VWAP. Their trading is therefore scheduled by the volume profile, not by price view. The volume profile is highly seasonal: it is high at the open and the close and low at midday. That seasonality is common across stocks, so it can be predicted. The deviation from the curve (the specific part) is short-lived and mean-reverting, and it is linked to news and arbitrage activity. The paper's own point is that volume surprises coincide with price surprises. So when volume runs above its expected curve, price is moving and VWAP-tracking flow has to chase it.

- **Who is forced / predictable:** Buy-side desks and brokers executing VWAP orders (guaranteed or agency). They must track the benchmark and cannot revise past fills. Brokers with guaranteed-VWAP books carry the residual risk. Mandate or evaluation rules ('beat VWAP') force them to trade in proportion to volume whatever the price.
- **Why it persists:** Benchmarked evaluation (VWAP, TWAP, POV) is an institutional and compliance habit. The U-shaped volume pattern comes from market structure (open/close auctions, index and fund rebalancing at the close, global overnight news). Neither is arbitraged away. Our edge would sit in the VWAP flow footprint, not in the forecasting model the authors build.
- **What would kill it:** Execution moving away from VWAP to implementation-shortfall or arrival-price algos, or to close-auction-only execution. A flattening of the intraday volume curve. Market fragmentation that makes the 'market volume' unobservable. For this particular paper, the forecasting gain is just a broker cost saving that competitors already have.

## Setting
- Markets: Euronext Paris
- Instruments: CAC40 constituent stocks (39 names)
- Period: Sep 2003 - Aug 2004 (main tests Sep 2 - Dec 16, 2003; robustness Jan-Apr and Apr-Aug 2004)  Frequency: Tick data aggregated to 20-minute intervals (25 bars/day, 9:20-17:20 Paris)  Holding: Intraday (one-day VWAP order)

## Reported results
The decomposition-based volume forecast reduces VWAP tracking error by about 10-20% on a CAC40 basket versus the classical rolling volume average, and by more than 1bp for roughly 77% of stocks in the theoretical case. It is not a trading strategy and reports no PnL.
- Volume MAPE: SETAR 7.5bp, ARMA 8.3bp, classical 9.1bp
- Out-of-sample VWAP error, Sep-Dec 2003: classical 10.1bp, dynamic SETAR 9.0bp, theoretical SETAR 7.7bp
- Basket tracking error: classical ~10bp, theoretical ~8bp (-20%), dynamic ~8bp (-10%)
- Out-of-sample dynamic execution: 30 of 39 stocks better, 14 improve by more than 1bp, 2 materially worse
- Robustness Jan-Apr 2004: dynamic SETAR 11.2bp vs classical 12.0bp
- Costs: Not applicable. The paper measures tracking error in bp and does not model transaction costs, commissions or market impact.

## Tradable edge (our framing)
The paper gives a model, not a trading rule. Our edge framing: intraday volume has a predictable seasonal shape, and the part above or below that shape (relative volume) is the signal that tells you when VWAP-driven institutional flow is likely to be heavier or lighter than usual. We can build an expected-volume-by-time-of-day curve per instrument from the last ~20 days, take the surprise as a conditioning variable, and use it to filter or size VWAP-pullback, opening-range or gamma-level continuation trades. In practice that means taking continuation signals only when volume is running above the curve, and standing aside or fading when it is below. This is a filter and a sizing input and is not a stand-alone strategy. The paper gives no return evidence for it, so it has to be validated in-sample first.

## Angles to test
- Filter for the existing VWAP-pullback strategy: only take VWAP-cross continuation when cumulative volume vs the 20-day expected curve is above a threshold (a relative-volume gate).
- Replace the 'minimum % move in last hour' speed condition with a volume-surprise condition (specific volume component > 0).
- Time-of-day volume clock for ES/NQ 1-min bars: build the expected curve with a simple time-of-day average or a 1st-PC approach, with no ARMA/SETAR needed.
- Cross-instrument: ES and NQ volume curves are strongly common, so the common component can be extracted by PCA across the two. The deviation shows rotation between ES and NQ.
- Position sizing: scale risk down on days when the specific volume component is high (volume surprises coincide with price surprises and trendy days, where execution error is largest).
- Different session: build the curve separately for ETH/overnight and RTH to improve any overnight-bias or overnight-ORB variant.
- Close-side: the volume ramp into the close (U-shape right arm) is predictable, so test a late-day continuation or flattening rule around 15:00-15:55 ET.
- Different universe: single stocks or European stocks where VWAP usage is high and volume surprises are larger (not available in our data).

## Decay risk: medium
Published 2006-2008 on one year of CAC40 data. The broker-execution use is mature and well known, so the forecasting edge is already competed away and has no alpha content. The structural facts it rests on (VWAP benchmarking, U-shaped volume) are very stable and still true. Decay risk is low for the WHY, high for the model as a profit source. Overall medium.

## Data fit
"Partly testable. ES 1-min bars (2013-2026) and NQ 1-min bars (2021-2026) include volume, so an expected-volume-by-time-of-day curve and a relative-volume surprise can be computed, for example in 20-min or 1-min buckets with a 20-day rolling average and a simple common/specific split. We can test it as a filter on the VWAP-pullback strategy. Missing: single-stock data (the paper's universe is CAC40 stocks), shares outstanding (turnover normalisation is unnecessary for a single futures contract), and any record of actual VWAP execution flow. The paper itself offers no PnL evidence to replicate. Note that futures volume is contract-roll-affected, so use front-month volume only."

## Caveats
- Not a return-generating strategy. The authors state they could not beat the VWAP.
- Only about one year of data, 39 large-cap French stocks, 75 trading days in the main test and 50 out of sample. No significance tests on the tracking-error gains.
- The headline gains come from the 'theoretical' execution that uses the full-day volume, which is not implementable. The implementable dynamic version gets roughly half of the gain.
- Static execution is worse than classical (results not shown). Two stocks get significantly worse.
- The paper assumes orders are small relative to daily volume, no strategic traders, and low-motivation (non-informed) flow. These assumptions are exactly where a trader could find an edge, but the paper does not test it.
- Price is a 20-minute average of transaction prices, not true VWAP bars, and the PCA window is one month.
- Tables are in %/bp of the VWAP price and some means-of-MAPE comparisons are mixed between sections, so the exact figures should be read from Tables 11, 28 and 31-32.
- Working-paper version (EPEE 06-08, 2006); the SSRN listing is dated 2008.

## Cited papers worth reading
- Trading Volume: Definition, Data Analysis, and Implications of Portfolio Theory (2000)
- Trading volume and arbitrage (2003)
- Return Volatility and Trading Volume: An Information Flow Interpretation of Stochastic Volatility (1996)
- Price, Trade Size, and Information in Securities Markets (1987)
- VWAP Strategies (2002)
