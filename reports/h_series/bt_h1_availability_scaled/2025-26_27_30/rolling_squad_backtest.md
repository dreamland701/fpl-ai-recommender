# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 279.22
- Total actual points: 258.00
- Average predicted points: 69.81
- Average actual points: 64.50
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
- Predicted score: 70.94
- Actual score: 51.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.75 | 13.16 | 20.83 | 3.00 | 89.9 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.00 | 0.11 | 0.00 | 2.4 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 6.81 | 19.07 | 29.33 | 2.00 | 90.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.89 | 13.93 | 22.14 | 11.00 | 90.1 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.76 | 13.04 | 19.82 | 2.00 | 90.6 | 90.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.0 | 3.86 | 11.12 | 17.44 | 6.00 | 91.3 | 90.0 |
| Bench 4 | Bench | James Justin | DEF | 11 | 3.9 | 2.47 | 8.08 | 13.48 | 2.00 | 72.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 7.16 | 20.53 | 33.88 | 6.00 | 86.6 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.42 | 16.99 | 26.87 | 7.00 | 84.6 | 79.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 4.73 | 12.92 | 19.35 | 2.00 | 89.9 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.6 | 6.56 | 18.71 | 29.31 | 4.00 | 91.6 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 5.92 | 17.59 | 29.83 | 2.00 | 81.6 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 6.28 | 17.24 | 27.75 | 4.00 | 90.7 | 86.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.9 | 5.50 | 15.27 | 24.83 | 2.00 | 85.2 | 90.0 |
| Bench 3 | Bench | Ilia Gruev | MID | 11 | 4.7 | 2.84 | 8.80 | 14.16 | 1.00 | 76.4 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Declan Rice
- Chip used: none
- Predicted score: 66.11
- Actual score: 63.00
- Transfer: none
- No transfer was applied this week.
- Autosub: Mateus Mané replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.97 | 11.35 | 18.46 | 3.00 | 89.7 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.25 | 0.24 | 0.34 | 0.00 | 3.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.77 | 16.36 | 25.86 | 9.00 | 92.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.30 | 14.35 | 22.58 | 7.00 | 90.5 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.40 | 12.56 | 19.81 | 6.00 | 85.7 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.0 | 4.38 | 11.77 | 18.04 | 2.00 | 90.7 | 90.0 |
| Bench 4 | Bench | James Justin | DEF | 11 | 3.9 | 2.78 | 8.66 | 13.76 | 2.00 | 82.2 | 86.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.8 | 7.73 | 22.22 | 36.20 | 0.00 | 87.8 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.21 | 16.28 | 26.44 | 2.00 | 70.3 | 90.0 |
| Bench 2 | Autosub In | Mateus Mané | FWD | 20 | 4.6 | 3.81 | 11.22 | 17.21 | 2.00 | 88.9 | 90.0 |
| Vice Captain | Captain | Declan Rice | MID | 1 | 7.6 | 6.04 | 17.61 | 27.69 | 5.00 | 90.1 | 75.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 5.84 | 16.79 | 28.04 | 13.00 | 87.5 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.81 | 16.50 | 26.32 | 8.00 | 91.8 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.8 | 3.94 | 13.11 | 22.14 | 1.00 | 72.0 | 85.0 |
| Bench 3 | Bench | Ilia Gruev | MID | 11 | 4.7 | 3.14 | 9.58 | 15.01 | 2.00 | 82.4 | 74.0 |

## GW29

- Train rows: 182721
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Bruno Borges Fernandes
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 69.28
- Actual score: 85.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.53) beats the best remaining Triple Captain opportunity (7.98).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.53) beats the best remaining Triple Captain opportunity (7.98).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.76 | 11.45 | 18.65 | 7.00 | 90.5 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.10 | 0.14 | 0.24 | 0.00 | 1.5 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.57 | 16.72 | 26.57 | 11.00 | 90.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.20 | 14.50 | 22.83 | 1.00 | 88.7 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.66 | 13.00 | 20.43 | 1.00 | 90.9 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.0 | 3.65 | 10.48 | 16.45 | 8.00 | 89.5 | 90.0 |
| Bench 3 | Bench | James Justin | DEF | 11 | 3.9 | 2.98 | 8.31 | 12.93 | 2.00 | 80.6 | 73.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.7 | 6.35 | 20.00 | 34.48 | 2.00 | 55.4 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 5.24 | 15.66 | 25.79 | 19.00 | 80.1 | 84.0 |
| Bench 2 | Bench | Mateus Mané | FWD | 20 | 4.6 | 3.61 | 10.43 | 16.09 | 2.00 | 89.9 | 69.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.53 | 18.35 | 29.09 | 7.00 | 91.3 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.9 | 6.51 | 18.17 | 29.92 | 8.00 | 89.7 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.5 | 4.73 | 14.84 | 24.10 | 3.00 | 90.1 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 4.02 | 12.93 | 21.63 | 4.00 | 73.8 | 78.0 |
| Bench 4 | Bench | Ilia Gruev | MID | 11 | 4.7 | 2.86 | 8.01 | 12.78 | 3.00 | 69.8 | 61.0 |

## GW30

- Train rows: 183541
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: João Pedro Junqueira de Jesus
- Vice captain: Bruno Borges Fernandes
- Effective captain: João Pedro Junqueira de Jesus
- Chip used: bench_boost
- Predicted score: 72.89
- Actual score: 59.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.09) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.09) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.97 | 11.37 | 18.57 | 7.00 | 88.6 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.11 | 0.17 | 0.00 | 2.3 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.19 | 15.01 | 24.89 | 9.00 | 89.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.34 | 14.52 | 23.10 | 2.00 | 85.3 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.12 | 11.63 | 18.63 | 2.00 | 83.5 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.1 | 4.15 | 11.08 | 17.91 | 8.00 | 88.0 | 90.0 |
| Bench 2 | Bench Boost | James Justin | DEF | 11 | 3.9 | 2.51 | 7.54 | 12.30 | 6.00 | 72.2 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.6 | 6.54 | 20.01 | 33.40 | 2.00 | 82.6 | 90.0 |
| Captain | Captain | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.84 | 18.51 | 29.88 | 2.00 | 88.7 | 90.0 |
| Bench 3 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 2.41 | 7.11 | 12.24 | 1.00 | 63.6 | 45.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.9 | 6.73 | 20.10 | 32.64 | 10.00 | 90.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 6.42 | 18.37 | 29.08 | 2.00 | 89.7 | 74.0 |
| XI | XI | Declan Rice | MID | 1 | 7.4 | 5.10 | 14.64 | 24.30 | 3.00 | 85.4 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.6 | 4.56 | 13.59 | 22.15 | 2.00 | 79.0 | 90.0 |
| Bench 4 | Bench Boost | Ilia Gruev | MID | 11 | 4.7 | 2.17 | 6.68 | 11.09 | 1.00 | 57.0 | 45.0 |