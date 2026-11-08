# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 261.66
- Total actual points: 246.00
- Average predicted points: 65.41
- Average actual points: 61.50
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
- Vice captain: Cole Palmer
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 67.45
- Actual score: 51.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.68 | 13.19 | 21.31 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.00 | 0.11 | 0.00 | 2.4 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 6.53 | 18.95 | 29.21 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.64 | 13.50 | 21.64 | 11.00 | 90.0 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.6 | 3.84 | 11.30 | 18.11 | 1.00 | 86.2 | 11.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.0 | 3.73 | 11.05 | 17.43 | 6.00 | 90.0 | 90.0 |
| Bench 4 | Bench | James Justin | DEF | 11 | 3.9 | 2.47 | 8.08 | 13.48 | 2.00 | 72.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 6.85 | 20.24 | 33.06 | 6.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.74 | 15.93 | 24.95 | 7.00 | 83.6 | 79.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 4.39 | 12.55 | 18.39 | 2.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.6 | 6.42 | 19.30 | 30.07 | 4.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.6 | 6.57 | 18.45 | 29.74 | 3.00 | 87.5 | 74.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 6.05 | 16.98 | 27.20 | 4.00 | 90.0 | 86.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.9 | 4.88 | 14.41 | 23.35 | 2.00 | 83.5 | 90.0 |
| Bench 3 | Bench | Pape Matar Sarr | MID | 18 | 4.5 | 2.92 | 8.18 | 11.07 | 4.00 | 76.9 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 0.00 -> 0.90
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Declan Rice
- Chip used: none
- Predicted score: 61.99
- Actual score: 57.00
- Transfer: Enzo Fernández -> Harry Wilson (projected gain 3.81, hit 0)
- Autosub: Pape Matar Sarr replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.02 | 11.53 | 18.76 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.25 | 0.24 | 0.34 | 0.00 | 3.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.53 | 16.25 | 25.90 | 9.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.00 | 13.94 | 22.31 | 7.00 | 90.0 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.0 | 4.19 | 11.79 | 17.99 | 2.00 | 90.0 | 90.0 |
| Bench 3 | Bench | James Justin | DEF | 11 | 3.9 | 2.78 | 8.66 | 13.76 | 2.00 | 82.2 | 86.0 |
| Bench 4 | Bench | Nordi Mukiele | DEF | 17 | 4.6 | 1.91 | 6.75 | 11.68 | 0.00 | 50.2 | 0.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.8 | 7.54 | 21.73 | 35.70 | 0.00 | 90.0 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.08 | 13.69 | 21.88 | 2.00 | 68.8 | 90.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 3.55 | 10.48 | 16.40 | 2.00 | 90.0 | 90.0 |
| Vice Captain | Captain | Declan Rice | MID | 1 | 7.6 | 5.81 | 17.76 | 27.77 | 5.00 | 90.0 | 75.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.56 | 15.89 | 25.42 | 8.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.62 | 15.22 | 25.27 | 1.00 | 70.1 | 85.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.56 | 12.85 | 20.20 | 12.00 | 87.1 | 71.0 |
| Bench 2 | Autosub In | Pape Matar Sarr | MID | 18 | 4.5 | 3.23 | 9.07 | 12.76 | 1.00 | 79.2 | 32.0 |

## GW29

- Train rows: 182721
- Bank: 0.90 -> 0.20
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 63.40
- Actual score: 84.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.30) beats the best remaining Triple Captain opportunity (7.44).
- Transfer: Nordi Mukiele -> Marc Guéhi (projected gain 3.16, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.30) beats the best remaining Triple Captain opportunity (7.44).
- Autosub: Mateus Mané replaced Harry Wilson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.67 | 11.38 | 18.92 | 7.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.10 | 0.14 | 0.24 | 0.00 | 1.5 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.29 | 16.42 | 26.28 | 11.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.81 | 14.03 | 22.03 | 1.00 | 87.7 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.40 | 12.92 | 20.46 | 1.00 | 88.8 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.0 | 3.34 | 10.45 | 16.14 | 8.00 | 88.3 | 90.0 |
| Bench 3 | Bench | James Justin | DEF | 11 | 3.9 | 2.98 | 8.31 | 12.93 | 2.00 | 80.6 | 73.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.7 | 4.93 | 16.23 | 27.85 | 2.00 | 54.7 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.51 | 14.33 | 23.31 | 19.00 | 78.4 | 84.0 |
| Bench 2 | Autosub In | Mateus Mané | FWD | 20 | 4.6 | 3.27 | 9.88 | 15.17 | 2.00 | 90.0 | 69.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.30 | 17.95 | 28.42 | 7.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.79 | 16.24 | 27.27 | 9.00 | 78.5 | 84.0 |
| XI | XI | Declan Rice | MID | 1 | 7.5 | 4.41 | 14.71 | 23.91 | 3.00 | 90.0 | 90.0 |
| XI | Bench | Harry Wilson | MID | 10 | 5.9 | 4.34 | 12.67 | 20.04 | 0.00 | 77.0 | 0.0 |
| Bench 4 | Bench | Pape Matar Sarr | MID | 18 | 4.5 | 2.49 | 7.20 | 11.13 | 1.00 | 57.9 | 90.0 |

## GW30

- Train rows: 183541
- Bank: 0.20 -> 0.60
- Free transfers: 2 -> 2
- Captain: João Pedro Junqueira de Jesus
- Vice captain: Antoine Semenyo
- Effective captain: João Pedro Junqueira de Jesus
- Chip used: bench_boost
- Predicted score: 68.82
- Actual score: 54.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.44) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Harry Wilson -> Elliot Anderson (projected gain 5.83, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.44) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.90 | 11.21 | 18.80 | 7.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.11 | 0.17 | 0.00 | 2.3 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 4.86 | 14.64 | 24.73 | 9.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.79 | 13.61 | 21.82 | 2.00 | 84.1 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 3.67 | 10.76 | 17.48 | 2.00 | 82.9 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.1 | 3.95 | 10.50 | 17.45 | 8.00 | 86.8 | 90.0 |
| Bench 3 | Bench Boost | James Justin | DEF | 11 | 3.9 | 2.51 | 7.54 | 12.30 | 6.00 | 72.2 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.6 | 5.99 | 18.47 | 31.02 | 2.00 | 83.7 | 90.0 |
| Captain | Captain | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.51 | 18.43 | 29.29 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 2.41 | 7.11 | 12.24 | 1.00 | 63.6 | 45.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 8.1 | 6.20 | 17.73 | 28.48 | 2.00 | 90.0 | 74.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.67 | 17.64 | 29.12 | 2.00 | 84.3 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.4 | 4.78 | 14.18 | 23.79 | 3.00 | 84.3 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.5 | 4.54 | 13.04 | 20.99 | 2.00 | 88.7 | 87.0 |
| Bench 2 | Bench Boost | Pape Matar Sarr | MID | 18 | 4.5 | 2.52 | 7.22 | 11.57 | 4.00 | 66.4 | 90.0 |