# Band delta check (reports/llm_residual_v2_e22_top96_ts2n_thru_2526_26_eval_2526_27_38/eval.jsonl, reports/llm_residual_v2_e22_top96_ts2n_eval_2627_2_6/eval.jsonl; 1632 rows; Isak-pattern rows 5)

| band (fc min) | n | classic Δpts (real−fc) | h5 Δpts | h6 Δpts | h12 Δpts | classic Δmin | h5 Δmin | h6 Δmin | h12 Δmin |
|---|---|---|---|---|---|---|---|---|---|
| 0-45 | 47 | -0.02 ± 0.63 | -0.29 | -0.43 | -0.13 | +2.0 | -1.9 | -3.2 | +0.8 |
| 45-60 | 80 | -0.12 ± 0.79 | -0.08 | -0.09 | -0.06 | +8.2 | +0.5 | +0.1 | +0.6 |
| 60-72 | 316 | +0.16 ± 0.40 | -0.08 | -0.09 | -0.06 | +3.3 | +0.3 | +0.5 | +0.7 |
| 72-80 | 480 | +0.12 ± 0.30 | -0.09 | -0.10 | -0.07 | +1.1 | -0.1 | +0.3 | +0.7 |
| 80-86 | 377 | -0.16 ± 0.31 | -0.07 | -0.07 | -0.06 | -0.9 | +0.1 | +0.7 | +0.7 |
| 86-91 | 259 | -0.23 ± 0.48 | -0.10 | -0.08 | -0.06 | -6.8 | -0.7 | +0.6 | +0.7 |
| Isak pattern | 5 | -0.13 ± 2.74 | -0.31 | -0.34 | -0.08 | +21.3 | -1.0 | -0.7 | +0.9 |

corr(adapter Δpts, classic residual) / corr(adapter Δmin, classic minutes residual):
- h5: pts +0.096, minutes +0.152; sd of Δpts 0.124, sd of Δmin 1.92
- h6: pts +0.088, minutes +0.156; sd of Δpts 0.128, sd of Δmin 2.09
- h12: pts +0.086, minutes +0.042; sd of Δpts 0.036, sd of Δmin 0.37
