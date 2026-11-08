# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW1
- Simulated weeks: GW2-GW8
- Total predicted points: 388.04
- Total actual points: 407.00
- Average predicted points: 55.43
- Average actual points: 58.14
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
- Predicted score: 52.68
- Actual score: 47.00
- League average score: 81.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 5.0 | 4.31 | 13.12 | 21.89 | 2.00 | 93.9 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 4.5 | 2.86 | 9.17 | 14.90 | 0.00 | 85.1 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.5 | 4.22 | 13.86 | 23.27 | 2.00 | 91.3 | 90.0 |
| XI | XI | Pervis Estupiñán | DEF | 5 | 5.0 | 3.87 | 12.16 | 20.61 | 11.00 | 74.9 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.0 | 3.70 | 11.04 | 18.17 | 2.00 | 85.5 | 75.0 |
| Bench 3 | Bench | Axel Disasi | DEF | 7 | 5.0 | 3.20 | 9.93 | 16.45 | 0.00 | 76.0 | 90.0 |
| Bench 2 | Bench | William Saliba | DEF | 1 | 5.0 | 3.26 | 9.75 | 16.00 | 8.00 | 86.3 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.0 | 4.53 | 13.34 | 22.83 | 5.00 | 91.5 | 73.0 |
| XI | XI | Odsonne Edouard | FWD | 8 | 5.5 | 3.43 | 9.31 | 14.50 | 2.00 | 61.3 | 90.0 |
| Bench 4 | Bench | William Osula | FWD | 17 | 4.5 | 1.80 | 5.41 | 8.82 | 2.00 | 67.3 | 73.0 |
| Captain | Captain | Marcus Rashford | MID | 14 | 9.0 | 5.32 | 15.86 | 26.20 | 2.00 | 87.2 | 84.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.5 | 4.89 | 15.18 | 25.65 | 5.00 | 78.8 | 85.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 4.71 | 13.81 | 22.70 | 12.00 | 84.8 | 80.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 3.86 | 13.76 | 24.70 | 1.00 | 86.9 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.5 | 4.51 | 13.54 | 22.59 | 1.00 | 80.7 | 80.0 |

## GW3

- Train rows: 105327
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Pervis Estupiñán
- Vice captain: Marcus Rashford
- Effective captain: Pervis Estupiñán
- Chip used: none
- Predicted score: 52.74
- Actual score: 45.00
- League average score: 51.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 5.0 | 3.90 | 11.62 | 18.92 | 0.00 | 87.8 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 4.5 | 3.07 | 8.85 | 14.81 | 2.00 | 81.7 | 90.0 |
| Captain | Captain | Pervis Estupiñán | DEF | 5 | 5.1 | 5.26 | 15.71 | 24.95 | 1.00 | 89.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.5 | 3.99 | 12.94 | 21.23 | 0.00 | 88.8 | 90.0 |
| Bench 2 | Bench | Trent Alexander-Arnold | DEF | 11 | 8.0 | 3.23 | 10.47 | 16.89 | 1.00 | 70.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.1 | 3.46 | 9.95 | 15.37 | 1.00 | 79.2 | 90.0 |
| Bench 3 | Bench | Axel Disasi | DEF | 7 | 5.0 | 2.64 | 8.05 | 12.90 | 6.00 | 65.4 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.0 | 4.12 | 12.46 | 20.89 | 5.00 | 70.4 | 85.0 |
| XI | XI | Odsonne Edouard | FWD | 8 | 5.5 | 3.55 | 9.93 | 15.37 | 2.00 | 67.5 | 70.0 |
| Bench 4 | Bench | William Osula | FWD | 17 | 4.5 | 1.45 | 5.36 | 8.94 | 1.00 | 56.7 | 70.0 |
| XI | XI | Mohamed Salah | MID | 11 | 12.5 | 4.97 | 16.57 | 26.75 | 5.00 | 76.5 | 90.0 |
| Vice Captain | XI | Marcus Rashford | MID | 14 | 9.0 | 5.23 | 15.54 | 25.38 | 7.00 | 79.8 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 4.76 | 14.61 | 23.82 | 1.00 | 80.8 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.59 | 14.49 | 24.67 | 12.00 | 82.5 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.5 | 3.64 | 11.08 | 18.59 | 10.00 | 72.0 | 90.0 |

## GW4

- Train rows: 106012
- Bank: 0.00 -> 2.30
- Free transfers: 2 -> 2
- Captain: Pervis Estupiñán
- Vice captain: Mohamed Salah
- Effective captain: Pervis Estupiñán
- Chip used: none
- Predicted score: 50.38
- Actual score: 35.00
- League average score: 0.00
- Transfer: Trent Alexander-Arnold -> Ben Chilwell (projected gain 1.64, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 5.0 | 2.92 | 9.82 | 16.64 | 0.00 | 84.2 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 4.5 | 2.64 | 7.73 | 13.13 | 1.00 | 77.3 | 90.0 |
| Captain | Captain | Pervis Estupiñán | DEF | 5 | 5.2 | 5.20 | 15.74 | 25.30 | 2.00 | 82.7 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.5 | 3.84 | 12.10 | 20.23 | 1.00 | 84.8 | 90.0 |
| XI | XI | Ben Chilwell | DEF | 7 | 5.7 | 3.67 | 10.57 | 16.58 | 1.00 | 55.2 | 61.0 |
| XI | XI | William Saliba | DEF | 1 | 5.2 | 3.47 | 10.33 | 16.32 | 2.00 | 78.1 | 90.0 |
| Bench 3 | Bench | Axel Disasi | DEF | 7 | 5.1 | 3.04 | 8.53 | 13.87 | 2.00 | 70.8 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.0 | 3.92 | 12.79 | 21.26 | 2.00 | 73.8 | 72.0 |
| Bench 2 | Bench | Odsonne Edouard | FWD | 8 | 5.5 | 3.21 | 8.93 | 13.71 | 13.00 | 60.6 | 89.0 |
| Bench 4 | Bench | William Osula | FWD | 17 | 4.5 | 2.03 | 5.94 | 9.94 | 0.00 | 55.5 | 0.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.5 | 4.95 | 15.89 | 26.62 | 8.00 | 78.4 | 90.0 |
| XI | XI | Marcus Rashford | MID | 14 | 9.0 | 4.47 | 14.82 | 25.44 | 7.00 | 81.0 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.6 | 4.77 | 14.64 | 23.71 | 5.00 | 76.1 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.10 | 14.30 | 24.66 | 2.00 | 82.0 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.4 | 3.86 | 11.85 | 20.15 | 3.00 | 78.3 | 88.0 |

## GW5

- Train rows: 106715
- Bank: 2.30 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Pervis Estupiñán
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 54.28
- Actual score: 65.00
- League average score: 0.00
- Transfer: William Osula -> Julián Álvarez (projected gain 1.61, hit 0)
- Autosub outfielders: Pascal Groß.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 5.0 | 3.11 | 9.18 | 15.90 | 2.00 | 79.5 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 4.5 | 2.19 | 7.50 | 12.76 | 3.00 | 81.4 | 90.0 |
| Vice Captain | Bench | Pervis Estupiñán | DEF | 5 | 5.3 | 5.06 | 15.34 | 25.03 | 0.00 | 90.2 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.5 | 3.80 | 11.28 | 18.71 | 8.00 | 80.9 | 90.0 |
| XI | XI | Ben Chilwell | DEF | 7 | 5.8 | 3.81 | 11.11 | 17.31 | 0.00 | 56.3 | 10.0 |
| XI | XI | William Saliba | DEF | 1 | 5.2 | 3.61 | 10.66 | 17.23 | 6.00 | 82.6 | 90.0 |
| Bench 4 | Bench | Axel Disasi | DEF | 7 | 5.1 | 3.09 | 9.36 | 15.13 | 5.00 | 76.1 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.0 | 4.26 | 12.20 | 20.27 | 5.00 | 64.3 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.6 | 4.10 | 12.15 | 19.57 | 9.00 | 77.7 | 90.0 |
| Bench 3 | Bench | Odsonne Edouard | FWD | 8 | 5.5 | 3.21 | 9.66 | 15.38 | 8.00 | 69.5 | 89.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.5 | 5.98 | 17.49 | 28.37 | 10.00 | 83.2 | 90.0 |
| XI | XI | Marcus Rashford | MID | 14 | 9.0 | 5.03 | 15.36 | 26.16 | 2.00 | 83.9 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.98 | 14.64 | 24.25 | 1.00 | 82.5 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.6 | 4.56 | 14.42 | 23.99 | 2.00 | 82.2 | 90.0 |
| Bench 2 | Autosub In | Pascal Groß | MID | 5 | 6.4 | 3.24 | 10.66 | 18.18 | 10.00 | 75.8 | 90.0 |

## GW6

- Train rows: 107432
- Bank: 0.20 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Marcus Rashford
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 52.40
- Actual score: 86.00
- League average score: 0.00
- Transfer: Jordan Pickford -> Alphonse Areola (projected gain 1.60, hit 0)
- Autosub outfielders: Odsonne Edouard.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.1 | 3.14 | 10.73 | 17.93 | 2.00 | 92.1 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 5.0 | 3.02 | 9.14 | 15.52 | 7.00 | 79.1 | 90.0 |
| XI | XI | Pervis Estupiñán | DEF | 5 | 5.3 | 4.04 | 12.14 | 19.88 | 6.00 | 53.2 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.5 | 3.76 | 11.20 | 18.44 | 18.00 | 78.0 | 69.0 |
| XI | XI | William Saliba | DEF | 1 | 5.2 | 3.78 | 11.09 | 17.76 | 1.00 | 85.6 | 90.0 |
| Bench 3 | Bench | Axel Disasi | DEF | 7 | 5.1 | 3.28 | 9.87 | 15.93 | 2.00 | 83.1 | 90.0 |
| Bench 4 | Bench | Ben Chilwell | DEF | 7 | 5.8 | 2.99 | 9.24 | 15.48 | 0.00 | 41.9 | 29.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.7 | 4.55 | 13.31 | 21.13 | 1.00 | 76.9 | 56.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.0 | 4.26 | 12.82 | 21.18 | 9.00 | 73.6 | 90.0 |
| Bench 2 | Autosub In | Odsonne Edouard | FWD | 8 | 5.5 | 3.79 | 10.62 | 17.07 | 2.00 | 71.5 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.5 | 5.58 | 17.28 | 28.63 | 10.00 | 84.9 | 90.0 |
| Vice Captain | XI | Marcus Rashford | MID | 14 | 8.9 | 4.95 | 15.34 | 25.35 | 3.00 | 85.0 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 4.71 | 13.97 | 22.77 | 14.00 | 76.9 | 45.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.18 | 13.22 | 22.50 | 10.00 | 76.6 | 90.0 |
| XI | Bench | Pascal Groß | MID | 5 | 6.3 | 3.86 | 11.37 | 19.17 | 0.00 | 80.6 | 0.0 |

## GW7

- Train rows: 108150
- Bank: 0.50 -> 1.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Marcus Rashford
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 59.25
- Actual score: 65.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.69) beats the best remaining Triple Captain opportunity (6.66).
- League average score: 0.00
- Transfer: Pascal Groß -> Pedro Lomba Neto (projected gain 1.04, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.69) beats the best remaining Triple Captain opportunity (6.66).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.1 | 3.68 | 10.99 | 18.19 | 6.00 | 90.6 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 4.9 | 3.41 | 9.77 | 16.32 | 2.00 | 86.9 | 90.0 |
| XI | XI | Pervis Estupiñán | DEF | 5 | 5.3 | 4.64 | 14.37 | 23.16 | -2.00 | 83.0 | 45.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.5 | 4.44 | 13.09 | 21.42 | 12.00 | 82.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.2 | 3.64 | 10.67 | 17.35 | 6.00 | 86.1 | 90.0 |
| Bench 3 | Bench | Axel Disasi | DEF | 7 | 5.1 | 3.01 | 9.29 | 15.09 | 6.00 | 83.5 | 90.0 |
| Bench 4 | Bench | Ben Chilwell | DEF | 7 | 5.7 | 2.44 | 8.10 | 14.50 | 0.00 | 38.7 | 0.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.25 | 13.10 | 20.69 | 8.00 | 61.6 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 7.9 | 4.01 | 11.93 | 20.39 | 23.00 | 73.3 | 90.0 |
| Bench 2 | Bench | Odsonne Edouard | FWD | 8 | 5.6 | 3.41 | 10.48 | 16.77 | 0.00 | 77.5 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.5 | 5.64 | 18.20 | 29.77 | 1.00 | 85.9 | 73.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 5.00 | 14.96 | 24.41 | 1.00 | 75.8 | 90.0 |
| Vice Captain | XI | Marcus Rashford | MID | 14 | 8.9 | 5.02 | 14.45 | 23.79 | 2.00 | 82.3 | 76.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.23 | 12.83 | 22.22 | 2.00 | 75.8 | 90.0 |
| XI | XI | Pedro Lomba Neto | MID | 20 | 5.5 | 3.41 | 11.42 | 19.48 | 4.00 | 87.6 | 90.0 |

## GW8

- Train rows: 108872
- Bank: 1.30 -> 2.20
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Mohamed Salah
- Effective captain: Ollie Watkins
- Chip used: bench_boost
- Predicted score: 66.31
- Actual score: 64.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (12.00) beats the best remaining Bench Boost opportunity (0.00).
- League average score: 0.00
- Transfer: Ben Chilwell -> Joachim Andersen (projected gain 2.54, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (12.00) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.94 | 11.56 | 19.12 | 1.00 | 97.6 | 90.0 |
| Bench 1 | Bench Boost | André Onana | GK | 14 | 4.9 | 3.47 | 9.77 | 15.95 | 2.00 | 86.4 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.7 | 4.66 | 14.68 | 23.88 | 6.00 | 83.0 | 90.0 |
| XI | XI | Pervis Estupiñán | DEF | 5 | 5.3 | 3.79 | 11.66 | 18.93 | 0.00 | 63.9 | 0.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 4.7 | 4.20 | 11.63 | 18.55 | 6.00 | 93.9 | 90.0 |
| Bench 3 | Bench Boost | William Saliba | DEF | 1 | 5.2 | 3.29 | 10.28 | 16.89 | 7.00 | 85.5 | 90.0 |
| Bench 2 | Bench Boost | Axel Disasi | DEF | 7 | 5.1 | 3.29 | 9.21 | 15.35 | 2.00 | 80.1 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 7.9 | 5.87 | 16.79 | 27.35 | 5.00 | 96.6 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 7.0 | 4.11 | 13.88 | 23.12 | 2.00 | 81.1 | 67.0 |
| Bench 4 | Bench Boost | Odsonne Edouard | FWD | 8 | 5.6 | 1.95 | 6.06 | 10.68 | 2.00 | 39.2 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.5 | 4.85 | 16.40 | 27.17 | 15.00 | 76.6 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.6 | 4.60 | 13.67 | 21.86 | 2.00 | 74.4 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.30 | 13.29 | 22.19 | 2.00 | 78.4 | 90.0 |
| XI | XI | Marcus Rashford | MID | 14 | 8.9 | 4.62 | 13.11 | 21.90 | 2.00 | 67.1 | 62.0 |
| XI | XI | Pedro Lomba Neto | MID | 20 | 5.6 | 3.50 | 10.95 | 18.67 | 5.00 | 80.0 | 90.0 |