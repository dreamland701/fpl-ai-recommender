# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 242.36
- Total actual points: 231.00
- Average predicted points: 60.59
- Average actual points: 57.75
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
- Vice captain: Kieran Trippier
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 56.89
- Actual score: 64.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Joachim Andersen replaced James Maddison.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.68 | 10.43 | 17.05 | 2.00 | 85.9 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | 15 | 5.5 | 3.53 | 9.99 | 16.31 | 4.00 | 83.9 | 90.0 |
| Vice Captain | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.54 | 16.38 | 26.70 | 1.00 | 88.6 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 7.9 | 4.02 | 11.33 | 18.00 | 7.00 | 72.5 | 89.0 |
| Bench 2 | Autosub In | Joachim Andersen | DEF | 8 | 5.0 | 3.70 | 11.09 | 18.05 | 1.00 | 84.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.2 | 3.72 | 10.43 | 16.78 | 9.00 | 81.0 | 90.0 |
| XI | XI | Matty Cash | DEF | 2 | 5.2 | 3.78 | 10.39 | 16.25 | 2.00 | 68.6 | 90.0 |
| XI | XI | Eddie Nketiah | FWD | 1 | 5.6 | 3.62 | 10.36 | 16.09 | 1.00 | 61.7 | 9.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 4.5 | 2.91 | 8.52 | 14.18 | 2.00 | 72.6 | 90.0 |
| Bench 4 | Bench | Chiedozie Ogbene | FWD | 12 | 4.9 | 2.31 | 7.37 | 12.78 | 2.00 | 71.0 | 85.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.9 | 6.68 | 19.92 | 32.70 | 16.00 | 94.7 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 5.26 | 16.04 | 27.03 | 2.00 | 83.2 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.6 | 5.45 | 14.93 | 24.50 | 5.00 | 78.2 | 80.0 |
| XI | Bench | James Maddison | MID | 18 | 8.1 | 4.53 | 14.06 | 23.21 | 0.00 | 67.7 | 0.0 |
| XI | XI | Douglas Luiz Soares de Paulo | MID | 2 | 5.6 | 3.95 | 11.73 | 18.72 | 2.00 | 77.5 | 90.0 |

## GW13

- Train rows: 112534
- Bank: 0.10 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Jarrod Bowen
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 53.61
- Actual score: 48.00
- Transfer: James Maddison -> Jarrod Bowen (projected gain 4.45, hit 0)
- Autosub: Douglas Luiz Soares de Paulo replaced Jarrod Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.64 | 10.41 | 16.82 | 3.00 | 85.8 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | 15 | 5.5 | 3.39 | 9.93 | 16.45 | 3.00 | 87.7 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.18 | 15.68 | 25.41 | 1.00 | 90.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.2 | 4.12 | 11.92 | 18.78 | 6.00 | 85.2 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.0 | 3.67 | 10.82 | 17.59 | 1.00 | 85.6 | 90.0 |
| XI | XI | Matty Cash | DEF | 2 | 5.2 | 3.41 | 10.26 | 15.91 | 0.00 | 72.0 | 45.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 7.9 | 3.17 | 10.06 | 16.62 | 8.00 | 71.9 | 90.0 |
| Bench 3 | Bench | Eddie Nketiah | FWD | 1 | 5.6 | 2.83 | 8.76 | 14.04 | 1.00 | 45.4 | 24.0 |
| XI | XI | Cameron Archer | FWD | 17 | 4.5 | 2.95 | 8.16 | 13.41 | 2.00 | 70.1 | 90.0 |
| Bench 4 | Bench | Chiedozie Ogbene | FWD | 12 | 4.9 | 2.83 | 8.02 | 13.45 | 5.00 | 70.9 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.9 | 6.17 | 20.57 | 33.92 | 5.00 | 98.8 | 90.0 |
| Vice Captain | Bench | Jarrod Bowen | MID | 19 | 7.6 | 5.19 | 15.12 | 23.32 | 0.00 | 81.7 | 0.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 4.91 | 14.80 | 24.66 | 2.00 | 84.2 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.6 | 5.02 | 14.76 | 23.70 | 8.00 | 74.3 | 90.0 |
| Bench 2 | Autosub In | Douglas Luiz Soares de Paulo | MID | 2 | 5.6 | 3.13 | 10.77 | 17.42 | 7.00 | 76.5 | 90.0 |

## GW14

- Train rows: 113281
- Bank: 0.50 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 63.29
- Actual score: 68.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.46) beats the best remaining Triple Captain opportunity (9.48).
- Transfer: Matty Cash -> Pedro Porro (projected gain 0.01, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.46) beats the best remaining Triple Captain opportunity (9.48).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.67 | 10.33 | 16.77 | 2.00 | 86.1 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | 15 | 5.5 | 3.02 | 9.42 | 15.73 | 6.00 | 85.8 | 85.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.77 | 14.31 | 23.92 | 12.00 | 88.6 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 7.9 | 4.35 | 12.21 | 19.95 | 13.00 | 78.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.25 | 12.05 | 19.07 | 1.00 | 83.5 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.65 | 10.81 | 17.53 | 2.00 | 85.8 | 90.0 |
| Bench 3 | Bench | Pedro Porro | DEF | 18 | 5.3 | 3.08 | 10.03 | 17.04 | 0.00 | 87.9 | 90.0 |
| Bench 2 | Bench | Chiedozie Ogbene | FWD | 12 | 4.9 | 3.14 | 9.15 | 15.39 | 1.00 | 81.7 | 59.0 |
| XI | XI | Cameron Archer | FWD | 17 | 4.5 | 3.16 | 8.77 | 14.40 | 1.00 | 73.6 | 45.0 |
| Bench 4 | Bench | Eddie Nketiah | FWD | 1 | 5.6 | 2.44 | 7.32 | 12.35 | 1.00 | 38.4 | 23.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.9 | 7.46 | 21.85 | 36.07 | 5.00 | 97.3 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.6 | 5.58 | 15.78 | 25.19 | 8.00 | 83.5 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 4.46 | 14.81 | 25.11 | 10.00 | 85.0 | 90.0 |
| XI | XI | Douglas Luiz Soares de Paulo | MID | 2 | 5.6 | 3.59 | 10.79 | 17.90 | 2.00 | 80.9 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.6 | 3.40 | 10.34 | 17.71 | 2.00 | 47.0 | 90.0 |

## GW15

- Train rows: 114034
- Bank: 0.30 -> 0.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 68.57
- Actual score: 51.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.75) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Eddie Nketiah -> Matheus Santos Carneiro Da Cunha (projected gain 3.30, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.75) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.22 | 9.90 | 16.17 | 0.00 | 86.2 | 0.0 |
| Bench 1 | Bench Boost | Nick Pope | GK | 15 | 5.5 | 3.19 | 9.52 | 15.81 | 0.00 | 84.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.43 | 15.53 | 25.58 | 1.00 | 95.5 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 7.9 | 4.78 | 13.66 | 22.64 | 12.00 | 84.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.14 | 11.92 | 19.27 | 1.00 | 84.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 3.67 | 10.96 | 18.27 | 5.00 | 83.3 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.79 | 10.59 | 17.46 | 1.00 | 84.9 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.5 | 4.06 | 11.13 | 17.85 | 5.00 | 80.3 | 86.0 |
| Bench 3 | Bench Boost | Chiedozie Ogbene | FWD | 12 | 4.9 | 2.36 | 7.84 | 13.26 | 1.00 | 75.1 | 28.0 |
| Bench 4 | Bench Boost | Cameron Archer | FWD | 17 | 4.5 | 2.32 | 7.23 | 11.86 | 2.00 | 62.3 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.0 | 7.33 | 21.97 | 36.33 | 3.00 | 99.6 | 66.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.7 | 5.73 | 16.17 | 26.01 | 5.00 | 84.6 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 5.27 | 15.61 | 26.67 | 2.00 | 85.7 | 87.0 |
| Bench 2 | Bench Boost | Jarrod Bowen | MID | 19 | 7.6 | 2.88 | 10.08 | 18.05 | 7.00 | 56.1 | 90.0 |
| XI | XI | Douglas Luiz Soares de Paulo | MID | 2 | 5.6 | 3.09 | 9.70 | 16.13 | 3.00 | 81.4 | 90.0 |