# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW5
- Simulated weeks: GW6-GW9
- Total predicted points: 284.75
- Total actual points: 289.00
- Average predicted points: 71.19
- Average actual points: 72.25
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW5 are included before the first simulated week.
- League-average scores were not available for this run.

## GW6

- Train rows: 164865
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Erling Haaland
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 67.95
- Actual score: 62.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.82 | 11.46 | 19.29 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.52 | 1.28 | 2.87 | 0.00 | 2.7 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.17 | 14.45 | 20.07 | 7.00 | 90.0 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.2 | 3.29 | 13.89 | 20.48 | -3.00 | 90.0 | 52.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.7 | 3.77 | 12.50 | 19.62 | 7.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Omar Alderete | DEF | 17 | 4.0 | 1.97 | 10.25 | 14.49 | 17.00 | 85.3 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.0 | 3.21 | 10.24 | 14.16 | 6.00 | 84.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.93 | 24.30 | 40.33 | 16.00 | 90.0 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.89 | 18.46 | 30.57 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 1.61 | 3.64 | 6.49 | 12.00 | 17.7 | 18.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.5 | 6.35 | 20.04 | 34.34 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.86 | 18.14 | 27.69 | 7.00 | 90.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 5.19 | 14.68 | 23.03 | 2.00 | 90.0 | 82.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.45 | 14.48 | 23.67 | 2.00 | 87.4 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.32 | 14.44 | 21.92 | 2.00 | 90.0 | 80.0 |

## GW7

- Train rows: 165607
- Bank: 0.10 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 63.29
- Actual score: 67.00
- Transfer: João Pedro Junqueira de Jesus -> Jean-Philippe Mateta (projected gain 0.98, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.97 | 11.36 | 18.23 | 6.00 | 83.4 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.17 | 0.96 | 2.04 | 0.00 | 3.5 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 4.90 | 14.94 | 20.12 | 2.00 | 82.2 | 77.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.7 | 4.47 | 14.55 | 21.15 | 3.00 | 90.0 | 90.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.0 | 4.22 | 13.04 | 18.08 | 0.00 | 90.0 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 3.59 | 9.89 | 13.58 | 3.00 | 77.7 | 90.0 |
| Bench 4 | Bench | Trevoh Chalobah | DEF | 7 | 5.2 | 1.45 | 6.07 | 9.34 | 0.00 | 29.7 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.68 | 25.41 | 39.31 | 8.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.5 | 4.23 | 11.91 | 18.99 | 2.00 | 77.0 | 69.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 3.27 | 6.00 | 9.33 | 0.00 | 44.8 | 0.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 6.38 | 18.91 | 31.91 | 2.00 | 88.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 6.11 | 18.48 | 27.72 | 18.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Iliman Ndiaye | MID | 9 | 6.5 | 3.49 | 12.70 | 18.67 | 7.00 | 68.1 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.32 | 12.41 | 19.35 | 12.00 | 75.3 | 89.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 3.72 | 11.39 | 16.91 | 3.00 | 67.2 | 75.0 |

## GW8

- Train rows: 166350
- Bank: 0.30 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 72.99
- Actual score: 98.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.46) beats the best remaining Triple Captain opportunity (9.18).
- Transfer: Tijjani Reijnders -> Moisés Caicedo Corozo (projected gain 3.34, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.46) beats the best remaining Triple Captain opportunity (9.18).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.88 | 11.23 | 18.22 | 6.00 | 86.1 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.25 | 0.83 | 1.71 | 0.00 | 3.1 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.34 | 14.45 | 20.22 | 2.00 | 77.9 | 90.0 |
| Bench 2 | Bench | Omar Alderete | DEF | 17 | 4.0 | 3.69 | 11.81 | 16.12 | 6.00 | 67.5 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 3.97 | 11.58 | 14.87 | 17.00 | 77.8 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.59 | 10.98 | 21.33 | 4.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Trevoh Chalobah | DEF | 7 | 5.1 | 2.48 | 7.41 | 12.39 | 6.00 | 40.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 8.08 | 24.56 | 39.48 | 13.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.5 | 3.71 | 10.40 | 18.22 | 17.00 | 65.2 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 1.73 | 3.67 | 6.32 | 24.00 | 16.9 | 148.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.8 | 7.08 | 19.98 | 32.42 | 4.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.4 | 6.22 | 18.29 | 30.90 | 2.00 | 85.4 | 84.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 6.10 | 17.44 | 26.03 | 2.00 | 90.0 | 90.0 |
| XI | XI | Moisés Caicedo Corozo | MID | 7 | 5.8 | 4.80 | 13.86 | 20.16 | 1.00 | 90.0 | 45.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.06 | 12.85 | 20.42 | 4.00 | 82.3 | 85.0 |

## GW9

- Train rows: 167095
- Bank: 0.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: Junior Kroupi
- Vice captain: Erling Haaland
- Effective captain: Junior Kroupi
- Chip used: bench_boost
- Predicted score: 80.53
- Actual score: 62.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.74) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.74) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.99 | 11.46 | 18.50 | 6.00 | 86.3 | 90.0 |
| Bench 1 | Bench Boost | Antonín Kinský | GK | 18 | 3.9 | 0.15 | 0.72 | 1.55 | 0.00 | 2.5 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 5.03 | 14.75 | 21.23 | 5.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.16 | 13.26 | 21.50 | 4.00 | 90.0 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 3.92 | 11.28 | 17.20 | 2.00 | 83.4 | 90.0 |
| Bench 3 | Bench Boost | Trevoh Chalobah | DEF | 7 | 5.1 | 3.54 | 9.85 | 15.13 | 1.00 | 64.3 | 90.0 |
| Bench 4 | Bench Boost | Omar Alderete | DEF | 17 | 4.0 | 2.56 | 8.31 | 12.44 | 0.00 | 57.0 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.5 | 7.91 | 24.78 | 41.02 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Junior Kroupi | FWD | 4 | 4.5 | 9.32 | 13.22 | 18.76 | 12.00 | 180.0 | 136.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.5 | 4.30 | 13.07 | 22.33 | 2.00 | 79.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.9 | 6.84 | 19.30 | 29.77 | 3.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.3 | 5.88 | 17.07 | 28.53 | 6.00 | 76.7 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 5.07 | 14.92 | 22.06 | 2.00 | 83.8 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.52 | 13.28 | 20.37 | 3.00 | 77.8 | 77.0 |
| Bench 2 | Bench Boost | Moisés Caicedo Corozo | MID | 7 | 5.8 | 4.01 | 12.11 | 17.22 | 2.00 | 71.0 | 90.0 |