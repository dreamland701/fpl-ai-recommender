# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 233.42
- Total actual points: 279.00
- Average predicted points: 58.35
- Average actual points: 69.75
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
- Predicted score: 63.02
- Actual score: 46.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.71 | 10.58 | 17.09 | 6.00 | 87.9 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.03 | 0.41 | 0.63 | 0.00 | 4.5 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.63 | 12.76 | 20.43 | 1.00 | 90.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.3 | 4.32 | 12.35 | 20.27 | 0.00 | 87.6 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 3.61 | 10.22 | 16.33 | 1.00 | 88.7 | 90.0 |
| Bench 2 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.53 | 7.99 | 12.91 | 1.00 | 82.4 | 90.0 |
| Bench 3 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 2.28 | 7.22 | 11.92 | 0.00 | 83.6 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 5.41 | 14.94 | 23.53 | 2.00 | 85.6 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 6.0 | 3.79 | 11.86 | 18.81 | 2.00 | 79.1 | 85.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 5.0 | 1.93 | 6.68 | 10.64 | 1.00 | 60.2 | 13.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 7.84 | 22.14 | 36.15 | 13.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.88 | 19.36 | 31.73 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 6.02 | 16.52 | 26.38 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 4.26 | 14.39 | 23.64 | 3.00 | 88.5 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 4.71 | 12.69 | 20.55 | 1.00 | 84.8 | 58.0 |

## GW13

- Train rows: 141592
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 64.82
- Actual score: 83.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.04) beats the best remaining Triple Captain opportunity (8.77).
- Transfer: Emile Smith Rowe -> Alex Iwobi (projected gain 1.74, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.04) beats the best remaining Triple Captain opportunity (8.77).
- Autosub: Taylor Harwood-Bellis replaced Joško Gvardiol.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.95 | 10.97 | 17.62 | 2.00 | 89.8 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.34 | 0.54 | 0.79 | 0.00 | 3.5 | 0.0 |
| XI | Bench | Joško Gvardiol | DEF | 13 | 6.3 | 3.68 | 11.70 | 19.59 | 0.00 | 85.5 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.70 | 11.17 | 17.96 | 6.00 | 84.8 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 2.74 | 8.61 | 13.84 | 2.00 | 72.3 | 90.0 |
| Bench 2 | Autosub In | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.60 | 8.01 | 13.01 | 1.00 | 84.8 | 90.0 |
| Bench 4 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 1.16 | 4.04 | 7.19 | 0.00 | 44.4 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 3.97 | 12.81 | 20.56 | 1.00 | 59.2 | 21.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 6.0 | 3.71 | 10.33 | 16.86 | 2.00 | 72.2 | 78.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 5.0 | 1.54 | 5.18 | 8.83 | 2.00 | 39.9 | 87.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 8.04 | 24.07 | 38.21 | 13.00 | 90.0 | 83.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.45 | 18.41 | 29.83 | 14.00 | 90.0 | 85.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.25 | 14.47 | 24.21 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.73 | 12.92 | 20.94 | 9.00 | 68.7 | 65.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.6 | 3.53 | 10.79 | 17.58 | 5.00 | 83.7 | 85.0 |

## GW14

- Train rows: 142282
- Bank: 0.20 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 61.17
- Actual score: 78.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.40) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Alexander Isak -> Nicolas Jackson (projected gain 9.88, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.40) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.62 | 10.06 | 16.34 | 6.00 | 85.8 | 90.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.00 | 0.24 | 0.47 | 0.00 | 3.4 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.25 | 12.79 | 20.69 | 1.00 | 90.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 2.66 | 8.63 | 15.03 | 6.00 | 46.6 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 2.52 | 8.24 | 13.60 | 1.00 | 76.8 | 90.0 |
| Bench 3 | Bench Boost | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.33 | 7.02 | 11.63 | 0.00 | 81.8 | 0.0 |
| Bench 4 | Bench Boost | Jan Bednarek | DEF | 17 | 4.0 | 0.69 | 2.54 | 4.76 | 0.00 | 32.7 | 0.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 8.1 | 5.75 | 16.51 | 25.53 | 0.00 | 89.7 | 0.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.9 | 3.07 | 9.45 | 15.72 | 0.00 | 68.5 | 0.0 |
| Bench 2 | Bench Boost | Cameron Archer | FWD | 17 | 5.0 | 2.38 | 6.65 | 10.79 | 2.00 | 63.3 | 71.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 7.87 | 24.28 | 38.99 | 18.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 7.37 | 20.81 | 33.37 | 7.00 | 90.0 | 78.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.46 | 12.60 | 21.84 | 2.00 | 70.3 | 90.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.6 | 3.72 | 10.84 | 17.74 | 15.00 | 80.9 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.8 | 3.61 | 10.76 | 19.43 | 2.00 | 74.5 | 90.0 |

## GW15

- Train rows: 142975
- Bank: 0.60 -> 0.60
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Bruno Borges Fernandes
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 44.41
- Actual score: 72.00
- Transfer: Danny Welbeck -> João Pedro Junqueira de Jesus (projected gain 5.99, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.78 | 11.04 | 17.78 | 2.00 | 88.6 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.21 | 0.32 | 0.51 | 0.00 | 2.1 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.08 | 11.64 | 19.52 | 1.00 | 79.4 | 90.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 12 | 6.3 | 0.00 | 9.81 | 16.63 | 0.00 | 0.0 | 0.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 2.67 | 7.75 | 12.72 | 1.00 | 77.1 | 82.0 |
| XI | XI | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 1.00 | 3.68 | 6.88 | 2.00 | 44.8 | 90.0 |
| Bench 2 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.19 | 1.43 | 3.08 | 0.00 | 19.5 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.9 | 4.17 | 11.15 | 17.51 | 2.00 | 60.6 | 70.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 8.1 | 2.40 | 8.41 | 13.94 | 2.00 | 27.2 | 75.0 |
| XI | XI | Cameron Archer | FWD | 17 | 5.0 | 2.23 | 6.51 | 10.91 | 2.00 | 61.7 | 72.0 |
| Bench 4 | Bench | Mohamed Salah | MID | 12 | 13.1 | 0.00 | 23.17 | 38.64 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 10.9 | 6.56 | 19.39 | 31.52 | 18.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.42 | 14.02 | 23.63 | 9.00 | 83.6 | 75.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.6 | 3.28 | 10.95 | 17.99 | 2.00 | 82.3 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 3.27 | 10.18 | 18.46 | 13.00 | 71.6 | 90.0 |