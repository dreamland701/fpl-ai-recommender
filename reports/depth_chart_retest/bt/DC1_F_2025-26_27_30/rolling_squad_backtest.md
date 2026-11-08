# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 278.62
- Total actual points: 259.00
- Average predicted points: 69.66
- Average actual points: 64.75
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
- Vice captain: Declan Rice
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 71.42
- Actual score: 51.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 5.06 | 14.08 | 22.30 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.00 | 0.01 | 0.00 | 1.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 6.67 | 18.71 | 28.73 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.87 | 13.89 | 22.08 | 11.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.66 | 12.79 | 19.42 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.0 | 3.95 | 11.41 | 17.91 | 6.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Reinildo Mandava | DEF | 17 | 3.8 | 2.51 | 6.80 | 10.41 | 0.00 | 69.2 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 7.58 | 21.71 | 35.76 | 6.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.16 | 16.34 | 25.83 | 7.00 | 83.8 | 79.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.49 | 15.33 | 24.72 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.6 | 6.70 | 19.18 | 30.06 | 4.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 6.08 | 16.76 | 27.01 | 4.00 | 90.0 | 86.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.39 | 14.77 | 24.01 | 2.00 | 84.5 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.9 | 5.19 | 14.46 | 23.53 | 2.00 | 82.4 | 90.0 |
| Bench 3 | Bench | Pape Matar Sarr | MID | 18 | 4.5 | 2.84 | 8.02 | 10.84 | 4.00 | 76.2 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 0.00 -> 0.90
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Declan Rice
- Chip used: none
- Predicted score: 67.57
- Actual score: 67.00
- Transfer: Enzo Fernández -> Harry Wilson (projected gain 1.42, hit 0)
- Autosub: Marc Guéhi replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.26 | 12.17 | 19.78 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.23 | 0.17 | 0.23 | 0.00 | 1.8 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.58 | 15.87 | 25.09 | 9.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.26 | 14.26 | 22.47 | 7.00 | 90.0 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.0 | 4.46 | 12.00 | 18.41 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Autosub In | Marc Guéhi | DEF | 13 | 5.2 | 4.07 | 11.69 | 18.46 | 6.00 | 82.5 | 90.0 |
| Bench 4 | Bench | Reinildo Mandava | DEF | 17 | 3.8 | 0.94 | 3.45 | 5.76 | 0.00 | 38.5 | 0.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.8 | 8.12 | 23.32 | 37.95 | 0.00 | 90.0 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.65 | 15.58 | 25.00 | 6.00 | 89.1 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.64 | 14.41 | 23.38 | 2.00 | 71.2 | 90.0 |
| Vice Captain | Captain | Declan Rice | MID | 1 | 7.6 | 6.19 | 18.07 | 28.44 | 5.00 | 90.0 | 75.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.65 | 16.12 | 25.76 | 8.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.03 | 13.90 | 22.38 | 2.00 | 82.1 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.61 | 13.02 | 20.42 | 12.00 | 85.6 | 71.0 |
| Bench 3 | Bench | Pape Matar Sarr | MID | 18 | 4.5 | 3.15 | 8.90 | 12.54 | 1.00 | 78.7 | 32.0 |

## GW29

- Train rows: 182721
- Bank: 0.90 -> 0.00
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Erling Haaland
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 67.07
- Actual score: 80.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.35) beats the best remaining Triple Captain opportunity (7.49).
- Transfer: Pape Matar Sarr -> Elliot Anderson (projected gain 1.29, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.35) beats the best remaining Triple Captain opportunity (7.49).
- Autosub: Morgan Rogers replaced Harry Wilson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.06 | 12.31 | 20.04 | 7.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.09 | 0.09 | 0.15 | 0.00 | 0.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.43 | 16.38 | 26.05 | 11.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.97 | 13.87 | 21.84 | 1.00 | 86.2 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.46 | 12.48 | 19.63 | 1.00 | 86.9 | 90.0 |
| Bench 3 | Bench | James Hill | DEF | 4 | 4.0 | 3.61 | 10.36 | 16.28 | 8.00 | 87.8 | 90.0 |
| Bench 4 | Bench | Reinildo Mandava | DEF | 17 | 3.8 | 0.72 | 2.40 | 4.80 | 0.00 | 27.4 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.7 | 5.70 | 17.77 | 30.52 | 2.00 | 59.1 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.04 | 15.13 | 24.27 | 2.00 | 85.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 5.05 | 15.07 | 24.81 | 19.00 | 80.8 | 84.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.35 | 17.89 | 28.39 | 7.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.5 | 4.86 | 15.28 | 24.84 | 3.00 | 90.0 | 90.0 |
| XI | Bench | Harry Wilson | MID | 10 | 5.9 | 4.44 | 12.34 | 19.67 | 0.00 | 75.2 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.01 | 12.25 | 19.56 | 12.00 | 81.2 | 90.0 |
| Bench 2 | Autosub In | Morgan Rogers | MID | 2 | 7.6 | 3.81 | 11.05 | 18.55 | 1.00 | 68.9 | 90.0 |

## GW30

- Train rows: 183541
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: João Pedro Junqueira de Jesus
- Vice captain: Erling Haaland
- Effective captain: João Pedro Junqueira de Jesus
- Chip used: bench_boost
- Predicted score: 72.57
- Actual score: 61.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.08) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Morgan Rogers -> Dominik Szoboszlai (projected gain 2.88, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.08) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.39 | 12.54 | 20.44 | 7.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 3.8 | 0.03 | 0.12 | 0.13 | 0.00 | 3.1 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.18 | 14.99 | 24.89 | 9.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.00 | 13.58 | 21.60 | 2.00 | 83.1 | 90.0 |
| Bench 2 | Bench Boost | Marc Guéhi | DEF | 13 | 5.2 | 3.92 | 11.04 | 17.68 | 2.00 | 82.6 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.1 | 4.12 | 10.97 | 17.71 | 8.00 | 87.6 | 90.0 |
| Bench 4 | Bench Boost | Reinildo Mandava | DEF | 17 | 3.8 | 0.00 | 0.28 | 1.84 | 0.00 | 7.5 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 6.59 | 20.11 | 33.51 | 2.00 | 86.6 | 90.0 |
| Captain | Captain | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 7.09 | 19.20 | 30.98 | 2.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.67 | 15.55 | 24.73 | 6.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 6.36 | 18.19 | 28.79 | 2.00 | 90.0 | 74.0 |
| XI | XI | Declan Rice | MID | 1 | 7.4 | 5.11 | 14.55 | 24.08 | 3.00 | 87.8 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.9 | 5.00 | 13.89 | 21.71 | 11.00 | 84.7 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.89 | 13.52 | 21.52 | 2.00 | 90.0 | 87.0 |
| Bench 3 | Bench Boost | Harry Wilson | MID | 10 | 5.9 | 2.13 | 6.94 | 12.06 | 3.00 | 32.3 | 90.0 |