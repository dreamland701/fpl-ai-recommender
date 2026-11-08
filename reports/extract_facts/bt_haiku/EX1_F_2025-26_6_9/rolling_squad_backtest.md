# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW5
- Simulated weeks: GW6-GW9
- Total predicted points: 286.05
- Total actual points: 279.00
- Average predicted points: 71.51
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
- Predicted score: 68.01
- Actual score: 62.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.80 | 11.42 | 19.34 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.68 | 1.53 | 3.24 | 0.00 | 7.3 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.17 | 14.45 | 20.12 | 7.00 | 90.0 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.2 | 3.39 | 13.89 | 20.54 | -3.00 | 90.0 | 52.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.7 | 3.81 | 12.52 | 19.73 | 7.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.0 | 3.26 | 10.24 | 14.21 | 6.00 | 85.5 | 90.0 |
| Bench 3 | Bench | Omar Alderete | DEF | 17 | 4.0 | 2.06 | 10.23 | 14.52 | 17.00 | 87.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.90 | 24.43 | 40.71 | 16.00 | 90.0 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.84 | 18.45 | 30.70 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 1.72 | 3.76 | 6.72 | 12.00 | 21.3 | 18.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.5 | 6.34 | 20.04 | 34.43 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.87 | 18.13 | 27.76 | 7.00 | 90.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 5.20 | 14.65 | 23.07 | 2.00 | 90.0 | 82.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.43 | 14.47 | 23.74 | 2.00 | 87.0 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.36 | 14.41 | 21.96 | 2.00 | 90.0 | 80.0 |

## GW7

- Train rows: 165607
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 62.72
- Actual score: 72.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.94 | 11.31 | 18.25 | 6.00 | 82.6 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.33 | 1.23 | 2.39 | 0.00 | 8.1 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 4.99 | 15.11 | 20.22 | 2.00 | 84.4 | 77.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.7 | 4.50 | 14.54 | 21.16 | 3.00 | 90.0 | 90.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.0 | 4.24 | 13.04 | 18.10 | 0.00 | 90.0 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 3.59 | 9.88 | 13.58 | 3.00 | 77.9 | 90.0 |
| Bench 4 | Bench | Trevoh Chalobah | DEF | 7 | 5.2 | 1.71 | 6.64 | 10.03 | 0.00 | 35.9 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.69 | 25.45 | 39.39 | 8.00 | 90.0 | 90.0 |
| Bench 2 | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 3.30 | 10.62 | 18.31 | 2.00 | 59.7 | 73.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 2.99 | 5.82 | 9.09 | 0.00 | 36.3 | 0.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 6.38 | 18.91 | 31.97 | 2.00 | 87.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 6.21 | 18.65 | 27.82 | 18.00 | 90.0 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 3.49 | 12.66 | 18.64 | 7.00 | 68.1 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.28 | 12.37 | 19.33 | 12.00 | 74.3 | 89.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 3.71 | 11.36 | 16.90 | 3.00 | 66.9 | 75.0 |

## GW8

- Train rows: 166350
- Bank: 0.10 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 73.84
- Actual score: 83.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.46) beats the best remaining Triple Captain opportunity (9.19).
- Transfer: Tijjani Reijnders -> Moisés Caicedo Corozo (projected gain 3.24, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.46) beats the best remaining Triple Captain opportunity (9.19).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.85 | 11.20 | 18.24 | 6.00 | 85.5 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.41 | 1.09 | 2.05 | 0.00 | 7.7 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.32 | 14.38 | 20.21 | 2.00 | 77.6 | 90.0 |
| Bench 2 | Bench | Omar Alderete | DEF | 17 | 4.0 | 3.82 | 11.49 | 15.33 | 6.00 | 71.5 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 3.95 | 11.49 | 14.84 | 17.00 | 77.3 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.60 | 11.18 | 21.33 | 4.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Trevoh Chalobah | DEF | 7 | 5.1 | 2.36 | 7.21 | 12.27 | 6.00 | 37.3 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 8.08 | 24.59 | 39.54 | 13.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.66 | 12.70 | 22.69 | 2.00 | 77.6 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 1.84 | 3.80 | 6.53 | 24.00 | 20.6 | 148.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.8 | 7.10 | 20.08 | 32.45 | 4.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.4 | 6.20 | 18.25 | 30.92 | 2.00 | 85.0 | 84.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 6.09 | 17.40 | 26.02 | 2.00 | 90.0 | 90.0 |
| XI | XI | Moisés Caicedo Corozo | MID | 7 | 5.8 | 4.78 | 13.77 | 20.13 | 1.00 | 90.0 | 45.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.04 | 12.81 | 20.41 | 4.00 | 81.7 | 85.0 |

## GW9

- Train rows: 167095
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Junior Kroupi
- Vice captain: Erling Haaland
- Effective captain: Junior Kroupi
- Chip used: bench_boost
- Predicted score: 81.47
- Actual score: 62.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.09) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: João Pedro Junqueira de Jesus -> Nick Woltemade (projected gain 3.68, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.09) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.96 | 11.41 | 18.50 | 6.00 | 85.5 | 90.0 |
| Bench 1 | Bench Boost | Antonín Kinský | GK | 18 | 3.9 | 0.30 | 0.98 | 1.88 | 0.00 | 7.1 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 5.03 | 14.70 | 21.22 | 5.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.16 | 13.26 | 21.49 | 4.00 | 90.0 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 3.91 | 11.24 | 17.21 | 2.00 | 83.1 | 90.0 |
| Bench 3 | Bench Boost | Trevoh Chalobah | DEF | 7 | 5.1 | 3.46 | 9.66 | 15.07 | 1.00 | 62.1 | 90.0 |
| Bench 4 | Bench Boost | Omar Alderete | DEF | 17 | 4.0 | 2.92 | 9.04 | 13.38 | 0.00 | 65.7 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.5 | 7.90 | 24.79 | 41.07 | 2.00 | 90.0 | 90.0 |
| XI | XI | Nick Woltemade | FWD | 15 | 7.4 | 5.19 | 15.15 | 22.55 | 2.00 | 79.5 | 85.0 |
| Captain | Captain | Junior Kroupi | FWD | 4 | 4.5 | 9.23 | 13.14 | 18.70 | 12.00 | 179.1 | 136.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.9 | 6.82 | 19.24 | 29.78 | 3.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.3 | 5.90 | 17.15 | 28.71 | 6.00 | 77.3 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 5.06 | 14.84 | 22.06 | 2.00 | 83.4 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.49 | 13.23 | 20.34 | 3.00 | 77.0 | 77.0 |
| Bench 2 | Bench Boost | Moisés Caicedo Corozo | MID | 7 | 5.8 | 3.92 | 11.91 | 17.13 | 2.00 | 68.6 | 90.0 |