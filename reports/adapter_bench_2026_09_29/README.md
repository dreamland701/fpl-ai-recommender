# Adapter decomposition + 21-window decision bench (2026-09-29)

CPU-only analysis on decodes already on disk. Nothing live was changed.

## Results

**1. What the E19 adapter's points delta is.** 42% (1gw) / 30% (5gw) of its
variance is a per-week linear shrink on the classic baseline. That shrink
alone delivers ~90% of the MAE gain (1gw MAE: classic 2.2716, shrink-only
2.1478, full adapter 2.1358, player-specific remainder alone 2.2590) and is
decision-neutral (shrink-only backtest = classic within 1 point per window).

**2. Availability discrimination, among likely starters (classic P>=0.5):**

| decode | classic AUC | adapter AUC |
|---|---|---|
| E19, 2025-26 GW27-38 (late season) | 0.547 | 0.717 |
| E9, 2025-26 GW2-30 | 0.645 | 0.658 |
| E7-chrono, 2023-24 GW12-38 | 0.628 | 0.656 |
| E7-chrono, 2024-25 GW12-38 | 0.634 | 0.675 |
| LIVE 2026-27 GW2-5 (E11-full) | 0.673 | 0.673 |

Live evidence coverage is not the cause (95% of live rows carry evidence vs
83-86% in the training-era eval sets).

**3. Decision backtests vs classic+F6 (points per 4-week window).**
V3 = points x (LLM P / classic P), clamped [0.6, 1.4], divided by the week's
mean ratio (pre-registered in `make_availnorm.py` before any backtest of it).

| set | windows | raw adapter | V3 |
|---|---|---|---|
| E19 GW27-38 | 3 | +9 (1/3) | **+52 (3/3)** |
| E9 2025-26 GW2-25 | 6 | +16 (2/6) | +42 (2/6) |
| E7c 2023-24 GW12-35 | 6 | -39 (2/6) | +136 (4/6) |
| E7c 2024-25 GW12-35 | 6 | +53 (4/6) | -65 (3/6, one -111) |
| **all** | **21** | **+39** | **+165 (12/21)** |

Other E19 variants: de-shrunk points +28 (1/3); raw availability_scaled -18;
evidence-gated -5; shrink-only -1.

**4. Noise.** Per-window sd of the deltas: raw adapter 24.3, V3 39.6 — not
the 14.9 measured for small anchor tweaks. Adapter-vs-classic comparisons
diverge the drafted squad far more. Raw adapter over 21 windows: mean +1.9
per window, 95% CI roughly -9.5..+13.3 (about -2.4..+3.3 per gameweek).
Caveat: 18 of the 21 windows use older adapters trained against the pre-F6
anchor and applied on the F6 anchor.

## Reproduce

```
cd /home/wescheng/projects/fpl/fpl
PY=/home/wescheng/venvs/fpl-gemma-lite/bin/python
B=reports/adapter_bench_2026_09_29
$PY $B/decompose_e19.py                      # decomposition + E19 variant files
$PY $B/make_availnorm.py                     # E19 V3 file
$PY $B/make_availnorm.py <eval.jsonl> <sft_predictions.jsonl> $B/e9_pred_availnorm.jsonl   # and e7c2324_, e7c2425_ (paths in run_replication.sh)
$B/run_variants.sh                           # 18 backtests, ~30 s
$B/run_replication.sh                        # 54 backtests, ~90 s
```

`gw6_forecast.py` builds the classic+F6 GW6 frame without touching data/
(output saved here as `gw6_2627_classic_f6_forecasts.jsonl`, snapshot of the
API on 2026-09-28); `haaland_routes.py` costs every 1-3 transfer route from
the post-GW5 squad.
