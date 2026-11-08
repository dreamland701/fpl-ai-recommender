# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 249.75
- Total actual points: 210.00
- Average predicted points: 62.44
- Average actual points: 52.50
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
- Bank: 100.00 -> 0.20
- Free transfers: 1 -> 2
- Captain: Morgan Rogers
- Vice captain: Cole Palmer
- Effective captain: Morgan Rogers
- Chip used: none
- Predicted score: 54.42
- Actual score: 54.00
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 5.6 | 3.72 | 11.15 | 18.41 | 7.00 | 88.7 | 90.0 |
| XI | XI | Emiliano Martínez Romero | GK | 2 | 5.1 | 3.92 | 10.69 | 16.62 | 6.00 | 84.4 | 90.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 6 | 4.4 | 3.62 | 12.95 | 19.63 | 4.00 | 83.5 | 90.0 |
| XI | XI | Ezri Konsa Ngoyo | DEF | 2 | 4.4 | 3.86 | 12.05 | 16.76 | 6.00 | 85.9 | 90.0 |
| Bench 4 | Bench | Marc Cucurella Saseta | DEF | 7 | 6.0 | 3.60 | 11.89 | 18.03 | 1.00 | 71.8 | 90.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 4.27 | 11.47 | 18.16 | 0.00 | 85.7 | 36.0 |
| XI | XI | Joachim Andersen | DEF | 10 | 4.6 | 4.08 | 10.18 | 17.91 | 4.00 | 77.9 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 4.85 | 16.32 | 23.77 | 2.00 | 84.4 | 77.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.37 | 14.99 | 23.41 | 4.00 | 85.4 | 90.0 |
| Bench 2 | Bench | Dominic Calvert-Lewin | FWD | 11 | 5.6 | 3.87 | 10.67 | 16.41 | 2.00 | 79.7 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.6 | 5.13 | 18.77 | 33.03 | 2.00 | 81.6 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 4.07 | 17.52 | 26.47 | 13.00 | 88.6 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.47 | 14.92 | 24.88 | 3.00 | 89.5 | 90.0 |
| Captain | Captain | Morgan Rogers | MID | 2 | 7.5 | 5.55 | 14.64 | 22.60 | 6.00 | 87.4 | 76.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.6 | 4.31 | 14.39 | 25.57 | 2.00 | 76.6 | 70.0 |

## GW32

- Train rows: 185188
- Bank: 0.20 -> 0.30
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Cole Palmer
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 61.14
- Actual score: 47.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.72) beats the best remaining Bench Boost opportunity (16.01).
- Transfer: Morgan Rogers -> Declan Rice (projected gain 3.76, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.72) beats the best remaining Bench Boost opportunity (16.01).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.6 | 3.18 | 9.38 | 16.40 | 0.00 | 85.1 | 90.0 |
| Bench 1 | Bench Boost | Emiliano Martínez Romero | GK | 2 | 5.1 | 2.49 | 6.52 | 11.65 | 0.00 | 63.3 | 0.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.4 | 4.57 | 12.66 | 22.69 | 5.00 | 84.5 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 2.55 | 9.73 | 16.91 | 0.00 | 69.0 | 90.0 |
| XI | XI | Ezri Konsa Ngoyo | DEF | 2 | 4.4 | 3.28 | 8.64 | 15.74 | 0.00 | 79.8 | 0.0 |
| Bench 3 | Bench Boost | Joachim Andersen | DEF | 10 | 4.6 | 1.37 | 7.17 | 10.92 | 1.00 | 48.7 | 90.0 |
| Bench 4 | Bench Boost | Malick Thiaw | DEF | 15 | 5.1 | 0.69 | 3.16 | 6.92 | 2.00 | 13.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.27 | 12.36 | 22.36 | 13.00 | 84.6 | 90.0 |
| Bench 2 | Bench Boost | Dominic Calvert-Lewin | FWD | 11 | 5.6 | 3.16 | 12.25 | 18.88 | 2.00 | 83.5 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 4.37 | 11.71 | 21.31 | 2.00 | 69.5 | 81.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.6 | 5.38 | 16.36 | 23.46 | 4.00 | 77.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.43 | 15.92 | 22.89 | 4.00 | 82.4 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 4.00 | 13.08 | 18.60 | 4.00 | 63.2 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 3.86 | 11.81 | 21.70 | 5.00 | 77.8 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.6 | 4.09 | 11.34 | 16.42 | 1.00 | 55.5 | 20.0 |

## GW33

- Train rows: 186014
- Bank: 0.30 -> 0.00
- Free transfers: 2 -> 2
- Captain: Dominic Calvert-Lewin
- Vice captain: Cole Palmer
- Effective captain: Dominic Calvert-Lewin
- Chip used: triple_captain
- Predicted score: 90.71
- Actual score: 72.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (15.13) beats the best remaining Triple Captain opportunity (5.31).
- Chip advisory: triple_captain (0.65): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Ezri Konsa Ngoyo -> Adrien Truffert (projected gain 7.97, hit 0)
- Chip used: Triple Captain on Dominic Calvert-Lewin. Optimizer chose Triple Captain here because the current estimated captain upside (15.13) beats the best remaining Triple Captain opportunity (5.31).
- Autosub: Malick Thiaw replaced João Pedro Junqueira de Jesus.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.6 | 3.24 | 9.06 | 16.49 | 1.00 | 86.4 | 90.0 |
| Bench 1 | Bench | Emiliano Martínez Romero | GK | 2 | 5.1 | 2.01 | 5.95 | 10.75 | 2.00 | 53.3 | 90.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 7.93 | 16.40 | 22.52 | 12.00 | 166.0 | 180.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 6.87 | 15.17 | 22.43 | 3.00 | 151.5 | 180.0 |
| XI | XI | Adrien Truffert | DEF | 4 | 4.7 | 7.43 | 14.60 | 20.16 | 13.00 | 164.4 | 180.0 |
| Bench 4 | Bench | Joachim Andersen | DEF | 10 | 4.5 | 2.26 | 7.17 | 10.79 | 6.00 | 52.5 | 90.0 |
| Bench 2 | Autosub In | Malick Thiaw | DEF | 15 | 5.1 | 2.67 | 6.85 | 14.58 | 1.00 | 46.4 | 90.0 |
| XI | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 8.35 | 17.21 | 23.56 | 0.00 | 150.3 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.46 | 13.31 | 23.78 | 2.00 | 75.3 | 90.0 |
| Captain | Captain | Dominic Calvert-Lewin | FWD | 11 | 5.6 | 10.53 | 12.99 | 21.79 | 8.00 | 154.4 | 180.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.5 | 9.68 | 20.66 | 30.35 | 2.00 | 161.6 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 5.55 | 18.55 | 25.03 | 6.00 | 81.9 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 2.80 | 10.95 | 20.34 | 5.00 | 68.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.5 | 2.79 | 9.44 | 13.09 | 3.00 | 48.4 | 86.0 |
| Bench 3 | Bench | Declan Rice | MID | 1 | 7.2 | 2.64 | 9.09 | 16.31 | 2.00 | 77.0 | 90.0 |

## GW34

- Train rows: 186843
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Dominik Szoboszlai
- Vice captain: Jarrod Bowen
- Effective captain: Dominik Szoboszlai
- Chip used: none
- Predicted score: 43.48
- Actual score: 37.00
- Transfer: João Pedro Junqueira de Jesus -> Jarrod Bowen (projected gain 2.65, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Emiliano Martínez Romero | GK | 2 | 5.1 | 3.24 | 10.67 | 16.75 | 3.00 | 84.7 | 90.0 |
| XI | XI | Jordan Pickford | GK | 9 | 5.6 | 3.45 | 9.40 | 16.14 | 1.00 | 85.9 | 90.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 1.95 | 10.70 | 16.75 | 2.00 | 87.5 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 10 | 4.5 | 3.58 | 10.63 | 16.14 | 11.00 | 86.1 | 90.0 |
| Bench 4 | Bench | Adrien Truffert | DEF | 4 | 4.7 | 0.00 | 10.33 | 17.89 | 0.00 | 2.3 | 0.0 |
| XI | Bench | Jan Paul van Hecke | DEF | 6 | 4.5 | 0.67 | 10.19 | 17.83 | 0.00 | 2.8 | 0.0 |
| Bench 3 | Bench | Marc Cucurella Saseta | DEF | 7 | 6.0 | 0.07 | 8.72 | 14.56 | 0.00 | 0.0 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.31 | 14.78 | 22.99 | 1.00 | 85.8 | 90.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.7 | 5.23 | 13.59 | 24.53 | 10.00 | 86.1 | 90.0 |
| XI | Bench | Dominic Calvert-Lewin | FWD | 11 | 5.6 | 0.17 | 12.55 | 15.96 | 0.00 | 1.1 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 5.08 | 16.59 | 29.02 | 5.00 | 88.2 | 90.0 |
| Captain | Captain | Dominik Szoboszlai | MID | 12 | 7.0 | 5.25 | 13.90 | 22.52 | 1.00 | 86.5 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 4.49 | 12.86 | 21.13 | 2.00 | 86.1 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.5 | 4.06 | 12.63 | 19.80 | 3.00 | 66.4 | 73.0 |
| Bench 2 | Bench | Cole Palmer | MID | 7 | 10.5 | 0.08 | 12.11 | 21.11 | 0.00 | 1.3 | 0.0 |