# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 275.07
- Total actual points: 252.00
- Average predicted points: 68.77
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
- Predicted score: 70.32
- Actual score: 50.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.75 | 13.17 | 20.85 | 3.00 | 89.3 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.00 | 0.11 | 0.00 | 2.4 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 6.84 | 19.16 | 29.46 | 2.00 | 87.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.88 | 13.91 | 22.10 | 11.00 | 89.8 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.6 | 4.21 | 11.58 | 18.74 | 1.00 | 88.9 | 11.0 |
| Bench 3 | Bench | James Hill | DEF | 4 | 4.0 | 3.84 | 11.08 | 17.37 | 6.00 | 87.1 | 90.0 |
| Bench 4 | Bench | Reinildo Mandava | DEF | 17 | 3.8 | 2.61 | 7.03 | 10.77 | 0.00 | 70.6 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 7.13 | 20.43 | 33.70 | 6.00 | 86.5 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.46 | 17.11 | 27.05 | 7.00 | 85.3 | 79.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 4.78 | 13.04 | 19.54 | 2.00 | 90.7 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.6 | 6.56 | 18.70 | 29.29 | 4.00 | 91.3 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 5.82 | 17.30 | 29.33 | 2.00 | 79.5 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 6.28 | 17.24 | 27.75 | 4.00 | 89.0 | 86.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.9 | 5.49 | 15.25 | 24.80 | 2.00 | 85.7 | 90.0 |
| Bench 2 | Bench | Amine Adli | MID | 4 | 5.4 | 4.49 | 12.84 | 21.47 | 3.00 | 67.5 | 65.0 |

## GW28

- Train rows: 181902
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Declan Rice
- Chip used: none
- Predicted score: 66.72
- Actual score: 58.00
- Transfer: none
- No transfer was applied this week.
- Autosub: Mateus Mané replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.81 | 10.88 | 17.70 | 3.00 | 84.3 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.25 | 0.24 | 0.34 | 0.00 | 3.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.63 | 15.99 | 25.27 | 9.00 | 87.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.32 | 14.42 | 22.69 | 7.00 | 91.6 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.0 | 4.37 | 11.75 | 18.00 | 2.00 | 89.3 | 90.0 |
| Bench 3 | Bench | Nordi Mukiele | DEF | 17 | 4.6 | 1.91 | 6.75 | 11.68 | 0.00 | 50.2 | 0.0 |
| Bench 4 | Bench | Reinildo Mandava | DEF | 17 | 3.8 | 1.02 | 3.64 | 6.05 | 0.00 | 39.4 | 0.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.8 | 7.80 | 22.42 | 36.52 | 0.00 | 88.8 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.43 | 16.96 | 27.54 | 2.00 | 71.3 | 90.0 |
| Bench 2 | Autosub In | Mateus Mané | FWD | 20 | 4.6 | 3.76 | 11.06 | 16.96 | 2.00 | 86.3 | 90.0 |
| Vice Captain | Captain | Declan Rice | MID | 1 | 7.6 | 6.04 | 17.62 | 27.69 | 5.00 | 89.7 | 75.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 5.76 | 16.55 | 27.65 | 13.00 | 83.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.81 | 16.49 | 26.31 | 8.00 | 90.2 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.8 | 4.12 | 13.71 | 23.16 | 1.00 | 74.0 | 85.0 |
| XI | XI | Amine Adli | MID | 4 | 5.4 | 4.82 | 13.41 | 22.00 | 1.00 | 63.8 | 9.0 |

## GW29

- Train rows: 182721
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Bruno Borges Fernandes
- Effective captain: Antoine Semenyo
- Chip used: bench_boost
- Predicted score: 64.47
- Actual score: 91.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.41) beats the best remaining Bench Boost opportunity (6.49).
- Transfer: Amine Adli -> Elliot Anderson (projected gain 2.68, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.41) beats the best remaining Bench Boost opportunity (6.49).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.72 | 11.35 | 18.47 | 7.00 | 87.3 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 3.8 | 0.10 | 0.14 | 0.24 | 0.00 | 1.5 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.40 | 16.22 | 25.77 | 11.00 | 84.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.19 | 14.48 | 22.79 | 1.00 | 87.9 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.0 | 3.65 | 10.47 | 16.43 | 8.00 | 88.0 | 90.0 |
| Bench 3 | Bench Boost | Nordi Mukiele | DEF | 17 | 4.5 | 1.20 | 4.21 | 8.20 | 0.00 | 28.5 | 0.0 |
| Bench 4 | Bench Boost | Reinildo Mandava | DEF | 17 | 3.8 | 0.76 | 2.49 | 4.91 | 0.00 | 27.9 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 5.24 | 15.67 | 25.80 | 19.00 | 80.2 | 84.0 |
| Bench 2 | Bench Boost | Erling Haaland | FWD | 13 | 14.7 | 3.35 | 10.55 | 18.20 | 2.00 | 48.5 | 90.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 3.58 | 10.36 | 15.98 | 2.00 | 87.7 | 69.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.50 | 18.26 | 28.95 | 7.00 | 87.6 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.9 | 6.38 | 17.82 | 29.35 | 8.00 | 85.7 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.5 | 4.68 | 14.69 | 23.84 | 3.00 | 87.1 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 4.06 | 13.06 | 21.84 | 4.00 | 73.1 | 78.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.14 | 12.67 | 20.21 | 12.00 | 80.6 | 90.0 |

## GW30

- Train rows: 183541
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: João Pedro Junqueira de Jesus
- Vice captain: Erling Haaland
- Effective captain: João Pedro Junqueira de Jesus
- Chip used: triple_captain
- Predicted score: 73.57
- Actual score: 53.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.87) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on João Pedro Junqueira de Jesus. Optimizer chose Triple Captain here because the current estimated captain upside (6.87) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.95 | 11.32 | 18.48 | 7.00 | 88.5 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.11 | 0.17 | 0.00 | 2.3 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.23 | 15.12 | 25.08 | 9.00 | 87.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.39 | 14.67 | 23.34 | 2.00 | 86.2 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.1 | 4.13 | 11.02 | 17.81 | 8.00 | 88.0 | 90.0 |
| Bench 3 | Bench | Nordi Mukiele | DEF | 17 | 4.5 | 0.23 | 1.42 | 3.95 | 0.00 | 4.1 | 0.0 |
| Bench 4 | Bench | Reinildo Mandava | DEF | 17 | 3.8 | 0.00 | 0.12 | 1.60 | 0.00 | 5.2 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 6.70 | 20.50 | 34.20 | 2.00 | 85.1 | 90.0 |
| Captain | Captain | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.87 | 18.59 | 30.00 | 2.00 | 89.1 | 90.0 |
| Bench 2 | Bench | Mateus Mané | FWD | 20 | 4.5 | 2.41 | 7.11 | 12.24 | 1.00 | 63.6 | 45.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.9 | 6.66 | 19.90 | 32.31 | 10.00 | 87.3 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 6.37 | 18.22 | 28.84 | 2.00 | 85.6 | 74.0 |
| XI | XI | Declan Rice | MID | 1 | 7.4 | 5.17 | 14.84 | 24.63 | 3.00 | 87.3 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.6 | 4.64 | 13.82 | 22.52 | 2.00 | 79.8 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.73 | 13.10 | 20.86 | 2.00 | 87.7 | 87.0 |