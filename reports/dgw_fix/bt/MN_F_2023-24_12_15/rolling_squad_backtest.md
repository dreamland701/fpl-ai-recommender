# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 266.74
- Total actual points: 230.00
- Average predicted points: 66.69
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
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Erling Haaland
- Vice captain: Kieran Trippier
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 65.62
- Actual score: 69.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.88 | 10.57 | 16.88 | 2.00 | 92.0 | 90.0 |
| Bench 1 | Bench | Joseph Anang | GK | 19 | 4.0 | 0.21 | 0.21 | 0.28 | 0.00 | 2.3 | 0.0 |
| Vice Captain | XI | Kieran Trippier | DEF | 15 | 7.0 | 6.37 | 16.95 | 26.88 | 1.00 | 96.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.49 | 11.58 | 18.15 | 9.00 | 92.0 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.89 | 11.28 | 18.05 | 1.00 | 89.7 | 90.0 |
| Bench 2 | Bench | Jamaal Lascelles | DEF | 15 | 4.1 | 3.01 | 7.52 | 11.62 | 0.00 | 71.4 | 90.0 |
| Bench 4 | Bench | Jarrad Branthwaite | DEF | 9 | 4.0 | 2.37 | 6.81 | 11.11 | 1.00 | 73.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.14 | 22.36 | 36.37 | 16.00 | 97.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 5.93 | 17.35 | 27.54 | 6.00 | 89.2 | 90.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.79 | 7.83 | 13.07 | 2.00 | 69.6 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 5.73 | 16.87 | 27.95 | 2.00 | 91.2 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.6 | 5.98 | 15.93 | 25.98 | 5.00 | 87.8 | 80.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.6 | 5.83 | 15.81 | 24.64 | 8.00 | 106.2 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 5.02 | 13.38 | 20.86 | 1.00 | 85.6 | 45.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 4.22 | 13.08 | 21.72 | 2.00 | 88.7 | 90.0 |

## GW13

- Train rows: 112534
- Bank: 0.00 -> 1.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 63.99
- Actual score: 46.00
- Transfer: Kaoru Mitoma -> Cole Palmer (projected gain 4.75, hit 0)
- Autosub: Cameron Archer replaced Jarrod Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.89 | 10.59 | 16.78 | 3.00 | 91.9 | 90.0 |
| Bench 1 | Bench | Joseph Anang | GK | 19 | 4.0 | 0.00 | 0.00 | 0.15 | 0.00 | 1.6 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.91 | 14.42 | 23.49 | 1.00 | 88.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.82 | 13.04 | 19.97 | 6.00 | 98.3 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.93 | 11.14 | 17.76 | 1.00 | 91.1 | 90.0 |
| Bench 3 | Bench | Jarrad Branthwaite | DEF | 9 | 4.0 | 2.23 | 6.82 | 11.12 | 1.00 | 74.8 | 90.0 |
| Bench 4 | Bench | Jamaal Lascelles | DEF | 15 | 4.1 | 2.09 | 6.05 | 9.76 | 7.00 | 64.8 | 85.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 8.55 | 24.56 | 40.20 | 7.00 | 120.5 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.95 | 15.76 | 24.18 | 5.00 | 81.3 | 90.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 4.6 | 2.91 | 7.83 | 12.83 | 2.00 | 68.6 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.6 | 6.07 | 16.96 | 26.86 | 8.00 | 94.6 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 4.89 | 14.80 | 24.58 | 2.00 | 84.5 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 4.61 | 13.75 | 22.00 | 2.00 | 89.2 | 90.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.6 | 4.59 | 12.97 | 20.80 | 0.00 | 74.5 | 0.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 4.23 | 12.48 | 19.83 | 2.00 | 91.7 | 74.0 |

## GW14

- Train rows: 113281
- Bank: 1.30 -> 0.60
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 68.88
- Actual score: 75.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.25) beats the best remaining Triple Captain opportunity (8.99).
- Transfer: Jarrod Bowen -> Bruno Borges Fernandes (projected gain 4.83, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.25) beats the best remaining Triple Captain opportunity (8.99).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.74 | 10.14 | 16.22 | 2.00 | 89.5 | 90.0 |
| Bench 1 | Bench | Joseph Anang | GK | 19 | 4.0 | 0.06 | 0.00 | 0.07 | 0.00 | 0.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.65 | 13.69 | 22.64 | 12.00 | 87.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.41 | 11.88 | 18.55 | 1.00 | 85.3 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.20 | 9.64 | 15.65 | 2.00 | 78.0 | 90.0 |
| Bench 3 | Bench | Jamaal Lascelles | DEF | 15 | 4.1 | 2.40 | 6.92 | 11.34 | 6.00 | 73.2 | 90.0 |
| Bench 4 | Bench | Jarrad Branthwaite | DEF | 9 | 4.0 | 2.29 | 6.55 | 10.65 | 9.00 | 75.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 8.25 | 24.78 | 40.77 | 7.00 | 105.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.56 | 13.87 | 23.15 | 11.00 | 67.0 | 90.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.90 | 7.98 | 13.12 | 1.00 | 71.7 | 45.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.7 | 6.47 | 17.60 | 28.02 | 8.00 | 99.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 6.30 | 16.54 | 25.95 | 5.00 | 100.1 | 77.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 3.55 | 12.91 | 22.39 | 10.00 | 70.7 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 3.80 | 12.71 | 21.33 | 2.00 | 84.9 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 3.44 | 10.35 | 16.54 | 1.00 | 64.2 | 24.0 |

## GW15

- Train rows: 114034
- Bank: 0.60 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 68.26
- Actual score: 40.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.29) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Cole Palmer -> Hwang Hee-chan (projected gain 2.57, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.29) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.20 | 9.49 | 15.41 | 0.00 | 87.3 | 0.0 |
| Bench 1 | Bench Boost | Joseph Anang | GK | 19 | 4.0 | 0.00 | 0.00 | 0.00 | 0.00 | 0.4 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.47 | 15.31 | 24.83 | 1.00 | 98.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.17 | 11.59 | 18.47 | 1.00 | 84.5 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.63 | 9.89 | 16.27 | 1.00 | 82.1 | 90.0 |
| Bench 2 | Bench Boost | Jamaal Lascelles | DEF | 15 | 4.1 | 2.96 | 8.13 | 12.84 | 1.00 | 78.7 | 89.0 |
| Bench 4 | Bench Boost | Jarrad Branthwaite | DEF | 9 | 4.0 | 2.16 | 6.22 | 10.48 | 6.00 | 75.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 8.15 | 24.64 | 40.36 | 2.00 | 109.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.49 | 14.34 | 24.26 | 1.00 | 77.8 | 89.0 |
| Bench 3 | Bench Boost | Cameron Archer | FWD | 17 | 4.6 | 2.17 | 6.68 | 10.90 | 2.00 | 59.6 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.7 | 6.41 | 17.63 | 28.32 | 5.00 | 96.1 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 5.43 | 15.47 | 26.20 | 2.00 | 90.7 | 87.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 4.12 | 12.44 | 20.86 | 0.00 | 82.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 3.90 | 12.30 | 19.77 | 6.00 | 60.7 | 39.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.6 | 3.84 | 10.62 | 17.14 | 10.00 | 84.5 | 90.0 |