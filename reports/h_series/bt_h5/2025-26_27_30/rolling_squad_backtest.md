# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 274.82
- Total actual points: 294.00
- Average predicted points: 68.70
- Average actual points: 73.50
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
- Predicted score: 69.37
- Actual score: 51.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.85 | 13.63 | 21.40 | 3.00 | 89.7 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.00 | 0.11 | 0.00 | 2.4 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 6.81 | 19.44 | 29.86 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.92 | 13.78 | 22.13 | 11.00 | 90.7 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.70 | 13.34 | 20.24 | 2.00 | 90.5 | 90.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.0 | 3.80 | 11.19 | 17.63 | 6.00 | 87.4 | 90.0 |
| Bench 4 | Bench | James Justin | DEF | 11 | 3.9 | 2.47 | 8.08 | 13.48 | 2.00 | 72.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 6.95 | 20.20 | 33.10 | 6.00 | 84.8 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.09 | 16.47 | 25.76 | 7.00 | 84.6 | 79.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 4.66 | 12.94 | 18.92 | 2.00 | 88.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.6 | 6.57 | 19.32 | 30.16 | 4.00 | 91.3 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 6.26 | 17.37 | 27.98 | 4.00 | 90.5 | 86.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 5.50 | 16.61 | 27.56 | 2.00 | 79.8 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.9 | 5.11 | 14.59 | 23.26 | 2.00 | 85.1 | 90.0 |
| Bench 3 | Bench | Ilia Gruev | MID | 11 | 4.7 | 2.84 | 8.80 | 14.16 | 1.00 | 76.4 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 0.00 -> 0.90
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Declan Rice
- Chip used: none
- Predicted score: 65.21
- Actual score: 74.00
- Transfer: Enzo Fernández -> Harry Wilson (projected gain 2.76, hit 0)
- Autosub: Mateus Mané replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.06 | 11.67 | 19.09 | 3.00 | 89.8 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.25 | 0.24 | 0.34 | 0.00 | 3.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.67 | 16.32 | 25.82 | 9.00 | 88.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.22 | 14.34 | 22.31 | 7.00 | 90.6 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.16 | 12.22 | 19.23 | 6.00 | 86.1 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.0 | 4.43 | 11.81 | 18.03 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | James Justin | DEF | 11 | 3.9 | 2.78 | 8.66 | 13.76 | 2.00 | 82.2 | 86.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.8 | 7.58 | 21.63 | 35.12 | 0.00 | 84.2 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.27 | 13.77 | 21.87 | 2.00 | 69.1 | 90.0 |
| Bench 2 | Autosub In | Mateus Mané | FWD | 20 | 4.6 | 3.65 | 10.50 | 15.83 | 2.00 | 86.4 | 90.0 |
| Vice Captain | Captain | Declan Rice | MID | 1 | 7.6 | 6.05 | 17.86 | 28.05 | 5.00 | 89.7 | 75.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 5.67 | 16.55 | 27.33 | 13.00 | 86.6 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.72 | 16.22 | 26.03 | 8.00 | 90.2 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.79 | 13.22 | 20.33 | 12.00 | 87.3 | 71.0 |
| Bench 3 | Bench | Ilia Gruev | MID | 11 | 4.7 | 2.87 | 8.78 | 13.08 | 2.00 | 79.7 | 74.0 |

## GW29

- Train rows: 182721
- Bank: 0.90 -> 0.20
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Antoine Semenyo
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 67.47
- Actual score: 95.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.51) beats the best remaining Triple Captain opportunity (7.99).
- Transfer: Ilia Gruev -> Elliot Anderson (projected gain 1.51, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (6.51) beats the best remaining Triple Captain opportunity (7.99).
- Autosub: James Hill replaced Harry Wilson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.77 | 11.68 | 19.50 | 7.00 | 89.6 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.10 | 0.14 | 0.24 | 0.00 | 1.5 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.47 | 16.86 | 26.85 | 11.00 | 88.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.03 | 14.04 | 22.03 | 1.00 | 87.6 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.50 | 12.75 | 20.26 | 1.00 | 88.8 | 90.0 |
| Bench 2 | Autosub In | James Hill | DEF | 4 | 4.0 | 3.58 | 10.16 | 15.94 | 8.00 | 88.6 | 90.0 |
| Bench 4 | Bench | James Justin | DEF | 11 | 3.9 | 2.98 | 8.31 | 12.93 | 2.00 | 80.6 | 73.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.7 | 5.01 | 15.99 | 27.58 | 2.00 | 50.8 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.80 | 14.56 | 23.62 | 19.00 | 78.7 | 84.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.6 | 3.41 | 9.71 | 14.79 | 2.00 | 86.0 | 69.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.9 | 6.51 | 18.19 | 29.87 | 8.00 | 88.7 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 8.1 | 6.50 | 18.13 | 28.94 | 7.00 | 88.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.5 | 4.53 | 14.41 | 23.95 | 3.00 | 86.3 | 90.0 |
| XI | Bench | Harry Wilson | MID | 10 | 5.9 | 4.53 | 12.87 | 19.93 | 0.00 | 78.2 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.83 | 11.62 | 18.58 | 12.00 | 78.6 | 90.0 |

## GW30

- Train rows: 183541
- Bank: 0.20 -> 0.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 72.77
- Actual score: 74.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.72) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Harry Wilson -> Dango Ouattara (projected gain 0.17, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.72) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.99 | 11.28 | 18.81 | 7.00 | 88.6 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.11 | 0.17 | 0.00 | 2.3 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.06 | 14.71 | 24.75 | 9.00 | 88.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.94 | 13.47 | 21.44 | 2.00 | 84.1 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 3.84 | 11.03 | 17.93 | 2.00 | 81.8 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.1 | 3.97 | 10.49 | 17.10 | 8.00 | 86.5 | 90.0 |
| Bench 3 | Bench Boost | James Justin | DEF | 11 | 3.9 | 2.51 | 7.54 | 12.30 | 6.00 | 72.2 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.6 | 6.09 | 18.87 | 31.75 | 2.00 | 81.4 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.72 | 18.45 | 29.89 | 2.00 | 87.2 | 90.0 |
| Bench 4 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 2.41 | 7.11 | 12.24 | 1.00 | 63.6 | 45.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.9 | 6.83 | 20.25 | 32.79 | 10.00 | 89.2 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 6.34 | 17.85 | 28.58 | 2.00 | 86.7 | 74.0 |
| XI | XI | Declan Rice | MID | 1 | 7.4 | 4.85 | 14.10 | 23.47 | 3.00 | 83.8 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.56 | 12.68 | 20.25 | 2.00 | 86.7 | 87.0 |
| Bench 2 | Bench Boost | Dango Ouattara | MID | 5 | 6.0 | 3.80 | 10.54 | 16.58 | 8.00 | 75.1 | 84.0 |