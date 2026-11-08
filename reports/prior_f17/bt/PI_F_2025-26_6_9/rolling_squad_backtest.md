# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW5
- Simulated weeks: GW6-GW9
- Total predicted points: 281.54
- Total actual points: 278.00
- Average predicted points: 70.39
- Average actual points: 69.50
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
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 66.67
- Actual score: 62.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.83 | 11.48 | 19.45 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.71 | 1.66 | 3.51 | 0.00 | 7.6 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.21 | 14.58 | 20.31 | 7.00 | 90.0 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.2 | 3.41 | 13.86 | 20.50 | -3.00 | 90.0 | 52.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.7 | 3.50 | 11.68 | 18.44 | 7.00 | 85.3 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.0 | 3.29 | 10.21 | 14.15 | 6.00 | 85.5 | 90.0 |
| Bench 3 | Bench | Omar Alderete | DEF | 17 | 4.0 | 2.07 | 10.15 | 14.38 | 17.00 | 87.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.72 | 24.20 | 39.30 | 16.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 5.77 | 15.79 | 26.18 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 1.63 | 3.64 | 6.58 | 12.00 | 21.3 | 18.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 6.50 | 20.57 | 35.45 | 2.00 | 88.5 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.99 | 18.40 | 28.23 | 7.00 | 90.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 5.27 | 14.77 | 23.23 | 2.00 | 90.0 | 82.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.39 | 14.42 | 21.98 | 2.00 | 90.0 | 80.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.37 | 14.31 | 23.54 | 2.00 | 87.0 | 90.0 |

## GW7

- Train rows: 165607
- Bank: 0.10 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 63.08
- Actual score: 71.00
- Transfer: Tijjani Reijnders -> Elliot Anderson (projected gain 1.23, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.97 | 11.37 | 18.36 | 6.00 | 82.2 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.37 | 1.39 | 2.69 | 0.00 | 8.6 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.02 | 15.17 | 20.38 | 2.00 | 85.5 | 77.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.7 | 4.55 | 14.60 | 21.26 | 3.00 | 90.0 | 90.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.0 | 4.26 | 13.02 | 18.05 | 0.00 | 90.0 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 3.59 | 9.83 | 13.54 | 3.00 | 77.5 | 90.0 |
| Bench 4 | Bench | Trevoh Chalobah | DEF | 7 | 5.2 | 2.33 | 8.15 | 12.18 | 0.00 | 46.6 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.64 | 25.29 | 39.28 | 8.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 3.91 | 12.68 | 20.96 | 2.00 | 73.0 | 73.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 2.85 | 5.63 | 8.84 | 0.00 | 36.2 | 0.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 6.52 | 19.40 | 32.95 | 2.00 | 84.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 6.30 | 18.84 | 28.21 | 18.00 | 90.0 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 3.48 | 12.59 | 18.64 | 7.00 | 67.9 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.20 | 12.17 | 19.14 | 12.00 | 74.1 | 89.0 |
| Bench 2 | Bench | Elliot Anderson | MID | 16 | 5.4 | 3.27 | 11.40 | 15.64 | 1.00 | 80.5 | 90.0 |

## GW8

- Train rows: 166350
- Bank: 0.40 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 72.96
- Actual score: 83.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.34) beats the best remaining Triple Captain opportunity (9.21).
- Transfer: Elliot Anderson -> Moisés Caicedo Corozo (projected gain 3.52, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.34) beats the best remaining Triple Captain opportunity (9.21).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.87 | 11.24 | 18.31 | 6.00 | 85.0 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.45 | 1.25 | 2.36 | 0.00 | 8.2 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.28 | 14.28 | 20.14 | 2.00 | 78.3 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 3.94 | 11.44 | 14.76 | 17.00 | 76.8 | 90.0 |
| Bench 2 | Bench | Omar Alderete | DEF | 17 | 4.0 | 3.81 | 11.40 | 15.20 | 6.00 | 70.7 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.63 | 11.23 | 21.34 | 4.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Trevoh Chalobah | DEF | 7 | 5.1 | 2.29 | 6.97 | 12.05 | 6.00 | 36.3 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 7.97 | 24.28 | 39.15 | 13.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.47 | 12.18 | 21.94 | 2.00 | 77.5 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 1.72 | 3.64 | 6.29 | 24.00 | 20.8 | 148.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.8 | 7.20 | 20.31 | 32.79 | 4.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.4 | 6.33 | 18.74 | 31.83 | 2.00 | 81.7 | 84.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.48 | 15.77 | 23.58 | 2.00 | 90.0 | 90.0 |
| XI | XI | Moisés Caicedo Corozo | MID | 7 | 5.8 | 4.84 | 13.86 | 20.33 | 1.00 | 90.0 | 45.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.01 | 12.73 | 20.33 | 4.00 | 81.5 | 85.0 |

## GW9

- Train rows: 167095
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Junior Kroupi
- Vice captain: Erling Haaland
- Effective captain: Junior Kroupi
- Chip used: bench_boost
- Predicted score: 78.84
- Actual score: 62.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.09) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.09) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.98 | 11.44 | 18.55 | 6.00 | 85.0 | 90.0 |
| Bench 1 | Bench Boost | Antonín Kinský | GK | 18 | 3.9 | 0.35 | 1.15 | 2.21 | 0.00 | 7.5 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.96 | 14.52 | 20.99 | 5.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.15 | 13.21 | 21.40 | 4.00 | 90.0 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 3.90 | 11.19 | 17.10 | 2.00 | 82.3 | 90.0 |
| Bench 3 | Bench Boost | Trevoh Chalobah | DEF | 7 | 5.1 | 3.41 | 9.56 | 14.96 | 1.00 | 61.6 | 90.0 |
| Bench 4 | Bench Boost | Omar Alderete | DEF | 17 | 4.0 | 2.88 | 8.89 | 13.14 | 0.00 | 64.4 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.5 | 7.76 | 24.42 | 40.57 | 2.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 4.50 | 12.73 | 21.20 | 2.00 | 78.7 | 84.0 |
| Captain | Captain | Junior Kroupi | FWD | 4 | 4.5 | 8.49 | 12.20 | 17.20 | 12.00 | 155.6 | 136.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.9 | 6.85 | 19.31 | 29.93 | 3.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.3 | 5.68 | 16.90 | 30.00 | 6.00 | 72.1 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 5.05 | 14.81 | 22.06 | 2.00 | 83.3 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.41 | 13.01 | 20.05 | 3.00 | 76.9 | 77.0 |
| Bench 2 | Bench Boost | Moisés Caicedo Corozo | MID | 7 | 5.8 | 3.97 | 12.02 | 17.32 | 2.00 | 68.0 | 90.0 |