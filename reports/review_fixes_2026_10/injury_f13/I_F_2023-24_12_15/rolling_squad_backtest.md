# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 254.91
- Total actual points: 215.00
- Average predicted points: 63.73
- Average actual points: 53.75
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
- Bank: 100.00 -> 0.30
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Kieran Trippier
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 62.27
- Actual score: 69.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.86 | 10.64 | 17.05 | 2.00 | 91.6 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | 15 | 5.5 | 3.65 | 10.00 | 16.23 | 4.00 | 83.5 | 90.0 |
| Vice Captain | XI | Kieran Trippier | DEF | 15 | 7.0 | 6.38 | 16.94 | 26.84 | 1.00 | 96.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.48 | 11.55 | 18.12 | 9.00 | 92.6 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.90 | 11.26 | 17.98 | 1.00 | 89.8 | 90.0 |
| XI | XI | Matty Cash | DEF | 2 | 5.2 | 3.79 | 10.54 | 16.82 | 2.00 | 70.2 | 90.0 |
| Bench 3 | Bench | Tyrick Mitchell | DEF | 8 | 4.6 | 3.59 | 9.87 | 15.86 | 1.00 | 92.6 | 90.0 |
| XI | XI | Nicolas Jackson | FWD | 7 | 6.8 | 3.87 | 11.27 | 18.03 | 5.00 | 76.5 | 90.0 |
| Bench 2 | Bench | Eddie Nketiah | FWD | 1 | 5.7 | 3.73 | 9.76 | 15.11 | 1.00 | 61.2 | 9.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.79 | 7.85 | 13.11 | 2.00 | 69.0 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.9 | 7.08 | 21.06 | 34.50 | 16.00 | 104.7 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 5.74 | 16.87 | 27.93 | 2.00 | 91.3 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.6 | 6.00 | 15.95 | 25.99 | 5.00 | 87.7 | 80.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.6 | 5.86 | 15.84 | 24.66 | 8.00 | 106.1 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 4.23 | 13.09 | 21.71 | 2.00 | 88.7 | 90.0 |

## GW13

- Train rows: 112534
- Bank: 0.30 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 58.65
- Actual score: 42.00
- Transfer: Matty Cash -> Pedro Porro (projected gain 2.01, hit 0)
- Autosub: Cameron Archer replaced Jarrod Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.88 | 10.66 | 16.95 | 3.00 | 91.5 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | 15 | 5.5 | 3.25 | 9.53 | 15.87 | 3.00 | 86.8 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.92 | 14.41 | 23.46 | 1.00 | 89.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.82 | 13.03 | 19.97 | 6.00 | 98.8 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.94 | 11.11 | 17.68 | 1.00 | 91.2 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 3.32 | 9.86 | 16.75 | 5.00 | 86.7 | 90.0 |
| Bench 3 | Bench | Tyrick Mitchell | DEF | 8 | 4.6 | 2.84 | 8.47 | 13.49 | 1.00 | 73.9 | 90.0 |
| XI | XI | Nicolas Jackson | FWD | 7 | 6.8 | 4.12 | 11.81 | 18.75 | 2.00 | 81.5 | 68.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 4.6 | 2.91 | 7.85 | 12.87 | 2.00 | 68.0 | 90.0 |
| Bench 4 | Bench | Eddie Nketiah | FWD | 1 | 5.7 | 2.41 | 7.63 | 12.26 | 1.00 | 39.1 | 24.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.9 | 6.73 | 21.98 | 36.02 | 5.00 | 106.8 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.6 | 6.09 | 16.98 | 26.87 | 8.00 | 94.5 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 4.89 | 14.80 | 24.56 | 2.00 | 84.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 4.62 | 13.75 | 21.99 | 2.00 | 89.2 | 90.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.6 | 4.61 | 12.99 | 20.81 | 0.00 | 74.4 | 0.0 |

## GW14

- Train rows: 113281
- Bank: 0.10 -> 1.80
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 65.22
- Actual score: 71.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.33) beats the best remaining Triple Captain opportunity (9.31).
- Transfer: Jarrod Bowen -> Anthony Gordon (projected gain 2.45, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.33) beats the best remaining Triple Captain opportunity (9.31).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.73 | 10.21 | 16.38 | 2.00 | 89.1 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | 15 | 5.5 | 2.99 | 9.10 | 15.20 | 6.00 | 86.1 | 85.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.65 | 13.67 | 22.60 | 12.00 | 87.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.41 | 11.87 | 18.54 | 1.00 | 85.7 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.21 | 9.61 | 15.57 | 2.00 | 78.1 | 90.0 |
| Bench 2 | Bench | Pedro Porro | DEF | 18 | 5.3 | 2.72 | 9.31 | 15.93 | 0.00 | 81.5 | 90.0 |
| Bench 3 | Bench | Tyrick Mitchell | DEF | 8 | 4.6 | 2.43 | 7.55 | 12.50 | 2.00 | 71.3 | 90.0 |
| XI | XI | Nicolas Jackson | FWD | 7 | 6.8 | 3.72 | 10.69 | 16.78 | 5.00 | 64.9 | 71.0 |
| XI | XI | Cameron Archer | FWD | 17 | 4.6 | 2.90 | 7.99 | 13.14 | 1.00 | 71.1 | 45.0 |
| Bench 4 | Bench | Eddie Nketiah | FWD | 1 | 5.7 | 2.02 | 6.11 | 10.58 | 1.00 | 30.1 | 23.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.0 | 7.33 | 21.63 | 35.89 | 5.00 | 106.3 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.7 | 6.49 | 17.62 | 28.03 | 8.00 | 98.9 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 6.31 | 16.55 | 25.94 | 5.00 | 100.0 | 77.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 3.56 | 12.90 | 22.37 | 10.00 | 70.8 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.9 | 4.25 | 11.69 | 18.66 | 10.00 | 93.2 | 90.0 |

## GW15

- Train rows: 114034
- Bank: 1.80 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 68.77
- Actual score: 33.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.40) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Nicolas Jackson -> Ollie Watkins (projected gain 7.62, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.40) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.19 | 9.56 | 15.57 | 0.00 | 86.9 | 0.0 |
| Bench 1 | Bench Boost | Nick Pope | GK | 15 | 5.5 | 2.61 | 8.13 | 13.84 | 0.00 | 75.3 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.48 | 15.30 | 24.80 | 1.00 | 98.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.17 | 11.58 | 18.46 | 1.00 | 85.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 3.66 | 10.24 | 17.05 | 5.00 | 82.9 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.64 | 9.86 | 16.19 | 1.00 | 82.1 | 90.0 |
| Bench 2 | Bench Boost | Tyrick Mitchell | DEF | 8 | 4.6 | 2.84 | 7.71 | 12.93 | 1.00 | 74.9 | 28.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.48 | 14.30 | 24.19 | 1.00 | 78.1 | 89.0 |
| Bench 3 | Bench Boost | Cameron Archer | FWD | 17 | 4.6 | 2.17 | 6.69 | 10.92 | 2.00 | 59.0 | 90.0 |
| Bench 4 | Bench Boost | Eddie Nketiah | FWD | 1 | 5.6 | 1.78 | 5.82 | 10.39 | 0.00 | 24.1 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.0 | 7.59 | 21.59 | 36.25 | 3.00 | 106.6 | 66.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.7 | 6.43 | 17.64 | 28.33 | 5.00 | 96.0 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 5.44 | 15.46 | 26.16 | 2.00 | 90.8 | 87.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 3.91 | 12.30 | 19.75 | 6.00 | 60.7 | 39.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.9 | 3.80 | 11.14 | 17.53 | 2.00 | 75.6 | 90.0 |