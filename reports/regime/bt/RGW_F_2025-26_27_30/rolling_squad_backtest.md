# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 267.72
- Total actual points: 263.00
- Average predicted points: 66.93
- Average actual points: 65.75
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
- Predicted score: 69.89
- Actual score: 54.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.85 | 13.29 | 20.65 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.02 | 0.09 | 0.23 | 0.00 | 1.6 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 6.86 | 19.49 | 29.81 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.95 | 14.10 | 22.46 | 11.00 | 90.0 | 90.0 |
| XI | XI | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 4.38 | 12.25 | 19.06 | 4.00 | 90.0 | 90.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.0 | 3.90 | 11.20 | 17.44 | 6.00 | 90.0 | 90.0 |
| Bench 4 | Bench | James Justin | DEF | 11 | 3.9 | 2.66 | 8.59 | 14.52 | 2.00 | 74.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 6.94 | 20.16 | 33.05 | 6.00 | 87.6 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.88 | 15.23 | 23.86 | 7.00 | 84.7 | 79.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 4.74 | 13.04 | 19.39 | 2.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.6 | 6.45 | 18.28 | 28.22 | 4.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 6.74 | 17.80 | 28.86 | 3.00 | 87.2 | 74.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 6.08 | 16.52 | 26.36 | 4.00 | 90.0 | 86.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.9 | 5.09 | 14.02 | 22.70 | 2.00 | 83.6 | 90.0 |
| Bench 3 | Bench | Ilia Gruev | MID | 11 | 4.7 | 2.79 | 8.64 | 13.78 | 1.00 | 75.9 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 0.10 -> 1.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Declan Rice
- Chip used: none
- Predicted score: 63.38
- Actual score: 65.00
- Transfer: Enzo Fernández -> Harry Wilson (projected gain 2.10, hit 0)
- Autosub: Yerson Mosquera Valdelamar replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.98 | 11.36 | 18.22 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.13 | 0.23 | 0.00 | 1.7 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.67 | 16.35 | 25.74 | 9.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.44 | 14.54 | 22.82 | 7.00 | 90.0 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.0 | 4.34 | 11.56 | 17.66 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Autosub In | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 3.58 | 10.68 | 16.56 | 9.00 | 90.0 | 90.0 |
| Bench 3 | Bench | James Justin | DEF | 11 | 3.9 | 2.87 | 9.04 | 14.52 | 2.00 | 83.4 | 86.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.8 | 7.58 | 21.92 | 35.26 | 0.00 | 90.0 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.17 | 12.87 | 21.08 | 2.00 | 69.9 | 90.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 3.74 | 11.20 | 17.16 | 2.00 | 90.0 | 90.0 |
| Vice Captain | Captain | Declan Rice | MID | 1 | 7.6 | 5.92 | 17.34 | 26.85 | 5.00 | 90.0 | 75.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.66 | 15.75 | 24.92 | 8.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.75 | 14.78 | 24.50 | 1.00 | 70.0 | 85.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.54 | 12.75 | 19.89 | 12.00 | 86.6 | 71.0 |
| Bench 4 | Bench | Ilia Gruev | MID | 11 | 4.7 | 2.87 | 8.80 | 13.66 | 2.00 | 79.6 | 74.0 |

## GW29

- Train rows: 182721
- Bank: 1.00 -> 0.30
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 64.54
- Actual score: 95.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.34) beats the best remaining Triple Captain opportunity (7.49).
- Transfer: Ilia Gruev -> Elliot Anderson (projected gain 1.30, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.34) beats the best remaining Triple Captain opportunity (7.49).
- Autosub: Mateus Mané replaced Harry Wilson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.84 | 11.55 | 18.66 | 7.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.11 | 0.22 | 0.32 | 0.00 | 1.5 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.56 | 16.77 | 26.47 | 11.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.20 | 14.24 | 22.36 | 1.00 | 89.5 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.0 | 3.56 | 10.19 | 15.95 | 8.00 | 88.4 | 90.0 |
| Bench 3 | Bench | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 3.46 | 10.17 | 16.04 | 1.00 | 90.0 | 31.0 |
| Bench 4 | Bench | James Justin | DEF | 11 | 3.9 | 3.05 | 8.86 | 13.87 | 2.00 | 81.2 | 73.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.7 | 4.88 | 16.06 | 27.51 | 2.00 | 49.5 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.68 | 13.72 | 22.76 | 19.00 | 79.5 | 84.0 |
| Bench 2 | Autosub In | Mateus Mané | FWD | 20 | 4.6 | 3.55 | 10.22 | 15.56 | 2.00 | 90.0 | 69.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.34 | 17.76 | 27.96 | 7.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.03 | 16.17 | 26.93 | 9.00 | 79.5 | 84.0 |
| XI | XI | Declan Rice | MID | 1 | 7.5 | 4.58 | 14.33 | 22.99 | 3.00 | 89.0 | 90.0 |
| XI | Bench | Harry Wilson | MID | 10 | 5.9 | 4.43 | 12.25 | 19.41 | 0.00 | 77.2 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.75 | 11.48 | 18.35 | 12.00 | 78.4 | 90.0 |

## GW30

- Train rows: 183541
- Bank: 0.30 -> 0.50
- Free transfers: 2 -> 2
- Captain: João Pedro Junqueira de Jesus
- Vice captain: Erling Haaland
- Effective captain: João Pedro Junqueira de Jesus
- Chip used: bench_boost
- Predicted score: 69.92
- Actual score: 49.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.45) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Harry Wilson -> Crysencio Summerville (projected gain 2.87, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.45) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.00 | 11.56 | 18.64 | 7.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Marcus Bettinelli | GK | 13 | 3.8 | 0.06 | 0.26 | 0.40 | 0.00 | 2.4 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.16 | 15.20 | 24.86 | 9.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.10 | 13.81 | 22.03 | 2.00 | 85.1 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.1 | 3.95 | 10.66 | 17.20 | 8.00 | 86.6 | 90.0 |
| Bench 2 | Bench Boost | James Justin | DEF | 11 | 3.9 | 2.61 | 8.00 | 13.11 | 6.00 | 73.3 | 90.0 |
| Bench 4 | Bench Boost | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 2.38 | 6.82 | 12.13 | 1.00 | 55.7 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 6.25 | 19.04 | 31.33 | 2.00 | 83.9 | 90.0 |
| Captain | Captain | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.67 | 17.98 | 29.30 | 2.00 | 90.0 | 90.0 |
| Bench 3 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 2.39 | 6.68 | 11.39 | 1.00 | 63.6 | 45.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 6.22 | 17.70 | 28.16 | 2.00 | 90.0 | 74.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.85 | 17.59 | 28.50 | 2.00 | 85.6 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.4 | 4.72 | 13.43 | 21.95 | 3.00 | 83.1 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.49 | 12.69 | 20.06 | 2.00 | 86.7 | 87.0 |
| XI | XI | Crysencio Summerville | MID | 19 | 5.7 | 3.38 | 10.83 | 17.79 | 0.00 | 73.3 | 0.0 |