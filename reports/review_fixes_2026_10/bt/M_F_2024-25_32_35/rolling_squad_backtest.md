# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 256.70
- Total actual points: 215.00
- Average predicted points: 64.17
- Average actual points: 53.75
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
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Daniel Muñoz
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 64.09
- Actual score: 57.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (9.81) beats the best remaining Triple Captain opportunity (14.80).
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (9.81) beats the best remaining Triple Captain opportunity (14.80).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.64 | 10.92 | 17.95 | 2.00 | 84.9 | 90.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 5.1 | 3.24 | 9.90 | 16.39 | 3.00 | 86.4 | 90.0 |
| Vice Captain | XI | Daniel Muñoz | DEF | 7 | 5.2 | 4.64 | 12.05 | 19.04 | -1.00 | 100.4 | 180.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.1 | 3.86 | 11.59 | 18.93 | 1.00 | 87.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.5 | 3.59 | 10.65 | 17.70 | 9.00 | 79.2 | 90.0 |
| Bench 3 | Bench | Nikola Milenković | DEF | 16 | 5.0 | 3.25 | 9.94 | 16.14 | 2.00 | 82.6 | 90.0 |
| Bench 2 | Bench | Rayan Aït-Nouri | DEF | 20 | 4.8 | 3.54 | 9.84 | 16.17 | 14.00 | 73.6 | 69.0 |
| XI | XI | Omar Marmoush | FWD | 13 | 7.5 | 4.47 | 12.76 | 20.75 | 7.00 | 76.5 | 81.0 |
| XI | XI | Francisco Evanilson de Lima Barbosa | FWD | 3 | 5.7 | 3.65 | 10.00 | 15.93 | 2.00 | 66.3 | 90.0 |
| Bench 4 | Bench | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.0 | 2.57 | 8.66 | 14.75 | 1.00 | 59.4 | 26.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.68 | 23.36 | 39.20 | 6.00 | 95.7 | 84.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.6 | 4.49 | 14.21 | 24.38 | 2.00 | 89.4 | 81.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.51 | 14.19 | 23.93 | 2.00 | 88.0 | 90.0 |
| XI | XI | Luis Díaz | MID | 12 | 7.5 | 4.15 | 12.65 | 21.45 | 9.00 | 60.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.5 | 4.03 | 11.44 | 18.75 | 6.00 | 76.3 | 84.0 |

## GW33

- Train rows: 156471
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Omar Marmoush
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 78.45
- Actual score: 78.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (18.80) beats the best remaining Bench Boost opportunity (11.66).
- Transfer: Virgil van Dijk -> William Saliba (projected gain 0.17, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (18.80) beats the best remaining Bench Boost opportunity (11.66).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.91 | 12.19 | 19.44 | 7.00 | 112.4 | 180.0 |
| Bench 1 | Bench Boost | Matz Sels | GK | 16 | 5.1 | 3.22 | 9.83 | 16.34 | 2.00 | 90.7 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 5.26 | 14.01 | 21.75 | 6.00 | 135.7 | 180.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.1 | 5.14 | 12.87 | 20.48 | 7.00 | 113.5 | 180.0 |
| XI | XI | William Saliba | DEF | 1 | 6.5 | 5.10 | 12.18 | 18.82 | 7.00 | 108.4 | 180.0 |
| Bench 2 | Bench Boost | Rayan Aït-Nouri | DEF | 20 | 4.8 | 3.65 | 11.06 | 18.35 | 5.00 | 75.7 | 81.0 |
| Bench 3 | Bench Boost | Nikola Milenković | DEF | 16 | 5.0 | 3.31 | 10.03 | 16.29 | 2.00 | 84.6 | 90.0 |
| Vice Captain | XI | Omar Marmoush | FWD | 13 | 7.5 | 6.39 | 15.30 | 24.33 | 4.00 | 107.9 | 180.0 |
| XI | XI | Francisco Evanilson de Lima Barbosa | FWD | 3 | 5.7 | 3.89 | 11.98 | 18.48 | 2.00 | 66.8 | 90.0 |
| Bench 4 | Bench Boost | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.9 | 1.91 | 6.57 | 11.16 | 1.00 | 45.9 | 27.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.73 | 22.77 | 37.86 | 3.00 | 97.4 | 90.0 |
| XI | XI | Luis Díaz | MID | 12 | 7.5 | 5.46 | 15.00 | 24.70 | 3.00 | 80.3 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.0 | 4.94 | 14.73 | 24.45 | 18.00 | 85.3 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.6 | 4.66 | 14.42 | 24.08 | 1.00 | 84.2 | 31.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.5 | 5.13 | 13.03 | 20.78 | 7.00 | 109.2 | 166.0 |

## GW34

- Train rows: 157270
- Bank: 0.10 -> 1.90
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 61.20
- Actual score: 42.00
- Transfer: Bruno Borges Fernandes -> Leandro Trossard (projected gain 1.65, hit 0)
- Autosub: Matz Sels replaced David Raya Martin.
- Autosub: Francisco Evanilson de Lima Barbosa replaced Daniel Muñoz.
- Autosub: Nikola Milenković replaced William Saliba.
- Autosub: Norberto Bercique Gomes Betuncal replaced Leandro Trossard.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martin | GK | 1 | 5.5 | 4.10 | 12.91 | 20.85 | 0.00 | 101.1 | 0.0 |
| Bench 1 | Autosub In | Matz Sels | GK | 16 | 5.1 | 3.10 | 9.29 | 15.65 | 1.00 | 89.2 | 90.0 |
| XI | Bench | Joško Gvardiol | DEF | 13 | 6.1 | 4.27 | 13.75 | 22.48 | 0.00 | 102.1 | 0.0 |
| XI | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 4.48 | 13.64 | 22.49 | 0.00 | 109.7 | 0.0 |
| XI | Bench | William Saliba | DEF | 1 | 6.5 | 4.35 | 13.38 | 21.08 | 0.00 | 98.9 | 0.0 |
| XI | XI | Rayan Aït-Nouri | DEF | 20 | 4.8 | 4.10 | 11.38 | 18.58 | 11.00 | 75.4 | 76.0 |
| Bench 3 | Autosub In | Nikola Milenković | DEF | 16 | 5.0 | 3.20 | 9.80 | 16.31 | 1.00 | 85.9 | 90.0 |
| XI | Bench | Omar Marmoush | FWD | 13 | 7.6 | 5.28 | 16.42 | 26.14 | 0.00 | 88.6 | 0.0 |
| Bench 2 | Autosub In | Francisco Evanilson de Lima Barbosa | FWD | 3 | 5.7 | 3.72 | 10.40 | 16.59 | 2.00 | 67.9 | 69.0 |
| Bench 4 | Autosub In | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 1.63 | 5.96 | 10.26 | 2.00 | 44.4 | 63.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.45 | 20.91 | 34.51 | 8.00 | 94.1 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.46 | 16.82 | 27.97 | 2.00 | 95.6 | 90.0 |
| XI | Bench | Morgan Rogers | MID | 2 | 5.6 | 4.68 | 14.52 | 23.44 | 0.00 | 88.7 | 0.0 |
| XI | Bench | Leandro Trossard | MID | 1 | 6.7 | 4.72 | 14.26 | 23.11 | 0.00 | 95.9 | 0.0 |
| XI | XI | Luis Díaz | MID | 12 | 7.5 | 4.86 | 14.00 | 22.83 | 7.00 | 78.8 | 75.0 |

## GW35

- Train rows: 158070
- Bank: 1.90 -> 1.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 52.96
- Actual score: 38.00
- Transfer: Leandro Trossard -> Jarrod Bowen (projected gain 5.30, hit 0)
- Autosub: Daniel Muñoz replaced Luis Díaz.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Matz Sels | GK | 16 | 5.1 | 3.14 | 9.64 | 15.63 | 1.00 | 85.2 | 90.0 |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.5 | 2.93 | 8.78 | 15.00 | 1.00 | 62.8 | 90.0 |
| XI | XI | Rayan Aït-Nouri | DEF | 20 | 4.9 | 3.73 | 12.61 | 19.24 | 2.00 | 74.5 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.1 | 3.13 | 9.67 | 16.67 | 8.00 | 66.4 | 90.0 |
| XI | XI | Nikola Milenković | DEF | 16 | 5.0 | 3.16 | 9.54 | 15.36 | 2.00 | 81.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.5 | 3.10 | 8.97 | 15.09 | 1.00 | 60.9 | 90.0 |
| Bench 2 | Autosub In | Daniel Muñoz | DEF | 7 | 5.2 | 2.85 | 8.91 | 15.09 | 1.00 | 68.3 | 90.0 |
| XI | XI | Omar Marmoush | FWD | 13 | 7.6 | 3.87 | 11.62 | 19.72 | 2.00 | 55.0 | 82.0 |
| Bench 3 | Bench | Francisco Evanilson de Lima Barbosa | FWD | 3 | 5.7 | 2.43 | 9.19 | 15.08 | 6.00 | 58.3 | 86.0 |
| Bench 4 | Bench | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 2.30 | 6.52 | 10.84 | 6.00 | 50.6 | 76.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.14 | 21.24 | 34.82 | 2.00 | 95.9 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.0 | 5.85 | 17.49 | 27.51 | 5.00 | 88.1 | 90.0 |
| XI | Bench | Luis Díaz | MID | 12 | 7.5 | 4.50 | 14.28 | 22.26 | 0.00 | 76.3 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.6 | 4.88 | 14.20 | 22.59 | 9.00 | 84.7 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 3.33 | 10.40 | 17.81 | 3.00 | 54.8 | 90.0 |