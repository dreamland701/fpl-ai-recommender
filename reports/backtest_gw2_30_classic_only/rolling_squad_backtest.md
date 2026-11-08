# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW30
- Total predicted points: 1749.17
- Total actual points: 1471.00
- Average predicted points: 60.32
- Average actual points: 50.72
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
- Bank: 100.00 -> 2.00
- Free transfers: 1 -> 2
- Captain: M.Salah
- Vice captain: Ballard
- Effective captain: M.Salah
- Chip used: none
- Predicted score: 82.58
- Actual score: 52.00
- Chip advisory: bench_boost (0.67): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Sánchez | GK | 7 | 5.0 | 5.89 | 16.09 | 24.99 | 3.00 | 107.7 | 90.0 |
| Bench 1 | Bench | Raya | GK | 1 | 5.5 | 5.09 | 14.47 | 23.38 | 6.00 | 111.0 | 90.0 |
| Vice Captain | XI | Ballard | DEF | 17 | 4.5 | 7.50 | 20.58 | 32.14 | 1.00 | 115.1 | 8.0 |
| XI | XI | Calafiori | DEF | 1 | 5.5 | 6.71 | 18.49 | 29.28 | 13.00 | 87.2 | 63.0 |
| XI | XI | Aït-Nouri | DEF | 13 | 6.0 | 6.06 | 17.40 | 27.82 | 1.00 | 106.6 | 22.0 |
| Bench 3 | Bench | Pedro Porro | DEF | 18 | 5.5 | 5.77 | 17.36 | 27.91 | 5.00 | 107.4 | 90.0 |
| Bench 2 | Bench | Lewis | DEF | 13 | 5.0 | 5.91 | 16.82 | 26.99 | 1.00 | 88.5 | 90.0 |
| XI | XI | Ekitiké | FWD | 12 | 8.5 | 6.29 | 18.45 | 29.60 | 9.00 | 91.0 | 79.0 |
| XI | XI | Wood | FWD | 16 | 7.5 | 6.11 | 17.44 | 27.87 | 2.00 | 105.0 | 87.0 |
| Bench 4 | Bench | Richarlison | FWD | 18 | 6.5 | 5.24 | 15.93 | 26.00 | 4.00 | 97.6 | 77.0 |
| Captain | Captain | M.Salah | MID | 12 | 14.5 | 7.73 | 22.31 | 35.46 | 5.00 | 114.8 | 90.0 |
| XI | XI | Kudus | MID | 18 | 6.5 | 7.38 | 22.02 | 35.47 | 3.00 | 112.5 | 85.0 |
| XI | XI | Reijnders | MID | 13 | 5.5 | 7.43 | 21.01 | 33.26 | 2.00 | 113.9 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 7.0 | 7.33 | 20.05 | 31.39 | 6.00 | 112.3 | 90.0 |
| XI | XI | Stach | MID | 11 | 5.0 | 6.43 | 18.74 | 29.70 | 2.00 | 102.7 | 90.0 |

## GW3

- Train rows: 162672
- Bank: 2.00 -> 1.10
- Free transfers: 2 -> 2
- Captain: João Pedro
- Vice captain: M.Salah
- Effective captain: João Pedro
- Chip used: none
- Predicted score: 62.39
- Actual score: 44.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Richarlison -> João Pedro (projected gain 6.77, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Raya | GK | 1 | 5.5 | 4.12 | 13.28 | 21.56 | 2.00 | 92.7 | 90.0 |
| XI | XI | Sánchez | GK | 7 | 5.0 | 4.63 | 13.26 | 21.01 | 6.00 | 93.1 | 90.0 |
| XI | XI | Calafiori | DEF | 1 | 5.5 | 5.40 | 16.53 | 26.42 | 2.00 | 68.2 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 4.88 | 14.29 | 22.41 | 4.00 | 86.5 | 70.0 |
| XI | XI | Lewis | DEF | 13 | 5.0 | 3.61 | 11.00 | 17.29 | 1.00 | 72.1 | 5.0 |
| Bench 3 | Bench | Ballard | DEF | 17 | 4.6 | 3.12 | 10.07 | 16.01 | 0.00 | 38.9 | 0.0 |
| Bench 4 | Bench | Aït-Nouri | DEF | 13 | 6.0 | 2.92 | 9.88 | 15.78 | 0.00 | 44.0 | 90.0 |
| Captain | Captain | João Pedro | FWD | 7 | 7.5 | 6.30 | 18.32 | 29.29 | 9.00 | 92.6 | 90.0 |
| XI | XI | Ekitiké | FWD | 12 | 8.6 | 4.68 | 15.20 | 24.90 | 2.00 | 73.5 | 78.0 |
| XI | XI | Wood | FWD | 16 | 7.6 | 4.91 | 14.55 | 22.93 | 2.00 | 76.7 | 72.0 |
| Vice Captain | XI | M.Salah | MID | 12 | 14.5 | 6.06 | 18.77 | 30.22 | 3.00 | 88.8 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 7.1 | 5.57 | 17.45 | 27.86 | 2.00 | 78.1 | 90.0 |
| XI | XI | Reijnders | MID | 13 | 5.6 | 4.91 | 15.71 | 24.59 | 2.00 | 80.1 | 90.0 |
| XI | XI | Kudus | MID | 18 | 6.5 | 5.14 | 15.69 | 24.83 | 2.00 | 80.2 | 90.0 |
| Bench 2 | Bench | Stach | MID | 11 | 5.0 | 4.17 | 11.82 | 18.15 | 3.00 | 75.4 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 1.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: M.Salah
- Vice captain: João Pedro
- Effective captain: M.Salah
- Chip used: none
- Predicted score: 59.60
- Actual score: 68.00
- Transfer: Ballard -> J.Timber (projected gain 3.62, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Sánchez | GK | 7 | 5.0 | 4.15 | 12.53 | 19.92 | 2.00 | 90.4 | 90.0 |
| Bench 1 | Bench | Raya | GK | 1 | 5.5 | 4.08 | 11.72 | 18.76 | 6.00 | 88.4 | 90.0 |
| XI | XI | Calafiori | DEF | 1 | 5.6 | 4.87 | 13.95 | 21.95 | 5.00 | 69.2 | 67.0 |
| XI | XI | J.Timber | DEF | 1 | 5.6 | 4.64 | 13.42 | 21.05 | 8.00 | 63.1 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.49 | 13.13 | 20.42 | 6.00 | 72.6 | 90.0 |
| Bench 3 | Bench | Aït-Nouri | DEF | 13 | 6.0 | 3.26 | 9.86 | 16.13 | 0.00 | 62.8 | 0.0 |
| Bench 4 | Bench | Lewis | DEF | 13 | 5.0 | 2.65 | 7.90 | 12.81 | 0.00 | 42.9 | 0.0 |
| Vice Captain | XI | João Pedro | FWD | 7 | 7.6 | 5.64 | 18.00 | 28.49 | 7.00 | 87.7 | 78.0 |
| XI | XI | Ekitiké | FWD | 12 | 8.7 | 4.45 | 13.79 | 22.30 | 2.00 | 66.2 | 71.0 |
| Bench 2 | Bench | Wood | FWD | 16 | 7.7 | 3.74 | 13.06 | 21.45 | 1.00 | 64.3 | 59.0 |
| Captain | Captain | M.Salah | MID | 12 | 14.5 | 6.19 | 18.23 | 28.96 | 9.00 | 83.6 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 7.3 | 5.15 | 15.98 | 25.29 | 13.00 | 70.5 | 90.0 |
| XI | XI | Kudus | MID | 18 | 6.6 | 5.06 | 15.16 | 23.82 | 3.00 | 78.6 | 90.0 |
| XI | XI | Reijnders | MID | 13 | 5.7 | 4.75 | 13.85 | 21.79 | 3.00 | 86.2 | 90.0 |
| XI | XI | Stach | MID | 11 | 5.0 | 4.00 | 11.19 | 17.29 | 1.00 | 75.8 | 90.0 |

## GW5

- Train rows: 164124
- Bank: 0.10 -> 0.50
- Free transfers: 2 -> 2
- Captain: M.Salah
- Vice captain: Semenyo
- Effective captain: M.Salah
- Chip used: none
- Predicted score: 59.94
- Actual score: 49.00
- Transfer: Aït-Nouri -> Muñoz (projected gain 3.57, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.5 | 4.03 | 12.02 | 19.06 | 2.00 | 86.9 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 5.0 | 3.73 | 11.20 | 17.98 | -3.00 | 86.2 | 4.0 |
| XI | XI | Muñoz | DEF | 8 | 5.6 | 4.82 | 13.63 | 21.15 | 2.00 | 80.2 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.68 | 13.54 | 21.43 | 1.00 | 82.6 | 88.0 |
| XI | XI | J.Timber | DEF | 1 | 5.7 | 4.65 | 13.28 | 20.96 | 1.00 | 73.1 | 79.0 |
| XI | XI | Calafiori | DEF | 1 | 5.7 | 4.21 | 12.87 | 20.66 | 2.00 | 60.2 | 90.0 |
| Bench 4 | Bench | Lewis | DEF | 13 | 5.0 | 1.28 | 4.77 | 8.67 | 0.00 | 28.5 | 0.0 |
| XI | XI | João Pedro | FWD | 7 | 7.7 | 5.82 | 17.64 | 28.23 | 2.00 | 88.5 | 90.0 |
| XI | XI | Ekitiké | FWD | 12 | 8.8 | 3.93 | 12.72 | 21.03 | 8.00 | 57.2 | 66.0 |
| Bench 3 | Bench | Wood | FWD | 16 | 7.7 | 3.59 | 10.80 | 18.04 | 2.00 | 59.1 | 74.0 |
| Captain | Captain | M.Salah | MID | 12 | 14.5 | 6.55 | 19.29 | 30.74 | 5.00 | 85.5 | 90.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.4 | 5.93 | 17.89 | 28.45 | 5.00 | 75.0 | 90.0 |
| XI | XI | Kudus | MID | 18 | 6.6 | 4.81 | 14.21 | 22.96 | 7.00 | 79.2 | 90.0 |
| XI | XI | Reijnders | MID | 13 | 5.7 | 3.97 | 12.66 | 20.81 | 9.00 | 81.1 | 90.0 |
| Bench 2 | Bench | Stach | MID | 11 | 5.0 | 3.78 | 10.21 | 15.92 | 15.00 | 73.7 | 90.0 |

## GW6

- Train rows: 164865
- Bank: 0.50 -> 0.40
- Free transfers: 2 -> 2
- Captain: M.Salah
- Vice captain: João Pedro
- Effective captain: M.Salah
- Chip used: none
- Predicted score: 60.32
- Actual score: 22.00
- Transfer: Lewis -> Chalobah (projected gain 1.56, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.5 | 3.61 | 10.76 | 17.03 | 2.00 | 86.4 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 5.0 | 2.46 | 7.53 | 12.51 | 1.00 | 50.9 | 90.0 |
| XI | XI | Chalobah | DEF | 7 | 5.1 | 4.55 | 14.06 | 21.26 | -3.00 | 90.1 | 52.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.55 | 13.09 | 19.94 | 1.00 | 84.2 | 27.0 |
| XI | XI | Muñoz | DEF | 8 | 5.6 | 4.47 | 12.75 | 19.92 | 2.00 | 83.7 | 90.0 |
| XI | XI | Calafiori | DEF | 1 | 5.7 | 3.98 | 12.54 | 19.40 | 1.00 | 73.0 | 69.0 |
| Bench 4 | Bench | J.Timber | DEF | 1 | 5.7 | 3.73 | 11.86 | 18.33 | 2.00 | 69.7 | 90.0 |
| Vice Captain | XI | João Pedro | FWD | 7 | 7.8 | 5.86 | 17.37 | 27.07 | 2.00 | 96.5 | 90.0 |
| Bench 2 | Bench | Ekitiké | FWD | 12 | 8.8 | 3.84 | 12.58 | 20.25 | 0.00 | 66.1 | 0.0 |
| Bench 3 | Bench | Wood | FWD | 16 | 7.6 | 3.80 | 11.31 | 17.88 | 2.00 | 63.2 | 89.0 |
| XI | XI | Semenyo | MID | 4 | 7.6 | 5.79 | 18.63 | 28.43 | 7.00 | 83.8 | 90.0 |
| Captain | Captain | M.Salah | MID | 12 | 14.5 | 6.42 | 18.30 | 29.96 | 2.00 | 82.7 | 90.0 |
| XI | XI | Kudus | MID | 18 | 6.6 | 5.45 | 14.74 | 23.63 | 2.00 | 82.8 | 90.0 |
| XI | XI | Reijnders | MID | 13 | 5.7 | 5.03 | 14.20 | 21.90 | 2.00 | 89.8 | 82.0 |
| XI | XI | Stach | MID | 11 | 5.0 | 4.19 | 11.62 | 18.42 | 2.00 | 83.3 | 90.0 |

## GW7

- Train rows: 165607
- Bank: 0.40 -> 1.30
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: M.Salah
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 58.16
- Actual score: 91.00
- Transfer: Pedro Porro -> Guéhi (projected gain 3.53, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.6 | 4.01 | 11.29 | 17.84 | 6.00 | 82.7 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.9 | 2.68 | 8.20 | 13.85 | 2.00 | 66.3 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 4.7 | 4.82 | 14.13 | 22.25 | 3.00 | 89.0 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 5.8 | 4.38 | 12.22 | 19.27 | 11.00 | 72.6 | 90.0 |
| XI | XI | Muñoz | DEF | 8 | 5.6 | 4.04 | 11.26 | 18.44 | 8.00 | 79.1 | 90.0 |
| XI | XI | Calafiori | DEF | 1 | 5.7 | 3.96 | 11.15 | 17.87 | 6.00 | 61.6 | 74.0 |
| Bench 3 | Bench | Chalobah | DEF | 7 | 5.2 | 3.56 | 10.92 | 17.78 | 0.00 | 66.2 | 0.0 |
| XI | XI | João Pedro | FWD | 7 | 7.8 | 5.37 | 16.24 | 26.52 | 2.00 | 89.3 | 73.0 |
| XI | XI | Wood | FWD | 16 | 7.5 | 3.64 | 11.02 | 17.96 | 2.00 | 65.2 | 63.0 |
| Bench 4 | Bench | Ekitiké | FWD | 12 | 8.7 | 1.96 | 7.77 | 14.65 | 1.00 | 26.8 | 16.0 |
| Captain | Captain | Semenyo | MID | 4 | 7.7 | 6.64 | 19.55 | 30.90 | 18.00 | 90.1 | 90.0 |
| Vice Captain | XI | M.Salah | MID | 12 | 14.5 | 5.68 | 17.28 | 28.63 | 2.00 | 77.7 | 90.0 |
| XI | XI | Kudus | MID | 18 | 6.7 | 4.89 | 13.95 | 22.53 | 12.00 | 80.0 | 89.0 |
| XI | XI | Reijnders | MID | 13 | 5.7 | 4.09 | 12.87 | 20.62 | 3.00 | 76.9 | 75.0 |
| Bench 2 | Bench | Stach | MID | 11 | 5.0 | 3.59 | 10.62 | 16.75 | 2.00 | 77.4 | 66.0 |

## GW8

- Train rows: 166350
- Bank: 1.30 -> 1.60
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: M.Salah
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 60.21
- Actual score: 49.00
- Transfer: Chalobah -> Senesi (projected gain 4.30, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.6 | 3.99 | 11.72 | 18.50 | 6.00 | 85.0 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.9 | 2.78 | 7.93 | 12.69 | 5.00 | 69.7 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 4.8 | 5.05 | 15.01 | 23.72 | 4.00 | 91.2 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.9 | 4.31 | 13.77 | 22.64 | 2.00 | 79.6 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 5.8 | 4.31 | 12.35 | 19.60 | 6.00 | 78.6 | 90.0 |
| XI | XI | Muñoz | DEF | 8 | 5.6 | 4.42 | 12.31 | 19.85 | 10.00 | 85.5 | 90.0 |
| XI | XI | Calafiori | DEF | 1 | 5.7 | 3.88 | 11.08 | 17.83 | 6.00 | 67.2 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.7 | 4.74 | 14.50 | 24.26 | 2.00 | 78.4 | 90.0 |
| Bench 3 | Bench | Wood | FWD | 16 | 7.4 | 3.27 | 9.44 | 15.78 | 1.00 | 54.8 | 16.0 |
| Bench 4 | Bench | Ekitiké | FWD | 12 | 8.7 | 2.72 | 8.38 | 14.70 | 1.00 | 36.4 | 28.0 |
| Captain | Captain | Semenyo | MID | 4 | 7.8 | 7.08 | 20.84 | 33.18 | 4.00 | 104.1 | 90.0 |
| Vice Captain | XI | M.Salah | MID | 12 | 14.5 | 5.61 | 16.49 | 27.37 | 2.00 | 73.0 | 84.0 |
| XI | XI | Kudus | MID | 18 | 6.7 | 5.38 | 15.19 | 24.13 | 2.00 | 91.7 | 90.0 |
| XI | XI | Reijnders | MID | 13 | 5.8 | 4.36 | 12.49 | 20.20 | 1.00 | 78.3 | 58.0 |
| Bench 2 | Bench | Stach | MID | 11 | 5.0 | 3.34 | 9.55 | 15.36 | 2.00 | 72.4 | 72.0 |

## GW9

- Train rows: 167095
- Bank: 1.60 -> 1.00
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: João Pedro
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 61.78
- Actual score: 50.00
- Transfer: Calafiori -> Gabriel (projected gain 3.47, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.7 | 4.22 | 11.94 | 18.66 | 6.00 | 85.3 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.9 | 3.37 | 8.91 | 14.26 | 1.00 | 82.4 | 90.0 |
| XI | XI | Gabriel | DEF | 1 | 6.3 | 5.12 | 15.22 | 24.53 | 9.00 | 91.7 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 4.9 | 4.89 | 15.12 | 24.45 | 4.00 | 95.6 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 5.0 | 4.99 | 14.38 | 23.23 | 5.00 | 95.0 | 90.0 |
| XI | XI | Muñoz | DEF | 8 | 5.6 | 4.63 | 13.77 | 21.89 | 2.00 | 97.0 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 5.9 | 4.47 | 12.96 | 20.66 | 6.00 | 77.3 | 90.0 |
| Vice Captain | XI | João Pedro | FWD | 7 | 7.6 | 5.53 | 15.78 | 25.57 | 2.00 | 86.9 | 84.0 |
| Bench 4 | Bench | Ekitiké | FWD | 12 | 8.7 | 2.12 | 7.72 | 14.23 | 2.00 | 30.4 | 90.0 |
| Bench 3 | Bench | Wood | FWD | 16 | 7.3 | 2.37 | 7.65 | 13.42 | 0.00 | 38.3 | 0.0 |
| Captain | Captain | Semenyo | MID | 4 | 8.0 | 7.07 | 20.40 | 32.68 | 3.00 | 98.0 | 90.0 |
| XI | XI | M.Salah | MID | 12 | 14.4 | 4.97 | 15.33 | 25.98 | 6.00 | 66.3 | 90.0 |
| XI | XI | Kudus | MID | 18 | 6.8 | 5.12 | 15.10 | 24.09 | 3.00 | 83.9 | 77.0 |
| XI | XI | Reijnders | MID | 13 | 5.8 | 3.71 | 11.64 | 19.45 | 1.00 | 68.8 | 75.0 |
| Bench 2 | Bench | Stach | MID | 11 | 5.0 | 3.09 | 8.59 | 13.96 | 0.00 | 63.2 | 0.0 |

## GW10

- Train rows: 167841
- Bank: 1.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: Guéhi
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 60.39
- Actual score: 76.00
- Transfer: Reijnders -> Ndiaye (projected gain 3.48, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.7 | 4.33 | 11.92 | 18.48 | 6.00 | 86.4 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.9 | 2.87 | 8.12 | 13.02 | 6.00 | 80.5 | 90.0 |
| Vice Captain | XI | Guéhi | DEF | 8 | 4.9 | 5.27 | 15.44 | 24.85 | 10.00 | 93.0 | 90.0 |
| XI | XI | Gabriel | DEF | 1 | 6.4 | 4.93 | 14.94 | 24.48 | 12.00 | 86.2 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 5.0 | 4.30 | 13.94 | 23.22 | 3.00 | 92.4 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.0 | 4.90 | 13.92 | 22.34 | 6.00 | 83.5 | 90.0 |
| XI | XI | Muñoz | DEF | 8 | 5.6 | 4.63 | 13.45 | 21.36 | 6.00 | 89.5 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.5 | 5.06 | 15.05 | 24.97 | 9.00 | 81.9 | 90.0 |
| Bench 2 | Bench | Ekitiké | FWD | 12 | 8.6 | 3.08 | 9.64 | 16.32 | 2.00 | 54.8 | 76.0 |
| Bench 3 | Bench | Wood | FWD | 16 | 7.2 | 1.42 | 5.31 | 9.57 | 0.00 | 22.7 | 0.0 |
| Captain | Captain | Semenyo | MID | 4 | 8.1 | 6.31 | 19.02 | 30.91 | 2.00 | 101.2 | 90.0 |
| XI | XI | M.Salah | MID | 12 | 14.3 | 5.21 | 15.29 | 25.71 | 10.00 | 68.9 | 90.0 |
| XI | XI | Ndiaye | MID | 9 | 6.5 | 4.53 | 13.83 | 22.21 | 9.00 | 88.3 | 61.0 |
| XI | XI | Kudus | MID | 18 | 6.8 | 4.60 | 13.64 | 22.32 | 1.00 | 78.4 | 90.0 |
| Bench 4 | Bench | Stach | MID | 11 | 5.1 | 1.32 | 4.97 | 9.38 | 1.00 | 32.3 | 30.0 |

## GW11

- Train rows: 168588
- Bank: 0.20 -> 1.00
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: Guéhi
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 60.03
- Actual score: 29.00
- Transfer: Ekitiké -> Mateta (projected gain 1.60, hit 0)
- Autosub outfielders: Stach.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.8 | 4.17 | 12.04 | 18.65 | 1.00 | 84.9 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.8 | 3.38 | 8.84 | 13.49 | 6.00 | 79.5 | 90.0 |
| XI | XI | Gabriel | DEF | 1 | 6.5 | 5.24 | 16.47 | 27.04 | 1.00 | 90.4 | 90.0 |
| Vice Captain | Bench | Guéhi | DEF | 8 | 5.0 | 5.66 | 15.89 | 25.55 | 0.00 | 95.3 | 0.0 |
| XI | XI | Senesi | DEF | 4 | 5.0 | 4.50 | 13.48 | 22.56 | 2.00 | 96.3 | 90.0 |
| XI | XI | Muñoz | DEF | 8 | 5.7 | 4.51 | 13.33 | 21.73 | 6.00 | 83.4 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.1 | 4.38 | 13.21 | 21.07 | 1.00 | 81.2 | 90.0 |
| XI | XI | Mateta | FWD | 8 | 7.8 | 4.92 | 14.37 | 22.77 | 2.00 | 78.6 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.4 | 4.95 | 14.22 | 24.27 | 7.00 | 80.1 | 82.0 |
| Bench 4 | Bench | Wood | FWD | 16 | 7.2 | 1.36 | 4.30 | 7.78 | 0.00 | 16.6 | 0.0 |
| Captain | Captain | Semenyo | MID | 4 | 8.1 | 6.06 | 18.22 | 29.32 | 0.00 | 99.2 | 90.0 |
| XI | XI | M.Salah | MID | 12 | 14.2 | 4.99 | 15.24 | 25.36 | 2.00 | 74.8 | 90.0 |
| XI | XI | Ndiaye | MID | 9 | 6.5 | 4.59 | 13.20 | 21.01 | 3.00 | 78.2 | 90.0 |
| Bench 2 | Bench | Kudus | MID | 18 | 6.7 | 4.33 | 12.95 | 21.33 | 0.00 | 80.0 | 0.0 |
| Bench 3 | Autosub In | Stach | MID | 11 | 5.0 | 1.85 | 5.94 | 10.63 | 4.00 | 41.7 | 90.0 |

## GW12

- Train rows: 169340
- Bank: 1.00 -> 1.30
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: João Pedro
- Effective captain: João Pedro
- Chip used: none
- Predicted score: 60.39
- Actual score: 38.00
- Transfer: Guéhi -> Van de Ven (projected gain 1.87, hit 0)
- Autosub outfielders: Stach, Kudus.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.31 | 11.92 | 18.46 | 2.00 | 81.5 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.8 | 3.26 | 8.81 | 13.33 | 6.00 | 76.5 | 90.0 |
| XI | Bench | Gabriel | DEF | 1 | 6.6 | 5.45 | 16.16 | 26.18 | 0.00 | 90.1 | 0.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.8 | 4.38 | 13.21 | 21.41 | 0.00 | 95.4 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 5.0 | 4.77 | 13.08 | 21.57 | 3.00 | 90.0 | 90.0 |
| XI | XI | Muñoz | DEF | 8 | 5.7 | 4.54 | 12.48 | 20.47 | 14.00 | 79.3 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.1 | 4.35 | 12.47 | 19.92 | 5.00 | 80.4 | 90.0 |
| Vice Captain | Captain | João Pedro | FWD | 7 | 7.4 | 5.60 | 15.64 | 24.41 | 1.00 | 88.7 | 75.0 |
| XI | XI | Mateta | FWD | 8 | 8.0 | 4.37 | 13.84 | 21.93 | 1.00 | 69.4 | 59.0 |
| Bench 4 | Bench | Wood | FWD | 16 | 7.2 | 0.65 | 2.81 | 5.63 | 0.00 | 12.9 | 0.0 |
| Captain | Bench | Semenyo | MID | 4 | 8.1 | 6.63 | 18.34 | 28.77 | 0.00 | 96.6 | 0.0 |
| XI | XI | M.Salah | MID | 12 | 14.2 | 5.48 | 15.35 | 24.62 | 2.00 | 77.3 | 90.0 |
| XI | XI | Ndiaye | MID | 9 | 6.5 | 3.88 | 11.89 | 20.13 | 3.00 | 75.8 | 80.0 |
| Bench 2 | Autosub In | Stach | MID | 11 | 4.9 | 2.70 | 7.99 | 13.53 | 4.00 | 63.8 | 22.0 |
| Bench 3 | Autosub In | Kudus | MID | 18 | 6.6 | 1.84 | 7.73 | 15.01 | 2.00 | 39.4 | 77.0 |

## GW13

- Train rows: 170095
- Bank: 1.30 -> 2.10
- Free transfers: 2 -> 2
- Captain: M.Salah
- Vice captain: João Pedro
- Effective captain: João Pedro
- Chip used: none
- Predicted score: 54.50
- Actual score: 40.00
- Transfer: Wood -> Thiago (projected gain 4.48, hit 0)
- Autosub outfielders: Kudus.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 3.75 | 11.08 | 17.59 | 3.00 | 80.5 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.8 | 3.14 | 8.89 | 13.67 | 3.00 | 77.5 | 90.0 |
| XI | XI | Muñoz | DEF | 8 | 5.8 | 4.97 | 13.81 | 22.20 | 1.00 | 87.4 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 5.0 | 4.43 | 13.40 | 22.00 | 2.00 | 93.2 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.2 | 4.27 | 12.93 | 20.79 | 2.00 | 78.9 | 90.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.8 | 4.27 | 12.40 | 19.84 | 0.00 | 85.9 | 90.0 |
| Bench 3 | Bench | Gabriel | DEF | 1 | 6.5 | 2.34 | 9.58 | 19.00 | 0.00 | 37.3 | 0.0 |
| Vice Captain | Captain | João Pedro | FWD | 7 | 7.5 | 5.22 | 14.59 | 23.27 | 1.00 | 85.9 | 54.0 |
| XI | XI | Thiago | FWD | 5 | 6.4 | 5.04 | 13.96 | 21.86 | 13.00 | 80.2 | 90.0 |
| XI | XI | Mateta | FWD | 8 | 8.1 | 4.14 | 13.14 | 21.28 | 6.00 | 65.4 | 90.0 |
| Captain | Bench | M.Salah | MID | 12 | 14.2 | 5.23 | 14.96 | 23.81 | 0.00 | 74.0 | 0.0 |
| XI | XI | Semenyo | MID | 4 | 8.0 | 4.12 | 12.76 | 22.01 | 1.00 | 53.8 | 90.0 |
| XI | XI | Ndiaye | MID | 9 | 6.6 | 3.83 | 10.51 | 18.03 | 2.00 | 69.0 | 79.0 |
| Bench 2 | Autosub In | Kudus | MID | 18 | 6.5 | 3.16 | 9.64 | 17.02 | 8.00 | 59.8 | 90.0 |
| Bench 4 | Bench | Stach | MID | 11 | 4.9 | 2.28 | 7.29 | 12.00 | 0.00 | 50.6 | 0.0 |

## GW14

- Train rows: 170850
- Bank: 2.10 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mbeumo
- Vice captain: Thiago
- Effective captain: Mbeumo
- Chip used: none
- Predicted score: 54.87
- Actual score: 35.00
- Transfer: Kudus -> Mbeumo (projected gain 5.75, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 3.91 | 11.03 | 17.36 | 6.00 | 81.8 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.8 | 3.29 | 9.17 | 14.32 | 1.00 | 80.7 | 90.0 |
| XI | Bench | Senesi | DEF | 4 | 5.0 | 4.55 | 13.06 | 21.02 | 0.00 | 93.4 | 0.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 4.54 | 12.99 | 20.67 | 1.00 | 80.4 | 46.0 |
| XI | XI | Muñoz | DEF | 8 | 5.9 | 4.47 | 12.92 | 20.71 | 14.00 | 82.2 | 90.0 |
| XI | Bench | Van de Ven | DEF | 18 | 4.8 | 4.01 | 12.23 | 19.53 | 0.00 | 83.8 | 0.0 |
| Bench 3 | Bench | Gabriel | DEF | 1 | 6.4 | 2.13 | 7.72 | 15.40 | 0.00 | 27.3 | 0.0 |
| Vice Captain | XI | Thiago | FWD | 5 | 6.6 | 5.05 | 15.65 | 25.20 | 1.00 | 88.4 | 30.0 |
| XI | XI | Mateta | FWD | 8 | 8.1 | 4.78 | 13.23 | 21.01 | 2.00 | 81.1 | 63.0 |
| XI | XI | João Pedro | FWD | 7 | 7.5 | 4.11 | 12.66 | 21.16 | 2.00 | 67.0 | 90.0 |
| Captain | Captain | Mbeumo | MID | 14 | 8.6 | 5.47 | 15.47 | 24.93 | 2.00 | 85.1 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 7.9 | 4.78 | 14.02 | 23.66 | 4.00 | 73.8 | 90.0 |
| XI | XI | M.Salah | MID | 12 | 14.2 | 3.72 | 11.11 | 18.57 | 1.00 | 36.8 | 45.0 |
| Bench 2 | Bench | Ndiaye | MID | 9 | 6.6 | 3.55 | 10.14 | 16.72 | 3.00 | 72.7 | 90.0 |
| Bench 4 | Bench | Stach | MID | 11 | 4.8 | 1.65 | 4.94 | 8.22 | 6.00 | 30.4 | 90.0 |

## GW15

- Train rows: 171608
- Bank: 0.00 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mbeumo
- Vice captain: Semenyo
- Effective captain: Mbeumo
- Chip used: none
- Predicted score: 54.50
- Actual score: 63.00
- Transfer: Gabriel -> Guéhi (projected gain 5.91, hit 0)
- Autosub outfielders: Stach, Van de Ven.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.00 | 11.73 | 18.63 | 2.00 | 85.7 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.8 | 3.13 | 9.00 | 14.10 | 10.00 | 80.9 | 90.0 |
| XI | Bench | Muñoz | DEF | 8 | 6.0 | 5.17 | 15.01 | 23.82 | 0.00 | 93.5 | 0.0 |
| XI | XI | Guéhi | DEF | 8 | 5.1 | 4.74 | 13.92 | 22.03 | 8.00 | 96.1 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 3.97 | 12.19 | 19.99 | 3.00 | 69.8 | 90.0 |
| Bench 4 | Bench | Senesi | DEF | 4 | 5.0 | 2.55 | 8.26 | 15.61 | 8.00 | 46.5 | 61.0 |
| Bench 3 | Autosub In | Van de Ven | DEF | 18 | 4.8 | 2.72 | 8.12 | 13.97 | 6.00 | 50.7 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.4 | 4.42 | 13.89 | 22.48 | 1.00 | 77.7 | 32.0 |
| XI | XI | Mateta | FWD | 8 | 8.1 | 4.32 | 12.74 | 20.67 | 2.00 | 69.5 | 65.0 |
| XI | XI | Thiago | FWD | 5 | 6.7 | 4.10 | 12.17 | 19.79 | 2.00 | 67.1 | 90.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.8 | 5.32 | 15.51 | 25.22 | 3.00 | 82.0 | 90.0 |
| Captain | Captain | Mbeumo | MID | 14 | 8.6 | 5.44 | 15.12 | 24.34 | 8.00 | 83.1 | 90.0 |
| XI | Bench | M.Salah | MID | 12 | 14.1 | 3.73 | 11.36 | 18.93 | 0.00 | 46.5 | 0.0 |
| XI | XI | Ndiaye | MID | 9 | 6.6 | 3.86 | 10.76 | 17.35 | 8.00 | 76.9 | 90.0 |
| Bench 2 | Autosub In | Stach | MID | 11 | 4.8 | 2.97 | 8.02 | 12.53 | 12.00 | 55.7 | 90.0 |

## GW16

- Train rows: 172367
- Bank: 1.20 -> 6.30
- Free transfers: 2 -> 2
- Captain: B.Fernandes
- Vice captain: Mbeumo
- Effective captain: B.Fernandes
- Chip used: none
- Predicted score: 56.99
- Actual score: 48.00
- Transfer: M.Salah -> B.Fernandes (projected gain 8.27, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.34 | 11.61 | 18.01 | 2.00 | 87.9 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.8 | 3.31 | 9.48 | 15.03 | 6.00 | 86.3 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.1 | 4.86 | 14.31 | 22.65 | 1.00 | 94.8 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 4.75 | 13.35 | 20.91 | 2.00 | 85.0 | 90.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.7 | 3.86 | 11.10 | 18.37 | 1.00 | 77.3 | 90.0 |
| Bench 3 | Bench | Muñoz | DEF | 8 | 6.1 | 3.36 | 10.73 | 17.91 | 0.00 | 49.6 | 0.0 |
| Bench 2 | Bench | Senesi | DEF | 4 | 5.0 | 3.40 | 10.44 | 17.68 | 1.00 | 68.3 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 6.8 | 4.55 | 13.78 | 22.21 | 2.00 | 74.8 | 90.0 |
| XI | XI | Mateta | FWD | 8 | 8.1 | 4.21 | 12.71 | 20.96 | 2.00 | 67.6 | 62.0 |
| XI | XI | João Pedro | FWD | 7 | 7.4 | 3.86 | 11.86 | 20.11 | 2.00 | 61.1 | 80.0 |
| Captain | Captain | B.Fernandes | MID | 14 | 9.0 | 6.25 | 17.72 | 28.42 | 13.00 | 99.0 | 90.0 |
| Vice Captain | XI | Mbeumo | MID | 14 | 8.5 | 5.30 | 15.02 | 24.64 | 2.00 | 85.2 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 7.7 | 4.82 | 14.49 | 23.70 | 6.00 | 83.4 | 90.0 |
| XI | XI | Ndiaye | MID | 9 | 6.5 | 3.93 | 11.78 | 19.07 | 2.00 | 80.4 | 90.0 |
| Bench 4 | Bench | Stach | MID | 11 | 4.8 | 3.24 | 9.48 | 15.08 | 2.00 | 67.6 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 6.30 -> 2.40
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: B.Fernandes
- Effective captain: Foden
- Chip used: none
- Predicted score: 56.36
- Actual score: 45.00
- Transfer: Stach -> Foden (projected gain 8.65, hit 0)
- Autosub outfielders: Mateta.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.89 | 11.30 | 17.83 | 7.00 | 85.2 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.9 | 3.03 | 9.12 | 14.71 | 4.00 | 84.9 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 4.80 | 14.08 | 22.27 | 1.00 | 89.1 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.5 | 3.95 | 12.09 | 19.96 | 6.00 | 74.8 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 5.0 | 3.72 | 10.54 | 17.96 | 4.00 | 72.7 | 90.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.7 | 3.71 | 10.48 | 17.34 | 0.00 | 74.6 | 90.0 |
| Bench 4 | Bench | Muñoz | DEF | 8 | 6.0 | 1.65 | 6.68 | 13.95 | 0.00 | 20.2 | 0.0 |
| XI | XI | Thiago | FWD | 5 | 7.1 | 4.60 | 14.57 | 23.21 | 2.00 | 66.8 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.3 | 3.72 | 11.78 | 20.11 | 6.00 | 67.8 | 90.0 |
| Bench 3 | Autosub In | Mateta | FWD | 8 | 7.9 | 2.55 | 9.27 | 17.20 | 2.00 | 40.7 | 76.0 |
| Vice Captain | XI | B.Fernandes | MID | 14 | 9.2 | 6.19 | 18.69 | 30.33 | 1.00 | 94.2 | 45.0 |
| Captain | Captain | Foden | MID | 13 | 8.7 | 6.22 | 18.57 | 28.95 | 3.00 | 83.0 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 7.6 | 5.21 | 14.53 | 23.74 | 10.00 | 84.6 | 90.0 |
| XI | Bench | Mbeumo | MID | 14 | 8.3 | 4.12 | 13.09 | 22.97 | 0.00 | 72.8 | 0.0 |
| Bench 2 | Bench | Ndiaye | MID | 9 | 6.4 | 3.60 | 10.77 | 17.98 | 0.00 | 74.6 | 0.0 |

## GW18

- Train rows: 173897
- Bank: 2.40 -> 0.30
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: B.Fernandes
- Effective captain: Foden
- Chip used: none
- Predicted score: 57.78
- Actual score: 41.00
- Transfer: Mbeumo -> Saka (projected gain 5.15, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.07 | 11.43 | 17.97 | 2.00 | 90.1 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.9 | 3.38 | 9.57 | 15.40 | 3.00 | 87.0 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.3 | 4.87 | 13.66 | 21.69 | 2.00 | 90.5 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.9 | 4.14 | 12.83 | 20.64 | 2.00 | 89.9 | 90.0 |
| XI | Bench | J.Timber | DEF | 1 | 6.5 | 4.56 | 12.77 | 20.20 | 0.00 | 85.5 | 0.0 |
| Bench 2 | Bench | Van de Ven | DEF | 18 | 4.6 | 3.26 | 9.57 | 15.42 | 11.00 | 80.3 | 90.0 |
| Bench 4 | Bench | Muñoz | DEF | 8 | 5.9 | 1.51 | 5.38 | 10.90 | 0.00 | 15.1 | 0.0 |
| XI | XI | Thiago | FWD | 5 | 7.2 | 4.39 | 12.92 | 20.76 | 5.00 | 79.3 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.2 | 4.20 | 12.08 | 19.71 | 8.00 | 77.0 | 68.0 |
| XI | XI | Mateta | FWD | 8 | 7.8 | 3.40 | 10.28 | 17.03 | 2.00 | 59.5 | 90.0 |
| Captain | Captain | Foden | MID | 13 | 8.9 | 6.00 | 18.03 | 28.76 | 2.00 | 86.1 | 90.0 |
| Vice Captain | Bench | B.Fernandes | MID | 14 | 9.3 | 5.68 | 17.07 | 28.11 | 0.00 | 80.0 | 0.0 |
| XI | XI | Semenyo | MID | 4 | 7.6 | 5.23 | 15.41 | 24.86 | 9.00 | 88.3 | 90.0 |
| XI | XI | Saka | MID | 1 | 10.3 | 5.26 | 14.60 | 23.43 | 7.00 | 77.3 | 90.0 |
| Bench 3 | Bench | Ndiaye | MID | 9 | 6.3 | 2.28 | 7.14 | 12.86 | 0.00 | 36.9 | 0.0 |

## GW19

- Train rows: 174672
- Bank: 0.30 -> 0.80
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: Semenyo
- Effective captain: Foden
- Chip used: none
- Predicted score: 55.34
- Actual score: 44.00
- Transfer: Ndiaye -> Wilson (projected gain 5.61, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.81 | 10.83 | 17.14 | 2.00 | 86.1 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.9 | 3.33 | 9.25 | 14.54 | 2.00 | 87.8 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.3 | 4.73 | 13.11 | 20.79 | 2.00 | 90.0 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.9 | 4.05 | 12.55 | 19.86 | 3.00 | 94.4 | 90.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.6 | 3.41 | 10.33 | 16.40 | 6.00 | 86.0 | 90.0 |
| Bench 2 | Bench | J.Timber | DEF | 1 | 6.5 | 3.04 | 8.95 | 15.07 | 9.00 | 45.3 | 82.0 |
| Bench 4 | Bench | Muñoz | DEF | 8 | 5.9 | 1.66 | 5.05 | 9.38 | 0.00 | 16.5 | 0.0 |
| XI | XI | Thiago | FWD | 5 | 7.1 | 4.22 | 12.42 | 21.01 | 2.00 | 75.3 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.2 | 4.19 | 11.47 | 18.43 | 1.00 | 74.1 | 27.0 |
| XI | XI | Mateta | FWD | 8 | 7.7 | 3.51 | 9.95 | 16.28 | 9.00 | 65.5 | 90.0 |
| Captain | Captain | Foden | MID | 13 | 9.0 | 5.91 | 17.79 | 28.64 | 3.00 | 89.4 | 90.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.7 | 5.46 | 15.85 | 25.14 | 5.00 | 96.2 | 90.0 |
| XI | XI | Saka | MID | 1 | 10.3 | 5.20 | 15.06 | 24.49 | 6.00 | 77.9 | 82.0 |
| XI | XI | Wilson | MID | 10 | 5.8 | 4.95 | 14.27 | 22.72 | 2.00 | 88.1 | 84.0 |
| Bench 3 | Bench | B.Fernandes | MID | 14 | 9.2 | 2.81 | 10.35 | 20.36 | 0.00 | 26.3 | 0.0 |

## GW20

- Train rows: 175452
- Bank: 0.80 -> 3.20
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: Semenyo
- Effective captain: Foden
- Chip used: none
- Predicted score: 56.23
- Actual score: 50.00
- Transfer: B.Fernandes -> Cherki (projected gain 4.59, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.70 | 10.61 | 16.86 | 1.00 | 88.2 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.9 | 2.65 | 8.47 | 13.88 | 0.00 | 89.0 | 0.0 |
| XI | XI | Guéhi | DEF | 8 | 5.3 | 4.63 | 13.74 | 21.91 | 2.00 | 96.3 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.9 | 3.89 | 11.75 | 19.42 | 1.00 | 85.8 | 90.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.5 | 4.12 | 11.36 | 17.55 | 7.00 | 85.8 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 3.73 | 10.97 | 18.48 | 3.00 | 63.9 | 90.0 |
| Bench 4 | Bench | Muñoz | DEF | 8 | 5.8 | 1.07 | 4.14 | 7.84 | 0.00 | 16.0 | 0.0 |
| XI | XI | Thiago | FWD | 5 | 7.0 | 4.05 | 11.63 | 19.17 | 17.00 | 76.4 | 90.0 |
| Bench 2 | Bench | Mateta | FWD | 8 | 7.7 | 3.49 | 10.38 | 16.75 | 2.00 | 75.9 | 86.0 |
| Bench 3 | Bench | João Pedro | FWD | 7 | 7.2 | 3.13 | 9.66 | 16.06 | 2.00 | 60.3 | 61.0 |
| Captain | Captain | Foden | MID | 13 | 9.0 | 6.01 | 17.38 | 28.20 | 2.00 | 84.8 | 90.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.7 | 5.51 | 16.02 | 25.33 | 1.00 | 93.4 | 90.0 |
| XI | XI | Cherki | MID | 13 | 6.7 | 5.08 | 14.87 | 23.50 | 4.00 | 80.0 | 90.0 |
| XI | XI | Saka | MID | 1 | 10.3 | 4.88 | 14.15 | 22.84 | 4.00 | 73.3 | 23.0 |
| XI | XI | Wilson | MID | 10 | 5.8 | 4.63 | 13.24 | 21.29 | 6.00 | 80.9 | 84.0 |

## GW21

- Train rows: 176242
- Bank: 3.20 -> 3.40
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: Semenyo
- Effective captain: Foden
- Chip used: none
- Predicted score: 57.85
- Actual score: 57.00
- Transfer: Muñoz -> Tarkowski (projected gain 3.38, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.65 | 10.43 | 16.79 | 6.00 | 85.6 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.9 | 1.79 | 5.95 | 10.38 | 2.00 | 51.2 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.6 | 4.79 | 13.40 | 20.82 | 4.00 | 91.1 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.3 | 4.69 | 13.30 | 21.52 | 6.00 | 93.8 | 90.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.5 | 3.98 | 11.76 | 18.21 | 0.00 | 90.5 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 3.97 | 11.68 | 18.88 | 6.00 | 71.1 | 90.0 |
| Bench 2 | Bench | Senesi | DEF | 4 | 4.8 | 3.57 | 10.14 | 17.57 | 6.00 | 76.2 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 6.9 | 5.24 | 13.97 | 22.15 | 12.00 | 92.8 | 81.0 |
| Bench 4 | Bench | João Pedro | FWD | 7 | 7.2 | 3.46 | 10.22 | 16.51 | 1.00 | 61.7 | 15.0 |
| Bench 3 | Bench | Mateta | FWD | 8 | 7.6 | 3.48 | 9.96 | 16.22 | 2.00 | 69.9 | 90.0 |
| Captain | Captain | Foden | MID | 13 | 8.9 | 5.84 | 16.56 | 27.11 | 2.00 | 82.6 | 72.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.7 | 5.46 | 15.39 | 24.69 | 6.00 | 92.6 | 90.0 |
| XI | XI | Cherki | MID | 13 | 6.8 | 5.15 | 14.96 | 23.22 | 1.00 | 85.3 | 17.0 |
| XI | XI | Wilson | MID | 10 | 5.8 | 4.91 | 13.90 | 22.30 | 9.00 | 84.3 | 90.0 |
| XI | XI | Saka | MID | 1 | 10.3 | 4.32 | 12.67 | 20.84 | 3.00 | 54.6 | 77.0 |

## GW22

- Train rows: 177037
- Bank: 3.40 -> 1.90
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: Thiago
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 55.53
- Actual score: 35.00
- Transfer: João Pedro -> Watkins (projected gain 1.54, hit 0)
- Autosub outfielders: Senesi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.83 | 10.99 | 17.40 | 6.00 | 86.2 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.9 | 2.60 | 7.74 | 12.88 | 11.00 | 73.7 | 90.0 |
| XI | Bench | Guéhi | DEF | 8 | 5.3 | 4.66 | 13.56 | 21.91 | 0.00 | 96.3 | 0.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.7 | 4.38 | 13.19 | 21.33 | 8.00 | 90.2 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 4.44 | 12.92 | 20.25 | 5.00 | 81.4 | 90.0 |
| Bench 2 | Autosub In | Senesi | DEF | 4 | 4.8 | 4.02 | 11.71 | 19.20 | 3.00 | 84.6 | 90.0 |
| Bench 3 | Bench | Van de Ven | DEF | 18 | 4.5 | 4.02 | 10.88 | 17.22 | 0.00 | 82.5 | 90.0 |
| Vice Captain | XI | Thiago | FWD | 5 | 7.0 | 4.96 | 14.05 | 22.08 | 2.00 | 89.0 | 90.0 |
| XI | XI | Watkins | FWD | 2 | 8.7 | 4.64 | 13.18 | 20.35 | 2.00 | 75.1 | 90.0 |
| Bench 4 | Bench | Mateta | FWD | 8 | 7.6 | 3.19 | 9.33 | 15.11 | 2.00 | 71.6 | 90.0 |
| Captain | Captain | Semenyo | MID | 4 | 7.6 | 5.22 | 15.63 | 25.25 | 2.00 | 91.5 | 90.0 |
| XI | XI | Foden | MID | 13 | 8.8 | 4.91 | 14.72 | 24.34 | 1.00 | 75.5 | 45.0 |
| XI | XI | Wilson | MID | 10 | 5.8 | 4.77 | 13.43 | 21.81 | 2.00 | 87.2 | 87.0 |
| XI | XI | Cherki | MID | 13 | 6.8 | 4.24 | 12.99 | 21.07 | 1.00 | 60.9 | 45.0 |
| XI | XI | Saka | MID | 1 | 10.2 | 4.27 | 12.72 | 21.10 | 1.00 | 58.7 | 33.0 |

## GW23

- Train rows: 177836
- Bank: 1.90 -> 1.70
- Free transfers: 2 -> 2
- Captain: Thiago
- Vice captain: Semenyo
- Effective captain: Thiago
- Chip used: none
- Predicted score: 55.60
- Actual score: 41.00
- Transfer: Guéhi -> Chalobah (projected gain 1.00, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.10 | 11.58 | 18.16 | 1.00 | 84.9 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.9 | 2.90 | 8.50 | 13.70 | 3.00 | 76.3 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 4.61 | 13.22 | 20.59 | 1.00 | 83.2 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.7 | 4.70 | 13.14 | 21.44 | 4.00 | 86.1 | 90.0 |
| XI | XI | Chalobah | DEF | 7 | 5.5 | 4.28 | 12.50 | 19.52 | 4.00 | 91.5 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.8 | 4.31 | 12.13 | 19.16 | 3.00 | 87.6 | 90.0 |
| Bench 3 | Bench | Van de Ven | DEF | 18 | 4.6 | 3.73 | 10.51 | 17.32 | 7.00 | 85.1 | 90.0 |
| Captain | Captain | Thiago | FWD | 5 | 7.1 | 5.56 | 14.88 | 23.34 | 2.00 | 92.7 | 90.0 |
| Bench 2 | Bench | Watkins | FWD | 2 | 8.8 | 3.79 | 11.53 | 18.28 | 8.00 | 69.9 | 90.0 |
| Bench 4 | Bench | Mateta | FWD | 8 | 7.6 | 3.53 | 9.92 | 15.71 | 2.00 | 72.5 | 84.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.6 | 5.46 | 15.60 | 25.18 | 8.00 | 85.3 | 90.0 |
| XI | XI | Wilson | MID | 10 | 5.9 | 4.68 | 13.11 | 21.50 | 10.00 | 79.6 | 90.0 |
| XI | XI | Cherki | MID | 13 | 6.8 | 4.46 | 12.45 | 20.94 | 3.00 | 60.7 | 72.0 |
| XI | XI | Saka | MID | 1 | 10.2 | 3.96 | 11.91 | 20.00 | 2.00 | 48.9 | 90.0 |
| XI | XI | Foden | MID | 13 | 8.7 | 3.92 | 11.77 | 20.45 | 1.00 | 55.6 | 29.0 |

## GW24

- Train rows: 178639
- Bank: 1.70 -> 2.60
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: Rogers
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 56.77
- Actual score: 44.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Foden -> Rogers (projected gain 4.59, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 3.94 | 11.14 | 17.41 | 6.00 | 82.6 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.9 | 3.15 | 8.59 | 13.62 | 2.00 | 81.8 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.8 | 4.50 | 12.64 | 19.85 | 8.00 | 92.1 | 90.0 |
| XI | XI | Chalobah | DEF | 7 | 5.6 | 4.44 | 12.44 | 19.64 | 3.00 | 88.6 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.8 | 4.20 | 12.32 | 20.30 | 2.00 | 84.4 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 4.13 | 11.94 | 18.98 | 5.00 | 76.2 | 90.0 |
| Bench 3 | Bench | Van de Ven | DEF | 18 | 4.6 | 3.88 | 11.28 | 18.40 | 0.00 | 91.5 | 0.0 |
| XI | XI | Thiago | FWD | 5 | 7.2 | 4.73 | 14.33 | 22.68 | 2.00 | 91.0 | 90.0 |
| XI | Bench | Watkins | FWD | 2 | 8.8 | 4.30 | 12.25 | 19.90 | 0.00 | 72.7 | 0.0 |
| Bench 4 | Bench | Mateta | FWD | 8 | 7.5 | 3.35 | 9.57 | 15.25 | 0.00 | 71.2 | 0.0 |
| Captain | Captain | Semenyo | MID | 4 | 7.7 | 5.86 | 16.62 | 26.55 | 7.00 | 93.1 | 90.0 |
| Vice Captain | XI | Rogers | MID | 2 | 7.7 | 5.70 | 15.98 | 25.34 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Saka | MID | 1 | 10.1 | 4.50 | 13.44 | 21.65 | 0.00 | 68.7 | 0.0 |
| XI | XI | Wilson | MID | 10 | 6.0 | 4.60 | 13.31 | 21.36 | 2.00 | 88.7 | 90.0 |
| Bench 2 | Bench | Cherki | MID | 13 | 6.7 | 3.99 | 11.45 | 19.45 | 8.00 | 58.3 | 68.0 |

## GW25

- Train rows: 179450
- Bank: 2.60 -> 5.20
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: Rogers
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 55.67
- Actual score: 48.00
- Transfer: Saka -> Rice (projected gain 6.49, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.40 | 11.96 | 18.56 | 7.00 | 83.7 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.9 | 2.97 | 8.39 | 13.56 | 2.00 | 81.5 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.8 | 4.38 | 12.36 | 20.02 | 2.00 | 88.6 | 90.0 |
| XI | XI | Chalobah | DEF | 7 | 5.7 | 4.30 | 12.33 | 19.86 | 4.00 | 86.8 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.8 | 4.11 | 12.09 | 19.89 | 2.00 | 84.3 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 4.40 | 11.96 | 19.06 | 6.00 | 74.5 | 90.0 |
| Bench 3 | Bench | Van de Ven | DEF | 18 | 4.6 | 2.33 | 7.86 | 13.83 | 1.00 | 53.5 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.2 | 3.98 | 13.47 | 22.27 | 5.00 | 82.3 | 90.0 |
| Bench 2 | Bench | Watkins | FWD | 2 | 8.8 | 2.37 | 7.71 | 13.98 | 2.00 | 31.6 | 85.0 |
| Bench 4 | Bench | Mateta | FWD | 8 | 7.5 | 2.10 | 6.34 | 11.20 | 0.00 | 36.4 | 0.0 |
| Captain | Captain | Semenyo | MID | 4 | 7.8 | 5.69 | 16.49 | 26.55 | 2.00 | 93.2 | 90.0 |
| Vice Captain | XI | Rogers | MID | 2 | 7.7 | 5.42 | 15.61 | 24.72 | 10.00 | 86.2 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.4 | 5.39 | 15.36 | 24.58 | 5.00 | 85.1 | 90.0 |
| XI | XI | Wilson | MID | 10 | 6.1 | 4.22 | 12.19 | 19.33 | 2.00 | 82.4 | 90.0 |
| XI | XI | Cherki | MID | 13 | 6.6 | 3.70 | 11.22 | 18.75 | 1.00 | 62.0 | 29.0 |

## GW26

- Train rows: 180267
- Bank: 5.20 -> 2.10
- Free transfers: 2 -> 2
- Captain: Rice
- Vice captain: Semenyo
- Effective captain: Rice
- Chip used: bench_boost
- Predicted score: 72.24
- Actual score: 68.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (15.83) beats the best remaining Bench Boost opportunity (12.60).
- Transfer: Cherki -> B.Fernandes (projected gain 5.20, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (15.83) beats the best remaining Bench Boost opportunity (12.60).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 5.17 | 12.88 | 19.56 | 3.00 | 112.4 | 180.0 |
| Bench 1 | Bench Boost | Sánchez | GK | 7 | 4.9 | 2.93 | 7.98 | 12.36 | 1.00 | 81.2 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 5.44 | 13.50 | 20.47 | 3.00 | 107.3 | 180.0 |
| XI | XI | Chalobah | DEF | 7 | 5.7 | 4.37 | 12.49 | 20.14 | 3.00 | 87.4 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.8 | 4.09 | 11.65 | 19.22 | 2.00 | 82.7 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.8 | 3.87 | 11.10 | 18.39 | 1.00 | 80.1 | 90.0 |
| Bench 2 | Bench Boost | Van de Ven | DEF | 18 | 4.5 | 3.60 | 10.41 | 17.06 | 3.00 | 76.7 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.1 | 4.42 | 13.87 | 22.99 | 2.00 | 84.3 | 90.0 |
| Bench 3 | Bench Boost | Watkins | FWD | 2 | 8.7 | 3.30 | 9.72 | 16.32 | 2.00 | 57.6 | 73.0 |
| Bench 4 | Bench Boost | Mateta | FWD | 8 | 7.5 | 1.90 | 5.09 | 9.34 | 0.00 | 23.2 | 0.0 |
| Captain | Captain | Rice | MID | 1 | 7.5 | 6.26 | 16.30 | 25.59 | 14.00 | 114.2 | 180.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.8 | 5.88 | 16.23 | 25.83 | 14.00 | 90.7 | 90.0 |
| XI | XI | B.Fernandes | MID | 14 | 9.7 | 5.63 | 15.59 | 24.84 | 2.00 | 77.2 | 90.0 |
| XI | XI | Rogers | MID | 2 | 7.6 | 5.25 | 15.35 | 24.44 | 2.00 | 92.0 | 90.0 |
| XI | XI | Wilson | MID | 10 | 6.1 | 3.89 | 12.06 | 19.37 | 2.00 | 84.7 | 71.0 |

## GW27

- Train rows: 181084
- Bank: 2.10 -> 2.00
- Free transfers: 2 -> 2
- Captain: Rice
- Vice captain: Semenyo
- Effective captain: Rice
- Chip used: none
- Predicted score: 64.69
- Actual score: 39.00
- Transfer: Mateta -> João Pedro (projected gain 5.18, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 5.19 | 14.35 | 22.00 | 3.00 | 117.2 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.9 | 2.94 | 7.75 | 11.94 | 2.00 | 78.0 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 5.82 | 16.20 | 24.87 | 3.00 | 119.5 | 56.0 |
| XI | XI | Chalobah | DEF | 7 | 5.8 | 4.53 | 12.44 | 20.06 | 2.00 | 86.8 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.8 | 3.97 | 11.00 | 18.16 | 5.00 | 82.9 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.8 | 3.58 | 10.13 | 16.96 | 1.00 | 76.4 | 90.0 |
| Bench 3 | Bench | Van de Ven | DEF | 18 | 4.5 | 3.25 | 9.78 | 16.11 | 0.00 | 78.4 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.6 | 5.74 | 15.49 | 24.03 | 7.00 | 83.6 | 79.0 |
| XI | XI | Thiago | FWD | 5 | 7.0 | 4.91 | 13.95 | 22.79 | 2.00 | 82.8 | 90.0 |
| Bench 4 | Bench | Watkins | FWD | 2 | 8.7 | 2.97 | 8.60 | 14.19 | 2.00 | 50.1 | 90.0 |
| Captain | Captain | Rice | MID | 1 | 7.5 | 7.25 | 20.88 | 32.72 | 4.00 | 131.6 | 90.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.9 | 6.07 | 16.84 | 26.68 | 4.00 | 96.0 | 86.0 |
| XI | XI | B.Fernandes | MID | 14 | 9.8 | 5.30 | 15.08 | 24.47 | 2.00 | 76.9 | 90.0 |
| XI | XI | Rogers | MID | 2 | 7.6 | 5.08 | 14.20 | 22.90 | 2.00 | 80.2 | 90.0 |
| Bench 2 | Bench | Wilson | MID | 10 | 6.0 | 3.38 | 10.40 | 17.39 | 8.00 | 69.6 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 2.00 -> 1.80
- Free transfers: 2 -> 2
- Captain: Rice
- Vice captain: Semenyo
- Effective captain: Rice
- Chip used: none
- Predicted score: 62.03
- Actual score: 75.00
- Transfer: Tarkowski -> Virgil (projected gain 3.69, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.28 | 11.87 | 18.73 | 3.00 | 95.8 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.9 | 2.26 | 7.34 | 11.90 | 2.00 | 77.9 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 5.9 | 5.32 | 14.69 | 23.59 | 7.00 | 89.0 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 4.49 | 12.83 | 20.56 | 8.00 | 87.1 | 90.0 |
| Bench 3 | Bench | Chalobah | DEF | 7 | 5.8 | 3.58 | 11.44 | 19.11 | 1.00 | 85.4 | 90.0 |
| Bench 2 | Bench | Van de Ven | DEF | 18 | 4.5 | 3.73 | 11.04 | 17.37 | 0.00 | 89.7 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.8 | 4.06 | 11.02 | 17.82 | 4.00 | 84.9 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.7 | 5.40 | 16.09 | 25.22 | 2.00 | 82.6 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.0 | 5.27 | 14.62 | 23.40 | 6.00 | 81.2 | 90.0 |
| Bench 4 | Bench | Watkins | FWD | 2 | 8.6 | 3.44 | 9.82 | 15.62 | 2.00 | 63.0 | 85.0 |
| Captain | Captain | Rice | MID | 1 | 7.6 | 6.22 | 18.32 | 29.37 | 5.00 | 108.6 | 75.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 8.0 | 5.99 | 17.41 | 27.59 | 8.00 | 90.4 | 90.0 |
| XI | XI | B.Fernandes | MID | 14 | 9.8 | 5.30 | 14.94 | 23.96 | 13.00 | 78.3 | 90.0 |
| XI | XI | Rogers | MID | 2 | 7.7 | 4.97 | 13.91 | 22.28 | 2.00 | 82.9 | 90.0 |
| XI | XI | Wilson | MID | 10 | 5.9 | 4.52 | 13.02 | 20.44 | 12.00 | 86.6 | 71.0 |

## GW29

- Train rows: 182721
- Bank: 1.80 -> 1.10
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: B.Fernandes
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 64.37
- Actual score: 80.00
- Transfer: Van de Ven -> Guéhi (projected gain 2.34, hit 0)
- Autosub outfielders: Senesi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.12 | 11.86 | 18.60 | 7.00 | 94.9 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.9 | 2.53 | 7.74 | 12.42 | 0.00 | 79.3 | 0.0 |
| XI | XI | Virgil | DEF | 12 | 6.0 | 5.52 | 15.66 | 24.71 | 1.00 | 89.7 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 4.74 | 13.50 | 21.40 | 13.00 | 92.4 | 90.0 |
| XI | XI | Guéhi | DEF | 13 | 5.2 | 4.88 | 13.50 | 21.15 | 1.00 | 90.8 | 90.0 |
| Bench 2 | Autosub In | Senesi | DEF | 4 | 4.9 | 3.92 | 11.23 | 17.81 | 11.00 | 89.3 | 90.0 |
| Bench 3 | Bench | Chalobah | DEF | 7 | 5.7 | 3.28 | 10.49 | 17.50 | 2.00 | 79.7 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.7 | 5.47 | 15.70 | 24.83 | 19.00 | 81.9 | 84.0 |
| XI | XI | Thiago | FWD | 5 | 7.1 | 5.07 | 14.40 | 22.63 | 2.00 | 84.2 | 90.0 |
| Bench 4 | Bench | Watkins | FWD | 2 | 8.6 | 3.27 | 9.15 | 14.61 | 1.00 | 62.3 | 70.0 |
| Captain | Captain | Semenyo | MID | 4 | 8.1 | 6.93 | 19.11 | 29.54 | 7.00 | 101.0 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.6 | 5.55 | 16.78 | 26.40 | 3.00 | 100.1 | 90.0 |
| Vice Captain | XI | B.Fernandes | MID | 14 | 9.9 | 5.75 | 16.74 | 26.58 | 8.00 | 90.5 | 90.0 |
| XI | Bench | Wilson | MID | 10 | 5.9 | 4.87 | 13.40 | 21.11 | 0.00 | 81.0 | 0.0 |
| XI | XI | Rogers | MID | 2 | 7.7 | 4.56 | 12.92 | 20.60 | 1.00 | 81.6 | 90.0 |

## GW30

- Train rows: 183541
- Bank: 1.10 -> 0.60
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: João Pedro
- Effective captain: Semenyo
- Chip used: triple_captain
- Predicted score: 72.05
- Actual score: 50.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.05) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Watkins -> Ekitiké (projected gain 2.87, hit 0)
- Chip used: Triple Captain on Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (7.05) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.14 | 11.62 | 18.12 | 7.00 | 91.0 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.9 | 1.74 | 5.28 | 8.91 | 3.00 | 43.8 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 6.1 | 5.13 | 14.63 | 22.87 | 2.00 | 86.2 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 5.06 | 14.37 | 22.48 | 1.00 | 91.2 | 37.0 |
| XI | XI | Guéhi | DEF | 13 | 5.2 | 4.46 | 12.29 | 19.07 | 2.00 | 86.8 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.9 | 4.26 | 11.96 | 18.45 | 10.00 | 92.0 | 90.0 |
| Bench 3 | Bench | Chalobah | DEF | 7 | 5.6 | 3.52 | 10.26 | 16.52 | 2.00 | 79.6 | 90.0 |
| Vice Captain | XI | João Pedro | FWD | 7 | 7.6 | 6.88 | 18.86 | 29.52 | 2.00 | 96.1 | 90.0 |
| XI | XI | Ekitiké | FWD | 12 | 9.1 | 5.12 | 14.77 | 23.07 | 1.00 | 75.3 | 26.0 |
| XI | XI | Thiago | FWD | 5 | 7.2 | 5.00 | 13.79 | 21.33 | 6.00 | 86.3 | 90.0 |
| Captain | Captain | Semenyo | MID | 4 | 8.2 | 7.05 | 19.55 | 29.96 | 2.00 | 103.0 | 74.0 |
| XI | XI | B.Fernandes | MID | 14 | 10.0 | 6.33 | 18.44 | 28.97 | 10.00 | 97.1 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.5 | 4.54 | 13.53 | 22.43 | 3.00 | 80.0 | 90.0 |
| Bench 2 | Bench | Rogers | MID | 2 | 7.6 | 3.91 | 11.98 | 19.41 | 2.00 | 79.9 | 90.0 |
| Bench 4 | Bench | Wilson | MID | 10 | 6.0 | 3.16 | 9.43 | 15.58 | 3.00 | 48.1 | 90.0 |