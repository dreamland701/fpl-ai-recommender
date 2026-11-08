# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 238.59
- Total actual points: 267.00
- Average predicted points: 59.65
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
- Predicted score: 62.74
- Actual score: 64.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.52 | 10.08 | 16.32 | 6.00 | 89.7 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.36 | 1.05 | 1.48 | 0.00 | 12.4 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.66 | 12.74 | 20.31 | 1.00 | 90.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.3 | 4.30 | 12.15 | 19.85 | 0.00 | 88.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.1 | 3.88 | 11.40 | 18.17 | 6.00 | 88.5 | 90.0 |
| Bench 3 | Bench | Dara O'Shea | DEF | 10 | 4.0 | 2.48 | 6.79 | 11.00 | 2.00 | 82.5 | 90.0 |
| Bench 4 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 1.83 | 6.24 | 10.76 | 0.00 | 74.2 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 5.41 | 14.88 | 23.39 | 2.00 | 85.6 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.8 | 4.22 | 12.58 | 20.93 | 16.00 | 84.6 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 6.0 | 3.85 | 11.92 | 18.82 | 2.00 | 80.1 | 85.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 7.96 | 22.32 | 36.37 | 13.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.24 | 18.45 | 30.75 | 2.00 | 84.8 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 6.03 | 16.51 | 26.32 | 2.00 | 90.0 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 4.68 | 12.55 | 20.29 | 1.00 | 85.7 | 58.0 |
| Bench 2 | Bench | Harry Winks | MID | 11 | 4.5 | 3.20 | 9.18 | 14.57 | 1.00 | 79.3 | 10.0 |

## GW13

- Train rows: 141592
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 67.99
- Actual score: 80.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.18) beats the best remaining Triple Captain opportunity (8.98).
- Transfer: Gabriel dos Santos Magalhães -> Pedro Porro (projected gain 3.15, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.18) beats the best remaining Triple Captain opportunity (8.98).
- Autosub: Dara O'Shea replaced Joško Gvardiol.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.89 | 10.75 | 17.23 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.70 | 1.21 | 1.67 | 0.00 | 11.7 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 4.72 | 13.18 | 21.09 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Joško Gvardiol | DEF | 13 | 6.3 | 3.64 | 11.48 | 19.18 | 0.00 | 87.7 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.81 | 11.35 | 18.14 | 6.00 | 86.4 | 90.0 |
| Bench 2 | Autosub In | Dara O'Shea | DEF | 10 | 4.0 | 2.23 | 6.91 | 11.16 | 1.00 | 81.0 | 90.0 |
| Bench 4 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.49 | 2.50 | 5.05 | 0.00 | 28.2 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 6.04 | 17.57 | 27.20 | 2.00 | 90.0 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 4.05 | 12.97 | 20.78 | 1.00 | 62.5 | 21.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 6.0 | 3.83 | 10.47 | 16.96 | 2.00 | 73.7 | 78.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 8.18 | 24.34 | 38.57 | 13.00 | 90.0 | 83.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.60 | 18.70 | 30.20 | 14.00 | 90.0 | 85.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.84 | 13.15 | 21.26 | 9.00 | 73.1 | 65.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 3.02 | 9.34 | 15.57 | 2.00 | 61.5 | 85.0 |
| Bench 3 | Bench | Harry Winks | MID | 11 | 4.5 | 1.25 | 5.11 | 9.30 | 0.00 | 29.9 | 0.0 |

## GW14

- Train rows: 142282
- Bank: 0.60 -> 1.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 60.70
- Actual score: 64.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (3.98) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Alexander Isak -> Nicolas Jackson (projected gain 9.45, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (3.98) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.50 | 9.83 | 16.14 | 6.00 | 84.0 | 90.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.23 | 0.76 | 1.33 | 0.00 | 9.4 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.15 | 12.58 | 20.52 | 1.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 3.93 | 11.59 | 18.74 | 1.00 | 85.2 | 28.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 2.59 | 8.40 | 14.77 | 6.00 | 51.9 | 90.0 |
| Bench 2 | Bench Boost | Dara O'Shea | DEF | 10 | 4.0 | 2.34 | 6.77 | 11.15 | 1.00 | 77.5 | 90.0 |
| Bench 4 | Bench Boost | Jan Bednarek | DEF | 17 | 4.0 | 0.47 | 2.04 | 4.01 | 0.00 | 25.6 | 0.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 8.1 | 5.59 | 16.16 | 25.09 | 0.00 | 85.4 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.15 | 13.67 | 21.35 | 2.00 | 74.0 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.9 | 3.06 | 9.47 | 15.84 | 0.00 | 67.8 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 7.81 | 24.17 | 38.98 | 18.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 7.36 | 20.79 | 33.45 | 7.00 | 90.0 | 78.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.59 | 12.99 | 22.57 | 2.00 | 72.4 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.7 | 3.17 | 9.55 | 16.24 | 2.00 | 66.8 | 70.0 |
| Bench 3 | Bench Boost | Harry Winks | MID | 11 | 4.5 | 0.95 | 3.07 | 5.69 | 0.00 | 19.2 | 0.0 |

## GW15

- Train rows: 142975
- Bank: 1.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Matheus Santos Carneiro Da Cunha
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 47.17
- Actual score: 59.00
- Transfer: Harry Winks -> Morgan Rogers (projected gain 10.72, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.77 | 10.96 | 17.62 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.56 | 1.01 | 1.45 | 0.00 | 11.1 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.08 | 11.56 | 19.33 | 1.00 | 83.0 | 90.0 |
| Bench 2 | Bench | Virgil van Dijk | DEF | 12 | 6.3 | 0.00 | 9.86 | 16.57 | 0.00 | 0.0 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 3.10 | 9.46 | 16.05 | 3.00 | 71.9 | 90.0 |
| XI | XI | Dara O'Shea | DEF | 10 | 4.0 | 2.32 | 6.64 | 10.80 | 1.00 | 78.6 | 90.0 |
| Bench 3 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.00 | 0.71 | 2.00 | 0.00 | 9.1 | 0.0 |
| Vice Captain | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.73 | 13.43 | 21.58 | 1.00 | 84.3 | 90.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 8.1 | 2.84 | 9.24 | 15.02 | 2.00 | 35.1 | 75.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.9 | 1.64 | 5.38 | 10.32 | 1.00 | 24.9 | 20.0 |
| Bench 4 | Bench | Mohamed Salah | MID | 12 | 13.1 | 0.00 | 23.32 | 38.77 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 10.9 | 6.66 | 19.48 | 31.54 | 18.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.55 | 14.32 | 24.05 | 9.00 | 87.9 | 75.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.3 | 4.25 | 11.37 | 18.25 | 2.00 | 77.4 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.6 | 2.56 | 8.54 | 14.11 | 1.00 | 60.7 | 59.0 |