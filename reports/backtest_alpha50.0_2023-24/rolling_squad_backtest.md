# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW1
- Simulated weeks: GW2-GW8
- Total predicted points: 385.18
- Total actual points: 389.00
- Average predicted points: 55.03
- Average actual points: 55.57
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
- Predicted score: 52.04
- Actual score: 48.00
- League average score: 81.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 5.0 | 4.31 | 13.08 | 21.85 | 2.00 | 93.7 | 90.0 |
| Bench 1 | Bench | Emiliano Martínez Romero | GK | 2 | 5.0 | 2.97 | 9.18 | 15.72 | 8.00 | 93.6 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.5 | 4.19 | 13.58 | 22.99 | 2.00 | 89.3 | 90.0 |
| XI | XI | Pervis Estupiñán | DEF | 5 | 5.0 | 3.91 | 12.06 | 20.46 | 11.00 | 75.0 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.0 | 3.68 | 10.88 | 18.09 | 2.00 | 83.6 | 75.0 |
| Bench 4 | Bench | Axel Disasi | DEF | 7 | 5.0 | 3.22 | 9.66 | 16.30 | 0.00 | 73.2 | 90.0 |
| Bench 3 | Bench | William Saliba | DEF | 1 | 5.0 | 3.23 | 9.50 | 15.69 | 8.00 | 85.3 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.5 | 3.84 | 11.13 | 18.32 | 7.00 | 73.4 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 3.77 | 10.85 | 18.02 | 0.00 | 71.3 | 33.0 |
| Bench 2 | Bench | Odsonne Edouard | FWD | 8 | 5.5 | 3.45 | 9.63 | 14.88 | 2.00 | 62.6 | 90.0 |
| Captain | Captain | Marcus Rashford | MID | 14 | 9.0 | 5.31 | 16.06 | 26.49 | 2.00 | 87.6 | 84.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.5 | 4.88 | 14.99 | 25.53 | 5.00 | 77.2 | 85.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 3.86 | 13.97 | 24.84 | 1.00 | 89.0 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 4.69 | 13.64 | 22.61 | 12.00 | 82.9 | 80.0 |
| XI | XI | Eberechi Eze | MID | 8 | 6.5 | 4.30 | 13.01 | 21.46 | 2.00 | 76.3 | 90.0 |

## GW3

- Train rows: 105327
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Pervis Estupiñán
- Vice captain: Marcus Rashford
- Effective captain: Pervis Estupiñán
- Chip used: none
- Predicted score: 52.58
- Actual score: 34.00
- League average score: 51.00
- Transfer: Julián Álvarez -> Dominic Solanke (projected gain 1.35, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 5.0 | 3.90 | 11.62 | 18.94 | 0.00 | 87.5 | 90.0 |
| Bench 1 | Bench | Emiliano Martínez Romero | GK | 2 | 5.0 | 2.87 | 8.48 | 14.09 | 0.00 | 81.0 | 0.0 |
| Captain | Captain | Pervis Estupiñán | DEF | 5 | 5.1 | 5.24 | 15.48 | 24.64 | 1.00 | 88.1 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.5 | 3.98 | 12.70 | 20.99 | 0.00 | 87.0 | 90.0 |
| Bench 2 | Bench | Trent Alexander-Arnold | DEF | 11 | 8.0 | 3.23 | 10.37 | 16.89 | 1.00 | 68.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.1 | 3.45 | 9.94 | 15.35 | 1.00 | 79.0 | 90.0 |
| Bench 4 | Bench | Axel Disasi | DEF | 7 | 5.0 | 2.66 | 7.96 | 12.81 | 6.00 | 64.8 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 6.5 | 3.72 | 11.06 | 18.08 | 2.00 | 76.0 | 90.0 |
| XI | XI | Odsonne Edouard | FWD | 8 | 5.5 | 3.55 | 10.01 | 15.54 | 2.00 | 66.9 | 70.0 |
| Bench 3 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 3.04 | 9.47 | 15.33 | 1.00 | 48.0 | 30.0 |
| XI | XI | Mohamed Salah | MID | 11 | 12.5 | 4.97 | 16.41 | 26.59 | 5.00 | 75.3 | 90.0 |
| Vice Captain | XI | Marcus Rashford | MID | 14 | 9.0 | 5.23 | 15.64 | 25.55 | 7.00 | 79.7 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.57 | 14.50 | 24.62 | 12.00 | 82.9 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 4.75 | 14.48 | 23.75 | 1.00 | 79.3 | 90.0 |
| XI | XI | Eberechi Eze | MID | 8 | 6.5 | 3.97 | 11.92 | 19.78 | 2.00 | 72.6 | 90.0 |

## GW4

- Train rows: 106012
- Bank: 0.00 -> 2.30
- Free transfers: 2 -> 2
- Captain: Pervis Estupiñán
- Vice captain: Mohamed Salah
- Effective captain: Pervis Estupiñán
- Chip used: none
- Predicted score: 49.89
- Actual score: 45.00
- League average score: 0.00
- Transfer: Trent Alexander-Arnold -> Ben Chilwell (projected gain 1.59, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 5.0 | 2.92 | 9.84 | 16.71 | 0.00 | 83.9 | 90.0 |
| Bench 1 | Bench | Emiliano Martínez Romero | GK | 2 | 5.0 | 1.27 | 5.20 | 9.43 | 1.00 | 44.8 | 90.0 |
| Captain | Captain | Pervis Estupiñán | DEF | 5 | 5.2 | 5.20 | 15.59 | 25.10 | 2.00 | 82.1 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.5 | 3.84 | 11.96 | 20.11 | 1.00 | 83.6 | 90.0 |
| XI | XI | Ben Chilwell | DEF | 7 | 5.7 | 3.68 | 10.56 | 16.56 | 1.00 | 55.6 | 61.0 |
| XI | XI | William Saliba | DEF | 1 | 5.2 | 3.48 | 10.33 | 16.31 | 2.00 | 78.1 | 90.0 |
| Bench 3 | Bench | Axel Disasi | DEF | 7 | 5.1 | 3.06 | 8.53 | 13.86 | 2.00 | 70.8 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 6.5 | 3.43 | 10.26 | 17.05 | 7.00 | 75.9 | 90.0 |
| Bench 2 | Bench | Odsonne Edouard | FWD | 8 | 5.5 | 3.22 | 8.98 | 13.87 | 13.00 | 59.7 | 89.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.6 | 2.48 | 8.07 | 14.16 | 2.00 | 39.5 | 76.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.5 | 4.94 | 15.73 | 26.50 | 8.00 | 76.8 | 90.0 |
| XI | XI | Marcus Rashford | MID | 14 | 9.0 | 4.47 | 14.89 | 25.57 | 7.00 | 80.8 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.6 | 4.77 | 14.58 | 23.75 | 5.00 | 74.8 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.09 | 14.31 | 24.60 | 2.00 | 82.5 | 90.0 |
| XI | XI | Eberechi Eze | MID | 8 | 6.4 | 3.86 | 11.34 | 18.70 | 8.00 | 71.4 | 90.0 |

## GW5

- Train rows: 106715
- Bank: 2.30 -> 0.80
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Pervis Estupiñán
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 53.79
- Actual score: 55.00
- League average score: 0.00
- Transfer: Dominic Solanke -> Ollie Watkins (projected gain 2.05, hit 0)
- Autosub outfielders: Odsonne Edouard.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 5.0 | 3.12 | 9.25 | 16.04 | 2.00 | 79.7 | 90.0 |
| Bench 1 | Bench | Emiliano Martínez Romero | GK | 2 | 5.0 | 2.57 | 7.31 | 12.34 | 2.00 | 63.9 | 90.0 |
| Vice Captain | Bench | Pervis Estupiñán | DEF | 5 | 5.3 | 5.06 | 15.20 | 24.84 | 0.00 | 89.7 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.5 | 3.82 | 11.26 | 18.76 | 8.00 | 81.0 | 90.0 |
| XI | XI | Ben Chilwell | DEF | 7 | 5.8 | 3.84 | 11.15 | 17.47 | 0.00 | 57.0 | 10.0 |
| XI | XI | William Saliba | DEF | 1 | 5.2 | 3.62 | 10.64 | 17.32 | 6.00 | 82.2 | 90.0 |
| Bench 3 | Bench | Axel Disasi | DEF | 7 | 5.1 | 3.12 | 9.37 | 15.27 | 5.00 | 75.9 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.0 | 4.24 | 12.24 | 20.20 | 5.00 | 64.6 | 90.0 |
| Bench 2 | Autosub In | Odsonne Edouard | FWD | 8 | 5.5 | 3.21 | 9.59 | 15.26 | 8.00 | 68.2 | 89.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 2.03 | 7.61 | 14.04 | 7.00 | 45.2 | 26.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.5 | 5.98 | 17.42 | 28.35 | 10.00 | 82.4 | 90.0 |
| XI | XI | Marcus Rashford | MID | 14 | 9.0 | 5.04 | 15.47 | 26.22 | 2.00 | 84.8 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.97 | 14.64 | 24.10 | 1.00 | 83.8 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.6 | 4.57 | 14.37 | 24.03 | 2.00 | 81.4 | 90.0 |
| XI | XI | Eberechi Eze | MID | 8 | 6.4 | 3.55 | 11.24 | 18.67 | 1.00 | 76.1 | 90.0 |

## GW6

- Train rows: 107432
- Bank: 0.80 -> 1.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Marcus Rashford
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 51.53
- Actual score: 88.00
- League average score: 0.00
- Transfer: Emiliano Martínez Romero -> Alphonse Areola (projected gain 1.40, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.1 | 3.13 | 10.61 | 17.86 | 2.00 | 91.3 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 5.0 | 3.05 | 9.26 | 15.72 | 7.00 | 79.9 | 90.0 |
| XI | XI | Pervis Estupiñán | DEF | 5 | 5.3 | 4.06 | 12.06 | 19.85 | 6.00 | 53.1 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.5 | 3.80 | 11.29 | 18.71 | 18.00 | 79.2 | 69.0 |
| XI | XI | William Saliba | DEF | 1 | 5.2 | 3.78 | 11.12 | 17.83 | 1.00 | 85.7 | 90.0 |
| Bench 2 | Bench | Axel Disasi | DEF | 7 | 5.1 | 3.27 | 9.83 | 15.96 | 2.00 | 82.3 | 90.0 |
| Bench 3 | Bench | Ben Chilwell | DEF | 7 | 5.8 | 3.00 | 9.24 | 15.55 | 0.00 | 42.0 | 29.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.0 | 4.23 | 12.77 | 20.89 | 9.00 | 73.3 | 90.0 |
| XI | XI | Odsonne Edouard | FWD | 8 | 5.5 | 3.77 | 10.52 | 16.95 | 2.00 | 70.3 | 90.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 2.62 | 8.12 | 14.61 | 1.00 | 40.6 | 27.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.5 | 5.58 | 17.21 | 28.65 | 10.00 | 83.9 | 90.0 |
| Vice Captain | XI | Marcus Rashford | MID | 14 | 8.9 | 4.98 | 15.47 | 25.49 | 3.00 | 85.8 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 4.73 | 13.93 | 22.82 | 14.00 | 76.1 | 45.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.20 | 13.30 | 22.54 | 10.00 | 78.2 | 90.0 |
| XI | XI | Eberechi Eze | MID | 8 | 6.3 | 3.68 | 10.90 | 18.11 | 3.00 | 73.1 | 90.0 |

## GW7

- Train rows: 108150
- Bank: 1.60 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Marcus Rashford
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 59.35
- Actual score: 67.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.70) beats the best remaining Triple Captain opportunity (6.66).
- League average score: 0.00
- Transfer: João Pedro Junqueira de Jesus -> Julián Álvarez (projected gain 2.58, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.70) beats the best remaining Triple Captain opportunity (6.66).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.1 | 3.68 | 10.94 | 18.24 | 6.00 | 90.4 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 4.9 | 3.43 | 9.93 | 16.51 | 2.00 | 88.2 | 90.0 |
| XI | XI | Pervis Estupiñán | DEF | 5 | 5.3 | 4.62 | 14.20 | 22.95 | -2.00 | 81.9 | 45.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.5 | 4.49 | 13.25 | 21.68 | 12.00 | 84.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.2 | 3.64 | 10.71 | 17.40 | 6.00 | 85.8 | 90.0 |
| Bench 3 | Bench | Axel Disasi | DEF | 7 | 5.1 | 2.99 | 9.24 | 14.90 | 6.00 | 82.8 | 90.0 |
| Bench 4 | Bench | Ben Chilwell | DEF | 7 | 5.7 | 2.45 | 8.11 | 14.48 | 0.00 | 38.3 | 0.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.26 | 12.98 | 20.44 | 8.00 | 61.1 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 7.9 | 4.02 | 11.98 | 20.37 | 23.00 | 73.6 | 90.0 |
| Bench 2 | Bench | Odsonne Edouard | FWD | 8 | 5.6 | 3.42 | 10.48 | 16.89 | 0.00 | 76.6 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.5 | 5.65 | 18.13 | 29.78 | 1.00 | 85.4 | 73.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 4.99 | 14.82 | 24.23 | 1.00 | 74.3 | 90.0 |
| Vice Captain | XI | Marcus Rashford | MID | 14 | 8.9 | 5.03 | 14.54 | 23.99 | 2.00 | 82.3 | 76.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.25 | 12.87 | 22.28 | 2.00 | 76.6 | 90.0 |
| XI | XI | Eberechi Eze | MID | 8 | 6.3 | 3.44 | 10.72 | 17.68 | 6.00 | 78.7 | 87.0 |

## GW8

- Train rows: 108872
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Mohamed Salah
- Effective captain: Ollie Watkins
- Chip used: bench_boost
- Predicted score: 65.99
- Actual score: 52.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.52) beats the best remaining Bench Boost opportunity (0.00).
- League average score: 0.00
- Transfer: Odsonne Edouard -> Carlton Morris (projected gain 1.64, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.52) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.96 | 11.62 | 19.30 | 1.00 | 98.5 | 90.0 |
| Bench 1 | Bench Boost | André Onana | GK | 14 | 4.9 | 3.46 | 9.79 | 15.88 | 2.00 | 86.8 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.7 | 4.68 | 14.80 | 23.99 | 6.00 | 84.3 | 90.0 |
| XI | XI | Pervis Estupiñán | DEF | 5 | 5.3 | 3.80 | 11.72 | 19.11 | 0.00 | 64.2 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.2 | 3.32 | 10.40 | 17.15 | 7.00 | 85.8 | 90.0 |
| Bench 3 | Bench Boost | Axel Disasi | DEF | 7 | 5.1 | 3.29 | 9.24 | 15.40 | 2.00 | 80.1 | 90.0 |
| Bench 4 | Bench Boost | Ben Chilwell | DEF | 7 | 5.6 | 1.07 | 4.53 | 9.83 | 0.00 | 9.3 | 0.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 7.9 | 5.84 | 16.55 | 26.94 | 5.00 | 95.2 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 7.0 | 4.14 | 13.76 | 23.12 | 2.00 | 80.0 | 67.0 |
| XI | XI | Carlton Morris | FWD | 12 | 5.6 | 4.52 | 12.59 | 19.46 | 1.00 | 94.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.5 | 4.85 | 16.29 | 27.03 | 15.00 | 75.6 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.6 | 4.63 | 13.81 | 22.17 | 2.00 | 75.2 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.29 | 13.22 | 22.05 | 2.00 | 78.2 | 90.0 |
| XI | XI | Marcus Rashford | MID | 14 | 8.9 | 4.61 | 13.06 | 21.91 | 2.00 | 66.1 | 62.0 |
| Bench 2 | Bench Boost | Eberechi Eze | MID | 8 | 6.2 | 3.70 | 11.07 | 18.31 | 0.00 | 78.8 | 0.0 |