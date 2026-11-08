# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 210.64
- Total actual points: 193.00
- Average predicted points: 52.66
- Average actual points: 48.25
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
- Bank: 100.00 -> 0.20
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Jarrod Bowen
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 54.52
- Actual score: 64.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.28 | 9.07 | 14.58 | 2.00 | 92.0 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | 15 | 5.5 | 2.86 | 8.23 | 13.18 | 4.00 | 85.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.17 | 12.95 | 20.88 | 1.00 | 76.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 3.89 | 10.18 | 15.85 | 9.00 | 95.0 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.29 | 9.98 | 15.45 | 1.00 | 91.7 | 90.0 |
| XI | XI | Matty Cash | DEF | 2 | 5.2 | 3.20 | 9.24 | 14.32 | 2.00 | 76.8 | 90.0 |
| Bench 2 | Bench | Tyrick Mitchell | DEF | 8 | 4.6 | 3.19 | 8.86 | 14.03 | 1.00 | 95.3 | 90.0 |
| Bench 3 | Bench | Julián Álvarez | FWD | 13 | 7.2 | 2.86 | 10.05 | 16.37 | 5.00 | 71.3 | 78.0 |
| XI | XI | Eddie Nketiah | FWD | 1 | 5.7 | 2.91 | 7.97 | 12.25 | 1.00 | 41.2 | 9.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.39 | 6.83 | 11.47 | 2.00 | 74.6 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.9 | 6.66 | 19.13 | 31.47 | 16.00 | 106.8 | 90.0 |
| Vice Captain | XI | Jarrod Bowen | MID | 19 | 7.6 | 5.53 | 14.01 | 21.44 | 8.00 | 108.2 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.6 | 4.88 | 13.33 | 22.48 | 5.00 | 67.8 | 80.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 4.53 | 12.87 | 21.95 | 2.00 | 71.2 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 4.52 | 11.98 | 18.76 | 1.00 | 90.6 | 45.0 |

## GW13

- Train rows: 112534
- Bank: 0.20 -> 1.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 47.30
- Actual score: 38.00
- Transfer: Kaoru Mitoma -> Cole Palmer (projected gain 4.70, hit 0)
- Autosub: Tyrick Mitchell replaced Jarrod Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.29 | 9.09 | 13.88 | 3.00 | 91.9 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | 15 | 5.5 | 2.86 | 8.55 | 14.30 | 3.00 | 88.3 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.02 | 11.14 | 16.87 | 6.00 | 99.3 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 3.91 | 11.12 | 18.39 | 1.00 | 88.9 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.33 | 9.64 | 14.86 | 1.00 | 93.1 | 90.0 |
| Bench 3 | Bench | Matty Cash | DEF | 2 | 5.1 | 2.40 | 7.52 | 11.40 | 0.00 | 70.1 | 45.0 |
| Bench 2 | Autosub In | Tyrick Mitchell | DEF | 8 | 4.6 | 2.54 | 6.55 | 10.35 | 1.00 | 79.5 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 7.1 | 3.43 | 10.16 | 16.97 | 2.00 | 75.2 | 90.0 |
| XI | XI | Cameron Archer | FWD | 17 | 4.6 | 2.61 | 7.43 | 11.83 | 2.00 | 74.6 | 90.0 |
| Bench 4 | Bench | Eddie Nketiah | FWD | 1 | 5.7 | 2.10 | 5.84 | 9.39 | 1.00 | 29.1 | 24.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.9 | 5.61 | 18.95 | 31.97 | 5.00 | 104.9 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.6 | 4.97 | 14.86 | 23.36 | 8.00 | 93.6 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 3.59 | 12.00 | 20.98 | 2.00 | 87.5 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 3.63 | 11.18 | 17.83 | 2.00 | 94.7 | 74.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.6 | 3.29 | 10.67 | 17.80 | 0.00 | 76.5 | 0.0 |

## GW14

- Train rows: 113281
- Bank: 1.50 -> 2.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 54.30
- Actual score: 62.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.52) beats the best remaining Triple Captain opportunity (8.28).
- Transfer: Jarrod Bowen -> Bryan Mbeumo (projected gain 6.63, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (6.52) beats the best remaining Triple Captain opportunity (8.28).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.04 | 8.24 | 13.12 | 2.00 | 89.5 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | 15 | 5.5 | 2.60 | 7.82 | 12.62 | 6.00 | 88.5 | 85.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 3.65 | 11.19 | 19.64 | 12.00 | 88.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 3.91 | 10.78 | 16.55 | 1.00 | 87.3 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 2.60 | 8.44 | 13.65 | 2.00 | 80.0 | 90.0 |
| Bench 2 | Bench | Matty Cash | DEF | 2 | 5.0 | 2.27 | 7.08 | 11.73 | 1.00 | 36.7 | 16.0 |
| Bench 3 | Bench | Tyrick Mitchell | DEF | 8 | 4.6 | 2.13 | 5.73 | 9.57 | 2.00 | 75.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 7.0 | 2.78 | 9.50 | 14.90 | 5.00 | 40.9 | 86.0 |
| XI | XI | Cameron Archer | FWD | 17 | 4.6 | 2.60 | 6.78 | 12.02 | 1.00 | 76.7 | 45.0 |
| Bench 4 | Bench | Eddie Nketiah | FWD | 1 | 5.7 | 1.51 | 4.91 | 9.02 | 1.00 | 16.1 | 23.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.0 | 6.52 | 18.71 | 31.77 | 5.00 | 107.3 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.7 | 5.27 | 15.10 | 24.12 | 8.00 | 79.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.1 | 5.00 | 13.64 | 21.95 | 5.00 | 105.1 | 77.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 3.05 | 11.31 | 20.79 | 10.00 | 73.7 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 2.84 | 8.85 | 14.24 | 1.00 | 71.2 | 24.0 |

## GW15

- Train rows: 114034
- Bank: 2.00 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 54.52
- Actual score: 29.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.91) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Cole Palmer -> Anthony Gordon (projected gain 3.09, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.91) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 2.40 | 8.09 | 13.41 | 0.00 | 88.3 | 0.0 |
| Bench 1 | Bench Boost | Nick Pope | GK | 15 | 5.5 | 2.22 | 7.15 | 12.06 | 0.00 | 77.8 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.27 | 12.71 | 20.93 | 1.00 | 96.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 3.37 | 9.69 | 15.37 | 1.00 | 86.5 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.03 | 8.39 | 13.37 | 1.00 | 84.1 | 90.0 |
| XI | XI | Tyrick Mitchell | DEF | 8 | 4.6 | 2.54 | 6.71 | 11.00 | 1.00 | 79.5 | 28.0 |
| Bench 4 | Bench Boost | Matty Cash | DEF | 2 | 4.9 | 0.64 | 3.90 | 7.31 | 0.00 | 18.4 | 0.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 7.0 | 3.79 | 11.23 | 17.67 | 2.00 | 77.2 | 67.0 |
| Bench 2 | Bench Boost | Cameron Archer | FWD | 17 | 4.6 | 1.67 | 5.48 | 9.80 | 2.00 | 48.6 | 90.0 |
| Bench 3 | Bench Boost | Eddie Nketiah | FWD | 1 | 5.6 | 1.37 | 4.62 | 7.82 | 0.00 | 13.1 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.0 | 6.38 | 17.57 | 30.24 | 3.00 | 86.6 | 66.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.7 | 5.21 | 15.03 | 24.82 | 5.00 | 99.1 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 4.33 | 13.97 | 23.70 | 2.00 | 93.7 | 87.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.1 | 3.70 | 10.80 | 16.67 | 6.00 | 68.7 | 39.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.0 | 3.21 | 9.65 | 14.64 | 2.00 | 82.2 | 90.0 |