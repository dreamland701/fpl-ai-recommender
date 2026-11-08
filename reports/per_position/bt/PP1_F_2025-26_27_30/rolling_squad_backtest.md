# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 270.10
- Total actual points: 213.00
- Average predicted points: 67.52
- Average actual points: 53.25
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW26 are included before the first simulated week.
- League-average scores were not available for this run.

## GW27

- Train rows: 181084
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Gabriel dos Santos Magalhães
- Vice captain: Declan Rice
- Effective captain: Gabriel dos Santos Magalhães
- Chip used: none
- Predicted score: 72.04
- Actual score: 43.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 5.90 | 17.16 | 26.82 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 7.12 | 20.54 | 31.64 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.04 | 14.50 | 23.31 | 11.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.91 | 13.54 | 20.67 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 4.21 | 11.58 | 17.95 | 4.00 | 90.0 | 90.0 |
| Bench 3 | Bench | James Hill | DEF | 4 | 4.0 | 3.47 | 9.91 | 15.81 | 6.00 | 90.0 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.8 | 6.71 | 18.79 | 31.67 | 6.00 | 83.1 | 90.0 |
| XI | XI | Adam Armstrong | FWD | 20 | 5.5 | 5.28 | 15.21 | 25.03 | 2.00 | 90.0 | 62.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 4.85 | 13.44 | 20.40 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.6 | 6.77 | 18.99 | 29.43 | 4.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 6.70 | 17.82 | 28.31 | 3.00 | 90.0 | 74.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 6.19 | 17.07 | 27.07 | 4.00 | 90.0 | 86.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.48 | 15.03 | 24.44 | 2.00 | 83.4 | 90.0 |
| Bench 4 | Bench | Vitaly Janelt | MID | 5 | 4.9 | 3.22 | 9.85 | 15.70 | 1.00 | 84.8 | 45.0 |

## GW28

- Train rows: 181902
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Gabriel dos Santos Magalhães
- Chip used: none
- Predicted score: 65.48
- Actual score: 63.00
- Transfer: none
- No transfer was applied this week.
- Autosub: Yerson Mosquera Valdelamar replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 5.20 | 15.12 | 24.43 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Vice Captain | Captain | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 6.26 | 17.86 | 28.28 | 9.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.63 | 15.11 | 24.28 | 7.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.29 | 11.97 | 18.94 | 6.00 | 83.0 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.0 | 4.16 | 11.02 | 17.03 | 2.00 | 84.9 | 90.0 |
| Bench 2 | Autosub In | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 3.51 | 9.96 | 15.27 | 9.00 | 90.0 | 90.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.8 | 7.07 | 20.48 | 33.89 | 0.00 | 90.0 | 0.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 3.72 | 11.42 | 17.91 | 2.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Adam Armstrong | FWD | 20 | 5.4 | 3.42 | 10.91 | 18.64 | 4.00 | 78.5 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.6 | 5.95 | 17.79 | 27.47 | 5.00 | 90.0 | 75.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.94 | 16.69 | 26.17 | 8.00 | 88.3 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.05 | 15.10 | 24.71 | 1.00 | 76.3 | 85.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.11 | 14.47 | 23.09 | 2.00 | 81.3 | 90.0 |
| Bench 4 | Bench | Vitaly Janelt | MID | 5 | 4.9 | 2.44 | 7.48 | 12.78 | 0.00 | 62.0 | 0.0 |

## GW29

- Train rows: 182721
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 66.80
- Actual score: 59.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.76) beats the best remaining Triple Captain opportunity (7.98).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.76) beats the best remaining Triple Captain opportunity (7.98).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 5.02 | 14.81 | 24.63 | 7.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.85 | 17.67 | 27.93 | 11.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.27 | 15.03 | 23.88 | 1.00 | 87.4 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 5.06 | 13.60 | 21.39 | 1.00 | 89.2 | 90.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.0 | 3.48 | 10.01 | 15.67 | 8.00 | 79.4 | 90.0 |
| Bench 3 | Bench | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 3.09 | 8.70 | 13.78 | 1.00 | 90.0 | 31.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.7 | 4.41 | 15.39 | 27.02 | 2.00 | 48.0 | 90.0 |
| XI | XI | Adam Armstrong | FWD | 20 | 5.4 | 3.89 | 11.47 | 18.15 | 1.00 | 86.5 | 59.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 3.60 | 11.00 | 17.04 | 2.00 | 90.0 | 69.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.76 | 18.54 | 28.98 | 7.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.41 | 15.02 | 25.36 | 9.00 | 80.4 | 84.0 |
| XI | XI | Declan Rice | MID | 1 | 7.5 | 4.74 | 14.99 | 24.23 | 3.00 | 89.9 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 4.29 | 12.12 | 20.24 | 1.00 | 67.0 | 90.0 |
| Bench 4 | Bench | Vitaly Janelt | MID | 5 | 4.9 | 1.01 | 3.79 | 7.55 | 0.00 | 28.4 | 0.0 |

## GW30

- Train rows: 183541
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Erling Haaland
- Effective captain: Antoine Semenyo
- Chip used: bench_boost
- Predicted score: 65.77
- Actual score: 48.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.12) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.12) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.79 | 13.42 | 22.39 | 7.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.51 | 15.43 | 25.86 | 9.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.52 | 15.37 | 24.04 | 2.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.33 | 12.37 | 19.38 | 2.00 | 81.4 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.1 | 4.17 | 10.48 | 16.76 | 8.00 | 82.7 | 90.0 |
| Bench 3 | Bench Boost | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 1.91 | 5.53 | 10.61 | 1.00 | 53.2 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 5.86 | 18.25 | 30.19 | 2.00 | 81.1 | 90.0 |
| XI | XI | Adam Armstrong | FWD | 20 | 5.3 | 3.20 | 9.60 | 15.57 | 5.00 | 67.2 | 86.0 |
| Bench 2 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 2.75 | 7.46 | 14.85 | 1.00 | 64.5 | 45.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.76 | 18.36 | 28.92 | 2.00 | 90.0 | 74.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.48 | 16.27 | 27.14 | 2.00 | 84.8 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.4 | 4.61 | 13.35 | 21.93 | 3.00 | 84.7 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 3.67 | 11.25 | 18.97 | 2.00 | 72.2 | 90.0 |
| Bench 4 | Bench Boost | Vitaly Janelt | MID | 5 | 4.9 | 0.46 | 1.76 | 4.15 | 0.00 | 4.2 | 0.0 |