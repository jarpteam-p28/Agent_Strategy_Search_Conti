# Agent Strategy Search — Conti method

Agents that find trading research on SSRN/arXiv, read the full papers, extract the **finding**
and the **WHY**, and turn them into strategy specs ready to code and backtest — following
Matteo Conti's institutional process (see [`knowledge/conti_method.md`](knowledge/conti_method.md)).

This is **step one: research → strategy specs**. Backtesting on the NinjaTrader data comes next.

## How it works

Every Monday a GitHub Action runs the agents and opens a pull request with what they found.

```
transcripts/ (new Conti videos) ──► Transcript miner ──► strategies/conti/  +  papers/seeds.yaml  +  knowledge/method_notes.md
                                                                                     │
papers/inbox/*.pdf ─┐                                                                │
papers/seeds.yaml ──┼──► queue ──► Resolver (find URL) ──► Reader (full PDF) ──► papers/summaries/
Scout (SSRN/arXiv) ─┘                                                    │
                                                                         ▼
                                     Strategist (finding + WHY → rules) ──► Critic (independent review)
                                                                         │
                                                                         ▼
                                                     strategies/candidates/*.yaml  +  reports/<date>.md
```

| Agent | What it does |
|---|---|
| **Transcript miner** | Reads a new Conti transcript (+ screenshots) → his strategies with exact rules, the papers he names, new method rules. |
| **Scout** | Web-searches SSRN and arXiv q-fin for new papers with a testable pattern and a structural WHY. |
| **Resolver** | Finds the SSRN/arXiv/journal page for a paper known only by title. |
| **Reader** | Reads the whole 40–60 page PDF → findings, the WHY (who is forced to trade, why it persists, what kills it), our framing of the edge, angles, decay risk, data fit. |
| **Strategist** | Turns the summary into specs with the three boxes filled: entry, exit (SL/TP/time), sizing (dev = 1 contract, live = volatility targeting) + validation plan. |
| **Librarian** | Searches for ES / NQ / S&P 500 / Nasdaq-100 research and writes `papers/READING_LIST.md`: papers to download by hand, where to get each one, why it's promising, and the file name to save it under. Also lists papers the reader couldn't get in full. |
| **Critic** | Separate agent that scores the WHY, persistence, simplicity, testability, overfit risk → backtest / refine / park / reject. |

No SSRN API is needed: search and fetching run through Claude's built-in web search and web fetch
tools. Papers the agents can't download (some SSRN PDFs block automated downloads, older journal
papers) are read from the abstract and marked `abstract_only`. For a full read, put the PDF in
`papers/inbox/` (see the note on repo visibility below) or run locally.

## What's in the repo

| Path | Contents |
|---|---|
| `knowledge/conti_method.md` | The playbook every agent follows |
| `strategies/conti/` | Strategies Conti described (transcript 01: ORB long-only, VWAP trend, PEAD, overnight drift, overnight ORB idea) |
| `strategies/candidates/` | Strategies the agents derived from papers, each with a critic `review` |
| `papers/READING_LIST.md` | **Papers for you to download** — save each PDF in `papers/inbox/` under the shown name |
| `papers/seeds.yaml` | Papers Conti named — read first |
| `papers/summaries/` | One Markdown + JSON summary per paper read |
| `papers/index.json` | Status of every paper (queued / summarized / failed) |
| `reports/` | One report per weekly run |
| `config/settings.yaml` | Models, papers per run, sources |
| `config/data_inventory.yaml` | NinjaTrader data on the Lexar drive (ES 1-min 2013–2026, ES/NQ ticks 2021–2026) |
| `config/search_topics.yaml` | What the scout looks for |

## Setup (one time)

1. **API key**: repo **Settings → Secrets and variables → Actions → New repository secret**,
   name `ANTHROPIC_API_KEY`, value = your key from console.anthropic.com.
2. **Allow the Action to open PRs**: **Settings → Actions → General → Workflow permissions** →
   "Read and write permissions" and tick "Allow GitHub Actions to create and approve pull requests".
3. First run: **Actions → Weekly research run → Run workflow** (set max papers to 1–2 for a test).

## Run locally

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY=...
python -m conti_agents run --max-papers 2    # full pipeline
python -m conti_agents run --no-scout        # only seeds + inbox PDFs
python -m conti_agents transcripts           # only mine new transcripts
python -m conti_agents validate              # check strategy YAMLs
pytest                                       # offline tests (no API key needed)
```

## Adding a new Conti video

Save the transcript as `transcripts/NN_short_name.txt` and any screenshots in
`transcripts/screenshots/NN_short_name/`. The next run mines it automatically.

## Repo visibility and copyrighted material

This repo is currently **public**, so raw YouTube transcripts, screenshots and paper PDFs are
git-ignored (see `.gitignore`) — committing them would republish third-party content. The agents'
own outputs (summaries in their own words, strategy specs) are committed. If you make the repo
**private**, remove the three marked lines in `.gitignore` so the weekly Action can see new
transcripts and inbox PDFs. Until then, run transcript mining and inbox reading locally.

## Cost control

`config/settings.yaml → limits.max_papers_per_run` caps how many papers are read per run
(default 4). Each report ends with the token usage per agent.
