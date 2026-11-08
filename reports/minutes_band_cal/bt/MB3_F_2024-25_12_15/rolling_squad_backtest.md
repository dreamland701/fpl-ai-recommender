# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 238.99
- Total actual points: 267.00
- Average predicted points: 59.75
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
- Predicted score: 62.53
- Actual score: 64.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.46 | 9.99 | 16.25 | 6.00 | 88.1 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.18 | 0.77 | 1.20 | 0.00 | 7.6 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.63 | 12.69 | 20.29 | 1.00 | 90.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.3 | 4.24 | 12.07 | 19.80 | 0.00 | 86.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.1 | 3.83 | 11.32 | 18.10 | 6.00 | 87.2 | 90.0 |
| Bench 4 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 2.20 | 7.07 | 11.70 | 0.00 | 82.9 | 0.0 |
| Bench 3 | Bench | Dara O'Shea | DEF | 10 | 4.0 | 2.43 | 6.72 | 10.95 | 2.00 | 81.1 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 5.40 | 14.89 | 23.44 | 2.00 | 85.4 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.8 | 4.18 | 12.52 | 20.91 | 16.00 | 83.5 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 6.0 | 3.82 | 11.83 | 18.55 | 2.00 | 80.9 | 85.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 7.95 | 22.33 | 36.42 | 13.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.40 | 18.23 | 29.99 | 2.00 | 89.4 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 6.02 | 16.50 | 26.35 | 2.00 | 90.0 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 4.64 | 12.50 | 20.27 | 1.00 | 84.6 | 58.0 |
| Bench 2 | Bench | Harry Winks | MID | 11 | 4.5 | 3.18 | 9.10 | 14.30 | 1.00 | 80.4 | 10.0 |

## GW13

- Train rows: 141592
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 67.88
- Actual score: 80.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.17) beats the best remaining Triple Captain opportunity (8.93).
- Transfer: Gabriel dos Santos Magalhães -> Pedro Porro (projected gain 3.21, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.17) beats the best remaining Triple Captain opportunity (8.93).
- Autosub: Dara O'Shea replaced Joško Gvardiol.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.83 | 10.66 | 17.19 | 2.00 | 89.6 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.53 | 0.94 | 1.42 | 0.00 | 7.1 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 4.68 | 13.12 | 21.05 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Joško Gvardiol | DEF | 13 | 6.3 | 3.60 | 11.43 | 19.14 | 0.00 | 86.8 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.76 | 11.28 | 18.10 | 6.00 | 85.2 | 90.0 |
| Bench 2 | Autosub In | Dara O'Shea | DEF | 10 | 4.0 | 2.18 | 6.77 | 10.85 | 1.00 | 81.3 | 90.0 |
| Bench 4 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.76 | 3.15 | 5.85 | 0.00 | 34.8 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 6.03 | 17.57 | 27.22 | 2.00 | 90.0 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 4.11 | 13.15 | 21.18 | 1.00 | 65.6 | 21.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 6.0 | 3.77 | 10.33 | 16.65 | 2.00 | 74.0 | 78.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 8.17 | 24.35 | 38.63 | 13.00 | 90.0 | 83.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.57 | 18.65 | 30.20 | 14.00 | 90.0 | 85.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.89 | 13.33 | 21.68 | 9.00 | 76.0 | 65.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 3.12 | 9.72 | 16.30 | 2.00 | 63.9 | 85.0 |
| Bench 3 | Bench | Harry Winks | MID | 11 | 4.5 | 1.30 | 4.77 | 8.44 | 0.00 | 31.9 | 0.0 |

## GW14

- Train rows: 142282
- Bank: 0.60 -> 1.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 61.85
- Actual score: 64.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (3.87) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Alexander Isak -> Nicolas Jackson (projected gain 9.53, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (3.87) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.57 | 9.93 | 16.16 | 6.00 | 85.5 | 90.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.18 | 0.66 | 1.14 | 0.00 | 7.6 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.24 | 12.70 | 20.55 | 1.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 4.01 | 11.71 | 18.78 | 1.00 | 87.0 | 28.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 2.79 | 8.89 | 15.48 | 6.00 | 56.4 | 90.0 |
| Bench 2 | Bench Boost | Dara O'Shea | DEF | 10 | 4.0 | 2.41 | 6.83 | 10.92 | 1.00 | 80.5 | 90.0 |
| Bench 4 | Bench Boost | Jan Bednarek | DEF | 17 | 4.0 | 0.40 | 1.90 | 3.81 | 0.00 | 23.8 | 0.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 8.1 | 5.68 | 16.29 | 25.14 | 0.00 | 87.3 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.23 | 13.76 | 21.16 | 2.00 | 77.5 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.9 | 3.20 | 9.75 | 16.25 | 0.00 | 72.8 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 7.93 | 24.36 | 39.10 | 18.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 7.45 | 20.93 | 33.52 | 7.00 | 90.0 | 78.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.65 | 13.03 | 22.31 | 2.00 | 75.2 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.7 | 3.30 | 9.81 | 16.63 | 2.00 | 71.4 | 70.0 |
| Bench 3 | Bench Boost | Harry Winks | MID | 11 | 4.5 | 0.89 | 2.96 | 5.53 | 0.00 | 17.9 | 0.0 |

## GW15

- Train rows: 142975
- Bank: 1.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Matheus Santos Carneiro Da Cunha
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 46.73
- Actual score: 59.00
- Transfer: Harry Winks -> Morgan Rogers (projected gain 11.07, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.72 | 10.88 | 17.57 | 2.00 | 88.7 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.39 | 0.74 | 1.21 | 0.00 | 6.4 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.01 | 11.45 | 19.25 | 1.00 | 80.9 | 90.0 |
| Bench 2 | Bench | Virgil van Dijk | DEF | 12 | 6.3 | 0.00 | 9.81 | 16.64 | 0.00 | 0.0 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 3.09 | 9.53 | 16.35 | 3.00 | 72.8 | 90.0 |
| XI | XI | Dara O'Shea | DEF | 10 | 4.0 | 2.27 | 6.54 | 10.53 | 1.00 | 78.9 | 90.0 |
| Bench 3 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.00 | 0.75 | 2.09 | 0.00 | 12.5 | 0.0 |
| Vice Captain | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.67 | 13.36 | 21.55 | 1.00 | 82.8 | 90.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 8.1 | 2.69 | 9.03 | 14.88 | 2.00 | 31.3 | 75.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.9 | 1.67 | 4.95 | 9.42 | 1.00 | 26.2 | 20.0 |
| Bench 4 | Bench | Mohamed Salah | MID | 12 | 13.1 | 0.00 | 23.34 | 38.92 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 10.9 | 6.63 | 19.46 | 31.57 | 18.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.51 | 14.26 | 24.00 | 9.00 | 87.0 | 75.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.3 | 4.20 | 11.27 | 17.97 | 2.00 | 77.7 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.6 | 2.65 | 8.90 | 14.79 | 1.00 | 62.9 | 59.0 |