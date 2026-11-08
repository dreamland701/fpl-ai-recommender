# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW30
- Total predicted points: 1778.76
- Total actual points: 1414.00
- Average predicted points: 61.34
- Average actual points: 48.76
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW1 are included before the first simulated week.
- League-average scores were not available for this run.

## GW2

- Train rows: 161967
- Bank: 100.00 -> 1.00
- Free transfers: 1 -> 2
- Captain: M.Salah
- Vice captain: Ballard
- Effective captain: M.Salah
- Chip used: none
- Predicted score: 82.65
- Actual score: 52.00
- Chip advisory: bench_boost (0.67): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Sánchez | GK | 7 | 5.0 | 5.89 | 16.09 | 24.99 | 3.00 | 106.7 | 90.0 |
| Bench 1 | Bench | Raya | GK | 1 | 5.5 | 5.09 | 14.47 | 23.38 | 6.00 | 110.0 | 90.0 |
| Vice Captain | XI | Ballard | DEF | 17 | 4.5 | 7.50 | 20.58 | 32.14 | 1.00 | 114.1 | 8.0 |
| XI | XI | Calafiori | DEF | 1 | 5.5 | 6.78 | 18.68 | 29.58 | 13.00 | 88.2 | 63.0 |
| XI | XI | Aït-Nouri | DEF | 13 | 6.0 | 6.06 | 17.40 | 27.82 | 1.00 | 94.6 | 22.0 |
| Bench 4 | Bench | Pedro Porro | DEF | 18 | 5.5 | 5.77 | 17.36 | 27.91 | 5.00 | 106.4 | 90.0 |
| Bench 3 | Bench | Lewis | DEF | 13 | 5.0 | 5.97 | 16.99 | 27.26 | 1.00 | 88.5 | 90.0 |
| XI | XI | Ekitiké | FWD | 12 | 8.5 | 6.29 | 18.45 | 29.60 | 9.00 | 90.0 | 79.0 |
| XI | XI | Wood | FWD | 16 | 7.5 | 6.11 | 17.44 | 27.87 | 2.00 | 90.0 | 87.0 |
| Bench 2 | Bench | João Pedro | FWD | 7 | 7.5 | 5.99 | 16.48 | 25.59 | 15.00 | 87.5 | 90.0 |
| Captain | Captain | M.Salah | MID | 12 | 14.5 | 7.73 | 22.31 | 35.46 | 5.00 | 113.8 | 90.0 |
| XI | XI | Kudus | MID | 18 | 6.5 | 7.38 | 22.02 | 35.47 | 3.00 | 100.5 | 85.0 |
| XI | XI | Reijnders | MID | 13 | 5.5 | 7.43 | 21.01 | 33.26 | 2.00 | 112.9 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 7.0 | 7.33 | 20.05 | 31.39 | 6.00 | 100.3 | 90.0 |
| XI | XI | Stach | MID | 11 | 5.0 | 6.43 | 18.74 | 29.70 | 2.00 | 101.7 | 90.0 |

## GW3

- Train rows: 162672
- Bank: 1.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: João Pedro
- Vice captain: M.Salah
- Effective captain: João Pedro
- Chip used: none
- Predicted score: 66.68
- Actual score: 45.00
- Chip advisory: bench_boost (0.62): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Lewis -> J.Timber (projected gain 3.39, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Raya | GK | 1 | 5.5 | 4.12 | 13.28 | 21.56 | 2.00 | 91.7 | 90.0 |
| XI | XI | Sánchez | GK | 7 | 5.0 | 4.63 | 13.26 | 21.01 | 6.00 | 92.1 | 90.0 |
| XI | XI | Calafiori | DEF | 1 | 5.5 | 5.97 | 18.27 | 29.21 | 2.00 | 67.2 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 5.5 | 5.88 | 17.47 | 27.50 | 2.00 | 74.7 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 4.93 | 14.44 | 22.64 | 4.00 | 87.5 | 70.0 |
| Bench 3 | Bench | Ballard | DEF | 17 | 4.6 | 4.36 | 14.10 | 22.41 | 0.00 | 24.9 | 0.0 |
| Bench 4 | Bench | Aït-Nouri | DEF | 13 | 6.0 | 4.00 | 13.52 | 21.59 | 0.00 | 60.0 | 90.0 |
| Captain | Captain | João Pedro | FWD | 7 | 7.5 | 6.30 | 18.32 | 29.29 | 9.00 | 90.6 | 90.0 |
| XI | XI | Ekitiké | FWD | 12 | 8.6 | 5.03 | 16.32 | 26.73 | 2.00 | 79.5 | 78.0 |
| XI | XI | Wood | FWD | 16 | 7.6 | 5.20 | 15.40 | 24.27 | 2.00 | 75.7 | 72.0 |
| Vice Captain | XI | M.Salah | MID | 12 | 14.5 | 6.06 | 18.77 | 30.22 | 3.00 | 88.8 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 7.1 | 5.89 | 18.45 | 29.46 | 2.00 | 82.1 | 90.0 |
| XI | XI | Reijnders | MID | 13 | 5.6 | 5.13 | 16.42 | 25.69 | 2.00 | 83.1 | 90.0 |
| XI | XI | Kudus | MID | 18 | 6.5 | 5.37 | 16.39 | 25.94 | 2.00 | 83.2 | 90.0 |
| Bench 2 | Bench | Stach | MID | 11 | 5.0 | 4.47 | 12.66 | 19.45 | 3.00 | 80.4 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 0.50 -> 0.10
- Free transfers: 2 -> 2
- Captain: M.Salah
- Vice captain: João Pedro
- Effective captain: M.Salah
- Chip used: none
- Predicted score: 63.46
- Actual score: 70.00
- Chip advisory: bench_boost (0.67): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Ballard -> Chalobah (projected gain 2.03, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Sánchez | GK | 7 | 5.0 | 4.15 | 12.53 | 19.92 | 2.00 | 90.4 | 90.0 |
| Bench 1 | Bench | Raya | GK | 1 | 5.5 | 4.12 | 11.84 | 18.95 | 6.00 | 89.4 | 90.0 |
| XI | XI | Calafiori | DEF | 1 | 5.6 | 5.38 | 15.40 | 24.23 | 5.00 | 76.2 | 67.0 |
| XI | XI | J.Timber | DEF | 1 | 5.6 | 5.30 | 15.34 | 24.05 | 8.00 | 45.1 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.88 | 14.27 | 22.19 | 6.00 | 78.6 | 90.0 |
| XI | XI | Chalobah | DEF | 7 | 5.0 | 4.62 | 13.96 | 21.67 | 3.00 | 82.2 | 90.0 |
| Bench 4 | Bench | Aït-Nouri | DEF | 13 | 6.0 | 3.77 | 11.41 | 18.67 | 0.00 | 47.8 | 0.0 |
| Vice Captain | XI | João Pedro | FWD | 7 | 7.6 | 5.70 | 18.18 | 28.79 | 7.00 | 67.7 | 78.0 |
| XI | XI | Ekitiké | FWD | 12 | 8.7 | 5.00 | 15.48 | 25.03 | 2.00 | 65.2 | 71.0 |
| Bench 3 | Bench | Wood | FWD | 16 | 7.7 | 4.26 | 14.89 | 24.46 | 1.00 | 73.3 | 59.0 |
| Captain | Captain | M.Salah | MID | 12 | 14.5 | 6.33 | 18.62 | 29.58 | 9.00 | 85.6 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 7.3 | 5.68 | 17.61 | 27.87 | 13.00 | 77.5 | 90.0 |
| XI | XI | Kudus | MID | 18 | 6.6 | 5.29 | 15.86 | 24.91 | 3.00 | 82.6 | 90.0 |
| XI | XI | Reijnders | MID | 13 | 5.7 | 4.80 | 14.00 | 22.02 | 3.00 | 87.2 | 90.0 |
| Bench 2 | Bench | Stach | MID | 11 | 5.0 | 4.28 | 11.99 | 18.52 | 1.00 | 80.8 | 90.0 |

## GW5

- Train rows: 164124
- Bank: 0.10 -> 0.50
- Free transfers: 2 -> 2
- Captain: M.Salah
- Vice captain: Semenyo
- Effective captain: M.Salah
- Chip used: none
- Predicted score: 63.56
- Actual score: 42.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Aït-Nouri -> Muñoz (projected gain 1.32, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.5 | 4.07 | 12.15 | 19.26 | 2.00 | 87.9 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 5.0 | 3.76 | 11.32 | 18.16 | -3.00 | 87.2 | 4.0 |
| XI | XI | Calafiori | DEF | 1 | 5.7 | 4.96 | 15.17 | 24.37 | 2.00 | 70.2 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 5.7 | 5.05 | 14.43 | 22.77 | 1.00 | 79.1 | 79.0 |
| XI | XI | Muñoz | DEF | 8 | 5.6 | 5.04 | 14.24 | 22.10 | 2.00 | 83.2 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.83 | 13.98 | 22.13 | 1.00 | 85.6 | 88.0 |
| Bench 4 | Bench | Chalobah | DEF | 7 | 5.1 | 2.81 | 8.54 | 13.61 | 8.00 | 52.6 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.7 | 5.87 | 17.81 | 28.52 | 2.00 | 89.5 | 90.0 |
| XI | XI | Ekitiké | FWD | 12 | 8.8 | 4.73 | 15.32 | 25.33 | 8.00 | 47.2 | 66.0 |
| XI | XI | Wood | FWD | 16 | 7.7 | 4.25 | 12.77 | 21.34 | 2.00 | 70.1 | 74.0 |
| Captain | Captain | M.Salah | MID | 12 | 14.5 | 6.69 | 19.69 | 31.38 | 5.00 | 87.5 | 90.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.4 | 6.36 | 19.18 | 30.50 | 5.00 | 80.0 | 90.0 |
| XI | XI | Kudus | MID | 18 | 6.6 | 5.02 | 14.85 | 24.00 | 7.00 | 83.2 | 90.0 |
| Bench 2 | Bench | Reijnders | MID | 13 | 5.7 | 4.11 | 13.08 | 21.50 | 9.00 | 84.1 | 90.0 |
| Bench 3 | Bench | Stach | MID | 11 | 5.0 | 4.05 | 10.96 | 17.08 | 15.00 | 79.7 | 90.0 |

## GW6

- Train rows: 164865
- Bank: 0.50 -> 0.00
- Free transfers: 2 -> 2
- Captain: M.Salah
- Vice captain: Semenyo
- Effective captain: M.Salah
- Chip used: none
- Predicted score: 61.53
- Actual score: 27.00
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Stach -> Anthony (projected gain 2.09, hit 0)
- Autosub outfielders: J.Timber.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.5 | 3.65 | 10.87 | 17.21 | 2.00 | 87.4 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 5.0 | 3.11 | 9.53 | 15.83 | 1.00 | 64.9 | 90.0 |
| XI | XI | Calafiori | DEF | 1 | 5.7 | 4.33 | 13.62 | 21.07 | 1.00 | 79.0 | 69.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.64 | 13.37 | 20.37 | 1.00 | 86.2 | 27.0 |
| Bench 2 | Autosub In | J.Timber | DEF | 1 | 5.7 | 4.12 | 13.09 | 20.22 | 2.00 | 76.7 | 90.0 |
| XI | XI | Muñoz | DEF | 8 | 5.6 | 4.57 | 13.02 | 20.35 | 2.00 | 85.7 | 90.0 |
| Bench 4 | Bench | Chalobah | DEF | 7 | 5.1 | 3.41 | 10.54 | 15.94 | -3.00 | 70.1 | 52.0 |
| XI | XI | João Pedro | FWD | 7 | 7.8 | 5.86 | 17.37 | 27.07 | 2.00 | 94.5 | 90.0 |
| XI | Bench | Ekitiké | FWD | 12 | 8.8 | 4.31 | 14.13 | 22.73 | 0.00 | 65.1 | 0.0 |
| XI | XI | Wood | FWD | 16 | 7.6 | 4.34 | 12.92 | 20.42 | 2.00 | 72.2 | 89.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.6 | 5.92 | 19.03 | 29.04 | 7.00 | 85.8 | 90.0 |
| Captain | Captain | M.Salah | MID | 12 | 14.5 | 6.63 | 18.90 | 30.94 | 2.00 | 85.7 | 90.0 |
| XI | XI | Kudus | MID | 18 | 6.6 | 5.63 | 15.22 | 24.40 | 2.00 | 85.8 | 90.0 |
| XI | XI | Reijnders | MID | 13 | 5.7 | 5.03 | 14.20 | 21.90 | 2.00 | 89.8 | 82.0 |
| Bench 3 | Bench | Anthony | MID | 3 | 5.5 | 3.86 | 11.82 | 19.16 | 6.00 | 85.9 | 87.0 |

## GW7

- Train rows: 165607
- Bank: 0.00 -> 0.90
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: M.Salah
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 60.56
- Actual score: 84.00
- Transfer: Muñoz -> Guéhi (projected gain 2.35, hit 0)
- Autosub outfielders: Anthony.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.6 | 4.14 | 11.66 | 18.43 | 6.00 | 85.7 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.9 | 3.01 | 9.21 | 15.54 | 2.00 | 65.3 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 4.7 | 4.82 | 14.13 | 22.25 | 3.00 | 89.0 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 5.8 | 4.75 | 13.28 | 20.94 | 11.00 | 78.6 | 90.0 |
| XI | XI | Calafiori | DEF | 1 | 5.7 | 4.60 | 12.94 | 20.75 | 6.00 | 51.6 | 74.0 |
| XI | Bench | Chalobah | DEF | 7 | 5.2 | 4.00 | 12.26 | 19.96 | 0.00 | 65.2 | 0.0 |
| Bench 3 | Bench | Pedro Porro | DEF | 18 | 5.6 | 3.84 | 11.60 | 20.14 | 7.00 | 41.4 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.8 | 5.37 | 16.24 | 26.52 | 2.00 | 88.3 | 73.0 |
| XI | XI | Wood | FWD | 16 | 7.5 | 4.14 | 12.54 | 20.44 | 2.00 | 74.2 | 63.0 |
| Bench 4 | Bench | Ekitiké | FWD | 12 | 8.7 | 1.31 | 5.16 | 9.73 | 1.00 | 17.8 | 16.0 |
| Captain | Captain | Semenyo | MID | 4 | 7.7 | 6.64 | 19.55 | 30.90 | 18.00 | 90.1 | 90.0 |
| Vice Captain | XI | M.Salah | MID | 12 | 14.5 | 6.01 | 18.28 | 30.29 | 2.00 | 81.7 | 90.0 |
| XI | XI | Kudus | MID | 18 | 6.7 | 5.11 | 14.58 | 23.54 | 12.00 | 83.0 | 89.0 |
| XI | XI | Reijnders | MID | 13 | 5.7 | 4.33 | 13.62 | 21.83 | 3.00 | 81.9 | 75.0 |
| Bench 2 | Autosub In | Anthony | MID | 3 | 5.6 | 3.92 | 11.92 | 19.15 | 1.00 | 82.4 | 58.0 |

## GW8

- Train rows: 166350
- Bank: 0.90 -> 1.20
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: M.Salah
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 61.92
- Actual score: 41.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Chalobah -> Senesi (projected gain 2.38, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.6 | 4.07 | 11.96 | 18.89 | 6.00 | 87.0 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.9 | 3.07 | 8.75 | 14.00 | 5.00 | 76.7 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 4.8 | 5.05 | 15.01 | 23.72 | 4.00 | 90.2 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.9 | 4.50 | 14.40 | 23.66 | 2.00 | 83.6 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 5.8 | 4.51 | 12.92 | 20.50 | 6.00 | 82.6 | 90.0 |
| XI | XI | Calafiori | DEF | 1 | 5.7 | 4.35 | 12.42 | 19.98 | 6.00 | 75.2 | 90.0 |
| Bench 2 | Bench | Pedro Porro | DEF | 18 | 5.6 | 4.19 | 12.09 | 19.99 | 1.00 | 81.8 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.7 | 4.95 | 15.16 | 25.37 | 2.00 | 58.4 | 90.0 |
| Bench 4 | Bench | Ekitiké | FWD | 12 | 8.7 | 3.80 | 11.73 | 20.58 | 1.00 | 26.4 | 28.0 |
| Bench 3 | Bench | Wood | FWD | 16 | 7.4 | 4.03 | 11.61 | 19.42 | 1.00 | 35.8 | 16.0 |
| Captain | Captain | Semenyo | MID | 4 | 7.8 | 7.08 | 20.84 | 33.18 | 4.00 | 103.1 | 90.0 |
| Vice Captain | XI | M.Salah | MID | 12 | 14.5 | 6.10 | 17.91 | 29.73 | 2.00 | 79.0 | 84.0 |
| XI | XI | Kudus | MID | 18 | 6.7 | 5.38 | 15.19 | 24.13 | 2.00 | 90.7 | 90.0 |
| XI | XI | Reijnders | MID | 13 | 5.8 | 4.61 | 13.21 | 21.37 | 1.00 | 82.3 | 58.0 |
| XI | XI | Anthony | MID | 3 | 5.7 | 4.24 | 12.00 | 19.55 | 2.00 | 75.5 | 82.0 |

## GW9

- Train rows: 167095
- Bank: 1.20 -> 0.40
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: João Pedro
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 61.83
- Actual score: 53.00
- Transfer: Anthony -> Ndiaye (projected gain 2.31, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.7 | 4.31 | 12.20 | 19.05 | 6.00 | 87.3 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.9 | 3.48 | 9.20 | 14.72 | 1.00 | 85.4 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 4.9 | 4.89 | 15.12 | 24.45 | 4.00 | 93.6 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 5.9 | 4.73 | 13.71 | 21.86 | 6.00 | 81.3 | 90.0 |
| XI | XI | Calafiori | DEF | 1 | 5.7 | 4.53 | 12.61 | 20.01 | 6.00 | 80.2 | 81.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 3.99 | 11.67 | 19.08 | 11.00 | 80.7 | 90.0 |
| Bench 2 | Bench | Senesi | DEF | 4 | 5.0 | 3.74 | 10.79 | 17.42 | 5.00 | 75.0 | 90.0 |
| Vice Captain | XI | João Pedro | FWD | 7 | 7.6 | 5.59 | 15.94 | 25.84 | 2.00 | 87.9 | 84.0 |
| Bench 4 | Bench | Ekitiké | FWD | 12 | 8.7 | 2.97 | 10.81 | 19.92 | 2.00 | 29.4 | 90.0 |
| Bench 3 | Bench | Wood | FWD | 16 | 7.3 | 3.31 | 10.71 | 18.79 | 0.00 | 25.3 | 0.0 |
| Captain | Captain | Semenyo | MID | 4 | 8.0 | 7.07 | 20.40 | 32.68 | 3.00 | 95.0 | 90.0 |
| XI | XI | M.Salah | MID | 12 | 14.4 | 5.57 | 17.20 | 29.15 | 6.00 | 65.3 | 90.0 |
| XI | XI | Kudus | MID | 18 | 6.8 | 5.23 | 15.42 | 24.60 | 3.00 | 85.9 | 77.0 |
| XI | XI | Ndiaye | MID | 9 | 6.5 | 4.76 | 13.77 | 22.77 | 2.00 | 83.3 | 90.0 |
| XI | XI | Reijnders | MID | 13 | 5.8 | 4.09 | 12.86 | 21.49 | 1.00 | 75.8 | 75.0 |

## GW10

- Train rows: 167841
- Bank: 0.40 -> 0.70
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: M.Salah
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 61.87
- Actual score: 65.00
- Transfer: Senesi -> Van de Ven (projected gain 2.91, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.7 | 4.38 | 12.04 | 18.67 | 6.00 | 87.4 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.9 | 3.00 | 8.48 | 13.60 | 6.00 | 83.5 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 4.9 | 5.27 | 15.44 | 24.85 | 10.00 | 92.0 | 90.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.7 | 5.29 | 14.73 | 23.33 | 2.00 | 99.0 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.0 | 5.06 | 14.37 | 23.06 | 6.00 | 85.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.32 | 12.29 | 19.42 | 2.00 | 88.5 | 72.0 |
| XI | XI | Calafiori | DEF | 1 | 5.8 | 4.49 | 12.17 | 19.03 | 6.00 | 79.3 | 71.0 |
| XI | XI | João Pedro | FWD | 7 | 7.5 | 5.23 | 15.55 | 25.79 | 9.00 | 80.9 | 90.0 |
| Bench 2 | Bench | Ekitiké | FWD | 12 | 8.6 | 3.79 | 11.85 | 20.08 | 2.00 | 44.8 | 76.0 |
| Bench 4 | Bench | Wood | FWD | 16 | 7.2 | 0.92 | 3.41 | 6.16 | 0.00 | 14.7 | 0.0 |
| Captain | Captain | Semenyo | MID | 4 | 8.1 | 6.31 | 19.02 | 30.91 | 2.00 | 100.2 | 90.0 |
| Vice Captain | XI | M.Salah | MID | 12 | 14.3 | 5.75 | 16.88 | 28.40 | 10.00 | 75.9 | 90.0 |
| XI | XI | Kudus | MID | 18 | 6.8 | 4.87 | 14.42 | 23.60 | 1.00 | 82.4 | 90.0 |
| XI | XI | Ndiaye | MID | 9 | 6.5 | 4.58 | 13.97 | 22.44 | 9.00 | 89.3 | 61.0 |
| Bench 3 | Bench | Reijnders | MID | 13 | 5.7 | 3.79 | 11.81 | 20.29 | 1.00 | 73.0 | 17.0 |

## GW11

- Train rows: 168588
- Bank: 0.70 -> 0.10
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: Guéhi
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 58.50
- Actual score: 21.00
- Transfer: Wood -> Mateta (projected gain 4.06, hit 0)
- Autosub outfielders: Ekitiké, Ndiaye.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.8 | 4.26 | 12.30 | 19.05 | 1.00 | 86.9 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.8 | 3.54 | 9.24 | 14.10 | 6.00 | 83.5 | 90.0 |
| Vice Captain | Bench | Guéhi | DEF | 8 | 5.0 | 5.66 | 15.89 | 25.55 | 0.00 | 93.3 | 0.0 |
| XI | XI | J.Timber | DEF | 1 | 6.1 | 4.53 | 13.65 | 21.77 | 1.00 | 84.2 | 90.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.7 | 4.77 | 13.64 | 21.89 | 1.00 | 90.5 | 90.0 |
| XI | XI | Calafiori | DEF | 1 | 5.8 | 3.90 | 11.65 | 18.54 | 1.00 | 78.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 3.95 | 11.56 | 18.86 | 2.00 | 78.4 | 66.0 |
| XI | XI | Mateta | FWD | 8 | 7.8 | 5.15 | 15.03 | 23.81 | 2.00 | 82.6 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.4 | 5.18 | 14.86 | 25.37 | 7.00 | 83.1 | 82.0 |
| Bench 2 | Autosub In | Ekitiké | FWD | 12 | 8.6 | 3.50 | 11.07 | 18.51 | 1.00 | 65.9 | 55.0 |
| Captain | Captain | Semenyo | MID | 4 | 8.1 | 6.06 | 18.22 | 29.32 | 0.00 | 96.2 | 90.0 |
| XI | XI | M.Salah | MID | 12 | 14.2 | 5.35 | 16.34 | 27.19 | 2.00 | 79.8 | 90.0 |
| XI | Bench | Reijnders | MID | 13 | 5.6 | 3.64 | 11.44 | 20.13 | 0.00 | 32.7 | 0.0 |
| Bench 3 | Autosub In | Ndiaye | MID | 9 | 6.5 | 3.27 | 9.40 | 14.97 | 3.00 | 58.2 | 90.0 |
| Bench 4 | Bench | Kudus | MID | 18 | 6.7 | 3.11 | 9.31 | 15.33 | 0.00 | 60.0 | 0.0 |

## GW12

- Train rows: 169340
- Bank: 0.10 -> 0.70
- Free transfers: 2 -> 2
- Captain: M.Salah
- Vice captain: João Pedro
- Effective captain: M.Salah
- Chip used: none
- Predicted score: 58.40
- Actual score: 24.00
- Transfer: Kudus -> Caicedo (projected gain 2.12, hit 0)
- Autosub outfielders: Calafiori, Pedro Porro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.45 | 12.31 | 19.07 | 2.00 | 84.5 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.8 | 3.45 | 9.33 | 14.11 | 6.00 | 81.5 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.1 | 4.94 | 13.93 | 23.23 | 5.00 | 36.1 | 90.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.8 | 4.38 | 13.21 | 21.41 | 0.00 | 93.4 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.1 | 4.55 | 13.03 | 20.81 | 5.00 | 83.4 | 90.0 |
| Bench 2 | Autosub In | Calafiori | DEF | 1 | 5.8 | 4.16 | 11.65 | 18.57 | 2.00 | 78.0 | 90.0 |
| Bench 3 | Autosub In | Pedro Porro | DEF | 18 | 5.5 | 3.15 | 10.36 | 17.55 | 0.00 | 76.2 | 12.0 |
| Vice Captain | XI | João Pedro | FWD | 7 | 7.4 | 5.66 | 15.79 | 24.66 | 1.00 | 87.7 | 75.0 |
| XI | XI | Mateta | FWD | 8 | 8.0 | 4.82 | 15.27 | 24.21 | 1.00 | 76.4 | 59.0 |
| XI | XI | Ekitiké | FWD | 12 | 8.6 | 4.24 | 11.58 | 18.04 | 1.00 | 41.3 | 35.0 |
| Captain | Captain | M.Salah | MID | 12 | 14.2 | 5.80 | 16.25 | 26.06 | 2.00 | 81.3 | 90.0 |
| XI | Bench | Semenyo | MID | 4 | 8.1 | 4.97 | 13.75 | 21.58 | 0.00 | 76.6 | 0.0 |
| XI | Bench | Caicedo | MID | 7 | 6.0 | 4.63 | 13.61 | 21.57 | 0.00 | 84.9 | 0.0 |
| XI | XI | Ndiaye | MID | 9 | 6.5 | 4.16 | 12.74 | 21.56 | 3.00 | 80.8 | 80.0 |
| Bench 4 | Bench | Reijnders | MID | 13 | 5.5 | 2.29 | 8.85 | 16.58 | 1.00 | 27.9 | 13.0 |

## GW13

- Train rows: 170095
- Bank: 0.70 -> 0.10
- Free transfers: 2 -> 2
- Captain: M.Salah
- Vice captain: Mbeumo
- Effective captain: Mbeumo
- Chip used: none
- Predicted score: 56.25
- Actual score: 15.00
- Transfer: Semenyo -> Mbeumo (projected gain 5.61, hit 0)
- Autosub outfielders: Calafiori.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 3.92 | 11.57 | 18.38 | 3.00 | 83.5 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.8 | 3.33 | 9.40 | 14.47 | 3.00 | 81.5 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.2 | 4.47 | 13.52 | 21.74 | 2.00 | 82.9 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.1 | 4.64 | 13.36 | 22.13 | 0.00 | 83.0 | 90.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.8 | 4.36 | 12.66 | 20.25 | 0.00 | 86.9 | 90.0 |
| Bench 2 | Autosub In | Calafiori | DEF | 1 | 5.8 | 3.65 | 10.88 | 17.68 | 0.00 | 79.7 | 45.0 |
| Bench 3 | Bench | Pedro Porro | DEF | 18 | 5.5 | 3.26 | 9.57 | 16.41 | 1.00 | 29.0 | 90.0 |
| XI | XI | Mateta | FWD | 8 | 8.1 | 4.71 | 14.94 | 24.20 | 6.00 | 74.4 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.5 | 5.33 | 14.90 | 23.76 | 1.00 | 87.9 | 54.0 |
| XI | XI | Ekitiké | FWD | 12 | 8.6 | 4.14 | 11.85 | 18.80 | 1.00 | 58.0 | 22.0 |
| Vice Captain | Captain | Mbeumo | MID | 14 | 8.6 | 5.54 | 16.42 | 25.91 | 1.00 | 85.9 | 90.0 |
| Captain | Bench | M.Salah | MID | 12 | 14.2 | 5.61 | 16.05 | 25.55 | 0.00 | 80.0 | 0.0 |
| XI | XI | Caicedo | MID | 7 | 6.1 | 3.70 | 11.96 | 20.52 | -2.00 | 62.2 | 37.0 |
| XI | XI | Ndiaye | MID | 9 | 6.6 | 4.22 | 11.61 | 19.91 | 2.00 | 68.0 | 79.0 |
| Bench 4 | Bench | Reijnders | MID | 13 | 5.4 | 3.01 | 9.64 | 16.66 | 3.00 | 21.3 | 74.0 |

## GW14

- Train rows: 170850
- Bank: 0.10 -> 2.00
- Free transfers: 2 -> 2
- Captain: Mbeumo
- Vice captain: M.Salah
- Effective captain: Mbeumo
- Chip used: none
- Predicted score: 55.48
- Actual score: 42.00
- Transfer: Ekitiké -> Thiago (projected gain 5.59, hit 0)
- Autosub outfielders: Pedro Porro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.04 | 11.40 | 17.93 | 6.00 | 84.8 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.8 | 3.44 | 9.57 | 14.96 | 1.00 | 83.7 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 4.74 | 13.57 | 21.60 | 1.00 | 83.4 | 46.0 |
| XI | Bench | Van de Ven | DEF | 18 | 4.8 | 4.09 | 12.49 | 19.95 | 0.00 | 85.8 | 0.0 |
| XI | XI | Guéhi | DEF | 8 | 5.1 | 4.19 | 12.17 | 19.99 | 14.00 | 82.1 | 90.0 |
| XI | XI | Calafiori | DEF | 1 | 5.8 | 3.52 | 10.58 | 17.35 | 7.00 | 71.1 | 90.0 |
| Bench 2 | Autosub In | Pedro Porro | DEF | 18 | 5.4 | 3.43 | 10.33 | 16.70 | 1.00 | 75.5 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 6.6 | 5.10 | 15.81 | 25.46 | 1.00 | 89.4 | 30.0 |
| XI | XI | João Pedro | FWD | 7 | 7.5 | 4.61 | 14.19 | 23.72 | 2.00 | 66.0 | 90.0 |
| XI | XI | Mateta | FWD | 8 | 8.1 | 4.94 | 13.67 | 21.71 | 2.00 | 84.1 | 63.0 |
| Captain | Captain | Mbeumo | MID | 14 | 8.6 | 5.59 | 15.79 | 25.46 | 2.00 | 87.1 | 90.0 |
| Vice Captain | XI | M.Salah | MID | 12 | 14.2 | 5.21 | 15.56 | 26.00 | 1.00 | 55.8 | 45.0 |
| Bench 3 | Bench | Caicedo | MID | 7 | 6.0 | 3.34 | 11.04 | 19.85 | 0.00 | 62.0 | 0.0 |
| XI | XI | Ndiaye | MID | 9 | 6.6 | 3.86 | 11.02 | 18.17 | 3.00 | 78.7 | 90.0 |
| Bench 4 | Bench | Reijnders | MID | 13 | 5.4 | 3.00 | 9.22 | 15.21 | 7.00 | 41.8 | 81.0 |

## GW15

- Train rows: 171608
- Bank: 2.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mbeumo
- Vice captain: Semenyo
- Effective captain: Mbeumo
- Chip used: none
- Predicted score: 56.66
- Actual score: 44.00
- Transfer: Caicedo -> Semenyo (projected gain 6.00, hit 0)
- Autosub outfielders: Pedro Porro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.08 | 11.98 | 19.02 | 2.00 | 87.7 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.8 | 3.27 | 9.40 | 14.73 | 10.00 | 83.9 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.1 | 4.74 | 13.92 | 22.03 | 8.00 | 94.1 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 4.38 | 13.45 | 22.05 | 3.00 | 76.8 | 90.0 |
| XI | XI | Calafiori | DEF | 1 | 5.8 | 3.71 | 11.41 | 18.46 | 1.00 | 82.5 | 85.0 |
| Bench 3 | Bench | Van de Ven | DEF | 18 | 4.8 | 3.45 | 10.29 | 17.69 | 6.00 | 37.7 | 90.0 |
| Bench 2 | Autosub In | Pedro Porro | DEF | 18 | 5.4 | 3.60 | 10.15 | 16.32 | 5.00 | 80.9 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.4 | 4.67 | 14.70 | 23.78 | 1.00 | 81.7 | 32.0 |
| XI | XI | Mateta | FWD | 8 | 8.1 | 4.76 | 14.06 | 22.81 | 2.00 | 76.5 | 65.0 |
| XI | XI | Thiago | FWD | 5 | 6.7 | 4.60 | 13.64 | 22.18 | 2.00 | 75.1 | 90.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.8 | 5.50 | 16.02 | 26.05 | 3.00 | 85.0 | 90.0 |
| Captain | Captain | Mbeumo | MID | 14 | 8.6 | 5.61 | 15.61 | 25.13 | 8.00 | 85.1 | 90.0 |
| XI | Bench | M.Salah | MID | 12 | 14.1 | 4.96 | 15.09 | 25.15 | 0.00 | 61.5 | 0.0 |
| XI | XI | Reijnders | MID | 13 | 5.3 | 4.02 | 10.89 | 16.86 | 1.00 | 74.4 | 21.0 |
| Bench 4 | Bench | Ndiaye | MID | 9 | 6.6 | 2.73 | 7.61 | 12.28 | 8.00 | 56.9 | 90.0 |

## GW16

- Train rows: 172367
- Bank: 0.10 -> 0.40
- Free transfers: 2 -> 2
- Captain: Mbeumo
- Vice captain: Semenyo
- Effective captain: Mbeumo
- Chip used: none
- Predicted score: 56.73
- Actual score: 25.00
- Transfer: Reijnders -> Dewsbury-Hall (projected gain 1.76, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.38 | 11.73 | 18.19 | 2.00 | 88.9 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.8 | 3.35 | 9.57 | 15.19 | 6.00 | 87.3 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.1 | 4.86 | 14.31 | 22.65 | 1.00 | 92.8 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 4.85 | 13.63 | 21.35 | 2.00 | 87.0 | 90.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.7 | 4.09 | 11.75 | 19.44 | 1.00 | 81.3 | 90.0 |
| Bench 3 | Bench | Pedro Porro | DEF | 18 | 5.4 | 3.75 | 10.58 | 16.88 | 0.00 | 85.8 | 90.0 |
| Bench 4 | Bench | Calafiori | DEF | 1 | 5.8 | 2.68 | 7.37 | 11.60 | 0.00 | 54.8 | 0.0 |
| XI | XI | Thiago | FWD | 5 | 6.8 | 4.88 | 14.77 | 23.81 | 2.00 | 79.8 | 90.0 |
| XI | XI | Mateta | FWD | 8 | 8.1 | 4.72 | 14.24 | 23.47 | 2.00 | 66.6 | 62.0 |
| XI | XI | João Pedro | FWD | 7 | 7.4 | 4.48 | 13.78 | 23.37 | 2.00 | 71.1 | 80.0 |
| Captain | Captain | Mbeumo | MID | 14 | 8.5 | 5.41 | 15.34 | 25.16 | 2.00 | 87.2 | 90.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.7 | 4.98 | 14.96 | 24.47 | 6.00 | 85.4 | 90.0 |
| XI | XI | Dewsbury-Hall | MID | 9 | 5.0 | 4.56 | 13.50 | 21.67 | 1.00 | 89.9 | 15.0 |
| XI | XI | Ndiaye | MID | 9 | 6.5 | 4.11 | 12.30 | 19.92 | 2.00 | 60.4 | 90.0 |
| Bench 2 | Bench | M.Salah | MID | 12 | 14.1 | 3.81 | 12.00 | 21.31 | 7.00 | 17.1 | 64.0 |

## GW17

- Train rows: 173127
- Bank: 0.40 -> 0.20
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: M.Salah
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 53.18
- Actual score: 44.00
- Transfer: Van de Ven -> Cash (projected gain 1.26, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.97 | 11.54 | 18.21 | 7.00 | 87.2 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.9 | 3.10 | 9.32 | 15.03 | 4.00 | 86.9 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 4.80 | 14.08 | 22.27 | 1.00 | 89.1 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.5 | 4.23 | 12.96 | 21.41 | 6.00 | 79.8 | 90.0 |
| XI | XI | Cash | DEF | 2 | 4.9 | 4.16 | 12.49 | 20.12 | 2.00 | 58.2 | 90.0 |
| Bench 2 | Bench | Pedro Porro | DEF | 18 | 5.3 | 3.49 | 10.10 | 16.37 | 1.00 | 83.5 | 90.0 |
| Bench 4 | Bench | Calafiori | DEF | 1 | 5.7 | 2.15 | 7.89 | 15.48 | 6.00 | 23.0 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.3 | 4.17 | 13.18 | 22.51 | 6.00 | 75.8 | 90.0 |
| XI | XI | Mateta | FWD | 8 | 7.9 | 3.56 | 12.98 | 24.08 | 2.00 | 57.7 | 76.0 |
| Bench 3 | Bench | Thiago | FWD | 5 | 7.1 | 3.05 | 9.66 | 15.40 | 2.00 | 46.8 | 90.0 |
| Vice Captain | Bench | M.Salah | MID | 12 | 14.0 | 5.26 | 15.60 | 25.96 | 0.00 | 63.1 | 0.0 |
| Captain | Captain | Semenyo | MID | 4 | 7.6 | 5.32 | 14.84 | 24.25 | 10.00 | 86.6 | 90.0 |
| XI | Bench | Mbeumo | MID | 14 | 8.3 | 4.48 | 14.23 | 24.95 | 0.00 | 78.8 | 0.0 |
| XI | Bench | Dewsbury-Hall | MID | 9 | 5.1 | 4.04 | 13.33 | 22.55 | 0.00 | 63.3 | 0.0 |
| XI | Bench | Ndiaye | MID | 9 | 6.4 | 3.86 | 11.55 | 19.28 | 0.00 | 79.6 | 0.0 |

## GW18

- Train rows: 173897
- Bank: 0.20 -> 0.80
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: Guéhi
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 53.23
- Actual score: 43.00
- Transfer: Ndiaye -> Wilson (projected gain 5.09, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.07 | 11.43 | 17.97 | 2.00 | 90.1 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.9 | 3.42 | 9.67 | 15.55 | 3.00 | 88.0 | 90.0 |
| Vice Captain | XI | Guéhi | DEF | 8 | 5.3 | 4.87 | 13.66 | 21.69 | 2.00 | 90.5 | 90.0 |
| XI | Bench | J.Timber | DEF | 1 | 6.5 | 4.66 | 13.04 | 20.63 | 0.00 | 87.5 | 0.0 |
| XI | XI | Cash | DEF | 2 | 4.9 | 3.49 | 10.53 | 17.30 | 1.00 | 83.3 | 90.0 |
| Bench 3 | Bench | Calafiori | DEF | 1 | 5.7 | 3.25 | 9.48 | 15.65 | 0.00 | 74.2 | 0.0 |
| Bench 2 | Bench | Pedro Porro | DEF | 18 | 5.3 | 3.29 | 9.43 | 15.41 | 6.00 | 81.5 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.2 | 4.59 | 13.50 | 21.70 | 5.00 | 83.3 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.2 | 4.44 | 12.79 | 20.87 | 8.00 | 76.0 | 68.0 |
| XI | XI | Mateta | FWD | 8 | 7.8 | 4.01 | 12.14 | 20.12 | 2.00 | 70.5 | 90.0 |
| Captain | Captain | Semenyo | MID | 4 | 7.6 | 5.28 | 15.57 | 25.11 | 9.00 | 89.3 | 90.0 |
| XI | XI | Wilson | MID | 10 | 5.7 | 4.86 | 14.50 | 23.45 | 5.00 | 77.6 | 90.0 |
| XI | Bench | M.Salah | MID | 12 | 14.0 | 4.14 | 12.42 | 20.93 | 0.00 | 17.0 | 0.0 |
| XI | Bench | Dewsbury-Hall | MID | 9 | 5.1 | 3.54 | 11.06 | 19.97 | 0.00 | 22.2 | 0.0 |
| Bench 4 | Bench | Mbeumo | MID | 14 | 8.2 | 3.03 | 10.52 | 20.72 | 0.00 | 19.4 | 0.0 |

## GW19

- Train rows: 174672
- Bank: 0.80 -> 1.60
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: Guéhi
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 51.82
- Actual score: 48.00
- Transfer: Mbeumo -> Rogers (projected gain 5.14, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.89 | 11.05 | 17.50 | 2.00 | 87.1 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.9 | 3.36 | 9.35 | 14.68 | 2.00 | 88.8 | 90.0 |
| Vice Captain | XI | Guéhi | DEF | 8 | 5.3 | 4.73 | 13.11 | 20.79 | 2.00 | 90.0 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.5 | 4.07 | 11.98 | 20.16 | 9.00 | 29.3 | 82.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 3.20 | 9.54 | 15.41 | 10.00 | 81.5 | 90.0 |
| Bench 4 | Bench | Calafiori | DEF | 1 | 5.7 | 2.08 | 6.87 | 12.67 | 0.00 | 18.9 | 0.0 |
| Bench 3 | Bench | Cash | DEF | 2 | 4.9 | 2.13 | 6.81 | 11.39 | 0.00 | 58.4 | 0.0 |
| XI | XI | Thiago | FWD | 5 | 7.1 | 4.52 | 13.31 | 22.52 | 2.00 | 80.3 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.2 | 4.49 | 12.30 | 19.78 | 1.00 | 73.1 | 27.0 |
| XI | XI | Mateta | FWD | 8 | 7.7 | 4.00 | 11.31 | 18.52 | 9.00 | 74.5 | 90.0 |
| Captain | Captain | Semenyo | MID | 4 | 7.7 | 5.46 | 15.85 | 25.14 | 5.00 | 94.2 | 90.0 |
| XI | XI | Rogers | MID | 2 | 7.3 | 4.64 | 14.63 | 24.00 | 1.00 | 86.0 | 81.0 |
| XI | Bench | M.Salah | MID | 12 | 14.0 | 3.66 | 11.08 | 18.76 | 0.00 | 36.5 | 0.0 |
| XI | XI | Wilson | MID | 10 | 5.8 | 3.68 | 10.62 | 16.92 | 2.00 | 68.1 | 84.0 |
| Bench 2 | Bench | Dewsbury-Hall | MID | 9 | 5.0 | 2.26 | 7.72 | 15.07 | 0.00 | 15.7 | 0.0 |

## GW20

- Train rows: 175452
- Bank: 1.60 -> 6.60
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: Semenyo
- Effective captain: Foden
- Chip used: none
- Predicted score: 54.66
- Actual score: 47.00
- Transfer: M.Salah -> Foden (projected gain 10.36, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.74 | 10.72 | 17.03 | 1.00 | 89.2 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.9 | 2.65 | 8.47 | 13.88 | 0.00 | 89.0 | 0.0 |
| XI | XI | Guéhi | DEF | 8 | 5.3 | 4.63 | 13.74 | 21.91 | 2.00 | 94.3 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 4.26 | 12.51 | 21.09 | 3.00 | 72.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.2 | 4.14 | 11.10 | 17.44 | 4.00 | 84.7 | 90.0 |
| Bench 2 | Bench | Cash | DEF | 2 | 4.9 | 2.70 | 8.20 | 14.94 | 5.00 | 28.6 | 89.0 |
| Bench 3 | Bench | Calafiori | DEF | 1 | 5.7 | 1.39 | 4.60 | 8.33 | 0.00 | 26.9 | 0.0 |
| XI | XI | Thiago | FWD | 5 | 7.0 | 4.29 | 12.32 | 20.30 | 17.00 | 81.4 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.2 | 3.69 | 11.39 | 18.93 | 2.00 | 70.3 | 61.0 |
| XI | XI | Mateta | FWD | 8 | 7.7 | 3.70 | 11.00 | 17.74 | 2.00 | 80.9 | 86.0 |
| Captain | Captain | Foden | MID | 13 | 9.0 | 6.14 | 17.75 | 28.80 | 2.00 | 86.8 | 90.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.7 | 5.51 | 16.02 | 25.33 | 1.00 | 92.4 | 90.0 |
| XI | XI | Wilson | MID | 10 | 5.8 | 4.84 | 13.83 | 22.23 | 6.00 | 83.9 | 84.0 |
| XI | XI | Rogers | MID | 2 | 7.4 | 3.59 | 10.04 | 16.11 | 5.00 | 62.0 | 90.0 |
| Bench 4 | Bench | Dewsbury-Hall | MID | 9 | 5.0 | 1.29 | 4.27 | 8.61 | 0.00 | 15.8 | 0.0 |

## GW21

- Train rows: 176242
- Bank: 6.60 -> 4.80
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: Semenyo
- Effective captain: Foden
- Chip used: none
- Predicted score: 57.43
- Actual score: 47.00
- Transfer: Dewsbury-Hall -> Cherki (projected gain 5.24, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.73 | 10.65 | 17.15 | 6.00 | 87.6 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.9 | 2.27 | 7.52 | 13.12 | 2.00 | 65.2 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.3 | 4.69 | 13.30 | 21.52 | 6.00 | 92.8 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 4.33 | 12.72 | 20.55 | 6.00 | 78.1 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.2 | 3.94 | 11.34 | 17.98 | 0.00 | 87.5 | 90.0 |
| Bench 3 | Bench | Cash | DEF | 2 | 4.8 | 3.28 | 9.56 | 15.67 | 6.00 | 75.6 | 90.0 |
| Bench 4 | Bench | Calafiori | DEF | 1 | 5.7 | 0.88 | 3.12 | 6.53 | 0.00 | 13.2 | 0.0 |
| XI | XI | Thiago | FWD | 5 | 6.9 | 5.24 | 13.97 | 22.15 | 12.00 | 91.8 | 81.0 |
| XI | XI | João Pedro | FWD | 7 | 7.2 | 4.02 | 11.86 | 19.16 | 1.00 | 71.7 | 15.0 |
| XI | XI | Mateta | FWD | 8 | 7.6 | 3.84 | 10.98 | 17.89 | 2.00 | 76.9 | 90.0 |
| Captain | Captain | Foden | MID | 13 | 8.9 | 6.03 | 17.10 | 27.99 | 2.00 | 85.6 | 72.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.7 | 5.46 | 15.39 | 24.69 | 6.00 | 91.6 | 90.0 |
| XI | XI | Cherki | MID | 13 | 6.8 | 5.26 | 15.27 | 23.71 | 1.00 | 87.3 | 17.0 |
| XI | XI | Rogers | MID | 2 | 7.5 | 4.85 | 14.77 | 23.68 | 3.00 | 81.8 | 90.0 |
| Bench 2 | Bench | Wilson | MID | 10 | 5.8 | 3.60 | 10.19 | 16.35 | 9.00 | 64.3 | 90.0 |

## GW22

- Train rows: 177037
- Bank: 4.80 -> 5.30
- Free transfers: 2 -> 2
- Captain: Bruno G.
- Vice captain: Foden
- Effective captain: Bruno G.
- Chip used: none
- Predicted score: 56.91
- Actual score: 39.00
- Transfer: Rogers -> Bruno G. (projected gain 3.13, hit 0)
- Autosub outfielders: João Pedro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.87 | 11.10 | 17.58 | 6.00 | 87.2 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.9 | 2.79 | 8.31 | 13.82 | 11.00 | 79.7 | 90.0 |
| XI | Bench | Guéhi | DEF | 8 | 5.3 | 4.66 | 13.56 | 21.91 | 0.00 | 94.3 | 0.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 4.59 | 13.35 | 20.93 | 5.00 | 84.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.2 | 4.12 | 11.42 | 17.77 | 4.00 | 85.4 | 90.0 |
| XI | XI | Cash | DEF | 2 | 4.8 | 3.74 | 10.37 | 16.36 | 2.00 | 79.1 | 90.0 |
| Bench 4 | Bench | Calafiori | DEF | 1 | 5.6 | 0.81 | 3.08 | 6.15 | 0.00 | 11.2 | 0.0 |
| XI | XI | Thiago | FWD | 5 | 7.0 | 4.96 | 14.05 | 22.08 | 2.00 | 69.0 | 90.0 |
| Bench 2 | Autosub In | João Pedro | FWD | 7 | 7.2 | 3.63 | 11.87 | 20.25 | 8.00 | 58.9 | 73.0 |
| Bench 3 | Bench | Mateta | FWD | 8 | 7.6 | 3.47 | 10.16 | 16.44 | 2.00 | 70.6 | 90.0 |
| Vice Captain | XI | Foden | MID | 13 | 8.8 | 5.26 | 15.77 | 26.08 | 1.00 | 74.5 | 45.0 |
| XI | XI | Semenyo | MID | 4 | 7.6 | 5.22 | 15.63 | 25.25 | 2.00 | 90.5 | 90.0 |
| XI | XI | Cherki | MID | 13 | 6.8 | 4.93 | 15.11 | 24.50 | 1.00 | 70.9 | 45.0 |
| Captain | Captain | Bruno G. | MID | 15 | 7.1 | 5.37 | 14.88 | 23.72 | 3.00 | 92.3 | 90.0 |
| XI | XI | Wilson | MID | 10 | 5.8 | 4.82 | 13.57 | 22.03 | 2.00 | 86.2 | 87.0 |

## GW23

- Train rows: 177836
- Bank: 5.30 -> 4.00
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: Thiago
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 59.08
- Actual score: 54.00
- Transfer: Mateta -> Ekitiké (projected gain 4.88, hit 0)
- Autosub outfielders: João Pedro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.19 | 11.83 | 18.54 | 1.00 | 86.9 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.9 | 3.07 | 9.01 | 14.50 | 3.00 | 81.3 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 4.76 | 13.65 | 21.26 | 1.00 | 85.2 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.3 | 4.06 | 11.79 | 20.03 | 6.00 | 34.8 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.2 | 4.20 | 11.57 | 18.38 | 1.00 | 87.7 | 45.0 |
| Bench 3 | Bench | Cash | DEF | 2 | 4.8 | 3.55 | 10.39 | 16.31 | 6.00 | 84.1 | 90.0 |
| Bench 4 | Bench | Calafiori | DEF | 1 | 5.6 | 0.79 | 2.65 | 4.96 | 0.00 | 11.1 | 0.0 |
| XI | XI | Ekitiké | FWD | 12 | 8.9 | 5.14 | 15.66 | 26.45 | 1.00 | 41.9 | 31.0 |
| Vice Captain | XI | Thiago | FWD | 5 | 7.1 | 5.56 | 14.88 | 23.34 | 2.00 | 72.7 | 90.0 |
| Bench 2 | Autosub In | João Pedro | FWD | 7 | 7.1 | 3.81 | 11.82 | 19.32 | 12.00 | 51.9 | 84.0 |
| Captain | Captain | Semenyo | MID | 4 | 7.6 | 5.57 | 15.93 | 25.71 | 8.00 | 87.3 | 90.0 |
| XI | Bench | Bruno G. | MID | 15 | 7.2 | 5.19 | 15.03 | 24.09 | 0.00 | 89.4 | 0.0 |
| XI | XI | Cherki | MID | 13 | 6.8 | 5.19 | 14.48 | 24.35 | 3.00 | 59.7 | 72.0 |
| XI | XI | Foden | MID | 13 | 8.7 | 4.75 | 14.25 | 24.75 | 1.00 | 45.6 | 29.0 |
| XI | XI | Wilson | MID | 10 | 5.9 | 4.89 | 13.71 | 22.47 | 10.00 | 83.6 | 90.0 |

## GW24

- Train rows: 178639
- Bank: 4.00 -> 2.70
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: Ekitiké
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 57.16
- Actual score: 72.00
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Calafiori -> Gabriel (projected gain 3.67, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.07 | 11.50 | 17.98 | 6.00 | 85.6 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.9 | 3.25 | 8.87 | 14.07 | 2.00 | 84.8 | 90.0 |
| XI | XI | Gabriel | DEF | 1 | 6.9 | 4.92 | 14.10 | 22.06 | 8.00 | 80.8 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 4.37 | 12.65 | 20.10 | 5.00 | 81.2 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 4.19 | 12.23 | 20.23 | 3.00 | 81.4 | 90.0 |
| Bench 3 | Bench | Cash | DEF | 2 | 4.8 | 3.79 | 10.57 | 16.38 | 2.00 | 86.4 | 90.0 |
| Bench 4 | Bench | Pedro Porro | DEF | 18 | 5.2 | 3.40 | 10.03 | 17.01 | 0.00 | 65.3 | 0.0 |
| Vice Captain | XI | Ekitiké | FWD | 12 | 8.9 | 5.11 | 14.93 | 24.81 | 13.00 | 61.1 | 83.0 |
| XI | XI | Thiago | FWD | 5 | 7.2 | 4.73 | 14.33 | 22.68 | 2.00 | 90.0 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.1 | 4.63 | 12.60 | 20.14 | 10.00 | 78.5 | 45.0 |
| Captain | Captain | Semenyo | MID | 4 | 7.7 | 5.86 | 16.62 | 26.55 | 7.00 | 92.1 | 90.0 |
| XI | XI | Cherki | MID | 13 | 6.7 | 4.73 | 13.57 | 23.05 | 8.00 | 69.3 | 68.0 |
| XI | XI | Foden | MID | 13 | 8.6 | 4.02 | 13.47 | 23.53 | 1.00 | 62.1 | 2.0 |
| XI | XI | Wilson | MID | 10 | 6.0 | 4.64 | 13.44 | 21.58 | 2.00 | 89.7 | 90.0 |
| Bench 2 | Bench | Bruno G. | MID | 15 | 7.3 | 3.90 | 12.60 | 22.33 | 0.00 | 62.4 | 0.0 |

## GW25

- Train rows: 179450
- Bank: 2.70 -> 1.60
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: Gabriel
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 58.32
- Actual score: 54.00
- Transfer: Foden -> B.Fernandes (projected gain 5.46, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.50 | 12.21 | 18.96 | 7.00 | 85.7 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.9 | 3.07 | 8.67 | 14.01 | 2.00 | 84.5 | 90.0 |
| Vice Captain | XI | Gabriel | DEF | 1 | 7.0 | 5.62 | 15.56 | 24.41 | 6.00 | 86.3 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 4.71 | 12.83 | 20.44 | 6.00 | 79.5 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 4.20 | 12.37 | 20.17 | 3.00 | 82.0 | 90.0 |
| Bench 2 | Bench | Cash | DEF | 2 | 4.8 | 3.74 | 10.71 | 17.04 | 2.00 | 81.6 | 90.0 |
| Bench 4 | Bench | Pedro Porro | DEF | 18 | 5.2 | 2.81 | 9.15 | 16.74 | 0.00 | 29.3 | 0.0 |
| XI | XI | João Pedro | FWD | 7 | 7.3 | 4.94 | 14.37 | 23.35 | 8.00 | 72.8 | 74.0 |
| XI | XI | Thiago | FWD | 5 | 7.2 | 4.11 | 13.91 | 23.00 | 5.00 | 85.3 | 90.0 |
| XI | XI | Ekitiké | FWD | 12 | 8.8 | 4.75 | 13.81 | 22.28 | 2.00 | 77.3 | 90.0 |
| Captain | Captain | Semenyo | MID | 4 | 7.8 | 5.69 | 16.49 | 26.55 | 2.00 | 92.2 | 90.0 |
| XI | XI | B.Fernandes | MID | 14 | 9.5 | 5.46 | 16.04 | 24.93 | 10.00 | 79.7 | 90.0 |
| XI | XI | Cherki | MID | 13 | 6.6 | 4.29 | 13.01 | 21.74 | 1.00 | 72.0 | 29.0 |
| XI | XI | Wilson | MID | 10 | 6.1 | 4.36 | 12.59 | 19.97 | 2.00 | 85.4 | 90.0 |
| Bench 3 | Bench | Bruno G. | MID | 15 | 7.2 | 3.11 | 10.94 | 20.82 | 11.00 | 17.2 | 90.0 |

## GW26

- Train rows: 180267
- Bank: 1.60 -> 0.60
- Free transfers: 2 -> 2
- Captain: Gabriel
- Vice captain: J.Timber
- Effective captain: Gabriel
- Chip used: triple_captain
- Predicted score: 75.37
- Actual score: 69.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (10.59) beats the best remaining Triple Captain opportunity (7.76).
- Chip advisory: triple_captain (0.60): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Cherki -> Rogers (projected gain 2.93, hit 0)
- Chip used: Triple Captain on Gabriel. Optimizer chose Triple Captain here because the current estimated captain upside (10.59) beats the best remaining Triple Captain opportunity (7.76).
- Autosub outfielders: Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 6.24 | 15.56 | 23.63 | 3.00 | 132.4 | 180.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.9 | 3.03 | 8.24 | 12.77 | 1.00 | 84.2 | 90.0 |
| Captain | Captain | Gabriel | DEF | 1 | 7.1 | 7.56 | 19.57 | 30.15 | 7.00 | 138.7 | 180.0 |
| Vice Captain | XI | J.Timber | DEF | 1 | 6.4 | 6.72 | 16.67 | 25.27 | 3.00 | 127.3 | 180.0 |
| XI | Bench | Cash | DEF | 2 | 4.8 | 3.77 | 10.45 | 16.57 | 0.00 | 82.4 | 0.0 |
| Bench 3 | Autosub In | Guéhi | DEF | 8 | 5.2 | 3.75 | 10.36 | 16.13 | 7.00 | 74.1 | 90.0 |
| Bench 4 | Bench | Pedro Porro | DEF | 18 | 5.2 | 1.13 | 3.64 | 6.51 | 0.00 | 18.4 | 0.0 |
| XI | XI | João Pedro | FWD | 7 | 7.5 | 5.46 | 15.24 | 23.87 | 10.00 | 73.3 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.1 | 4.51 | 14.17 | 23.48 | 2.00 | 86.3 | 90.0 |
| XI | XI | Ekitiké | FWD | 12 | 8.9 | 4.57 | 13.11 | 20.79 | 2.00 | 77.0 | 87.0 |
| XI | XI | B.Fernandes | MID | 14 | 9.7 | 5.96 | 16.50 | 26.29 | 2.00 | 81.2 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 7.8 | 5.88 | 16.23 | 25.83 | 14.00 | 90.7 | 90.0 |
| XI | XI | Rogers | MID | 2 | 7.6 | 5.25 | 15.35 | 24.44 | 2.00 | 91.0 | 90.0 |
| XI | XI | Bruno G. | MID | 15 | 7.1 | 4.33 | 13.51 | 22.99 | 3.00 | 70.4 | 90.0 |
| Bench 2 | Bench | Wilson | MID | 10 | 6.1 | 3.97 | 12.31 | 19.78 | 2.00 | 86.7 | 71.0 |

## GW27

- Train rows: 181084
- Bank: 0.60 -> 0.70
- Free transfers: 2 -> 2
- Captain: Gabriel
- Vice captain: Semenyo
- Effective captain: Gabriel
- Chip used: none
- Predicted score: 68.81
- Actual score: 33.00
- Transfer: Bruno G. -> Enzo (projected gain 1.25, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 5.19 | 14.35 | 22.00 | 3.00 | 116.2 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.9 | 3.11 | 8.20 | 12.63 | 2.00 | 82.0 | 90.0 |
| Captain | Captain | Gabriel | DEF | 1 | 7.1 | 7.29 | 20.72 | 32.03 | 2.00 | 128.8 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 5.82 | 16.20 | 24.87 | 3.00 | 118.5 | 56.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 5.03 | 14.35 | 22.37 | 2.00 | 95.2 | 90.0 |
| Bench 3 | Bench | Cash | DEF | 2 | 4.9 | 3.46 | 9.44 | 15.56 | 2.00 | 27.3 | 86.0 |
| Bench 4 | Bench | Pedro Porro | DEF | 18 | 5.2 | 0.98 | 4.03 | 7.78 | 0.00 | 19.8 | 0.0 |
| XI | XI | João Pedro | FWD | 7 | 7.6 | 5.87 | 15.82 | 24.55 | 7.00 | 85.6 | 79.0 |
| XI | XI | Thiago | FWD | 5 | 7.0 | 5.07 | 14.40 | 23.53 | 2.00 | 85.8 | 90.0 |
| XI | XI | Ekitiké | FWD | 12 | 8.9 | 4.88 | 13.47 | 21.12 | 2.00 | 77.6 | 90.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.9 | 6.07 | 16.84 | 26.68 | 4.00 | 94.0 | 86.0 |
| XI | XI | B.Fernandes | MID | 14 | 9.8 | 5.61 | 15.97 | 25.90 | 2.00 | 81.9 | 90.0 |
| XI | XI | Rogers | MID | 2 | 7.6 | 5.31 | 14.84 | 23.93 | 2.00 | 83.2 | 90.0 |
| XI | XI | Enzo | MID | 7 | 6.9 | 5.39 | 14.78 | 23.45 | 2.00 | 87.4 | 90.0 |
| Bench 2 | Bench | Wilson | MID | 10 | 6.0 | 3.73 | 11.48 | 19.18 | 8.00 | 76.6 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 0.70 -> 1.20
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: Gabriel
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 62.30
- Actual score: 90.00
- Transfer: J.Timber -> Virgil (projected gain 1.72, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.28 | 11.87 | 18.73 | 3.00 | 93.8 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.9 | 2.39 | 7.76 | 12.59 | 2.00 | 81.9 | 90.0 |
| Vice Captain | XI | Gabriel | DEF | 1 | 7.1 | 5.78 | 16.70 | 26.68 | 9.00 | 98.8 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 5.9 | 5.32 | 14.69 | 23.59 | 7.00 | 89.0 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 4.52 | 13.34 | 21.16 | 6.00 | 90.7 | 90.0 |
| Bench 3 | Bench | Cash | DEF | 2 | 4.9 | 3.48 | 9.78 | 15.91 | 0.00 | 73.8 | 90.0 |
| Bench 4 | Bench | Pedro Porro | DEF | 18 | 5.1 | 0.85 | 3.25 | 6.14 | 0.00 | 16.2 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.7 | 5.57 | 16.62 | 26.04 | 2.00 | 85.6 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.0 | 5.44 | 15.10 | 24.18 | 6.00 | 84.2 | 90.0 |
| XI | XI | Ekitiké | FWD | 12 | 8.9 | 4.91 | 13.57 | 20.91 | 15.00 | 76.5 | 75.0 |
| Captain | Captain | Semenyo | MID | 4 | 8.0 | 5.99 | 17.41 | 27.59 | 8.00 | 89.4 | 90.0 |
| XI | XI | B.Fernandes | MID | 14 | 9.8 | 5.60 | 15.80 | 25.34 | 13.00 | 82.3 | 90.0 |
| XI | XI | Enzo | MID | 7 | 6.9 | 4.33 | 13.56 | 22.01 | 1.00 | 83.7 | 85.0 |
| XI | XI | Wilson | MID | 10 | 5.9 | 4.56 | 13.16 | 20.65 | 12.00 | 87.6 | 71.0 |
| Bench 2 | Bench | Rogers | MID | 2 | 7.7 | 3.62 | 10.13 | 16.23 | 2.00 | 62.9 | 90.0 |

## GW29

- Train rows: 182721
- Bank: 1.20 -> 0.40
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: Gabriel
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 66.46
- Actual score: 69.00
- Transfer: Enzo -> Rice (projected gain 3.55, hit 0)
- Autosub outfielders: Rogers.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.12 | 11.86 | 18.60 | 7.00 | 92.9 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.9 | 2.65 | 8.09 | 12.98 | 0.00 | 83.3 | 0.0 |
| Vice Captain | XI | Gabriel | DEF | 1 | 7.1 | 5.81 | 17.27 | 26.97 | 11.00 | 111.5 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 6.0 | 5.52 | 15.66 | 24.71 | 1.00 | 89.7 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 4.88 | 13.50 | 21.15 | 1.00 | 90.8 | 90.0 |
| Bench 3 | Bench | Cash | DEF | 2 | 4.9 | 3.19 | 9.19 | 14.95 | -1.00 | 75.9 | 45.0 |
| Bench 4 | Bench | Pedro Porro | DEF | 18 | 5.1 | 2.64 | 7.49 | 11.82 | 1.00 | 34.5 | 73.0 |
| XI | XI | João Pedro | FWD | 7 | 7.7 | 5.65 | 16.22 | 25.65 | 19.00 | 84.9 | 84.0 |
| XI | XI | Thiago | FWD | 5 | 7.1 | 5.18 | 14.70 | 23.11 | 2.00 | 86.2 | 90.0 |
| XI | XI | Ekitiké | FWD | 12 | 8.9 | 5.13 | 14.66 | 22.70 | 2.00 | 73.0 | 90.0 |
| Captain | Captain | Semenyo | MID | 4 | 8.1 | 6.93 | 19.11 | 29.54 | 7.00 | 100.0 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.6 | 5.55 | 16.78 | 26.40 | 3.00 | 99.1 | 90.0 |
| XI | XI | B.Fernandes | MID | 14 | 9.9 | 5.75 | 16.74 | 26.58 | 8.00 | 90.5 | 90.0 |
| XI | Bench | Wilson | MID | 10 | 5.9 | 5.03 | 13.84 | 21.81 | 0.00 | 80.0 | 0.0 |
| Bench 2 | Autosub In | Rogers | MID | 2 | 7.7 | 4.71 | 13.35 | 21.29 | 1.00 | 84.6 | 90.0 |

## GW30

- Train rows: 183541
- Bank: 0.40 -> 1.00
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: João Pedro
- Effective captain: Semenyo
- Chip used: bench_boost
- Predicted score: 77.94
- Actual score: 55.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.63) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Wilson -> Anderson (projected gain 0.53, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.63) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.14 | 11.62 | 18.12 | 7.00 | 91.0 | 90.0 |
| Bench 1 | Bench Boost | Sánchez | GK | 7 | 4.9 | 2.38 | 7.23 | 12.20 | 3.00 | 31.8 | 90.0 |
| XI | XI | Gabriel | DEF | 1 | 7.1 | 5.26 | 15.52 | 24.66 | 9.00 | 96.3 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 6.1 | 5.18 | 14.78 | 23.11 | 2.00 | 87.2 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 4.51 | 12.41 | 19.27 | 2.00 | 87.8 | 90.0 |
| Bench 3 | Bench Boost | Cash | DEF | 2 | 4.8 | 2.68 | 8.35 | 13.46 | 0.00 | 72.8 | 0.0 |
| Bench 4 | Bench Boost | Pedro Porro | DEF | 18 | 5.1 | 2.48 | 7.44 | 11.49 | 2.00 | 42.3 | 90.0 |
| Vice Captain | XI | João Pedro | FWD | 7 | 7.6 | 6.88 | 18.86 | 29.52 | 2.00 | 94.1 | 90.0 |
| XI | XI | Ekitiké | FWD | 12 | 9.1 | 5.48 | 15.83 | 24.72 | 1.00 | 74.3 | 26.0 |
| XI | XI | Thiago | FWD | 5 | 7.2 | 5.05 | 13.93 | 21.55 | 6.00 | 87.3 | 90.0 |
| Captain | Captain | Semenyo | MID | 4 | 8.2 | 7.05 | 19.55 | 29.96 | 2.00 | 102.0 | 74.0 |
| XI | XI | B.Fernandes | MID | 14 | 10.0 | 6.33 | 18.44 | 28.97 | 10.00 | 94.1 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.5 | 4.74 | 14.13 | 23.44 | 3.00 | 83.0 | 90.0 |
| XI | XI | Anderson | MID | 16 | 5.4 | 4.64 | 12.78 | 20.10 | 2.00 | 89.1 | 87.0 |
| Bench 2 | Bench Boost | Rogers | MID | 2 | 7.6 | 4.09 | 12.52 | 20.28 | 2.00 | 83.9 | 90.0 |