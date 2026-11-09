# A Surprise That Keeps You Awake: Overnight Returns After Earnings Announcements

**Authors:** Fabian Gamm  
**Year:** 2019  **Type:** academic  **Read:** abstract_only  
**Source:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3293638

> After large earnings surprises (good or bad), single stocks earn unusually high overnight returns for several weeks, offset by negative intraday returns, which is consistent with retail attention-driven buying at the open.

## Findings
- For several weeks after large earnings surprises, stocks show strongly positive abnormal overnight (close-to-open) returns. This holds after both large positive and large negative surprises. — *Abstract only. Exact magnitudes, sample and period not seen.*
- Intraday (open-to-close) returns over the same weeks have the opposite sign. The two parts cancel in close-to-close returns, so the pattern is invisible in standard post-earnings-drift tests. — *Abstract only.*
- The effect exists only when retail investors are net buyers and pay attention to the surprise. — *Abstract only. The retail-trading and attention proxies were not seen.*
- The effect is stronger in high-sentiment periods and for hard-to-arbitrage firms. It is weaker when the average investor holds the stock at a gain (disposition effect). — *Abstract only.*

## The WHY
**Pattern:** Mix of attention-driven retail buying (close to 'new: retail attention / order-imbalance at the open') and a risk/liquidity-premium-style overnight vs intraday split. It is not one of the playbook's institutional-constraint patterns.

A large earnings surprise draws attention. Attention-constrained retail investors are net buyers of stocks that catch their eye, whichever the sign of the news. Their orders build up outside trading hours or at the open, so prices are pushed up overnight. During the day the price partly reverts, which gives negative intraday returns. Arbitrageurs find it hard to trade against this in hard-to-arbitrage stocks, and sentiment amplifies it.

- **Who is forced / predictable:** Retail investors buy attention-grabbing stocks. They only buy, since short selling is costly and rare for them. That makes them predictable, one-sided flow. Arbitrageurs are limited in the hard-to-arbitrage names. Holders sitting on gains sell instead, which weakens the effect.
- **Why it persists:** Limited attention and the retail buy-only habit are behavioural and structural, and retail participation has grown. Limits to arbitrage keep the pressure from being fully traded away in small, illiquid stocks.
- **What would kill it:** Retail investors becoming less attention-driven or less active as net buyers. Brokers or market structure shifting retail flow into the intraday session, for example through 24-hour trading. Arbitrage capital arriving at the open that offsets the imbalance. Wider awareness and exploitation of the overnight/intraday split.
- **Paper's view vs ours:** The author's own explanation (attention-induced buying pressure) is supported by the retail-flow and sentiment conditioning, so it seems reasonable. I could only read the abstract, so I could not check how robust the tests are. The overnight/intraday split could also reflect a general overnight risk premium or market-maker inventory effects, so treat attention as the leading but not the only candidate.

## Setting
- Markets: US equities
- Instruments: US single stocks
- Period: Not seen (abstract only)  Frequency: Daily (close-to-open and open-to-close decomposition); assumed from abstract  Holding: Overnight, repeated for several weeks after announcement

## Reported results
Strong positive abnormal overnight returns for several weeks after large positive and negative earnings surprises, with opposite-sign intraday returns. (Abstract only; no numbers seen.)
- Costs: Unknown (abstract only)

## Tradable edge (our framing)
Single stocks with large earnings surprises tend to rise overnight and give part of it back during the day, for weeks after the announcement. The edge is to hold the stock only close-to-open after a big surprise (in either direction), when retail buying is strongest. It could also be used in index or large-cap names as a "buy the close, sell the open" timing tilt, conditioned on how much retail attention the event drew. A fade of the intraday leg is the mirror image of the same effect. The paper's own universe is single stocks, which we cannot test directly.

## Angles to test
- Different universe: small and mid caps and hard-to-arbitrage names, and Europe, where retail attention differs.
- One side only: long overnight after both positive and negative surprises; the short-intraday leg may be a separate trade.
- Different instrument: NQ/ES overnight vs intraday split during heavy earnings weeks or around mega-cap earnings (e.g. NVDA, AAPL), as a proxy test with our data.
- Condition on sentiment: stronger effect in high-sentiment regimes, so use a sentiment or VIX filter.
- Combine with PEAD: the close-to-close drift hides this effect, so combine the surprise measure with the overnight/intraday split.
- Retail-flow proxies: abnormal retail volume, attention measures (Google search, news). Skip names where holders sit on gains (disposition effect).
- Test pre/post 2020, given retail trading growth after the pandemic.

## Decay risk: medium
The paper was published in 2019. Overnight/intraday decompositions are now well known, and the effect is linked to retail flow, which is large but may have changed since. Hard-to-arbitrage stocks keep it partly alive, but costs (two trades per day, small-cap spreads) are a big hurdle for a daily open/close strategy. Published effects typically lose around half their size out of sample.

## Data fit
We cannot test the core result, because it needs single stocks, earnings dates, EPS surprises and retail-flow data, and we have none of these. We have ES (2013 to 2026) and NQ (2021 to 2026) 1-minute bars, which would allow a rough test of the overnight-versus-intraday split on index futures around earnings season. That would be a weak proxy. A cleaner test would need stock-level data with open/close prices, earnings dates and retail order-flow proxies.

## Caveats
- Only the abstract was read; the SSRN full text and the PDF were not accessible. Magnitudes, sample, period, holding horizon (the 'several weeks') and robustness are unknown.
- Daily open/close trading in single stocks has high transaction costs. Net profitability is unknown.
- Effect depends on retail net buying, which has to be measured, so a live signal needs a data feed we lack.
- The cancelling intraday return means a pure close-to-close approach shows nothing.

## Cited papers worth reading
- Overnight Returns and Firm-Specific Investor Sentiment (2018)
- Overnight Returns and the Retail Investor / Attention papers (e.g. Barber & Odean 2008, All That Glitters) (2008)
