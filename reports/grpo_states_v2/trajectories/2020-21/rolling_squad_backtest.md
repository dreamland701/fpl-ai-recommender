# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2020-21 GW1-GW1
- Simulated weeks: GW2-GW38
- Total predicted points: 2153.59
- Total actual points: 2109.00
- Average predicted points: 58.21
- Average actual points: 57.00
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW1 are included before the first simulated week.
- League-average scores were not available for this run.

## GW2

- Train rows: 28570
- Bank: 100.00 -> 0.20
- Free transfers: 1 -> 2
- Captain: Timothy Castagne
- Vice captain: Gabriel Magalhães
- Effective captain: Timothy Castagne
- Chip used: none
- Predicted score: 52.56
- Actual score: 81.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Tyrick Mitchell replaced Billy Sharp.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Kasper Schmeichel | GK | 9 | 5.5 | 4.03 | 10.86 | 17.80 | 2.00 | 100.1 | 90.0 |
| Bench 1 | Bench | Rui Pedro dos Santos Patrício | GK | 20 | 5.5 | 3.55 | 10.17 | 16.45 | 3.00 | 100.7 | 90.0 |
| Captain | Captain | Timothy Castagne | DEF | 9 | 5.5 | 5.23 | 12.33 | 19.62 | 9.00 | 113.1 | 90.0 |
| Vice Captain | XI | Gabriel Magalhães | DEF | 1 | 5.0 | 4.85 | 11.75 | 18.88 | 2.00 | 103.4 | 90.0 |
| Bench 2 | Autosub In | Tyrick Mitchell | DEF | 6 | 4.0 | 3.70 | 11.27 | 17.59 | 5.00 | 112.2 | 90.0 |
| XI | XI | James Justin | DEF | 9 | 4.6 | 3.95 | 11.14 | 17.54 | 7.00 | 105.2 | 90.0 |
| Bench 4 | Bench | Romain Saïss | DEF | 20 | 5.0 | 3.22 | 9.85 | 16.23 | 1.00 | 101.3 | 90.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 7 | 7.1 | 4.03 | 11.02 | 17.06 | 17.00 | 85.7 | 70.0 |
| XI | Bench | Billy Sharp | FWD | 15 | 6.0 | 3.97 | 10.96 | 17.45 | 0.00 | 101.5 | 0.0 |
| XI | XI | Jordan Ayew | FWD | 6 | 6.0 | 3.77 | 10.70 | 17.80 | 5.00 | 100.7 | 80.0 |
| XI | XI | Mohamed Salah | MID | 11 | 12.0 | 4.82 | 21.79 | 43.79 | 3.00 | 38.3 | 90.0 |
| XI | XI | Pierre-Emerick Aubameyang | MID | 1 | 12.0 | 4.24 | 12.91 | 22.96 | 5.00 | 67.4 | 90.0 |
| XI | XI | Willian Borges Da Silva | MID | 1 | 8.1 | 4.24 | 12.24 | 19.16 | 2.00 | 78.3 | 63.0 |
| XI | XI | Wilfried Zaha | MID | 6 | 7.0 | 4.20 | 12.18 | 19.54 | 15.00 | 109.3 | 90.0 |
| Bench 3 | Bench | Adama Traoré | MID | 20 | 6.5 | 3.70 | 10.75 | 18.37 | 2.00 | 94.9 | 90.0 |

## GW3

- Train rows: 29109
- Bank: 0.20 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: James Rodríguez
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 46.29
- Actual score: 31.00
- Transfer: Willian Borges Da Silva -> James Rodríguez (projected gain 8.02, hit 0)
- Autosub: Jordan Ayew replaced Gabriel Magalhães.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Rui Pedro dos Santos Patrício | GK | 20 | 5.5 | 2.58 | 7.80 | 12.47 | 1.00 | 79.7 | 90.0 |
| Bench 1 | Bench | Kasper Schmeichel | GK | 9 | 5.5 | 2.25 | 7.58 | 13.07 | 2.00 | 74.0 | 90.0 |
| XI | XI | Tyrick Mitchell | DEF | 6 | 4.0 | 3.13 | 11.00 | 16.64 | 1.00 | 82.4 | 90.0 |
| Bench 3 | Bench | James Justin | DEF | 9 | 4.6 | 2.60 | 10.05 | 15.14 | 1.00 | 71.9 | 90.0 |
| XI | XI | Timothy Castagne | DEF | 9 | 5.5 | 3.04 | 9.61 | 15.91 | 4.00 | 84.5 | 90.0 |
| XI | XI | Romain Saïss | DEF | 20 | 5.0 | 2.82 | 9.55 | 14.95 | 0.00 | 80.2 | 90.0 |
| XI | Bench | Gabriel Magalhães | DEF | 1 | 5.0 | 3.09 | 9.06 | 14.79 | 0.00 | 73.3 | 0.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 7 | 7.2 | 4.24 | 15.83 | 22.65 | 6.00 | 72.5 | 90.0 |
| Bench 2 | Autosub In | Jordan Ayew | FWD | 6 | 5.9 | 2.68 | 7.73 | 12.55 | 2.00 | 63.4 | 81.0 |
| Bench 4 | Bench | Billy Sharp | FWD | 15 | 5.9 | 0.97 | 2.87 | 4.89 | 1.00 | 19.7 | 16.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.0 | 5.80 | 20.00 | 34.64 | 5.00 | 73.3 | 90.0 |
| Vice Captain | XI | James Rodríguez | MID | 7 | 7.6 | 4.81 | 15.74 | 23.63 | 2.00 | 92.6 | 85.0 |
| XI | XI | Wilfried Zaha | MID | 6 | 7.0 | 3.93 | 12.73 | 19.77 | 1.00 | 91.6 | 90.0 |
| XI | XI | Pierre-Emerick Aubameyang | MID | 1 | 11.9 | 4.04 | 9.93 | 18.32 | 2.00 | 57.3 | 90.0 |
| XI | XI | Adama Traoré | MID | 20 | 6.5 | 3.01 | 8.70 | 14.24 | 2.00 | 73.7 | 61.0 |

## GW4

- Train rows: 29663
- Bank: 0.70 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Dominic Calvert-Lewin
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 53.67
- Actual score: 72.00
- Transfer: Billy Sharp -> Patrick Bamford (projected gain 3.48, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Kasper Schmeichel | GK | 9 | 5.5 | 2.72 | 8.86 | 14.44 | 2.00 | 77.5 | 90.0 |
| XI | XI | Rui Pedro dos Santos Patrício | GK | 20 | 5.5 | 3.06 | 8.00 | 12.35 | 6.00 | 76.4 | 90.0 |
| XI | XI | Timothy Castagne | DEF | 9 | 5.6 | 3.76 | 12.03 | 18.48 | 1.00 | 82.1 | 90.0 |
| XI | XI | James Justin | DEF | 9 | 4.6 | 3.08 | 9.98 | 15.92 | 1.00 | 70.1 | 90.0 |
| Bench 2 | Bench | Tyrick Mitchell | DEF | 6 | 4.0 | 2.91 | 9.46 | 14.84 | 0.00 | 73.6 | 90.0 |
| XI | XI | Romain Saïss | DEF | 20 | 5.0 | 3.19 | 8.33 | 13.09 | 8.00 | 64.8 | 90.0 |
| Bench 4 | Bench | Gabriel Magalhães | DEF | 1 | 5.0 | 1.73 | 4.74 | 7.79 | 2.00 | 27.8 | 90.0 |
| Vice Captain | XI | Dominic Calvert-Lewin | FWD | 7 | 7.3 | 5.94 | 18.58 | 28.29 | 6.00 | 82.0 | 90.0 |
| XI | XI | Patrick Bamford | FWD | 10 | 5.8 | 4.46 | 12.83 | 19.27 | 1.00 | 66.7 | 90.0 |
| Bench 3 | Bench | Jordan Ayew | FWD | 6 | 5.9 | 2.56 | 7.85 | 12.25 | 2.00 | 65.2 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.1 | 6.11 | 18.99 | 30.44 | 13.00 | 89.5 | 90.0 |
| XI | XI | Pierre-Emerick Aubameyang | MID | 1 | 11.9 | 5.75 | 18.34 | 29.60 | 2.00 | 95.4 | 90.0 |
| XI | XI | James Rodríguez | MID | 7 | 7.6 | 4.94 | 14.62 | 22.09 | 18.00 | 70.4 | 77.0 |
| XI | XI | Wilfried Zaha | MID | 6 | 7.1 | 4.13 | 12.64 | 19.53 | 2.00 | 73.3 | 90.0 |
| XI | XI | Adama Traoré | MID | 20 | 6.5 | 3.14 | 8.87 | 13.98 | 1.00 | 61.0 | 8.0 |

## GW5

- Train rows: 30225
- Bank: 0.70 -> 0.00
- Free transfers: 2 -> 2
- Captain: Dominic Calvert-Lewin
- Vice captain: Mohamed Salah
- Effective captain: Dominic Calvert-Lewin
- Chip used: none
- Predicted score: 55.03
- Actual score: 52.00
- Transfer: Adama Traoré -> Jack Grealish (projected gain 5.38, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Kasper Schmeichel | GK | 9 | 5.5 | 2.75 | 8.32 | 13.40 | 3.00 | 76.9 | 90.0 |
| Bench 1 | Bench | Rui Pedro dos Santos Patrício | GK | 20 | 5.5 | 2.63 | 7.82 | 12.02 | 6.00 | 80.9 | 90.0 |
| XI | XI | Timothy Castagne | DEF | 9 | 5.6 | 3.90 | 11.04 | 17.34 | 1.00 | 79.4 | 90.0 |
| XI | XI | Romain Saïss | DEF | 20 | 5.0 | 3.03 | 9.18 | 14.68 | 7.00 | 80.8 | 90.0 |
| Bench 3 | Bench | Tyrick Mitchell | DEF | 6 | 4.0 | 2.88 | 8.72 | 14.05 | 1.00 | 77.1 | 90.0 |
| XI | XI | James Justin | DEF | 9 | 4.6 | 3.06 | 8.48 | 13.67 | 2.00 | 70.6 | 90.0 |
| Bench 4 | Bench | Gabriel Magalhães | DEF | 1 | 5.0 | 2.07 | 7.03 | 10.76 | 2.00 | 65.6 | 90.0 |
| Captain | Captain | Dominic Calvert-Lewin | FWD | 7 | 7.3 | 6.46 | 17.55 | 28.08 | 6.00 | 84.5 | 90.0 |
| XI | XI | Patrick Bamford | FWD | 10 | 5.8 | 4.47 | 11.17 | 17.49 | 2.00 | 66.6 | 90.0 |
| Bench 2 | Bench | Jordan Ayew | FWD | 6 | 5.8 | 3.10 | 8.49 | 12.77 | 0.00 | 69.7 | 0.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.1 | 6.37 | 18.94 | 28.84 | 7.00 | 90.9 | 90.0 |
| XI | XI | James Rodríguez | MID | 7 | 7.7 | 5.77 | 17.06 | 26.94 | 4.00 | 97.2 | 90.0 |
| XI | XI | Jack Grealish | MID | 2 | 7.1 | 4.37 | 13.79 | 21.11 | 3.00 | 94.0 | 90.0 |
| XI | XI | Pierre-Emerick Aubameyang | MID | 1 | 11.8 | 4.12 | 12.27 | 19.26 | 2.00 | 70.2 | 90.0 |
| XI | XI | Wilfried Zaha | MID | 6 | 7.1 | 4.26 | 10.94 | 16.61 | 9.00 | 68.6 | 90.0 |

## GW6

- Train rows: 30808
- Bank: 0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Dominic Calvert-Lewin
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 57.84
- Actual score: 58.00
- Transfer: Kasper Schmeichel -> Emiliano Martínez (projected gain 1.70, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez | GK | 2 | 4.8 | 3.70 | 10.57 | 17.46 | 3.00 | 84.4 | 90.0 |
| Bench 1 | Bench | Rui Pedro dos Santos Patrício | GK | 20 | 5.5 | 3.34 | 8.91 | 13.23 | 2.00 | 83.3 | 90.0 |
| XI | XI | Romain Saïss | DEF | 20 | 5.1 | 4.13 | 10.96 | 16.56 | 7.00 | 85.2 | 67.0 |
| XI | XI | Timothy Castagne | DEF | 9 | 5.6 | 3.33 | 10.11 | 15.16 | 6.00 | 76.4 | 90.0 |
| XI | XI | Tyrick Mitchell | DEF | 6 | 4.1 | 3.11 | 8.92 | 13.99 | 2.00 | 79.7 | 90.0 |
| Bench 3 | Bench | James Justin | DEF | 9 | 4.7 | 2.45 | 8.02 | 12.82 | 6.00 | 76.3 | 90.0 |
| Bench 2 | Bench | Gabriel Magalhães | DEF | 1 | 5.0 | 2.64 | 7.79 | 11.99 | 2.00 | 69.9 | 90.0 |
| Vice Captain | XI | Dominic Calvert-Lewin | FWD | 7 | 7.4 | 6.03 | 17.18 | 26.07 | 1.00 | 88.6 | 90.0 |
| XI | XI | Patrick Bamford | FWD | 10 | 5.8 | 3.71 | 10.91 | 17.00 | 17.00 | 72.7 | 90.0 |
| Bench 4 | Bench | Jordan Ayew | FWD | 6 | 5.8 | 1.53 | 4.02 | 6.01 | 0.00 | 26.8 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.1 | 6.80 | 18.88 | 28.02 | 2.00 | 89.5 | 90.0 |
| XI | XI | Pierre-Emerick Aubameyang | MID | 1 | 11.8 | 4.74 | 14.52 | 23.63 | 2.00 | 86.5 | 90.0 |
| XI | XI | Jack Grealish | MID | 2 | 7.1 | 5.59 | 13.83 | 20.68 | 1.00 | 83.1 | 90.0 |
| XI | XI | James Rodríguez | MID | 7 | 7.8 | 5.46 | 13.57 | 19.99 | 2.00 | 72.7 | 90.0 |
| XI | XI | Wilfried Zaha | MID | 6 | 7.1 | 4.45 | 12.74 | 19.49 | 13.00 | 85.9 | 90.0 |

## GW7

- Train rows: 31398
- Bank: 0.70 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Patrick Bamford
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 57.21
- Actual score: 66.00
- Transfer: Timothy Castagne -> Benjamin Chilwell (projected gain 3.49, hit 0)
- Autosub: Gabriel Magalhães replaced Romain Saïss.
- Autosub: Jordan Ayew replaced James Rodríguez.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez | GK | 2 | 4.8 | 3.38 | 10.35 | 15.23 | 0.00 | 81.3 | 90.0 |
| Bench 1 | Bench | Rui Pedro dos Santos Patrício | GK | 20 | 5.5 | 3.32 | 8.38 | 13.54 | 6.00 | 82.0 | 90.0 |
| XI | XI | Benjamin Chilwell | DEF | 5 | 5.8 | 4.61 | 12.21 | 18.11 | 6.00 | 86.3 | 90.0 |
| XI | Bench | Romain Saïss | DEF | 20 | 5.1 | 3.98 | 10.05 | 15.90 | 0.00 | 78.4 | 0.0 |
| XI | XI | James Justin | DEF | 9 | 4.7 | 3.31 | 9.05 | 14.63 | 2.00 | 85.1 | 90.0 |
| Bench 2 | Bench | Tyrick Mitchell | DEF | 6 | 4.1 | 2.84 | 8.36 | 13.60 | 0.00 | 79.4 | 0.0 |
| Bench 3 | Autosub In | Gabriel Magalhães | DEF | 1 | 5.0 | 2.58 | 7.28 | 11.74 | 7.00 | 76.0 | 90.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 7 | 7.4 | 5.25 | 15.63 | 23.20 | 8.00 | 82.4 | 90.0 |
| Vice Captain | XI | Patrick Bamford | FWD | 10 | 5.8 | 5.26 | 14.88 | 22.36 | 2.00 | 100.0 | 90.0 |
| Bench 4 | Autosub In | Jordan Ayew | FWD | 6 | 5.7 | 1.00 | 3.10 | 4.90 | 1.00 | 20.2 | 18.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.2 | 6.03 | 17.48 | 28.56 | 8.00 | 92.4 | 89.0 |
| XI | XI | Wilfried Zaha | MID | 6 | 7.1 | 4.87 | 13.88 | 21.57 | 1.00 | 92.9 | 90.0 |
| XI | Bench | James Rodríguez | MID | 7 | 7.8 | 5.08 | 13.88 | 20.56 | 0.00 | 77.2 | 0.0 |
| XI | XI | Jack Grealish | MID | 2 | 7.2 | 5.08 | 13.51 | 18.77 | 15.00 | 75.7 | 90.0 |
| XI | XI | Pierre-Emerick Aubameyang | MID | 1 | 11.7 | 4.31 | 13.37 | 21.75 | 8.00 | 84.3 | 86.0 |

## GW8

- Train rows: 31995
- Bank: 0.50 -> 0.30
- Free transfers: 2 -> 2
- Captain: Pierre-Emerick Aubameyang
- Vice captain: Mohamed Salah
- Effective captain: Pierre-Emerick Aubameyang
- Chip used: none
- Predicted score: 55.93
- Actual score: 63.00
- Transfer: Romain Saïss -> Kurt Zouma (projected gain 5.02, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Rui Pedro dos Santos Patrício | GK | 20 | 5.5 | 2.84 | 8.33 | 13.76 | 10.00 | 85.7 | 90.0 |
| Bench 1 | Bench | Emiliano Martínez | GK | 2 | 4.8 | 2.72 | 8.26 | 14.24 | 6.00 | 80.8 | 90.0 |
| XI | XI | Benjamin Chilwell | DEF | 5 | 5.8 | 4.86 | 13.53 | 18.34 | 8.00 | 83.2 | 90.0 |
| XI | XI | Kurt Zouma | DEF | 5 | 5.3 | 4.38 | 12.26 | 18.60 | 2.00 | 97.0 | 90.0 |
| XI | XI | James Justin | DEF | 9 | 4.7 | 3.39 | 8.45 | 14.42 | 6.00 | 82.7 | 90.0 |
| XI | XI | Gabriel Magalhães | DEF | 1 | 5.0 | 3.34 | 8.17 | 13.17 | 1.00 | 81.3 | 90.0 |
| Bench 4 | Bench | Tyrick Mitchell | DEF | 6 | 4.1 | 1.47 | 4.06 | 7.29 | 0.00 | 34.6 | 0.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 7 | 7.4 | 5.26 | 15.11 | 24.97 | 5.00 | 95.3 | 90.0 |
| XI | XI | Patrick Bamford | FWD | 10 | 5.9 | 5.00 | 13.10 | 18.81 | 7.00 | 76.4 | 90.0 |
| Bench 3 | Bench | Jordan Ayew | FWD | 6 | 5.7 | 1.66 | 4.41 | 7.58 | 8.00 | 33.3 | 84.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.2 | 5.51 | 17.28 | 29.19 | 9.00 | 96.4 | 90.0 |
| XI | XI | Jack Grealish | MID | 2 | 7.2 | 5.02 | 15.65 | 22.89 | 6.00 | 94.1 | 90.0 |
| Captain | Captain | Pierre-Emerick Aubameyang | MID | 1 | 11.7 | 5.52 | 15.04 | 24.38 | 2.00 | 93.4 | 90.0 |
| XI | XI | Wilfried Zaha | MID | 6 | 7.2 | 5.28 | 13.50 | 20.78 | 5.00 | 81.4 | 90.0 |
| Bench 2 | Bench | James Rodríguez | MID | 7 | 7.7 | 2.41 | 7.80 | 12.54 | 2.00 | 33.4 | 79.0 |

## GW9

- Train rows: 32595
- Bank: 0.30 -> 0.60
- Free transfers: 2 -> 2
- Captain: Jack Grealish
- Vice captain: Dominic Calvert-Lewin
- Effective captain: Jack Grealish
- Chip used: none
- Predicted score: 58.17
- Actual score: 40.00
- Transfer: Gabriel Magalhães -> Jannik Vestergaard (projected gain 1.15, hit 0)
- Autosub: James Justin replaced Wilfried Zaha.
- Autosub: Jordan Ayew replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez | GK | 2 | 4.8 | 3.58 | 10.32 | 16.69 | 1.00 | 91.8 | 90.0 |
| Bench 1 | Bench | Rui Pedro dos Santos Patrício | GK | 20 | 5.5 | 3.26 | 9.22 | 14.77 | 2.00 | 87.4 | 90.0 |
| XI | XI | Benjamin Chilwell | DEF | 5 | 5.9 | 4.87 | 13.92 | 20.26 | 7.00 | 91.7 | 81.0 |
| XI | XI | Kurt Zouma | DEF | 5 | 5.3 | 4.27 | 11.58 | 17.90 | 6.00 | 82.2 | 90.0 |
| XI | XI | Jannik Vestergaard | DEF | 16 | 4.7 | 3.64 | 10.42 | 15.14 | 2.00 | 90.8 | 90.0 |
| Bench 2 | Autosub In | James Justin | DEF | 9 | 4.7 | 3.34 | 9.33 | 15.62 | 0.00 | 88.3 | 90.0 |
| Bench 4 | Bench | Tyrick Mitchell | DEF | 6 | 4.0 | 1.37 | 3.60 | 6.38 | 0.00 | 25.8 | 0.0 |
| Vice Captain | XI | Dominic Calvert-Lewin | FWD | 7 | 7.4 | 5.93 | 16.15 | 26.32 | 13.00 | 100.1 | 90.0 |
| XI | XI | Patrick Bamford | FWD | 10 | 5.9 | 5.46 | 13.97 | 21.43 | 2.00 | 89.6 | 90.0 |
| Bench 3 | Autosub In | Jordan Ayew | FWD | 6 | 5.7 | 2.66 | 6.94 | 11.07 | 2.00 | 60.5 | 76.0 |
| Captain | Captain | Jack Grealish | MID | 2 | 7.3 | 6.02 | 17.27 | 26.27 | 1.00 | 101.8 | 90.0 |
| XI | Bench | Wilfried Zaha | MID | 6 | 7.2 | 5.52 | 14.57 | 22.79 | 0.00 | 88.5 | 0.0 |
| XI | XI | Pierre-Emerick Aubameyang | MID | 1 | 11.7 | 4.83 | 14.07 | 22.86 | 3.00 | 86.9 | 90.0 |
| XI | XI | James Rodríguez | MID | 7 | 7.7 | 4.09 | 12.26 | 19.46 | 2.00 | 79.7 | 73.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 12.1 | 3.94 | 11.65 | 21.24 | 0.00 | 57.0 | 0.0 |

## GW10

- Train rows: 33196
- Bank: 0.60 -> 1.00
- Free transfers: 2 -> 2
- Captain: Dominic Calvert-Lewin
- Vice captain: Jack Grealish
- Effective captain: Dominic Calvert-Lewin
- Chip used: none
- Predicted score: 58.84
- Actual score: 50.00
- Transfer: Wilfried Zaha -> Diogo Jota (projected gain 4.98, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez | GK | 2 | 4.8 | 3.09 | 9.70 | 16.45 | 1.00 | 89.1 | 90.0 |
| Bench 1 | Bench | Rui Pedro dos Santos Patrício | GK | 20 | 5.5 | 2.80 | 8.38 | 14.07 | 2.00 | 85.3 | 90.0 |
| XI | XI | Benjamin Chilwell | DEF | 5 | 5.9 | 4.56 | 13.18 | 20.48 | 8.00 | 86.1 | 90.0 |
| XI | XI | Kurt Zouma | DEF | 5 | 5.4 | 3.81 | 11.02 | 17.94 | 5.00 | 87.8 | 90.0 |
| XI | XI | James Justin | DEF | 9 | 4.7 | 3.78 | 10.41 | 16.67 | 1.00 | 91.3 | 90.0 |
| Bench 2 | Bench | Jannik Vestergaard | DEF | 16 | 4.7 | 3.34 | 9.68 | 14.64 | 1.00 | 84.5 | 90.0 |
| Bench 4 | Bench | Tyrick Mitchell | DEF | 6 | 4.0 | 1.62 | 4.14 | 6.98 | 0.00 | 24.9 | 0.0 |
| Captain | Captain | Dominic Calvert-Lewin | FWD | 7 | 7.5 | 7.18 | 19.72 | 30.98 | 2.00 | 110.0 | 90.0 |
| XI | XI | Patrick Bamford | FWD | 10 | 5.9 | 4.29 | 12.51 | 19.35 | 2.00 | 79.3 | 90.0 |
| Bench 3 | Bench | Jordan Ayew | FWD | 6 | 5.7 | 2.80 | 7.22 | 11.91 | 2.00 | 60.9 | 65.0 |
| XI | XI | Mohamed Salah | MID | 11 | 12.1 | 5.42 | 16.42 | 27.79 | 6.00 | 62.0 | 63.0 |
| Vice Captain | XI | Jack Grealish | MID | 2 | 7.3 | 5.68 | 15.79 | 24.63 | 10.00 | 84.9 | 90.0 |
| XI | XI | Diogo Jota | MID | 11 | 6.7 | 5.13 | 14.55 | 21.99 | 9.00 | 93.5 | 90.0 |
| XI | XI | Pierre-Emerick Aubameyang | MID | 1 | 11.6 | 5.02 | 14.46 | 23.81 | 2.00 | 89.6 | 90.0 |
| XI | XI | James Rodríguez | MID | 7 | 7.7 | 3.70 | 10.66 | 17.52 | 2.00 | 67.8 | 90.0 |

## GW11

- Train rows: 33799
- Bank: 1.00 -> 1.00
- Free transfers: 2 -> 2
- Captain: Dominic Calvert-Lewin
- Vice captain: Diogo Jota
- Effective captain: Dominic Calvert-Lewin
- Chip used: none
- Predicted score: 58.41
- Actual score: 62.00
- Transfer: Rui Pedro dos Santos Patrício -> Kasper Schmeichel (projected gain 2.10, hit 0)
- Autosub: Jannik Vestergaard replaced Jack Grealish.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Kasper Schmeichel | GK | 9 | 5.5 | 3.67 | 10.28 | 16.08 | 2.00 | 91.4 | 90.0 |
| Bench 1 | Bench | Emiliano Martínez | GK | 2 | 4.8 | 2.76 | 8.19 | 14.43 | 0.00 | 74.2 | 0.0 |
| XI | XI | Benjamin Chilwell | DEF | 5 | 6.0 | 5.09 | 14.32 | 22.40 | 2.00 | 99.8 | 90.0 |
| XI | XI | Kurt Zouma | DEF | 5 | 5.4 | 3.98 | 11.84 | 18.51 | 8.00 | 95.2 | 90.0 |
| XI | XI | James Justin | DEF | 9 | 4.7 | 4.01 | 10.98 | 16.83 | 2.00 | 89.3 | 90.0 |
| Bench 2 | Autosub In | Jannik Vestergaard | DEF | 16 | 4.7 | 3.18 | 8.78 | 13.96 | 9.00 | 88.3 | 90.0 |
| Bench 4 | Bench | Tyrick Mitchell | DEF | 6 | 4.0 | 1.15 | 3.18 | 5.53 | 0.00 | 19.9 | 0.0 |
| Captain | Captain | Dominic Calvert-Lewin | FWD | 7 | 7.5 | 6.20 | 17.13 | 27.83 | 6.00 | 100.9 | 90.0 |
| XI | XI | Patrick Bamford | FWD | 10 | 5.9 | 4.25 | 12.29 | 19.33 | 8.00 | 81.1 | 90.0 |
| Bench 3 | Bench | Jordan Ayew | FWD | 6 | 5.7 | 2.61 | 6.99 | 11.45 | 1.00 | 59.8 | 16.0 |
| Vice Captain | XI | Diogo Jota | MID | 11 | 6.8 | 6.19 | 17.45 | 25.35 | 1.00 | 94.7 | 17.0 |
| XI | XI | Mohamed Salah | MID | 11 | 12.1 | 5.42 | 15.73 | 26.11 | 14.00 | 77.9 | 90.0 |
| XI | XI | Pierre-Emerick Aubameyang | MID | 1 | 11.5 | 4.35 | 13.93 | 22.92 | 2.00 | 86.9 | 90.0 |
| XI | Bench | Jack Grealish | MID | 2 | 7.3 | 4.83 | 13.35 | 21.15 | 0.00 | 72.4 | 0.0 |
| XI | XI | James Rodríguez | MID | 7 | 7.7 | 4.22 | 11.39 | 19.00 | 2.00 | 76.5 | 90.0 |

## GW12

- Train rows: 34403
- Bank: 1.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Dominic Calvert-Lewin
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 56.22
- Actual score: 58.00
- Transfer: Jack Grealish -> Riyad Mahrez (projected gain 4.10, hit 0)
- Autosub: James Justin replaced Diogo Jota.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Kasper Schmeichel | GK | 9 | 5.5 | 3.09 | 8.92 | 14.28 | 7.00 | 86.6 | 90.0 |
| Bench 1 | Bench | Emiliano Martínez | GK | 2 | 4.8 | 1.37 | 4.48 | 8.24 | 11.00 | 36.4 | 90.0 |
| XI | XI | Kurt Zouma | DEF | 5 | 5.5 | 4.33 | 12.31 | 19.46 | 2.00 | 97.6 | 90.0 |
| XI | XI | Benjamin Chilwell | DEF | 5 | 6.0 | 4.13 | 11.72 | 18.77 | 2.00 | 81.5 | 90.0 |
| XI | XI | Jannik Vestergaard | DEF | 16 | 4.7 | 3.59 | 9.91 | 15.14 | 7.00 | 89.6 | 90.0 |
| Bench 2 | Autosub In | James Justin | DEF | 9 | 4.7 | 3.36 | 9.63 | 14.94 | 11.00 | 82.5 | 90.0 |
| Bench 4 | Bench | Tyrick Mitchell | DEF | 6 | 4.0 | 0.90 | 2.67 | 5.06 | 0.00 | 15.2 | 0.0 |
| Vice Captain | XI | Dominic Calvert-Lewin | FWD | 7 | 7.5 | 5.57 | 16.29 | 26.47 | 5.00 | 91.7 | 90.0 |
| XI | XI | Patrick Bamford | FWD | 10 | 6.0 | 5.20 | 14.24 | 22.71 | 5.00 | 96.2 | 73.0 |
| Bench 3 | Bench | Jordan Ayew | FWD | 6 | 5.7 | 1.77 | 5.35 | 8.68 | 0.00 | 35.2 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.1 | 6.34 | 18.83 | 30.46 | 8.00 | 101.0 | 83.0 |
| XI | XI | Pierre-Emerick Aubameyang | MID | 1 | 11.5 | 4.94 | 14.18 | 22.77 | 0.00 | 86.0 | 90.0 |
| XI | XI | Riyad Mahrez | MID | 12 | 8.4 | 4.76 | 13.67 | 20.85 | 3.00 | 68.6 | 65.0 |
| XI | Bench | Diogo Jota | MID | 11 | 6.8 | 4.07 | 11.74 | 17.96 | 0.00 | 41.6 | 0.0 |
| XI | Bench | James Rodríguez | MID | 7 | 7.6 | 3.87 | 10.43 | 18.06 | 0.00 | 70.6 | 0.0 |

## GW13

- Train rows: 35010
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Dominic Calvert-Lewin
- Vice captain: Mohamed Salah
- Effective captain: Dominic Calvert-Lewin
- Chip used: none
- Predicted score: 55.95
- Actual score: 53.00
- Transfer: James Rodríguez -> Wilfried Zaha (projected gain 5.36, hit 0)
- Autosub: Jordan Ayew replaced Riyad Mahrez.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez | GK | 2 | 4.8 | 3.83 | 10.33 | 16.48 | 8.00 | 86.9 | 90.0 |
| Bench 1 | Bench | Kasper Schmeichel | GK | 9 | 5.5 | 2.95 | 9.21 | 15.44 | 2.00 | 91.1 | 90.0 |
| XI | XI | Benjamin Chilwell | DEF | 5 | 6.0 | 4.20 | 12.05 | 19.29 | 5.00 | 87.4 | 90.0 |
| XI | XI | Kurt Zouma | DEF | 5 | 5.5 | 4.22 | 11.60 | 18.46 | 1.00 | 92.6 | 90.0 |
| XI | XI | James Justin | DEF | 9 | 4.7 | 3.55 | 10.28 | 16.74 | 1.00 | 90.1 | 90.0 |
| XI | XI | Jannik Vestergaard | DEF | 16 | 4.8 | 3.38 | 9.96 | 15.85 | 2.00 | 88.4 | 90.0 |
| Bench 4 | Bench | Tyrick Mitchell | DEF | 6 | 4.0 | 0.58 | 2.38 | 4.54 | 0.00 | 14.2 | 0.0 |
| Captain | Captain | Dominic Calvert-Lewin | FWD | 7 | 7.5 | 5.84 | 17.32 | 28.08 | 5.00 | 100.9 | 89.0 |
| XI | XI | Patrick Bamford | FWD | 10 | 6.0 | 5.03 | 13.59 | 21.62 | 6.00 | 82.6 | 83.0 |
| Bench 3 | Autosub In | Jordan Ayew | FWD | 6 | 5.7 | 0.81 | 3.27 | 5.10 | 1.00 | 17.6 | 14.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.1 | 5.76 | 17.79 | 30.04 | 7.00 | 90.0 | 90.0 |
| XI | Bench | Riyad Mahrez | MID | 12 | 8.4 | 5.06 | 13.54 | 21.24 | 0.00 | 71.9 | 0.0 |
| XI | XI | Pierre-Emerick Aubameyang | MID | 1 | 11.5 | 4.84 | 13.48 | 21.89 | 10.00 | 83.8 | 90.0 |
| XI | XI | Wilfried Zaha | MID | 6 | 7.5 | 4.40 | 12.65 | 20.48 | 2.00 | 80.6 | 90.0 |
| Bench 2 | Bench | Diogo Jota | MID | 11 | 6.8 | 0.89 | 2.62 | 4.85 | 0.00 | 0.0 | 0.0 |

## GW14

- Train rows: 35617
- Bank: 0.10 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Dominic Calvert-Lewin
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.88
- Actual score: 75.00
- Transfer: Riyad Mahrez -> Jack Grealish (projected gain 7.36, hit 0)
- Autosub: Jordan Ayew replaced Pierre-Emerick Aubameyang.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez | GK | 2 | 4.8 | 4.05 | 11.05 | 17.55 | 6.00 | 86.3 | 90.0 |
| Bench 1 | Bench | Kasper Schmeichel | GK | 9 | 5.5 | 2.88 | 8.94 | 15.23 | 7.00 | 89.6 | 90.0 |
| XI | XI | Benjamin Chilwell | DEF | 5 | 6.0 | 3.99 | 11.91 | 19.46 | 1.00 | 92.4 | 9.0 |
| XI | XI | Kurt Zouma | DEF | 5 | 5.5 | 3.80 | 10.99 | 17.83 | 6.00 | 94.4 | 90.0 |
| XI | XI | James Justin | DEF | 9 | 4.7 | 3.38 | 9.47 | 15.84 | 8.00 | 83.7 | 90.0 |
| XI | XI | Jannik Vestergaard | DEF | 16 | 4.8 | 3.29 | 9.08 | 15.59 | 2.00 | 87.1 | 90.0 |
| Bench 4 | Bench | Tyrick Mitchell | DEF | 6 | 4.0 | 0.52 | 2.21 | 4.38 | 0.00 | 14.0 | 0.0 |
| Vice Captain | XI | Dominic Calvert-Lewin | FWD | 7 | 7.5 | 5.99 | 17.15 | 27.73 | 4.00 | 100.1 | 90.0 |
| XI | XI | Patrick Bamford | FWD | 10 | 6.0 | 4.60 | 13.05 | 21.03 | 2.00 | 85.0 | 90.0 |
| Bench 3 | Autosub In | Jordan Ayew | FWD | 6 | 5.7 | 1.19 | 4.17 | 7.32 | 2.00 | 28.8 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.2 | 6.49 | 19.54 | 32.95 | 16.00 | 110.7 | 33.0 |
| XI | XI | Jack Grealish | MID | 2 | 7.8 | 5.08 | 13.87 | 21.80 | 10.00 | 77.6 | 90.0 |
| XI | Bench | Pierre-Emerick Aubameyang | MID | 1 | 11.4 | 4.65 | 13.53 | 22.11 | 0.00 | 86.6 | 0.0 |
| XI | XI | Wilfried Zaha | MID | 6 | 7.5 | 4.09 | 12.19 | 21.02 | 2.00 | 79.2 | 90.0 |
| Bench 2 | Bench | Diogo Jota | MID | 11 | 6.7 | 2.07 | 7.18 | 10.24 | 0.00 | 16.3 | 0.0 |

## GW15

- Train rows: 36228
- Bank: 0.70 -> 2.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Heung-Min Son
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 59.08
- Actual score: 32.00
- Transfer: Pierre-Emerick Aubameyang -> Heung-Min Son (projected gain 9.63, hit 0)
- Autosub: Benjamin Chilwell replaced Jannik Vestergaard.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez | GK | 2 | 4.8 | 4.36 | 12.01 | 19.32 | 10.00 | 89.6 | 90.0 |
| Bench 1 | Bench | Kasper Schmeichel | GK | 9 | 5.5 | 3.22 | 9.50 | 15.77 | 1.00 | 89.8 | 90.0 |
| XI | XI | Kurt Zouma | DEF | 5 | 5.6 | 4.04 | 12.06 | 18.97 | 1.00 | 98.1 | 90.0 |
| XI | XI | James Justin | DEF | 9 | 4.7 | 3.75 | 10.59 | 17.20 | 1.00 | 87.9 | 90.0 |
| XI | Bench | Jannik Vestergaard | DEF | 16 | 4.8 | 3.46 | 9.23 | 14.72 | 0.00 | 81.2 | 0.0 |
| Bench 2 | Autosub In | Benjamin Chilwell | DEF | 5 | 5.9 | 1.43 | 4.96 | 9.55 | 1.00 | 26.8 | 90.0 |
| Bench 4 | Bench | Tyrick Mitchell | DEF | 6 | 3.9 | 0.59 | 2.00 | 3.53 | 0.00 | 9.7 | 0.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 7 | 7.5 | 5.86 | 16.39 | 26.42 | 1.00 | 96.7 | 90.0 |
| XI | XI | Patrick Bamford | FWD | 10 | 6.1 | 5.12 | 13.95 | 22.38 | 8.00 | 89.1 | 90.0 |
| XI | Bench | Jordan Ayew | FWD | 6 | 5.7 | 2.27 | 6.12 | 9.73 | 0.00 | 57.2 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.3 | 7.23 | 21.45 | 34.54 | 2.00 | 98.7 | 90.0 |
| Vice Captain | XI | Heung-Min Son | MID | 17 | 9.7 | 5.98 | 17.98 | 29.85 | 3.00 | 102.7 | 83.0 |
| XI | XI | Jack Grealish | MID | 2 | 7.8 | 5.96 | 15.74 | 24.96 | 2.00 | 85.8 | 90.0 |
| XI | XI | Wilfried Zaha | MID | 6 | 7.5 | 3.81 | 11.56 | 18.33 | 1.00 | 75.0 | 90.0 |
| Bench 3 | Bench | Diogo Jota | MID | 11 | 6.7 | 1.19 | 3.48 | 6.28 | 0.00 | 9.9 | 0.0 |

## GW16

- Train rows: 36842
- Bank: 2.40 -> -0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Heung-Min Son
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 58.88
- Actual score: 42.00
- Transfer: Jannik Vestergaard -> Trent Alexander-Arnold (projected gain 8.64, hit 0)
- Autosub: Jordan Ayew replaced Kurt Zouma.
- Autosub: Tyrick Mitchell replaced Heung-Min Son.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez | GK | 2 | 4.9 | 3.71 | 11.66 | 19.14 | 3.00 | 91.4 | 90.0 |
| Bench 1 | Bench | Kasper Schmeichel | GK | 9 | 5.5 | 3.12 | 9.14 | 14.55 | 2.00 | 84.1 | 90.0 |
| XI | XI | Benjamin Chilwell | DEF | 5 | 5.9 | 4.33 | 11.70 | 20.22 | 5.00 | 80.0 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 7.2 | 4.27 | 11.66 | 18.05 | 6.00 | 74.4 | 90.0 |
| XI | Bench | Kurt Zouma | DEF | 5 | 5.6 | 4.13 | 11.63 | 18.34 | 0.00 | 84.8 | 0.0 |
| XI | XI | James Justin | DEF | 9 | 4.8 | 3.60 | 10.37 | 15.77 | 2.00 | 82.3 | 90.0 |
| Bench 4 | Autosub In | Tyrick Mitchell | DEF | 6 | 3.9 | 0.50 | 1.88 | 3.23 | 2.00 | 8.9 | 90.0 |
| XI | XI | Patrick Bamford | FWD | 10 | 6.1 | 5.30 | 15.19 | 23.94 | 8.00 | 92.8 | 90.0 |
| XI | Bench | Dominic Calvert-Lewin | FWD | 7 | 7.5 | 4.86 | 14.62 | 24.47 | 0.00 | 80.2 | 0.0 |
| Bench 2 | Autosub In | Jordan Ayew | FWD | 6 | 5.6 | 0.97 | 3.08 | 5.30 | 1.00 | 21.2 | 6.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.3 | 7.22 | 21.33 | 33.81 | 3.00 | 91.8 | 90.0 |
| Vice Captain | Bench | Heung-Min Son | MID | 17 | 9.7 | 5.34 | 16.71 | 28.30 | 0.00 | 85.9 | 0.0 |
| XI | XI | Jack Grealish | MID | 2 | 7.8 | 5.10 | 13.89 | 22.77 | 2.00 | 77.0 | 90.0 |
| XI | XI | Wilfried Zaha | MID | 6 | 7.5 | 3.81 | 11.66 | 17.89 | 7.00 | 72.9 | 90.0 |
| Bench 3 | Bench | Diogo Jota | MID | 11 | 6.7 | 0.93 | 2.77 | 5.58 | 0.00 | 11.6 | 0.0 |

## GW17

- Train rows: 37458
- Bank: -0.00 -> 0.80
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Patrick Bamford
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 52.54
- Actual score: 39.00
- Transfer: Kurt Zouma -> Stuart Dallas (projected gain 4.97, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez | GK | 2 | 4.9 | 3.49 | 11.74 | 19.05 | 3.00 | 91.4 | 90.0 |
| Bench 1 | Bench | Kasper Schmeichel | GK | 9 | 5.5 | 3.19 | 9.07 | 14.88 | 2.00 | 86.4 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 7.2 | 4.06 | 11.27 | 17.99 | 2.00 | 82.5 | 76.0 |
| XI | XI | Stuart Dallas | DEF | 10 | 4.8 | 3.78 | 11.02 | 16.84 | 1.00 | 89.0 | 90.0 |
| XI | XI | Benjamin Chilwell | DEF | 5 | 5.9 | 3.53 | 10.65 | 17.50 | 1.00 | 84.1 | 90.0 |
| XI | XI | James Justin | DEF | 9 | 4.8 | 3.53 | 10.02 | 15.78 | 1.00 | 84.4 | 90.0 |
| Bench 2 | Bench | Tyrick Mitchell | DEF | 6 | 3.9 | 2.39 | 6.10 | 9.59 | 6.00 | 57.8 | 90.0 |
| Vice Captain | XI | Patrick Bamford | FWD | 10 | 6.2 | 5.25 | 15.66 | 24.63 | 2.00 | 94.3 | 90.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 7 | 7.5 | 3.12 | 10.22 | 18.19 | 2.00 | 48.4 | 78.0 |
| Bench 3 | Bench | Jordan Ayew | FWD | 6 | 5.6 | 1.61 | 4.36 | 7.28 | 1.00 | 30.1 | 42.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.3 | 6.17 | 18.68 | 31.33 | 2.00 | 98.2 | 90.0 |
| XI | XI | Heung-Min Son | MID | 17 | 9.7 | 4.24 | 13.24 | 23.01 | 13.00 | 62.7 | 90.0 |
| XI | XI | Jack Grealish | MID | 2 | 7.7 | 4.51 | 13.14 | 21.20 | 7.00 | 77.1 | 90.0 |
| XI | XI | Wilfried Zaha | MID | 6 | 7.4 | 4.69 | 12.64 | 20.20 | 3.00 | 91.2 | 90.0 |
| Bench 4 | Bench | Diogo Jota | MID | 11 | 6.7 | 0.93 | 2.41 | 5.25 | 0.00 | 14.4 | 0.0 |

## GW18

- Train rows: 38083
- Bank: 0.80 -> 0.20
- Free transfers: 2 -> 2
- Captain: Heung-Min Son
- Vice captain: Kieran Tierney
- Effective captain: Heung-Min Son
- Chip used: none
- Predicted score: 50.69
- Actual score: 16.00
- Transfer: James Justin -> Kieran Tierney (projected gain 6.51, hit 0)
- Autosub: Jordan Ayew replaced Kieran Tierney.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Emiliano Martínez | GK | 2 | 4.9 | 2.93 | 9.31 | 15.93 | 0.00 | 75.6 | 0.0 |
| Bench 1 | Bench | Kasper Schmeichel | GK | 9 | 5.5 | 2.21 | 7.20 | 12.26 | 0.00 | 68.0 | 0.0 |
| Vice Captain | Bench | Kieran Tierney | DEF | 1 | 5.4 | 5.48 | 14.48 | 22.24 | 0.00 | 117.4 | 0.0 |
| XI | XI | Tyrick Mitchell | DEF | 6 | 3.9 | 3.04 | 9.09 | 14.56 | 8.00 | 83.0 | 90.0 |
| XI | Bench | Benjamin Chilwell | DEF | 5 | 5.9 | 2.90 | 9.01 | 15.10 | 0.00 | 68.4 | 0.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 11 | 7.2 | 2.84 | 8.83 | 14.26 | 0.00 | 57.3 | 0.0 |
| XI | Bench | Stuart Dallas | DEF | 10 | 4.8 | 2.65 | 8.20 | 13.07 | 0.00 | 62.4 | 0.0 |
| XI | Bench | Patrick Bamford | FWD | 10 | 6.2 | 4.56 | 13.19 | 21.48 | 0.00 | 73.1 | 0.0 |
| Bench 2 | Bench | Dominic Calvert-Lewin | FWD | 7 | 7.4 | 2.50 | 7.94 | 14.44 | 0.00 | 37.8 | 0.0 |
| Bench 3 | Autosub In | Jordan Ayew | FWD | 6 | 5.6 | 1.74 | 5.22 | 8.52 | 1.00 | 40.2 | 9.0 |
| Captain | Captain | Heung-Min Son | MID | 17 | 9.7 | 6.61 | 18.85 | 31.23 | 2.00 | 109.1 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 12.3 | 5.14 | 16.60 | 28.00 | 0.00 | 80.9 | 0.0 |
| XI | Bench | Jack Grealish | MID | 2 | 7.7 | 3.94 | 11.88 | 19.26 | 0.00 | 69.5 | 0.0 |
| XI | XI | Wilfried Zaha | MID | 6 | 7.4 | 4.00 | 11.33 | 18.53 | 3.00 | 79.3 | 90.0 |
| Bench 4 | Bench | Diogo Jota | MID | 11 | 6.7 | 0.16 | 1.19 | 3.33 | 0.00 | 0.0 | 0.0 |

## GW19

- Train rows: 38716
- Bank: 0.20 -> 0.50
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Mohamed Salah
- Effective captain: Phil Foden
- Chip used: none
- Predicted score: 45.89
- Actual score: 67.00
- Chip advisory: triple_captain (0.63): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Diogo Jota -> Phil Foden (projected gain 12.88, hit 0)
- Autosub: Kieran Tierney replaced Wilfried Zaha.
- Autosub: Stuart Dallas replaced Dominic Calvert-Lewin.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Emiliano Martínez | GK | 2 | 4.9 | 1.80 | 6.09 | 9.11 | 9.00 | 69.0 | 180.0 |
| XI | XI | Kasper Schmeichel | GK | 9 | 5.5 | 2.72 | 5.22 | 7.23 | 17.00 | 68.4 | 180.0 |
| XI | XI | Tyrick Mitchell | DEF | 6 | 3.9 | 2.36 | 7.67 | 12.87 | 0.00 | 69.9 | 90.0 |
| XI | XI | Benjamin Chilwell | DEF | 5 | 5.9 | 2.16 | 6.95 | 10.97 | 7.00 | 66.1 | 180.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 7.2 | 3.30 | 6.52 | 8.96 | 8.00 | 65.1 | 180.0 |
| Bench 3 | Autosub In | Stuart Dallas | DEF | 10 | 4.8 | 1.68 | 4.81 | 8.48 | 2.00 | 36.2 | 90.0 |
| Bench 2 | Autosub In | Kieran Tierney | DEF | 1 | 5.4 | 1.71 | 3.96 | 6.79 | 6.00 | 13.8 | 90.0 |
| XI | XI | Patrick Bamford | FWD | 10 | 6.2 | 3.63 | 9.92 | 16.90 | 2.00 | 48.5 | 90.0 |
| XI | Bench | Dominic Calvert-Lewin | FWD | 7 | 7.4 | 2.65 | 9.01 | 16.43 | 0.00 | 24.7 | 0.0 |
| Bench 4 | Bench | Jordan Ayew | FWD | 6 | 5.6 | 1.08 | 4.18 | 7.46 | 2.00 | 28.3 | 90.0 |
| XI | XI | Heung-Min Son | MID | 17 | 9.7 | 4.88 | 13.83 | 24.01 | 5.00 | 68.7 | 90.0 |
| Captain | Captain | Phil Foden | MID | 12 | 6.3 | 6.94 | 13.13 | 19.48 | 4.00 | 117.7 | 120.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.2 | 4.89 | 12.15 | 19.84 | 4.00 | 74.6 | 123.0 |
| XI | Bench | Wilfried Zaha | MID | 6 | 7.3 | 3.60 | 10.66 | 18.15 | 0.00 | 79.3 | 0.0 |
| XI | XI | Jack Grealish | MID | 2 | 7.7 | 1.84 | 6.75 | 10.08 | 8.00 | 52.6 | 177.0 |

## GW20

- Train rows: 39355
- Bank: 0.50 -> 0.20
- Free transfers: 2 -> 2
- Captain: John Stones
- Vice captain: Mohamed Salah
- Effective captain: John Stones
- Chip used: none
- Predicted score: 66.01
- Actual score: 54.00
- Transfer: Stuart Dallas -> John Stones (projected gain 12.93, hit 0)
- Autosub: Wilfried Zaha replaced Kieran Tierney.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez | GK | 2 | 4.9 | 5.41 | 14.84 | 23.44 | 1.00 | 129.8 | 90.0 |
| Bench 1 | Bench | Kasper Schmeichel | GK | 9 | 5.5 | 4.31 | 12.26 | 19.84 | 2.00 | 120.8 | 90.0 |
| Captain | Captain | John Stones | DEF | 12 | 5.1 | 7.30 | 19.81 | 29.05 | 6.00 | 139.9 | 90.0 |
| XI | XI | Benjamin Chilwell | DEF | 5 | 5.9 | 5.20 | 14.05 | 21.91 | 5.00 | 115.8 | 75.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 7.2 | 4.97 | 13.47 | 20.88 | 14.00 | 111.9 | 90.0 |
| XI | Bench | Kieran Tierney | DEF | 1 | 5.4 | 3.50 | 9.58 | 15.27 | 0.00 | 77.5 | 0.0 |
| XI | XI | Tyrick Mitchell | DEF | 6 | 3.9 | 2.76 | 7.94 | 13.04 | 1.00 | 75.3 | 90.0 |
| XI | XI | Patrick Bamford | FWD | 10 | 6.2 | 5.01 | 14.04 | 22.19 | 1.00 | 80.5 | 59.0 |
| Bench 3 | Bench | Jordan Ayew | FWD | 6 | 5.6 | 2.31 | 6.71 | 10.90 | 4.00 | 59.1 | 17.0 |
| Bench 4 | Bench | Dominic Calvert-Lewin | FWD | 7 | 7.3 | 1.47 | 4.97 | 9.96 | 2.00 | 20.0 | 88.0 |
| XI | XI | Heung-Min Son | MID | 17 | 9.7 | 6.08 | 18.52 | 31.88 | 2.00 | 105.8 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.2 | 6.28 | 17.57 | 29.35 | 2.00 | 98.0 | 90.0 |
| XI | XI | Jack Grealish | MID | 2 | 7.7 | 6.23 | 17.04 | 26.92 | 8.00 | 123.2 | 90.0 |
| XI | XI | Phil Foden | MID | 12 | 6.3 | 5.97 | 15.58 | 23.40 | 1.00 | 78.3 | 51.0 |
| Bench 2 | Autosub In | Wilfried Zaha | MID | 6 | 7.2 | 2.43 | 7.71 | 12.88 | 7.00 | 40.3 | 90.0 |

## GW21

- Train rows: 39999
- Bank: 0.20 -> 0.70
- Free transfers: 2 -> 2
- Captain: Heung-Min Son
- Vice captain: Mohamed Salah
- Effective captain: Heung-Min Son
- Chip used: none
- Predicted score: 59.57
- Actual score: 59.00
- Transfer: Phil Foden -> Ilkay Gündogan (projected gain 4.82, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez | GK | 2 | 4.9 | 3.99 | 11.03 | 18.23 | 10.00 | 92.0 | 90.0 |
| Bench 1 | Bench | Kasper Schmeichel | GK | 9 | 5.5 | 3.07 | 9.03 | 15.43 | 2.00 | 85.1 | 90.0 |
| XI | Bench | John Stones | DEF | 12 | 5.1 | 5.32 | 13.75 | 21.62 | 0.00 | 91.8 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 7.2 | 4.16 | 12.38 | 19.68 | 2.00 | 92.0 | 90.0 |
| XI | Bench | Benjamin Chilwell | DEF | 5 | 5.9 | 3.89 | 11.23 | 18.30 | 0.00 | 79.7 | 0.0 |
| Bench 2 | Bench | Tyrick Mitchell | DEF | 6 | 3.9 | 3.15 | 8.60 | 13.23 | 0.00 | 76.6 | 0.0 |
| Bench 4 | Bench | Kieran Tierney | DEF | 1 | 5.4 | 1.20 | 4.54 | 6.83 | 0.00 | 29.8 | 0.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 7 | 7.3 | 5.27 | 15.44 | 24.19 | 2.00 | 87.8 | 90.0 |
| XI | XI | Patrick Bamford | FWD | 10 | 6.2 | 3.84 | 11.35 | 18.76 | 15.00 | 60.1 | 90.0 |
| Bench 3 | Bench | Jordan Ayew | FWD | 6 | 5.6 | 2.19 | 5.71 | 8.81 | 5.00 | 36.3 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.2 | 5.87 | 17.56 | 29.05 | 15.00 | 90.9 | 90.0 |
| Captain | Captain | Heung-Min Son | MID | 17 | 9.7 | 5.92 | 17.53 | 29.11 | 2.00 | 100.3 | 90.0 |
| XI | XI | Jack Grealish | MID | 2 | 7.7 | 5.51 | 15.28 | 23.87 | 6.00 | 89.8 | 90.0 |
| XI | XI | Ilkay Gündogan | MID | 12 | 5.8 | 5.83 | 14.80 | 22.42 | 3.00 | 87.1 | 90.0 |
| XI | XI | Wilfried Zaha | MID | 6 | 7.2 | 4.04 | 11.46 | 17.97 | 2.00 | 76.9 | 90.0 |

## GW22

- Train rows: 40649
- Bank: 0.70 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Jack Grealish
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 60.47
- Actual score: 53.00
- Transfer: Kieran Tierney -> Rúben Santos Gato Alves Dias (projected gain 6.70, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez | GK | 2 | 4.9 | 4.15 | 12.43 | 20.88 | 4.00 | 104.8 | 90.0 |
| Bench 1 | Bench | Kasper Schmeichel | GK | 9 | 5.5 | 3.43 | 9.68 | 16.40 | 6.00 | 92.3 | 90.0 |
| XI | XI | Rúben Santos Gato Alves Dias | DEF | 12 | 6.0 | 4.70 | 13.39 | 21.77 | 6.00 | 99.8 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 7.2 | 4.20 | 11.74 | 19.69 | 2.00 | 95.0 | 90.0 |
| XI | XI | John Stones | DEF | 12 | 5.1 | 3.12 | 8.71 | 14.51 | 6.00 | 51.8 | 90.0 |
| Bench 3 | Bench | Benjamin Chilwell | DEF | 5 | 5.9 | 2.19 | 6.98 | 12.64 | 0.00 | 43.7 | 0.0 |
| Bench 4 | Bench | Tyrick Mitchell | DEF | 6 | 3.9 | 1.52 | 4.79 | 6.74 | 0.00 | 38.8 | 0.0 |
| XI | XI | Patrick Bamford | FWD | 10 | 6.2 | 4.99 | 14.76 | 24.44 | 5.00 | 90.0 | 90.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 7 | 7.3 | 4.81 | 14.04 | 21.54 | 9.00 | 64.3 | 90.0 |
| Bench 2 | Bench | Jordan Ayew | FWD | 6 | 5.6 | 3.12 | 8.20 | 12.15 | 1.00 | 64.3 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.3 | 7.16 | 21.03 | 34.43 | 2.00 | 119.0 | 90.0 |
| XI | XI | Heung-Min Son | MID | 17 | 9.7 | 5.52 | 16.76 | 27.06 | 2.00 | 91.0 | 90.0 |
| Vice Captain | XI | Jack Grealish | MID | 2 | 7.8 | 5.66 | 16.46 | 26.46 | 6.00 | 106.3 | 90.0 |
| XI | XI | Ilkay Gündogan | MID | 12 | 5.8 | 5.26 | 14.08 | 21.00 | 8.00 | 75.2 | 90.0 |
| XI | XI | Wilfried Zaha | MID | 6 | 7.2 | 3.73 | 10.39 | 16.28 | 1.00 | 73.0 | 57.0 |

## GW23

- Train rows: 41312
- Bank: 0.00 -> 0.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Heung-Min Son
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 56.17
- Actual score: 73.00
- Transfer: Benjamin Chilwell -> Aaron Wan-Bissaka (projected gain 3.27, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez | GK | 2 | 5.0 | 3.63 | 10.63 | 18.11 | 9.00 | 94.5 | 90.0 |
| Bench 1 | Bench | Kasper Schmeichel | GK | 9 | 5.5 | 3.11 | 9.72 | 15.21 | 6.00 | 86.1 | 90.0 |
| XI | XI | Rúben Santos Gato Alves Dias | DEF | 12 | 6.0 | 4.21 | 12.60 | 19.16 | 1.00 | 88.7 | 90.0 |
| XI | XI | Aaron Wan-Bissaka | DEF | 13 | 5.5 | 4.01 | 12.12 | 18.83 | 4.00 | 94.2 | 90.0 |
| XI | XI | John Stones | DEF | 12 | 5.1 | 3.54 | 11.02 | 16.49 | 2.00 | 77.3 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 7.3 | 3.33 | 10.10 | 16.94 | 0.00 | 84.0 | 90.0 |
| Bench 4 | Bench | Tyrick Mitchell | DEF | 6 | 3.9 | 0.96 | 3.24 | 5.21 | 1.00 | 27.2 | 90.0 |
| XI | XI | Patrick Bamford | FWD | 10 | 6.2 | 5.49 | 15.19 | 24.88 | 6.00 | 95.2 | 90.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 7 | 7.3 | 4.40 | 13.39 | 22.24 | 12.00 | 82.7 | 90.0 |
| Bench 3 | Bench | Jordan Ayew | FWD | 6 | 5.6 | 2.52 | 7.03 | 11.12 | 2.00 | 61.2 | 75.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.3 | 6.19 | 18.25 | 29.80 | 7.00 | 89.0 | 90.0 |
| Vice Captain | XI | Heung-Min Son | MID | 17 | 9.7 | 5.83 | 16.50 | 26.74 | 10.00 | 93.4 | 90.0 |
| XI | XI | Jack Grealish | MID | 2 | 7.8 | 5.32 | 15.06 | 24.18 | 2.00 | 96.1 | 90.0 |
| XI | XI | Ilkay Gündogan | MID | 12 | 5.8 | 4.03 | 11.23 | 17.12 | 13.00 | 78.2 | 90.0 |
| Bench 2 | Bench | Wilfried Zaha | MID | 6 | 7.2 | 3.20 | 8.97 | 15.16 | 0.00 | 64.3 | 0.0 |

## GW24

- Train rows: 41979
- Bank: 0.40 -> 0.40
- Free transfers: 2 -> 2
- Captain: Dominic Calvert-Lewin
- Vice captain: Ilkay Gündogan
- Effective captain: Ilkay Gündogan
- Chip used: none
- Predicted score: 66.21
- Actual score: 74.00
- Transfer: Kasper Schmeichel -> Nick Pope (projected gain 1.47, hit 0)
- Autosub: Jordan Ayew replaced Dominic Calvert-Lewin.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Nick Pope | GK | 4 | 5.5 | 5.38 | 13.07 | 19.02 | 10.00 | 130.8 | 180.0 |
| Bench 1 | Bench | Emiliano Martínez | GK | 2 | 5.0 | 3.78 | 11.62 | 19.42 | 12.00 | 98.4 | 90.0 |
| XI | XI | John Stones | DEF | 12 | 5.1 | 5.28 | 13.04 | 19.10 | 6.00 | 115.4 | 90.0 |
| XI | XI | Rúben Santos Gato Alves Dias | DEF | 12 | 6.0 | 5.38 | 13.00 | 19.69 | 2.00 | 116.6 | 90.0 |
| XI | XI | Aaron Wan-Bissaka | DEF | 13 | 5.5 | 4.10 | 11.03 | 17.47 | 2.00 | 82.5 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 7.3 | 3.38 | 10.72 | 16.64 | 1.00 | 82.0 | 90.0 |
| Bench 3 | Bench | Tyrick Mitchell | DEF | 6 | 3.9 | 2.25 | 5.30 | 9.10 | 0.00 | 58.9 | 0.0 |
| Captain | Bench | Dominic Calvert-Lewin | FWD | 7 | 7.4 | 7.20 | 17.22 | 26.60 | 0.00 | 125.3 | 0.0 |
| XI | XI | Patrick Bamford | FWD | 10 | 6.3 | 5.60 | 15.89 | 25.54 | 2.00 | 100.2 | 90.0 |
| Bench 2 | Autosub In | Jordan Ayew | FWD | 6 | 5.6 | 2.53 | 6.60 | 10.37 | 2.00 | 60.1 | 90.0 |
| XI | XI | Mohamed Salah | MID | 11 | 12.3 | 5.95 | 18.02 | 29.85 | 7.00 | 95.3 | 90.0 |
| Vice Captain | Captain | Ilkay Gündogan | MID | 12 | 5.9 | 7.01 | 17.71 | 25.17 | 19.00 | 136.8 | 68.0 |
| XI | XI | Heung-Min Son | MID | 17 | 9.6 | 4.96 | 15.42 | 26.05 | 2.00 | 92.3 | 90.0 |
| XI | XI | Jack Grealish | MID | 2 | 7.8 | 4.77 | 13.81 | 21.91 | 2.00 | 90.2 | 90.0 |
| Bench 4 | Bench | Wilfried Zaha | MID | 6 | 7.1 | 1.97 | 5.89 | 10.45 | 0.00 | 32.3 | 0.0 |

## GW25

- Train rows: 42649
- Bank: 0.40 -> 2.10
- Free transfers: 2 -> 2
- Captain: Patrick Bamford
- Vice captain: Mohamed Salah
- Effective captain: Patrick Bamford
- Chip used: none
- Predicted score: 62.02
- Actual score: 63.00
- Chip advisory: triple_captain (0.61): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Wilfried Zaha -> Raphael Dias Belloli (projected gain 5.54, hit 0)
- Autosub: Dominic Calvert-Lewin replaced Jack Grealish.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Nick Pope | GK | 4 | 5.5 | 5.02 | 13.54 | 21.17 | 8.00 | 122.6 | 90.0 |
| Bench 1 | Bench | Emiliano Martínez | GK | 2 | 5.0 | 3.76 | 11.48 | 19.31 | 2.00 | 99.4 | 90.0 |
| XI | XI | Aaron Wan-Bissaka | DEF | 13 | 5.5 | 3.90 | 11.02 | 17.49 | 2.00 | 80.4 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 7.3 | 3.75 | 11.01 | 17.40 | 1.00 | 83.3 | 90.0 |
| XI | XI | Rúben Santos Gato Alves Dias | DEF | 12 | 6.0 | 3.27 | 10.46 | 17.45 | 7.00 | 80.6 | 90.0 |
| XI | XI | John Stones | DEF | 12 | 5.1 | 3.41 | 10.27 | 16.70 | 6.00 | 80.7 | 90.0 |
| Bench 4 | Bench | Tyrick Mitchell | DEF | 6 | 3.9 | 0.93 | 2.64 | 4.90 | 2.00 | 25.8 | 90.0 |
| Captain | Captain | Patrick Bamford | FWD | 10 | 6.3 | 7.93 | 20.12 | 29.69 | 8.00 | 138.4 | 180.0 |
| Bench 2 | Autosub In | Dominic Calvert-Lewin | FWD | 7 | 7.4 | 3.25 | 10.15 | 16.70 | 4.00 | 20.7 | 28.0 |
| Bench 3 | Bench | Jordan Ayew | FWD | 6 | 5.6 | 2.61 | 7.19 | 11.26 | 5.00 | 66.7 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.3 | 6.41 | 19.40 | 31.33 | 2.00 | 100.2 | 90.0 |
| XI | XI | Ilkay Gündogan | MID | 12 | 5.9 | 5.04 | 14.96 | 22.22 | 3.00 | 69.6 | 90.0 |
| XI | XI | Raphael Dias Belloli | MID | 10 | 5.4 | 6.19 | 14.82 | 21.16 | 12.00 | 125.0 | 180.0 |
| XI | XI | Heung-Min Son | MID | 17 | 9.5 | 4.81 | 14.72 | 25.58 | 2.00 | 94.8 | 90.0 |
| XI | Bench | Jack Grealish | MID | 2 | 7.7 | 4.36 | 12.87 | 21.03 | 0.00 | 83.8 | 0.0 |

## GW26

- Train rows: 43322
- Bank: 2.10 -> 2.80
- Free transfers: 2 -> 2
- Captain: Heung-Min Son
- Vice captain: Harvey Barnes
- Effective captain: Heung-Min Son
- Chip used: bench_boost
- Predicted score: 95.15
- Actual score: 113.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (28.42) beats the best remaining Bench Boost opportunity (20.45).
- Chip advisory: bench_boost (0.70): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Transfer: Jack Grealish -> Harvey Barnes (projected gain 8.16, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (28.42) beats the best remaining Bench Boost opportunity (20.45).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez | GK | 2 | 5.0 | 5.47 | 14.14 | 22.72 | 12.00 | 131.3 | 180.0 |
| Bench 1 | Bench Boost | Nick Pope | GK | 4 | 5.5 | 5.23 | 12.80 | 20.44 | 4.00 | 127.0 | 180.0 |
| XI | XI | Rúben Santos Gato Alves Dias | DEF | 12 | 6.0 | 5.19 | 13.21 | 20.58 | 12.00 | 125.8 | 180.0 |
| XI | XI | John Stones | DEF | 12 | 5.1 | 5.15 | 12.46 | 19.39 | 10.00 | 123.8 | 90.0 |
| Bench 3 | Bench Boost | Aaron Wan-Bissaka | DEF | 13 | 5.5 | 4.62 | 12.32 | 18.71 | 12.00 | 114.2 | 180.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 7.3 | 4.81 | 11.87 | 18.28 | 11.00 | 116.4 | 180.0 |
| Bench 4 | Bench Boost | Tyrick Mitchell | DEF | 6 | 3.9 | 3.98 | 8.92 | 13.34 | 0.00 | 102.9 | 0.0 |
| XI | XI | Patrick Bamford | FWD | 10 | 6.3 | 6.49 | 18.09 | 27.55 | 2.00 | 111.8 | 90.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 7 | 7.4 | 6.95 | 17.19 | 26.49 | 4.00 | 105.3 | 180.0 |
| Bench 2 | Bench Boost | Jordan Ayew | FWD | 6 | 5.6 | 4.74 | 10.62 | 15.12 | 4.00 | 109.7 | 180.0 |
| XI | XI | Mohamed Salah | MID | 11 | 12.3 | 7.45 | 20.44 | 31.97 | 5.00 | 131.2 | 151.0 |
| Captain | Captain | Heung-Min Son | MID | 17 | 9.5 | 7.55 | 18.77 | 29.97 | 14.00 | 134.8 | 180.0 |
| Vice Captain | XI | Harvey Barnes | MID | 9 | 6.9 | 7.55 | 18.68 | 27.88 | 1.00 | 146.0 | 50.0 |
| XI | XI | Ilkay Gündogan | MID | 12 | 6.0 | 6.46 | 15.94 | 24.58 | 6.00 | 129.3 | 96.0 |
| XI | XI | Raphael Dias Belloli | MID | 10 | 5.4 | 5.92 | 15.06 | 21.50 | 2.00 | 99.1 | 90.0 |

## GW27

- Train rows: 44004
- Bank: 2.80 -> 1.80
- Free transfers: 2 -> 2
- Captain: Heung-Min Son
- Vice captain: Mohamed Salah
- Effective captain: Heung-Min Son
- Chip used: none
- Predicted score: 74.28
- Actual score: 45.00
- Transfer: Jordan Ayew -> Ollie Watkins (projected gain 5.09, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez | GK | 2 | 5.0 | 6.01 | 16.59 | 26.94 | 7.00 | 137.4 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | 4 | 5.5 | 4.70 | 13.00 | 21.26 | 2.00 | 126.8 | 90.0 |
| XI | XI | Rúben Santos Gato Alves Dias | DEF | 12 | 6.0 | 6.61 | 16.91 | 26.39 | 2.00 | 163.4 | 180.0 |
| XI | XI | Aaron Wan-Bissaka | DEF | 13 | 5.5 | 4.99 | 14.66 | 22.59 | 6.00 | 126.3 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 7.3 | 5.29 | 13.76 | 21.99 | 1.00 | 122.3 | 14.0 |
| XI | XI | John Stones | DEF | 12 | 5.1 | 5.10 | 12.94 | 20.18 | 1.00 | 119.3 | 90.0 |
| Bench 4 | Bench | Tyrick Mitchell | DEF | 6 | 3.8 | 0.76 | 3.03 | 5.23 | 0.00 | 25.0 | 0.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 7 | 7.4 | 5.61 | 17.34 | 26.31 | 2.00 | 90.8 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 6.6 | 6.24 | 16.67 | 25.13 | 2.00 | 116.9 | 90.0 |
| XI | XI | Patrick Bamford | FWD | 10 | 6.3 | 4.94 | 15.16 | 24.87 | 2.00 | 97.6 | 90.0 |
| Captain | Captain | Heung-Min Son | MID | 17 | 9.5 | 8.05 | 22.94 | 35.94 | 5.00 | 144.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.3 | 6.97 | 20.03 | 32.96 | 2.00 | 121.5 | 90.0 |
| XI | XI | Ilkay Gündogan | MID | 12 | 6.0 | 6.44 | 17.36 | 26.37 | 10.00 | 117.2 | 180.0 |
| Bench 2 | Bench | Raphael Dias Belloli | MID | 10 | 5.4 | 3.92 | 11.10 | 16.90 | 2.00 | 80.4 | 90.0 |
| Bench 3 | Bench | Harvey Barnes | MID | 9 | 6.9 | 2.78 | 8.02 | 14.14 | 0.00 | 19.5 | 0.0 |

## GW28

- Train rows: 44689
- Bank: 1.80 -> 2.70
- Free transfers: 2 -> 2
- Captain: Ilkay Gündogan
- Vice captain: Heung-Min Son
- Effective captain: Heung-Min Son
- Chip used: none
- Predicted score: 62.54
- Actual score: 50.00
- Transfer: Harvey Barnes -> James Ward-Prowse (projected gain 6.31, hit 0)
- Autosub: Raphael Dias Belloli replaced Ilkay Gündogan.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez | GK | 2 | 5.1 | 4.66 | 13.69 | 22.14 | 3.00 | 109.6 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | 4 | 5.5 | 3.35 | 9.64 | 15.66 | 2.00 | 96.1 | 90.0 |
| XI | XI | Rúben Santos Gato Alves Dias | DEF | 12 | 6.0 | 5.37 | 14.75 | 23.75 | 6.00 | 133.2 | 74.0 |
| XI | XI | Aaron Wan-Bissaka | DEF | 13 | 5.6 | 3.93 | 11.47 | 18.82 | 5.00 | 100.1 | 90.0 |
| XI | XI | John Stones | DEF | 12 | 5.2 | 3.45 | 9.99 | 16.58 | 14.00 | 79.9 | 90.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | 11 | 7.3 | 3.05 | 8.94 | 15.41 | 9.00 | 61.2 | 90.0 |
| Bench 4 | Bench | Tyrick Mitchell | DEF | 6 | 3.8 | 1.02 | 2.64 | 4.54 | 0.00 | 24.5 | 0.0 |
| XI | XI | Patrick Bamford | FWD | 10 | 6.3 | 4.73 | 13.78 | 23.04 | 1.00 | 98.3 | 34.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 7 | 7.4 | 4.81 | 13.74 | 23.10 | 6.00 | 87.9 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 6.6 | 4.76 | 12.80 | 19.86 | 5.00 | 91.4 | 90.0 |
| Vice Captain | Captain | Heung-Min Son | MID | 17 | 9.6 | 6.25 | 19.35 | 31.17 | 1.00 | 109.4 | 18.0 |
| Captain | Bench | Ilkay Gündogan | MID | 12 | 6.0 | 6.58 | 18.79 | 28.25 | 0.00 | 121.1 | 0.0 |
| XI | XI | James Ward-Prowse | MID | 16 | 5.9 | 5.97 | 16.46 | 24.81 | 2.00 | 136.4 | 90.0 |
| XI | XI | Mohamed Salah | MID | 11 | 12.2 | 5.45 | 16.32 | 27.71 | 3.00 | 86.0 | 90.0 |
| Bench 2 | Autosub In | Raphael Dias Belloli | MID | 10 | 5.4 | 3.92 | 10.31 | 16.00 | 3.00 | 83.1 | 90.0 |

## GW29

- Train rows: 45375
- Bank: 2.70 -> 1.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Ollie Watkins
- Effective captain: Ollie Watkins
- Chip used: none
- Predicted score: 52.62
- Actual score: 26.00
- Transfer: Tyrick Mitchell -> Stuart Dallas (projected gain 3.44, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez | GK | 2 | 5.1 | 4.60 | 13.45 | 22.13 | 1.00 | 108.3 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | 4 | 5.5 | 2.87 | 9.56 | 15.29 | 0.00 | 83.1 | 0.0 |
| XI | XI | Stuart Dallas | DEF | 10 | 5.1 | 4.86 | 13.28 | 20.05 | 2.00 | 105.2 | 90.0 |
| XI | Bench | Rúben Santos Gato Alves Dias | DEF | 12 | 6.0 | 3.54 | 11.35 | 18.34 | 0.00 | 88.9 | 0.0 |
| XI | Bench | Aaron Wan-Bissaka | DEF | 13 | 5.6 | 3.61 | 10.53 | 17.43 | 0.00 | 81.8 | 0.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 11 | 7.3 | 3.36 | 10.28 | 17.46 | 0.00 | 66.1 | 0.0 |
| Bench 4 | Bench | John Stones | DEF | 12 | 5.2 | 3.17 | 10.01 | 16.92 | 0.00 | 72.9 | 0.0 |
| Vice Captain | Captain | Ollie Watkins | FWD | 2 | 6.6 | 5.13 | 13.92 | 21.65 | 2.00 | 97.8 | 90.0 |
| XI | Bench | Dominic Calvert-Lewin | FWD | 7 | 7.4 | 4.30 | 12.83 | 21.69 | 0.00 | 79.2 | 0.0 |
| XI | XI | Patrick Bamford | FWD | 10 | 6.2 | 4.13 | 11.40 | 18.98 | 11.00 | 68.1 | 76.0 |
| Captain | Bench | Mohamed Salah | MID | 11 | 12.2 | 5.16 | 15.99 | 27.79 | 0.00 | 77.5 | 0.0 |
| XI | Bench | Heung-Min Son | MID | 17 | 9.5 | 4.01 | 12.83 | 22.85 | 0.00 | 61.5 | 0.0 |
| XI | XI | Raphael Dias Belloli | MID | 10 | 5.5 | 4.75 | 12.23 | 17.63 | 8.00 | 95.3 | 90.0 |
| Bench 3 | Bench | Ilkay Gündogan | MID | 12 | 6.0 | 3.25 | 10.20 | 16.67 | 0.00 | 44.0 | 0.0 |
| Bench 2 | Bench | James Ward-Prowse | MID | 16 | 5.9 | 3.35 | 9.99 | 15.94 | 0.00 | 77.7 | 0.0 |

## GW30

- Train rows: 46061
- Bank: 1.40 -> 1.10
- Free transfers: 2 -> 2
- Captain: Patrick Bamford
- Vice captain: Emiliano Martínez
- Effective captain: Patrick Bamford
- Chip used: none
- Predicted score: 46.16
- Actual score: 54.00
- Transfer: Ilkay Gündogan -> Jesse Lingard (projected gain 4.15, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Vice Captain | XI | Emiliano Martínez | GK | 2 | 5.1 | 4.46 | 12.46 | 20.23 | 4.00 | 97.2 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | 4 | 5.5 | 1.84 | 5.76 | 9.42 | 2.00 | 45.2 | 90.0 |
| XI | XI | Stuart Dallas | DEF | 10 | 5.1 | 4.07 | 11.23 | 17.17 | 2.00 | 79.7 | 90.0 |
| XI | XI | Rúben Santos Gato Alves Dias | DEF | 12 | 6.0 | 2.19 | 8.66 | 14.26 | 6.00 | 53.9 | 90.0 |
| XI | XI | Aaron Wan-Bissaka | DEF | 13 | 5.6 | 2.35 | 7.00 | 11.38 | 2.00 | 49.5 | 90.0 |
| Bench 4 | Bench | John Stones | DEF | 12 | 5.2 | 1.74 | 6.82 | 11.70 | 0.00 | 40.7 | 0.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | 11 | 7.2 | 1.90 | 6.80 | 11.29 | 12.00 | 36.8 | 90.0 |
| Captain | Captain | Patrick Bamford | FWD | 10 | 6.2 | 5.18 | 14.63 | 23.58 | 2.00 | 85.2 | 64.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 6.6 | 4.35 | 11.20 | 17.36 | 7.00 | 77.5 | 90.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 7 | 7.3 | 3.24 | 8.87 | 14.59 | 2.00 | 45.7 | 90.0 |
| XI | XI | Jesse Lingard | MID | 19 | 6.2 | 4.02 | 11.37 | 17.48 | 12.00 | 67.4 | 90.0 |
| XI | XI | Heung-Min Son | MID | 17 | 9.4 | 3.54 | 11.17 | 19.69 | 1.00 | 43.9 | 45.0 |
| XI | XI | Mohamed Salah | MID | 11 | 12.2 | 3.28 | 11.02 | 19.23 | 8.00 | 45.2 | 90.0 |
| XI | XI | Raphael Dias Belloli | MID | 10 | 5.5 | 4.31 | 10.58 | 15.34 | 6.00 | 70.0 | 90.0 |
| Bench 2 | Bench | James Ward-Prowse | MID | 16 | 5.9 | 2.53 | 7.31 | 12.11 | 2.00 | 52.2 | 90.0 |

## GW31

- Train rows: 46748
- Bank: 1.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Diogo Jota
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 50.68
- Actual score: 85.00
- Transfer: James Ward-Prowse -> Diogo Jota (projected gain 3.30, hit 0)
- Autosub: Stuart Dallas replaced Rúben Santos Gato Alves Dias.
- Autosub: Raphael Dias Belloli replaced Dominic Calvert-Lewin.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez | GK | 2 | 5.1 | 3.86 | 11.70 | 19.29 | 4.00 | 96.4 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | 4 | 5.5 | 3.08 | 8.45 | 13.83 | 0.00 | 79.0 | 0.0 |
| XI | Bench | Rúben Santos Gato Alves Dias | DEF | 12 | 6.1 | 3.86 | 11.27 | 18.38 | 0.00 | 84.1 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 7.2 | 3.98 | 10.96 | 17.80 | 11.00 | 77.0 | 90.0 |
| XI | XI | Aaron Wan-Bissaka | DEF | 13 | 5.6 | 2.91 | 9.44 | 15.32 | 2.00 | 78.4 | 90.0 |
| Bench 3 | Autosub In | Stuart Dallas | DEF | 10 | 5.1 | 2.68 | 8.31 | 14.29 | 17.00 | 79.4 | 90.0 |
| Bench 4 | Bench | John Stones | DEF | 12 | 5.1 | 1.73 | 5.39 | 9.53 | 1.00 | 30.2 | 90.0 |
| XI | Bench | Dominic Calvert-Lewin | FWD | 7 | 7.3 | 4.36 | 11.98 | 19.01 | 0.00 | 77.0 | 0.0 |
| XI | XI | Patrick Bamford | FWD | 10 | 6.2 | 3.30 | 10.71 | 18.57 | 4.00 | 66.2 | 45.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 6.6 | 3.77 | 10.45 | 16.88 | 8.00 | 78.5 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.2 | 6.02 | 16.74 | 27.09 | 7.00 | 89.3 | 90.0 |
| XI | XI | Heung-Min Son | MID | 17 | 9.4 | 4.20 | 13.13 | 22.27 | 7.00 | 63.7 | 90.0 |
| Vice Captain | XI | Diogo Jota | MID | 11 | 6.9 | 4.49 | 12.19 | 18.41 | 2.00 | 69.8 | 90.0 |
| XI | XI | Jesse Lingard | MID | 19 | 6.2 | 3.92 | 11.32 | 17.93 | 14.00 | 79.3 | 90.0 |
| Bench 2 | Autosub In | Raphael Dias Belloli | MID | 10 | 5.5 | 2.85 | 8.34 | 13.74 | 2.00 | 68.5 | 90.0 |

## GW32

- Train rows: 47439
- Bank: 0.10 -> 1.40
- Free transfers: 2 -> 2
- Captain: Heung-Min Son
- Vice captain: Mohamed Salah
- Effective captain: Heung-Min Son
- Chip used: none
- Predicted score: 56.57
- Actual score: 59.00
- Chip advisory: triple_captain (0.61): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Dominic Calvert-Lewin -> Kelechi Iheanacho (projected gain 5.18, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez | GK | 2 | 5.1 | 3.53 | 10.73 | 18.45 | 1.00 | 98.0 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | 4 | 5.5 | 1.13 | 4.06 | 7.60 | 0.00 | 36.0 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 7.3 | 3.62 | 10.69 | 17.55 | 8.00 | 74.4 | 90.0 |
| XI | XI | Stuart Dallas | DEF | 10 | 5.1 | 3.38 | 10.45 | 17.35 | 1.00 | 92.4 | 90.0 |
| XI | XI | Aaron Wan-Bissaka | DEF | 13 | 5.6 | 3.23 | 8.98 | 14.25 | 1.00 | 76.4 | 90.0 |
| Bench 2 | Bench | John Stones | DEF | 12 | 5.1 | 2.83 | 7.69 | 12.34 | -2.00 | 56.6 | 43.0 |
| Bench 4 | Bench | Rúben Santos Gato Alves Dias | DEF | 12 | 6.1 | 2.24 | 6.69 | 11.61 | 2.00 | 38.8 | 90.0 |
| XI | XI | Kelechi Iheanacho | FWD | 9 | 6.0 | 4.49 | 12.80 | 18.50 | 6.00 | 77.7 | 90.0 |
| XI | XI | Patrick Bamford | FWD | 10 | 6.1 | 3.84 | 11.24 | 19.72 | 2.00 | 70.2 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 6.5 | 3.51 | 10.03 | 16.76 | 5.00 | 79.6 | 90.0 |
| Captain | Captain | Heung-Min Son | MID | 17 | 9.5 | 7.58 | 19.42 | 29.69 | 12.00 | 132.3 | 180.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.2 | 6.19 | 17.47 | 27.85 | 1.00 | 87.3 | 19.0 |
| XI | XI | Jesse Lingard | MID | 19 | 6.3 | 5.71 | 16.10 | 25.37 | 7.00 | 96.5 | 86.0 |
| XI | XI | Diogo Jota | MID | 11 | 6.9 | 3.91 | 11.71 | 16.98 | 3.00 | 50.5 | 80.0 |
| Bench 3 | Bench | Raphael Dias Belloli | MID | 10 | 5.4 | 2.73 | 7.90 | 13.34 | 0.00 | 68.0 | 0.0 |

## GW33

- Train rows: 48130
- Bank: 1.40 -> 0.80
- Free transfers: 2 -> 2
- Captain: Heung-Min Son
- Vice captain: Mohamed Salah
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 59.21
- Actual score: 67.00
- Transfer: John Stones -> Timothy Castagne (projected gain 0.58, hit 0)
- Autosub: Aaron Wan-Bissaka replaced Heung-Min Son.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez | GK | 2 | 5.1 | 4.31 | 12.04 | 20.06 | 2.00 | 101.4 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | 4 | 5.5 | 1.29 | 4.18 | 7.51 | 6.00 | 32.8 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 7.3 | 4.63 | 12.52 | 21.09 | 2.00 | 91.4 | 90.0 |
| XI | XI | Stuart Dallas | DEF | 10 | 5.1 | 3.54 | 10.58 | 17.63 | 6.00 | 90.8 | 90.0 |
| XI | XI | Timothy Castagne | DEF | 9 | 5.7 | 3.74 | 9.73 | 15.32 | 9.00 | 81.7 | 90.0 |
| Bench 2 | Autosub In | Aaron Wan-Bissaka | DEF | 13 | 5.6 | 3.19 | 9.27 | 15.25 | 9.00 | 80.8 | 90.0 |
| Bench 3 | Bench | Rúben Santos Gato Alves Dias | DEF | 12 | 6.1 | 2.70 | 8.44 | 15.04 | 0.00 | 63.6 | 0.0 |
| XI | XI | Kelechi Iheanacho | FWD | 9 | 6.0 | 5.31 | 13.92 | 20.03 | 12.00 | 73.4 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 6.6 | 4.92 | 13.36 | 21.42 | 5.00 | 94.6 | 90.0 |
| XI | XI | Patrick Bamford | FWD | 10 | 6.1 | 4.26 | 12.95 | 20.99 | 1.00 | 83.3 | 90.0 |
| Captain | Bench | Heung-Min Son | MID | 17 | 9.5 | 6.60 | 19.31 | 30.97 | 0.00 | 104.5 | 0.0 |
| Vice Captain | Captain | Mohamed Salah | MID | 11 | 12.3 | 6.25 | 17.85 | 29.22 | 9.00 | 80.9 | 90.0 |
| XI | XI | Jesse Lingard | MID | 19 | 6.4 | 5.02 | 15.13 | 23.95 | 2.00 | 81.6 | 90.0 |
| XI | XI | Diogo Jota | MID | 11 | 6.9 | 4.04 | 11.20 | 17.57 | 1.00 | 65.1 | 57.0 |
| Bench 4 | Bench | Raphael Dias Belloli | MID | 10 | 5.4 | 1.47 | 5.02 | 8.49 | 0.00 | 34.2 | 0.0 |

## GW34

- Train rows: 48823
- Bank: 0.80 -> 0.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Kelechi Iheanacho
- Effective captain: Kelechi Iheanacho
- Chip used: none
- Predicted score: 51.99
- Actual score: 44.00
- Transfer: Diogo Jota -> Mason Mount (projected gain 3.19, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez | GK | 2 | 5.1 | 3.74 | 10.99 | 18.38 | 2.00 | 95.0 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | 4 | 5.5 | 2.24 | 6.78 | 11.37 | 1.00 | 60.8 | 90.0 |
| XI | XI | Stuart Dallas | DEF | 10 | 5.2 | 3.68 | 10.52 | 17.26 | 1.00 | 91.8 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 11 | 7.3 | 3.19 | 10.06 | 17.26 | 0.00 | 57.8 | 0.0 |
| XI | XI | Timothy Castagne | DEF | 9 | 5.7 | 3.62 | 9.69 | 15.64 | 2.00 | 75.7 | 90.0 |
| Bench 2 | Bench | Aaron Wan-Bissaka | DEF | 13 | 5.6 | 2.64 | 8.00 | 14.00 | 0.00 | 64.5 | 0.0 |
| Bench 3 | Bench | Rúben Santos Gato Alves Dias | DEF | 12 | 6.0 | 1.86 | 5.58 | 9.98 | 0.00 | 36.7 | 0.0 |
| Vice Captain | Captain | Kelechi Iheanacho | FWD | 9 | 6.1 | 5.47 | 14.06 | 21.77 | 5.00 | 80.0 | 90.0 |
| XI | XI | Patrick Bamford | FWD | 10 | 6.1 | 3.89 | 11.73 | 19.11 | 1.00 | 79.4 | 58.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 6.6 | 3.96 | 11.35 | 18.04 | 8.00 | 74.9 | 90.0 |
| Captain | Bench | Mohamed Salah | MID | 11 | 12.3 | 5.53 | 17.02 | 27.74 | 0.00 | 67.0 | 0.0 |
| XI | XI | Jesse Lingard | MID | 19 | 6.4 | 4.77 | 13.60 | 21.57 | 2.00 | 87.1 | 90.0 |
| XI | XI | Heung-Min Son | MID | 17 | 9.5 | 4.17 | 11.65 | 20.38 | 12.00 | 59.9 | 90.0 |
| XI | XI | Mason Mount | MID | 5 | 7.3 | 4.44 | 11.53 | 18.33 | 6.00 | 75.0 | 75.0 |
| Bench 4 | Bench | Raphael Dias Belloli | MID | 10 | 5.4 | 0.98 | 3.50 | 5.72 | 0.00 | 23.5 | 0.0 |

## GW35

- Train rows: 49518
- Bank: 0.40 -> 0.60
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Kelechi Iheanacho
- Effective captain: Ollie Watkins
- Chip used: triple_captain
- Predicted score: 67.02
- Actual score: 75.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (11.70) beats the best remaining Triple Captain opportunity (6.43).
- Transfer: Aaron Wan-Bissaka -> Tyrone Mings (projected gain 2.81, hit 0)
- Chip used: Triple Captain on Ollie Watkins. Optimizer chose Triple Captain here because the current estimated captain upside (11.70) beats the best remaining Triple Captain opportunity (6.43).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez | GK | 2 | 5.1 | 5.55 | 13.70 | 21.00 | 12.00 | 127.3 | 180.0 |
| Bench 1 | Bench | Nick Pope | GK | 4 | 5.5 | 2.66 | 7.37 | 12.17 | 7.00 | 67.5 | 90.0 |
| XI | XI | Tyrone Mings | DEF | 2 | 5.4 | 4.82 | 11.14 | 16.29 | 7.00 | 114.4 | 180.0 |
| XI | XI | Stuart Dallas | DEF | 10 | 5.2 | 3.80 | 11.03 | 17.29 | 9.00 | 80.0 | 90.0 |
| XI | XI | Timothy Castagne | DEF | 9 | 5.7 | 4.61 | 11.02 | 16.56 | 2.00 | 105.9 | 180.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 7.4 | 3.80 | 9.24 | 14.19 | 16.00 | 75.9 | 180.0 |
| Bench 3 | Bench | Rúben Santos Gato Alves Dias | DEF | 12 | 6.0 | 1.41 | 4.85 | 8.80 | 1.00 | 29.0 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 6.5 | 6.40 | 15.57 | 22.81 | -1.00 | 118.3 | 88.0 |
| Vice Captain | XI | Kelechi Iheanacho | FWD | 9 | 6.1 | 5.94 | 14.51 | 21.23 | 9.00 | 109.2 | 180.0 |
| Bench 2 | Bench | Patrick Bamford | FWD | 10 | 6.1 | 3.41 | 9.23 | 15.48 | 9.00 | 61.7 | 78.0 |
| XI | XI | Mohamed Salah | MID | 11 | 12.3 | 5.54 | 14.59 | 22.87 | 13.00 | 80.4 | 176.0 |
| XI | XI | Heung-Min Son | MID | 17 | 9.6 | 4.87 | 14.51 | 23.84 | 7.00 | 77.1 | 90.0 |
| XI | XI | Mason Mount | MID | 5 | 7.3 | 5.04 | 12.62 | 18.26 | 2.00 | 102.5 | 90.0 |
| XI | XI | Jesse Lingard | MID | 19 | 6.4 | 3.85 | 11.78 | 18.88 | 1.00 | 75.3 | 90.0 |
| Bench 4 | Bench | Raphael Dias Belloli | MID | 10 | 5.4 | 0.85 | 2.52 | 4.35 | 4.00 | 17.0 | 32.0 |

## GW36

- Train rows: 50221
- Bank: 0.60 -> 0.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Heung-Min Son
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 65.26
- Actual score: 53.00
- Transfer: Rúben Santos Gato Alves Dias -> Lucas Digne (projected gain 4.31, hit 0)
- Autosub: Raphael Dias Belloli replaced Tyrone Mings.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez | GK | 2 | 5.1 | 5.24 | 14.89 | 24.18 | 2.00 | 133.6 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | 4 | 5.5 | 2.88 | 8.25 | 13.56 | 0.00 | 74.9 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 7.4 | 5.94 | 16.48 | 25.74 | 6.00 | 111.2 | 90.0 |
| XI | XI | Lucas Digne | DEF | 7 | 6.2 | 5.51 | 14.85 | 23.37 | 2.00 | 119.5 | 90.0 |
| XI | XI | Stuart Dallas | DEF | 10 | 5.2 | 4.69 | 13.13 | 20.50 | 6.00 | 96.1 | 90.0 |
| XI | Bench | Tyrone Mings | DEF | 2 | 5.4 | 4.32 | 12.12 | 18.99 | 0.00 | 118.3 | 0.0 |
| Bench 2 | Bench | Timothy Castagne | DEF | 9 | 5.7 | 3.51 | 10.59 | 17.12 | 0.00 | 95.8 | 0.0 |
| XI | Bench | Kelechi Iheanacho | FWD | 9 | 6.1 | 5.03 | 14.14 | 21.88 | 0.00 | 92.3 | 0.0 |
| XI | XI | Patrick Bamford | FWD | 10 | 6.1 | 4.68 | 13.15 | 20.75 | 1.00 | 84.9 | 57.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 6.5 | 3.81 | 10.69 | 17.14 | 5.00 | 67.2 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.3 | 7.91 | 21.95 | 34.46 | 10.00 | 121.3 | 90.0 |
| Vice Captain | XI | Heung-Min Son | MID | 17 | 9.6 | 6.00 | 17.51 | 28.04 | 3.00 | 93.2 | 90.0 |
| XI | XI | Jesse Lingard | MID | 19 | 6.4 | 4.23 | 12.53 | 19.89 | 2.00 | 82.8 | 90.0 |
| Bench 3 | Bench | Mason Mount | MID | 5 | 7.3 | 3.44 | 10.04 | 16.15 | 0.00 | 57.1 | 0.0 |
| Bench 4 | Autosub In | Raphael Dias Belloli | MID | 10 | 5.4 | 2.12 | 5.85 | 9.72 | 6.00 | 41.8 | 80.0 |

## GW37

- Train rows: 50924
- Bank: 0.40 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Heung-Min Son
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 54.06
- Actual score: 63.00
- Transfer: Mason Mount -> Wilfried Zaha (projected gain 5.93, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez | GK | 2 | 5.1 | 3.61 | 10.73 | 18.27 | 3.00 | 101.9 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | 4 | 5.5 | 1.45 | 4.80 | 8.14 | 0.00 | 37.5 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 7.4 | 4.71 | 13.03 | 21.15 | 6.00 | 76.5 | 90.0 |
| XI | XI | Stuart Dallas | DEF | 10 | 5.2 | 4.31 | 11.81 | 18.42 | 5.00 | 79.2 | 90.0 |
| XI | XI | Lucas Digne | DEF | 7 | 6.2 | 3.90 | 10.48 | 17.08 | 8.00 | 82.6 | 90.0 |
| Bench 4 | Bench | Timothy Castagne | DEF | 9 | 5.7 | 1.37 | 5.48 | 9.17 | 1.00 | 42.7 | 90.0 |
| Bench 2 | Bench | Tyrone Mings | DEF | 2 | 5.4 | 1.56 | 5.01 | 8.53 | 2.00 | 50.8 | 90.0 |
| XI | XI | Patrick Bamford | FWD | 10 | 6.1 | 4.36 | 11.73 | 18.88 | 12.00 | 67.2 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 6.4 | 3.42 | 9.96 | 16.09 | 9.00 | 70.0 | 90.0 |
| Bench 3 | Bench | Kelechi Iheanacho | FWD | 9 | 6.1 | 1.54 | 5.17 | 8.76 | 6.00 | 25.9 | 30.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.4 | 6.65 | 19.03 | 30.60 | 3.00 | 87.4 | 90.0 |
| Vice Captain | XI | Heung-Min Son | MID | 17 | 9.7 | 5.90 | 16.23 | 26.52 | 2.00 | 82.7 | 90.0 |
| XI | XI | Wilfried Zaha | MID | 6 | 7.2 | 3.80 | 11.11 | 17.62 | 2.00 | 80.5 | 90.0 |
| XI | XI | Jesse Lingard | MID | 19 | 6.4 | 4.12 | 10.89 | 17.37 | 7.00 | 78.0 | 90.0 |
| XI | XI | Raphael Dias Belloli | MID | 10 | 5.4 | 2.63 | 7.60 | 11.95 | 3.00 | 52.5 | 90.0 |

## GW38

- Train rows: 51630
- Bank: 0.50 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 58.52
- Actual score: 42.00
- Transfer: Nick Pope -> Jordan Pickford (projected gain 0.08, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez | GK | 2 | 5.0 | 3.80 | 11.67 | 19.52 | 3.00 | 103.1 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 7 | 4.8 | 3.10 | 9.88 | 15.90 | 2.00 | 89.3 | 90.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 11 | 7.5 | 5.89 | 15.26 | 24.08 | 5.00 | 94.9 | 90.0 |
| XI | XI | Stuart Dallas | DEF | 10 | 5.3 | 4.73 | 12.55 | 20.03 | 2.00 | 89.7 | 90.0 |
| XI | XI | Lucas Digne | DEF | 7 | 6.2 | 3.55 | 11.14 | 18.37 | 0.00 | 89.1 | 90.0 |
| Bench 3 | Bench | Timothy Castagne | DEF | 9 | 5.7 | 2.75 | 7.95 | 12.85 | 0.00 | 75.5 | 90.0 |
| Bench 4 | Bench | Tyrone Mings | DEF | 2 | 5.4 | 2.68 | 7.92 | 12.89 | 2.00 | 78.5 | 90.0 |
| XI | XI | Patrick Bamford | FWD | 10 | 6.2 | 5.46 | 14.69 | 23.31 | 6.00 | 92.1 | 45.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 6.3 | 3.50 | 10.19 | 16.07 | 2.00 | 66.4 | 90.0 |
| XI | XI | Kelechi Iheanacho | FWD | 9 | 6.1 | 3.52 | 9.81 | 15.66 | 2.00 | 59.5 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.4 | 7.43 | 20.48 | 32.98 | 6.00 | 103.7 | 90.0 |
| XI | XI | Heung-Min Son | MID | 17 | 9.6 | 4.93 | 14.94 | 24.84 | 5.00 | 90.0 | 90.0 |
| XI | XI | Wilfried Zaha | MID | 6 | 7.1 | 3.99 | 11.72 | 18.46 | 2.00 | 81.5 | 90.0 |
| XI | XI | Jesse Lingard | MID | 19 | 6.4 | 4.30 | 11.31 | 18.24 | 3.00 | 80.2 | 90.0 |
| Bench 2 | Bench | Raphael Dias Belloli | MID | 10 | 5.5 | 3.25 | 8.95 | 14.36 | 5.00 | 64.1 | 90.0 |