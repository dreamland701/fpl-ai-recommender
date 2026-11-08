# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 267.55
- Total actual points: 248.00
- Average predicted points: 66.89
- Average actual points: 62.00
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
- Predicted score: 69.07
- Actual score: 51.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.70 | 13.27 | 21.28 | 3.00 | 92.4 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.00 | 0.11 | 0.00 | 2.4 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 6.74 | 19.22 | 29.55 | 2.00 | 91.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.79 | 14.13 | 22.42 | 11.00 | 92.5 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.68 | 13.25 | 20.14 | 2.00 | 92.9 | 90.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.0 | 3.80 | 11.25 | 17.76 | 6.00 | 92.8 | 90.0 |
| Bench 4 | Bench | Reinildo Mandava | DEF | 17 | 3.8 | 2.61 | 7.03 | 10.77 | 0.00 | 70.6 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 7.06 | 20.54 | 33.78 | 6.00 | 89.9 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.94 | 15.94 | 25.43 | 7.00 | 85.3 | 79.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 4.96 | 14.31 | 23.18 | 2.00 | 92.5 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.6 | 6.47 | 18.79 | 29.59 | 4.00 | 92.6 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 6.22 | 17.45 | 27.98 | 4.00 | 92.3 | 86.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.39 | 14.97 | 24.31 | 2.00 | 88.1 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.9 | 5.07 | 14.27 | 23.19 | 2.00 | 85.8 | 90.0 |
| Bench 3 | Bench | Pape Matar Sarr | MID | 18 | 4.5 | 2.92 | 8.18 | 11.07 | 4.00 | 76.9 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 0.00 -> 1.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Declan Rice
- Chip used: none
- Predicted score: 64.81
- Actual score: 56.00
- Transfer: Enzo Fernández -> Elliot Anderson (projected gain 0.09, hit 0)
- Autosub: Elliot Anderson replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.90 | 11.41 | 18.74 | 3.00 | 91.9 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.25 | 0.24 | 0.34 | 0.00 | 3.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.60 | 16.21 | 25.82 | 9.00 | 91.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.28 | 14.54 | 23.10 | 7.00 | 92.4 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.24 | 12.17 | 19.40 | 6.00 | 87.3 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.0 | 4.30 | 11.97 | 18.44 | 2.00 | 93.0 | 90.0 |
| Bench 4 | Bench | Reinildo Mandava | DEF | 17 | 3.8 | 1.02 | 3.64 | 6.05 | 0.00 | 39.4 | 0.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.8 | 7.72 | 22.61 | 36.87 | 0.00 | 92.1 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.07 | 14.47 | 23.27 | 6.00 | 88.3 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.22 | 13.57 | 22.07 | 2.00 | 71.0 | 90.0 |
| Vice Captain | Captain | Declan Rice | MID | 1 | 7.6 | 5.94 | 17.80 | 28.12 | 5.00 | 91.9 | 75.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.76 | 16.51 | 26.77 | 8.00 | 92.4 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.05 | 14.18 | 22.76 | 2.00 | 85.9 | 90.0 |
| Bench 2 | Autosub In | Elliot Anderson | MID | 16 | 5.4 | 3.92 | 11.85 | 19.17 | 1.00 | 80.8 | 90.0 |
| Bench 3 | Bench | Pape Matar Sarr | MID | 18 | 4.5 | 3.23 | 9.07 | 12.76 | 1.00 | 79.2 | 32.0 |

## GW29

- Train rows: 182721
- Bank: 1.40 -> 0.30
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 64.77
- Actual score: 80.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.44) beats the best remaining Triple Captain opportunity (7.60).
- Transfer: Morgan Rogers -> Bryan Mbeumo (projected gain 2.72, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.44) beats the best remaining Triple Captain opportunity (7.60).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.57 | 11.52 | 18.59 | 7.00 | 91.9 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.10 | 0.14 | 0.24 | 0.00 | 1.5 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.52 | 17.01 | 27.04 | 11.00 | 92.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.01 | 14.35 | 22.75 | 1.00 | 90.9 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.58 | 12.91 | 20.37 | 1.00 | 91.4 | 90.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.0 | 3.53 | 10.44 | 16.57 | 8.00 | 91.6 | 90.0 |
| Bench 4 | Bench | Reinildo Mandava | DEF | 17 | 3.8 | 0.76 | 2.49 | 4.91 | 0.00 | 27.9 | 0.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.7 | 4.73 | 15.16 | 27.59 | 2.00 | 51.8 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.64 | 14.36 | 23.94 | 19.00 | 80.6 | 84.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.51 | 13.81 | 22.39 | 2.00 | 83.9 | 90.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.44 | 18.39 | 29.53 | 7.00 | 92.6 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.5 | 4.43 | 14.29 | 23.52 | 3.00 | 89.5 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.7 | 4.88 | 14.10 | 22.82 | 1.00 | 79.0 | 76.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.59 | 11.40 | 18.35 | 12.00 | 81.0 | 90.0 |
| Bench 3 | Bench | Pape Matar Sarr | MID | 18 | 4.5 | 2.49 | 7.20 | 11.13 | 1.00 | 57.9 | 90.0 |

## GW30

- Train rows: 183541
- Bank: 0.30 -> 0.50
- Free transfers: 2 -> 2
- Captain: João Pedro Junqueira de Jesus
- Vice captain: Antoine Semenyo
- Effective captain: João Pedro Junqueira de Jesus
- Chip used: bench_boost
- Predicted score: 68.90
- Actual score: 61.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.41) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Marc Guéhi -> Marcos Senesi Barón (projected gain 0.73, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.41) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.87 | 11.64 | 18.97 | 7.00 | 92.7 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.11 | 0.17 | 0.00 | 2.3 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.10 | 15.09 | 25.09 | 9.00 | 90.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.97 | 13.92 | 22.72 | 2.00 | 85.8 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.22 | 11.52 | 18.36 | 10.00 | 92.8 | 90.0 |
| Bench 2 | Bench Boost | James Hill | DEF | 4 | 4.1 | 3.89 | 10.81 | 17.71 | 8.00 | 89.9 | 90.0 |
| Bench 4 | Bench Boost | Reinildo Mandava | DEF | 17 | 3.8 | 0.00 | 0.12 | 1.60 | 0.00 | 5.2 | 0.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.6 | 6.07 | 19.12 | 32.06 | 2.00 | 84.4 | 90.0 |
| Captain | Captain | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.71 | 18.37 | 29.74 | 2.00 | 91.7 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.04 | 14.40 | 22.91 | 6.00 | 90.7 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 8.1 | 6.29 | 18.41 | 29.06 | 2.00 | 91.0 | 74.0 |
| XI | XI | Declan Rice | MID | 1 | 7.4 | 4.69 | 13.69 | 23.22 | 3.00 | 85.4 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.54 | 13.01 | 20.75 | 2.00 | 90.8 | 87.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.7 | 4.28 | 12.89 | 21.84 | 2.00 | 72.9 | 74.0 |
| Bench 3 | Bench Boost | Pape Matar Sarr | MID | 18 | 4.5 | 2.52 | 7.22 | 11.57 | 4.00 | 66.4 | 90.0 |