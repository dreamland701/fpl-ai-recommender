# Double-gameweek calibration: standard forecasts vs per-fixture heads

Regular starters (>=60 predicted minutes the week before, single fixture then). Variant: `/home/wescheng/projects/fpl/fpl/reports/dgw_fix/states_pf`.

| rows | variant | n | P(appear) | forecast p1 | actual | forecast − actual |
|---|---|---|---|---|---|---|
| doublers in a DGW | base | 743 | 0.56 | 4.29 | 5.91 | -1.62 |
| doublers in a DGW | fix | 743 | 0.80 | 6.11 | 5.91 | +0.20 |
| singles in a DGW | base | 1047 | 0.76 | 2.73 | 2.77 | -0.04 |
| singles in a DGW | fix | 1047 | 0.77 | 2.76 | 2.77 | -0.01 |
| normal weeks | base | 27016 | 0.77 | 2.89 | 2.98 | -0.09 |
| normal weeks | fix | 27016 | 0.78 | 2.92 | 2.98 | -0.06 |

## Forecast-best captain

| weeks | variant | n | captain forecast | captain actual | doubles chosen |
|---|---|---|---|---|---|
| double gameweeks | base | 15 | 8.08 | 11.47 | 12 |
| double gameweeks | fix | 15 | 13.94 | 12.40 | 14 |
| normal weeks | base | 200 | 7.91 | 6.86 | 16 |
| normal weeks | fix | 200 | 8.52 | 7.25 | 27 |

## Per double gameweek (doublers)

| season | GW | variant | n | P(appear) | forecast | actual |
|---|---|---|---|---|---|---|
| 2020-21 | 19 | base | 28 | 0.57 | 4.65 | 7.04 |
| 2020-21 | 19 | fix | 28 | 0.84 | 6.64 | 7.04 |
| 2020-21 | 26 | base | 132 | 0.58 | 4.50 | 5.79 |
| 2020-21 | 26 | fix | 132 | 0.84 | 6.46 | 5.79 |
| 2020-21 | 35 | base | 48 | 0.53 | 4.07 | 6.27 |
| 2020-21 | 35 | fix | 48 | 0.76 | 5.67 | 6.27 |
| 2021-22 | 26 | base | 53 | 0.57 | 4.39 | 7.00 |
| 2021-22 | 26 | fix | 53 | 0.83 | 6.31 | 7.00 |
| 2021-22 | 28 | base | 65 | 0.58 | 4.34 | 5.28 |
| 2021-22 | 28 | fix | 65 | 0.84 | 6.02 | 5.28 |
| 2021-22 | 29 | base | 28 | 0.56 | 4.28 | 5.29 |
| 2021-22 | 29 | fix | 28 | 0.79 | 6.14 | 5.29 |
| 2021-22 | 33 | base | 52 | 0.52 | 3.79 | 5.69 |
| 2021-22 | 33 | fix | 52 | 0.74 | 5.27 | 5.69 |
| 2021-22 | 36 | base | 96 | 0.55 | 4.20 | 5.47 |
| 2021-22 | 36 | fix | 96 | 0.79 | 5.99 | 5.47 |
| 2021-22 | 37 | base | 14 | 0.54 | 3.75 | 3.71 |
| 2021-22 | 37 | fix | 14 | 0.79 | 5.17 | 3.71 |
| 2022-23 | 29 | base | 55 | 0.54 | 4.04 | 5.33 |
| 2022-23 | 29 | fix | 55 | 0.75 | 5.61 | 5.33 |
| 2022-23 | 34 | base | 21 | 0.55 | 4.42 | 5.86 |
| 2022-23 | 34 | fix | 21 | 0.77 | 6.47 | 5.86 |
| 2022-23 | 37 | base | 16 | 0.56 | 4.80 | 5.31 |
| 2022-23 | 37 | fix | 16 | 0.75 | 6.81 | 5.31 |
| 2023-24 | 34 | base | 50 | 0.56 | 4.11 | 7.54 |
| 2023-24 | 34 | fix | 50 | 0.80 | 5.89 | 7.54 |
| 2023-24 | 37 | base | 39 | 0.56 | 4.38 | 6.23 |
| 2023-24 | 37 | fix | 39 | 0.80 | 6.42 | 6.23 |
| 2025-26-holdout | 33 | base | 46 | 0.56 | 4.56 | 5.93 |
| 2025-26-holdout | 33 | fix | 46 | 0.81 | 6.69 | 5.93 |
