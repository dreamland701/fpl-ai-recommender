# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 261.16
- Total actual points: 225.00
- Average predicted points: 65.29
- Average actual points: 56.25
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
- Predicted score: 64.01
- Actual score: 69.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.83 | 10.32 | 16.46 | 2.00 | 88.6 | 90.0 |
| Bench 1 | Bench | Zack Steffen | GK | 13 | 3.9 | 0.03 | 0.44 | 0.87 | 0.00 | 4.7 | 0.0 |
| Vice Captain | XI | Kieran Trippier | DEF | 15 | 7.0 | 6.22 | 16.90 | 26.79 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.35 | 11.54 | 18.08 | 9.00 | 88.6 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.84 | 11.29 | 18.04 | 1.00 | 88.5 | 90.0 |
| Bench 2 | Bench | Jamaal Lascelles | DEF | 15 | 4.1 | 2.93 | 7.65 | 11.85 | 0.00 | 70.5 | 90.0 |
| Bench 4 | Bench | Charlie Taylor | DEF | 6 | 4.0 | 1.92 | 6.51 | 10.91 | 1.00 | 76.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.28 | 22.33 | 36.21 | 16.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 5.75 | 17.31 | 27.45 | 6.00 | 86.3 | 90.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.89 | 7.92 | 13.19 | 2.00 | 71.5 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 5.69 | 16.98 | 28.13 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.6 | 5.47 | 15.88 | 24.81 | 8.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.6 | 5.52 | 15.30 | 25.40 | 5.00 | 75.1 | 80.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 4.90 | 13.34 | 20.75 | 1.00 | 82.0 | 45.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 3.87 | 13.16 | 21.86 | 2.00 | 83.4 | 90.0 |

## GW13

- Train rows: 112534
- Bank: 0.10 -> 1.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 60.23
- Actual score: 46.00
- Transfer: Kaoru Mitoma -> Cole Palmer (projected gain 4.63, hit 0)
- Autosub: Cameron Archer replaced Jarrod Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.81 | 10.32 | 16.34 | 3.00 | 87.3 | 90.0 |
| Bench 1 | Bench | Zack Steffen | GK | 13 | 3.9 | 0.00 | 0.34 | 0.72 | 0.00 | 3.5 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.92 | 14.34 | 23.38 | 1.00 | 87.3 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.47 | 12.91 | 19.79 | 6.00 | 90.0 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.84 | 11.15 | 17.76 | 1.00 | 88.2 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 4.0 | 2.79 | 7.59 | 12.43 | 1.00 | 80.5 | 90.0 |
| Bench 4 | Bench | Jamaal Lascelles | DEF | 15 | 4.1 | 2.07 | 6.17 | 9.93 | 7.00 | 64.4 | 85.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.77 | 23.85 | 39.43 | 7.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.83 | 15.89 | 24.39 | 5.00 | 80.1 | 90.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 4.6 | 2.98 | 7.80 | 12.74 | 2.00 | 69.5 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.6 | 5.89 | 16.97 | 26.89 | 8.00 | 88.2 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 4.99 | 14.90 | 24.68 | 2.00 | 85.8 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 4.22 | 13.86 | 22.22 | 2.00 | 83.8 | 90.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.6 | 4.12 | 12.59 | 20.59 | 0.00 | 65.4 | 0.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 3.60 | 12.36 | 19.72 | 2.00 | 83.5 | 74.0 |

## GW14

- Train rows: 113281
- Bank: 1.40 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 68.31
- Actual score: 75.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.18) beats the best remaining Triple Captain opportunity (8.92).
- Transfer: Jarrod Bowen -> Bruno Borges Fernandes (projected gain 5.07, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.18) beats the best remaining Triple Captain opportunity (8.92).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.70 | 9.89 | 15.82 | 2.00 | 86.2 | 90.0 |
| Bench 1 | Bench | Zack Steffen | GK | 13 | 3.9 | 0.09 | 0.41 | 0.68 | 0.00 | 2.3 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.68 | 13.65 | 22.58 | 12.00 | 86.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.26 | 11.88 | 18.54 | 1.00 | 82.5 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.30 | 9.68 | 15.65 | 2.00 | 78.0 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 4.0 | 2.82 | 7.60 | 12.32 | 10.00 | 80.3 | 90.0 |
| Bench 4 | Bench | Jamaal Lascelles | DEF | 15 | 4.1 | 2.31 | 6.99 | 11.43 | 6.00 | 71.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 8.18 | 24.63 | 40.47 | 7.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.77 | 14.15 | 23.53 | 11.00 | 73.2 | 90.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.93 | 7.95 | 13.04 | 1.00 | 71.5 | 45.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.7 | 6.27 | 17.49 | 27.91 | 8.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 5.71 | 16.51 | 26.02 | 5.00 | 90.0 | 77.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 4.00 | 13.15 | 22.65 | 10.00 | 78.4 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 3.92 | 12.96 | 21.65 | 2.00 | 86.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 3.16 | 10.48 | 16.74 | 1.00 | 62.4 | 24.0 |

## GW15

- Train rows: 114034
- Bank: 0.70 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 68.62
- Actual score: 35.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.03) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Cole Palmer -> Hwang Hee-chan (projected gain 2.50, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.03) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.22 | 9.30 | 15.09 | 0.00 | 85.1 | 0.0 |
| Bench 1 | Bench Boost | Zack Steffen | GK | 13 | 3.9 | 0.00 | 0.20 | 0.57 | 0.00 | 3.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.36 | 15.17 | 24.64 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.11 | 11.54 | 18.36 | 1.00 | 82.6 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.70 | 9.93 | 16.29 | 1.00 | 81.8 | 90.0 |
| Bench 2 | Bench Boost | Jamaal Lascelles | DEF | 15 | 4.1 | 2.91 | 8.27 | 13.05 | 1.00 | 77.6 | 89.0 |
| Bench 3 | Bench Boost | Charlie Taylor | DEF | 6 | 4.0 | 2.89 | 8.00 | 13.02 | 1.00 | 81.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 8.03 | 24.44 | 40.02 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.59 | 14.71 | 24.72 | 1.00 | 82.6 | 89.0 |
| Bench 4 | Bench Boost | Cameron Archer | FWD | 17 | 4.6 | 2.23 | 6.74 | 10.93 | 2.00 | 59.5 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.7 | 6.18 | 17.50 | 28.19 | 5.00 | 89.4 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 5.57 | 15.77 | 26.56 | 2.00 | 90.0 | 87.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 4.25 | 12.67 | 21.18 | 0.00 | 84.8 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 3.84 | 12.39 | 19.88 | 6.00 | 61.4 | 39.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.6 | 3.71 | 10.72 | 17.29 | 10.00 | 83.8 | 90.0 |