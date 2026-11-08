# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26
- In-season warm start: 2022-23 GW1-GW5
- Simulated weeks: GW6-GW38
- Total predicted points: 2125.74
- Total actual points: 1898.00
- Average predicted points: 64.42
- Average actual points: 57.52
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW5 are included before the first simulated week.
- League-average scores were not available for this run.

## GW6

- Train rows: 80619
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Gabriel Fernando de Jesus
- Vice captain: Mohamed Salah
- Effective captain: Gabriel Fernando de Jesus
- Chip used: none
- Predicted score: 64.65
- Actual score: 34.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub outfielders: Kieran Trippier.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Edouard Mendy | GK | -1 | 5.0 | 3.72 | 10.38 | 16.24 | 2.00 | 89.6 | 90.0 |
| Bench 1 | Bench | Robert Sánchez | GK | -1 | 4.6 | 3.42 | 10.09 | 15.89 | 1.00 | 84.1 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | -1 | 7.5 | 5.36 | 15.18 | 23.56 | 1.00 | 88.0 | 58.0 |
| XI | XI | João Cancelo | DEF | -1 | 7.1 | 4.97 | 13.67 | 21.27 | 2.00 | 80.6 | 90.0 |
| Bench 2 | Autosub In | Kieran Trippier | DEF | -1 | 5.1 | 4.10 | 11.86 | 19.08 | 8.00 | 88.0 | 90.0 |
| XI | XI | Ivan Perišić | DEF | -1 | 5.6 | 4.28 | 11.71 | 18.38 | 1.00 | 72.6 | 6.0 |
| Bench 3 | Bench | Gabriel dos Santos Magalhães | DEF | -1 | 5.0 | 3.47 | 10.22 | 15.81 | 1.00 | 84.2 | 90.0 |
| Captain | Captain | Gabriel Fernando de Jesus | FWD | -1 | 8.2 | 7.76 | 21.84 | 33.13 | 1.00 | 113.1 | 90.0 |
| XI | XI | Aleksandar Mitrović | FWD | -1 | 6.7 | 4.75 | 13.68 | 21.06 | 5.00 | 90.3 | 90.0 |
| Bench 4 | Bench | Odsonne Edouard | FWD | -1 | 5.4 | 2.17 | 6.31 | 9.76 | 1.00 | 49.5 | 27.0 |
| Vice Captain | XI | Mohamed Salah | MID | -1 | 13.0 | 7.04 | 20.12 | 32.29 | 3.00 | 95.8 | 90.0 |
| XI | XI | Gabriel Martinelli Silva | MID | -1 | 6.4 | 5.52 | 15.33 | 23.33 | 2.00 | 90.1 | 90.0 |
| XI | XI | Luis Díaz | MID | -1 | 8.1 | 5.13 | 14.76 | 22.75 | 3.00 | 80.9 | 90.0 |
| XI | XI | Pascal Groß | MID | -1 | 5.8 | 4.22 | 12.77 | 20.08 | 5.00 | 79.9 | 90.0 |
| XI | Bench | Rodrigo Moreno | MID | -1 | 6.5 | 4.14 | 12.62 | 19.77 | 0.00 | 55.2 | 0.0 |

## GW7

- Train rows: 81243
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Gabriel Fernando de Jesus
- Vice captain: Mohamed Salah
- Effective captain: Gabriel Fernando de Jesus
- Chip used: none
- Predicted score: 55.09
- Actual score: 0.00
- Transfer: Rodrigo Moreno -> Marcus Rashford (projected gain 2.21, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Robert Sánchez | GK | -1 | 4.7 | 2.60 | 7.94 | 13.30 | 0.00 | 68.5 | 0.0 |
| Bench 1 | Bench | Edouard Mendy | GK | -1 | 5.0 | 2.58 | 7.84 | 13.23 | 0.00 | 71.8 | 0.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | -1 | 7.5 | 4.44 | 13.08 | 21.64 | 0.00 | 70.7 | 0.0 |
| XI | Bench | João Cancelo | DEF | -1 | 7.1 | 4.15 | 11.87 | 18.98 | 0.00 | 66.0 | 0.0 |
| XI | Bench | Kieran Trippier | DEF | -1 | 5.1 | 3.67 | 10.91 | 17.78 | 0.00 | 73.2 | 0.0 |
| Bench 2 | Bench | Gabriel dos Santos Magalhães | DEF | -1 | 5.1 | 2.88 | 8.17 | 13.29 | 0.00 | 67.3 | 0.0 |
| Bench 3 | Bench | Ivan Perišić | DEF | -1 | 5.6 | 2.33 | 8.00 | 13.60 | 0.00 | 31.1 | 0.0 |
| Captain | Bench | Gabriel Fernando de Jesus | FWD | -1 | 8.2 | 6.82 | 19.45 | 30.44 | 0.00 | 93.0 | 0.0 |
| XI | Bench | Aleksandar Mitrović | FWD | -1 | 6.8 | 4.12 | 11.91 | 19.39 | 0.00 | 71.2 | 0.0 |
| Bench 4 | Bench | Odsonne Edouard | FWD | -1 | 5.4 | 1.29 | 4.15 | 7.35 | 0.00 | 27.8 | 0.0 |
| Vice Captain | Bench | Mohamed Salah | MID | -1 | 13.0 | 5.83 | 17.22 | 28.13 | 0.00 | 75.3 | 0.0 |
| XI | Bench | Gabriel Martinelli Silva | MID | -1 | 6.5 | 4.74 | 13.43 | 21.09 | 0.00 | 66.3 | 0.0 |
| XI | Bench | Luis Díaz | MID | -1 | 8.2 | 4.49 | 12.99 | 20.81 | 0.00 | 70.3 | 0.0 |
| XI | Bench | Pascal Groß | MID | -1 | 5.9 | 3.75 | 11.66 | 19.36 | 0.00 | 64.4 | 0.0 |
| XI | Bench | Marcus Rashford | MID | -1 | 6.4 | 3.66 | 10.25 | 16.50 | 0.00 | 68.2 | 0.0 |

## GW8

- Train rows: 81867
- Bank: 0.00 -> 1.40
- Free transfers: 2 -> 2
- Captain: Gabriel Fernando de Jesus
- Vice captain: Gabriel Martinelli Silva
- Effective captain: Gabriel Fernando de Jesus
- Chip used: none
- Predicted score: 42.16
- Actual score: 39.00
- Transfer: Marcus Rashford -> Granit Xhaka (projected gain 0.06, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Robert Sánchez | GK | -1 | 4.7 | 0.84 | 5.18 | 9.40 | 0.00 | 19.8 | 0.0 |
| Bench 1 | Bench | Edouard Mendy | GK | -1 | 5.0 | 0.73 | 4.93 | 9.11 | 0.00 | 19.1 | 0.0 |
| XI | XI | João Cancelo | DEF | -1 | 7.1 | 4.03 | 10.63 | 16.88 | 9.00 | 57.2 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | -1 | 7.5 | 2.41 | 10.08 | 17.11 | 0.00 | 25.8 | 0.0 |
| XI | XI | Kieran Trippier | DEF | -1 | 5.1 | 3.43 | 9.18 | 14.74 | 5.00 | 60.7 | 90.0 |
| XI | XI | Ivan Perišić | DEF | -1 | 5.6 | 2.82 | 7.84 | 12.47 | 2.00 | 42.4 | 54.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | -1 | 5.1 | 2.41 | 6.93 | 10.98 | 6.00 | 52.1 | 90.0 |
| Captain | Captain | Gabriel Fernando de Jesus | FWD | -1 | 8.2 | 6.15 | 16.80 | 26.27 | 6.00 | 79.2 | 90.0 |
| XI | XI | Aleksandar Mitrović | FWD | -1 | 6.8 | 3.74 | 10.28 | 16.32 | 2.00 | 59.6 | 89.0 |
| Bench 4 | Bench | Odsonne Edouard | FWD | -1 | 5.4 | 0.00 | 2.71 | 5.66 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Mohamed Salah | MID | -1 | 13.0 | 3.75 | 13.42 | 22.58 | 0.00 | 27.6 | 0.0 |
| Vice Captain | XI | Gabriel Martinelli Silva | MID | -1 | 6.5 | 4.12 | 11.09 | 17.38 | 3.00 | 58.9 | 77.0 |
| XI | Bench | Luis Díaz | MID | -1 | 8.2 | 2.33 | 9.28 | 15.57 | 0.00 | 20.0 | 0.0 |
| Bench 3 | Bench | Pascal Groß | MID | -1 | 5.9 | 1.94 | 8.18 | 13.99 | 0.00 | 24.7 | 0.0 |
| Bench 2 | Bench | Granit Xhaka | MID | -1 | 5.0 | 2.09 | 5.91 | 9.60 | 5.00 | 47.8 | 90.0 |

## GW9

- Train rows: 82498
- Bank: 1.40 -> 0.60
- Free transfers: 2 -> 2
- Captain: Gabriel Fernando de Jesus
- Vice captain: João Cancelo
- Effective captain: Gabriel Fernando de Jesus
- Chip used: none
- Predicted score: 55.89
- Actual score: 50.00
- Transfer: Robert Sánchez -> Ederson Santana de Moraes (projected gain 3.27, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Ederson Santana de Moraes | GK | -1 | 5.5 | 3.47 | 9.38 | 15.05 | 2.00 | 78.1 | 90.0 |
| Bench 1 | Bench | Edouard Mendy | GK | -1 | 5.0 | 2.19 | 6.28 | 10.38 | 0.00 | 46.6 | 0.0 |
| Vice Captain | XI | João Cancelo | DEF | -1 | 7.2 | 5.12 | 14.39 | 22.14 | 1.00 | 84.5 | 90.0 |
| XI | XI | Kieran Trippier | DEF | -1 | 5.3 | 5.00 | 14.33 | 21.66 | 7.00 | 79.9 | 82.0 |
| XI | XI | Trent Alexander-Arnold | DEF | -1 | 7.5 | 3.73 | 11.45 | 18.49 | 0.00 | 56.5 | 90.0 |
| Bench 2 | Bench | Ivan Perišić | DEF | -1 | 5.6 | 3.24 | 9.79 | 16.04 | 1.00 | 54.9 | 70.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | -1 | 5.1 | 3.63 | 9.78 | 15.03 | 2.00 | 78.9 | 90.0 |
| Captain | Captain | Gabriel Fernando de Jesus | FWD | -1 | 8.1 | 6.82 | 18.90 | 30.01 | 8.00 | 99.1 | 79.0 |
| XI | XI | Aleksandar Mitrović | FWD | -1 | 6.9 | 4.57 | 13.24 | 20.28 | 0.00 | 76.4 | 36.0 |
| Bench 4 | Bench | Odsonne Edouard | FWD | -1 | 5.4 | 1.37 | 3.79 | 6.49 | 5.00 | 26.0 | 83.0 |
| XI | XI | Mohamed Salah | MID | -1 | 13.0 | 4.83 | 14.11 | 22.61 | 5.00 | 56.2 | 90.0 |
| XI | XI | Gabriel Martinelli Silva | MID | -1 | 6.5 | 5.10 | 13.91 | 20.73 | 4.00 | 77.5 | 90.0 |
| XI | XI | Luis Díaz | MID | -1 | 8.2 | 3.45 | 10.11 | 16.17 | 4.00 | 49.2 | 45.0 |
| Bench 3 | Bench | Pascal Groß | MID | -1 | 5.9 | 3.00 | 8.87 | 14.21 | 2.00 | 52.6 | 64.0 |
| XI | XI | Granit Xhaka | MID | -1 | 5.0 | 3.36 | 8.62 | 13.35 | 9.00 | 74.8 | 90.0 |

## GW10

- Train rows: 83136
- Bank: 0.60 -> 0.00
- Free transfers: 2 -> 2
- Captain: Gabriel Fernando de Jesus
- Vice captain: João Cancelo
- Effective captain: Gabriel Fernando de Jesus
- Chip used: none
- Predicted score: 51.53
- Actual score: 63.00
- Transfer: Pascal Groß -> Marcus Rashford (projected gain 0.86, hit 0)
- Autosub outfielders: Trent Alexander-Arnold.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Ederson Santana de Moraes | GK | -1 | 5.5 | 3.44 | 9.19 | 14.78 | 6.00 | 77.7 | 90.0 |
| Bench 1 | Bench | Edouard Mendy | GK | -1 | 4.9 | 1.44 | 4.01 | 7.97 | 0.00 | 26.8 | 0.0 |
| XI | XI | Kieran Trippier | DEF | -1 | 5.4 | 4.85 | 13.44 | 21.54 | 7.00 | 83.2 | 83.0 |
| Vice Captain | XI | João Cancelo | DEF | -1 | 7.2 | 4.86 | 13.37 | 21.03 | 18.00 | 80.2 | 69.0 |
| XI | XI | Ivan Perišić | DEF | -1 | 5.6 | 3.36 | 9.55 | 15.58 | 1.00 | 60.9 | 10.0 |
| Bench 2 | Autosub In | Trent Alexander-Arnold | DEF | -1 | 7.4 | 3.14 | 9.45 | 17.08 | 0.00 | 62.5 | 45.0 |
| Bench 3 | Bench | Gabriel dos Santos Magalhães | DEF | -1 | 5.1 | 3.03 | 8.29 | 13.19 | 1.00 | 74.1 | 90.0 |
| Captain | Captain | Gabriel Fernando de Jesus | FWD | -1 | 8.0 | 6.39 | 18.59 | 29.74 | 5.00 | 95.6 | 90.0 |
| XI | Bench | Aleksandar Mitrović | FWD | -1 | 6.9 | 3.53 | 10.77 | 17.60 | 0.00 | 56.2 | 0.0 |
| Bench 4 | Bench | Odsonne Edouard | FWD | -1 | 5.3 | 2.60 | 6.52 | 10.09 | 8.00 | 52.9 | 85.0 |
| XI | XI | Gabriel Martinelli Silva | MID | -1 | 6.6 | 4.84 | 13.22 | 20.50 | 12.00 | 79.6 | 90.0 |
| XI | XI | Mohamed Salah | MID | -1 | 12.8 | 3.88 | 12.16 | 22.17 | 2.00 | 57.8 | 68.0 |
| XI | XI | Marcus Rashford | MID | -1 | 6.6 | 3.39 | 10.30 | 15.98 | 2.00 | 57.3 | 90.0 |
| XI | XI | Luis Díaz | MID | -1 | 8.2 | 3.33 | 9.94 | 17.02 | 3.00 | 53.0 | 41.0 |
| XI | XI | Granit Xhaka | MID | -1 | 5.1 | 3.28 | 8.58 | 13.53 | 2.00 | 76.2 | 90.0 |

## GW11

- Train rows: 83777
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Gabriel Fernando de Jesus
- Vice captain: Gabriel Martinelli Silva
- Effective captain: Gabriel Fernando de Jesus
- Chip used: none
- Predicted score: 52.73
- Actual score: 47.00
- Transfer: Granit Xhaka -> Miguel Almirón Rejala (projected gain 1.37, hit 0)
- Autosub outfielders: Odsonne Edouard.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Ederson Santana de Moraes | GK | -1 | 5.5 | 3.34 | 9.76 | 15.81 | 2.00 | 86.4 | 90.0 |
| Bench 1 | Bench | Edouard Mendy | GK | -1 | 4.9 | 1.37 | 4.17 | 7.73 | 0.00 | 27.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | -1 | 5.5 | 5.06 | 15.01 | 23.95 | 6.00 | 89.3 | 90.0 |
| XI | XI | João Cancelo | DEF | -1 | 7.2 | 5.15 | 14.48 | 23.00 | 2.00 | 87.6 | 90.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | -1 | 7.3 | 2.74 | 9.28 | 16.69 | 1.00 | 53.6 | 1.0 |
| XI | XI | Ivan Perišić | DEF | -1 | 5.6 | 3.23 | 8.97 | 14.96 | 8.00 | 48.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | -1 | 5.1 | 3.33 | 8.90 | 14.28 | 8.00 | 81.4 | 90.0 |
| Captain | Captain | Gabriel Fernando de Jesus | FWD | -1 | 8.0 | 6.81 | 18.78 | 29.66 | 2.00 | 103.7 | 81.0 |
| Bench 4 | Bench | Aleksandar Mitrović | FWD | -1 | 6.8 | 2.68 | 8.50 | 15.91 | 7.00 | 36.1 | 90.0 |
| Bench 2 | Autosub In | Odsonne Edouard | FWD | -1 | 5.3 | 2.78 | 7.64 | 12.14 | 2.00 | 64.2 | 64.0 |
| Vice Captain | XI | Gabriel Martinelli Silva | MID | -1 | 6.6 | 5.64 | 14.77 | 23.30 | 3.00 | 90.3 | 90.0 |
| XI | XI | Mohamed Salah | MID | -1 | 12.7 | 3.49 | 11.75 | 20.90 | 8.00 | 54.0 | 89.0 |
| XI | XI | Miguel Almirón Rejala | MID | -1 | 5.1 | 3.58 | 10.24 | 16.34 | 3.00 | 77.1 | 90.0 |
| XI | XI | Marcus Rashford | MID | -1 | 6.5 | 3.28 | 10.13 | 16.47 | 1.00 | 63.9 | 18.0 |
| XI | Bench | Luis Díaz | MID | -1 | 8.1 | 3.01 | 9.90 | 17.24 | 0.00 | 54.5 | 0.0 |

## GW12

- Train rows: 84420
- Bank: 0.00 -> 3.40
- Free transfers: 2 -> 2
- Captain: Kieran Trippier
- Vice captain: Mohamed Salah
- Effective captain: Kieran Trippier
- Chip used: none
- Predicted score: 49.29
- Actual score: 44.00
- Transfer: Luis Díaz -> Andreas Hoelgebaum Pereira (projected gain 3.43, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Ederson Santana de Moraes | GK | -1 | 5.5 | 1.90 | 8.01 | 13.93 | 0.00 | 50.2 | 0.0 |
| Bench 1 | Bench | Edouard Mendy | GK | -1 | 4.9 | 1.18 | 3.99 | 7.49 | 0.00 | 25.1 | 0.0 |
| Captain | Captain | Kieran Trippier | DEF | -1 | 5.6 | 5.86 | 16.01 | 25.64 | 9.00 | 95.0 | 90.0 |
| XI | Bench | João Cancelo | DEF | -1 | 7.3 | 3.71 | 12.99 | 21.41 | 0.00 | 51.0 | 0.0 |
| XI | XI | Ivan Perišić | DEF | -1 | 5.5 | 3.63 | 10.51 | 16.83 | 1.00 | 69.4 | 88.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | -1 | 7.3 | 2.48 | 7.81 | 15.03 | 8.00 | 33.4 | 90.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | -1 | 5.1 | 1.70 | 7.26 | 12.75 | 0.00 | 49.3 | 0.0 |
| XI | Bench | Gabriel Fernando de Jesus | FWD | -1 | 8.0 | 4.76 | 15.90 | 26.03 | 0.00 | 62.0 | 0.0 |
| XI | XI | Aleksandar Mitrović | FWD | -1 | 6.7 | 4.10 | 11.02 | 18.11 | 6.00 | 69.5 | 84.0 |
| Bench 2 | Bench | Odsonne Edouard | FWD | -1 | 5.3 | 2.60 | 6.98 | 11.50 | 5.00 | 59.4 | 80.0 |
| Vice Captain | XI | Mohamed Salah | MID | -1 | 12.7 | 4.92 | 13.59 | 22.72 | 3.00 | 73.5 | 90.0 |
| XI | Bench | Gabriel Martinelli Silva | MID | -1 | 6.6 | 3.62 | 12.73 | 21.08 | 0.00 | 52.1 | 0.0 |
| XI | XI | Andreas Hoelgebaum Pereira | MID | -1 | 4.6 | 4.08 | 10.38 | 16.14 | 3.00 | 78.1 | 86.0 |
| XI | XI | Miguel Almirón Rejala | MID | -1 | 5.2 | 3.91 | 10.32 | 16.53 | 10.00 | 79.3 | 72.0 |
| XI | XI | Marcus Rashford | MID | -1 | 6.5 | 2.93 | 8.51 | 14.10 | 3.00 | 50.2 | 90.0 |

## GW13

- Train rows: 85065
- Bank: 3.40 -> 2.90
- Free transfers: 2 -> 2
- Captain: Kieran Trippier
- Vice captain: Gabriel Fernando de Jesus
- Effective captain: Kieran Trippier
- Chip used: none
- Predicted score: 55.99
- Actual score: 44.00
- Transfer: Edouard Mendy -> Alisson Ramses Becker (projected gain 4.35, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alisson Ramses Becker | GK | -1 | 5.4 | 4.16 | 11.47 | 18.34 | 4.00 | 95.1 | 90.0 |
| Bench 1 | Bench | Ederson Santana de Moraes | GK | -1 | 5.5 | 2.41 | 7.17 | 11.62 | 5.00 | 54.0 | 90.0 |
| Captain | Captain | Kieran Trippier | DEF | -1 | 5.7 | 5.94 | 17.27 | 27.04 | 2.00 | 103.1 | 90.0 |
| XI | XI | João Cancelo | DEF | -1 | 7.3 | 4.37 | 12.29 | 19.44 | 2.00 | 63.2 | 90.0 |
| XI | XI | Ivan Perišić | DEF | -1 | 5.5 | 3.80 | 10.68 | 16.63 | 1.00 | 71.7 | 29.0 |
| XI | XI | Trent Alexander-Arnold | DEF | -1 | 7.2 | 3.64 | 10.07 | 16.04 | 1.00 | 65.6 | 28.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | -1 | 5.1 | 2.09 | 6.22 | 10.27 | 2.00 | 51.7 | 90.0 |
| Vice Captain | XI | Gabriel Fernando de Jesus | FWD | -1 | 8.0 | 5.61 | 15.64 | 24.11 | 2.00 | 72.8 | 90.0 |
| XI | XI | Aleksandar Mitrović | FWD | -1 | 6.7 | 4.85 | 13.31 | 20.27 | 6.00 | 73.9 | 90.0 |
| Bench 3 | Bench | Odsonne Edouard | FWD | -1 | 5.3 | 2.91 | 8.05 | 12.89 | 2.00 | 67.3 | 90.0 |
| XI | XI | Mohamed Salah | MID | -1 | 12.7 | 5.40 | 16.40 | 25.59 | 2.00 | 70.6 | 90.0 |
| XI | XI | Gabriel Martinelli Silva | MID | -1 | 6.6 | 4.30 | 12.03 | 18.90 | 2.00 | 62.0 | 70.0 |
| XI | XI | Miguel Almirón Rejala | MID | -1 | 5.2 | 3.75 | 11.06 | 16.97 | 10.00 | 77.8 | 90.0 |
| XI | XI | Andreas Hoelgebaum Pereira | MID | -1 | 4.6 | 4.25 | 11.00 | 16.76 | 10.00 | 78.8 | 90.0 |
| Bench 2 | Bench | Marcus Rashford | MID | -1 | 6.6 | 3.63 | 10.23 | 16.07 | 3.00 | 71.7 | 80.0 |

## GW14

- Train rows: 85713
- Bank: 2.90 -> 0.90
- Free transfers: 2 -> 2
- Captain: Kieran Trippier
- Vice captain: Gabriel Fernando de Jesus
- Effective captain: Kieran Trippier
- Chip used: none
- Predicted score: 59.00
- Actual score: 75.00
- Transfer: Odsonne Edouard -> Ivan Toney (projected gain 2.45, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alisson Ramses Becker | GK | -1 | 5.4 | 3.71 | 10.91 | 17.80 | 2.00 | 88.0 | 90.0 |
| Bench 1 | Bench | Ederson Santana de Moraes | GK | -1 | 5.4 | 3.15 | 9.32 | 14.85 | 9.00 | 77.3 | 90.0 |
| Captain | Captain | Kieran Trippier | DEF | -1 | 5.7 | 6.10 | 17.15 | 27.15 | 11.00 | 104.7 | 90.0 |
| XI | XI | João Cancelo | DEF | -1 | 7.3 | 4.85 | 14.43 | 22.51 | 6.00 | 82.4 | 90.0 |
| XI | XI | Ivan Perišić | DEF | -1 | 5.5 | 3.37 | 9.59 | 15.50 | 4.00 | 60.1 | 27.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | -1 | 7.2 | 3.08 | 8.54 | 13.77 | 2.00 | 47.8 | 78.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | -1 | 5.1 | 2.98 | 8.28 | 13.29 | 6.00 | 74.3 | 90.0 |
| Vice Captain | XI | Gabriel Fernando de Jesus | FWD | -1 | 8.0 | 5.70 | 15.74 | 25.55 | 9.00 | 81.1 | 90.0 |
| XI | XI | Aleksandar Mitrović | FWD | -1 | 6.8 | 5.17 | 13.53 | 21.47 | 1.00 | 83.9 | 90.0 |
| XI | XI | Ivan Toney | FWD | -1 | 7.4 | 4.83 | 12.96 | 20.03 | 1.00 | 80.9 | 90.0 |
| XI | XI | Mohamed Salah | MID | -1 | 12.8 | 5.35 | 14.83 | 24.12 | 7.00 | 73.9 | 90.0 |
| XI | XI | Gabriel Martinelli Silva | MID | -1 | 6.7 | 4.59 | 13.10 | 20.50 | 8.00 | 67.9 | 62.0 |
| XI | XI | Andreas Hoelgebaum Pereira | MID | -1 | 4.6 | 4.81 | 12.39 | 18.80 | 3.00 | 86.2 | 75.0 |
| XI | XI | Miguel Almirón Rejala | MID | -1 | 5.3 | 4.41 | 12.16 | 19.00 | 12.00 | 81.2 | 85.0 |
| Bench 2 | Bench | Marcus Rashford | MID | -1 | 6.6 | 3.97 | 10.60 | 16.36 | 8.00 | 66.1 | 90.0 |

## GW15

- Train rows: 86369
- Bank: 0.90 -> 1.10
- Free transfers: 2 -> 2
- Captain: Kieran Trippier
- Vice captain: Gabriel Fernando de Jesus
- Effective captain: Kieran Trippier
- Chip used: none
- Predicted score: 59.12
- Actual score: 64.00
- Transfer: Gabriel dos Santos Magalhães -> Fabian Schär (projected gain 0.81, hit 0)
- Autosub outfielders: Andreas Hoelgebaum Pereira, Trent Alexander-Arnold.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Alisson Ramses Becker | GK | -1 | 5.4 | 3.20 | 10.12 | 16.06 | 3.00 | 86.7 | 90.0 |
| XI | XI | Ederson Santana de Moraes | GK | -1 | 5.4 | 3.58 | 9.39 | 14.99 | 2.00 | 78.1 | 90.0 |
| Captain | Captain | Kieran Trippier | DEF | -1 | 5.8 | 6.52 | 17.84 | 27.88 | 12.00 | 109.5 | 79.0 |
| XI | XI | João Cancelo | DEF | -1 | 7.4 | 5.62 | 15.18 | 23.30 | -2.00 | 86.1 | 25.0 |
| XI | XI | Fabian Schär | DEF | -1 | 4.9 | 3.85 | 10.25 | 15.87 | 2.00 | 81.1 | 90.0 |
| Bench 4 | Bench | Ivan Perišić | DEF | -1 | 5.5 | 3.20 | 9.47 | 15.14 | 1.00 | 58.3 | 90.0 |
| Bench 3 | Autosub In | Trent Alexander-Arnold | DEF | -1 | 7.2 | 3.27 | 9.47 | 14.80 | 2.00 | 65.1 | 90.0 |
| Vice Captain | XI | Gabriel Fernando de Jesus | FWD | -1 | 8.0 | 5.91 | 16.93 | 27.01 | 2.00 | 89.6 | 90.0 |
| XI | Bench | Aleksandar Mitrović | FWD | -1 | 6.9 | 4.45 | 13.06 | 20.50 | 0.00 | 75.1 | 0.0 |
| XI | Bench | Ivan Toney | FWD | -1 | 7.5 | 4.27 | 11.79 | 17.96 | 0.00 | 73.3 | 0.0 |
| XI | XI | Mohamed Salah | MID | -1 | 12.8 | 5.24 | 15.24 | 24.25 | 15.00 | 78.4 | 90.0 |
| XI | XI | Miguel Almirón Rejala | MID | -1 | 5.5 | 4.59 | 13.29 | 21.55 | 8.00 | 74.0 | 80.0 |
| XI | XI | Gabriel Martinelli Silva | MID | -1 | 6.8 | 4.46 | 13.05 | 20.40 | 3.00 | 71.0 | 90.0 |
| XI | XI | Marcus Rashford | MID | -1 | 6.6 | 4.12 | 11.07 | 17.40 | 2.00 | 73.1 | 90.0 |
| Bench 2 | Autosub In | Andreas Hoelgebaum Pereira | MID | -1 | 4.6 | 3.65 | 10.87 | 17.04 | 6.00 | 74.8 | 87.0 |

## GW16

- Train rows: 87030
- Bank: 1.10 -> 0.80
- Free transfers: 2 -> 2
- Captain: Kieran Trippier
- Vice captain: Gabriel Fernando de Jesus
- Effective captain: Kieran Trippier
- Chip used: none
- Predicted score: 60.13
- Actual score: 45.00
- Transfer: Fabian Schär -> William Saliba (projected gain 1.20, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alisson Ramses Becker | GK | -1 | 5.4 | 3.82 | 10.50 | 16.30 | 3.00 | 88.4 | 90.0 |
| Bench 1 | Bench | Ederson Santana de Moraes | GK | -1 | 5.4 | 3.28 | 9.00 | 14.75 | 2.00 | 82.3 | 90.0 |
| Captain | Captain | Kieran Trippier | DEF | -1 | 5.9 | 6.37 | 17.66 | 27.95 | 7.00 | 108.7 | 90.0 |
| XI | XI | João Cancelo | DEF | -1 | 7.4 | 4.55 | 12.65 | 20.30 | 1.00 | 64.7 | 85.0 |
| XI | XI | William Saliba | DEF | -1 | 5.2 | 4.15 | 10.79 | 17.00 | 6.00 | 83.5 | 90.0 |
| XI | XI | Ivan Perišić | DEF | -1 | 5.5 | 4.05 | 10.33 | 16.12 | 1.00 | 70.0 | 90.0 |
| Bench 2 | Bench | Trent Alexander-Arnold | DEF | -1 | 7.2 | 3.72 | 9.62 | 15.08 | 2.00 | 69.8 | 86.0 |
| Vice Captain | XI | Gabriel Fernando de Jesus | FWD | -1 | 8.0 | 6.30 | 17.32 | 27.74 | 2.00 | 91.4 | 90.0 |
| Bench 3 | Bench | Aleksandar Mitrović | FWD | -1 | 6.9 | 3.51 | 9.96 | 16.27 | 0.00 | 39.0 | 0.0 |
| Bench 4 | Bench | Ivan Toney | FWD | -1 | 7.4 | 1.33 | 5.82 | 12.28 | 13.00 | 23.4 | 90.0 |
| XI | XI | Mohamed Salah | MID | -1 | 12.8 | 6.19 | 16.47 | 26.11 | 2.00 | 86.1 | 90.0 |
| XI | XI | Miguel Almirón Rejala | MID | -1 | 5.7 | 4.91 | 14.34 | 23.25 | 6.00 | 76.5 | 90.0 |
| XI | XI | Gabriel Martinelli Silva | MID | -1 | 6.8 | 5.12 | 13.64 | 21.53 | 6.00 | 80.7 | 90.0 |
| XI | XI | Andreas Hoelgebaum Pereira | MID | -1 | 4.6 | 4.25 | 11.30 | 18.06 | 2.00 | 81.6 | 90.0 |
| XI | XI | Marcus Rashford | MID | -1 | 6.7 | 4.05 | 10.99 | 17.26 | 2.00 | 69.3 | 90.0 |

## GW17

- Train rows: 87697
- Bank: 0.80 -> 2.10
- Free transfers: 2 -> 2
- Captain: Gabriel Fernando de Jesus
- Vice captain: Kieran Trippier
- Effective captain: Kieran Trippier
- Chip used: none
- Predicted score: 61.41
- Actual score: 79.00
- Transfer: Ederson Santana de Moraes -> Danny Ward (projected gain 0.21, hit 0)
- Autosub outfielders: Ivan Perišić.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Danny Ward | GK | -1 | 4.1 | 4.08 | 11.02 | 17.21 | 1.00 | 93.7 | 90.0 |
| Bench 1 | Bench | Alisson Ramses Becker | GK | -1 | 5.4 | 3.78 | 10.83 | 17.21 | 3.00 | 91.6 | 90.0 |
| Vice Captain | Captain | Kieran Trippier | DEF | -1 | 5.9 | 6.09 | 17.45 | 27.95 | 12.00 | 109.2 | 90.0 |
| XI | XI | João Cancelo | DEF | -1 | 7.4 | 4.98 | 13.71 | 22.10 | 1.00 | 74.8 | 22.0 |
| XI | XI | William Saliba | DEF | -1 | 5.3 | 4.17 | 11.00 | 17.43 | 2.00 | 82.1 | 90.0 |
| Bench 2 | Autosub In | Ivan Perišić | DEF | -1 | 5.5 | 3.76 | 10.33 | 16.23 | 1.00 | 73.9 | 90.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | -1 | 7.2 | 3.57 | 9.84 | 15.67 | 2.00 | 74.6 | 78.0 |
| Captain | Bench | Gabriel Fernando de Jesus | FWD | -1 | 8.0 | 6.47 | 17.61 | 28.01 | 0.00 | 92.2 | 0.0 |
| XI | XI | Ivan Toney | FWD | -1 | 7.4 | 4.08 | 10.45 | 16.40 | 5.00 | 69.1 | 90.0 |
| Bench 4 | Bench | Aleksandar Mitrović | FWD | -1 | 6.8 | 2.67 | 8.14 | 14.48 | 15.00 | 24.6 | 84.0 |
| XI | XI | Mohamed Salah | MID | -1 | 12.8 | 5.71 | 16.15 | 25.87 | 12.00 | 82.7 | 90.0 |
| XI | XI | Miguel Almirón Rejala | MID | -1 | 5.8 | 5.55 | 15.68 | 24.76 | 8.00 | 91.4 | 82.0 |
| XI | XI | Gabriel Martinelli Silva | MID | -1 | 6.8 | 5.41 | 14.33 | 22.72 | 8.00 | 86.1 | 87.0 |
| XI | XI | Marcus Rashford | MID | -1 | 6.7 | 4.30 | 11.35 | 17.97 | 14.00 | 77.3 | 85.0 |
| XI | XI | Andreas Hoelgebaum Pereira | MID | -1 | 4.6 | 4.09 | 11.17 | 17.51 | 3.00 | 81.0 | 84.0 |

## GW18

- Train rows: 88372
- Bank: 2.10 -> 3.00
- Free transfers: 2 -> 2
- Captain: Kieran Trippier
- Vice captain: Miguel Almirón Rejala
- Effective captain: Kieran Trippier
- Chip used: none
- Predicted score: 53.52
- Actual score: 47.00
- Transfer: João Cancelo -> Virgil van Dijk (projected gain 0.98, hit 0)
- Autosub outfielders: Ivan Perišić.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Danny Ward | GK | -1 | 4.1 | 2.56 | 12.47 | 21.20 | 3.00 | 70.4 | 90.0 |
| XI | XI | Alisson Ramses Becker | GK | -1 | 5.5 | 3.33 | 12.05 | 20.74 | 2.00 | 82.3 | 90.0 |
| Captain | Captain | Kieran Trippier | DEF | -1 | 5.9 | 6.43 | 18.75 | 33.84 | 8.00 | 102.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | -1 | 6.5 | 3.58 | 12.05 | 20.32 | 2.00 | 79.3 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 5.3 | 3.29 | 11.69 | 20.71 | 1.00 | 60.0 | 90.0 |
| Bench 2 | Autosub In | Ivan Perišić | DEF | -1 | 5.5 | 3.10 | 11.67 | 21.62 | 1.00 | 63.1 | 87.0 |
| Bench 4 | Bench | Trent Alexander-Arnold | DEF | -1 | 7.2 | 2.62 | 8.84 | 21.22 | 8.00 | 60.9 | 85.0 |
| XI | Bench | Gabriel Fernando de Jesus | FWD | -1 | 8.0 | 3.40 | 11.87 | 24.27 | 0.00 | 23.2 | 0.0 |
| XI | XI | Aleksandar Mitrović | FWD | -1 | 6.8 | 3.96 | 11.07 | 21.13 | 0.00 | 31.8 | 90.0 |
| Bench 3 | Bench | Ivan Toney | FWD | -1 | 7.4 | 2.87 | 10.60 | 19.97 | 12.00 | 16.8 | 90.0 |
| Vice Captain | XI | Miguel Almirón Rejala | MID | -1 | 5.8 | 5.66 | 16.82 | 29.96 | 3.00 | 66.2 | 83.0 |
| XI | XI | Mohamed Salah | MID | -1 | 12.8 | 5.43 | 16.80 | 29.41 | 2.00 | 50.4 | 90.0 |
| XI | XI | Gabriel Martinelli Silva | MID | -1 | 6.8 | 4.68 | 15.63 | 27.24 | 10.00 | 68.4 | 90.0 |
| XI | XI | Marcus Rashford | MID | -1 | 6.7 | 3.91 | 13.62 | 24.81 | 5.00 | 44.7 | 45.0 |
| XI | XI | Andreas Hoelgebaum Pereira | MID | -1 | 4.6 | 3.40 | 12.30 | 22.70 | 5.00 | 54.6 | 90.0 |

## GW19

- Train rows: 89050
- Bank: 3.00 -> 3.10
- Free transfers: 2 -> 2
- Captain: Kieran Trippier
- Vice captain: Gabriel Martinelli Silva
- Effective captain: Kieran Trippier
- Chip used: none
- Predicted score: 63.41
- Actual score: 64.00
- Transfer: William Saliba -> Gabriel dos Santos Magalhães (projected gain 0.42, hit 0)
- Autosub outfielders: Gabriel dos Santos Magalhães.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Danny Ward | GK | -1 | 4.1 | 4.38 | 13.37 | 22.09 | 2.00 | 96.6 | 90.0 |
| Bench 1 | Bench | Alisson Ramses Becker | GK | -1 | 5.5 | 3.87 | 13.00 | 20.96 | 2.00 | 98.4 | 90.0 |
| Captain | Captain | Kieran Trippier | DEF | -1 | 5.9 | 6.55 | 22.34 | 34.99 | 8.00 | 121.3 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | -1 | 7.2 | 3.95 | 14.00 | 22.38 | 5.00 | 86.8 | 90.0 |
| XI | XI | Ivan Perišić | DEF | -1 | 5.5 | 4.13 | 13.89 | 22.31 | 10.00 | 88.0 | 85.0 |
| Bench 2 | Autosub In | Gabriel dos Santos Magalhães | DEF | -1 | 5.2 | 3.83 | 12.83 | 19.57 | 6.00 | 89.1 | 90.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | -1 | 6.5 | 3.78 | 12.77 | 20.50 | 0.00 | 92.8 | 45.0 |
| XI | XI | Aleksandar Mitrović | FWD | -1 | 7.0 | 5.29 | 14.49 | 21.24 | 5.00 | 94.8 | 90.0 |
| XI | Bench | Ivan Toney | FWD | -1 | 7.5 | 4.67 | 14.22 | 22.04 | 0.00 | 87.4 | 0.0 |
| Bench 4 | Bench | Gabriel Fernando de Jesus | FWD | -1 | 8.0 | 3.33 | 10.99 | 17.97 | 0.00 | 41.7 | 0.0 |
| XI | XI | Miguel Almirón Rejala | MID | -1 | 5.9 | 5.60 | 19.15 | 29.32 | 2.00 | 103.7 | 67.0 |
| Vice Captain | XI | Gabriel Martinelli Silva | MID | -1 | 6.8 | 6.07 | 18.59 | 28.26 | 3.00 | 100.9 | 90.0 |
| XI | XI | Mohamed Salah | MID | -1 | 12.8 | 5.66 | 17.95 | 27.53 | 2.00 | 90.2 | 90.0 |
| XI | XI | Andreas Hoelgebaum Pereira | MID | -1 | 4.6 | 5.76 | 15.40 | 22.86 | 5.00 | 115.4 | 148.0 |
| XI | XI | Marcus Rashford | MID | -1 | 6.8 | 4.80 | 15.31 | 24.41 | 8.00 | 77.0 | 90.0 |

## GW20

- Train rows: 89739
- Bank: 3.10 -> 1.10
- Free transfers: 2 -> 2
- Captain: Martin Ødegaard
- Vice captain: Kieran Trippier
- Effective captain: Martin Ødegaard
- Chip used: none
- Predicted score: 57.14
- Actual score: 64.00
- Transfer: Andreas Hoelgebaum Pereira -> Martin Ødegaard (projected gain 11.29, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alisson Ramses Becker | GK | -1 | 5.5 | 1.93 | 8.83 | 14.10 | 2.00 | 62.7 | 90.0 |
| Bench 1 | Bench | Danny Ward | GK | -1 | 4.1 | 1.65 | 7.56 | 11.54 | 2.00 | 46.3 | 90.0 |
| Vice Captain | XI | Kieran Trippier | DEF | -1 | 5.9 | 6.79 | 24.83 | 40.45 | 9.00 | 111.7 | 90.0 |
| Bench 4 | Bench | Trent Alexander-Arnold | DEF | -1 | 7.2 | 1.80 | 13.39 | 23.31 | 0.00 | 46.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | -1 | 5.2 | 3.29 | 12.34 | 19.37 | 5.00 | 82.0 | 90.0 |
| XI | XI | Ivan Perišić | DEF | -1 | 5.5 | 3.17 | 12.29 | 18.55 | 2.00 | 73.2 | 82.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | -1 | 6.5 | 2.02 | 8.34 | 13.51 | 0.00 | 48.9 | 0.0 |
| XI | XI | Aleksandar Mitrović | FWD | -1 | 7.1 | 3.48 | 14.48 | 23.87 | 0.00 | 70.1 | 90.0 |
| Bench 2 | Bench | Gabriel Fernando de Jesus | FWD | -1 | 8.0 | 2.56 | 9.42 | 16.81 | 0.00 | 32.3 | 0.0 |
| XI | XI | Ivan Toney | FWD | -1 | 7.5 | 2.68 | 6.25 | 11.18 | 9.00 | 13.5 | 81.0 |
| XI | XI | Miguel Almirón Rejala | MID | -1 | 5.9 | 5.43 | 20.16 | 32.75 | 3.00 | 89.6 | 84.0 |
| Captain | Captain | Martin Ødegaard | MID | -1 | 6.6 | 7.45 | 19.43 | 31.99 | 9.00 | 105.9 | 90.0 |
| XI | XI | Gabriel Martinelli Silva | MID | -1 | 6.8 | 4.89 | 17.92 | 28.16 | 2.00 | 80.7 | 78.0 |
| XI | XI | Mohamed Salah | MID | -1 | 12.9 | 5.61 | 16.60 | 27.11 | 2.00 | 74.2 | 90.0 |
| XI | XI | Marcus Rashford | MID | -1 | 6.9 | 4.97 | 15.34 | 23.84 | 12.00 | 86.1 | 180.0 |

## GW21

- Train rows: 90438
- Bank: 1.10 -> 2.50
- Free transfers: 2 -> 2
- Captain: Kieran Trippier
- Vice captain: Martin Ødegaard
- Effective captain: Kieran Trippier
- Chip used: none
- Predicted score: 71.05
- Actual score: 46.00
- Transfer: Virgil van Dijk -> Luke Shaw (projected gain 5.73, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Danny Ward | GK | -1 | 4.1 | 2.74 | 9.86 | 15.53 | 1.00 | 78.7 | 90.0 |
| Bench 1 | Bench | Alisson Ramses Becker | GK | -1 | 5.5 | 2.58 | 9.10 | 14.67 | 9.00 | 82.3 | 90.0 |
| Captain | Captain | Kieran Trippier | DEF | -1 | 6.0 | 8.37 | 20.66 | 34.01 | 8.00 | 120.6 | 90.0 |
| XI | XI | Luke Shaw | DEF | -1 | 5.1 | 5.20 | 13.38 | 22.50 | 0.00 | 114.8 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | -1 | 7.3 | 6.20 | 13.02 | 24.67 | 1.00 | 100.1 | 18.0 |
| XI | XI | Ivan Perišić | DEF | -1 | 5.5 | 4.30 | 12.43 | 21.67 | 6.00 | 76.8 | 90.0 |
| Bench 3 | Bench | Gabriel dos Santos Magalhães | DEF | -1 | 5.2 | 3.51 | 9.77 | 15.63 | 1.00 | 86.6 | 90.0 |
| XI | XI | Aleksandar Mitrović | FWD | -1 | 7.2 | 4.25 | 11.57 | 20.27 | 2.00 | 84.4 | 90.0 |
| Bench 2 | Bench | Ivan Toney | FWD | -1 | 7.4 | 3.97 | 7.80 | 14.99 | 1.00 | 68.1 | 90.0 |
| Bench 4 | Bench | Gabriel Fernando de Jesus | FWD | -1 | 7.9 | 2.63 | 6.09 | 11.69 | 0.00 | 34.2 | 0.0 |
| XI | XI | Marcus Rashford | MID | -1 | 7.0 | 6.77 | 18.97 | 31.63 | 7.00 | 125.1 | 90.0 |
| XI | XI | Gabriel Martinelli Silva | MID | -1 | 6.8 | 6.07 | 17.02 | 27.77 | 2.00 | 80.4 | 81.0 |
| Vice Captain | XI | Martin Ødegaard | MID | -1 | 6.7 | 7.03 | 14.76 | 26.52 | 5.00 | 106.5 | 90.0 |
| XI | XI | Miguel Almirón Rejala | MID | -1 | 5.9 | 6.28 | 14.69 | 24.56 | 3.00 | 100.0 | 85.0 |
| XI | XI | Mohamed Salah | MID | -1 | 12.9 | 5.46 | 12.90 | 23.73 | 3.00 | 83.3 | 90.0 |

## GW22

- Train rows: 91145
- Bank: 2.50 -> 4.70
- Free transfers: 2 -> 2
- Captain: Marcus Rashford
- Vice captain: Kieran Trippier
- Effective captain: Marcus Rashford
- Chip used: none
- Predicted score: 65.70
- Actual score: 66.00
- Transfer: Trent Alexander-Arnold -> Fabian Schär (projected gain 2.02, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Danny Ward | GK | -1 | 4.1 | 3.50 | 9.84 | 15.69 | 2.00 | 81.2 | 90.0 |
| Bench 1 | Bench | Alisson Ramses Becker | GK | -1 | 5.5 | 3.16 | 9.71 | 16.01 | 2.00 | 86.8 | 90.0 |
| Vice Captain | XI | Kieran Trippier | DEF | -1 | 6.0 | 7.61 | 21.48 | 36.02 | 2.00 | 107.8 | 90.0 |
| XI | XI | Luke Shaw | DEF | -1 | 5.2 | 5.01 | 12.14 | 18.22 | 6.00 | 113.8 | 180.0 |
| XI | XI | Ivan Perišić | DEF | -1 | 5.5 | 3.79 | 11.63 | 20.19 | 5.00 | 82.2 | 78.0 |
| XI | XI | Fabian Schär | DEF | -1 | 5.1 | 4.40 | 11.57 | 18.48 | 2.00 | 86.2 | 90.0 |
| Bench 2 | Bench | Gabriel dos Santos Magalhães | DEF | -1 | 5.2 | 3.69 | 9.60 | 15.52 | 2.00 | 84.1 | 90.0 |
| XI | XI | Aleksandar Mitrović | FWD | -1 | 7.1 | 3.42 | 10.90 | 18.59 | 2.00 | 75.4 | 90.0 |
| Bench 3 | Bench | Ivan Toney | FWD | -1 | 7.6 | 3.36 | 9.09 | 15.50 | 1.00 | 49.9 | 90.0 |
| Bench 4 | Bench | Gabriel Fernando de Jesus | FWD | -1 | 7.9 | 2.30 | 7.05 | 12.48 | 0.00 | 28.3 | 0.0 |
| Captain | Captain | Marcus Rashford | MID | -1 | 7.1 | 8.15 | 21.14 | 32.31 | 20.00 | 137.5 | 180.0 |
| XI | XI | Gabriel Martinelli Silva | MID | -1 | 6.8 | 5.90 | 16.02 | 26.17 | 1.00 | 75.5 | 58.0 |
| XI | XI | Martin Ødegaard | MID | -1 | 6.8 | 5.49 | 15.45 | 26.65 | 2.00 | 87.1 | 76.0 |
| XI | XI | Miguel Almirón Rejala | MID | -1 | 5.9 | 5.22 | 14.19 | 23.39 | 2.00 | 85.8 | 80.0 |
| XI | XI | Mohamed Salah | MID | -1 | 12.8 | 5.06 | 14.03 | 24.49 | 2.00 | 79.3 | 90.0 |

## GW23

- Train rows: 91885
- Bank: 4.70 -> 0.40
- Free transfers: 2 -> 2
- Captain: Marcus Rashford
- Vice captain: Erling Haaland
- Effective captain: Marcus Rashford
- Chip used: none
- Predicted score: 68.86
- Actual score: 78.00
- Chip advisory: bench_boost (0.58): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Transfer: Gabriel Fernando de Jesus -> Erling Haaland (projected gain 12.21, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Danny Ward | GK | -1 | 4.0 | 3.68 | 9.54 | 15.78 | 3.00 | 80.9 | 90.0 |
| Bench 1 | Bench | Alisson Ramses Becker | GK | -1 | 5.4 | 3.27 | 9.17 | 15.48 | 6.00 | 81.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | -1 | 6.1 | 6.60 | 20.36 | 33.13 | 2.00 | 106.0 | 90.0 |
| XI | XI | Luke Shaw | DEF | -1 | 5.3 | 4.99 | 15.40 | 23.67 | 12.00 | 119.9 | 90.0 |
| Bench 2 | Bench | Ivan Perišić | DEF | -1 | 5.5 | 3.76 | 11.83 | 18.97 | 1.00 | 81.7 | 74.0 |
| XI | XI | Fabian Schär | DEF | -1 | 5.2 | 3.80 | 11.22 | 18.41 | 2.00 | 84.4 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | -1 | 5.2 | 4.20 | 10.43 | 16.66 | 3.00 | 112.8 | 180.0 |
| Vice Captain | XI | Erling Haaland | FWD | -1 | 12.2 | 8.39 | 23.65 | 36.99 | 10.00 | 154.5 | 135.0 |
| Bench 3 | Bench | Ivan Toney | FWD | -1 | 7.7 | 3.46 | 11.47 | 18.81 | 9.00 | 70.6 | 90.0 |
| Bench 4 | Bench | Aleksandar Mitrović | FWD | -1 | 7.0 | 3.12 | 10.43 | 19.17 | 2.00 | 71.8 | 83.0 |
| Captain | Captain | Marcus Rashford | MID | -1 | 7.2 | 8.71 | 25.58 | 38.98 | 8.00 | 152.0 | 90.0 |
| XI | XI | Martin Ødegaard | MID | -1 | 6.9 | 5.88 | 17.01 | 26.51 | 4.00 | 113.8 | 180.0 |
| XI | XI | Gabriel Martinelli Silva | MID | -1 | 6.7 | 5.41 | 15.28 | 25.31 | 5.00 | 100.6 | 136.0 |
| XI | XI | Mohamed Salah | MID | -1 | 12.7 | 4.26 | 13.57 | 24.30 | 11.00 | 77.0 | 89.0 |
| XI | XI | Miguel Almirón Rejala | MID | -1 | 5.8 | 4.24 | 12.65 | 21.18 | 10.00 | 76.6 | 80.0 |

## GW24

- Train rows: 92630
- Bank: 0.40 -> 0.90
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Martin Ødegaard
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 68.31
- Actual score: 52.00
- Chip advisory: bench_boost (0.62): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Alisson Ramses Becker -> Aaron Ramsdale (projected gain 3.07, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Aaron Ramsdale | GK | -1 | 4.9 | 4.23 | 12.27 | 19.40 | 2.00 | 113.8 | 90.0 |
| Bench 1 | Bench | Danny Ward | GK | -1 | 4.0 | 3.18 | 9.21 | 15.44 | 2.00 | 80.1 | 90.0 |
| XI | XI | Kieran Trippier | DEF | -1 | 6.1 | 6.74 | 19.85 | 31.79 | 1.00 | 112.1 | 63.0 |
| XI | XI | Luke Shaw | DEF | -1 | 5.3 | 4.22 | 13.35 | 21.30 | 6.00 | 104.1 | 68.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | -1 | 5.2 | 4.18 | 12.26 | 19.69 | 1.00 | 113.4 | 90.0 |
| Bench 2 | Bench | Ivan Perišić | DEF | -1 | 5.5 | 3.94 | 11.01 | 18.10 | 0.00 | 74.6 | 12.0 |
| Bench 3 | Bench | Fabian Schär | DEF | -1 | 5.2 | 3.58 | 10.61 | 17.65 | 1.00 | 83.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | -1 | 12.2 | 8.45 | 23.41 | 39.36 | 2.00 | 144.9 | 90.0 |
| XI | XI | Ivan Toney | FWD | -1 | 7.6 | 4.34 | 12.34 | 20.49 | 2.00 | 79.4 | 90.0 |
| Bench 4 | Bench | Aleksandar Mitrović | FWD | -1 | 7.0 | 3.51 | 10.15 | 19.30 | 0.00 | 75.2 | 0.0 |
| Vice Captain | XI | Martin Ødegaard | MID | -1 | 7.0 | 6.98 | 19.69 | 30.76 | 8.00 | 124.0 | 90.0 |
| XI | XI | Marcus Rashford | MID | -1 | 7.2 | 6.30 | 19.66 | 33.62 | 15.00 | 129.1 | 68.0 |
| XI | XI | Gabriel Martinelli Silva | MID | -1 | 6.6 | 5.59 | 15.80 | 24.70 | 6.00 | 94.8 | 22.0 |
| XI | XI | Mohamed Salah | MID | -1 | 12.7 | 4.76 | 13.73 | 22.79 | 6.00 | 75.1 | 90.0 |
| XI | XI | Miguel Almirón Rejala | MID | -1 | 5.7 | 4.07 | 12.13 | 20.22 | 1.00 | 80.0 | 63.0 |

## GW25

- Train rows: 93376
- Bank: 0.90 -> 0.80
- Free transfers: 2 -> 2
- Captain: Martin Ødegaard
- Vice captain: Erling Haaland
- Effective captain: Martin Ødegaard
- Chip used: none
- Predicted score: 62.23
- Actual score: 109.00
- Transfer: Fabian Schär -> William Saliba (projected gain 5.91, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Aaron Ramsdale | GK | -1 | 4.9 | 4.58 | 11.44 | 17.07 | 13.00 | 121.2 | 180.0 |
| Bench 1 | Bench | Danny Ward | GK | -1 | 4.0 | 3.15 | 10.13 | 16.43 | 2.00 | 83.4 | 90.0 |
| XI | Bench | Kieran Trippier | DEF | -1 | 6.1 | 4.95 | 17.21 | 26.71 | 0.00 | 66.0 | 0.0 |
| XI | XI | William Saliba | DEF | -1 | 5.3 | 5.12 | 12.82 | 19.29 | 12.00 | 122.3 | 180.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | -1 | 5.2 | 4.37 | 11.49 | 17.35 | 15.00 | 119.4 | 180.0 |
| XI | Bench | Luke Shaw | DEF | -1 | 5.4 | 3.02 | 10.55 | 17.59 | 0.00 | 55.9 | 0.0 |
| XI | Bench | Ivan Perišić | DEF | -1 | 5.5 | 2.61 | 7.74 | 13.90 | 0.00 | 47.9 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | -1 | 12.2 | 6.65 | 19.49 | 34.68 | 10.00 | 111.2 | 71.0 |
| Bench 3 | Bench | Ivan Toney | FWD | -1 | 7.7 | 2.24 | 9.52 | 16.50 | 0.00 | 44.2 | 0.0 |
| Bench 2 | Bench | Aleksandar Mitrović | FWD | -1 | 6.9 | 2.55 | 7.31 | 14.64 | 0.00 | 39.3 | 0.0 |
| Captain | Captain | Martin Ødegaard | MID | -1 | 7.0 | 7.06 | 17.79 | 28.21 | 11.00 | 130.3 | 173.0 |
| XI | Bench | Marcus Rashford | MID | -1 | 7.3 | 5.36 | 17.34 | 30.39 | 0.00 | 80.5 | 0.0 |
| XI | XI | Mohamed Salah | MID | -1 | 12.6 | 6.27 | 15.72 | 24.31 | 11.00 | 104.0 | 180.0 |
| XI | XI | Gabriel Martinelli Silva | MID | -1 | 6.5 | 5.17 | 13.75 | 20.60 | 26.00 | 89.5 | 180.0 |
| Bench 4 | Bench | Miguel Almirón Rejala | MID | -1 | 5.6 | 1.94 | 8.64 | 15.52 | 0.00 | 35.1 | 0.0 |

## GW26

- Train rows: 94122
- Bank: 0.80 -> 1.90
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Gabriel Martinelli Silva
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 69.33
- Actual score: 47.00
- Transfer: Ivan Perišić -> James Tarkowski (projected gain 6.10, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Aaron Ramsdale | GK | -1 | 4.9 | 5.40 | 14.27 | 21.87 | 1.00 | 132.5 | 90.0 |
| Bench 1 | Bench | Danny Ward | GK | -1 | 4.0 | 3.58 | 10.14 | 16.27 | 11.00 | 82.7 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 5.3 | 5.86 | 15.46 | 23.60 | 1.00 | 132.3 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | -1 | 5.2 | 5.43 | 14.78 | 22.74 | 1.00 | 131.8 | 90.0 |
| XI | XI | Kieran Trippier | DEF | -1 | 6.1 | 4.74 | 14.41 | 23.85 | 1.00 | 69.5 | 90.0 |
| XI | XI | James Tarkowski | DEF | -1 | 4.4 | 4.39 | 14.35 | 22.78 | 0.00 | 108.8 | 90.0 |
| Bench 2 | Bench | Luke Shaw | DEF | -1 | 5.4 | 2.68 | 8.38 | 14.22 | -1.00 | 50.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | -1 | 12.2 | 7.39 | 21.54 | 35.56 | 4.00 | 107.2 | 90.0 |
| XI | XI | Ivan Toney | FWD | -1 | 7.7 | 3.03 | 8.68 | 14.16 | 8.00 | 41.6 | 90.0 |
| Bench 4 | Bench | Aleksandar Mitrović | FWD | -1 | 6.8 | 1.72 | 5.95 | 11.05 | 1.00 | 24.3 | 90.0 |
| XI | XI | Mohamed Salah | MID | -1 | 12.7 | 6.69 | 21.07 | 32.77 | 21.00 | 111.4 | 90.0 |
| XI | XI | Martin Ødegaard | MID | -1 | 7.0 | 7.06 | 19.54 | 31.15 | 2.00 | 131.1 | 90.0 |
| Vice Captain | XI | Gabriel Martinelli Silva | MID | -1 | 6.5 | 7.10 | 19.50 | 29.75 | 2.00 | 125.4 | 90.0 |
| XI | XI | Marcus Rashford | MID | -1 | 7.3 | 4.84 | 15.12 | 25.86 | 2.00 | 68.7 | 84.0 |
| Bench 3 | Bench | Miguel Almirón Rejala | MID | -1 | 5.6 | 1.99 | 7.24 | 12.53 | 2.00 | 43.7 | 76.0 |

## GW27

- Train rows: 94869
- Bank: 1.90 -> 1.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 63.68
- Actual score: 79.00
- Transfer: Aaron Ramsdale -> Alisson Ramses Becker (projected gain 2.65, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alisson Ramses Becker | GK | -1 | 5.4 | 4.44 | 12.38 | 19.94 | 2.00 | 98.2 | 90.0 |
| Bench 1 | Bench | Danny Ward | GK | -1 | 4.0 | 3.57 | 10.65 | 17.75 | 2.00 | 87.4 | 90.0 |
| XI | XI | Kieran Trippier | DEF | -1 | 6.0 | 5.55 | 15.89 | 26.54 | 5.00 | 86.3 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 5.3 | 4.36 | 11.38 | 17.72 | 7.00 | 90.3 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | -1 | 5.2 | 3.82 | 10.36 | 16.54 | 14.00 | 84.9 | 90.0 |
| XI | XI | James Tarkowski | DEF | -1 | 4.4 | 3.30 | 10.35 | 17.83 | 8.00 | 88.0 | 90.0 |
| Bench 2 | Bench | Luke Shaw | DEF | -1 | 5.3 | 3.29 | 9.86 | 17.35 | 5.00 | 65.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | -1 | 12.2 | 7.31 | 21.24 | 34.21 | 6.00 | 101.1 | 90.0 |
| XI | XI | Ivan Toney | FWD | -1 | 7.7 | 4.22 | 10.00 | 18.44 | 13.00 | 78.3 | 180.0 |
| Bench 4 | Bench | Aleksandar Mitrović | FWD | -1 | 6.8 | 2.10 | 7.09 | 13.75 | 2.00 | 54.5 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | -1 | 12.7 | 6.58 | 19.32 | 33.01 | 0.00 | 104.1 | 90.0 |
| XI | XI | Marcus Rashford | MID | -1 | 7.3 | 5.76 | 17.36 | 29.96 | 3.00 | 84.1 | 90.0 |
| XI | XI | Gabriel Martinelli Silva | MID | -1 | 6.5 | 5.36 | 15.86 | 25.20 | 8.00 | 82.7 | 76.0 |
| XI | XI | Martin Ødegaard | MID | -1 | 7.0 | 5.68 | 15.67 | 25.69 | 7.00 | 91.7 | 90.0 |
| Bench 3 | Bench | Miguel Almirón Rejala | MID | -1 | 5.5 | 2.81 | 8.11 | 14.39 | 9.00 | 54.2 | 22.0 |

## GW28

- Train rows: 95619
- Bank: 1.40 -> 1.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Martin Ødegaard
- Effective captain: Martin Ødegaard
- Chip used: none
- Predicted score: 59.28
- Actual score: 17.00
- Transfer: Miguel Almirón Rejala -> Kaoru Mitoma (projected gain 4.46, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Alisson Ramses Becker | GK | -1 | 5.4 | 2.84 | 10.18 | 16.94 | 0.00 | 63.0 | 0.0 |
| XI | Bench | Danny Ward | GK | -1 | 4.0 | 3.20 | 8.96 | 14.68 | 0.00 | 78.4 | 0.0 |
| XI | XI | Kieran Trippier | DEF | -1 | 6.0 | 5.79 | 16.51 | 26.71 | 2.00 | 92.7 | 90.0 |
| XI | Bench | William Saliba | DEF | -1 | 5.3 | 4.68 | 11.91 | 18.60 | 0.00 | 96.1 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | -1 | 5.2 | 4.48 | 11.61 | 18.68 | 2.00 | 97.0 | 85.0 |
| Bench 2 | Bench | James Tarkowski | DEF | -1 | 4.3 | 3.30 | 10.48 | 17.81 | 4.00 | 97.0 | 90.0 |
| Bench 3 | Bench | Luke Shaw | DEF | -1 | 5.2 | 1.98 | 8.77 | 15.98 | 0.00 | 42.1 | 0.0 |
| Captain | Bench | Erling Haaland | FWD | -1 | 12.2 | 5.89 | 19.55 | 33.13 | 0.00 | 72.3 | 0.0 |
| XI | XI | Ivan Toney | FWD | -1 | 7.8 | 5.22 | 15.49 | 25.63 | 2.00 | 96.3 | 90.0 |
| Bench 4 | Bench | Aleksandar Mitrović | FWD | -1 | 6.7 | 1.28 | 7.12 | 14.01 | 0.00 | 32.9 | 0.0 |
| Vice Captain | Captain | Martin Ødegaard | MID | -1 | 6.9 | 5.89 | 16.40 | 27.45 | 2.00 | 97.8 | 90.0 |
| XI | Bench | Mohamed Salah | MID | -1 | 12.8 | 4.31 | 16.12 | 28.07 | 0.00 | 60.9 | 0.0 |
| XI | XI | Gabriel Martinelli Silva | MID | -1 | 6.5 | 5.53 | 15.47 | 25.50 | 7.00 | 87.0 | 82.0 |
| XI | Bench | Marcus Rashford | MID | -1 | 7.4 | 4.29 | 15.20 | 26.86 | 0.00 | 61.2 | 0.0 |
| XI | Bench | Kaoru Mitoma | MID | -1 | 5.5 | 4.12 | 14.85 | 24.31 | 0.00 | 69.5 | 0.0 |

## GW29

- Train rows: 96370
- Bank: 1.30 -> 1.90
- Free transfers: 2 -> 2
- Captain: Kieran Trippier
- Vice captain: Ivan Toney
- Effective captain: Kieran Trippier
- Chip used: bench_boost
- Predicted score: 73.18
- Actual score: 96.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (18.67) beats the best remaining Bench Boost opportunity (19.36).
- Chip advisory: triple_captain (0.63): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Alisson Ramses Becker -> David Raya Martin (projected gain 3.89, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (18.67) beats the best remaining Bench Boost opportunity (19.36).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 4.8 | 4.75 | 11.33 | 17.18 | 8.00 | 118.2 | 180.0 |
| Bench 1 | Bench Boost | Danny Ward | GK | -1 | 4.0 | 3.56 | 7.86 | 12.10 | 0.00 | 72.7 | 0.0 |
| Captain | Captain | Kieran Trippier | DEF | -1 | 6.1 | 7.12 | 18.04 | 27.46 | 14.00 | 124.5 | 176.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | -1 | 5.2 | 3.30 | 10.00 | 16.47 | 2.00 | 78.3 | 90.0 |
| Bench 2 | Bench Boost | James Tarkowski | DEF | -1 | 4.3 | 3.15 | 9.24 | 15.43 | 2.00 | 83.2 | 90.0 |
| XI | XI | Luke Shaw | DEF | -1 | 5.2 | 3.46 | 8.46 | 13.62 | 1.00 | 74.5 | 126.0 |
| Bench 3 | Bench Boost | William Saliba | DEF | -1 | 5.3 | 2.21 | 7.20 | 12.80 | 0.00 | 46.9 | 0.0 |
| XI | XI | Erling Haaland | FWD | -1 | 12.2 | 5.47 | 16.74 | 28.40 | 0.00 | 65.9 | 0.0 |
| Vice Captain | XI | Ivan Toney | FWD | -1 | 7.8 | 5.88 | 15.92 | 24.68 | 11.00 | 114.4 | 180.0 |
| Bench 4 | Bench Boost | Aleksandar Mitrović | FWD | -1 | 6.7 | 2.15 | 6.89 | 12.17 | 0.00 | 41.9 | 0.0 |
| XI | XI | Martin Ødegaard | MID | -1 | 6.9 | 4.84 | 15.06 | 25.28 | 6.00 | 88.7 | 84.0 |
| XI | XI | Marcus Rashford | MID | -1 | 7.4 | 5.53 | 14.89 | 24.36 | 12.00 | 92.3 | 180.0 |
| XI | XI | Gabriel Martinelli Silva | MID | -1 | 6.6 | 5.05 | 14.48 | 23.80 | 5.00 | 78.9 | 90.0 |
| XI | XI | Mohamed Salah | MID | -1 | 12.8 | 4.60 | 13.59 | 23.52 | 7.00 | 78.0 | 94.0 |
| XI | XI | Kaoru Mitoma | MID | -1 | 5.5 | 4.99 | 12.49 | 19.56 | 14.00 | 91.0 | 180.0 |

## GW30

- Train rows: 97124
- Bank: 1.90 -> 3.00
- Free transfers: 2 -> 2
- Captain: Dominic Solanke
- Vice captain: Ivan Toney
- Effective captain: Dominic Solanke
- Chip used: none
- Predicted score: 154.67
- Actual score: 40.00
- Transfer: Aleksandar Mitrović -> Dominic Solanke (projected gain 89.15, hit 0)
- Autosub outfielders: James Tarkowski.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 4.9 | 5.07 | 14.03 | 22.11 | 0.00 | 134.5 | 90.0 |
| Bench 1 | Bench | Danny Ward | GK | -1 | 4.0 | 1.56 | 5.01 | 8.85 | 0.00 | 33.4 | 0.0 |
| XI | XI | Kieran Trippier | DEF | -1 | 6.1 | 14.31 | 43.05 | 57.61 | 2.00 | 180.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | -1 | 5.2 | 6.75 | 22.21 | 30.39 | 1.00 | 115.0 | 90.0 |
| XI | Bench | Luke Shaw | DEF | -1 | 5.2 | 5.81 | 16.92 | 24.71 | 0.00 | 94.7 | 0.0 |
| Bench 2 | Autosub In | James Tarkowski | DEF | -1 | 4.2 | 4.40 | 14.51 | 21.47 | 1.00 | 101.4 | 90.0 |
| Bench 4 | Bench | William Saliba | DEF | -1 | 5.2 | 1.02 | 5.34 | 10.87 | 0.00 | 30.5 | 0.0 |
| Captain | Captain | Dominic Solanke | FWD | -1 | 5.5 | 27.95 | 91.01 | 110.36 | 2.00 | 180.0 | 87.0 |
| Vice Captain | XI | Ivan Toney | FWD | -1 | 7.9 | 15.45 | 48.56 | 64.45 | 4.00 | 180.0 | 90.0 |
| Bench 3 | Bench | Erling Haaland | FWD | -1 | 12.0 | 4.37 | 14.19 | 25.77 | 12.00 | 42.6 | 68.0 |
| XI | XI | Kaoru Mitoma | MID | -1 | 5.6 | 13.92 | 44.34 | 59.07 | 2.00 | 180.0 | 90.0 |
| XI | XI | Gabriel Martinelli Silva | MID | -1 | 6.6 | 12.73 | 40.89 | 53.92 | 13.00 | 153.9 | 90.0 |
| XI | XI | Marcus Rashford | MID | -1 | 7.3 | 10.76 | 31.92 | 45.96 | 6.00 | 153.9 | 80.0 |
| XI | XI | Mohamed Salah | MID | -1 | 12.8 | 7.00 | 24.12 | 36.61 | 5.00 | 100.7 | 90.0 |
| XI | XI | Martin Ødegaard | MID | -1 | 6.8 | 6.98 | 23.18 | 34.81 | 2.00 | 111.9 | 79.0 |

## GW31

- Train rows: 97878
- Bank: 3.00 -> 3.30
- Free transfers: 2 -> 2
- Captain: Kieran Trippier
- Vice captain: Marcus Rashford
- Effective captain: Kieran Trippier
- Chip used: none
- Predicted score: 54.59
- Actual score: 74.00
- Transfer: William Saliba -> Benjamin White (projected gain 2.12, hit 0)
- Autosub outfielders: Dominic Solanke.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 4.9 | 2.97 | 9.61 | 16.14 | 5.00 | 93.3 | 90.0 |
| Bench 1 | Bench | Danny Ward | GK | -1 | 4.0 | 0.84 | 4.01 | 7.12 | 0.00 | 23.8 | 0.0 |
| Captain | Captain | Kieran Trippier | DEF | -1 | 6.1 | 5.79 | 16.29 | 27.98 | 1.00 | 96.2 | 90.0 |
| XI | XI | Benjamin White | DEF | -1 | 4.8 | 3.35 | 10.55 | 19.33 | 6.00 | 72.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | -1 | 5.2 | 3.25 | 10.31 | 18.27 | 1.00 | 80.7 | 90.0 |
| Bench 3 | Bench | James Tarkowski | DEF | -1 | 4.2 | 2.86 | 8.52 | 14.72 | 1.00 | 81.6 | 90.0 |
| Bench 4 | Bench | Luke Shaw | DEF | -1 | 5.2 | 1.79 | 5.91 | 11.25 | 0.00 | 26.4 | 0.0 |
| XI | XI | Erling Haaland | FWD | -1 | 12.1 | 5.45 | 17.47 | 29.55 | 12.00 | 66.2 | 45.0 |
| XI | XI | Ivan Toney | FWD | -1 | 7.9 | 4.35 | 14.37 | 26.85 | 2.00 | 76.1 | 90.0 |
| Bench 2 | Autosub In | Dominic Solanke | FWD | -1 | 5.5 | 2.94 | 8.94 | 19.60 | 15.00 | 46.2 | 90.0 |
| XI | XI | Mohamed Salah | MID | -1 | 12.8 | 5.23 | 16.70 | 29.03 | 14.00 | 76.5 | 80.0 |
| Vice Captain | Bench | Marcus Rashford | MID | -1 | 7.3 | 5.70 | 16.36 | 27.31 | 0.00 | 80.6 | 0.0 |
| XI | XI | Gabriel Martinelli Silva | MID | -1 | 6.6 | 5.11 | 14.95 | 26.83 | 5.00 | 81.9 | 84.0 |
| XI | XI | Martin Ødegaard | MID | -1 | 6.7 | 4.04 | 12.98 | 22.91 | 10.00 | 81.3 | 89.0 |
| XI | XI | Kaoru Mitoma | MID | -1 | 5.6 | 3.56 | 12.25 | 22.65 | 2.00 | 68.2 | 90.0 |

## GW32

- Train rows: 98637
- Bank: 3.30 -> 1.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Kieran Trippier
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 58.78
- Actual score: 61.00
- Transfer: Luke Shaw -> Trent Alexander-Arnold (projected gain 1.96, hit 0)
- Autosub outfielders: Gabriel dos Santos Magalhães, James Tarkowski.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 4.9 | 2.86 | 9.12 | 15.66 | 2.00 | 96.0 | 90.0 |
| Bench 1 | Bench | Danny Ward | GK | -1 | 3.9 | 1.50 | 4.16 | 7.28 | 0.00 | 20.9 | 0.0 |
| Vice Captain | XI | Kieran Trippier | DEF | -1 | 6.2 | 5.81 | 16.30 | 27.96 | 2.00 | 103.3 | 69.0 |
| XI | XI | Trent Alexander-Arnold | DEF | -1 | 7.3 | 4.21 | 12.08 | 20.87 | 5.00 | 90.4 | 90.0 |
| XI | XI | Benjamin White | DEF | -1 | 4.9 | 3.67 | 10.64 | 19.60 | 4.00 | 81.7 | 90.0 |
| Bench 2 | Autosub In | Gabriel dos Santos Magalhães | DEF | -1 | 5.3 | 3.48 | 10.32 | 18.05 | 1.00 | 84.3 | 90.0 |
| Bench 3 | Autosub In | James Tarkowski | DEF | -1 | 4.2 | 3.00 | 9.03 | 15.20 | 6.00 | 81.2 | 90.0 |
| XI | Bench | Erling Haaland | FWD | -1 | 12.2 | 5.27 | 18.88 | 31.42 | 0.00 | 44.4 | 0.0 |
| XI | XI | Ivan Toney | FWD | -1 | 7.8 | 5.03 | 14.73 | 25.93 | 9.00 | 83.9 | 90.0 |
| XI | XI | Dominic Solanke | FWD | -1 | 5.5 | 5.42 | 12.88 | 24.15 | 2.00 | 73.2 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 12.8 | 6.52 | 18.24 | 30.62 | 7.00 | 90.2 | 90.0 |
| XI | XI | Gabriel Martinelli Silva | MID | -1 | 6.8 | 5.25 | 15.62 | 28.04 | 9.00 | 77.9 | 84.0 |
| XI | XI | Martin Ødegaard | MID | -1 | 6.7 | 4.56 | 13.37 | 23.38 | 7.00 | 87.5 | 90.0 |
| XI | Bench | Kaoru Mitoma | MID | -1 | 5.7 | 3.66 | 13.15 | 23.44 | 0.00 | 51.3 | 0.0 |
| Bench 4 | Bench | Marcus Rashford | MID | -1 | 7.2 | 1.69 | 10.11 | 21.88 | 0.00 | 0.9 | 0.0 |

## GW33

- Train rows: 99397
- Bank: 1.10 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.58
- Actual score: 53.00
- Transfer: Kaoru Mitoma -> Eberechi Eze (projected gain 1.41, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 4.9 | 2.77 | 8.94 | 14.60 | 9.00 | 83.1 | 90.0 |
| Bench 1 | Bench | Danny Ward | GK | -1 | 3.9 | 1.41 | 4.18 | 7.45 | 0.00 | 20.5 | 0.0 |
| XI | XI | Kieran Trippier | DEF | -1 | 6.2 | 4.91 | 14.65 | 19.00 | 2.00 | 107.2 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | -1 | 7.4 | 4.30 | 13.24 | 20.27 | 5.00 | 90.7 | 90.0 |
| Bench 3 | Bench | Benjamin White | DEF | -1 | 5.0 | 2.65 | 9.43 | 10.82 | 0.00 | 99.3 | 90.0 |
| XI | XI | James Tarkowski | DEF | -1 | 4.2 | 3.17 | 9.37 | 13.95 | 0.00 | 89.4 | 90.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | -1 | 5.3 | 2.62 | 9.27 | 13.14 | 0.00 | 95.7 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | -1 | 12.2 | 6.11 | 18.43 | 29.53 | 14.00 | 68.9 | 90.0 |
| XI | XI | Ivan Toney | FWD | -1 | 7.7 | 5.10 | 14.66 | 15.65 | 2.00 | 104.2 | 82.0 |
| Bench 2 | Bench | Dominic Solanke | FWD | -1 | 5.6 | 3.07 | 7.42 | 0.00 | 5.00 | 110.0 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 12.9 | 6.76 | 20.27 | 29.63 | 2.00 | 96.2 | 90.0 |
| XI | XI | Gabriel Martinelli Silva | MID | -1 | 6.9 | 4.96 | 15.73 | 20.39 | 1.00 | 112.8 | 59.0 |
| XI | XI | Martin Ødegaard | MID | -1 | 6.7 | 4.03 | 13.25 | 20.33 | 2.00 | 99.3 | 70.0 |
| XI | XI | Eberechi Eze | MID | -1 | 5.6 | 3.61 | 10.58 | 14.35 | 2.00 | 76.3 | 90.0 |
| XI | XI | Marcus Rashford | MID | -1 | 7.2 | 3.08 | 9.83 | 12.93 | 12.00 | 47.7 | 90.0 |

## GW34

- Train rows: 100158
- Bank: 1.20 -> 1.60
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 73.09
- Actual score: 93.00
- Chip advisory: triple_captain (0.66): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Eberechi Eze -> Solly March (projected gain 3.99, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 4.9 | 3.73 | 10.76 | 17.24 | 2.00 | 91.4 | 90.0 |
| Bench 1 | Bench | Danny Ward | GK | -1 | 3.9 | 1.37 | 3.82 | 6.62 | 0.00 | 17.1 | 0.0 |
| XI | XI | Kieran Trippier | DEF | -1 | 6.2 | 6.44 | 19.01 | 30.40 | 2.00 | 112.4 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | -1 | 7.5 | 5.84 | 14.78 | 23.41 | 11.00 | 116.6 | 180.0 |
| XI | XI | Benjamin White | DEF | -1 | 5.0 | 3.87 | 12.16 | 19.83 | 2.00 | 89.2 | 90.0 |
| Bench 3 | Bench | Gabriel dos Santos Magalhães | DEF | -1 | 5.3 | 3.53 | 10.68 | 17.12 | 2.00 | 85.2 | 84.0 |
| Bench 4 | Bench | James Tarkowski | DEF | -1 | 4.2 | 2.89 | 8.84 | 14.17 | 1.00 | 80.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | -1 | 12.3 | 8.90 | 23.31 | 36.42 | 16.00 | 116.1 | 180.0 |
| XI | XI | Dominic Solanke | FWD | -1 | 5.6 | 5.18 | 16.06 | 25.68 | 8.00 | 103.5 | 88.0 |
| XI | XI | Ivan Toney | FWD | -1 | 7.6 | 5.05 | 15.45 | 26.03 | 7.00 | 82.1 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | -1 | 13.0 | 7.09 | 18.79 | 30.39 | 18.00 | 107.3 | 173.0 |
| XI | XI | Gabriel Martinelli Silva | MID | -1 | 6.9 | 5.86 | 17.63 | 28.72 | 1.00 | 93.1 | 31.0 |
| XI | XI | Solly March | MID | -1 | 5.2 | 6.33 | 17.19 | 25.79 | 2.00 | 123.1 | 82.0 |
| XI | XI | Marcus Rashford | MID | -1 | 7.1 | 5.89 | 15.62 | 24.77 | 8.00 | 94.8 | 175.0 |
| Bench 2 | Bench | Martin Ødegaard | MID | -1 | 6.7 | 4.18 | 13.28 | 22.05 | 15.00 | 83.8 | 90.0 |

## GW35

- Train rows: 100920
- Bank: 1.60 -> 0.90
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 66.93
- Actual score: 47.00
- Transfer: James Tarkowski -> Pervis Estupiñán (projected gain 3.45, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 4.9 | 2.84 | 9.17 | 15.58 | 3.00 | 87.7 | 90.0 |
| Bench 1 | Bench | Danny Ward | GK | -1 | 3.9 | 0.93 | 2.68 | 4.74 | 0.00 | 10.9 | 0.0 |
| XI | XI | Kieran Trippier | DEF | -1 | 6.2 | 5.66 | 16.92 | 28.11 | 1.00 | 102.5 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | -1 | 7.6 | 5.74 | 16.55 | 26.73 | 7.00 | 119.6 | 90.0 |
| XI | XI | Pervis Estupiñán | DEF | -1 | 4.8 | 5.03 | 13.25 | 21.06 | 0.00 | 106.1 | 90.0 |
| Bench 3 | Bench | Benjamin White | DEF | -1 | 5.0 | 3.27 | 9.83 | 16.17 | 6.00 | 80.3 | 90.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | -1 | 5.3 | 3.04 | 9.25 | 14.99 | 7.00 | 75.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | -1 | 12.4 | 8.89 | 24.65 | 39.06 | 2.00 | 120.2 | 90.0 |
| XI | XI | Ivan Toney | FWD | -1 | 7.5 | 3.85 | 11.96 | 21.72 | 2.00 | 77.3 | 90.0 |
| XI | XI | Dominic Solanke | FWD | -1 | 5.6 | 3.78 | 10.97 | 18.27 | 2.00 | 78.9 | 89.0 |
| Vice Captain | XI | Mohamed Salah | MID | -1 | 13.0 | 7.41 | 21.20 | 34.55 | 10.00 | 112.1 | 90.0 |
| XI | XI | Marcus Rashford | MID | -1 | 7.2 | 6.15 | 18.45 | 29.36 | 2.00 | 99.8 | 90.0 |
| XI | XI | Martin Ødegaard | MID | -1 | 6.6 | 4.58 | 13.83 | 23.15 | 10.00 | 88.4 | 79.0 |
| XI | XI | Gabriel Martinelli Silva | MID | -1 | 6.8 | 4.09 | 13.21 | 22.89 | 6.00 | 62.1 | 79.0 |
| Bench 2 | Bench | Solly March | MID | -1 | 5.3 | 3.74 | 10.77 | 17.52 | 1.00 | 72.5 | 32.0 |

## GW36

- Train rows: 101683
- Bank: 0.90 -> 0.60
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Kieran Trippier
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 67.71
- Actual score: 85.00
- Transfer: Solly March -> Kaoru Mitoma (projected gain 5.33, hit 0)
- Autosub outfielders: Dominic Solanke, Benjamin White.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 4.9 | 3.26 | 9.46 | 15.48 | 7.00 | 84.5 | 90.0 |
| Bench 1 | Bench | Danny Ward | GK | -1 | 3.9 | 0.58 | 2.05 | 3.47 | 0.00 | 8.0 | 0.0 |
| Vice Captain | XI | Kieran Trippier | DEF | -1 | 6.1 | 6.85 | 18.43 | 28.93 | 11.00 | 131.3 | 180.0 |
| XI | XI | Trent Alexander-Arnold | DEF | -1 | 7.6 | 4.92 | 14.54 | 23.53 | 13.00 | 96.9 | 90.0 |
| XI | XI | Pervis Estupiñán | DEF | -1 | 4.9 | 4.81 | 11.94 | 18.45 | 17.00 | 108.0 | 180.0 |
| Bench 3 | Autosub In | Benjamin White | DEF | -1 | 5.0 | 3.53 | 10.08 | 16.06 | 1.00 | 82.4 | 90.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | -1 | 5.2 | 2.99 | 8.79 | 14.09 | 1.00 | 76.6 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | -1 | 12.4 | 8.03 | 23.40 | 36.30 | 7.00 | 104.0 | 77.0 |
| XI | Bench | Ivan Toney | FWD | -1 | 7.4 | 3.97 | 11.33 | 18.79 | 0.00 | 74.3 | 0.0 |
| Bench 2 | Autosub In | Dominic Solanke | FWD | -1 | 5.6 | 3.62 | 10.68 | 17.35 | 2.00 | 77.2 | 90.0 |
| XI | XI | Mohamed Salah | MID | -1 | 13.0 | 6.44 | 19.33 | 30.66 | 12.00 | 94.6 | 87.0 |
| XI | Bench | Marcus Rashford | MID | -1 | 7.2 | 6.07 | 16.99 | 26.60 | 0.00 | 94.1 | 0.0 |
| XI | XI | Kaoru Mitoma | MID | -1 | 5.6 | 5.98 | 15.18 | 23.08 | 5.00 | 118.5 | 180.0 |
| XI | XI | Martin Ødegaard | MID | -1 | 6.6 | 4.64 | 13.91 | 22.71 | 2.00 | 82.3 | 76.0 |
| XI | XI | Gabriel Martinelli Silva | MID | -1 | 6.7 | 4.71 | 13.76 | 22.11 | 1.00 | 74.2 | 19.0 |

## GW37

- Train rows: 102448
- Bank: 0.60 -> 0.80
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 86.64
- Actual score: 61.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (13.36) beats the best remaining Triple Captain opportunity (9.68).
- Chip advisory: triple_captain (0.66): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Ivan Toney -> Callum Wilson (projected gain 8.97, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (13.36) beats the best remaining Triple Captain opportunity (9.68).
- Autosub outfielders: Benjamin White.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 4.8 | 3.26 | 9.97 | 15.97 | 4.00 | 87.3 | 90.0 |
| Bench 1 | Bench | Danny Ward | GK | -1 | 3.8 | 0.44 | 1.91 | 3.24 | 0.00 | 7.4 | 0.0 |
| XI | XI | Kieran Trippier | DEF | -1 | 6.1 | 7.23 | 20.91 | 32.66 | 9.00 | 142.4 | 90.0 |
| XI | XI | Pervis Estupiñán | DEF | -1 | 4.9 | 6.92 | 18.00 | 26.89 | 4.00 | 162.2 | 180.0 |
| XI | XI | Trent Alexander-Arnold | DEF | -1 | 7.7 | 5.68 | 15.94 | 25.03 | 1.00 | 104.9 | 90.0 |
| Bench 2 | Autosub In | Benjamin White | DEF | -1 | 5.0 | 3.43 | 9.65 | 15.10 | 2.00 | 79.3 | 90.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | -1 | 5.2 | 3.07 | 8.51 | 13.02 | 1.00 | 74.6 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | -1 | 12.4 | 9.46 | 24.46 | 36.07 | 6.00 | 132.5 | 106.0 |
| XI | XI | Callum Wilson | FWD | -1 | 7.1 | 6.64 | 18.57 | 26.82 | 2.00 | 106.6 | 67.0 |
| Bench 3 | Bench | Dominic Solanke | FWD | -1 | 5.7 | 3.33 | 9.67 | 15.61 | 2.00 | 77.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | -1 | 13.1 | 7.62 | 21.19 | 32.30 | 5.00 | 106.3 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | -1 | 5.6 | 7.03 | 18.33 | 27.20 | 7.00 | 151.7 | 178.0 |
| XI | XI | Martin Ødegaard | MID | -1 | 6.7 | 4.73 | 13.95 | 22.19 | 2.00 | 77.6 | 90.0 |
| XI | XI | Marcus Rashford | MID | -1 | 7.3 | 5.22 | 13.32 | 21.51 | 7.00 | 79.3 | 61.0 |
| XI | Bench | Gabriel Martinelli Silva | MID | -1 | 6.7 | 3.91 | 11.19 | 17.43 | 0.00 | 50.8 | 0.0 |

## GW38

- Train rows: 103223
- Bank: 0.80 -> 2.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Kaoru Mitoma
- Effective captain: Kaoru Mitoma
- Chip used: none
- Predicted score: 65.09
- Actual score: 35.00
- Transfer: Gabriel Martinelli Silva -> Pascal Groß (projected gain 6.27, hit 0)
- Autosub outfielders: Benjamin White.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 4.8 | 2.92 | 9.47 | 15.40 | 6.00 | 88.1 | 90.0 |
| Bench 1 | Bench | Danny Ward | GK | -1 | 3.8 | 1.00 | 2.62 | 4.22 | 0.00 | 8.5 | 0.0 |
| XI | XI | Kieran Trippier | DEF | -1 | 6.1 | 5.57 | 16.68 | 27.19 | 0.00 | 107.4 | 90.0 |
| XI | XI | Pervis Estupiñán | DEF | -1 | 5.0 | 5.32 | 15.86 | 24.13 | 1.00 | 125.9 | 45.0 |
| XI | XI | Trent Alexander-Arnold | DEF | -1 | 7.7 | 4.80 | 14.58 | 23.21 | 4.00 | 90.0 | 90.0 |
| Bench 2 | Autosub In | Benjamin White | DEF | -1 | 5.0 | 3.42 | 9.48 | 14.85 | 6.00 | 80.7 | 90.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | -1 | 5.2 | 3.02 | 8.36 | 13.08 | 6.00 | 75.2 | 90.0 |
| Captain | Bench | Erling Haaland | FWD | -1 | 12.4 | 7.65 | 23.09 | 35.44 | 0.00 | 105.8 | 0.0 |
| XI | XI | Callum Wilson | FWD | -1 | 7.2 | 3.57 | 11.49 | 17.58 | 1.00 | 59.7 | 21.0 |
| Bench 3 | Bench | Dominic Solanke | FWD | -1 | 5.7 | 3.15 | 9.08 | 14.30 | 1.00 | 73.4 | 90.0 |
| XI | XI | Mohamed Salah | MID | -1 | 13.1 | 6.24 | 18.69 | 29.41 | 5.00 | 86.7 | 90.0 |
| Vice Captain | Captain | Kaoru Mitoma | MID | -1 | 5.7 | 6.76 | 18.05 | 25.66 | 1.00 | 126.0 | 25.0 |
| XI | XI | Pascal Groß | MID | -1 | 5.4 | 5.59 | 15.70 | 23.29 | 5.00 | 127.1 | 90.0 |
| XI | XI | Martin Ødegaard | MID | -1 | 6.8 | 4.82 | 13.66 | 21.34 | 3.00 | 79.2 | 74.0 |
| XI | XI | Marcus Rashford | MID | -1 | 7.2 | 4.19 | 12.80 | 21.04 | 2.00 | 52.2 | 76.0 |