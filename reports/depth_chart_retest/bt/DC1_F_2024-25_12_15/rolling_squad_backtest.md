# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 229.68
- Total actual points: 231.00
- Average predicted points: 57.42
- Average actual points: 57.75
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW11 are included before the first simulated week.
- League-average scores were not available for this run.

## GW12

- Train rows: 140908
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 63.61
- Actual score: 34.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.83 | 11.07 | 17.98 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.16 | 0.66 | 0.96 | 0.00 | 7.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.46 | 12.12 | 19.35 | 1.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 3.66 | 10.17 | 16.18 | 1.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.71 | 10.14 | 16.51 | 0.00 | 85.8 | 90.0 |
| Bench 3 | Bench | Milos Kerkez | DEF | 3 | 4.4 | 2.65 | 7.95 | 13.07 | 1.00 | 75.7 | 80.0 |
| Bench 4 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 1.97 | 6.49 | 10.82 | 0.00 | 79.1 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.2 | 8.06 | 22.47 | 37.24 | 2.00 | 90.0 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 5.82 | 16.08 | 25.36 | 2.00 | 88.9 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 6.0 | 4.12 | 12.79 | 20.29 | 2.00 | 81.7 | 85.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.0 | 7.56 | 21.22 | 34.68 | 13.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 6.02 | 16.43 | 26.19 | 2.00 | 90.0 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 4.50 | 12.18 | 19.80 | 1.00 | 82.5 | 58.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.4 | 3.81 | 10.87 | 17.43 | 2.00 | 79.2 | 81.0 |
| Bench 2 | Bench | Harry Winks | MID | 11 | 4.5 | 3.17 | 9.09 | 14.44 | 1.00 | 78.8 | 10.0 |

## GW13

- Train rows: 141592
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 61.50
- Actual score: 72.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.73) beats the best remaining Triple Captain opportunity (8.42).
- Transfer: Emile Smith Rowe -> Alex Iwobi (projected gain 1.83, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.73) beats the best remaining Triple Captain opportunity (8.42).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.24 | 11.83 | 19.05 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.51 | 0.83 | 1.19 | 0.00 | 6.4 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.68 | 10.80 | 17.21 | 6.00 | 86.6 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.04 | 9.09 | 14.81 | 2.00 | 80.3 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 2.69 | 8.48 | 13.64 | 2.00 | 72.7 | 90.0 |
| Bench 2 | Bench | Milos Kerkez | DEF | 3 | 4.4 | 2.52 | 7.94 | 13.14 | 7.00 | 72.8 | 90.0 |
| Bench 4 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.66 | 2.91 | 5.42 | 0.00 | 32.5 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 15.1 | 5.97 | 18.69 | 32.34 | 2.00 | 81.3 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 4.31 | 13.79 | 22.15 | 1.00 | 63.8 | 21.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 6.0 | 4.00 | 11.07 | 18.00 | 2.00 | 74.2 | 78.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 7.73 | 23.11 | 36.68 | 13.00 | 90.0 | 83.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.77 | 13.11 | 21.30 | 9.00 | 71.1 | 65.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.6 | 3.54 | 10.80 | 17.58 | 5.00 | 83.0 | 85.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.4 | 3.07 | 9.37 | 15.54 | 2.00 | 70.0 | 65.0 |
| Bench 3 | Bench | Harry Winks | MID | 11 | 4.5 | 1.33 | 4.80 | 8.42 | 0.00 | 31.9 | 0.0 |

## GW14

- Train rows: 142282
- Bank: 0.20 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 59.14
- Actual score: 88.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (3.91) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Alexander Isak -> Nicolas Jackson (projected gain 9.66, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (3.91) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.98 | 11.10 | 18.04 | 6.00 | 89.1 | 90.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.15 | 0.54 | 0.89 | 0.00 | 6.8 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.12 | 12.21 | 19.68 | 1.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.27 | 9.23 | 14.99 | 6.00 | 82.3 | 90.0 |
| XI | XI | Milos Kerkez | DEF | 3 | 4.4 | 2.97 | 8.58 | 13.89 | 8.00 | 76.4 | 90.0 |
| Bench 2 | Bench Boost | Lewis Hall | DEF | 15 | 4.4 | 2.47 | 8.04 | 13.28 | 1.00 | 76.9 | 90.0 |
| Bench 4 | Bench Boost | Jan Bednarek | DEF | 17 | 4.0 | 0.39 | 1.78 | 3.50 | 0.00 | 24.2 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 15.0 | 6.28 | 19.50 | 33.30 | 5.00 | 83.3 | 90.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 8.1 | 6.15 | 17.65 | 27.35 | 0.00 | 90.0 | 0.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.9 | 3.24 | 9.93 | 16.46 | 0.00 | 69.7 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 7.45 | 23.01 | 36.97 | 18.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.65 | 13.08 | 22.59 | 2.00 | 73.4 | 90.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.6 | 3.84 | 11.04 | 17.98 | 15.00 | 82.4 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.3 | 2.85 | 8.22 | 13.74 | 8.00 | 62.1 | 86.0 |
| Bench 3 | Bench Boost | Harry Winks | MID | 11 | 4.5 | 0.90 | 2.96 | 5.47 | 0.00 | 17.5 | 0.0 |

## GW15

- Train rows: 142975
- Bank: 0.60 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 45.43
- Actual score: 37.00
- Transfer: Danny Welbeck -> Francisco Evanilson de Lima Barbosa (projected gain 7.23, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.13 | 12.08 | 19.50 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.36 | 0.61 | 0.95 | 0.00 | 5.5 | 0.0 |
| XI | XI | Milos Kerkez | DEF | 3 | 4.5 | 3.19 | 9.32 | 15.04 | 2.00 | 79.1 | 90.0 |
| Bench 2 | Bench | Virgil van Dijk | DEF | 12 | 6.3 | 0.00 | 9.30 | 15.76 | 0.00 | 0.0 | 0.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 2.80 | 8.98 | 14.74 | 1.00 | 81.6 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 2.57 | 7.43 | 12.20 | 1.00 | 77.0 | 82.0 |
| Bench 3 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.00 | 0.74 | 1.97 | 0.00 | 12.9 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.0 | 6.69 | 19.93 | 33.93 | 7.00 | 90.0 | 90.0 |
| XI | XI | Francisco Evanilson de Lima Barbosa | FWD | 3 | 6.1 | 3.88 | 11.80 | 18.86 | 2.00 | 66.7 | 73.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 8.1 | 3.31 | 10.74 | 17.57 | 2.00 | 38.2 | 75.0 |
| Bench 4 | Bench | Mohamed Salah | MID | 12 | 13.1 | 0.00 | 22.07 | 36.90 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.45 | 14.16 | 23.88 | 9.00 | 85.6 | 75.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.3 | 4.13 | 11.14 | 17.98 | 2.00 | 76.0 | 90.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.6 | 3.36 | 11.06 | 18.10 | 2.00 | 84.4 | 90.0 |
| XI | Bench | Harry Winks | MID | 11 | 4.5 | 0.23 | 1.30 | 2.81 | 0.00 | 5.7 | 0.0 |