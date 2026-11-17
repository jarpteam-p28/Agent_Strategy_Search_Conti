# All That Glitters: The Effect of Attention and News on the Buying Behavior of Individual and Institutional Investors

**Authors:** Brad M. Barber, Terrance Odean  
**Year:** 2008  **Type:** academic  **Read:** full_pdf  
**Source:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=460660

> Retail investors are net buyers of stocks that grab attention (abnormal volume, extreme one-day returns up or down, news), while institutions are not. The paper measures order flow only and shows no return or tradable edge.

## Findings
- Individual investors are net buyers of high-abnormal-volume stocks and net sellers of low-volume stocks. The imbalance rises almost monotonically with volume. — *Large discount broker (78,000 households, 1991-96): number imbalance is -18.2% in the lowest volume decile and +29.5% in the top 5% vingtile. By value: -16.3% to +17.7%. The large retail broker (30 months to mid-1999) and the small discount broker (1996-99) show the same pattern. Abnormal volume = today's dollar volume / 252-day average.*
- Retail buying is U-shaped in the previous day's return. They buy both big losers and big winners, with more buying after losses. — *Large discount broker: +29.4% imbalance after the worst 5% of returns, about +1.8% in the 8th decile, +24% after the best 5%. The large retail and small discount brokers buy big losers more strongly than big winners. Retail winner-buying disappears by value at the large retail broker and is absent at the small discount broker.*
- Stocks in the news (Dow Jones feed, 1994-99) see more net retail buying than stocks not in the news. This holds on positive-, negative- and zero-return days. — *Large discount broker: +9.35% in the news vs +2.70% not in the news. Large retail broker: +16.2% vs -1.8%. About 91% of stocks have no news on a given day. News is the weakest attention proxy; abnormal volume is the strongest, then returns.*
- Institutions (Plexus Group, 43 managers, 1993-96) do not show attention buying. Their buying is heavier on low-volume days. Momentum managers buy yesterday's winners and sell losers. Value managers do the opposite. — *Value managers' imbalance by number: +34.6% in the lowest volume decile vs +4.8% in the highest. Momentum managers after the worst 5% of returns: -21%. Value managers after the best 5%: -17%. The authors attribute these to the managers' own selection criteria, not to attention.*
- Attention buying is as strong in large caps as in small caps. — *Table 4. Top-volume vingtile: +20.8% (small), +24.4% (mid), +28.3% (large). Large caps after the worst returns: +38.7%.*
- The effect is not explained by short-sale constraints. It also appears for stocks the investor already owns and for stocks with and without listed options. — *Table 5 shows the buy/sell ratio of already-owned stocks rising with volume. The imbalance is -54% in the lowest volume decile and -25% in the top at the large discount broker. After big winners there is no extra buying of owned stocks, which fits the disposition effect.*
- The authors' own caveat: attention-driven buying does not generate superior returns. Their Kyle-style model predicts noise-trader losses grow with attention. — *Conclusion and Proposition 1. Returns are not tested in the paper; they appear only in unreported auxiliary analysis.*

## The WHY
**Pattern:** new: behavioural order-flow imbalance, caused by retail attention and search-cost constraints. It is related to 'slow information diffusion' and 'execution mechanics of big players', with a short-sale constraint element.

Retail investors face thousands of stocks to buy but only a few to sell, because they hold small portfolios and do not short. Attention therefore decides what they buy. Volume spikes, extreme moves and news create a one-sided retail buy flow. Someone must take the other side, mostly professional liquidity providers. Price pressure from the herded buying can push prices temporarily away from value. Seasholes & Wu (cited) found a transitory effect that reverses within about 10 days. This paper does not test that.

- **Who is forced / predictable:** Retail investors (long-only, with limited search capacity) are predictably net buyers on attention days. They buy after both crashes and spikes. Market makers and institutions are the forced counterparties and supply the shares.
- **Why it persists:** Cognitive limits are stable. Retail now has app-driven attention triggers (top-movers lists, social media, meme flow) that concentrate attention more. Short-sale constraints on retail remain.
- **What would kill it:** The retail share of volume falls, or retail starts to short and scan systematically (screeners, robo-advice). Zero-commission retail flow gets internalised or paid for in a way that removes the price impact. Attention events get arbitraged within the first minutes, before a next-day trade.
- **Paper's view vs ours:** The authors stress the search problem (attention sets the choice set, preferences choose within it) and reject short-sale constraints as the sole driver. Our reading adds that the paper shows order flow, not returns. For us it is a flow-direction clue, not an edge. Any edge would come from fading or front-running the temporary price pressure, and that needs separate evidence. The paper says buyers lose, but this is only an inference from other work.

## Setting
- Markets: US equities
- Instruments: US common stocks (NYSE, AMEX, NASDAQ)
- Period: 1991-1999 (broker data); institutional 1993-1996; news 1994-1999  Frequency: daily  Holding: none (daily buy-sell imbalances; no holding-period returns)

## Reported results
Retail net-buying imbalance rises from about -18% (lowest-volume decile) to about +30% (top 5% volume). It is also about +29% after the worst returns and +24% after the best returns. Institutions show no such pattern.
- Large discount broker: 78,000 households, 1.08M purchases, 0.89M sales, 1991-96
- Large retail broker: 665,533 accounts, about 7.2M common-stock trades, 30 months to June 1999
- Plexus: 43 institutional managers (18 momentum, 11 value, 14 diversified), 1993-96
- News: +9.35% vs +2.70% (large discount broker), +16.2% vs -1.8% (large retail broker)
- Buy-sell imbalance by size: top-volume vingtile +20.8% (small), +24.4% (mid), +28.3% (large)
- Costs: Not applicable. The paper is order-flow only and has no trading strategy or returns.

## Tradable edge (our framing)
The paper shows who trades, not what the price does next. The tradable idea is a hypothesis built on the WHY: on days of abnormal volume or extreme moves, retail-driven buying pressure may push stocks and retail-heavy index products too far in the short run, and that may partly reverse. We would test index-futures proxies. These are NQ (more retail- and tech-heavy than ES) versus ES, high-volume or big-gap days, and next-day or multi-day reversal after extreme up and down days. The trade is a fade of attention-driven runs on high-attention days, or avoiding longs there. Single-stock testing would be the cleaner version, but we lack that data. Treat this as an exploratory conditional-return study, not a replication.

## Angles to test
- Index futures proxy: after days with abnormal ES/NQ volume (volume divided by 252-day average) or extreme returns (top and bottom 5%), measure next-day to 10-day returns. Test a reversal fade, long-only after crash days and avoiding longs after spikes.
- NQ vs ES spread: NQ is more retail-heavy, so test whether attention-day overshoot is bigger in NQ than in ES. NQ data starts only in 2021, so the NQ part covers about 5 years and has to be split by regime.
- Intraday version: first-hour abnormal volume or opening gap as an attention trigger. Test a fade after the retail-heavy opening burst, hold 60+ minutes to beat costs.
- Both-tails test: the U-shape means big drops and big rallies both attract retail buying. Test long-only after capitulation days and short-only after euphoric spikes separately.
- Conditioning on top of another signal: add an attention filter to opening range breakout or VWAP-pullback strategies. Check whether breakouts on abnormal-volume days fail more often.
- Stock-level (needs new data): single stocks with news, earnings dates or top-mover lists, as in the paper. Not testable with our inventory.

## Decay risk: medium
The behaviour (retail attention buying) is well established and probably stronger now. But this paper is a 2008 order-flow study with no return predictability claim, so there is nothing published to decay. The related price-impact and reversal effects are widely known (Seasholes & Wu, Gervais et al.). Heavy HFT and market-maker competition probably leaves any reversal very short-lived. Index-level adaptation is speculative.

## Data fit
Poor direct fit. The paper's data (broker account trades, Plexus institutional trades, Dow Jones news, CRSP single stocks) is not in our inventory. We have no single stocks, no retail order flow and no news feed. Only a proxy is testable: ES 1-min from 2013 and NQ 1-min from mid-2021, where abnormal volume can be computed as volume over a trailing 252-day average and extreme-return days defined from the same bars. That tests index-level reversal after attention days, not the paper's finding about retail order imbalance. Missing: retail flow data (e.g. odd-lot or retail volume), news and earnings dates, single-stock data, and NQ before mid-2021.

## Caveats
- The paper reports no returns. It measures buy-sell imbalance and does not show attention buying is profitable for anyone.
- The sample is 1991-99 and the institutional sample is only 43 managers over 3 years, which the authors call 'illustrative, not representative'.
- Retail buying on both big gains and big losses may partly reflect executed limit orders, which the data cannot separate from market orders. Dip-buying after drops is also tied to the disposition effect.
- The news proxy has no intensity measure and missing days.
- The model section is stylized (Kyle extension) and its only proposition is untested here.
- Daily horizon and equities only. Nothing on futures or intraday timing.

## Cited papers worth reading
- Profiting from predictability: Smart traders, daily price limits, and investor attention (2004)
- The high-volume return premium (2001)
- Do noise traders move markets? (2006)
- Market efficiency in real time (2002)
- Do individual investors drive post-earnings announcement drift? Direct evidence from personal trades (2003)
