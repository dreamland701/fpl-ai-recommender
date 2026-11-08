# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 270.43
- Total actual points: 269.00
- Average predicted points: 67.61
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
- Predicted score: 70.32
- Actual score: 54.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.84 | 13.34 | 20.82 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 2.0 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 6.88 | 19.54 | 29.87 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.94 | 14.04 | 22.34 | 11.00 | 90.0 | 90.0 |
| XI | XI | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 4.28 | 11.89 | 18.43 | 4.00 | 90.0 | 90.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.0 | 3.93 | 11.29 | 17.60 | 6.00 | 90.0 | 90.0 |
| Bench 4 | Bench | James Justin | DEF | 11 | 3.9 | 2.55 | 8.19 | 13.79 | 2.00 | 73.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 6.97 | 20.20 | 33.11 | 6.00 | 86.9 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.00 | 15.61 | 24.53 | 7.00 | 85.1 | 79.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 4.84 | 13.40 | 20.07 | 2.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.6 | 6.54 | 18.64 | 28.91 | 4.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 6.69 | 17.63 | 28.56 | 3.00 | 86.3 | 74.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 6.23 | 17.03 | 27.25 | 4.00 | 90.0 | 86.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.9 | 5.15 | 14.23 | 23.08 | 2.00 | 84.1 | 90.0 |
| Bench 3 | Bench | Ilia Gruev | MID | 11 | 4.7 | 2.88 | 8.94 | 14.31 | 1.00 | 76.3 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 0.10 -> 1.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Declan Rice
- Chip used: none
- Predicted score: 63.99
- Actual score: 65.00
- Transfer: Enzo Fernández -> Harry Wilson (projected gain 2.73, hit 0)
- Autosub: Yerson Mosquera Valdelamar replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.00 | 11.50 | 18.55 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 2.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.71 | 16.47 | 25.94 | 9.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.40 | 14.40 | 22.57 | 7.00 | 90.0 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.0 | 4.35 | 11.61 | 17.78 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Autosub In | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 3.50 | 10.38 | 16.02 | 9.00 | 90.0 | 90.0 |
| Bench 4 | Bench | James Justin | DEF | 11 | 3.9 | 2.79 | 8.76 | 14.00 | 2.00 | 82.4 | 86.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.8 | 7.61 | 21.97 | 35.33 | 0.00 | 90.0 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.27 | 13.19 | 21.67 | 2.00 | 70.1 | 90.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 3.85 | 11.58 | 17.87 | 2.00 | 90.0 | 90.0 |
| Vice Captain | Captain | Declan Rice | MID | 1 | 7.6 | 6.06 | 17.86 | 27.82 | 5.00 | 90.0 | 75.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.81 | 16.26 | 25.82 | 8.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.68 | 14.51 | 24.01 | 1.00 | 68.8 | 85.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.64 | 13.09 | 20.52 | 12.00 | 87.7 | 71.0 |
| Bench 3 | Bench | Ilia Gruev | MID | 11 | 4.7 | 2.96 | 9.09 | 14.19 | 2.00 | 80.0 | 74.0 |

## GW29

- Train rows: 182721
- Bank: 1.00 -> 0.30
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 65.36
- Actual score: 95.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.49) beats the best remaining Triple Captain opportunity (7.66).
- Transfer: Ilia Gruev -> Elliot Anderson (projected gain 1.19, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.49) beats the best remaining Triple Captain opportunity (7.66).
- Autosub: Mateus Mané replaced Harry Wilson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.84 | 11.65 | 18.90 | 7.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.02 | 0.00 | 0.00 | 0.00 | 1.8 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.59 | 16.85 | 26.61 | 11.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.17 | 14.11 | 22.11 | 1.00 | 88.5 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.0 | 3.56 | 10.19 | 15.96 | 8.00 | 88.0 | 90.0 |
| Bench 3 | Bench | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 3.40 | 9.93 | 15.62 | 1.00 | 90.0 | 31.0 |
| Bench 4 | Bench | James Justin | DEF | 11 | 3.9 | 2.98 | 8.60 | 13.39 | 2.00 | 80.2 | 73.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.7 | 4.88 | 16.07 | 27.48 | 2.00 | 48.5 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.81 | 14.16 | 23.53 | 19.00 | 79.8 | 84.0 |
| Bench 2 | Autosub In | Mateus Mané | FWD | 20 | 4.6 | 3.65 | 10.62 | 16.29 | 2.00 | 90.0 | 69.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.49 | 18.26 | 28.81 | 7.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.97 | 15.93 | 26.49 | 9.00 | 78.2 | 84.0 |
| XI | XI | Declan Rice | MID | 1 | 7.5 | 4.71 | 14.82 | 23.89 | 3.00 | 90.0 | 90.0 |
| XI | Bench | Harry Wilson | MID | 10 | 5.9 | 4.54 | 12.64 | 20.11 | 0.00 | 78.1 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.82 | 11.74 | 18.86 | 12.00 | 79.7 | 90.0 |

## GW30

- Train rows: 183541
- Bank: 0.30 -> 0.60
- Free transfers: 2 -> 2
- Captain: João Pedro Junqueira de Jesus
- Vice captain: Antoine Semenyo
- Effective captain: João Pedro Junqueira de Jesus
- Chip used: bench_boost
- Predicted score: 70.76
- Actual score: 55.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.33) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Harry Wilson -> Carlos Henrique Casimiro (projected gain 3.35, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.33) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.00 | 11.63 | 18.86 | 7.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.01 | 0.08 | 0.00 | 2.6 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.17 | 15.22 | 24.91 | 9.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.05 | 13.62 | 21.69 | 2.00 | 83.9 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.1 | 3.95 | 10.65 | 17.20 | 8.00 | 86.1 | 90.0 |
| Bench 2 | Bench Boost | James Justin | DEF | 11 | 3.9 | 2.53 | 7.71 | 12.61 | 6.00 | 72.2 | 90.0 |
| Bench 4 | Bench Boost | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 2.30 | 6.54 | 11.66 | 1.00 | 55.3 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.6 | 6.26 | 19.05 | 31.33 | 2.00 | 83.2 | 90.0 |
| Captain | Captain | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.79 | 18.36 | 29.94 | 2.00 | 90.0 | 90.0 |
| Bench 3 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 2.50 | 7.06 | 12.10 | 1.00 | 64.6 | 45.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 8.1 | 6.37 | 18.20 | 29.03 | 2.00 | 90.0 | 74.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.80 | 17.38 | 28.11 | 2.00 | 84.1 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.4 | 4.86 | 13.93 | 22.85 | 3.00 | 84.5 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.58 | 13.03 | 20.69 | 2.00 | 88.0 | 87.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.6 | 3.83 | 11.04 | 18.00 | 6.00 | 71.0 | 90.0 |