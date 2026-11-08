# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 266.82
- Total actual points: 225.00
- Average predicted points: 66.71
- Average actual points: 56.25
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
- Predicted score: 66.86
- Actual score: 62.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (9.89) beats the best remaining Triple Captain opportunity (15.48).
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (9.89) beats the best remaining Triple Captain opportunity (15.48).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.82 | 11.39 | 18.61 | 2.00 | 87.7 | 90.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 5.1 | 3.46 | 10.39 | 17.22 | 3.00 | 89.3 | 90.0 |
| Vice Captain | XI | Daniel Muñoz | DEF | 7 | 5.2 | 4.95 | 12.73 | 20.12 | -1.00 | 104.1 | 180.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.1 | 4.03 | 11.87 | 19.23 | 1.00 | 88.3 | 90.0 |
| XI | XI | Rayan Aït-Nouri | DEF | 20 | 4.8 | 3.84 | 10.64 | 17.27 | 14.00 | 77.4 | 69.0 |
| Bench 3 | Bench | Nikola Milenković | DEF | 16 | 5.0 | 3.53 | 10.57 | 17.23 | 2.00 | 85.5 | 90.0 |
| Bench 4 | Bench | Diogo Dalot Teixeira | DEF | 14 | 5.0 | 3.30 | 9.96 | 16.53 | 3.00 | 82.5 | 90.0 |
| XI | XI | Omar Marmoush | FWD | 13 | 7.5 | 4.76 | 13.50 | 21.67 | 7.00 | 77.1 | 81.0 |
| Bench 2 | Bench | Yoane Wissa | FWD | 4 | 6.6 | 3.66 | 11.92 | 19.79 | 9.00 | 78.6 | 90.0 |
| XI | XI | Francisco Evanilson de Lima Barbosa | FWD | 3 | 5.7 | 3.89 | 10.59 | 16.67 | 2.00 | 68.1 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.77 | 23.27 | 38.91 | 6.00 | 95.5 | 84.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.86 | 15.18 | 25.28 | 2.00 | 91.2 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.6 | 4.77 | 14.97 | 25.33 | 2.00 | 89.2 | 81.0 |
| XI | XI | Luis Díaz | MID | 12 | 7.5 | 4.39 | 12.92 | 21.84 | 9.00 | 61.8 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.5 | 4.23 | 12.17 | 19.77 | 6.00 | 79.9 | 84.0 |

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
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (20.67) beats the best remaining Bench Boost opportunity (12.69).
- Chip advisory: bench_boost (0.63): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Transfer: Diogo Dalot Teixeira -> Tino Livramento (projected gain 1.10, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (20.67) beats the best remaining Bench Boost opportunity (12.69).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.98 | 12.38 | 19.69 | 7.00 | 113.6 | 180.0 |
| Bench 1 | Bench Boost | Matz Sels | GK | 16 | 5.1 | 3.37 | 10.16 | 16.91 | 2.00 | 93.0 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 5.42 | 14.46 | 22.37 | 6.00 | 138.3 | 180.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 5.23 | 12.99 | 20.56 | 7.00 | 112.9 | 180.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 4.38 | 12.89 | 20.08 | 0.00 | 112.1 | 90.0 |
| Bench 2 | Bench Boost | Rayan Aït-Nouri | DEF | 20 | 4.8 | 3.98 | 11.85 | 19.48 | 5.00 | 79.8 | 81.0 |
| Bench 4 | Bench Boost | Nikola Milenković | DEF | 16 | 5.1 | 3.48 | 10.47 | 17.12 | 2.00 | 87.1 | 90.0 |
| Vice Captain | XI | Omar Marmoush | FWD | 13 | 7.6 | 6.63 | 16.17 | 25.20 | 4.00 | 108.3 | 180.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.17 | 12.39 | 20.37 | 11.00 | 81.8 | 90.0 |
| Bench 3 | Bench Boost | Francisco Evanilson de Lima Barbosa | FWD | 3 | 5.8 | 3.59 | 10.32 | 16.37 | 2.00 | 67.6 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.57 | 22.41 | 37.23 | 3.00 | 95.4 | 90.0 |
| XI | XI | Luis Díaz | MID | 12 | 7.5 | 5.54 | 15.19 | 24.91 | 3.00 | 83.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.0 | 5.01 | 14.85 | 24.60 | 18.00 | 87.5 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.6 | 4.73 | 14.47 | 24.13 | 1.00 | 83.4 | 31.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 5.47 | 13.91 | 21.87 | 7.00 | 110.4 | 166.0 |

## GW34

- Train rows: 157270
- Bank: 0.40 -> 2.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 61.89
- Actual score: 44.00
- Transfer: Bruno Borges Fernandes -> Leandro Trossard (projected gain 3.53, hit 0)
- Autosub: Matz Sels replaced David Raya Martin.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martin | GK | 1 | 5.6 | 4.14 | 13.00 | 20.93 | 0.00 | 101.6 | 0.0 |
| Bench 1 | Autosub In | Matz Sels | GK | 16 | 5.1 | 3.21 | 9.59 | 16.16 | 1.00 | 91.4 | 90.0 |
| XI | Bench | Daniel Muñoz | DEF | 7 | 5.3 | 4.69 | 14.26 | 23.41 | 0.00 | 113.5 | 0.0 |
| XI | Bench | Joško Gvardiol | DEF | 13 | 6.2 | 4.27 | 13.70 | 22.32 | 0.00 | 102.0 | 0.0 |
| XI | XI | Rayan Aït-Nouri | DEF | 20 | 4.9 | 4.30 | 12.04 | 19.54 | 11.00 | 79.4 | 76.0 |
| Bench 3 | Bench | Tino Livramento | DEF | 15 | 4.6 | 3.68 | 10.25 | 16.88 | 6.00 | 87.3 | 90.0 |
| Bench 4 | Bench | Nikola Milenković | DEF | 16 | 5.1 | 3.35 | 10.16 | 17.02 | 1.00 | 88.7 | 90.0 |
| XI | Bench | Omar Marmoush | FWD | 13 | 7.7 | 5.26 | 16.26 | 25.76 | 0.00 | 88.2 | 0.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.34 | 13.05 | 21.47 | 7.00 | 87.4 | 90.0 |
| Bench 2 | Bench | Francisco Evanilson de Lima Barbosa | FWD | 3 | 5.8 | 4.01 | 10.88 | 17.34 | 2.00 | 71.1 | 69.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.27 | 20.34 | 33.48 | 8.00 | 91.3 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.80 | 17.51 | 29.12 | 2.00 | 98.5 | 90.0 |
| XI | Bench | Morgan Rogers | MID | 2 | 5.7 | 4.86 | 14.98 | 24.07 | 0.00 | 91.8 | 0.0 |
| XI | Bench | Leandro Trossard | MID | 1 | 6.7 | 4.74 | 14.40 | 23.27 | 0.00 | 96.3 | 0.0 |
| XI | XI | Luis Díaz | MID | 12 | 7.5 | 4.92 | 13.97 | 22.72 | 7.00 | 80.0 | 75.0 |

## GW35

- Train rows: 158070
- Bank: 2.20 -> 2.90
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 56.96
- Actual score: 38.00
- Transfer: Leandro Trossard -> Harvey Barnes (projected gain 4.43, hit 0)
- Autosub outfielders: Joško Gvardiol.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Matz Sels | GK | 16 | 5.1 | 3.22 | 9.99 | 16.23 | 1.00 | 87.5 | 90.0 |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.6 | 3.10 | 9.23 | 15.65 | 1.00 | 65.4 | 90.0 |
| XI | XI | Rayan Aït-Nouri | DEF | 20 | 5.0 | 4.29 | 13.64 | 21.14 | 2.00 | 79.1 | 90.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.64 | 10.44 | 17.03 | 2.00 | 87.9 | 90.0 |
| XI | XI | Nikola Milenković | DEF | 16 | 5.1 | 3.28 | 9.97 | 16.14 | 2.00 | 84.5 | 90.0 |
| Bench 2 | Autosub In | Joško Gvardiol | DEF | 13 | 6.2 | 3.26 | 9.77 | 16.71 | 8.00 | 67.2 | 90.0 |
| Bench 3 | Bench | Daniel Muñoz | DEF | 7 | 5.3 | 3.10 | 9.54 | 16.06 | 1.00 | 72.0 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.6 | 4.81 | 13.52 | 21.94 | 7.00 | 87.8 | 90.0 |
| XI | XI | Omar Marmoush | FWD | 13 | 7.7 | 4.22 | 12.30 | 20.60 | 2.00 | 57.1 | 82.0 |
| Bench 4 | Bench | Francisco Evanilson de Lima Barbosa | FWD | 3 | 5.8 | 2.61 | 9.30 | 15.39 | 6.00 | 60.1 | 86.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.17 | 21.13 | 34.65 | 2.00 | 93.9 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.0 | 6.07 | 17.55 | 27.79 | 5.00 | 90.4 | 90.0 |
| XI | Bench | Luis Díaz | MID | 12 | 7.6 | 4.88 | 14.90 | 23.39 | 0.00 | 78.8 | 0.0 |
| XI | XI | Harvey Barnes | MID | 15 | 6.0 | 4.57 | 14.18 | 22.78 | 2.00 | 80.1 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.7 | 3.64 | 11.14 | 18.92 | 3.00 | 59.4 | 90.0 |