# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 274.08
- Total actual points: 247.00
- Average predicted points: 68.52
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
- Predicted score: 71.28
- Actual score: 54.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.81 | 13.28 | 21.01 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.02 | 0.17 | 0.00 | 2.4 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 6.94 | 19.46 | 29.94 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.94 | 14.06 | 22.34 | 11.00 | 90.0 | 90.0 |
| XI | XI | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 4.20 | 11.52 | 17.99 | 4.00 | 90.0 | 90.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.0 | 3.92 | 11.30 | 17.72 | 6.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Reinildo Mandava | DEF | 17 | 3.8 | 2.62 | 7.07 | 10.84 | 0.00 | 70.7 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 7.31 | 20.85 | 34.35 | 6.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.10 | 16.15 | 25.53 | 7.00 | 83.5 | 79.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 4.82 | 13.20 | 19.79 | 2.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.6 | 6.61 | 18.85 | 29.52 | 4.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 6.71 | 18.01 | 29.20 | 3.00 | 87.5 | 74.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 6.34 | 17.40 | 28.01 | 4.00 | 90.0 | 86.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.9 | 5.20 | 14.43 | 23.46 | 2.00 | 83.4 | 90.0 |
| Bench 3 | Bench | Enzo Le Fée | MID | 17 | 4.9 | 3.65 | 10.44 | 16.41 | 10.00 | 87.2 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 0.00 -> 0.90
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Declan Rice
- Chip used: none
- Predicted score: 65.00
- Actual score: 65.00
- Transfer: Enzo Fernández -> Harry Wilson (projected gain 3.10, hit 0)
- Autosub: Yerson Mosquera Valdelamar replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.01 | 11.40 | 18.50 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.25 | 0.27 | 0.41 | 0.00 | 3.3 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.82 | 16.50 | 26.07 | 9.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.36 | 14.53 | 22.86 | 7.00 | 90.0 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.0 | 4.43 | 11.89 | 18.21 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Autosub In | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 3.47 | 10.12 | 15.53 | 9.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Reinildo Mandava | DEF | 17 | 3.8 | 1.02 | 3.63 | 6.02 | 0.00 | 39.3 | 0.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.8 | 7.86 | 22.56 | 36.71 | 0.00 | 90.0 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.42 | 13.76 | 22.33 | 2.00 | 68.6 | 90.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 3.88 | 11.41 | 17.51 | 2.00 | 90.0 | 90.0 |
| Vice Captain | Captain | Declan Rice | MID | 1 | 7.6 | 6.12 | 17.80 | 27.96 | 5.00 | 90.0 | 75.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.87 | 16.64 | 26.53 | 8.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.67 | 14.85 | 24.51 | 1.00 | 70.0 | 85.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.70 | 13.21 | 20.71 | 12.00 | 87.1 | 71.0 |
| Bench 3 | Bench | Enzo Le Fée | MID | 17 | 4.9 | 3.13 | 9.52 | 16.06 | 2.00 | 82.8 | 90.0 |

## GW29

- Train rows: 182721
- Bank: 0.90 -> 0.00
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 67.07
- Actual score: 84.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.60) beats the best remaining Triple Captain opportunity (7.78).
- Transfer: Yerson Mosquera Valdelamar -> Marc Guéhi (projected gain 2.55, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.60) beats the best remaining Triple Captain opportunity (7.78).
- Autosub: James Hill replaced Harry Wilson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.81 | 11.56 | 18.77 | 7.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.11 | 0.17 | 0.30 | 0.00 | 1.6 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.65 | 16.96 | 26.94 | 11.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.12 | 14.28 | 22.47 | 1.00 | 87.7 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.63 | 12.91 | 20.28 | 1.00 | 88.7 | 90.0 |
| Bench 2 | Autosub In | James Hill | DEF | 4 | 4.0 | 3.61 | 10.37 | 16.27 | 8.00 | 88.3 | 90.0 |
| Bench 4 | Bench | Reinildo Mandava | DEF | 17 | 3.8 | 0.76 | 2.49 | 4.92 | 0.00 | 27.9 | 0.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.7 | 5.31 | 16.62 | 28.61 | 2.00 | 54.3 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.84 | 14.46 | 23.81 | 19.00 | 78.3 | 84.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 3.66 | 10.56 | 16.32 | 2.00 | 90.0 | 69.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.60 | 18.51 | 29.34 | 7.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.89 | 16.06 | 26.80 | 9.00 | 78.5 | 84.0 |
| XI | XI | Declan Rice | MID | 1 | 7.5 | 4.82 | 15.10 | 24.49 | 3.00 | 90.0 | 90.0 |
| XI | Bench | Harry Wilson | MID | 10 | 5.9 | 4.55 | 12.59 | 20.04 | 0.00 | 76.9 | 0.0 |
| Bench 3 | Bench | Enzo Le Fée | MID | 17 | 4.9 | 3.49 | 9.74 | 16.10 | 5.00 | 82.6 | 90.0 |

## GW30

- Train rows: 183541
- Bank: 0.00 -> 0.40
- Free transfers: 2 -> 2
- Captain: João Pedro Junqueira de Jesus
- Vice captain: Antoine Semenyo
- Effective captain: João Pedro Junqueira de Jesus
- Chip used: bench_boost
- Predicted score: 70.74
- Actual score: 44.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.98) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Harry Wilson -> Elliot Anderson (projected gain 3.02, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.98) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.06 | 11.58 | 18.88 | 7.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.14 | 0.24 | 0.00 | 2.3 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.32 | 15.38 | 25.50 | 9.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.14 | 13.98 | 22.23 | 2.00 | 84.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.02 | 11.35 | 18.17 | 2.00 | 82.9 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.1 | 4.06 | 10.86 | 17.56 | 8.00 | 86.8 | 90.0 |
| Bench 4 | Bench Boost | Reinildo Mandava | DEF | 17 | 3.8 | 0.00 | 0.00 | 1.28 | 0.00 | 4.8 | 0.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.6 | 6.34 | 19.33 | 32.24 | 2.00 | 83.6 | 90.0 |
| Captain | Captain | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.94 | 18.77 | 30.30 | 2.00 | 90.0 | 90.0 |
| Bench 3 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 2.41 | 7.12 | 12.26 | 1.00 | 63.6 | 45.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 8.1 | 6.52 | 18.64 | 29.48 | 2.00 | 90.0 | 74.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.79 | 17.40 | 28.47 | 2.00 | 84.2 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.4 | 4.93 | 14.14 | 23.46 | 3.00 | 84.2 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.5 | 4.70 | 13.02 | 20.74 | 2.00 | 88.7 | 87.0 |
| Bench 2 | Bench Boost | Enzo Le Fée | MID | 17 | 4.9 | 3.57 | 10.15 | 16.55 | 0.00 | 83.9 | 0.0 |