# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 238.18
- Total actual points: 267.00
- Average predicted points: 59.54
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
- Predicted score: 62.52
- Actual score: 64.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.46 | 9.99 | 16.25 | 6.00 | 88.1 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.23 | 0.85 | 1.28 | 0.00 | 8.4 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.63 | 12.69 | 20.29 | 1.00 | 90.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.3 | 4.24 | 12.07 | 19.80 | 0.00 | 86.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.1 | 3.83 | 11.32 | 18.10 | 6.00 | 87.2 | 90.0 |
| Bench 4 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 2.20 | 7.07 | 11.70 | 0.00 | 82.9 | 0.0 |
| Bench 3 | Bench | Dara O'Shea | DEF | 10 | 4.0 | 2.43 | 6.72 | 10.95 | 2.00 | 81.1 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 5.40 | 14.89 | 23.44 | 2.00 | 85.4 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.8 | 4.18 | 12.52 | 20.91 | 16.00 | 83.5 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 6.0 | 3.81 | 11.86 | 18.79 | 2.00 | 79.0 | 85.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 7.95 | 22.33 | 36.42 | 13.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.40 | 18.23 | 29.99 | 2.00 | 89.4 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 6.02 | 16.50 | 26.35 | 2.00 | 90.0 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 4.64 | 12.50 | 20.27 | 1.00 | 84.6 | 58.0 |
| Bench 2 | Bench | Harry Winks | MID | 11 | 4.5 | 3.17 | 9.13 | 14.55 | 1.00 | 78.5 | 10.0 |

## GW13

- Train rows: 141592
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 67.51
- Actual score: 80.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.17) beats the best remaining Triple Captain opportunity (8.93).
- Transfer: Gabriel dos Santos Magalhães -> Pedro Porro (projected gain 3.15, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.17) beats the best remaining Triple Captain opportunity (8.93).
- Autosub: Dara O'Shea replaced Joško Gvardiol.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.83 | 10.66 | 17.19 | 2.00 | 89.6 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.57 | 1.02 | 1.50 | 0.00 | 7.9 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 4.68 | 13.12 | 21.05 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Joško Gvardiol | DEF | 13 | 6.3 | 3.60 | 11.43 | 19.14 | 0.00 | 86.8 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.76 | 11.28 | 18.10 | 6.00 | 85.2 | 90.0 |
| Bench 2 | Autosub In | Dara O'Shea | DEF | 10 | 4.0 | 2.18 | 6.83 | 11.11 | 1.00 | 79.5 | 90.0 |
| Bench 4 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.81 | 3.23 | 5.93 | 0.00 | 35.6 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 6.03 | 17.57 | 27.22 | 2.00 | 90.0 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 4.01 | 12.93 | 20.76 | 1.00 | 61.5 | 21.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 6.0 | 3.77 | 10.39 | 16.91 | 2.00 | 72.2 | 78.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 8.17 | 24.35 | 38.63 | 13.00 | 90.0 | 83.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.57 | 18.65 | 30.20 | 14.00 | 90.0 | 85.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.79 | 13.10 | 21.26 | 9.00 | 71.9 | 65.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 2.93 | 9.23 | 15.50 | 2.00 | 59.2 | 85.0 |
| Bench 3 | Bench | Harry Winks | MID | 11 | 4.5 | 1.35 | 4.85 | 8.51 | 0.00 | 32.7 | 0.0 |

## GW14

- Train rows: 142282
- Bank: 0.60 -> 1.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 61.61
- Actual score: 64.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (4.01) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Alexander Isak -> Nicolas Jackson (projected gain 9.62, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (4.01) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.57 | 9.93 | 16.16 | 6.00 | 85.5 | 90.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.23 | 0.74 | 1.22 | 0.00 | 8.4 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.24 | 12.70 | 20.55 | 1.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 4.01 | 11.71 | 18.78 | 1.00 | 87.0 | 28.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 2.60 | 8.40 | 14.70 | 6.00 | 51.7 | 90.0 |
| Bench 2 | Bench Boost | Dara O'Shea | DEF | 10 | 4.0 | 2.40 | 6.86 | 11.15 | 1.00 | 78.7 | 90.0 |
| Bench 4 | Bench Boost | Jan Bednarek | DEF | 17 | 4.0 | 0.44 | 1.99 | 3.88 | 0.00 | 24.6 | 0.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 8.1 | 5.68 | 16.29 | 25.14 | 0.00 | 87.3 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.22 | 13.79 | 21.40 | 2.00 | 75.7 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.9 | 3.11 | 9.53 | 15.82 | 0.00 | 68.7 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 7.93 | 24.36 | 39.10 | 18.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 7.45 | 20.93 | 33.52 | 7.00 | 90.0 | 78.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.64 | 13.06 | 22.55 | 2.00 | 73.3 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.7 | 3.20 | 9.59 | 16.20 | 2.00 | 67.4 | 70.0 |
| Bench 3 | Bench Boost | Harry Winks | MID | 11 | 4.5 | 0.94 | 3.04 | 5.60 | 0.00 | 18.7 | 0.0 |

## GW15

- Train rows: 142975
- Bank: 1.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Matheus Santos Carneiro Da Cunha
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 46.54
- Actual score: 59.00
- Transfer: Harry Winks -> Morgan Rogers (projected gain 11.00, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.72 | 10.88 | 17.57 | 2.00 | 88.7 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.44 | 0.82 | 1.28 | 0.00 | 7.3 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.01 | 11.45 | 19.25 | 1.00 | 80.9 | 90.0 |
| Bench 2 | Bench | Virgil van Dijk | DEF | 12 | 6.3 | 0.00 | 9.81 | 16.64 | 0.00 | 0.0 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 2.99 | 9.31 | 15.94 | 3.00 | 68.8 | 90.0 |
| XI | XI | Dara O'Shea | DEF | 10 | 4.0 | 2.27 | 6.57 | 10.76 | 1.00 | 77.1 | 90.0 |
| Bench 3 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.00 | 0.83 | 2.16 | 0.00 | 13.3 | 0.0 |
| Vice Captain | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.67 | 13.36 | 21.55 | 1.00 | 82.8 | 90.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 8.1 | 2.73 | 9.11 | 14.95 | 2.00 | 32.2 | 75.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.9 | 1.72 | 5.03 | 9.49 | 1.00 | 27.0 | 20.0 |
| Bench 4 | Bench | Mohamed Salah | MID | 12 | 13.1 | 0.00 | 23.34 | 38.92 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 10.9 | 6.63 | 19.46 | 31.57 | 18.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.51 | 14.26 | 24.00 | 9.00 | 87.0 | 75.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.3 | 4.19 | 11.30 | 18.19 | 2.00 | 75.9 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.6 | 2.47 | 8.41 | 14.01 | 1.00 | 58.3 | 59.0 |