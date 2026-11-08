# Iteration plan 2026-10-15: SFT and RL runs (GW7 set, GPU go-ahead for 5–6 runs)

Wes, 2026-10-15: "keep thinking and iterating ways to improve the model, both the SFT and RL part … execute on GPU
without asking my approval … 5-6 GPU runs until pausing". This file is the design, the gates and the decision rules;
results are appended as they land. Everything scores on the fixed pipeline (status-backfilled table, per-fixture 1GW
heads, MILP draft), the production forecaster since 2026-10-14.

## 1. Where the SFT/RL layers stand

Three weeks of evidence on the adapters and the RL layers, all on the fixed pipeline:

- The token-trained residual adapters (E19/E20/E21) are **median estimators**: greedy decoding returns the mode of a
  digit-token distribution, so the written deltas shrink the classic forecast. Expectation decoding recovers the mean
  but lands level with classic+F6 (992 vs 995 over 4 windows) and costs ~3.5 s/row.
- Their only measurable edge is **availability**, late in the season and from team-news text inside the last 24 h;
  a logistic P(appear) on structured features beats the LLM's P(appear) (AUC 0.744 vs 0.717 on E19).
- **Every adapter so far trained with an empty official-news line.** Historical status/news did not exist in the
  table until the 2026-10-14 backfill; the prompts said "Status pre-deadline: none / Official player news pre-deadline:
  none" on every 2022–26 row, while live rows carry the real line. The one text channel that is train/live-consistent
  and timestamp-exact was never in the training corpus.
- RL: chip timing is closed (planner at the forecast-information ceiling, G10); transfer-choice RL flat (G3);
  RL-on-forecasts with a decision-value reward failed (G4: ~70% zero-advantage groups, reward sd ≫ signal). Wes's
  direction (10-13): RL only where the signal is low-noise; forecasts are a baseline to subtract, never a reward.

## 2. Diagnosis and the runs

| Run | What | Why (prior) | Cost |
|---|---|---|---|
| P0 | LoRA throughput probe (`scripts/probe_lora_throughput.py`) | E21 trained at 6.4 s/row; module-LoRA vs ParamWrapper, batch sizes | 25 min (see §4) |
| **H1** | **Regression-head LoRA** on the **E22 corpus**: Gemma-4-E4B + module LoRA, 5-output head on the final hidden state; Huber on standardised point/minute residuals, cross-entropy with the classic P(appear) as logit offset. Prompt compacted (format instructions removed, −34% tokens). `train_gemma_reghead.py`, `src/fpl_ai/reghead.py`, `scripts/reghead_predict.py` | Fixes the median defect at the loss (mean-targeted), one forward per row at inference (the decision bench becomes affordable), and the first adapter that sees the official news line with the production baseline in the prompt | ~9.5 h train + 10 min predict |
| **R4** | **GRPO on availability with a verifiable reward**: policy reads the E22 prompt + "will he play ≥1 min?", answers `{reasoning, p_play}`; reward = Brier improvement over the classic P(appear), (y−b)² − (y−p)², unparseable −0.5; 1,200 prompts where text could matter, 6 samples, KL β 0.04. `train_gemma_grpo_avail.py`, `src/fpl_ai/avail_rl.py` | The one RL formulation that satisfies Wes's rule: low-noise binary label, baseline subtracted, credit only where the text changes the answer. Tests whether reasoning extracts more from team news than the supervised head (H1) | ~5 h + zero-shot/trained reads |
| **R5** | **31B zero-shot availability reader** (4-bit) on the same rows | Ceiling for "reading" without training; interprets R4 | ~2 h |
| **H2** | H1 recipe on the **old E21 corpus** (no official news, old baseline) | Completes the 2×2 with E21-token: head effect vs corpus/news effect | ~9.5 h |
| H3 | contingent (see §5) | | |

Corpus: `scripts/run_e22_corpus.sh` → `reports/llm_residual_v2_e22_top96_thru_2526_26_eval_2526_27_38` (13,440 train /
1,152 holdout rows) and `..._eval_2627_2_6` (480 live rows). 90% of training rows carry an official status, 26% a news
line; the 2025-26 holdout weeks carry status only in GW30-31 (vaastav snapshots), so holdout prompts mostly say
"none" (= unknown) while live rows are complete; `a` (available) and "none" (unknown) are distinguishable in the prompt.

## 3. Protocol and gates

- Accuracy ledger (`scripts/track_sft_accuracy.py`): holdout 2025-26 GW27-38 and live 2026-27 GW2-6, classic vs adapter.
- Availability: AUC and Brier, all rows and the uncertain subset (classic P(appear) in 0.15–0.95), classic vs head
  vs R4 policy vs 31B (`scripts/avail_auc_from_preds.py`, `scripts/avail_policy_eval.py`).
- Decisions: the E21 protocol, 3 holdout windows + live GW2-6, with the classic reference re-run under the production
  flags (`reports/h_series/bt_classic`). Noise floor: adapter per-window sd 24–40, so only a gap > ~60 over the 4
  windows is a signal; anything smaller is "level" and the run is judged on accuracy and availability.
- Ship gate unchanged: 21-window bench before any live use; nothing from this plan touches GW7.

## 4. Infrastructure findings (2026-10-15)

- P0: training is compute-bound at ~210 tokens/s regardless of batch (b1 4.59 s/row, b2 5.05, b4 7.24 per row at
  ~1,060 tokens); module LoRA is 23% faster than ParamWrapper LoRA; no checkpointing saves ~30% (2.6 vs 3.9 s/row at
  600 tokens). The 34% prompt compaction is the real lever.
- **Global OOM at 09:32** from the probe's batch-4/no-checkpoint config: the systemd MemoryMax cap does not cover GPU
  unified-memory allocations; the kernel killed Xorg, gnome-shell, the user managers and the Claude session. Rules
  now: one GPU job at a time, planned peak ≤ ~55 GB, never probe limits. `user@1000.service` is failed until
  `sudo systemctl start user@1000.service`; jobs run as detached `nohup setsid` processes with pids in `logs/pids/`.
- Queue: `scripts/run_h1_chain.sh` (H1) → `scripts/run_gpu_queue_1015.sh` (R4 → R5 → H2). Logs `logs/h1_chain.log`,
  `logs/train_h1.log`, `logs/r4_chain.log`, `logs/r5_chain.log`, `logs/h2_chain.log`, `logs/gpu_queue_1015.log`.

## 5. Decision rules for H3 (the sixth run)

- H1 beats classic on decisions by > 60 and on holdout RMSE → H3 = H1 with 2 epochs / r=32 and the live GW2-7
  re-score once GW7 settles (candidate for the shadow slot, then the 21-window bench on CPU with its predictions).
- H1 level on decisions but its P(appear) head beats the logistic head on the uncertain subset → H3 = availability-
  only head (`FPL_RH_FIELDS=availability`) on all rows, evaluated under the soft-availability optimizer.
- R4 beats both the classic and H1's head on Brier in the uncertain subset → H3 = R4 with 2× prompts and the H1 prompt
  (points) reward replaced by the same Brier form on minutes bands; otherwise R4 is closed like G4.
- Nothing beats classic → stop the SFT/RL line for the season; the remaining lever is data-flow audits (parity audit
  every packet) and the hit-policy calibration in §6.

## 6. CPU work in parallel: transfer-gain calibration (hit policy)

Projected wildcard gains were shown not to realise (+16.8 projected → −0.7 realised). The same question for ordinary
transfers decides every −4 (this week's Haaland route): for each transfer the backtests took, realised gain = points
of the player bought minus points of the player sold over the horizon, against the projected gain. The slope gives the
hit rule: take a hit only when projected × slope > 4. Output: `reports/transfer_calibration/`.

### 6.1 Result (2026-10-15 13:15): free-transfer projections are calibrated; hits are decision-neutral

`scripts/transfer_gain_calibration.py` over the 21-window bench (`reports/transfer_calibration/summary.md`), production
forecaster (ST1_F/MP1_F = per-fixture, MILP draft):

- The single free transfers the engine took (49–54 per config) projected +4.5 to +4.7 over 3 GWs and realised +4.4
  to +5.7 (± 1.4); slope of realised on projected 1.0–1.2 (± 0.45). Unlike wildcard projections (+16.8 → −0.7),
  ordinary transfer projections realise at face value.
- Hits were never taken on the bench (max one transfer per week). Allowing a second transfer at −4 whenever its net
  projected gain is the best option (HT2_F, `--max-transfers-per-week 2`): +6 over 21 windows (11/3/7, t 0.13),
  4 hits taken in 84 weeks, realised +11.8 ± 12 before the hit (projected +8.1). Requiring net gain ≥ 2 (HT2G_F): −22.
  All 50 two-transfer options listed (taken or not): forecast Δ3 +9.5, realised +8.2 ± 2.3, i.e. ~85% before the hit
  and +7.5 net, against +5.9 for the free single moves actually taken.
- Reading for the weekly sheet: a −4 route whose projected gain (net of the hit) is well above the best free move is
  not a projection artefact; the GW7 Haaland route (+15.6 net over 5 GWs, forecast Δ5 ≈ +19.6) sits in the top
  projection bin, which realised +17 over 3 GWs (n = 23). Keep the current rule: take the hit when the exact optimizer
  says it beats the free move by a clear margin; do not add a stricter threshold (HT2G_F loses).

## 7. H1 result (2026-10-15 20:08) and the queue change

Trained 840 steps (13,440 rows, 6.6 h, batch 1 / no checkpointing / accumulation 16, 28.4 s per step). Predictions in
one forward pass: 0.6 s per row (the token adapters needed 3.5 s with expectation decoding). Ledger
`reports/h_series/h1_accuracy.md`, predictions `h1_{holdout,live}_pred.jsonl`, backtests `reports/h_series/bt_*`.

| Channel | Holdout 2025-26 GW27-38 (1,152 rows) | Live 2026-27 GW2-6 (480 rows) |
|---|---|---|
| Points RMSE classic / H1 | 3.420 / 3.419 | 3.424 / 3.441 |
| Points MAE classic / H1 | 2.609 / 2.557 | 2.614 / 2.568 |
| Points bias classic / H1 | +0.10 / −0.15 | −0.23 / −0.47 |
| P(appear) AUC classic / H1 | 0.704 / 0.771 (uncertain rows 0.574 / 0.706) | 0.645 / 0.760 (uncertain 0.701 / 0.855) |
| P(appear) Brier classic / H1 | 0.0767 / 0.0604 | 0.0444 / 0.0252 |
| Decisions, all deltas | 750 vs classic 788 (−38) | 335 vs 315 (+20) |

- **Points: null, and the Huber loss re-created the shrink.** The written 1GW delta is a constant −0.24 (sd 0.11, slope
  on the baseline 0.00, correlation with the realised residual +0.04). Replacing every delta with its linear fit on the
  baseline gives the same RMSE/MAE. The training regression loss never fell below the constant-prediction level
  (1.66 → 1.41 over 840 steps). Standardised Huber (δ = 1) treats the hauls as outliers, so the estimate sits between the
  mean and the median, exactly the defect the head was meant to fix; the text added no player-specific points signal
  with the official news line present (26% of training rows) and the production baseline in the prompt.
- **Availability: the strongest read any adapter has produced**, and it does not come from the status line. The holdout
  carries status for GW30-31 only (960 of 1,152 prompts say "none", 2 have a news line) and still gains +0.074 AUC on
  the "none" rows; rows with text evidence gain +0.078, rows without lose −0.015 (n 189). Two parts: the classic
  P(appear) is under-confident on regular starters (bin 0.5–0.8 says 0.72, they play 92%; bin 0.8–0.95 says 0.88, they
  play 94%) and the head recalibrates it; and a genuine ranking gain on the uncertain rows (0.57 → 0.71, 0.70 → 0.85).
  So H2 (the same head on the E21 corpus without the status line) would answer a question already answered: dropped
  (`logs/SKIP_H2`), its GPU time goes to H3.
- **Decision value is unproven.** Through the production optimizer the availability deltas are inert by construction
  (threshold penalty below P = 0.65 only): holdout 788 = 788 on all three windows, live +37 from four near-tie lineup
  swaps (De Cuyper/Groß in, Wissa/Calvert-Lewin out). The principled coupling, unconditional points = P × conditional
  points, so rescale the classic points by P_head / Platt(P_classic) (`scripts/avail_couple_preds.py`, Platt a +1.52
  b 0.87 on the training rows), gives holdout 822 vs 788 and live 335 vs 315: +54 over 4 windows, but the diff shows
  it is again tie-breaks among near-equal starters moved by −0.1…−0.6 deltas, not "he will not play" calls (only
  16 holdout + 11 live rows have a ratio below 0.7, and they rarely sit in the squad). The soft optimizer changes
  nothing here (classic 781 / Platt 782 / H1 782 vs 788 threshold).

| 4-window arm (holdout 3 windows + live) | Holdout | Live |
|---|---|---|
| classic, threshold optimizer | 788 | 315 |
| H1 all deltas | 750 | 335 |
| H1 availability only, threshold | 788 | 352 |
| H1 availability → points via Platt ratio, threshold | 822 | 335 |
| classic / Platt-only / H1 availability, soft optimizer | 781 / 782 / 782 | 315 / 315 / 352 |

**H3 (6th run, armed behind R5): availability-only head on all players.** Rule 2 of §5 applies (level on decisions,
head beats the classic P(appear) by far more than the logistic head's +0.007). On the top-96 universe non-appearance is
rare (5–10%) and rarely in the squad; on the uncertain rows of all players (classic P in 0.15–0.95: ~12.5k per season,
62% played) rotation, bench and enabler calls live. Design: train on 2022-23..2024-25 uncertain rows (random 16,000 of
38,700, seed 7), evaluate on all of 2025-26 GW2-38 (≈12.5k uncertain rows, the 9 bench windows) and live GW2-6; arms:
classic, head P through the threshold optimizer, Platt-ratio coupling into points, soft optimizer with/without the
head, Platt-only control. Scripts: `build_h3_splits.sh` (CPU, running), `filter_split_rows.py`, `run_h3_avail_chain.sh`,
`run_h3_queue.sh` (waits for the queue tail), `avail_ledger.py`. Veto flag: `logs/SKIP_H3`. Gate: the coupled arm
must beat classic by > 100 over the 10 windows (sd ≈ 15–40 per window) to earn a shadow slot; otherwise the
availability channel is closed for the ridge universe and the head stays an accuracy result.

Queue after the OOM relaunch: R4 (running since 20:11, zero-shot reads 3.4 s/row) → H1 shadow read on the GW7 interim
corpus (`scripts/run_gpu_queue_1015b.sh`, replaces the original queue bash from R4 onwards) → R5 → H3 → H1 read on the
GW7 final corpus once Friday's refresh has built it.

### 7.1 R4 config failure, launcher incident and the queue rebuild (2026-10-15 21:40–21:50)

- **R4 died at the GRPO config** (21:38) after its zero-shot reads: `GRPOConfig.__init__() got an unexpected keyword
  argument 'max_prompt_length'`. TRL 1.0 dropped the argument; `train_gemma_grpo.py` and `train_gemma_grpo_plan.py`
  already carried the note. Fix in `train_gemma_grpo_avail.py`: no `max_prompt_length`; the prompts are bounded by
  construction (measured on the 1,200 training prompts: mean 737 tokens, p95 890, max 1,148; rows above
  `FPL_R4_MAX_PROMPT_TOKENS` = 1,400 are dropped, bound ≤ 1,536 asserted). Chain now runs 4 generations × accum 3
  (12 completions per optimizer step as before; planned peak < 40 GB with checkpointing instead of ~50 GB at 6 × 2)
  and keeps the finished zero-shot reads. Zero-shot base E4B, for the record: holdout (963 rows) AUC 0.649 vs classic
  0.695, Brier 0.088 vs 0.081; live (480) AUC 0.673 vs 0.645, Brier 0.052 vs 0.044; uncertain rows AUC 0.574→0.605
  holdout, 0.701→0.749 live. The untrained reader ranks a little and calibrates worse than the ridge.
- **Launcher bug, two GPU jobs for ~2 minutes.** `run_h3_queue.sh` grepped the queue log for "QUEUE DONE", and its
  own armed line ("waits for QUEUE DONE") matched it, so it only waited for the pgrep guard; when R4's python died the
  guard cleared and H3 started (21:39:46) 14 s before the queue tail launched the GW7 interim shadow read (21:40:00).
  Caught at 21:41 (memory 22–31 GB used, no harm); H3's launcher, chain and trainer were killed before its first step,
  the queue tail was paused and then killed, and the shadow read finished alone (667 rows, 8.1 min). Rule: one
  sequential queue script, never log the sentinel you wait for, pgrep guards are not a substitute for ordering.
- **Queue C** (`scripts/run_gpu_queue_1015c.sh`, pid in `logs/pids/gpu_queue_1015c.pid`, log `logs/gpu_queue_1015.log`,
  sentinel "GPU QUEUE C COMPLETE"): R5 (21:50 →) → H3 (~00:00 → ~10:30 Fri) → wait for the GW7 final refresh marker
  (until 14:00 PDT Fri) → H1 read on the final corpus → R4 fixed (~2.5 h at 4 × 3) → done ~13:30–14:30 Fri. Flags:
  `logs/SKIP_R5`, `logs/SKIP_H3`, `logs/SKIP_R4`. H3's classic reference arms (CPU) already completed: 2,555 over the
  10 windows (threshold), 2,542 soft.
- **GW7 interim shadow sheet** (`reports/gw7_packet_2026_10/interim_1015/side_by_side_h1.md`, entry refreshed 21:47
  UTC-7: transfers not yet made, so B.Fernandes→McGinn and Isak→Haaland applied): classic and classic+H1 pick the
  identical XI, bench order and Haaland/Cherki captaincy. H1 writes the usual constant shrink (+0.064 × classic − 0.41)
  and small player-specific parts (Haaland −0.36, Cherki −0.28, João Pedro −0.21); P(appear) moves up for everyone
  (Saka 0.73→0.93, Groß 0.78→0.93, Konsa 0.80→0.95, De Cuyper 0.81→0.94), the recalibration seen on the holdout,
  with all 21 listed players status "a" and no out call. Final sheet follows Friday's corpus.
- **R5 speed (01:11 Fri):** the 31B 4-bit reads ran at 41 s/row (batch 4, 96 new tokens), not the ~5 s the 2-hour
  estimate assumed: 284/480 live rows after 3.3 h, ~14 h for the full 1,443. Stopped (output resumable, the reader
  appends with `--resume`) and moved last. **Queue D** (`scripts/run_gpu_queue_1015d.sh`, pid in
  `logs/pids/gpu_queue_1015d.pid`, sentinel "GPU QUEUE D COMPLETE"): H3 (01:14 → ~11:45 Fri) → GW7 final read → R4
  (~2.5 h) → R5 resume (~13 h, ends ~04:00 Sat; veto `logs/SKIP_R5`).

### 7.2 H3 result (2026-10-16 11:57): best P(appear) reader yet, decisions flat, availability channel closed

Run: 16,000 uncertain rows (classic P 0.15–0.95, random of 38,700, seed 7) of 2022-23..2024-25, availability field
only, batch 1 × accum 16, 1,000 steps / 7.9 h (28.4 s/step), BCE 0.68 → 0.36; predictions on 12,157 holdout rows
(2025-26 GW2-38) and 1,503 live rows (GW2-6) in 2.8 h. Ledger `reports/h_series/h3_availability.md`.

| Uncertain rows | AUC classic → H3 | Brier classic → Platt → H3 |
|---|---|---|
| Holdout, all (12,157) | 0.783 → 0.812 | 0.196 → 0.143 → 0.136 |
| Holdout, status flagged (247) | 0.541 → 0.726 | 0.252 → 0.305 → 0.210 |
| Holdout, no evidence (1,912) | 0.819 → 0.828 | 0.180 → 0.136 → 0.134 |
| Live, all (1,503) | 0.767 → 0.794 | 0.185 → 0.126 → 0.129 |
| Live, status flagged (82) | 0.716 → 0.842 | 0.207 → 0.322 → 0.165 |
| Live, no evidence (163) | 0.755 → 0.736 | 0.168 → 0.105 → 0.129 |

Platt recalibration of the classic P alone takes 85% of the holdout Brier gain and beats H3 on live Brier; the
head's own edge sits on the flagged/news rows (2% of the universe), where the status line and the text say something.

| Decision arm (9 windows 2025-26 + live GW2-6) | Holdout | Live | Total vs classic |
|---|---|---|---|
| classic, threshold | 2,240 | 315 | 2,555 |
| H3 availability deltas, threshold | 2,222 | 315 | −18 |
| H3 → points via Platt ratio (the gate arm) | 2,203 | 351 | −1 |
| classic, soft optimizer | 2,227 | 315 | −13 |
| H3 coupled, soft | 2,192 | 351 | −12 |
| Platt-only, soft | 2,211 | 315 | −29 |

**Verdict:** the gate (> +100 on the coupled arm) is failed by a wide margin; by §5 rule 2 the availability channel
is **closed for the ridge universe**. The live +36 is the same near-tie lineup swaps H1 showed (H1's availability
arm scored 352 on the same window); over the nine holdout windows the coupling loses 37. Accuracy on flagged rows is
real but those rows rarely sit in a squad, and the recalibration half of the gain is a one-line Platt fit, not a
reader. Remaining use: none in production; the head can read flagged players for the weekly sheet without retraining.

### 7.3 R4 result (2026-10-17 00:28): availability GRPO learns the base rate, not the text; R4 closed; R5 truncated

Run: 1,201 prompts (the holdout-training split's rows where text could matter: 97% with classic P(appear) 0.15–0.95,
93% played, classic P mean 0.77), 4 generations × accumulation 3 = 12 completions per step, 400 steps / 10.9 h
(97 s/step, 26 GB), LoRA r16/α32, lr 1e-5, temperature 1.0, KL β 0.04, 96 completion tokens, reward = Brier
improvement over the classic P (unparseable −0.5). Completions parsed 99.9%. Reads of the merged policy at 3.4 s/row:
963 "text could matter" holdout rows (2025-26 GW27-38) and the 480 live rows (GW2-6), `reports/r4_avail/r4_*.jsonl`,
trace `logs/r4_reward_trace.jsonl`, adapter `artifacts/gemma4_e4b_r4_avail_grpo`.

**Training curve.** Mean reward +0.014 (steps 0-50) → +0.044 (200-300) → +0.036 at the end. Within 50 steps the
policy stopped echoing the baseline (echo share 32% → 0%) and settled on answering p ≈ 0.97 for everyone (completion
p mean 0.84 → 0.98 against a baseline mean 0.77 and a 93% play rate). Deviating completions earned +0.031 on
average, echoes 0.000: the reward paid, at scale, for raising every answer towards the training base rate.

| Reader (same rows for all) | Holdout 963: AUC / Brier | Holdout uncertain 765: AUC / Brier | Live 480: AUC / Brier | Live uncertain 395: AUC / Brier |
|---|---|---|---|---|
| classic P(appear) | 0.695 / 0.0805 | 0.574 / 0.0888 | 0.645 / 0.0444 | 0.701 / 0.0490 |
| Platt fit of the classic P on the 1,201 training prompts (a 1.27, b +1.33) | 0.695 / 0.0667 | 0.574 / 0.0710 | 0.645 / 0.0243 | 0.701 / 0.0245 |
| E4B zero-shot, same prompt | 0.648 / 0.0881 | 0.605 / 0.0843 | 0.673 / 0.0519 | 0.749 / 0.0573 |
| **R4 trained policy** | 0.647 / 0.0859 | 0.630 / 0.0700 | 0.694 / 0.0368 | 0.752 / 0.0392 |
| R4 gated to the uncertain rows | — / 0.0656 | 0.630 / 0.0700 | — / 0.0363 | 0.752 / 0.0392 |
| H1 regression head (§7) | 0.773 / 0.0638 | 0.725 / 0.0676 | 0.760 / 0.0252 | 0.855 / 0.0257 |

- **Mechanism.** On holdout the policy moved 680 of 963 rows by ≥ 0.05, 664 of them up (mean +0.18). The 27 rows the
  classic puts at ≤ 0.15 (none played; such rows were absent from training) get p = 0.75 → Brier 0.72, which is the
  whole of the all-row loss. Its 15 downward calls on holdout were good (played 40%: Damsgaard, Wirtz, Amad, Palmer,
  Enzo, Sesko…), its 23 on live were wrong (played 96%: Miley ×4, Gibbs-White ×3, Semenyo, Sávio…).
- **Against the controls.** A one-line Platt fit matches R4 on the holdout uncertain rows (0.0710 vs 0.0700) and beats
  it by a wide margin on live (0.0245 vs 0.0392). R4's ranking gain on the uncertain rows (+0.056 / +0.051 AUC) is
  real but H1's head has +0.151 / +0.154 on the same rows, better Brier everywhere, and no damage to the confident
  rows (0.0487 vs classic 0.0486; R4 0.1474).
- **Verdict: R4 closed** (§5 rule: "otherwise R4 is closed like G4"). With a low-noise, baseline-subtracted reward the
  policy still converged on the baseline's calibration defect, because that defect is the dominant systematic reward
  source and the text-specific credit (a dozen right downward calls per thousand rows) is too thin to learn from
  1,200 prompts × 12 samples. The supervised head extracts more from the same prompts in 6.6 h for five fields than
  GRPO does in 10.9 h for one. Fifth RL formulation to lose to a cheaper supervised or analytic baseline (G3
  transfers, G4 forecasts, G7–G10 chips, R4 availability); RL at the decision layer stays closed.

**R5 (31B-it 4-bit zero-shot, same prompt): invalid as run, and negative where it answered.** 41.7 s/row; live 480
rows done 02:53 Sat, holdout 963 rows done 14:13 Sat, "GPU QUEUE D COMPLETE" 14:13:55, GPU idle since. 53% of live
and 60% of holdout completions do not parse, and every unparsed one ends without the closing brace: the 31B writes a
"thought" preamble and the 96-token completion cap cuts it before `p_play` (the E4B answers inside ~90 tokens). On
the rows it did answer it is far worse than the classic P: holdout (381 rows, 87% played) Brier 0.0718 → 0.2155,
AUC 0.798 → 0.737; live (226 rows, 99% played) Brier 0.0307 → 0.1413, AUC 0.708 → 0.729. It moves probabilities
down for players who play. Not re-run; the model decision is §7.4.

**GW7 (checked 10:46 PDT Sat with `gw_status`): in play, not settled** (5 of 10 fixtures under way). The entered team
matches the accepted route: Isak → Haaland and B.Fernandes → McGinn made 2026-10-15 02:47 UTC (−4), C Haaland,
VC Cherki, XI/bench as the final packet, bank 0.2, no chip. Friday's refresh showed the pre-transfer squad because the
public API hides the upcoming gameweek's transfers and picks until its deadline.

### 7.4 Reader-model decision (2026-10-17, Wes delegated the call): keep E4B, no 31B re-read, no model swap

What the "31B re-read" was: R5 = Gemma-4-31B-it (the largest Gemma 4, 30.7B dense), untrained, in bitsandbytes
4-bit, asked R4's question on R4's rows to measure the ceiling of pure reading; it failed mechanically (96-token cap)
and a corrected pass costs ~16 h at 41 s/row. Not re-run.

The model landscape under 31B (Hugging Face, checked 10-17): Gemma 4 has E2B, E4B, **12B dense** (released
2026-05-23, 24 GB bf16), 26B-A4B MoE (4B active, ~52 GB bf16) and 31B, all with a **January 2025 training cutoff**.
Outside Google the current picks are Qwen3.8-27B (2026-08-05, dense hybrid DeltaNet, thinking on by default, 54 GB
bf16 = at this box's one-job limit), Qwen3.6-27B / 3.6-35B-A3B (April 2026) and gpt-oss-20b (2025-08-04, 3.6B
active, cutoff June 2024, ~42 GB bf16 after MXFP4 dequant).

Why no swap: (1) any model finished after mid-2025 has read the 2025-26 season, so our holdout (2025-26 GW27-38 and
the 9 bench windows) is contaminated for it; only Gemma 4 and gpt-oss are clean, and the clean live set (480 rows,
~12 non-plays) cannot resolve anything for a year. (2) The base model is not the bottleneck: four SFT recipes and the
regression head found no player-specific points signal in text (the market already prices the articles), the best
availability reader (H3) is decision-flat, and the 31B expert reader's start_risk gain (AUC 0.63 vs 0.48) reversed
on live. A stronger reader reads the same official news line. (3) The one-job memory rule (≤ 55 GB) rules out
training anything above 12B in bf16, and 4-bit training is the slow path on this box.

Decision: Gemma-4-E4B stays the SFT/head base and the H3 head stays the weekly-sheet reader; no GPU run is scheduled.
Reopen only if a decision bench shows availability reads converting into points (e.g. bench-boost/DGW weeks); the
test then is the H3 recipe on Gemma-4-12B (same family, same cutoff, 24 GB), not a zero-shot big model. Infrastructure
item worth doing before any further GPU work: a CUDA 13 torch build with sm_121 kernels (the current build warns the
GB10 is above its supported capability; bnb 4-bit at 41 s/row is the symptom).
