# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 243.48
- Total actual points: 243.00
- Average predicted points: 60.87
- Average actual points: 60.75
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW15 are included before the first simulated week.
- League-average scores were not available for this run.

## GW16

- Train rows: 114791
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.28
- Actual score: 76.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub outfielders: Cole Palmer.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.33 | 9.25 | 14.97 | 9.00 | 88.6 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 4.8 | 3.12 | 9.24 | 15.66 | 1.00 | 86.9 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.91 | 15.03 | 24.67 | -1.00 | 93.0 | 85.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.0 | 4.54 | 13.74 | 22.94 | 4.00 | 88.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 3.51 | 11.05 | 18.08 | 2.00 | 83.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 3.77 | 10.94 | 18.22 | 5.00 | 80.1 | 90.0 |
| Bench 3 | Bench | Joachim Andersen | DEF | 8 | 5.2 | 3.11 | 9.45 | 15.44 | 0.00 | 81.3 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.72 | 10.42 | 16.74 | 9.00 | 80.5 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.3 | 3.66 | 10.30 | 16.45 | 2.00 | 61.9 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.87 | 7.81 | 12.44 | 2.00 | 70.2 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.32 | 19.16 | 31.84 | 13.00 | 87.8 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 5.26 | 15.87 | 25.69 | 2.00 | 87.8 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 5.19 | 15.48 | 25.65 | 17.00 | 92.0 | 90.0 |
| XI | Bench | Bryan Mbeumo | MID | 4 | 7.1 | 4.75 | 14.03 | 22.82 | 0.00 | 69.2 | 0.0 |
| Bench 2 | Autosub In | Cole Palmer | MID | 7 | 5.3 | 3.38 | 10.69 | 18.70 | 1.00 | 73.9 | 90.0 |

## GW17

- Train rows: 115549
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Son Heung-min
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 57.46
- Actual score: 58.00
- Transfer: Bryan Mbeumo -> Bernardo Veiga de Carvalho e Silva (projected gain 3.18, hit 0)
- Autosub outfielders: Cameron Archer.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.15 | 9.68 | 15.73 | 3.00 | 89.3 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 4.8 | 2.66 | 9.15 | 15.24 | 10.00 | 85.6 | 90.0 |
| XI | Bench | Kieran Trippier | DEF | 15 | 7.0 | 5.20 | 14.99 | 25.00 | 0.00 | 94.7 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.37 | 13.57 | 22.92 | 9.00 | 85.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 4.15 | 11.80 | 19.36 | 8.00 | 81.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 3.85 | 11.08 | 18.08 | 7.00 | 81.8 | 90.0 |
| Bench 4 | Bench | Joachim Andersen | DEF | 8 | 5.1 | 2.51 | 8.38 | 13.83 | 0.00 | 78.2 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.97 | 11.54 | 18.53 | 2.00 | 83.8 | 90.0 |
| Bench 3 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 2.91 | 9.40 | 15.16 | 1.00 | 61.6 | 30.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 4.6 | 2.93 | 8.45 | 13.39 | 2.00 | 71.2 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.54 | 19.96 | 33.02 | 3.00 | 96.9 | 90.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.6 | 5.96 | 17.14 | 28.54 | 2.00 | 97.2 | 87.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 5.81 | 16.82 | 26.92 | 3.00 | 88.9 | 88.0 |
| XI | XI | Bernardo Veiga de Carvalho e Silva | MID | 13 | 6.4 | 4.14 | 11.57 | 18.62 | 2.00 | 86.1 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.78 | 10.80 | 18.01 | 14.00 | 72.1 | 90.0 |

## GW18

- Train rows: 116314
- Bank: 0.60 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Son Heung-min
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 59.69
- Actual score: 51.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.18) beats the best remaining Triple Captain opportunity (7.45).
- Transfer: Bernardo Veiga de Carvalho e Silva -> Pascal Groß (projected gain 2.32, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (5.18) beats the best remaining Triple Captain opportunity (7.45).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.40 | 10.14 | 16.93 | 2.00 | 89.5 | 90.0 |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.7 | 3.39 | 9.62 | 15.85 | 1.00 | 87.9 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.2 | 4.40 | 13.97 | 23.31 | 5.00 | 86.7 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 4.35 | 11.89 | 19.04 | 2.00 | 81.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 3.48 | 10.89 | 17.66 | 2.00 | 87.8 | 90.0 |
| Bench 2 | Bench | Kieran Trippier | DEF | 15 | 6.9 | 2.78 | 9.37 | 17.17 | 2.00 | 41.5 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.0 | 2.93 | 8.31 | 13.61 | 2.00 | 75.6 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.7 | 3.90 | 11.04 | 17.63 | 1.00 | 76.4 | 85.0 |
| Bench 3 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 2.71 | 8.16 | 13.49 | 2.00 | 42.3 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.54 | 7.57 | 12.25 | 8.00 | 73.9 | 89.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.2 | 5.87 | 18.78 | 31.12 | 7.00 | 89.0 | 90.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.7 | 5.68 | 16.30 | 26.21 | 7.00 | 87.1 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.37 | 16.25 | 25.81 | 1.00 | 87.2 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 4.60 | 12.80 | 20.59 | 1.00 | 91.3 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.4 | 3.97 | 12.04 | 19.74 | 7.00 | 83.1 | 90.0 |

## GW19

- Train rows: 117083
- Bank: 0.60 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 71.05
- Actual score: 58.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.16) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Joachim Andersen -> Gabriel dos Santos Magalhães (projected gain 0.06, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.16) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.09 | 9.47 | 15.89 | 1.00 | 89.9 | 90.0 |
| Bench 1 | Bench Boost | Bernd Leno | GK | 10 | 4.8 | 2.99 | 9.00 | 15.01 | 0.00 | 86.1 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.2 | 4.88 | 14.50 | 23.91 | 8.00 | 86.9 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 4.66 | 13.45 | 22.02 | 1.00 | 78.1 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 4.07 | 12.04 | 19.28 | 5.00 | 83.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 4.02 | 11.07 | 17.86 | 1.00 | 86.6 | 90.0 |
| Bench 2 | Bench Boost | Gabriel dos Santos Magalhães | DEF | 1 | 4.9 | 3.61 | 9.89 | 16.11 | 1.00 | 84.2 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.7 | 3.50 | 10.32 | 16.90 | 5.00 | 70.4 | 90.0 |
| Bench 4 | Bench Boost | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 3.27 | 9.17 | 14.65 | 16.00 | 65.1 | 90.0 |
| Bench 3 | Bench Boost | Cameron Archer | FWD | 17 | 4.6 | 3.30 | 8.92 | 14.36 | 5.00 | 77.2 | 85.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.2 | 6.75 | 20.02 | 33.32 | 3.00 | 95.3 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.8 | 5.66 | 16.91 | 27.72 | 5.00 | 96.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 5.86 | 16.33 | 25.99 | 2.00 | 83.8 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.6 | 4.52 | 13.18 | 20.83 | 0.00 | 82.0 | 0.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.4 | 4.14 | 11.71 | 19.29 | 2.00 | 84.0 | 90.0 |