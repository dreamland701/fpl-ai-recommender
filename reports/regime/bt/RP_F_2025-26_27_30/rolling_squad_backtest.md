# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 274.05
- Total actual points: 254.00
- Average predicted points: 68.51
- Average actual points: 63.50
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
- Predicted score: 71.14
- Actual score: 54.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.84 | 13.39 | 21.17 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.10 | 0.29 | 0.61 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 6.88 | 19.27 | 29.61 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.94 | 14.09 | 22.42 | 11.00 | 90.0 | 90.0 |
| XI | XI | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 4.24 | 11.65 | 18.22 | 4.00 | 90.0 | 90.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.0 | 3.89 | 11.18 | 17.51 | 6.00 | 90.0 | 90.0 |
| Bench 4 | Bench | James Justin | DEF | 11 | 3.9 | 2.51 | 8.24 | 13.76 | 2.00 | 73.6 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 7.34 | 21.03 | 34.70 | 6.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.03 | 15.89 | 25.07 | 7.00 | 83.0 | 79.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 4.75 | 12.87 | 19.16 | 2.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.6 | 6.58 | 18.71 | 29.25 | 4.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 6.79 | 18.34 | 29.82 | 3.00 | 88.9 | 74.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 6.24 | 17.09 | 27.49 | 4.00 | 90.0 | 86.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.9 | 5.17 | 14.32 | 23.27 | 2.00 | 83.0 | 90.0 |
| Bench 3 | Bench | Ilia Gruev | MID | 11 | 4.7 | 2.79 | 8.63 | 13.87 | 1.00 | 76.1 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 0.10 -> 1.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Declan Rice
- Chip used: none
- Predicted score: 64.77
- Actual score: 65.00
- Transfer: Enzo Fernández -> Harry Wilson (projected gain 2.76, hit 0)
- Autosub: Yerson Mosquera Valdelamar replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.03 | 11.49 | 18.65 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.35 | 0.53 | 0.83 | 0.00 | 0.8 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.75 | 16.31 | 25.74 | 9.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.38 | 14.61 | 23.02 | 7.00 | 90.0 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.0 | 4.39 | 11.76 | 17.98 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Autosub In | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 3.51 | 10.27 | 15.80 | 9.00 | 90.0 | 90.0 |
| Bench 4 | Bench | James Justin | DEF | 11 | 3.9 | 2.80 | 8.72 | 13.87 | 2.00 | 83.1 | 86.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.8 | 7.89 | 22.67 | 36.94 | 0.00 | 90.0 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.37 | 13.61 | 22.05 | 2.00 | 68.3 | 90.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 3.80 | 11.09 | 16.88 | 2.00 | 90.0 | 90.0 |
| Vice Captain | Captain | Declan Rice | MID | 1 | 7.6 | 6.07 | 17.63 | 27.64 | 5.00 | 90.0 | 75.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.79 | 16.42 | 26.17 | 8.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.78 | 15.25 | 25.26 | 1.00 | 71.5 | 85.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.64 | 13.01 | 20.34 | 12.00 | 86.2 | 71.0 |
| Bench 3 | Bench | Ilia Gruev | MID | 11 | 4.7 | 2.89 | 8.81 | 13.77 | 2.00 | 79.7 | 74.0 |

## GW29

- Train rows: 182721
- Bank: 1.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 66.63
- Actual score: 84.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.52) beats the best remaining Triple Captain opportunity (7.69).
- Transfer: Yerson Mosquera Valdelamar -> Marc Guéhi (projected gain 2.52, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.52) beats the best remaining Triple Captain opportunity (7.69).
- Autosub: James Hill replaced Harry Wilson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.83 | 11.63 | 18.90 | 7.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.20 | 0.42 | 0.70 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.60 | 16.81 | 26.69 | 11.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.13 | 14.33 | 22.57 | 1.00 | 88.8 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.57 | 12.75 | 20.02 | 1.00 | 89.4 | 90.0 |
| Bench 2 | Autosub In | James Hill | DEF | 4 | 4.0 | 3.58 | 10.25 | 16.04 | 8.00 | 88.3 | 90.0 |
| Bench 3 | Bench | James Justin | DEF | 11 | 3.9 | 2.99 | 8.35 | 13.00 | 2.00 | 81.4 | 73.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.7 | 5.35 | 16.86 | 29.09 | 2.00 | 55.7 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.75 | 14.17 | 23.29 | 19.00 | 77.9 | 84.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 3.58 | 10.26 | 15.70 | 2.00 | 90.0 | 69.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.52 | 18.28 | 28.95 | 7.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.98 | 16.41 | 27.45 | 9.00 | 80.2 | 84.0 |
| XI | XI | Declan Rice | MID | 1 | 7.5 | 4.78 | 14.96 | 24.22 | 3.00 | 89.7 | 90.0 |
| XI | Bench | Harry Wilson | MID | 10 | 5.9 | 4.49 | 12.41 | 19.73 | 0.00 | 76.4 | 0.0 |
| Bench 4 | Bench | Ilia Gruev | MID | 11 | 4.7 | 2.82 | 7.87 | 12.51 | 3.00 | 69.3 | 61.0 |

## GW30

- Train rows: 183541
- Bank: 0.10 -> 0.50
- Free transfers: 2 -> 2
- Captain: João Pedro Junqueira de Jesus
- Vice captain: Antoine Semenyo
- Effective captain: João Pedro Junqueira de Jesus
- Chip used: bench_boost
- Predicted score: 71.51
- Actual score: 51.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.07) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Harry Wilson -> Elliot Anderson (projected gain 5.39, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.07) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.08 | 11.67 | 19.02 | 7.00 | 89.5 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 3.8 | 0.07 | 0.41 | 0.66 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.28 | 15.26 | 25.30 | 9.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.15 | 14.03 | 22.36 | 2.00 | 85.4 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 3.96 | 11.17 | 17.87 | 2.00 | 83.6 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.1 | 4.03 | 10.73 | 17.32 | 8.00 | 86.8 | 90.0 |
| Bench 2 | Bench Boost | James Justin | DEF | 11 | 3.9 | 2.52 | 7.57 | 12.36 | 6.00 | 73.0 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.6 | 6.36 | 19.46 | 32.49 | 2.00 | 84.5 | 90.0 |
| Captain | Captain | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.85 | 18.49 | 29.79 | 2.00 | 90.0 | 90.0 |
| Bench 3 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 2.34 | 6.81 | 11.67 | 1.00 | 61.7 | 45.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 8.1 | 6.44 | 18.40 | 29.08 | 2.00 | 90.0 | 74.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.88 | 17.74 | 29.11 | 2.00 | 85.9 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.4 | 4.88 | 13.95 | 23.09 | 3.00 | 82.6 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.5 | 4.68 | 12.93 | 20.54 | 2.00 | 87.2 | 87.0 |
| Bench 4 | Bench Boost | Ilia Gruev | MID | 11 | 4.7 | 2.14 | 6.58 | 10.90 | 1.00 | 56.4 | 45.0 |