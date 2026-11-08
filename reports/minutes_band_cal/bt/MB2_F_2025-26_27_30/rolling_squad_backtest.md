# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 262.17
- Total actual points: 252.00
- Average predicted points: 65.54
- Average actual points: 63.00
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
- Predicted score: 66.99
- Actual score: 51.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.40 | 12.13 | 19.40 | 3.00 | 83.5 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.00 | 0.03 | 0.00 | 1.5 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 6.53 | 18.24 | 28.20 | 2.00 | 83.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.52 | 12.86 | 20.63 | 11.00 | 83.5 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.41 | 12.01 | 18.38 | 2.00 | 83.5 | 90.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.0 | 3.50 | 10.08 | 15.99 | 6.00 | 83.5 | 90.0 |
| Bench 4 | Bench | James Justin | DEF | 11 | 3.9 | 2.48 | 8.09 | 13.50 | 2.00 | 73.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 6.91 | 19.79 | 32.93 | 6.00 | 83.5 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.12 | 16.10 | 25.33 | 7.00 | 81.7 | 79.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 4.40 | 11.94 | 17.98 | 2.00 | 83.5 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.6 | 6.19 | 17.64 | 27.80 | 4.00 | 83.5 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.92 | 16.20 | 26.31 | 4.00 | 83.5 | 86.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 5.46 | 16.13 | 27.21 | 2.00 | 78.4 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.9 | 5.22 | 14.38 | 23.26 | 2.00 | 81.7 | 90.0 |
| Bench 3 | Bench | Ilia Gruev | MID | 11 | 4.7 | 2.84 | 8.80 | 14.18 | 1.00 | 76.8 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Declan Rice
- Chip used: none
- Predicted score: 61.53
- Actual score: 63.00
- Transfer: none
- No transfer was applied this week.
- Autosub: Mateus Mané replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.60 | 10.28 | 17.00 | 3.00 | 83.4 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.21 | 0.16 | 0.25 | 0.00 | 2.3 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.41 | 15.33 | 24.45 | 9.00 | 83.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.94 | 13.30 | 21.14 | 7.00 | 83.4 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.24 | 12.02 | 18.82 | 6.00 | 82.5 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.0 | 4.01 | 10.68 | 16.52 | 2.00 | 83.4 | 90.0 |
| Bench 4 | Bench | James Justin | DEF | 11 | 3.9 | 2.80 | 8.61 | 13.53 | 2.00 | 80.4 | 86.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.8 | 7.46 | 21.42 | 35.17 | 0.00 | 83.4 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.51 | 14.05 | 22.83 | 2.00 | 72.1 | 90.0 |
| Bench 2 | Autosub In | Mateus Mané | FWD | 20 | 4.6 | 3.46 | 10.19 | 15.79 | 2.00 | 83.4 | 90.0 |
| Vice Captain | Captain | Declan Rice | MID | 1 | 7.6 | 5.70 | 16.63 | 26.35 | 5.00 | 83.4 | 75.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.45 | 15.45 | 24.89 | 8.00 | 83.4 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 5.26 | 15.10 | 25.55 | 13.00 | 79.5 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.8 | 3.48 | 11.52 | 19.47 | 1.00 | 72.8 | 85.0 |
| Bench 3 | Bench | Ilia Gruev | MID | 11 | 4.7 | 2.95 | 8.92 | 13.81 | 2.00 | 78.2 | 74.0 |

## GW29

- Train rows: 182721
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Bruno Borges Fernandes
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 63.88
- Actual score: 79.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.19) beats the best remaining Triple Captain opportunity (7.56).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.19) beats the best remaining Triple Captain opportunity (7.56).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.41 | 10.45 | 17.26 | 7.00 | 83.5 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.06 | 0.06 | 0.13 | 0.00 | 0.5 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.25 | 15.81 | 25.33 | 11.00 | 83.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.72 | 13.11 | 20.82 | 1.00 | 81.2 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.22 | 11.74 | 18.64 | 1.00 | 82.3 | 90.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.0 | 3.21 | 9.19 | 14.59 | 8.00 | 81.7 | 90.0 |
| Bench 3 | Bench | James Justin | DEF | 11 | 3.9 | 2.99 | 8.25 | 12.69 | 2.00 | 78.8 | 73.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.7 | 5.51 | 17.29 | 29.69 | 2.00 | 58.9 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.85 | 14.48 | 23.85 | 19.00 | 78.8 | 84.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 3.25 | 9.39 | 14.64 | 2.00 | 83.5 | 69.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.19 | 17.34 | 27.69 | 7.00 | 83.5 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.9 | 6.16 | 17.15 | 28.52 | 8.00 | 83.5 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.5 | 4.42 | 13.99 | 22.95 | 3.00 | 83.5 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 3.53 | 11.30 | 18.90 | 4.00 | 74.1 | 78.0 |
| Bench 4 | Bench | Ilia Gruev | MID | 11 | 4.7 | 2.94 | 8.22 | 13.13 | 3.00 | 73.1 | 61.0 |

## GW30

- Train rows: 183541
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: João Pedro Junqueira de Jesus
- Vice captain: Bruno Borges Fernandes
- Effective captain: João Pedro Junqueira de Jesus
- Chip used: bench_boost
- Predicted score: 69.78
- Actual score: 59.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.35) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.35) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.66 | 10.47 | 17.33 | 7.00 | 83.4 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.02 | 0.07 | 0.00 | 1.3 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 4.92 | 14.21 | 23.83 | 9.00 | 83.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.17 | 13.94 | 22.03 | 2.00 | 82.3 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.05 | 11.31 | 17.97 | 2.00 | 81.1 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.1 | 3.66 | 9.66 | 15.83 | 8.00 | 80.2 | 90.0 |
| Bench 2 | Bench Boost | James Justin | DEF | 11 | 3.9 | 2.52 | 7.54 | 12.30 | 6.00 | 72.7 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.6 | 6.37 | 19.35 | 32.15 | 2.00 | 81.9 | 90.0 |
| Captain | Captain | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.54 | 17.61 | 28.63 | 2.00 | 83.4 | 90.0 |
| Bench 3 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 2.49 | 7.32 | 12.60 | 1.00 | 66.8 | 45.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.9 | 6.37 | 19.04 | 31.15 | 10.00 | 83.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 6.12 | 17.48 | 27.84 | 2.00 | 83.4 | 74.0 |
| XI | XI | Declan Rice | MID | 1 | 7.4 | 4.96 | 14.12 | 23.29 | 3.00 | 82.5 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.6 | 4.09 | 12.17 | 19.84 | 2.00 | 76.7 | 90.0 |
| Bench 4 | Bench Boost | Ilia Gruev | MID | 11 | 4.7 | 2.34 | 7.17 | 11.82 | 1.00 | 61.1 | 45.0 |