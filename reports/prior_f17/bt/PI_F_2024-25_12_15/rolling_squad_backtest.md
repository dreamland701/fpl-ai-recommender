# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 238.23
- Total actual points: 267.00
- Average predicted points: 59.56
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
- Predicted score: 62.51
- Actual score: 64.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.44 | 9.93 | 16.13 | 6.00 | 87.9 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.21 | 0.79 | 1.16 | 0.00 | 8.2 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.67 | 12.77 | 20.39 | 1.00 | 90.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.3 | 4.20 | 11.96 | 19.63 | 0.00 | 86.4 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.1 | 3.85 | 11.35 | 18.13 | 6.00 | 86.9 | 90.0 |
| Bench 4 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 2.21 | 7.07 | 11.69 | 0.00 | 83.0 | 0.0 |
| Bench 3 | Bench | Dara O'Shea | DEF | 10 | 4.0 | 2.41 | 6.64 | 10.80 | 2.00 | 80.9 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 5.34 | 14.70 | 23.14 | 2.00 | 85.5 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.8 | 4.18 | 12.55 | 20.96 | 16.00 | 83.3 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 6.0 | 3.78 | 11.79 | 18.69 | 2.00 | 78.9 | 85.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 7.94 | 22.28 | 36.34 | 13.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.45 | 18.37 | 30.22 | 2.00 | 89.5 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 6.07 | 16.66 | 26.59 | 2.00 | 90.0 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 4.65 | 12.53 | 20.31 | 1.00 | 84.2 | 58.0 |
| Bench 2 | Bench | Harry Winks | MID | 11 | 4.5 | 3.15 | 9.13 | 14.61 | 1.00 | 79.4 | 10.0 |

## GW13

- Train rows: 141592
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 67.47
- Actual score: 80.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.14) beats the best remaining Triple Captain opportunity (9.01).
- Transfer: Gabriel dos Santos Magalhães -> Pedro Porro (projected gain 3.04, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.14) beats the best remaining Triple Captain opportunity (9.01).
- Autosub: Dara O'Shea replaced Joško Gvardiol.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.83 | 10.62 | 17.09 | 2.00 | 89.4 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.56 | 0.97 | 1.40 | 0.00 | 7.7 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 4.67 | 13.08 | 20.96 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.80 | 11.36 | 18.20 | 6.00 | 85.0 | 90.0 |
| XI | Bench | Joško Gvardiol | DEF | 13 | 6.3 | 3.56 | 11.31 | 18.97 | 0.00 | 86.5 | 0.0 |
| Bench 2 | Autosub In | Dara O'Shea | DEF | 10 | 4.0 | 2.16 | 6.76 | 10.97 | 1.00 | 79.2 | 90.0 |
| Bench 4 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.81 | 3.26 | 5.97 | 0.00 | 35.8 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 6.03 | 17.59 | 27.26 | 2.00 | 90.0 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 3.96 | 12.80 | 20.56 | 1.00 | 61.6 | 21.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 6.0 | 3.75 | 10.34 | 16.84 | 2.00 | 72.0 | 78.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 8.14 | 24.27 | 38.50 | 13.00 | 90.0 | 83.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.63 | 18.83 | 30.49 | 14.00 | 90.0 | 85.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.86 | 13.29 | 21.57 | 9.00 | 72.1 | 65.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 2.94 | 9.26 | 15.55 | 2.00 | 58.8 | 85.0 |
| Bench 3 | Bench | Harry Winks | MID | 11 | 4.5 | 1.33 | 4.85 | 8.59 | 0.00 | 33.6 | 0.0 |

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
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (3.97) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Alexander Isak -> Nicolas Jackson (projected gain 9.67, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (3.97) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.57 | 9.88 | 16.06 | 6.00 | 85.2 | 90.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.21 | 0.69 | 1.11 | 0.00 | 8.2 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.27 | 12.76 | 20.62 | 1.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 4.02 | 11.70 | 18.74 | 1.00 | 86.8 | 28.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 2.56 | 8.30 | 14.54 | 6.00 | 51.4 | 90.0 |
| Bench 2 | Bench Boost | Dara O'Shea | DEF | 10 | 4.0 | 2.38 | 6.79 | 11.02 | 1.00 | 78.4 | 90.0 |
| Bench 4 | Bench Boost | Jan Bednarek | DEF | 17 | 4.0 | 0.45 | 2.01 | 3.92 | 0.00 | 24.8 | 0.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 8.1 | 5.72 | 16.38 | 25.30 | 0.00 | 87.4 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.24 | 13.84 | 21.49 | 2.00 | 75.5 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.9 | 3.10 | 9.49 | 15.75 | 0.00 | 68.4 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 7.90 | 24.26 | 38.94 | 18.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 7.51 | 21.10 | 33.79 | 7.00 | 90.0 | 78.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.69 | 13.19 | 22.77 | 2.00 | 73.5 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.7 | 3.21 | 9.59 | 16.20 | 2.00 | 67.0 | 70.0 |
| Bench 3 | Bench Boost | Harry Winks | MID | 11 | 4.5 | 0.92 | 3.06 | 5.69 | 0.00 | 19.7 | 0.0 |

## GW15

- Train rows: 142975
- Bank: 1.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Matheus Santos Carneiro Da Cunha
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 46.63
- Actual score: 59.00
- Transfer: Harry Winks -> Morgan Rogers (projected gain 10.89, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.72 | 10.86 | 17.51 | 2.00 | 88.5 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.43 | 0.77 | 1.18 | 0.00 | 7.0 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 3.98 | 11.36 | 19.11 | 1.00 | 80.6 | 90.0 |
| Bench 2 | Bench | Virgil van Dijk | DEF | 12 | 6.3 | 0.00 | 9.88 | 16.72 | 0.00 | 0.0 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 2.98 | 9.26 | 15.83 | 3.00 | 68.6 | 90.0 |
| XI | XI | Dara O'Shea | DEF | 10 | 4.0 | 2.25 | 6.50 | 10.62 | 1.00 | 76.9 | 90.0 |
| Bench 3 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.00 | 0.85 | 2.21 | 0.00 | 13.5 | 0.0 |
| Vice Captain | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.67 | 13.35 | 21.53 | 1.00 | 82.5 | 90.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 8.1 | 2.77 | 9.21 | 15.11 | 2.00 | 32.3 | 75.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.9 | 1.71 | 5.02 | 9.46 | 1.00 | 26.7 | 20.0 |
| Bench 4 | Bench | Mohamed Salah | MID | 12 | 13.1 | 0.00 | 23.21 | 38.70 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 10.9 | 6.67 | 19.59 | 31.80 | 18.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.56 | 14.40 | 24.24 | 9.00 | 87.0 | 75.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.3 | 4.17 | 11.22 | 18.07 | 2.00 | 75.9 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.6 | 2.47 | 8.41 | 14.00 | 1.00 | 57.9 | 59.0 |