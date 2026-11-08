# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW1
- Simulated weeks: GW2-GW8
- Total predicted points: 388.16
- Total actual points: 411.00
- Average predicted points: 55.45
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
- Predicted score: 51.75
- Actual score: 49.00
- League average score: 81.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 5.0 | 4.31 | 13.07 | 21.85 | 2.00 | 93.6 | 90.0 |
| Bench 1 | Bench | Emiliano Martínez Romero | GK | 2 | 5.0 | 2.97 | 9.15 | 15.65 | 8.00 | 93.8 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.5 | 4.19 | 13.58 | 23.01 | 2.00 | 89.3 | 90.0 |
| XI | XI | Pervis Estupiñán | DEF | 5 | 5.0 | 3.84 | 11.97 | 20.43 | 11.00 | 73.6 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.0 | 3.68 | 10.84 | 17.99 | 2.00 | 84.1 | 75.0 |
| Bench 3 | Bench | Axel Disasi | DEF | 7 | 5.0 | 3.21 | 9.61 | 16.18 | 0.00 | 73.5 | 90.0 |
| Bench 2 | Bench | William Saliba | DEF | 1 | 5.0 | 3.23 | 9.54 | 15.81 | 8.00 | 84.8 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.5 | 3.83 | 11.18 | 18.51 | 7.00 | 72.6 | 90.0 |
| XI | XI | Odsonne Edouard | FWD | 8 | 5.5 | 3.42 | 9.51 | 14.65 | 2.00 | 62.9 | 90.0 |
| Bench 4 | Bench | Carlton Morris | FWD | 12 | 5.5 | 1.86 | 7.24 | 13.50 | 0.00 | 49.8 | 0.0 |
| Captain | Captain | Marcus Rashford | MID | 14 | 9.0 | 5.31 | 15.99 | 26.30 | 2.00 | 88.3 | 84.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.5 | 4.88 | 14.98 | 25.47 | 5.00 | 77.2 | 85.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 3.82 | 13.91 | 24.81 | 1.00 | 88.2 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 4.68 | 13.60 | 22.51 | 12.00 | 83.2 | 80.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.5 | 4.48 | 13.32 | 22.38 | 1.00 | 79.2 | 80.0 |

## GW3

- Train rows: 105327
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Pervis Estupiñán
- Vice captain: Marcus Rashford
- Effective captain: Pervis Estupiñán
- Chip used: none
- Predicted score: 52.20
- Actual score: 42.00
- League average score: 0.00
- Transfer: Julián Álvarez -> Dominic Solanke (projected gain 1.28, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 5.0 | 3.90 | 11.60 | 18.89 | 0.00 | 87.6 | 90.0 |
| Bench 1 | Bench | Emiliano Martínez Romero | GK | 2 | 5.0 | 2.87 | 8.50 | 14.12 | 0.00 | 80.9 | 0.0 |
| Captain | Captain | Pervis Estupiñán | DEF | 5 | 5.1 | 5.24 | 15.54 | 24.79 | 1.00 | 87.6 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.5 | 3.98 | 12.71 | 21.02 | 0.00 | 86.9 | 90.0 |
| Bench 2 | Bench | Trent Alexander-Arnold | DEF | 11 | 8.0 | 3.23 | 10.32 | 16.74 | 1.00 | 69.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.1 | 3.45 | 9.93 | 15.35 | 1.00 | 79.0 | 90.0 |
| Bench 3 | Bench | Axel Disasi | DEF | 7 | 5.0 | 2.66 | 7.95 | 12.81 | 6.00 | 64.8 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 6.5 | 3.71 | 11.00 | 17.96 | 2.00 | 76.3 | 90.0 |
| XI | XI | Odsonne Edouard | FWD | 8 | 5.5 | 3.53 | 9.92 | 15.34 | 2.00 | 67.3 | 70.0 |
| Bench 4 | Bench | Carlton Morris | FWD | 12 | 5.5 | 1.01 | 4.16 | 8.06 | 2.00 | 26.1 | 90.0 |
| XI | XI | Mohamed Salah | MID | 11 | 12.5 | 4.97 | 16.41 | 26.58 | 5.00 | 75.2 | 90.0 |
| Vice Captain | XI | Marcus Rashford | MID | 14 | 9.0 | 5.22 | 15.60 | 25.42 | 7.00 | 80.2 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.57 | 14.53 | 24.70 | 12.00 | 82.7 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 4.75 | 14.44 | 23.65 | 1.00 | 79.4 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.5 | 3.63 | 10.88 | 18.41 | 10.00 | 70.4 | 90.0 |

## GW4

- Train rows: 106012
- Bank: 0.00 -> 2.30
- Free transfers: 2 -> 2
- Captain: Pervis Estupiñán
- Vice captain: Mohamed Salah
- Effective captain: Pervis Estupiñán
- Chip used: none
- Predicted score: 49.86
- Actual score: 40.00
- League average score: 0.00
- Transfer: Trent Alexander-Arnold -> Ben Chilwell (projected gain 1.70, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 5.0 | 2.92 | 9.80 | 16.62 | 0.00 | 84.1 | 90.0 |
| Bench 1 | Bench | Emiliano Martínez Romero | GK | 2 | 5.0 | 1.27 | 5.21 | 9.45 | 1.00 | 44.7 | 90.0 |
| Captain | Captain | Pervis Estupiñán | DEF | 5 | 5.2 | 5.20 | 15.63 | 25.21 | 2.00 | 81.8 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.5 | 3.84 | 11.96 | 20.10 | 1.00 | 83.6 | 90.0 |
| XI | XI | Ben Chilwell | DEF | 7 | 5.7 | 3.68 | 10.57 | 16.59 | 1.00 | 55.3 | 61.0 |
| XI | XI | William Saliba | DEF | 1 | 5.2 | 3.47 | 10.33 | 16.32 | 2.00 | 78.0 | 90.0 |
| Bench 3 | Bench | Axel Disasi | DEF | 7 | 5.1 | 3.05 | 8.52 | 13.85 | 2.00 | 70.8 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 6.5 | 3.43 | 10.21 | 16.95 | 7.00 | 76.2 | 90.0 |
| Bench 2 | Bench | Odsonne Edouard | FWD | 8 | 5.5 | 3.20 | 8.88 | 13.66 | 13.00 | 60.2 | 89.0 |
| Bench 4 | Bench | Carlton Morris | FWD | 12 | 5.5 | 2.38 | 7.01 | 12.02 | 5.00 | 56.4 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.5 | 4.94 | 15.71 | 26.44 | 8.00 | 76.9 | 90.0 |
| XI | XI | Marcus Rashford | MID | 14 | 9.0 | 4.47 | 14.85 | 25.45 | 7.00 | 81.2 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.6 | 4.77 | 14.53 | 23.61 | 5.00 | 75.1 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.09 | 14.33 | 24.67 | 2.00 | 82.2 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.4 | 3.85 | 11.74 | 20.04 | 3.00 | 77.4 | 88.0 |

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
- Transfer: Dominic Solanke -> Ollie Watkins (projected gain 2.13, hit 0)
- Autosub outfielders: Odsonne Edouard.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 5.0 | 3.12 | 9.23 | 15.99 | 2.00 | 79.8 | 90.0 |
| Bench 1 | Bench | Emiliano Martínez Romero | GK | 2 | 5.0 | 2.59 | 7.33 | 12.39 | 2.00 | 63.9 | 90.0 |
| Vice Captain | Bench | Pervis Estupiñán | DEF | 5 | 5.3 | 5.06 | 15.23 | 24.93 | 0.00 | 89.5 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.5 | 3.82 | 11.27 | 18.78 | 8.00 | 80.8 | 90.0 |
| XI | XI | Ben Chilwell | DEF | 7 | 5.8 | 3.84 | 11.15 | 17.44 | 0.00 | 56.8 | 10.0 |
| XI | XI | William Saliba | DEF | 1 | 5.2 | 3.62 | 10.65 | 17.31 | 6.00 | 82.5 | 90.0 |
| Bench 3 | Bench | Axel Disasi | DEF | 7 | 5.1 | 3.11 | 9.36 | 15.26 | 5.00 | 75.7 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.0 | 4.25 | 12.24 | 20.16 | 5.00 | 64.6 | 90.0 |
| Bench 2 | Autosub In | Odsonne Edouard | FWD | 8 | 5.5 | 3.19 | 9.49 | 15.05 | 8.00 | 68.4 | 89.0 |
| Bench 4 | Bench | Carlton Morris | FWD | 12 | 5.5 | 2.35 | 7.30 | 12.48 | 2.00 | 55.7 | 73.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.5 | 5.98 | 17.41 | 28.34 | 10.00 | 82.3 | 90.0 |
| XI | XI | Marcus Rashford | MID | 14 | 9.0 | 5.04 | 15.42 | 26.16 | 2.00 | 84.8 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.98 | 14.70 | 24.25 | 1.00 | 83.4 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.6 | 4.56 | 14.32 | 23.93 | 2.00 | 81.5 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.4 | 3.24 | 10.67 | 18.27 | 10.00 | 75.8 | 90.0 |

## GW6

- Train rows: 107432
- Bank: 0.80 -> 1.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Marcus Rashford
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 51.71
- Actual score: 87.00
- League average score: 0.00
- Transfer: Emiliano Martínez Romero -> Alphonse Areola (projected gain 1.45, hit 0)
- Autosub outfielders: Axel Disasi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.1 | 3.14 | 10.65 | 17.93 | 2.00 | 91.1 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 5.0 | 3.04 | 9.24 | 15.69 | 7.00 | 79.9 | 90.0 |
| XI | XI | Pervis Estupiñán | DEF | 5 | 5.3 | 4.06 | 12.10 | 19.92 | 6.00 | 53.1 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.5 | 3.80 | 11.31 | 18.76 | 18.00 | 79.0 | 69.0 |
| XI | XI | William Saliba | DEF | 1 | 5.2 | 3.79 | 11.12 | 17.82 | 1.00 | 85.9 | 90.0 |
| Bench 2 | Autosub In | Axel Disasi | DEF | 7 | 5.1 | 3.28 | 9.83 | 15.95 | 2.00 | 82.4 | 90.0 |
| Bench 3 | Bench | Ben Chilwell | DEF | 7 | 5.8 | 3.00 | 9.24 | 15.52 | 0.00 | 41.8 | 29.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.0 | 4.24 | 12.75 | 20.87 | 9.00 | 73.2 | 90.0 |
| XI | XI | Odsonne Edouard | FWD | 8 | 5.5 | 3.76 | 10.45 | 16.80 | 2.00 | 70.4 | 90.0 |
| Bench 4 | Bench | Carlton Morris | FWD | 12 | 5.5 | 2.66 | 7.78 | 13.14 | 9.00 | 56.8 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.5 | 5.58 | 17.20 | 28.60 | 10.00 | 84.2 | 90.0 |
| Vice Captain | XI | Marcus Rashford | MID | 14 | 8.9 | 4.97 | 15.42 | 25.41 | 3.00 | 86.0 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 4.72 | 13.88 | 22.73 | 14.00 | 76.2 | 45.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.21 | 13.34 | 22.64 | 10.00 | 78.0 | 90.0 |
| XI | Bench | Pascal Groß | MID | 5 | 6.3 | 3.87 | 11.39 | 19.32 | 0.00 | 80.6 | 0.0 |

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
- Transfer: Pascal Groß -> James Maddison (projected gain 4.27, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.05) beats the best remaining Triple Captain opportunity (6.67).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.1 | 3.69 | 10.98 | 18.32 | 6.00 | 90.4 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 4.9 | 3.42 | 9.89 | 16.49 | 2.00 | 87.9 | 90.0 |
| XI | XI | Pervis Estupiñán | DEF | 5 | 5.3 | 4.64 | 14.26 | 23.03 | -2.00 | 82.1 | 45.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.5 | 4.47 | 13.24 | 21.70 | 12.00 | 83.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.2 | 3.63 | 10.67 | 17.29 | 6.00 | 86.2 | 90.0 |
| Bench 3 | Bench | Axel Disasi | DEF | 7 | 5.1 | 2.98 | 9.23 | 14.88 | 6.00 | 82.8 | 90.0 |
| Bench 4 | Bench | Ben Chilwell | DEF | 7 | 5.7 | 2.43 | 8.07 | 14.41 | 0.00 | 38.4 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 7.9 | 4.01 | 11.92 | 20.35 | 23.00 | 73.2 | 90.0 |
| XI | XI | Carlton Morris | FWD | 12 | 5.5 | 4.99 | 11.24 | 17.11 | 10.00 | 101.3 | 167.0 |
| Bench 2 | Bench | Odsonne Edouard | FWD | 8 | 5.6 | 3.41 | 10.40 | 16.77 | 0.00 | 76.8 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.5 | 5.65 | 18.13 | 29.78 | 1.00 | 85.4 | 73.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 4.99 | 14.79 | 24.19 | 1.00 | 74.4 | 90.0 |
| XI | XI | James Maddison | MID | 18 | 7.9 | 4.75 | 14.58 | 24.63 | 2.00 | 79.5 | 89.0 |
| Vice Captain | XI | Marcus Rashford | MID | 14 | 8.9 | 5.03 | 14.52 | 23.94 | 2.00 | 82.6 | 76.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.25 | 12.91 | 22.37 | 2.00 | 76.5 | 90.0 |

## GW8

- Train rows: 108872
- Bank: 0.00 -> 0.90
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Mohamed Salah
- Effective captain: Ollie Watkins
- Chip used: bench_boost
- Predicted score: 67.74
- Actual score: 64.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (12.01) beats the best remaining Bench Boost opportunity (0.00).
- League average score: 0.00
- Transfer: Ben Chilwell -> Joachim Andersen (projected gain 1.47, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (12.01) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.96 | 11.64 | 19.37 | 1.00 | 98.1 | 90.0 |
| Bench 1 | Bench Boost | André Onana | GK | 14 | 4.9 | 3.47 | 9.79 | 15.91 | 2.00 | 86.6 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.7 | 4.68 | 14.80 | 24.00 | 6.00 | 84.2 | 90.0 |
| XI | XI | Pervis Estupiñán | DEF | 5 | 5.3 | 3.81 | 11.73 | 19.09 | 0.00 | 64.5 | 0.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 4.7 | 4.21 | 11.70 | 18.70 | 6.00 | 94.5 | 90.0 |
| Bench 2 | Bench Boost | William Saliba | DEF | 1 | 5.2 | 3.31 | 10.35 | 17.04 | 7.00 | 86.0 | 90.0 |
| Bench 3 | Bench Boost | Axel Disasi | DEF | 7 | 5.1 | 3.28 | 9.21 | 15.36 | 2.00 | 80.0 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 7.9 | 5.86 | 16.61 | 27.07 | 5.00 | 95.0 | 90.0 |
| XI | XI | Carlton Morris | FWD | 12 | 5.6 | 4.52 | 12.58 | 19.46 | 1.00 | 93.7 | 90.0 |
| Bench 4 | Bench Boost | Odsonne Edouard | FWD | 8 | 5.6 | 1.96 | 6.04 | 10.79 | 2.00 | 38.8 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.5 | 4.85 | 16.27 | 26.96 | 15.00 | 75.7 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.6 | 4.63 | 13.78 | 22.08 | 2.00 | 75.5 | 90.0 |
| XI | XI | James Maddison | MID | 18 | 7.9 | 4.45 | 13.59 | 23.33 | 6.00 | 73.1 | 75.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.30 | 13.29 | 22.16 | 2.00 | 78.2 | 90.0 |
| XI | XI | Marcus Rashford | MID | 14 | 8.9 | 4.62 | 13.09 | 21.88 | 2.00 | 66.6 | 62.0 |