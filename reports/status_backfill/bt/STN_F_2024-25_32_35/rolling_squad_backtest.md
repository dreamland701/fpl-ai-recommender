# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 277.74
- Total actual points: 221.00
- Average predicted points: 69.43
- Average actual points: 55.25
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
- Bank: 100.00 -> 0.20
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 76.73
- Actual score: 69.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (14.62) beats the best remaining Bench Boost opportunity (15.75).
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (14.62) beats the best remaining Bench Boost opportunity (15.75).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.88 | 11.22 | 18.05 | 2.00 | 92.6 | 90.0 |
| Bench 1 | Bench Boost | Will Dennis | GK | 3 | 3.9 | 0.33 | 0.81 | 1.31 | 0.00 | 10.8 | 0.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 5.04 | 12.57 | 19.33 | -1.00 | 109.9 | 180.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.22 | 12.34 | 19.81 | 1.00 | 96.7 | 90.0 |
| Bench 2 | Bench Boost | William Saliba | DEF | 1 | 6.5 | 3.94 | 11.68 | 18.41 | 2.00 | 84.7 | 90.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 4.79 | 10.98 | 16.53 | 8.00 | 106.4 | 180.0 |
| Bench 3 | Bench Boost | Neco Williams | DEF | 16 | 4.5 | 3.19 | 9.20 | 14.94 | 2.00 | 86.1 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 6.89 | 17.11 | 27.03 | 11.00 | 105.8 | 148.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 5.56 | 13.86 | 21.34 | 2.00 | 103.9 | 100.0 |
| Bench 4 | Bench Boost | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.9 | 2.43 | 8.11 | 13.63 | 1.00 | 60.2 | 26.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.18 | 24.47 | 40.63 | 6.00 | 108.8 | 84.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.6 | 4.77 | 14.78 | 25.39 | 2.00 | 93.9 | 81.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.0 | 4.38 | 14.18 | 23.81 | 2.00 | 89.3 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 6.05 | 13.57 | 20.23 | 19.00 | 111.8 | 138.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 4.92 | 12.62 | 20.16 | 6.00 | 88.8 | 84.0 |

## GW33

- Train rows: 156471
- Bank: 0.20 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Omar Marmoush
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 79.33
- Actual score: 68.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (12.82) beats the best remaining Triple Captain opportunity (9.35).
- Transfer: Jean-Philippe Mateta -> Omar Marmoush (projected gain 4.52, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (12.82) beats the best remaining Triple Captain opportunity (9.35).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 5.71 | 13.55 | 20.98 | 7.00 | 127.4 | 180.0 |
| Bench 1 | Bench | Will Dennis | GK | 3 | 3.9 | 0.14 | 0.58 | 0.96 | 0.00 | 9.3 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.5 | 6.34 | 15.07 | 23.09 | 7.00 | 129.3 | 180.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 5.96 | 14.51 | 22.49 | 7.00 | 127.9 | 180.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 5.15 | 13.26 | 20.29 | 6.00 | 134.6 | 180.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.44 | 10.60 | 16.90 | 0.00 | 99.1 | 90.0 |
| Bench 3 | Bench | Neco Williams | DEF | 16 | 4.5 | 2.95 | 8.52 | 14.12 | 2.00 | 84.1 | 90.0 |
| Vice Captain | XI | Omar Marmoush | FWD | 13 | 7.7 | 7.43 | 17.66 | 27.33 | 4.00 | 125.1 | 180.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.65 | 16.58 | 27.64 | 2.00 | 90.4 | 75.0 |
| Bench 4 | Bench | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 1.85 | 6.20 | 10.46 | 1.00 | 46.9 | 27.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.22 | 23.34 | 38.76 | 3.00 | 106.4 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 5.97 | 14.65 | 22.55 | 7.00 | 123.1 | 166.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.37 | 13.97 | 23.54 | 1.00 | 82.1 | 31.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 4.67 | 13.79 | 23.01 | 18.00 | 83.1 | 90.0 |
| Bench 2 | Bench | Jacob Murphy | MID | 15 | 5.2 | 3.38 | 10.84 | 18.02 | 2.00 | 70.1 | 64.0 |

## GW34

- Train rows: 157270
- Bank: 0.30 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 66.46
- Actual score: 42.00
- Transfer: none
- No transfer was applied this week.
- Autosub: Tino Livramento replaced William Saliba.
- Autosub: Neco Williams replaced Daniel Muñoz.
- Autosub: Norberto Bercique Gomes Betuncal replaced Morgan Rogers.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martin | GK | 1 | 5.5 | 3.81 | 12.17 | 19.73 | 0.00 | 97.1 | 0.0 |
| Bench 1 | Bench | Will Dennis | GK | 3 | 3.9 | 0.46 | 0.79 | 1.27 | 0.00 | 8.4 | 0.0 |
| XI | Bench | William Saliba | DEF | 1 | 6.5 | 4.29 | 13.63 | 21.96 | 0.00 | 98.2 | 0.0 |
| XI | Bench | Joško Gvardiol | DEF | 13 | 6.2 | 3.88 | 12.71 | 20.95 | 0.00 | 96.7 | 0.0 |
| XI | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 4.15 | 12.71 | 20.93 | 0.00 | 105.5 | 0.0 |
| Bench 2 | Autosub In | Tino Livramento | DEF | 15 | 4.6 | 3.84 | 10.05 | 16.28 | 6.00 | 86.2 | 90.0 |
| Bench 3 | Autosub In | Neco Williams | DEF | 16 | 4.5 | 2.89 | 8.27 | 13.82 | 0.00 | 84.5 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 7.42 | 19.16 | 30.49 | 6.00 | 101.4 | 76.0 |
| XI | Bench | Omar Marmoush | FWD | 13 | 7.7 | 4.76 | 15.20 | 24.38 | 0.00 | 80.1 | 0.0 |
| Bench 4 | Autosub In | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 1.65 | 5.76 | 9.88 | 2.00 | 46.5 | 63.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.50 | 22.99 | 37.14 | 8.00 | 112.7 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.0 | 7.37 | 20.46 | 32.40 | 2.00 | 128.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.59 | 14.03 | 23.61 | 4.00 | 79.4 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 5.26 | 13.48 | 22.08 | 6.00 | 80.1 | 66.0 |
| XI | Bench | Morgan Rogers | MID | 2 | 5.6 | 3.94 | 12.62 | 20.56 | 0.00 | 77.8 | 0.0 |

## GW35

- Train rows: 158070
- Bank: 0.30 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.22
- Actual score: 42.00
- Transfer: David Raya Martin -> Jordan Pickford (projected gain 2.25, hit 0)
- Autosub: Omar Marmoush replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.71 | 10.06 | 16.26 | 2.00 | 93.1 | 90.0 |
| Bench 1 | Bench | Will Dennis | GK | 3 | 3.9 | 0.00 | 0.34 | 0.85 | 0.00 | 9.0 | 0.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.64 | 9.62 | 15.53 | 2.00 | 82.8 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 3.14 | 9.52 | 16.47 | 8.00 | 70.3 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.5 | 3.01 | 9.12 | 15.98 | 1.00 | 62.4 | 90.0 |
| XI | XI | Neco Williams | DEF | 16 | 4.5 | 2.93 | 8.40 | 13.75 | 5.00 | 84.2 | 90.0 |
| Bench 4 | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 2.13 | 7.21 | 12.71 | 1.00 | 59.2 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 6.28 | 17.24 | 27.68 | 9.00 | 80.1 | 90.0 |
| Bench 2 | Autosub In | Omar Marmoush | FWD | 13 | 7.6 | 2.86 | 9.81 | 17.40 | 2.00 | 41.1 | 82.0 |
| Bench 3 | Bench | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 2.34 | 6.39 | 10.64 | 6.00 | 52.3 | 76.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.51 | 22.28 | 36.59 | 2.00 | 104.9 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.0 | 6.13 | 17.60 | 28.18 | 5.00 | 94.7 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.44 | 13.59 | 22.80 | 0.00 | 78.6 | 0.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 4.07 | 11.75 | 19.64 | 1.00 | 59.7 | 55.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 2.86 | 8.93 | 15.63 | 3.00 | 49.2 | 90.0 |