# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW30
- Total predicted points: 1487.17
- Total actual points: 1553.00
- Average predicted points: 51.28
- Average actual points: 53.55
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
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Haaland
- Vice captain: M.Salah
- Effective captain: Haaland
- Chip used: none
- Predicted score: 69.46
- Actual score: 46.00
- Chip advisory: bench_boost (0.67): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Sánchez | GK | 7 | 5.0 | 4.89 | 13.99 | 23.59 | 3.00 | 106.7 | 90.0 |
| Bench 1 | Bench | M.Bizot | GK | 2 | 4.5 | 3.89 | 11.15 | 20.76 | 0.00 | 101.6 | 0.0 |
| XI | XI | Ballard | DEF | 17 | 4.5 | 5.90 | 16.58 | 26.14 | 1.00 | 114.1 | 8.0 |
| XI | XI | Calafiori | DEF | 1 | 5.5 | 5.41 | 16.19 | 24.98 | 13.00 | 88.2 | 63.0 |
| XI | XI | Saliba | DEF | 1 | 6.0 | 4.65 | 14.76 | 22.15 | 6.00 | 105.9 | 90.0 |
| XI | XI | Lewis | DEF | 13 | 5.0 | 4.91 | 14.42 | 25.59 | 1.00 | 88.5 | 90.0 |
| Bench 4 | Bench | Van de Ven | DEF | 18 | 4.5 | 4.18 | 13.95 | 23.99 | 6.00 | 103.8 | 90.0 |
| Captain | Captain | Haaland | FWD | 13 | 14.0 | 6.91 | 19.99 | 33.21 | 2.00 | 88.1 | 90.0 |
| Bench 2 | Bench | Richarlison | FWD | 18 | 6.5 | 4.44 | 14.93 | 23.90 | 4.00 | 96.6 | 77.0 |
| Bench 3 | Bench | Thiago | FWD | 5 | 6.0 | 4.29 | 12.31 | 18.89 | 2.00 | 96.6 | 90.0 |
| XI | XI | Reijnders | MID | 13 | 5.5 | 6.23 | 18.91 | 31.76 | 2.00 | 112.9 | 90.0 |
| Vice Captain | XI | M.Salah | MID | 12 | 14.5 | 6.43 | 18.31 | 29.46 | 5.00 | 113.8 | 90.0 |
| XI | XI | Kudus | MID | 18 | 6.5 | 6.18 | 18.02 | 29.47 | 3.00 | 100.5 | 85.0 |
| XI | XI | Stach | MID | 11 | 5.0 | 5.23 | 16.74 | 26.30 | 2.00 | 101.7 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 7.0 | 5.83 | 16.05 | 25.39 | 6.00 | 100.3 | 90.0 |

## GW3

- Train rows: 162672
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: M.Salah
- Vice captain: Semenyo
- Effective captain: M.Salah
- Chip used: none
- Predicted score: 48.52
- Actual score: 32.00
- Transfer: M.Bizot -> Dúbravka (projected gain 0.39, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Dúbravka | GK | 3 | 4.0 | 4.00 | 12.07 | 18.27 | 2.00 | 97.1 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 5.0 | 3.73 | 11.76 | 18.91 | 6.00 | 92.1 | 90.0 |
| XI | XI | Calafiori | DEF | 1 | 5.5 | 4.20 | 14.23 | 21.72 | 2.00 | 67.2 | 90.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.5 | 3.68 | 12.22 | 18.44 | 1.00 | 87.6 | 90.0 |
| XI | XI | Saliba | DEF | 1 | 6.0 | 3.21 | 11.38 | 17.97 | 1.00 | 80.9 | 4.0 |
| Bench 3 | Bench | Lewis | DEF | 13 | 5.0 | 2.71 | 9.60 | 15.79 | 1.00 | 71.1 | 5.0 |
| Bench 4 | Bench | Ballard | DEF | 17 | 4.6 | 2.42 | 7.97 | 12.81 | 0.00 | 24.9 | 0.0 |
| XI | XI | Haaland | FWD | 13 | 14.0 | 4.34 | 15.20 | 26.17 | 9.00 | 70.4 | 90.0 |
| XI | XI | Richarlison | FWD | 18 | 6.6 | 3.18 | 10.78 | 16.31 | 2.00 | 67.9 | 90.0 |
| Bench 2 | Bench | Thiago | FWD | 5 | 6.0 | 3.02 | 9.55 | 15.03 | 6.00 | 81.1 | 90.0 |
| Captain | Captain | M.Salah | MID | 12 | 14.5 | 4.96 | 16.77 | 28.72 | 3.00 | 88.8 | 90.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.1 | 4.67 | 16.25 | 25.46 | 2.00 | 82.1 | 90.0 |
| XI | XI | Reijnders | MID | 13 | 5.6 | 3.91 | 13.71 | 22.99 | 2.00 | 83.1 | 90.0 |
| XI | XI | Kudus | MID | 18 | 6.5 | 4.04 | 13.69 | 23.83 | 2.00 | 83.2 | 90.0 |
| XI | XI | Stach | MID | 11 | 5.0 | 3.37 | 10.82 | 17.05 | 3.00 | 80.4 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 0.50 -> 0.50
- Free transfers: 2 -> 2
- Captain: M.Salah
- Vice captain: Haaland
- Effective captain: M.Salah
- Chip used: none
- Predicted score: 48.86
- Actual score: 74.00
- Transfer: Saliba -> Cucurella (projected gain 5.24, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Sánchez | GK | 7 | 5.0 | 3.75 | 11.33 | 17.12 | 2.00 | 90.4 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.43 | 10.65 | 16.93 | 3.00 | 94.5 | 90.0 |
| XI | XI | Cucurella | DEF | 7 | 6.1 | 3.81 | 12.12 | 18.88 | 1.00 | 82.9 | 45.0 |
| XI | XI | Calafiori | DEF | 1 | 5.6 | 3.87 | 11.15 | 17.45 | 5.00 | 76.2 | 67.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.6 | 3.36 | 10.58 | 16.20 | 14.00 | 85.5 | 79.0 |
| Bench 3 | Bench | Lewis | DEF | 13 | 5.0 | 2.45 | 6.90 | 10.41 | 0.00 | 59.9 | 0.0 |
| Bench 4 | Bench | Ballard | DEF | 17 | 4.6 | 1.74 | 5.92 | 9.67 | 0.00 | 18.3 | 0.0 |
| Vice Captain | XI | Haaland | FWD | 13 | 14.1 | 4.97 | 14.80 | 26.82 | 13.00 | 81.3 | 86.0 |
| XI | XI | Richarlison | FWD | 18 | 6.7 | 3.25 | 10.62 | 16.50 | 1.00 | 76.2 | 19.0 |
| Bench 2 | Bench | Thiago | FWD | 5 | 6.0 | 3.22 | 9.49 | 15.04 | 1.00 | 84.1 | 71.0 |
| Captain | Captain | M.Salah | MID | 12 | 14.5 | 5.39 | 16.73 | 26.86 | 9.00 | 85.6 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 7.3 | 4.05 | 13.18 | 20.99 | 13.00 | 77.5 | 90.0 |
| XI | XI | Kudus | MID | 18 | 6.6 | 3.96 | 12.96 | 22.12 | 3.00 | 82.6 | 90.0 |
| XI | XI | Reijnders | MID | 13 | 5.7 | 3.75 | 12.85 | 19.39 | 3.00 | 87.2 | 90.0 |
| XI | XI | Stach | MID | 11 | 5.0 | 3.30 | 9.69 | 14.39 | 1.00 | 80.8 | 90.0 |

## GW5

- Train rows: 164124
- Bank: 0.50 -> 0.90
- Free transfers: 2 -> 2
- Captain: M.Salah
- Vice captain: Haaland
- Effective captain: M.Salah
- Chip used: none
- Predicted score: 50.15
- Actual score: 69.00
- Transfer: Lewis -> Guéhi (projected gain 4.19, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Dúbravka | GK | 3 | 4.0 | 3.93 | 10.88 | 16.95 | 4.00 | 94.5 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 5.0 | 3.13 | 10.10 | 16.58 | -3.00 | 87.2 | 4.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.6 | 3.66 | 12.16 | 19.04 | 1.00 | 86.9 | 90.0 |
| XI | XI | Calafiori | DEF | 1 | 5.7 | 3.81 | 11.87 | 18.66 | 2.00 | 70.2 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 4.6 | 3.54 | 11.60 | 18.15 | 7.00 | 81.3 | 90.0 |
| XI | XI | Cucurella | DEF | 7 | 6.1 | 3.15 | 9.97 | 15.96 | 0.00 | 73.9 | 63.0 |
| Bench 4 | Bench | Ballard | DEF | 17 | 4.6 | 1.69 | 5.22 | 8.53 | 1.00 | 19.6 | 53.0 |
| Vice Captain | XI | Haaland | FWD | 13 | 14.1 | 4.57 | 15.94 | 26.69 | 9.00 | 81.7 | 75.0 |
| Bench 3 | Bench | Richarlison | FWD | 18 | 6.7 | 2.48 | 8.05 | 12.98 | 9.00 | 61.3 | 90.0 |
| Bench 2 | Bench | Thiago | FWD | 5 | 6.0 | 2.69 | 7.50 | 11.84 | 2.00 | 73.7 | 64.0 |
| Captain | Captain | M.Salah | MID | 12 | 14.5 | 6.35 | 17.79 | 28.34 | 5.00 | 87.5 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 7.4 | 4.53 | 15.49 | 24.05 | 5.00 | 80.0 | 90.0 |
| XI | XI | Kudus | MID | 18 | 6.6 | 3.81 | 11.71 | 21.56 | 7.00 | 83.2 | 90.0 |
| XI | XI | Reijnders | MID | 13 | 5.7 | 3.27 | 11.36 | 18.41 | 9.00 | 84.1 | 90.0 |
| XI | XI | Stach | MID | 11 | 5.0 | 3.18 | 9.11 | 14.52 | 15.00 | 79.7 | 90.0 |

## GW6

- Train rows: 164865
- Bank: 0.90 -> 0.00
- Free transfers: 2 -> 2
- Captain: M.Salah
- Vice captain: Haaland
- Effective captain: M.Salah
- Chip used: none
- Predicted score: 51.05
- Actual score: 46.00
- Transfer: Richarlison -> Mateta (projected gain 1.61, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Dúbravka | GK | 3 | 4.0 | 3.08 | 9.25 | 14.95 | 1.00 | 96.3 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 5.0 | 2.26 | 7.03 | 11.31 | 1.00 | 64.9 | 90.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.7 | 3.58 | 11.88 | 17.63 | 2.00 | 85.2 | 90.0 |
| XI | XI | Calafiori | DEF | 1 | 5.7 | 3.28 | 11.34 | 16.80 | 1.00 | 79.0 | 69.0 |
| XI | XI | Guéhi | DEF | 8 | 4.7 | 3.39 | 11.09 | 17.13 | 7.00 | 68.3 | 90.0 |
| Bench 2 | Bench | Cucurella | DEF | 7 | 6.2 | 2.99 | 9.26 | 14.75 | 0.00 | 75.7 | 90.0 |
| Bench 4 | Bench | Ballard | DEF | 17 | 4.6 | 1.80 | 4.32 | 7.83 | 1.00 | 23.1 | 15.0 |
| Vice Captain | XI | Haaland | FWD | 13 | 14.2 | 5.01 | 15.23 | 23.82 | 16.00 | 81.6 | 90.0 |
| XI | XI | Mateta | FWD | 8 | 7.6 | 3.81 | 10.77 | 16.00 | 2.00 | 84.3 | 90.0 |
| Bench 3 | Bench | Thiago | FWD | 5 | 6.0 | 2.59 | 7.12 | 11.22 | 13.00 | 70.7 | 89.0 |
| Captain | Captain | M.Salah | MID | 12 | 14.5 | 5.92 | 16.80 | 27.86 | 2.00 | 85.7 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 7.6 | 4.79 | 16.63 | 24.03 | 7.00 | 85.8 | 90.0 |
| XI | XI | Kudus | MID | 18 | 6.6 | 4.95 | 13.44 | 21.63 | 2.00 | 85.8 | 90.0 |
| XI | XI | Reijnders | MID | 13 | 5.7 | 3.93 | 11.70 | 17.10 | 2.00 | 89.8 | 82.0 |
| XI | XI | Stach | MID | 11 | 5.0 | 3.39 | 10.32 | 15.82 | 2.00 | 85.3 | 90.0 |

## GW7

- Train rows: 165607
- Bank: 0.00 -> 1.40
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Semenyo
- Effective captain: Haaland
- Chip used: none
- Predicted score: 47.58
- Actual score: 64.00
- Transfer: Cucurella -> Senesi (projected gain 3.51, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Dúbravka | GK | 3 | 4.0 | 3.02 | 9.32 | 14.30 | 2.00 | 93.6 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.9 | 2.08 | 6.40 | 11.45 | 2.00 | 65.3 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.8 | 3.84 | 12.15 | 18.95 | 2.00 | 82.2 | 77.0 |
| XI | XI | Guéhi | DEF | 8 | 4.7 | 3.82 | 11.63 | 20.75 | 3.00 | 89.0 | 90.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.7 | 3.36 | 10.77 | 17.13 | 2.00 | 86.5 | 90.0 |
| Bench 2 | Bench | Calafiori | DEF | 1 | 5.7 | 2.96 | 8.65 | 14.07 | 6.00 | 51.6 | 74.0 |
| Bench 4 | Bench | Ballard | DEF | 17 | 4.6 | 1.47 | 4.36 | 7.23 | 3.00 | 23.1 | 53.0 |
| Captain | Captain | Haaland | FWD | 13 | 14.3 | 5.32 | 16.68 | 26.93 | 8.00 | 85.1 | 90.0 |
| XI | XI | Mateta | FWD | 8 | 7.6 | 3.19 | 10.02 | 15.45 | 2.00 | 79.3 | 69.0 |
| Bench 3 | Bench | Thiago | FWD | 5 | 6.0 | 2.74 | 7.97 | 12.48 | 2.00 | 81.5 | 67.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.7 | 5.04 | 15.55 | 24.90 | 18.00 | 90.1 | 90.0 |
| XI | XI | M.Salah | MID | 12 | 14.5 | 4.38 | 15.08 | 23.83 | 2.00 | 81.7 | 90.0 |
| XI | XI | Reijnders | MID | 13 | 5.7 | 3.39 | 11.87 | 19.32 | 3.00 | 81.9 | 75.0 |
| XI | XI | Kudus | MID | 18 | 6.7 | 3.89 | 11.15 | 18.13 | 12.00 | 83.0 | 89.0 |
| XI | XI | Stach | MID | 11 | 5.0 | 2.99 | 9.02 | 14.05 | 2.00 | 81.4 | 66.0 |

## GW8

- Train rows: 166350
- Bank: 1.40 -> 0.90
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Semenyo
- Effective captain: Haaland
- Chip used: none
- Predicted score: 53.12
- Actual score: 79.00
- Transfer: Calafiori -> Gabriel (projected gain 3.78, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Dúbravka | GK | 3 | 4.0 | 3.24 | 9.40 | 14.24 | 9.00 | 94.7 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.9 | 2.48 | 6.93 | 11.09 | 5.00 | 76.7 | 90.0 |
| XI | XI | Gabriel | DEF | 1 | 6.2 | 4.04 | 13.06 | 20.41 | 12.00 | 87.9 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.9 | 3.81 | 12.77 | 21.34 | 2.00 | 83.6 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 4.8 | 3.65 | 11.01 | 17.72 | 4.00 | 90.2 | 90.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.8 | 3.74 | 10.92 | 16.62 | 0.00 | 88.7 | 90.0 |
| Bench 3 | Bench | Ballard | DEF | 17 | 4.6 | 2.72 | 7.07 | 10.61 | 10.00 | 68.6 | 90.0 |
| Captain | Captain | Haaland | FWD | 13 | 14.4 | 5.91 | 18.61 | 30.01 | 13.00 | 85.3 | 90.0 |
| XI | XI | Mateta | FWD | 8 | 7.5 | 2.98 | 8.95 | 15.25 | 17.00 | 62.0 | 90.0 |
| Bench 4 | Bench | Thiago | FWD | 5 | 6.0 | 2.64 | 7.27 | 11.45 | 8.00 | 74.2 | 90.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.8 | 5.68 | 17.04 | 27.18 | 4.00 | 103.1 | 90.0 |
| XI | XI | M.Salah | MID | 12 | 14.5 | 5.41 | 15.29 | 26.17 | 2.00 | 79.0 | 84.0 |
| XI | XI | Kudus | MID | 18 | 6.7 | 4.88 | 14.09 | 21.63 | 2.00 | 90.7 | 90.0 |
| XI | XI | Reijnders | MID | 13 | 5.8 | 3.86 | 10.89 | 18.00 | 1.00 | 82.3 | 58.0 |
| Bench 2 | Bench | Stach | MID | 11 | 5.0 | 2.84 | 7.95 | 12.46 | 2.00 | 78.4 | 72.0 |

## GW9

- Train rows: 167095
- Bank: 0.90 -> 1.50
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: Haaland
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 49.92
- Actual score: 64.00
- Transfer: Ballard -> Mukiele (projected gain 1.63, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Dúbravka | GK | 3 | 4.0 | 3.32 | 9.62 | 14.64 | 2.00 | 95.9 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.9 | 2.87 | 7.91 | 12.76 | 1.00 | 85.4 | 90.0 |
| XI | XI | Gabriel | DEF | 1 | 6.3 | 4.02 | 13.02 | 22.93 | 9.00 | 90.7 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 4.9 | 3.89 | 12.62 | 20.05 | 4.00 | 93.6 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 5.0 | 3.59 | 10.38 | 17.23 | 5.00 | 75.0 | 90.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.8 | 3.28 | 10.32 | 16.23 | 23.00 | 88.5 | 90.0 |
| XI | XI | Mukiele | DEF | 17 | 4.0 | 3.15 | 10.16 | 16.22 | 2.00 | 86.0 | 90.0 |
| Vice Captain | XI | Haaland | FWD | 13 | 14.6 | 5.43 | 16.77 | 27.55 | 2.00 | 93.0 | 90.0 |
| XI | XI | Mateta | FWD | 8 | 7.5 | 3.92 | 11.64 | 19.10 | 2.00 | 83.3 | 90.0 |
| Bench 2 | Bench | Thiago | FWD | 5 | 6.1 | 3.11 | 8.56 | 13.95 | 5.00 | 82.8 | 90.0 |
| Captain | Captain | Semenyo | MID | 4 | 8.0 | 5.67 | 16.40 | 26.68 | 3.00 | 95.0 | 90.0 |
| XI | XI | M.Salah | MID | 12 | 14.4 | 3.97 | 13.83 | 23.88 | 6.00 | 65.3 | 90.0 |
| XI | XI | Kudus | MID | 18 | 6.8 | 4.02 | 12.60 | 22.69 | 3.00 | 85.9 | 77.0 |
| Bench 3 | Bench | Reijnders | MID | 13 | 5.8 | 3.11 | 10.34 | 17.85 | 1.00 | 75.8 | 75.0 |
| Bench 4 | Bench | Stach | MID | 11 | 5.0 | 2.69 | 6.99 | 11.16 | 0.00 | 72.2 | 0.0 |

## GW10

- Train rows: 167841
- Bank: 1.50 -> 0.10
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Semenyo
- Effective captain: Haaland
- Chip used: none
- Predicted score: 48.71
- Actual score: 84.00
- Transfer: Thiago -> João Pedro (projected gain 3.69, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Dúbravka | GK | 3 | 4.0 | 3.00 | 8.68 | 13.77 | 2.00 | 95.4 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.9 | 2.57 | 7.02 | 11.62 | 6.00 | 83.5 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 4.9 | 3.77 | 11.44 | 18.85 | 10.00 | 92.0 | 90.0 |
| XI | XI | Gabriel | DEF | 1 | 6.4 | 3.53 | 10.94 | 18.48 | 12.00 | 87.2 | 90.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.7 | 3.79 | 10.73 | 17.33 | 2.00 | 99.0 | 90.0 |
| Bench 3 | Bench | Senesi | DEF | 4 | 5.0 | 2.80 | 9.94 | 17.22 | 3.00 | 72.4 | 90.0 |
| XI | XI | Mukiele | DEF | 17 | 4.1 | 3.02 | 9.24 | 14.96 | 1.00 | 82.1 | 90.0 |
| Captain | Captain | Haaland | FWD | 13 | 14.7 | 5.34 | 15.83 | 25.76 | 13.00 | 90.7 | 81.0 |
| XI | XI | João Pedro | FWD | 7 | 7.5 | 3.66 | 12.55 | 20.77 | 9.00 | 80.9 | 90.0 |
| XI | XI | Mateta | FWD | 8 | 7.6 | 3.93 | 11.42 | 17.82 | 9.00 | 79.2 | 89.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 8.1 | 4.81 | 15.02 | 24.91 | 2.00 | 100.2 | 90.0 |
| XI | XI | M.Salah | MID | 12 | 14.3 | 4.81 | 13.79 | 23.71 | 10.00 | 75.9 | 90.0 |
| XI | XI | Kudus | MID | 18 | 6.8 | 3.70 | 12.34 | 21.12 | 1.00 | 82.4 | 90.0 |
| Bench 2 | Bench | Reijnders | MID | 13 | 5.7 | 2.82 | 9.16 | 15.39 | 1.00 | 73.0 | 17.0 |
| Bench 4 | Bench | Stach | MID | 11 | 5.1 | 1.22 | 4.27 | 8.18 | 1.00 | 21.3 | 30.0 |

## GW11

- Train rows: 168588
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Semenyo
- Effective captain: Haaland
- Chip used: none
- Predicted score: 52.17
- Actual score: 31.00
- Transfer: Kudus -> Rice (projected gain 4.24, hit 0)
- Autosub outfielders: Mukiele.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Dúbravka | GK | 3 | 4.0 | 3.16 | 8.68 | 13.95 | 2.00 | 95.1 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.8 | 2.88 | 7.84 | 11.89 | 6.00 | 83.5 | 90.0 |
| XI | XI | Gabriel | DEF | 1 | 6.5 | 4.14 | 13.87 | 22.84 | 1.00 | 90.4 | 90.0 |
| XI | Bench | Guéhi | DEF | 8 | 5.0 | 4.36 | 13.49 | 21.15 | 0.00 | 93.3 | 0.0 |
| XI | XI | Senesi | DEF | 4 | 5.0 | 3.60 | 11.88 | 20.26 | 2.00 | 94.3 | 90.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.7 | 3.77 | 11.34 | 20.19 | 1.00 | 90.5 | 90.0 |
| Bench 2 | Autosub In | Mukiele | DEF | 17 | 4.1 | 2.92 | 8.94 | 15.00 | 4.00 | 82.8 | 90.0 |
| Captain | Captain | Haaland | FWD | 13 | 14.8 | 6.31 | 17.32 | 27.68 | 4.00 | 99.1 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.4 | 3.95 | 12.02 | 22.77 | 7.00 | 83.1 | 82.0 |
| XI | XI | Mateta | FWD | 8 | 7.8 | 3.92 | 11.77 | 17.97 | 2.00 | 82.6 | 90.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 8.1 | 4.66 | 14.22 | 23.32 | 0.00 | 96.2 | 90.0 |
| XI | XI | M.Salah | MID | 12 | 14.2 | 3.99 | 13.74 | 22.76 | 2.00 | 79.8 | 90.0 |
| XI | XI | Rice | MID | 1 | 6.7 | 4.02 | 13.19 | 21.14 | 2.00 | 88.5 | 90.0 |
| Bench 3 | Bench | Reijnders | MID | 13 | 5.6 | 2.12 | 6.97 | 12.97 | 0.00 | 32.7 | 0.0 |
| Bench 4 | Bench | Stach | MID | 11 | 5.0 | 1.55 | 4.94 | 9.03 | 4.00 | 31.7 | 90.0 |

## GW12

- Train rows: 169340
- Bank: 0.10 -> 0.30
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Semenyo
- Effective captain: Haaland
- Chip used: none
- Predicted score: 49.64
- Actual score: 37.00
- Transfer: Reijnders -> Anderson (projected gain 1.93, hit 0)
- Autosub outfielders: Mukiele, Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Dúbravka | GK | 3 | 4.0 | 3.01 | 8.27 | 13.46 | 2.00 | 94.2 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.8 | 2.46 | 6.41 | 9.73 | 6.00 | 81.5 | 90.0 |
| XI | Bench | Gabriel | DEF | 1 | 6.6 | 4.25 | 12.16 | 20.18 | 0.00 | 90.1 | 0.0 |
| XI | XI | Senesi | DEF | 4 | 5.0 | 3.77 | 10.98 | 19.97 | 3.00 | 90.0 | 90.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.8 | 3.18 | 10.71 | 17.11 | 0.00 | 93.4 | 90.0 |
| Bench 2 | Autosub In | Mukiele | DEF | 17 | 4.2 | 2.99 | 8.49 | 13.97 | 4.00 | 83.2 | 90.0 |
| Bench 3 | Autosub In | Guéhi | DEF | 8 | 5.1 | 2.92 | 8.44 | 14.41 | 5.00 | 36.1 | 90.0 |
| Captain | Captain | Haaland | FWD | 13 | 14.8 | 5.59 | 16.36 | 26.38 | 2.00 | 95.2 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.4 | 4.30 | 13.64 | 23.21 | 1.00 | 87.7 | 75.0 |
| XI | XI | Mateta | FWD | 8 | 8.0 | 3.87 | 12.84 | 19.53 | 1.00 | 76.4 | 59.0 |
| Vice Captain | Bench | Semenyo | MID | 4 | 8.1 | 4.63 | 14.34 | 22.77 | 0.00 | 76.6 | 0.0 |
| XI | XI | M.Salah | MID | 12 | 14.2 | 4.58 | 14.15 | 23.32 | 2.00 | 81.3 | 90.0 |
| XI | XI | Rice | MID | 1 | 6.8 | 3.57 | 11.04 | 17.65 | 6.00 | 65.1 | 90.0 |
| XI | XI | Anderson | MID | 16 | 5.3 | 3.30 | 10.34 | 16.28 | 9.00 | 87.5 | 90.0 |
| Bench 4 | Bench | Stach | MID | 11 | 4.9 | 2.10 | 6.59 | 10.93 | 4.00 | 62.8 | 22.0 |

## GW13

- Train rows: 170095
- Bank: 0.30 -> 0.70
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Rice
- Effective captain: Haaland
- Chip used: none
- Predicted score: 52.35
- Actual score: 28.00
- Transfer: Semenyo -> Eze (projected gain 1.01, hit 0)
- Autosub outfielders: Van de Ven.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Sánchez | GK | 7 | 4.8 | 2.74 | 7.89 | 12.37 | 3.00 | 81.5 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.51 | 7.33 | 11.38 | 1.00 | 92.1 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 5.0 | 3.93 | 12.20 | 20.60 | 2.00 | 92.2 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.1 | 3.94 | 11.78 | 18.97 | 0.00 | 83.0 | 90.0 |
| Bench 2 | Autosub In | Van de Ven | DEF | 18 | 4.8 | 3.47 | 11.20 | 17.44 | 0.00 | 86.9 | 90.0 |
| XI | XI | Mukiele | DEF | 17 | 4.2 | 3.56 | 10.13 | 16.09 | 0.00 | 86.4 | 90.0 |
| Bench 4 | Bench | Gabriel | DEF | 1 | 6.5 | 1.84 | 7.98 | 15.50 | 0.00 | 24.3 | 0.0 |
| Captain | Captain | Haaland | FWD | 13 | 14.9 | 5.95 | 16.67 | 26.56 | 2.00 | 95.9 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.5 | 4.82 | 12.99 | 20.37 | 1.00 | 87.9 | 54.0 |
| XI | XI | Mateta | FWD | 8 | 8.1 | 3.74 | 12.04 | 19.08 | 6.00 | 74.4 | 90.0 |
| Vice Captain | XI | Rice | MID | 1 | 6.9 | 4.85 | 14.90 | 23.47 | 4.00 | 92.2 | 90.0 |
| XI | Bench | M.Salah | MID | 12 | 14.2 | 4.83 | 13.96 | 21.81 | 0.00 | 80.0 | 0.0 |
| XI | XI | Eze | MID | 1 | 7.6 | 4.02 | 12.15 | 18.99 | 2.00 | 87.4 | 71.0 |
| XI | XI | Anderson | MID | 16 | 5.3 | 4.02 | 10.97 | 17.94 | 6.00 | 90.5 | 90.0 |
| Bench 3 | Bench | Stach | MID | 11 | 4.9 | 2.18 | 6.49 | 10.60 | 0.00 | 64.6 | 0.0 |

## GW14

- Train rows: 170850
- Bank: 0.70 -> 0.80
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Rice
- Effective captain: Haaland
- Chip used: none
- Predicted score: 46.47
- Actual score: 56.00
- Transfer: Gabriel -> J.Timber (projected gain 3.01, hit 0)
- Autosub outfielders: Mukiele.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Dúbravka | GK | 3 | 4.0 | 2.99 | 8.32 | 12.64 | 2.00 | 91.3 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.8 | 2.49 | 7.67 | 12.12 | 1.00 | 83.7 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 3.64 | 11.99 | 18.67 | 1.00 | 83.4 | 46.0 |
| XI | Bench | Van de Ven | DEF | 18 | 4.8 | 3.31 | 10.73 | 17.23 | 0.00 | 85.8 | 0.0 |
| XI | XI | Guéhi | DEF | 8 | 5.1 | 2.95 | 9.20 | 15.09 | 14.00 | 82.1 | 90.0 |
| Bench 2 | Bench | Senesi | DEF | 4 | 5.0 | 2.95 | 9.06 | 15.02 | 0.00 | 73.4 | 0.0 |
| Bench 3 | Autosub In | Mukiele | DEF | 17 | 4.2 | 2.93 | 8.66 | 13.97 | 0.00 | 86.8 | 90.0 |
| Captain | Captain | Haaland | FWD | 13 | 14.9 | 5.66 | 16.36 | 26.44 | 14.00 | 94.6 | 90.0 |
| XI | XI | Mateta | FWD | 8 | 8.1 | 3.78 | 11.73 | 18.91 | 2.00 | 84.1 | 63.0 |
| XI | XI | João Pedro | FWD | 7 | 7.5 | 3.41 | 11.36 | 18.96 | 2.00 | 66.0 | 90.0 |
| Vice Captain | XI | Rice | MID | 1 | 7.0 | 4.47 | 14.27 | 23.96 | 3.00 | 89.0 | 82.0 |
| XI | XI | Eze | MID | 1 | 7.7 | 3.49 | 11.39 | 18.04 | 1.00 | 78.1 | 29.0 |
| XI | XI | Anderson | MID | 16 | 5.3 | 4.00 | 11.34 | 18.39 | 2.00 | 89.0 | 90.0 |
| XI | XI | M.Salah | MID | 12 | 14.2 | 3.12 | 10.01 | 16.97 | 1.00 | 55.8 | 45.0 |
| Bench 4 | Bench | Stach | MID | 11 | 4.8 | 1.05 | 3.54 | 6.02 | 6.00 | 19.4 | 90.0 |

## GW15

- Train rows: 171608
- Bank: 0.80 -> 0.20
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Rice
- Effective captain: Haaland
- Chip used: none
- Predicted score: 46.41
- Actual score: 53.00
- Transfer: Van de Ven -> Tarkowski (projected gain 4.10, hit 0)
- Autosub outfielders: Stach.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Dúbravka | GK | 3 | 4.0 | 2.94 | 8.76 | 13.77 | 3.00 | 91.0 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.8 | 2.73 | 7.60 | 11.60 | 10.00 | 83.9 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.1 | 3.44 | 11.12 | 17.83 | 8.00 | 94.1 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.4 | 3.43 | 10.86 | 16.46 | 9.00 | 89.6 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 2.97 | 9.99 | 16.19 | 3.00 | 76.8 | 90.0 |
| Bench 4 | Bench | Mukiele | DEF | 17 | 4.2 | 2.34 | 8.42 | 13.95 | 1.00 | 85.3 | 90.0 |
| Bench 3 | Bench | Senesi | DEF | 4 | 5.0 | 2.35 | 6.76 | 12.61 | 8.00 | 61.5 | 61.0 |
| Captain | Captain | Haaland | FWD | 13 | 14.9 | 6.33 | 17.51 | 27.87 | 2.00 | 100.8 | 68.0 |
| XI | XI | João Pedro | FWD | 7 | 7.4 | 3.92 | 12.89 | 20.18 | 1.00 | 81.7 | 32.0 |
| XI | XI | Mateta | FWD | 8 | 8.1 | 3.52 | 11.74 | 18.67 | 2.00 | 76.5 | 65.0 |
| Vice Captain | XI | Rice | MID | 1 | 7.0 | 4.03 | 13.23 | 21.97 | 6.00 | 85.4 | 90.0 |
| XI | XI | Eze | MID | 1 | 7.8 | 3.15 | 10.77 | 17.24 | 1.00 | 71.6 | 45.0 |
| XI | XI | Anderson | MID | 16 | 5.4 | 3.22 | 10.62 | 17.91 | 4.00 | 83.6 | 90.0 |
| XI | Bench | M.Salah | MID | 12 | 14.1 | 3.13 | 10.16 | 17.53 | 0.00 | 61.5 | 0.0 |
| Bench 2 | Autosub In | Stach | MID | 11 | 4.8 | 2.67 | 6.92 | 10.93 | 12.00 | 67.7 | 90.0 |

## GW16

- Train rows: 172367
- Bank: 0.20 -> 5.90
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Foden
- Effective captain: Haaland
- Chip used: none
- Predicted score: 47.66
- Actual score: 52.00
- Transfer: M.Salah -> Foden (projected gain 5.16, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Dúbravka | GK | 3 | 4.0 | 3.20 | 8.45 | 13.24 | 1.00 | 90.8 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.8 | 2.51 | 7.88 | 12.93 | 6.00 | 87.3 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 3.45 | 12.85 | 18.51 | 2.00 | 87.0 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.1 | 3.86 | 12.11 | 21.05 | 1.00 | 92.8 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.4 | 3.19 | 10.79 | 16.95 | 1.00 | 87.2 | 90.0 |
| Bench 2 | Bench | Senesi | DEF | 4 | 5.0 | 2.90 | 9.24 | 14.98 | 1.00 | 76.3 | 90.0 |
| Bench 3 | Bench | Mukiele | DEF | 17 | 4.2 | 2.86 | 8.37 | 13.46 | 8.00 | 83.9 | 90.0 |
| Captain | Captain | Haaland | FWD | 13 | 15.0 | 5.75 | 17.40 | 27.02 | 13.00 | 87.0 | 90.0 |
| XI | XI | Mateta | FWD | 8 | 8.1 | 3.41 | 11.41 | 18.16 | 2.00 | 66.6 | 62.0 |
| XI | XI | João Pedro | FWD | 7 | 7.4 | 3.56 | 10.86 | 18.01 | 2.00 | 71.1 | 80.0 |
| Vice Captain | XI | Foden | MID | 13 | 8.4 | 4.71 | 14.36 | 22.86 | 11.00 | 78.6 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.1 | 3.93 | 11.16 | 18.50 | 2.00 | 87.7 | 90.0 |
| XI | XI | Anderson | MID | 16 | 5.4 | 3.73 | 11.11 | 17.48 | 3.00 | 85.0 | 90.0 |
| XI | XI | Eze | MID | 1 | 7.8 | 3.11 | 9.92 | 15.40 | 1.00 | 44.9 | 56.0 |
| Bench 4 | Bench | Stach | MID | 11 | 4.8 | 2.44 | 7.88 | 12.98 | 2.00 | 75.6 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 5.90 -> 1.50
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: B.Fernandes
- Effective captain: Haaland
- Chip used: none
- Predicted score: 47.81
- Actual score: 73.00
- Transfer: Stach -> B.Fernandes (projected gain 8.14, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Dúbravka | GK | 3 | 4.0 | 2.84 | 8.18 | 12.76 | 2.00 | 89.6 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.9 | 2.63 | 8.02 | 12.71 | 4.00 | 86.9 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 3.50 | 11.98 | 20.77 | 1.00 | 89.1 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.5 | 2.95 | 9.99 | 16.46 | 6.00 | 79.8 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.5 | 2.93 | 8.96 | 15.26 | 3.00 | 83.1 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 5.0 | 3.12 | 8.94 | 15.16 | 4.00 | 78.7 | 90.0 |
| Bench 2 | Bench | Mukiele | DEF | 17 | 4.2 | 2.87 | 8.75 | 14.53 | 6.00 | 85.1 | 90.0 |
| Captain | Captain | Haaland | FWD | 13 | 15.0 | 6.31 | 17.41 | 27.81 | 16.00 | 96.6 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.3 | 3.12 | 10.78 | 17.61 | 6.00 | 75.8 | 90.0 |
| Bench 4 | Bench | Mateta | FWD | 8 | 7.9 | 2.35 | 7.77 | 14.30 | 2.00 | 57.7 | 76.0 |
| Vice Captain | XI | B.Fernandes | MID | 14 | 9.2 | 5.09 | 16.69 | 28.83 | 1.00 | 92.2 | 45.0 |
| XI | XI | Foden | MID | 13 | 8.7 | 4.72 | 14.57 | 22.95 | 3.00 | 82.0 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.1 | 3.92 | 11.87 | 20.76 | 11.00 | 82.5 | 90.0 |
| XI | XI | Anderson | MID | 16 | 5.4 | 3.00 | 9.68 | 15.94 | 4.00 | 84.0 | 90.0 |
| Bench 3 | Bench | Eze | MID | 1 | 7.8 | 2.44 | 8.22 | 14.14 | 0.00 | 34.7 | 0.0 |

## GW18

- Train rows: 173897
- Bank: 1.50 -> 1.60
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Foden
- Effective captain: Haaland
- Chip used: none
- Predicted score: 50.11
- Actual score: 56.00
- Transfer: Eze -> Semenyo (projected gain 3.95, hit 0)
- Autosub outfielders: Senesi, Mateta.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Dúbravka | GK | 3 | 4.0 | 3.00 | 7.98 | 12.09 | 11.00 | 88.9 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.9 | 2.88 | 7.97 | 12.80 | 3.00 | 88.0 | 90.0 |
| XI | Bench | J.Timber | DEF | 1 | 6.5 | 3.66 | 11.77 | 18.00 | 0.00 | 87.5 | 0.0 |
| XI | XI | Guéhi | DEF | 8 | 5.3 | 3.87 | 11.66 | 17.89 | 2.00 | 90.5 | 90.0 |
| Bench 2 | Autosub In | Senesi | DEF | 4 | 4.9 | 3.04 | 9.33 | 14.74 | 2.00 | 88.9 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.5 | 3.04 | 9.33 | 14.98 | 8.00 | 85.3 | 90.0 |
| Bench 4 | Bench | Mukiele | DEF | 17 | 4.2 | 2.43 | 6.62 | 11.26 | 4.00 | 63.0 | 90.0 |
| Captain | Captain | Haaland | FWD | 13 | 15.0 | 6.30 | 17.84 | 28.63 | 2.00 | 103.9 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.2 | 3.40 | 10.68 | 17.01 | 8.00 | 76.0 | 68.0 |
| Bench 3 | Autosub In | Mateta | FWD | 8 | 7.8 | 2.90 | 8.78 | 14.93 | 2.00 | 70.5 | 90.0 |
| Vice Captain | XI | Foden | MID | 13 | 8.9 | 5.00 | 15.93 | 23.96 | 2.00 | 87.1 | 90.0 |
| XI | Bench | B.Fernandes | MID | 14 | 9.3 | 4.38 | 14.97 | 23.91 | 0.00 | 84.0 | 0.0 |
| XI | XI | Rice | MID | 1 | 7.1 | 3.92 | 13.69 | 21.98 | 5.00 | 90.0 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 7.6 | 4.13 | 13.21 | 23.16 | 9.00 | 89.3 | 90.0 |
| XI | XI | Anderson | MID | 16 | 5.4 | 3.12 | 9.77 | 16.31 | 3.00 | 85.8 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 1.60 -> 0.30
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Foden
- Effective captain: Haaland
- Chip used: none
- Predicted score: 47.85
- Actual score: 46.00
- Transfer: Mateta -> Ekitiké (projected gain 4.25, hit 0)
- Autosub outfielders: Senesi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Dúbravka | GK | 3 | 4.0 | 3.12 | 8.75 | 13.17 | 2.00 | 92.9 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.9 | 2.83 | 7.75 | 12.24 | 2.00 | 88.8 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.3 | 3.43 | 10.61 | 16.69 | 2.00 | 90.0 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.5 | 3.22 | 9.81 | 16.20 | 9.00 | 86.4 | 90.0 |
| Bench 2 | Autosub In | Senesi | DEF | 4 | 4.9 | 2.95 | 8.85 | 13.86 | 3.00 | 74.4 | 90.0 |
| XI | XI | Mukiele | DEF | 17 | 4.2 | 3.03 | 8.56 | 13.82 | 11.00 | 86.8 | 90.0 |
| Bench 4 | Bench | J.Timber | DEF | 1 | 6.5 | 2.34 | 7.55 | 12.97 | 9.00 | 29.3 | 82.0 |
| Captain | Captain | Haaland | FWD | 13 | 15.1 | 5.56 | 16.33 | 26.45 | 2.00 | 99.3 | 90.0 |
| XI | XI | Ekitiké | FWD | 12 | 9.0 | 4.07 | 12.80 | 19.36 | 2.00 | 76.6 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.2 | 3.39 | 10.27 | 15.83 | 1.00 | 73.1 | 27.0 |
| Vice Captain | XI | Foden | MID | 13 | 9.0 | 4.91 | 15.39 | 23.84 | 3.00 | 89.4 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 7.7 | 4.26 | 12.75 | 19.84 | 5.00 | 94.2 | 90.0 |
| XI | Bench | Rice | MID | 1 | 7.2 | 4.08 | 12.66 | 21.91 | 0.00 | 85.9 | 0.0 |
| XI | XI | Anderson | MID | 16 | 5.3 | 3.23 | 9.69 | 16.20 | 4.00 | 85.4 | 90.0 |
| Bench 3 | Bench | B.Fernandes | MID | 14 | 9.2 | 2.51 | 9.15 | 17.76 | 0.00 | 46.3 | 0.0 |

## GW20

- Train rows: 175452
- Bank: 0.30 -> 2.70
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Foden
- Effective captain: Haaland
- Chip used: none
- Predicted score: 48.71
- Actual score: 28.00
- Transfer: B.Fernandes -> Cherki (projected gain 2.86, hit 0)
- Autosub outfielders: Anderson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Dúbravka | GK | 3 | 4.0 | 3.00 | 8.86 | 13.16 | 1.00 | 91.2 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.9 | 2.45 | 7.27 | 11.48 | 0.00 | 89.0 | 0.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.5 | 4.03 | 11.92 | 18.25 | 2.00 | 90.8 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.9 | 3.19 | 10.75 | 16.82 | 1.00 | 86.8 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 3.13 | 9.97 | 16.88 | 3.00 | 72.9 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.3 | 3.33 | 9.74 | 15.91 | 2.00 | 94.3 | 90.0 |
| XI | XI | Mukiele | DEF | 17 | 4.2 | 3.24 | 9.66 | 14.99 | 4.00 | 89.6 | 90.0 |
| Captain | Captain | Haaland | FWD | 13 | 15.1 | 5.91 | 17.42 | 27.05 | 2.00 | 91.8 | 90.0 |
| XI | Bench | Ekitiké | FWD | 12 | 9.1 | 3.79 | 11.13 | 20.57 | 0.00 | 80.1 | 0.0 |
| Bench 3 | Bench | João Pedro | FWD | 7 | 7.2 | 2.73 | 8.36 | 13.96 | 2.00 | 70.3 | 61.0 |
| Vice Captain | XI | Foden | MID | 13 | 9.0 | 4.91 | 14.78 | 23.50 | 2.00 | 86.8 | 90.0 |
| XI | XI | Cherki | MID | 13 | 6.7 | 3.98 | 12.47 | 22.30 | 4.00 | 83.0 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 7.7 | 4.31 | 12.02 | 19.33 | 1.00 | 92.4 | 90.0 |
| Bench 2 | Autosub In | Anderson | MID | 16 | 5.3 | 3.04 | 9.69 | 15.82 | 4.00 | 87.5 | 90.0 |
| Bench 4 | Bench | Rice | MID | 1 | 7.2 | 2.64 | 8.88 | 14.76 | 17.00 | 61.2 | 90.0 |

## GW21

- Train rows: 176242
- Bank: 2.70 -> 4.90
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Foden
- Effective captain: Haaland
- Chip used: none
- Predicted score: 48.56
- Actual score: 59.00
- Transfer: Ekitiké -> Thiago (projected gain 1.52, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Dúbravka | GK | 3 | 4.0 | 3.03 | 8.40 | 13.08 | 3.00 | 90.8 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.9 | 1.49 | 4.95 | 8.88 | 2.00 | 65.2 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.3 | 3.39 | 11.10 | 17.82 | 6.00 | 92.8 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.6 | 3.79 | 10.80 | 16.02 | 4.00 | 90.1 | 90.0 |
| XI | XI | Mukiele | DEF | 17 | 4.3 | 3.04 | 9.92 | 15.27 | 3.00 | 88.0 | 90.0 |
| Bench 2 | Bench | J.Timber | DEF | 1 | 6.4 | 2.97 | 9.68 | 15.78 | 6.00 | 78.1 | 90.0 |
| Bench 4 | Bench | Senesi | DEF | 4 | 4.8 | 2.67 | 8.34 | 14.57 | 6.00 | 81.2 | 90.0 |
| Captain | Captain | Haaland | FWD | 13 | 15.1 | 5.39 | 15.59 | 25.13 | 6.00 | 90.3 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 6.9 | 4.14 | 11.17 | 17.55 | 12.00 | 91.8 | 81.0 |
| Bench 3 | Bench | João Pedro | FWD | 7 | 7.2 | 2.96 | 9.12 | 15.31 | 1.00 | 71.7 | 15.0 |
| Vice Captain | XI | Foden | MID | 13 | 8.9 | 4.84 | 14.26 | 22.51 | 2.00 | 85.6 | 72.0 |
| XI | XI | Semenyo | MID | 4 | 7.7 | 4.26 | 12.49 | 19.89 | 6.00 | 91.6 | 90.0 |
| XI | XI | Cherki | MID | 13 | 6.8 | 4.05 | 12.16 | 18.92 | 1.00 | 87.3 | 17.0 |
| XI | XI | Rice | MID | 1 | 7.1 | 3.86 | 11.55 | 20.67 | 3.00 | 79.6 | 90.0 |
| XI | XI | Anderson | MID | 16 | 5.3 | 3.37 | 9.99 | 15.99 | 7.00 | 88.0 | 90.0 |

## GW22

- Train rows: 177037
- Bank: 4.90 -> 3.10
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Bruno G.
- Effective captain: Haaland
- Chip used: none
- Predicted score: 48.59
- Actual score: 37.00
- Transfer: Anderson -> Bruno G. (projected gain 3.48, hit 0)
- Autosub outfielders: Senesi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Dúbravka | GK | 3 | 4.0 | 2.46 | 7.97 | 12.70 | 5.00 | 92.3 | 90.0 |
| Bench 1 | Bench | Sánchez | GK | 7 | 4.9 | 2.40 | 6.44 | 10.48 | 11.00 | 79.7 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 3.94 | 11.92 | 18.05 | 5.00 | 84.4 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.7 | 3.88 | 11.69 | 18.43 | 8.00 | 90.2 | 90.0 |
| XI | Bench | Guéhi | DEF | 8 | 5.3 | 3.36 | 11.26 | 20.51 | 0.00 | 94.3 | 0.0 |
| Bench 2 | Autosub In | Senesi | DEF | 4 | 4.8 | 3.32 | 10.41 | 17.00 | 3.00 | 86.6 | 90.0 |
| Bench 3 | Bench | Mukiele | DEF | 17 | 4.3 | 3.14 | 9.74 | 14.78 | 6.00 | 86.7 | 90.0 |
| Captain | Captain | Haaland | FWD | 13 | 15.1 | 5.81 | 17.09 | 27.29 | 2.00 | 94.5 | 79.0 |
| XI | XI | Thiago | FWD | 5 | 7.0 | 3.56 | 11.95 | 18.18 | 2.00 | 69.0 | 90.0 |
| Bench 4 | Bench | João Pedro | FWD | 7 | 7.2 | 2.43 | 8.02 | 13.40 | 8.00 | 58.9 | 73.0 |
| Vice Captain | XI | Bruno G. | MID | 15 | 7.1 | 4.87 | 13.88 | 22.72 | 3.00 | 92.3 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 7.6 | 4.12 | 13.33 | 20.95 | 2.00 | 90.5 | 90.0 |
| XI | XI | Foden | MID | 13 | 8.8 | 3.91 | 12.72 | 23.14 | 1.00 | 74.5 | 45.0 |
| XI | XI | Cherki | MID | 13 | 6.8 | 3.44 | 11.59 | 18.97 | 1.00 | 70.9 | 45.0 |
| XI | XI | Rice | MID | 1 | 7.2 | 3.44 | 11.40 | 18.82 | 3.00 | 76.7 | 90.0 |

## GW23

- Train rows: 177836
- Bank: 3.10 -> 2.10
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Rice
- Effective captain: Haaland
- Chip used: none
- Predicted score: 50.02
- Actual score: 30.00
- Transfer: Sánchez -> Raya (projected gain 1.49, hit 0)
- Autosub outfielders: Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 3.40 | 9.98 | 15.66 | 1.00 | 86.9 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.03 | 8.51 | 12.90 | 5.00 | 94.6 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.8 | 3.51 | 11.03 | 16.96 | 3.00 | 88.6 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 3.31 | 11.02 | 18.99 | 1.00 | 85.2 | 90.0 |
| XI | XI | Mukiele | DEF | 17 | 4.4 | 3.46 | 10.75 | 16.46 | 4.00 | 88.6 | 82.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.7 | 3.40 | 10.64 | 17.44 | 4.00 | 87.1 | 90.0 |
| Bench 3 | Bench | Guéhi | DEF | 8 | 5.3 | 2.49 | 7.25 | 11.93 | 6.00 | 34.8 | 90.0 |
| Captain | Captain | Haaland | FWD | 13 | 15.1 | 5.75 | 15.86 | 25.58 | 1.00 | 88.7 | 17.0 |
| XI | XI | Thiago | FWD | 5 | 7.1 | 3.96 | 10.88 | 17.34 | 2.00 | 72.7 | 90.0 |
| Bench 4 | Bench | João Pedro | FWD | 7 | 7.1 | 2.48 | 8.69 | 14.35 | 12.00 | 51.9 | 84.0 |
| Vice Captain | XI | Rice | MID | 1 | 7.3 | 4.87 | 13.97 | 22.24 | 1.00 | 89.9 | 90.0 |
| XI | Bench | Bruno G. | MID | 15 | 7.2 | 4.79 | 13.63 | 21.99 | 0.00 | 89.4 | 0.0 |
| XI | XI | Semenyo | MID | 4 | 7.6 | 4.26 | 13.60 | 24.08 | 8.00 | 87.3 | 90.0 |
| XI | XI | Cherki | MID | 13 | 6.8 | 3.56 | 11.25 | 18.84 | 3.00 | 59.7 | 72.0 |
| Bench 2 | Autosub In | Foden | MID | 13 | 8.7 | 3.22 | 10.77 | 18.15 | 1.00 | 45.6 | 29.0 |

## GW24

- Train rows: 178639
- Bank: 2.10 -> 1.70
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Semenyo
- Effective captain: Haaland
- Chip used: none
- Predicted score: 47.24
- Actual score: 58.00
- Transfer: Bruno G. -> Rogers (projected gain 4.92, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Dúbravka | GK | 3 | 4.0 | 2.94 | 9.02 | 14.68 | 1.00 | 96.6 | 90.0 |
| Bench 1 | Bench | Raya | GK | 1 | 5.9 | 2.94 | 8.64 | 14.11 | 6.00 | 85.6 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.8 | 3.60 | 11.34 | 17.45 | 8.00 | 91.1 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.8 | 3.80 | 11.12 | 18.10 | 2.00 | 86.4 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 3.43 | 10.94 | 17.58 | 5.00 | 81.2 | 90.0 |
| Bench 3 | Bench | Guéhi | DEF | 8 | 5.2 | 2.96 | 9.25 | 15.90 | 3.00 | 81.4 | 90.0 |
| Bench 2 | Bench | Mukiele | DEF | 17 | 4.5 | 3.15 | 8.31 | 13.25 | 9.00 | 64.0 | 90.0 |
| Captain | Captain | Haaland | FWD | 13 | 15.1 | 5.00 | 15.38 | 24.52 | 5.00 | 65.7 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.2 | 3.43 | 11.43 | 21.38 | 2.00 | 90.0 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.1 | 3.46 | 9.99 | 16.23 | 10.00 | 78.5 | 45.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.7 | 4.86 | 14.62 | 24.95 | 7.00 | 92.1 | 90.0 |
| XI | XI | Rogers | MID | 2 | 7.7 | 4.40 | 13.18 | 21.04 | 2.00 | 90.0 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.4 | 4.02 | 12.18 | 22.35 | 3.00 | 88.7 | 90.0 |
| XI | XI | Cherki | MID | 13 | 6.7 | 3.29 | 10.25 | 17.15 | 8.00 | 69.3 | 68.0 |
| Bench 4 | Bench | Foden | MID | 13 | 8.6 | 2.64 | 8.67 | 15.06 | 1.00 | 62.1 | 2.0 |

## GW25

- Train rows: 179450
- Bank: 1.70 -> 1.00
- Free transfers: 2 -> 2
- Captain: Rogers
- Vice captain: Rice
- Effective captain: Rogers
- Chip used: none
- Predicted score: 49.62
- Actual score: 69.00
- Transfer: J.Timber -> Gabriel (projected gain 2.47, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 3.90 | 10.56 | 16.26 | 7.00 | 85.7 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.03 | 8.59 | 13.44 | 1.00 | 93.9 | 90.0 |
| XI | XI | Gabriel | DEF | 1 | 7.0 | 4.30 | 13.03 | 22.50 | 6.00 | 86.3 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.8 | 3.88 | 11.16 | 17.92 | 2.00 | 89.6 | 90.0 |
| XI | XI | Mukiele | DEF | 17 | 4.5 | 3.35 | 11.15 | 17.61 | 1.00 | 86.8 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.8 | 3.41 | 10.99 | 17.49 | 2.00 | 86.3 | 90.0 |
| Bench 3 | Bench | Guéhi | DEF | 8 | 5.2 | 2.97 | 8.99 | 14.45 | 3.00 | 82.0 | 90.0 |
| XI | XI | Haaland | FWD | 13 | 15.0 | 4.56 | 16.07 | 28.62 | 11.00 | 78.4 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.2 | 3.28 | 11.87 | 20.07 | 5.00 | 85.3 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.3 | 3.83 | 11.29 | 18.17 | 8.00 | 72.8 | 74.0 |
| XI | XI | Semenyo | MID | 4 | 7.8 | 4.39 | 14.19 | 22.15 | 2.00 | 92.2 | 90.0 |
| Vice Captain | XI | Rice | MID | 1 | 7.4 | 4.89 | 14.16 | 22.28 | 5.00 | 87.1 | 90.0 |
| Captain | Captain | Rogers | MID | 2 | 7.7 | 4.92 | 14.01 | 22.72 | 10.00 | 87.2 | 90.0 |
| Bench 2 | Bench | Cherki | MID | 13 | 6.6 | 3.10 | 10.12 | 16.75 | 1.00 | 72.0 | 29.0 |
| Bench 4 | Bench | Foden | MID | 13 | 8.4 | 1.30 | 6.42 | 12.74 | 0.00 | 17.7 | 0.0 |

## GW26

- Train rows: 180267
- Bank: 1.00 -> 1.00
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Gabriel
- Effective captain: Haaland
- Chip used: bench_boost
- Predicted score: 67.08
- Actual score: 79.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (16.66) beats the best remaining Bench Boost opportunity (12.18).
- Chip advisory: bench_boost (0.58): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Transfer: Foden -> Wirtz (projected gain 1.87, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (16.66) beats the best remaining Bench Boost opportunity (12.18).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.07 | 10.48 | 15.86 | 3.00 | 132.4 | 180.0 |
| Bench 1 | Bench Boost | Dúbravka | GK | 3 | 4.0 | 2.87 | 8.42 | 12.43 | 1.00 | 92.9 | 90.0 |
| Vice Captain | XI | Gabriel | DEF | 1 | 7.1 | 5.20 | 14.25 | 23.60 | 7.00 | 138.7 | 180.0 |
| Bench 2 | Bench Boost | Senesi | DEF | 4 | 4.8 | 3.39 | 10.35 | 17.02 | 2.00 | 85.7 | 90.0 |
| Bench 3 | Bench Boost | Mukiele | DEF | 17 | 4.6 | 3.31 | 10.02 | 15.97 | 2.00 | 82.8 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.8 | 3.57 | 10.00 | 15.79 | 1.00 | 83.1 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 3.60 | 9.82 | 15.51 | 7.00 | 74.1 | 90.0 |
| Captain | Captain | Haaland | FWD | 13 | 14.9 | 6.09 | 17.69 | 28.08 | 5.00 | 87.3 | 45.0 |
| XI | XI | Thiago | FWD | 5 | 7.1 | 3.92 | 12.87 | 21.59 | 2.00 | 86.3 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.5 | 3.99 | 11.71 | 17.96 | 10.00 | 73.3 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 7.8 | 4.88 | 14.03 | 21.03 | 14.00 | 90.7 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.5 | 4.76 | 13.70 | 21.19 | 14.00 | 113.2 | 180.0 |
| XI | XI | Rogers | MID | 2 | 7.6 | 4.45 | 13.45 | 21.14 | 2.00 | 91.0 | 90.0 |
| XI | XI | Wirtz | MID | 12 | 8.3 | 3.92 | 12.13 | 19.03 | 3.00 | 83.9 | 90.0 |
| Bench 4 | Bench Boost | Cherki | MID | 13 | 6.6 | 2.97 | 8.31 | 13.87 | 1.00 | 63.2 | 19.0 |

## GW27

- Train rows: 181084
- Bank: 1.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Gabriel
- Vice captain: Rice
- Effective captain: Gabriel
- Chip used: none
- Predicted score: 55.82
- Actual score: 37.00
- Transfer: Cherki -> Enzo (projected gain 1.47, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.09 | 12.15 | 17.50 | 3.00 | 116.2 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.66 | 7.93 | 12.69 | 2.00 | 89.7 | 90.0 |
| Captain | Captain | Gabriel | DEF | 1 | 7.1 | 5.79 | 16.72 | 26.03 | 2.00 | 128.8 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 3.63 | 11.45 | 17.37 | 2.00 | 95.2 | 90.0 |
| XI | XI | Mukiele | DEF | 17 | 4.6 | 3.81 | 10.50 | 16.81 | 1.00 | 86.1 | 11.0 |
| Bench 4 | Bench | Tarkowski | DEF | 9 | 5.8 | 2.68 | 8.33 | 14.16 | 1.00 | 81.4 | 90.0 |
| Bench 3 | Bench | Senesi | DEF | 4 | 4.8 | 2.97 | 8.20 | 13.56 | 5.00 | 85.9 | 90.0 |
| XI | XI | Haaland | FWD | 13 | 14.9 | 4.83 | 13.92 | 22.51 | 6.00 | 60.2 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.6 | 4.44 | 13.19 | 20.53 | 7.00 | 85.6 | 79.0 |
| XI | XI | Thiago | FWD | 5 | 7.0 | 3.91 | 11.15 | 17.99 | 2.00 | 85.8 | 90.0 |
| Vice Captain | XI | Rice | MID | 1 | 7.5 | 5.75 | 16.88 | 26.72 | 4.00 | 119.6 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 7.9 | 4.97 | 14.44 | 21.58 | 4.00 | 94.0 | 86.0 |
| XI | XI | Enzo | MID | 7 | 6.9 | 4.84 | 13.33 | 21.00 | 2.00 | 87.4 | 90.0 |
| Bench 2 | Bench | Wirtz | MID | 12 | 8.4 | 3.81 | 12.00 | 19.20 | 0.00 | 86.0 | 0.0 |
| XI | XI | Rogers | MID | 2 | 7.6 | 3.98 | 11.70 | 18.40 | 2.00 | 83.2 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 0.60 -> 0.40
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Rice
- Effective captain: Rice
- Chip used: none
- Predicted score: 54.23
- Actual score: 53.00
- Transfer: Wirtz -> Mbeumo (projected gain 2.37, hit 0)
- Autosub outfielders: Rogers.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.48 | 9.47 | 14.63 | 3.00 | 93.8 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.85 | 8.17 | 13.06 | 0.00 | 89.1 | 90.0 |
| XI | XI | Gabriel | DEF | 1 | 7.1 | 4.78 | 14.70 | 21.88 | 9.00 | 98.8 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 4.02 | 12.14 | 17.96 | 6.00 | 90.7 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.8 | 3.36 | 9.62 | 15.42 | 4.00 | 86.9 | 90.0 |
| Bench 3 | Bench | Tarkowski | DEF | 9 | 5.7 | 2.65 | 8.01 | 12.95 | 3.00 | 81.2 | 90.0 |
| Bench 4 | Bench | Mukiele | DEF | 17 | 4.6 | 2.21 | 7.38 | 12.17 | 0.00 | 45.4 | 0.0 |
| Captain | Bench | Haaland | FWD | 13 | 14.8 | 5.67 | 16.95 | 25.72 | 0.00 | 89.4 | 0.0 |
| XI | XI | João Pedro | FWD | 7 | 7.7 | 4.90 | 14.99 | 23.02 | 2.00 | 85.6 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.0 | 4.47 | 13.32 | 21.20 | 6.00 | 84.2 | 90.0 |
| Vice Captain | Captain | Rice | MID | 1 | 7.6 | 5.12 | 16.12 | 24.97 | 5.00 | 107.6 | 75.0 |
| XI | XI | Semenyo | MID | 4 | 8.0 | 4.59 | 13.41 | 21.59 | 8.00 | 89.4 | 90.0 |
| XI | XI | Mbeumo | MID | 14 | 8.6 | 4.44 | 12.16 | 18.67 | 2.00 | 78.1 | 85.0 |
| XI | XI | Enzo | MID | 7 | 6.9 | 3.74 | 11.58 | 18.97 | 1.00 | 83.7 | 85.0 |
| Bench 2 | Autosub In | Rogers | MID | 2 | 7.7 | 3.57 | 9.91 | 16.28 | 2.00 | 62.9 | 90.0 |

## GW29

- Train rows: 182721
- Bank: 0.40 -> 0.10
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: Gabriel
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 52.45
- Actual score: 62.00
- Transfer: Tarkowski -> Virgil (projected gain 4.28, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.72 | 9.46 | 14.20 | 7.00 | 92.9 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.47 | 7.74 | 12.26 | 2.00 | 88.3 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 6.0 | 4.32 | 13.66 | 21.31 | 1.00 | 89.7 | 90.0 |
| Vice Captain | XI | Gabriel | DEF | 1 | 7.1 | 4.81 | 13.27 | 20.97 | 11.00 | 111.5 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 3.88 | 10.50 | 15.85 | 1.00 | 90.8 | 90.0 |
| Bench 2 | Bench | Senesi | DEF | 4 | 4.9 | 2.92 | 9.03 | 14.41 | 11.00 | 89.3 | 90.0 |
| Bench 4 | Bench | Mukiele | DEF | 17 | 4.6 | 1.18 | 4.12 | 7.44 | 0.00 | 21.2 | 0.0 |
| XI | XI | João Pedro | FWD | 7 | 7.7 | 4.57 | 14.40 | 22.43 | 19.00 | 84.9 | 84.0 |
| XI | XI | Haaland | FWD | 13 | 14.8 | 4.45 | 13.70 | 20.95 | 2.00 | 65.2 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.1 | 3.97 | 11.80 | 17.83 | 2.00 | 86.2 | 90.0 |
| Captain | Captain | Semenyo | MID | 4 | 8.1 | 5.53 | 15.11 | 23.54 | 7.00 | 100.0 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.6 | 3.95 | 12.78 | 20.40 | 3.00 | 99.1 | 90.0 |
| XI | XI | Mbeumo | MID | 14 | 8.7 | 4.07 | 11.97 | 18.98 | 1.00 | 78.9 | 76.0 |
| XI | XI | Rogers | MID | 2 | 7.7 | 3.66 | 11.92 | 18.30 | 1.00 | 84.6 | 90.0 |
| Bench 3 | Bench | Enzo | MID | 7 | 6.8 | 2.92 | 9.59 | 16.05 | 4.00 | 78.7 | 78.0 |

## GW30

- Train rows: 183541
- Bank: 0.10 -> 0.30
- Free transfers: 2 -> 2
- Captain: João Pedro
- Vice captain: Semenyo
- Effective captain: João Pedro
- Chip used: triple_captain
- Predicted score: 56.99
- Actual score: 51.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.88) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Guéhi -> Thiaw (projected gain 0.81, hit 0)
- Chip used: Triple Captain on João Pedro. Optimizer chose Triple Captain here because the current estimated captain upside (5.88) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.74 | 9.32 | 13.92 | 7.00 | 91.0 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.90 | 8.15 | 12.22 | 6.00 | 88.7 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 6.1 | 4.03 | 12.33 | 19.07 | 2.00 | 87.2 | 90.0 |
| XI | XI | Gabriel | DEF | 1 | 7.1 | 3.76 | 11.52 | 18.66 | 9.00 | 96.3 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.9 | 3.46 | 10.96 | 17.25 | 10.00 | 91.0 | 90.0 |
| Bench 3 | Bench | Thiaw | DEF | 15 | 5.0 | 2.95 | 9.09 | 13.64 | 9.00 | 84.1 | 90.0 |
| Bench 4 | Bench | Mukiele | DEF | 17 | 4.5 | 1.02 | 3.63 | 7.26 | 0.00 | 17.5 | 0.0 |
| Captain | Captain | João Pedro | FWD | 7 | 7.6 | 5.88 | 16.46 | 24.72 | 2.00 | 94.1 | 90.0 |
| XI | XI | Haaland | FWD | 13 | 14.7 | 4.19 | 12.28 | 20.50 | 2.00 | 75.6 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.2 | 3.60 | 9.79 | 15.33 | 6.00 | 87.3 | 90.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 8.2 | 5.65 | 15.55 | 23.96 | 2.00 | 102.0 | 74.0 |
| XI | XI | Mbeumo | MID | 14 | 8.7 | 3.65 | 11.60 | 18.33 | 2.00 | 67.4 | 74.0 |
| XI | XI | Rice | MID | 1 | 7.5 | 4.04 | 10.93 | 17.73 | 3.00 | 83.0 | 90.0 |
| XI | XI | Enzo | MID | 7 | 6.7 | 3.26 | 10.92 | 17.09 | 2.00 | 80.5 | 90.0 |
| Bench 2 | Bench | Rogers | MID | 2 | 7.6 | 3.21 | 10.58 | 16.81 | 2.00 | 83.9 | 90.0 |