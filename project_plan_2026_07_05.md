# FPL 2026-27 LLM Predictor — Project Plan

Written: 2026-07-05
Status: APPROVED 2026-07-05 (with clarifications below)
Predecessor: `project_summary_2026_07_03.md`

Approval clarifications from Wes:

- The **fine-tuned LLM is the load-bearing component** of the system. Classic ML is welcome as an input *signal* (one feature among several the LLM reads), not as the authority the LLM merely nudges. Framing shift: instead of "classic ML forecast + small LLM correction," the target is "LLM forecast that consumes classic ML output as one of its signals." The residual/anchored parametrization remains the training trick (it demonstrably stabilizes learning), but success is measured by what the SFT model contributes.
- If Sky podcast MP3 download/transcription proves hard, skip it and lean on the other sources (Guardian API, BBC, PL/Scout backfill, FPL API crowd signals).
- Runway confirmed: 1+ month before the 2026-27 season starts.
- Model: `google/gemma-4-E4B-it` (effective-4B, ~8B raw params) — the 4B-class member of the Gemma 4 family; downloadable without gating.

## 1. Objective and Deadline

Two goals, in priority order:

1. **A working weekly predictor for the 2026-27 season**, usable from GW1: every gameweek it recommends transfers, captain/vice, starting XI, bench order, and chip usage, with cited reasoning.
2. **A genuine validation of LLM fine-tuning** — the LLM must be a load-bearing component (reading text evidence and adjusting forecasts), not a wrapper around classical ML. Classical ML stays as the anchor/baseline, per the residual architecture already validated as the most promising direction.

Hard deadline: **2026-27 GW1 deadline, expected ~mid-August 2026** (typically the second Friday of August, so roughly Aug 14). That gives us **~6 weeks**. The plan is organized so that a usable end-to-end system exists by week 4, and weeks 5-6 are polish + live rehearsal.

## 2. Where We Are (evidence-based)

- The 31B anchored reranking experiment is **complete and closed**. Checkpoint-160 GW26 eval: classic ML value/example 76.69, base Gemma 77.05, SFT Gemma 72.92 (top1 accuracy dropped 0.30 → 0.125). The SFT model learned format perfectly (128/128 strict JSON) but *degraded* decisions. Combined with ~16 min/step training cost, 31B listwise reranking is a dead end for now.
- What has been proven to work: the structured data layer, the classic ML baseline, strict-JSON learnability, the timestamp-safe evidence pipeline, and residual forecasting showing genuine promise (SFT residual improved 3GW/5GW RMSE in the GW1-10 pilot: 6.85→6.53, 9.80→8.55).
- What failed both times it was tried: letting the LLM freely override the baseline on noisy single-GW outcomes.
- Data on disk: `data/fpl_history/` covers **2019-20 through 2025-26**; `data/fpl_training_rows.csv` has ~184k player-week rows. Evidence corpus covers 2025-26 GW1-30 (PL/FPL Scout full text, Sky podcast RSS summaries, Google News backfill).

## 3. Model Choice: Gemma 4B (recommendation)

Switch the mainline from `google/gemma-4-31B-it` to the **4B instruction-tuned Gemma** for all iteration.

Rationale:

- The task is bounded: read a structured snapshot + short evidence packet, emit strict-JSON residual corrections. This is calibration + extraction, not open-ended reasoning. Small models handle constrained, well-formatted tasks close to large ones — and our own results show the 31B's size bought us nothing (it *lost* to classic ML).
- Iteration speed is the binding constraint. ~8x fewer parameters plus shorter sequences should take a training step from ~16 min to well under a minute — meaning **a full experiment (train + eval) per day instead of per fortnight**. Objective design, clipping bounds, evidence formats, and data mixes all need many cycles; that's where the wins are.
- Inference for weekly use also matters: in-season we need ~600 player forecasts before each deadline. 4B makes that minutes, not hours.
- Escalation path: once the objective is proven on 4B (Phase 3 gate), optionally rerun the single best recipe on a mid-size Gemma (~12B) as a one-shot "does scale add anything" check. Never iterate on the big model.

Practical speedups alongside the smaller model: bf16 LoRA (QLoRA fallback if memory-constrained), shorter max sequence length (compact evidence packets, target ≤2048 tokens), batch size >1 now feasible, no gradient checkpointing.

## 4. Architecture (unchanged, now made concrete)

```
classic ML forecast (anchor)
  + timestamp-safe evidence packet
  + Gemma-4B residual adjustment (clipped)
  + legal optimizer (transfers / captain / bench / chips)
  + cited explanation report
```

Core example unit: `player × gameweek × pre-deadline snapshot`, with the strict residual JSON schema from the summary doc (expected points 1/3/5GW, minutes, appearance probability, bounded deltas, confidence, risk flags, reason).

Two leakage rules enforced mechanically in the dataset builder, not by convention:

- All features/evidence must satisfy `available_at <= deadline_ts` of the target GW. Evidence rows carry `published_at`; anything missing a trustworthy timestamp is excluded from training.
- **Double gameweeks**: labels are computed per *deadline window* — points from all fixtures whose kickoff falls between this deadline and the next, regardless of the fixture's nominal GW. A unit test locks this in for known 2025-26 DGWs.

Residual clipping (the key lesson from every failed run): deltas clipped both in training labels and at inference parse time. Starting bounds: ±2.0 pts (1GW), ±4.0 (3GW), ±6.0 (5GW); treated as a tunable hyperparameter. A confidence-weighted shrink (`delta * confidence`) is a cheap variant to test.

## 5. Phases

### Phase 1 — Small-model residual mainline (weeks 1-2)

The core experiment loop. Everything else supports this.

1. **Expanded multi-season residual dataset.** Train window: 2022-23, 2023-24, 2024-25 full seasons + 2025-26 GW1-11. Older seasons (2019-22) held in reserve — COVID schedules and missing xG/defensive-contribution fields make them noisier; add only if data volume proves limiting. Evidence-poor historical weeks are kept (with an explicit `evidence_present: false` marker) so the model learns to output ~zero delta when there's nothing to read.
2. **Rolling chronological eval, 2025-26 GW12-30.** To score GW `n`: train on prior seasons + 2025-26 GW1..(n-1). In practice: train one model on the base window, then evaluate GW12-30 with per-GW snapshots; periodic re-trains (e.g. every 6 GWs: GW12, GW18, GW24 models) approximate true rolling retraining at affordable cost. GW31 stays excluded.
3. **Gemma-4B LoRA training pipeline** — reuse `train_gemma_sft.py` (env-driven, model id is already configurable), new runner scripts, higher batch size, seq len 2048.
4. **Experiment ladder** (each ~1 day on 4B):
   - E0: base 4B, no SFT (control — does the small base model parse/behave?)
   - E1: residual SFT, structured features only (no text) — isolates whether text is doing anything
   - E2: E1 + compact evidence packets
   - E3: E2 + clipping-bound / confidence-shrink sweep
   - E4 (stretch): multi-task — availability/minutes head alongside points residual
5. **Metrics**, logged identically for every run: 1/3/5GW RMSE+MAE, minutes RMSE, appearance-probability calibration, rank correlation, top-k lift vs classic ML, strict-JSON rate. Acceptance is per the summary doc: parity-or-better RMSE **plus** top-k lift **plus** downstream optimizer gain — not "beats ML everywhere."

### Phase 2 — Evidence & signal expansion (weeks 1-4, parallel track)

Ordered by (consistency across seasons × signal density × effort):

1. **Sky podcast transcripts** (user's specific ask — yes, feasible). The RSS feed exposes MP3 enclosures; archives typically go back years. Pipeline: download enclosures → transcribe locally on the Spark with `faster-whisper` (large-v3, batched; the GB10 will chew through a full season of weekly ~45-min episodes in a few hours) → segment by player/team mentions → timestamp = episode publish time. First step is an audit script: how far back does the feed actually go, and is episode cadence consistent since 2021-22? If the feed truncates, check archive.org podcast snapshots before giving up.
2. **Guardian football articles via the Guardian Open Platform API.** Free API key, full article text, reliable timestamps, consistent format **back well past 2021-22**, and it's a mass-readership source — exactly the consistency criterion. This is likely the single best historical-text addition available at zero cost.
3. **BBC Sport football** (team news + the daily gossip column): RSS/pages consistent for a decade, very widely read. Scrape respectfully with timestamps.
4. **More PL/FPL Scout historical bodies** — extend the existing canonical-URL resolution backfill to 2022-25 seasons.
5. **Crowd sentiment — from the FPL API itself, not social media.** Ownership %, transfers in/out per GW, price changes: this *is* "what popular opinion thinks," it's perfectly timestamped, identically shaped since 2016, and already partially in the feature table. Add derived features: net-transfer momentum, ownership-change z-score, price-change direction.
6. **Reddit r/FantasyPL** (stretch, clearly separated): historical dumps exist via Arctic Shift/Academic Torrents; weekly "Rate My Team"/pre-deadline threads give a crowd-consensus signal. Only if time permits, tagged `source_type: social_noisy`, never mixed into curated evidence.

**The sentiment-vs-expert-vs-performance study** (user's mining idea): a standalone analysis notebook/report, built on the eval window, correlating (a) crowd signals (net transfers, ownership deltas, price moves), (b) expert signals (Scout picks, podcast/article mention sentiment), (c) classic ML forecast, against realized points. Questions: does crowd momentum add anything over the ML baseline? Are experts differentially right about rotation/availability vs upside? Findings feed back as features and/or evidence-packet fields in E2/E3, and the report itself is a deliverable (`reports/signal_study_2025_26.md`).

Every source gets a row in a **coverage matrix** (season × source × weeks-covered × full-text-vs-snippet) checked into `docs/`, so "is this source consistent back to 21-22" is answered by data, not memory.

### Phase 3 — Downstream integration & season backtest (weeks 3-5)

1. Wire residual-adjusted forecasts into the existing optimizer/decision engine (`hybrid.py` path).
2. Rolling GW12-30 squad backtest: LLM-adjusted vs classic-ML-only, tracking weekly points, transfer value after hits, captain points, bench correctness, season total.
3. **Gate**: LLM-adjusted pipeline must be ≥ classic-ML-only on season-total points over GW12-30. If it fails, ship classic-ML-only as the GW1 default with the LLM in shadow mode (logging its counterfactual picks) — the season launch does not slip.
4. Optional: one 12B run of the winning recipe.

### Phase 4 — 2026-27 season readiness (weeks 4-6)

1. **New-season ingest**: 2026-27 bootstrap (new player IDs, promoted teams, prices) lands via the existing FPL API ingest as soon as the game launches (usually early-to-mid July — worth checking now). Cold-start features: previous-season aggregates for returning players; for transfers-in/promoted players, explicit `history_missing` flags + evidence-packet reliance. ID mapping across seasons handled and tested.
2. **Weekly runbook — one command**: `fpl-ai weekly --gw N` → fetch latest FPL data → build pre-deadline snapshot → classic ML forecast → build evidence packets (last 7 days, timestamp-filtered) → Gemma-4B residual pass → optimizer → markdown report: recommended transfers (with hit math), captain/vice, XI + bench order, chip advice, and per-decision citations into the evidence.
3. **Automation**: scheduled run ~48h and ~6h before each GW deadline (cron on the Spark), report written to `reports/weekly/2026-27/`.
4. **In-season learning loop**: after each GW completes, append rows + evidence; re-SFT the residual model every ~6 GWs (cheap on 4B); keep a fixed holdout discipline (never eval on GWs seen in training).
5. **Live rehearsal**: run the full weekly pipeline against preseason data at least twice before the real GW1 deadline.

## 6. Success Criteria

| Level | Criterion |
|---|---|
| Model | Residual SFT ≥ classic ML on 3/5GW RMSE **and** positive top-k lift on rolling GW12-30 |
| Decision | LLM-adjusted optimizer ≥ classic-ML-only on GW12-30 season total |
| Product | One-command weekly recommendation with citations, running on schedule before every 2026-27 deadline from GW1 |
| Learning | Written comparison of what fine-tuning bought (format, residual quality, evidence use) vs base model and vs classic ML — the "did LLM fine-tuning work" answer, with numbers |

## 7. Risks

- **FPL API/schema changes for 2026-27** (new scoring rules have happened before, e.g. defensive contributions). Mitigation: ingest is versioned per season; check rule changes at game launch.
- **Sky feed doesn't reach back to 2021-22** → Guardian/BBC become the historical text backbone; Sky transcripts still used from 2025-26 onward.
- **Text evidence adds nothing** (E1 ≈ E2) → the honest finding is itself goal #2 output; pivot LLM value to availability/rotation calls and explanation quality, where text plausibly matters most.
- **Cold-start GW1-5**: forecasts for promoted/new players are weak for everyone; lean on preseason evidence packets and conservative optimizer settings (bank transfers early).
- **Small-model ceiling**: if 4B can't learn the residual task at all (E1 clearly worse than base), step to the ~12B mid-size once — still ~4x faster than 31B.

## 8. Immediate Next Actions (upon approval)

1. Write the Gemma-4B runner + verify a 100-step smoke train on the existing GW1-25 residual dataset (establishes real step-time on the Spark).
2. Build the multi-season residual dataset + rolling GW12-30 split generator (with the DGW-window label fix and unit tests).
3. Start the Sky RSS audit + Guardian API key/backfill scripts in parallel.
4. Check whether the 2026-27 FPL game has launched and pull the bootstrap if so.
