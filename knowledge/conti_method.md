# The Conti Method: from research paper to tradable strategy

This is the playbook every agent in this repo follows. It is distilled from Matteo Conti's
explanation of how institutional traders build strategies (Chart Fanatics episode, transcript 01).
New transcripts add to `knowledge/method_notes.md`; this file holds the core.

## 1. The core principle

> Retail chases trades. Institutions trade **validated strategies**.

A strategy is a set of rules that, applied systematically every time, has a known probability
of success over many trades. A single trade proves nothing; 100+ trades under fixed rules do.

## 2. The pipeline

```
IDEA (research) -> RULES -> CODE -> BACKTEST -> VALIDATION -> LIVE (automated) -> monitor -> back to IDEA
```

1. **Idea** — 90–95% of institutional strategy ideas come from research papers
   (SSRN is the main place). Two kinds: *academic* (university researchers) and
   *industry* (hedge funds, traders, research firms).
2. **Rules** — so specific a machine can execute them.
3. **Code** — build it iteratively: entry first, check it works; then exit; then sizing.
4. **Backtest** — replay history; report net profit, win rate, average trade, max drawdown.
5. **Validation** — in-sample/out-of-sample split and Monte Carlo (see §6).
6. **Live** — automated. The trader's job becomes monitoring performance and risk,
   and going back to research for the next strategy.

## 3. "You don't copy the paper"

The paper is a trigger, not a template. Copying a paper's exact rules usually gives a
beautiful equity curve up to the publication date and a poor one after (alpha decay).

Instead, for every paper extract exactly two things:

1. **The finding** — what the authors observed in the data, stated plainly.
2. **The WHY** — the economic reason the finding exists, which is what makes it likely to
   keep working in the future.

Then frame **your own** simple rules around the WHY.

## 4. How Conti finds the WHY

Look for a *structural reason someone is forced or very likely to trade in a predictable way*.
In his four examples the WHY was always one of these:

| WHY pattern | Example from transcript 01 |
|---|---|
| **Information arrives while the market is closed, and is digested slowly once it opens** | Opening range breakout: news, earnings and global positioning pile up overnight; orders collide in the first 30 min; the imbalance is too big to absorb, so it carries through the day. |
| **Institutional constraint / mandate** | Many funds can only trade after 9:30 ET. If that rule changed, the ORB effect would weaken. Knowing the WHY tells you what would kill the edge. |
| **Execution mechanics of big players** | VWAP algos are used by almost every institutional desk; they add volume in the direction of the move when price crosses VWAP, amplifying it. |
| **Slow information diffusion** | Post-earnings drift: low analyst coverage of small/mid caps means news spreads slowly. |
| **Liquidity constraints on large orders** | Post-earnings drift: a fund can't build a full position in one day, so it spreads buying over days/weeks, creating drift. |
| **Risk premium / liquidity premium** | Overnight drift: holders are paid for carrying risk while the market is closed and illiquid; overnight overreaction then corrects intraday. |

Agent rule: a finding **without** a WHY of this kind is a curiosity, not an edge.
Always also state **what would kill the edge** (e.g. pension funds allowed to trade
pre-market; companies pre-announcing bad results).

## 5. Every strategy needs three boxes filled

1. **Entry** — the exact condition that opens a position.
2. **Exit** — stop loss and take profit, and very often a **time exit**
   (close after N minutes/days, or at a fixed clock time) if neither is hit.
3. **Position sizing**
   - Development: **fixed size (1 contract)** — keeps the test simple and comparable.
   - Live: **volatility targeting** — risk the same dollars every trade
     (e.g. $10,000), contracts = risk ÷ volatility (e.g. range width or ATR).
     Wide/volatile days → fewer contracts; quiet days → more.
     Backed by *Volatility-Managed Portfolios* (Moreira & Muir) and
     *The Impact of Volatility Targeting* (Harvey et al., 2018).
     It smooths results and improves risk-adjusted return.
   - Equities: % of portfolio (e.g. 1–2% per name) or fixed dollars.

Keep rules **simple**. Conti made 80% of his €30M from extremely simple strategies.
Complexity means fragility — more places for the strategy to break.

## 6. Validation rules

- **Split**: 80% in-sample / 20% out-of-sample (chronological). All rule changes,
  added filters and parameter tuning happen **only** in-sample. Then run the frozen
  rules on out-of-sample. If performance collapses → overfit.
- **Monte Carlo reshuffle**: reorder the backtest's trades thousands of times. Same start
  and end, different path. Wide dispersion of paths/drawdowns = weak edge; tight = strong.
- **Monte Carlo bootstrap/resample** (10,000–20,000 runs): sample trades with replacement
  ("spaghetti chart"). Gives the distribution of profit, drawdown, and probabilities like
  "P(drawdown > $10,000)".
- **Live yardstick / kill switch**: if live drawdown exceeds what the simulation said had
  only ~5% probability over that many trades, stop the strategy and review.
- Report at minimum: net profit, win rate, average trade, max drawdown (peak-to-valley).
- A long-only strategy must be checked against market beta: does it still work in a
  down year (e.g. 2022)?

## 7. Getting creative with a known anomaly ("find the angle")

Alpha decays, but the WHY often survives in a different place. Ways Conti adapts an idea:

- **Different instrument**: QQQ paper → test NQ, ES, CL, single stocks. Write the code once,
  run it everywhere the WHY applies (e.g. wherever institutions use VWAP algos).
- **Different universe**: PEAD has no edge in mega caps (heavily covered) but works in
  small/mid caps; try Europe, where coverage and liquidity are lower.
- **Different session**: if 90% of index returns happen overnight, try an opening range
  breakout that trades **the overnight session**.
- **One side only**: ORB works better long-only (breakdowns get absorbed by buyers);
  PEAD short side is weaker now (companies pre-announce bad news).
- **Combine findings from several papers**: PEAD = price reaction (1968) + 60-day horizon
  (1989) + analyst-consensus surprise (2006).

## 8. Portfolio end game

Run several **uncorrelated** strategies (e.g. a trend strategy and a mean-reversion
strategy) so one covers the other's bad regime. Retail target: at least 3–4 automated
strategies at once. Review all live strategies **monthly**; strategies stop working, so the
research → validate → deploy loop never ends.

## 9. Checklist an agent must complete for every paper

1. Finding (plain language, with the sample, market and period it was found on).
2. WHY (which pattern from §4, or a new one — explain it).
3. What would kill the edge.
4. Decay risk (how widely known/exploited; when published).
5. The tradable edge in one paragraph — **our** framing, not the paper's rules.
6. Rules: entry / exit (SL, TP, time) / sizing (dev = 1 contract; live = vol-target).
7. Starting parameters taken from the paper, with ranges to test **in-sample only**.
8. Angles to test (instrument, universe, session, side).
9. Data needed, and whether our NinjaTrader data covers it.
10. Open questions the rules don't settle yet.
