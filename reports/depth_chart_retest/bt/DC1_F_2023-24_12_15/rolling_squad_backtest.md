# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 260.76
- Total actual points: 245.00
- Average predicted points: 65.19
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
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 63.31
- Actual score: 80.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 4.18 | 11.42 | 18.24 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | João Neves Virgínia | GK | 9 | 3.9 | 0.29 | 0.56 | 0.82 | 0.00 | 6.1 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 6.23 | 16.82 | 26.69 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.16 | 11.07 | 17.35 | 9.00 | 85.9 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.60 | 10.70 | 17.12 | 1.00 | 85.2 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 4.0 | 1.80 | 6.22 | 10.46 | 1.00 | 75.1 | 90.0 |
| Bench 4 | Bench | George Baldock | DEF | 17 | 3.8 | 1.57 | 4.32 | 7.02 | 2.00 | 46.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 6.98 | 21.64 | 35.17 | 16.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 6.14 | 18.47 | 29.33 | 6.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.6 | 3.12 | 8.48 | 14.05 | 2.00 | 74.6 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.9 | 6.83 | 20.63 | 33.69 | 16.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.6 | 5.24 | 15.25 | 23.75 | 8.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 3.89 | 13.14 | 21.78 | 2.00 | 84.6 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 4.75 | 12.95 | 20.21 | 1.00 | 81.7 | 45.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.8 | 4.35 | 11.65 | 17.58 | 2.00 | 83.2 | 90.0 |

## GW13

- Train rows: 112534
- Bank: 0.00 -> 1.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 58.46
- Actual score: 54.00
- Transfer: Kaoru Mitoma -> Cole Palmer (projected gain 3.15, hit 0)
- Autosub: Anthony Gordon replaced Jarrod Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 4.15 | 11.39 | 18.08 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | João Neves Virgínia | GK | 9 | 3.9 | 0.18 | 0.36 | 0.61 | 0.00 | 4.8 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.89 | 14.17 | 23.10 | 1.00 | 88.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.29 | 12.36 | 18.87 | 6.00 | 89.2 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.59 | 10.50 | 16.74 | 1.00 | 84.7 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 4.0 | 2.66 | 7.32 | 12.08 | 1.00 | 78.6 | 90.0 |
| Bench 4 | Bench | George Baldock | DEF | 17 | 3.8 | 2.04 | 5.19 | 8.11 | 5.00 | 52.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.38 | 22.43 | 36.79 | 7.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 5.23 | 17.05 | 26.29 | 5.00 | 84.6 | 90.0 |
| XI | XI | Cameron Archer | FWD | 17 | 4.6 | 3.31 | 8.74 | 14.27 | 2.00 | 73.1 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.9 | 6.60 | 21.52 | 35.27 | 5.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 4.26 | 13.95 | 22.32 | 2.00 | 84.9 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 3.61 | 12.33 | 19.63 | 2.00 | 84.1 | 74.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.6 | 3.77 | 11.21 | 18.06 | 0.00 | 60.2 | 0.0 |
| Bench 2 | Autosub In | Anthony Gordon | MID | 15 | 5.8 | 3.25 | 9.30 | 15.00 | 13.00 | 74.0 | 90.0 |

## GW14

- Train rows: 113281
- Bank: 1.30 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 70.96
- Actual score: 83.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.06) beats the best remaining Bench Boost opportunity (9.37).
- Transfer: Jarrod Bowen -> Bukayo Saka (projected gain 7.09, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.06) beats the best remaining Bench Boost opportunity (9.37).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 4.03 | 10.95 | 17.54 | 2.00 | 88.9 | 90.0 |
| Bench 1 | Bench Boost | João Neves Virgínia | GK | 9 | 3.9 | 0.13 | 0.29 | 0.49 | 0.00 | 4.4 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.59 | 13.44 | 22.29 | 12.00 | 85.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.03 | 11.33 | 17.68 | 1.00 | 79.5 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.02 | 8.99 | 14.61 | 2.00 | 74.4 | 90.0 |
| Bench 3 | Bench Boost | Charlie Taylor | DEF | 6 | 4.0 | 2.66 | 7.31 | 11.94 | 10.00 | 77.9 | 90.0 |
| Bench 4 | Bench Boost | George Baldock | DEF | 17 | 3.8 | 2.12 | 5.94 | 9.58 | 1.00 | 57.6 | 24.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.84 | 23.82 | 39.27 | 7.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 5.10 | 15.21 | 25.29 | 11.00 | 76.7 | 90.0 |
| XI | XI | Cameron Archer | FWD | 17 | 4.6 | 3.23 | 8.85 | 14.51 | 1.00 | 74.9 | 45.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.0 | 7.29 | 21.33 | 35.40 | 5.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.8 | 6.25 | 17.43 | 27.80 | 8.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 5.73 | 16.43 | 25.79 | 5.00 | 90.0 | 77.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.8 | 3.93 | 11.38 | 18.13 | 10.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Cole Palmer | MID | 7 | 5.2 | 3.14 | 10.46 | 16.74 | 1.00 | 62.6 | 24.0 |

## GW15

- Train rows: 114034
- Bank: 0.10 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 68.03
- Actual score: 28.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.76) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Joachim Andersen -> Konstantinos Tsimikas (projected gain 0.74, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (7.76) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Cameron Archer replaced Konstantinos Tsimikas.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alphonse Areola | GK | 19 | 4.3 | 3.56 | 10.38 | 16.85 | 0.00 | 87.8 | 0.0 |
| Bench 1 | Bench | João Neves Virgínia | GK | 9 | 3.9 | 0.14 | 0.22 | 0.40 | 0.00 | 3.8 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.31 | 15.05 | 24.49 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 3.93 | 10.97 | 17.43 | 1.00 | 81.2 | 90.0 |
| XI | Bench | Konstantinos Tsimikas | DEF | 11 | 4.8 | 3.66 | 10.00 | 15.96 | 0.00 | 70.2 | 0.0 |
| XI | XI | Charlie Taylor | DEF | 6 | 4.0 | 2.86 | 7.85 | 12.78 | 1.00 | 81.9 | 90.0 |
| Bench 4 | Bench | George Baldock | DEF | 17 | 3.8 | 0.61 | 3.02 | 5.19 | 0.00 | 27.4 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.76 | 23.77 | 38.97 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.81 | 15.57 | 26.25 | 1.00 | 84.3 | 89.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 4.6 | 2.44 | 7.35 | 11.96 | 2.00 | 62.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.0 | 7.52 | 21.32 | 35.77 | 3.00 | 90.0 | 66.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.8 | 6.19 | 17.49 | 28.14 | 5.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 3.90 | 12.41 | 19.88 | 6.00 | 64.3 | 39.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.9 | 3.03 | 9.67 | 15.25 | 2.00 | 62.6 | 90.0 |
| Bench 3 | Bench | Cole Palmer | MID | 7 | 5.2 | 2.26 | 8.61 | 14.59 | 8.00 | 51.7 | 90.0 |