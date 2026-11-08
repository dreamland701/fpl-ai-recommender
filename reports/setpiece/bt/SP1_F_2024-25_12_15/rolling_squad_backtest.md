# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 239.22
- Total actual points: 267.00
- Average predicted points: 59.81
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
- Predicted score: 62.73
- Actual score: 64.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.44 | 9.90 | 16.09 | 6.00 | 88.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.23 | 0.86 | 1.30 | 0.00 | 8.4 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.60 | 12.55 | 20.03 | 1.00 | 90.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.3 | 4.17 | 11.71 | 19.13 | 0.00 | 86.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.1 | 3.80 | 11.16 | 17.81 | 6.00 | 86.9 | 90.0 |
| Bench 4 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 2.20 | 7.02 | 11.61 | 0.00 | 82.8 | 0.0 |
| Bench 3 | Bench | Dara O'Shea | DEF | 10 | 4.0 | 2.43 | 6.67 | 10.86 | 2.00 | 81.2 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 5.45 | 15.10 | 23.88 | 2.00 | 85.6 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 6.0 | 4.01 | 12.74 | 20.52 | 2.00 | 81.0 | 85.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.8 | 4.19 | 12.54 | 20.96 | 16.00 | 83.1 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 7.93 | 22.25 | 36.34 | 13.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.52 | 18.82 | 31.05 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 6.12 | 16.93 | 27.11 | 2.00 | 90.0 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 4.58 | 12.19 | 19.71 | 1.00 | 84.0 | 58.0 |
| Bench 2 | Bench | Harry Winks | MID | 11 | 4.5 | 3.13 | 8.94 | 14.18 | 1.00 | 77.9 | 10.0 |

## GW13

- Train rows: 141592
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 67.72
- Actual score: 80.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.14) beats the best remaining Triple Captain opportunity (9.11).
- Transfer: Gabriel dos Santos Magalhães -> Pedro Porro (projected gain 3.65, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.14) beats the best remaining Triple Captain opportunity (9.11).
- Autosub: Dara O'Shea replaced Joško Gvardiol.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.82 | 10.61 | 17.08 | 2.00 | 89.5 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.58 | 1.04 | 1.52 | 0.00 | 7.9 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 4.77 | 13.48 | 21.79 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.73 | 11.10 | 17.78 | 6.00 | 85.0 | 90.0 |
| XI | Bench | Joško Gvardiol | DEF | 13 | 6.3 | 3.48 | 10.86 | 18.09 | 0.00 | 85.6 | 0.0 |
| Bench 2 | Autosub In | Dara O'Shea | DEF | 10 | 4.0 | 2.18 | 6.82 | 11.09 | 1.00 | 79.5 | 90.0 |
| Bench 4 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.80 | 3.19 | 5.84 | 0.00 | 35.5 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 6.04 | 17.60 | 27.29 | 2.00 | 90.0 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 4.05 | 13.07 | 21.08 | 1.00 | 61.6 | 21.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 6.0 | 3.98 | 11.29 | 18.67 | 2.00 | 74.1 | 78.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 8.14 | 24.21 | 38.44 | 13.00 | 90.0 | 83.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.70 | 19.31 | 31.37 | 14.00 | 90.0 | 85.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.86 | 13.38 | 21.76 | 9.00 | 72.1 | 65.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 2.87 | 8.93 | 14.95 | 2.00 | 58.6 | 85.0 |
| Bench 3 | Bench | Harry Winks | MID | 11 | 4.5 | 1.31 | 4.67 | 8.17 | 0.00 | 32.2 | 0.0 |

## GW14

- Train rows: 142282
- Bank: 0.60 -> 1.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 61.80
- Actual score: 64.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (3.99) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Alexander Isak -> Nicolas Jackson (projected gain 9.60, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (3.99) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.57 | 9.90 | 16.11 | 6.00 | 85.4 | 90.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.23 | 0.75 | 1.24 | 0.00 | 8.4 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.20 | 12.55 | 20.28 | 1.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 4.12 | 12.13 | 19.61 | 1.00 | 88.3 | 28.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 2.50 | 7.89 | 13.77 | 6.00 | 50.7 | 90.0 |
| Bench 2 | Bench Boost | Dara O'Shea | DEF | 10 | 4.0 | 2.40 | 6.87 | 11.16 | 1.00 | 78.7 | 90.0 |
| Bench 4 | Bench Boost | Jan Bednarek | DEF | 17 | 4.0 | 0.45 | 2.00 | 3.90 | 0.00 | 24.6 | 0.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 8.1 | 5.70 | 16.40 | 25.38 | 0.00 | 87.3 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.21 | 13.73 | 21.30 | 2.00 | 75.2 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.9 | 3.31 | 10.43 | 17.54 | 0.00 | 70.6 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 7.88 | 24.14 | 38.77 | 18.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 7.58 | 21.58 | 34.67 | 7.00 | 90.0 | 78.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.72 | 13.36 | 23.07 | 2.00 | 73.5 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.7 | 3.14 | 9.26 | 15.60 | 2.00 | 66.7 | 70.0 |
| Bench 3 | Bench Boost | Harry Winks | MID | 11 | 4.5 | 0.92 | 2.93 | 5.38 | 0.00 | 18.4 | 0.0 |

## GW15

- Train rows: 142975
- Bank: 1.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Matheus Santos Carneiro Da Cunha
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 46.98
- Actual score: 59.00
- Transfer: Harry Winks -> Morgan Rogers (projected gain 10.69, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.71 | 10.86 | 17.54 | 2.00 | 88.7 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.44 | 0.83 | 1.29 | 0.00 | 7.3 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 3.91 | 10.99 | 18.42 | 1.00 | 80.2 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 3.10 | 9.73 | 16.77 | 3.00 | 69.9 | 90.0 |
| Bench 2 | Bench | Virgil van Dijk | DEF | 12 | 6.3 | 0.00 | 9.68 | 16.40 | 0.00 | 0.0 | 0.0 |
| XI | XI | Dara O'Shea | DEF | 10 | 4.0 | 2.27 | 6.59 | 10.79 | 1.00 | 77.2 | 90.0 |
| Bench 3 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.00 | 0.83 | 2.17 | 0.00 | 13.3 | 0.0 |
| Vice Captain | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.69 | 13.42 | 21.68 | 1.00 | 82.5 | 90.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 8.1 | 2.76 | 9.26 | 15.24 | 2.00 | 32.3 | 75.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.9 | 1.93 | 5.96 | 11.27 | 1.00 | 28.8 | 20.0 |
| Bench 4 | Bench | Mohamed Salah | MID | 12 | 13.1 | 0.00 | 23.07 | 38.49 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 10.9 | 6.74 | 20.00 | 32.52 | 18.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.59 | 14.58 | 24.58 | 9.00 | 87.1 | 75.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.3 | 4.12 | 10.96 | 17.58 | 2.00 | 75.4 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.6 | 2.41 | 8.13 | 13.50 | 1.00 | 57.7 | 59.0 |