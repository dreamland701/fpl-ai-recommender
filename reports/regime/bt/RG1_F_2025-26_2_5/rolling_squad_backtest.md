# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW5
- Total predicted points: 253.33
- Total actual points: 223.00
- Average predicted points: 63.33
- Average actual points: 55.75
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
- Predicted score: 70.02
- Actual score: 47.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Marco Bizot | GK | 2 | 4.5 | 3.91 | 10.65 | 17.17 | 0.00 | 89.1 | 0.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 4.0 | 0.12 | 1.07 | 1.88 | 0.00 | 9.1 | 0.0 |
| Vice Captain | XI | Daniel Ballard | DEF | 17 | 4.6 | 7.47 | 17.15 | 27.19 | 1.00 | 90.0 | 8.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 4.90 | 12.20 | 19.45 | 5.00 | 90.0 | 68.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.64 | 11.99 | 19.15 | 6.00 | 90.0 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 4.31 | 10.26 | 16.28 | 3.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.96 | 9.38 | 16.19 | -1.00 | 86.6 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.0 | 6.39 | 19.70 | 32.95 | 2.00 | 72.6 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 5.54 | 18.28 | 30.22 | 9.00 | 87.1 | 79.0 |
| Bench 2 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 4.12 | 10.33 | 16.77 | 2.00 | 60.5 | 62.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.53 | 22.85 | 38.44 | 5.00 | 90.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 6.56 | 19.38 | 30.19 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.1 | 6.84 | 16.27 | 25.31 | 6.00 | 90.0 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 4.39 | 14.36 | 23.57 | 3.00 | 90.0 | 85.0 |
| Bench 3 | Bench | Anton Stach | MID | 11 | 5.0 | 3.71 | 12.71 | 21.23 | 2.00 | 88.0 | 90.0 |

## GW3

- Train rows: 162672
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 54.75
- Actual score: 35.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Marco Bizot | GK | 2 | 4.5 | 1.37 | 4.78 | 8.13 | 0.00 | 34.3 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 4.0 | 0.46 | 1.45 | 2.33 | 0.00 | 6.7 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 4.52 | 13.21 | 20.70 | 6.00 | 78.4 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 3.31 | 10.11 | 16.52 | 2.00 | 77.2 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 3.36 | 8.46 | 13.67 | 1.00 | 75.2 | 90.0 |
| Bench 2 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.51 | 7.22 | 11.96 | 9.00 | 70.7 | 79.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 2.13 | 6.01 | 10.64 | 0.00 | 13.9 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.0 | 6.69 | 21.36 | 34.92 | 9.00 | 80.6 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 4.25 | 15.82 | 25.94 | 2.00 | 71.1 | 78.0 |
| Bench 3 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.31 | 7.69 | 12.75 | 2.00 | 44.3 | 64.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.08 | 22.66 | 37.90 | 3.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 4.56 | 15.92 | 24.64 | 2.00 | 84.7 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 5.02 | 15.01 | 23.51 | 2.00 | 85.4 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.55 | 11.97 | 18.40 | 2.00 | 68.8 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 3.95 | 10.46 | 17.12 | 3.00 | 73.9 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 67.37
- Actual score: 75.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.92) beats the best remaining Bench Boost opportunity (9.74).
- Transfer: Daniel Ballard -> Marc Guéhi (projected gain 4.58, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.92) beats the best remaining Bench Boost opportunity (9.74).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Marco Bizot | GK | 2 | 4.5 | 2.11 | 6.21 | 10.53 | 0.00 | 63.4 | 0.0 |
| Bench 1 | Bench Boost | Daniel Bentley | GK | 20 | 4.0 | 0.33 | 1.07 | 2.22 | 0.00 | 6.1 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.6 | 4.56 | 13.23 | 18.68 | 6.00 | 90.0 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 4.04 | 12.90 | 18.73 | 1.00 | 71.7 | 45.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.16 | 12.59 | 18.29 | 9.00 | 86.5 | 90.0 |
| Bench 2 | Bench Boost | Reinildo Mandava | DEF | 17 | 4.0 | 2.98 | 8.77 | 12.36 | 6.00 | 75.5 | 90.0 |
| Bench 3 | Bench Boost | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.51 | 8.14 | 11.57 | 0.00 | 61.4 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.0 | 6.72 | 20.69 | 34.21 | 13.00 | 77.8 | 86.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 5.04 | 15.15 | 24.28 | 2.00 | 66.7 | 71.0 |
| Bench 4 | Bench Boost | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.06 | 7.06 | 12.00 | 0.00 | 47.4 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 8.13 | 23.67 | 38.06 | 9.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 5.50 | 17.14 | 25.46 | 13.00 | 81.0 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 3.93 | 12.19 | 19.03 | 3.00 | 67.5 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.56 | 11.06 | 17.46 | 3.00 | 75.1 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 3.62 | 10.28 | 16.31 | 1.00 | 75.0 | 90.0 |

## GW5

- Train rows: 164124
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 61.19
- Actual score: 66.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.43) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.43) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Marco Bizot | GK | 2 | 4.5 | 1.04 | 3.25 | 6.21 | 0.00 | 29.5 | 0.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 4.0 | 0.62 | 1.21 | 2.50 | 0.00 | 7.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.28 | 12.39 | 18.29 | 2.00 | 83.2 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.6 | 4.18 | 12.08 | 17.35 | 7.00 | 78.7 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.1 | 3.53 | 10.95 | 16.93 | 0.00 | 61.4 | 63.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 3.50 | 9.35 | 13.43 | -2.00 | 81.7 | 32.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.82 | 7.91 | 11.66 | 4.00 | 68.1 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.1 | 6.29 | 21.40 | 36.78 | 9.00 | 86.7 | 75.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 3.18 | 10.76 | 19.53 | 8.00 | 45.9 | 66.0 |
| Bench 4 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 1.34 | 4.11 | 8.25 | 1.00 | 25.8 | 10.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.41 | 22.22 | 36.91 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.3 | 5.72 | 17.54 | 27.24 | 5.00 | 82.7 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 3.79 | 11.40 | 19.22 | 7.00 | 73.5 | 90.0 |
| Bench 2 | Bench | Tijjani Reijnders | MID | 13 | 5.6 | 3.09 | 9.92 | 17.03 | 9.00 | 76.7 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 3.44 | 9.10 | 15.13 | 15.00 | 74.3 | 90.0 |