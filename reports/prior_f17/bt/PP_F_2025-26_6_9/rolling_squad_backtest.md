# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW5
- Simulated weeks: GW6-GW9
- Total predicted points: 282.52
- Total actual points: 271.00
- Average predicted points: 70.63
- Average actual points: 67.75
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
- Predicted score: 66.85
- Actual score: 62.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.88 | 11.68 | 19.78 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.9 | 0.22 | 0.79 | 2.19 | 0.00 | 7.0 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.16 | 14.25 | 19.71 | 7.00 | 88.7 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.2 | 3.42 | 13.72 | 20.23 | -3.00 | 90.0 | 52.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.7 | 3.56 | 11.87 | 18.71 | 7.00 | 89.0 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.0 | 3.19 | 9.85 | 13.56 | 6.00 | 82.1 | 90.0 |
| Bench 3 | Bench | Omar Alderete | DEF | 17 | 4.0 | 1.98 | 9.76 | 13.75 | 17.00 | 83.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.85 | 24.61 | 39.94 | 16.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 5.97 | 16.34 | 26.99 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 1.67 | 3.72 | 6.66 | 12.00 | 20.7 | 18.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 6.20 | 19.53 | 33.61 | 2.00 | 88.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 6.00 | 18.45 | 28.29 | 7.00 | 90.0 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.42 | 14.41 | 23.59 | 2.00 | 87.1 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.41 | 14.41 | 21.91 | 2.00 | 90.0 | 80.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 5.12 | 14.23 | 22.27 | 2.00 | 90.0 | 82.0 |

## GW7

- Train rows: 165607
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 63.42
- Actual score: 78.00
- Transfer: Tijjani Reijnders -> Moisés Caicedo Corozo (projected gain 0.92, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 4.00 | 11.52 | 18.62 | 6.00 | 86.3 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.9 | 0.03 | 0.48 | 1.12 | 0.00 | 5.5 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 4.97 | 14.80 | 19.57 | 2.00 | 81.3 | 77.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.7 | 4.60 | 14.73 | 21.46 | 3.00 | 90.0 | 90.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.0 | 4.15 | 12.61 | 17.29 | 0.00 | 86.2 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.0 | 3.49 | 9.48 | 12.88 | 3.00 | 73.4 | 90.0 |
| Bench 4 | Bench | Trevoh Chalobah | DEF | 7 | 5.2 | 2.33 | 8.01 | 11.85 | 0.00 | 45.6 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.76 | 25.61 | 39.76 | 8.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.08 | 13.08 | 21.52 | 2.00 | 71.5 | 73.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 2.93 | 5.78 | 9.06 | 0.00 | 35.8 | 0.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.7 | 6.28 | 18.79 | 28.11 | 18.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.5 | 6.20 | 18.28 | 31.00 | 2.00 | 84.3 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 3.50 | 12.59 | 18.58 | 7.00 | 69.3 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.28 | 12.37 | 19.43 | 12.00 | 75.4 | 89.0 |
| XI | XI | Moisés Caicedo Corozo | MID | 7 | 5.7 | 3.83 | 11.87 | 16.90 | 10.00 | 82.1 | 90.0 |

## GW8

- Train rows: 166350
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 73.35
- Actual score: 68.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.50) beats the best remaining Triple Captain opportunity (9.23).
- Transfer: Trevoh Chalobah -> Dan Burn (projected gain 0.92, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.50) beats the best remaining Triple Captain opportunity (9.23).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.91 | 11.41 | 18.63 | 6.00 | 89.2 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.9 | 0.16 | 0.53 | 1.16 | 0.00 | 6.5 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.26 | 13.96 | 19.47 | 2.00 | 73.6 | 90.0 |
| XI | XI | Dan Burn | DEF | 15 | 5.1 | 3.87 | 11.87 | 17.75 | 2.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.69 | 11.51 | 21.62 | 4.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.0 | 3.83 | 11.05 | 14.10 | 17.00 | 72.2 | 90.0 |
| Bench 3 | Bench | Omar Alderete | DEF | 17 | 4.0 | 3.69 | 10.99 | 14.47 | 6.00 | 66.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 8.12 | 24.73 | 39.87 | 13.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.58 | 12.42 | 22.26 | 2.00 | 75.7 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 1.81 | 3.81 | 6.57 | 24.00 | 21.2 | 148.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.8 | 7.18 | 20.30 | 32.73 | 4.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.4 | 6.03 | 17.68 | 30.01 | 2.00 | 81.6 | 84.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.56 | 16.01 | 23.94 | 2.00 | 90.0 | 90.0 |
| XI | XI | Moisés Caicedo Corozo | MID | 7 | 5.7 | 4.87 | 13.98 | 20.70 | 1.00 | 90.0 | 45.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.02 | 12.69 | 20.24 | 4.00 | 81.3 | 85.0 |

## GW9

- Train rows: 167095
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Junior Kroupi
- Vice captain: Erling Haaland
- Effective captain: Junior Kroupi
- Chip used: bench_boost
- Predicted score: 78.90
- Actual score: 63.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.01) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.01) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 4.00 | 11.54 | 18.75 | 6.00 | 88.5 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 3.9 | 0.08 | 0.43 | 1.04 | 0.00 | 6.2 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.96 | 14.32 | 20.47 | 5.00 | 89.2 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.22 | 13.44 | 21.76 | 4.00 | 90.0 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 3.78 | 10.76 | 16.33 | 2.00 | 77.2 | 90.0 |
| Bench 3 | Bench Boost | Dan Burn | DEF | 15 | 5.1 | 3.68 | 10.64 | 16.83 | 2.00 | 78.6 | 90.0 |
| Bench 4 | Bench Boost | Omar Alderete | DEF | 17 | 4.0 | 2.75 | 8.44 | 12.38 | 0.00 | 59.0 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.5 | 7.90 | 24.79 | 41.14 | 2.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 4.58 | 12.85 | 21.31 | 2.00 | 77.3 | 84.0 |
| Captain | Captain | Junior Kroupi | FWD | 4 | 4.5 | 8.58 | 12.41 | 17.53 | 12.00 | 155.5 | 136.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.9 | 6.84 | 19.29 | 29.97 | 3.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.3 | 5.39 | 15.91 | 28.33 | 6.00 | 72.6 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 5.05 | 14.76 | 21.96 | 2.00 | 83.1 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.50 | 13.27 | 20.45 | 3.00 | 78.5 | 77.0 |
| Bench 2 | Bench Boost | Moisés Caicedo Corozo | MID | 7 | 5.8 | 4.02 | 12.23 | 17.83 | 2.00 | 73.4 | 90.0 |