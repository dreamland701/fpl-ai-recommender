# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 248.01
- Total actual points: 267.00
- Average predicted points: 62.00
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
- Predicted score: 64.13
- Actual score: 64.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.42 | 9.99 | 16.25 | 6.00 | 89.3 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.26 | 0.85 | 1.28 | 0.00 | 8.8 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.78 | 12.69 | 20.29 | 1.00 | 101.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.3 | 4.21 | 12.07 | 19.80 | 0.00 | 86.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.1 | 3.90 | 11.32 | 18.10 | 6.00 | 90.2 | 90.0 |
| Bench 4 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 2.25 | 7.07 | 11.70 | 0.00 | 83.9 | 0.0 |
| Bench 3 | Bench | Dara O'Shea | DEF | 10 | 4.0 | 2.44 | 6.72 | 10.95 | 2.00 | 81.4 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 5.72 | 14.89 | 23.44 | 2.00 | 91.3 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.8 | 4.32 | 12.52 | 20.91 | 16.00 | 85.6 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 6.0 | 3.89 | 11.86 | 18.79 | 2.00 | 80.0 | 85.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 8.16 | 22.33 | 36.42 | 13.00 | 115.3 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.43 | 18.23 | 29.99 | 2.00 | 92.5 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 6.34 | 16.50 | 26.35 | 2.00 | 105.8 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 4.79 | 12.50 | 20.27 | 1.00 | 88.1 | 58.0 |
| Bench 2 | Bench | Harry Winks | MID | 11 | 4.5 | 3.20 | 9.13 | 14.55 | 1.00 | 79.7 | 10.0 |

## GW13

- Train rows: 141592
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 68.02
- Actual score: 80.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.21) beats the best remaining Triple Captain opportunity (8.98).
- Transfer: Gabriel dos Santos Magalhães -> Pedro Porro (projected gain 3.15, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.21) beats the best remaining Triple Captain opportunity (8.98).
- Autosub: Dara O'Shea replaced Joško Gvardiol.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.86 | 10.66 | 17.19 | 2.00 | 91.6 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.60 | 1.02 | 1.50 | 0.00 | 8.1 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 4.82 | 13.12 | 21.05 | 2.00 | 101.7 | 90.0 |
| XI | Bench | Joško Gvardiol | DEF | 13 | 6.3 | 3.42 | 11.43 | 19.14 | 0.00 | 83.8 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.75 | 11.28 | 18.10 | 6.00 | 85.4 | 90.0 |
| Bench 2 | Autosub In | Dara O'Shea | DEF | 10 | 4.0 | 2.22 | 6.83 | 11.11 | 1.00 | 80.6 | 90.0 |
| Bench 4 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.90 | 3.23 | 5.93 | 0.00 | 37.3 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 6.41 | 17.57 | 27.22 | 2.00 | 114.2 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 4.03 | 12.93 | 20.76 | 1.00 | 61.1 | 21.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 6.0 | 3.73 | 10.39 | 16.91 | 2.00 | 70.9 | 78.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 8.21 | 24.35 | 38.63 | 13.00 | 108.3 | 83.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.60 | 18.65 | 30.20 | 14.00 | 97.1 | 85.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.92 | 13.10 | 21.26 | 9.00 | 73.9 | 65.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 2.84 | 9.23 | 15.50 | 2.00 | 58.2 | 85.0 |
| Bench 3 | Bench | Harry Winks | MID | 11 | 4.5 | 1.42 | 4.85 | 8.51 | 0.00 | 34.1 | 0.0 |

## GW14

- Train rows: 142282
- Bank: 0.60 -> 1.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 62.33
- Actual score: 64.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (4.10) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Alexander Isak -> Nicolas Jackson (projected gain 9.52, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (4.10) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.56 | 9.93 | 16.16 | 6.00 | 86.4 | 90.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.24 | 0.74 | 1.22 | 0.00 | 8.6 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.30 | 12.70 | 20.55 | 1.00 | 97.6 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 4.04 | 11.71 | 18.78 | 1.00 | 87.5 | 28.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 2.46 | 8.40 | 14.70 | 6.00 | 49.3 | 90.0 |
| Bench 2 | Bench Boost | Dara O'Shea | DEF | 10 | 4.0 | 2.45 | 6.86 | 11.15 | 1.00 | 80.1 | 90.0 |
| Bench 4 | Bench Boost | Jan Bednarek | DEF | 17 | 4.0 | 0.45 | 1.99 | 3.88 | 0.00 | 24.7 | 0.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 8.1 | 6.06 | 16.29 | 25.14 | 0.00 | 95.1 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.39 | 13.79 | 21.40 | 2.00 | 77.9 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.9 | 3.03 | 9.53 | 15.82 | 0.00 | 67.3 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 8.08 | 24.36 | 39.10 | 18.00 | 115.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 7.57 | 20.93 | 33.52 | 7.00 | 110.4 | 78.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.57 | 13.06 | 22.55 | 2.00 | 72.0 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.7 | 3.09 | 9.59 | 16.20 | 2.00 | 65.8 | 70.0 |
| Bench 3 | Bench Boost | Harry Winks | MID | 11 | 4.5 | 0.95 | 3.04 | 5.60 | 0.00 | 19.3 | 0.0 |

## GW15

- Train rows: 142975
- Bank: 1.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 53.54
- Actual score: 59.00
- Transfer: Harry Winks -> Morgan Rogers (projected gain 4.90, hit 0)
- Autosub: Dara O'Shea replaced Virgil van Dijk.
- Autosub: Danny Welbeck replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.75 | 10.88 | 17.57 | 2.00 | 90.4 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.46 | 0.82 | 1.28 | 0.00 | 7.4 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.03 | 11.45 | 19.25 | 1.00 | 81.7 | 90.0 |
| XI | Bench | Virgil van Dijk | DEF | 12 | 6.3 | 2.84 | 9.81 | 16.64 | 0.00 | 65.6 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 2.93 | 9.31 | 15.94 | 3.00 | 67.7 | 90.0 |
| Bench 2 | Autosub In | Dara O'Shea | DEF | 10 | 4.0 | 2.30 | 6.57 | 10.76 | 1.00 | 78.0 | 90.0 |
| Bench 4 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.00 | 0.83 | 2.16 | 0.00 | 12.3 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.64 | 13.36 | 21.55 | 1.00 | 81.4 | 90.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 8.1 | 2.76 | 9.11 | 14.95 | 2.00 | 33.6 | 75.0 |
| Bench 3 | Autosub In | Danny Welbeck | FWD | 5 | 5.9 | 1.60 | 5.03 | 9.49 | 1.00 | 25.3 | 20.0 |
| Captain | Bench | Mohamed Salah | MID | 12 | 13.1 | 7.39 | 23.34 | 38.92 | 0.00 | 91.6 | 0.0 |
| Vice Captain | Captain | Cole Palmer | MID | 6 | 10.9 | 6.83 | 19.46 | 31.57 | 18.00 | 96.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.43 | 14.26 | 24.00 | 9.00 | 85.2 | 75.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.3 | 4.24 | 11.30 | 18.19 | 2.00 | 76.9 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.6 | 2.33 | 8.41 | 14.01 | 1.00 | 56.9 | 59.0 |