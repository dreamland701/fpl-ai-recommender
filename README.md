# FPL AI: a fine-tuned LLM forecaster for Fantasy Premier League, tested honestly

A season-long research project (April 2026 to now) that builds a Fantasy Premier League (FPL) assistant
in which a **fine-tuned language model is meant to do real forecasting work**, and that measures, every
week and in walk-forward backtests, whether it actually does. It runs live for the 2026-27 season on a
single DGX Spark (GB10, 119 GB unified memory, aarch64), with every recommendation and its settlement
written down.

The headline result is a negative one, stated plainly: across roughly forty supervised fine-tuning,
reinforcement-learning and regression-head experiments on Gemma-4 (E4B, 12B and 31B), the fine-tuned
reader learned to read **availability** from text (team news, the Guardian's predicted lineups), but no
configuration produced a **player-specific points signal** beyond the classic ridge model, and no
configuration moved realised decision value beyond the measured noise floor. The classic model plus
fixture features makes the live decisions; the LLM runs in shadow with its reasoning shown side by side.
Most of the engineering effort went into making that conclusion trustworthy: a strict data contract,
leakage audits, a 21-window re-baseline, and an expected-points instrument that cut the decision-backtest
noise by 40 percent.

## The system

```
vaastav history + official FPL API ──► player-week table (data contract, pre-deadline status/news)
        │
        ├─► classic anchor: ridge suite (availability/minutes, points 1/3/5 GW) + fixture features (F6)
        │
        ├─► LLM reader: Gemma-4-E4B LoRA, regression head (H-series), team-sheet prompt block
        │       inputs: the classic forecast, role facts, Guardian/Scout evidence attached per player
        │
        └─► decision layer: exact MILP squad/transfer optimiser, chip planner, captain/bench,
                walk-forward backtests scored in realised points and in expected points (xPts)
                        │
                        └─► weekly runbook: interim and final packets, Guardian predicted lineups,
                            classic vs classic+SFT side by side, settlement and ledger
```

| Where | What |
|---|---|
| `src/fpl_ai/` | the library: `dataset.py` (table + contract), `models.py` (ridge suite), `decision.py` and `squad_milp.py` (optimiser), `backtest.py`, `evaluation.py`, `reghead.py` (LLM regression head), `grpo_*_env.py` (RL environments), `evidence*.py`, `rules.py`, `cli.py` |
| `scripts/` | training, scoring and backtest drivers for every experiment; the weekly runbook (`run_gw*_interim.sh`, `run_gw*_final_refresh.sh`, `settle_gw.py`, `gw_status.py`); evidence collectors |
| `reports/` | one directory per experiment or gameweek packet with its markdown write-up; the weekly `RECOMMENDATION_*.md` files and the classic-vs-SFT sheets |
| `docs/` | `fpl_project_deep_dive_2026_10_03.md` (the complete record, 37k words), `programme_2026_10_17.md` (the running log since October), `review_fixes_2026_10.md`, design docs |
| `Codex/` | an independent code and evaluation review (3 October 2026) and the diagnostic scripts behind it; its findings were fixed in `docs/review_fixes_2026_10.md` |
| `tests/` | unit tests for the contract, rules, decision layer, evidence handling and the RL environments |

## What was learned

- **Decision value is the only metric that matters, and it is noisy.** One four-week decision backtest has a standard deviation of about 15 points between forecasters. An effect has to clear roughly 65 points over five windows to be real. Most published "wins" earlier in the project were inside that band; the expected-points instrument (score the chosen squad by its own forecasts instead of by realised points) cut the noise by 40 percent and is now the primary bench.
- **Text helps on availability, not on points.** The one prompt block that is provably used on holdout is the team sheet (facts plus the Guardian predicted lineup). Match reports, podcasts, bookmaker odds and news horizons were each tested as features or as prompt text: null or negative.
- **Loss, inputs, optimisation and capacity were all measured.** Mean-squared-error training removed the median-estimator shrink of the earlier adapters; adding numeric history, more epochs, and moving from 4B to 12B and 31B parameters all left the player-specific delta as a near-constant shift. The reader line is closed on this corpus; the remaining candidate is data scaling to all players.
- **Reinforcement learning at the decision layer learned the base rate.** GRPO on chip timing, transfer choice and availability each collapsed to a constant policy or to a Platt fit; the exact optimiser already captures the noise-free part of the decision.
- **The data contract was the biggest lever.** Ownership counts passed as percentages, status flags that were always 'a' in history, player ids reused across seasons, labels that crossed the prediction cutoff: each was found, fixed and re-baselined, and several earlier verdicts changed sign.

The live season (entry GZFC) has run every gameweek since GW1 2026-27 with the recommendation written before
the deadline and settled afterwards; see `reports/gw*_packet_*/RECOMMENDATION_*.md` and the ledger sections of
`docs/programme_2026_10_17.md`.

## What is not in this repository

- **Model weights** (87 GB of LoRA adapters, merged checkpoints and regression heads). The training scripts
  reproduce them; nothing here depends on a hosted model.
- **Data tables** (4.8 GB). Rebuild with the CLI (`docs/cli_quickstart_2026_07.md`): the history comes from
  `vaastav/Fantasy-Premier-League` and the official FPL API.
- **Evidence stores** (Guardian Open Platform and Premier League Scout article text) and **run logs**.
  The collectors are here; the Guardian key is read from `GUARDIAN_API_KEY` in `~/.fpl_secrets.env`, never
  from the repository.

## Running it

```bash
# unit tests
PYTHONPATH=src python3 -m pytest -q tests

# build the player-week table and train the classic suite (see docs/cli_quickstart_2026_07.md)
PYTHONPATH=src python3 -m fpl_ai.cli bootstrap-training-data --history-root /tmp/fpl_history --output /tmp/rows.csv
PYTHONPATH=src python3 -m fpl_ai.cli train-models --training-data /tmp/rows.csv --model-dir /tmp/fpl_models

# a weekly packet (fixed pipeline flags as used live)
PYTHONPATH=src FPL_PLANNER_DISCIPLINE=1 FPL_PER_FIXTURE=1 FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1 \
  bash scripts/run_gw10_interim.sh
```

GPU experiments (`scripts/train_gemma_reghead.py`, `scripts/reghead_predict.py`, the `run_h*_chain.sh`
drivers) expect Gemma-4 weights on disk and a 100 GB-class GPU; they were run one at a time on the Spark.

Built by Wes Cheng with Claude (Anthropic) as pair programmer and the independent review in `Codex/`.
Start with `docs/fpl_project_deep_dive_2026_10_03.md`, Part 0, for the thirty-minute version.

## License

Code and write-ups are released under the MIT License (see `LICENSE`). The short quotations from Guardian and
Premier League articles inside the gameweek write-ups are attributed excerpts used for commentary on the model's
reads; the article stores themselves are not distributed.
