
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

## h6_arms: baseline bt_classic (5 windows; replay mismatches 0/57 weeks, table-vs-file actual mismatches 0, missing player-weeks 78)

| config | windows | actual total | xPts total | luck (actual−xPts) | Δactual vs base | sd/window | t | Δxpts vs base | sd/window | t | corr(Δactual, Δxpts) | Δxpts+skill | t |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bt_classic (base) | 5 | 1232 | 1116 | +116 | | | | | | | | | |
| bt_h5 | 5 | 1261 | 1140 | +121 | +29 | 14.7 | +0.89 | +24 | 15.1 | +0.71 | 0.77 | +23 | +0.70 |
| bt_h6 | 5 | 1231 | 1121 | +110 | -1 | 16.1 | -0.03 | +5 | 8.0 | +0.28 | 0.62 | +6 | +0.31 |

Pooled per-window config-minus-base diffs over 10 window pairs: sd actual 14.9, sd xPts 11.6 (ratio 0.78), corr 0.69; mean |diff| actual 12.4 xPts 8.0.

## h6b_arms: baseline bt_classic (5 windows; replay mismatches 0/76 weeks, table-vs-file actual mismatches 0, missing player-weeks 104)

| config | windows | actual total | xPts total | luck (actual−xPts) | Δactual vs base | sd/window | t | Δxpts vs base | sd/window | t | corr(Δactual, Δxpts) | Δxpts+skill | t |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bt_classic (base) | 5 | 1232 | 1116 | +116 | | | | | | | | | |
| bt_h5 | 5 | 1261 | 1140 | +121 | +29 | 14.7 | +0.89 | +24 | 15.1 | +0.71 | 0.77 | +23 | +0.70 |
| bt_h6 | 5 | 1231 | 1121 | +110 | -1 | 16.1 | -0.03 | +5 | 8.0 | +0.28 | 0.62 | +6 | +0.31 |
| bt_h6b | 5 | 1225 | 1129 | +96 | -7 | 12.8 | -0.24 | +13 | 14.5 | +0.40 | 0.66 | +12 | +0.37 |

Pooled per-window config-minus-base diffs over 15 window pairs: sd actual 13.9, sd xPts 12.1 (ratio 0.87), corr 0.66; mean |diff| actual 11.8 xPts 9.4.

## h12_arms: baseline bt_classic (5 windows; replay mismatches 0/95 weeks, table-vs-file actual mismatches 0, missing player-weeks 130)

| config | windows | actual total | xPts total | luck (actual−xPts) | Δactual vs base | sd/window | t | Δxpts vs base | sd/window | t | corr(Δactual, Δxpts) | Δxpts+skill | t |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bt_classic (base) | 5 | 1232 | 1116 | +116 | | | | | | | | | |
| bt_h12 | 5 | 1241 | 1130 | +111 | +9 | 3.5 | +1.15 | +14 | 9.1 | +0.70 | 0.94 | +13 | +0.66 |
| bt_h5 | 5 | 1261 | 1140 | +121 | +29 | 14.7 | +0.89 | +24 | 15.1 | +0.71 | 0.77 | +23 | +0.70 |
| bt_h6 | 5 | 1231 | 1121 | +110 | -1 | 16.1 | -0.03 | +5 | 8.0 | +0.28 | 0.62 | +6 | +0.31 |
| bt_h6b | 5 | 1225 | 1129 | +96 | -7 | 12.8 | -0.24 | +13 | 14.5 | +0.40 | 0.66 | +12 | +0.37 |

Pooled per-window config-minus-base diffs over 20 window pairs: sd actual 12.0, sd xPts 11.2 (ratio 0.93), corr 0.65; mean |diff| actual 9.3 xPts 8.2.
