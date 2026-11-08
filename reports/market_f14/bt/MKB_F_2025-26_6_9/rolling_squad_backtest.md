# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW5
- Simulated weeks: GW6-GW9
- Total predicted points: 284.31
- Total actual points: 290.00
- Average predicted points: 71.08
- Average actual points: 72.50
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
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Erling Haaland
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 68.97
- Actual score: 57.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.83 | 11.54 | 19.73 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 4.0 | 0.06 | 0.52 | 1.95 | 0.00 | 4.7 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.29 | 14.73 | 21.11 | 7.00 | 90.0 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.2 | 3.49 | 13.78 | 20.93 | -3.00 | 90.0 | 52.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.25 | 11.35 | 18.81 | 2.00 | 80.9 | 90.0 |
| Bench 3 | Bench | Omar Alderete | DEF | 17 | 4.0 | 2.15 | 10.10 | 14.89 | 17.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.0 | 3.28 | 10.02 | 14.49 | 6.00 | 87.3 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 9.50 | 26.12 | 42.65 | 16.00 | 90.0 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.02 | 16.54 | 27.80 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 1.96 | 4.14 | 7.53 | 12.00 | 23.3 | 18.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.5 | 5.92 | 19.10 | 33.48 | 2.00 | 85.1 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 6.00 | 18.29 | 28.66 | 7.00 | 90.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 5.43 | 15.05 | 24.14 | 2.00 | 90.0 | 82.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.45 | 14.35 | 22.44 | 2.00 | 90.0 | 80.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.27 | 14.05 | 23.60 | 2.00 | 86.6 | 90.0 |

## GW7

- Train rows: 165607
- Bank: 0.00 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 62.70
- Actual score: 66.00
- Transfer: Trevoh Chalobah -> Marc Guéhi (projected gain 5.02, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 4.01 | 11.50 | 18.68 | 6.00 | 83.7 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 4.0 | 0.02 | 0.27 | 0.96 | 0.00 | 3.6 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.06 | 15.19 | 20.38 | 2.00 | 85.6 | 77.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.61 | 14.67 | 21.45 | 3.00 | 90.0 | 90.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.0 | 4.30 | 13.06 | 18.19 | 0.00 | 90.0 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 3.54 | 10.65 | 16.91 | 2.00 | 79.7 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.0 | 3.53 | 9.69 | 13.39 | 3.00 | 77.6 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.70 | 25.46 | 39.60 | 8.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 3.95 | 12.87 | 21.40 | 2.00 | 72.2 | 73.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 3.44 | 6.39 | 10.08 | 0.00 | 43.1 | 0.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.7 | 6.27 | 18.67 | 27.99 | 18.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.5 | 5.74 | 17.41 | 29.95 | 2.00 | 79.0 | 90.0 |
| Bench 4 | Bench | Iliman Ndiaye | MID | 9 | 6.5 | 3.42 | 12.29 | 18.20 | 7.00 | 66.7 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.15 | 12.03 | 19.01 | 12.00 | 72.9 | 89.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 3.67 | 11.19 | 16.78 | 3.00 | 65.4 | 75.0 |

## GW8

- Train rows: 166350
- Bank: 0.40 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 72.37
- Actual score: 83.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.40) beats the best remaining Triple Captain opportunity (9.15).
- Transfer: Tijjani Reijnders -> Moisés Caicedo Corozo (projected gain 2.88, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.40) beats the best remaining Triple Captain opportunity (9.15).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.91 | 11.37 | 18.57 | 6.00 | 85.1 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 4.0 | 0.07 | 0.30 | 0.96 | 0.00 | 2.7 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.27 | 14.15 | 20.06 | 2.00 | 77.8 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.69 | 11.63 | 21.52 | 4.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Omar Alderete | DEF | 17 | 4.0 | 3.73 | 11.11 | 14.94 | 6.00 | 70.8 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 3.84 | 11.06 | 14.33 | 17.00 | 76.9 | 90.0 |
| Bench 3 | Bench | Micky van de Ven | DEF | 18 | 4.7 | 3.62 | 9.69 | 16.48 | 0.00 | 83.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 8.03 | 24.46 | 39.45 | 13.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.54 | 12.40 | 22.36 | 2.00 | 76.8 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 1.71 | 3.76 | 6.65 | 24.00 | 20.9 | 148.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.8 | 7.15 | 20.29 | 32.66 | 4.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.4 | 5.67 | 16.99 | 29.15 | 2.00 | 77.1 | 84.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.51 | 15.85 | 23.76 | 2.00 | 90.0 | 90.0 |
| XI | XI | Moisés Caicedo Corozo | MID | 7 | 5.8 | 4.74 | 13.46 | 19.95 | 1.00 | 89.0 | 45.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 3.96 | 12.54 | 20.12 | 4.00 | 80.1 | 85.0 |

## GW9

- Train rows: 167095
- Bank: 0.30 -> 0.30
- Free transfers: 2 -> 2
- Captain: Junior Kroupi
- Vice captain: Erling Haaland
- Effective captain: Junior Kroupi
- Chip used: bench_boost
- Predicted score: 80.28
- Actual score: 84.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.40) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.40) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 4.05 | 11.57 | 18.83 | 6.00 | 86.4 | 90.0 |
| Bench 1 | Bench Boost | Daniel Bentley | GK | 20 | 4.0 | 0.34 | 0.35 | 0.83 | 0.00 | 2.9 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 5.06 | 14.66 | 21.22 | 5.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.25 | 13.45 | 21.77 | 4.00 | 90.0 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 3.77 | 10.80 | 16.63 | 2.00 | 81.9 | 90.0 |
| Bench 3 | Bench Boost | Omar Alderete | DEF | 17 | 4.0 | 3.34 | 9.89 | 14.90 | 0.00 | 75.6 | 0.0 |
| Bench 4 | Bench Boost | Micky van de Ven | DEF | 18 | 4.7 | 3.32 | 9.55 | 15.32 | 23.00 | 80.8 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.5 | 7.87 | 24.74 | 41.07 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Junior Kroupi | FWD | 4 | 4.5 | 9.24 | 13.09 | 18.60 | 12.00 | 167.3 | 136.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 4.65 | 13.05 | 21.72 | 2.00 | 79.2 | 84.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.9 | 6.81 | 19.13 | 29.78 | 3.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.3 | 5.06 | 15.20 | 27.37 | 6.00 | 66.8 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 5.03 | 14.64 | 21.92 | 2.00 | 82.6 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.36 | 12.88 | 19.86 | 3.00 | 76.1 | 77.0 |
| Bench 2 | Bench Boost | Moisés Caicedo Corozo | MID | 7 | 5.8 | 3.91 | 11.70 | 17.00 | 2.00 | 66.6 | 90.0 |