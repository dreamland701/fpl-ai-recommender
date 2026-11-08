# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 258.99
- Total actual points: 208.00
- Average predicted points: 64.75
- Average actual points: 52.00
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
- Vice captain: Jarrod Bowen
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 63.85
- Actual score: 70.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.91 | 10.61 | 16.97 | 2.00 | 92.8 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | 15 | 5.5 | 3.42 | 9.73 | 15.88 | 4.00 | 83.2 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.63 | 16.24 | 26.02 | 1.00 | 94.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.37 | 11.58 | 18.17 | 9.00 | 92.9 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 4.11 | 11.57 | 18.47 | 1.00 | 92.3 | 90.0 |
| XI | XI | Matty Cash | DEF | 2 | 5.2 | 3.82 | 10.61 | 16.86 | 2.00 | 70.1 | 90.0 |
| Bench 2 | Bench | Tyrick Mitchell | DEF | 8 | 4.6 | 3.77 | 10.17 | 16.25 | 1.00 | 94.3 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 5.95 | 17.46 | 27.60 | 6.00 | 89.7 | 90.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.64 | 7.74 | 12.86 | 2.00 | 67.9 | 90.0 |
| Bench 4 | Bench | Rodrigo Muniz Carvalho | FWD | 10 | 4.4 | 1.13 | 3.62 | 5.85 | 0.00 | 33.8 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.9 | 7.26 | 21.48 | 34.90 | 16.00 | 105.9 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 5.89 | 17.05 | 28.26 | 2.00 | 93.6 | 90.0 |
| Vice Captain | XI | Jarrod Bowen | MID | 19 | 7.6 | 6.12 | 16.11 | 25.12 | 8.00 | 109.2 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.6 | 5.50 | 15.50 | 25.35 | 5.00 | 85.3 | 80.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 4.03 | 13.29 | 21.63 | 2.00 | 85.3 | 90.0 |

## GW13

- Train rows: 112534
- Bank: 0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 60.67
- Actual score: 39.00
- Transfer: Nick Pope -> André Onana (projected gain 0.01, hit 0)
- Autosub: Tyrick Mitchell replaced Jarrod Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.85 | 10.52 | 16.62 | 3.00 | 91.0 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 4.8 | 3.33 | 9.49 | 15.78 | 9.00 | 91.3 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.80 | 14.29 | 23.25 | 1.00 | 88.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.89 | 13.10 | 20.06 | 6.00 | 98.7 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 4.00 | 11.32 | 18.02 | 1.00 | 93.1 | 90.0 |
| XI | XI | Matty Cash | DEF | 2 | 5.1 | 3.05 | 9.60 | 15.40 | 0.00 | 67.5 | 45.0 |
| Bench 2 | Autosub In | Tyrick Mitchell | DEF | 8 | 4.6 | 2.88 | 8.55 | 13.59 | 1.00 | 74.6 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 5.72 | 16.75 | 26.16 | 5.00 | 90.9 | 90.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.76 | 7.60 | 12.45 | 2.00 | 67.2 | 90.0 |
| Bench 4 | Bench | Rodrigo Muniz Carvalho | FWD | 10 | 4.4 | 0.86 | 2.13 | 3.53 | 0.00 | 13.6 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.9 | 7.00 | 22.27 | 36.62 | 5.00 | 110.2 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.6 | 6.17 | 17.13 | 27.13 | 8.00 | 96.3 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 5.05 | 15.02 | 24.97 | 2.00 | 86.1 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 4.86 | 14.16 | 22.62 | 2.00 | 90.5 | 90.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.6 | 4.28 | 12.70 | 20.23 | 0.00 | 73.4 | 0.0 |

## GW14

- Train rows: 113281
- Bank: 0.70 -> -0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 67.88
- Actual score: 70.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.55) beats the best remaining Bench Boost opportunity (10.32).
- Transfer: Jarrod Bowen -> Bruno Borges Fernandes (projected gain 5.39, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.55) beats the best remaining Bench Boost opportunity (10.32).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench Boost | André Onana | GK | 14 | 4.8 | 3.23 | 10.30 | 17.07 | 3.00 | 93.3 | 90.0 |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.75 | 10.18 | 16.27 | 2.00 | 89.8 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.93 | 14.24 | 23.50 | 12.00 | 91.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.42 | 11.96 | 18.58 | 1.00 | 86.2 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.17 | 9.61 | 15.57 | 2.00 | 77.9 | 90.0 |
| XI | XI | Matty Cash | DEF | 2 | 5.0 | 2.95 | 8.57 | 14.25 | 1.00 | 55.0 | 16.0 |
| Bench 3 | Bench Boost | Tyrick Mitchell | DEF | 8 | 4.6 | 2.31 | 7.37 | 12.18 | 2.00 | 70.1 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.61 | 14.05 | 23.25 | 11.00 | 68.9 | 90.0 |
| Bench 2 | Bench Boost | Cameron Archer | FWD | 17 | 4.6 | 2.83 | 7.92 | 12.97 | 1.00 | 72.0 | 45.0 |
| Bench 4 | Bench Boost | Rodrigo Muniz Carvalho | FWD | 10 | 4.4 | 0.17 | 1.39 | 2.36 | 0.00 | 12.4 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.0 | 7.48 | 22.01 | 36.47 | 5.00 | 111.7 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.7 | 6.56 | 17.85 | 28.30 | 8.00 | 101.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 6.22 | 16.54 | 25.96 | 5.00 | 100.1 | 77.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 4.05 | 13.19 | 22.04 | 2.00 | 87.9 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 3.72 | 13.08 | 22.72 | 10.00 | 72.2 | 90.0 |

## GW15

- Train rows: 114034
- Bank: -0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 66.59
- Actual score: 29.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.12) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Matty Cash -> Konstantinos Tsimikas (projected gain 1.91, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.12) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: André Onana replaced Alphonse Areola.
- Autosub: Tyrick Mitchell replaced Konstantinos Tsimikas.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Autosub In | André Onana | GK | 14 | 4.8 | 3.23 | 10.01 | 16.68 | 2.00 | 90.5 | 90.0 |
| XI | Bench | Alphonse Areola | GK | 19 | 4.3 | 3.24 | 9.65 | 15.57 | 0.00 | 88.8 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.79 | 15.87 | 25.69 | 1.00 | 103.3 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.26 | 11.93 | 18.88 | 1.00 | 87.5 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.60 | 9.96 | 16.27 | 1.00 | 82.5 | 90.0 |
| XI | Bench | Konstantinos Tsimikas | DEF | 11 | 4.8 | 3.37 | 9.56 | 15.24 | 0.00 | 70.9 | 0.0 |
| Bench 2 | Autosub In | Tyrick Mitchell | DEF | 8 | 4.6 | 2.80 | 7.77 | 12.90 | 1.00 | 74.7 | 28.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.75 | 14.61 | 24.48 | 1.00 | 81.2 | 89.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.22 | 6.74 | 10.94 | 2.00 | 59.6 | 90.0 |
| Bench 4 | Bench | Rodrigo Muniz Carvalho | FWD | 10 | 4.4 | 0.33 | 0.84 | 1.28 | 0.00 | 2.7 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.0 | 7.12 | 21.29 | 35.33 | 3.00 | 107.7 | 66.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.7 | 6.48 | 18.01 | 28.78 | 5.00 | 99.5 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 5.44 | 15.60 | 26.33 | 2.00 | 90.8 | 87.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 4.20 | 12.72 | 21.10 | 0.00 | 86.2 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 4.11 | 12.69 | 20.32 | 6.00 | 64.0 | 39.0 |