# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 265.79
- Total actual points: 245.00
- Average predicted points: 66.45
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
- Predicted score: 64.98
- Actual score: 69.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.72 | 9.80 | 15.52 | 2.00 | 84.7 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.26 | 0.50 | 0.75 | 0.00 | 6.4 | 0.0 |
| Vice Captain | XI | Kieran Trippier | DEF | 15 | 7.0 | 6.30 | 17.14 | 27.30 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.43 | 11.75 | 18.48 | 9.00 | 90.0 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.99 | 11.69 | 18.74 | 1.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Vitalii Mykolenko | DEF | 9 | 4.3 | 2.74 | 8.08 | 13.10 | 9.00 | 78.1 | 90.0 |
| Bench 4 | Bench | Auston Trusty | DEF | 17 | 3.9 | 1.74 | 5.24 | 8.31 | 2.00 | 61.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.32 | 22.38 | 36.43 | 16.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 5.87 | 17.69 | 28.17 | 6.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.78 | 7.37 | 12.14 | 2.00 | 67.5 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 5.75 | 17.03 | 28.17 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.6 | 5.66 | 16.35 | 25.58 | 8.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.6 | 5.58 | 14.95 | 24.58 | 5.00 | 78.2 | 80.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 5.02 | 13.62 | 21.29 | 1.00 | 86.1 | 45.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 4.01 | 13.47 | 22.38 | 2.00 | 87.8 | 90.0 |

## GW13

- Train rows: 112534
- Bank: 0.00 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 62.04
- Actual score: 45.00
- Transfer: Kaoru Mitoma -> James Ward-Prowse (projected gain 3.70, hit 0)
- Autosub: Vitalii Mykolenko replaced Jarrod Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.70 | 9.83 | 15.45 | 3.00 | 83.6 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.15 | 0.42 | 0.69 | 0.00 | 6.2 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.06 | 14.68 | 23.99 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.57 | 13.11 | 20.11 | 6.00 | 90.0 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 4.00 | 11.54 | 18.45 | 1.00 | 90.0 | 90.0 |
| Bench 2 | Autosub In | Vitalii Mykolenko | DEF | 9 | 4.3 | 2.89 | 8.85 | 14.67 | 1.00 | 84.8 | 90.0 |
| Bench 4 | Bench | Auston Trusty | DEF | 17 | 3.9 | 2.07 | 5.43 | 8.47 | 1.00 | 63.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.78 | 23.30 | 38.22 | 7.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.99 | 16.26 | 25.02 | 5.00 | 85.0 | 90.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.86 | 7.28 | 11.79 | 2.00 | 65.5 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.6 | 6.03 | 17.19 | 27.28 | 8.00 | 90.0 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 5.06 | 15.02 | 24.87 | 2.00 | 88.3 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 4.34 | 14.11 | 22.56 | 2.00 | 87.4 | 90.0 |
| XI | XI | James Ward-Prowse | MID | 19 | 6.2 | 4.51 | 12.50 | 20.54 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.6 | 4.24 | 12.39 | 19.97 | 0.00 | 69.5 | 0.0 |

## GW14

- Train rows: 113281
- Bank: 0.30 -> 2.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 69.66
- Actual score: 83.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.24) beats the best remaining Triple Captain opportunity (8.99).
- Transfer: Jarrod Bowen -> Anthony Gordon (projected gain 4.14, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.24) beats the best remaining Triple Captain opportunity (8.99).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.58 | 9.39 | 14.91 | 2.00 | 82.4 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.00 | 0.01 | 0.18 | 8.00 | 5.9 | 67.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.79 | 13.96 | 23.17 | 12.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.34 | 12.05 | 18.84 | 1.00 | 85.1 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.44 | 10.08 | 16.40 | 2.00 | 82.6 | 90.0 |
| Bench 3 | Bench | Vitalii Mykolenko | DEF | 9 | 4.3 | 2.81 | 8.34 | 13.71 | 6.00 | 76.2 | 90.0 |
| Bench 4 | Bench | Auston Trusty | DEF | 17 | 3.9 | 2.00 | 5.55 | 8.84 | 0.00 | 65.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 8.24 | 24.78 | 40.90 | 7.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.87 | 14.42 | 24.05 | 11.00 | 76.6 | 90.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.82 | 7.44 | 12.09 | 1.00 | 67.7 | 45.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.7 | 6.41 | 17.73 | 28.31 | 8.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 5.85 | 16.80 | 26.43 | 5.00 | 90.0 | 77.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 4.04 | 13.18 | 22.81 | 10.00 | 80.2 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.9 | 3.93 | 11.53 | 18.32 | 10.00 | 86.2 | 90.0 |
| XI | XI | James Ward-Prowse | MID | 19 | 6.2 | 3.66 | 10.72 | 17.92 | 1.00 | 77.1 | 90.0 |

## GW15

- Train rows: 114034
- Bank: 2.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 69.11
- Actual score: 48.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.98) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Cameron Archer -> Dominic Solanke (projected gain 1.58, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.98) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.10 | 8.78 | 14.15 | 0.00 | 81.1 | 0.0 |
| Bench 1 | Bench Boost | Daniel Bentley | GK | 20 | 3.9 | 1.11 | 2.42 | 4.00 | 7.00 | 29.9 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.49 | 15.49 | 25.23 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.15 | 11.61 | 18.49 | 1.00 | 84.1 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.82 | 10.26 | 16.91 | 1.00 | 85.9 | 90.0 |
| Bench 3 | Bench Boost | Vitalii Mykolenko | DEF | 9 | 4.3 | 2.91 | 8.56 | 13.82 | 6.00 | 82.1 | 90.0 |
| Bench 4 | Bench Boost | Auston Trusty | DEF | 17 | 3.9 | 1.87 | 5.62 | 9.13 | 2.00 | 70.1 | 87.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 8.10 | 24.59 | 40.32 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.61 | 14.78 | 24.90 | 1.00 | 84.1 | 89.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 6.5 | 3.74 | 11.46 | 18.16 | 2.00 | 74.9 | 87.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.7 | 6.34 | 17.79 | 28.66 | 5.00 | 90.0 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 5.60 | 15.74 | 26.56 | 2.00 | 90.0 | 87.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 3.97 | 12.70 | 20.40 | 6.00 | 65.7 | 39.0 |
| Bench 2 | Bench Boost | Anthony Gordon | MID | 15 | 5.9 | 3.10 | 9.95 | 15.63 | 2.00 | 60.8 | 90.0 |
| XI | XI | James Ward-Prowse | MID | 19 | 6.2 | 3.10 | 9.81 | 16.86 | 8.00 | 80.4 | 90.0 |