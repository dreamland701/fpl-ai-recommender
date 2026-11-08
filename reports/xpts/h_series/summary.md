
## h3_arms: baseline bt_h3_classic (10 windows; replay mismatches 0/246 weeks, table-vs-file actual mismatches 0, missing player-weeks 0)

| config | windows | actual total | xPts total | luck (actual−xPts) | Δactual vs base | sd/window | t | Δxpts vs base | sd/window | t | corr(Δactual, Δxpts) | Δxpts+skill | t |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bt_h3_classic (base) | 10 | 2555 | 2373 | +182 | | | | | | | | | |
| bt_h3_availability | 10 | 2537 | 2353 | +184 | -18 | 5.7 | -1.00 | -20 | 6.3 | -1.00 | 1.00 | -20 | -1.00 |
| bt_h3_classic_soft | 10 | 2542 | 2363 | +179 | -13 | 4.2 | -0.98 | -10 | 2.0 | -1.53 | 0.33 | -10 | -1.52 |
| bt_h3_coupled | 10 | 2554 | 2362 | +192 | -1 | 15.9 | -0.02 | -11 | 8.9 | -0.39 | 0.85 | -11 | -0.38 |
| bt_h3_coupled_soft | 10 | 2543 | 2360 | +183 | -12 | 16.2 | -0.23 | -13 | 8.9 | -0.45 | 0.83 | -12 | -0.43 |
| bt_h3_platt_soft | 10 | 2526 | 2352 | +174 | -29 | 6.3 | -1.45 | -21 | 6.2 | -1.08 | 0.88 | -21 | -1.08 |

Pooled per-window config-minus-base diffs over 50 window pairs: sd actual 10.6, sd xPts 6.7 (ratio 0.63), corr 0.82; mean |diff| actual 5.3 xPts 2.9.
