# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 261.10
- Total actual points: 230.00
- Average predicted points: 65.28
- Average actual points: 57.50
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
- Predicted score: 64.18
- Actual score: 69.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.92 | 10.61 | 16.92 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Jordan Amissah | GK | 17 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 3.7 | 0.0 |
| Vice Captain | XI | Kieran Trippier | DEF | 15 | 7.0 | 6.09 | 16.54 | 26.31 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.45 | 11.72 | 18.32 | 9.00 | 88.5 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.83 | 11.23 | 17.96 | 1.00 | 88.2 | 90.0 |
| Bench 2 | Bench | Jamaal Lascelles | DEF | 15 | 4.1 | 2.83 | 7.36 | 11.40 | 0.00 | 69.9 | 90.0 |
| Bench 4 | Bench | Jarrad Branthwaite | DEF | 9 | 4.0 | 2.35 | 6.76 | 11.04 | 1.00 | 72.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.14 | 22.16 | 36.06 | 16.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 5.66 | 17.11 | 27.18 | 6.00 | 86.9 | 90.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.80 | 7.71 | 12.89 | 2.00 | 70.8 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 5.58 | 16.72 | 27.74 | 2.00 | 89.6 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.6 | 6.08 | 15.96 | 26.01 | 5.00 | 86.4 | 80.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.6 | 5.47 | 15.85 | 24.67 | 8.00 | 90.0 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 4.99 | 13.63 | 21.20 | 1.00 | 81.8 | 45.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 3.84 | 13.06 | 21.70 | 2.00 | 82.8 | 90.0 |

## GW13

- Train rows: 112534
- Bank: 0.10 -> 1.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 61.51
- Actual score: 46.00
- Transfer: Kaoru Mitoma -> Cole Palmer (projected gain 5.08, hit 0)
- Autosub: Cameron Archer replaced Jarrod Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.90 | 10.56 | 16.73 | 3.00 | 89.5 | 90.0 |
| Bench 1 | Bench | Jordan Amissah | GK | 17 | 3.9 | 0.02 | 0.00 | 0.00 | 0.00 | 2.2 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.85 | 14.17 | 23.16 | 1.00 | 88.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.54 | 13.06 | 19.97 | 6.00 | 90.0 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.88 | 11.24 | 17.86 | 1.00 | 87.7 | 90.0 |
| Bench 3 | Bench | Jarrad Branthwaite | DEF | 9 | 4.0 | 2.16 | 6.76 | 11.06 | 1.00 | 73.6 | 90.0 |
| Bench 4 | Bench | Jamaal Lascelles | DEF | 15 | 4.1 | 2.02 | 6.03 | 9.74 | 7.00 | 63.6 | 85.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 8.20 | 24.47 | 40.08 | 7.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.74 | 15.69 | 24.09 | 5.00 | 79.1 | 90.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 4.6 | 2.93 | 7.68 | 12.63 | 2.00 | 69.7 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.6 | 5.84 | 16.79 | 26.60 | 8.00 | 88.3 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 4.86 | 14.69 | 24.47 | 2.00 | 84.8 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 4.25 | 13.82 | 22.10 | 2.00 | 83.1 | 90.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.6 | 4.49 | 12.92 | 20.71 | 0.00 | 73.8 | 0.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 3.76 | 12.66 | 20.08 | 2.00 | 85.0 | 74.0 |

## GW14

- Train rows: 113281
- Bank: 1.40 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 68.06
- Actual score: 75.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.18) beats the best remaining Triple Captain opportunity (8.91).
- Transfer: Jarrod Bowen -> Bruno Borges Fernandes (projected gain 5.00, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.18) beats the best remaining Triple Captain opportunity (8.91).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.79 | 10.15 | 16.21 | 2.00 | 88.0 | 90.0 |
| Bench 1 | Bench | Jordan Amissah | GK | 17 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 1.6 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.59 | 13.50 | 22.39 | 12.00 | 86.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.35 | 12.11 | 18.84 | 1.00 | 81.9 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.24 | 9.55 | 15.52 | 2.00 | 77.2 | 90.0 |
| Bench 4 | Bench | Jamaal Lascelles | DEF | 15 | 4.1 | 2.28 | 6.96 | 11.41 | 6.00 | 70.9 | 90.0 |
| Bench 3 | Bench | Jarrad Branthwaite | DEF | 9 | 4.0 | 2.31 | 6.64 | 10.75 | 9.00 | 73.6 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 8.18 | 24.75 | 40.76 | 7.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.49 | 13.59 | 22.79 | 11.00 | 70.3 | 90.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.86 | 7.79 | 12.87 | 1.00 | 71.6 | 45.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.7 | 6.37 | 17.65 | 28.05 | 8.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 5.84 | 16.72 | 26.17 | 5.00 | 90.0 | 77.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 3.88 | 12.97 | 22.44 | 10.00 | 75.3 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 3.78 | 12.71 | 21.34 | 2.00 | 83.1 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 3.17 | 10.55 | 16.81 | 1.00 | 61.0 | 24.0 |

## GW15

- Train rows: 114034
- Bank: 0.70 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 67.36
- Actual score: 40.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.18) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Cole Palmer -> Hwang Hee-chan (projected gain 2.60, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.18) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.23 | 9.39 | 15.31 | 0.00 | 86.6 | 0.0 |
| Bench 1 | Bench Boost | Jordan Amissah | GK | 17 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 1.2 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.34 | 15.10 | 24.54 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.27 | 11.96 | 18.94 | 1.00 | 82.0 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.61 | 9.75 | 16.08 | 1.00 | 81.0 | 90.0 |
| Bench 2 | Bench Boost | Jamaal Lascelles | DEF | 15 | 4.1 | 2.84 | 8.13 | 12.85 | 1.00 | 76.2 | 89.0 |
| Bench 4 | Bench Boost | Jarrad Branthwaite | DEF | 9 | 4.0 | 2.17 | 6.20 | 10.47 | 6.00 | 75.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 8.09 | 24.70 | 40.42 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.33 | 14.16 | 24.01 | 1.00 | 78.2 | 89.0 |
| Bench 3 | Bench Boost | Cameron Archer | FWD | 17 | 4.6 | 2.17 | 6.69 | 10.88 | 2.00 | 58.3 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.7 | 6.38 | 17.86 | 28.60 | 5.00 | 90.0 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 5.38 | 15.46 | 26.20 | 2.00 | 89.4 | 87.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 4.06 | 12.26 | 20.64 | 0.00 | 82.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 3.71 | 12.09 | 19.51 | 6.00 | 60.7 | 39.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.6 | 3.68 | 10.66 | 17.17 | 10.00 | 82.7 | 90.0 |