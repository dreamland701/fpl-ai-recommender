# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW5
- Simulated weeks: GW6-GW9
- Total predicted points: 281.82
- Total actual points: 278.00
- Average predicted points: 70.45
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
- Predicted score: 66.81
- Actual score: 62.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.83 | 11.48 | 19.51 | 2.00 | 88.7 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.76 | 1.78 | 3.72 | 0.00 | 4.5 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.24 | 14.61 | 20.28 | 7.00 | 90.0 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.2 | 3.42 | 13.89 | 20.48 | -3.00 | 90.0 | 52.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.7 | 3.45 | 11.54 | 18.21 | 7.00 | 86.6 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.0 | 3.30 | 10.28 | 14.21 | 6.00 | 86.4 | 90.0 |
| Bench 3 | Bench | Omar Alderete | DEF | 17 | 4.0 | 2.08 | 10.20 | 14.44 | 17.00 | 88.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 9.02 | 25.15 | 40.97 | 16.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 5.82 | 15.84 | 26.21 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 1.69 | 3.70 | 6.69 | 12.00 | 18.4 | 18.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 6.27 | 19.94 | 34.51 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.91 | 18.17 | 27.87 | 7.00 | 90.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 5.14 | 14.37 | 22.55 | 2.00 | 90.0 | 82.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.36 | 14.33 | 21.78 | 2.00 | 90.0 | 80.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.34 | 14.18 | 23.31 | 2.00 | 86.1 | 90.0 |

## GW7

- Train rows: 165607
- Bank: 0.10 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 63.12
- Actual score: 71.00
- Transfer: Tijjani Reijnders -> Elliot Anderson (projected gain 1.51, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.96 | 11.37 | 18.37 | 6.00 | 79.8 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.42 | 1.50 | 2.85 | 0.00 | 5.5 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.02 | 15.14 | 20.30 | 2.00 | 85.4 | 77.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.7 | 4.49 | 14.42 | 20.98 | 3.00 | 90.0 | 90.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.0 | 4.27 | 13.06 | 18.17 | 0.00 | 90.0 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 3.59 | 9.85 | 13.58 | 3.00 | 78.3 | 90.0 |
| Bench 4 | Bench | Trevoh Chalobah | DEF | 7 | 5.2 | 2.37 | 8.25 | 12.37 | 0.00 | 47.4 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.86 | 26.02 | 40.51 | 8.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 3.92 | 12.59 | 20.69 | 2.00 | 71.4 | 73.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 2.97 | 5.78 | 9.08 | 0.00 | 33.2 | 0.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 6.28 | 18.78 | 32.00 | 2.00 | 87.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 6.18 | 18.50 | 27.65 | 18.00 | 90.0 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 3.46 | 12.52 | 18.50 | 7.00 | 67.2 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.20 | 12.12 | 19.02 | 12.00 | 73.5 | 89.0 |
| Bench 2 | Bench | Elliot Anderson | MID | 16 | 5.4 | 3.23 | 11.23 | 15.32 | 1.00 | 79.3 | 90.0 |

## GW8

- Train rows: 166350
- Bank: 0.40 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 73.11
- Actual score: 83.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.57) beats the best remaining Triple Captain opportunity (9.31).
- Transfer: Elliot Anderson -> Moisés Caicedo Corozo (projected gain 2.03, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.57) beats the best remaining Triple Captain opportunity (9.31).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.87 | 11.25 | 18.33 | 6.00 | 82.7 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.49 | 1.36 | 2.49 | 0.00 | 5.1 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.30 | 14.27 | 20.06 | 2.00 | 78.3 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 3.94 | 11.44 | 14.76 | 17.00 | 77.3 | 90.0 |
| Bench 2 | Bench | Omar Alderete | DEF | 17 | 4.0 | 3.80 | 11.44 | 15.29 | 6.00 | 71.8 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.59 | 11.10 | 21.13 | 4.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Trevoh Chalobah | DEF | 7 | 5.1 | 2.30 | 7.01 | 12.11 | 6.00 | 37.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 8.19 | 24.97 | 40.32 | 13.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.44 | 11.99 | 21.53 | 2.00 | 76.2 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 1.78 | 3.71 | 6.40 | 24.00 | 18.1 | 148.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.8 | 7.05 | 19.87 | 32.05 | 4.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.4 | 6.15 | 18.28 | 31.15 | 2.00 | 84.5 | 84.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.47 | 15.75 | 23.51 | 2.00 | 90.0 | 90.0 |
| XI | XI | Moisés Caicedo Corozo | MID | 7 | 5.8 | 4.71 | 13.46 | 19.64 | 1.00 | 89.9 | 45.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.00 | 12.66 | 20.18 | 4.00 | 80.8 | 85.0 |

## GW9

- Train rows: 167095
- Bank: 0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Junior Kroupi
- Vice captain: Erling Haaland
- Effective captain: Junior Kroupi
- Chip used: bench_boost
- Predicted score: 78.78
- Actual score: 62.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.11) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Moisés Caicedo Corozo -> Granit Xhaka (projected gain 0.01, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.11) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.97 | 11.42 | 18.53 | 6.00 | 82.5 | 90.0 |
| Bench 1 | Bench Boost | Antonín Kinský | GK | 18 | 3.9 | 0.39 | 1.23 | 2.31 | 0.00 | 4.4 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.97 | 14.49 | 20.88 | 5.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.13 | 13.14 | 21.28 | 4.00 | 90.0 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 3.88 | 11.16 | 17.07 | 2.00 | 83.1 | 90.0 |
| Bench 3 | Bench Boost | Trevoh Chalobah | DEF | 7 | 5.1 | 3.43 | 9.59 | 15.02 | 1.00 | 62.5 | 90.0 |
| Bench 4 | Bench Boost | Omar Alderete | DEF | 17 | 4.0 | 2.87 | 8.92 | 13.24 | 0.00 | 65.3 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.5 | 7.95 | 24.98 | 41.48 | 2.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 4.44 | 12.43 | 20.61 | 2.00 | 77.5 | 84.0 |
| Captain | Captain | Junior Kroupi | FWD | 4 | 4.5 | 8.57 | 12.32 | 17.38 | 12.00 | 153.4 | 136.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.9 | 6.69 | 18.82 | 29.12 | 3.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.3 | 5.55 | 16.57 | 29.54 | 6.00 | 74.6 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 5.03 | 14.75 | 21.92 | 2.00 | 82.3 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.42 | 13.02 | 20.04 | 3.00 | 76.5 | 77.0 |
| Bench 2 | Bench Boost | Granit Xhaka | MID | 17 | 5.1 | 3.93 | 11.04 | 18.24 | 2.00 | 84.8 | 90.0 |