# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW5
- Simulated weeks: GW6-GW9
- Total predicted points: 282.99
- Total actual points: 271.00
- Average predicted points: 70.75
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
- Predicted score: 66.71
- Actual score: 62.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.92 | 11.76 | 19.79 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.51 | 1.25 | 2.81 | 0.00 | 2.7 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.14 | 14.22 | 19.65 | 7.00 | 88.2 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.2 | 3.29 | 13.71 | 20.18 | -3.00 | 90.0 | 52.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.7 | 3.58 | 11.95 | 18.74 | 7.00 | 89.3 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.0 | 3.11 | 9.81 | 13.48 | 6.00 | 80.2 | 90.0 |
| Bench 3 | Bench | Omar Alderete | DEF | 17 | 4.0 | 1.85 | 9.75 | 13.69 | 17.00 | 80.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.84 | 24.57 | 39.82 | 16.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.02 | 16.40 | 26.99 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 1.57 | 3.61 | 6.45 | 12.00 | 17.3 | 18.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 6.22 | 19.58 | 33.58 | 2.00 | 88.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.99 | 18.48 | 28.25 | 7.00 | 90.0 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.35 | 14.45 | 21.91 | 2.00 | 90.0 | 80.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.45 | 14.45 | 23.56 | 2.00 | 87.7 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 5.08 | 14.21 | 22.20 | 2.00 | 90.0 | 82.0 |

## GW7

- Train rows: 165607
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 63.36
- Actual score: 78.00
- Transfer: Tijjani Reijnders -> Moisés Caicedo Corozo (projected gain 0.94, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 4.06 | 11.61 | 18.66 | 6.00 | 87.6 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.18 | 0.98 | 2.07 | 0.00 | 3.9 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.7 | 4.58 | 14.76 | 21.46 | 3.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 4.87 | 14.59 | 19.40 | 2.00 | 78.6 | 77.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.0 | 4.10 | 12.57 | 17.21 | 0.00 | 85.0 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.0 | 3.47 | 9.44 | 12.84 | 3.00 | 72.9 | 90.0 |
| Bench 4 | Bench | Trevoh Chalobah | DEF | 7 | 5.2 | 1.90 | 7.05 | 10.63 | 0.00 | 35.5 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.76 | 25.59 | 39.69 | 8.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.15 | 13.19 | 21.62 | 2.00 | 73.5 | 73.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 3.22 | 5.99 | 9.32 | 0.00 | 44.6 | 0.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 6.17 | 18.61 | 27.98 | 18.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 6.24 | 18.34 | 31.01 | 2.00 | 85.1 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 3.51 | 12.66 | 18.63 | 7.00 | 69.4 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.33 | 12.44 | 19.49 | 12.00 | 76.7 | 89.0 |
| XI | XI | Moisés Caicedo Corozo | MID | 7 | 5.7 | 3.85 | 11.90 | 16.95 | 10.00 | 82.6 | 90.0 |

## GW8

- Train rows: 166350
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 73.62
- Actual score: 68.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.51) beats the best remaining Triple Captain opportunity (9.24).
- Transfer: Trevoh Chalobah -> Dan Burn (projected gain 0.86, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.51) beats the best remaining Triple Captain opportunity (9.24).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.96 | 11.48 | 18.66 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.25 | 0.85 | 1.75 | 0.00 | 3.6 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.26 | 14.02 | 19.44 | 2.00 | 73.6 | 90.0 |
| XI | XI | Dan Burn | DEF | 15 | 5.1 | 3.89 | 11.89 | 17.79 | 2.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.69 | 11.25 | 21.63 | 4.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Omar Alderete | DEF | 17 | 4.0 | 3.51 | 11.20 | 15.10 | 6.00 | 61.1 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.0 | 3.83 | 11.13 | 14.08 | 17.00 | 72.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 8.13 | 24.71 | 39.82 | 13.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.66 | 12.51 | 22.38 | 2.00 | 77.7 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 1.71 | 3.70 | 6.40 | 24.00 | 17.8 | 148.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.8 | 7.17 | 20.18 | 32.69 | 4.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.4 | 6.07 | 17.78 | 30.06 | 2.00 | 82.7 | 84.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.58 | 16.06 | 23.95 | 2.00 | 90.0 | 90.0 |
| XI | XI | Moisés Caicedo Corozo | MID | 7 | 5.7 | 4.90 | 14.12 | 20.75 | 1.00 | 90.0 | 45.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.05 | 12.74 | 20.26 | 4.00 | 81.9 | 85.0 |

## GW9

- Train rows: 167095
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Junior Kroupi
- Vice captain: Erling Haaland
- Effective captain: Junior Kroupi
- Chip used: bench_boost
- Predicted score: 79.29
- Actual score: 63.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.78) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.78) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 4.06 | 11.64 | 18.82 | 6.00 | 89.8 | 90.0 |
| Bench 1 | Bench Boost | Antonín Kinský | GK | 18 | 3.9 | 0.16 | 0.75 | 1.60 | 0.00 | 3.0 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.94 | 14.35 | 20.44 | 5.00 | 88.8 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.23 | 13.45 | 21.78 | 4.00 | 90.0 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 3.77 | 10.76 | 16.27 | 2.00 | 77.1 | 90.0 |
| Bench 3 | Bench Boost | Dan Burn | DEF | 15 | 5.1 | 3.73 | 10.73 | 16.89 | 2.00 | 79.9 | 90.0 |
| Bench 4 | Bench Boost | Omar Alderete | DEF | 17 | 4.0 | 2.30 | 7.51 | 11.12 | 0.00 | 48.4 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.5 | 7.92 | 24.78 | 41.11 | 2.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 4.64 | 12.95 | 21.39 | 2.00 | 78.9 | 84.0 |
| Captain | Captain | Junior Kroupi | FWD | 4 | 4.5 | 8.74 | 12.56 | 17.66 | 12.00 | 160.4 | 136.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.9 | 6.87 | 19.37 | 29.97 | 3.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.3 | 5.46 | 16.02 | 28.40 | 6.00 | 74.0 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 5.07 | 14.85 | 21.96 | 2.00 | 83.5 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.54 | 13.36 | 20.51 | 3.00 | 79.7 | 77.0 |
| Bench 2 | Bench Boost | Moisés Caicedo Corozo | MID | 7 | 5.8 | 4.12 | 12.49 | 17.97 | 2.00 | 76.2 | 90.0 |