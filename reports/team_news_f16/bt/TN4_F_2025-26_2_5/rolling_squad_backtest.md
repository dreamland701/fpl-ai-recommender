# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW5
- Total predicted points: 258.32
- Total actual points: 252.00
- Average predicted points: 64.58
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
- Predicted score: 69.88
- Actual score: 45.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 4.20 | 10.67 | 17.34 | 1.00 | 88.0 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 4.0 | 0.17 | 0.96 | 1.89 | 0.00 | 7.7 | 0.0 |
| Vice Captain | XI | Daniel Ballard | DEF | 17 | 4.6 | 7.29 | 17.35 | 27.49 | 1.00 | 90.0 | 8.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.42 | 12.09 | 19.32 | 6.00 | 90.0 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 4.13 | 10.51 | 16.73 | 3.00 | 87.9 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.66 | 9.22 | 15.88 | -1.00 | 81.9 | 90.0 |
| Bench 4 | Bench | Joe Rodon | DEF | 11 | 4.0 | 2.54 | 8.34 | 14.16 | 2.00 | 86.4 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.0 | 6.24 | 18.96 | 31.60 | 2.00 | 78.3 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 5.58 | 18.21 | 30.09 | 9.00 | 90.0 | 79.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.6 | 4.50 | 14.19 | 23.12 | 2.00 | 89.6 | 87.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.60 | 22.70 | 38.15 | 5.00 | 90.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 6.83 | 19.97 | 31.25 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.1 | 6.95 | 16.24 | 25.23 | 6.00 | 90.0 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 4.54 | 14.52 | 23.88 | 3.00 | 90.0 | 85.0 |
| Bench 2 | Bench | Anton Stach | MID | 11 | 5.0 | 3.83 | 12.81 | 21.44 | 2.00 | 90.0 | 90.0 |

## GW3

- Train rows: 162672
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 57.84
- Actual score: 44.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 2.76 | 8.07 | 13.24 | 8.00 | 78.0 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 4.0 | 0.32 | 1.24 | 2.18 | 0.00 | 5.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 3.17 | 10.21 | 16.68 | 2.00 | 74.7 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 3.26 | 8.65 | 14.01 | 1.00 | 73.5 | 90.0 |
| XI | XI | Joe Rodon | DEF | 11 | 4.0 | 3.04 | 7.73 | 12.72 | 7.00 | 76.3 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.31 | 7.06 | 11.66 | 9.00 | 67.9 | 79.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 0.06 | 3.93 | 8.27 | 0.00 | 0.3 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.0 | 6.72 | 20.74 | 33.82 | 9.00 | 83.4 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.6 | 6.35 | 16.57 | 25.32 | 2.00 | 83.3 | 72.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 4.45 | 15.78 | 25.87 | 2.00 | 74.7 | 78.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.14 | 22.59 | 37.74 | 3.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 4.59 | 15.72 | 24.27 | 2.00 | 84.6 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 5.16 | 15.21 | 23.88 | 2.00 | 87.1 | 90.0 |
| Bench 2 | Bench | Tijjani Reijnders | MID | 13 | 5.6 | 3.73 | 12.37 | 19.10 | 2.00 | 69.8 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 4.05 | 10.52 | 17.24 | 3.00 | 76.4 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 66.44
- Actual score: 89.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.02) beats the best remaining Bench Boost opportunity (8.86).
- Transfer: Daniel Ballard -> Marc Guéhi (projected gain 5.29, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.02) beats the best remaining Bench Boost opportunity (8.86).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 2.77 | 9.36 | 14.80 | 10.00 | 85.9 | 90.0 |
| Bench 1 | Bench Boost | Antonín Kinský | GK | 18 | 4.0 | 0.24 | 1.67 | 2.22 | 0.00 | 5.6 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.6 | 4.42 | 12.58 | 18.86 | 6.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.00 | 11.93 | 18.43 | 9.00 | 84.3 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 2.87 | 8.15 | 12.59 | 6.00 | 74.2 | 90.0 |
| Bench 2 | Bench Boost | Joe Rodon | DEF | 11 | 4.0 | 2.60 | 7.42 | 11.54 | 4.00 | 68.5 | 90.0 |
| Bench 3 | Bench Boost | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.27 | 7.17 | 11.17 | 0.00 | 59.5 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.0 | 6.67 | 20.49 | 32.98 | 13.00 | 79.2 | 86.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 5.20 | 15.68 | 24.35 | 2.00 | 69.5 | 71.0 |
| Bench 4 | Bench Boost | Chris Wood | FWD | 16 | 7.6 | 1.88 | 9.01 | 14.92 | 1.00 | 34.8 | 59.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 8.18 | 23.70 | 37.80 | 9.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 5.56 | 17.17 | 25.19 | 13.00 | 81.1 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 4.09 | 12.59 | 19.44 | 3.00 | 68.6 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.78 | 11.67 | 18.25 | 3.00 | 76.1 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 3.74 | 10.49 | 16.41 | 1.00 | 77.1 | 90.0 |

## GW5

- Train rows: 164124
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 64.17
- Actual score: 74.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.49) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.49) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 3.12 | 9.45 | 15.55 | 2.00 | 88.1 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 4.0 | 0.19 | 1.28 | 2.22 | 0.00 | 6.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.12 | 11.82 | 18.45 | 2.00 | 81.5 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.6 | 4.00 | 11.51 | 17.51 | 7.00 | 77.0 | 90.0 |
| XI | XI | Joe Rodon | DEF | 11 | 4.0 | 3.73 | 9.16 | 13.55 | 2.00 | 79.3 | 90.0 |
| Bench 2 | Bench | Reinildo Mandava | DEF | 17 | 4.0 | 3.36 | 8.90 | 13.73 | -2.00 | 80.7 | 32.0 |
| Bench 4 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.56 | 7.08 | 11.37 | 4.00 | 66.3 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.1 | 6.30 | 21.56 | 35.61 | 9.00 | 87.7 | 75.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 3.41 | 11.66 | 19.67 | 8.00 | 48.4 | 66.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.6 | 3.78 | 11.45 | 19.25 | 2.00 | 59.8 | 74.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.46 | 22.33 | 36.59 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.3 | 5.81 | 17.85 | 27.12 | 5.00 | 82.4 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 3.96 | 11.96 | 19.59 | 7.00 | 74.4 | 90.0 |
| Bench 3 | Bench | Tijjani Reijnders | MID | 13 | 5.6 | 3.31 | 10.65 | 17.72 | 9.00 | 77.6 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 3.56 | 9.49 | 15.20 | 15.00 | 75.7 | 90.0 |