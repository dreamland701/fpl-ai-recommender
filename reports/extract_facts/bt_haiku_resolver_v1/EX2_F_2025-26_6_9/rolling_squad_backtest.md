# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW5
- Simulated weeks: GW6-GW9
- Total predicted points: 285.45
- Total actual points: 279.00
- Average predicted points: 71.36
- Average actual points: 69.75
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
- Predicted score: 67.93
- Actual score: 62.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.82 | 11.45 | 19.28 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.52 | 1.28 | 2.86 | 0.00 | 2.7 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.17 | 14.45 | 20.05 | 7.00 | 90.0 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.2 | 3.29 | 13.88 | 20.46 | -3.00 | 90.0 | 52.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.7 | 3.79 | 12.65 | 19.89 | 7.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Omar Alderete | DEF | 17 | 4.0 | 1.97 | 10.24 | 14.48 | 17.00 | 85.3 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.0 | 3.20 | 10.24 | 14.15 | 6.00 | 84.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.93 | 24.13 | 40.39 | 16.00 | 90.0 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.85 | 18.38 | 30.51 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 1.60 | 3.64 | 6.48 | 12.00 | 17.7 | 18.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.5 | 6.35 | 20.04 | 34.33 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.85 | 18.14 | 27.67 | 7.00 | 90.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 5.19 | 14.68 | 23.01 | 2.00 | 90.0 | 82.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.45 | 14.48 | 23.65 | 2.00 | 87.4 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.32 | 14.44 | 21.92 | 2.00 | 90.0 | 80.0 |

## GW7

- Train rows: 165607
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 62.53
- Actual score: 72.00
- Transfer: João Pedro Junqueira de Jesus -> Jarrod Bowen (projected gain 1.78, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.97 | 11.35 | 18.22 | 6.00 | 83.3 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.17 | 0.96 | 2.03 | 0.00 | 3.4 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 4.90 | 14.93 | 20.10 | 2.00 | 82.1 | 77.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.7 | 4.48 | 14.54 | 21.14 | 3.00 | 90.0 | 90.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.0 | 4.22 | 13.03 | 18.07 | 0.00 | 90.0 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 3.59 | 9.88 | 13.58 | 3.00 | 77.7 | 90.0 |
| Bench 4 | Bench | Trevoh Chalobah | DEF | 7 | 5.2 | 1.45 | 6.07 | 9.30 | 0.00 | 29.8 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.68 | 25.41 | 39.30 | 8.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Jarrod Bowen | FWD | 19 | 7.7 | 3.47 | 11.07 | 17.99 | 2.00 | 82.0 | 90.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 3.27 | 6.00 | 9.32 | 0.00 | 44.8 | 0.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 6.38 | 18.90 | 31.89 | 2.00 | 88.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 6.11 | 18.48 | 27.71 | 18.00 | 90.0 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 3.49 | 12.70 | 18.67 | 7.00 | 68.2 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.32 | 12.40 | 19.35 | 12.00 | 75.3 | 89.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 3.72 | 11.39 | 16.91 | 3.00 | 67.2 | 75.0 |

## GW8

- Train rows: 166350
- Bank: 0.10 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 73.43
- Actual score: 83.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.46) beats the best remaining Triple Captain opportunity (9.19).
- Transfer: Tijjani Reijnders -> Moisés Caicedo Corozo (projected gain 3.34, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.46) beats the best remaining Triple Captain opportunity (9.19).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.87 | 11.22 | 18.21 | 6.00 | 86.0 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.25 | 0.82 | 1.71 | 0.00 | 3.0 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.33 | 14.44 | 20.20 | 2.00 | 77.9 | 90.0 |
| Bench 2 | Bench | Omar Alderete | DEF | 17 | 4.0 | 3.68 | 11.81 | 16.11 | 6.00 | 67.5 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 3.96 | 11.57 | 14.86 | 17.00 | 77.8 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.59 | 10.98 | 21.31 | 4.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Trevoh Chalobah | DEF | 7 | 5.1 | 2.48 | 7.42 | 12.37 | 6.00 | 40.3 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 8.09 | 24.57 | 39.48 | 13.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 4.23 | 11.03 | 19.40 | 2.00 | 86.2 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 1.72 | 3.67 | 6.32 | 24.00 | 16.9 | 148.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.8 | 7.09 | 19.99 | 32.41 | 4.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.4 | 6.21 | 18.27 | 30.88 | 2.00 | 85.4 | 84.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 6.03 | 17.31 | 25.91 | 2.00 | 90.0 | 90.0 |
| XI | XI | Moisés Caicedo Corozo | MID | 7 | 5.8 | 4.81 | 13.86 | 20.15 | 1.00 | 90.0 | 45.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.06 | 12.85 | 20.41 | 4.00 | 82.3 | 85.0 |

## GW9

- Train rows: 167095
- Bank: 0.00 -> 0.30
- Free transfers: 2 -> 2
- Captain: Junior Kroupi
- Vice captain: Erling Haaland
- Effective captain: Junior Kroupi
- Chip used: bench_boost
- Predicted score: 81.56
- Actual score: 62.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.74) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Jarrod Bowen -> Nick Woltemade (projected gain 3.07, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.74) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.99 | 11.45 | 18.49 | 6.00 | 86.3 | 90.0 |
| Bench 1 | Bench Boost | Antonín Kinský | GK | 18 | 3.9 | 0.15 | 0.72 | 1.55 | 0.00 | 2.5 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 5.03 | 14.74 | 21.21 | 5.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.16 | 13.25 | 21.48 | 4.00 | 90.0 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 3.92 | 11.28 | 17.19 | 2.00 | 83.4 | 90.0 |
| Bench 3 | Bench Boost | Trevoh Chalobah | DEF | 7 | 5.1 | 3.54 | 9.85 | 15.12 | 1.00 | 64.3 | 90.0 |
| Bench 4 | Bench Boost | Omar Alderete | DEF | 17 | 4.0 | 2.56 | 8.31 | 12.44 | 0.00 | 57.0 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.5 | 7.91 | 24.79 | 41.02 | 2.00 | 90.0 | 90.0 |
| XI | XI | Nick Woltemade | FWD | 15 | 7.4 | 5.20 | 15.15 | 22.51 | 2.00 | 79.6 | 85.0 |
| Captain | Captain | Junior Kroupi | FWD | 4 | 4.5 | 9.35 | 13.35 | 19.04 | 12.00 | 180.0 | 136.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.9 | 6.84 | 19.30 | 29.76 | 3.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.3 | 5.95 | 17.55 | 29.03 | 6.00 | 77.8 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 5.08 | 14.91 | 22.05 | 2.00 | 83.8 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.52 | 13.28 | 20.36 | 3.00 | 77.8 | 77.0 |
| Bench 2 | Bench Boost | Moisés Caicedo Corozo | MID | 7 | 5.8 | 4.01 | 12.10 | 17.20 | 2.00 | 71.0 | 90.0 |