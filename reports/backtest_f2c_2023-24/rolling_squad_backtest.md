# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW1
- Simulated weeks: GW2-GW8
- Total predicted points: 404.88
- Total actual points: 419.00
- Average predicted points: 57.84
- Average actual points: 59.86
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
- Bank: 100.00 -> 0.50
- Free transfers: 1 -> 2
- Captain: Marcus Rashford
- Vice captain: Bukayo Saka
- Effective captain: Marcus Rashford
- Chip used: none
- Predicted score: 53.28
- Actual score: 50.00
- League average score: 81.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 5.0 | 4.29 | 13.06 | 21.80 | 2.00 | 94.0 | 90.0 |
| Bench 1 | Bench | Emiliano Martínez Romero | GK | 2 | 5.0 | 3.10 | 9.50 | 16.28 | 8.00 | 93.4 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.5 | 4.18 | 13.57 | 22.98 | 2.00 | 91.4 | 90.0 |
| XI | XI | Pervis Estupiñán | DEF | 5 | 5.0 | 3.88 | 12.04 | 20.43 | 11.00 | 74.7 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.0 | 3.61 | 10.62 | 17.61 | 2.00 | 82.2 | 75.0 |
| Bench 4 | Bench | Axel Disasi | DEF | 7 | 5.0 | 3.32 | 9.93 | 16.59 | 0.00 | 78.6 | 90.0 |
| Bench 3 | Bench | William Saliba | DEF | 1 | 5.0 | 3.34 | 9.84 | 16.19 | 8.00 | 85.4 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.0 | 4.73 | 14.06 | 23.76 | 5.00 | 93.4 | 73.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.5 | 3.95 | 11.50 | 18.89 | 7.00 | 73.5 | 90.0 |
| Bench 2 | Bench | Dominic Solanke | FWD | 3 | 6.5 | 3.45 | 10.44 | 16.69 | 5.00 | 71.7 | 90.0 |
| Captain | Captain | Marcus Rashford | MID | 14 | 9.0 | 5.29 | 15.96 | 26.23 | 2.00 | 88.7 | 84.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.5 | 5.07 | 14.38 | 23.44 | 3.00 | 83.9 | 88.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 3.78 | 13.84 | 24.67 | 1.00 | 88.3 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 4.70 | 13.63 | 22.44 | 12.00 | 84.2 | 80.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.5 | 4.50 | 13.38 | 22.35 | 1.00 | 80.3 | 80.0 |

## GW3

- Train rows: 105327
- Bank: 0.50 -> 0.50
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Bryan Mbeumo
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 55.51
- Actual score: 47.00
- League average score: 0.00
- Transfer: Pascal Groß -> Bryan Mbeumo (projected gain 4.07, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 5.0 | 3.94 | 11.73 | 19.05 | 0.00 | 87.6 | 90.0 |
| Bench 1 | Bench | Emiliano Martínez Romero | GK | 2 | 5.0 | 2.91 | 8.62 | 14.32 | 0.00 | 81.6 | 0.0 |
| XI | XI | Pervis Estupiñán | DEF | 5 | 5.1 | 5.28 | 15.59 | 24.78 | 1.00 | 88.3 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.5 | 3.98 | 12.73 | 21.05 | 0.00 | 87.0 | 90.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | 11 | 8.0 | 3.23 | 10.31 | 16.73 | 1.00 | 69.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.1 | 3.41 | 9.86 | 15.35 | 1.00 | 79.2 | 90.0 |
| Bench 4 | Bench | Axel Disasi | DEF | 7 | 5.0 | 2.70 | 8.08 | 13.03 | 6.00 | 67.1 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.0 | 4.18 | 12.85 | 21.33 | 5.00 | 73.3 | 85.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 6.5 | 3.74 | 11.08 | 18.04 | 2.00 | 76.5 | 90.0 |
| Bench 2 | Bench | Julián Álvarez | FWD | 13 | 6.5 | 3.46 | 9.98 | 15.83 | 2.00 | 70.9 | 90.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 8.6 | 5.46 | 16.07 | 24.56 | 8.00 | 80.0 | 90.0 |
| XI | XI | Marcus Rashford | MID | 14 | 9.0 | 5.28 | 15.75 | 25.61 | 7.00 | 80.3 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 6.5 | 5.39 | 15.00 | 22.25 | 2.00 | 90.6 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.61 | 14.64 | 24.82 | 12.00 | 82.5 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 4.77 | 14.46 | 23.60 | 1.00 | 80.0 | 90.0 |

## GW4

- Train rows: 106012
- Bank: 0.50 -> 2.80
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Pervis Estupiñán
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 53.15
- Actual score: 50.00
- League average score: 0.00
- Transfer: Trent Alexander-Arnold -> Ben Chilwell (projected gain 0.71, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 5.0 | 2.86 | 9.63 | 16.36 | 0.00 | 83.3 | 90.0 |
| Bench 1 | Bench | Emiliano Martínez Romero | GK | 2 | 5.0 | 1.28 | 5.24 | 9.50 | 1.00 | 45.1 | 90.0 |
| Vice Captain | XI | Pervis Estupiñán | DEF | 5 | 5.2 | 5.18 | 15.59 | 25.15 | 2.00 | 82.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.5 | 3.86 | 12.00 | 20.15 | 1.00 | 83.5 | 90.0 |
| XI | XI | Ben Chilwell | DEF | 7 | 5.7 | 3.79 | 10.88 | 17.04 | 1.00 | 57.7 | 61.0 |
| Bench 3 | Bench | William Saliba | DEF | 1 | 5.2 | 3.42 | 10.18 | 16.09 | 2.00 | 77.0 | 90.0 |
| Bench 4 | Bench | Axel Disasi | DEF | 7 | 5.1 | 3.17 | 8.85 | 14.35 | 2.00 | 73.5 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.0 | 3.95 | 12.95 | 21.42 | 2.00 | 75.4 | 72.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.6 | 3.92 | 11.19 | 17.34 | 14.00 | 66.4 | 89.0 |
| Bench 2 | Bench | Dominic Solanke | FWD | 3 | 6.5 | 3.48 | 10.35 | 17.14 | 7.00 | 76.7 | 90.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 8.6 | 6.02 | 18.11 | 29.03 | 4.00 | 88.5 | 90.0 |
| XI | XI | Marcus Rashford | MID | 14 | 9.0 | 4.41 | 14.68 | 25.20 | 7.00 | 80.4 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.6 | 4.74 | 14.45 | 23.51 | 5.00 | 75.1 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.01 | 14.12 | 24.36 | 2.00 | 81.1 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.7 | 4.40 | 13.66 | 20.58 | 8.00 | 66.3 | 90.0 |

## GW5

- Train rows: 106715
- Bank: 2.80 -> 2.30
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Pervis Estupiñán
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 56.53
- Actual score: 49.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- League average score: 0.00
- Transfer: Emiliano Martínez Romero -> Alisson Ramses Becker (projected gain 0.54, hit 0)
- Autosub outfielders: William Saliba.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alisson Ramses Becker | GK | 11 | 5.5 | 3.28 | 9.73 | 16.11 | 2.00 | 86.0 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 5.0 | 3.12 | 9.21 | 15.95 | 2.00 | 79.5 | 90.0 |
| Vice Captain | Bench | Pervis Estupiñán | DEF | 5 | 5.3 | 5.04 | 15.17 | 24.86 | 0.00 | 89.5 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.5 | 3.88 | 11.43 | 19.04 | 8.00 | 81.1 | 90.0 |
| XI | XI | Ben Chilwell | DEF | 7 | 5.8 | 3.80 | 11.06 | 17.33 | 0.00 | 56.7 | 10.0 |
| Bench 2 | Autosub In | William Saliba | DEF | 1 | 5.2 | 3.58 | 10.54 | 17.16 | 6.00 | 81.8 | 90.0 |
| Bench 4 | Bench | Axel Disasi | DEF | 7 | 5.1 | 3.08 | 9.27 | 15.15 | 5.00 | 75.7 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.0 | 4.30 | 12.38 | 20.38 | 5.00 | 65.2 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.6 | 4.14 | 12.23 | 19.58 | 9.00 | 77.3 | 90.0 |
| Bench 3 | Bench | Dominic Solanke | FWD | 3 | 6.5 | 3.29 | 10.15 | 17.30 | 2.00 | 78.5 | 90.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 8.7 | 6.51 | 18.82 | 29.57 | 6.00 | 92.6 | 90.0 |
| XI | XI | Marcus Rashford | MID | 14 | 9.0 | 5.04 | 15.40 | 26.12 | 2.00 | 84.4 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.97 | 14.65 | 24.16 | 1.00 | 82.8 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 4.54 | 14.53 | 23.47 | 2.00 | 83.1 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.6 | 4.53 | 14.23 | 23.81 | 2.00 | 81.3 | 90.0 |

## GW6

- Train rows: 107432
- Bank: 2.30 -> 3.70
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Marcus Rashford
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 53.98
- Actual score: 91.00
- League average score: 0.00
- Transfer: Alisson Ramses Becker -> Alphonse Areola (projected gain 1.42, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.1 | 3.15 | 10.67 | 17.96 | 2.00 | 91.6 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 5.0 | 3.04 | 9.23 | 15.68 | 7.00 | 79.8 | 90.0 |
| XI | XI | Pervis Estupiñán | DEF | 5 | 5.3 | 4.05 | 12.06 | 19.86 | 6.00 | 53.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.5 | 3.80 | 11.31 | 18.77 | 18.00 | 78.8 | 69.0 |
| XI | XI | William Saliba | DEF | 1 | 5.2 | 3.80 | 11.15 | 17.84 | 1.00 | 85.8 | 90.0 |
| Bench 3 | Bench | Axel Disasi | DEF | 7 | 5.1 | 3.28 | 9.84 | 15.96 | 2.00 | 82.5 | 90.0 |
| Bench 4 | Bench | Ben Chilwell | DEF | 7 | 5.8 | 3.00 | 9.26 | 15.56 | 0.00 | 41.9 | 29.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.7 | 4.56 | 13.24 | 20.88 | 1.00 | 76.7 | 56.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.0 | 4.25 | 12.79 | 20.93 | 9.00 | 73.3 | 90.0 |
| Bench 2 | Bench | Dominic Solanke | FWD | 3 | 6.5 | 3.34 | 10.35 | 17.29 | 6.00 | 77.3 | 90.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 8.7 | 6.18 | 18.38 | 29.12 | 13.00 | 95.4 | 90.0 |
| Vice Captain | XI | Marcus Rashford | MID | 14 | 8.9 | 4.97 | 15.41 | 25.38 | 3.00 | 85.9 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 4.70 | 13.81 | 22.63 | 14.00 | 75.9 | 45.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.19 | 13.30 | 22.56 | 10.00 | 77.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 4.15 | 13.08 | 22.13 | 1.00 | 73.3 | 90.0 |

## GW7

- Train rows: 108150
- Bank: 3.70 -> 4.70
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Marcus Rashford
- Effective captain: Bukayo Saka
- Chip used: triple_captain
- Predicted score: 62.83
- Actual score: 87.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.65) beats the best remaining Triple Captain opportunity (6.86).
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- League average score: 0.00
- Transfer: Ben Chilwell -> Matty Cash (projected gain 0.05, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (8.65) beats the best remaining Triple Captain opportunity (6.86).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.1 | 3.72 | 11.07 | 18.45 | 6.00 | 90.8 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 4.9 | 3.42 | 9.87 | 16.47 | 2.00 | 87.9 | 90.0 |
| XI | XI | Pervis Estupiñán | DEF | 5 | 5.3 | 4.65 | 14.28 | 23.07 | -2.00 | 82.2 | 45.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.5 | 4.47 | 13.24 | 21.71 | 12.00 | 83.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.2 | 3.63 | 10.67 | 17.27 | 6.00 | 86.1 | 90.0 |
| Bench 3 | Bench | Matty Cash | DEF | 2 | 4.7 | 3.50 | 9.82 | 16.02 | 6.00 | 72.3 | 90.0 |
| Bench 4 | Bench | Axel Disasi | DEF | 7 | 5.1 | 2.99 | 9.25 | 14.91 | 6.00 | 82.9 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.24 | 12.94 | 20.40 | 8.00 | 60.9 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 7.9 | 4.00 | 11.90 | 20.31 | 23.00 | 73.1 | 90.0 |
| Bench 2 | Bench | Dominic Solanke | FWD | 3 | 6.4 | 3.63 | 11.31 | 18.51 | 2.00 | 87.8 | 90.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 8.7 | 6.60 | 18.84 | 31.03 | 9.00 | 93.8 | 75.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 4.99 | 14.80 | 24.19 | 1.00 | 74.4 | 90.0 |
| Vice Captain | XI | Marcus Rashford | MID | 14 | 8.9 | 5.02 | 14.49 | 23.88 | 2.00 | 82.4 | 76.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.23 | 12.86 | 22.29 | 2.00 | 76.2 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 4.09 | 12.75 | 21.39 | 2.00 | 76.9 | 90.0 |

## GW8

- Train rows: 108872
- Bank: 4.70 -> 5.10
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Bukayo Saka
- Effective captain: Ollie Watkins
- Chip used: bench_boost
- Predicted score: 69.61
- Actual score: 45.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (14.29) beats the best remaining Bench Boost opportunity (0.00).
- Chip advisory: bench_boost (0.62): Bench depth is strong enough that a Bench Boost is worth considering.
- League average score: 0.00
- Transfer: Axel Disasi -> Joachim Andersen (projected gain 0.77, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (14.29) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.96 | 11.66 | 19.41 | 1.00 | 98.3 | 90.0 |
| Bench 1 | Bench Boost | André Onana | GK | 14 | 4.9 | 3.47 | 9.79 | 15.91 | 2.00 | 86.6 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.7 | 4.67 | 14.80 | 24.00 | 6.00 | 84.1 | 90.0 |
| XI | XI | Pervis Estupiñán | DEF | 5 | 5.3 | 3.81 | 11.75 | 19.13 | 0.00 | 64.7 | 0.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 4.7 | 4.21 | 11.70 | 18.70 | 6.00 | 94.6 | 90.0 |
| Bench 2 | Bench Boost | Matty Cash | DEF | 2 | 4.8 | 3.81 | 10.97 | 17.18 | 2.00 | 75.7 | 81.0 |
| Bench 4 | Bench Boost | William Saliba | DEF | 1 | 5.2 | 3.31 | 10.37 | 17.07 | 7.00 | 86.0 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 7.9 | 5.85 | 16.58 | 27.03 | 5.00 | 94.9 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 7.0 | 4.13 | 13.78 | 23.15 | 2.00 | 80.1 | 67.0 |
| Bench 3 | Bench Boost | Dominic Solanke | FWD | 3 | 6.4 | 3.70 | 10.71 | 17.48 | 1.00 | 81.4 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.7 | 5.32 | 17.23 | 29.51 | 0.00 | 75.6 | 0.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.6 | 4.63 | 13.78 | 22.09 | 2.00 | 75.5 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.28 | 13.24 | 22.09 | 2.00 | 77.9 | 90.0 |
| XI | XI | Marcus Rashford | MID | 14 | 8.9 | 4.61 | 13.06 | 21.83 | 2.00 | 66.4 | 62.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 4.00 | 12.59 | 21.21 | 2.00 | 78.9 | 90.0 |