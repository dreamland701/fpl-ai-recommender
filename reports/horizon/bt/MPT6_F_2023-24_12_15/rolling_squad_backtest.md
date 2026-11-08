# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 259.66
- Total actual points: 224.00
- Average predicted points: 64.92
- Average actual points: 56.00
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
- Predicted score: 63.93
- Actual score: 69.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.83 | 10.46 | 16.80 | 2.00 | 88.5 | 90.0 |
| Bench 1 | Bench | Joseph Anang | GK | 19 | 4.0 | 0.45 | 0.85 | 1.25 | 0.00 | 7.6 | 0.0 |
| Vice Captain | XI | Kieran Trippier | DEF | 15 | 7.0 | 6.20 | 16.42 | 26.27 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.35 | 11.37 | 17.80 | 9.00 | 88.6 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.84 | 11.14 | 17.77 | 1.00 | 88.5 | 90.0 |
| Bench 2 | Bench | Jamaal Lascelles | DEF | 15 | 4.1 | 2.95 | 7.14 | 10.84 | 0.00 | 70.8 | 90.0 |
| Bench 4 | Bench | Issa Kaboré | DEF | 12 | 4.0 | 1.98 | 5.98 | 10.25 | 1.00 | 67.6 | 86.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.28 | 22.62 | 37.58 | 16.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 5.74 | 16.97 | 27.08 | 6.00 | 86.2 | 90.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.89 | 7.81 | 12.97 | 2.00 | 71.5 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 5.69 | 16.88 | 28.10 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.6 | 5.48 | 15.15 | 23.95 | 8.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.6 | 5.46 | 14.84 | 24.25 | 5.00 | 73.9 | 80.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 4.89 | 12.66 | 20.05 | 1.00 | 81.8 | 45.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 3.89 | 12.33 | 20.16 | 2.00 | 83.7 | 90.0 |

## GW13

- Train rows: 112534
- Bank: 0.00 -> 1.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 60.10
- Actual score: 46.00
- Transfer: Kaoru Mitoma -> Cole Palmer (projected gain 9.45, hit 0)
- Autosub: Cameron Archer replaced Jarrod Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.81 | 10.39 | 16.72 | 3.00 | 87.3 | 90.0 |
| Bench 1 | Bench | Joseph Anang | GK | 19 | 4.0 | 0.24 | 0.63 | 1.12 | 0.00 | 7.1 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.92 | 14.32 | 23.49 | 1.00 | 87.3 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.48 | 12.36 | 19.20 | 6.00 | 90.0 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.84 | 10.83 | 17.45 | 1.00 | 88.1 | 90.0 |
| Bench 3 | Bench | Jamaal Lascelles | DEF | 15 | 4.1 | 2.07 | 5.72 | 8.81 | 7.00 | 64.5 | 85.0 |
| Bench 4 | Bench | Issa Kaboré | DEF | 12 | 4.0 | 1.88 | 5.20 | 7.26 | 0.00 | 58.9 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.71 | 22.95 | 37.90 | 7.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.84 | 14.73 | 23.50 | 5.00 | 80.5 | 90.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 4.6 | 2.97 | 7.79 | 12.61 | 2.00 | 69.3 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.6 | 5.89 | 16.54 | 26.63 | 8.00 | 88.1 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 4.98 | 15.08 | 24.92 | 2.00 | 85.5 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 4.23 | 13.10 | 21.20 | 2.00 | 83.9 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 3.62 | 11.10 | 17.63 | 2.00 | 83.9 | 74.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.6 | 4.07 | 10.99 | 17.56 | 0.00 | 64.2 | 0.0 |

## GW14

- Train rows: 113281
- Bank: 1.30 -> 0.60
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 68.27
- Actual score: 75.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.18) beats the best remaining Triple Captain opportunity (8.91).
- Transfer: Jarrod Bowen -> Bruno Borges Fernandes (projected gain 15.01, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.18) beats the best remaining Triple Captain opportunity (8.91).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.70 | 10.10 | 16.30 | 2.00 | 86.2 | 90.0 |
| Bench 1 | Bench | Joseph Anang | GK | 19 | 4.0 | 0.31 | 0.62 | 1.06 | 0.00 | 5.7 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.67 | 13.81 | 22.98 | 12.00 | 85.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.26 | 11.61 | 18.23 | 1.00 | 82.6 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.29 | 9.44 | 15.52 | 2.00 | 77.8 | 90.0 |
| Bench 3 | Bench | Jamaal Lascelles | DEF | 15 | 4.1 | 2.31 | 6.70 | 10.68 | 6.00 | 71.6 | 90.0 |
| Bench 4 | Bench | Issa Kaboré | DEF | 12 | 4.0 | 0.72 | 2.66 | 4.04 | 1.00 | 27.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 8.18 | 24.80 | 33.29 | 7.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.77 | 13.76 | 23.31 | 11.00 | 73.1 | 90.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.92 | 7.84 | 12.78 | 1.00 | 71.4 | 45.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.7 | 6.29 | 17.08 | 27.13 | 8.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 5.73 | 15.89 | 20.01 | 5.00 | 90.0 | 77.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 3.97 | 13.30 | 22.68 | 10.00 | 77.6 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 3.90 | 12.60 | 21.23 | 2.00 | 85.7 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 3.16 | 9.40 | 15.20 | 1.00 | 62.6 | 24.0 |

## GW15

- Train rows: 114034
- Bank: 0.60 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 67.37
- Actual score: 34.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.87) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Cole Palmer -> Hwang Hee-chan (projected gain 6.92, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.87) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.22 | 9.59 | 15.61 | 0.00 | 85.0 | 0.0 |
| Bench 1 | Bench Boost | Joseph Anang | GK | 19 | 4.0 | 0.00 | 0.30 | 0.66 | 0.00 | 5.8 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.36 | 14.96 | 24.48 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.10 | 11.53 | 18.43 | 1.00 | 82.5 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.68 | 9.87 | 16.11 | 1.00 | 81.6 | 90.0 |
| Bench 2 | Bench Boost | Jamaal Lascelles | DEF | 15 | 4.1 | 2.91 | 7.96 | 12.61 | 1.00 | 77.7 | 89.0 |
| Bench 4 | Bench Boost | Issa Kaboré | DEF | 12 | 4.0 | 1.74 | 3.65 | 7.14 | 0.00 | 61.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 8.04 | 25.02 | 33.06 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.53 | 13.71 | 23.65 | 1.00 | 81.5 | 89.0 |
| Bench 3 | Bench Boost | Cameron Archer | FWD | 17 | 4.6 | 2.22 | 6.60 | 10.72 | 2.00 | 59.3 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.7 | 6.21 | 17.14 | 27.32 | 5.00 | 90.0 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 5.53 | 15.38 | 25.77 | 2.00 | 90.0 | 87.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 4.24 | 12.16 | 20.38 | 0.00 | 84.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 3.83 | 11.60 | 14.93 | 6.00 | 61.4 | 39.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.6 | 3.70 | 10.19 | 16.46 | 10.00 | 83.6 | 90.0 |