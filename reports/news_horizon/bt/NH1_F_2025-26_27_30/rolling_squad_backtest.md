# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 274.30
- Total actual points: 247.00
- Average predicted points: 68.58
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
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 71.26
- Actual score: 54.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.80 | 13.29 | 21.03 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.00 | 0.18 | 0.00 | 2.1 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 6.93 | 19.45 | 29.95 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.93 | 14.06 | 22.35 | 11.00 | 90.0 | 90.0 |
| XI | XI | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 4.18 | 11.51 | 18.01 | 4.00 | 90.0 | 90.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.0 | 3.91 | 11.29 | 17.72 | 6.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Reinildo Mandava | DEF | 17 | 3.8 | 2.59 | 7.05 | 10.86 | 0.00 | 70.1 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 7.36 | 20.90 | 34.33 | 6.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.09 | 16.14 | 25.54 | 7.00 | 83.3 | 79.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 4.80 | 13.18 | 19.81 | 2.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.6 | 6.57 | 18.82 | 29.56 | 4.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 6.70 | 18.00 | 29.21 | 3.00 | 87.4 | 74.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 6.32 | 17.39 | 28.03 | 4.00 | 90.0 | 86.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.9 | 5.20 | 14.43 | 23.46 | 2.00 | 83.5 | 90.0 |
| Bench 3 | Bench | Enzo Le Fée | MID | 17 | 4.9 | 3.65 | 10.44 | 16.41 | 10.00 | 87.2 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 0.00 -> 0.90
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Declan Rice
- Chip used: none
- Predicted score: 65.12
- Actual score: 65.00
- Transfer: Enzo Fernández -> Harry Wilson (projected gain 3.09, hit 0)
- Autosub: Yerson Mosquera Valdelamar replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.03 | 11.43 | 18.51 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.24 | 0.25 | 0.41 | 0.00 | 2.9 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.83 | 16.52 | 26.09 | 9.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.34 | 14.51 | 22.89 | 7.00 | 90.0 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.0 | 4.43 | 11.89 | 18.21 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Autosub In | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 3.47 | 10.13 | 15.54 | 9.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Reinildo Mandava | DEF | 17 | 3.8 | 1.02 | 3.64 | 6.03 | 0.00 | 39.5 | 0.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.8 | 7.91 | 22.59 | 36.68 | 0.00 | 90.0 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.42 | 13.78 | 22.35 | 2.00 | 68.6 | 90.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 3.87 | 11.41 | 17.53 | 2.00 | 90.0 | 90.0 |
| Vice Captain | Captain | Declan Rice | MID | 1 | 7.6 | 6.14 | 17.82 | 27.96 | 5.00 | 90.0 | 75.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.86 | 16.64 | 26.56 | 8.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.69 | 14.87 | 24.52 | 1.00 | 70.4 | 85.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.70 | 13.21 | 20.69 | 12.00 | 87.1 | 71.0 |
| Bench 3 | Bench | Enzo Le Fée | MID | 17 | 4.9 | 3.11 | 9.51 | 16.07 | 2.00 | 82.5 | 90.0 |

## GW29

- Train rows: 182721
- Bank: 0.90 -> 0.00
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 67.16
- Actual score: 84.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.58) beats the best remaining Triple Captain opportunity (7.77).
- Transfer: Yerson Mosquera Valdelamar -> Marc Guéhi (projected gain 2.55, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.58) beats the best remaining Triple Captain opportunity (7.77).
- Autosub: James Hill replaced Harry Wilson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.83 | 11.59 | 18.78 | 7.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.09 | 0.16 | 0.31 | 0.00 | 1.2 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.66 | 16.97 | 26.95 | 11.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.11 | 14.28 | 22.50 | 1.00 | 87.4 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.62 | 12.90 | 20.30 | 1.00 | 88.5 | 90.0 |
| Bench 2 | Autosub In | James Hill | DEF | 4 | 4.0 | 3.62 | 10.38 | 16.27 | 8.00 | 88.5 | 90.0 |
| Bench 4 | Bench | Reinildo Mandava | DEF | 17 | 3.8 | 0.77 | 2.50 | 4.91 | 0.00 | 28.1 | 0.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.7 | 5.38 | 16.69 | 28.58 | 2.00 | 55.9 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.86 | 14.48 | 23.81 | 19.00 | 78.7 | 84.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 3.65 | 10.57 | 16.33 | 2.00 | 90.0 | 69.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.58 | 18.51 | 29.37 | 7.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.90 | 16.07 | 26.79 | 9.00 | 78.8 | 84.0 |
| XI | XI | Declan Rice | MID | 1 | 7.5 | 4.86 | 15.13 | 24.48 | 3.00 | 90.0 | 90.0 |
| XI | Bench | Harry Wilson | MID | 10 | 5.9 | 4.55 | 12.59 | 20.05 | 0.00 | 76.8 | 0.0 |
| Bench 3 | Bench | Enzo Le Fée | MID | 17 | 4.9 | 3.47 | 9.72 | 16.11 | 5.00 | 82.1 | 90.0 |

## GW30

- Train rows: 183541
- Bank: 0.00 -> 0.40
- Free transfers: 2 -> 2
- Captain: João Pedro Junqueira de Jesus
- Vice captain: Antoine Semenyo
- Effective captain: João Pedro Junqueira de Jesus
- Chip used: bench_boost
- Predicted score: 70.76
- Actual score: 44.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.97) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Harry Wilson -> Elliot Anderson (projected gain 3.01, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.97) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.08 | 11.61 | 18.88 | 7.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.13 | 0.24 | 0.00 | 2.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.31 | 15.37 | 25.52 | 9.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.13 | 13.97 | 22.25 | 2.00 | 83.8 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.00 | 11.34 | 18.20 | 2.00 | 82.5 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.1 | 4.04 | 10.85 | 17.58 | 8.00 | 86.4 | 90.0 |
| Bench 4 | Bench Boost | Reinildo Mandava | DEF | 17 | 3.8 | 0.00 | 0.00 | 1.59 | 0.00 | 0.0 | 0.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.6 | 6.42 | 19.39 | 32.16 | 2.00 | 85.4 | 90.0 |
| Captain | Captain | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.92 | 18.76 | 30.33 | 2.00 | 90.0 | 90.0 |
| Bench 3 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 2.41 | 7.12 | 12.27 | 1.00 | 63.4 | 45.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 8.1 | 6.51 | 18.63 | 29.50 | 2.00 | 90.0 | 74.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.81 | 17.42 | 28.46 | 2.00 | 84.6 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.4 | 4.97 | 14.17 | 23.44 | 3.00 | 85.0 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.5 | 4.69 | 13.01 | 20.75 | 2.00 | 88.5 | 87.0 |
| Bench 2 | Bench Boost | Enzo Le Fée | MID | 17 | 4.9 | 3.56 | 10.15 | 16.56 | 0.00 | 83.8 | 0.0 |