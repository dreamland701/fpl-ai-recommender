# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 275.99
- Total actual points: 264.00
- Average predicted points: 69.00
- Average actual points: 66.00
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
- Predicted score: 71.02
- Actual score: 51.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.85 | 13.48 | 21.39 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.07 | 0.29 | 0.00 | 2.8 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 6.89 | 19.20 | 29.46 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.99 | 14.30 | 22.79 | 11.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.89 | 13.51 | 20.67 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.0 | 3.83 | 10.82 | 16.78 | 6.00 | 89.9 | 90.0 |
| Bench 4 | Bench | Reinildo Mandava | DEF | 17 | 3.8 | 2.55 | 6.87 | 10.49 | 0.00 | 67.7 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 7.26 | 20.68 | 34.08 | 6.00 | 88.7 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.12 | 16.19 | 25.60 | 7.00 | 84.1 | 79.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.01 | 13.75 | 22.01 | 2.00 | 85.4 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.6 | 6.61 | 18.86 | 29.56 | 4.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 6.36 | 17.51 | 28.23 | 4.00 | 90.0 | 86.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.55 | 15.24 | 24.80 | 2.00 | 89.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.9 | 5.23 | 14.56 | 23.71 | 2.00 | 85.0 | 90.0 |
| Bench 3 | Bench | Pape Matar Sarr | MID | 18 | 4.5 | 2.98 | 8.42 | 11.52 | 4.00 | 79.6 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 0.00 -> 0.90
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Declan Rice
- Chip used: none
- Predicted score: 66.69
- Actual score: 67.00
- Transfer: Enzo Fernández -> Harry Wilson (projected gain 0.72, hit 0)
- Autosub: Marc Guéhi replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.06 | 11.63 | 18.95 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.25 | 0.31 | 0.50 | 0.00 | 3.5 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.78 | 16.31 | 25.72 | 9.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.43 | 14.82 | 23.41 | 7.00 | 90.0 | 90.0 |
| Bench 2 | Autosub In | Marc Guéhi | DEF | 13 | 5.2 | 4.29 | 12.39 | 19.66 | 6.00 | 87.7 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.0 | 4.34 | 11.43 | 17.30 | 2.00 | 88.5 | 90.0 |
| Bench 4 | Bench | Reinildo Mandava | DEF | 17 | 3.8 | 0.97 | 3.53 | 5.85 | 0.00 | 37.3 | 0.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.8 | 7.80 | 22.31 | 36.31 | 0.00 | 90.0 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.18 | 14.07 | 22.40 | 6.00 | 80.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.44 | 13.83 | 22.46 | 2.00 | 69.1 | 90.0 |
| Vice Captain | Captain | Declan Rice | MID | 1 | 7.6 | 6.10 | 17.73 | 27.83 | 5.00 | 90.0 | 75.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.90 | 16.82 | 26.89 | 8.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.19 | 14.35 | 23.13 | 2.00 | 86.1 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.66 | 13.01 | 20.28 | 12.00 | 84.9 | 71.0 |
| Bench 3 | Bench | Pape Matar Sarr | MID | 18 | 4.5 | 3.28 | 9.28 | 13.16 | 1.00 | 81.6 | 32.0 |

## GW29

- Train rows: 182721
- Bank: 0.90 -> 1.20
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 67.10
- Actual score: 83.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.63) beats the best remaining Triple Captain opportunity (7.82).
- Transfer: Morgan Rogers -> Morgan Gibbs-White (projected gain 0.35, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.63) beats the best remaining Triple Captain opportunity (7.82).
- Autosub: James Hill replaced Harry Wilson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.86 | 11.79 | 19.24 | 7.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.10 | 0.21 | 0.39 | 0.00 | 1.8 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.62 | 16.80 | 26.63 | 11.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.19 | 14.57 | 23.01 | 1.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.69 | 13.23 | 20.90 | 1.00 | 90.0 | 90.0 |
| Bench 2 | Autosub In | James Hill | DEF | 4 | 4.0 | 3.54 | 9.92 | 15.38 | 8.00 | 83.7 | 90.0 |
| Bench 4 | Bench | Reinildo Mandava | DEF | 17 | 3.8 | 0.72 | 2.38 | 4.72 | 0.00 | 26.1 | 0.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.7 | 5.28 | 16.57 | 28.57 | 2.00 | 52.7 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.82 | 14.34 | 23.56 | 19.00 | 77.3 | 84.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.58 | 13.69 | 21.83 | 2.00 | 76.7 | 90.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.63 | 18.66 | 29.63 | 7.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.5 | 4.81 | 15.07 | 24.44 | 3.00 | 90.0 | 90.0 |
| XI | Bench | Harry Wilson | MID | 10 | 5.9 | 4.52 | 12.42 | 19.68 | 0.00 | 74.9 | 0.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.3 | 3.83 | 12.04 | 19.67 | 8.00 | 85.0 | 89.0 |
| Bench 3 | Bench | Pape Matar Sarr | MID | 18 | 4.5 | 2.55 | 7.43 | 11.57 | 1.00 | 60.4 | 90.0 |

## GW30

- Train rows: 183541
- Bank: 1.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: João Pedro Junqueira de Jesus
- Vice captain: Antoine Semenyo
- Effective captain: João Pedro Junqueira de Jesus
- Chip used: bench_boost
- Predicted score: 71.19
- Actual score: 63.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.55) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Harry Wilson -> Dominik Szoboszlai (projected gain 3.33, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.55) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.10 | 11.81 | 19.35 | 7.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.19 | 0.35 | 0.00 | 2.6 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.29 | 15.25 | 25.27 | 9.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.22 | 14.32 | 22.88 | 2.00 | 87.8 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.09 | 11.69 | 18.83 | 2.00 | 86.5 | 90.0 |
| Bench 2 | Bench Boost | James Hill | DEF | 4 | 4.1 | 3.98 | 10.39 | 16.61 | 8.00 | 82.0 | 90.0 |
| Bench 4 | Bench Boost | Reinildo Mandava | DEF | 17 | 3.8 | 0.00 | 0.01 | 1.41 | 0.00 | 3.3 | 0.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.6 | 6.28 | 19.11 | 31.84 | 2.00 | 81.1 | 90.0 |
| Captain | Captain | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.92 | 18.67 | 30.09 | 2.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.17 | 14.02 | 22.15 | 6.00 | 83.3 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 8.1 | 6.55 | 18.79 | 29.79 | 2.00 | 90.0 | 74.0 |
| XI | XI | Declan Rice | MID | 1 | 7.4 | 4.92 | 14.08 | 23.32 | 3.00 | 83.6 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.9 | 4.84 | 13.53 | 21.18 | 11.00 | 83.7 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.3 | 4.33 | 12.48 | 20.45 | 3.00 | 84.9 | 73.0 |
| Bench 3 | Bench Boost | Pape Matar Sarr | MID | 18 | 4.5 | 2.57 | 7.47 | 12.03 | 4.00 | 68.9 | 90.0 |