# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 276.67
- Total actual points: 255.00
- Average predicted points: 69.17
- Average actual points: 63.75
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
- Predicted score: 71.40
- Actual score: 51.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.86 | 13.50 | 21.39 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.10 | 0.26 | 0.48 | 0.00 | 5.7 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 6.88 | 19.17 | 29.40 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.04 | 14.39 | 22.87 | 11.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.93 | 13.58 | 20.73 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.0 | 3.83 | 10.82 | 16.75 | 6.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Reinildo Mandava | DEF | 17 | 3.8 | 2.56 | 6.89 | 10.49 | 0.00 | 68.3 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 7.32 | 20.78 | 34.15 | 6.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.19 | 16.31 | 25.71 | 7.00 | 86.1 | 79.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.01 | 13.75 | 21.98 | 2.00 | 85.6 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.6 | 6.58 | 18.81 | 29.48 | 4.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 6.40 | 17.57 | 28.26 | 4.00 | 90.0 | 86.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.60 | 15.32 | 24.85 | 2.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.9 | 5.28 | 14.63 | 23.76 | 2.00 | 86.2 | 90.0 |
| Bench 3 | Bench | Pape Matar Sarr | MID | 18 | 4.5 | 3.00 | 8.45 | 11.55 | 4.00 | 80.6 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 0.00 -> 0.90
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Declan Rice
- Chip used: none
- Predicted score: 66.93
- Actual score: 67.00
- Transfer: Enzo Fernández -> Harry Wilson (projected gain 1.71, hit 0)
- Autosub: James Hill replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.10 | 11.71 | 19.02 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.35 | 0.49 | 0.69 | 0.00 | 6.4 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.80 | 16.33 | 25.71 | 9.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.47 | 14.88 | 23.45 | 7.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.35 | 12.49 | 19.75 | 6.00 | 89.3 | 90.0 |
| Bench 2 | Autosub In | James Hill | DEF | 4 | 4.0 | 4.35 | 11.43 | 17.26 | 2.00 | 88.8 | 90.0 |
| Bench 4 | Bench | Reinildo Mandava | DEF | 17 | 3.8 | 1.05 | 3.66 | 5.97 | 0.00 | 39.5 | 0.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.8 | 7.83 | 22.36 | 36.32 | 0.00 | 90.0 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.17 | 14.05 | 22.34 | 6.00 | 79.9 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.50 | 13.93 | 22.53 | 2.00 | 70.8 | 90.0 |
| Vice Captain | Captain | Declan Rice | MID | 1 | 7.6 | 6.11 | 17.74 | 27.82 | 5.00 | 90.0 | 75.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.94 | 16.88 | 26.93 | 8.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.16 | 14.28 | 23.08 | 2.00 | 85.3 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.67 | 13.03 | 20.29 | 12.00 | 85.3 | 71.0 |
| Bench 3 | Bench | Pape Matar Sarr | MID | 18 | 4.5 | 3.28 | 9.28 | 13.16 | 1.00 | 82.0 | 32.0 |

## GW29

- Train rows: 182721
- Bank: 0.90 -> 1.20
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 66.46
- Actual score: 83.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.56) beats the best remaining Triple Captain opportunity (7.74).
- Transfer: Morgan Rogers -> Morgan Gibbs-White (projected gain 0.29, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.56) beats the best remaining Triple Captain opportunity (7.74).
- Autosub: James Hill replaced Harry Wilson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.81 | 11.69 | 19.17 | 7.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.12 | 0.22 | 0.45 | 0.00 | 2.3 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.53 | 16.64 | 26.49 | 11.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.15 | 14.48 | 22.95 | 1.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.66 | 13.15 | 20.85 | 1.00 | 90.0 | 90.0 |
| Bench 2 | Autosub In | James Hill | DEF | 4 | 4.0 | 3.46 | 9.78 | 15.24 | 8.00 | 81.9 | 90.0 |
| Bench 4 | Bench | Reinildo Mandava | DEF | 17 | 3.8 | 0.74 | 2.40 | 4.78 | 0.00 | 26.7 | 0.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.7 | 5.32 | 16.62 | 28.65 | 2.00 | 53.6 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.79 | 14.26 | 23.51 | 19.00 | 76.4 | 84.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.50 | 13.53 | 21.67 | 2.00 | 74.7 | 90.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.56 | 18.52 | 29.50 | 7.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.5 | 4.76 | 14.97 | 24.35 | 3.00 | 89.1 | 90.0 |
| XI | Bench | Harry Wilson | MID | 10 | 5.9 | 4.46 | 12.28 | 19.56 | 0.00 | 73.2 | 0.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.3 | 3.80 | 11.96 | 19.62 | 8.00 | 84.0 | 89.0 |
| Bench 3 | Bench | Pape Matar Sarr | MID | 18 | 4.5 | 2.53 | 7.39 | 11.55 | 1.00 | 60.4 | 90.0 |

## GW30

- Train rows: 183541
- Bank: 1.20 -> 1.60
- Free transfers: 2 -> 2
- Captain: João Pedro Junqueira de Jesus
- Vice captain: Antoine Semenyo
- Effective captain: João Pedro Junqueira de Jesus
- Chip used: bench_boost
- Predicted score: 71.88
- Actual score: 54.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.76) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Harry Wilson -> Elliot Anderson (projected gain 3.04, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.76) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.17 | 11.94 | 19.47 | 7.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 3.8 | 0.07 | 0.37 | 0.54 | 0.00 | 5.5 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.33 | 15.32 | 25.33 | 9.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.27 | 14.42 | 22.96 | 2.00 | 89.3 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.15 | 11.79 | 18.93 | 2.00 | 88.1 | 90.0 |
| Bench 2 | Bench Boost | James Hill | DEF | 4 | 4.1 | 4.00 | 10.42 | 16.62 | 8.00 | 82.7 | 90.0 |
| Bench 4 | Bench Boost | Reinildo Mandava | DEF | 17 | 3.8 | 0.03 | 0.33 | 1.74 | 0.00 | 7.4 | 0.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.6 | 6.38 | 19.29 | 32.03 | 2.00 | 83.4 | 90.0 |
| Captain | Captain | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.94 | 18.67 | 30.05 | 2.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.19 | 14.04 | 22.14 | 6.00 | 84.0 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 8.1 | 6.58 | 18.83 | 29.80 | 2.00 | 90.0 | 74.0 |
| XI | XI | Declan Rice | MID | 1 | 7.4 | 5.00 | 14.23 | 23.47 | 3.00 | 85.5 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.5 | 4.79 | 13.27 | 21.11 | 2.00 | 90.0 | 87.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.3 | 4.38 | 12.57 | 20.53 | 3.00 | 86.2 | 73.0 |
| Bench 3 | Bench Boost | Pape Matar Sarr | MID | 18 | 4.5 | 2.66 | 7.62 | 12.17 | 4.00 | 71.3 | 90.0 |