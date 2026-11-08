# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 287.09
- Total actual points: 242.00
- Average predicted points: 71.77
- Average actual points: 60.50
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW30 are included before the first simulated week.
- League-average scores were not available for this run.

## GW31

- Train rows: 184363
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 64.25
- Actual score: 48.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Adrien Truffert replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.10 | 11.75 | 14.32 | 2.00 | 88.8 | 90.0 |
| XI | XI | Emiliano Martínez Romero | GK | 2 | 5.1 | 3.36 | 9.17 | 14.75 | 6.00 | 88.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 5.77 | 16.67 | 26.44 | 3.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 4.48 | 16.66 | 19.77 | 1.00 | 90.0 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.89 | 14.56 | 17.79 | -1.00 | 86.3 | 90.0 |
| Bench 2 | Autosub In | Adrien Truffert | DEF | 4 | 4.6 | 3.82 | 14.27 | 17.48 | 4.00 | 86.2 | 90.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 5.58 | 14.11 | 21.54 | 0.00 | 90.0 | 36.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.41 | 24.13 | 29.21 | 2.00 | 90.0 | 77.0 |
| Bench 3 | Bench | Dominic Calvert-Lewin | FWD | 11 | 5.6 | 3.23 | 11.73 | 14.11 | 2.00 | 70.5 | 90.0 |
| Bench 4 | Bench | Lyle Foster | FWD | 3 | 4.9 | 2.32 | 8.34 | 9.78 | 5.00 | 51.7 | 77.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.67 | 22.56 | 27.74 | 2.00 | 86.7 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.36 | 22.03 | 35.38 | 13.00 | 90.0 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 14.0 | 5.06 | 16.46 | 27.84 | 0.00 | 69.3 | 0.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 4.12 | 16.24 | 19.25 | 2.00 | 89.9 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.19 | 15.47 | 24.45 | 3.00 | 90.0 | 90.0 |

## GW32

- Train rows: 185188
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Cole Palmer
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 55.37
- Actual score: 54.00
- Transfer: Malick Thiaw -> Jan Paul van Hecke (projected gain 1.53, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dúbravka | GK | 3 | 4.0 | 3.18 | 8.85 | 14.32 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Emiliano Martínez Romero | GK | 2 | 5.1 | 2.50 | 7.65 | 12.82 | 0.00 | 80.0 | 0.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 4.58 | 11.89 | 18.02 | 5.00 | 89.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.74 | 11.59 | 19.14 | 9.00 | 76.5 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.67 | 11.05 | 17.65 | 3.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Marcos Senesi Barón | DEF | 4 | 5.1 | 3.31 | 10.44 | 17.18 | 4.00 | 82.7 | 90.0 |
| Bench 3 | Bench | Adrien Truffert | DEF | 4 | 4.6 | 3.03 | 9.65 | 15.91 | 4.00 | 82.8 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 4.83 | 15.23 | 25.67 | 2.00 | 79.3 | 81.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 11 | 5.6 | 3.49 | 10.12 | 15.81 | 2.00 | 78.2 | 90.0 |
| Bench 4 | Bench | Lyle Foster | FWD | 3 | 4.9 | 2.63 | 7.24 | 11.04 | 0.00 | 61.8 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.01 | 21.59 | 34.70 | 4.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.6 | 5.02 | 15.47 | 25.71 | 4.00 | 84.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.0 | 4.33 | 13.74 | 23.77 | 8.00 | 47.4 | 89.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.27 | 12.90 | 20.77 | 5.00 | 79.3 | 90.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 4.24 | 11.78 | 18.82 | 6.00 | 88.3 | 90.0 |

## GW33

- Train rows: 186014
- Bank: 0.60 -> 0.40
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Cole Palmer
- Chip used: bench_boost
- Predicted score: 113.44
- Actual score: 102.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (20.01) beats the best remaining Bench Boost opportunity (0.00).
- Chip advisory: bench_boost (0.56): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.69): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: James Hill -> Konstantinos Mavropanos (projected gain 2.41, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (20.01) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dúbravka | GK | 3 | 4.0 | 5.44 | 7.91 | 13.10 | 4.00 | 175.1 | 180.0 |
| Bench 1 | Bench Boost | Emiliano Martínez Romero | GK | 2 | 5.1 | 1.67 | 5.14 | 9.07 | 2.00 | 43.5 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 10.16 | 13.55 | 20.92 | 6.00 | 180.0 | 180.0 |
| Bench 2 | Bench Boost | Virgil van Dijk | DEF | 12 | 6.3 | 4.24 | 12.89 | 21.34 | 8.00 | 87.1 | 90.0 |
| Bench 3 | Bench Boost | Konstantinos Mavropanos | DEF | 19 | 4.4 | 4.11 | 12.54 | 19.61 | 6.00 | 90.0 | 90.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 8.41 | 11.27 | 17.23 | 12.00 | 162.1 | 180.0 |
| XI | XI | Adrien Truffert | DEF | 4 | 4.6 | 8.02 | 11.12 | 17.70 | 13.00 | 175.8 | 180.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 10.87 | 16.17 | 26.41 | 0.00 | 179.8 | 0.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 11 | 5.6 | 8.91 | 11.52 | 17.46 | 8.00 | 166.3 | 180.0 |
| Bench 4 | Bench Boost | Lyle Foster | FWD | 3 | 4.9 | 1.94 | 3.43 | 6.06 | 2.00 | 50.8 | 44.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.53 | 19.36 | 32.35 | 6.00 | 90.0 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.5 | 12.46 | 17.36 | 27.98 | 2.00 | 180.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.0 | 5.39 | 16.32 | 27.66 | 10.00 | 74.7 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.37 | 13.06 | 21.03 | 5.00 | 80.8 | 90.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 8.45 | 11.83 | 18.77 | 16.00 | 173.4 | 180.0 |

## GW34

- Train rows: 186843
- Bank: 0.40 -> 0.40
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Mohamed Salah
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 54.03
- Actual score: 38.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.96) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: João Pedro Junqueira de Jesus -> Jarrod Bowen (projected gain 10.39, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (5.96) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 0.00 | 8.34 | 16.25 | 0.00 | 0.0 | 0.0 |
| XI | XI | Emiliano Martínez Romero | GK | 2 | 5.1 | 2.59 | 7.56 | 12.53 | 3.00 | 73.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 6.39 | 17.69 | 28.08 | 4.00 | 90.0 | 90.0 |
| XI | XI | Konstantinos Mavropanos | DEF | 19 | 4.4 | 4.70 | 13.03 | 20.73 | 4.00 | 90.0 | 90.0 |
| XI | Bench | Marcos Senesi Barón | DEF | 4 | 5.1 | 0.00 | 10.32 | 19.92 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 6 | 4.5 | 0.00 | 10.09 | 19.60 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Adrien Truffert | DEF | 4 | 4.6 | 0.00 | 9.86 | 19.04 | 0.00 | 0.0 | 0.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 6.39 | 17.21 | 27.49 | 10.00 | 90.0 | 90.0 |
| XI | Bench | Dominic Calvert-Lewin | FWD | 11 | 5.6 | 0.00 | 8.82 | 16.70 | 0.00 | 0.0 | 0.0 |
| Bench 4 | Bench | Lyle Foster | FWD | 3 | 4.9 | 0.00 | 4.76 | 9.69 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.46 | 21.22 | 35.32 | 5.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.0 | 6.55 | 19.17 | 31.83 | 1.00 | 90.0 | 58.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.03 | 14.02 | 22.51 | 1.00 | 90.0 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 0.00 | 10.14 | 20.79 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Pascal Groß | MID | 6 | 5.5 | 0.00 | 10.10 | 19.79 | 0.00 | 0.0 | 0.0 |