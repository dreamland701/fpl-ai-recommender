# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 253.36
- Total actual points: 218.00
- Average predicted points: 63.34
- Average actual points: 54.50
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
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Kieran Trippier
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 63.98
- Actual score: 71.00
- Chip advisory: bench_boost (0.62): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.88 | 10.57 | 16.88 | 2.00 | 92.0 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | 15 | 5.5 | 3.78 | 10.36 | 16.81 | 4.00 | 85.0 | 90.0 |
| Vice Captain | XI | Kieran Trippier | DEF | 15 | 7.0 | 6.37 | 16.95 | 26.88 | 1.00 | 76.7 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 7.9 | 4.60 | 12.71 | 20.21 | 7.00 | 81.7 | 89.0 |
| Bench 2 | Bench | Matty Cash | DEF | 2 | 5.2 | 4.19 | 11.63 | 18.55 | 2.00 | 76.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.49 | 11.58 | 18.15 | 9.00 | 95.0 | 90.0 |
| Bench 3 | Bench | Joachim Andersen | DEF | 8 | 5.1 | 3.90 | 11.32 | 18.10 | 1.00 | 91.7 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 5.98 | 17.50 | 27.78 | 6.00 | 91.2 | 90.0 |
| XI | XI | Eddie Nketiah | FWD | 1 | 5.7 | 4.26 | 11.20 | 17.37 | 1.00 | 41.2 | 9.0 |
| Bench 4 | Bench | Evan Ferguson | FWD | 5 | 6.0 | 3.78 | 10.33 | 16.23 | 0.00 | 44.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.9 | 7.06 | 21.03 | 34.47 | 16.00 | 106.8 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.6 | 5.83 | 15.81 | 24.64 | 8.00 | 108.2 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 5.28 | 14.06 | 21.92 | 1.00 | 90.6 | 45.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 4.26 | 13.21 | 21.94 | 2.00 | 89.7 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.8 | 4.92 | 12.66 | 19.16 | 2.00 | 90.0 | 90.0 |

## GW13

- Train rows: 112534
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Ollie Watkins
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 56.52
- Actual score: 39.00
- Transfer: Anthony Gordon -> Cole Palmer (projected gain 1.96, hit 0)
- Autosub: Matty Cash replaced Jarrod Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.89 | 10.59 | 16.78 | 3.00 | 91.9 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | 15 | 5.5 | 3.33 | 9.75 | 16.23 | 3.00 | 88.3 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.91 | 14.42 | 23.49 | 1.00 | 88.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.82 | 13.04 | 19.97 | 6.00 | 99.3 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 7.9 | 3.62 | 11.54 | 18.91 | 8.00 | 78.4 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.93 | 11.14 | 17.76 | 1.00 | 93.1 | 90.0 |
| Bench 2 | Autosub In | Matty Cash | DEF | 2 | 5.1 | 3.14 | 10.20 | 16.24 | 0.00 | 70.1 | 45.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.95 | 15.76 | 24.18 | 5.00 | 81.3 | 90.0 |
| XI | XI | Eddie Nketiah | FWD | 1 | 5.7 | 3.34 | 10.62 | 17.10 | 1.00 | 29.1 | 24.0 |
| Bench 4 | Bench | Evan Ferguson | FWD | 5 | 6.0 | 1.40 | 4.53 | 7.71 | 5.00 | 25.3 | 76.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.9 | 6.71 | 21.95 | 35.97 | 5.00 | 104.9 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 4.65 | 13.87 | 22.20 | 2.00 | 92.2 | 90.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.6 | 4.75 | 13.44 | 21.55 | 0.00 | 76.5 | 0.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 4.23 | 12.48 | 19.83 | 2.00 | 94.7 | 74.0 |
| Bench 3 | Bench | Kaoru Mitoma | MID | 5 | 6.5 | 2.22 | 9.09 | 16.57 | 0.00 | 37.1 | 0.0 |

## GW14

- Train rows: 113281
- Bank: 0.60 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 65.08
- Actual score: 64.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.32) beats the best remaining Triple Captain opportunity (9.30).
- Transfer: Kaoru Mitoma -> Jérémy Doku (projected gain 3.60, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.32) beats the best remaining Triple Captain opportunity (9.30).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.74 | 10.14 | 16.22 | 2.00 | 89.5 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | 15 | 5.5 | 3.09 | 9.40 | 15.70 | 6.00 | 88.5 | 85.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.69 | 13.83 | 22.87 | 12.00 | 88.7 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 7.9 | 4.48 | 12.64 | 20.77 | 13.00 | 85.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.55 | 12.26 | 19.14 | 1.00 | 87.3 | 90.0 |
| XI | XI | Matty Cash | DEF | 2 | 5.0 | 3.59 | 10.38 | 17.34 | 1.00 | 36.7 | 16.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.28 | 9.87 | 16.01 | 2.00 | 80.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.56 | 13.87 | 23.15 | 11.00 | 67.0 | 90.0 |
| Bench 2 | Bench | Evan Ferguson | FWD | 5 | 6.0 | 2.98 | 8.74 | 14.61 | 2.00 | 66.4 | 90.0 |
| Bench 3 | Bench | Eddie Nketiah | FWD | 1 | 5.7 | 2.81 | 8.56 | 14.86 | 1.00 | 16.1 | 23.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.0 | 7.32 | 21.61 | 35.87 | 5.00 | 107.3 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 6.9 | 6.30 | 16.54 | 25.95 | 5.00 | 105.1 | 77.0 |
| XI | XI | Jérémy Doku | MID | 13 | 6.8 | 4.10 | 12.27 | 20.03 | 1.00 | 74.3 | 51.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 3.82 | 11.51 | 18.40 | 1.00 | 71.2 | 24.0 |
| Bench 4 | Bench | Jarrod Bowen | MID | 19 | 7.6 | 2.23 | 8.96 | 17.17 | 2.00 | 31.4 | 90.0 |

## GW15

- Train rows: 114034
- Bank: 0.30 -> 0.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Kieran Trippier
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 67.79
- Actual score: 44.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.07) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Matty Cash -> Konstantinos Tsimikas (projected gain 2.17, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.07) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.24 | 9.59 | 15.57 | 0.00 | 88.3 | 0.0 |
| Bench 1 | Bench Boost | Nick Pope | GK | 15 | 5.5 | 2.75 | 8.54 | 14.53 | 0.00 | 77.8 | 0.0 |
| Vice Captain | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.47 | 15.31 | 24.83 | 1.00 | 96.1 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 7.9 | 4.95 | 13.68 | 22.92 | 12.00 | 87.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.26 | 11.84 | 18.86 | 1.00 | 86.5 | 90.0 |
| XI | XI | Konstantinos Tsimikas | DEF | 11 | 4.8 | 3.97 | 10.67 | 17.09 | 0.00 | 75.5 | 0.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.71 | 10.10 | 16.63 | 1.00 | 84.1 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.54 | 14.50 | 24.54 | 1.00 | 78.8 | 89.0 |
| Bench 2 | Bench Boost | Evan Ferguson | FWD | 5 | 6.0 | 3.08 | 8.63 | 14.52 | 1.00 | 71.7 | 21.0 |
| Bench 4 | Bench Boost | Eddie Nketiah | FWD | 1 | 5.6 | 2.48 | 8.15 | 14.59 | 0.00 | 13.1 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.0 | 7.58 | 21.57 | 36.24 | 3.00 | 86.6 | 66.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 4.36 | 13.76 | 22.12 | 6.00 | 68.7 | 39.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.6 | 3.67 | 11.75 | 21.13 | 7.00 | 68.7 | 90.0 |
| XI | XI | Jérémy Doku | MID | 13 | 6.8 | 3.40 | 11.45 | 18.90 | 0.00 | 54.8 | 0.0 |
| Bench 3 | Bench Boost | Cole Palmer | MID | 7 | 5.2 | 2.76 | 10.42 | 17.65 | 8.00 | 59.7 | 90.0 |