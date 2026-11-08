# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 256.23
- Total actual points: 229.00
- Average predicted points: 64.06
- Average actual points: 57.25
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
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 64.18
- Actual score: 69.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 4.00 | 10.77 | 17.09 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Loris Karius | GK | 15 | 3.9 | 0.00 | 0.07 | 0.25 | 0.00 | 1.2 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.86 | 15.56 | 25.31 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.66 | 12.20 | 18.85 | 9.00 | 87.9 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.97 | 11.09 | 17.73 | 1.00 | 89.7 | 90.0 |
| Bench 2 | Bench | Harry Maguire | DEF | 14 | 4.2 | 2.80 | 8.21 | 12.70 | 6.00 | 66.7 | 90.0 |
| Bench 3 | Bench | Jonny Evans | DEF | 14 | 4.0 | 2.66 | 7.59 | 11.85 | 0.00 | 62.8 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.04 | 21.34 | 35.05 | 16.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 5.63 | 16.92 | 26.82 | 6.00 | 87.3 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.62 | 7.21 | 12.37 | 2.00 | 72.3 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 5.54 | 16.43 | 27.46 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.6 | 6.22 | 16.12 | 25.98 | 5.00 | 85.9 | 80.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.6 | 5.50 | 15.71 | 24.45 | 8.00 | 90.0 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 5.02 | 14.04 | 21.60 | 1.00 | 80.0 | 45.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 3.70 | 12.68 | 21.72 | 2.00 | 86.8 | 90.0 |

## GW13

- Train rows: 112534
- Bank: 0.00 -> 1.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 60.87
- Actual score: 46.00
- Transfer: Kaoru Mitoma -> Cole Palmer (projected gain 5.03, hit 0)
- Autosub: Cameron Archer replaced Jarrod Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.94 | 10.44 | 16.55 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Loris Karius | GK | 15 | 3.9 | 0.00 | 0.00 | 0.04 | 0.00 | 1.4 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.70 | 13.63 | 22.64 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.58 | 12.95 | 19.85 | 6.00 | 90.0 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 4.03 | 11.13 | 17.67 | 1.00 | 88.9 | 90.0 |
| Bench 3 | Bench | Harry Maguire | DEF | 14 | 4.2 | 2.33 | 6.83 | 11.01 | 6.00 | 70.9 | 90.0 |
| Bench 4 | Bench | Jonny Evans | DEF | 14 | 4.0 | 0.92 | 2.95 | 5.38 | 0.00 | 34.8 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 8.01 | 23.96 | 39.06 | 7.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.53 | 15.05 | 23.47 | 5.00 | 81.8 | 90.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 4.6 | 2.88 | 7.50 | 12.44 | 2.00 | 70.4 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.6 | 5.81 | 16.29 | 25.99 | 8.00 | 90.0 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 4.73 | 14.57 | 24.40 | 2.00 | 85.1 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 4.31 | 13.62 | 22.41 | 2.00 | 87.8 | 90.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.6 | 4.51 | 12.57 | 20.40 | 0.00 | 76.6 | 0.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 3.72 | 12.46 | 20.02 | 2.00 | 87.1 | 74.0 |

## GW14

- Train rows: 113281
- Bank: 1.30 -> 0.60
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 66.53
- Actual score: 75.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.69) beats the best remaining Triple Captain opportunity (8.38).
- Transfer: Jarrod Bowen -> Bruno Borges Fernandes (projected gain 5.35, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (7.69) beats the best remaining Triple Captain opportunity (8.38).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.93 | 10.23 | 16.27 | 2.00 | 88.4 | 90.0 |
| Bench 1 | Bench | Loris Karius | GK | 15 | 3.9 | 0.04 | 0.00 | 0.07 | 0.00 | 1.1 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.56 | 13.43 | 22.32 | 12.00 | 86.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.53 | 12.59 | 19.33 | 1.00 | 80.8 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.16 | 8.94 | 14.76 | 2.00 | 79.5 | 90.0 |
| Bench 3 | Bench | Harry Maguire | DEF | 14 | 4.2 | 2.11 | 7.24 | 11.99 | 1.00 | 73.4 | 90.0 |
| Bench 4 | Bench | Jonny Evans | DEF | 14 | 4.0 | 0.55 | 2.70 | 4.87 | 0.00 | 24.9 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.69 | 23.60 | 38.48 | 7.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.32 | 13.28 | 22.46 | 11.00 | 70.9 | 90.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.78 | 7.33 | 12.31 | 1.00 | 73.4 | 45.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.7 | 6.47 | 17.66 | 27.93 | 8.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 5.88 | 16.79 | 26.06 | 5.00 | 90.0 | 77.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 3.74 | 12.59 | 21.28 | 2.00 | 84.3 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 3.69 | 12.50 | 22.12 | 10.00 | 78.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 3.19 | 10.76 | 16.83 | 1.00 | 58.9 | 24.0 |

## GW15

- Train rows: 114034
- Bank: 0.60 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 64.65
- Actual score: 39.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (4.90) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Cole Palmer -> Hwang Hee-chan (projected gain 3.25, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (4.90) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 2.94 | 8.69 | 14.51 | 0.00 | 88.3 | 0.0 |
| Bench 1 | Bench Boost | Loris Karius | GK | 15 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.34 | 14.74 | 24.18 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.54 | 12.69 | 19.70 | 1.00 | 80.3 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.64 | 9.58 | 15.85 | 1.00 | 82.1 | 90.0 |
| Bench 2 | Bench Boost | Harry Maguire | DEF | 14 | 4.2 | 2.58 | 7.85 | 13.03 | 5.00 | 76.3 | 90.0 |
| Bench 4 | Bench Boost | Jonny Evans | DEF | 14 | 4.0 | 0.37 | 1.47 | 2.86 | 1.00 | 12.9 | 1.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.92 | 24.06 | 39.37 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.24 | 13.49 | 23.65 | 1.00 | 83.8 | 89.0 |
| Bench 3 | Bench Boost | Cameron Archer | FWD | 17 | 4.6 | 1.95 | 6.17 | 10.30 | 2.00 | 59.7 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.7 | 6.52 | 17.95 | 28.46 | 5.00 | 90.0 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 5.33 | 15.75 | 26.46 | 2.00 | 87.4 | 87.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 3.95 | 11.97 | 20.38 | 0.00 | 83.9 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 3.59 | 11.63 | 19.26 | 6.00 | 64.5 | 39.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.6 | 3.82 | 11.05 | 17.63 | 10.00 | 82.0 | 90.0 |