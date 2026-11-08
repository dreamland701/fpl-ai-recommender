# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 267.42
- Total actual points: 215.00
- Average predicted points: 66.85
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
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Jacob Murphy
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 76.30
- Actual score: 74.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (16.52) beats the best remaining Bench Boost opportunity (19.50).
- Chip advisory: bench_boost (0.58): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (16.52) beats the best remaining Bench Boost opportunity (19.50).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.97 | 11.40 | 18.35 | 2.00 | 94.2 | 90.0 |
| Bench 1 | Bench Boost | Matz Sels | GK | 16 | 5.1 | 3.42 | 10.07 | 16.43 | 3.00 | 92.1 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 5.15 | 12.66 | 19.46 | -1.00 | 110.2 | 180.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.31 | 12.40 | 19.88 | 1.00 | 95.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.5 | 3.97 | 11.67 | 18.41 | 2.00 | 84.3 | 90.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 4.77 | 10.94 | 16.36 | 8.00 | 103.1 | 180.0 |
| Bench 2 | Bench Boost | Nikola Milenković | DEF | 16 | 5.1 | 3.68 | 10.58 | 16.75 | 2.00 | 90.6 | 90.0 |
| XI | XI | Omar Marmoush | FWD | 13 | 7.6 | 4.76 | 13.38 | 21.42 | 7.00 | 79.4 | 81.0 |
| Bench 3 | Bench Boost | Jørgen Strand Larsen | FWD | 20 | 5.4 | 3.13 | 8.55 | 13.90 | 6.00 | 64.9 | 69.0 |
| Bench 4 | Bench Boost | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.9 | 2.45 | 7.95 | 13.49 | 1.00 | 59.8 | 26.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.24 | 24.34 | 40.50 | 6.00 | 108.7 | 84.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.6 | 4.65 | 14.74 | 25.18 | 2.00 | 89.7 | 81.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 4.83 | 14.70 | 25.15 | 4.00 | 60.2 | 90.0 |
| Vice Captain | XI | Jacob Murphy | MID | 15 | 5.2 | 6.19 | 13.95 | 20.65 | 19.00 | 110.5 | 138.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 4.52 | 12.25 | 19.56 | 6.00 | 86.3 | 84.0 |

## GW33

- Train rows: 156471
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Omar Marmoush
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 77.06
- Actual score: 52.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (12.94) beats the best remaining Triple Captain opportunity (9.06).
- Transfer: Matz Sels -> Dean Henderson (projected gain 0.08, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (12.94) beats the best remaining Triple Captain opportunity (9.06).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 5.76 | 13.72 | 21.21 | 7.00 | 128.8 | 180.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.6 | 4.53 | 11.51 | 17.78 | 10.00 | 139.0 | 180.0 |
| XI | XI | William Saliba | DEF | 1 | 6.5 | 6.37 | 15.22 | 23.29 | 7.00 | 130.3 | 180.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 6.23 | 15.06 | 23.24 | 7.00 | 131.0 | 180.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 5.16 | 13.33 | 20.38 | 6.00 | 133.9 | 180.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.60 | 11.05 | 17.43 | 0.00 | 98.4 | 90.0 |
| Bench 3 | Bench | Nikola Milenković | DEF | 16 | 5.1 | 2.99 | 9.24 | 15.09 | 2.00 | 81.6 | 90.0 |
| Vice Captain | XI | Omar Marmoush | FWD | 13 | 7.6 | 7.70 | 18.27 | 28.05 | 4.00 | 127.1 | 180.0 |
| Bench 2 | Bench | Jørgen Strand Larsen | FWD | 20 | 5.4 | 3.14 | 9.03 | 14.92 | 2.00 | 61.6 | 73.0 |
| Bench 4 | Bench | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 1.90 | 6.26 | 10.52 | 1.00 | 47.6 | 27.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.99 | 23.44 | 38.80 | 3.00 | 106.4 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 6.13 | 14.92 | 22.82 | 7.00 | 121.4 | 166.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.32 | 13.71 | 23.10 | 1.00 | 79.7 | 31.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 4.19 | 13.69 | 23.64 | 2.00 | 66.4 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 3.63 | 11.79 | 19.07 | 2.00 | 68.8 | 64.0 |

## GW34

- Train rows: 157270
- Bank: 0.50 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Rayan Aït-Nouri
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 65.23
- Actual score: 49.00
- Transfer: Tino Livramento -> Rayan Aït-Nouri (projected gain 5.92, hit 0)
- Autosub: Jørgen Strand Larsen replaced William Saliba.
- Autosub: Nikola Milenković replaced Daniel Muñoz.
- Autosub: Norberto Bercique Gomes Betuncal replaced Morgan Rogers.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martin | GK | 1 | 5.5 | 4.02 | 12.67 | 20.49 | 0.00 | 101.2 | 0.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.6 | 3.32 | 10.59 | 17.62 | 0.00 | 108.1 | 0.0 |
| Vice Captain | XI | Rayan Aït-Nouri | DEF | 20 | 5.0 | 6.48 | 16.12 | 24.41 | 11.00 | 114.8 | 76.0 |
| XI | Bench | William Saliba | DEF | 1 | 6.5 | 4.47 | 14.07 | 22.62 | 0.00 | 101.9 | 0.0 |
| XI | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 4.42 | 13.37 | 21.95 | 0.00 | 111.1 | 0.0 |
| XI | Bench | Joško Gvardiol | DEF | 13 | 6.2 | 4.08 | 13.21 | 21.71 | 0.00 | 100.8 | 0.0 |
| Bench 3 | Autosub In | Nikola Milenković | DEF | 16 | 5.1 | 3.71 | 10.59 | 17.02 | 1.00 | 96.2 | 90.0 |
| XI | Bench | Omar Marmoush | FWD | 13 | 7.6 | 4.95 | 15.68 | 25.11 | 0.00 | 83.9 | 0.0 |
| Bench 2 | Autosub In | Jørgen Strand Larsen | FWD | 20 | 5.4 | 3.90 | 10.24 | 16.44 | 6.00 | 67.4 | 76.0 |
| Bench 4 | Autosub In | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 1.79 | 6.03 | 10.26 | 2.00 | 49.8 | 63.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.55 | 23.13 | 37.37 | 8.00 | 115.4 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 6.36 | 17.23 | 27.88 | 3.00 | 101.5 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.57 | 14.16 | 23.62 | 4.00 | 79.3 | 90.0 |
| XI | Bench | Morgan Rogers | MID | 2 | 5.6 | 4.11 | 13.05 | 21.21 | 0.00 | 81.3 | 0.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 4.66 | 12.75 | 21.08 | 6.00 | 78.1 | 66.0 |

## GW35

- Train rows: 158070
- Bank: 0.10 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bruno Borges Fernandes
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 48.83
- Actual score: 40.00
- Transfer: David Raya Martin -> Jordan Pickford (projected gain 2.26, hit 0)
- Autosub: Norberto Bercique Gomes Betuncal replaced Bruno Borges Fernandes.
- Autosub: Daniel Muñoz replaced Jørgen Strand Larsen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.64 | 10.10 | 16.27 | 2.00 | 95.6 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.6 | 1.69 | 5.75 | 10.15 | 3.00 | 64.3 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 3.12 | 9.31 | 16.02 | 8.00 | 67.0 | 90.0 |
| XI | XI | Nikola Milenković | DEF | 16 | 5.1 | 3.15 | 9.24 | 14.85 | 2.00 | 83.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.5 | 2.97 | 9.19 | 15.92 | 1.00 | 61.4 | 90.0 |
| Bench 4 | Bench | Rayan Aït-Nouri | DEF | 20 | 5.0 | 1.68 | 7.64 | 13.42 | 2.00 | 40.2 | 90.0 |
| Bench 3 | Autosub In | Daniel Muñoz | DEF | 7 | 5.2 | 2.02 | 6.97 | 12.28 | 1.00 | 56.7 | 90.0 |
| XI | XI | Omar Marmoush | FWD | 13 | 7.6 | 2.94 | 9.61 | 16.95 | 2.00 | 38.7 | 82.0 |
| XI | Bench | Jørgen Strand Larsen | FWD | 20 | 5.4 | 2.67 | 8.71 | 14.47 | 0.00 | 53.2 | 0.0 |
| Bench 2 | Autosub In | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 2.40 | 6.64 | 10.91 | 6.00 | 54.0 | 76.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.87 | 22.78 | 37.22 | 2.00 | 109.0 | 90.0 |
| Vice Captain | Bench | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.49 | 13.67 | 22.83 | 0.00 | 79.4 | 0.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.5 | 4.00 | 13.14 | 22.02 | 10.00 | 69.5 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 3.41 | 11.43 | 19.17 | 1.00 | 57.0 | 55.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 2.70 | 8.74 | 15.24 | 3.00 | 46.4 | 90.0 |