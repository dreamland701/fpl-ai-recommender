# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 261.55
- Total actual points: 237.00
- Average predicted points: 65.39
- Average actual points: 59.25
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
- Captain: Erling Haaland
- Vice captain: Kieran Trippier
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 64.00
- Actual score: 69.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.83 | 10.31 | 16.46 | 2.00 | 88.4 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.30 | 0.82 | 1.33 | 0.00 | 8.1 | 0.0 |
| Vice Captain | XI | Kieran Trippier | DEF | 15 | 7.0 | 6.20 | 16.88 | 26.81 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.35 | 11.54 | 18.09 | 9.00 | 88.6 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.83 | 11.28 | 18.03 | 1.00 | 88.4 | 90.0 |
| Bench 2 | Bench | Jamaal Lascelles | DEF | 15 | 4.1 | 2.95 | 7.65 | 11.82 | 0.00 | 70.7 | 90.0 |
| Bench 4 | Bench | Jarrad Branthwaite | DEF | 9 | 4.0 | 1.95 | 6.60 | 11.20 | 1.00 | 64.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.26 | 22.30 | 36.22 | 16.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 5.74 | 17.29 | 27.45 | 6.00 | 86.1 | 90.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.89 | 7.92 | 13.19 | 2.00 | 71.5 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 5.69 | 16.98 | 28.13 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.6 | 5.49 | 15.90 | 24.81 | 8.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.6 | 5.57 | 15.61 | 25.92 | 5.00 | 76.6 | 80.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 4.88 | 13.33 | 20.77 | 1.00 | 81.6 | 45.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 3.89 | 13.15 | 21.81 | 2.00 | 83.6 | 90.0 |

## GW13

- Train rows: 112534
- Bank: 0.10 -> 1.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 60.40
- Actual score: 46.00
- Transfer: Kaoru Mitoma -> Cole Palmer (projected gain 4.69, hit 0)
- Autosub: Cameron Archer replaced Jarrod Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.80 | 10.31 | 16.34 | 3.00 | 87.2 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.19 | 0.73 | 1.28 | 0.00 | 7.9 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.92 | 14.33 | 23.38 | 1.00 | 87.3 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.48 | 12.92 | 19.78 | 6.00 | 90.0 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.84 | 11.14 | 17.75 | 1.00 | 88.1 | 90.0 |
| Bench 3 | Bench | Jarrad Branthwaite | DEF | 9 | 4.0 | 2.23 | 6.89 | 11.22 | 1.00 | 74.5 | 90.0 |
| Bench 4 | Bench | Jamaal Lascelles | DEF | 15 | 4.1 | 2.07 | 6.16 | 9.91 | 7.00 | 64.4 | 85.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.82 | 24.14 | 39.92 | 7.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.84 | 15.88 | 24.37 | 5.00 | 80.4 | 90.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 4.6 | 2.97 | 7.79 | 12.75 | 2.00 | 69.2 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.6 | 5.89 | 16.97 | 26.89 | 8.00 | 88.2 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 4.97 | 14.88 | 24.68 | 2.00 | 85.5 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 4.23 | 13.86 | 22.19 | 2.00 | 84.0 | 90.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.6 | 4.17 | 12.89 | 21.08 | 0.00 | 66.8 | 0.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 3.62 | 12.38 | 19.69 | 2.00 | 84.1 | 74.0 |

## GW14

- Train rows: 113281
- Bank: 1.40 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 68.21
- Actual score: 75.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.17) beats the best remaining Triple Captain opportunity (8.90).
- Transfer: Jarrod Bowen -> Bruno Borges Fernandes (projected gain 5.10, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.17) beats the best remaining Triple Captain opportunity (8.90).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.69 | 9.88 | 15.81 | 2.00 | 86.0 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.00 | 0.32 | 0.77 | 8.00 | 7.6 | 67.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.67 | 13.64 | 22.57 | 12.00 | 85.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.26 | 11.87 | 18.52 | 1.00 | 82.4 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.29 | 9.66 | 15.65 | 2.00 | 77.6 | 90.0 |
| Bench 4 | Bench | Jamaal Lascelles | DEF | 15 | 4.1 | 2.31 | 6.97 | 11.40 | 6.00 | 71.5 | 90.0 |
| Bench 3 | Bench | Jarrad Branthwaite | DEF | 9 | 4.0 | 2.34 | 6.71 | 10.87 | 9.00 | 75.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 8.17 | 24.62 | 40.50 | 7.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.75 | 14.11 | 23.50 | 11.00 | 72.8 | 90.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.92 | 7.94 | 13.03 | 1.00 | 71.3 | 45.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.7 | 6.29 | 17.51 | 27.89 | 8.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 5.74 | 16.53 | 25.98 | 5.00 | 90.0 | 77.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 3.96 | 13.12 | 22.69 | 10.00 | 77.5 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 3.90 | 12.95 | 21.66 | 2.00 | 85.6 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 3.16 | 10.47 | 16.71 | 1.00 | 62.5 | 24.0 |

## GW15

- Train rows: 114034
- Bank: 0.70 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 68.93
- Actual score: 47.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.49) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Cole Palmer -> Hwang Hee-chan (projected gain 2.53, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.49) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.21 | 9.29 | 15.08 | 0.00 | 84.9 | 0.0 |
| Bench 1 | Bench Boost | Daniel Bentley | GK | 20 | 3.9 | 1.13 | 2.70 | 4.57 | 7.00 | 31.2 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.36 | 15.16 | 24.63 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.10 | 11.52 | 18.34 | 1.00 | 82.3 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.68 | 9.91 | 16.29 | 1.00 | 81.4 | 90.0 |
| Bench 2 | Bench Boost | Jamaal Lascelles | DEF | 15 | 4.1 | 2.91 | 8.26 | 13.03 | 1.00 | 77.6 | 89.0 |
| Bench 3 | Bench Boost | Jarrad Branthwaite | DEF | 9 | 4.0 | 2.24 | 6.30 | 10.59 | 6.00 | 76.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 8.03 | 24.43 | 39.99 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.53 | 14.67 | 24.77 | 1.00 | 81.4 | 89.0 |
| Bench 4 | Bench Boost | Cameron Archer | FWD | 17 | 4.6 | 2.21 | 6.72 | 10.93 | 2.00 | 59.1 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.7 | 6.21 | 17.51 | 28.15 | 5.00 | 90.0 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 5.53 | 15.74 | 26.61 | 2.00 | 90.0 | 87.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 4.24 | 12.67 | 21.21 | 0.00 | 84.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 3.83 | 12.37 | 19.86 | 6.00 | 61.2 | 39.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.6 | 3.70 | 10.71 | 17.28 | 10.00 | 83.6 | 90.0 |