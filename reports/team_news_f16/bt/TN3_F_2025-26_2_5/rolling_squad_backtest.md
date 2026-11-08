# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW5
- Total predicted points: 259.10
- Total actual points: 252.00
- Average predicted points: 64.77
- Average actual points: 63.00
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
- Captain: Mohamed Salah
- Vice captain: Daniel Ballard
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 69.94
- Actual score: 45.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 4.23 | 10.76 | 17.41 | 1.00 | 88.4 | 90.0 |
| Bench 1 | Bench | Angus Gunn | GK | 16 | 4.0 | 0.40 | 0.89 | 1.52 | 0.00 | 3.3 | 0.0 |
| Vice Captain | XI | Daniel Ballard | DEF | 17 | 4.6 | 7.29 | 17.40 | 27.50 | 1.00 | 90.0 | 8.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.44 | 12.16 | 19.36 | 6.00 | 90.0 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 4.16 | 10.60 | 16.80 | 3.00 | 88.3 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.68 | 9.28 | 15.93 | -1.00 | 82.0 | 90.0 |
| Bench 4 | Bench | Joe Rodon | DEF | 11 | 4.0 | 2.57 | 8.43 | 14.23 | 2.00 | 86.7 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.0 | 6.24 | 18.95 | 31.59 | 2.00 | 78.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 5.57 | 18.22 | 30.09 | 9.00 | 90.0 | 79.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.6 | 4.51 | 14.22 | 23.12 | 2.00 | 89.7 | 87.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.60 | 22.73 | 38.16 | 5.00 | 90.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 6.80 | 19.96 | 31.23 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.1 | 6.94 | 16.25 | 25.20 | 6.00 | 90.0 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 4.55 | 14.57 | 23.91 | 3.00 | 90.0 | 85.0 |
| Bench 2 | Bench | Anton Stach | MID | 11 | 5.0 | 3.84 | 12.86 | 21.46 | 2.00 | 89.9 | 90.0 |

## GW3

- Train rows: 162672
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 57.97
- Actual score: 44.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 2.80 | 8.16 | 13.31 | 8.00 | 78.7 | 90.0 |
| Bench 1 | Bench | Angus Gunn | GK | 16 | 4.0 | 0.19 | 0.70 | 1.24 | 0.00 | 1.3 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 3.20 | 10.29 | 16.73 | 2.00 | 75.5 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 3.29 | 8.75 | 14.08 | 1.00 | 74.2 | 90.0 |
| XI | XI | Joe Rodon | DEF | 11 | 4.0 | 3.06 | 7.83 | 12.79 | 7.00 | 76.8 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.34 | 7.15 | 11.73 | 9.00 | 68.6 | 79.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 1.56 | 5.03 | 9.30 | 0.00 | 0.1 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.0 | 6.72 | 20.74 | 33.77 | 9.00 | 83.1 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.6 | 6.36 | 16.61 | 25.33 | 2.00 | 83.5 | 72.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 4.46 | 15.82 | 25.89 | 2.00 | 75.0 | 78.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.14 | 22.63 | 37.75 | 3.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 4.57 | 15.71 | 24.23 | 2.00 | 84.1 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 5.16 | 15.25 | 23.90 | 2.00 | 87.3 | 90.0 |
| Bench 2 | Bench | Tijjani Reijnders | MID | 13 | 5.6 | 3.77 | 12.45 | 19.14 | 2.00 | 70.6 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 4.06 | 10.58 | 17.28 | 3.00 | 76.5 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 66.61
- Actual score: 89.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.92) beats the best remaining Bench Boost opportunity (8.77).
- Transfer: Daniel Ballard -> Marc Guéhi (projected gain 5.22, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.92) beats the best remaining Bench Boost opportunity (8.77).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 2.81 | 9.43 | 14.86 | 10.00 | 86.7 | 90.0 |
| Bench 1 | Bench Boost | Angus Gunn | GK | 16 | 4.0 | 0.00 | 0.92 | 0.96 | 0.00 | 2.1 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.6 | 4.42 | 12.62 | 18.89 | 6.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.04 | 12.01 | 18.49 | 9.00 | 85.2 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 2.90 | 8.24 | 12.66 | 6.00 | 75.1 | 90.0 |
| Bench 2 | Bench Boost | Joe Rodon | DEF | 11 | 4.0 | 2.62 | 7.51 | 11.60 | 4.00 | 68.8 | 90.0 |
| Bench 3 | Bench Boost | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.30 | 7.26 | 11.24 | 0.00 | 60.0 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.0 | 6.68 | 20.50 | 32.95 | 13.00 | 79.4 | 86.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 5.23 | 15.74 | 24.39 | 2.00 | 70.1 | 71.0 |
| Bench 4 | Bench Boost | Chris Wood | FWD | 16 | 7.6 | 1.96 | 9.14 | 15.02 | 1.00 | 36.7 | 59.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 8.19 | 23.74 | 37.81 | 9.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 5.56 | 17.19 | 25.18 | 13.00 | 81.1 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 4.13 | 12.68 | 19.50 | 3.00 | 69.8 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.83 | 11.77 | 18.32 | 3.00 | 77.3 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 3.76 | 10.55 | 16.45 | 1.00 | 77.4 | 90.0 |

## GW5

- Train rows: 164124
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 64.58
- Actual score: 74.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.51) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.51) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 3.15 | 9.51 | 15.61 | 2.00 | 88.8 | 90.0 |
| Bench 1 | Bench | Angus Gunn | GK | 16 | 4.0 | 0.26 | 0.88 | 1.47 | 0.00 | 3.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.16 | 11.88 | 18.52 | 2.00 | 82.4 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.6 | 4.03 | 11.56 | 17.55 | 7.00 | 77.9 | 90.0 |
| XI | XI | Joe Rodon | DEF | 11 | 4.0 | 3.75 | 9.20 | 13.62 | 2.00 | 79.9 | 90.0 |
| Bench 2 | Bench | Reinildo Mandava | DEF | 17 | 4.0 | 3.39 | 8.94 | 13.80 | -2.00 | 81.5 | 32.0 |
| Bench 4 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.60 | 7.14 | 11.44 | 4.00 | 67.2 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.1 | 6.29 | 21.53 | 35.57 | 9.00 | 87.5 | 75.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 3.48 | 11.78 | 19.78 | 8.00 | 50.3 | 66.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.6 | 3.87 | 11.60 | 19.40 | 2.00 | 61.9 | 74.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.48 | 22.36 | 36.61 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.3 | 5.81 | 17.84 | 27.10 | 5.00 | 82.5 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 4.00 | 12.02 | 19.66 | 7.00 | 75.5 | 90.0 |
| Bench 3 | Bench | Tijjani Reijnders | MID | 13 | 5.6 | 3.35 | 10.72 | 17.80 | 9.00 | 78.8 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 3.59 | 9.52 | 15.25 | 15.00 | 76.3 | 90.0 |