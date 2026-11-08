# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 279.00
- Total actual points: 247.00
- Average predicted points: 69.75
- Average actual points: 61.75
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
- Captain: Erling Haaland
- Vice captain: Cole Palmer
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 73.90
- Actual score: 54.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.84 | 13.41 | 21.20 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.00 | 0.11 | 0.00 | 2.3 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 6.95 | 19.48 | 29.92 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.91 | 13.99 | 22.22 | 11.00 | 90.0 | 90.0 |
| XI | XI | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 4.18 | 11.46 | 17.87 | 4.00 | 90.0 | 90.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.0 | 3.90 | 11.24 | 17.62 | 6.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Reinildo Mandava | DEF | 17 | 3.8 | 2.61 | 7.04 | 10.76 | 0.00 | 70.5 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.17 | 23.98 | 38.04 | 6.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.39 | 16.75 | 26.52 | 7.00 | 89.4 | 79.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 4.80 | 13.10 | 19.60 | 2.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.6 | 6.66 | 18.99 | 29.66 | 4.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.6 | 6.99 | 18.62 | 30.15 | 3.00 | 90.0 | 74.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 6.62 | 18.00 | 28.99 | 4.00 | 90.0 | 86.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.9 | 5.23 | 14.52 | 23.54 | 2.00 | 83.6 | 90.0 |
| Bench 3 | Bench | Enzo Le Fée | MID | 17 | 4.9 | 3.65 | 10.43 | 16.36 | 10.00 | 87.1 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 0.00 -> 0.90
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Declan Rice
- Chip used: none
- Predicted score: 66.32
- Actual score: 65.00
- Transfer: Enzo Fernández -> Harry Wilson (projected gain 1.67, hit 0)
- Autosub: Yerson Mosquera Valdelamar replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.06 | 11.59 | 18.80 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.25 | 0.24 | 0.35 | 0.00 | 3.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.85 | 16.59 | 26.17 | 9.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.61 | 15.14 | 23.85 | 7.00 | 90.0 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.0 | 4.41 | 11.87 | 18.17 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Autosub In | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 3.47 | 10.11 | 15.51 | 9.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Reinildo Mandava | DEF | 17 | 3.8 | 1.03 | 3.68 | 6.08 | 0.00 | 39.6 | 0.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.8 | 8.33 | 23.36 | 38.76 | 0.00 | 90.0 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.46 | 13.94 | 22.56 | 2.00 | 68.9 | 90.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 3.87 | 11.37 | 17.41 | 2.00 | 90.0 | 90.0 |
| Vice Captain | Captain | Declan Rice | MID | 1 | 7.6 | 6.17 | 17.96 | 28.15 | 5.00 | 90.0 | 75.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.85 | 16.63 | 26.49 | 8.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.70 | 14.97 | 24.63 | 1.00 | 70.1 | 85.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.68 | 13.17 | 20.61 | 12.00 | 86.7 | 71.0 |
| Bench 3 | Bench | Enzo Le Fée | MID | 17 | 4.9 | 3.13 | 9.51 | 16.00 | 2.00 | 82.8 | 90.0 |

## GW29

- Train rows: 182721
- Bank: 0.90 -> 0.00
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 67.68
- Actual score: 84.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.89) beats the best remaining Triple Captain opportunity (8.13).
- Transfer: Yerson Mosquera Valdelamar -> Marc Guéhi (projected gain 2.58, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.89) beats the best remaining Triple Captain opportunity (8.13).
- Autosub: James Hill replaced Harry Wilson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.84 | 11.69 | 19.00 | 7.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.10 | 0.14 | 0.23 | 0.00 | 1.5 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.66 | 17.01 | 26.99 | 11.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.43 | 14.88 | 23.49 | 1.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.63 | 12.93 | 20.29 | 1.00 | 88.5 | 90.0 |
| Bench 2 | Autosub In | James Hill | DEF | 4 | 4.0 | 3.61 | 10.36 | 16.24 | 8.00 | 88.0 | 90.0 |
| Bench 4 | Bench | Reinildo Mandava | DEF | 17 | 3.8 | 0.78 | 2.52 | 4.95 | 0.00 | 28.2 | 0.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.7 | 4.59 | 15.30 | 27.26 | 2.00 | 40.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.86 | 14.53 | 23.86 | 19.00 | 78.4 | 84.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 3.65 | 10.56 | 16.27 | 2.00 | 90.0 | 69.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.89 | 19.08 | 30.31 | 7.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.91 | 16.11 | 26.81 | 9.00 | 78.5 | 84.0 |
| XI | XI | Declan Rice | MID | 1 | 7.5 | 4.90 | 15.32 | 24.80 | 3.00 | 90.0 | 90.0 |
| XI | Bench | Harry Wilson | MID | 10 | 5.9 | 4.55 | 12.63 | 20.07 | 0.00 | 76.8 | 0.0 |
| Bench 3 | Bench | Enzo Le Fée | MID | 17 | 4.9 | 3.49 | 9.72 | 16.02 | 5.00 | 82.5 | 90.0 |

## GW30

- Train rows: 183541
- Bank: 0.00 -> 0.40
- Free transfers: 2 -> 2
- Captain: João Pedro Junqueira de Jesus
- Vice captain: Antoine Semenyo
- Effective captain: João Pedro Junqueira de Jesus
- Chip used: bench_boost
- Predicted score: 71.10
- Actual score: 44.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.98) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Harry Wilson -> Elliot Anderson (projected gain 3.01, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.98) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.07 | 11.68 | 19.04 | 7.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.11 | 0.17 | 0.00 | 2.3 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.34 | 15.44 | 25.57 | 9.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.15 | 14.02 | 22.26 | 2.00 | 83.9 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.03 | 11.38 | 18.20 | 2.00 | 82.8 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.1 | 4.07 | 10.87 | 17.54 | 8.00 | 86.8 | 90.0 |
| Bench 4 | Bench Boost | Reinildo Mandava | DEF | 17 | 3.8 | 0.00 | 0.00 | 1.34 | 0.00 | 0.0 | 0.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.6 | 6.44 | 19.62 | 32.60 | 2.00 | 85.0 | 90.0 |
| Captain | Captain | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.90 | 18.72 | 30.15 | 2.00 | 90.0 | 90.0 |
| Bench 3 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 2.42 | 7.12 | 12.24 | 1.00 | 63.7 | 45.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 8.1 | 6.71 | 19.49 | 31.40 | 2.00 | 90.0 | 74.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.83 | 17.53 | 28.61 | 2.00 | 84.7 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.4 | 4.99 | 14.30 | 23.65 | 3.00 | 85.1 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.5 | 4.69 | 13.00 | 20.68 | 2.00 | 88.5 | 87.0 |
| Bench 2 | Bench Boost | Enzo Le Fée | MID | 17 | 4.9 | 3.57 | 10.14 | 16.50 | 0.00 | 83.8 | 0.0 |