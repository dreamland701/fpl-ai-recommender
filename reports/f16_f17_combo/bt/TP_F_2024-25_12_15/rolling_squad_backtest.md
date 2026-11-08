# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 242.01
- Total actual points: 302.00
- Average predicted points: 60.50
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
- Predicted score: 64.09
- Actual score: 68.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 4.9 | 3.48 | 9.65 | 15.76 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.33 | 1.01 | 1.44 | 0.00 | 12.2 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.78 | 12.97 | 20.71 | 1.00 | 90.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.3 | 4.35 | 12.19 | 19.90 | 0.00 | 89.9 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 4.00 | 10.80 | 17.53 | 0.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.37 | 7.53 | 12.10 | 1.00 | 79.7 | 90.0 |
| Bench 3 | Bench | Dara O'Shea | DEF | 10 | 4.0 | 2.68 | 7.36 | 12.00 | 2.00 | 88.7 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 5.52 | 15.14 | 23.84 | 2.00 | 89.0 | 90.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 7.9 | 4.76 | 13.06 | 21.31 | 12.00 | 85.4 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.8 | 4.35 | 12.87 | 21.43 | 16.00 | 88.6 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 7.95 | 22.12 | 35.99 | 13.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.24 | 18.29 | 30.46 | 2.00 | 85.3 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 6.15 | 16.77 | 26.78 | 2.00 | 90.0 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 4.56 | 11.99 | 19.27 | 1.00 | 81.4 | 58.0 |
| Bench 2 | Bench | Harry Winks | MID | 11 | 4.5 | 3.06 | 8.69 | 13.72 | 1.00 | 75.6 | 10.0 |

## GW13

- Train rows: 141592
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 68.21
- Actual score: 85.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.15) beats the best remaining Triple Captain opportunity (9.00).
- Transfer: Emile Smith Rowe -> Alex Iwobi (projected gain 2.10, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.15) beats the best remaining Triple Captain opportunity (9.00).
- Autosub: Taylor Harwood-Bellis replaced Joško Gvardiol.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 4.9 | 3.11 | 9.29 | 15.36 | 0.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.68 | 1.20 | 1.68 | 0.00 | 11.9 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.94 | 11.59 | 18.53 | 6.00 | 90.0 | 90.0 |
| XI | Bench | Joško Gvardiol | DEF | 13 | 6.3 | 3.68 | 11.50 | 19.16 | 0.00 | 89.1 | 0.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.28 | 9.72 | 15.84 | 2.00 | 86.8 | 90.0 |
| Bench 2 | Autosub In | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.49 | 7.62 | 12.26 | 1.00 | 81.4 | 90.0 |
| Bench 3 | Bench | Dara O'Shea | DEF | 10 | 4.0 | 2.43 | 7.48 | 12.14 | 1.00 | 86.9 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 6.12 | 17.72 | 27.41 | 2.00 | 90.0 | 90.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 7.9 | 5.17 | 14.63 | 23.40 | 6.00 | 90.0 | 70.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 4.18 | 13.30 | 21.33 | 1.00 | 66.2 | 21.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 8.15 | 24.08 | 38.09 | 13.00 | 90.0 | 83.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.62 | 18.59 | 29.98 | 14.00 | 90.0 | 85.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.00 | 13.54 | 21.92 | 9.00 | 78.1 | 65.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.6 | 3.67 | 10.91 | 17.61 | 5.00 | 87.0 | 85.0 |
| Bench 4 | Bench | Harry Winks | MID | 11 | 4.5 | 1.08 | 4.60 | 8.44 | 0.00 | 25.7 | 0.0 |

## GW14

- Train rows: 142282
- Bank: 0.20 -> 2.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 62.55
- Actual score: 84.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.18) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Alexander Isak -> Chris Wood (projected gain 3.81, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.18) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 4.9 | 3.08 | 8.91 | 14.94 | 6.00 | 88.8 | 90.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.21 | 0.74 | 1.33 | 0.00 | 9.6 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.27 | 12.82 | 20.88 | 1.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.38 | 9.70 | 15.94 | 6.00 | 85.9 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 2.64 | 8.42 | 14.75 | 6.00 | 53.5 | 90.0 |
| Bench 2 | Bench Boost | Dara O'Shea | DEF | 10 | 4.0 | 2.52 | 7.32 | 12.07 | 1.00 | 83.2 | 90.0 |
| Bench 3 | Bench Boost | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 1.64 | 5.38 | 9.13 | 0.00 | 63.5 | 0.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 8.0 | 5.75 | 16.59 | 25.83 | 0.00 | 90.0 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.28 | 13.97 | 21.80 | 2.00 | 77.9 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.6 | 3.69 | 11.05 | 18.25 | 2.00 | 73.5 | 61.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 7.75 | 23.79 | 38.27 | 18.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 7.37 | 20.66 | 33.17 | 7.00 | 90.0 | 78.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.66 | 13.09 | 22.70 | 2.00 | 75.1 | 90.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.6 | 3.76 | 10.89 | 17.88 | 15.00 | 81.4 | 90.0 |
| Bench 4 | Bench Boost | Harry Winks | MID | 11 | 4.5 | 0.82 | 2.67 | 5.03 | 0.00 | 15.9 | 0.0 |

## GW15

- Train rows: 142975
- Bank: 2.10 -> 1.50
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Matheus Santos Carneiro Da Cunha
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 47.16
- Actual score: 65.00
- Transfer: Jordan Pickford -> David Raya Martin (projected gain 11.08, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.86 | 11.12 | 17.84 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.55 | 1.01 | 1.47 | 0.00 | 11.3 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.13 | 11.56 | 19.27 | 1.00 | 84.3 | 90.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 12 | 6.3 | 0.00 | 10.09 | 16.97 | 0.00 | 0.0 | 0.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.07 | 9.67 | 15.80 | 1.00 | 89.0 | 90.0 |
| XI | XI | Dara O'Shea | DEF | 10 | 4.0 | 2.51 | 7.19 | 11.74 | 1.00 | 84.1 | 90.0 |
| XI | XI | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 1.15 | 3.88 | 7.03 | 2.00 | 48.5 | 90.0 |
| Vice Captain | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.79 | 13.46 | 21.56 | 1.00 | 86.1 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.5 | 3.15 | 9.90 | 16.27 | 8.00 | 62.7 | 78.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 8.0 | 3.03 | 9.78 | 15.90 | 2.00 | 40.9 | 75.0 |
| Bench 4 | Bench | Mohamed Salah | MID | 12 | 13.1 | 0.00 | 22.76 | 37.81 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 10.9 | 6.72 | 19.62 | 31.77 | 18.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.60 | 14.34 | 24.03 | 9.00 | 89.8 | 75.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.6 | 3.42 | 11.12 | 18.11 | 2.00 | 86.2 | 90.0 |
| Bench 2 | Bench | Harry Winks | MID | 11 | 4.5 | 0.09 | 1.44 | 3.30 | 0.00 | 2.1 | 0.0 |