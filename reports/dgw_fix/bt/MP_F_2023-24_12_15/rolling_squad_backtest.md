# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 261.66
- Total actual points: 230.00
- Average predicted points: 65.42
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
- Predicted score: 64.40
- Actual score: 69.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.92 | 10.69 | 17.17 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Jordan Amissah | GK | 17 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 3.3 | 0.0 |
| Vice Captain | XI | Kieran Trippier | DEF | 15 | 7.0 | 6.24 | 16.51 | 26.36 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.35 | 11.38 | 17.82 | 9.00 | 88.7 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.83 | 11.10 | 17.72 | 1.00 | 88.2 | 90.0 |
| Bench 2 | Bench | Jamaal Lascelles | DEF | 15 | 4.1 | 2.90 | 7.01 | 10.61 | 0.00 | 69.6 | 90.0 |
| Bench 4 | Bench | Jarrad Branthwaite | DEF | 9 | 4.0 | 2.35 | 6.70 | 10.79 | 1.00 | 72.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.22 | 22.48 | 37.42 | 16.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 5.76 | 17.00 | 27.13 | 6.00 | 86.5 | 90.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.84 | 7.68 | 12.78 | 2.00 | 70.4 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 5.65 | 16.76 | 27.92 | 2.00 | 89.3 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.6 | 6.02 | 16.28 | 26.49 | 5.00 | 86.4 | 80.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.6 | 5.46 | 15.09 | 23.87 | 8.00 | 90.0 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 4.90 | 12.68 | 20.09 | 1.00 | 82.0 | 45.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 3.84 | 12.23 | 20.02 | 2.00 | 82.7 | 90.0 |

## GW13

- Train rows: 112534
- Bank: 0.10 -> 1.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 61.74
- Actual score: 46.00
- Transfer: Kaoru Mitoma -> Cole Palmer (projected gain 3.56, hit 0)
- Autosub: Cameron Archer replaced Jarrod Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.91 | 10.65 | 17.15 | 3.00 | 89.5 | 90.0 |
| Bench 1 | Bench | Jordan Amissah | GK | 17 | 3.9 | 0.09 | 0.02 | 0.06 | 0.00 | 1.9 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.95 | 14.41 | 23.61 | 1.00 | 88.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.53 | 12.48 | 19.38 | 6.00 | 90.0 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.83 | 10.80 | 17.42 | 1.00 | 87.9 | 90.0 |
| Bench 3 | Bench | Jarrad Branthwaite | DEF | 9 | 4.0 | 2.19 | 6.69 | 10.85 | 1.00 | 73.5 | 90.0 |
| Bench 4 | Bench | Jamaal Lascelles | DEF | 15 | 4.1 | 2.03 | 5.61 | 8.62 | 7.00 | 63.6 | 85.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 8.27 | 24.38 | 40.19 | 7.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.78 | 14.54 | 23.18 | 5.00 | 78.9 | 90.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 4.6 | 2.98 | 7.81 | 12.65 | 2.00 | 69.5 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.6 | 5.89 | 16.53 | 26.63 | 8.00 | 88.1 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 4.93 | 14.95 | 24.73 | 2.00 | 84.5 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 4.20 | 12.99 | 21.04 | 2.00 | 83.3 | 90.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.6 | 4.49 | 12.10 | 19.29 | 0.00 | 73.8 | 0.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 3.69 | 11.27 | 17.89 | 2.00 | 85.4 | 74.0 |

## GW14

- Train rows: 113281
- Bank: 1.40 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 68.07
- Actual score: 75.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.21) beats the best remaining Triple Captain opportunity (8.95).
- Transfer: Jarrod Bowen -> Bruno Borges Fernandes (projected gain 4.56, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.21) beats the best remaining Triple Captain opportunity (8.95).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.78 | 10.33 | 16.65 | 2.00 | 88.1 | 90.0 |
| Bench 1 | Bench | Jordan Amissah | GK | 17 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 1.3 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.68 | 13.84 | 23.01 | 12.00 | 86.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.25 | 11.57 | 18.15 | 1.00 | 82.2 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.26 | 9.37 | 15.42 | 2.00 | 77.1 | 90.0 |
| Bench 3 | Bench | Jamaal Lascelles | DEF | 15 | 4.1 | 2.28 | 6.62 | 10.54 | 6.00 | 70.9 | 90.0 |
| Bench 4 | Bench | Jarrad Branthwaite | DEF | 9 | 4.0 | 2.27 | 6.30 | 10.19 | 9.00 | 73.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 8.21 | 24.90 | 33.42 | 7.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.62 | 13.39 | 22.72 | 11.00 | 69.7 | 90.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.92 | 7.84 | 12.79 | 1.00 | 71.3 | 45.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.7 | 6.33 | 17.21 | 27.32 | 8.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 5.77 | 15.99 | 20.11 | 5.00 | 90.0 | 77.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 3.86 | 13.03 | 22.27 | 10.00 | 75.2 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 3.79 | 12.30 | 20.79 | 2.00 | 83.1 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 3.11 | 9.25 | 14.96 | 1.00 | 61.3 | 24.0 |

## GW15

- Train rows: 114034
- Bank: 0.70 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 67.46
- Actual score: 40.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.19) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Cole Palmer -> Hwang Hee-chan (projected gain 2.39, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.19) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.28 | 9.76 | 15.88 | 0.00 | 86.4 | 0.0 |
| Bench 1 | Bench Boost | Jordan Amissah | GK | 17 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.9 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.42 | 15.11 | 24.70 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.10 | 11.55 | 18.46 | 1.00 | 82.5 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.65 | 9.80 | 16.00 | 1.00 | 80.9 | 90.0 |
| Bench 2 | Bench Boost | Jamaal Lascelles | DEF | 15 | 4.1 | 2.85 | 7.80 | 12.35 | 1.00 | 76.2 | 89.0 |
| Bench 3 | Bench Boost | Jarrad Branthwaite | DEF | 9 | 4.0 | 2.19 | 6.16 | 10.10 | 6.00 | 75.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 8.08 | 25.15 | 33.25 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.38 | 13.30 | 22.98 | 1.00 | 78.1 | 89.0 |
| Bench 4 | Bench Boost | Cameron Archer | FWD | 17 | 4.6 | 2.16 | 6.47 | 10.52 | 2.00 | 58.1 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.7 | 6.26 | 17.28 | 27.52 | 5.00 | 90.0 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 5.42 | 15.09 | 25.32 | 2.00 | 89.3 | 87.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 4.14 | 11.90 | 19.98 | 0.00 | 82.2 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 3.79 | 11.48 | 14.78 | 6.00 | 60.4 | 39.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.6 | 3.66 | 10.10 | 16.32 | 10.00 | 82.8 | 90.0 |