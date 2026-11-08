# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW5
- Simulated weeks: GW6-GW9
- Total predicted points: 284.13
- Total actual points: 265.00
- Average predicted points: 71.03
- Average actual points: 66.25
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
- Predicted score: 67.59
- Actual score: 62.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.89 | 11.48 | 19.75 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.59 | 1.36 | 3.39 | 0.00 | 8.0 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.40 | 15.01 | 21.68 | 7.00 | 90.0 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.2 | 3.44 | 14.10 | 21.18 | -3.00 | 90.0 | 52.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.7 | 3.56 | 12.15 | 19.36 | 7.00 | 89.2 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.0 | 3.31 | 10.27 | 14.64 | 6.00 | 87.4 | 90.0 |
| Bench 3 | Bench | Omar Alderete | DEF | 17 | 4.0 | 2.04 | 10.14 | 14.97 | 17.00 | 89.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 9.09 | 24.37 | 39.88 | 16.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 5.69 | 15.62 | 25.93 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 1.40 | 3.62 | 7.11 | 12.00 | 21.1 | 18.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 6.30 | 20.18 | 34.53 | 2.00 | 87.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 6.20 | 18.55 | 28.97 | 7.00 | 90.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 5.20 | 14.44 | 23.12 | 2.00 | 90.0 | 82.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.40 | 14.41 | 22.34 | 2.00 | 90.0 | 80.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.34 | 14.02 | 23.35 | 2.00 | 88.5 | 90.0 |

## GW7

- Train rows: 165607
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 64.30
- Actual score: 69.00
- Transfer: Tijjani Reijnders -> Jaidon Anthony (projected gain 1.14, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.86 | 11.28 | 18.31 | 6.00 | 85.4 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.32 | 1.13 | 2.36 | 0.00 | 8.3 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.25 | 15.57 | 21.59 | 2.00 | 88.7 | 77.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.7 | 4.65 | 14.80 | 21.88 | 3.00 | 90.0 | 90.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.0 | 4.26 | 13.18 | 18.67 | 0.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.0 | 3.55 | 9.79 | 13.68 | 3.00 | 78.7 | 90.0 |
| Bench 4 | Bench | Trevoh Chalobah | DEF | 7 | 5.2 | 2.41 | 8.45 | 12.61 | 0.00 | 48.9 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.95 | 25.47 | 40.05 | 8.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 3.83 | 12.85 | 20.76 | 2.00 | 78.0 | 73.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 2.86 | 5.94 | 9.31 | 0.00 | 39.3 | 0.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.7 | 6.32 | 18.93 | 28.83 | 18.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.5 | 6.31 | 18.79 | 31.30 | 2.00 | 82.1 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 3.60 | 12.76 | 19.07 | 7.00 | 70.4 | 90.0 |
| XI | XI | Jaidon Anthony | MID | 3 | 5.7 | 4.16 | 12.24 | 19.18 | 1.00 | 86.1 | 58.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.17 | 11.90 | 19.03 | 12.00 | 76.0 | 89.0 |

## GW8

- Train rows: 166350
- Bank: 0.10 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 74.37
- Actual score: 72.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.73) beats the best remaining Triple Captain opportunity (9.48).
- Transfer: Jaidon Anthony -> Moisés Caicedo Corozo (projected gain 2.37, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.73) beats the best remaining Triple Captain opportunity (9.48).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.78 | 11.17 | 18.28 | 6.00 | 87.9 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.38 | 1.03 | 1.96 | 0.00 | 8.0 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.63 | 14.79 | 21.16 | 2.00 | 81.6 | 90.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.0 | 4.01 | 11.81 | 15.86 | 6.00 | 73.5 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.0 | 3.91 | 11.59 | 15.02 | 17.00 | 77.3 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.74 | 11.39 | 21.75 | 4.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Trevoh Chalobah | DEF | 7 | 5.1 | 2.38 | 6.99 | 12.28 | 6.00 | 35.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 8.36 | 25.16 | 40.10 | 13.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.50 | 12.33 | 21.82 | 2.00 | 82.2 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 1.49 | 3.44 | 6.20 | 24.00 | 21.9 | 148.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.8 | 7.23 | 20.57 | 33.46 | 4.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.4 | 6.14 | 18.05 | 30.22 | 2.00 | 80.5 | 84.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.50 | 15.86 | 23.81 | 2.00 | 90.0 | 90.0 |
| XI | XI | Moisés Caicedo Corozo | MID | 7 | 5.8 | 4.74 | 13.91 | 20.63 | 1.00 | 89.5 | 45.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.04 | 12.75 | 20.53 | 4.00 | 81.8 | 85.0 |

## GW9

- Train rows: 167095
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Junior Kroupi
- Vice captain: Erling Haaland
- Effective captain: Junior Kroupi
- Chip used: bench_boost
- Predicted score: 77.86
- Actual score: 62.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.21) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.21) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.84 | 11.27 | 18.29 | 6.00 | 88.7 | 90.0 |
| Bench 1 | Bench Boost | Antonín Kinský | GK | 18 | 3.9 | 0.30 | 0.95 | 1.86 | 0.00 | 7.2 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 5.07 | 14.98 | 21.60 | 5.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.24 | 13.55 | 21.87 | 4.00 | 90.0 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 3.79 | 11.45 | 17.70 | 2.00 | 82.8 | 90.0 |
| Bench 3 | Bench Boost | Trevoh Chalobah | DEF | 7 | 5.1 | 3.43 | 9.56 | 15.19 | 1.00 | 63.0 | 90.0 |
| Bench 4 | Bench Boost | Omar Alderete | DEF | 17 | 4.0 | 2.98 | 9.11 | 13.54 | 0.00 | 68.9 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.5 | 7.94 | 24.82 | 41.04 | 2.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 4.48 | 12.81 | 20.94 | 2.00 | 83.5 | 84.0 |
| Captain | Captain | Junior Kroupi | FWD | 4 | 4.5 | 7.96 | 11.47 | 16.19 | 12.00 | 164.5 | 136.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.9 | 6.82 | 19.12 | 29.55 | 3.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.3 | 5.41 | 15.93 | 28.02 | 6.00 | 71.3 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 5.07 | 14.92 | 22.30 | 2.00 | 83.1 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.55 | 13.09 | 20.23 | 3.00 | 78.8 | 77.0 |
| Bench 2 | Bench Boost | Moisés Caicedo Corozo | MID | 7 | 5.8 | 4.02 | 12.06 | 17.48 | 2.00 | 69.2 | 90.0 |