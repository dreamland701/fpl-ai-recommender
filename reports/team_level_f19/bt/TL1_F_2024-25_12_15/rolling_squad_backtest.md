# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 239.36
- Total actual points: 267.00
- Average predicted points: 59.84
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
- Predicted score: 63.07
- Actual score: 64.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.50 | 10.32 | 16.85 | 6.00 | 88.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.22 | 0.82 | 1.21 | 0.00 | 9.6 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.71 | 12.66 | 20.37 | 1.00 | 90.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.3 | 4.30 | 12.35 | 20.29 | 0.00 | 86.2 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.1 | 3.88 | 11.65 | 18.72 | 6.00 | 87.1 | 90.0 |
| Bench 4 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 2.16 | 6.94 | 11.41 | 0.00 | 83.3 | 0.0 |
| Bench 3 | Bench | Dara O'Shea | DEF | 10 | 4.0 | 2.33 | 6.40 | 10.42 | 2.00 | 81.9 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 5.43 | 15.05 | 23.71 | 2.00 | 85.7 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.8 | 4.24 | 12.82 | 21.32 | 16.00 | 83.7 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 6.0 | 3.78 | 11.80 | 18.68 | 2.00 | 79.8 | 85.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 8.02 | 22.32 | 36.49 | 13.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.47 | 18.25 | 30.02 | 2.00 | 89.7 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 6.12 | 16.66 | 26.58 | 2.00 | 90.0 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 4.61 | 12.38 | 20.12 | 1.00 | 85.6 | 58.0 |
| Bench 2 | Bench | Harry Winks | MID | 11 | 4.5 | 3.08 | 8.85 | 14.00 | 1.00 | 79.8 | 10.0 |

## GW13

- Train rows: 141592
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 67.98
- Actual score: 80.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.22) beats the best remaining Triple Captain opportunity (8.96).
- Transfer: Gabriel dos Santos Magalhães -> Pedro Porro (projected gain 2.81, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.22) beats the best remaining Triple Captain opportunity (8.96).
- Autosub: Dara O'Shea replaced Joško Gvardiol.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.87 | 10.85 | 17.57 | 2.00 | 89.6 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.65 | 0.98 | 1.47 | 0.00 | 8.8 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 4.62 | 12.98 | 20.81 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Joško Gvardiol | DEF | 13 | 6.3 | 3.71 | 11.80 | 19.79 | 0.00 | 85.9 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.82 | 11.25 | 18.13 | 6.00 | 85.1 | 90.0 |
| Bench 2 | Autosub In | Dara O'Shea | DEF | 10 | 4.0 | 2.03 | 6.52 | 10.56 | 1.00 | 80.4 | 90.0 |
| Bench 4 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.71 | 3.05 | 5.55 | 0.00 | 36.3 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 6.07 | 17.78 | 27.52 | 2.00 | 90.0 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 4.06 | 13.08 | 21.07 | 1.00 | 61.5 | 21.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 6.0 | 3.83 | 10.33 | 16.85 | 2.00 | 72.7 | 78.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 8.22 | 24.34 | 38.65 | 13.00 | 90.0 | 83.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.56 | 18.61 | 30.10 | 14.00 | 90.0 | 85.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.81 | 13.08 | 21.32 | 9.00 | 72.5 | 65.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 2.97 | 9.38 | 15.64 | 2.00 | 59.9 | 85.0 |
| Bench 3 | Bench | Harry Winks | MID | 11 | 4.5 | 1.22 | 4.50 | 7.88 | 0.00 | 34.0 | 0.0 |

## GW14

- Train rows: 142282
- Bank: 0.60 -> 1.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 61.56
- Actual score: 64.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (3.71) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Alexander Isak -> Nicolas Jackson (projected gain 9.80, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (3.71) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.62 | 10.12 | 16.52 | 6.00 | 85.4 | 90.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.22 | 0.70 | 1.13 | 0.00 | 9.6 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.24 | 12.61 | 20.50 | 1.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 3.95 | 11.57 | 18.56 | 1.00 | 87.7 | 28.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 2.64 | 8.72 | 15.27 | 6.00 | 51.1 | 90.0 |
| Bench 2 | Bench Boost | Dara O'Shea | DEF | 10 | 4.0 | 2.29 | 6.46 | 10.54 | 1.00 | 79.5 | 90.0 |
| Bench 4 | Bench Boost | Jan Bednarek | DEF | 17 | 4.0 | 0.38 | 1.83 | 3.54 | 0.00 | 25.5 | 0.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 8.1 | 5.74 | 16.22 | 25.07 | 0.00 | 87.7 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.28 | 13.96 | 21.70 | 2.00 | 76.1 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.9 | 3.09 | 9.47 | 15.69 | 0.00 | 69.6 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 7.94 | 24.27 | 39.06 | 18.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 7.50 | 20.86 | 33.42 | 7.00 | 90.0 | 78.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.71 | 13.07 | 22.56 | 2.00 | 73.5 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.7 | 3.22 | 9.69 | 16.30 | 2.00 | 68.3 | 70.0 |
| Bench 3 | Bench Boost | Harry Winks | MID | 11 | 4.5 | 0.83 | 2.68 | 4.99 | 0.00 | 19.9 | 0.0 |

## GW15

- Train rows: 142975
- Bank: 1.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Matheus Santos Carneiro Da Cunha
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 46.74
- Actual score: 59.00
- Transfer: Harry Winks -> Morgan Rogers (projected gain 11.47, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.75 | 11.03 | 17.85 | 2.00 | 88.7 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.52 | 0.92 | 1.37 | 0.00 | 8.0 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.07 | 11.63 | 19.65 | 1.00 | 80.1 | 90.0 |
| Bench 2 | Bench | Virgil van Dijk | DEF | 12 | 6.3 | 0.00 | 9.77 | 16.61 | 0.00 | 0.0 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 2.97 | 9.28 | 15.84 | 3.00 | 69.1 | 90.0 |
| XI | XI | Dara O'Shea | DEF | 10 | 4.0 | 2.15 | 6.27 | 10.22 | 1.00 | 78.1 | 90.0 |
| Bench 3 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.00 | 0.64 | 1.85 | 0.00 | 14.2 | 0.0 |
| Vice Captain | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.73 | 13.60 | 21.93 | 1.00 | 83.2 | 90.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 8.1 | 2.72 | 9.06 | 14.83 | 2.00 | 32.9 | 75.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.9 | 1.78 | 5.10 | 9.53 | 1.00 | 27.4 | 20.0 |
| Bench 4 | Bench | Mohamed Salah | MID | 12 | 13.1 | 0.00 | 23.30 | 38.87 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 10.9 | 6.61 | 19.38 | 31.42 | 18.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.48 | 14.30 | 24.03 | 9.00 | 87.5 | 75.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.3 | 4.31 | 11.47 | 18.49 | 2.00 | 75.8 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.6 | 2.55 | 8.47 | 14.10 | 1.00 | 58.8 | 59.0 |