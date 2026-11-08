# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW1
- Simulated weeks: GW2-GW8
- Total predicted points: 388.22
- Total actual points: 411.00
- Average predicted points: 55.46
- Average actual points: 58.71
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW1 are included before the first simulated week.
- League-average scores were pulled from official FPL event metadata when available.

## GW2

- Train rows: 104659
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Marcus Rashford
- Vice captain: Mohamed Salah
- Effective captain: Marcus Rashford
- Chip used: none
- Predicted score: 51.78
- Actual score: 49.00
- League average score: 81.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 5.0 | 4.31 | 13.07 | 21.85 | 2.00 | 93.6 | 90.0 |
| Bench 1 | Bench | Emiliano Martínez Romero | GK | 2 | 5.0 | 2.97 | 9.17 | 15.70 | 8.00 | 93.7 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.5 | 4.19 | 13.58 | 23.00 | 2.00 | 89.3 | 90.0 |
| XI | XI | Pervis Estupiñán | DEF | 5 | 5.0 | 3.86 | 11.97 | 20.38 | 11.00 | 74.0 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.0 | 3.68 | 10.87 | 18.06 | 2.00 | 83.9 | 75.0 |
| Bench 3 | Bench | Axel Disasi | DEF | 7 | 5.0 | 3.21 | 9.64 | 16.24 | 0.00 | 73.4 | 90.0 |
| Bench 2 | Bench | William Saliba | DEF | 1 | 5.0 | 3.23 | 9.51 | 15.73 | 8.00 | 85.1 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.5 | 3.83 | 11.13 | 18.38 | 7.00 | 73.1 | 90.0 |
| XI | XI | Odsonne Edouard | FWD | 8 | 5.5 | 3.43 | 9.57 | 14.77 | 2.00 | 62.7 | 90.0 |
| Bench 4 | Bench | Carlton Morris | FWD | 12 | 5.5 | 1.87 | 7.27 | 13.56 | 0.00 | 49.7 | 0.0 |
| Captain | Captain | Marcus Rashford | MID | 14 | 9.0 | 5.31 | 16.04 | 26.43 | 2.00 | 88.0 | 84.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.5 | 4.88 | 14.99 | 25.51 | 5.00 | 77.1 | 85.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 3.83 | 13.92 | 24.80 | 1.00 | 88.4 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 4.69 | 13.62 | 22.57 | 12.00 | 83.1 | 80.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.5 | 4.47 | 13.28 | 22.26 | 1.00 | 79.5 | 80.0 |

## GW3

- Train rows: 105327
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Pervis Estupiñán
- Vice captain: Marcus Rashford
- Effective captain: Pervis Estupiñán
- Chip used: none
- Predicted score: 52.21
- Actual score: 42.00
- League average score: 51.00
- Transfer: Julián Álvarez -> Dominic Solanke (projected gain 1.34, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 5.0 | 3.90 | 11.61 | 18.93 | 0.00 | 87.5 | 90.0 |
| Bench 1 | Bench | Emiliano Martínez Romero | GK | 2 | 5.0 | 2.87 | 8.49 | 14.10 | 0.00 | 81.0 | 0.0 |
| Captain | Captain | Pervis Estupiñán | DEF | 5 | 5.1 | 5.24 | 15.50 | 24.70 | 1.00 | 87.8 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.5 | 3.98 | 12.71 | 21.00 | 0.00 | 87.0 | 90.0 |
| Bench 2 | Bench | Trent Alexander-Arnold | DEF | 11 | 8.0 | 3.23 | 10.35 | 16.83 | 1.00 | 68.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.1 | 3.45 | 9.93 | 15.34 | 1.00 | 79.0 | 90.0 |
| Bench 3 | Bench | Axel Disasi | DEF | 7 | 5.0 | 2.66 | 7.95 | 12.81 | 6.00 | 64.8 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 6.5 | 3.72 | 11.04 | 18.03 | 2.00 | 76.2 | 90.0 |
| XI | XI | Odsonne Edouard | FWD | 8 | 5.5 | 3.54 | 9.97 | 15.45 | 2.00 | 67.0 | 70.0 |
| Bench 4 | Bench | Carlton Morris | FWD | 12 | 5.5 | 1.01 | 4.17 | 8.07 | 2.00 | 26.1 | 90.0 |
| XI | XI | Mohamed Salah | MID | 11 | 12.5 | 4.97 | 16.41 | 26.58 | 5.00 | 75.2 | 90.0 |
| Vice Captain | XI | Marcus Rashford | MID | 14 | 9.0 | 5.23 | 15.64 | 25.51 | 7.00 | 79.9 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.57 | 14.51 | 24.65 | 12.00 | 82.8 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 4.75 | 14.46 | 23.71 | 1.00 | 79.3 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.5 | 3.63 | 10.86 | 18.35 | 10.00 | 70.6 | 90.0 |

## GW4

- Train rows: 106012
- Bank: 0.00 -> 2.30
- Free transfers: 2 -> 2
- Captain: Pervis Estupiñán
- Vice captain: Mohamed Salah
- Effective captain: Pervis Estupiñán
- Chip used: none
- Predicted score: 49.87
- Actual score: 40.00
- League average score: 0.00
- Transfer: Trent Alexander-Arnold -> Ben Chilwell (projected gain 1.63, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 5.0 | 2.92 | 9.83 | 16.68 | 0.00 | 84.0 | 90.0 |
| Bench 1 | Bench | Emiliano Martínez Romero | GK | 2 | 5.0 | 1.27 | 5.20 | 9.44 | 1.00 | 44.7 | 90.0 |
| Captain | Captain | Pervis Estupiñán | DEF | 5 | 5.2 | 5.20 | 15.61 | 25.14 | 2.00 | 82.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.5 | 3.84 | 11.96 | 20.10 | 1.00 | 83.6 | 90.0 |
| XI | XI | Ben Chilwell | DEF | 7 | 5.7 | 3.68 | 10.56 | 16.56 | 1.00 | 55.4 | 61.0 |
| XI | XI | William Saliba | DEF | 1 | 5.2 | 3.47 | 10.32 | 16.31 | 2.00 | 78.0 | 90.0 |
| Bench 3 | Bench | Axel Disasi | DEF | 7 | 5.1 | 3.05 | 8.52 | 13.85 | 2.00 | 70.8 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 6.5 | 3.43 | 10.24 | 17.02 | 7.00 | 76.1 | 90.0 |
| Bench 2 | Bench | Odsonne Edouard | FWD | 8 | 5.5 | 3.21 | 8.94 | 13.78 | 13.00 | 59.9 | 89.0 |
| Bench 4 | Bench | Carlton Morris | FWD | 12 | 5.5 | 2.38 | 7.01 | 12.02 | 5.00 | 56.5 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.5 | 4.94 | 15.73 | 26.48 | 8.00 | 76.8 | 90.0 |
| XI | XI | Marcus Rashford | MID | 14 | 9.0 | 4.47 | 14.88 | 25.53 | 7.00 | 81.0 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.6 | 4.77 | 14.56 | 23.70 | 5.00 | 75.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.09 | 14.31 | 24.63 | 2.00 | 82.4 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.4 | 3.85 | 11.73 | 20.00 | 3.00 | 77.6 | 88.0 |

## GW5

- Train rows: 106715
- Bank: 2.30 -> 0.80
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Pervis Estupiñán
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 53.49
- Actual score: 64.00
- League average score: 0.00
- Transfer: Dominic Solanke -> Ollie Watkins (projected gain 2.10, hit 0)
- Autosub outfielders: Odsonne Edouard.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 5.0 | 3.12 | 9.24 | 16.02 | 2.00 | 79.7 | 90.0 |
| Bench 1 | Bench | Emiliano Martínez Romero | GK | 2 | 5.0 | 2.59 | 7.33 | 12.39 | 2.00 | 63.9 | 90.0 |
| Vice Captain | Bench | Pervis Estupiñán | DEF | 5 | 5.3 | 5.06 | 15.20 | 24.87 | 0.00 | 89.6 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.5 | 3.82 | 11.27 | 18.77 | 8.00 | 80.9 | 90.0 |
| XI | XI | Ben Chilwell | DEF | 7 | 5.8 | 3.83 | 11.14 | 17.44 | 0.00 | 56.8 | 10.0 |
| XI | XI | William Saliba | DEF | 1 | 5.2 | 3.62 | 10.64 | 17.32 | 6.00 | 82.3 | 90.0 |
| Bench 3 | Bench | Axel Disasi | DEF | 7 | 5.1 | 3.12 | 9.37 | 15.27 | 5.00 | 75.8 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.0 | 4.25 | 12.26 | 20.20 | 5.00 | 64.6 | 90.0 |
| Bench 2 | Autosub In | Odsonne Edouard | FWD | 8 | 5.5 | 3.19 | 9.54 | 15.16 | 8.00 | 68.2 | 89.0 |
| Bench 4 | Bench | Carlton Morris | FWD | 12 | 5.5 | 2.36 | 7.31 | 12.50 | 2.00 | 55.7 | 73.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.5 | 5.98 | 17.42 | 28.35 | 10.00 | 82.4 | 90.0 |
| XI | XI | Marcus Rashford | MID | 14 | 9.0 | 5.04 | 15.46 | 26.20 | 2.00 | 84.8 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.98 | 14.68 | 24.18 | 1.00 | 83.7 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.6 | 4.57 | 14.35 | 23.98 | 2.00 | 81.4 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.4 | 3.24 | 10.64 | 18.21 | 10.00 | 75.8 | 90.0 |

## GW6

- Train rows: 107432
- Bank: 0.80 -> 1.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Marcus Rashford
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 51.72
- Actual score: 87.00
- League average score: 0.00
- Transfer: Emiliano Martínez Romero -> Alphonse Areola (projected gain 1.41, hit 0)
- Autosub outfielders: Axel Disasi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.1 | 3.13 | 10.62 | 17.89 | 2.00 | 91.2 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 5.0 | 3.04 | 9.25 | 15.72 | 7.00 | 79.9 | 90.0 |
| XI | XI | Pervis Estupiñán | DEF | 5 | 5.3 | 4.06 | 12.06 | 19.87 | 6.00 | 53.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.5 | 3.80 | 11.30 | 18.73 | 18.00 | 79.1 | 69.0 |
| XI | XI | William Saliba | DEF | 1 | 5.2 | 3.79 | 11.12 | 17.83 | 1.00 | 85.8 | 90.0 |
| Bench 2 | Autosub In | Axel Disasi | DEF | 7 | 5.1 | 3.28 | 9.83 | 15.96 | 2.00 | 82.3 | 90.0 |
| Bench 3 | Bench | Ben Chilwell | DEF | 7 | 5.8 | 3.00 | 9.23 | 15.52 | 0.00 | 41.8 | 29.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.0 | 4.24 | 12.78 | 20.90 | 9.00 | 73.3 | 90.0 |
| XI | XI | Odsonne Edouard | FWD | 8 | 5.5 | 3.77 | 10.50 | 16.90 | 2.00 | 70.4 | 90.0 |
| Bench 4 | Bench | Carlton Morris | FWD | 12 | 5.5 | 2.66 | 7.77 | 13.07 | 9.00 | 57.3 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.5 | 5.58 | 17.20 | 28.63 | 10.00 | 84.0 | 90.0 |
| Vice Captain | XI | Marcus Rashford | MID | 14 | 8.9 | 4.98 | 15.46 | 25.47 | 3.00 | 86.0 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 4.73 | 13.91 | 22.79 | 14.00 | 76.2 | 45.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.20 | 13.32 | 22.59 | 10.00 | 78.1 | 90.0 |
| XI | Bench | Pascal Groß | MID | 5 | 6.3 | 3.87 | 11.36 | 19.27 | 0.00 | 80.7 | 0.0 |

## GW7

- Train rows: 108150
- Bank: 1.60 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Marcus Rashford
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 61.41
- Actual score: 65.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.05) beats the best remaining Triple Captain opportunity (6.67).
- League average score: 0.00
- Transfer: Pascal Groß -> James Maddison (projected gain 4.19, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.05) beats the best remaining Triple Captain opportunity (6.67).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.1 | 3.68 | 10.96 | 18.28 | 6.00 | 90.4 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 4.9 | 3.43 | 9.92 | 16.51 | 2.00 | 88.1 | 90.0 |
| XI | XI | Pervis Estupiñán | DEF | 5 | 5.3 | 4.63 | 14.23 | 22.99 | -2.00 | 82.0 | 45.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.5 | 4.48 | 13.24 | 21.68 | 12.00 | 83.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.2 | 3.63 | 10.69 | 17.34 | 6.00 | 85.9 | 90.0 |
| Bench 3 | Bench | Axel Disasi | DEF | 7 | 5.1 | 2.98 | 9.22 | 14.88 | 6.00 | 82.8 | 90.0 |
| Bench 4 | Bench | Ben Chilwell | DEF | 7 | 5.7 | 2.43 | 8.07 | 14.43 | 0.00 | 38.2 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 7.9 | 4.02 | 11.97 | 20.37 | 23.00 | 73.5 | 90.0 |
| XI | XI | Carlton Morris | FWD | 12 | 5.5 | 4.98 | 11.22 | 17.05 | 10.00 | 101.5 | 167.0 |
| Bench 2 | Bench | Odsonne Edouard | FWD | 8 | 5.6 | 3.42 | 10.46 | 16.86 | 0.00 | 76.8 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.5 | 5.65 | 18.14 | 29.79 | 1.00 | 85.4 | 73.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 4.99 | 14.83 | 24.24 | 1.00 | 74.4 | 90.0 |
| XI | XI | James Maddison | MID | 18 | 7.9 | 4.75 | 14.55 | 24.60 | 2.00 | 79.5 | 89.0 |
| Vice Captain | XI | Marcus Rashford | MID | 14 | 8.9 | 5.03 | 14.54 | 23.98 | 2.00 | 82.5 | 76.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.24 | 12.88 | 22.31 | 2.00 | 76.5 | 90.0 |

## GW8

- Train rows: 108872
- Bank: 0.00 -> 0.90
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Mohamed Salah
- Effective captain: Ollie Watkins
- Chip used: bench_boost
- Predicted score: 67.75
- Actual score: 64.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (12.03) beats the best remaining Bench Boost opportunity (0.00).
- League average score: 0.00
- Transfer: Ben Chilwell -> Joachim Andersen (projected gain 1.44, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (12.03) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.96 | 11.63 | 19.33 | 1.00 | 98.3 | 90.0 |
| Bench 1 | Bench Boost | André Onana | GK | 14 | 4.9 | 3.47 | 9.80 | 15.90 | 2.00 | 86.8 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.7 | 4.68 | 14.80 | 23.98 | 6.00 | 84.3 | 90.0 |
| XI | XI | Pervis Estupiñán | DEF | 5 | 5.3 | 3.80 | 11.73 | 19.10 | 0.00 | 64.3 | 0.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 4.7 | 4.21 | 11.70 | 18.67 | 6.00 | 94.6 | 90.0 |
| Bench 2 | Bench Boost | William Saliba | DEF | 1 | 5.2 | 3.31 | 10.37 | 17.10 | 7.00 | 85.9 | 90.0 |
| Bench 3 | Bench Boost | Axel Disasi | DEF | 7 | 5.1 | 3.28 | 9.22 | 15.37 | 2.00 | 80.0 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 7.9 | 5.85 | 16.60 | 27.02 | 5.00 | 95.2 | 90.0 |
| XI | XI | Carlton Morris | FWD | 12 | 5.6 | 4.52 | 12.58 | 19.46 | 1.00 | 93.9 | 90.0 |
| Bench 4 | Bench Boost | Odsonne Edouard | FWD | 8 | 5.6 | 1.97 | 6.08 | 10.86 | 2.00 | 38.8 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.5 | 4.85 | 16.28 | 27.00 | 15.00 | 75.6 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.6 | 4.63 | 13.80 | 22.14 | 2.00 | 75.3 | 90.0 |
| XI | XI | James Maddison | MID | 18 | 7.9 | 4.46 | 13.59 | 23.32 | 6.00 | 73.1 | 75.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.29 | 13.25 | 22.10 | 2.00 | 78.2 | 90.0 |
| XI | XI | Marcus Rashford | MID | 14 | 8.9 | 4.62 | 13.08 | 21.91 | 2.00 | 66.3 | 62.0 |