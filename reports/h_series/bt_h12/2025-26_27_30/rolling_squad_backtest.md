# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 275.29
- Total actual points: 289.00
- Average predicted points: 68.82
- Average actual points: 72.25
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
- Predicted score: 69.69
- Actual score: 51.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.70 | 13.30 | 20.95 | 3.00 | 89.9 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.00 | 0.11 | 0.00 | 2.4 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 6.85 | 19.38 | 29.77 | 2.00 | 89.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.87 | 14.03 | 22.29 | 11.00 | 90.7 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.73 | 13.25 | 19.88 | 2.00 | 89.9 | 90.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.0 | 3.76 | 11.01 | 16.96 | 6.00 | 90.9 | 90.0 |
| Bench 4 | Bench | James Justin | DEF | 11 | 3.9 | 2.47 | 8.08 | 13.48 | 2.00 | 72.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 7.26 | 20.90 | 34.37 | 6.00 | 90.1 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.02 | 16.13 | 25.32 | 7.00 | 83.4 | 79.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 4.69 | 13.05 | 19.42 | 2.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.6 | 6.51 | 18.77 | 29.24 | 4.00 | 90.2 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 6.27 | 17.28 | 27.79 | 4.00 | 90.5 | 86.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 5.38 | 16.18 | 27.27 | 2.00 | 80.9 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.9 | 5.13 | 14.41 | 23.42 | 2.00 | 83.9 | 90.0 |
| Bench 3 | Bench | Ilia Gruev | MID | 11 | 4.7 | 2.84 | 8.80 | 14.16 | 1.00 | 76.4 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 0.00 -> 0.90
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Declan Rice
- Chip used: none
- Predicted score: 65.39
- Actual score: 74.00
- Transfer: Enzo Fernández -> Harry Wilson (projected gain 1.95, hit 0)
- Autosub: Mateus Mané replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.95 | 11.48 | 18.52 | 3.00 | 90.3 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.25 | 0.24 | 0.34 | 0.00 | 3.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.75 | 16.46 | 26.02 | 9.00 | 91.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.26 | 14.50 | 22.64 | 7.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.13 | 11.97 | 18.77 | 6.00 | 84.4 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.0 | 4.38 | 11.78 | 18.07 | 2.00 | 90.4 | 90.0 |
| Bench 4 | Bench | James Justin | DEF | 11 | 3.9 | 2.78 | 8.66 | 13.76 | 2.00 | 82.2 | 86.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.8 | 7.76 | 22.49 | 36.66 | 0.00 | 90.0 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.34 | 13.91 | 22.30 | 2.00 | 69.0 | 90.0 |
| Bench 2 | Autosub In | Mateus Mané | FWD | 20 | 4.6 | 3.79 | 11.33 | 17.48 | 2.00 | 90.5 | 90.0 |
| Vice Captain | Captain | Declan Rice | MID | 1 | 7.6 | 6.03 | 17.87 | 27.91 | 5.00 | 90.4 | 75.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.76 | 16.52 | 26.37 | 8.00 | 90.2 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 5.61 | 16.28 | 27.16 | 13.00 | 86.7 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.65 | 13.22 | 20.53 | 12.00 | 87.6 | 71.0 |
| Bench 3 | Bench | Ilia Gruev | MID | 11 | 4.7 | 2.86 | 8.83 | 13.90 | 2.00 | 80.9 | 74.0 |

## GW29

- Train rows: 182721
- Bank: 0.90 -> 0.20
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Antoine Semenyo
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 68.08
- Actual score: 95.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.50) beats the best remaining Triple Captain opportunity (7.98).
- Transfer: Ilia Gruev -> Elliot Anderson (projected gain 1.63, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (6.50) beats the best remaining Triple Captain opportunity (7.98).
- Autosub: James Hill replaced Harry Wilson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.75 | 11.63 | 18.87 | 7.00 | 90.1 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.10 | 0.14 | 0.24 | 0.00 | 1.5 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.62 | 17.04 | 26.95 | 11.00 | 90.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.07 | 14.27 | 22.43 | 1.00 | 88.3 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.58 | 12.89 | 20.17 | 1.00 | 89.4 | 90.0 |
| Bench 2 | Autosub In | James Hill | DEF | 4 | 4.0 | 3.58 | 10.28 | 16.18 | 8.00 | 88.8 | 90.0 |
| Bench 4 | Bench | James Justin | DEF | 11 | 3.9 | 2.98 | 8.31 | 12.93 | 2.00 | 80.6 | 73.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.7 | 5.24 | 16.67 | 28.73 | 2.00 | 55.1 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.81 | 14.47 | 23.75 | 19.00 | 79.1 | 84.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.6 | 3.57 | 10.52 | 16.19 | 2.00 | 91.2 | 69.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 8.1 | 6.47 | 18.39 | 29.18 | 7.00 | 90.1 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.9 | 6.50 | 18.31 | 30.13 | 8.00 | 90.7 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.5 | 4.75 | 15.15 | 24.66 | 3.00 | 90.5 | 90.0 |
| XI | Bench | Harry Wilson | MID | 10 | 5.9 | 4.46 | 12.60 | 19.90 | 0.00 | 77.3 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.83 | 11.87 | 18.78 | 12.00 | 80.8 | 90.0 |

## GW30

- Train rows: 183541
- Bank: 0.20 -> 0.40
- Free transfers: 2 -> 2
- Captain: João Pedro Junqueira de Jesus
- Vice captain: Bruno Borges Fernandes
- Effective captain: João Pedro Junqueira de Jesus
- Chip used: bench_boost
- Predicted score: 72.13
- Actual score: 69.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.10) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Marc Guéhi -> Marcos Senesi Barón (projected gain 0.49, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.10) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.91 | 11.52 | 18.82 | 7.00 | 89.7 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.11 | 0.17 | 0.00 | 2.3 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.22 | 15.33 | 25.30 | 9.00 | 89.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.05 | 13.95 | 22.06 | 2.00 | 84.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.30 | 11.77 | 18.64 | 10.00 | 91.3 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.1 | 3.96 | 10.79 | 17.49 | 8.00 | 88.1 | 90.0 |
| Bench 2 | Bench Boost | James Justin | DEF | 11 | 3.9 | 2.51 | 7.54 | 12.30 | 6.00 | 72.2 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.6 | 6.25 | 19.28 | 32.24 | 2.00 | 84.0 | 90.0 |
| Captain | Captain | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.88 | 18.82 | 30.26 | 2.00 | 90.0 | 90.0 |
| Bench 3 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 2.41 | 7.11 | 12.24 | 1.00 | 63.6 | 45.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.9 | 6.66 | 20.23 | 32.72 | 10.00 | 90.2 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 6.40 | 18.56 | 29.32 | 2.00 | 89.9 | 74.0 |
| XI | XI | Declan Rice | MID | 1 | 7.4 | 4.85 | 14.10 | 23.28 | 3.00 | 84.4 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.68 | 13.06 | 20.65 | 2.00 | 89.2 | 87.0 |
| Bench 4 | Bench Boost | Harry Wilson | MID | 10 | 5.9 | 2.18 | 7.10 | 12.33 | 3.00 | 32.3 | 90.0 |