# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 230.07
- Total actual points: 296.00
- Average predicted points: 57.52
- Average actual points: 74.00
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
- Predicted score: 63.01
- Actual score: 45.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.06 | 11.39 | 18.03 | 6.00 | 86.4 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.08 | 0.47 | 0.68 | 0.00 | 4.4 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.66 | 13.34 | 21.29 | 1.00 | 90.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.3 | 4.31 | 13.05 | 21.32 | 0.00 | 85.7 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 4.01 | 11.06 | 17.82 | 0.00 | 87.1 | 90.0 |
| Bench 2 | Bench | Lewis Hall | DEF | 15 | 4.4 | 3.63 | 10.56 | 16.81 | 1.00 | 87.9 | 90.0 |
| Bench 3 | Bench | Cameron Burgess | DEF | 10 | 3.9 | 1.93 | 4.99 | 7.75 | 2.00 | 68.3 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 5.34 | 14.85 | 23.33 | 2.00 | 85.0 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 6.0 | 3.66 | 11.68 | 18.69 | 2.00 | 80.0 | 85.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.5 | 0.16 | 1.04 | 2.17 | 0.00 | 10.3 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 7.67 | 21.85 | 35.64 | 13.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.84 | 19.27 | 31.56 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 5.86 | 15.97 | 25.69 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 4.27 | 14.33 | 23.62 | 3.00 | 89.7 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 4.65 | 12.50 | 20.31 | 1.00 | 85.5 | 58.0 |

## GW13

- Train rows: 141592
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 61.25
- Actual score: 73.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.14) beats the best remaining Bench Boost opportunity (5.77).
- Transfer: Emile Smith Rowe -> Alex Iwobi (projected gain 1.81, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.14) beats the best remaining Bench Boost opportunity (5.77).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.09 | 11.50 | 18.33 | 2.00 | 89.0 | 90.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.33 | 0.23 | 0.35 | 0.00 | 4.4 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.3 | 3.62 | 11.72 | 19.73 | 0.00 | 86.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.60 | 11.15 | 18.03 | 6.00 | 85.2 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 2.85 | 9.02 | 15.03 | 2.00 | 81.1 | 90.0 |
| Bench 2 | Bench Boost | Lewis Hall | DEF | 15 | 4.4 | 2.79 | 8.70 | 13.97 | 2.00 | 72.7 | 90.0 |
| Bench 3 | Bench Boost | Cameron Burgess | DEF | 10 | 3.9 | 1.76 | 5.56 | 8.60 | 2.00 | 67.6 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 3.99 | 12.77 | 20.59 | 1.00 | 60.5 | 21.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 6.0 | 3.71 | 10.91 | 17.61 | 2.00 | 70.0 | 78.0 |
| Bench 4 | Bench Boost | Ross Stewart | FWD | 17 | 4.5 | 0.26 | 0.94 | 1.89 | 0.00 | 8.5 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 7.74 | 23.18 | 37.18 | 13.00 | 90.0 | 83.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.29 | 17.97 | 29.29 | 14.00 | 90.0 | 85.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.21 | 14.48 | 24.25 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.96 | 13.29 | 21.17 | 9.00 | 67.1 | 65.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.6 | 3.32 | 10.49 | 17.34 | 5.00 | 84.9 | 85.0 |

## GW14

- Train rows: 142282
- Bank: 0.20 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.68
- Actual score: 82.00
- Transfer: Alexander Isak -> Nicolas Jackson (projected gain 8.34, hit 0)
- Autosub: Lewis Hall replaced Nicolas Jackson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.75 | 10.64 | 17.14 | 6.00 | 84.8 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.03 | 0.26 | 0.48 | 0.00 | 3.3 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.19 | 12.73 | 20.67 | 1.00 | 90.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 2.81 | 9.20 | 15.61 | 6.00 | 44.6 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.16 | 9.15 | 15.06 | 6.00 | 83.1 | 90.0 |
| Bench 2 | Autosub In | Lewis Hall | DEF | 15 | 4.4 | 2.43 | 8.12 | 13.58 | 1.00 | 77.6 | 90.0 |
| Bench 3 | Bench | Cameron Burgess | DEF | 10 | 3.9 | 2.28 | 6.22 | 9.64 | 0.00 | 70.5 | 0.0 |
| XI | Bench | Nicolas Jackson | FWD | 6 | 8.1 | 5.61 | 16.44 | 25.37 | 0.00 | 89.0 | 0.0 |
| XI | Bench | Danny Welbeck | FWD | 5 | 5.9 | 3.03 | 9.51 | 15.86 | 0.00 | 68.8 | 0.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.30 | 0.87 | 1.56 | 0.00 | 7.2 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 7.79 | 23.95 | 38.56 | 18.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 7.22 | 20.68 | 33.08 | 7.00 | 90.0 | 78.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.30 | 12.12 | 21.54 | 2.00 | 73.6 | 90.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.6 | 3.64 | 10.64 | 17.57 | 15.00 | 82.1 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.8 | 3.39 | 10.25 | 19.03 | 2.00 | 77.2 | 90.0 |

## GW15

- Train rows: 142975
- Bank: 0.60 -> 0.20
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Bruno Borges Fernandes
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 50.13
- Actual score: 96.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.63) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Nicolas Jackson -> Alexander Isak (projected gain 5.44, hit 0)
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (5.63) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.85 | 11.23 | 18.02 | 2.00 | 88.7 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.20 | 0.17 | 0.31 | 0.00 | 2.5 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.12 | 11.78 | 19.65 | 1.00 | 78.9 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 2.73 | 8.72 | 14.54 | 1.00 | 83.7 | 90.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 12 | 6.3 | 0.00 | 8.13 | 14.50 | 0.00 | 0.0 | 0.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 2.64 | 7.96 | 13.07 | 1.00 | 76.7 | 82.0 |
| XI | XI | Cameron Burgess | DEF | 10 | 3.9 | 0.97 | 3.10 | 5.54 | 4.00 | 37.9 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 4.19 | 12.89 | 21.76 | 8.00 | 73.9 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.9 | 1.99 | 5.87 | 10.72 | 1.00 | 32.4 | 20.0 |
| Bench 2 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.01 | 0.63 | 1.15 | 0.00 | 3.7 | 0.0 |
| Bench 4 | Bench | Mohamed Salah | MID | 12 | 13.1 | 0.00 | 22.41 | 39.04 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 10.9 | 6.26 | 18.77 | 30.76 | 18.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.49 | 14.03 | 23.53 | 9.00 | 83.8 | 75.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.6 | 3.22 | 10.71 | 17.85 | 2.00 | 84.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 3.15 | 10.02 | 18.33 | 13.00 | 72.2 | 90.0 |