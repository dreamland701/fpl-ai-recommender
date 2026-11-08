# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 241.10
- Total actual points: 302.00
- Average predicted points: 60.27
- Average actual points: 75.50
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
- Predicted score: 63.75
- Actual score: 68.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 4.9 | 3.39 | 9.50 | 15.62 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.20 | 0.80 | 1.22 | 0.00 | 8.2 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.73 | 12.87 | 20.62 | 1.00 | 90.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.3 | 4.29 | 12.08 | 19.81 | 0.00 | 88.3 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.93 | 10.68 | 17.42 | 0.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.32 | 7.46 | 12.05 | 1.00 | 78.2 | 90.0 |
| Bench 3 | Bench | Dara O'Shea | DEF | 10 | 4.0 | 2.61 | 7.24 | 11.88 | 2.00 | 86.8 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 5.50 | 15.11 | 23.84 | 2.00 | 88.5 | 90.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 7.9 | 4.70 | 12.95 | 21.21 | 12.00 | 83.8 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.8 | 4.29 | 12.78 | 21.35 | 16.00 | 87.0 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 7.94 | 22.10 | 36.01 | 13.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.40 | 18.08 | 29.75 | 2.00 | 89.9 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 6.12 | 16.73 | 26.75 | 2.00 | 90.0 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 4.52 | 11.95 | 19.25 | 1.00 | 80.4 | 58.0 |
| Bench 2 | Bench | Harry Winks | MID | 11 | 4.5 | 3.03 | 8.66 | 13.72 | 1.00 | 75.0 | 10.0 |

## GW13

- Train rows: 141592
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 67.64
- Actual score: 85.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.14) beats the best remaining Triple Captain opportunity (8.94).
- Transfer: Emile Smith Rowe -> Alex Iwobi (projected gain 2.13, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.14) beats the best remaining Triple Captain opportunity (8.94).
- Autosub: Taylor Harwood-Bellis replaced Joško Gvardiol.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 4.9 | 3.03 | 9.15 | 15.23 | 0.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.55 | 1.00 | 1.49 | 0.00 | 8.1 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.87 | 11.47 | 18.42 | 6.00 | 89.0 | 90.0 |
| XI | Bench | Joško Gvardiol | DEF | 13 | 6.3 | 3.64 | 11.42 | 19.09 | 0.00 | 88.0 | 0.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.21 | 9.60 | 15.73 | 2.00 | 85.1 | 90.0 |
| Bench 2 | Autosub In | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.44 | 7.56 | 12.22 | 1.00 | 80.1 | 90.0 |
| Bench 3 | Bench | Dara O'Shea | DEF | 10 | 4.0 | 2.35 | 7.35 | 12.02 | 1.00 | 84.8 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 6.11 | 17.69 | 27.41 | 2.00 | 90.0 | 90.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 7.9 | 5.11 | 14.54 | 23.32 | 6.00 | 88.9 | 70.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 4.12 | 13.22 | 21.27 | 1.00 | 64.8 | 21.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 8.14 | 24.08 | 38.12 | 13.00 | 90.0 | 83.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.57 | 18.52 | 29.94 | 14.00 | 90.0 | 85.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.94 | 13.45 | 21.86 | 9.00 | 76.5 | 65.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.6 | 3.62 | 10.83 | 17.55 | 5.00 | 85.8 | 85.0 |
| Bench 4 | Bench | Harry Winks | MID | 11 | 4.5 | 1.20 | 4.40 | 7.74 | 0.00 | 29.1 | 0.0 |

## GW14

- Train rows: 142282
- Bank: 0.20 -> 2.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 63.46
- Actual score: 84.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.30) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Alexander Isak -> Chris Wood (projected gain 3.78, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.30) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 4.9 | 3.14 | 8.97 | 14.91 | 6.00 | 89.9 | 90.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.21 | 0.73 | 1.24 | 0.00 | 8.6 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.34 | 12.92 | 20.89 | 1.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.44 | 9.77 | 15.92 | 6.00 | 87.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 2.64 | 8.41 | 14.66 | 6.00 | 53.0 | 90.0 |
| Bench 2 | Bench Boost | Dara O'Shea | DEF | 10 | 4.0 | 2.56 | 7.38 | 12.04 | 1.00 | 83.9 | 90.0 |
| Bench 3 | Bench Boost | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 1.71 | 5.48 | 9.16 | 0.00 | 65.4 | 0.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 8.0 | 5.82 | 16.70 | 25.85 | 0.00 | 90.0 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.34 | 14.07 | 21.84 | 2.00 | 79.3 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.6 | 3.71 | 11.08 | 18.19 | 2.00 | 73.7 | 61.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 7.87 | 23.99 | 38.41 | 18.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 7.45 | 20.80 | 33.24 | 7.00 | 90.0 | 78.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.71 | 13.15 | 22.66 | 2.00 | 75.7 | 90.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.6 | 3.84 | 11.00 | 17.92 | 15.00 | 83.1 | 90.0 |
| Bench 4 | Bench Boost | Harry Winks | MID | 11 | 4.5 | 0.82 | 2.66 | 4.95 | 0.00 | 15.6 | 0.0 |

## GW15

- Train rows: 142975
- Bank: 2.10 -> 1.50
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Matheus Santos Carneiro Da Cunha
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 46.25
- Actual score: 65.00
- Transfer: Jordan Pickford -> David Raya Martin (projected gain 11.24, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.79 | 11.00 | 17.73 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.42 | 0.81 | 1.29 | 0.00 | 7.5 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.04 | 11.42 | 19.14 | 1.00 | 82.0 | 90.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 12 | 6.3 | 0.00 | 10.00 | 16.97 | 0.00 | 0.0 | 0.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.00 | 9.55 | 15.68 | 1.00 | 87.2 | 90.0 |
| XI | XI | Dara O'Shea | DEF | 10 | 4.0 | 2.43 | 7.07 | 11.62 | 1.00 | 82.1 | 90.0 |
| XI | XI | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 1.05 | 3.72 | 6.89 | 2.00 | 45.6 | 90.0 |
| Vice Captain | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.72 | 13.36 | 21.47 | 1.00 | 84.3 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.5 | 3.04 | 9.72 | 16.11 | 8.00 | 59.5 | 78.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 8.0 | 2.90 | 9.59 | 15.75 | 2.00 | 37.4 | 75.0 |
| Bench 4 | Bench | Mohamed Salah | MID | 12 | 13.1 | 0.00 | 22.77 | 37.94 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 10.9 | 6.68 | 19.57 | 31.76 | 18.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.55 | 14.24 | 23.94 | 9.00 | 88.5 | 75.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.6 | 3.36 | 11.03 | 18.04 | 2.00 | 84.6 | 90.0 |
| Bench 2 | Bench | Harry Winks | MID | 11 | 4.5 | 0.16 | 1.09 | 2.48 | 0.00 | 3.9 | 0.0 |