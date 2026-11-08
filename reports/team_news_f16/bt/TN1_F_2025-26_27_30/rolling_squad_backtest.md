# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 279.53
- Total actual points: 281.00
- Average predicted points: 69.88
- Average actual points: 70.25
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
- Predicted score: 70.86
- Actual score: 51.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.80 | 13.32 | 21.07 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.10 | 0.17 | 0.29 | 0.00 | 5.2 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 6.94 | 19.43 | 29.87 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.97 | 14.12 | 22.38 | 11.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.85 | 13.25 | 20.11 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.0 | 3.94 | 11.33 | 17.72 | 6.00 | 90.0 | 90.0 |
| Bench 4 | Bench | James Justin | DEF | 11 | 3.9 | 2.28 | 7.77 | 13.11 | 2.00 | 66.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 7.39 | 21.10 | 34.71 | 6.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.17 | 16.27 | 25.64 | 7.00 | 85.4 | 79.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 4.79 | 13.09 | 19.61 | 2.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.6 | 6.58 | 18.79 | 29.43 | 4.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 6.36 | 17.44 | 28.03 | 4.00 | 90.0 | 86.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 5.38 | 16.06 | 27.35 | 2.00 | 78.4 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.9 | 5.24 | 14.50 | 23.51 | 2.00 | 84.5 | 90.0 |
| Bench 3 | Bench | Ilia Gruev | MID | 11 | 4.7 | 2.88 | 8.87 | 14.21 | 1.00 | 77.6 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 0.00 -> 0.90
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Declan Rice
- Chip used: none
- Predicted score: 66.67
- Actual score: 74.00
- Transfer: Enzo Fernández -> Harry Wilson (projected gain 2.06, hit 0)
- Autosub: Mateus Mané replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.05 | 11.54 | 18.71 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.35 | 0.41 | 0.52 | 0.00 | 6.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.86 | 16.57 | 26.15 | 9.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.38 | 14.55 | 22.84 | 7.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.27 | 12.14 | 19.09 | 6.00 | 85.5 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.0 | 4.45 | 11.93 | 18.24 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | James Justin | DEF | 11 | 3.9 | 2.59 | 8.34 | 13.39 | 2.00 | 76.2 | 86.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.8 | 7.90 | 22.68 | 36.88 | 0.00 | 90.0 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.49 | 13.92 | 22.52 | 2.00 | 70.3 | 90.0 |
| Bench 2 | Autosub In | Mateus Mané | FWD | 20 | 4.6 | 3.80 | 11.23 | 17.35 | 2.00 | 90.0 | 90.0 |
| Vice Captain | Captain | Declan Rice | MID | 1 | 7.6 | 6.14 | 17.87 | 28.05 | 5.00 | 90.0 | 75.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.90 | 16.71 | 26.60 | 8.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 5.61 | 16.19 | 27.13 | 13.00 | 84.2 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.72 | 13.25 | 20.71 | 12.00 | 87.6 | 71.0 |
| Bench 3 | Bench | Ilia Gruev | MID | 11 | 4.7 | 2.98 | 9.03 | 14.10 | 2.00 | 81.2 | 74.0 |

## GW29

- Train rows: 182721
- Bank: 0.90 -> 0.20
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Bruno Borges Fernandes
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 68.37
- Actual score: 87.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.53) beats the best remaining Triple Captain opportunity (7.98).
- Transfer: Ilia Gruev -> Elliot Anderson (projected gain 1.31, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.53) beats the best remaining Triple Captain opportunity (7.98).
- Autosub: Mateus Mané replaced Harry Wilson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.75 | 11.52 | 18.85 | 7.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.12 | 0.16 | 0.31 | 0.00 | 2.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.59 | 16.86 | 26.90 | 11.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.07 | 14.19 | 22.41 | 1.00 | 86.3 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.59 | 12.83 | 20.24 | 1.00 | 87.7 | 90.0 |
| Bench 3 | Bench | James Hill | DEF | 4 | 4.0 | 3.57 | 10.28 | 16.21 | 8.00 | 87.0 | 90.0 |
| Bench 4 | Bench | James Justin | DEF | 11 | 3.9 | 2.94 | 8.22 | 12.87 | 2.00 | 79.6 | 73.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.7 | 5.38 | 16.84 | 29.03 | 2.00 | 55.6 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.81 | 14.41 | 23.81 | 19.00 | 77.5 | 84.0 |
| Bench 2 | Autosub In | Mateus Mané | FWD | 20 | 4.6 | 3.60 | 10.44 | 16.20 | 2.00 | 90.0 | 69.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.53 | 18.38 | 29.25 | 7.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.9 | 6.50 | 18.21 | 30.09 | 8.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.5 | 4.79 | 15.08 | 24.57 | 3.00 | 90.0 | 90.0 |
| XI | Bench | Harry Wilson | MID | 10 | 5.9 | 4.50 | 12.51 | 20.02 | 0.00 | 75.5 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.81 | 11.70 | 18.74 | 12.00 | 79.1 | 90.0 |

## GW30

- Train rows: 183541
- Bank: 0.20 -> 0.40
- Free transfers: 2 -> 2
- Captain: João Pedro Junqueira de Jesus
- Vice captain: Bruno Borges Fernandes
- Effective captain: João Pedro Junqueira de Jesus
- Chip used: bench_boost
- Predicted score: 73.63
- Actual score: 69.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.02) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Marc Guéhi -> Marcos Senesi Barón (projected gain 0.43, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.02) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.11 | 11.74 | 19.09 | 7.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 3.8 | 0.07 | 0.29 | 0.35 | 0.00 | 5.1 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.37 | 15.47 | 25.58 | 9.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.19 | 14.05 | 22.29 | 2.00 | 85.2 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.42 | 11.86 | 18.72 | 10.00 | 90.0 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.1 | 4.10 | 10.92 | 17.57 | 8.00 | 87.9 | 90.0 |
| Bench 3 | Bench Boost | James Justin | DEF | 11 | 3.9 | 2.35 | 7.27 | 11.97 | 6.00 | 66.9 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.6 | 6.44 | 19.58 | 32.54 | 2.00 | 86.0 | 90.0 |
| Captain | Captain | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.96 | 18.80 | 30.29 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 2.50 | 7.26 | 12.38 | 1.00 | 65.9 | 45.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.9 | 6.77 | 20.21 | 32.80 | 10.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 6.54 | 18.69 | 29.53 | 2.00 | 90.0 | 74.0 |
| XI | XI | Declan Rice | MID | 1 | 7.4 | 5.01 | 14.32 | 23.64 | 3.00 | 86.2 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.73 | 13.06 | 20.74 | 2.00 | 89.7 | 87.0 |
| Bench 4 | Bench Boost | Harry Wilson | MID | 10 | 5.9 | 2.11 | 7.40 | 13.12 | 3.00 | 29.6 | 90.0 |