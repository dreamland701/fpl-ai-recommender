# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 238.70
- Total actual points: 267.00
- Average predicted points: 59.67
- Average actual points: 66.75
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
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 62.70
- Actual score: 64.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.47 | 10.06 | 16.40 | 6.00 | 88.5 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.18 | 0.69 | 1.02 | 0.00 | 7.6 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.64 | 12.72 | 20.34 | 1.00 | 90.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.3 | 4.26 | 12.13 | 19.90 | 0.00 | 87.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.1 | 3.84 | 11.36 | 18.20 | 6.00 | 87.4 | 90.0 |
| Bench 3 | Bench | Dara O'Shea | DEF | 10 | 4.0 | 2.48 | 6.88 | 11.23 | 2.00 | 82.1 | 90.0 |
| Bench 4 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 2.13 | 6.86 | 11.34 | 0.00 | 81.6 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 5.44 | 15.03 | 23.69 | 2.00 | 86.1 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.8 | 4.22 | 12.67 | 21.17 | 16.00 | 84.4 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 6.0 | 3.85 | 12.01 | 19.04 | 2.00 | 79.9 | 85.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 7.95 | 22.34 | 36.44 | 13.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.38 | 18.20 | 29.97 | 2.00 | 89.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 6.03 | 16.57 | 26.47 | 2.00 | 90.0 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 4.66 | 12.59 | 20.44 | 1.00 | 85.2 | 58.0 |
| Bench 2 | Bench | Harry Winks | MID | 11 | 4.5 | 3.10 | 8.91 | 14.18 | 1.00 | 77.2 | 10.0 |

## GW13

- Train rows: 141592
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 67.69
- Actual score: 80.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.16) beats the best remaining Triple Captain opportunity (8.92).
- Transfer: Gabriel dos Santos Magalhães -> Pedro Porro (projected gain 3.14, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.16) beats the best remaining Triple Captain opportunity (8.92).
- Autosub: Dara O'Shea replaced Joško Gvardiol.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.85 | 10.75 | 17.35 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.53 | 0.88 | 1.26 | 0.00 | 7.3 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 4.69 | 13.15 | 21.11 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Joško Gvardiol | DEF | 13 | 6.3 | 3.62 | 11.49 | 19.26 | 0.00 | 87.3 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.77 | 11.29 | 18.12 | 6.00 | 85.4 | 90.0 |
| Bench 2 | Autosub In | Dara O'Shea | DEF | 10 | 4.0 | 2.22 | 6.99 | 11.39 | 1.00 | 80.3 | 90.0 |
| Bench 4 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.73 | 2.99 | 5.52 | 0.00 | 34.2 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 6.06 | 17.67 | 27.39 | 2.00 | 90.0 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 4.05 | 13.08 | 21.02 | 1.00 | 62.3 | 21.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 6.0 | 3.80 | 10.49 | 17.07 | 2.00 | 73.0 | 78.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 8.16 | 24.34 | 38.64 | 13.00 | 90.0 | 83.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.56 | 18.65 | 30.22 | 14.00 | 90.0 | 85.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.82 | 13.20 | 21.42 | 9.00 | 72.6 | 65.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 2.97 | 9.34 | 15.68 | 2.00 | 60.0 | 85.0 |
| Bench 3 | Bench | Harry Winks | MID | 11 | 4.5 | 1.26 | 4.59 | 8.08 | 0.00 | 31.2 | 0.0 |

## GW14

- Train rows: 142282
- Bank: 0.60 -> 1.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 61.62
- Actual score: 64.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (3.87) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Alexander Isak -> Nicolas Jackson (projected gain 9.45, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (3.87) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.59 | 10.01 | 16.32 | 6.00 | 86.0 | 90.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.18 | 0.60 | 0.99 | 0.00 | 7.8 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.25 | 12.73 | 20.60 | 1.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 4.04 | 11.78 | 18.89 | 1.00 | 87.6 | 28.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 2.62 | 8.47 | 14.81 | 6.00 | 52.2 | 90.0 |
| Bench 2 | Bench Boost | Dara O'Shea | DEF | 10 | 4.0 | 2.44 | 7.02 | 11.43 | 1.00 | 79.5 | 90.0 |
| Bench 4 | Bench Boost | Jan Bednarek | DEF | 17 | 4.0 | 0.38 | 1.77 | 3.52 | 0.00 | 23.4 | 0.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 8.1 | 5.71 | 16.39 | 25.34 | 0.00 | 87.8 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.27 | 13.92 | 21.60 | 2.00 | 76.7 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.9 | 3.13 | 9.59 | 15.90 | 0.00 | 69.2 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 7.92 | 24.32 | 39.06 | 18.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 7.45 | 20.95 | 33.57 | 7.00 | 90.0 | 78.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.65 | 13.09 | 22.62 | 2.00 | 73.5 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.7 | 3.23 | 9.68 | 16.35 | 2.00 | 67.9 | 70.0 |
| Bench 3 | Bench Boost | Harry Winks | MID | 11 | 4.5 | 0.87 | 2.82 | 5.22 | 0.00 | 17.4 | 0.0 |

## GW15

- Train rows: 142975
- Bank: 1.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Matheus Santos Carneiro Da Cunha
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 46.70
- Actual score: 59.00
- Transfer: Harry Winks -> Morgan Rogers (projected gain 11.01, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.73 | 10.94 | 17.68 | 2.00 | 89.1 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.40 | 0.69 | 1.06 | 0.00 | 6.7 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.03 | 11.50 | 19.32 | 1.00 | 81.4 | 90.0 |
| Bench 2 | Bench | Virgil van Dijk | DEF | 12 | 6.3 | 0.00 | 9.86 | 16.79 | 0.00 | 0.0 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 3.01 | 9.38 | 16.07 | 3.00 | 69.3 | 90.0 |
| XI | XI | Dara O'Shea | DEF | 10 | 4.0 | 2.31 | 6.72 | 11.03 | 1.00 | 77.9 | 90.0 |
| Bench 3 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.00 | 0.63 | 1.84 | 0.00 | 12.3 | 0.0 |
| Vice Captain | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.70 | 13.43 | 21.66 | 1.00 | 83.3 | 90.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 8.1 | 2.77 | 9.23 | 15.15 | 2.00 | 33.0 | 75.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.9 | 1.73 | 5.07 | 9.54 | 1.00 | 27.5 | 20.0 |
| Bench 4 | Bench | Mohamed Salah | MID | 12 | 13.1 | 0.00 | 23.29 | 38.92 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 10.9 | 6.64 | 19.52 | 31.71 | 18.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.51 | 14.26 | 24.02 | 9.00 | 87.0 | 75.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.3 | 4.14 | 11.08 | 17.80 | 2.00 | 73.8 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.6 | 2.50 | 8.52 | 14.20 | 1.00 | 58.9 | 59.0 |