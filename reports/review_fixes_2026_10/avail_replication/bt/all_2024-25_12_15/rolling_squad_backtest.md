# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 206.24
- Total actual points: 273.00
- Average predicted points: 51.56
- Average actual points: 68.25
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
- Predicted score: 54.77
- Actual score: 46.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 2.96 | 9.09 | 14.40 | 6.00 | 92.2 | 90.0 |
| Bench 1 | Bench | Emiliano Martínez Romero | GK | 2 | 5.0 | 2.76 | 8.33 | 13.71 | 2.00 | 92.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.97 | 11.16 | 17.15 | 1.00 | 101.8 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.3 | 3.74 | 10.54 | 17.12 | 0.00 | 88.3 | 90.0 |
| XI | XI | Noussair Mazraoui | DEF | 14 | 4.6 | 3.42 | 9.21 | 14.29 | 2.00 | 92.9 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 3.44 | 8.68 | 13.51 | 1.00 | 96.5 | 90.0 |
| Bench 3 | Bench | Marc Guéhi | DEF | 7 | 4.5 | 2.68 | 8.16 | 13.63 | 1.00 | 87.9 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 6.0 | 3.28 | 10.45 | 16.56 | 2.00 | 78.9 | 85.0 |
| Bench 2 | Bench | Raúl Jiménez | FWD | 9 | 5.8 | 3.04 | 8.65 | 14.50 | 2.00 | 73.1 | 70.0 |
| Bench 4 | Bench | Liam Delap | FWD | 10 | 5.6 | 2.46 | 7.89 | 12.74 | 2.00 | 70.5 | 80.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 7.61 | 20.91 | 32.13 | 13.00 | 115.2 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 5.94 | 16.81 | 27.68 | 2.00 | 105.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 5.06 | 14.15 | 22.93 | 2.00 | 108.3 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 3.12 | 12.28 | 20.52 | 3.00 | 84.9 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 4.61 | 11.17 | 17.97 | 1.00 | 91.6 | 58.0 |

## GW13

- Train rows: 141592
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 55.48
- Actual score: 82.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.18) beats the best remaining Triple Captain opportunity (7.82).
- Transfer: Raúl Jiménez -> João Pedro Junqueira de Jesus (projected gain 1.39, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.18) beats the best remaining Triple Captain opportunity (7.82).
- Autosub: Liam Delap replaced Joško Gvardiol.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.28 | 9.12 | 14.57 | 2.00 | 93.1 | 90.0 |
| Bench 1 | Bench | Emiliano Martínez Romero | GK | 2 | 5.0 | 2.54 | 7.51 | 12.58 | 1.00 | 91.6 | 45.0 |
| XI | Bench | Joško Gvardiol | DEF | 13 | 6.3 | 2.58 | 9.95 | 16.63 | 0.00 | 83.1 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.13 | 9.82 | 15.32 | 6.00 | 87.9 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 7 | 4.5 | 2.57 | 7.58 | 12.95 | 3.00 | 89.1 | 90.0 |
| XI | XI | Noussair Mazraoui | DEF | 14 | 4.6 | 2.65 | 7.49 | 11.89 | 1.00 | 81.7 | 55.0 |
| Bench 3 | Bench | Lewis Hall | DEF | 15 | 4.4 | 2.54 | 7.15 | 11.01 | 2.00 | 79.2 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.7 | 3.65 | 9.47 | 14.11 | 2.00 | 49.2 | 71.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 6.0 | 3.30 | 8.91 | 14.59 | 2.00 | 75.2 | 78.0 |
| Bench 2 | Autosub In | Liam Delap | FWD | 10 | 5.6 | 2.56 | 8.13 | 13.25 | 2.00 | 71.5 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 7.18 | 20.26 | 32.49 | 13.00 | 105.5 | 83.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 5.59 | 15.94 | 25.78 | 14.00 | 98.0 | 85.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 3.90 | 12.42 | 20.20 | 2.00 | 93.1 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.29 | 11.39 | 18.78 | 9.00 | 76.1 | 65.0 |
| Bench 4 | Bench | Emile Smith Rowe | MID | 9 | 5.8 | 2.18 | 7.37 | 12.95 | 2.00 | 64.8 | 85.0 |

## GW14

- Train rows: 142282
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 54.25
- Actual score: 74.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.10) beats the best remaining Bench Boost opportunity (3.91).
- Transfer: Joško Gvardiol -> Pedro Porro (projected gain 3.76, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.10) beats the best remaining Bench Boost opportunity (3.91).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 2.99 | 8.59 | 13.85 | 6.00 | 88.9 | 90.0 |
| Bench 1 | Bench Boost | Emiliano Martínez Romero | GK | 2 | 5.0 | 2.22 | 6.22 | 10.94 | 2.00 | 80.1 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 3.36 | 10.75 | 17.45 | 1.00 | 88.9 | 28.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.59 | 9.28 | 15.02 | 1.00 | 98.4 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 7 | 4.5 | 2.62 | 7.13 | 11.93 | 6.00 | 84.8 | 90.0 |
| Bench 3 | Bench Boost | Lewis Hall | DEF | 15 | 4.4 | 2.00 | 6.99 | 11.45 | 1.00 | 83.1 | 90.0 |
| Bench 4 | Bench Boost | Noussair Mazraoui | DEF | 14 | 4.6 | 1.78 | 5.83 | 9.60 | 1.00 | 64.0 | 90.0 |
| XI | XI | Liam Delap | FWD | 10 | 5.6 | 2.94 | 8.43 | 13.42 | 2.00 | 77.6 | 78.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.9 | 2.51 | 8.38 | 14.14 | 0.00 | 73.8 | 0.0 |
| Bench 2 | Bench Boost | João Pedro Junqueira de Jesus | FWD | 5 | 5.7 | 2.09 | 6.55 | 9.77 | 5.00 | 24.9 | 79.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 6.86 | 20.30 | 33.01 | 18.00 | 94.6 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.28 | 16.97 | 27.57 | 7.00 | 109.7 | 78.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 2.84 | 11.63 | 19.95 | 2.00 | 75.1 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.8 | 2.86 | 9.49 | 18.40 | 2.00 | 67.9 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.7 | 2.44 | 8.18 | 13.43 | 2.00 | 70.8 | 70.0 |

## GW15

- Train rows: 142975
- Bank: 0.60 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 41.74
- Actual score: 71.00
- Transfer: Emile Smith Rowe -> Alex Iwobi (projected gain 3.96, hit 0)
- Autosub: Lewis Hall replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.27 | 9.82 | 16.13 | 2.00 | 92.7 | 90.0 |
| Bench 1 | Bench | Emiliano Martínez Romero | GK | 2 | 5.0 | 2.91 | 7.48 | 12.24 | 6.00 | 86.6 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 2.44 | 8.24 | 14.39 | 3.00 | 74.9 | 90.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 12 | 6.3 | 1.96 | 8.18 | 14.14 | 0.00 | 47.2 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 7 | 4.5 | 2.61 | 7.16 | 11.37 | 1.00 | 83.6 | 90.0 |
| XI | XI | Noussair Mazraoui | DEF | 14 | 4.6 | 2.22 | 6.55 | 10.30 | 1.00 | 73.3 | 24.0 |
| Bench 2 | Autosub In | Lewis Hall | DEF | 15 | 4.4 | 2.17 | 6.02 | 9.59 | 1.00 | 83.5 | 82.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.8 | 3.66 | 10.06 | 16.01 | 2.00 | 74.2 | 70.0 |
| XI | XI | Liam Delap | FWD | 10 | 5.6 | 2.53 | 6.91 | 11.37 | 1.00 | 68.5 | 80.0 |
| Bench 4 | Bench | Danny Welbeck | FWD | 5 | 5.9 | 1.64 | 4.05 | 7.64 | 1.00 | 20.7 | 20.0 |
| Captain | Bench | Mohamed Salah | MID | 12 | 13.1 | 5.38 | 19.33 | 32.89 | 0.00 | 71.5 | 0.0 |
| Vice Captain | Captain | Cole Palmer | MID | 6 | 10.9 | 5.30 | 15.64 | 25.84 | 18.00 | 96.7 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.61 | 12.34 | 20.64 | 9.00 | 87.5 | 75.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.6 | 2.89 | 9.96 | 15.61 | 2.00 | 82.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 2.45 | 8.68 | 15.72 | 13.00 | 72.6 | 90.0 |