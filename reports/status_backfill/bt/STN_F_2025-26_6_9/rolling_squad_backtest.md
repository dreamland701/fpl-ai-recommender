# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW5
- Simulated weeks: GW6-GW9
- Total predicted points: 281.88
- Total actual points: 280.00
- Average predicted points: 70.47
- Average actual points: 70.00
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
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 69.61
- Actual score: 57.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.90 | 11.42 | 19.37 | 2.00 | 93.8 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.69 | 1.52 | 3.24 | 0.00 | 6.7 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.58 | 14.60 | 20.35 | 7.00 | 98.5 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.2 | 3.47 | 13.90 | 20.57 | -3.00 | 99.0 | 52.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.31 | 11.39 | 18.40 | 2.00 | 78.9 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.0 | 3.27 | 10.24 | 14.23 | 6.00 | 85.3 | 90.0 |
| Bench 3 | Bench | Omar Alderete | DEF | 17 | 4.0 | 2.10 | 10.21 | 14.53 | 17.00 | 87.6 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 9.40 | 24.50 | 39.73 | 16.00 | 109.6 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 5.88 | 16.34 | 27.02 | 2.00 | 91.7 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 2.02 | 3.72 | 6.68 | 12.00 | 36.2 | 18.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.5 | 5.92 | 19.78 | 34.14 | 2.00 | 86.6 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.7 | 6.25 | 18.22 | 27.92 | 7.00 | 97.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 5.43 | 14.73 | 23.18 | 2.00 | 102.6 | 82.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.56 | 14.45 | 22.02 | 2.00 | 94.3 | 80.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.49 | 14.42 | 23.68 | 2.00 | 87.5 | 90.0 |

## GW7

- Train rows: 165607
- Bank: 0.10 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 63.75
- Actual score: 66.00
- Transfer: Trevoh Chalobah -> Marc Guéhi (projected gain 4.83, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 4.04 | 11.29 | 18.24 | 6.00 | 84.3 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.35 | 1.24 | 2.40 | 0.00 | 8.0 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.22 | 15.17 | 20.33 | 2.00 | 87.3 | 77.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.74 | 14.61 | 21.29 | 3.00 | 100.7 | 90.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.0 | 4.31 | 13.06 | 18.14 | 0.00 | 91.3 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 3.56 | 10.72 | 16.92 | 2.00 | 79.6 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.0 | 3.54 | 9.86 | 13.60 | 3.00 | 76.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 9.00 | 25.52 | 39.60 | 8.00 | 97.9 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 3.72 | 13.14 | 21.67 | 2.00 | 66.9 | 73.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 2.72 | 5.75 | 9.01 | 0.00 | 42.3 | 0.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.7 | 6.39 | 18.70 | 27.98 | 18.00 | 97.3 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.5 | 5.91 | 18.55 | 31.56 | 2.00 | 81.6 | 90.0 |
| Bench 3 | Bench | Iliman Ndiaye | MID | 9 | 6.5 | 3.44 | 12.57 | 18.60 | 7.00 | 67.1 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.24 | 12.29 | 19.31 | 12.00 | 73.7 | 89.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 3.62 | 11.25 | 16.83 | 3.00 | 65.5 | 75.0 |

## GW8

- Train rows: 166350
- Bank: 0.50 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 73.89
- Actual score: 83.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.63) beats the best remaining Triple Captain opportunity (9.37).
- Transfer: Tijjani Reijnders -> Moisés Caicedo Corozo (projected gain 3.33, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.63) beats the best remaining Triple Captain opportunity (9.37).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.86 | 11.17 | 18.20 | 6.00 | 86.0 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.41 | 1.09 | 2.05 | 0.00 | 7.3 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.38 | 14.36 | 20.23 | 2.00 | 78.3 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 3.96 | 11.46 | 14.83 | 17.00 | 76.6 | 90.0 |
| Bench 2 | Bench | Omar Alderete | DEF | 17 | 4.0 | 3.80 | 11.42 | 15.26 | 6.00 | 69.5 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.68 | 11.27 | 21.36 | 4.00 | 93.2 | 90.0 |
| Bench 3 | Bench | Micky van de Ven | DEF | 18 | 4.7 | 3.53 | 9.68 | 16.39 | 0.00 | 81.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 8.25 | 24.61 | 39.63 | 13.00 | 99.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.53 | 12.54 | 22.49 | 2.00 | 76.2 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 2.05 | 3.75 | 6.46 | 24.00 | 35.7 | 148.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.8 | 7.33 | 20.23 | 32.65 | 4.00 | 118.1 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.4 | 5.80 | 17.91 | 30.49 | 2.00 | 79.5 | 84.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.67 | 15.92 | 23.83 | 2.00 | 100.4 | 90.0 |
| XI | XI | Moisés Caicedo Corozo | MID | 7 | 5.8 | 4.92 | 13.79 | 20.23 | 1.00 | 92.0 | 45.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.01 | 12.76 | 20.37 | 4.00 | 81.1 | 85.0 |

## GW9

- Train rows: 167095
- Bank: 0.40 -> 1.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 74.64
- Actual score: 74.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.84) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Moisés Caicedo Corozo -> Granit Xhaka (projected gain 0.00, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.84) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.96 | 11.38 | 18.47 | 6.00 | 85.9 | 90.0 |
| Bench 1 | Bench Boost | Antonín Kinský | GK | 18 | 3.9 | 0.31 | 0.98 | 1.88 | 0.00 | 6.6 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.99 | 14.68 | 21.23 | 5.00 | 92.1 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.17 | 13.27 | 21.51 | 4.00 | 90.9 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 3.87 | 11.20 | 17.16 | 2.00 | 81.0 | 90.0 |
| Bench 3 | Bench Boost | Micky van de Ven | DEF | 18 | 4.7 | 3.22 | 9.63 | 15.39 | 23.00 | 77.9 | 90.0 |
| Bench 4 | Bench Boost | Omar Alderete | DEF | 17 | 4.0 | 2.84 | 8.93 | 13.25 | 0.00 | 63.0 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.5 | 7.98 | 24.82 | 41.16 | 2.00 | 106.8 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 4.41 | 12.99 | 21.61 | 2.00 | 75.9 | 84.0 |
| XI | XI | Junior Kroupi | FWD | 4 | 4.5 | 5.52 | 12.35 | 17.46 | 12.00 | 100.6 | 136.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.9 | 6.77 | 19.22 | 29.82 | 3.00 | 96.3 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.3 | 5.15 | 16.08 | 28.66 | 6.00 | 69.6 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 5.10 | 14.82 | 22.08 | 2.00 | 83.9 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.36 | 13.15 | 20.27 | 3.00 | 74.9 | 77.0 |
| Bench 2 | Bench Boost | Granit Xhaka | MID | 17 | 5.1 | 3.99 | 11.30 | 18.74 | 2.00 | 85.7 | 90.0 |