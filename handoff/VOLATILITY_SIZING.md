# Volatility sizing — one rule for every strategy (Pablo, 2026-10-21)

Conti: develop with 1 contract; live = same dollars at risk, contracts set by volatility (higher volatility → fewer
contracts, lower → more). Sources he cites: Moreira & Muir, *Volatility-Managed Portfolios*; Harvey et al. (2018),
*The Impact of Volatility Targeting*.

## The volatility measure = Conti's noise unit (same one as the Vault Break level)
- **AvgRange** = average session high − low (midnight CT → 16:00 CT) of the last **15 completed sessions**, skipping
  the most recent one. Already computed in the Vault Break engine — reuse it.
- **Noise unit (N)** = **0.30 × AvgRange**, in points. Known at the start of the session (no look-ahead), fixed all day.

## Contracts
    contracts = floor( Risk$ / (N × point value + 2 ticks × tick value) )
- Size in **MES** (point value $5, tick $1.25) so it can adjust finely; 10 MES = 1 ES.
- **Cap:** max 20 MES (or the prop firm's max contracts, or margin — whichever is lowest).
- **Minimum:** if the formula gives 0, skip the trade (never round up).
- **Risk$ settings to report:** personal account 0.5% and 1% of equity (no compounding above the cap — D5);
  prop 50K: $250 and $500 per trade.
- Example: AvgRange 75 pts → N = 22.5 pts → $112.50 + $2.50 per MES → $500 buys 4 MES.
  AvgRange 40 pts (quiet 2019) → N = 12 pts → $62.50 per MES → 8 MES.

## How it applies
Every strategy uses the same N, whatever its own stop is. Where the stop is itself N-based (Overnight Bias: stop =
0.30 × AvgRange) the dollar loss per stopped trade ≈ Risk$ exactly. Where the stop is fixed (Vault Break $1,500,
Drift VWAP 16/20/32 pts) or trailing (Noise Area), N only scales the size: loss per trade then varies around Risk$,
but size still goes down when volatility rises and up when it falls — which is the point.

## Testing rules (Conti Revised)
- The headline stays **1 contract** for every strategy and every verdict (C1, C9, C10).
- Volatility sizing is a **SIZING VIEW**, not a trade variant: same trades, different size. It does NOT add to the
  variant count N for DSR/PBO. Report it next to fixed size in Part D (D1b, D5) and Part P (P2–P6, P4 sweep replaced by
  the Risk$ settings above).
- Compare fixed vs volatility-sized: net $, max drawdown, worst day, longest drawdown, Sharpe of daily P&L, and prop
  pass rate. Expect smoother results, not a bigger edge.
