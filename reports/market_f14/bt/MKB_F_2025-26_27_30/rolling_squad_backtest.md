# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 275.48
- Total actual points: 263.00
- Average predicted points: 68.87
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
- Predicted score: 72.06
- Actual score: 54.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 5.07 | 13.95 | 21.99 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 7.07 | 19.69 | 30.25 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.04 | 14.35 | 22.77 | 11.00 | 90.0 | 90.0 |
| XI | XI | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 4.34 | 11.82 | 18.45 | 4.00 | 90.0 | 90.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.0 | 3.93 | 11.36 | 17.82 | 6.00 | 90.0 | 90.0 |
| Bench 4 | Bench | James Justin | DEF | 11 | 3.9 | 2.50 | 8.19 | 13.66 | 2.00 | 72.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 7.27 | 20.95 | 34.59 | 6.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.22 | 16.46 | 26.02 | 7.00 | 86.4 | 79.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 4.88 | 13.25 | 19.88 | 2.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.6 | 6.65 | 18.87 | 29.52 | 4.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 6.70 | 18.00 | 29.18 | 3.00 | 87.7 | 74.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 6.39 | 17.61 | 28.35 | 4.00 | 90.0 | 86.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.9 | 5.17 | 14.33 | 23.32 | 2.00 | 83.2 | 90.0 |
| Bench 3 | Bench | Ilia Gruev | MID | 11 | 4.7 | 2.83 | 8.80 | 14.18 | 1.00 | 76.1 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 0.10 -> 1.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Declan Rice
- Chip used: none
- Predicted score: 64.96
- Actual score: 65.00
- Transfer: Enzo Fernández -> Harry Wilson (projected gain 3.22, hit 0)
- Autosub: Yerson Mosquera Valdelamar replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.13 | 11.75 | 19.09 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.78 | 16.42 | 25.94 | 9.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.48 | 14.85 | 23.37 | 7.00 | 90.0 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.0 | 4.39 | 11.78 | 18.03 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Autosub In | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 3.46 | 10.13 | 15.55 | 9.00 | 90.0 | 90.0 |
| Bench 4 | Bench | James Justin | DEF | 11 | 3.9 | 2.76 | 8.62 | 13.71 | 2.00 | 81.7 | 86.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.8 | 7.84 | 22.59 | 36.81 | 0.00 | 90.0 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.48 | 13.95 | 22.66 | 2.00 | 69.8 | 90.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 3.76 | 11.12 | 17.06 | 2.00 | 90.0 | 90.0 |
| Vice Captain | Captain | Declan Rice | MID | 1 | 7.6 | 5.97 | 17.45 | 27.40 | 5.00 | 90.0 | 75.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.96 | 16.89 | 26.92 | 8.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.58 | 14.64 | 24.21 | 1.00 | 68.2 | 85.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.75 | 13.33 | 20.89 | 12.00 | 88.5 | 71.0 |
| Bench 3 | Bench | Ilia Gruev | MID | 11 | 4.7 | 2.89 | 8.86 | 13.89 | 2.00 | 79.4 | 74.0 |

## GW29

- Train rows: 182721
- Bank: 1.00 -> 0.30
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 66.61
- Actual score: 95.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.72) beats the best remaining Triple Captain opportunity (7.93).
- Transfer: Ilia Gruev -> Elliot Anderson (projected gain 1.57, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.72) beats the best remaining Triple Captain opportunity (7.93).
- Autosub: Mateus Mané replaced Harry Wilson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.98 | 12.02 | 19.54 | 7.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.02 | 0.00 | 0.01 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.70 | 17.12 | 27.13 | 11.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.18 | 14.44 | 22.69 | 1.00 | 88.0 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.0 | 3.58 | 10.33 | 16.19 | 8.00 | 88.4 | 90.0 |
| Bench 3 | Bench | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 3.40 | 9.90 | 15.62 | 1.00 | 90.0 | 31.0 |
| Bench 4 | Bench | James Justin | DEF | 11 | 3.9 | 2.99 | 8.31 | 12.86 | 2.00 | 79.5 | 73.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.7 | 5.11 | 16.29 | 28.22 | 2.00 | 51.6 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.93 | 14.71 | 24.24 | 19.00 | 80.5 | 84.0 |
| Bench 2 | Autosub In | Mateus Mané | FWD | 20 | 4.6 | 3.51 | 10.22 | 15.75 | 2.00 | 90.0 | 69.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.72 | 18.84 | 29.82 | 7.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.80 | 15.84 | 26.47 | 9.00 | 76.5 | 84.0 |
| XI | XI | Declan Rice | MID | 1 | 7.5 | 4.80 | 15.08 | 24.41 | 3.00 | 90.0 | 90.0 |
| XI | Bench | Harry Wilson | MID | 10 | 5.9 | 4.53 | 12.56 | 20.05 | 0.00 | 78.2 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.83 | 11.76 | 18.71 | 12.00 | 79.1 | 90.0 |

## GW30

- Train rows: 183541
- Bank: 0.30 -> 0.50
- Free transfers: 2 -> 2
- Captain: João Pedro Junqueira de Jesus
- Vice captain: Antoine Semenyo
- Effective captain: João Pedro Junqueira de Jesus
- Chip used: bench_boost
- Predicted score: 71.85
- Actual score: 49.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.25) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Harry Wilson -> Crysencio Summerville (projected gain 3.79, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.25) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.26 | 12.06 | 19.62 | 7.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.01 | 0.00 | 0.6 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.38 | 15.50 | 25.64 | 9.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.20 | 14.19 | 22.55 | 2.00 | 83.9 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.1 | 4.07 | 10.89 | 17.58 | 8.00 | 86.4 | 90.0 |
| Bench 2 | Bench Boost | James Justin | DEF | 11 | 3.9 | 2.54 | 7.61 | 12.38 | 6.00 | 71.3 | 90.0 |
| Bench 4 | Bench Boost | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 2.33 | 6.81 | 12.11 | 1.00 | 57.0 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.6 | 6.17 | 18.97 | 31.75 | 2.00 | 82.2 | 90.0 |
| Captain | Captain | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 7.01 | 18.95 | 30.59 | 2.00 | 90.0 | 90.0 |
| Bench 3 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 2.38 | 7.02 | 12.15 | 1.00 | 64.2 | 45.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 8.1 | 6.59 | 18.87 | 29.83 | 2.00 | 90.0 | 74.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.61 | 17.00 | 27.87 | 2.00 | 81.4 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.4 | 4.93 | 14.09 | 23.34 | 3.00 | 83.2 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.66 | 12.92 | 20.54 | 2.00 | 87.3 | 87.0 |
| XI | XI | Crysencio Summerville | MID | 19 | 5.7 | 3.71 | 11.56 | 18.83 | 0.00 | 79.8 | 0.0 |