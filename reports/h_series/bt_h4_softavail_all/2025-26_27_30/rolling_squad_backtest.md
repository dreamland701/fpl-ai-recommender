# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 253.61
- Total actual points: 229.00
- Average predicted points: 63.40
- Average actual points: 57.25
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
- Predicted score: 67.04
- Actual score: 51.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.56 | 13.30 | 21.16 | 3.00 | 89.3 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.05 | 0.00 | 1.9 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 6.50 | 18.79 | 29.17 | 2.00 | 87.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.57 | 13.40 | 21.65 | 11.00 | 89.8 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.6 | 3.89 | 11.26 | 18.20 | 1.00 | 88.9 | 11.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.0 | 3.59 | 10.49 | 16.73 | 6.00 | 87.1 | 90.0 |
| Bench 4 | Bench | James Justin | DEF | 11 | 3.9 | 2.47 | 8.08 | 13.48 | 2.00 | 72.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 6.71 | 19.89 | 33.24 | 6.00 | 86.5 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.90 | 16.65 | 25.83 | 7.00 | 85.3 | 79.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 4.42 | 12.74 | 19.04 | 2.00 | 90.7 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.6 | 6.26 | 18.50 | 29.55 | 4.00 | 91.3 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.6 | 6.55 | 18.42 | 29.16 | 3.00 | 86.1 | 74.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.91 | 16.70 | 27.06 | 4.00 | 89.0 | 86.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.9 | 5.07 | 14.82 | 23.53 | 2.00 | 85.7 | 90.0 |
| Bench 3 | Bench | Pape Matar Sarr | MID | 18 | 4.5 | 2.92 | 8.18 | 11.07 | 4.00 | 76.9 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Declan Rice
- Chip used: none
- Predicted score: 60.02
- Actual score: 46.00
- Transfer: none
- No transfer was applied this week.
- Autosub: Enzo Fernández replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.65 | 10.87 | 17.47 | 3.00 | 84.3 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.03 | 0.10 | 0.00 | 2.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.38 | 15.84 | 25.10 | 9.00 | 87.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.00 | 13.95 | 22.51 | 7.00 | 91.6 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.0 | 4.27 | 11.51 | 17.48 | 2.00 | 89.3 | 90.0 |
| Bench 3 | Bench | James Justin | DEF | 11 | 3.9 | 2.78 | 8.66 | 13.76 | 2.00 | 82.2 | 86.0 |
| Bench 4 | Bench | Nordi Mukiele | DEF | 17 | 4.6 | 1.91 | 6.75 | 11.68 | 0.00 | 50.2 | 0.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.8 | 7.39 | 21.85 | 35.72 | 0.00 | 88.8 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.20 | 13.69 | 22.00 | 2.00 | 71.3 | 90.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 3.42 | 10.41 | 15.86 | 2.00 | 86.3 | 90.0 |
| Vice Captain | Captain | Declan Rice | MID | 1 | 7.6 | 5.81 | 17.55 | 28.00 | 5.00 | 89.7 | 75.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.51 | 16.09 | 25.67 | 8.00 | 90.2 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.75 | 15.04 | 25.15 | 1.00 | 74.1 | 85.0 |
| Bench 2 | Autosub In | Enzo Fernández | MID | 7 | 6.8 | 3.21 | 11.43 | 19.41 | 1.00 | 74.0 | 85.0 |
| XI | XI | Pape Matar Sarr | MID | 18 | 4.5 | 3.23 | 9.07 | 12.76 | 1.00 | 79.2 | 32.0 |

## GW29

- Train rows: 182721
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Antoine Semenyo
- Chip used: bench_boost
- Predicted score: 60.55
- Actual score: 83.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.72) beats the best remaining Bench Boost opportunity (7.77).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.72) beats the best remaining Bench Boost opportunity (7.77).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.52 | 11.34 | 18.52 | 7.00 | 87.3 | 90.0 |
| Bench 1 | Bench Boost | Marcus Bettinelli | GK | 13 | 3.8 | 0.05 | 0.10 | 0.17 | 0.00 | 1.9 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.11 | 15.98 | 25.35 | 11.00 | 84.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.81 | 14.05 | 22.17 | 1.00 | 87.9 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.0 | 3.43 | 10.05 | 15.73 | 8.00 | 88.0 | 90.0 |
| XI | XI | James Justin | DEF | 11 | 3.9 | 2.98 | 8.31 | 12.93 | 2.00 | 80.6 | 73.0 |
| Bench 4 | Bench Boost | Nordi Mukiele | DEF | 17 | 4.5 | 1.20 | 4.21 | 8.20 | 0.00 | 28.5 | 0.0 |
| Bench 2 | Bench Boost | Erling Haaland | FWD | 13 | 14.7 | 4.50 | 14.94 | 26.29 | 2.00 | 48.5 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.60 | 14.13 | 23.10 | 19.00 | 80.2 | 84.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 3.19 | 9.82 | 15.04 | 2.00 | 87.7 | 69.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.16 | 17.75 | 27.97 | 7.00 | 87.6 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.83 | 15.96 | 26.58 | 9.00 | 79.9 | 84.0 |
| XI | XI | Declan Rice | MID | 1 | 7.5 | 4.39 | 14.93 | 24.04 | 3.00 | 87.1 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 3.12 | 10.96 | 17.99 | 4.00 | 73.1 | 78.0 |
| Bench 3 | Bench Boost | Pape Matar Sarr | MID | 18 | 4.5 | 2.49 | 7.20 | 11.13 | 1.00 | 57.9 | 90.0 |

## GW30

- Train rows: 183541
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: João Pedro Junqueira de Jesus
- Vice captain: Antoine Semenyo
- Effective captain: João Pedro Junqueira de Jesus
- Chip used: triple_captain
- Predicted score: 66.00
- Actual score: 49.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.56) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on João Pedro Junqueira de Jesus. Optimizer chose Triple Captain here because the current estimated captain upside (6.56) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.95 | 11.11 | 18.54 | 7.00 | 88.5 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.09 | 0.17 | 0.00 | 2.6 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 4.96 | 14.56 | 24.58 | 9.00 | 87.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.77 | 13.52 | 22.12 | 2.00 | 86.2 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.1 | 3.85 | 10.50 | 17.24 | 8.00 | 88.0 | 90.0 |
| XI | XI | James Justin | DEF | 11 | 3.9 | 2.51 | 7.54 | 12.30 | 6.00 | 72.2 | 90.0 |
| Bench 4 | Bench | Nordi Mukiele | DEF | 17 | 4.5 | 0.23 | 1.42 | 3.95 | 0.00 | 4.1 | 0.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.6 | 6.00 | 19.20 | 32.29 | 2.00 | 85.1 | 90.0 |
| Captain | Captain | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.56 | 17.88 | 29.12 | 2.00 | 89.1 | 90.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.5 | 2.41 | 7.11 | 12.24 | 1.00 | 63.6 | 45.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 8.1 | 6.09 | 17.48 | 28.00 | 2.00 | 85.6 | 74.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.53 | 17.16 | 28.30 | 2.00 | 85.5 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.4 | 4.90 | 14.56 | 24.48 | 3.00 | 87.3 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.6 | 3.76 | 12.12 | 19.80 | 2.00 | 79.8 | 90.0 |
| Bench 2 | Bench | Pape Matar Sarr | MID | 18 | 4.5 | 2.52 | 7.22 | 11.57 | 4.00 | 66.4 | 90.0 |