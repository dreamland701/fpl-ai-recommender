# H-series comparison: h1 vs h4

Recomputed from the prediction files on identical rows. RMSE on the 1/3/5GW points labels (classic / arm); bias = forecast − actual; closer = share of rows where the arm lands strictly nearer the actual than classic; |Δ| = mean absolute change the arm makes to the classic forecast.

## holdout

| arm | subset | n | RMSE 1GW classic / arm | RMSE 3GW | RMSE 5GW | MAE 1GW | bias 1GW | closer | Δ1 mean / abs / sd |
|---|---|---|---|---|---|---|---|---|---|
| h1 | all | 1152 | 3.420 / 3.419 | 6.807 / 6.737 | 10.035 / 9.922 | 2.609 / 2.557 | 0.10 / -0.15 | 61% | -0.25 / 0.25 / 0.11 |
| h1 | with text | 963 | 3.425 / 3.422 | 6.943 / 6.873 | 10.259 / 10.141 | 2.628 / 2.571 | 0.14 / -0.12 | 62% | -0.26 / 0.26 / 0.11 |
| h1 | no text | 189 | 3.395 / 3.408 | 6.070 / 5.999 | 8.803 / 8.721 | 2.512 / 2.487 | -0.10 / -0.28 | 58% | -0.18 / 0.18 / 0.09 |
| h1 | classic >= 4 | 337 | 3.995 / 3.987 | 7.611 / 7.542 | 11.192 / 11.089 | 3.264 / 3.210 | 0.26 / 0.00 | 61% | -0.25 / 0.25 / 0.11 |
| h1 | flagged (P<0.95) | 947 | 3.352 / 3.359 | 6.619 / 6.564 | 9.743 / 9.657 | 2.497 / 2.451 | -0.00 / -0.25 | 60% | -0.24 / 0.25 / 0.11 |
| h4 | all | 1152 | 3.420 / 3.411 | 6.807 / 6.731 | 10.035 / 9.919 | 2.609 / 2.542 | 0.10 / -0.17 | 61% | -0.27 / 0.27 / 0.13 |
| h4 | with text | 963 | 3.425 / 3.412 | 6.943 / 6.865 | 10.259 / 10.143 | 2.628 / 2.556 | 0.14 / -0.13 | 62% | -0.27 / 0.27 / 0.14 |
| h4 | no text | 189 | 3.395 / 3.408 | 6.070 / 6.005 | 8.803 / 8.686 | 2.512 / 2.469 | -0.10 / -0.35 | 57% | -0.26 / 0.26 / 0.10 |
| h4 | classic >= 4 | 337 | 3.995 / 3.978 | 7.611 / 7.549 | 11.192 / 11.088 | 3.264 / 3.196 | 0.26 / -0.03 | 59% | -0.28 / 0.28 / 0.14 |
| h4 | flagged (P<0.95) | 947 | 3.352 / 3.351 | 6.619 / 6.553 | 9.743 / 9.662 | 2.497 / 2.439 | -0.00 / -0.25 | 60% | -0.25 / 0.25 / 0.13 |

| arm | subset | n | AUC classic / arm | Brier classic / arm | uncertain n | AUC unc classic / arm | Brier unc classic / arm | |ΔP| mean |
|---|---|---|---|---|---|---|---|---|
| h1 | all | 1152 | 0.704 / 0.771 | 0.0767 / 0.0604 | 914 | 0.574 / 0.706 | 0.0851 / 0.0646 | 0.072 |
| h1 | with text | 963 | 0.695 / 0.773 | 0.0805 / 0.0638 | 765 | 0.574 / 0.725 | 0.0888 / 0.0676 | 0.070 |
| h1 | no text | 189 | 0.763 / 0.748 | 0.0575 / 0.0436 | 149 | 0.585 / 0.541 | 0.0661 / 0.0487 | 0.078 |
| h1 | classic >= 4 | 337 | 0.533 / 0.596 | 0.0639 / 0.0564 | 197 | 0.560 / 0.684 | 0.0742 / 0.0619 | 0.052 |
| h1 | flagged (P<0.95) | 947 | 0.718 / 0.805 | 0.0821 / 0.0623 | 914 | 0.574 / 0.706 | 0.0851 / 0.0646 | 0.084 |
| h4 | all | 1152 | 0.704 / 0.788 | 0.0767 / 0.0558 | 914 | 0.574 / 0.739 | 0.0851 / 0.0588 | 0.092 |
| h4 | with text | 963 | 0.695 / 0.791 | 0.0805 / 0.0586 | 765 | 0.574 / 0.755 | 0.0888 / 0.0614 | 0.093 |
| h4 | no text | 189 | 0.763 / 0.759 | 0.0575 / 0.0414 | 149 | 0.585 / 0.589 | 0.0661 / 0.0458 | 0.089 |
| h4 | classic >= 4 | 337 | 0.533 / 0.603 | 0.0639 / 0.0488 | 197 | 0.560 / 0.756 | 0.0742 / 0.0487 | 0.070 |
| h4 | flagged (P<0.95) | 947 | 0.718 / 0.827 | 0.0821 / 0.0568 | 914 | 0.574 / 0.739 | 0.0851 / 0.0588 | 0.108 |

Head to head on matched rows (arm A vs arm B): correlation of the deltas, share of rows with the same sign, RMSE of A and B on 1GW points, and share of rows where A is strictly closer than B.

| A | B | n | corr Δ1 | corr ΔP(app) | same sign Δ1 | RMSE A / B | A closer than B |
|---|---|---|---|---|---|---|---|
| h1 | h4 | 1152 | 0.630 | 0.818 | 98% | 3.419 / 3.411 | 44% |

## live

| arm | subset | n | RMSE 1GW classic / arm | RMSE 3GW | RMSE 5GW | MAE 1GW | bias 1GW | closer | Δ1 mean / abs / sd |
|---|---|---|---|---|---|---|---|---|---|
| h1 | all | 480 | 3.424 / 3.441 | 7.490 / 7.491 | 12.012 / 11.987 | 2.614 / 2.568 | -0.23 / -0.47 | 59% | -0.24 / 0.24 / 0.12 |
| h1 | with text | 445 | 3.375 / 3.393 | 7.209 / 7.217 | 11.498 / 11.486 | 2.593 / 2.547 | -0.21 / -0.46 | 59% | -0.25 / 0.25 / 0.11 |
| h1 | no text | 35 | 3.994 / 3.994 | 10.425 / 10.363 | 17.252 / 17.130 | 2.883 / 2.832 | -0.37 / -0.58 | 60% | -0.20 / 0.20 / 0.18 |
| h1 | classic >= 4 | 130 | 4.069 / 4.080 | 8.577 / 8.545 | 13.749 / 13.704 | 3.254 / 3.209 | -0.08 / -0.31 | 59% | -0.24 / 0.24 / 0.11 |
| h1 | flagged (P<0.95) | 395 | 3.220 / 3.240 | 7.067 / 7.088 | 11.465 / 11.459 | 2.461 / 2.419 | -0.21 / -0.45 | 59% | -0.24 / 0.24 / 0.12 |
| h4 | all | 480 | 3.424 / 3.437 | 7.490 / 7.466 | 12.012 / 11.946 | 2.614 / 2.566 | -0.23 / -0.46 | 60% | -0.24 / 0.24 / 0.16 |
| h4 | with text | 445 | 3.375 / 3.389 | 7.209 / 7.188 | 11.498 / 11.445 | 2.593 / 2.546 | -0.21 / -0.45 | 60% | -0.23 / 0.24 / 0.15 |
| h4 | no text | 35 | 3.994 / 4.000 | 10.425 / 10.375 | 17.252 / 17.079 | 2.883 / 2.825 | -0.37 / -0.66 | 60% | -0.29 / 0.29 / 0.23 |
| h4 | classic >= 4 | 130 | 4.069 / 4.079 | 8.577 / 8.533 | 13.749 / 13.665 | 3.254 / 3.192 | -0.08 / -0.34 | 59% | -0.27 / 0.27 / 0.14 |
| h4 | flagged (P<0.95) | 395 | 3.220 / 3.235 | 7.067 / 7.064 | 11.465 / 11.417 | 2.461 / 2.423 | -0.21 / -0.43 | 59% | -0.22 / 0.22 / 0.15 |

| arm | subset | n | AUC classic / arm | Brier classic / arm | uncertain n | AUC unc classic / arm | Brier unc classic / arm | |ΔP| mean |
|---|---|---|---|---|---|---|---|---|
| h1 | all | 480 | 0.645 / 0.760 | 0.0444 / 0.0252 | 395 | 0.701 / 0.855 | 0.0490 / 0.0257 | 0.087 |
| h1 | with text | 445 | 0.648 / 0.765 | 0.0454 / 0.0248 | 364 | 0.702 / 0.860 | 0.0502 / 0.0250 | 0.085 |
| h1 | no text | 35 | nan / nan | 0.0314 / 0.0295 | 31 | nan / nan | 0.0353 / 0.0333 | 0.106 |
| h1 | classic >= 4 | 130 | 0.140 / 0.310 | 0.0220 / 0.0132 | 71 | nan / nan | 0.0260 / 0.0102 | 0.057 |
| h1 | flagged (P<0.95) | 395 | 0.701 / 0.855 | 0.0490 / 0.0257 | 395 | 0.701 / 0.855 | 0.0490 / 0.0257 | 0.103 |
| h4 | all | 480 | 0.645 / 0.780 | 0.0444 / 0.0250 | 395 | 0.701 / 0.832 | 0.0490 / 0.0255 | 0.103 |
| h4 | with text | 445 | 0.648 / 0.790 | 0.0454 / 0.0247 | 364 | 0.702 / 0.844 | 0.0502 / 0.0250 | 0.102 |
| h4 | no text | 35 | nan / nan | 0.0314 / 0.0289 | 31 | nan / nan | 0.0353 / 0.0326 | 0.112 |
| h4 | classic >= 4 | 130 | 0.140 / 0.845 | 0.0220 / 0.0096 | 71 | nan / nan | 0.0260 / 0.0044 | 0.064 |
| h4 | flagged (P<0.95) | 395 | 0.701 / 0.832 | 0.0490 / 0.0255 | 395 | 0.701 / 0.832 | 0.0490 / 0.0255 | 0.122 |

Head to head on matched rows (arm A vs arm B): correlation of the deltas, share of rows with the same sign, RMSE of A and B on 1GW points, and share of rows where A is strictly closer than B.

| A | B | n | corr Δ1 | corr ΔP(app) | same sign Δ1 | RMSE A / B | A closer than B |
|---|---|---|---|---|---|---|---|
| h1 | h4 | 480 | 0.760 | 0.876 | 97% | 3.441 / 3.437 | 50% |

## Decision windows (realised squad points, same engine, `--llm-fields all`)

| window | classic | h1 | h4 | h1 − classic | h4 − classic |
|---|---|---|---|---|---|
| 2025-26_27_30 | 281 | 246 | 227 | -35 | -54 |
| 2025-26_31_34 | 254 | 237 | 245 | -17 | -9 |
| 2025-26_35_38 | 253 | 267 | 267 | +14 | +14 |
| 2026-27_2_6 | 315 | 335 | 328 | +20 | +13 |
| total | 1103 (4w) | 1085 (4w) | 1067 (4w) | -18 | -36 |

## xPts re-score (reports/h_series/xpts/summary.md)

## h31_arms: baseline bt_classic (4 windows; replay mismatches 0/51 weeks, table-vs-file actual mismatches 0, missing player-weeks 0)

| config | windows | actual total | xPts total | luck (actual−xPts) | Δactual vs base | sd/window | t | Δxpts vs base | sd/window | t | corr(Δactual, Δxpts) | Δxpts+skill | t |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bt_classic (base) | 4 | 1103 | 987 | +116 | | | | | | | | | |
| bt_h1 | 4 | 1085 | 964 | +121 | -18 | 26.0 | -0.35 | -23 | 12.3 | -0.93 | 0.97 | -21 | -0.85 |
| bt_h31 | 4 | 1123 | 991 | +132 | +20 | 29.3 | +0.34 | +4 | 9.9 | +0.22 | 1.00 | +5 | +0.25 |

Pooled per-window config-minus-base diffs over 8 window pairs: sd actual 26.1, sd xPts 10.9 (ratio 0.42), corr 0.96; mean |diff| actual 21.5 xPts 8.6.

## h4_arms: baseline bt_classic (4 windows; replay mismatches 0/51 weeks, table-vs-file actual mismatches 0, missing player-weeks 0)

| config | windows | actual total | xPts total | luck (actual−xPts) | Δactual vs base | sd/window | t | Δxpts vs base | sd/window | t | corr(Δactual, Δxpts) | Δxpts+skill | t |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bt_classic (base) | 4 | 1103 | 987 | +116 | | | | | | | | | |
| bt_h1 | 4 | 1085 | 964 | +121 | -18 | 26.0 | -0.35 | -23 | 12.3 | -0.93 | 0.97 | -21 | -0.85 |
| bt_h4 | 4 | 1067 | 958 | +109 | -36 | 31.8 | -0.57 | -29 | 15.3 | -0.95 | 0.98 | -30 | -0.92 |

Pooled per-window config-minus-base diffs over 8 window pairs: sd actual 27.0, sd xPts 12.9 (ratio 0.48), corr 0.98; mean |diff| actual 22.0 xPts 10.3.

