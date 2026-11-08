# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 279.92
- Total actual points: 221.00
- Average predicted points: 69.98
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
- Predicted score: 76.92
- Actual score: 69.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (14.64) beats the best remaining Bench Boost opportunity (15.90).
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (14.64) beats the best remaining Bench Boost opportunity (15.90).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.93 | 11.34 | 18.23 | 2.00 | 93.6 | 90.0 |
| Bench 1 | Bench Boost | Daniel Bentley | GK | 20 | 3.9 | 0.41 | 0.80 | 1.32 | 0.00 | 7.1 | 0.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 5.09 | 12.70 | 19.52 | -1.00 | 111.1 | 180.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.23 | 12.37 | 19.87 | 1.00 | 97.0 | 90.0 |
| Bench 2 | Bench Boost | William Saliba | DEF | 1 | 6.5 | 3.93 | 11.65 | 18.37 | 2.00 | 84.5 | 90.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 4.80 | 11.02 | 16.59 | 8.00 | 106.8 | 180.0 |
| Bench 3 | Bench Boost | Neco Williams | DEF | 16 | 4.5 | 3.15 | 9.11 | 14.79 | 2.00 | 85.3 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 7.00 | 17.39 | 27.46 | 11.00 | 108.2 | 148.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 5.54 | 13.83 | 21.29 | 2.00 | 103.6 | 100.0 |
| Bench 4 | Bench Boost | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.9 | 2.42 | 8.10 | 13.63 | 1.00 | 60.2 | 26.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.16 | 24.40 | 40.51 | 6.00 | 108.3 | 84.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.6 | 4.66 | 14.49 | 24.93 | 2.00 | 91.5 | 81.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.0 | 4.36 | 14.13 | 23.74 | 2.00 | 88.9 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 6.16 | 13.84 | 20.64 | 19.00 | 114.2 | 138.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 4.93 | 12.65 | 20.20 | 6.00 | 89.1 | 84.0 |

## GW33

- Train rows: 156471
- Bank: 0.20 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Omar Marmoush
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 79.98
- Actual score: 68.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (12.80) beats the best remaining Triple Captain opportunity (9.32).
- Transfer: Jean-Philippe Mateta -> Omar Marmoush (projected gain 11.18, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (12.80) beats the best remaining Triple Captain opportunity (9.32).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 5.77 | 13.72 | 21.23 | 7.00 | 128.8 | 180.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.12 | 0.47 | 0.88 | 7.00 | 4.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.5 | 6.41 | 15.25 | 23.37 | 7.00 | 130.9 | 180.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 6.08 | 14.81 | 22.93 | 7.00 | 130.3 | 180.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 5.29 | 13.59 | 20.80 | 6.00 | 137.4 | 180.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.55 | 10.86 | 17.30 | 0.00 | 101.3 | 90.0 |
| Bench 3 | Bench | Neco Williams | DEF | 16 | 4.5 | 2.94 | 8.51 | 14.10 | 2.00 | 84.0 | 90.0 |
| Vice Captain | XI | Omar Marmoush | FWD | 13 | 7.7 | 7.56 | 17.99 | 27.83 | 4.00 | 127.9 | 180.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.83 | 17.03 | 28.31 | 2.00 | 94.1 | 75.0 |
| Bench 4 | Bench | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 1.85 | 6.19 | 10.45 | 1.00 | 46.8 | 27.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.20 | 23.28 | 38.67 | 3.00 | 105.9 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 6.05 | 14.85 | 22.85 | 7.00 | 124.8 | 166.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.27 | 13.72 | 23.16 | 1.00 | 80.0 | 31.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 4.59 | 13.58 | 22.69 | 18.00 | 81.3 | 90.0 |
| Bench 2 | Bench | Jacob Murphy | MID | 15 | 5.2 | 3.47 | 11.06 | 18.35 | 2.00 | 71.9 | 64.0 |

## GW34

- Train rows: 157270
- Bank: 0.30 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 68.03
- Actual score: 42.00
- Transfer: none
- No transfer was applied this week.
- Autosub: Tino Livramento replaced William Saliba.
- Autosub: Neco Williams replaced Daniel Muñoz.
- Autosub: Norberto Bercique Gomes Betuncal replaced Morgan Rogers.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martin | GK | 1 | 5.5 | 4.01 | 12.66 | 20.48 | 0.00 | 101.2 | 0.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 1.63 | 3.66 | 5.48 | 0.00 | 38.1 | 0.0 |
| XI | Bench | William Saliba | DEF | 1 | 6.5 | 4.47 | 14.10 | 22.65 | 0.00 | 102.1 | 0.0 |
| XI | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 4.41 | 13.36 | 21.91 | 0.00 | 110.9 | 0.0 |
| XI | Bench | Joško Gvardiol | DEF | 13 | 6.2 | 4.08 | 13.21 | 21.71 | 0.00 | 100.8 | 0.0 |
| Bench 2 | Autosub In | Tino Livramento | DEF | 15 | 4.6 | 3.86 | 10.10 | 16.35 | 6.00 | 86.6 | 90.0 |
| Bench 3 | Autosub In | Neco Williams | DEF | 16 | 4.5 | 2.88 | 8.27 | 13.81 | 0.00 | 84.5 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 7.60 | 19.59 | 31.14 | 6.00 | 104.9 | 76.0 |
| XI | Bench | Omar Marmoush | FWD | 13 | 7.7 | 4.98 | 15.75 | 25.22 | 0.00 | 84.6 | 0.0 |
| Bench 4 | Autosub In | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 1.64 | 5.73 | 9.83 | 2.00 | 46.2 | 63.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.55 | 23.11 | 37.30 | 8.00 | 113.7 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.0 | 7.47 | 20.70 | 32.76 | 2.00 | 130.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.49 | 13.79 | 23.24 | 4.00 | 77.4 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 5.30 | 13.59 | 22.25 | 6.00 | 81.1 | 66.0 |
| XI | Bench | Morgan Rogers | MID | 2 | 5.6 | 4.12 | 13.09 | 21.26 | 0.00 | 81.6 | 0.0 |

## GW35

- Train rows: 158070
- Bank: 0.30 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 54.98
- Actual score: 42.00
- Transfer: David Raya Martin -> Jordan Pickford (projected gain 5.16, hit 0)
- Autosub: Morgan Rogers replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.72 | 10.08 | 16.30 | 2.00 | 93.3 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.10 | 0.71 | 1.50 | 0.00 | 12.1 | 0.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.64 | 9.63 | 15.55 | 2.00 | 82.8 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 3.03 | 9.24 | 16.05 | 8.00 | 67.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.5 | 2.86 | 8.76 | 15.44 | 1.00 | 59.4 | 90.0 |
| XI | XI | Neco Williams | DEF | 16 | 4.5 | 2.92 | 8.39 | 13.74 | 5.00 | 84.1 | 90.0 |
| Bench 4 | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 2.01 | 6.90 | 12.25 | 1.00 | 56.6 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 6.42 | 17.61 | 28.25 | 9.00 | 83.0 | 90.0 |
| XI | XI | Omar Marmoush | FWD | 13 | 7.6 | 2.73 | 9.51 | 16.95 | 2.00 | 38.6 | 82.0 |
| Bench 3 | Bench | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 2.37 | 6.45 | 10.74 | 6.00 | 52.9 | 76.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.52 | 22.32 | 36.64 | 2.00 | 105.2 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.0 | 6.15 | 17.65 | 28.26 | 5.00 | 95.1 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.36 | 13.40 | 22.50 | 0.00 | 76.9 | 0.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 4.11 | 11.84 | 19.77 | 1.00 | 60.4 | 55.0 |
| Bench 2 | Autosub In | Morgan Rogers | MID | 2 | 5.6 | 2.72 | 8.57 | 15.10 | 3.00 | 46.3 | 90.0 |