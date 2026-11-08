# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 279.69
- Total actual points: 281.00
- Average predicted points: 69.92
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
- Predicted score: 70.68
- Actual score: 51.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.81 | 13.33 | 21.11 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 1.0 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 6.94 | 19.45 | 29.91 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.94 | 14.06 | 22.35 | 11.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.83 | 13.22 | 20.09 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.0 | 3.91 | 11.29 | 17.70 | 6.00 | 90.0 | 90.0 |
| Bench 4 | Bench | James Justin | DEF | 11 | 3.9 | 2.51 | 8.11 | 13.45 | 2.00 | 74.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 7.33 | 21.00 | 34.65 | 6.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.11 | 16.16 | 25.56 | 7.00 | 83.6 | 79.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 4.82 | 13.15 | 19.69 | 2.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.6 | 6.61 | 18.84 | 29.51 | 4.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 6.34 | 17.41 | 28.03 | 4.00 | 90.0 | 86.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 5.44 | 16.18 | 27.44 | 2.00 | 80.2 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.9 | 5.20 | 14.44 | 23.49 | 2.00 | 83.5 | 90.0 |
| Bench 3 | Bench | Ilia Gruev | MID | 11 | 4.7 | 2.88 | 8.82 | 14.13 | 1.00 | 77.9 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 0.00 -> 0.90
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Declan Rice
- Chip used: none
- Predicted score: 66.50
- Actual score: 74.00
- Transfer: Enzo Fernández -> Harry Wilson (projected gain 1.85, hit 0)
- Autosub: Mateus Mané replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.02 | 11.50 | 18.70 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.18 | 0.09 | 0.17 | 0.00 | 1.8 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.83 | 16.54 | 26.15 | 9.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.36 | 14.51 | 22.84 | 7.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.23 | 12.07 | 19.05 | 6.00 | 84.3 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.0 | 4.43 | 11.89 | 18.22 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | James Justin | DEF | 11 | 3.9 | 2.78 | 8.66 | 13.76 | 2.00 | 82.2 | 86.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.8 | 7.87 | 22.63 | 36.87 | 0.00 | 90.0 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.53 | 14.06 | 22.85 | 2.00 | 72.0 | 90.0 |
| Bench 2 | Autosub In | Mateus Mané | FWD | 20 | 4.6 | 3.88 | 11.40 | 17.49 | 2.00 | 90.0 | 90.0 |
| Vice Captain | Captain | Declan Rice | MID | 1 | 7.6 | 6.12 | 17.85 | 28.05 | 5.00 | 90.0 | 75.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.87 | 16.66 | 26.59 | 8.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 5.68 | 16.32 | 27.25 | 13.00 | 86.1 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.70 | 13.20 | 20.69 | 12.00 | 87.1 | 71.0 |
| Bench 3 | Bench | Ilia Gruev | MID | 11 | 4.7 | 2.94 | 8.97 | 14.05 | 2.00 | 80.0 | 74.0 |

## GW29

- Train rows: 182721
- Bank: 0.90 -> 0.20
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Bruno Borges Fernandes
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 69.20
- Actual score: 87.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.60) beats the best remaining Triple Captain opportunity (8.06).
- Transfer: Ilia Gruev -> Elliot Anderson (projected gain 1.26, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.60) beats the best remaining Triple Captain opportunity (8.06).
- Autosub: Mateus Mané replaced Harry Wilson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.82 | 11.64 | 18.94 | 7.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.03 | 0.00 | 0.06 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.66 | 17.00 | 27.01 | 11.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.12 | 14.29 | 22.49 | 1.00 | 87.7 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.63 | 12.93 | 20.31 | 1.00 | 88.8 | 90.0 |
| Bench 3 | Bench | James Hill | DEF | 4 | 4.0 | 3.61 | 10.37 | 16.27 | 8.00 | 88.3 | 90.0 |
| Bench 4 | Bench | James Justin | DEF | 11 | 3.9 | 2.98 | 8.31 | 12.93 | 2.00 | 80.6 | 73.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.7 | 5.46 | 17.14 | 29.48 | 2.00 | 57.8 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.88 | 14.49 | 23.81 | 19.00 | 79.9 | 84.0 |
| Bench 2 | Autosub In | Mateus Mané | FWD | 20 | 4.6 | 3.66 | 10.57 | 16.31 | 2.00 | 90.0 | 69.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.60 | 18.53 | 29.37 | 7.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.9 | 6.57 | 18.34 | 30.20 | 8.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.5 | 4.83 | 15.17 | 24.63 | 3.00 | 90.0 | 90.0 |
| XI | Bench | Harry Wilson | MID | 10 | 5.9 | 4.59 | 12.64 | 20.07 | 0.00 | 78.5 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.85 | 11.79 | 18.80 | 12.00 | 80.3 | 90.0 |

## GW30

- Train rows: 183541
- Bank: 0.20 -> 0.40
- Free transfers: 2 -> 2
- Captain: João Pedro Junqueira de Jesus
- Vice captain: Bruno Borges Fernandes
- Effective captain: João Pedro Junqueira de Jesus
- Chip used: bench_boost
- Predicted score: 73.31
- Actual score: 69.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.17) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Marc Guéhi -> Marcos Senesi Barón (projected gain 0.45, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.17) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.07 | 11.65 | 19.03 | 7.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.8 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.32 | 15.39 | 25.53 | 9.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.14 | 13.99 | 22.26 | 2.00 | 84.1 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.39 | 11.82 | 18.70 | 10.00 | 90.0 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.1 | 4.06 | 10.85 | 17.53 | 8.00 | 86.8 | 90.0 |
| Bench 2 | Bench Boost | James Justin | DEF | 11 | 3.9 | 2.55 | 7.56 | 12.27 | 6.00 | 73.8 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.6 | 6.34 | 19.40 | 32.38 | 2.00 | 83.7 | 90.0 |
| Captain | Captain | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.94 | 18.79 | 30.33 | 2.00 | 90.0 | 90.0 |
| Bench 3 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 2.51 | 7.34 | 12.61 | 1.00 | 66.7 | 45.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.9 | 6.77 | 20.23 | 32.85 | 10.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 6.52 | 18.66 | 29.54 | 2.00 | 90.0 | 74.0 |
| XI | XI | Declan Rice | MID | 1 | 7.4 | 4.94 | 14.17 | 23.51 | 3.00 | 84.3 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.70 | 13.02 | 20.72 | 2.00 | 88.7 | 87.0 |
| Bench 4 | Bench Boost | Harry Wilson | MID | 10 | 5.9 | 2.11 | 6.95 | 12.15 | 3.00 | 30.8 | 90.0 |