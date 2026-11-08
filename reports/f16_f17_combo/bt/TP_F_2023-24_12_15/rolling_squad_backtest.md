# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 265.33
- Total actual points: 245.00
- Average predicted points: 66.33
- Average actual points: 61.25
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
- Predicted score: 65.45
- Actual score: 69.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.78 | 9.90 | 15.62 | 2.00 | 86.2 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.12 | 0.26 | 0.40 | 0.00 | 1.5 | 0.0 |
| Vice Captain | XI | Kieran Trippier | DEF | 15 | 7.0 | 6.37 | 17.27 | 27.40 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.49 | 11.86 | 18.57 | 9.00 | 90.0 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 4.06 | 11.80 | 18.82 | 1.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Vitalii Mykolenko | DEF | 9 | 4.3 | 2.81 | 8.19 | 13.20 | 9.00 | 79.7 | 90.0 |
| Bench 4 | Bench | Auston Trusty | DEF | 17 | 3.9 | 1.80 | 5.33 | 8.40 | 2.00 | 63.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.37 | 22.45 | 36.46 | 16.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 5.93 | 17.78 | 28.23 | 6.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.87 | 7.52 | 12.30 | 2.00 | 70.0 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 5.81 | 17.11 | 28.22 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.6 | 5.70 | 16.41 | 25.61 | 8.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.6 | 5.42 | 15.13 | 25.05 | 5.00 | 74.0 | 80.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 5.10 | 13.74 | 21.38 | 1.00 | 87.8 | 45.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 4.05 | 13.51 | 22.40 | 2.00 | 88.5 | 90.0 |

## GW13

- Train rows: 112534
- Bank: 0.00 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 62.08
- Actual score: 45.00
- Transfer: Kaoru Mitoma -> James Ward-Prowse (projected gain 3.71, hit 0)
- Autosub: Vitalii Mykolenko replaced Jarrod Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.76 | 9.93 | 15.55 | 3.00 | 85.2 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.01 | 0.19 | 0.35 | 0.00 | 1.3 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.12 | 14.80 | 24.08 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.62 | 13.20 | 20.18 | 6.00 | 90.0 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 4.07 | 11.65 | 18.52 | 1.00 | 90.0 | 90.0 |
| Bench 2 | Autosub In | Vitalii Mykolenko | DEF | 9 | 4.3 | 2.96 | 8.96 | 14.76 | 1.00 | 86.2 | 90.0 |
| Bench 4 | Bench | Auston Trusty | DEF | 17 | 3.9 | 2.13 | 5.54 | 8.57 | 1.00 | 65.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.60 | 23.41 | 38.65 | 7.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 5.03 | 16.32 | 25.04 | 5.00 | 86.0 | 90.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.96 | 7.44 | 11.96 | 2.00 | 68.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.6 | 6.08 | 17.29 | 27.33 | 8.00 | 90.0 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 5.12 | 15.11 | 24.92 | 2.00 | 89.7 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 4.38 | 14.17 | 22.58 | 2.00 | 88.4 | 90.0 |
| XI | XI | James Ward-Prowse | MID | 19 | 6.2 | 4.57 | 12.60 | 20.63 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.6 | 4.11 | 12.57 | 20.49 | 0.00 | 65.9 | 0.0 |

## GW14

- Train rows: 113281
- Bank: 0.30 -> 2.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 70.16
- Actual score: 83.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.29) beats the best remaining Triple Captain opportunity (9.03).
- Transfer: Jarrod Bowen -> Anthony Gordon (projected gain 3.19, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.29) beats the best remaining Triple Captain opportunity (9.03).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.64 | 9.49 | 15.00 | 2.00 | 83.9 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.00 | 0.00 | 0.00 | 8.00 | 1.1 | 67.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.86 | 14.08 | 23.27 | 12.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.40 | 12.14 | 18.89 | 1.00 | 86.4 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.52 | 10.20 | 16.50 | 2.00 | 84.5 | 90.0 |
| Bench 2 | Bench | Vitalii Mykolenko | DEF | 9 | 4.3 | 2.88 | 8.46 | 13.80 | 6.00 | 77.9 | 90.0 |
| Bench 4 | Bench | Auston Trusty | DEF | 17 | 3.9 | 2.05 | 5.65 | 8.93 | 0.00 | 66.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 8.29 | 24.84 | 40.92 | 7.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.73 | 14.58 | 24.58 | 11.00 | 73.2 | 90.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.87 | 7.52 | 12.16 | 1.00 | 69.1 | 45.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.7 | 6.46 | 17.83 | 28.38 | 8.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 5.88 | 16.83 | 26.44 | 5.00 | 90.0 | 77.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 4.11 | 13.31 | 22.92 | 10.00 | 81.9 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.9 | 3.97 | 11.59 | 18.37 | 10.00 | 87.0 | 90.0 |
| XI | XI | James Ward-Prowse | MID | 19 | 6.2 | 3.73 | 10.83 | 18.01 | 1.00 | 78.9 | 90.0 |

## GW15

- Train rows: 114034
- Bank: 2.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 67.65
- Actual score: 48.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.66) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Cameron Archer -> Dominic Solanke (projected gain 1.58, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.66) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.00 | 8.65 | 14.09 | 0.00 | 79.5 | 0.0 |
| Bench 1 | Bench Boost | Daniel Bentley | GK | 20 | 3.9 | 1.07 | 2.41 | 4.09 | 7.00 | 30.4 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.39 | 15.38 | 25.18 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.06 | 11.49 | 18.43 | 1.00 | 82.5 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.74 | 10.17 | 16.88 | 1.00 | 84.6 | 90.0 |
| Bench 3 | Bench Boost | Vitalii Mykolenko | DEF | 9 | 4.3 | 2.81 | 8.45 | 13.77 | 6.00 | 80.5 | 90.0 |
| Bench 4 | Bench Boost | Auston Trusty | DEF | 17 | 3.9 | 1.78 | 5.50 | 9.08 | 2.00 | 68.7 | 87.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.98 | 24.40 | 40.16 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.54 | 14.68 | 24.83 | 1.00 | 83.0 | 89.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 6.5 | 3.65 | 11.32 | 18.06 | 2.00 | 73.3 | 87.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.7 | 6.22 | 17.66 | 28.59 | 5.00 | 90.0 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 5.52 | 15.66 | 26.53 | 2.00 | 90.0 | 87.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 3.89 | 12.60 | 20.34 | 6.00 | 64.5 | 39.0 |
| Bench 2 | Bench Boost | Anthony Gordon | MID | 15 | 5.9 | 2.99 | 9.81 | 15.53 | 2.00 | 58.5 | 90.0 |
| XI | XI | James Ward-Prowse | MID | 19 | 6.2 | 3.02 | 9.72 | 16.84 | 8.00 | 79.1 | 90.0 |