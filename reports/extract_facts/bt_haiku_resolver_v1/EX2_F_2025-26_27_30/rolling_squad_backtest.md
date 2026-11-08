# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 281.40
- Total actual points: 281.00
- Average predicted points: 70.35
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
- Predicted score: 72.64
- Actual score: 51.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.81 | 13.37 | 21.11 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.10 | 0.16 | 0.27 | 0.00 | 5.1 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 6.94 | 19.47 | 29.89 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.94 | 14.05 | 22.26 | 11.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.84 | 13.23 | 20.05 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.0 | 3.92 | 11.28 | 17.64 | 6.00 | 90.0 | 90.0 |
| Bench 4 | Bench | James Justin | DEF | 11 | 3.9 | 2.27 | 7.77 | 13.11 | 2.00 | 66.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.30 | 22.14 | 36.41 | 6.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.14 | 16.21 | 25.54 | 7.00 | 84.6 | 79.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 4.78 | 13.08 | 19.58 | 2.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.6 | 6.62 | 18.92 | 29.57 | 4.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 6.33 | 17.39 | 27.94 | 4.00 | 90.0 | 86.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 5.37 | 16.09 | 27.36 | 2.00 | 78.2 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.9 | 5.26 | 14.56 | 23.58 | 2.00 | 84.6 | 90.0 |
| Bench 3 | Bench | Ilia Gruev | MID | 11 | 4.7 | 2.88 | 8.86 | 14.18 | 1.00 | 77.5 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 0.00 -> 0.90
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Declan Rice
- Chip used: none
- Predicted score: 66.01
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
| XI | XI | James Hill | DEF | 4 | 4.0 | 4.44 | 11.91 | 18.18 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | James Justin | DEF | 11 | 3.9 | 2.59 | 8.33 | 13.38 | 2.00 | 76.1 | 86.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.8 | 7.59 | 21.49 | 36.33 | 0.00 | 90.0 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.51 | 14.01 | 22.61 | 2.00 | 70.5 | 90.0 |
| Bench 2 | Autosub In | Mateus Mané | FWD | 20 | 4.6 | 3.80 | 11.24 | 17.34 | 2.00 | 90.0 | 90.0 |
| Vice Captain | Captain | Declan Rice | MID | 1 | 7.6 | 6.17 | 17.97 | 28.15 | 5.00 | 90.0 | 75.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.88 | 16.68 | 26.53 | 8.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 5.62 | 16.24 | 27.18 | 13.00 | 84.1 | 90.0 |
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
- Predicted score: 68.46
- Actual score: 87.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.87) beats the best remaining Triple Captain opportunity (8.10).
- Transfer: Ilia Gruev -> Elliot Anderson (projected gain 1.31, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.87) beats the best remaining Triple Captain opportunity (8.10).
- Autosub: Mateus Mané replaced Harry Wilson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.76 | 11.55 | 18.88 | 7.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.12 | 0.16 | 0.31 | 0.00 | 2.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.58 | 16.87 | 26.87 | 11.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.05 | 14.15 | 22.32 | 1.00 | 85.8 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.59 | 12.85 | 20.25 | 1.00 | 87.6 | 90.0 |
| Bench 3 | Bench | James Hill | DEF | 4 | 4.0 | 3.56 | 10.28 | 16.20 | 8.00 | 87.0 | 90.0 |
| Bench 4 | Bench | James Justin | DEF | 11 | 3.9 | 2.95 | 8.25 | 12.90 | 2.00 | 79.8 | 73.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.7 | 4.39 | 14.54 | 25.94 | 2.00 | 37.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.83 | 14.47 | 23.86 | 19.00 | 77.5 | 84.0 |
| Bench 2 | Autosub In | Mateus Mané | FWD | 20 | 4.6 | 3.60 | 10.46 | 16.22 | 2.00 | 90.0 | 69.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.87 | 19.40 | 31.18 | 7.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.9 | 6.51 | 18.25 | 30.11 | 8.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.5 | 4.83 | 15.21 | 24.71 | 3.00 | 90.0 | 90.0 |
| XI | Bench | Harry Wilson | MID | 10 | 5.9 | 4.50 | 12.53 | 20.01 | 0.00 | 75.3 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.81 | 11.72 | 18.76 | 12.00 | 79.2 | 90.0 |

## GW30

- Train rows: 183541
- Bank: 0.20 -> 0.40
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Antoine Semenyo
- Chip used: bench_boost
- Predicted score: 74.29
- Actual score: 69.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.08) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Marc Guéhi -> Marcos Senesi Barón (projected gain 0.40, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.08) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.11 | 11.73 | 19.07 | 7.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 3.8 | 0.07 | 0.27 | 0.33 | 0.00 | 5.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.37 | 15.49 | 25.58 | 9.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.19 | 14.09 | 22.31 | 2.00 | 85.2 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.41 | 11.84 | 18.68 | 10.00 | 90.0 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.1 | 4.10 | 10.92 | 17.58 | 8.00 | 87.9 | 90.0 |
| Bench 3 | Bench Boost | James Justin | DEF | 11 | 3.9 | 2.35 | 7.29 | 11.99 | 6.00 | 67.0 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.6 | 6.50 | 19.76 | 32.74 | 2.00 | 86.6 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.94 | 18.78 | 30.20 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 2.50 | 7.26 | 12.38 | 1.00 | 65.8 | 45.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.9 | 6.75 | 20.20 | 32.74 | 10.00 | 90.0 | 90.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 7.03 | 19.91 | 31.46 | 2.00 | 90.0 | 74.0 |
| XI | XI | Declan Rice | MID | 1 | 7.4 | 5.05 | 14.40 | 23.75 | 3.00 | 86.7 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.72 | 13.05 | 20.71 | 2.00 | 89.5 | 87.0 |
| Bench 4 | Bench Boost | Harry Wilson | MID | 10 | 5.9 | 2.17 | 7.58 | 13.30 | 3.00 | 30.4 | 90.0 |