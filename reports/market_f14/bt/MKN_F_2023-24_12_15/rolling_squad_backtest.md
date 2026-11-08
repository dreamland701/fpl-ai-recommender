# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 256.42
- Total actual points: 222.00
- Average predicted points: 64.10
- Average actual points: 55.50
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
- Captain: Bukayo Saka
- Vice captain: Erling Haaland
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 63.40
- Actual score: 62.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 4.04 | 10.77 | 17.09 | 2.00 | 93.6 | 90.0 |
| Bench 1 | Bench | Tom McGill | GK | 5 | 3.9 | 0.04 | 0.09 | 0.36 | 0.00 | 0.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.08 | 15.56 | 25.31 | 1.00 | 81.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 5.07 | 12.20 | 18.85 | 9.00 | 97.6 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.81 | 11.09 | 17.73 | 1.00 | 85.8 | 90.0 |
| XI | XI | Harry Maguire | DEF | 14 | 4.2 | 3.70 | 8.21 | 12.70 | 6.00 | 87.8 | 90.0 |
| Bench 2 | Bench | Jonny Evans | DEF | 14 | 4.0 | 3.43 | 7.59 | 11.85 | 0.00 | 81.7 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.0 | 6.37 | 21.34 | 35.05 | 16.00 | 84.4 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 5.78 | 16.92 | 26.82 | 6.00 | 87.3 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.21 | 7.21 | 12.37 | 2.00 | 63.2 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 5.28 | 16.43 | 27.46 | 2.00 | 86.5 | 90.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 8.6 | 6.43 | 16.12 | 25.98 | 5.00 | 89.7 | 80.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.6 | 5.77 | 15.71 | 24.45 | 8.00 | 103.7 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 5.62 | 14.04 | 21.60 | 1.00 | 92.5 | 45.0 |
| Bench 3 | Bench | Bryan Mbeumo | MID | 4 | 6.8 | 3.30 | 12.68 | 21.72 | 2.00 | 81.7 | 90.0 |

## GW13

- Train rows: 112534
- Bank: 0.00 -> 1.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 59.97
- Actual score: 46.00
- Transfer: Kaoru Mitoma -> Cole Palmer (projected gain 5.03, hit 0)
- Autosub: Cameron Archer replaced Jarrod Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.83 | 10.44 | 16.55 | 3.00 | 89.5 | 90.0 |
| Bench 1 | Bench | Tom McGill | GK | 5 | 3.9 | 0.06 | 0.12 | 0.31 | 0.00 | 1.5 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.16 | 13.63 | 22.64 | 1.00 | 81.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.74 | 12.95 | 19.85 | 6.00 | 95.7 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.98 | 11.13 | 17.67 | 1.00 | 87.6 | 90.0 |
| Bench 3 | Bench | Harry Maguire | DEF | 14 | 4.2 | 2.43 | 6.83 | 11.01 | 6.00 | 72.4 | 90.0 |
| Bench 4 | Bench | Jonny Evans | DEF | 14 | 4.0 | 1.03 | 2.95 | 5.38 | 0.00 | 36.1 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 8.49 | 23.96 | 39.06 | 7.00 | 116.2 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.18 | 15.05 | 23.47 | 5.00 | 72.5 | 90.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 4.6 | 2.66 | 7.50 | 12.44 | 2.00 | 66.3 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.6 | 5.56 | 16.29 | 25.99 | 8.00 | 86.3 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 4.62 | 14.57 | 24.40 | 2.00 | 84.1 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 3.87 | 13.62 | 22.41 | 2.00 | 82.8 | 90.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.6 | 4.13 | 12.57 | 20.40 | 0.00 | 67.7 | 0.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 3.93 | 12.46 | 20.02 | 2.00 | 87.7 | 74.0 |

## GW14

- Train rows: 113281
- Bank: 1.30 -> 0.60
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 69.43
- Actual score: 75.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.47) beats the best remaining Triple Captain opportunity (9.23).
- Transfer: Jarrod Bowen -> Bruno Borges Fernandes (projected gain 5.32, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.47) beats the best remaining Triple Captain opportunity (9.23).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.88 | 10.23 | 16.27 | 2.00 | 89.4 | 90.0 |
| Bench 1 | Bench | Tom McGill | GK | 5 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 5.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.47 | 13.43 | 22.32 | 12.00 | 87.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 5.07 | 12.59 | 19.33 | 1.00 | 91.4 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 2.66 | 8.94 | 14.76 | 2.00 | 68.7 | 90.0 |
| Bench 3 | Bench | Harry Maguire | DEF | 14 | 4.2 | 2.13 | 7.24 | 11.99 | 1.00 | 72.7 | 90.0 |
| Bench 4 | Bench | Jonny Evans | DEF | 14 | 4.0 | 0.62 | 2.70 | 4.87 | 0.00 | 26.0 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 8.47 | 23.60 | 38.48 | 7.00 | 96.3 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.10 | 13.28 | 22.46 | 11.00 | 64.5 | 90.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.40 | 7.33 | 12.31 | 1.00 | 64.8 | 45.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.7 | 6.70 | 17.66 | 27.93 | 8.00 | 98.5 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 6.69 | 16.79 | 26.06 | 5.00 | 101.5 | 77.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 3.58 | 12.59 | 21.28 | 2.00 | 82.8 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 2.88 | 12.50 | 22.12 | 10.00 | 64.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 4.00 | 10.76 | 16.83 | 1.00 | 68.4 | 24.0 |

## GW15

- Train rows: 114034
- Bank: 0.60 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 63.61
- Actual score: 39.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (4.68) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Cole Palmer -> Hwang Hee-chan (projected gain 3.21, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (4.68) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 2.48 | 8.69 | 14.51 | 0.00 | 78.7 | 0.0 |
| Bench 1 | Bench Boost | Tom McGill | GK | 5 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.99 | 14.74 | 24.18 | 1.00 | 92.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 5.17 | 12.69 | 19.70 | 1.00 | 93.8 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.44 | 9.58 | 15.85 | 1.00 | 78.9 | 90.0 |
| Bench 2 | Bench Boost | Harry Maguire | DEF | 14 | 4.2 | 2.62 | 7.85 | 13.03 | 5.00 | 76.2 | 90.0 |
| Bench 4 | Bench Boost | Jonny Evans | DEF | 14 | 4.0 | 0.40 | 1.47 | 2.86 | 1.00 | 13.4 | 1.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.99 | 24.06 | 39.37 | 2.00 | 101.3 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 3.28 | 13.49 | 23.65 | 1.00 | 66.1 | 89.0 |
| Bench 3 | Bench Boost | Cameron Archer | FWD | 17 | 4.6 | 1.66 | 6.17 | 10.30 | 2.00 | 53.2 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.7 | 6.96 | 17.95 | 28.46 | 5.00 | 96.8 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 5.77 | 15.75 | 26.46 | 2.00 | 96.7 | 87.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 3.67 | 11.97 | 20.38 | 0.00 | 78.7 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 2.99 | 11.63 | 19.26 | 6.00 | 53.1 | 39.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.6 | 4.22 | 11.05 | 17.63 | 10.00 | 89.4 | 90.0 |