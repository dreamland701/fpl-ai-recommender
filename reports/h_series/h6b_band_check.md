# Band delta check (reports/llm_residual_v2_e22_top96_ts2n_thru_2526_26_eval_2526_27_38/eval.jsonl, reports/llm_residual_v2_e22_top96_ts2n_eval_2627_2_6/eval.jsonl; 1632 rows; Isak-pattern rows 5)

| band (fc min) | n | classic Δpts (real−fc) | h5 Δpts | h6b Δpts | classic Δmin | h5 Δmin | h6b Δmin |
|---|---|---|---|---|---|---|---|
| 0-45 | 47 | -0.02 ± 0.63 | -0.29 | -0.08 | +2.0 | -1.9 | +0.1 |
| 45-60 | 80 | -0.12 ± 0.79 | -0.08 | +0.01 | +8.2 | +0.5 | +2.2 |
| 60-72 | 316 | +0.16 ± 0.40 | -0.08 | -0.01 | +3.3 | +0.3 | +1.5 |
| 72-80 | 480 | +0.12 ± 0.30 | -0.09 | -0.07 | +1.1 | -0.1 | +0.2 |
| 80-86 | 377 | -0.16 ± 0.31 | -0.07 | -0.06 | -0.9 | +0.1 | +0.0 |
| 86-91 | 259 | -0.23 ± 0.48 | -0.10 | -0.21 | -6.8 | -0.7 | -1.2 |
| Isak pattern | 5 | -0.13 ± 2.74 | -0.31 | -0.07 | +21.3 | -1.0 | +2.1 |

corr(adapter Δpts, classic residual) / corr(adapter Δmin, classic minutes residual):
- h5: pts +0.096, minutes +0.152; sd of Δpts 0.124, sd of Δmin 1.92
- h6b: pts +0.141, minutes +0.218; sd of Δpts 0.180, sd of Δmin 2.88
