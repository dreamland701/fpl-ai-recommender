# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26
- In-season warm start: 2023-24 GW1-GW1
- Simulated weeks: GW2-GW38
- Total predicted points: 2180.47
- Total actual points: 2136.00
- Average predicted points: 58.93
- Average actual points: 57.73
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW1 are included before the first simulated week.
- League-average scores were not available for this run.

## GW2

- Train rows: 104659
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 64.81
- Actual score: 47.00
- Chip advisory: bench_boost (0.67): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | -1 | 5.0 | 4.37 | 12.04 | 18.42 | 2.00 | 90.8 | 90.0 |
| Bench 1 | Bench | Bernd Leno | GK | -1 | 4.5 | 4.08 | 11.58 | 18.47 | 2.00 | 103.9 | 90.0 |
| XI | XI | Pervis Estupiñán | DEF | -1 | 5.0 | 5.46 | 14.35 | 21.32 | 11.00 | 97.1 | 90.0 |
| XI | XI | Raphaël Varane | DEF | -1 | 5.0 | 4.85 | 13.50 | 20.44 | 1.00 | 95.7 | 90.0 |
| XI | XI | Aaron Wan-Bissaka | DEF | -1 | 4.5 | 4.23 | 12.12 | 18.72 | 1.00 | 98.3 | 65.0 |
| Bench 3 | Bench | Emerson Leite de Souza Junior | DEF | -1 | 4.5 | 3.76 | 10.64 | 16.70 | 1.00 | 92.6 | 2.0 |
| Bench 4 | Bench | William Saliba | DEF | -1 | 5.0 | 3.75 | 10.57 | 16.75 | 8.00 | 88.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | -1 | 14.0 | 7.42 | 20.71 | 32.07 | 2.00 | 98.9 | 90.0 |
| XI | XI | Ollie Watkins | FWD | -1 | 8.0 | 5.06 | 13.55 | 20.57 | 5.00 | 92.7 | 73.0 |
| Bench 2 | Bench | Alexander Isak | FWD | -1 | 7.5 | 4.46 | 12.82 | 19.19 | 2.00 | 77.2 | 65.0 |
| Vice Captain | XI | Bukayo Saka | MID | -1 | 8.5 | 5.80 | 15.82 | 24.31 | 3.00 | 95.9 | 88.0 |
| XI | XI | James Maddison | MID | -1 | 7.5 | 5.23 | 14.51 | 22.45 | 3.00 | 96.5 | 90.0 |
| XI | XI | Rodrigo Hernandez | MID | -1 | 5.5 | 5.25 | 14.19 | 21.61 | 3.00 | 94.9 | 90.0 |
| XI | XI | Marcus Rashford | MID | -1 | 9.0 | 4.81 | 13.51 | 20.47 | 2.00 | 82.1 | 84.0 |
| XI | XI | Kaoru Mitoma | MID | -1 | 6.5 | 4.88 | 12.82 | 19.14 | 12.00 | 88.8 | 80.0 |

## GW3

- Train rows: 105327
- Bank: 0.00 -> 2.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Pervis Estupiñán
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 59.72
- Actual score: 51.00
- Transfer: Alexander Isak -> Odsonne Edouard (projected gain 0.07, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | -1 | 5.0 | 3.98 | 11.24 | 17.43 | 0.00 | 86.7 | 90.0 |
| Bench 1 | Bench | Bernd Leno | GK | -1 | 4.5 | 2.65 | 9.30 | 15.36 | 5.00 | 91.9 | 90.0 |
| Vice Captain | XI | Pervis Estupiñán | DEF | -1 | 5.1 | 5.89 | 16.64 | 25.24 | 1.00 | 97.0 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 5.1 | 3.91 | 11.24 | 17.51 | 1.00 | 86.0 | 90.0 |
| XI | XI | Raphaël Varane | DEF | -1 | 5.0 | 3.82 | 10.46 | 15.88 | 0.00 | 80.8 | 45.0 |
| Bench 3 | Bench | Aaron Wan-Bissaka | DEF | -1 | 4.5 | 2.93 | 8.45 | 13.44 | 0.00 | 66.0 | 90.0 |
| Bench 4 | Bench | Emerson Leite de Souza Junior | DEF | -1 | 4.5 | 1.92 | 5.98 | 9.91 | 0.00 | 40.8 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | -1 | 14.0 | 6.86 | 20.56 | 30.83 | 4.00 | 91.9 | 90.0 |
| XI | XI | Ollie Watkins | FWD | -1 | 8.0 | 4.26 | 12.34 | 19.48 | 5.00 | 72.6 | 85.0 |
| Bench 2 | Bench | Odsonne Edouard | FWD | -1 | 5.5 | 3.96 | 10.50 | 14.92 | 2.00 | 74.9 | 70.0 |
| XI | XI | Bukayo Saka | MID | -1 | 8.6 | 5.47 | 15.93 | 23.94 | 8.00 | 82.7 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | -1 | 6.5 | 5.37 | 15.06 | 22.84 | 1.00 | 87.7 | 90.0 |
| XI | XI | Marcus Rashford | MID | -1 | 9.0 | 4.88 | 13.84 | 21.26 | 7.00 | 74.3 | 90.0 |
| XI | XI | James Maddison | MID | -1 | 7.5 | 4.40 | 13.09 | 20.70 | 10.00 | 81.4 | 72.0 |
| XI | XI | Rodrigo Hernandez | MID | -1 | 5.6 | 4.00 | 11.80 | 18.01 | 10.00 | 81.0 | 90.0 |

## GW4

- Train rows: 106012
- Bank: 2.10 -> 0.90
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 59.01
- Actual score: 71.00
- Transfer: Emerson Leite de Souza Junior -> Ben Chilwell (projected gain 4.51, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | -1 | 5.0 | 2.93 | 9.48 | 15.52 | 0.00 | 84.4 | 90.0 |
| Bench 1 | Bench | Bernd Leno | GK | -1 | 4.5 | 2.68 | 9.07 | 15.31 | 0.00 | 92.9 | 90.0 |
| XI | XI | Pervis Estupiñán | DEF | -1 | 5.2 | 5.37 | 15.86 | 24.94 | 2.00 | 87.0 | 90.0 |
| XI | XI | Ben Chilwell | DEF | -1 | 5.7 | 4.28 | 12.17 | 18.98 | 1.00 | 66.6 | 61.0 |
| XI | XI | William Saliba | DEF | -1 | 5.2 | 3.53 | 10.62 | 16.94 | 2.00 | 79.8 | 90.0 |
| Bench 3 | Bench | Raphaël Varane | DEF | -1 | 5.1 | 2.32 | 7.70 | 12.27 | 0.00 | 63.9 | 0.0 |
| Bench 4 | Bench | Aaron Wan-Bissaka | DEF | -1 | 4.6 | 2.28 | 7.49 | 12.20 | 1.00 | 73.3 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | -1 | 14.0 | 7.40 | 21.23 | 31.73 | 20.00 | 94.6 | 90.0 |
| XI | XI | Ollie Watkins | FWD | -1 | 8.0 | 4.00 | 12.47 | 19.68 | 2.00 | 74.1 | 72.0 |
| Bench 2 | Bench | Odsonne Edouard | FWD | -1 | 5.5 | 3.41 | 8.99 | 12.91 | 13.00 | 64.4 | 89.0 |
| Vice Captain | XI | Bukayo Saka | MID | -1 | 8.6 | 6.11 | 17.47 | 26.41 | 4.00 | 90.9 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | -1 | 6.6 | 4.90 | 14.30 | 22.27 | 5.00 | 79.0 | 90.0 |
| XI | XI | Marcus Rashford | MID | -1 | 9.0 | 4.41 | 13.85 | 22.69 | 7.00 | 78.7 | 90.0 |
| XI | XI | James Maddison | MID | -1 | 7.6 | 4.37 | 12.68 | 20.22 | 7.00 | 72.9 | 85.0 |
| XI | XI | Rodrigo Hernandez | MID | -1 | 5.6 | 4.31 | 11.98 | 18.43 | 1.00 | 85.8 | 75.0 |

## GW5

- Train rows: 106715
- Bank: 0.90 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 62.60
- Actual score: 38.00
- Transfer: Odsonne Edouard -> Yoane Wissa (projected gain 1.25, hit 0)
- Autosub outfielders: Aaron Wan-Bissaka.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | -1 | 5.0 | 3.17 | 8.93 | 14.93 | 2.00 | 80.4 | 90.0 |
| Bench 1 | Bench | Bernd Leno | GK | -1 | 4.5 | 2.93 | 8.58 | 13.97 | 6.00 | 85.1 | 90.0 |
| XI | Bench | Pervis Estupiñán | DEF | -1 | 5.3 | 5.05 | 14.61 | 22.94 | 0.00 | 91.2 | 0.0 |
| XI | XI | Ben Chilwell | DEF | -1 | 5.8 | 3.85 | 10.95 | 16.80 | 0.00 | 59.1 | 10.0 |
| XI | XI | William Saliba | DEF | -1 | 5.2 | 3.50 | 10.24 | 16.45 | 6.00 | 81.8 | 90.0 |
| Bench 3 | Autosub In | Aaron Wan-Bissaka | DEF | -1 | 4.6 | 3.02 | 7.69 | 12.05 | 1.00 | 73.0 | 5.0 |
| Bench 4 | Bench | Raphaël Varane | DEF | -1 | 5.1 | 1.71 | 4.90 | 8.45 | 0.00 | 31.9 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | -1 | 14.0 | 8.69 | 24.34 | 35.99 | 6.00 | 114.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | -1 | 8.0 | 4.34 | 11.63 | 18.12 | 5.00 | 63.1 | 90.0 |
| XI | XI | Yoane Wissa | FWD | -1 | 6.2 | 3.79 | 11.09 | 16.72 | 1.00 | 68.7 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | -1 | 8.7 | 6.40 | 17.69 | 26.23 | 6.00 | 91.8 | 90.0 |
| XI | XI | James Maddison | MID | -1 | 7.7 | 5.44 | 15.43 | 23.45 | 1.00 | 72.8 | 90.0 |
| XI | XI | Marcus Rashford | MID | -1 | 9.0 | 5.08 | 14.58 | 23.47 | 2.00 | 81.7 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | -1 | 6.6 | 4.57 | 13.59 | 21.59 | 2.00 | 82.4 | 90.0 |
| Bench 2 | Bench | Rodrigo Hernandez | MID | -1 | 5.7 | 3.18 | 9.73 | 15.31 | 1.00 | 70.7 | 90.0 |

## GW6

- Train rows: 107432
- Bank: 0.20 -> 1.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 60.93
- Actual score: 73.00
- Transfer: Ben Chilwell -> Cristian Romero (projected gain 1.12, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | -1 | 4.6 | 3.37 | 9.61 | 15.21 | 10.00 | 85.3 | 90.0 |
| Bench 1 | Bench | André Onana | GK | -1 | 5.0 | 3.09 | 9.06 | 14.92 | 7.00 | 81.7 | 90.0 |
| XI | XI | Pervis Estupiñán | DEF | -1 | 5.3 | 3.98 | 11.53 | 18.37 | 6.00 | 53.1 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 5.2 | 3.88 | 11.04 | 17.18 | 1.00 | 86.0 | 90.0 |
| XI | XI | Cristian Romero | DEF | -1 | 4.7 | 2.83 | 9.71 | 15.81 | -2.00 | 74.5 | 90.0 |
| Bench 3 | Bench | Aaron Wan-Bissaka | DEF | -1 | 4.6 | 1.94 | 5.64 | 9.38 | 0.00 | 46.6 | 0.0 |
| Bench 4 | Bench | Raphaël Varane | DEF | -1 | 5.0 | 1.23 | 3.85 | 6.73 | 1.00 | 22.1 | 11.0 |
| Captain | Captain | Erling Haaland | FWD | -1 | 14.1 | 9.22 | 25.19 | 36.60 | 6.00 | 116.2 | 90.0 |
| XI | XI | Ollie Watkins | FWD | -1 | 8.0 | 4.31 | 12.26 | 19.10 | 9.00 | 71.2 | 90.0 |
| Bench 2 | Bench | Yoane Wissa | FWD | -1 | 6.1 | 3.35 | 9.55 | 15.62 | 2.00 | 62.4 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | -1 | 8.7 | 6.22 | 17.61 | 26.39 | 13.00 | 94.4 | 90.0 |
| XI | XI | James Maddison | MID | -1 | 7.8 | 4.76 | 14.89 | 23.07 | 9.00 | 77.6 | 77.0 |
| XI | XI | Marcus Rashford | MID | -1 | 8.9 | 4.94 | 14.59 | 22.83 | 3.00 | 83.8 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | -1 | 6.5 | 4.64 | 12.97 | 20.38 | 14.00 | 75.5 | 45.0 |
| XI | XI | Rodrigo Hernandez | MID | -1 | 5.7 | 3.56 | 10.33 | 16.09 | -2.00 | 77.3 | 45.0 |

## GW7

- Train rows: 108150
- Bank: 1.30 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 61.63
- Actual score: 55.00
- Transfer: Yoane Wissa -> Julián Álvarez (projected gain 3.98, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | -1 | 4.6 | 3.80 | 10.31 | 15.71 | 1.00 | 86.4 | 90.0 |
| Bench 1 | Bench | André Onana | GK | -1 | 4.9 | 3.49 | 9.81 | 15.85 | 2.00 | 87.9 | 90.0 |
| XI | XI | Pervis Estupiñán | DEF | -1 | 5.3 | 4.63 | 13.69 | 21.33 | -2.00 | 81.5 | 45.0 |
| XI | XI | William Saliba | DEF | -1 | 5.2 | 3.55 | 10.19 | 16.09 | 6.00 | 85.6 | 90.0 |
| XI | XI | Cristian Romero | DEF | -1 | 4.8 | 2.89 | 8.64 | 13.77 | 1.00 | 78.3 | 90.0 |
| Bench 4 | Bench | Aaron Wan-Bissaka | DEF | -1 | 4.6 | 1.26 | 3.65 | 6.72 | 0.00 | 32.4 | 0.0 |
| Bench 3 | Bench | Raphaël Varane | DEF | -1 | 5.0 | 1.29 | 3.64 | 6.31 | 2.00 | 25.2 | 86.0 |
| Captain | Captain | Erling Haaland | FWD | -1 | 14.1 | 8.65 | 24.02 | 36.44 | 2.00 | 113.1 | 90.0 |
| XI | XI | Julián Álvarez | FWD | -1 | 6.9 | 4.27 | 13.29 | 21.40 | 8.00 | 63.6 | 90.0 |
| XI | XI | Ollie Watkins | FWD | -1 | 7.9 | 3.96 | 11.42 | 18.63 | 23.00 | 71.4 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | -1 | 8.7 | 6.49 | 17.51 | 27.40 | 9.00 | 91.4 | 75.0 |
| XI | XI | Marcus Rashford | MID | -1 | 8.9 | 5.11 | 14.10 | 22.16 | 2.00 | 81.0 | 76.0 |
| XI | XI | Kaoru Mitoma | MID | -1 | 6.5 | 4.91 | 13.70 | 21.47 | 1.00 | 72.8 | 90.0 |
| XI | XI | James Maddison | MID | -1 | 7.9 | 4.72 | 13.63 | 21.99 | 2.00 | 79.0 | 89.0 |
| Bench 2 | Bench | Rodrigo Hernandez | MID | -1 | 5.7 | 2.78 | 8.41 | 13.24 | 0.00 | 63.7 | 0.0 |

## GW8

- Train rows: 108872
- Bank: 0.50 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Ollie Watkins
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 58.29
- Actual score: 36.00
- Transfer: Aaron Wan-Bissaka -> Joachim Andersen (projected gain 2.35, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | André Onana | GK | -1 | 4.9 | 3.53 | 9.70 | 15.36 | 2.00 | 87.1 | 90.0 |
| XI | XI | Bernd Leno | GK | -1 | 4.7 | 3.56 | 9.61 | 14.85 | 2.00 | 83.3 | 90.0 |
| XI | Bench | Pervis Estupiñán | DEF | -1 | 5.3 | 3.90 | 11.73 | 18.53 | 0.00 | 65.9 | 0.0 |
| XI | XI | Joachim Andersen | DEF | -1 | 4.7 | 4.14 | 11.27 | 17.33 | 6.00 | 92.0 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 5.2 | 3.38 | 10.39 | 16.72 | 7.00 | 86.9 | 90.0 |
| Bench 2 | Bench | Cristian Romero | DEF | -1 | 4.8 | 3.20 | 9.09 | 14.27 | 8.00 | 78.7 | 90.0 |
| Bench 3 | Bench | Raphaël Varane | DEF | -1 | 5.0 | 2.33 | 6.33 | 10.04 | 0.00 | 54.6 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | -1 | 14.1 | 7.09 | 21.74 | 34.18 | 2.00 | 97.5 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | -1 | 7.9 | 5.76 | 15.65 | 24.14 | 5.00 | 94.1 | 90.0 |
| XI | XI | Julián Álvarez | FWD | -1 | 7.0 | 4.07 | 13.15 | 21.53 | 2.00 | 80.2 | 67.0 |
| XI | Bench | Bukayo Saka | MID | -1 | 8.7 | 5.37 | 16.76 | 27.70 | 0.00 | 76.0 | 0.0 |
| XI | XI | Kaoru Mitoma | MID | -1 | 6.6 | 4.68 | 13.54 | 21.31 | 2.00 | 75.4 | 90.0 |
| XI | XI | James Maddison | MID | -1 | 7.9 | 4.53 | 13.28 | 22.07 | 6.00 | 74.3 | 75.0 |
| XI | XI | Marcus Rashford | MID | -1 | 8.9 | 4.72 | 12.88 | 20.77 | 2.00 | 67.1 | 62.0 |
| Bench 4 | Bench | Rodrigo Hernandez | MID | -1 | 5.6 | 1.27 | 5.98 | 10.73 | 0.00 | 38.7 | 0.0 |

## GW9

- Train rows: 109597
- Bank: 0.30 -> 0.80
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Ollie Watkins
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 53.12
- Actual score: 64.00
- Transfer: Bernd Leno -> Alphonse Areola (projected gain 1.68, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | -1 | 4.2 | 3.56 | 11.12 | 17.90 | 1.00 | 89.3 | 90.0 |
| Bench 1 | Bench | André Onana | GK | -1 | 4.9 | 3.33 | 9.46 | 15.08 | 3.00 | 81.8 | 90.0 |
| XI | XI | Joachim Andersen | DEF | -1 | 4.8 | 3.62 | 11.06 | 17.68 | 0.00 | 82.3 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 5.2 | 3.58 | 10.47 | 16.80 | 1.00 | 85.1 | 90.0 |
| XI | XI | Cristian Romero | DEF | -1 | 4.8 | 3.53 | 9.68 | 15.16 | 8.00 | 82.4 | 90.0 |
| Bench 4 | Bench | Pervis Estupiñán | DEF | -1 | 5.2 | 1.27 | 7.14 | 15.51 | 0.00 | 20.1 | 0.0 |
| Bench 3 | Bench | Raphaël Varane | DEF | -1 | 5.0 | 1.49 | 4.44 | 7.58 | 1.00 | 31.4 | 6.0 |
| Captain | Captain | Erling Haaland | FWD | -1 | 14.1 | 6.55 | 20.38 | 33.47 | 8.00 | 87.8 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | -1 | 8.1 | 5.36 | 15.84 | 25.19 | 11.00 | 80.3 | 90.0 |
| XI | XI | Julián Álvarez | FWD | -1 | 7.0 | 3.96 | 12.09 | 19.90 | 9.00 | 64.0 | 90.0 |
| XI | XI | James Maddison | MID | -1 | 8.0 | 5.05 | 15.04 | 24.17 | 9.00 | 74.3 | 81.0 |
| XI | XI | Bukayo Saka | MID | -1 | 8.6 | 3.83 | 12.96 | 22.04 | 5.00 | 44.1 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | -1 | 6.6 | 3.91 | 12.28 | 19.96 | 2.00 | 76.5 | 90.0 |
| XI | XI | Marcus Rashford | MID | -1 | 8.8 | 3.62 | 10.98 | 18.59 | 2.00 | 52.9 | 87.0 |
| Bench 2 | Bench | Rodrigo Hernandez | MID | -1 | 5.6 | 1.71 | 4.65 | 8.54 | 1.00 | 27.1 | 90.0 |

## GW10

- Train rows: 110327
- Bank: 0.80 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Ollie Watkins
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 56.63
- Actual score: 69.00
- Transfer: Rodrigo Hernandez -> James Ward-Prowse (projected gain 2.09, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | -1 | 4.2 | 4.15 | 11.53 | 18.03 | 3.00 | 91.7 | 90.0 |
| Bench 1 | Bench | André Onana | GK | -1 | 4.9 | 2.64 | 8.46 | 13.55 | 2.00 | 81.2 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 5.2 | 3.65 | 10.09 | 16.00 | 7.00 | 80.8 | 90.0 |
| XI | XI | Joachim Andersen | DEF | -1 | 4.9 | 3.54 | 10.03 | 16.23 | 3.00 | 82.9 | 90.0 |
| XI | XI | Cristian Romero | DEF | -1 | 4.8 | 3.54 | 9.69 | 15.21 | 4.00 | 85.1 | 90.0 |
| Bench 3 | Bench | Pervis Estupiñán | DEF | -1 | 5.1 | 1.51 | 5.30 | 10.60 | 0.00 | 15.0 | 0.0 |
| Bench 4 | Bench | Raphaël Varane | DEF | -1 | 5.0 | 0.90 | 3.61 | 6.05 | 0.00 | 29.0 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | -1 | 14.0 | 6.29 | 19.86 | 32.58 | 16.00 | 90.7 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | -1 | 8.2 | 6.13 | 16.61 | 25.75 | 2.00 | 93.7 | 90.0 |
| XI | XI | Julián Álvarez | FWD | -1 | 7.1 | 4.04 | 12.44 | 19.94 | 2.00 | 79.6 | 86.0 |
| XI | XI | James Maddison | MID | -1 | 8.1 | 5.66 | 15.71 | 24.42 | 6.00 | 83.6 | 88.0 |
| XI | XI | Bukayo Saka | MID | -1 | 8.5 | 4.76 | 14.08 | 22.79 | 6.00 | 68.5 | 72.0 |
| XI | XI | James Ward-Prowse | MID | -1 | 6.3 | 4.34 | 12.12 | 19.11 | 2.00 | 83.5 | 72.0 |
| XI | XI | Kaoru Mitoma | MID | -1 | 6.5 | 4.24 | 11.88 | 18.78 | 2.00 | 72.4 | 90.0 |
| Bench 2 | Bench | Marcus Rashford | MID | -1 | 8.8 | 3.29 | 10.18 | 16.41 | 2.00 | 64.8 | 85.0 |

## GW11

- Train rows: 111058
- Bank: 0.10 -> 2.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Ollie Watkins
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 58.90
- Actual score: 24.00
- Transfer: Marcus Rashford -> Bryan Mbeumo (projected gain 3.87, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | -1 | 4.2 | 3.85 | 11.02 | 17.44 | 1.00 | 90.1 | 90.0 |
| Bench 1 | Bench | André Onana | GK | -1 | 4.8 | 2.63 | 8.29 | 13.90 | 6.00 | 83.7 | 90.0 |
| XI | XI | Joachim Andersen | DEF | -1 | 4.9 | 3.63 | 10.57 | 17.04 | 5.00 | 84.5 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 5.2 | 3.44 | 10.28 | 16.19 | 2.00 | 84.1 | 90.0 |
| XI | XI | Cristian Romero | DEF | -1 | 4.9 | 3.17 | 9.02 | 14.30 | -4.00 | 82.8 | 32.0 |
| Bench 3 | Bench | Pervis Estupiñán | DEF | -1 | 5.0 | 1.02 | 3.61 | 6.94 | 0.00 | 11.3 | 0.0 |
| Bench 4 | Bench | Raphaël Varane | DEF | -1 | 5.0 | 0.53 | 2.14 | 3.96 | 1.00 | 13.5 | 1.0 |
| Captain | Captain | Erling Haaland | FWD | -1 | 14.0 | 7.87 | 22.09 | 34.74 | 1.00 | 106.3 | 45.0 |
| Vice Captain | XI | Ollie Watkins | FWD | -1 | 8.3 | 5.69 | 17.02 | 26.47 | 2.00 | 81.7 | 90.0 |
| XI | XI | Julián Álvarez | FWD | -1 | 7.1 | 4.28 | 12.26 | 19.33 | 2.00 | 75.1 | 70.0 |
| XI | XI | James Maddison | MID | -1 | 8.1 | 5.54 | 15.83 | 24.92 | 1.00 | 82.8 | 45.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 6.7 | 4.95 | 13.96 | 22.03 | 5.00 | 89.7 | 90.0 |
| XI | XI | Bukayo Saka | MID | -1 | 8.6 | 4.35 | 13.51 | 21.99 | 2.00 | 59.4 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | -1 | 6.5 | 4.25 | 12.17 | 18.77 | 6.00 | 74.2 | 90.0 |
| Bench 2 | Bench | James Ward-Prowse | MID | -1 | 6.3 | 3.56 | 10.14 | 16.49 | 2.00 | 71.2 | 90.0 |

## GW12

- Train rows: 111791
- Bank: 2.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Ollie Watkins
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 59.20
- Actual score: 75.00
- Transfer: Raphaël Varane -> Kieran Trippier (projected gain 8.58, hit 0)
- Autosub outfielders: James Ward-Prowse.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | -1 | 4.3 | 3.86 | 10.51 | 16.43 | 2.00 | 89.6 | 90.0 |
| Bench 1 | Bench | André Onana | GK | -1 | 4.8 | 3.26 | 8.83 | 14.24 | 8.00 | 87.4 | 90.0 |
| XI | XI | Kieran Trippier | DEF | -1 | 7.0 | 5.31 | 15.42 | 24.71 | 1.00 | 90.4 | 90.0 |
| XI | XI | Joachim Andersen | DEF | -1 | 5.0 | 3.84 | 10.90 | 17.28 | 1.00 | 84.2 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 5.2 | 3.67 | 10.08 | 15.91 | 9.00 | 82.3 | 90.0 |
| Bench 3 | Bench | Cristian Romero | DEF | -1 | 4.9 | 2.19 | 6.91 | 11.95 | 0.00 | 62.5 | 0.0 |
| Bench 4 | Bench | Pervis Estupiñán | DEF | -1 | 5.0 | 1.08 | 3.18 | 5.79 | 0.00 | 11.0 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | -1 | 14.0 | 6.99 | 20.47 | 31.80 | 16.00 | 91.2 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | -1 | 8.4 | 5.78 | 16.57 | 25.82 | 6.00 | 86.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | -1 | 7.2 | 4.08 | 11.92 | 18.90 | 5.00 | 74.8 | 78.0 |
| XI | Bench | James Maddison | MID | -1 | 8.1 | 4.81 | 14.04 | 22.53 | 0.00 | 68.2 | 0.0 |
| XI | XI | Bukayo Saka | MID | -1 | 8.6 | 5.07 | 13.81 | 22.04 | 5.00 | 75.7 | 80.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 6.7 | 4.29 | 13.71 | 21.80 | 2.00 | 87.9 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | -1 | 6.5 | 4.51 | 12.00 | 18.23 | 1.00 | 75.6 | 45.0 |
| Bench 2 | Autosub In | James Ward-Prowse | MID | -1 | 6.2 | 3.71 | 10.17 | 16.33 | 11.00 | 74.8 | 90.0 |

## GW13

- Train rows: 112534
- Bank: 0.10 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Ollie Watkins
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 60.37
- Actual score: 42.00
- Transfer: James Maddison -> Jarrod Bowen (projected gain 3.91, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | -1 | 4.3 | 3.78 | 10.52 | 16.44 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | André Onana | GK | -1 | 4.8 | 3.39 | 9.40 | 14.99 | 9.00 | 88.6 | 90.0 |
| XI | XI | Kieran Trippier | DEF | -1 | 7.0 | 5.00 | 14.73 | 23.55 | 1.00 | 89.8 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 5.3 | 4.17 | 11.60 | 17.94 | 6.00 | 86.7 | 90.0 |
| XI | XI | Joachim Andersen | DEF | -1 | 5.1 | 3.71 | 10.50 | 16.69 | 1.00 | 85.7 | 90.0 |
| Bench 3 | Bench | Cristian Romero | DEF | -1 | 5.0 | 0.95 | 3.85 | 8.22 | 0.00 | 35.4 | 0.0 |
| Bench 4 | Bench | Pervis Estupiñán | DEF | -1 | 5.0 | 0.88 | 2.72 | 5.03 | 0.00 | 8.9 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | -1 | 14.0 | 7.86 | 22.27 | 34.03 | 7.00 | 106.5 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | -1 | 8.4 | 5.76 | 16.63 | 25.06 | 5.00 | 89.7 | 90.0 |
| XI | XI | Julián Álvarez | FWD | -1 | 7.2 | 4.10 | 11.70 | 18.63 | 2.00 | 73.8 | 90.0 |
| XI | XI | Bukayo Saka | MID | -1 | 8.6 | 5.02 | 14.18 | 22.31 | 8.00 | 73.1 | 90.0 |
| XI | Bench | Jarrod Bowen | MID | -1 | 7.6 | 4.95 | 13.94 | 21.63 | 0.00 | 83.4 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 6.8 | 4.31 | 12.94 | 20.49 | 2.00 | 81.1 | 90.0 |
| XI | Bench | Kaoru Mitoma | MID | -1 | 6.5 | 3.84 | 10.66 | 16.69 | 0.00 | 60.7 | 0.0 |
| Bench 2 | Bench | James Ward-Prowse | MID | -1 | 6.1 | 3.70 | 10.24 | 16.51 | 2.00 | 79.2 | 90.0 |

## GW14

- Train rows: 113281
- Bank: 0.50 -> 1.90
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Ollie Watkins
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 59.45
- Actual score: 62.00
- Transfer: Kaoru Mitoma -> Cole Palmer (projected gain 1.23, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | -1 | 4.3 | 3.83 | 10.56 | 16.59 | 2.00 | 90.6 | 90.0 |
| Bench 1 | Bench | André Onana | GK | -1 | 4.8 | 3.30 | 10.03 | 15.98 | 3.00 | 89.5 | 90.0 |
| XI | XI | Kieran Trippier | DEF | -1 | 7.0 | 4.93 | 14.19 | 22.79 | 12.00 | 88.1 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 5.4 | 4.38 | 12.05 | 18.82 | 1.00 | 83.6 | 90.0 |
| XI | XI | Joachim Andersen | DEF | -1 | 5.2 | 3.67 | 10.57 | 16.58 | 2.00 | 85.1 | 90.0 |
| Bench 4 | Bench | Cristian Romero | DEF | -1 | 4.9 | 0.33 | 2.83 | 6.32 | 0.00 | 27.7 | 0.0 |
| Bench 3 | Bench | Pervis Estupiñán | DEF | -1 | 5.0 | 0.61 | 2.31 | 4.39 | 0.00 | 8.9 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | -1 | 14.0 | 7.37 | 21.35 | 33.44 | 7.00 | 93.1 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | -1 | 8.5 | 5.85 | 16.23 | 24.92 | 11.00 | 89.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | -1 | 7.1 | 4.35 | 12.25 | 19.25 | 5.00 | 75.2 | 86.0 |
| XI | XI | Bukayo Saka | MID | -1 | 8.7 | 5.56 | 15.13 | 23.40 | 8.00 | 80.1 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 6.9 | 4.75 | 13.54 | 21.56 | 5.00 | 74.5 | 77.0 |
| XI | XI | Cole Palmer | MID | -1 | 5.2 | 3.83 | 11.19 | 17.82 | 1.00 | 70.2 | 24.0 |
| Bench 2 | Bench | Jarrod Bowen | MID | -1 | 7.7 | 3.44 | 10.32 | 17.40 | 2.00 | 47.1 | 90.0 |
| XI | XI | James Ward-Prowse | MID | -1 | 6.2 | 3.57 | 10.06 | 16.25 | 1.00 | 76.5 | 90.0 |

## GW15

- Train rows: 114034
- Bank: 1.90 -> 1.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 58.14
- Actual score: 32.00
- Transfer: Cole Palmer -> Anthony Gordon (projected gain 1.35, hit 0)
- Autosub: André Onana replaced Alphonse Areola.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alphonse Areola | GK | -1 | 4.3 | 3.35 | 10.04 | 15.86 | 0.00 | 88.8 | 0.0 |
| Bench 1 | Autosub In | André Onana | GK | -1 | 4.8 | 3.17 | 9.35 | 15.11 | 2.00 | 86.7 | 90.0 |
| XI | XI | Kieran Trippier | DEF | -1 | 7.0 | 5.51 | 15.06 | 23.67 | 1.00 | 95.9 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 5.5 | 4.21 | 11.64 | 18.27 | 1.00 | 83.9 | 90.0 |
| XI | XI | Joachim Andersen | DEF | -1 | 5.2 | 3.77 | 10.31 | 16.38 | 1.00 | 84.4 | 90.0 |
| Bench 3 | Bench | Cristian Romero | DEF | -1 | 4.9 | 1.33 | 3.80 | 6.61 | 9.00 | 21.4 | 90.0 |
| Bench 4 | Bench | Pervis Estupiñán | DEF | -1 | 5.0 | 0.65 | 1.72 | 3.14 | 0.00 | 4.3 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | -1 | 14.0 | 7.40 | 21.75 | 33.91 | 2.00 | 97.6 | 90.0 |
| XI | XI | Ollie Watkins | FWD | -1 | 8.5 | 5.20 | 15.23 | 24.53 | 1.00 | 87.2 | 89.0 |
| XI | XI | Julián Álvarez | FWD | -1 | 7.0 | 4.43 | 13.06 | 21.02 | 2.00 | 77.4 | 67.0 |
| Vice Captain | XI | Bukayo Saka | MID | -1 | 8.8 | 5.70 | 15.55 | 24.15 | 5.00 | 82.2 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.1 | 4.48 | 13.29 | 21.38 | 6.00 | 68.8 | 39.0 |
| XI | XI | Anthony Gordon | MID | -1 | 5.9 | 3.72 | 10.32 | 16.06 | 2.00 | 70.1 | 90.0 |
| XI | XI | Jarrod Bowen | MID | -1 | 7.6 | 2.96 | 10.17 | 18.05 | 7.00 | 56.9 | 90.0 |
| Bench 2 | Bench | James Ward-Prowse | MID | -1 | 6.2 | 2.90 | 8.98 | 14.65 | 8.00 | 77.5 | 90.0 |

## GW16

- Train rows: 114791
- Bank: 1.30 -> 1.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 55.97
- Actual score: 24.00
- Transfer: Pervis Estupiñán -> Pedro Porro (projected gain 1.32, hit 0)
- Autosub outfielders: James Ward-Prowse, Joachim Andersen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | -1 | 4.8 | 3.20 | 9.11 | 14.85 | 1.00 | 85.5 | 90.0 |
| Bench 1 | Bench | Alphonse Areola | GK | -1 | 4.3 | 2.33 | 7.29 | 12.16 | 0.00 | 53.8 | 0.0 |
| XI | XI | Kieran Trippier | DEF | -1 | 7.0 | 4.83 | 14.31 | 22.57 | -1.00 | 93.4 | 85.0 |
| XI | XI | William Saliba | DEF | -1 | 5.5 | 3.66 | 11.13 | 17.73 | 2.00 | 84.7 | 90.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.3 | 3.83 | 10.49 | 16.64 | 5.00 | 82.7 | 90.0 |
| Bench 3 | Autosub In | Joachim Andersen | DEF | -1 | 5.2 | 3.13 | 9.27 | 14.73 | 0.00 | 82.0 | 90.0 |
| Bench 4 | Bench | Cristian Romero | DEF | -1 | 4.9 | 2.65 | 7.40 | 11.90 | 1.00 | 60.0 | 90.0 |
| Captain | Bench | Erling Haaland | FWD | -1 | 14.0 | 7.35 | 21.10 | 32.99 | 0.00 | 94.3 | 0.0 |
| XI | XI | Ollie Watkins | FWD | -1 | 8.4 | 4.27 | 13.26 | 21.77 | 2.00 | 82.5 | 90.0 |
| XI | XI | Julián Álvarez | FWD | -1 | 7.0 | 4.33 | 12.24 | 19.54 | 5.00 | 69.4 | 90.0 |
| Vice Captain | Captain | Bukayo Saka | MID | -1 | 8.9 | 5.38 | 15.65 | 24.35 | 2.00 | 86.3 | 90.0 |
| XI | Bench | Bryan Mbeumo | MID | -1 | 7.1 | 4.67 | 13.02 | 20.59 | 0.00 | 69.5 | 0.0 |
| XI | XI | Jarrod Bowen | MID | -1 | 7.6 | 3.68 | 11.00 | 17.84 | 2.00 | 70.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | -1 | 6.0 | 3.43 | 10.21 | 15.93 | 2.00 | 69.8 | 73.0 |
| Bench 2 | Autosub In | James Ward-Prowse | MID | -1 | 6.2 | 3.29 | 9.81 | 15.49 | 2.00 | 79.6 | 90.0 |

## GW17

- Train rows: 115549
- Bank: 1.00 -> 0.80
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 54.58
- Actual score: 64.00
- Transfer: James Ward-Prowse -> Pascal Groß (projected gain 1.03, hit 0)
- Autosub outfielders: Joachim Andersen, Cristian Romero.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | -1 | 4.8 | 2.66 | 8.81 | 14.25 | 10.00 | 83.9 | 90.0 |
| Bench 1 | Bench | Alphonse Areola | GK | -1 | 4.3 | 2.27 | 6.76 | 11.56 | 0.00 | 40.3 | 0.0 |
| XI | Bench | Kieran Trippier | DEF | -1 | 7.0 | 5.03 | 14.26 | 22.79 | 0.00 | 93.9 | 0.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.3 | 4.09 | 11.38 | 18.03 | 8.00 | 84.6 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 5.5 | 3.98 | 11.21 | 17.84 | 7.00 | 83.4 | 90.0 |
| Bench 2 | Autosub In | Joachim Andersen | DEF | -1 | 5.1 | 2.57 | 8.63 | 14.03 | 0.00 | 80.5 | 90.0 |
| Bench 3 | Autosub In | Cristian Romero | DEF | -1 | 4.9 | 2.52 | 7.23 | 11.74 | 7.00 | 63.7 | 90.0 |
| Captain | Bench | Erling Haaland | FWD | -1 | 14.0 | 6.02 | 17.85 | 28.92 | 0.00 | 58.7 | 0.0 |
| XI | XI | Ollie Watkins | FWD | -1 | 8.4 | 4.50 | 13.35 | 22.06 | 9.00 | 79.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | -1 | 7.0 | 4.70 | 13.13 | 20.75 | 2.00 | 81.4 | 90.0 |
| Vice Captain | Captain | Bukayo Saka | MID | -1 | 8.9 | 5.92 | 16.60 | 25.73 | 3.00 | 88.9 | 88.0 |
| XI | XI | Jarrod Bowen | MID | -1 | 7.7 | 4.37 | 12.18 | 19.04 | 8.00 | 78.0 | 90.0 |
| XI | XI | Pascal Groß | MID | -1 | 6.3 | 3.39 | 11.11 | 17.82 | 1.00 | 81.6 | 90.0 |
| XI | XI | Anthony Gordon | MID | -1 | 6.1 | 3.92 | 10.56 | 16.28 | 6.00 | 67.7 | 83.0 |
| Bench 4 | Bench | Bryan Mbeumo | MID | -1 | 7.0 | 2.21 | 8.50 | 16.73 | 0.00 | 24.2 | 0.0 |

## GW18

- Train rows: 116314
- Bank: 0.80 -> 2.20
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 51.68
- Actual score: 31.00
- Transfer: Bryan Mbeumo -> Cole Palmer (projected gain 3.65, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | -1 | 4.8 | 3.42 | 10.06 | 16.27 | 2.00 | 90.7 | 90.0 |
| Bench 1 | Bench | Alphonse Areola | GK | -1 | 4.2 | 1.81 | 5.98 | 10.63 | 8.00 | 31.6 | 90.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.4 | 4.60 | 12.76 | 20.10 | 2.00 | 84.9 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 5.5 | 3.70 | 11.36 | 17.99 | 2.00 | 89.9 | 90.0 |
| Bench 2 | Bench | Kieran Trippier | DEF | -1 | 6.9 | 3.00 | 10.19 | 18.42 | 2.00 | 47.9 | 90.0 |
| XI | XI | Joachim Andersen | DEF | -1 | 5.0 | 3.08 | 8.87 | 14.35 | 2.00 | 79.7 | 90.0 |
| XI | XI | Cristian Romero | DEF | -1 | 4.9 | 3.07 | 8.34 | 13.15 | 1.00 | 76.0 | 45.0 |
| Vice Captain | XI | Ollie Watkins | FWD | -1 | 8.5 | 5.25 | 15.02 | 23.81 | 2.00 | 82.6 | 90.0 |
| Bench 4 | Bench | Erling Haaland | FWD | -1 | 14.0 | 2.57 | 11.97 | 23.68 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Julián Álvarez | FWD | -1 | 6.9 | 2.79 | 10.96 | 18.81 | 0.00 | 42.4 | 0.0 |
| Captain | Captain | Bukayo Saka | MID | -1 | 9.0 | 5.50 | 16.56 | 25.52 | 1.00 | 87.8 | 90.0 |
| XI | XI | Cole Palmer | MID | -1 | 5.5 | 4.92 | 13.57 | 21.22 | 1.00 | 93.5 | 90.0 |
| XI | XI | Jarrod Bowen | MID | -1 | 7.7 | 4.55 | 12.83 | 20.28 | 8.00 | 85.4 | 87.0 |
| XI | XI | Pascal Groß | MID | -1 | 6.4 | 4.02 | 11.72 | 18.63 | 7.00 | 84.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | -1 | 6.2 | 4.07 | 11.45 | 18.11 | 2.00 | 71.2 | 90.0 |

## GW19

- Train rows: 117083
- Bank: 2.20 -> 2.30
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 55.28
- Actual score: 30.00
- Transfer: Julián Álvarez -> Dominic Solanke (projected gain 1.71, hit 0)
- Autosub outfielders: Joachim Andersen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | -1 | 4.8 | 3.25 | 9.48 | 15.44 | 1.00 | 90.2 | 90.0 |
| Bench 1 | Bench | Alphonse Areola | GK | -1 | 4.2 | 2.71 | 8.69 | 14.27 | 10.00 | 67.3 | 90.0 |
| XI | XI | Kieran Trippier | DEF | -1 | 6.9 | 4.67 | 13.44 | 21.57 | 1.00 | 81.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.5 | 4.17 | 12.31 | 19.37 | 5.00 | 88.1 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 5.5 | 4.14 | 11.27 | 17.71 | 1.00 | 89.1 | 90.0 |
| Bench 3 | Autosub In | Joachim Andersen | DEF | -1 | 5.0 | 2.92 | 8.70 | 13.93 | 1.00 | 82.6 | 90.0 |
| Bench 4 | Bench | Cristian Romero | DEF | -1 | 4.9 | 2.31 | 7.01 | 10.93 | 0.00 | 59.7 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | -1 | 8.7 | 4.91 | 15.22 | 24.21 | 2.00 | 81.6 | 90.0 |
| XI | XI | Dominic Solanke | FWD | -1 | 6.8 | 4.67 | 14.04 | 21.40 | 6.00 | 80.5 | 90.0 |
| Bench 2 | Bench | Erling Haaland | FWD | -1 | 14.0 | 4.15 | 12.87 | 21.96 | 0.00 | 34.1 | 0.0 |
| Captain | Captain | Bukayo Saka | MID | -1 | 9.0 | 5.89 | 16.17 | 25.01 | 2.00 | 85.4 | 90.0 |
| XI | Bench | Cole Palmer | MID | -1 | 5.6 | 4.83 | 13.78 | 21.47 | 0.00 | 85.5 | 0.0 |
| XI | XI | Jarrod Bowen | MID | -1 | 7.8 | 4.38 | 13.26 | 20.70 | 6.00 | 84.9 | 90.0 |
| XI | XI | Pascal Groß | MID | -1 | 6.4 | 4.24 | 11.82 | 18.69 | 2.00 | 84.2 | 90.0 |
| XI | XI | Anthony Gordon | MID | -1 | 6.2 | 4.24 | 11.62 | 18.27 | 1.00 | 73.8 | 90.0 |

## GW20

- Train rows: 117854
- Bank: 2.30 -> 0.70
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 53.33
- Actual score: 43.00
- Transfer: Cole Palmer -> Dejan Kulusevski (projected gain 0.42, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | -1 | 4.2 | 3.78 | 10.32 | 16.51 | 11.00 | 80.0 | 90.0 |
| Bench 1 | Bench | André Onana | GK | -1 | 4.8 | 3.20 | 9.03 | 14.65 | 1.00 | 87.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.6 | 4.49 | 12.57 | 19.87 | 2.00 | 92.2 | 90.0 |
| XI | Bench | Kieran Trippier | DEF | -1 | 6.9 | 3.88 | 11.99 | 19.55 | 0.00 | 82.5 | 0.0 |
| XI | XI | William Saliba | DEF | -1 | 5.5 | 3.75 | 10.90 | 17.35 | 0.00 | 87.3 | 90.0 |
| Bench 3 | Bench | Joachim Andersen | DEF | -1 | 4.9 | 3.07 | 8.43 | 13.47 | 2.00 | 81.4 | 90.0 |
| Bench 4 | Bench | Cristian Romero | DEF | -1 | 5.0 | 1.73 | 4.77 | 7.62 | 0.00 | 36.1 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | -1 | 8.8 | 5.27 | 14.41 | 22.85 | 8.00 | 86.7 | 90.0 |
| XI | XI | Dominic Solanke | FWD | -1 | 7.0 | 4.22 | 12.60 | 20.09 | 2.00 | 78.5 | 90.0 |
| XI | Bench | Erling Haaland | FWD | -1 | 13.9 | 3.85 | 11.17 | 19.99 | 0.00 | 26.7 | 0.0 |
| Captain | Captain | Bukayo Saka | MID | -1 | 9.0 | 5.73 | 16.08 | 24.80 | 7.00 | 86.2 | 90.0 |
| XI | XI | Jarrod Bowen | MID | -1 | 7.8 | 4.87 | 13.84 | 21.90 | 3.00 | 83.7 | 90.0 |
| XI | Bench | Dejan Kulusevski | MID | -1 | 7.2 | 4.01 | 11.25 | 18.36 | 0.00 | 80.0 | 0.0 |
| XI | XI | Pascal Groß | MID | -1 | 6.4 | 3.75 | 10.99 | 17.60 | 3.00 | 82.2 | 90.0 |
| Bench 2 | Bench | Anthony Gordon | MID | -1 | 6.2 | 3.63 | 10.90 | 17.10 | 5.00 | 76.5 | 90.0 |

## GW21

- Train rows: 118627
- Bank: 0.70 -> 7.70
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 53.24
- Actual score: 39.00
- Transfer: Erling Haaland -> Julián Álvarez (projected gain 5.44, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | -1 | 4.2 | 3.93 | 10.94 | 17.48 | 3.00 | 89.3 | 90.0 |
| Bench 1 | Bench | André Onana | GK | -1 | 4.8 | 3.00 | 8.41 | 13.30 | 2.00 | 81.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.7 | 3.74 | 11.40 | 18.50 | 6.00 | 88.4 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 5.6 | 3.79 | 10.32 | 16.36 | 6.00 | 84.3 | 90.0 |
| XI | XI | Kieran Trippier | DEF | -1 | 6.8 | 2.74 | 8.99 | 15.76 | 1.00 | 50.4 | 90.0 |
| Bench 2 | Bench | Joachim Andersen | DEF | -1 | 4.9 | 2.51 | 7.84 | 12.64 | 0.00 | 81.9 | 90.0 |
| Bench 4 | Bench | Cristian Romero | DEF | -1 | 5.0 | 0.78 | 3.27 | 6.07 | 1.00 | 22.5 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | -1 | 8.8 | 5.65 | 15.94 | 24.98 | 1.00 | 91.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | -1 | 6.9 | 4.44 | 13.28 | 20.82 | 2.00 | 72.1 | 90.0 |
| XI | XI | Dominic Solanke | FWD | -1 | 7.1 | 4.48 | 12.94 | 20.23 | 2.00 | 83.9 | 82.0 |
| Captain | Captain | Bukayo Saka | MID | -1 | 9.0 | 6.14 | 16.08 | 24.89 | 3.00 | 87.5 | 90.0 |
| XI | XI | Jarrod Bowen | MID | -1 | 7.9 | 4.76 | 13.45 | 21.26 | 2.00 | 80.1 | 90.0 |
| XI | XI | Pascal Groß | MID | -1 | 6.4 | 4.05 | 11.08 | 17.56 | 3.00 | 80.3 | 90.0 |
| XI | XI | Anthony Gordon | MID | -1 | 6.1 | 3.39 | 10.41 | 17.34 | 7.00 | 77.8 | 85.0 |
| Bench 3 | Bench | Dejan Kulusevski | MID | -1 | 7.2 | 2.07 | 6.96 | 12.32 | 0.00 | 39.9 | 0.0 |

## GW22

- Train rows: 119414
- Bank: 7.70 -> 6.90
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 54.98
- Actual score: 70.00
- Transfer: Dejan Kulusevski -> Phil Foden (projected gain 4.31, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | -1 | 4.2 | 3.64 | 10.38 | 16.81 | 3.00 | 82.3 | 90.0 |
| Bench 1 | Bench | André Onana | GK | -1 | 4.8 | 2.83 | 8.01 | 12.87 | 1.00 | 77.8 | 90.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.8 | 4.24 | 12.36 | 20.29 | 1.00 | 86.2 | 90.0 |
| XI | XI | Kieran Trippier | DEF | -1 | 6.7 | 3.36 | 11.07 | 18.63 | 7.00 | 72.2 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 5.6 | 3.92 | 10.96 | 17.43 | 2.00 | 83.4 | 90.0 |
| Bench 3 | Bench | Joachim Andersen | DEF | -1 | 4.9 | 2.92 | 7.92 | 12.77 | 1.00 | 79.9 | 90.0 |
| Bench 4 | Bench | Cristian Romero | DEF | -1 | 4.9 | 2.03 | 5.71 | 9.33 | 1.00 | 49.8 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | -1 | 8.9 | 5.40 | 15.58 | 24.65 | 7.00 | 85.3 | 90.0 |
| XI | XI | Julián Álvarez | FWD | -1 | 7.0 | 5.28 | 14.40 | 22.17 | 13.00 | 79.4 | 86.0 |
| XI | XI | Dominic Solanke | FWD | -1 | 7.1 | 4.08 | 12.30 | 19.41 | 8.00 | 71.3 | 90.0 |
| Captain | Captain | Bukayo Saka | MID | -1 | 9.1 | 6.08 | 17.03 | 26.66 | 10.00 | 81.1 | 90.0 |
| XI | XI | Phil Foden | MID | -1 | 7.9 | 4.80 | 14.47 | 23.61 | 6.00 | 64.2 | 76.0 |
| XI | XI | Jarrod Bowen | MID | -1 | 8.1 | 4.25 | 13.09 | 22.48 | 1.00 | 65.7 | 90.0 |
| XI | XI | Pascal Groß | MID | -1 | 6.5 | 3.85 | 11.19 | 17.89 | 2.00 | 76.7 | 90.0 |
| Bench 2 | Bench | Anthony Gordon | MID | -1 | 6.1 | 3.42 | 10.27 | 16.85 | 1.00 | 77.8 | 90.0 |

## GW23

- Train rows: 120213
- Bank: 6.90 -> 7.20
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 55.72
- Actual score: 91.00
- Transfer: Anthony Gordon -> Cole Palmer (projected gain 2.31, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | -1 | 4.2 | 3.27 | 10.04 | 15.86 | 1.00 | 84.0 | 45.0 |
| Bench 1 | Bench | André Onana | GK | -1 | 4.8 | 2.89 | 7.92 | 12.58 | 8.00 | 79.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.9 | 4.22 | 12.29 | 19.86 | 1.00 | 88.1 | 90.0 |
| XI | XI | Kieran Trippier | DEF | -1 | 6.7 | 3.91 | 11.43 | 18.67 | 9.00 | 74.7 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 5.6 | 3.60 | 10.66 | 17.02 | 1.00 | 86.0 | 90.0 |
| Bench 3 | Bench | Joachim Andersen | DEF | -1 | 4.8 | 2.61 | 7.95 | 12.74 | 3.00 | 80.5 | 90.0 |
| Bench 4 | Bench | Cristian Romero | DEF | -1 | 4.9 | 2.44 | 6.84 | 10.87 | 1.00 | 64.7 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | -1 | 8.9 | 5.82 | 16.40 | 26.11 | 18.00 | 91.9 | 90.0 |
| XI | XI | Julián Álvarez | FWD | -1 | 7.0 | 5.24 | 14.43 | 22.47 | 2.00 | 82.6 | 90.0 |
| XI | XI | Dominic Solanke | FWD | -1 | 7.1 | 4.44 | 12.54 | 19.79 | 2.00 | 75.6 | 90.0 |
| Captain | Captain | Bukayo Saka | MID | -1 | 9.1 | 5.83 | 16.61 | 26.20 | 9.00 | 88.1 | 78.0 |
| XI | XI | Cole Palmer | MID | -1 | 5.8 | 5.04 | 14.27 | 22.67 | 8.00 | 89.2 | 90.0 |
| XI | XI | Phil Foden | MID | -1 | 8.0 | 4.55 | 13.49 | 22.01 | 20.00 | 73.1 | 90.0 |
| Bench 2 | Bench | Jarrod Bowen | MID | -1 | 8.1 | 3.94 | 11.99 | 20.10 | 2.00 | 71.9 | 90.0 |
| XI | XI | Pascal Groß | MID | -1 | 6.5 | 3.98 | 11.29 | 17.92 | 11.00 | 81.4 | 90.0 |

## GW24

- Train rows: 121022
- Bank: 7.20 -> 6.60
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Phil Foden
- Effective captain: Ollie Watkins
- Chip used: none
- Predicted score: 57.78
- Actual score: 58.00
- Transfer: Pascal Groß -> Richarlison de Andrade (projected gain 1.52, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | -1 | 4.2 | 2.90 | 9.33 | 14.72 | 0.00 | 71.6 | 90.0 |
| Bench 1 | Bench | André Onana | GK | -1 | 4.8 | 2.67 | 8.07 | 13.03 | 4.00 | 85.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | -1 | 6.7 | 4.62 | 13.14 | 20.89 | 4.00 | 88.3 | 90.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.9 | 4.31 | 12.16 | 19.51 | 2.00 | 88.7 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 5.6 | 3.53 | 10.45 | 16.73 | 12.00 | 83.6 | 90.0 |
| Bench 3 | Bench | Joachim Andersen | DEF | -1 | 4.8 | 2.85 | 8.03 | 12.81 | 1.00 | 81.8 | 90.0 |
| Bench 4 | Bench | Cristian Romero | DEF | -1 | 4.9 | 2.64 | 6.99 | 10.97 | 2.00 | 72.5 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | -1 | 8.8 | 6.30 | 17.60 | 27.99 | 2.00 | 98.1 | 90.0 |
| XI | XI | Julián Álvarez | FWD | -1 | 6.9 | 4.74 | 13.50 | 21.57 | 2.00 | 73.3 | 76.0 |
| XI | XI | Dominic Solanke | FWD | -1 | 7.1 | 3.85 | 11.34 | 18.38 | 4.00 | 72.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | -1 | 9.0 | 5.57 | 16.30 | 25.90 | 15.00 | 79.3 | 66.0 |
| Vice Captain | XI | Phil Foden | MID | -1 | 7.9 | 5.75 | 15.99 | 25.14 | 3.00 | 89.9 | 90.0 |
| XI | XI | Cole Palmer | MID | -1 | 5.8 | 5.06 | 14.85 | 23.47 | 10.00 | 90.2 | 90.0 |
| XI | XI | Richarlison de Andrade | MID | -1 | 7.1 | 4.85 | 12.74 | 20.08 | 2.00 | 79.4 | 90.0 |
| Bench 2 | Bench | Jarrod Bowen | MID | -1 | 8.0 | 3.63 | 11.22 | 18.57 | 2.00 | 72.3 | 90.0 |

## GW25

- Train rows: 121836
- Bank: 6.60 -> 6.10
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Bukayo Saka
- Effective captain: Phil Foden
- Chip used: none
- Predicted score: 61.78
- Actual score: 66.00
- Transfer: Dominic Solanke -> Darwin Núñez Ribeiro (projected gain 3.26, hit 0)
- Autosub outfielders: Joachim Andersen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | -1 | 4.2 | 3.67 | 10.39 | 16.47 | 3.00 | 85.0 | 90.0 |
| Bench 1 | Bench | André Onana | GK | -1 | 4.8 | 2.99 | 8.33 | 13.48 | 3.00 | 86.3 | 90.0 |
| XI | XI | Kieran Trippier | DEF | -1 | 6.8 | 4.68 | 12.96 | 20.70 | 1.00 | 87.6 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 5.6 | 4.36 | 12.04 | 19.05 | 6.00 | 90.7 | 90.0 |
| XI | Bench | Pedro Porro | DEF | -1 | 5.9 | 4.06 | 11.49 | 18.39 | 0.00 | 85.6 | 0.0 |
| Bench 3 | Autosub In | Joachim Andersen | DEF | -1 | 4.8 | 2.73 | 7.62 | 12.31 | 2.00 | 78.1 | 90.0 |
| Bench 4 | Bench | Cristian Romero | DEF | -1 | 4.9 | 2.59 | 6.69 | 10.38 | 1.00 | 72.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | -1 | 8.8 | 5.81 | 16.97 | 27.27 | 13.00 | 91.1 | 90.0 |
| XI | XI | Darwin Núñez Ribeiro | FWD | -1 | 7.5 | 5.93 | 14.62 | 21.83 | 5.00 | 93.1 | 45.0 |
| XI | XI | Julián Álvarez | FWD | -1 | 6.8 | 5.18 | 13.20 | 20.42 | 7.00 | 91.9 | 151.0 |
| Vice Captain | XI | Bukayo Saka | MID | -1 | 9.0 | 6.05 | 17.26 | 26.96 | 15.00 | 80.8 | 68.0 |
| Captain | Captain | Phil Foden | MID | -1 | 8.0 | 6.47 | 16.51 | 25.11 | 5.00 | 108.1 | 180.0 |
| XI | XI | Cole Palmer | MID | -1 | 5.9 | 4.65 | 14.28 | 23.00 | 2.00 | 85.8 | 70.0 |
| XI | XI | Richarlison de Andrade | MID | -1 | 7.2 | 4.43 | 12.39 | 19.37 | 2.00 | 70.1 | 70.0 |
| Bench 2 | Bench | Jarrod Bowen | MID | -1 | 7.9 | 3.72 | 10.89 | 18.01 | 2.00 | 71.4 | 90.0 |

## GW26

- Train rows: 122659
- Bank: 6.10 -> 6.40
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Bukayo Saka
- Effective captain: Phil Foden
- Chip used: none
- Predicted score: 56.34
- Actual score: 52.00
- Transfer: Jarrod Bowen -> Luis Díaz (projected gain 5.69, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | -1 | 4.2 | 3.98 | 10.87 | 17.55 | 2.00 | 91.8 | 90.0 |
| Bench 1 | Bench | André Onana | GK | -1 | 4.8 | 2.98 | 8.26 | 13.40 | 2.00 | 85.4 | 90.0 |
| XI | XI | Kieran Trippier | DEF | -1 | 6.9 | 4.07 | 12.86 | 20.71 | 0.00 | 91.9 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 5.6 | 4.26 | 12.16 | 19.20 | 2.00 | 86.8 | 90.0 |
| XI | XI | Joachim Andersen | DEF | -1 | 4.7 | 2.77 | 7.68 | 12.40 | 6.00 | 79.7 | 90.0 |
| Bench 4 | Bench | Pedro Porro | DEF | -1 | 5.8 | 0.31 | 5.85 | 12.24 | 0.00 | 4.6 | 0.0 |
| Bench 3 | Bench | Cristian Romero | DEF | -1 | 4.9 | 0.64 | 5.17 | 8.78 | 0.00 | 36.4 | 0.0 |
| XI | XI | Ollie Watkins | FWD | -1 | 8.7 | 6.05 | 17.03 | 27.36 | 9.00 | 91.6 | 90.0 |
| XI | XI | Julián Álvarez | FWD | -1 | 6.7 | 5.15 | 14.35 | 22.60 | 1.00 | 89.8 | 15.0 |
| XI | Bench | Darwin Núñez Ribeiro | FWD | -1 | 7.6 | 2.58 | 11.56 | 19.16 | 0.00 | 21.9 | 0.0 |
| Captain | Captain | Phil Foden | MID | -1 | 8.0 | 6.88 | 18.96 | 29.21 | 11.00 | 116.6 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | -1 | 9.0 | 6.34 | 18.09 | 27.59 | 10.00 | 85.0 | 75.0 |
| XI | Bench | Luis Díaz | MID | -1 | 7.5 | 4.70 | 15.70 | 23.74 | 0.00 | 77.9 | 0.0 |
| XI | Bench | Cole Palmer | MID | -1 | 5.8 | 2.68 | 11.62 | 20.15 | 0.00 | 38.2 | 0.0 |
| Bench 2 | Bench | Richarlison de Andrade | MID | -1 | 7.2 | 2.09 | 9.53 | 16.05 | 0.00 | 26.3 | 0.0 |

## GW27

- Train rows: 123487
- Bank: 6.40 -> 6.10
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 57.88
- Actual score: 85.00
- Transfer: Cristian Romero -> Gabriel dos Santos Magalhães (projected gain 3.49, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | -1 | 4.2 | 3.82 | 10.91 | 17.57 | 13.00 | 95.3 | 90.0 |
| Bench 1 | Bench | André Onana | GK | -1 | 4.8 | 2.39 | 8.20 | 13.37 | 2.00 | 85.4 | 90.0 |
| XI | XI | Kieran Trippier | DEF | -1 | 6.9 | 4.43 | 13.24 | 21.16 | 1.00 | 87.3 | 51.0 |
| XI | XI | William Saliba | DEF | -1 | 5.7 | 4.48 | 12.68 | 19.86 | 6.00 | 88.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | -1 | 5.2 | 4.41 | 12.29 | 19.06 | 6.00 | 85.6 | 90.0 |
| Bench 2 | Bench | Joachim Andersen | DEF | -1 | 4.7 | 2.80 | 8.88 | 14.06 | 1.00 | 82.5 | 90.0 |
| Bench 4 | Bench | Pedro Porro | DEF | -1 | 5.8 | 2.09 | 6.22 | 10.66 | 0.00 | 39.1 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | -1 | 8.8 | 6.54 | 19.25 | 29.46 | 13.00 | 96.1 | 90.0 |
| XI | XI | Julián Álvarez | FWD | -1 | 6.7 | 3.76 | 11.15 | 18.08 | 4.00 | 56.4 | 31.0 |
| XI | XI | Darwin Núñez Ribeiro | FWD | -1 | 7.6 | 3.52 | 10.11 | 16.13 | 5.00 | 44.6 | 30.0 |
| Captain | Captain | Bukayo Saka | MID | -1 | 9.1 | 6.57 | 19.73 | 30.33 | 7.00 | 83.2 | 45.0 |
| XI | XI | Phil Foden | MID | -1 | 8.1 | 6.40 | 17.86 | 27.61 | 15.00 | 97.5 | 90.0 |
| XI | XI | Luis Díaz | MID | -1 | 7.5 | 4.02 | 11.30 | 17.20 | 3.00 | 54.0 | 90.0 |
| XI | XI | Cole Palmer | MID | -1 | 5.8 | 3.37 | 10.10 | 16.81 | 5.00 | 50.7 | 90.0 |
| Bench 3 | Bench | Richarlison de Andrade | MID | -1 | 7.2 | 2.66 | 7.72 | 12.48 | 0.00 | 33.3 | 0.0 |

## GW28

- Train rows: 124319
- Bank: 6.10 -> 6.60
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Phil Foden
- Effective captain: Ollie Watkins
- Chip used: none
- Predicted score: 63.27
- Actual score: 40.00
- Transfer: Darwin Núñez Ribeiro -> Dominic Solanke (projected gain 5.28, hit 0)
- Autosub outfielders: Joachim Andersen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | -1 | 4.2 | 4.26 | 11.82 | 18.89 | 2.00 | 102.5 | 90.0 |
| Bench 1 | Bench | André Onana | GK | -1 | 4.8 | 3.01 | 8.62 | 13.89 | 11.00 | 86.2 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 5.7 | 4.70 | 13.11 | 20.64 | 2.00 | 88.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | -1 | 5.3 | 4.61 | 12.41 | 19.47 | 1.00 | 85.7 | 90.0 |
| XI | Bench | Kieran Trippier | DEF | -1 | 6.9 | 3.76 | 11.86 | 19.28 | 0.00 | 75.7 | 0.0 |
| Bench 2 | Autosub In | Joachim Andersen | DEF | -1 | 4.7 | 3.09 | 8.66 | 13.79 | 2.00 | 81.1 | 90.0 |
| Bench 4 | Bench | Pedro Porro | DEF | -1 | 5.7 | 0.91 | 3.68 | 7.90 | 7.00 | 22.3 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | -1 | 8.9 | 7.16 | 19.79 | 30.67 | 2.00 | 105.0 | 90.0 |
| XI | XI | Dominic Solanke | FWD | -1 | 7.1 | 5.83 | 14.00 | 20.72 | 8.00 | 102.3 | 180.0 |
| XI | XI | Julián Álvarez | FWD | -1 | 6.6 | 3.64 | 11.50 | 18.89 | 2.00 | 62.4 | 68.0 |
| Vice Captain | XI | Phil Foden | MID | -1 | 8.1 | 6.74 | 19.64 | 30.19 | 2.00 | 105.9 | 90.0 |
| XI | XI | Bukayo Saka | MID | -1 | 9.2 | 6.37 | 18.32 | 29.42 | 2.00 | 71.2 | 90.0 |
| XI | XI | Cole Palmer | MID | -1 | 5.7 | 4.68 | 13.50 | 21.76 | 13.00 | 78.4 | 85.0 |
| XI | XI | Luis Díaz | MID | -1 | 7.5 | 4.37 | 12.46 | 19.20 | 2.00 | 75.6 | 90.0 |
| Bench 3 | Bench | Richarlison de Andrade | MID | -1 | 7.1 | 1.13 | 4.72 | 9.51 | 0.00 | 14.8 | 0.0 |

## GW29

- Train rows: 125157
- Bank: 6.60 -> 7.60
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Alfie Doughty
- Effective captain: Ollie Watkins
- Chip used: none
- Predicted score: 47.81
- Actual score: 8.00
- Transfer: Pedro Porro -> Alfie Doughty (projected gain 6.58, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | -1 | 4.3 | 3.53 | 10.49 | 17.10 | 3.00 | 94.3 | 90.0 |
| Bench 1 | Bench | André Onana | GK | -1 | 4.8 | 1.74 | 7.87 | 13.72 | 0.00 | 57.8 | 0.0 |
| Vice Captain | XI | Alfie Doughty | DEF | -1 | 4.7 | 4.96 | 14.15 | 22.14 | 1.00 | 109.4 | 45.0 |
| XI | Bench | William Saliba | DEF | -1 | 5.8 | 2.95 | 11.31 | 18.97 | 0.00 | 54.2 | 0.0 |
| XI | Bench | Gabriel dos Santos Magalhães | DEF | -1 | 5.3 | 2.80 | 10.74 | 17.90 | 0.00 | 50.3 | 0.0 |
| Bench 2 | Bench | Joachim Andersen | DEF | -1 | 4.7 | 1.58 | 7.32 | 12.57 | 0.00 | 47.6 | 0.0 |
| Bench 3 | Bench | Kieran Trippier | DEF | -1 | 6.8 | 0.92 | 6.87 | 13.87 | 0.00 | 7.8 | 0.0 |
| Captain | Captain | Ollie Watkins | FWD | -1 | 9.0 | 6.18 | 17.43 | 27.58 | 2.00 | 95.7 | 90.0 |
| XI | Bench | Dominic Solanke | FWD | -1 | 7.2 | 4.23 | 15.18 | 24.80 | 0.00 | 67.8 | 0.0 |
| XI | Bench | Julián Álvarez | FWD | -1 | 6.5 | 1.74 | 8.86 | 16.24 | 0.00 | 23.2 | 0.0 |
| XI | Bench | Bukayo Saka | MID | -1 | 9.2 | 4.88 | 16.97 | 28.35 | 0.00 | 45.1 | 0.0 |
| XI | Bench | Phil Foden | MID | -1 | 8.2 | 4.65 | 15.81 | 25.68 | 0.00 | 60.3 | 0.0 |
| XI | Bench | Cole Palmer | MID | -1 | 5.7 | 3.37 | 12.13 | 20.45 | 0.00 | 49.9 | 0.0 |
| XI | Bench | Luis Díaz | MID | -1 | 7.5 | 2.32 | 9.61 | 16.72 | 0.00 | 28.3 | 0.0 |
| Bench 4 | Bench | Richarlison de Andrade | MID | -1 | 7.0 | 0.78 | 3.44 | 7.13 | 1.00 | 9.1 | 10.0 |

## GW30

- Train rows: 125995
- Bank: 7.60 -> 4.50
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Son Heung-min
- Effective captain: Ollie Watkins
- Chip used: none
- Predicted score: 48.47
- Actual score: 67.00
- Transfer: Richarlison de Andrade -> Son Heung-min (projected gain 8.50, hit 0)
- Autosub outfielders: Gabriel dos Santos Magalhães.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | -1 | 4.3 | 3.38 | 10.29 | 17.03 | 2.00 | 94.1 | 45.0 |
| Bench 1 | Bench | André Onana | GK | -1 | 4.8 | 1.88 | 5.87 | 10.47 | 3.00 | 53.1 | 90.0 |
| XI | XI | Alfie Doughty | DEF | -1 | 4.7 | 3.52 | 12.01 | 18.64 | 2.00 | 84.3 | 82.0 |
| XI | XI | William Saliba | DEF | -1 | 5.8 | 2.67 | 8.82 | 14.92 | 7.00 | 56.1 | 90.0 |
| XI | Bench | Kieran Trippier | DEF | -1 | 6.8 | 2.80 | 8.05 | 13.64 | 0.00 | 41.0 | 0.0 |
| Bench 2 | Autosub In | Gabriel dos Santos Magalhães | DEF | -1 | 5.3 | 2.33 | 7.78 | 13.00 | 6.00 | 52.8 | 90.0 |
| Bench 4 | Bench | Joachim Andersen | DEF | -1 | 4.7 | 2.01 | 5.88 | 10.05 | 2.00 | 47.3 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | -1 | 9.0 | 5.84 | 16.77 | 27.24 | 1.00 | 88.7 | 45.0 |
| XI | XI | Dominic Solanke | FWD | -1 | 7.2 | 3.82 | 10.83 | 17.94 | 7.00 | 56.2 | 84.0 |
| Bench 3 | Bench | Julián Álvarez | FWD | -1 | 6.5 | 2.12 | 7.48 | 12.96 | 0.00 | 39.6 | 0.0 |
| Vice Captain | XI | Son Heung-min | MID | -1 | 10.0 | 4.98 | 16.21 | 24.74 | 10.00 | 72.0 | 87.0 |
| XI | XI | Bukayo Saka | MID | -1 | 9.2 | 4.78 | 14.29 | 23.30 | 3.00 | 52.7 | 77.0 |
| XI | XI | Phil Foden | MID | -1 | 8.2 | 4.22 | 13.35 | 21.86 | 3.00 | 60.6 | 60.0 |
| XI | XI | Cole Palmer | MID | -1 | 5.7 | 3.64 | 10.17 | 17.01 | 15.00 | 55.7 | 90.0 |
| XI | XI | Luis Díaz | MID | -1 | 7.5 | 3.00 | 8.58 | 14.56 | 10.00 | 40.6 | 88.0 |

## GW31

- Train rows: 126837
- Bank: 4.50 -> 5.50
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Bukayo Saka
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 54.41
- Actual score: 93.00
- Transfer: Kieran Trippier -> Benjamin White (projected gain 1.08, hit 0)
- Autosub: André Onana replaced Alphonse Areola.
- Autosub outfielders: Alfie Doughty, Joachim Andersen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alphonse Areola | GK | -1 | 4.3 | 3.30 | 10.05 | 16.18 | 0.00 | 77.2 | 0.0 |
| Bench 1 | Autosub In | André Onana | GK | -1 | 4.8 | 2.59 | 8.06 | 13.57 | 2.00 | 75.6 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 5.8 | 4.20 | 11.51 | 18.76 | 7.00 | 81.0 | 90.0 |
| XI | XI | Benjamin White | DEF | -1 | 5.7 | 3.75 | 10.28 | 16.75 | 6.00 | 72.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | -1 | 5.3 | 3.75 | 10.20 | 16.59 | 6.00 | 74.4 | 90.0 |
| Bench 2 | Autosub In | Alfie Doughty | DEF | -1 | 4.7 | 3.18 | 9.28 | 16.32 | 1.00 | 87.4 | 90.0 |
| Bench 3 | Autosub In | Joachim Andersen | DEF | -1 | 4.7 | 2.83 | 7.84 | 12.89 | 1.00 | 71.0 | 90.0 |
| XI | Bench | Ollie Watkins | FWD | -1 | 9.0 | 4.57 | 14.39 | 24.24 | 0.00 | 72.2 | 0.0 |
| XI | XI | Dominic Solanke | FWD | -1 | 7.2 | 4.88 | 12.86 | 20.83 | 2.00 | 81.9 | 89.0 |
| Bench 4 | Bench | Julián Álvarez | FWD | -1 | 6.5 | 2.03 | 6.36 | 11.09 | 2.00 | 32.2 | 90.0 |
| Captain | Captain | Cole Palmer | MID | -1 | 5.8 | 5.46 | 15.31 | 24.22 | 20.00 | 83.7 | 90.0 |
| Vice Captain | Bench | Bukayo Saka | MID | -1 | 9.1 | 5.44 | 15.01 | 24.90 | 0.00 | 65.8 | 0.0 |
| XI | XI | Son Heung-min | MID | -1 | 10.1 | 5.32 | 14.61 | 24.56 | 2.00 | 79.9 | 90.0 |
| XI | XI | Phil Foden | MID | -1 | 8.1 | 4.12 | 12.63 | 21.45 | 20.00 | 62.4 | 79.0 |
| XI | XI | Luis Díaz | MID | -1 | 7.5 | 4.17 | 11.26 | 18.01 | 6.00 | 70.6 | 90.0 |

## GW32

- Train rows: 127681
- Bank: 5.50 -> 0.10
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Phil Foden
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 54.37
- Actual score: 62.00
- Transfer: Ollie Watkins -> Erling Haaland (projected gain 4.45, hit 0)
- Autosub outfielders: Julián Álvarez.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | -1 | 4.9 | 2.58 | 8.02 | 13.24 | 2.00 | 79.7 | 90.0 |
| Bench 1 | Bench | Alphonse Areola | GK | -1 | 4.3 | 2.43 | 7.83 | 13.67 | 0.00 | 51.1 | 0.0 |
| XI | XI | William Saliba | DEF | -1 | 5.8 | 4.10 | 12.03 | 19.63 | 5.00 | 82.5 | 90.0 |
| XI | XI | Benjamin White | DEF | -1 | 5.8 | 3.65 | 10.91 | 17.65 | 5.00 | 73.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | -1 | 5.3 | 3.60 | 10.59 | 17.30 | 6.00 | 77.3 | 90.0 |
| Bench 3 | Bench | Alfie Doughty | DEF | -1 | 4.7 | 3.11 | 8.86 | 14.64 | 2.00 | 77.0 | 90.0 |
| Bench 4 | Bench | Joachim Andersen | DEF | -1 | 4.7 | 2.25 | 7.28 | 12.05 | 0.00 | 71.4 | 90.0 |
| XI | XI | Erling Haaland | FWD | -1 | 14.3 | 4.49 | 14.30 | 25.10 | 8.00 | 42.9 | 90.0 |
| XI | XI | Dominic Solanke | FWD | -1 | 7.2 | 3.98 | 11.87 | 19.51 | 2.00 | 70.1 | 90.0 |
| Bench 2 | Autosub In | Julián Álvarez | FWD | -1 | 6.4 | 3.37 | 9.64 | 15.38 | 2.00 | 56.1 | 73.0 |
| Captain | Captain | Cole Palmer | MID | -1 | 5.9 | 6.97 | 18.92 | 29.06 | 5.00 | 100.4 | 73.0 |
| XI | XI | Son Heung-min | MID | -1 | 10.1 | 5.32 | 15.47 | 24.80 | 5.00 | 78.6 | 90.0 |
| Vice Captain | Bench | Phil Foden | MID | -1 | 8.1 | 5.32 | 15.27 | 25.15 | 0.00 | 82.7 | 0.0 |
| XI | XI | Bukayo Saka | MID | -1 | 9.0 | 3.75 | 11.76 | 19.89 | 10.00 | 38.2 | 63.0 |
| XI | XI | Luis Díaz | MID | -1 | 7.5 | 3.64 | 11.19 | 18.42 | 7.00 | 67.4 | 90.0 |

## GW33

- Train rows: 128527
- Bank: 0.10 -> 1.80
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Erling Haaland
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 57.14
- Actual score: 84.00
- Transfer: Julián Álvarez -> Rodrigo Muniz Carvalho (projected gain 0.02, hit 0)
- Autosub outfielders: Rodrigo Muniz Carvalho.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | -1 | 4.9 | 3.00 | 8.61 | 13.92 | 2.00 | 88.0 | 90.0 |
| Bench 1 | Bench | Alphonse Areola | GK | -1 | 4.2 | 2.06 | 6.43 | 11.66 | 0.00 | 35.8 | 0.0 |
| XI | XI | William Saliba | DEF | -1 | 5.8 | 4.28 | 11.93 | 18.92 | 1.00 | 86.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | -1 | 5.3 | 4.15 | 11.32 | 17.60 | 0.00 | 83.3 | 90.0 |
| XI | XI | Benjamin White | DEF | -1 | 5.9 | 3.96 | 10.92 | 17.11 | 5.00 | 80.0 | 66.0 |
| Bench 3 | Bench | Alfie Doughty | DEF | -1 | 4.6 | 2.61 | 8.27 | 13.43 | 0.00 | 78.0 | 90.0 |
| Bench 4 | Bench | Joachim Andersen | DEF | -1 | 4.7 | 2.26 | 7.29 | 11.78 | 8.00 | 78.8 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | -1 | 14.3 | 6.21 | 17.68 | 28.66 | 10.00 | 80.5 | 80.0 |
| XI | XI | Dominic Solanke | FWD | -1 | 7.3 | 4.13 | 11.88 | 19.01 | 7.00 | 76.3 | 90.0 |
| Bench 2 | Autosub In | Rodrigo Muniz Carvalho | FWD | -1 | 4.7 | 3.59 | 10.18 | 16.39 | 2.00 | 68.5 | 90.0 |
| Captain | Captain | Cole Palmer | MID | -1 | 6.0 | 6.52 | 17.85 | 27.41 | 26.00 | 92.5 | 79.0 |
| XI | XI | Son Heung-min | MID | -1 | 10.1 | 5.06 | 14.85 | 23.66 | 1.00 | 80.6 | 57.0 |
| XI | XI | Bukayo Saka | MID | -1 | 8.9 | 4.50 | 12.93 | 21.21 | 2.00 | 55.8 | 90.0 |
| XI | XI | Luis Díaz | MID | -1 | 7.6 | 4.81 | 12.80 | 20.07 | 2.00 | 78.9 | 65.0 |
| XI | Bench | Phil Foden | MID | -1 | 8.2 | 3.99 | 11.88 | 20.04 | 0.00 | 50.3 | 0.0 |

## GW34

- Train rows: 129378
- Bank: 1.80 -> 1.90
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Erling Haaland
- Effective captain: Cole Palmer
- Chip used: bench_boost
- Predicted score: 76.23
- Actual score: 106.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (17.49) beats the best remaining Bench Boost opportunity (16.80).
- Transfer: Phil Foden -> Bruno Borges Fernandes (projected gain 3.75, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (17.49) beats the best remaining Bench Boost opportunity (16.80).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | -1 | 4.9 | 3.20 | 8.76 | 14.10 | 1.00 | 87.5 | 90.0 |
| Bench 1 | Bench Boost | Alphonse Areola | GK | -1 | 4.2 | 1.70 | 5.44 | 10.07 | 0.00 | 27.2 | 0.0 |
| XI | XI | William Saliba | DEF | -1 | 5.9 | 5.38 | 12.77 | 19.20 | 14.00 | 112.1 | 180.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | -1 | 5.4 | 5.19 | 12.08 | 17.89 | 12.00 | 108.7 | 180.0 |
| XI | XI | Benjamin White | DEF | -1 | 5.9 | 4.98 | 11.83 | 17.93 | 26.00 | 98.3 | 180.0 |
| XI | XI | Joachim Andersen | DEF | -1 | 4.7 | 4.37 | 9.97 | 14.66 | 11.00 | 112.0 | 180.0 |
| Bench 4 | Bench Boost | Alfie Doughty | DEF | -1 | 4.6 | 2.88 | 7.85 | 12.49 | -1.00 | 77.7 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | -1 | 14.3 | 6.43 | 18.48 | 29.30 | 0.00 | 80.3 | 0.0 |
| XI | XI | Dominic Solanke | FWD | -1 | 7.2 | 4.97 | 12.70 | 20.02 | 8.00 | 107.3 | 176.0 |
| Bench 2 | Bench Boost | Rodrigo Muniz Carvalho | FWD | -1 | 4.7 | 3.36 | 9.83 | 15.74 | 5.00 | 65.8 | 90.0 |
| Captain | Captain | Cole Palmer | MID | -1 | 6.1 | 7.08 | 20.14 | 31.34 | 0.00 | 107.5 | 0.0 |
| XI | XI | Bukayo Saka | MID | -1 | 8.9 | 6.25 | 15.12 | 22.86 | 9.00 | 94.7 | 171.0 |
| XI | XI | Bruno Borges Fernandes | MID | -1 | 8.2 | 4.97 | 13.56 | 21.52 | 18.00 | 94.3 | 90.0 |
| XI | XI | Luis Díaz | MID | -1 | 7.7 | 5.17 | 12.23 | 18.22 | 3.00 | 88.3 | 163.0 |
| Bench 3 | Bench Boost | Son Heung-min | MID | -1 | 10.0 | 3.22 | 12.09 | 20.44 | 0.00 | 38.0 | 0.0 |

## GW35

- Train rows: 130234
- Bank: 1.90 -> 3.30
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Martin Ødegaard
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 67.00
- Actual score: 57.00
- Transfer: Son Heung-min -> Martin Ødegaard (projected gain 6.50, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | -1 | 5.0 | 2.86 | 7.84 | 12.55 | 4.00 | 81.7 | 90.0 |
| Bench 1 | Bench | Alphonse Areola | GK | -1 | 4.2 | 1.36 | 4.73 | 8.83 | 1.00 | 22.6 | 90.0 |
| XI | XI | Benjamin White | DEF | -1 | 6.0 | 6.04 | 16.57 | 25.53 | 1.00 | 122.6 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 5.9 | 5.28 | 14.72 | 22.44 | 1.00 | 121.4 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | -1 | 5.4 | 5.15 | 14.26 | 21.61 | 1.00 | 117.8 | 90.0 |
| Bench 2 | Bench | Joachim Andersen | DEF | -1 | 4.7 | 4.42 | 12.17 | 18.43 | 1.00 | 120.2 | 90.0 |
| Bench 4 | Bench | Alfie Doughty | DEF | -1 | 4.5 | 2.66 | 7.57 | 12.44 | 1.00 | 78.9 | 87.0 |
| XI | XI | Dominic Solanke | FWD | -1 | 7.2 | 5.79 | 15.90 | 24.38 | 2.00 | 114.7 | 90.0 |
| XI | XI | Erling Haaland | FWD | -1 | 14.2 | 4.95 | 14.72 | 24.71 | 5.00 | 43.6 | 28.0 |
| Bench 3 | Bench | Rodrigo Muniz Carvalho | FWD | -1 | 4.6 | 4.10 | 11.02 | 17.08 | 6.00 | 69.1 | 84.0 |
| Captain | Captain | Bukayo Saka | MID | -1 | 9.0 | 6.88 | 18.79 | 28.44 | 12.00 | 107.6 | 90.0 |
| Vice Captain | XI | Martin Ødegaard | MID | -1 | 8.6 | 6.35 | 17.88 | 27.61 | 2.00 | 119.7 | 88.0 |
| XI | XI | Cole Palmer | MID | -1 | 6.2 | 5.74 | 16.21 | 26.27 | 8.00 | 81.6 | 180.0 |
| XI | XI | Bruno Borges Fernandes | MID | -1 | 8.3 | 5.70 | 16.18 | 25.65 | 4.00 | 98.3 | 90.0 |
| XI | XI | Luis Díaz | MID | -1 | 7.8 | 5.39 | 15.22 | 23.05 | 5.00 | 96.5 | 78.0 |

## GW36

- Train rows: 131093
- Bank: 3.30 -> 2.90
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Bukayo Saka
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 62.84
- Actual score: 81.00
- Transfer: Alphonse Areola -> Đorđe Petrović (projected gain 1.88, hit 0)
- Autosub outfielders: Rodrigo Muniz Carvalho.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Đorđe Petrović | GK | -1 | 4.6 | 3.82 | 10.22 | 15.39 | 6.00 | 113.2 | 90.0 |
| Bench 1 | Bench | André Onana | GK | -1 | 5.0 | 2.84 | 8.38 | 13.33 | 2.00 | 80.4 | 90.0 |
| XI | XI | Benjamin White | DEF | -1 | 6.0 | 4.57 | 12.74 | 20.69 | 6.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 5.9 | 4.27 | 11.77 | 18.62 | 6.00 | 93.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | -1 | 5.4 | 3.99 | 11.03 | 17.48 | 7.00 | 89.6 | 90.0 |
| Bench 3 | Bench | Joachim Andersen | DEF | -1 | 4.7 | 3.39 | 9.40 | 14.68 | 6.00 | 91.6 | 90.0 |
| Bench 4 | Bench | Alfie Doughty | DEF | -1 | 4.5 | 2.70 | 7.12 | 11.60 | 2.00 | 78.9 | 90.0 |
| XI | XI | Erling Haaland | FWD | -1 | 14.1 | 5.12 | 15.43 | 25.20 | 21.00 | 45.8 | 82.0 |
| XI | XI | Dominic Solanke | FWD | -1 | 7.3 | 4.27 | 12.72 | 20.51 | 2.00 | 92.0 | 90.0 |
| Bench 2 | Autosub In | Rodrigo Muniz Carvalho | FWD | -1 | 4.5 | 4.05 | 11.05 | 16.80 | 2.00 | 71.4 | 63.0 |
| Captain | Captain | Cole Palmer | MID | -1 | 6.2 | 7.70 | 21.88 | 33.61 | 8.00 | 119.0 | 88.0 |
| XI | Bench | Bruno Borges Fernandes | MID | -1 | 8.4 | 5.67 | 16.88 | 26.87 | 0.00 | 86.4 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | -1 | 9.0 | 6.17 | 16.79 | 26.59 | 10.00 | 86.7 | 85.0 |
| XI | XI | Martin Ødegaard | MID | -1 | 8.6 | 5.16 | 14.29 | 22.74 | 3.00 | 88.3 | 90.0 |
| XI | XI | Luis Díaz | MID | -1 | 7.8 | 4.41 | 12.73 | 20.53 | 2.00 | 69.6 | 74.0 |

## GW37

- Train rows: 131952
- Bank: 2.90 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Cole Palmer
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 74.19
- Actual score: 107.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (12.21) beats the best remaining Triple Captain opportunity (8.39).
- Transfer: Rodrigo Muniz Carvalho -> Nicolas Jackson (projected gain 2.57, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (12.21) beats the best remaining Triple Captain opportunity (8.39).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Đorđe Petrović | GK | -1 | 4.6 | 4.13 | 9.56 | 14.00 | 3.00 | 118.4 | 180.0 |
| Bench 1 | Bench | André Onana | GK | -1 | 5.0 | 3.60 | 9.09 | 13.55 | 5.00 | 108.8 | 180.0 |
| XI | XI | Benjamin White | DEF | -1 | 6.1 | 4.58 | 13.56 | 21.42 | 6.00 | 95.4 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 5.9 | 4.33 | 12.50 | 19.48 | 9.00 | 97.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | -1 | 5.4 | 3.98 | 11.54 | 17.85 | 7.00 | 93.2 | 90.0 |
| Bench 3 | Bench | Joachim Andersen | DEF | -1 | 4.7 | 3.70 | 10.03 | 15.03 | 2.00 | 90.9 | 90.0 |
| Bench 4 | Bench | Alfie Doughty | DEF | -1 | 4.4 | 2.70 | 7.49 | 11.76 | 4.00 | 74.5 | 86.0 |
| Captain | Captain | Erling Haaland | FWD | -1 | 14.1 | 7.61 | 20.52 | 31.24 | 15.00 | 100.9 | 171.0 |
| XI | XI | Nicolas Jackson | FWD | -1 | 6.9 | 6.14 | 14.63 | 21.07 | 7.00 | 122.2 | 179.0 |
| XI | XI | Dominic Solanke | FWD | -1 | 7.2 | 4.40 | 12.35 | 19.36 | 6.00 | 85.3 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | -1 | 6.2 | 7.55 | 19.57 | 29.85 | 14.00 | 120.2 | 180.0 |
| XI | XI | Bukayo Saka | MID | -1 | 9.0 | 6.35 | 18.16 | 27.89 | 2.00 | 88.7 | 81.0 |
| XI | XI | Martin Ødegaard | MID | -1 | 8.6 | 5.09 | 14.90 | 23.37 | 3.00 | 91.7 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | -1 | 8.5 | 4.81 | 13.35 | 21.23 | 5.00 | 77.2 | 89.0 |
| Bench 2 | Bench | Luis Díaz | MID | -1 | 7.7 | 4.08 | 12.14 | 19.16 | 2.00 | 68.9 | 75.0 |

## GW38

- Train rows: 132813
- Bank: 0.50 -> 0.10
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Erling Haaland
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 73.35
- Actual score: 39.00
- Transfer: Joachim Andersen -> Joško Gvardiol (projected gain 7.12, hit 0)
- Autosub outfielders: Luis Díaz.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Đorđe Petrović | GK | -1 | 4.7 | 4.23 | 11.61 | 17.53 | 3.00 | 123.1 | 90.0 |
| Bench 1 | Bench | André Onana | GK | -1 | 5.0 | 3.94 | 11.23 | 17.48 | 7.00 | 124.3 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 5.1 | 6.62 | 18.04 | 27.22 | 2.00 | 123.9 | 90.0 |
| XI | XI | Benjamin White | DEF | -1 | 6.1 | 4.69 | 13.61 | 21.83 | 2.00 | 89.1 | 68.0 |
| XI | XI | William Saliba | DEF | -1 | 5.9 | 4.51 | 12.28 | 19.65 | 2.00 | 92.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | -1 | 5.4 | 4.07 | 11.15 | 17.75 | 1.00 | 88.0 | 58.0 |
| Bench 4 | Bench | Alfie Doughty | DEF | -1 | 4.3 | 3.08 | 8.26 | 12.88 | 5.00 | 78.5 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | -1 | 14.2 | 9.08 | 25.52 | 38.50 | 2.00 | 118.9 | 90.0 |
| XI | XI | Nicolas Jackson | FWD | -1 | 7.0 | 6.62 | 18.20 | 26.68 | 2.00 | 125.2 | 90.0 |
| Bench 3 | Bench | Dominic Solanke | FWD | -1 | 7.0 | 3.56 | 11.30 | 18.86 | 1.00 | 76.3 | 31.0 |
| Captain | Captain | Cole Palmer | MID | -1 | 6.3 | 9.21 | 25.06 | 37.97 | 6.00 | 148.9 | 88.0 |
| XI | Bench | Bukayo Saka | MID | -1 | 8.9 | 5.90 | 16.78 | 26.64 | 0.00 | 74.5 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | -1 | 8.5 | 4.40 | 14.02 | 23.45 | 0.00 | 71.4 | 59.0 |
| XI | XI | Martin Ødegaard | MID | -1 | 8.6 | 4.81 | 13.88 | 22.32 | 10.00 | 82.4 | 90.0 |
| Bench 2 | Autosub In | Luis Díaz | MID | -1 | 7.6 | 4.02 | 11.00 | 18.03 | 3.00 | 64.7 | 70.0 |