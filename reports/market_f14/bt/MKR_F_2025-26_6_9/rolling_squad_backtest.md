# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW5
- Simulated weeks: GW6-GW9
- Total predicted points: 280.04
- Total actual points: 295.00
- Average predicted points: 70.01
- Average actual points: 73.75
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
- Predicted score: 68.38
- Actual score: 57.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Gianluigi Donnarumma | GK | 13 | 5.6 | 4.25 | 12.13 | 19.70 | 2.00 | 88.7 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.27 | 0.92 | 2.56 | 0.00 | 4.9 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.19 | 14.17 | 20.45 | 7.00 | 90.0 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.2 | 3.45 | 13.68 | 20.82 | -3.00 | 90.0 | 52.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.12 | 11.37 | 18.74 | 2.00 | 80.9 | 90.0 |
| Bench 3 | Bench | Omar Alderete | DEF | 17 | 4.0 | 2.00 | 9.54 | 14.20 | 17.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Joe Rodon | DEF | 11 | 4.0 | 3.43 | 8.85 | 14.08 | 7.00 | 77.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 9.29 | 25.71 | 41.03 | 16.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 5.85 | 16.09 | 27.18 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 1.75 | 3.69 | 7.04 | 12.00 | 25.9 | 18.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.5 | 5.89 | 19.22 | 33.52 | 2.00 | 84.9 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.90 | 17.73 | 28.11 | 7.00 | 90.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 5.51 | 15.78 | 24.89 | 2.00 | 90.0 | 82.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.48 | 14.21 | 22.19 | 2.00 | 90.0 | 80.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.16 | 14.07 | 23.55 | 2.00 | 86.6 | 90.0 |

## GW7

- Train rows: 165607
- Bank: 0.10 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 60.13
- Actual score: 71.00
- Transfer: Trevoh Chalobah -> Marc Guéhi (projected gain 4.47, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Gianluigi Donnarumma | GK | 13 | 5.6 | 2.75 | 8.90 | 14.46 | 6.00 | 69.0 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.15 | 0.85 | 1.92 | 0.00 | 4.2 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.07 | 14.93 | 20.02 | 2.00 | 86.5 | 77.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.54 | 14.12 | 20.71 | 3.00 | 90.0 | 90.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.0 | 4.10 | 12.21 | 17.18 | 0.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Micky van de Ven | DEF | 18 | 4.7 | 3.46 | 10.25 | 16.38 | 2.00 | 80.8 | 90.0 |
| Bench 2 | Bench | Joe Rodon | DEF | 11 | 4.0 | 3.47 | 9.70 | 13.83 | 1.00 | 78.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.46 | 24.62 | 38.40 | 8.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 3.72 | 12.66 | 21.24 | 2.00 | 72.9 | 73.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 3.07 | 5.71 | 9.18 | 0.00 | 45.8 | 0.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.7 | 6.25 | 18.33 | 27.66 | 18.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.5 | 5.46 | 17.07 | 29.64 | 2.00 | 80.0 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 3.51 | 12.25 | 18.14 | 7.00 | 67.1 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.12 | 11.81 | 18.82 | 12.00 | 74.0 | 89.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 3.68 | 11.31 | 16.92 | 3.00 | 65.0 | 75.0 |

## GW8

- Train rows: 166350
- Bank: 0.50 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 71.14
- Actual score: 72.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.38) beats the best remaining Triple Captain opportunity (9.10).
- Transfer: Tijjani Reijnders -> Moisés Caicedo Corozo (projected gain 2.24, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.38) beats the best remaining Triple Captain opportunity (9.10).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Gianluigi Donnarumma | GK | 13 | 5.6 | 3.51 | 10.16 | 16.42 | 6.00 | 79.5 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.18 | 0.58 | 1.40 | 0.00 | 3.8 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.10 | 13.79 | 19.75 | 2.00 | 79.1 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.73 | 11.65 | 21.44 | 4.00 | 90.0 | 90.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.0 | 3.70 | 11.07 | 14.84 | 6.00 | 71.1 | 90.0 |
| Bench 3 | Bench | Joe Rodon | DEF | 11 | 4.0 | 3.45 | 10.50 | 13.46 | 1.00 | 75.4 | 90.0 |
| Bench 2 | Bench | Micky van de Ven | DEF | 18 | 4.7 | 3.64 | 9.71 | 16.49 | 0.00 | 83.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 8.00 | 24.08 | 38.57 | 13.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.48 | 12.05 | 21.96 | 2.00 | 78.1 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 1.47 | 3.42 | 6.23 | 24.00 | 22.3 | 148.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.8 | 6.90 | 19.62 | 32.05 | 4.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.4 | 5.61 | 17.21 | 29.39 | 2.00 | 76.2 | 84.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.47 | 15.72 | 23.66 | 2.00 | 90.0 | 90.0 |
| XI | XI | Moisés Caicedo Corozo | MID | 7 | 5.8 | 4.73 | 13.24 | 19.71 | 1.00 | 89.2 | 45.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 3.89 | 12.09 | 19.87 | 4.00 | 82.7 | 85.0 |

## GW9

- Train rows: 167095
- Bank: 0.40 -> 0.30
- Free transfers: 2 -> 2
- Captain: Junior Kroupi
- Vice captain: Erling Haaland
- Effective captain: Junior Kroupi
- Chip used: bench_boost
- Predicted score: 80.40
- Actual score: 95.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.93) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Gianluigi Donnarumma -> David Raya Martín (projected gain 2.26, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.93) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.7 | 4.19 | 11.90 | 19.28 | 6.00 | 86.3 | 90.0 |
| Bench 1 | Bench Boost | Antonín Kinský | GK | 18 | 3.9 | 0.09 | 0.48 | 1.24 | 0.00 | 3.2 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 5.16 | 14.82 | 21.44 | 5.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.13 | 12.83 | 21.11 | 4.00 | 90.0 | 90.0 |
| XI | XI | Joe Rodon | DEF | 11 | 4.0 | 3.57 | 9.33 | 13.72 | 13.00 | 71.9 | 90.0 |
| Bench 4 | Bench Boost | Omar Alderete | DEF | 17 | 4.0 | 3.03 | 9.29 | 14.25 | 0.00 | 77.0 | 0.0 |
| Bench 3 | Bench Boost | Micky van de Ven | DEF | 18 | 4.7 | 3.23 | 9.28 | 14.97 | 23.00 | 81.6 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.5 | 7.83 | 24.31 | 40.42 | 2.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 4.78 | 13.60 | 22.37 | 2.00 | 78.0 | 84.0 |
| Captain | Captain | Junior Kroupi | FWD | 4 | 4.5 | 9.60 | 13.29 | 18.14 | 12.00 | 161.0 | 136.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.9 | 6.74 | 18.61 | 29.23 | 3.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.3 | 5.06 | 15.41 | 27.58 | 6.00 | 66.1 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 5.05 | 14.58 | 21.94 | 2.00 | 83.3 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.27 | 12.61 | 19.66 | 3.00 | 77.4 | 77.0 |
| Bench 2 | Bench Boost | Moisés Caicedo Corozo | MID | 7 | 5.8 | 4.09 | 12.43 | 17.93 | 2.00 | 64.5 | 90.0 |