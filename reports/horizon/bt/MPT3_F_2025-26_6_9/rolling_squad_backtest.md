# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW5
- Simulated weeks: GW6-GW9
- Total predicted points: 283.01
- Total actual points: 291.00
- Average predicted points: 70.75
- Average actual points: 72.75
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
- Predicted score: 67.57
- Actual score: 57.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.80 | 11.25 | 19.00 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.68 | 1.45 | 2.96 | 0.00 | 7.2 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.23 | 14.00 | 19.37 | 7.00 | 90.0 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.2 | 3.43 | 13.78 | 20.07 | -3.00 | 90.0 | 52.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.26 | 11.24 | 17.88 | 2.00 | 78.9 | 90.0 |
| Bench 3 | Bench | Omar Alderete | DEF | 17 | 4.0 | 2.09 | 10.29 | 14.48 | 17.00 | 87.9 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.0 | 3.29 | 10.25 | 13.94 | 6.00 | 85.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.83 | 23.52 | 38.26 | 16.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 5.96 | 16.48 | 27.06 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 1.69 | 5.15 | 9.24 | 12.00 | 20.8 | 18.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 6.23 | 20.47 | 34.95 | 2.00 | 89.7 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.92 | 17.43 | 26.56 | 7.00 | 90.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 5.25 | 14.40 | 22.42 | 2.00 | 90.0 | 82.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.41 | 14.21 | 23.13 | 2.00 | 86.8 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.40 | 14.17 | 21.35 | 2.00 | 90.0 | 80.0 |

## GW7

- Train rows: 165607
- Bank: 0.10 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 63.29
- Actual score: 67.00
- Transfer: Trevoh Chalobah -> Marc Guéhi (projected gain 5.98, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.94 | 11.01 | 17.80 | 6.00 | 82.7 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.34 | 1.14 | 2.19 | 0.00 | 8.2 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.03 | 14.57 | 19.36 | 2.00 | 85.1 | 77.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.55 | 14.23 | 20.73 | 3.00 | 90.0 | 90.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.0 | 4.27 | 13.00 | 18.03 | 0.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Micky van de Ven | DEF | 18 | 4.7 | 3.58 | 10.67 | 16.81 | 2.00 | 79.9 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 3.59 | 9.88 | 13.51 | 3.00 | 77.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.72 | 24.33 | 38.10 | 8.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.08 | 13.67 | 22.19 | 2.00 | 72.1 | 73.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 2.94 | 8.88 | 12.17 | 0.00 | 35.5 | 0.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.5 | 6.23 | 18.82 | 31.69 | 2.00 | 85.7 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.7 | 6.24 | 18.35 | 27.57 | 18.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Iliman Ndiaye | MID | 9 | 6.5 | 3.47 | 12.29 | 18.01 | 7.00 | 68.0 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.25 | 12.12 | 18.95 | 12.00 | 73.9 | 89.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 3.67 | 11.00 | 16.46 | 3.00 | 66.5 | 75.0 |

## GW8

- Train rows: 166350
- Bank: 0.50 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 73.17
- Actual score: 83.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.46) beats the best remaining Triple Captain opportunity (9.19).
- Transfer: Tijjani Reijnders -> Moisés Caicedo Corozo (projected gain 4.41, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.46) beats the best remaining Triple Captain opportunity (9.19).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.84 | 11.05 | 18.06 | 6.00 | 85.5 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.41 | 1.06 | 1.89 | 0.00 | 7.7 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.32 | 14.15 | 19.76 | 2.00 | 77.7 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 3.94 | 11.34 | 14.44 | 17.00 | 77.2 | 90.0 |
| Bench 2 | Bench | Omar Alderete | DEF | 17 | 4.0 | 3.80 | 11.30 | 14.81 | 6.00 | 71.1 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.63 | 11.11 | 20.96 | 4.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Micky van de Ven | DEF | 18 | 4.7 | 3.62 | 9.85 | 16.55 | 0.00 | 83.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 8.09 | 24.19 | 39.17 | 13.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.60 | 12.55 | 22.31 | 2.00 | 76.8 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 1.80 | 4.56 | 7.19 | 24.00 | 20.1 | 148.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.8 | 7.16 | 20.14 | 32.75 | 4.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.4 | 6.05 | 18.24 | 30.55 | 2.00 | 83.0 | 84.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.53 | 15.82 | 23.71 | 2.00 | 90.0 | 90.0 |
| XI | XI | Moisés Caicedo Corozo | MID | 7 | 5.8 | 4.81 | 13.75 | 20.07 | 1.00 | 90.0 | 45.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.03 | 12.75 | 20.15 | 4.00 | 81.5 | 85.0 |

## GW9

- Train rows: 167095
- Bank: 0.40 -> 1.10
- Free transfers: 2 -> 2
- Captain: Junior Kroupi
- Vice captain: Erling Haaland
- Effective captain: Junior Kroupi
- Chip used: bench_boost
- Predicted score: 78.98
- Actual score: 84.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.01) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Moisés Caicedo Corozo -> Granit Xhaka (projected gain 0.01, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.01) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.95 | 11.30 | 18.43 | 6.00 | 85.4 | 90.0 |
| Bench 1 | Bench Boost | Antonín Kinský | GK | 18 | 3.9 | 0.30 | 0.97 | 1.77 | 0.00 | 7.1 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 5.03 | 14.80 | 21.24 | 5.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.17 | 13.25 | 21.31 | 4.00 | 90.0 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 3.89 | 11.12 | 16.94 | 2.00 | 82.8 | 90.0 |
| Bench 3 | Bench Boost | Micky van de Ven | DEF | 18 | 4.7 | 3.34 | 9.79 | 15.55 | 23.00 | 79.9 | 90.0 |
| Bench 4 | Bench Boost | Omar Alderete | DEF | 17 | 4.0 | 2.88 | 8.87 | 12.93 | 0.00 | 64.9 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.5 | 7.91 | 24.67 | 41.15 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Junior Kroupi | FWD | 4 | 4.5 | 8.59 | 14.49 | 18.88 | 12.00 | 155.1 | 136.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 4.60 | 13.12 | 21.65 | 2.00 | 78.3 | 84.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.9 | 6.81 | 19.38 | 30.06 | 3.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.3 | 5.41 | 16.40 | 28.67 | 6.00 | 73.3 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 5.06 | 14.75 | 21.82 | 2.00 | 83.3 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.46 | 13.21 | 20.27 | 3.00 | 76.7 | 77.0 |
| Bench 2 | Bench Boost | Granit Xhaka | MID | 17 | 5.1 | 4.00 | 11.36 | 18.73 | 2.00 | 86.3 | 90.0 |