# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 266.68
- Total actual points: 234.00
- Average predicted points: 66.67
- Average actual points: 58.50
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW31 are included before the first simulated week.
- League-average scores were not available for this run.

## GW32

- Train rows: 155673
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Daniel Muñoz
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 66.76
- Actual score: 62.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (9.87) beats the best remaining Triple Captain opportunity (15.51).
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (9.87) beats the best remaining Triple Captain opportunity (15.51).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.85 | 11.42 | 18.75 | 2.00 | 87.7 | 90.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 5.1 | 3.47 | 10.41 | 17.19 | 3.00 | 89.3 | 90.0 |
| Vice Captain | XI | Daniel Muñoz | DEF | 7 | 5.2 | 4.94 | 12.68 | 20.05 | -1.00 | 104.1 | 180.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.1 | 4.04 | 11.88 | 19.36 | 1.00 | 88.3 | 90.0 |
| XI | XI | Rayan Aït-Nouri | DEF | 20 | 4.8 | 3.82 | 10.61 | 17.38 | 14.00 | 77.4 | 69.0 |
| Bench 3 | Bench | Nikola Milenković | DEF | 16 | 5.0 | 3.54 | 10.55 | 17.09 | 2.00 | 85.4 | 90.0 |
| Bench 4 | Bench | Diogo Dalot Teixeira | DEF | 14 | 5.0 | 3.28 | 9.91 | 16.52 | 3.00 | 82.5 | 90.0 |
| XI | XI | Omar Marmoush | FWD | 13 | 7.5 | 4.77 | 13.50 | 21.81 | 7.00 | 77.1 | 81.0 |
| Bench 2 | Bench | Yoane Wissa | FWD | 4 | 6.6 | 3.69 | 11.94 | 19.96 | 9.00 | 78.6 | 90.0 |
| XI | XI | Francisco Evanilson de Lima Barbosa | FWD | 3 | 5.7 | 3.89 | 10.66 | 16.93 | 2.00 | 68.1 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.74 | 23.19 | 38.98 | 6.00 | 95.6 | 84.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.90 | 15.20 | 25.45 | 2.00 | 91.2 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.6 | 4.76 | 14.93 | 25.38 | 2.00 | 89.2 | 81.0 |
| XI | XI | Luis Díaz | MID | 12 | 7.5 | 4.36 | 12.96 | 21.95 | 9.00 | 61.9 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.5 | 4.21 | 12.10 | 19.82 | 6.00 | 80.0 | 84.0 |

## GW33

- Train rows: 156471
- Bank: 0.00 -> 0.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Omar Marmoush
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 81.11
- Actual score: 81.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (20.62) beats the best remaining Bench Boost opportunity (12.69).
- Chip advisory: bench_boost (0.63): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Transfer: Diogo Dalot Teixeira -> Tino Livramento (projected gain 1.10, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (20.62) beats the best remaining Bench Boost opportunity (12.69).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.98 | 12.38 | 19.77 | 7.00 | 113.6 | 180.0 |
| Bench 1 | Bench Boost | Matz Sels | GK | 16 | 5.1 | 3.34 | 10.18 | 16.93 | 2.00 | 93.0 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 5.44 | 14.48 | 22.50 | 6.00 | 138.2 | 180.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.1 | 5.23 | 13.00 | 20.68 | 7.00 | 112.9 | 180.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 4.41 | 12.82 | 20.07 | 0.00 | 112.1 | 90.0 |
| Bench 2 | Bench Boost | Rayan Aït-Nouri | DEF | 20 | 4.8 | 3.97 | 11.77 | 19.53 | 5.00 | 79.8 | 81.0 |
| Bench 4 | Bench Boost | Nikola Milenković | DEF | 16 | 5.0 | 3.46 | 10.43 | 16.95 | 2.00 | 87.2 | 90.0 |
| Vice Captain | XI | Omar Marmoush | FWD | 13 | 7.5 | 6.64 | 16.17 | 25.44 | 4.00 | 108.3 | 180.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.19 | 12.37 | 20.43 | 11.00 | 81.7 | 90.0 |
| Bench 3 | Bench Boost | Francisco Evanilson de Lima Barbosa | FWD | 3 | 5.7 | 3.60 | 10.41 | 16.65 | 2.00 | 67.6 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.57 | 22.37 | 37.24 | 3.00 | 95.4 | 90.0 |
| XI | XI | Luis Díaz | MID | 12 | 7.5 | 5.54 | 15.20 | 25.10 | 3.00 | 83.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.0 | 5.03 | 14.85 | 24.74 | 18.00 | 87.5 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.6 | 4.70 | 14.39 | 24.01 | 1.00 | 83.4 | 31.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.5 | 5.44 | 13.85 | 21.93 | 7.00 | 110.4 | 166.0 |

## GW34

- Train rows: 157270
- Bank: 0.40 -> 2.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 61.78
- Actual score: 53.00
- Transfer: Bruno Borges Fernandes -> Leandro Trossard (projected gain 3.44, hit 0)
- Autosub: Matz Sels replaced David Raya Martin.
- Autosub: Tino Livramento replaced Daniel Muñoz.
- Autosub: Nikola Milenković replaced Joško Gvardiol.
- Autosub: Francisco Evanilson de Lima Barbosa replaced Morgan Rogers.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martin | GK | 1 | 5.5 | 4.14 | 13.01 | 21.01 | 0.00 | 101.6 | 0.0 |
| Bench 1 | Autosub In | Matz Sels | GK | 16 | 5.1 | 3.24 | 9.63 | 16.21 | 1.00 | 91.3 | 90.0 |
| XI | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 4.69 | 14.24 | 23.47 | 0.00 | 113.5 | 0.0 |
| XI | Bench | Joško Gvardiol | DEF | 13 | 6.1 | 4.27 | 13.74 | 22.47 | 0.00 | 102.0 | 0.0 |
| XI | XI | Rayan Aït-Nouri | DEF | 20 | 4.8 | 4.30 | 12.02 | 19.61 | 11.00 | 79.4 | 76.0 |
| Bench 3 | Autosub In | Tino Livramento | DEF | 15 | 4.6 | 3.69 | 10.26 | 16.98 | 6.00 | 87.3 | 90.0 |
| Bench 4 | Autosub In | Nikola Milenković | DEF | 16 | 5.0 | 3.37 | 10.20 | 16.96 | 1.00 | 88.7 | 90.0 |
| XI | Bench | Omar Marmoush | FWD | 13 | 7.6 | 5.26 | 16.36 | 26.04 | 0.00 | 88.2 | 0.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.32 | 13.03 | 21.46 | 7.00 | 87.5 | 90.0 |
| Bench 2 | Autosub In | Francisco Evanilson de Lima Barbosa | FWD | 3 | 5.7 | 4.00 | 10.90 | 17.47 | 2.00 | 71.1 | 69.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.25 | 20.25 | 33.55 | 8.00 | 91.3 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.78 | 17.48 | 29.03 | 2.00 | 98.5 | 90.0 |
| XI | Bench | Morgan Rogers | MID | 2 | 5.6 | 4.87 | 15.02 | 24.25 | 0.00 | 91.8 | 0.0 |
| XI | Bench | Leandro Trossard | MID | 1 | 6.7 | 4.74 | 14.33 | 23.23 | 0.00 | 96.3 | 0.0 |
| XI | XI | Luis Díaz | MID | 12 | 7.5 | 4.90 | 13.97 | 22.87 | 7.00 | 80.0 | 75.0 |

## GW35

- Train rows: 158070
- Bank: 2.20 -> 2.90
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 57.03
- Actual score: 38.00
- Transfer: Leandro Trossard -> Harvey Barnes (projected gain 4.43, hit 0)
- Autosub: Joško Gvardiol replaced Luis Díaz.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Matz Sels | GK | 16 | 5.1 | 3.23 | 10.00 | 16.20 | 1.00 | 87.4 | 90.0 |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.5 | 3.12 | 9.26 | 15.78 | 1.00 | 65.4 | 90.0 |
| XI | XI | Rayan Aït-Nouri | DEF | 20 | 4.9 | 4.28 | 13.70 | 20.96 | 2.00 | 79.1 | 90.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.66 | 10.46 | 17.03 | 2.00 | 87.9 | 90.0 |
| XI | XI | Nikola Milenković | DEF | 16 | 5.0 | 3.30 | 9.97 | 16.06 | 2.00 | 84.5 | 90.0 |
| Bench 2 | Autosub In | Joško Gvardiol | DEF | 13 | 6.1 | 3.23 | 9.80 | 16.88 | 8.00 | 67.2 | 90.0 |
| Bench 3 | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 3.08 | 9.56 | 16.14 | 1.00 | 72.0 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.6 | 4.80 | 13.57 | 21.99 | 7.00 | 87.8 | 90.0 |
| XI | XI | Omar Marmoush | FWD | 13 | 7.6 | 4.19 | 12.35 | 20.82 | 2.00 | 57.2 | 82.0 |
| Bench 4 | Bench | Francisco Evanilson de Lima Barbosa | FWD | 3 | 5.7 | 2.64 | 9.36 | 15.38 | 6.00 | 60.0 | 86.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.19 | 21.20 | 34.72 | 2.00 | 93.9 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.0 | 6.07 | 17.68 | 27.86 | 5.00 | 90.4 | 90.0 |
| XI | Bench | Luis Díaz | MID | 12 | 7.5 | 4.90 | 15.01 | 23.39 | 0.00 | 78.7 | 0.0 |
| XI | XI | Harvey Barnes | MID | 15 | 6.0 | 4.59 | 14.22 | 22.68 | 2.00 | 80.1 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 3.64 | 11.20 | 19.10 | 3.00 | 59.4 | 90.0 |