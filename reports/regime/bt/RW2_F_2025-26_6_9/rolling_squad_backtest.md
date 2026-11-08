# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW5
- Simulated weeks: GW6-GW9
- Total predicted points: 282.26
- Total actual points: 278.00
- Average predicted points: 70.56
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
- Predicted score: 67.17
- Actual score: 62.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.84 | 11.45 | 19.58 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.9 | 0.21 | 0.65 | 2.15 | 0.00 | 7.5 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.34 | 14.86 | 21.11 | 7.00 | 90.0 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.2 | 3.48 | 14.06 | 21.03 | -3.00 | 90.0 | 52.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.7 | 3.53 | 11.91 | 18.95 | 7.00 | 87.4 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.0 | 3.32 | 10.31 | 14.58 | 6.00 | 86.8 | 90.0 |
| Bench 3 | Bench | Omar Alderete | DEF | 17 | 4.0 | 2.09 | 10.23 | 14.91 | 17.00 | 88.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.94 | 24.39 | 39.76 | 16.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 5.79 | 15.90 | 26.40 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 1.56 | 3.69 | 6.98 | 12.00 | 21.7 | 18.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 6.21 | 19.92 | 34.25 | 2.00 | 87.1 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 6.07 | 18.33 | 28.36 | 7.00 | 90.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 5.23 | 14.58 | 23.16 | 2.00 | 90.0 | 82.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.42 | 14.47 | 22.30 | 2.00 | 90.0 | 80.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.37 | 14.18 | 23.47 | 2.00 | 87.3 | 90.0 |

## GW7

- Train rows: 165607
- Bank: 0.10 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 63.38
- Actual score: 71.00
- Transfer: Tijjani Reijnders -> Elliot Anderson (projected gain 1.49, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.92 | 11.32 | 18.34 | 6.00 | 84.3 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.9 | 0.04 | 0.41 | 0.99 | 0.00 | 5.5 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.18 | 15.37 | 20.88 | 2.00 | 87.3 | 77.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.7 | 4.61 | 14.70 | 21.57 | 3.00 | 90.0 | 90.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.0 | 4.29 | 13.17 | 18.46 | 0.00 | 90.0 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 3.57 | 9.86 | 13.69 | 3.00 | 78.4 | 90.0 |
| Bench 4 | Bench | Trevoh Chalobah | DEF | 7 | 5.2 | 2.41 | 8.34 | 12.43 | 0.00 | 48.3 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.81 | 25.37 | 39.52 | 8.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 3.91 | 12.90 | 21.05 | 2.00 | 74.4 | 73.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 2.91 | 5.82 | 9.21 | 0.00 | 37.8 | 0.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.7 | 6.30 | 18.87 | 28.39 | 18.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.5 | 6.25 | 18.57 | 31.16 | 2.00 | 83.0 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 3.53 | 12.64 | 18.79 | 7.00 | 69.3 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.20 | 12.04 | 19.06 | 12.00 | 74.7 | 89.0 |
| Bench 2 | Bench | Elliot Anderson | MID | 16 | 5.4 | 3.23 | 11.35 | 15.68 | 1.00 | 80.7 | 90.0 |

## GW8

- Train rows: 166350
- Bank: 0.40 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 73.59
- Actual score: 83.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.55) beats the best remaining Triple Captain opportunity (9.29).
- Transfer: Elliot Anderson -> Moisés Caicedo Corozo (projected gain 2.25, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.55) beats the best remaining Triple Captain opportunity (9.29).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.81 | 11.18 | 18.27 | 6.00 | 86.7 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.9 | 0.15 | 0.41 | 0.92 | 0.00 | 6.4 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.49 | 14.55 | 20.60 | 2.00 | 80.1 | 90.0 |
| Bench 2 | Bench | Omar Alderete | DEF | 17 | 4.0 | 3.92 | 11.62 | 15.55 | 6.00 | 72.6 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 3.93 | 11.51 | 14.91 | 17.00 | 77.1 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.69 | 11.31 | 21.48 | 4.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Trevoh Chalobah | DEF | 7 | 5.1 | 2.38 | 7.04 | 12.23 | 6.00 | 35.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 8.18 | 24.78 | 39.62 | 13.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.54 | 12.37 | 21.98 | 2.00 | 78.9 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 1.63 | 3.60 | 6.40 | 24.00 | 21.8 | 148.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.8 | 7.17 | 20.38 | 32.99 | 4.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.4 | 6.07 | 17.88 | 30.08 | 2.00 | 80.6 | 84.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.51 | 15.90 | 23.79 | 2.00 | 90.0 | 90.0 |
| XI | XI | Moisés Caicedo Corozo | MID | 7 | 5.8 | 4.79 | 13.85 | 20.43 | 1.00 | 89.8 | 45.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.04 | 12.78 | 20.49 | 4.00 | 81.5 | 85.0 |

## GW9

- Train rows: 167095
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Junior Kroupi
- Vice captain: Erling Haaland
- Effective captain: Junior Kroupi
- Chip used: bench_boost
- Predicted score: 78.11
- Actual score: 62.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.88) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.88) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.88 | 11.31 | 18.37 | 6.00 | 86.9 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 3.9 | 0.08 | 0.33 | 0.83 | 0.00 | 6.0 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 5.09 | 14.88 | 21.45 | 5.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.21 | 13.42 | 21.72 | 4.00 | 90.0 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 3.86 | 11.32 | 17.42 | 2.00 | 82.6 | 90.0 |
| Bench 3 | Bench Boost | Trevoh Chalobah | DEF | 7 | 5.1 | 3.43 | 9.61 | 15.20 | 1.00 | 62.4 | 90.0 |
| Bench 4 | Bench Boost | Omar Alderete | DEF | 17 | 4.0 | 2.94 | 9.01 | 13.38 | 0.00 | 67.0 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.5 | 7.85 | 24.66 | 40.84 | 2.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 4.50 | 12.83 | 21.11 | 2.00 | 80.4 | 84.0 |
| Captain | Captain | Junior Kroupi | FWD | 4 | 4.5 | 8.28 | 11.85 | 16.78 | 12.00 | 160.1 | 136.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.9 | 6.79 | 19.10 | 29.57 | 3.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.3 | 5.39 | 15.89 | 28.11 | 6.00 | 71.2 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 5.09 | 14.89 | 22.22 | 2.00 | 83.3 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.49 | 13.10 | 20.19 | 3.00 | 77.7 | 77.0 |
| Bench 2 | Bench Boost | Moisés Caicedo Corozo | MID | 7 | 5.8 | 3.94 | 11.90 | 17.17 | 2.00 | 69.0 | 90.0 |