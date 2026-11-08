# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 276.24
- Total actual points: 264.00
- Average predicted points: 69.06
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
- Predicted score: 71.00
- Actual score: 51.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.81 | 13.33 | 21.09 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 1.5 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 6.93 | 19.41 | 29.85 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.94 | 14.07 | 22.37 | 11.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.83 | 13.25 | 20.17 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.0 | 3.93 | 11.32 | 17.76 | 6.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Reinildo Mandava | DEF | 17 | 3.8 | 2.57 | 6.89 | 10.51 | 0.00 | 69.0 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 7.30 | 20.98 | 34.66 | 6.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.12 | 16.22 | 25.66 | 7.00 | 84.1 | 79.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.12 | 14.29 | 23.06 | 2.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.6 | 6.60 | 18.84 | 29.51 | 4.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 6.34 | 17.43 | 28.08 | 4.00 | 90.0 | 86.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.49 | 14.98 | 24.31 | 2.00 | 85.7 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.9 | 5.21 | 14.46 | 23.51 | 2.00 | 83.7 | 90.0 |
| Bench 3 | Bench | Pape Matar Sarr | MID | 18 | 4.5 | 2.95 | 8.30 | 11.29 | 4.00 | 78.1 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 0.00 -> 0.90
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Declan Rice
- Chip used: none
- Predicted score: 66.91
- Actual score: 67.00
- Transfer: Enzo Fernández -> Harry Wilson (projected gain 1.26, hit 0)
- Autosub: Marc Guéhi replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.02 | 11.48 | 18.67 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.23 | 0.14 | 0.18 | 0.00 | 2.3 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.82 | 16.52 | 26.11 | 9.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.37 | 14.54 | 22.88 | 7.00 | 90.0 | 90.0 |
| Bench 2 | Autosub In | Marc Guéhi | DEF | 13 | 5.2 | 4.23 | 12.11 | 19.12 | 6.00 | 84.6 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.0 | 4.44 | 11.93 | 18.28 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Reinildo Mandava | DEF | 17 | 3.8 | 0.99 | 3.52 | 5.83 | 0.00 | 38.1 | 0.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.8 | 7.85 | 22.60 | 36.86 | 0.00 | 90.0 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.29 | 14.58 | 23.38 | 6.00 | 85.8 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.44 | 13.88 | 22.55 | 2.00 | 69.3 | 90.0 |
| Vice Captain | Captain | Declan Rice | MID | 1 | 7.6 | 6.11 | 17.82 | 28.01 | 5.00 | 90.0 | 75.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.87 | 16.69 | 26.63 | 8.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.13 | 14.12 | 22.70 | 2.00 | 83.2 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.71 | 13.26 | 20.78 | 12.00 | 87.7 | 71.0 |
| Bench 3 | Bench | Pape Matar Sarr | MID | 18 | 4.5 | 3.26 | 9.18 | 12.98 | 1.00 | 80.4 | 32.0 |

## GW29

- Train rows: 182721
- Bank: 0.90 -> 1.20
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 67.08
- Actual score: 83.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.60) beats the best remaining Triple Captain opportunity (7.79).
- Transfer: Morgan Rogers -> Morgan Gibbs-White (projected gain 0.51, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.60) beats the best remaining Triple Captain opportunity (7.79).
- Autosub: James Hill replaced Harry Wilson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.82 | 11.63 | 18.93 | 7.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.08 | 0.04 | 0.06 | 0.00 | 0.6 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.65 | 16.98 | 27.00 | 11.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.13 | 14.30 | 22.49 | 1.00 | 87.9 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.64 | 12.96 | 20.38 | 1.00 | 89.1 | 90.0 |
| Bench 2 | Autosub In | James Hill | DEF | 4 | 4.0 | 3.63 | 10.41 | 16.33 | 8.00 | 88.9 | 90.0 |
| Bench 4 | Bench | Reinildo Mandava | DEF | 17 | 3.8 | 0.73 | 2.37 | 4.70 | 0.00 | 26.8 | 0.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.7 | 5.32 | 16.79 | 28.99 | 2.00 | 54.3 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.85 | 14.49 | 23.87 | 19.00 | 78.6 | 84.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.67 | 14.12 | 22.66 | 2.00 | 81.7 | 90.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.60 | 18.55 | 29.41 | 7.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.5 | 4.82 | 15.15 | 24.61 | 3.00 | 90.0 | 90.0 |
| XI | Bench | Harry Wilson | MID | 10 | 5.9 | 4.58 | 12.68 | 20.18 | 0.00 | 77.7 | 0.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.3 | 3.80 | 11.94 | 19.48 | 8.00 | 83.3 | 89.0 |
| Bench 3 | Bench | Pape Matar Sarr | MID | 18 | 4.5 | 2.52 | 7.32 | 11.36 | 1.00 | 59.1 | 90.0 |

## GW30

- Train rows: 183541
- Bank: 1.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: João Pedro Junqueira de Jesus
- Vice captain: Antoine Semenyo
- Effective captain: João Pedro Junqueira de Jesus
- Chip used: bench_boost
- Predicted score: 71.24
- Actual score: 63.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.58) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Harry Wilson -> Dominik Szoboszlai (projected gain 2.26, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.58) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.06 | 11.65 | 19.03 | 7.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.02 | 0.01 | 0.00 | 1.4 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.32 | 15.40 | 25.56 | 9.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.15 | 14.02 | 22.29 | 2.00 | 84.4 | 90.0 |
| Bench 2 | Bench Boost | Marc Guéhi | DEF | 13 | 5.2 | 4.03 | 11.40 | 18.27 | 2.00 | 83.2 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.1 | 4.08 | 10.89 | 17.59 | 8.00 | 87.3 | 90.0 |
| Bench 4 | Bench Boost | Reinildo Mandava | DEF | 17 | 3.8 | 0.00 | 0.00 | 1.35 | 0.00 | 3.7 | 0.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.6 | 6.32 | 19.37 | 32.35 | 2.00 | 83.1 | 90.0 |
| Captain | Captain | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.95 | 18.80 | 30.34 | 2.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.26 | 14.46 | 23.02 | 6.00 | 88.4 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 8.1 | 6.53 | 18.69 | 29.58 | 2.00 | 90.0 | 74.0 |
| XI | XI | Declan Rice | MID | 1 | 7.4 | 4.93 | 14.16 | 23.50 | 3.00 | 84.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.9 | 4.82 | 13.46 | 21.05 | 11.00 | 82.4 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.3 | 4.30 | 12.36 | 20.22 | 3.00 | 83.0 | 73.0 |
| Bench 3 | Bench Boost | Pape Matar Sarr | MID | 18 | 4.5 | 2.55 | 7.35 | 11.81 | 4.00 | 67.6 | 90.0 |