# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW5
- Total predicted points: 254.11
- Total actual points: 231.00
- Average predicted points: 63.53
- Average actual points: 57.75
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
- Predicted score: 70.01
- Actual score: 46.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Marco Bizot | GK | 2 | 4.5 | 4.07 | 10.59 | 17.06 | 0.00 | 90.0 | 0.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 4.0 | 0.25 | 1.12 | 2.14 | 0.00 | 11.6 | 0.0 |
| Vice Captain | XI | Daniel Ballard | DEF | 17 | 4.6 | 7.29 | 17.39 | 27.60 | 1.00 | 90.0 | 8.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.43 | 12.07 | 19.25 | 6.00 | 90.0 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 4.58 | 11.90 | 18.86 | 5.00 | 90.0 | 68.0 |
| Bench 2 | Bench | Reinildo Mandava | DEF | 17 | 4.0 | 4.15 | 10.50 | 16.66 | 3.00 | 88.3 | 90.0 |
| Bench 4 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.67 | 9.19 | 15.82 | -1.00 | 82.0 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.0 | 6.26 | 18.95 | 31.54 | 2.00 | 78.7 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 5.57 | 18.24 | 30.20 | 9.00 | 90.0 | 79.0 |
| XI | XI | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 4.28 | 10.60 | 17.22 | 2.00 | 69.0 | 62.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.62 | 22.64 | 37.98 | 5.00 | 90.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 6.81 | 20.04 | 31.50 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.1 | 6.95 | 16.26 | 25.26 | 6.00 | 90.0 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 4.54 | 14.51 | 23.86 | 3.00 | 90.0 | 85.0 |
| Bench 3 | Bench | Anton Stach | MID | 11 | 5.0 | 3.83 | 12.80 | 21.43 | 2.00 | 90.0 | 90.0 |

## GW3

- Train rows: 162672
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.15
- Actual score: 35.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Marco Bizot | GK | 2 | 4.5 | 1.44 | 4.54 | 7.72 | 0.00 | 38.6 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 4.0 | 0.48 | 1.43 | 2.46 | 0.00 | 7.7 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 4.30 | 13.06 | 20.43 | 6.00 | 75.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 3.17 | 10.14 | 16.50 | 2.00 | 74.7 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 3.27 | 8.62 | 13.89 | 1.00 | 73.6 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.31 | 7.06 | 11.60 | 9.00 | 67.9 | 79.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 1.99 | 6.38 | 11.41 | 0.00 | 13.0 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.0 | 6.73 | 20.69 | 33.66 | 9.00 | 83.6 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 4.45 | 15.77 | 25.84 | 2.00 | 74.6 | 78.0 |
| Bench 2 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.57 | 7.80 | 12.92 | 2.00 | 49.1 | 64.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.16 | 22.54 | 37.58 | 3.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 4.56 | 15.71 | 24.29 | 2.00 | 84.1 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 5.14 | 15.20 | 23.88 | 2.00 | 86.7 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.73 | 12.29 | 18.92 | 2.00 | 69.8 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 4.05 | 10.51 | 17.21 | 3.00 | 76.3 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 67.64
- Actual score: 75.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.84) beats the best remaining Bench Boost opportunity (9.67).
- Transfer: Daniel Ballard -> Marc Guéhi (projected gain 4.60, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.84) beats the best remaining Bench Boost opportunity (9.67).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Marco Bizot | GK | 2 | 4.5 | 2.11 | 6.69 | 10.10 | 0.00 | 66.8 | 0.0 |
| Bench 1 | Bench Boost | Antonín Kinský | GK | 18 | 4.0 | 0.36 | 1.92 | 2.51 | 0.00 | 8.4 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.6 | 4.40 | 12.58 | 18.88 | 6.00 | 90.0 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 3.85 | 12.07 | 18.51 | 1.00 | 69.9 | 45.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.01 | 11.90 | 18.31 | 9.00 | 84.6 | 90.0 |
| Bench 2 | Bench Boost | Reinildo Mandava | DEF | 17 | 4.0 | 2.86 | 8.12 | 12.47 | 6.00 | 74.2 | 90.0 |
| Bench 3 | Bench Boost | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.33 | 7.82 | 12.52 | 0.00 | 60.4 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.0 | 6.69 | 20.42 | 32.75 | 13.00 | 79.7 | 86.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 5.21 | 15.65 | 24.26 | 2.00 | 69.7 | 71.0 |
| Bench 4 | Bench Boost | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.26 | 7.68 | 12.20 | 0.00 | 51.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 8.20 | 23.67 | 37.64 | 9.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 5.54 | 17.15 | 25.16 | 13.00 | 80.8 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 4.09 | 12.53 | 19.24 | 3.00 | 68.7 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.79 | 11.61 | 18.05 | 3.00 | 76.4 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 3.74 | 10.48 | 16.36 | 1.00 | 77.0 | 90.0 |

## GW5

- Train rows: 164124
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 61.31
- Actual score: 75.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.52) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.52) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Marco Bizot | GK | 2 | 4.5 | 0.99 | 3.35 | 5.66 | 0.00 | 32.7 | 0.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 4.0 | 0.28 | 1.47 | 2.50 | 0.00 | 9.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.13 | 11.79 | 18.28 | 2.00 | 81.7 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.6 | 3.99 | 11.49 | 17.38 | 7.00 | 76.8 | 90.0 |
| Bench 2 | Bench | Marc Cucurella Saseta | DEF | 7 | 6.1 | 3.30 | 10.16 | 16.60 | 0.00 | 59.7 | 63.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 3.36 | 8.89 | 13.61 | -2.00 | 80.7 | 32.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.57 | 7.09 | 11.27 | 4.00 | 66.4 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.1 | 6.30 | 21.53 | 35.45 | 9.00 | 87.8 | 75.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 3.44 | 11.58 | 19.35 | 8.00 | 49.1 | 66.0 |
| Bench 4 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 1.62 | 5.07 | 8.49 | 1.00 | 29.1 | 10.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.49 | 22.29 | 36.35 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.3 | 5.78 | 17.84 | 27.06 | 5.00 | 81.7 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 3.97 | 11.94 | 19.42 | 7.00 | 74.7 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.33 | 10.63 | 17.55 | 9.00 | 78.0 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 3.56 | 9.49 | 15.13 | 15.00 | 75.7 | 90.0 |