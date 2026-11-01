# High-Frequency Trading around Large Institutional Orders

**Authors:** Vincent van Kervel, Albert J. Menkveld  
**Year:** 2019  **Type:** academic  **Read:** full_pdf  
**Source:** https://www.cemfi.es/ftp/pdf/papers/wshop/SSRN-id2619686.pdf

> HFTs first trade against large institutional orders (cutting their cost) but then trade with long-lasting orders after ~2-7 hours (raising it): 1 SD of against-flow cuts implementation shortfall 3.4 bps (−46%), 1 SD of with-flow adds 12.5 bps (+169%).

## Findings
- Average implementation shortfall 7.4 bps; HFT against-the-order flow −3.4 bps, with-the-order +12.5 bps per SD. — *Swedish index stocks 2011-2013, 5,910 institutional orders.*
- Pattern fits back-running of informed orders.

## The WHY
**Pattern:** Execution mechanics: fast traders detect and ride persistent institutional order flow.




## Setting
- Markets: Sweden
- Instruments: index stocks
- Period: 2011-2013  Frequency: trade-level  Holding: hours

## Reported results
HFTs first trade against large institutional orders (cutting their cost) but then trade with long-lasting orders after ~2-7 hours (raising it): 1 SD of against-flow cuts implementation shortfall 3.4 bps (−46%), 1 SD of with-flow adds 12.5 bps (+169%).

## Tradable edge (our framing)
No strategy; supports the order-splitting WHY behind VWAP/drift specs (persistent institutional flow is detectable).

## Angles to test

## Decay risk: low
Microstructure.

## Data fit
Single-stock study — not testable on our ES/NQ data.

## Caveats
- Read by Claude in a chat session (manual run 3), not by the weekly pipeline.
