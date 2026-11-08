
## regime_21w: baseline ST1_F (21 windows; replay mismatches 0/504 weeks, table-vs-file actual mismatches 0, missing player-weeks 11)

| config | windows | actual total | xPts total | luck (actual−xPts) | Δactual vs base | sd/window | t | Δxpts vs base | sd/window | t | corr(Δactual, Δxpts) | Δxpts+skill | t |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ST1_F (base) | 21 | 5314 | 5127 | +187 | | | | | | | | | |
| RG1_F | 21 | 5208 | 5062 | +146 | -106 | 12.4 | -1.86 | -65 | 10.7 | -1.31 | 0.93 | -76 | -1.53 |
| RGW_F | 21 | 5303 | 5162 | +141 | -11 | 9.6 | -0.25 | +35 | 6.7 | +1.14 | 0.68 | +22 | +0.75 |
| RP_F | 21 | 5192 | 5057 | +135 | -122 | 14.2 | -1.87 | -70 | 11.3 | -1.35 | 0.93 | -81 | -1.59 |
| RW1_F | 21 | 5186 | 5082 | +104 | -128 | 17.4 | -1.61 | -45 | 11.4 | -0.86 | 0.89 | -56 | -1.15 |
| RW2_F | 21 | 5266 | 5115 | +151 | -48 | 14.4 | -0.73 | -12 | 9.0 | -0.29 | 0.89 | -24 | -0.64 |

Pooled per-window config-minus-base diffs over 105 window pairs: sd actual 13.8, sd xPts 10.0 (ratio 0.72), corr 0.88; mean |diff| actual 9.4 xPts 6.5.

## regime_live: baseline ST1_F (1 windows; replay mismatches 0/30 weeks, table-vs-file actual mismatches 0, missing player-weeks 0)

| config | windows | actual total | xPts total | luck (actual−xPts) | Δactual vs base | sd/window | t | Δxpts vs base | sd/window | t | corr(Δactual, Δxpts) | Δxpts+skill | t |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ST1_F (base) | 1 | 315 | 280 | +35 | | | | | | | | | |
| RG1_F | 1 | 342 | 299 | +43 | +27 | nan | +nan | +20 | nan | +nan | nan | +20 | +nan |
| RGW_F | 1 | 332 | 296 | +36 | +17 | nan | +nan | +16 | nan | +nan | nan | +17 | +nan |
| RP_F | 1 | 342 | 299 | +43 | +27 | nan | +nan | +20 | nan | +nan | nan | +20 | +nan |
| RW1_F | 1 | 329 | 288 | +41 | +14 | nan | +nan | +8 | nan | +nan | nan | +8 | +nan |
| RW2_F | 1 | 315 | 280 | +35 | +0 | nan | +nan | +0 | nan | +nan | nan | +0 | +nan |

Pooled per-window config-minus-base diffs over 5 window pairs: sd actual 11.2, sd xPts 8.5 (ratio 0.77), corr 0.97; mean |diff| actual 17.0 xPts 12.8.

## bench_weights: baseline ST1_F (21 windows; replay mismatches 0/252 weeks, table-vs-file actual mismatches 0, missing player-weeks 3)

| config | windows | actual total | xPts total | luck (actual−xPts) | Δactual vs base | sd/window | t | Δxpts vs base | sd/window | t | corr(Δactual, Δxpts) | Δxpts+skill | t |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ST1_F (base) | 21 | 5314 | 5127 | +187 | | | | | | | | | |
| SB1_F | 21 | 5317 | 5133 | +184 | +3 | 2.1 | +0.31 | +6 | 1.9 | +0.67 | 0.97 | +6 | +0.60 |
| SB2_F | 21 | 5314 | 5127 | +187 | +0 | 0.0 | +nan | +0 | 0.0 | +nan | nan | +0 | +nan |

Pooled per-window config-minus-base diffs over 42 window pairs: sd actual 1.5, sd xPts 1.3 (ratio 0.89), corr 0.96; mean |diff| actual 0.3 xPts 0.2.
