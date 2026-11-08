# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 281.63
- Total actual points: 281.00
- Average predicted points: 70.41
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
- Predicted score: 72.67
- Actual score: 51.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.81 | 13.37 | 21.12 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.10 | 0.16 | 0.27 | 0.00 | 5.1 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 6.94 | 19.47 | 29.89 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.94 | 14.05 | 22.27 | 11.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.84 | 13.23 | 20.05 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.0 | 3.92 | 11.28 | 17.64 | 6.00 | 90.0 | 90.0 |
| Bench 4 | Bench | James Justin | DEF | 11 | 3.9 | 2.27 | 7.77 | 13.10 | 2.00 | 66.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.31 | 22.21 | 36.40 | 6.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.14 | 16.22 | 25.55 | 7.00 | 84.7 | 79.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 4.78 | 13.08 | 19.59 | 2.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.6 | 6.62 | 18.92 | 29.57 | 4.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 6.33 | 17.39 | 27.94 | 4.00 | 90.0 | 86.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 5.37 | 16.08 | 27.36 | 2.00 | 78.2 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.9 | 5.26 | 14.56 | 23.58 | 2.00 | 84.6 | 90.0 |
| Bench 3 | Bench | Ilia Gruev | MID | 11 | 4.7 | 2.88 | 8.86 | 14.19 | 1.00 | 77.5 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 0.00 -> 0.90
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Declan Rice
- Chip used: none
- Predicted score: 65.94
- Actual score: 74.00
- Transfer: Enzo Fernández -> Harry Wilson (projected gain 2.01, hit 0)
- Autosub: Mateus Mané replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.06 | 11.60 | 18.77 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.35 | 0.41 | 0.51 | 0.00 | 5.9 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.86 | 16.61 | 26.17 | 9.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.32 | 14.41 | 22.63 | 7.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.28 | 12.19 | 19.13 | 6.00 | 85.6 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.0 | 4.44 | 11.91 | 18.19 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | James Justin | DEF | 11 | 3.9 | 2.59 | 8.33 | 13.38 | 2.00 | 76.1 | 86.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.8 | 7.55 | 21.72 | 36.69 | 0.00 | 90.0 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.51 | 14.01 | 22.61 | 2.00 | 70.5 | 90.0 |
| Bench 2 | Autosub In | Mateus Mané | FWD | 20 | 4.6 | 3.80 | 11.24 | 17.34 | 2.00 | 90.0 | 90.0 |
| Vice Captain | Captain | Declan Rice | MID | 1 | 7.6 | 6.17 | 17.96 | 28.14 | 5.00 | 90.0 | 75.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.88 | 16.68 | 26.53 | 8.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 5.62 | 16.24 | 27.17 | 13.00 | 84.1 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.70 | 13.21 | 20.65 | 12.00 | 87.2 | 71.0 |
| Bench 3 | Bench | Ilia Gruev | MID | 11 | 4.7 | 2.97 | 9.02 | 14.07 | 2.00 | 81.1 | 74.0 |

## GW29

- Train rows: 182721
- Bank: 0.90 -> 0.20
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Bruno Borges Fernandes
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 68.65
- Actual score: 87.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.93) beats the best remaining Triple Captain opportunity (8.17).
- Transfer: Ilia Gruev -> Elliot Anderson (projected gain 1.31, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.93) beats the best remaining Triple Captain opportunity (8.17).
- Autosub: Mateus Mané replaced Harry Wilson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.76 | 11.55 | 18.88 | 7.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.12 | 0.16 | 0.31 | 0.00 | 2.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.58 | 16.87 | 26.87 | 11.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.06 | 14.15 | 22.33 | 1.00 | 85.8 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.59 | 12.85 | 20.25 | 1.00 | 87.6 | 90.0 |
| Bench 3 | Bench | James Hill | DEF | 4 | 4.0 | 3.56 | 10.28 | 16.20 | 8.00 | 87.0 | 90.0 |
| Bench 4 | Bench | James Justin | DEF | 11 | 3.9 | 2.95 | 8.26 | 12.91 | 2.00 | 79.8 | 73.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.7 | 4.38 | 14.66 | 26.09 | 2.00 | 37.6 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.83 | 14.47 | 23.86 | 19.00 | 77.5 | 84.0 |
| Bench 2 | Autosub In | Mateus Mané | FWD | 20 | 4.6 | 3.60 | 10.46 | 16.21 | 2.00 | 90.0 | 69.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.93 | 19.56 | 31.32 | 7.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.9 | 6.51 | 18.25 | 30.11 | 8.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.5 | 4.83 | 15.20 | 24.70 | 3.00 | 90.0 | 90.0 |
| XI | Bench | Harry Wilson | MID | 10 | 5.9 | 4.50 | 12.53 | 20.01 | 0.00 | 75.4 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.81 | 11.72 | 18.75 | 12.00 | 79.2 | 90.0 |

## GW30

- Train rows: 183541
- Bank: 0.20 -> 0.40
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Antoine Semenyo
- Chip used: bench_boost
- Predicted score: 74.38
- Actual score: 69.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.09) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Marc Guéhi -> Marcos Senesi Barón (projected gain 0.40, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.09) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.11 | 11.74 | 19.08 | 7.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 3.8 | 0.07 | 0.27 | 0.33 | 0.00 | 5.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.37 | 15.48 | 25.58 | 9.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.19 | 14.09 | 22.32 | 2.00 | 85.2 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.41 | 11.84 | 18.67 | 10.00 | 90.0 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.1 | 4.10 | 10.92 | 17.58 | 8.00 | 87.9 | 90.0 |
| Bench 3 | Bench Boost | James Justin | DEF | 11 | 3.9 | 2.35 | 7.29 | 11.99 | 6.00 | 67.1 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.6 | 6.51 | 19.76 | 32.75 | 2.00 | 86.6 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.94 | 18.78 | 30.21 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 2.50 | 7.26 | 12.38 | 1.00 | 65.8 | 45.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.9 | 6.75 | 20.20 | 32.75 | 10.00 | 90.0 | 90.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 7.08 | 19.99 | 31.54 | 2.00 | 90.0 | 74.0 |
| XI | XI | Declan Rice | MID | 1 | 7.4 | 5.05 | 14.40 | 23.75 | 3.00 | 86.7 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.72 | 13.05 | 20.70 | 2.00 | 89.5 | 87.0 |
| Bench 4 | Bench Boost | Harry Wilson | MID | 10 | 5.9 | 2.17 | 7.57 | 13.30 | 3.00 | 30.4 | 90.0 |