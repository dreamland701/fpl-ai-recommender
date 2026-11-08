# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW11
- Total predicted points: 642.64
- Total actual points: 538.00
- Average predicted points: 64.26
- Average actual points: 53.80
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
- Chip used: triple_captain
- Predicted score: 66.70
- Actual score: 78.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.31) beats the best remaining Triple Captain opportunity (6.88).
- Transfer: Reijnders -> Ndiaye (projected gain 3.48, hit 0)
- Chip used: Triple Captain on Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.31) beats the best remaining Triple Captain opportunity (6.88).

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
- Chip used: bench_boost
- Predicted score: 70.96
- Actual score: 35.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.93) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Ekitiké -> Mateta (projected gain 1.60, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.93) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.8 | 4.17 | 12.04 | 18.65 | 1.00 | 84.9 | 90.0 |
| Bench 1 | Bench Boost | Sánchez | GK | 7 | 4.8 | 3.38 | 8.84 | 13.49 | 6.00 | 79.5 | 90.0 |
| XI | XI | Gabriel | DEF | 1 | 6.5 | 5.24 | 16.47 | 27.04 | 1.00 | 90.4 | 90.0 |
| Vice Captain | XI | Guéhi | DEF | 8 | 5.0 | 5.66 | 15.89 | 25.55 | 0.00 | 95.3 | 0.0 |
| XI | XI | Senesi | DEF | 4 | 5.0 | 4.50 | 13.48 | 22.56 | 2.00 | 96.3 | 90.0 |
| XI | XI | Muñoz | DEF | 8 | 5.7 | 4.51 | 13.33 | 21.73 | 6.00 | 83.4 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.1 | 4.38 | 13.21 | 21.07 | 1.00 | 81.2 | 90.0 |
| XI | XI | Mateta | FWD | 8 | 7.8 | 4.92 | 14.37 | 22.77 | 2.00 | 78.6 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.4 | 4.95 | 14.22 | 24.27 | 7.00 | 80.1 | 82.0 |
| Bench 4 | Bench Boost | Wood | FWD | 16 | 7.2 | 1.36 | 4.30 | 7.78 | 0.00 | 16.6 | 0.0 |
| Captain | Captain | Semenyo | MID | 4 | 8.1 | 6.06 | 18.22 | 29.32 | 0.00 | 99.2 | 90.0 |
| XI | XI | M.Salah | MID | 12 | 14.2 | 4.99 | 15.24 | 25.36 | 2.00 | 74.8 | 90.0 |
| XI | XI | Ndiaye | MID | 9 | 6.5 | 4.59 | 13.20 | 21.01 | 3.00 | 78.2 | 90.0 |
| Bench 2 | Bench Boost | Kudus | MID | 18 | 6.7 | 4.33 | 12.95 | 21.33 | 0.00 | 80.0 | 0.0 |
| Bench 3 | Bench Boost | Stach | MID | 11 | 5.0 | 1.85 | 5.94 | 10.63 | 4.00 | 41.7 | 90.0 |