# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 272.60
- Total actual points: 269.00
- Average predicted points: 68.15
- Average actual points: 67.25
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
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Erling Haaland
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 70.95
- Actual score: 54.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.82 | 13.29 | 20.96 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.06 | 0.18 | 0.34 | 0.00 | 1.6 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 6.94 | 19.47 | 29.98 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.98 | 14.21 | 22.62 | 11.00 | 90.0 | 90.0 |
| XI | XI | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 4.30 | 11.84 | 18.56 | 4.00 | 90.0 | 90.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.0 | 3.91 | 11.26 | 17.63 | 6.00 | 90.0 | 90.0 |
| Bench 4 | Bench | James Justin | DEF | 11 | 3.9 | 2.60 | 8.54 | 14.29 | 2.00 | 74.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 7.29 | 20.92 | 34.52 | 6.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.00 | 15.81 | 24.92 | 7.00 | 83.3 | 79.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 4.72 | 12.79 | 19.01 | 2.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.6 | 6.50 | 18.45 | 28.78 | 4.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 6.75 | 18.19 | 29.54 | 3.00 | 88.4 | 74.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 6.21 | 16.97 | 27.27 | 4.00 | 90.0 | 86.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.9 | 5.14 | 14.23 | 23.10 | 2.00 | 82.9 | 90.0 |
| Bench 3 | Bench | Ilia Gruev | MID | 11 | 4.7 | 2.76 | 8.52 | 13.66 | 1.00 | 75.9 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 0.10 -> 1.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Declan Rice
- Chip used: none
- Predicted score: 64.53
- Actual score: 65.00
- Transfer: Enzo Fernández -> Harry Wilson (projected gain 2.41, hit 0)
- Autosub: Yerson Mosquera Valdelamar replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.01 | 11.39 | 18.42 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.02 | 0.23 | 0.36 | 0.00 | 1.8 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.81 | 16.50 | 26.08 | 9.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.42 | 14.73 | 23.23 | 7.00 | 90.0 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.0 | 4.42 | 11.85 | 18.13 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Autosub In | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 3.57 | 10.46 | 16.14 | 9.00 | 90.0 | 90.0 |
| Bench 3 | Bench | James Justin | DEF | 11 | 3.9 | 2.89 | 9.01 | 14.41 | 2.00 | 83.5 | 86.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.8 | 7.85 | 22.57 | 36.77 | 0.00 | 90.0 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.34 | 13.54 | 21.93 | 2.00 | 68.7 | 90.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 3.78 | 11.03 | 16.76 | 2.00 | 90.0 | 90.0 |
| Vice Captain | Captain | Declan Rice | MID | 1 | 7.6 | 5.98 | 17.32 | 27.06 | 5.00 | 90.0 | 75.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.74 | 16.24 | 25.84 | 8.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.75 | 15.16 | 25.10 | 1.00 | 71.3 | 85.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.59 | 12.85 | 20.04 | 12.00 | 85.9 | 71.0 |
| Bench 4 | Bench | Ilia Gruev | MID | 11 | 4.7 | 2.86 | 8.70 | 13.57 | 2.00 | 79.6 | 74.0 |

## GW29

- Train rows: 182721
- Bank: 1.00 -> 0.30
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 65.59
- Actual score: 95.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.47) beats the best remaining Triple Captain opportunity (7.63).
- Transfer: Ilia Gruev -> Elliot Anderson (projected gain 1.32, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.47) beats the best remaining Triple Captain opportunity (7.63).
- Autosub: Mateus Mané replaced Harry Wilson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.81 | 11.55 | 18.71 | 7.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.14 | 0.31 | 0.45 | 0.00 | 1.8 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.65 | 16.97 | 26.96 | 11.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.18 | 14.51 | 22.89 | 1.00 | 89.1 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.0 | 3.62 | 10.39 | 16.29 | 8.00 | 88.7 | 90.0 |
| Bench 3 | Bench | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 3.49 | 10.19 | 16.11 | 1.00 | 90.0 | 31.0 |
| Bench 4 | Bench | James Justin | DEF | 11 | 3.9 | 3.07 | 8.64 | 13.52 | 2.00 | 81.9 | 73.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.7 | 5.33 | 16.77 | 28.94 | 2.00 | 55.9 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.73 | 14.09 | 23.17 | 19.00 | 78.2 | 84.0 |
| Bench 2 | Autosub In | Mateus Mané | FWD | 20 | 4.6 | 3.56 | 10.19 | 15.59 | 2.00 | 90.0 | 69.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.47 | 18.11 | 28.65 | 7.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.96 | 16.33 | 27.29 | 9.00 | 80.0 | 84.0 |
| XI | XI | Declan Rice | MID | 1 | 7.5 | 4.69 | 14.65 | 23.67 | 3.00 | 89.7 | 90.0 |
| XI | Bench | Harry Wilson | MID | 10 | 5.9 | 4.44 | 12.24 | 19.43 | 0.00 | 75.9 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.77 | 11.47 | 18.19 | 12.00 | 78.7 | 90.0 |

## GW30

- Train rows: 183541
- Bank: 0.30 -> 0.60
- Free transfers: 2 -> 2
- Captain: João Pedro Junqueira de Jesus
- Vice captain: Antoine Semenyo
- Effective captain: João Pedro Junqueira de Jesus
- Chip used: bench_boost
- Predicted score: 71.54
- Actual score: 55.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.41) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Harry Wilson -> Carlos Henrique Casimiro (projected gain 2.93, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.41) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.07 | 11.60 | 18.82 | 7.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Marcus Bettinelli | GK | 13 | 3.8 | 0.07 | 0.31 | 0.45 | 0.00 | 2.5 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.33 | 15.42 | 25.56 | 9.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.22 | 14.27 | 22.76 | 2.00 | 85.9 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.1 | 4.08 | 10.88 | 17.57 | 8.00 | 87.4 | 90.0 |
| Bench 2 | Bench Boost | James Justin | DEF | 11 | 3.9 | 2.61 | 7.88 | 12.87 | 6.00 | 73.6 | 90.0 |
| Bench 3 | Bench Boost | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 2.41 | 7.08 | 12.53 | 1.00 | 56.3 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.6 | 6.33 | 19.37 | 32.34 | 2.00 | 84.7 | 90.0 |
| Captain | Captain | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.84 | 18.45 | 29.73 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 2.31 | 6.75 | 11.55 | 1.00 | 62.6 | 45.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 8.1 | 6.39 | 18.23 | 28.78 | 2.00 | 90.0 | 74.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.85 | 17.66 | 28.95 | 2.00 | 85.9 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.4 | 4.79 | 13.64 | 22.55 | 3.00 | 82.6 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.59 | 12.63 | 20.01 | 2.00 | 87.2 | 87.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.6 | 3.80 | 10.77 | 17.28 | 6.00 | 70.7 | 90.0 |