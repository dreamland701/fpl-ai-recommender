# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 269.72
- Total actual points: 260.00
- Average predicted points: 67.43
- Average actual points: 65.00
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
- Predicted score: 69.15
- Actual score: 51.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.98 | 13.84 | 21.94 | 3.00 | 91.5 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.00 | 0.11 | 0.00 | 2.4 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 6.79 | 19.24 | 29.93 | 2.00 | 89.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.87 | 14.00 | 22.33 | 11.00 | 91.3 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.61 | 13.30 | 19.84 | 2.00 | 89.1 | 90.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.0 | 3.86 | 11.63 | 18.16 | 6.00 | 91.6 | 90.0 |
| Bench 4 | Bench | Reinildo Mandava | DEF | 17 | 3.8 | 2.61 | 7.03 | 10.77 | 0.00 | 70.6 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 6.86 | 19.97 | 32.65 | 6.00 | 84.7 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.97 | 16.46 | 25.70 | 7.00 | 82.2 | 79.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.11 | 14.30 | 23.05 | 2.00 | 91.7 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.6 | 6.60 | 19.19 | 29.96 | 4.00 | 91.6 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 6.17 | 17.37 | 27.86 | 4.00 | 90.4 | 86.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.39 | 15.00 | 24.32 | 2.00 | 85.7 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.9 | 4.95 | 14.62 | 23.78 | 2.00 | 84.3 | 90.0 |
| Bench 3 | Bench | Pape Matar Sarr | MID | 18 | 4.5 | 2.92 | 8.18 | 11.07 | 4.00 | 76.9 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 0.00 -> 0.90
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Declan Rice
- Chip used: none
- Predicted score: 65.45
- Actual score: 67.00
- Transfer: Enzo Fernández -> Harry Wilson (projected gain 1.27, hit 0)
- Autosub: Marc Guéhi replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.08 | 12.08 | 19.80 | 3.00 | 91.8 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.25 | 0.24 | 0.34 | 0.00 | 3.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.70 | 16.58 | 26.23 | 9.00 | 90.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.33 | 14.48 | 22.73 | 7.00 | 90.6 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.0 | 4.31 | 12.19 | 18.53 | 2.00 | 91.1 | 90.0 |
| Bench 2 | Autosub In | Marc Guéhi | DEF | 13 | 5.2 | 4.11 | 12.10 | 19.16 | 6.00 | 84.7 | 90.0 |
| Bench 4 | Bench | Reinildo Mandava | DEF | 17 | 3.8 | 1.02 | 3.64 | 6.05 | 0.00 | 39.4 | 0.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.8 | 7.61 | 21.73 | 35.55 | 0.00 | 85.7 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.18 | 14.55 | 23.12 | 6.00 | 86.4 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.20 | 13.82 | 22.26 | 2.00 | 67.2 | 90.0 |
| Vice Captain | Captain | Declan Rice | MID | 1 | 7.6 | 6.02 | 18.88 | 29.01 | 5.00 | 90.9 | 75.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.66 | 16.19 | 26.15 | 8.00 | 90.5 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.14 | 14.18 | 22.86 | 2.00 | 84.5 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.62 | 13.27 | 20.52 | 12.00 | 87.9 | 71.0 |
| Bench 3 | Bench | Pape Matar Sarr | MID | 18 | 4.5 | 3.23 | 9.07 | 12.76 | 1.00 | 79.2 | 32.0 |

## GW29

- Train rows: 182721
- Bank: 0.90 -> 1.60
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 65.31
- Actual score: 80.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.53) beats the best remaining Triple Captain opportunity (7.71).
- Transfer: Morgan Rogers -> Dominik Szoboszlai (projected gain 0.30, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.53) beats the best remaining Triple Captain opportunity (7.71).
- Autosub: James Hill replaced Harry Wilson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.85 | 11.93 | 19.62 | 7.00 | 91.5 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.10 | 0.14 | 0.24 | 0.00 | 1.5 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.43 | 16.73 | 26.71 | 11.00 | 89.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.95 | 14.11 | 22.36 | 1.00 | 88.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.48 | 12.95 | 20.40 | 1.00 | 89.3 | 90.0 |
| Bench 2 | Autosub In | James Hill | DEF | 4 | 4.0 | 3.54 | 10.50 | 16.28 | 8.00 | 89.2 | 90.0 |
| Bench 4 | Bench | Reinildo Mandava | DEF | 17 | 3.8 | 0.76 | 2.49 | 4.91 | 0.00 | 27.9 | 0.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.7 | 4.98 | 16.14 | 28.02 | 2.00 | 50.5 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.70 | 14.60 | 23.89 | 19.00 | 78.6 | 84.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.52 | 14.09 | 22.57 | 2.00 | 81.9 | 90.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.53 | 18.27 | 29.28 | 7.00 | 89.1 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.5 | 4.44 | 14.40 | 23.57 | 3.00 | 85.5 | 90.0 |
| XI | Bench | Harry Wilson | MID | 10 | 5.9 | 4.47 | 12.81 | 20.23 | 0.00 | 78.1 | 0.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.9 | 3.92 | 11.89 | 18.79 | 5.00 | 69.1 | 90.0 |
| Bench 3 | Bench | Pape Matar Sarr | MID | 18 | 4.5 | 2.49 | 7.20 | 11.13 | 1.00 | 57.9 | 90.0 |

## GW30

- Train rows: 183541
- Bank: 1.60 -> 2.00
- Free transfers: 2 -> 2
- Captain: João Pedro Junqueira de Jesus
- Vice captain: Antoine Semenyo
- Effective captain: João Pedro Junqueira de Jesus
- Chip used: bench_boost
- Predicted score: 69.81
- Actual score: 62.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.35) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Harry Wilson -> Elliot Anderson (projected gain 2.23, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.35) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.20 | 11.65 | 19.72 | 7.00 | 90.8 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.11 | 0.17 | 0.00 | 2.3 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.08 | 15.16 | 25.41 | 9.00 | 88.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.00 | 13.58 | 22.16 | 2.00 | 83.9 | 90.0 |
| Bench 2 | Bench Boost | Marc Guéhi | DEF | 13 | 5.2 | 3.83 | 10.97 | 18.11 | 2.00 | 82.1 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.1 | 3.95 | 10.65 | 17.39 | 8.00 | 87.6 | 90.0 |
| Bench 4 | Bench Boost | Reinildo Mandava | DEF | 17 | 3.8 | 0.00 | 0.12 | 1.60 | 0.00 | 5.2 | 0.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.6 | 6.12 | 19.11 | 32.12 | 2.00 | 82.2 | 90.0 |
| Captain | Captain | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.76 | 19.06 | 30.07 | 2.00 | 89.7 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.18 | 14.43 | 23.13 | 6.00 | 89.1 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 8.1 | 6.37 | 18.45 | 29.58 | 2.00 | 88.7 | 74.0 |
| XI | XI | Declan Rice | MID | 1 | 7.4 | 4.80 | 14.36 | 24.04 | 3.00 | 84.5 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.9 | 4.58 | 13.67 | 21.18 | 11.00 | 80.8 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.5 | 4.63 | 13.03 | 21.05 | 2.00 | 88.4 | 87.0 |
| Bench 3 | Bench Boost | Pape Matar Sarr | MID | 18 | 4.5 | 2.52 | 7.22 | 11.57 | 4.00 | 66.4 | 90.0 |