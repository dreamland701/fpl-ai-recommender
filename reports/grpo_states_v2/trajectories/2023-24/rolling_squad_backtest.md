# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW1
- Simulated weeks: GW2-GW38
- Total predicted points: 2178.63
- Total actual points: 2238.00
- Average predicted points: 58.88
- Average actual points: 60.49
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
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Bukayo Saka
- Vice captain: Mohamed Salah
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 65.44
- Actual score: 54.00
- Chip advisory: bench_boost (0.67): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 5.0 | 5.17 | 14.33 | 23.21 | 2.00 | 106.2 | 90.0 |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.5 | 3.89 | 11.13 | 18.63 | 2.00 | 103.0 | 90.0 |
| Bench 2 | Bench | Kieran Trippier | DEF | 15 | 6.5 | 4.36 | 13.72 | 23.10 | 2.00 | 95.3 | 90.0 |
| XI | XI | Pervis Estupiñán | DEF | 5 | 5.1 | 4.62 | 13.70 | 22.94 | 11.00 | 83.4 | 90.0 |
| XI | XI | Ben Chilwell | DEF | 7 | 5.6 | 5.15 | 13.24 | 20.30 | 1.00 | 108.3 | 60.0 |
| XI | XI | William Saliba | DEF | 1 | 5.1 | 4.77 | 12.76 | 20.05 | 8.00 | 112.4 | 90.0 |
| Bench 3 | Bench | Luke Shaw | DEF | 14 | 5.5 | 4.20 | 12.57 | 20.74 | 1.00 | 100.4 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.0 | 5.06 | 14.71 | 24.72 | 5.00 | 103.5 | 73.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 4.47 | 12.23 | 19.74 | 0.00 | 81.5 | 33.0 |
| Bench 4 | Bench | Julián Álvarez | FWD | 13 | 6.5 | 3.97 | 11.36 | 18.63 | 7.00 | 73.2 | 90.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 8.6 | 7.38 | 19.91 | 31.66 | 3.00 | 126.2 | 88.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.5 | 6.76 | 19.39 | 31.98 | 5.00 | 108.8 | 85.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.43 | 15.60 | 27.51 | 1.00 | 98.6 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 5.37 | 15.39 | 25.40 | 12.00 | 94.0 | 80.0 |
| XI | XI | Moussa Diaby | MID | 2 | 6.5 | 4.87 | 13.50 | 22.21 | 3.00 | 100.9 | 63.0 |

## GW3

- Train rows: 105327
- Bank: 0.10 -> 0.50
- Free transfers: 2 -> 2
- Captain: Pervis Estupiñán
- Vice captain: Kaoru Mitoma
- Effective captain: Pervis Estupiñán
- Chip used: none
- Predicted score: 59.10
- Actual score: 42.00
- Transfer: Luke Shaw -> Raphaël Varane (projected gain 0.10, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 5.0 | 3.80 | 11.36 | 18.71 | 0.00 | 86.8 | 90.0 |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.5 | 2.35 | 9.14 | 16.11 | 5.00 | 90.7 | 90.0 |
| Captain | Captain | Pervis Estupiñán | DEF | 5 | 5.1 | 6.56 | 17.93 | 28.42 | 1.00 | 107.3 | 90.0 |
| XI | XI | Ben Chilwell | DEF | 7 | 5.6 | 4.37 | 13.57 | 20.71 | 6.00 | 73.2 | 85.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.5 | 3.92 | 12.35 | 20.79 | 0.00 | 85.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.1 | 4.54 | 12.13 | 18.76 | 1.00 | 96.8 | 90.0 |
| Bench 2 | Bench | Raphaël Varane | DEF | 14 | 5.1 | 3.59 | 10.05 | 16.03 | 0.00 | 80.3 | 45.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.0 | 4.24 | 13.24 | 22.09 | 5.00 | 70.3 | 85.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.5 | 4.33 | 11.69 | 18.45 | 2.00 | 82.6 | 90.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 1.66 | 5.63 | 10.41 | 1.00 | 21.0 | 30.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.6 | 5.86 | 16.93 | 27.19 | 8.00 | 85.3 | 90.0 |
| Vice Captain | XI | Kaoru Mitoma | MID | 5 | 6.5 | 6.06 | 16.62 | 27.19 | 1.00 | 97.8 | 90.0 |
| XI | XI | Mohamed Salah | MID | 11 | 12.5 | 4.80 | 15.39 | 26.21 | 5.00 | 69.4 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.07 | 13.87 | 24.31 | 12.00 | 74.1 | 90.0 |
| Bench 3 | Bench | Moussa Diaby | MID | 2 | 6.5 | 3.23 | 10.66 | 17.63 | 12.00 | 53.7 | 72.0 |

## GW4

- Train rows: 106012
- Bank: 0.50 -> 1.00
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Mohamed Salah
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 53.16
- Actual score: 50.00
- Transfer: Moussa Diaby -> James Ward-Prowse (projected gain 3.98, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.5 | 2.51 | 9.33 | 16.50 | 0.00 | 94.3 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 5.0 | 2.39 | 8.81 | 15.00 | 0.00 | 75.7 | 90.0 |
| XI | XI | Pervis Estupiñán | DEF | 5 | 5.2 | 4.79 | 15.02 | 24.48 | 2.00 | 76.4 | 90.0 |
| XI | XI | Ben Chilwell | DEF | 7 | 5.7 | 4.47 | 12.37 | 19.05 | 1.00 | 68.0 | 61.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.5 | 4.04 | 12.32 | 20.43 | 1.00 | 85.1 | 90.0 |
| Bench 2 | Bench | William Saliba | DEF | 1 | 5.1 | 3.22 | 9.68 | 15.35 | 2.00 | 74.2 | 90.0 |
| Bench 3 | Bench | Raphaël Varane | DEF | 14 | 5.1 | 1.39 | 5.97 | 10.43 | 0.00 | 48.2 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.0 | 3.47 | 11.43 | 19.14 | 2.00 | 67.5 | 72.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.5 | 3.72 | 10.43 | 16.61 | 14.00 | 61.1 | 89.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 1.36 | 5.48 | 10.68 | 2.00 | 21.1 | 76.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 8.6 | 6.11 | 18.05 | 29.66 | 4.00 | 91.4 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.5 | 5.59 | 17.47 | 29.61 | 8.00 | 84.3 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.01 | 13.80 | 24.08 | 2.00 | 79.5 | 90.0 |
| XI | XI | James Ward-Prowse | MID | 19 | 6.0 | 4.62 | 13.63 | 21.91 | 7.00 | 89.3 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 3.73 | 12.98 | 22.17 | 5.00 | 58.3 | 90.0 |

## GW5

- Train rows: 106715
- Bank: 1.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Mohamed Salah
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 57.50
- Actual score: 61.00
- Transfer: James Ward-Prowse -> Bryan Mbeumo (projected gain 4.37, hit 0)
- Autosub: Ben Chilwell replaced Pervis Estupiñán.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.5 | 3.40 | 9.72 | 16.63 | 6.00 | 88.4 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 5.0 | 2.78 | 8.31 | 14.85 | 2.00 | 73.7 | 90.0 |
| XI | Bench | Pervis Estupiñán | DEF | 5 | 5.2 | 4.98 | 14.66 | 24.90 | 0.00 | 88.6 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.5 | 4.05 | 11.57 | 19.35 | 8.00 | 82.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.1 | 3.73 | 10.63 | 16.85 | 6.00 | 82.6 | 90.0 |
| Bench 2 | Autosub In | Ben Chilwell | DEF | 7 | 5.7 | 3.19 | 9.41 | 15.34 | 0.00 | 45.6 | 10.0 |
| Bench 4 | Bench | Raphaël Varane | DEF | 14 | 5.0 | 0.98 | 3.44 | 6.64 | 0.00 | 20.6 | 0.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.6 | 4.82 | 13.53 | 20.28 | 9.00 | 88.6 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.0 | 3.83 | 11.21 | 18.29 | 5.00 | 57.0 | 90.0 |
| Bench 3 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 1.09 | 5.03 | 10.53 | 7.00 | 28.4 | 26.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 8.6 | 6.51 | 18.49 | 30.23 | 6.00 | 91.6 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.5 | 6.40 | 18.24 | 30.31 | 10.00 | 86.1 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.69 | 13.85 | 23.71 | 1.00 | 77.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 4.31 | 13.53 | 22.11 | 2.00 | 77.5 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 4.28 | 13.39 | 23.86 | 2.00 | 75.8 | 90.0 |

## GW6

- Train rows: 107432
- Bank: 0.20 -> 0.60
- Free transfers: 2 -> 2
- Captain: Julián Álvarez
- Vice captain: Mohamed Salah
- Effective captain: Julián Álvarez
- Chip used: none
- Predicted score: 60.47
- Actual score: 86.00
- Transfer: Bernd Leno -> Alphonse Areola (projected gain 0.38, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.1 | 3.19 | 10.41 | 17.69 | 2.00 | 96.4 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 4.9 | 2.83 | 8.50 | 14.82 | 7.00 | 75.3 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.5 | 4.58 | 12.75 | 20.92 | 18.00 | 89.1 | 69.0 |
| XI | XI | Pervis Estupiñán | DEF | 5 | 5.2 | 3.97 | 11.25 | 19.38 | 6.00 | 52.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.1 | 3.65 | 10.59 | 16.73 | 1.00 | 84.7 | 90.0 |
| Bench 3 | Bench | Ben Chilwell | DEF | 7 | 5.6 | 1.85 | 6.38 | 11.88 | 0.00 | 23.4 | 29.0 |
| Bench 4 | Bench | Raphaël Varane | DEF | 14 | 5.0 | 0.97 | 3.10 | 5.87 | 1.00 | 17.0 | 11.0 |
| Captain | Captain | Julián Álvarez | FWD | 13 | 6.7 | 6.77 | 17.80 | 26.25 | 1.00 | 113.1 | 56.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 7.9 | 3.74 | 11.44 | 18.65 | 9.00 | 65.3 | 90.0 |
| Bench 2 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 2.19 | 6.51 | 12.14 | 1.00 | 32.6 | 27.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.5 | 6.64 | 19.72 | 32.43 | 10.00 | 100.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.6 | 6.48 | 18.89 | 29.69 | 13.00 | 104.2 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 4.96 | 14.32 | 23.60 | 1.00 | 86.1 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 5.04 | 14.08 | 24.01 | 14.00 | 81.8 | 45.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.68 | 14.07 | 26.24 | 10.00 | 81.8 | 90.0 |

## GW7

- Train rows: 108150
- Bank: 0.60 -> 0.20
- Free transfers: 2 -> 2
- Captain: Kieran Trippier
- Vice captain: Mohamed Salah
- Effective captain: Kieran Trippier
- Chip used: none
- Predicted score: 58.99
- Actual score: 87.00
- Transfer: Bryan Mbeumo -> Jarrod Bowen (projected gain 4.41, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.1 | 4.25 | 11.65 | 19.10 | 6.00 | 97.4 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 4.9 | 3.31 | 9.34 | 15.61 | 2.00 | 85.5 | 90.0 |
| Captain | Captain | Kieran Trippier | DEF | 15 | 6.6 | 6.24 | 16.42 | 25.96 | 12.00 | 107.8 | 90.0 |
| XI | XI | Pervis Estupiñán | DEF | 5 | 5.2 | 4.34 | 13.07 | 21.39 | -2.00 | 80.0 | 45.0 |
| XI | XI | William Saliba | DEF | 1 | 5.1 | 3.18 | 9.34 | 15.25 | 6.00 | 77.9 | 90.0 |
| Bench 3 | Bench | Raphaël Varane | DEF | 14 | 5.0 | 1.16 | 3.39 | 5.95 | 2.00 | 22.6 | 86.0 |
| Bench 4 | Bench | Ben Chilwell | DEF | 7 | 5.6 | 0.00 | 2.55 | 6.69 | 0.00 | 0.0 | 0.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.7 | 3.98 | 12.44 | 18.90 | 8.00 | 53.5 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 7.9 | 4.05 | 11.82 | 19.67 | 23.00 | 73.7 | 90.0 |
| Bench 2 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 1.99 | 6.71 | 11.39 | 4.00 | 36.5 | 45.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.5 | 5.92 | 19.32 | 31.20 | 1.00 | 88.6 | 73.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.6 | 5.32 | 16.40 | 27.50 | 9.00 | 73.8 | 75.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.2 | 5.75 | 15.39 | 24.71 | 9.00 | 102.5 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 5.19 | 15.03 | 24.44 | 1.00 | 80.6 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.53 | 13.70 | 23.23 | 2.00 | 79.2 | 90.0 |

## GW8

- Train rows: 108872
- Bank: 0.20 -> 0.30
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Mohamed Salah
- Effective captain: Ollie Watkins
- Chip used: none
- Predicted score: 56.85
- Actual score: 51.00
- Transfer: Pervis Estupiñán -> Matty Cash (projected gain 9.04, hit 0)
- Autosub: João Pedro Junqueira de Jesus replaced Bukayo Saka.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.1 | 4.09 | 11.65 | 19.20 | 1.00 | 105.1 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 4.9 | 2.99 | 8.70 | 14.23 | 2.00 | 78.2 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.6 | 5.06 | 15.50 | 24.60 | 6.00 | 88.5 | 90.0 |
| XI | XI | Matty Cash | DEF | 2 | 5.0 | 5.67 | 14.83 | 22.21 | 2.00 | 107.9 | 81.0 |
| XI | XI | William Saliba | DEF | 1 | 5.1 | 2.97 | 9.38 | 15.28 | 7.00 | 81.7 | 90.0 |
| Bench 2 | Bench | Raphaël Varane | DEF | 14 | 5.0 | 2.20 | 6.00 | 9.52 | 0.00 | 51.7 | 0.0 |
| Bench 4 | Bench | Ben Chilwell | DEF | 7 | 5.5 | 0.02 | 1.58 | 5.41 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.0 | 7.47 | 19.68 | 30.60 | 5.00 | 121.5 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.7 | 3.48 | 12.26 | 19.99 | 2.00 | 71.3 | 67.0 |
| Bench 3 | Autosub In | João Pedro Junqueira de Jesus | FWD | 5 | 5.3 | 1.92 | 7.25 | 12.31 | 2.00 | 43.5 | 88.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.5 | 5.89 | 18.60 | 30.65 | 15.00 | 87.0 | 90.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 8.6 | 3.28 | 13.51 | 23.62 | 0.00 | 47.6 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.2 | 4.24 | 13.11 | 21.36 | 2.00 | 83.6 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.72 | 12.24 | 20.70 | 2.00 | 67.3 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 3.50 | 11.77 | 19.12 | 2.00 | 60.1 | 90.0 |

## GW9

- Train rows: 109597
- Bank: 0.30 -> 1.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Ollie Watkins
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 54.98
- Actual score: 90.00
- Transfer: Kaoru Mitoma -> Pedro Lomba Neto (projected gain 1.46, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.1 | 3.52 | 11.01 | 17.58 | 1.00 | 91.2 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 4.9 | 3.36 | 9.76 | 15.42 | 3.00 | 79.7 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.7 | 5.01 | 14.86 | 24.08 | 10.00 | 93.0 | 68.0 |
| XI | XI | Matty Cash | DEF | 2 | 5.0 | 3.72 | 10.74 | 16.07 | 2.00 | 66.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.1 | 3.12 | 9.52 | 15.65 | 1.00 | 80.5 | 90.0 |
| Bench 3 | Bench | Raphaël Varane | DEF | 14 | 5.0 | 1.30 | 3.93 | 6.74 | 1.00 | 29.1 | 6.0 |
| Bench 4 | Bench | Ben Chilwell | DEF | 7 | 5.5 | 0.28 | 2.35 | 5.32 | 0.00 | 7.4 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.1 | 5.51 | 16.15 | 25.46 | 11.00 | 80.4 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.8 | 4.18 | 12.25 | 19.99 | 9.00 | 63.2 | 90.0 |
| Bench 2 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.3 | 2.19 | 7.83 | 13.09 | 2.00 | 60.6 | 64.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.6 | 6.98 | 20.04 | 32.89 | 16.00 | 96.3 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.63 | 13.34 | 22.23 | 7.00 | 77.4 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.2 | 4.12 | 13.08 | 20.96 | 8.00 | 82.3 | 90.0 |
| XI | XI | Pedro Lomba Neto | MID | 20 | 5.8 | 4.28 | 12.07 | 19.38 | 4.00 | 75.2 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.5 | 2.91 | 11.24 | 19.79 | 5.00 | 35.8 | 90.0 |

## GW10

- Train rows: 110327
- Bank: 1.00 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Ollie Watkins
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 64.69
- Actual score: 46.00
- Transfer: Pedro Lomba Neto -> Kaoru Mitoma (projected gain 2.15, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.1 | 4.40 | 12.30 | 19.66 | 3.00 | 99.4 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 4.8 | 2.45 | 8.34 | 13.77 | 2.00 | 79.6 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.7 | 5.34 | 15.49 | 25.51 | 0.00 | 85.8 | 90.0 |
| XI | XI | Matty Cash | DEF | 2 | 5.0 | 4.21 | 11.73 | 18.60 | 5.00 | 84.3 | 78.0 |
| XI | XI | William Saliba | DEF | 1 | 5.1 | 3.95 | 10.43 | 16.83 | 7.00 | 82.4 | 90.0 |
| Bench 4 | Bench | Raphaël Varane | DEF | 14 | 5.0 | 0.93 | 3.66 | 6.26 | 0.00 | 28.9 | 0.0 |
| Bench 3 | Bench | Ben Chilwell | DEF | 7 | 5.4 | 1.03 | 3.11 | 5.48 | 0.00 | 11.1 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.1 | 7.49 | 20.07 | 31.51 | 2.00 | 113.5 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.8 | 4.00 | 12.44 | 20.22 | 2.00 | 80.5 | 86.0 |
| Bench 2 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.3 | 2.69 | 8.02 | 12.71 | 1.00 | 54.3 | 12.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.6 | 7.68 | 21.50 | 34.87 | 8.00 | 107.4 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.6 | 7.29 | 17.86 | 29.25 | 6.00 | 101.5 | 72.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.3 | 4.91 | 14.13 | 22.94 | 2.00 | 90.8 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 4.41 | 12.44 | 20.02 | 2.00 | 79.2 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 3.33 | 11.37 | 19.23 | 1.00 | 71.0 | 90.0 |

## GW11

- Train rows: 111058
- Bank: 0.30 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Ollie Watkins
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 56.40
- Actual score: 49.00
- Transfer: Raphaël Varane -> Joachim Andersen (projected gain 1.77, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.74 | 10.56 | 17.20 | 1.00 | 90.9 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 4.8 | 2.70 | 8.54 | 14.41 | 6.00 | 86.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.7 | 4.09 | 14.19 | 23.86 | 9.00 | 79.4 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.0 | 4.30 | 11.63 | 18.55 | 5.00 | 93.9 | 90.0 |
| XI | XI | Matty Cash | DEF | 2 | 5.1 | 4.26 | 11.59 | 18.40 | 0.00 | 78.5 | 58.0 |
| Bench 2 | Bench | William Saliba | DEF | 1 | 5.1 | 3.28 | 10.10 | 16.28 | 2.00 | 83.9 | 90.0 |
| Bench 4 | Bench | Ben Chilwell | DEF | 7 | 5.4 | 0.55 | 2.41 | 4.44 | 0.00 | 10.9 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.2 | 5.29 | 16.23 | 25.37 | 2.00 | 72.2 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.8 | 4.54 | 12.17 | 19.22 | 2.00 | 73.8 | 70.0 |
| Bench 3 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.3 | 2.04 | 5.94 | 10.28 | 1.00 | 35.2 | 45.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.7 | 7.35 | 21.14 | 34.49 | 2.00 | 99.9 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.6 | 3.73 | 12.97 | 22.10 | 2.00 | 56.4 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 4.26 | 12.41 | 19.86 | 6.00 | 77.9 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.3 | 3.91 | 11.90 | 19.90 | 7.00 | 75.4 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 3.58 | 11.47 | 19.50 | 11.00 | 76.4 | 90.0 |

## GW12

- Train rows: 111791
- Bank: 0.30 -> 1.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Kieran Trippier
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 64.05
- Actual score: 70.00
- Transfer: Ben Chilwell -> Tyrick Mitchell (projected gain 0.14, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.88 | 10.57 | 16.88 | 2.00 | 92.0 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 4.8 | 3.28 | 8.97 | 15.06 | 8.00 | 88.5 | 90.0 |
| Vice Captain | XI | Kieran Trippier | DEF | 15 | 6.7 | 6.37 | 16.95 | 26.88 | 1.00 | 96.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.2 | 4.49 | 11.58 | 18.15 | 9.00 | 92.0 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.0 | 3.89 | 11.28 | 18.05 | 1.00 | 89.7 | 90.0 |
| XI | XI | Matty Cash | DEF | 2 | 5.1 | 3.80 | 10.54 | 16.82 | 2.00 | 69.8 | 90.0 |
| Bench 2 | Bench | Tyrick Mitchell | DEF | 8 | 4.6 | 3.59 | 9.86 | 15.83 | 1.00 | 92.3 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.2 | 5.93 | 17.35 | 27.54 | 6.00 | 89.2 | 90.0 |
| Bench 3 | Bench | Julián Álvarez | FWD | 13 | 6.8 | 3.56 | 11.35 | 18.37 | 5.00 | 66.3 | 78.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.3 | 2.81 | 7.33 | 12.11 | 1.00 | 45.7 | 45.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.7 | 7.06 | 21.03 | 34.47 | 16.00 | 104.8 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.6 | 5.98 | 15.93 | 25.98 | 5.00 | 87.8 | 80.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.4 | 5.83 | 15.81 | 24.64 | 8.00 | 106.2 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 5.02 | 13.38 | 20.86 | 1.00 | 85.6 | 45.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 4.75 | 13.03 | 21.80 | 3.00 | 91.5 | 90.0 |

## GW13

- Train rows: 112534
- Bank: 1.10 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 58.91
- Actual score: 44.00
- Transfer: Kaoru Mitoma -> Bryan Mbeumo (projected gain 4.40, hit 0)
- Autosub: Matty Cash replaced Jarrod Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.89 | 10.59 | 16.78 | 3.00 | 91.9 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 4.8 | 3.13 | 9.09 | 15.23 | 9.00 | 88.7 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.7 | 4.91 | 14.42 | 23.49 | 1.00 | 88.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.2 | 4.82 | 13.04 | 19.97 | 6.00 | 98.3 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.93 | 11.14 | 17.76 | 1.00 | 91.1 | 90.0 |
| Bench 2 | Autosub In | Matty Cash | DEF | 2 | 5.0 | 2.90 | 9.42 | 15.00 | 0.00 | 65.1 | 45.0 |
| Bench 3 | Bench | Tyrick Mitchell | DEF | 8 | 4.6 | 2.84 | 8.45 | 13.45 | 1.00 | 73.5 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.2 | 4.95 | 15.76 | 24.18 | 5.00 | 81.3 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.8 | 3.83 | 11.46 | 18.97 | 2.00 | 69.2 | 90.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.3 | 2.12 | 6.20 | 10.41 | 13.00 | 42.0 | 69.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.7 | 6.71 | 21.95 | 35.97 | 5.00 | 106.9 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.6 | 6.07 | 16.96 | 26.86 | 8.00 | 94.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 4.61 | 13.75 | 22.00 | 2.00 | 89.2 | 90.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.4 | 4.59 | 12.97 | 20.80 | 0.00 | 74.5 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 3.88 | 11.77 | 19.62 | 6.00 | 79.4 | 90.0 |

## GW14

- Train rows: 113281
- Bank: 0.70 -> 2.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 59.62
- Actual score: 68.00
- Transfer: Jarrod Bowen -> Anthony Gordon (projected gain 3.20, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.74 | 10.14 | 16.22 | 2.00 | 89.5 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 4.8 | 2.95 | 9.74 | 16.31 | 3.00 | 90.1 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.7 | 4.65 | 13.69 | 22.64 | 12.00 | 87.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.41 | 11.88 | 18.55 | 1.00 | 85.3 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.20 | 9.64 | 15.65 | 2.00 | 78.0 | 90.0 |
| Bench 2 | Bench | Matty Cash | DEF | 2 | 5.0 | 2.97 | 8.58 | 14.33 | 1.00 | 55.7 | 16.0 |
| Bench 4 | Bench | Tyrick Mitchell | DEF | 8 | 4.6 | 2.43 | 7.53 | 12.47 | 2.00 | 71.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.2 | 4.56 | 13.87 | 23.15 | 11.00 | 67.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.7 | 3.58 | 11.00 | 18.00 | 5.00 | 60.9 | 86.0 |
| Bench 3 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.3 | 2.75 | 8.01 | 13.47 | 4.00 | 59.3 | 33.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.8 | 7.32 | 21.61 | 35.87 | 5.00 | 106.3 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.7 | 6.47 | 17.60 | 28.02 | 8.00 | 99.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.0 | 6.30 | 16.54 | 25.95 | 5.00 | 100.1 | 77.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 3.80 | 12.71 | 21.33 | 2.00 | 84.9 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.9 | 4.26 | 11.71 | 18.68 | 10.00 | 92.7 | 90.0 |

## GW15

- Train rows: 114034
- Bank: 2.20 -> 1.80
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 58.93
- Actual score: 31.00
- Transfer: Matty Cash -> Pedro Porro (projected gain 0.46, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.45 | 10.30 | 17.10 | 2.00 | 88.7 | 90.0 |
| Bench 1 | Bench | Alphonse Areola | GK | 19 | 4.2 | 3.20 | 9.49 | 15.41 | 0.00 | 87.3 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.7 | 5.47 | 15.31 | 24.83 | 1.00 | 98.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.17 | 11.59 | 18.47 | 1.00 | 84.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 3.66 | 10.19 | 16.95 | 5.00 | 83.4 | 90.0 |
| Bench 2 | Bench | Joachim Andersen | DEF | 8 | 5.1 | 3.63 | 9.89 | 16.27 | 1.00 | 82.1 | 90.0 |
| Bench 3 | Bench | Tyrick Mitchell | DEF | 8 | 4.6 | 2.84 | 7.71 | 12.90 | 1.00 | 74.5 | 28.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.2 | 4.49 | 14.34 | 24.26 | 1.00 | 77.8 | 89.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.7 | 4.29 | 12.63 | 20.77 | 2.00 | 73.2 | 67.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.3 | 2.78 | 8.19 | 13.48 | 2.00 | 51.7 | 68.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.8 | 7.58 | 21.57 | 36.24 | 3.00 | 106.6 | 66.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.7 | 6.41 | 17.63 | 28.32 | 5.00 | 96.1 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 4.12 | 12.44 | 20.86 | 0.00 | 82.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.0 | 3.90 | 12.30 | 19.77 | 6.00 | 60.7 | 39.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.9 | 3.81 | 11.15 | 17.54 | 2.00 | 75.2 | 90.0 |

## GW16

- Train rows: 114791
- Bank: 1.80 -> 1.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 56.85
- Actual score: 47.00
- Transfer: Bryan Mbeumo -> Jarrod Bowen (projected gain 4.04, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.26 | 9.12 | 15.54 | 1.00 | 88.8 | 90.0 |
| Bench 1 | Bench | Alphonse Areola | GK | 19 | 4.2 | 1.83 | 5.84 | 10.03 | 0.00 | 45.4 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.7 | 5.07 | 14.90 | 24.44 | -1.00 | 95.6 | 85.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 3.63 | 10.64 | 17.39 | 5.00 | 77.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 3.36 | 10.55 | 17.00 | 2.00 | 81.7 | 90.0 |
| Bench 3 | Bench | Joachim Andersen | DEF | 8 | 5.0 | 2.79 | 8.64 | 14.13 | 0.00 | 76.0 | 90.0 |
| Bench 4 | Bench | Tyrick Mitchell | DEF | 8 | 4.6 | 1.55 | 5.84 | 9.93 | 0.00 | 50.2 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.2 | 4.40 | 14.16 | 23.68 | 2.00 | 86.1 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.7 | 4.21 | 12.26 | 19.94 | 5.00 | 66.5 | 90.0 |
| Bench 2 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 3.35 | 8.96 | 14.59 | 2.00 | 60.1 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.8 | 6.70 | 20.26 | 33.38 | 13.00 | 93.9 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.7 | 5.84 | 17.50 | 28.27 | 2.00 | 97.5 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 4.87 | 13.19 | 22.25 | 1.00 | 90.5 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.7 | 4.52 | 12.84 | 20.85 | 2.00 | 83.6 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.0 | 4.30 | 12.26 | 19.64 | 2.00 | 81.2 | 73.0 |

## GW17

- Train rows: 115549
- Bank: 1.00 -> 0.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 59.33
- Actual score: 53.00
- Transfer: Alphonse Areola -> Bernd Leno (projected gain 1.24, hit 0)
- Autosub: Joachim Andersen replaced Kieran Trippier.
- Autosub: João Pedro Junqueira de Jesus replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.14 | 9.73 | 15.75 | 3.00 | 86.7 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 4.8 | 2.40 | 8.53 | 14.10 | 10.00 | 82.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 5.23 | 13.51 | 21.52 | 8.00 | 98.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.05 | 11.49 | 18.15 | 7.00 | 85.3 | 90.0 |
| XI | Bench | Kieran Trippier | DEF | 15 | 6.7 | 3.41 | 11.01 | 19.40 | 0.00 | 68.0 | 0.0 |
| Bench 3 | Autosub In | Joachim Andersen | DEF | 8 | 5.0 | 2.34 | 7.85 | 12.87 | 0.00 | 75.5 | 90.0 |
| Bench 4 | Bench | Tyrick Mitchell | DEF | 8 | 4.6 | 0.58 | 3.17 | 5.88 | 1.00 | 30.1 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.2 | 5.90 | 17.02 | 27.71 | 9.00 | 101.4 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.7 | 5.27 | 14.42 | 22.78 | 2.00 | 91.2 | 90.0 |
| Bench 2 | Autosub In | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 2.42 | 8.63 | 13.71 | 1.00 | 52.8 | 30.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.8 | 7.21 | 22.08 | 35.86 | 3.00 | 110.7 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.8 | 6.42 | 18.46 | 29.40 | 3.00 | 100.2 | 88.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.7 | 4.43 | 12.28 | 19.32 | 8.00 | 81.6 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.3 | 3.13 | 11.30 | 19.01 | 0.00 | 70.8 | 0.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.0 | 3.94 | 10.84 | 17.45 | 6.00 | 70.2 | 83.0 |

## GW18

- Train rows: 116314
- Bank: 0.40 -> 3.00
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Mohamed Salah
- Effective captain: Ollie Watkins
- Chip used: none
- Predicted score: 59.33
- Actual score: 32.00
- Transfer: Bruno Borges Fernandes -> Cole Palmer (projected gain 5.33, hit 0)
- Autosub: Joachim Andersen replaced Julián Álvarez.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.65 | 10.19 | 16.53 | 1.00 | 93.2 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 4.8 | 3.30 | 10.10 | 16.74 | 2.00 | 90.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 4.82 | 12.80 | 19.76 | 2.00 | 87.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.7 | 3.81 | 11.00 | 18.66 | 2.00 | 59.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 3.53 | 10.95 | 17.46 | 2.00 | 89.5 | 90.0 |
| Bench 2 | Autosub In | Joachim Andersen | DEF | 8 | 5.0 | 3.01 | 8.30 | 13.19 | 2.00 | 77.9 | 90.0 |
| Bench 4 | Bench | Tyrick Mitchell | DEF | 8 | 4.6 | 2.27 | 6.31 | 10.08 | 1.00 | 60.2 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.3 | 7.28 | 18.68 | 29.10 | 2.00 | 110.9 | 90.0 |
| XI | Bench | Julián Álvarez | FWD | 13 | 6.7 | 3.18 | 10.88 | 18.16 | 0.00 | 54.5 | 0.0 |
| Bench 3 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 2.67 | 7.85 | 13.10 | 2.00 | 41.7 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.8 | 6.37 | 20.40 | 33.56 | 7.00 | 96.9 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.8 | 5.91 | 18.18 | 28.80 | 1.00 | 97.3 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.6 | 5.16 | 13.62 | 21.50 | 1.00 | 99.3 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.7 | 4.32 | 12.58 | 19.98 | 8.00 | 86.8 | 87.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.0 | 4.02 | 11.58 | 18.86 | 2.00 | 69.4 | 90.0 |

## GW19

- Train rows: 117083
- Bank: 3.00 -> 2.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 59.03
- Actual score: 47.00
- Transfer: Julián Álvarez -> Dominic Solanke (projected gain 4.80, hit 0)
- Autosub: João Pedro Junqueira de Jesus replaced Cole Palmer.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.09 | 9.37 | 15.52 | 1.00 | 91.4 | 90.0 |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.7 | 2.95 | 8.79 | 14.69 | 0.00 | 84.2 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.7 | 4.84 | 13.43 | 22.13 | 1.00 | 82.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 4.14 | 12.03 | 19.11 | 5.00 | 83.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.31 | 11.58 | 18.33 | 1.00 | 93.8 | 90.0 |
| Bench 3 | Bench | Joachim Andersen | DEF | 8 | 4.9 | 2.87 | 8.55 | 13.68 | 1.00 | 81.0 | 90.0 |
| Bench 4 | Bench | Tyrick Mitchell | DEF | 8 | 4.6 | 2.05 | 6.31 | 10.11 | 0.00 | 64.9 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.55 | 14.34 | 22.80 | 2.00 | 75.0 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.0 | 5.04 | 13.39 | 21.29 | 6.00 | 79.7 | 90.0 |
| Bench 2 | Autosub In | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 3.12 | 8.64 | 13.78 | 16.00 | 63.2 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.9 | 6.95 | 20.91 | 34.64 | 3.00 | 104.2 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.8 | 6.28 | 17.64 | 28.27 | 2.00 | 96.2 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.7 | 4.48 | 13.63 | 21.68 | 6.00 | 89.6 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.0 | 4.81 | 12.88 | 21.02 | 1.00 | 82.6 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 5.6 | 3.60 | 11.13 | 17.98 | 0.00 | 66.2 | 0.0 |

## GW20

- Train rows: 117854
- Bank: 2.60 -> 0.90
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Ollie Watkins
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 59.83
- Actual score: 71.00
- Transfer: Anthony Gordon -> Phil Foden (projected gain 4.19, hit 0)
- Autosub: Joachim Andersen replaced Kieran Trippier.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.16 | 9.07 | 15.15 | 1.00 | 87.1 | 90.0 |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.7 | 2.63 | 8.38 | 13.93 | 1.00 | 84.6 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 4.54 | 12.97 | 20.74 | 2.00 | 92.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 3.95 | 11.23 | 18.19 | 0.00 | 91.6 | 90.0 |
| XI | Bench | Kieran Trippier | DEF | 15 | 6.6 | 3.27 | 11.05 | 18.90 | 0.00 | 72.7 | 0.0 |
| Bench 2 | Autosub In | Joachim Andersen | DEF | 8 | 4.9 | 3.12 | 8.39 | 13.56 | 2.00 | 80.9 | 90.0 |
| Bench 4 | Bench | Tyrick Mitchell | DEF | 8 | 4.6 | 2.42 | 6.68 | 10.65 | 6.00 | 72.2 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.4 | 5.92 | 16.17 | 25.75 | 8.00 | 98.4 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.0 | 4.06 | 12.47 | 20.11 | 2.00 | 74.5 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 4.24 | 10.84 | 16.81 | 2.00 | 80.5 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.9 | 7.57 | 21.08 | 34.44 | 16.00 | 103.5 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.8 | 5.50 | 16.37 | 26.65 | 7.00 | 89.2 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.8 | 5.34 | 15.25 | 24.61 | 3.00 | 96.0 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 7.7 | 4.72 | 12.54 | 19.82 | 12.00 | 85.4 | 90.0 |
| Bench 3 | Bench | Cole Palmer | MID | 7 | 5.6 | 3.05 | 8.92 | 15.19 | 18.00 | 47.6 | 90.0 |

## GW21

- Train rows: 118627
- Bank: 0.90 -> 1.20
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Cole Palmer
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 66.19
- Actual score: 45.00
- Transfer: Kieran Trippier -> Virgil van Dijk (projected gain 2.83, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 2.79 | 8.53 | 14.10 | 2.00 | 80.9 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 4.8 | 2.54 | 7.80 | 13.04 | 2.00 | 75.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 4.86 | 13.78 | 22.23 | 6.00 | 102.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.3 | 4.09 | 11.33 | 17.91 | 6.00 | 91.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.20 | 11.30 | 18.15 | 6.00 | 91.5 | 90.0 |
| Bench 2 | Bench | Joachim Andersen | DEF | 8 | 4.9 | 2.47 | 7.75 | 12.84 | 0.00 | 78.2 | 90.0 |
| Bench 3 | Bench | Tyrick Mitchell | DEF | 8 | 4.6 | 2.10 | 6.55 | 10.91 | 0.00 | 74.2 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 6.15 | 17.13 | 27.02 | 1.00 | 101.7 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.0 | 4.13 | 12.77 | 20.49 | 2.00 | 79.2 | 82.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 4.97 | 12.57 | 19.17 | 2.00 | 90.7 | 90.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 8.8 | 7.89 | 20.01 | 31.40 | 3.00 | 119.4 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 7.8 | 6.95 | 17.87 | 27.22 | 2.00 | 116.1 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 5.6 | 7.19 | 16.94 | 25.66 | 10.00 | 118.3 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.08 | 14.29 | 23.06 | 2.00 | 89.4 | 90.0 |
| Bench 4 | Bench | Mohamed Salah | MID | 11 | 12.8 | 1.92 | 11.15 | 21.38 | 0.00 | 13.5 | 0.0 |

## GW22

- Train rows: 119414
- Bank: 1.20 -> 1.80
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 50.97
- Actual score: 54.00
- Transfer: André Onana -> Alphonse Areola (projected gain 1.14, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.45 | 9.66 | 16.04 | 3.00 | 79.9 | 90.0 |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.7 | 3.09 | 8.54 | 14.08 | 8.00 | 83.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.61 | 12.90 | 21.15 | 1.00 | 86.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 3.99 | 10.88 | 17.56 | 2.00 | 84.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.3 | 3.37 | 9.95 | 16.05 | 2.00 | 76.8 | 90.0 |
| Bench 3 | Bench | Joachim Andersen | DEF | 8 | 4.8 | 3.02 | 8.15 | 13.51 | 1.00 | 80.5 | 90.0 |
| Bench 4 | Bench | Tyrick Mitchell | DEF | 8 | 4.6 | 2.57 | 6.75 | 11.09 | 1.00 | 74.3 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.98 | 14.80 | 23.95 | 7.00 | 78.7 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.0 | 3.60 | 11.32 | 18.07 | 8.00 | 67.6 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 3.92 | 10.78 | 16.92 | 2.00 | 72.7 | 70.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 8.8 | 6.21 | 17.07 | 27.21 | 10.00 | 83.6 | 90.0 |
| Bench 2 | Bench | Mohamed Salah | MID | 11 | 12.8 | 3.06 | 11.72 | 22.02 | 0.00 | 14.6 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 7.8 | 3.66 | 11.65 | 18.57 | 6.00 | 43.0 | 76.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 3.76 | 11.63 | 19.95 | 1.00 | 58.9 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.7 | 3.21 | 11.16 | 17.13 | 2.00 | 55.5 | 84.0 |

## GW23

- Train rows: 120213
- Bank: 1.80 -> 1.40
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Bukayo Saka
- Effective captain: Ollie Watkins
- Chip used: none
- Predicted score: 52.67
- Actual score: 97.00
- Transfer: Virgil van Dijk -> Kieran Trippier (projected gain 2.92, hit 0)
- Autosub: João Pedro Junqueira de Jesus replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Alphonse Areola | GK | 19 | 4.2 | 3.08 | 9.61 | 15.66 | 1.00 | 81.6 | 45.0 |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.15 | 8.66 | 14.13 | 1.00 | 84.4 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.7 | 4.47 | 12.57 | 20.31 | 9.00 | 83.6 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.19 | 12.16 | 19.95 | 1.00 | 84.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 3.40 | 10.32 | 16.71 | 1.00 | 83.1 | 90.0 |
| Bench 3 | Bench | Joachim Andersen | DEF | 8 | 4.8 | 2.61 | 7.80 | 12.62 | 3.00 | 77.5 | 90.0 |
| Bench 4 | Bench | Tyrick Mitchell | DEF | 8 | 4.6 | 2.15 | 6.38 | 10.40 | 0.00 | 71.3 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.4 | 5.78 | 16.25 | 26.22 | 18.00 | 93.3 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.0 | 4.39 | 12.28 | 19.99 | 2.00 | 73.0 | 90.0 |
| Bench 2 | Autosub In | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 2.76 | 8.62 | 14.81 | 8.00 | 49.2 | 87.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.8 | 5.55 | 16.75 | 26.86 | 9.00 | 87.6 | 78.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.7 | 4.47 | 12.86 | 20.62 | 8.00 | 86.2 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 7.8 | 4.22 | 12.67 | 20.98 | 20.00 | 62.1 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 12.7 | 3.58 | 12.65 | 21.80 | 0.00 | 36.5 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.8 | 3.69 | 11.57 | 20.04 | 2.00 | 67.9 | 90.0 |

## GW24

- Train rows: 121022
- Bank: 1.40 -> 1.00
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Phil Foden
- Effective captain: Ollie Watkins
- Chip used: none
- Predicted score: 53.55
- Actual score: 57.00
- Transfer: João Pedro Junqueira de Jesus -> Matheus Santos Carneiro Da Cunha (projected gain 4.59, hit 0)
- Autosub: Joachim Andersen replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Alphonse Areola | GK | 19 | 4.2 | 2.58 | 8.79 | 14.30 | 0.00 | 70.5 | 90.0 |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 2.99 | 8.30 | 13.64 | 3.00 | 79.9 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.7 | 4.71 | 13.15 | 21.15 | 4.00 | 90.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 3.86 | 11.27 | 18.78 | 2.00 | 78.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 3.44 | 10.33 | 16.61 | 12.00 | 81.0 | 90.0 |
| Bench 2 | Autosub In | Joachim Andersen | DEF | 8 | 4.8 | 2.74 | 7.82 | 12.76 | 1.00 | 76.7 | 90.0 |
| Bench 4 | Bench | Tyrick Mitchell | DEF | 8 | 4.6 | 2.11 | 6.17 | 10.02 | 1.00 | 69.6 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.4 | 5.87 | 16.44 | 27.25 | 2.00 | 94.2 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.8 | 4.86 | 12.40 | 20.24 | 1.00 | 85.0 | 19.0 |
| Bench 3 | Bench | Dominic Solanke | FWD | 3 | 7.0 | 2.64 | 9.12 | 15.76 | 4.00 | 54.1 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.8 | 5.15 | 16.36 | 26.75 | 15.00 | 75.6 | 66.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 7.8 | 5.84 | 15.79 | 25.39 | 3.00 | 93.1 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.7 | 4.71 | 13.64 | 22.05 | 10.00 | 81.8 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.8 | 3.08 | 10.25 | 17.77 | 2.00 | 63.6 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 12.7 | 3.17 | 10.19 | 19.57 | 0.00 | 16.2 | 0.0 |

## GW25

- Train rows: 121836
- Bank: 1.00 -> 0.30
- Free transfers: 2 -> 2
- Captain: Darwin Núñez Ribeiro
- Vice captain: Phil Foden
- Effective captain: Darwin Núñez Ribeiro
- Chip used: none
- Predicted score: 56.54
- Actual score: 70.00
- Transfer: Dominic Solanke -> Darwin Núñez Ribeiro (projected gain 8.96, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.16 | 9.19 | 15.03 | 3.00 | 80.7 | 90.0 |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.7 | 2.61 | 7.73 | 13.10 | 1.00 | 77.2 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.65 | 12.74 | 20.81 | 1.00 | 85.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.42 | 11.97 | 19.07 | 6.00 | 88.8 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 4.7 | 2.60 | 7.47 | 12.30 | 2.00 | 73.3 | 90.0 |
| Bench 3 | Bench | Pedro Porro | DEF | 18 | 5.5 | 1.92 | 6.90 | 12.61 | 0.00 | 49.2 | 0.0 |
| Bench 2 | Bench | Tyrick Mitchell | DEF | 8 | 4.5 | 2.27 | 6.58 | 10.71 | 2.00 | 71.2 | 90.0 |
| Captain | Captain | Darwin Núñez Ribeiro | FWD | 11 | 7.6 | 7.18 | 16.68 | 25.30 | 5.00 | 105.6 | 45.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.3 | 4.10 | 13.56 | 23.15 | 13.00 | 70.5 | 90.0 |
| Bench 4 | Bench | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.7 | 1.42 | 6.77 | 12.48 | 0.00 | 32.3 | 0.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.8 | 6.21 | 17.51 | 28.80 | 15.00 | 78.1 | 68.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 7.8 | 6.81 | 17.16 | 26.31 | 5.00 | 109.1 | 180.0 |
| XI | XI | Mohamed Salah | MID | 11 | 12.7 | 4.83 | 12.39 | 21.66 | 11.00 | 52.1 | 46.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.7 | 2.45 | 10.39 | 18.19 | 2.00 | 59.7 | 70.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.7 | 2.96 | 9.38 | 16.33 | 2.00 | 61.4 | 90.0 |

## GW26

- Train rows: 122659
- Bank: 0.30 -> 0.30
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 60.73
- Actual score: 75.00
- Transfer: Pedro Porro -> Kyle Walker (projected gain 2.82, hit 0)
- Autosub: Tyrick Mitchell replaced Kyle Walker.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.68 | 10.03 | 16.41 | 2.00 | 90.5 | 90.0 |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.7 | 2.40 | 7.71 | 12.86 | 3.00 | 79.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 3.96 | 13.17 | 21.30 | 0.00 | 94.2 | 90.0 |
| XI | Bench | Kyle Walker | DEF | 13 | 5.5 | 4.94 | 12.71 | 19.87 | 0.00 | 101.2 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.60 | 12.56 | 19.69 | 2.00 | 89.4 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 4.7 | 3.16 | 8.46 | 13.55 | 6.00 | 83.5 | 90.0 |
| Bench 3 | Autosub In | Tyrick Mitchell | DEF | 8 | 4.5 | 2.49 | 6.74 | 10.73 | 5.00 | 74.0 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.4 | 7.53 | 19.82 | 31.61 | 9.00 | 118.7 | 90.0 |
| Bench 2 | Bench | Darwin Núñez Ribeiro | FWD | 11 | 7.6 | 2.88 | 10.56 | 17.68 | 0.00 | 28.6 | 0.0 |
| Bench 4 | Bench | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 2.12 | 6.27 | 11.72 | 0.00 | 25.1 | 0.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 8.8 | 7.98 | 21.36 | 32.94 | 10.00 | 104.8 | 75.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 6.67 | 18.25 | 28.89 | 11.00 | 110.7 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 12.7 | 3.24 | 11.56 | 20.35 | 0.00 | 35.8 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.7 | 3.93 | 10.86 | 18.10 | 20.00 | 77.6 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 5.7 | 3.06 | 10.56 | 18.46 | 0.00 | 52.8 | 0.0 |

## GW27

- Train rows: 123487
- Bank: 0.30 -> 0.80
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 57.52
- Actual score: 76.00
- Transfer: Darwin Núñez Ribeiro -> Dominic Solanke (projected gain 6.58, hit 0)
- Autosub: Tyrick Mitchell replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.54 | 9.97 | 16.09 | 13.00 | 92.9 | 90.0 |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.7 | 2.94 | 8.30 | 13.65 | 8.00 | 81.4 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.46 | 13.01 | 21.49 | 1.00 | 88.5 | 51.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.43 | 12.04 | 18.91 | 6.00 | 82.7 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 4.7 | 2.42 | 7.70 | 12.51 | 1.00 | 74.9 | 90.0 |
| Bench 3 | Bench | Kyle Walker | DEF | 13 | 5.5 | 2.03 | 6.35 | 10.91 | 2.00 | 38.9 | 90.0 |
| Bench 2 | Autosub In | Tyrick Mitchell | DEF | 8 | 4.5 | 2.04 | 6.29 | 10.15 | 1.00 | 70.1 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.4 | 6.47 | 18.90 | 29.37 | 13.00 | 83.1 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.1 | 4.73 | 12.83 | 19.68 | 2.00 | 73.1 | 88.0 |
| Bench 4 | Bench | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 0.81 | 3.89 | 8.18 | 0.00 | 13.6 | 0.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 8.9 | 7.45 | 20.00 | 32.83 | 7.00 | 85.1 | 45.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 5.62 | 16.63 | 26.78 | 15.00 | 88.6 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.7 | 4.43 | 12.59 | 20.28 | 5.00 | 90.9 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 12.7 | 3.61 | 11.14 | 19.09 | 0.00 | 37.2 | 0.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.6 | 2.92 | 8.60 | 14.95 | 5.00 | 42.9 | 90.0 |

## GW28

- Train rows: 124319
- Bank: 0.80 -> 0.80
- Free transfers: 2 -> 2
- Captain: Dominic Solanke
- Vice captain: Bukayo Saka
- Effective captain: Dominic Solanke
- Chip used: none
- Predicted score: 64.22
- Actual score: 49.00
- Transfer: Joachim Andersen -> Alfie Doughty (projected gain 4.05, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 4.17 | 11.27 | 18.27 | 2.00 | 98.0 | 90.0 |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.7 | 3.06 | 8.76 | 14.33 | 1.00 | 83.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.81 | 12.94 | 20.20 | 2.00 | 83.8 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 5.71 | 12.55 | 19.28 | 5.00 | 115.9 | 180.0 |
| XI | XI | Kyle Walker | DEF | 13 | 5.4 | 2.60 | 8.68 | 13.96 | 2.00 | 68.2 | 90.0 |
| Bench 3 | Bench | Kieran Trippier | DEF | 15 | 6.7 | 2.37 | 8.66 | 15.56 | 0.00 | 51.9 | 0.0 |
| Bench 2 | Bench | Tyrick Mitchell | DEF | 8 | 4.5 | 2.51 | 6.83 | 10.85 | 3.00 | 71.2 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.5 | 6.53 | 19.16 | 30.74 | 2.00 | 99.0 | 90.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.1 | 7.80 | 17.60 | 26.18 | 8.00 | 126.7 | 180.0 |
| Bench 4 | Bench | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.5 | 0.56 | 3.06 | 5.99 | 0.00 | 5.8 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 6.58 | 19.03 | 32.05 | 2.00 | 63.1 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 6.11 | 18.68 | 29.50 | 2.00 | 99.3 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.8 | 5.33 | 14.63 | 23.50 | 2.00 | 94.2 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.6 | 4.00 | 11.34 | 18.71 | 13.00 | 69.8 | 85.0 |
| XI | XI | Mohamed Salah | MID | 11 | 12.7 | 2.78 | 9.95 | 17.26 | 1.00 | 29.1 | 29.0 |

## GW29

- Train rows: 125157
- Bank: 0.80 -> 1.10
- Free transfers: 2 -> 2
- Captain: Jarrod Bowen
- Vice captain: Ollie Watkins
- Effective captain: Jarrod Bowen
- Chip used: none
- Predicted score: 57.23
- Actual score: 16.00
- Transfer: Matheus Santos Carneiro Da Cunha -> Carlton Morris (projected gain 5.75, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Alphonse Areola | GK | 19 | 4.2 | 2.75 | 8.98 | 15.07 | 3.00 | 78.5 | 90.0 |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 2.81 | 8.41 | 13.75 | 7.00 | 81.7 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 6.11 | 16.46 | 24.61 | 1.00 | 123.5 | 45.0 |
| XI | Bench | William Saliba | DEF | 1 | 5.4 | 3.38 | 11.29 | 18.78 | 0.00 | 70.5 | 0.0 |
| XI | Bench | Kyle Walker | DEF | 13 | 5.4 | 2.03 | 7.34 | 12.57 | 0.00 | 49.3 | 0.0 |
| Bench 3 | Bench | Kieran Trippier | DEF | 15 | 6.7 | 1.82 | 7.24 | 13.57 | 0.00 | 27.9 | 0.0 |
| Bench 4 | Bench | Tyrick Mitchell | DEF | 8 | 4.5 | 1.72 | 6.25 | 10.61 | 0.00 | 54.7 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.5 | 6.43 | 17.81 | 28.91 | 2.00 | 98.0 | 90.0 |
| XI | XI | Carlton Morris | FWD | 12 | 5.2 | 5.31 | 14.68 | 22.05 | 2.00 | 105.7 | 90.0 |
| XI | Bench | Dominic Solanke | FWD | 3 | 7.1 | 4.06 | 13.80 | 22.84 | 0.00 | 67.9 | 0.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 8.9 | 5.65 | 18.45 | 31.40 | 0.00 | 68.3 | 0.0 |
| Captain | Captain | Jarrod Bowen | MID | 19 | 7.8 | 6.70 | 18.26 | 27.90 | 2.00 | 121.6 | 90.0 |
| XI | Bench | Phil Foden | MID | 13 | 7.9 | 4.80 | 15.40 | 25.24 | 0.00 | 67.3 | 0.0 |
| XI | Bench | Cole Palmer | MID | 7 | 5.6 | 3.25 | 10.68 | 18.26 | 0.00 | 56.9 | 0.0 |
| Bench 2 | Bench | Mohamed Salah | MID | 11 | 12.7 | 2.63 | 9.94 | 17.58 | 0.00 | 16.2 | 0.0 |

## GW30

- Train rows: 125995
- Bank: 1.10 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Ollie Watkins
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 39.74
- Actual score: 65.00
- Transfer: Alfie Doughty -> Antonee Robinson (projected gain 4.58, hit 0)
- Autosub: Tyrick Mitchell replaced Kieran Trippier.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.39 | 10.54 | 17.19 | 2.00 | 93.7 | 45.0 |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.7 | 3.33 | 9.53 | 15.47 | 1.00 | 84.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.6 | 2.87 | 8.43 | 13.89 | 1.00 | 70.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 2.18 | 7.74 | 13.21 | 7.00 | 48.5 | 90.0 |
| XI | Bench | Kieran Trippier | DEF | 15 | 6.7 | 1.65 | 5.76 | 10.46 | 0.00 | 22.8 | 0.0 |
| Bench 4 | Bench | Kyle Walker | DEF | 13 | 5.4 | 0.95 | 4.49 | 7.98 | 0.00 | 33.5 | 0.0 |
| Bench 2 | Autosub In | Tyrick Mitchell | DEF | 8 | 4.5 | 1.37 | 4.25 | 7.19 | 2.00 | 38.5 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.5 | 4.82 | 15.59 | 26.38 | 1.00 | 76.1 | 45.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.1 | 2.53 | 8.64 | 15.24 | 7.00 | 32.9 | 84.0 |
| Bench 3 | Bench | Carlton Morris | FWD | 12 | 5.1 | 1.11 | 5.94 | 10.99 | 2.00 | 44.4 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.8 | 5.35 | 14.51 | 22.83 | 7.00 | 60.6 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.8 | 3.20 | 12.67 | 21.89 | 3.00 | 33.6 | 77.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 2.61 | 11.63 | 19.35 | 3.00 | 40.7 | 60.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.7 | 4.35 | 11.12 | 17.95 | 15.00 | 67.7 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.8 | 1.43 | 7.72 | 14.56 | 10.00 | 34.2 | 90.0 |

## GW31

- Train rows: 126837
- Bank: 1.20 -> 0.40
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Mohamed Salah
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 51.86
- Actual score: 66.00
- Transfer: Tyrick Mitchell -> Gabriel dos Santos Magalhães (projected gain 3.02, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.02 | 8.82 | 14.42 | 1.00 | 83.2 | 90.0 |
| Bench 1 | Bench | Alphonse Areola | GK | 19 | 4.2 | 2.44 | 7.73 | 13.33 | 0.00 | 64.4 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.15 | 10.96 | 17.94 | 7.00 | 77.2 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.76 | 9.62 | 15.58 | 6.00 | 70.7 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.6 | 3.00 | 8.76 | 14.14 | 1.00 | 77.6 | 90.0 |
| Bench 2 | Bench | Kieran Trippier | DEF | 15 | 6.7 | 1.73 | 5.26 | 9.51 | 0.00 | 22.2 | 0.0 |
| Bench 4 | Bench | Kyle Walker | DEF | 13 | 5.3 | 1.11 | 3.73 | 7.09 | 0.00 | 26.2 | 0.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.1 | 4.55 | 12.65 | 20.14 | 2.00 | 76.4 | 89.0 |
| Bench 3 | Bench | Ollie Watkins | FWD | 2 | 8.4 | 1.58 | 8.95 | 17.52 | 0.00 | 30.1 | 0.0 |
| XI | XI | Carlton Morris | FWD | 12 | 5.1 | 2.36 | 7.99 | 13.36 | 2.00 | 76.0 | 90.0 |
| Captain | Bench | Bukayo Saka | MID | 1 | 8.8 | 6.19 | 16.34 | 26.71 | 0.00 | 76.7 | 0.0 |
| Vice Captain | Captain | Mohamed Salah | MID | 11 | 12.9 | 5.92 | 15.92 | 24.57 | 1.00 | 61.9 | 59.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.8 | 4.32 | 13.23 | 22.14 | 5.00 | 84.6 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.7 | 4.59 | 13.08 | 20.51 | 20.00 | 72.8 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 3.80 | 11.95 | 20.09 | 20.00 | 56.4 | 79.0 |

## GW32

- Train rows: 127681
- Bank: 0.40 -> 0.90
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Phil Foden
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 56.39
- Actual score: 57.00
- Transfer: Ollie Watkins -> Alexander Isak (projected gain 5.13, hit 0)
- Autosub: Carlton Morris replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.06 | 8.76 | 14.28 | 3.00 | 84.3 | 90.0 |
| Bench 1 | Bench | Alphonse Areola | GK | 19 | 4.2 | 1.41 | 5.23 | 9.62 | 0.00 | 36.5 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 3.96 | 11.38 | 18.63 | 5.00 | 82.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.42 | 9.88 | 16.08 | 6.00 | 76.6 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.6 | 3.03 | 8.60 | 14.08 | 2.00 | 78.2 | 90.0 |
| Bench 3 | Bench | Kieran Trippier | DEF | 15 | 6.6 | 1.19 | 4.39 | 8.05 | 0.00 | 17.7 | 0.0 |
| Bench 4 | Bench | Kyle Walker | DEF | 13 | 5.3 | 0.90 | 3.01 | 5.95 | 0.00 | 16.1 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.63 | 13.25 | 19.90 | 2.00 | 74.3 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.41 | 11.79 | 19.75 | 2.00 | 72.3 | 90.0 |
| Bench 2 | Autosub In | Carlton Morris | FWD | 12 | 5.0 | 2.85 | 8.23 | 14.01 | 8.00 | 70.7 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 5.8 | 7.44 | 17.89 | 27.58 | 5.00 | 96.3 | 73.0 |
| Vice Captain | Bench | Phil Foden | MID | 13 | 7.9 | 5.67 | 16.23 | 26.69 | 0.00 | 92.3 | 0.0 |
| XI | XI | Mohamed Salah | MID | 11 | 12.9 | 5.28 | 15.28 | 24.23 | 8.00 | 62.7 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.8 | 4.99 | 14.28 | 23.54 | 1.00 | 96.1 | 53.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.7 | 3.06 | 10.19 | 17.93 | 10.00 | 31.0 | 63.0 |

## GW33

- Train rows: 128527
- Bank: 0.90 -> 0.90
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.86
- Actual score: 71.00
- Transfer: Kieran Trippier -> Virgil van Dijk (projected gain 2.26, hit 0)
- Autosub: Antonee Robinson replaced Jarrod Bowen.
- Autosub: Carlton Morris replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 2.85 | 8.50 | 13.80 | 9.00 | 82.9 | 90.0 |
| Bench 1 | Bench | Alphonse Areola | GK | 19 | 4.2 | 1.22 | 3.96 | 7.37 | 0.00 | 24.5 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 4.51 | 12.28 | 19.63 | 1.00 | 89.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.28 | 11.30 | 17.60 | 0.00 | 84.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.6 | 3.80 | 10.42 | 16.55 | 2.00 | 80.3 | 90.0 |
| Bench 2 | Autosub In | Antonee Robinson | DEF | 10 | 4.6 | 2.90 | 8.28 | 13.40 | 6.00 | 75.3 | 90.0 |
| Bench 4 | Bench | Kyle Walker | DEF | 13 | 5.3 | 0.99 | 2.99 | 5.70 | 0.00 | 15.5 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.42 | 13.08 | 19.91 | 12.00 | 76.2 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.1 | 3.84 | 11.30 | 18.58 | 7.00 | 68.9 | 90.0 |
| Bench 3 | Autosub In | Carlton Morris | FWD | 12 | 5.0 | 2.53 | 8.26 | 13.65 | 2.00 | 73.5 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.0 | 6.87 | 18.64 | 28.84 | 2.00 | 86.8 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 5.8 | 6.10 | 16.33 | 25.13 | 26.00 | 89.7 | 79.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.7 | 5.44 | 14.80 | 24.17 | 2.00 | 71.8 | 90.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.7 | 3.48 | 11.11 | 18.74 | 0.00 | 63.3 | 0.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.0 | 3.40 | 10.41 | 17.85 | 0.00 | 41.5 | 0.0 |

## GW34

- Train rows: 129378
- Bank: 0.90 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 66.82
- Actual score: 76.00
- Transfer: Jarrod Bowen -> Bruno Borges Fernandes (projected gain 6.00, hit 0)
- Autosub: Antonee Robinson replaced Cole Palmer.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 2.89 | 8.84 | 14.68 | 2.00 | 85.3 | 90.0 |
| Bench 1 | Bench | Alphonse Areola | GK | 19 | 4.2 | 0.89 | 3.09 | 6.09 | 0.00 | 17.0 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 5.51 | 13.31 | 20.75 | 14.00 | 117.2 | 180.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 5.30 | 12.48 | 18.95 | 12.00 | 113.9 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.6 | 5.25 | 12.10 | 18.61 | 2.00 | 115.0 | 180.0 |
| Bench 2 | Autosub In | Antonee Robinson | DEF | 10 | 4.6 | 2.87 | 8.41 | 13.79 | 1.00 | 75.9 | 90.0 |
| Bench 4 | Bench | Kyle Walker | DEF | 13 | 5.3 | 0.76 | 2.57 | 4.55 | 14.00 | 11.7 | 78.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.1 | 6.05 | 14.79 | 23.27 | 8.00 | 124.0 | 176.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 5.11 | 14.58 | 23.02 | 2.00 | 83.8 | 90.0 |
| XI | XI | Carlton Morris | FWD | 12 | 4.9 | 2.88 | 7.94 | 12.93 | 2.00 | 74.0 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.0 | 8.01 | 20.30 | 31.76 | 3.00 | 120.3 | 106.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.8 | 7.67 | 18.56 | 28.36 | 9.00 | 122.9 | 171.0 |
| XI | Bench | Cole Palmer | MID | 7 | 5.9 | 4.80 | 16.02 | 25.24 | 0.00 | 84.3 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 5.33 | 14.36 | 23.18 | 18.00 | 97.4 | 90.0 |
| Bench 3 | Bench | Phil Foden | MID | 13 | 7.9 | 2.39 | 8.73 | 15.73 | 16.00 | 30.3 | 71.0 |

## GW35

- Train rows: 130234
- Bank: 0.30 -> 0.30
- Free transfers: 2 -> 2
- Captain: Alexander Isak
- Vice captain: Bruno Borges Fernandes
- Effective captain: Alexander Isak
- Chip used: bench_boost
- Predicted score: 72.97
- Actual score: 84.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.03) beats the best remaining Bench Boost opportunity (18.18).
- Transfer: Bernd Leno -> Jordan Pickford (projected gain 2.48, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.03) beats the best remaining Bench Boost opportunity (18.18).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.7 | 3.72 | 10.85 | 17.45 | 10.00 | 112.2 | 90.0 |
| Bench 1 | Bench Boost | Alphonse Areola | GK | 19 | 4.2 | 0.82 | 2.92 | 5.48 | 1.00 | 16.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 4.86 | 14.13 | 22.41 | 1.00 | 115.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.67 | 13.35 | 20.83 | 1.00 | 111.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.6 | 4.03 | 11.61 | 18.34 | 1.00 | 101.8 | 90.0 |
| Bench 2 | Bench Boost | Antonee Robinson | DEF | 10 | 4.6 | 2.96 | 7.99 | 12.97 | 2.00 | 73.8 | 90.0 |
| Bench 4 | Bench Boost | Kyle Walker | DEF | 13 | 5.3 | 2.41 | 6.49 | 10.36 | 8.00 | 45.1 | 90.0 |
| Captain | Captain | Alexander Isak | FWD | 15 | 8.0 | 7.50 | 17.26 | 27.30 | 13.00 | 104.9 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.69 | 13.64 | 21.45 | 2.00 | 94.9 | 90.0 |
| Bench 3 | Bench Boost | Carlton Morris | FWD | 12 | 4.8 | 2.87 | 8.03 | 13.21 | 7.00 | 75.6 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 6.12 | 17.42 | 28.05 | 4.00 | 111.2 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.8 | 5.96 | 17.22 | 27.48 | 12.00 | 93.2 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.9 | 5.25 | 14.97 | 24.19 | 8.00 | 79.4 | 180.0 |
| XI | XI | Mohamed Salah | MID | 11 | 13.0 | 4.73 | 14.71 | 24.71 | 1.00 | 52.1 | 11.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 4.87 | 14.06 | 22.85 | 0.00 | 70.2 | 0.0 |

## GW36

- Train rows: 131093
- Bank: 0.30 -> 0.60
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Bukayo Saka
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 57.15
- Actual score: 69.00
- Transfer: Phil Foden -> Luis Díaz (projected gain 2.22, hit 0)
- Autosub: Kyle Walker replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.7 | 3.91 | 10.67 | 17.14 | 3.00 | 94.1 | 90.0 |
| Bench 1 | Bench | Alphonse Areola | GK | 19 | 4.2 | 1.90 | 5.50 | 9.02 | 3.00 | 51.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 4.33 | 12.03 | 19.57 | 6.00 | 95.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.91 | 10.97 | 17.69 | 7.00 | 89.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.6 | 3.41 | 9.73 | 15.75 | 1.00 | 80.9 | 90.0 |
| Bench 2 | Autosub In | Kyle Walker | DEF | 13 | 5.4 | 2.91 | 7.57 | 11.85 | 2.00 | 54.8 | 90.0 |
| Bench 4 | Bench | Antonee Robinson | DEF | 10 | 4.6 | 2.61 | 7.47 | 12.18 | 7.00 | 74.4 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.1 | 5.19 | 15.66 | 23.88 | 7.00 | 81.1 | 76.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.1 | 3.32 | 11.37 | 18.81 | 2.00 | 79.6 | 90.0 |
| Bench 3 | Bench | Carlton Morris | FWD | 12 | 4.8 | 2.77 | 7.94 | 12.89 | 2.00 | 75.9 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 5.9 | 6.98 | 19.67 | 30.41 | 8.00 | 109.7 | 88.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.8 | 6.38 | 17.90 | 28.95 | 10.00 | 93.1 | 85.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.4 | 5.21 | 15.65 | 25.82 | 0.00 | 78.8 | 0.0 |
| XI | XI | Mohamed Salah | MID | 11 | 13.0 | 3.48 | 12.06 | 21.75 | 13.00 | 26.4 | 90.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 4.05 | 11.94 | 19.50 | 2.00 | 60.6 | 74.0 |

## GW37

- Train rows: 131952
- Bank: 0.60 -> 0.60
- Free transfers: 2 -> 2
- Captain: Nicolas Jackson
- Vice captain: Alexander Isak
- Effective captain: Nicolas Jackson
- Chip used: triple_captain
- Predicted score: 69.72
- Actual score: 87.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (11.76) beats the best remaining Triple Captain opportunity (7.21).
- Transfer: Dominic Solanke -> Nicolas Jackson (projected gain 7.76, hit 0)
- Chip used: Triple Captain on Nicolas Jackson. Optimizer chose Triple Captain here because the current estimated captain upside (11.76) beats the best remaining Triple Captain opportunity (7.21).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.7 | 4.11 | 10.86 | 17.30 | 8.00 | 86.7 | 90.0 |
| Bench 1 | Bench | Alphonse Areola | GK | 19 | 4.2 | 2.46 | 6.46 | 10.31 | 2.00 | 66.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 3.98 | 11.77 | 19.29 | 9.00 | 90.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.58 | 10.59 | 17.22 | 7.00 | 84.5 | 90.0 |
| Bench 2 | Bench | Virgil van Dijk | DEF | 11 | 6.6 | 2.87 | 8.92 | 14.69 | 1.00 | 76.7 | 90.0 |
| XI | XI | Kyle Walker | DEF | 13 | 5.5 | 3.74 | 8.66 | 13.05 | 13.00 | 87.1 | 158.0 |
| Bench 4 | Bench | Antonee Robinson | DEF | 10 | 4.5 | 2.11 | 7.15 | 11.89 | -1.00 | 74.2 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 8.1 | 7.31 | 18.15 | 27.63 | 4.00 | 114.1 | 157.0 |
| Captain | Captain | Nicolas Jackson | FWD | 7 | 7.0 | 7.51 | 17.11 | 25.69 | 7.00 | 141.2 | 179.0 |
| Bench 3 | Bench | Carlton Morris | FWD | 12 | 4.7 | 2.71 | 7.66 | 12.46 | 1.00 | 68.2 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.9 | 7.27 | 18.15 | 28.92 | 14.00 | 119.9 | 180.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.7 | 5.46 | 16.49 | 27.42 | 2.00 | 70.4 | 81.0 |
| XI | XI | Mohamed Salah | MID | 11 | 12.9 | 4.59 | 15.75 | 26.83 | 2.00 | 60.5 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.80 | 12.51 | 21.03 | 5.00 | 69.3 | 89.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.6 | 3.36 | 10.82 | 17.86 | 2.00 | 56.1 | 75.0 |

## GW38

- Train rows: 132813
- Bank: 0.60 -> 2.00
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 65.02
- Actual score: 45.00
- Transfer: Virgil van Dijk -> Joško Gvardiol (projected gain 5.40, hit 0)
- Autosub: Gabriel dos Santos Magalhães replaced Bukayo Saka.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.7 | 2.05 | 8.15 | 14.13 | 1.00 | 82.1 | 90.0 |
| Bench 1 | Bench | Alphonse Areola | GK | 19 | 4.2 | 1.96 | 6.24 | 9.93 | 4.00 | 73.4 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.2 | 6.26 | 16.28 | 24.99 | 2.00 | 107.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 4.28 | 11.99 | 19.94 | 2.00 | 92.2 | 90.0 |
| XI | XI | Kyle Walker | DEF | 13 | 5.5 | 4.14 | 11.04 | 16.96 | 2.00 | 81.3 | 90.0 |
| Bench 2 | Autosub In | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.93 | 10.93 | 18.06 | 1.00 | 88.6 | 58.0 |
| Bench 4 | Bench | Antonee Robinson | DEF | 10 | 4.5 | 2.59 | 7.28 | 12.01 | 0.00 | 75.8 | 78.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.1 | 5.03 | 16.82 | 26.40 | 14.00 | 90.8 | 80.0 |
| XI | XI | Nicolas Jackson | FWD | 7 | 7.0 | 6.06 | 16.75 | 25.41 | 2.00 | 110.3 | 90.0 |
| Bench 3 | Bench | Carlton Morris | FWD | 12 | 4.7 | 2.78 | 7.69 | 12.53 | 5.00 | 75.4 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 5.9 | 8.43 | 23.19 | 36.61 | 6.00 | 139.2 | 88.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.9 | 6.51 | 18.13 | 29.85 | 6.00 | 85.9 | 90.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 8.7 | 5.58 | 16.34 | 27.36 | 0.00 | 74.1 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.19 | 13.65 | 23.67 | 0.00 | 64.2 | 59.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.6 | 4.06 | 11.00 | 18.44 | 3.00 | 61.5 | 70.0 |