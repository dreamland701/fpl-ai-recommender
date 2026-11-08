# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW5
- Simulated weeks: GW6-GW9
- Total predicted points: 285.43
- Total actual points: 290.00
- Average predicted points: 71.36
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
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.85 | 11.62 | 19.86 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.54 | 1.27 | 3.03 | 0.00 | 4.5 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.30 | 14.77 | 21.11 | 7.00 | 90.0 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.2 | 3.49 | 13.86 | 21.01 | -3.00 | 90.0 | 52.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.34 | 11.60 | 19.22 | 2.00 | 80.4 | 90.0 |
| Bench 3 | Bench | Omar Alderete | DEF | 17 | 4.0 | 2.20 | 10.30 | 15.11 | 17.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.0 | 3.34 | 10.23 | 14.72 | 6.00 | 87.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 9.52 | 26.18 | 42.76 | 16.00 | 90.0 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.10 | 16.70 | 28.05 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 1.85 | 4.01 | 7.37 | 12.00 | 24.1 | 18.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.5 | 5.99 | 19.27 | 33.76 | 2.00 | 84.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 6.01 | 18.33 | 28.73 | 7.00 | 90.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 5.38 | 14.98 | 24.05 | 2.00 | 90.0 | 82.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.45 | 14.43 | 22.58 | 2.00 | 90.0 | 80.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.38 | 14.36 | 24.10 | 2.00 | 86.1 | 90.0 |

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
- Transfer: Trevoh Chalobah -> Marc Guéhi (projected gain 5.06, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.98 | 11.46 | 18.63 | 6.00 | 83.6 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.14 | 0.85 | 1.92 | 0.00 | 4.3 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.06 | 15.21 | 20.45 | 2.00 | 85.6 | 77.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.64 | 14.78 | 21.60 | 3.00 | 90.0 | 90.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.0 | 4.31 | 13.12 | 18.28 | 0.00 | 90.0 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 3.57 | 10.72 | 16.99 | 2.00 | 79.7 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.0 | 3.56 | 9.76 | 13.48 | 3.00 | 77.3 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.72 | 25.48 | 39.63 | 8.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.05 | 13.11 | 21.70 | 2.00 | 71.6 | 73.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 3.36 | 6.32 | 10.01 | 0.00 | 43.9 | 0.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.7 | 6.30 | 18.77 | 28.15 | 18.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.5 | 5.86 | 17.67 | 30.29 | 2.00 | 78.5 | 90.0 |
| Bench 3 | Bench | Iliman Ndiaye | MID | 9 | 6.5 | 3.42 | 12.34 | 18.29 | 7.00 | 66.9 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.20 | 12.15 | 19.16 | 12.00 | 72.9 | 89.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 3.62 | 11.07 | 16.62 | 3.00 | 65.5 | 75.0 |

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
- Transfer: Tijjani Reijnders -> Moisés Caicedo Corozo (projected gain 2.97, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.41) beats the best remaining Triple Captain opportunity (9.26).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.84 | 11.23 | 18.42 | 6.00 | 85.5 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.20 | 0.66 | 1.51 | 0.00 | 3.7 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.31 | 14.27 | 20.21 | 2.00 | 77.5 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.70 | 11.62 | 21.63 | 4.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Omar Alderete | DEF | 17 | 4.0 | 3.79 | 11.32 | 15.24 | 6.00 | 70.8 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 3.92 | 11.31 | 14.69 | 17.00 | 76.7 | 90.0 |
| Bench 3 | Bench | Micky van de Ven | DEF | 18 | 4.7 | 3.65 | 9.76 | 16.58 | 0.00 | 83.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 8.03 | 24.49 | 39.51 | 13.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.59 | 12.52 | 22.54 | 2.00 | 76.7 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 1.82 | 3.86 | 6.76 | 24.00 | 20.4 | 148.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.8 | 7.24 | 20.46 | 32.91 | 4.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.4 | 5.74 | 17.13 | 29.34 | 2.00 | 76.6 | 84.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.57 | 15.97 | 23.92 | 2.00 | 90.0 | 90.0 |
| XI | XI | Moisés Caicedo Corozo | MID | 7 | 5.8 | 4.73 | 13.45 | 19.91 | 1.00 | 89.0 | 45.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 3.96 | 12.56 | 20.14 | 4.00 | 80.2 | 85.0 |

## GW9

- Train rows: 167095
- Bank: 0.40 -> 1.10
- Free transfers: 2 -> 2
- Captain: Junior Kroupi
- Vice captain: Erling Haaland
- Effective captain: Junior Kroupi
- Chip used: bench_boost
- Predicted score: 80.36
- Actual score: 84.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.30) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Moisés Caicedo Corozo -> Granit Xhaka (projected gain 0.01, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.30) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 4.00 | 11.49 | 18.74 | 6.00 | 86.6 | 90.0 |
| Bench 1 | Bench Boost | Antonín Kinský | GK | 18 | 3.9 | 0.12 | 0.50 | 1.26 | 0.00 | 3.4 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 5.10 | 14.78 | 21.38 | 5.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.27 | 13.51 | 21.88 | 4.00 | 90.0 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 3.83 | 10.97 | 16.86 | 2.00 | 81.4 | 90.0 |
| Bench 3 | Bench Boost | Omar Alderete | DEF | 17 | 4.0 | 3.39 | 10.05 | 15.10 | 0.00 | 75.2 | 0.0 |
| Bench 4 | Bench Boost | Micky van de Ven | DEF | 18 | 4.7 | 3.38 | 9.69 | 15.50 | 23.00 | 80.6 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.5 | 7.89 | 24.77 | 41.14 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Junior Kroupi | FWD | 4 | 4.5 | 9.21 | 13.08 | 18.58 | 12.00 | 167.6 | 136.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 4.64 | 13.06 | 21.76 | 2.00 | 79.2 | 84.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.9 | 6.86 | 19.28 | 30.00 | 3.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.3 | 5.08 | 15.21 | 27.40 | 6.00 | 66.7 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 5.03 | 14.65 | 21.91 | 2.00 | 82.7 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.42 | 13.03 | 20.04 | 3.00 | 75.9 | 77.0 |
| Bench 2 | Bench Boost | Granit Xhaka | MID | 17 | 5.1 | 3.92 | 11.13 | 18.35 | 2.00 | 84.7 | 90.0 |