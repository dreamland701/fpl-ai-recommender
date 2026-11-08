# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 274.93
- Total actual points: 249.00
- Average predicted points: 68.73
- Average actual points: 62.25
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
- Predicted score: 70.96
- Actual score: 47.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.81 | 13.32 | 21.08 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.00 | 0.14 | 0.00 | 2.4 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 6.94 | 19.40 | 29.82 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.93 | 14.00 | 22.22 | 11.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.82 | 13.16 | 19.99 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.0 | 3.91 | 11.27 | 17.68 | 6.00 | 90.0 | 90.0 |
| Bench 4 | Bench | James Justin | DEF | 11 | 3.9 | 2.46 | 8.03 | 13.36 | 2.00 | 72.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 7.23 | 20.58 | 33.83 | 6.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.16 | 14.55 | 23.60 | 2.00 | 90.0 | 90.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 4.81 | 13.07 | 19.55 | 2.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.6 | 6.68 | 19.19 | 30.17 | 4.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 6.76 | 18.26 | 29.64 | 3.00 | 87.8 | 74.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 6.36 | 17.52 | 28.28 | 4.00 | 90.0 | 86.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.9 | 5.23 | 14.63 | 23.89 | 2.00 | 83.7 | 90.0 |
| Bench 3 | Bench | Kobbie Mainoo | MID | 14 | 4.6 | 2.91 | 8.41 | 13.23 | 3.00 | 72.1 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 0.00 -> 0.90
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Declan Rice
- Chip used: none
- Predicted score: 66.26
- Actual score: 66.00
- Transfer: Enzo Fernández -> Harry Wilson (projected gain 2.07, hit 0)
- Autosub: Mateus Mané replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.02 | 11.48 | 18.66 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.25 | 0.25 | 0.37 | 0.00 | 3.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.82 | 16.51 | 26.09 | 9.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.35 | 14.46 | 22.75 | 7.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.22 | 12.03 | 18.97 | 6.00 | 84.2 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.0 | 4.42 | 11.89 | 18.21 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | James Justin | DEF | 11 | 3.9 | 2.78 | 8.63 | 13.71 | 2.00 | 82.1 | 86.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.8 | 7.78 | 22.20 | 36.01 | 0.00 | 90.0 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.32 | 14.82 | 23.93 | 6.00 | 85.8 | 90.0 |
| Bench 2 | Autosub In | Mateus Mané | FWD | 20 | 4.6 | 3.86 | 11.32 | 17.33 | 2.00 | 90.0 | 90.0 |
| Vice Captain | Captain | Declan Rice | MID | 1 | 7.6 | 6.21 | 18.24 | 28.78 | 5.00 | 90.0 | 75.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.89 | 16.78 | 26.85 | 8.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.74 | 15.13 | 24.99 | 1.00 | 70.4 | 85.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.72 | 13.34 | 21.00 | 12.00 | 87.3 | 71.0 |
| Bench 3 | Bench | Kobbie Mainoo | MID | 14 | 4.6 | 3.24 | 9.05 | 14.08 | 2.00 | 75.4 | 90.0 |

## GW29

- Train rows: 182721
- Bank: 0.90 -> 0.10
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 67.31
- Actual score: 71.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.62) beats the best remaining Triple Captain opportunity (7.81).
- Transfer: Kobbie Mainoo -> Elliot Anderson (projected gain 1.37, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.62) beats the best remaining Triple Captain opportunity (7.81).
- Autosub: Mateus Mané replaced Harry Wilson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.82 | 11.62 | 18.92 | 7.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.11 | 0.16 | 0.27 | 0.00 | 1.5 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.65 | 16.95 | 26.93 | 11.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.12 | 14.22 | 22.35 | 1.00 | 87.5 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.63 | 12.89 | 20.24 | 1.00 | 88.7 | 90.0 |
| Bench 3 | Bench | James Hill | DEF | 4 | 4.0 | 3.61 | 10.37 | 16.28 | 8.00 | 88.3 | 90.0 |
| Bench 4 | Bench | James Justin | DEF | 11 | 3.9 | 2.97 | 8.30 | 12.89 | 2.00 | 80.5 | 73.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.7 | 5.23 | 16.38 | 28.14 | 2.00 | 53.7 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.70 | 14.32 | 23.13 | 2.00 | 81.6 | 90.0 |
| Bench 2 | Autosub In | Mateus Mané | FWD | 20 | 4.6 | 3.65 | 10.52 | 16.21 | 2.00 | 90.0 | 69.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.62 | 18.61 | 29.57 | 7.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.95 | 16.31 | 27.22 | 9.00 | 78.8 | 84.0 |
| XI | XI | Declan Rice | MID | 1 | 7.5 | 4.93 | 15.62 | 25.47 | 3.00 | 90.0 | 90.0 |
| XI | Bench | Harry Wilson | MID | 10 | 5.9 | 4.58 | 12.77 | 20.42 | 0.00 | 77.2 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.86 | 11.86 | 18.97 | 12.00 | 80.3 | 90.0 |

## GW30

- Train rows: 183541
- Bank: 0.10 -> 0.30
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Erling Haaland
- Effective captain: Antoine Semenyo
- Chip used: bench_boost
- Predicted score: 70.40
- Actual score: 65.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.24) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Marc Guéhi -> Marcos Senesi Barón (projected gain 0.45, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.24) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.06 | 11.63 | 19.00 | 7.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.12 | 0.20 | 0.00 | 2.3 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.31 | 15.34 | 25.45 | 9.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.14 | 13.90 | 22.09 | 2.00 | 83.9 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.39 | 11.79 | 18.66 | 10.00 | 90.0 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.1 | 4.06 | 10.85 | 17.53 | 8.00 | 86.8 | 90.0 |
| Bench 2 | Bench Boost | James Justin | DEF | 11 | 3.9 | 2.51 | 7.53 | 12.28 | 6.00 | 72.2 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 6.25 | 18.99 | 31.56 | 2.00 | 82.7 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.29 | 14.66 | 23.45 | 6.00 | 88.4 | 90.0 |
| Bench 3 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 2.41 | 7.08 | 12.18 | 1.00 | 63.5 | 45.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.54 | 18.75 | 29.74 | 2.00 | 90.0 | 74.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.70 | 17.07 | 27.81 | 2.00 | 83.4 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.4 | 5.03 | 14.62 | 24.36 | 3.00 | 85.5 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.83 | 13.73 | 22.08 | 2.00 | 90.0 | 87.0 |
| Bench 4 | Bench Boost | Harry Wilson | MID | 10 | 5.9 | 2.33 | 7.89 | 13.83 | 3.00 | 34.4 | 90.0 |