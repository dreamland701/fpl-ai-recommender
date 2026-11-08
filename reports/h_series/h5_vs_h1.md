# H-series comparison: h1 vs h5

Recomputed from the prediction files on identical rows. RMSE on the 1/3/5GW points labels (classic / arm); bias = forecast − actual; closer = share of rows where the arm lands strictly nearer the actual than classic; |Δ| = mean absolute change the arm makes to the classic forecast.

## holdout

| arm | subset | n | RMSE 1GW classic / arm | RMSE 3GW | RMSE 5GW | MAE 1GW | bias 1GW | closer | Δ1 mean / abs / sd |
|---|---|---|---|---|---|---|---|---|---|
| h1 | all | 1152 | 3.420 / 3.419 | 6.807 / 6.737 | 10.035 / 9.922 | 2.609 / 2.557 | 0.10 / -0.15 | 61% | -0.25 / 0.25 / 0.11 |
| h1 | with text | 963 | 3.425 / 3.422 | 6.943 / 6.873 | 10.259 / 10.141 | 2.628 / 2.571 | 0.14 / -0.12 | 62% | -0.26 / 0.26 / 0.11 |
| h1 | no text | 189 | 3.395 / 3.408 | 6.070 / 5.999 | 8.803 / 8.721 | 2.512 / 2.487 | -0.10 / -0.28 | 58% | -0.18 / 0.18 / 0.09 |
| h1 | classic >= 4 | 337 | 3.995 / 3.987 | 7.611 / 7.542 | 11.192 / 11.089 | 3.264 / 3.210 | 0.26 / 0.00 | 61% | -0.25 / 0.25 / 0.11 |
| h1 | flagged (P<0.95) | 947 | 3.352 / 3.359 | 6.619 / 6.564 | 9.743 / 9.657 | 2.497 / 2.451 | -0.00 / -0.25 | 60% | -0.24 / 0.25 / 0.11 |
| h5 | all | 1152 | 3.420 / 3.415 | 6.807 / 6.765 | 10.035 / 9.962 | 2.609 / 2.589 | 0.10 / 0.01 | 58% | -0.09 / 0.11 / 0.11 |
| h5 | with text | 963 | 3.425 / 3.418 | 6.943 / 6.899 | 10.259 / 10.183 | 2.628 / 2.606 | 0.14 / 0.05 | 58% | -0.09 / 0.11 / 0.11 |
| h5 | no text | 189 | 3.395 / 3.400 | 6.070 / 6.035 | 8.803 / 8.744 | 2.512 / 2.502 | -0.10 / -0.18 | 61% | -0.08 / 0.09 / 0.08 |
| h5 | classic >= 4 | 337 | 3.995 / 3.987 | 7.611 / 7.572 | 11.192 / 11.106 | 3.264 / 3.239 | 0.26 / 0.17 | 56% | -0.09 / 0.10 / 0.10 |
| h5 | flagged (P<0.95) | 947 | 3.352 / 3.350 | 6.619 / 6.586 | 9.743 / 9.698 | 2.497 / 2.481 | -0.00 / -0.09 | 57% | -0.09 / 0.11 / 0.11 |

| arm | subset | n | AUC classic / arm | Brier classic / arm | uncertain n | AUC unc classic / arm | Brier unc classic / arm | |ΔP| mean |
|---|---|---|---|---|---|---|---|---|
| h1 | all | 1152 | 0.704 / 0.771 | 0.0767 / 0.0604 | 914 | 0.574 / 0.706 | 0.0851 / 0.0646 | 0.072 |
| h1 | with text | 963 | 0.695 / 0.773 | 0.0805 / 0.0638 | 765 | 0.574 / 0.725 | 0.0888 / 0.0676 | 0.070 |
| h1 | no text | 189 | 0.763 / 0.748 | 0.0575 / 0.0436 | 149 | 0.585 / 0.541 | 0.0661 / 0.0487 | 0.078 |
| h1 | classic >= 4 | 337 | 0.533 / 0.596 | 0.0639 / 0.0564 | 197 | 0.560 / 0.684 | 0.0742 / 0.0619 | 0.052 |
| h1 | flagged (P<0.95) | 947 | 0.718 / 0.805 | 0.0821 / 0.0623 | 914 | 0.574 / 0.706 | 0.0851 / 0.0646 | 0.084 |
| h5 | all | 1152 | 0.704 / 0.776 | 0.0767 / 0.0569 | 914 | 0.574 / 0.711 | 0.0851 / 0.0600 | 0.086 |
| h5 | with text | 963 | 0.695 / 0.779 | 0.0805 / 0.0597 | 765 | 0.574 / 0.728 | 0.0888 / 0.0625 | 0.086 |
| h5 | no text | 189 | 0.763 / 0.754 | 0.0575 / 0.0424 | 149 | 0.585 / 0.557 | 0.0661 / 0.0472 | 0.082 |
| h5 | classic >= 4 | 337 | 0.533 / 0.623 | 0.0639 / 0.0505 | 197 | 0.560 / 0.723 | 0.0742 / 0.0518 | 0.063 |
| h5 | flagged (P<0.95) | 947 | 0.718 / 0.808 | 0.0821 / 0.0579 | 914 | 0.574 / 0.711 | 0.0851 / 0.0600 | 0.101 |

Head to head on matched rows (arm A vs arm B): correlation of the deltas, share of rows with the same sign, RMSE of A and B on 1GW points, and share of rows where A is strictly closer than B.

| A | B | n | corr Δ1 | corr ΔP(app) | same sign Δ1 | RMSE A / B | A closer than B |
|---|---|---|---|---|---|---|---|
| h1 | h5 | 1152 | 0.694 | 0.825 | 82% | 3.419 / 3.415 | 60% |

## live

| arm | subset | n | RMSE 1GW classic / arm | RMSE 3GW | RMSE 5GW | MAE 1GW | bias 1GW | closer | Δ1 mean / abs / sd |
|---|---|---|---|---|---|---|---|---|---|
| h1 | all | 480 | 3.424 / 3.441 | 7.490 / 7.491 | 12.012 / 11.987 | 2.614 / 2.568 | -0.23 / -0.47 | 59% | -0.24 / 0.24 / 0.12 |
| h1 | with text | 445 | 3.375 / 3.393 | 7.209 / 7.217 | 11.498 / 11.486 | 2.593 / 2.547 | -0.21 / -0.46 | 59% | -0.25 / 0.25 / 0.11 |
| h1 | no text | 35 | 3.994 / 3.994 | 10.425 / 10.363 | 17.252 / 17.130 | 2.883 / 2.832 | -0.37 / -0.58 | 60% | -0.20 / 0.20 / 0.18 |
| h1 | classic >= 4 | 130 | 4.069 / 4.080 | 8.577 / 8.545 | 13.749 / 13.704 | 3.254 / 3.209 | -0.08 / -0.31 | 59% | -0.24 / 0.24 / 0.11 |
| h1 | flagged (P<0.95) | 395 | 3.220 / 3.240 | 7.067 / 7.088 | 11.465 / 11.459 | 2.461 / 2.419 | -0.21 / -0.45 | 59% | -0.24 / 0.24 / 0.12 |
| h5 | all | 480 | 3.424 / 3.421 | 7.490 / 7.471 | 12.012 / 11.994 | 2.614 / 2.597 | -0.23 / -0.31 | 55% | -0.08 / 0.11 / 0.12 |
| h5 | with text | 445 | 3.375 / 3.373 | 7.209 / 7.193 | 11.498 / 11.492 | 2.593 / 2.578 | -0.21 / -0.29 | 56% | -0.08 / 0.10 / 0.11 |
| h5 | no text | 35 | 3.994 / 3.981 | 10.425 / 10.377 | 17.252 / 17.138 | 2.883 / 2.838 | -0.37 / -0.52 | 51% | -0.15 / 0.15 / 0.20 |
| h5 | classic >= 4 | 130 | 4.069 / 4.069 | 8.577 / 8.545 | 13.749 / 13.662 | 3.254 / 3.240 | -0.08 / -0.15 | 57% | -0.08 / 0.10 / 0.09 |
| h5 | flagged (P<0.95) | 395 | 3.220 / 3.219 | 7.067 / 7.061 | 11.465 / 11.466 | 2.461 / 2.447 | -0.21 / -0.29 | 54% | -0.08 / 0.10 / 0.13 |

| arm | subset | n | AUC classic / arm | Brier classic / arm | uncertain n | AUC unc classic / arm | Brier unc classic / arm | |ΔP| mean |
|---|---|---|---|---|---|---|---|---|
| h1 | all | 480 | 0.645 / 0.760 | 0.0444 / 0.0252 | 395 | 0.701 / 0.855 | 0.0490 / 0.0257 | 0.087 |
| h1 | with text | 445 | 0.648 / 0.765 | 0.0454 / 0.0248 | 364 | 0.702 / 0.860 | 0.0502 / 0.0250 | 0.085 |
| h1 | no text | 35 | nan / nan | 0.0314 / 0.0295 | 31 | nan / nan | 0.0353 / 0.0333 | 0.106 |
| h1 | classic >= 4 | 130 | 0.140 / 0.310 | 0.0220 / 0.0132 | 71 | nan / nan | 0.0260 / 0.0102 | 0.057 |
| h1 | flagged (P<0.95) | 395 | 0.701 / 0.855 | 0.0490 / 0.0257 | 395 | 0.701 / 0.855 | 0.0490 / 0.0257 | 0.103 |
| h5 | all | 480 | 0.645 / 0.727 | 0.0444 / 0.0250 | 395 | 0.701 / 0.808 | 0.0490 / 0.0254 | 0.098 |
| h5 | with text | 445 | 0.648 / 0.735 | 0.0454 / 0.0246 | 364 | 0.702 / 0.817 | 0.0502 / 0.0247 | 0.098 |
| h5 | no text | 35 | nan / nan | 0.0314 / 0.0290 | 31 | nan / nan | 0.0353 / 0.0327 | 0.108 |
| h5 | classic >= 4 | 130 | 0.140 / 0.403 | 0.0220 / 0.0099 | 71 | nan / nan | 0.0260 / 0.0042 | 0.061 |
| h5 | flagged (P<0.95) | 395 | 0.701 / 0.808 | 0.0490 / 0.0254 | 395 | 0.701 / 0.808 | 0.0490 / 0.0254 | 0.117 |

Head to head on matched rows (arm A vs arm B): correlation of the deltas, share of rows with the same sign, RMSE of A and B on 1GW points, and share of rows where A is strictly closer than B.

| A | B | n | corr Δ1 | corr ΔP(app) | same sign Δ1 | RMSE A / B | A closer than B |
|---|---|---|---|---|---|---|---|
| h1 | h5 | 480 | 0.767 | 0.894 | 78% | 3.441 / 3.421 | 57% |

## Decision windows (realised squad points, same engine, `--llm-fields all`)

| window | classic | h1 | h5 | h1 − classic | h5 − classic |
|---|---|---|---|---|---|
| 2025-26_27_30 | 281 | 246 | 294 | -35 | +13 |
| 2025-26_31_34 | 254 | 237 | 237 | -17 | -17 |
| 2025-26_35_38 | 253 | 267 | 266 | +14 | +13 |
| 2026-27_2_6 | 315 | 335 | 335 | +20 | +20 |
| total | 1103 (4w) | 1085 (4w) | 1132 (4w) | -18 | +29 |

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

## h4_availability: baseline bt_classic (4 windows; replay mismatches 0/51 weeks, table-vs-file actual mismatches 0, missing player-weeks 0)

| config | windows | actual total | xPts total | luck (actual−xPts) | Δactual vs base | sd/window | t | Δxpts vs base | sd/window | t | corr(Δactual, Δxpts) | Δxpts+skill | t |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bt_classic (base) | 4 | 1103 | 987 | +116 | | | | | | | | | |
| bt_h1_availability | 4 | 1140 | 998 | +142 | +37 | 18.5 | +1.00 | +11 | 5.4 | +1.00 | 1.00 | +11 | +1.00 |
| bt_h4_availability | 4 | 1103 | 987 | +116 | +0 | 0.0 | +nan | +0 | 0.0 | +nan | nan | +0 | +nan |

Pooled per-window config-minus-base diffs over 8 window pairs: sd actual 13.1, sd xPts 3.8 (ratio 0.29), corr 1.00; mean |diff| actual 4.6 xPts 1.3.

## h4_availability_scaled: baseline bt_classic (4 windows; replay mismatches 0/51 weeks, table-vs-file actual mismatches 0, missing player-weeks 0)

| config | windows | actual total | xPts total | luck (actual−xPts) | Δactual vs base | sd/window | t | Δxpts vs base | sd/window | t | corr(Δactual, Δxpts) | Δxpts+skill | t |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bt_classic (base) | 4 | 1103 | 987 | +116 | | | | | | | | | |
| bt_h1_availability_scaled | 4 | 1050 | 973 | +77 | -53 | 34.4 | -0.77 | -14 | 20.3 | -0.36 | 0.97 | -18 | -0.49 |
| bt_h4_availability_scaled | 4 | 1047 | 971 | +76 | -56 | 35.5 | -0.79 | -16 | 22.1 | -0.37 | 0.96 | -19 | -0.47 |

Pooled per-window config-minus-base diffs over 8 window pairs: sd actual 32.4, sd xPts 19.6 (ratio 0.61), corr 0.97; mean |diff| actual 27.9 xPts 17.0.

## softavail_arms: baseline bt_classic_softavail (4 windows; replay mismatches 0/102 weeks, table-vs-file actual mismatches 0, missing player-weeks 0)

| config | windows | actual total | xPts total | luck (actual−xPts) | Δactual vs base | sd/window | t | Δxpts vs base | sd/window | t | corr(Δactual, Δxpts) | Δxpts+skill | t |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bt_classic_softavail (base) | 4 | 1096 | 982 | +114 | | | | | | | | | |
| bt_classic | 4 | 1103 | 987 | +116 | +7 | 6.4 | +0.54 | +5 | 1.6 | +1.53 | -0.17 | +5 | +1.47 |
| bt_h1_softavail_all | 4 | 1090 | 967 | +123 | -6 | 25.1 | -0.12 | -15 | 12.2 | -0.60 | 0.97 | -13 | -0.54 |
| bt_h1_softavail_availability | 4 | 1134 | 995 | +139 | +38 | 18.3 | +1.04 | +13 | 5.1 | +1.28 | 0.98 | +14 | +1.30 |
| bt_h4_softavail_all | 4 | 1057 | 956 | +101 | -39 | 29.7 | -0.66 | -27 | 16.1 | -0.83 | 1.00 | -27 | -0.79 |
| bt_h4_softavail_availability | 4 | 1103 | 989 | +114 | +7 | 2.9 | +1.22 | +7 | 2.3 | +1.56 | 0.94 | +7 | +1.61 |

Pooled per-window config-minus-base diffs over 20 window pairs: sd actual 18.5, sd xPts 9.2 (ratio 0.50), corr 0.95; mean |diff| actual 10.8 xPts 5.5.

## h5_arms: baseline bt_classic (4 windows; replay mismatches 0/68 weeks, table-vs-file actual mismatches 0, missing player-weeks 0)

| config | windows | actual total | xPts total | luck (actual−xPts) | Δactual vs base | sd/window | t | Δxpts vs base | sd/window | t | corr(Δactual, Δxpts) | Δxpts+skill | t |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bt_classic (base) | 4 | 1103 | 987 | +116 | | | | | | | | | |
| bt_h1 | 4 | 1085 | 964 | +121 | -18 | 26.0 | -0.35 | -23 | 12.3 | -0.93 | 0.97 | -21 | -0.85 |
| bt_h4 | 4 | 1067 | 958 | +109 | -36 | 31.8 | -0.57 | -29 | 15.3 | -0.95 | 0.98 | -30 | -0.92 |
| bt_h5 | 4 | 1132 | 1011 | +121 | +29 | 16.5 | +0.88 | +24 | 17.1 | +0.70 | 0.77 | +23 | +0.69 |

Pooled per-window config-minus-base diffs over 12 window pairs: sd actual 24.2, sd xPts 15.0 (ratio 0.62), corr 0.88; mean |diff| actual 19.9 xPts 11.3.

