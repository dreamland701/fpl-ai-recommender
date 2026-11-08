# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW5
- Total predicted points: 255.14
- Total actual points: 235.00
- Average predicted points: 63.78
- Average actual points: 58.75
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
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Daniel Ballard
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 71.06
- Actual score: 38.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Anton Stach replaced Cole Palmer.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Marco Bizot | GK | 2 | 4.5 | 4.05 | 10.56 | 17.23 | 0.00 | 90.0 | 0.0 |
| Bench 1 | Bench | Sam Proctor | GK | 2 | 4.0 | 0.35 | 0.94 | 1.64 | 0.00 | 13.4 | 0.0 |
| Vice Captain | XI | Daniel Ballard | DEF | 17 | 4.6 | 7.29 | 17.67 | 28.10 | 1.00 | 90.0 | 8.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 4.13 | 10.42 | 16.74 | 3.00 | 87.9 | 90.0 |
| XI | XI | Trai Hume | DEF | 17 | 4.5 | 4.08 | 10.36 | 16.80 | 1.00 | 84.0 | 90.0 |
| Bench 3 | Bench | Matty Cash | DEF | 2 | 4.5 | 3.46 | 9.35 | 15.08 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.66 | 9.10 | 15.58 | -1.00 | 81.9 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.0 | 6.24 | 19.44 | 32.80 | 2.00 | 78.3 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 5.58 | 17.64 | 29.30 | 9.00 | 90.0 | 79.0 |
| XI | XI | Junior Kroupi | FWD | 4 | 4.5 | 4.08 | 10.08 | 16.55 | 2.00 | 27.8 | 4.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.60 | 23.35 | 39.25 | 5.00 | 90.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 6.83 | 19.31 | 30.62 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 6.63 | 18.31 | 30.39 | 0.00 | 90.0 | 0.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.1 | 6.95 | 15.53 | 24.41 | 6.00 | 90.0 | 90.0 |
| Bench 2 | Autosub In | Anton Stach | MID | 11 | 5.0 | 3.83 | 12.54 | 21.00 | 2.00 | 90.0 | 90.0 |

## GW3

- Train rows: 162672
- Bank: 0.10 -> 1.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 54.31
- Actual score: 37.00
- Transfer: Cole Palmer -> Bruno Borges Fernandes (projected gain 29.83, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Marco Bizot | GK | 2 | 4.5 | 1.43 | 4.52 | 7.77 | 0.00 | 38.3 | 90.0 |
| Bench 1 | Bench | Sam Proctor | GK | 2 | 4.0 | 0.49 | 1.22 | 1.92 | 0.00 | 10.5 | 0.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 3.26 | 8.54 | 13.87 | 1.00 | 73.5 | 90.0 |
| XI | XI | Trai Hume | DEF | 17 | 4.5 | 2.79 | 8.29 | 13.53 | 2.00 | 74.8 | 90.0 |
| XI | XI | Matty Cash | DEF | 2 | 4.5 | 3.14 | 8.27 | 13.38 | 0.00 | 75.8 | 73.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.31 | 7.15 | 11.66 | 9.00 | 67.9 | 79.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 1.91 | 5.56 | 9.70 | 0.00 | 11.5 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.0 | 6.72 | 20.22 | 33.18 | 9.00 | 83.4 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 4.45 | 15.15 | 24.89 | 2.00 | 74.7 | 78.0 |
| Bench 2 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 2.56 | 8.34 | 14.44 | 2.00 | 23.6 | 18.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.14 | 22.94 | 38.40 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.87 | 15.44 | 25.29 | 10.00 | 85.8 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 4.59 | 14.60 | 22.77 | 2.00 | 84.6 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.73 | 11.71 | 18.22 | 2.00 | 69.8 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 4.05 | 10.37 | 17.00 | 3.00 | 76.4 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 1.50 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 66.93
- Actual score: 75.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.01) beats the best remaining Bench Boost opportunity (10.77).
- Transfer: Sam Proctor -> David Raya Martín (projected gain 14.48, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.01) beats the best remaining Bench Boost opportunity (10.77).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 3.78 | 11.36 | 17.92 | 6.00 | 88.2 | 90.0 |
| Bench 1 | Bench Boost | Marco Bizot | GK | 2 | 4.5 | 2.10 | 6.48 | 9.99 | 0.00 | 66.6 | 0.0 |
| XI | XI | Trai Hume | DEF | 17 | 4.5 | 2.65 | 8.14 | 12.81 | 6.00 | 75.3 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 2.87 | 7.91 | 12.44 | 6.00 | 74.2 | 90.0 |
| XI | XI | Matty Cash | DEF | 2 | 4.5 | 2.80 | 7.83 | 12.41 | 5.00 | 70.7 | 90.0 |
| Bench 3 | Bench Boost | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.27 | 6.87 | 10.87 | 0.00 | 59.5 | 90.0 |
| Bench 4 | Bench Boost | Daniel Ballard | DEF | 17 | 4.6 | 0.94 | 3.56 | 6.28 | 0.00 | 10.8 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.0 | 6.67 | 19.97 | 32.47 | 13.00 | 79.2 | 86.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 5.20 | 15.03 | 23.62 | 2.00 | 69.5 | 71.0 |
| Bench 2 | Bench Boost | Junior Kroupi | FWD | 4 | 4.5 | 3.23 | 10.81 | 16.88 | 0.00 | 36.3 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 8.18 | 23.83 | 38.43 | 9.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 5.56 | 15.73 | 23.47 | 13.00 | 81.1 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.00 | 14.14 | 23.24 | 2.00 | 75.3 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.78 | 11.37 | 18.02 | 3.00 | 76.1 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 3.74 | 10.21 | 16.20 | 1.00 | 77.1 | 90.0 |

## GW5

- Train rows: 164124
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 62.83
- Actual score: 85.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.84) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.84) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 3.37 | 10.41 | 17.01 | 2.00 | 80.8 | 90.0 |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.5 | 0.97 | 3.38 | 5.84 | 0.00 | 32.3 | 0.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 3.36 | 8.82 | 13.56 | -2.00 | 80.7 | 32.0 |
| XI | XI | Matty Cash | DEF | 2 | 4.5 | 3.07 | 8.71 | 13.82 | 10.00 | 79.8 | 90.0 |
| XI | XI | Trai Hume | DEF | 17 | 4.5 | 3.02 | 8.55 | 13.78 | 4.00 | 79.4 | 90.0 |
| Bench 2 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.56 | 7.02 | 11.18 | 4.00 | 66.3 | 90.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 0.89 | 2.83 | 4.79 | 1.00 | 6.8 | 53.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.1 | 6.30 | 20.93 | 34.76 | 9.00 | 87.7 | 75.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 3.41 | 11.35 | 19.17 | 8.00 | 48.4 | 66.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 2.23 | 7.04 | 11.89 | 0.00 | 22.1 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.46 | 22.51 | 37.10 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.3 | 5.81 | 16.66 | 25.49 | 5.00 | 82.4 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.24 | 14.46 | 22.95 | 10.00 | 80.2 | 86.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.31 | 10.35 | 17.21 | 9.00 | 77.6 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 3.56 | 9.37 | 15.04 | 15.00 | 75.7 | 90.0 |