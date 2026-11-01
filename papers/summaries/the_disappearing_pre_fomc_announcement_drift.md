# The Disappearing Pre-FOMC Announcement Drift

**Authors:** Alexander Kurov, Marketa Halova Wolfe, Thomas Gilbert  
**Year:** 2021  **Type:** academic  **Read:** full_pdf  
**Source:** https://ideas.repec.org/a/eee/finlet/v40y2021ics1544612320315956.html

> In S&P futures the pre-FOMC drift was 0.49% per meeting in 1994-2011, still 0.45% for press-conference meetings to 2015, but only 0.09% (insignificant) in 2016-2019 and ≈0 without press conferences; the decline lines up with lower VIX.

## Findings
- Mean pre-FOMC return (prior open → 15 min before announcement): 0.492% (1994-2011, 131 meetings). — *SE 0.107.*
- Press-conference meetings: 0.445% (Apr 2011-Dec 2015) → 0.092% (2016-2019, not significant); no-press-conference meetings −0.051%.
- Adding VIX makes the post-liftoff dummy insignificant; VIX coefficient ≈ 0.23 (t ≈ 3.3). — *Average VIX 17.7 → 14.7 after Dec 2015.*
- Authors reject publication-driven decay as the main cause.

## The WHY
**Pattern:** Uncertainty premium: the drift pays for resolving high policy uncertainty and fades when uncertainty is low.

Pre-FOMC returns scale with VIX/TYVIX two days before the meeting.


## Setting
- Markets: S&P 500 futures
- Instruments: SP, ES
- Period: 1994-2019  Frequency: intraday  Holding: previous open → 15 min before FOMC

## Reported results
0.49% (1994-2011) → 0.09% (2016-2019).
- VIX coefficient 0.229 (SE 0.069)

## Tradable edge (our framing)
Trade the pre-FOMC long only when pre-meeting uncertainty is high (VIX or our AvgRange proxy above its 1-year median).

## Angles to test
- Uncertainty-conditioned pre-FOMC long

## Decay risk: high
Documents the decay; small samples (20 meetings per sub-period).

## Data fit
ES 1-min Dec 2013 → Sep 2026, NQ 1-min Jul 2021 → Sep 2026 (2024+ protected in the backtest project).

## Caveats
- Read by Claude in a chat session (manual run 2), not by the weekly pipeline.
