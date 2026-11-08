# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 281.36
- Total actual points: 281.00
- Average predicted points: 70.34
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
- Predicted score: 72.61
- Actual score: 51.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.83 | 13.40 | 21.17 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.00 | 0.11 | 0.00 | 2.4 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 6.95 | 19.49 | 29.93 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.91 | 14.00 | 22.24 | 11.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.81 | 13.20 | 20.04 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.0 | 3.90 | 11.25 | 17.63 | 6.00 | 90.0 | 90.0 |
| Bench 4 | Bench | James Justin | DEF | 11 | 3.9 | 2.47 | 8.09 | 13.47 | 2.00 | 72.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.29 | 22.12 | 36.42 | 6.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.08 | 16.12 | 25.46 | 7.00 | 82.8 | 79.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 4.80 | 13.12 | 19.65 | 2.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.6 | 6.66 | 18.99 | 29.66 | 4.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 6.31 | 17.37 | 27.94 | 4.00 | 90.0 | 86.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 5.44 | 16.21 | 27.44 | 2.00 | 80.1 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.9 | 5.23 | 14.52 | 23.57 | 2.00 | 83.8 | 90.0 |
| Bench 3 | Bench | Ilia Gruev | MID | 11 | 4.7 | 2.84 | 8.80 | 14.14 | 1.00 | 76.4 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 0.00 -> 0.90
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Declan Rice
- Chip used: none
- Predicted score: 65.72
- Actual score: 74.00
- Transfer: Enzo Fernández -> Harry Wilson (projected gain 1.83, hit 0)
- Autosub: Mateus Mané replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.05 | 11.57 | 18.78 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.25 | 0.24 | 0.35 | 0.00 | 3.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.84 | 16.59 | 26.17 | 9.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.30 | 14.37 | 22.62 | 7.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.24 | 12.13 | 19.10 | 6.00 | 84.5 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.0 | 4.41 | 11.87 | 18.17 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | James Justin | DEF | 11 | 3.9 | 2.78 | 8.65 | 13.74 | 2.00 | 82.1 | 86.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.8 | 7.51 | 21.53 | 36.60 | 0.00 | 90.0 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.46 | 13.94 | 22.57 | 2.00 | 69.1 | 90.0 |
| Bench 2 | Autosub In | Mateus Mané | FWD | 20 | 4.6 | 3.87 | 11.39 | 17.46 | 2.00 | 90.0 | 90.0 |
| Vice Captain | Captain | Declan Rice | MID | 1 | 7.6 | 6.17 | 17.97 | 28.17 | 5.00 | 90.0 | 75.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.85 | 16.65 | 26.51 | 8.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 5.69 | 16.37 | 27.29 | 13.00 | 86.1 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.68 | 13.18 | 20.64 | 12.00 | 86.7 | 71.0 |
| Bench 3 | Bench | Ilia Gruev | MID | 11 | 4.7 | 2.94 | 8.96 | 14.02 | 2.00 | 79.9 | 74.0 |

## GW29

- Train rows: 182721
- Bank: 0.90 -> 0.20
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Bruno Borges Fernandes
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 69.00
- Actual score: 87.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.94) beats the best remaining Triple Captain opportunity (8.19).
- Transfer: Ilia Gruev -> Elliot Anderson (projected gain 1.27, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.94) beats the best remaining Triple Captain opportunity (8.19).
- Autosub: Mateus Mané replaced Harry Wilson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.83 | 11.67 | 18.96 | 7.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.10 | 0.14 | 0.24 | 0.00 | 1.5 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.65 | 17.00 | 26.96 | 11.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.10 | 14.24 | 22.39 | 1.00 | 87.1 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.63 | 12.94 | 20.30 | 1.00 | 88.7 | 90.0 |
| Bench 3 | Bench | James Hill | DEF | 4 | 4.0 | 3.61 | 10.36 | 16.24 | 8.00 | 88.2 | 90.0 |
| Bench 4 | Bench | James Justin | DEF | 11 | 3.9 | 2.99 | 8.34 | 12.95 | 2.00 | 80.7 | 73.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.87 | 14.55 | 23.91 | 19.00 | 78.5 | 84.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.7 | 4.25 | 14.47 | 25.99 | 2.00 | 33.4 | 90.0 |
| Bench 2 | Autosub In | Mateus Mané | FWD | 20 | 4.6 | 3.66 | 10.58 | 16.31 | 2.00 | 90.0 | 69.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.94 | 19.53 | 31.26 | 7.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.9 | 6.58 | 18.38 | 30.22 | 8.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.5 | 4.88 | 15.31 | 24.77 | 3.00 | 90.0 | 90.0 |
| XI | Bench | Harry Wilson | MID | 10 | 5.9 | 4.55 | 12.64 | 20.08 | 0.00 | 76.8 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.86 | 11.81 | 18.81 | 12.00 | 80.4 | 90.0 |

## GW30

- Train rows: 183541
- Bank: 0.20 -> 0.40
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Antoine Semenyo
- Chip used: bench_boost
- Predicted score: 74.03
- Actual score: 69.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.18) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Marc Guéhi -> Marcos Senesi Barón (projected gain 0.43, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.18) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.07 | 11.67 | 19.02 | 7.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.11 | 0.17 | 0.00 | 2.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.33 | 15.43 | 25.55 | 9.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.16 | 14.04 | 22.29 | 2.00 | 84.2 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.38 | 11.80 | 18.66 | 10.00 | 90.0 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.1 | 4.07 | 10.86 | 17.55 | 8.00 | 86.9 | 90.0 |
| Bench 2 | Bench Boost | James Justin | DEF | 11 | 3.9 | 2.52 | 7.57 | 12.32 | 6.00 | 72.3 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.6 | 6.44 | 19.64 | 32.65 | 2.00 | 85.0 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.93 | 18.77 | 30.24 | 2.00 | 90.0 | 90.0 |
| Bench 3 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 2.42 | 7.13 | 12.27 | 1.00 | 63.6 | 45.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.9 | 6.76 | 20.21 | 32.78 | 10.00 | 90.0 | 90.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 7.02 | 19.89 | 31.46 | 2.00 | 90.0 | 74.0 |
| XI | XI | Declan Rice | MID | 1 | 7.4 | 4.99 | 14.30 | 23.67 | 3.00 | 85.1 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.69 | 13.01 | 20.70 | 2.00 | 88.6 | 87.0 |
| Bench 4 | Bench Boost | Harry Wilson | MID | 10 | 5.9 | 2.24 | 7.27 | 12.51 | 3.00 | 33.3 | 90.0 |