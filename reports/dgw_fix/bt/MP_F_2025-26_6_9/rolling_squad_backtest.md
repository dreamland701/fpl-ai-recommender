# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW5
- Simulated weeks: GW6-GW9
- Total predicted points: 285.48
- Total actual points: 296.00
- Average predicted points: 71.37
- Average actual points: 74.00
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
- Predicted score: 69.35
- Actual score: 57.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.85 | 11.46 | 19.54 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.54 | 1.18 | 2.74 | 0.00 | 4.5 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.30 | 14.20 | 20.21 | 7.00 | 90.0 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.2 | 3.49 | 13.74 | 20.54 | -3.00 | 90.0 | 52.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.34 | 11.47 | 18.79 | 2.00 | 80.4 | 90.0 |
| Bench 3 | Bench | Omar Alderete | DEF | 17 | 4.0 | 2.20 | 10.38 | 15.10 | 17.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.0 | 3.34 | 10.23 | 14.48 | 6.00 | 87.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 9.52 | 25.34 | 41.58 | 16.00 | 90.0 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.10 | 16.86 | 28.18 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 1.85 | 5.76 | 10.53 | 12.00 | 24.1 | 18.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.5 | 5.99 | 19.92 | 34.54 | 2.00 | 84.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 6.01 | 17.56 | 27.46 | 7.00 | 90.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 5.38 | 14.67 | 23.37 | 2.00 | 90.0 | 82.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.45 | 14.16 | 21.98 | 2.00 | 90.0 | 80.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.38 | 14.16 | 23.61 | 2.00 | 86.1 | 90.0 |

## GW7

- Train rows: 165607
- Bank: 0.10 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 63.04
- Actual score: 66.00
- Transfer: Trevoh Chalobah -> Marc Guéhi (projected gain 4.69, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.98 | 11.20 | 18.24 | 6.00 | 83.6 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.14 | 0.72 | 1.68 | 0.00 | 4.3 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.06 | 14.63 | 19.50 | 2.00 | 85.6 | 77.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.64 | 14.41 | 21.07 | 3.00 | 90.0 | 90.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.0 | 4.31 | 13.06 | 18.18 | 0.00 | 90.0 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 3.57 | 10.67 | 16.88 | 2.00 | 79.7 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.0 | 3.56 | 9.76 | 13.38 | 3.00 | 77.3 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.72 | 24.31 | 38.16 | 8.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.05 | 13.65 | 22.23 | 2.00 | 71.6 | 73.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 3.36 | 10.08 | 13.88 | 0.00 | 43.9 | 0.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.7 | 6.30 | 18.42 | 27.75 | 18.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.5 | 5.86 | 17.90 | 30.34 | 2.00 | 78.5 | 90.0 |
| Bench 3 | Bench | Iliman Ndiaye | MID | 9 | 6.5 | 3.42 | 12.05 | 17.69 | 7.00 | 66.9 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.20 | 11.98 | 18.80 | 12.00 | 72.9 | 89.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 3.62 | 10.81 | 16.24 | 3.00 | 65.5 | 75.0 |

## GW8

- Train rows: 166350
- Bank: 0.50 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 72.69
- Actual score: 83.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.41) beats the best remaining Triple Captain opportunity (9.26).
- Transfer: Tijjani Reijnders -> Moisés Caicedo Corozo (projected gain 2.90, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.41) beats the best remaining Triple Captain opportunity (9.26).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.84 | 11.11 | 18.30 | 6.00 | 85.5 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.20 | 0.59 | 1.30 | 0.00 | 3.7 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.31 | 14.05 | 19.73 | 2.00 | 77.5 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.70 | 11.48 | 21.25 | 4.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Omar Alderete | DEF | 17 | 4.0 | 3.79 | 11.21 | 14.79 | 6.00 | 70.8 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 3.92 | 11.20 | 14.30 | 17.00 | 76.7 | 90.0 |
| Bench 3 | Bench | Micky van de Ven | DEF | 18 | 4.7 | 3.65 | 9.93 | 16.75 | 0.00 | 83.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 8.03 | 24.06 | 39.06 | 13.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.59 | 12.54 | 22.38 | 2.00 | 76.7 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 1.82 | 4.71 | 7.59 | 24.00 | 20.4 | 148.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.8 | 7.24 | 20.38 | 33.02 | 4.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.4 | 5.74 | 17.42 | 29.33 | 2.00 | 76.6 | 84.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.57 | 15.88 | 23.81 | 2.00 | 90.0 | 90.0 |
| XI | XI | Moisés Caicedo Corozo | MID | 7 | 5.8 | 4.73 | 13.38 | 19.72 | 1.00 | 89.0 | 45.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 3.96 | 12.53 | 19.90 | 4.00 | 80.2 | 85.0 |

## GW9

- Train rows: 167095
- Bank: 0.40 -> 0.80
- Free transfers: 2 -> 2
- Captain: Junior Kroupi
- Vice captain: Erling Haaland
- Effective captain: Junior Kroupi
- Chip used: bench_boost
- Predicted score: 80.41
- Actual score: 90.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.35) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Moisés Caicedo Corozo -> Marshall Munetsi (projected gain 0.02, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.35) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 4.00 | 11.42 | 18.73 | 6.00 | 86.6 | 90.0 |
| Bench 1 | Bench Boost | Antonín Kinský | GK | 18 | 3.9 | 0.12 | 0.46 | 1.10 | 0.00 | 3.4 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 5.10 | 14.90 | 21.39 | 5.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.27 | 13.51 | 21.70 | 4.00 | 90.0 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 3.83 | 10.87 | 16.62 | 2.00 | 81.4 | 90.0 |
| Bench 3 | Bench Boost | Omar Alderete | DEF | 17 | 4.0 | 3.39 | 10.09 | 14.95 | 0.00 | 75.2 | 0.0 |
| Bench 4 | Bench Boost | Micky van de Ven | DEF | 18 | 4.7 | 3.38 | 9.86 | 15.66 | 23.00 | 80.6 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.5 | 7.89 | 24.61 | 41.14 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Junior Kroupi | FWD | 4 | 4.5 | 9.21 | 15.53 | 20.35 | 12.00 | 167.6 | 136.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 4.64 | 13.20 | 21.83 | 2.00 | 79.2 | 84.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.9 | 6.86 | 19.43 | 30.24 | 3.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.3 | 5.08 | 15.48 | 27.33 | 6.00 | 66.7 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 5.03 | 14.56 | 21.64 | 2.00 | 82.7 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.42 | 13.09 | 20.03 | 3.00 | 75.9 | 77.0 |
| Bench 2 | Bench Boost | Marshall Munetsi | MID | 20 | 5.4 | 3.97 | 10.77 | 16.07 | 8.00 | 80.3 | 83.0 |