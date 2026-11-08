# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 282.78
- Total actual points: 274.00
- Average predicted points: 70.69
- Average actual points: 68.50
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
- Captain: Gabriel dos Santos Magalhães
- Vice captain: Erling Haaland
- Effective captain: Gabriel dos Santos Magalhães
- Chip used: none
- Predicted score: 71.68
- Actual score: 47.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 5.33 | 14.42 | 22.54 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.3 | 0.0 |
| Captain | Captain | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 7.30 | 20.11 | 30.75 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.12 | 14.79 | 23.35 | 11.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.84 | 13.65 | 20.82 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.0 | 3.85 | 11.45 | 18.04 | 6.00 | 90.0 | 90.0 |
| Bench 4 | Bench | James Justin | DEF | 11 | 3.9 | 2.51 | 8.26 | 13.82 | 2.00 | 72.8 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.8 | 7.07 | 20.41 | 33.89 | 6.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.10 | 16.14 | 25.31 | 7.00 | 86.0 | 79.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 4.78 | 12.90 | 19.57 | 2.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.6 | 6.89 | 19.23 | 29.90 | 4.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 6.22 | 17.43 | 28.14 | 4.00 | 90.0 | 86.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 5.38 | 15.94 | 27.14 | 2.00 | 82.1 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.9 | 5.34 | 14.89 | 23.59 | 2.00 | 80.2 | 90.0 |
| Bench 3 | Bench | Ilia Gruev | MID | 11 | 4.7 | 2.77 | 8.65 | 13.99 | 1.00 | 76.4 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 0.00 -> 0.90
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Declan Rice
- Chip used: none
- Predicted score: 66.61
- Actual score: 74.00
- Transfer: Enzo Fernández -> Harry Wilson (projected gain 2.24, hit 0)
- Autosub: Mateus Mané replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.29 | 12.30 | 19.84 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.14 | 0.00 | 0.00 | 0.00 | 2.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.91 | 16.89 | 26.59 | 9.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.56 | 15.53 | 24.22 | 7.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.36 | 12.36 | 19.44 | 6.00 | 85.3 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.0 | 4.48 | 11.98 | 18.26 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | James Justin | DEF | 11 | 3.9 | 2.71 | 8.50 | 13.62 | 2.00 | 82.1 | 86.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.8 | 7.73 | 21.94 | 36.04 | 0.00 | 90.0 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.21 | 13.19 | 22.24 | 2.00 | 74.1 | 90.0 |
| Bench 2 | Autosub In | Mateus Mané | FWD | 20 | 4.6 | 3.70 | 10.90 | 16.83 | 2.00 | 90.0 | 90.0 |
| Vice Captain | Captain | Declan Rice | MID | 1 | 7.6 | 6.08 | 17.90 | 27.95 | 5.00 | 90.0 | 75.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.92 | 16.69 | 26.69 | 8.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 5.70 | 16.30 | 27.12 | 13.00 | 86.2 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.64 | 13.08 | 20.65 | 12.00 | 89.5 | 71.0 |
| Bench 3 | Bench | Ilia Gruev | MID | 11 | 4.7 | 2.79 | 8.62 | 13.60 | 2.00 | 79.9 | 74.0 |

## GW29

- Train rows: 182721
- Bank: 0.90 -> 0.40
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Bruno Borges Fernandes
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 70.54
- Actual score: 91.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.79) beats the best remaining Triple Captain opportunity (8.01).
- Transfer: Ilia Gruev -> James Garner (projected gain 1.03, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.79) beats the best remaining Triple Captain opportunity (8.01).
- Autosub: James Hill replaced Harry Wilson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.18 | 12.39 | 19.99 | 7.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.90 | 17.53 | 27.64 | 11.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.27 | 14.85 | 23.17 | 1.00 | 86.8 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.86 | 13.58 | 21.09 | 1.00 | 88.8 | 90.0 |
| Bench 2 | Autosub In | James Hill | DEF | 4 | 4.0 | 3.54 | 10.44 | 16.37 | 8.00 | 87.9 | 90.0 |
| Bench 3 | Bench | James Justin | DEF | 11 | 3.9 | 3.29 | 8.98 | 13.61 | 2.00 | 77.9 | 73.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.7 | 5.06 | 15.92 | 27.55 | 2.00 | 52.1 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.84 | 14.49 | 24.08 | 19.00 | 81.8 | 84.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.6 | 3.27 | 9.71 | 15.25 | 2.00 | 90.0 | 69.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.79 | 18.98 | 29.82 | 7.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.9 | 6.11 | 17.18 | 29.13 | 8.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.5 | 5.01 | 15.56 | 24.96 | 3.00 | 89.1 | 90.0 |
| XI | Bench | Harry Wilson | MID | 10 | 5.9 | 4.40 | 12.26 | 19.79 | 0.00 | 79.3 | 0.0 |
| XI | XI | James Garner | MID | 9 | 5.2 | 4.53 | 11.43 | 18.25 | 10.00 | 78.3 | 90.0 |

## GW30

- Train rows: 183541
- Bank: 0.40 -> 0.80
- Free transfers: 2 -> 2
- Captain: João Pedro Junqueira de Jesus
- Vice captain: Bruno Borges Fernandes
- Effective captain: João Pedro Junqueira de Jesus
- Chip used: bench_boost
- Predicted score: 73.95
- Actual score: 62.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.09) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Harry Wilson -> Elliot Anderson (projected gain 3.04, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.09) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.52 | 12.53 | 20.17 | 7.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 1.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.61 | 15.92 | 26.11 | 9.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.12 | 14.45 | 22.83 | 2.00 | 82.4 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.14 | 11.85 | 18.91 | 2.00 | 84.3 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.1 | 4.03 | 11.03 | 17.79 | 8.00 | 85.9 | 90.0 |
| Bench 3 | Bench Boost | James Justin | DEF | 11 | 3.9 | 2.67 | 7.84 | 12.63 | 6.00 | 70.7 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.6 | 6.06 | 18.62 | 31.25 | 2.00 | 83.0 | 90.0 |
| Captain | Captain | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.70 | 18.15 | 29.48 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 2.28 | 6.84 | 11.94 | 1.00 | 64.5 | 45.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.9 | 6.65 | 19.84 | 32.30 | 10.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 6.52 | 18.77 | 29.68 | 2.00 | 90.0 | 74.0 |
| XI | XI | Declan Rice | MID | 1 | 7.4 | 5.15 | 14.51 | 23.75 | 3.00 | 82.4 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.5 | 4.67 | 12.79 | 20.45 | 2.00 | 88.0 | 87.0 |
| Bench 2 | Bench Boost | James Garner | MID | 9 | 5.2 | 3.14 | 9.82 | 16.82 | 4.00 | 81.6 | 90.0 |