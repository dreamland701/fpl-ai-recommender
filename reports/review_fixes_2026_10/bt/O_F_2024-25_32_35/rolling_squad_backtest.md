# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 260.23
- Total actual points: 225.00
- Average predicted points: 65.06
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
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Daniel Muñoz
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 71.11
- Actual score: 83.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (17.73) beats the best remaining Bench Boost opportunity (20.70).
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (17.73) beats the best remaining Bench Boost opportunity (20.70).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.62 | 10.91 | 17.86 | 2.00 | 84.9 | 90.0 |
| Bench 1 | Bench Boost | Matz Sels | GK | 16 | 5.1 | 3.23 | 9.90 | 16.45 | 3.00 | 86.4 | 90.0 |
| Vice Captain | XI | Daniel Muñoz | DEF | 7 | 5.2 | 4.65 | 12.14 | 19.16 | -1.00 | 100.4 | 180.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.1 | 3.85 | 11.61 | 18.86 | 1.00 | 87.8 | 90.0 |
| Bench 2 | Bench Boost | Virgil van Dijk | DEF | 12 | 6.5 | 3.62 | 10.65 | 17.68 | 9.00 | 79.1 | 90.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.5 | 4.25 | 10.04 | 15.27 | 8.00 | 96.7 | 180.0 |
| Bench 3 | Bench Boost | Rayan Aït-Nouri | DEF | 20 | 4.8 | 3.57 | 9.89 | 16.08 | 14.00 | 73.6 | 69.0 |
| XI | XI | Omar Marmoush | FWD | 13 | 7.5 | 4.46 | 12.76 | 20.64 | 7.00 | 76.5 | 81.0 |
| XI | XI | Francisco Evanilson de Lima Barbosa | FWD | 3 | 5.7 | 3.65 | 9.92 | 15.69 | 2.00 | 66.3 | 90.0 |
| Bench 4 | Bench Boost | Jørgen Strand Larsen | FWD | 20 | 5.3 | 3.48 | 9.39 | 15.03 | 6.00 | 71.1 | 69.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.71 | 23.48 | 39.19 | 6.00 | 95.7 | 84.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.6 | 4.51 | 14.26 | 24.36 | 2.00 | 89.3 | 81.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.49 | 14.18 | 23.78 | 2.00 | 88.1 | 90.0 |
| XI | XI | Luis Díaz | MID | 12 | 7.5 | 4.18 | 12.64 | 21.39 | 9.00 | 60.0 | 90.0 |
| XI | XI | Ismaïla Sarr | MID | 7 | 5.7 | 4.14 | 12.32 | 19.67 | 7.00 | 86.3 | 165.0 |

## GW33

- Train rows: 156471
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Omar Marmoush
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 74.61
- Actual score: 65.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (12.33) beats the best remaining Triple Captain opportunity (8.71).
- Transfer: Virgil van Dijk -> William Saliba (projected gain 0.18, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (12.33) beats the best remaining Triple Captain opportunity (8.71).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.91 | 12.20 | 19.39 | 7.00 | 112.4 | 180.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 5.1 | 3.25 | 9.81 | 16.34 | 2.00 | 90.6 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 5.24 | 14.00 | 21.64 | 6.00 | 135.7 | 180.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 5.14 | 12.87 | 20.41 | 7.00 | 113.5 | 180.0 |
| XI | XI | William Saliba | DEF | 1 | 6.5 | 5.10 | 12.20 | 18.73 | 7.00 | 108.4 | 180.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 4.09 | 12.13 | 18.96 | 0.00 | 111.1 | 90.0 |
| Bench 3 | Bench | Rayan Aït-Nouri | DEF | 20 | 4.8 | 3.66 | 11.16 | 18.37 | 5.00 | 75.6 | 81.0 |
| Vice Captain | XI | Omar Marmoush | FWD | 13 | 7.6 | 6.39 | 15.36 | 24.06 | 4.00 | 107.9 | 180.0 |
| Bench 2 | Bench | Francisco Evanilson de Lima Barbosa | FWD | 3 | 5.8 | 3.87 | 11.80 | 18.43 | 2.00 | 66.8 | 90.0 |
| Bench 4 | Bench | Jørgen Strand Larsen | FWD | 20 | 5.4 | 3.39 | 9.69 | 15.66 | 2.00 | 66.3 | 73.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.73 | 22.81 | 37.86 | 3.00 | 97.4 | 90.0 |
| XI | XI | Luis Díaz | MID | 12 | 7.5 | 5.46 | 14.98 | 24.54 | 3.00 | 80.3 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.0 | 4.92 | 14.74 | 24.36 | 18.00 | 85.4 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.6 | 4.69 | 14.51 | 24.25 | 1.00 | 84.2 | 31.0 |
| XI | XI | Ismaïla Sarr | MID | 7 | 5.8 | 5.48 | 14.31 | 22.42 | 3.00 | 131.6 | 117.0 |

## GW34

- Train rows: 157270
- Bank: 0.10 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 60.43
- Actual score: 41.00
- Transfer: Ismaïla Sarr -> Morgan Rogers (projected gain 4.11, hit 0)
- Autosub: Matz Sels replaced David Raya Martin.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martin | GK | 1 | 5.6 | 4.10 | 12.91 | 20.78 | 0.00 | 101.1 | 0.0 |
| Bench 1 | Autosub In | Matz Sels | GK | 16 | 5.1 | 3.08 | 9.26 | 15.64 | 1.00 | 89.3 | 90.0 |
| XI | Bench | Joško Gvardiol | DEF | 13 | 6.2 | 4.27 | 13.72 | 22.36 | 0.00 | 102.1 | 0.0 |
| XI | Bench | Daniel Muñoz | DEF | 7 | 5.3 | 4.48 | 13.67 | 22.45 | 0.00 | 109.7 | 0.0 |
| XI | Bench | William Saliba | DEF | 1 | 6.6 | 4.35 | 13.35 | 20.95 | 0.00 | 98.9 | 0.0 |
| XI | XI | Rayan Aït-Nouri | DEF | 20 | 4.9 | 4.10 | 11.41 | 18.52 | 11.00 | 75.4 | 76.0 |
| Bench 4 | Bench | Tino Livramento | DEF | 15 | 4.6 | 3.67 | 10.14 | 16.66 | 6.00 | 85.3 | 90.0 |
| XI | Bench | Omar Marmoush | FWD | 13 | 7.7 | 5.28 | 16.32 | 25.86 | 0.00 | 88.6 | 0.0 |
| Bench 2 | Bench | Francisco Evanilson de Lima Barbosa | FWD | 3 | 5.8 | 3.73 | 10.38 | 16.52 | 2.00 | 67.9 | 69.0 |
| Bench 3 | Bench | Jørgen Strand Larsen | FWD | 20 | 5.4 | 3.69 | 9.82 | 15.81 | 6.00 | 62.9 | 76.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.47 | 21.01 | 34.49 | 8.00 | 94.0 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.48 | 16.86 | 28.11 | 2.00 | 95.6 | 90.0 |
| XI | Bench | Morgan Rogers | MID | 2 | 5.7 | 4.68 | 14.49 | 23.29 | 0.00 | 88.7 | 0.0 |
| XI | XI | Luis Díaz | MID | 12 | 7.5 | 4.89 | 14.01 | 22.72 | 7.00 | 78.7 | 75.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 3.86 | 12.64 | 21.69 | 4.00 | 66.4 | 90.0 |

## GW35

- Train rows: 158070
- Bank: 0.20 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 54.08
- Actual score: 36.00
- Transfer: William Saliba -> Kieran Trippier (projected gain 2.27, hit 0)
- Autosub outfielders: Joško Gvardiol, Daniel Muñoz, Francisco Evanilson de Lima Barbosa.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Matz Sels | GK | 16 | 5.1 | 3.12 | 9.64 | 15.67 | 1.00 | 85.2 | 90.0 |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.6 | 2.90 | 8.76 | 14.91 | 1.00 | 62.8 | 90.0 |
| XI | XI | Rayan Aït-Nouri | DEF | 20 | 5.0 | 3.74 | 12.55 | 19.46 | 2.00 | 74.5 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 5.6 | 3.96 | 11.90 | 19.17 | 2.00 | 85.3 | 90.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.62 | 10.21 | 16.65 | 2.00 | 86.1 | 90.0 |
| Bench 2 | Autosub In | Joško Gvardiol | DEF | 13 | 6.2 | 3.16 | 9.64 | 16.53 | 8.00 | 66.3 | 90.0 |
| Bench 3 | Autosub In | Daniel Muñoz | DEF | 7 | 5.3 | 2.87 | 8.90 | 15.04 | 1.00 | 68.2 | 90.0 |
| XI | XI | Omar Marmoush | FWD | 13 | 7.7 | 3.91 | 11.54 | 19.44 | 2.00 | 54.9 | 82.0 |
| XI | Bench | Jørgen Strand Larsen | FWD | 20 | 5.4 | 3.27 | 10.10 | 16.40 | 0.00 | 64.7 | 0.0 |
| Bench 4 | Autosub In | Francisco Evanilson de Lima Barbosa | FWD | 3 | 5.8 | 2.40 | 9.12 | 15.06 | 6.00 | 58.3 | 86.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.12 | 21.16 | 34.74 | 2.00 | 96.0 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.0 | 5.86 | 17.35 | 27.43 | 5.00 | 88.1 | 90.0 |
| XI | Bench | Luis Díaz | MID | 12 | 7.6 | 4.48 | 14.14 | 22.27 | 0.00 | 76.3 | 0.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.54 | 13.71 | 22.78 | 0.00 | 79.5 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.7 | 3.32 | 10.34 | 17.64 | 3.00 | 54.8 | 90.0 |