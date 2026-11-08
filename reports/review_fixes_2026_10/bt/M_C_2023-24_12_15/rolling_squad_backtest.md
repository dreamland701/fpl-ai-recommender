# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 242.92
- Total actual points: 207.00
- Average predicted points: 60.73
- Average actual points: 51.75
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
- Predicted score: 58.19
- Actual score: 70.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Pedro Porro replaced James Maddison.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.77 | 10.64 | 17.37 | 2.00 | 87.4 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | 15 | 5.5 | 3.47 | 9.97 | 16.32 | 4.00 | 84.4 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.46 | 16.46 | 26.97 | 1.00 | 91.3 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.0 | 3.94 | 11.48 | 18.66 | 1.00 | 86.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.2 | 3.62 | 10.31 | 16.73 | 9.00 | 81.4 | 90.0 |
| XI | XI | Matty Cash | DEF | 2 | 5.2 | 3.73 | 10.22 | 16.04 | 2.00 | 68.5 | 90.0 |
| Bench 2 | Autosub In | Pedro Porro | DEF | 18 | 5.2 | 3.23 | 9.57 | 15.89 | 5.00 | 80.5 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.4 | 5.79 | 17.42 | 28.01 | 6.00 | 86.3 | 90.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 4.5 | 3.07 | 9.04 | 14.97 | 2.00 | 75.0 | 90.0 |
| Bench 4 | Bench | Neal Maupay | FWD | 4 | 4.9 | 2.69 | 8.31 | 13.25 | 1.00 | 62.6 | 18.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.9 | 6.32 | 19.11 | 31.36 | 16.00 | 89.2 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 5.48 | 16.39 | 27.64 | 2.00 | 84.9 | 90.0 |
| XI | Bench | James Maddison | MID | 18 | 8.1 | 4.76 | 14.54 | 24.03 | 0.00 | 70.5 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.7 | 4.28 | 14.21 | 23.29 | 2.00 | 88.7 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.4 | 4.72 | 13.63 | 22.17 | 8.00 | 84.1 | 90.0 |

## GW13

- Train rows: 112534
- Bank: 0.10 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Ollie Watkins
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 56.37
- Actual score: 37.00
- Transfer: James Maddison -> Phil Foden (projected gain 1.83, hit 0)
- Autosub: Pedro Porro replaced Jarrod Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.53 | 10.13 | 16.37 | 3.00 | 84.4 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | 15 | 5.5 | 3.18 | 9.54 | 15.86 | 3.00 | 86.4 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.09 | 15.41 | 25.20 | 1.00 | 92.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.2 | 4.14 | 11.88 | 18.87 | 6.00 | 86.5 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.0 | 3.81 | 11.15 | 18.10 | 1.00 | 87.5 | 90.0 |
| XI | XI | Matty Cash | DEF | 2 | 5.2 | 3.60 | 10.64 | 16.66 | 0.00 | 74.9 | 45.0 |
| Bench 2 | Autosub In | Pedro Porro | DEF | 18 | 5.2 | 3.34 | 9.93 | 17.01 | 5.00 | 86.1 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.4 | 5.97 | 17.74 | 28.02 | 5.00 | 93.4 | 90.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 4.5 | 2.97 | 8.24 | 13.55 | 2.00 | 70.9 | 90.0 |
| Bench 4 | Bench | Neal Maupay | FWD | 4 | 4.9 | 1.71 | 6.06 | 10.46 | 1.00 | 37.9 | 18.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.9 | 6.16 | 20.26 | 33.51 | 5.00 | 95.9 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 4.92 | 14.74 | 24.57 | 2.00 | 82.7 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.7 | 4.35 | 13.47 | 22.10 | 2.00 | 82.3 | 90.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.5 | 4.71 | 13.44 | 21.34 | 0.00 | 79.4 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 7.5 | 3.93 | 11.63 | 19.14 | 2.00 | 79.6 | 90.0 |

## GW14

- Train rows: 113281
- Bank: 0.60 -> 1.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Ollie Watkins
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 62.36
- Actual score: 68.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.44) beats the best remaining Triple Captain opportunity (8.18).
- Transfer: Jarrod Bowen -> Jérémy Doku (projected gain 1.46, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (6.44) beats the best remaining Triple Captain opportunity (8.18).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.71 | 10.44 | 16.95 | 2.00 | 86.9 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | 15 | 5.5 | 3.19 | 9.68 | 16.11 | 6.00 | 86.1 | 85.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.09 | 15.13 | 25.23 | 12.00 | 91.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.38 | 12.32 | 19.51 | 1.00 | 85.2 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.58 | 10.59 | 17.18 | 2.00 | 85.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.2 | 3.15 | 10.09 | 17.14 | 0.00 | 88.6 | 90.0 |
| Bench 2 | Bench | Matty Cash | DEF | 2 | 5.1 | 3.01 | 8.81 | 14.55 | 1.00 | 55.9 | 16.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.4 | 6.07 | 17.38 | 28.02 | 11.00 | 92.2 | 90.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 4.5 | 2.87 | 8.18 | 13.51 | 1.00 | 73.0 | 45.0 |
| Bench 4 | Bench | Neal Maupay | FWD | 4 | 4.9 | 2.22 | 6.63 | 11.43 | 8.00 | 33.9 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.9 | 6.44 | 19.41 | 32.47 | 5.00 | 92.3 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 4.44 | 14.56 | 24.71 | 10.00 | 83.8 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 4.79 | 13.98 | 22.99 | 5.00 | 75.5 | 77.0 |
| XI | XI | Phil Foden | MID | 13 | 7.5 | 3.90 | 11.68 | 19.44 | 9.00 | 74.9 | 72.0 |
| XI | XI | Jérémy Doku | MID | 13 | 6.7 | 3.92 | 11.49 | 18.89 | 1.00 | 73.8 | 51.0 |

## GW15

- Train rows: 114034
- Bank: 1.40 -> 2.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Kieran Trippier
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 65.99
- Actual score: 32.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.64) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Nick Pope -> André Onana (projected gain 0.41, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.64) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench Boost | André Onana | GK | 14 | 4.8 | 3.24 | 10.13 | 17.00 | 2.00 | 88.9 | 90.0 |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.26 | 10.01 | 16.35 | 0.00 | 87.0 | 0.0 |
| Vice Captain | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.70 | 16.14 | 26.59 | 1.00 | 99.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.32 | 12.41 | 20.05 | 1.00 | 86.9 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.91 | 10.93 | 17.99 | 1.00 | 86.7 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.2 | 3.53 | 10.25 | 17.22 | 5.00 | 83.3 | 90.0 |
| Bench 4 | Bench Boost | Matty Cash | DEF | 2 | 5.0 | 1.89 | 6.72 | 11.32 | 0.00 | 41.8 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 5.27 | 16.08 | 27.01 | 1.00 | 89.7 | 89.0 |
| Bench 2 | Bench Boost | Neal Maupay | FWD | 4 | 4.9 | 3.12 | 9.15 | 14.59 | 2.00 | 56.3 | 90.0 |
| Bench 3 | Bench Boost | Cameron Archer | FWD | 17 | 4.5 | 2.38 | 7.34 | 12.03 | 2.00 | 62.9 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.0 | 6.48 | 19.49 | 32.53 | 3.00 | 95.9 | 66.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 4.91 | 14.61 | 25.12 | 2.00 | 83.0 | 87.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 4.55 | 13.74 | 22.23 | 6.00 | 70.4 | 39.0 |
| XI | XI | Phil Foden | MID | 13 | 7.5 | 3.58 | 11.19 | 18.79 | 3.00 | 70.3 | 72.0 |
| XI | XI | Jérémy Doku | MID | 13 | 6.7 | 3.36 | 10.55 | 17.09 | 0.00 | 56.9 | 0.0 |