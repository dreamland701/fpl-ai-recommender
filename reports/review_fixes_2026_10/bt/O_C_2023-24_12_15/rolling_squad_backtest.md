# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 244.66
- Total actual points: 212.00
- Average predicted points: 61.17
- Average actual points: 53.00
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW11 are included before the first simulated week.
- League-average scores were not available for this run.

## GW12

- Train rows: 111791
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Ollie Watkins
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 58.20
- Actual score: 70.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub outfielders: Pedro Porro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.79 | 10.62 | 17.18 | 2.00 | 87.4 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | 15 | 5.5 | 3.44 | 9.89 | 16.15 | 4.00 | 84.5 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.43 | 16.36 | 27.16 | 1.00 | 91.3 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.0 | 3.94 | 11.43 | 18.52 | 1.00 | 86.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.2 | 3.60 | 10.24 | 16.67 | 9.00 | 81.4 | 90.0 |
| XI | XI | Matty Cash | DEF | 2 | 5.2 | 3.73 | 10.17 | 16.02 | 2.00 | 68.5 | 90.0 |
| Bench 2 | Autosub In | Pedro Porro | DEF | 18 | 5.2 | 3.26 | 9.67 | 16.09 | 5.00 | 80.4 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.4 | 5.79 | 17.32 | 28.09 | 6.00 | 86.3 | 90.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 4.5 | 3.05 | 8.97 | 14.75 | 2.00 | 75.0 | 90.0 |
| Bench 4 | Bench | Neal Maupay | FWD | 4 | 4.9 | 2.69 | 8.23 | 13.14 | 1.00 | 62.6 | 18.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.9 | 6.29 | 18.93 | 31.17 | 16.00 | 89.3 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 5.52 | 16.48 | 27.78 | 2.00 | 84.8 | 90.0 |
| XI | Bench | James Maddison | MID | 18 | 8.1 | 4.80 | 14.57 | 24.06 | 0.00 | 70.4 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.7 | 4.29 | 14.15 | 23.41 | 2.00 | 88.7 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.4 | 4.74 | 13.63 | 22.20 | 8.00 | 84.1 | 90.0 |

## GW13

- Train rows: 112534
- Bank: 0.10 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Ollie Watkins
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 56.31
- Actual score: 37.00
- Transfer: James Maddison -> Phil Foden (projected gain 1.96, hit 0)
- Autosub outfielders: Pedro Porro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.51 | 10.02 | 16.17 | 3.00 | 84.4 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | 15 | 5.5 | 3.17 | 9.46 | 15.70 | 3.00 | 86.4 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.07 | 15.38 | 25.33 | 1.00 | 92.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.12 | 11.74 | 18.55 | 6.00 | 86.6 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.81 | 11.10 | 17.96 | 1.00 | 87.4 | 90.0 |
| XI | XI | Matty Cash | DEF | 2 | 5.2 | 3.63 | 10.59 | 16.60 | 0.00 | 74.9 | 45.0 |
| Bench 2 | Autosub In | Pedro Porro | DEF | 18 | 5.2 | 3.31 | 9.90 | 16.83 | 5.00 | 86.2 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.4 | 6.00 | 17.78 | 27.86 | 5.00 | 93.4 | 90.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.94 | 8.19 | 13.43 | 2.00 | 71.0 | 90.0 |
| Bench 4 | Bench | Neal Maupay | FWD | 4 | 4.9 | 1.67 | 6.03 | 10.56 | 1.00 | 37.9 | 18.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.9 | 6.17 | 20.12 | 33.57 | 5.00 | 95.8 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 4.89 | 14.71 | 24.48 | 2.00 | 82.8 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 4.31 | 13.54 | 22.39 | 2.00 | 82.3 | 90.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.6 | 4.69 | 13.34 | 20.86 | 0.00 | 79.5 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 7.5 | 3.94 | 11.73 | 19.02 | 2.00 | 79.6 | 90.0 |

## GW14

- Train rows: 113281
- Bank: 0.60 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Ollie Watkins
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 67.48
- Actual score: 80.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.27) beats the best remaining Bench Boost opportunity (13.00).
- Transfer: Jarrod Bowen -> Bruno Borges Fernandes (projected gain 3.35, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.27) beats the best remaining Bench Boost opportunity (13.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.70 | 10.37 | 16.75 | 2.00 | 86.9 | 90.0 |
| Bench 1 | Bench Boost | Nick Pope | GK | 15 | 5.5 | 3.21 | 9.65 | 16.03 | 6.00 | 86.1 | 85.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.11 | 15.22 | 25.29 | 12.00 | 91.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.42 | 12.34 | 19.40 | 1.00 | 85.1 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.2 | 3.62 | 10.64 | 17.12 | 2.00 | 85.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 3.16 | 10.02 | 17.11 | 0.00 | 88.6 | 90.0 |
| Bench 2 | Bench Boost | Matty Cash | DEF | 2 | 5.1 | 2.98 | 8.72 | 14.37 | 1.00 | 55.9 | 16.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.5 | 6.05 | 17.29 | 27.65 | 11.00 | 92.3 | 90.0 |
| Bench 3 | Bench Boost | Cameron Archer | FWD | 17 | 4.6 | 2.85 | 8.16 | 13.42 | 1.00 | 73.0 | 45.0 |
| Bench 4 | Bench Boost | Neal Maupay | FWD | 4 | 4.9 | 2.23 | 6.68 | 11.48 | 8.00 | 33.9 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.0 | 6.43 | 19.39 | 32.30 | 5.00 | 92.3 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 4.45 | 14.55 | 24.64 | 10.00 | 83.7 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 4.79 | 14.17 | 23.29 | 5.00 | 75.5 | 77.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 4.11 | 13.26 | 21.99 | 2.00 | 87.0 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 7.5 | 3.93 | 11.79 | 19.69 | 9.00 | 74.8 | 72.0 |

## GW15

- Train rows: 114034
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Kieran Trippier
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 62.68
- Actual score: 25.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.51) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Pedro Porro -> Oleksandr Zinchenko (projected gain 0.37, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (6.51) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alphonse Areola | GK | 19 | 4.3 | 3.29 | 10.06 | 16.30 | 0.00 | 87.0 | 0.0 |
| Bench 1 | Bench | Nick Pope | GK | 15 | 5.5 | 3.26 | 9.60 | 15.82 | 0.00 | 84.4 | 0.0 |
| Vice Captain | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.69 | 16.20 | 26.51 | 1.00 | 99.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 4.32 | 12.35 | 19.82 | 1.00 | 86.9 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.2 | 3.88 | 10.89 | 17.86 | 1.00 | 86.8 | 90.0 |
| XI | XI | Oleksandr Zinchenko | DEF | 1 | 5.1 | 3.69 | 10.73 | 17.42 | 1.00 | 78.5 | 26.0 |
| Bench 4 | Bench | Matty Cash | DEF | 2 | 5.0 | 1.90 | 6.76 | 11.30 | 0.00 | 41.8 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.5 | 5.29 | 15.93 | 26.49 | 1.00 | 89.7 | 89.0 |
| Bench 2 | Bench | Neal Maupay | FWD | 4 | 4.9 | 3.10 | 9.06 | 14.46 | 2.00 | 56.3 | 90.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.39 | 7.37 | 11.99 | 2.00 | 62.9 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.51 | 19.47 | 32.27 | 3.00 | 95.8 | 66.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 4.94 | 14.67 | 25.01 | 2.00 | 83.0 | 87.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.1 | 4.52 | 13.69 | 22.11 | 6.00 | 70.5 | 39.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 3.99 | 12.06 | 19.97 | 0.00 | 82.4 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 7.5 | 3.54 | 11.16 | 18.63 | 3.00 | 70.3 | 72.0 |