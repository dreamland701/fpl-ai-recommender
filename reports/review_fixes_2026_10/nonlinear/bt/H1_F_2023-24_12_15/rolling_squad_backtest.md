# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 249.76
- Total actual points: 206.00
- Average predicted points: 62.44
- Average actual points: 51.50
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
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 59.87
- Actual score: 76.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 4.13 | 10.57 | 16.88 | 2.00 | 85.8 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | 15 | 5.5 | 3.67 | 10.03 | 16.28 | 4.00 | 89.4 | 90.0 |
| Bench 2 | Bench | Kieran Trippier | DEF | 15 | 7.0 | 3.27 | 16.95 | 26.88 | 1.00 | 76.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 3.91 | 11.58 | 18.15 | 9.00 | 77.3 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 4.19 | 11.28 | 18.05 | 1.00 | 88.1 | 90.0 |
| Bench 4 | Bench | Matty Cash | DEF | 2 | 5.2 | 2.53 | 10.54 | 16.82 | 2.00 | 47.5 | 90.0 |
| XI | XI | Fabian Schär | DEF | 15 | 5.2 | 3.51 | 10.09 | 16.10 | 1.00 | 83.5 | 90.0 |
| XI | XI | Eddie Nketiah | FWD | 1 | 5.7 | 4.87 | 9.77 | 15.15 | 1.00 | 76.0 | 9.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 6.4 | 3.59 | 9.20 | 15.06 | 13.00 | 75.0 | 90.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.89 | 7.83 | 13.07 | 2.00 | 79.9 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.9 | 8.44 | 21.03 | 34.47 | 16.00 | 87.8 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 4.65 | 16.87 | 27.95 | 2.00 | 87.2 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.6 | 5.81 | 15.93 | 25.98 | 5.00 | 75.6 | 80.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.6 | 4.57 | 15.81 | 24.64 | 8.00 | 89.2 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 3.74 | 13.08 | 21.72 | 2.00 | 85.8 | 90.0 |

## GW13

- Train rows: 112534
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Jarrod Bowen
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 57.46
- Actual score: 38.00
- Transfer: none
- No transfer was applied this week.
- Autosub: Eddie Nketiah replaced Jarrod Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 4.20 | 10.59 | 16.78 | 3.00 | 85.4 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | 15 | 5.5 | 3.13 | 9.55 | 15.90 | 3.00 | 89.3 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.91 | 14.42 | 23.49 | 1.00 | 88.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 3.07 | 13.04 | 19.97 | 6.00 | 86.6 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.23 | 11.14 | 17.76 | 1.00 | 85.1 | 90.0 |
| Bench 4 | Bench | Matty Cash | DEF | 2 | 5.1 | 2.52 | 9.42 | 15.00 | 0.00 | 69.5 | 45.0 |
| Bench 3 | Bench | Fabian Schär | DEF | 15 | 5.2 | 2.87 | 8.87 | 14.37 | 2.00 | 86.0 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 6.4 | 5.26 | 12.30 | 19.12 | 2.00 | 84.9 | 90.0 |
| XI | XI | Cameron Archer | FWD | 17 | 4.6 | 4.16 | 7.83 | 12.83 | 2.00 | 80.6 | 90.0 |
| Bench 2 | Autosub In | Eddie Nketiah | FWD | 1 | 5.7 | 3.35 | 7.64 | 12.29 | 1.00 | 63.4 | 24.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.9 | 6.04 | 21.95 | 35.97 | 5.00 | 89.2 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.6 | 4.60 | 16.96 | 26.86 | 8.00 | 77.7 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 5.80 | 14.80 | 24.58 | 2.00 | 88.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 4.23 | 13.75 | 22.00 | 2.00 | 87.7 | 90.0 |
| Vice Captain | Bench | Jarrod Bowen | MID | 19 | 7.6 | 5.92 | 12.97 | 20.80 | 0.00 | 82.2 | 0.0 |

## GW14

- Train rows: 113281
- Bank: 0.10 -> 0.90
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 66.65
- Actual score: 63.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.83) beats the best remaining Triple Captain opportunity (9.95).
- Transfer: Jarrod Bowen -> Jérémy Doku (projected gain 3.08, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.83) beats the best remaining Triple Captain opportunity (9.95).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 4.31 | 10.14 | 16.22 | 2.00 | 86.6 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | 15 | 5.5 | 2.88 | 9.12 | 15.22 | 6.00 | 88.5 | 85.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.16 | 13.69 | 22.64 | 12.00 | 86.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 3.63 | 11.88 | 18.55 | 1.00 | 85.7 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.24 | 9.64 | 15.65 | 2.00 | 78.0 | 90.0 |
| Bench 2 | Bench | Matty Cash | DEF | 2 | 5.0 | 2.70 | 8.58 | 14.33 | 1.00 | 44.9 | 16.0 |
| Bench 3 | Bench | Fabian Schär | DEF | 15 | 5.2 | 2.50 | 8.27 | 13.59 | 6.00 | 83.9 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 6.4 | 4.68 | 9.21 | 14.57 | 6.00 | 81.3 | 90.0 |
| XI | XI | Cameron Archer | FWD | 17 | 4.6 | 3.89 | 7.98 | 13.12 | 1.00 | 81.5 | 45.0 |
| Bench 4 | Bench | Eddie Nketiah | FWD | 1 | 5.7 | 2.49 | 6.11 | 10.62 | 1.00 | 39.2 | 23.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.0 | 7.83 | 21.61 | 35.87 | 5.00 | 86.9 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.7 | 5.63 | 17.60 | 28.02 | 8.00 | 82.8 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 5.29 | 16.54 | 25.95 | 5.00 | 81.7 | 77.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 3.56 | 12.91 | 22.39 | 10.00 | 74.1 | 90.0 |
| XI | XI | Jérémy Doku | MID | 13 | 6.8 | 4.77 | 11.39 | 18.59 | 1.00 | 71.5 | 51.0 |

## GW15

- Train rows: 114034
- Bank: 0.90 -> 1.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Son Heung-min
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 65.79
- Actual score: 29.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.74) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Nick Pope -> André Onana (projected gain 2.15, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.74) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 2.89 | 10.30 | 17.10 | 2.00 | 90.2 | 90.0 |
| Bench 1 | Bench Boost | Alphonse Areola | GK | 19 | 4.3 | 2.84 | 9.49 | 15.41 | 0.00 | 85.6 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.59 | 15.31 | 24.83 | 1.00 | 86.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.15 | 11.59 | 18.47 | 1.00 | 84.4 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 4.46 | 9.89 | 16.27 | 1.00 | 81.3 | 90.0 |
| XI | XI | Fabian Schär | DEF | 15 | 5.2 | 3.63 | 8.76 | 14.28 | 1.00 | 83.5 | 90.0 |
| Bench 4 | Bench Boost | Matty Cash | DEF | 2 | 4.9 | 1.45 | 5.60 | 10.11 | 0.00 | 32.3 | 0.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 6.4 | 4.27 | 10.80 | 17.08 | 2.00 | 79.0 | 87.0 |
| Bench 2 | Bench Boost | Cameron Archer | FWD | 17 | 4.6 | 2.30 | 6.68 | 10.90 | 2.00 | 59.7 | 90.0 |
| Bench 3 | Bench Boost | Eddie Nketiah | FWD | 1 | 5.6 | 2.15 | 5.82 | 10.42 | 0.00 | 41.8 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.0 | 7.10 | 21.57 | 36.24 | 3.00 | 87.3 | 66.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.7 | 5.40 | 17.63 | 28.32 | 5.00 | 84.3 | 90.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.6 | 6.31 | 15.47 | 26.20 | 2.00 | 88.8 | 87.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 4.59 | 12.30 | 19.77 | 6.00 | 87.1 | 39.0 |
| XI | XI | Jérémy Doku | MID | 13 | 6.8 | 2.55 | 9.04 | 14.91 | 0.00 | 48.4 | 0.0 |