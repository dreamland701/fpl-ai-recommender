# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 269.08
- Total actual points: 220.00
- Average predicted points: 67.27
- Average actual points: 55.00
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
- Predicted score: 76.73
- Actual score: 74.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (16.65) beats the best remaining Bench Boost opportunity (19.49).
- Chip advisory: bench_boost (0.58): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (16.65) beats the best remaining Bench Boost opportunity (19.49).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.93 | 11.36 | 18.25 | 2.00 | 93.1 | 90.0 |
| Bench 1 | Bench Boost | Matz Sels | GK | 16 | 5.1 | 3.42 | 10.09 | 16.40 | 3.00 | 92.7 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 5.12 | 12.70 | 19.45 | -1.00 | 110.9 | 180.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.26 | 12.39 | 19.84 | 1.00 | 96.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.5 | 3.94 | 11.65 | 18.34 | 2.00 | 84.5 | 90.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 4.81 | 11.04 | 16.60 | 8.00 | 106.3 | 180.0 |
| Bench 2 | Bench Boost | Nikola Milenković | DEF | 16 | 5.1 | 3.67 | 10.58 | 16.67 | 2.00 | 91.1 | 90.0 |
| XI | XI | Omar Marmoush | FWD | 13 | 7.6 | 4.55 | 13.15 | 21.23 | 7.00 | 81.8 | 81.0 |
| Bench 3 | Bench Boost | Jørgen Strand Larsen | FWD | 20 | 5.4 | 3.28 | 8.81 | 14.25 | 6.00 | 66.9 | 69.0 |
| Bench 4 | Bench Boost | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.9 | 2.45 | 8.09 | 13.56 | 1.00 | 60.1 | 26.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.16 | 24.46 | 40.61 | 6.00 | 107.8 | 84.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 5.20 | 14.93 | 25.56 | 4.00 | 63.2 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.6 | 4.68 | 14.52 | 24.93 | 2.00 | 91.4 | 81.0 |
| Vice Captain | XI | Jacob Murphy | MID | 15 | 5.2 | 6.16 | 13.87 | 20.69 | 19.00 | 113.7 | 138.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 4.95 | 12.65 | 20.18 | 6.00 | 89.1 | 84.0 |

## GW33

- Train rows: 156471
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Omar Marmoush
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 77.40
- Actual score: 52.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (13.17) beats the best remaining Triple Captain opportunity (9.36).
- Transfer: Matz Sels -> Dean Henderson (projected gain 0.08, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (13.17) beats the best remaining Triple Captain opportunity (9.36).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 5.78 | 13.74 | 21.24 | 7.00 | 128.2 | 180.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.6 | 4.66 | 11.78 | 18.17 | 10.00 | 142.5 | 180.0 |
| XI | XI | William Saliba | DEF | 1 | 6.5 | 6.43 | 15.25 | 23.33 | 7.00 | 130.9 | 180.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 6.11 | 14.82 | 22.90 | 7.00 | 130.2 | 180.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 5.32 | 13.60 | 20.75 | 6.00 | 137.3 | 180.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.56 | 10.88 | 17.30 | 0.00 | 100.8 | 90.0 |
| Bench 3 | Bench | Nikola Milenković | DEF | 16 | 5.1 | 3.08 | 9.24 | 15.04 | 2.00 | 80.9 | 90.0 |
| Vice Captain | XI | Omar Marmoush | FWD | 13 | 7.6 | 7.46 | 17.80 | 27.69 | 4.00 | 129.0 | 180.0 |
| Bench 2 | Bench | Jørgen Strand Larsen | FWD | 20 | 5.4 | 3.14 | 9.31 | 15.23 | 2.00 | 62.0 | 73.0 |
| Bench 4 | Bench | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 1.87 | 6.19 | 10.39 | 1.00 | 46.7 | 27.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.22 | 23.37 | 38.80 | 3.00 | 105.3 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 6.07 | 14.86 | 22.83 | 7.00 | 124.8 | 166.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.31 | 13.77 | 23.17 | 1.00 | 79.9 | 31.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 4.23 | 13.74 | 23.58 | 2.00 | 63.7 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 3.49 | 11.11 | 18.41 | 2.00 | 71.3 | 64.0 |

## GW34

- Train rows: 157270
- Bank: 0.50 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Rayan Aït-Nouri
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 66.06
- Actual score: 54.00
- Transfer: Nikola Milenković -> Rayan Aït-Nouri (projected gain 2.92, hit 0)
- Autosub: Tino Livramento replaced William Saliba.
- Autosub: Norberto Bercique Gomes Betuncal replaced Morgan Rogers.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martin | GK | 1 | 5.5 | 4.02 | 12.70 | 20.50 | 0.00 | 100.5 | 0.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.6 | 3.32 | 10.57 | 17.56 | 0.00 | 108.1 | 0.0 |
| Vice Captain | XI | Rayan Aït-Nouri | DEF | 20 | 5.0 | 6.62 | 16.11 | 24.44 | 11.00 | 113.8 | 76.0 |
| XI | Bench | William Saliba | DEF | 1 | 6.5 | 4.49 | 14.11 | 22.64 | 0.00 | 102.0 | 0.0 |
| XI | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 4.43 | 13.37 | 21.88 | 0.00 | 110.7 | 0.0 |
| Bench 2 | Bench | Joško Gvardiol | DEF | 13 | 6.2 | 4.10 | 13.23 | 21.69 | 0.00 | 100.7 | 0.0 |
| Bench 3 | Autosub In | Tino Livramento | DEF | 15 | 4.6 | 3.86 | 10.11 | 16.35 | 6.00 | 86.1 | 90.0 |
| XI | Bench | Omar Marmoush | FWD | 13 | 7.6 | 4.87 | 15.57 | 25.08 | 0.00 | 85.7 | 0.0 |
| XI | XI | Jørgen Strand Larsen | FWD | 20 | 5.4 | 4.16 | 10.17 | 16.37 | 6.00 | 67.2 | 76.0 |
| Bench 4 | Autosub In | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 1.66 | 5.72 | 9.77 | 2.00 | 46.2 | 63.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.60 | 23.25 | 37.48 | 8.00 | 112.9 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 6.28 | 17.05 | 27.52 | 3.00 | 97.2 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.53 | 13.86 | 23.27 | 4.00 | 77.3 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 5.31 | 13.64 | 22.31 | 6.00 | 80.6 | 66.0 |
| XI | Bench | Morgan Rogers | MID | 2 | 5.6 | 4.15 | 13.11 | 21.26 | 0.00 | 81.5 | 0.0 |

## GW35

- Train rows: 158070
- Bank: 0.60 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bruno Borges Fernandes
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 48.89
- Actual score: 40.00
- Transfer: Dean Henderson -> Jordan Pickford (projected gain 2.60, hit 0)
- Autosub: Norberto Bercique Gomes Betuncal replaced Bruno Borges Fernandes.
- Autosub: Daniel Muñoz replaced Jørgen Strand Larsen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.73 | 10.07 | 16.25 | 2.00 | 93.3 | 90.0 |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.5 | 2.45 | 7.51 | 13.16 | 1.00 | 56.8 | 90.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.64 | 9.63 | 15.54 | 2.00 | 82.3 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 3.05 | 9.26 | 16.04 | 8.00 | 67.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.5 | 2.87 | 8.76 | 15.42 | 1.00 | 59.5 | 90.0 |
| Bench 4 | Bench | Rayan Aït-Nouri | DEF | 20 | 5.0 | 1.49 | 7.41 | 13.18 | 2.00 | 40.1 | 90.0 |
| Bench 3 | Autosub In | Daniel Muñoz | DEF | 7 | 5.2 | 2.03 | 6.90 | 12.20 | 1.00 | 56.5 | 90.0 |
| XI | XI | Omar Marmoush | FWD | 13 | 7.6 | 2.61 | 9.28 | 16.77 | 2.00 | 39.7 | 82.0 |
| XI | Bench | Jørgen Strand Larsen | FWD | 20 | 5.4 | 2.60 | 8.67 | 14.52 | 0.00 | 54.2 | 0.0 |
| Bench 2 | Autosub In | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 2.38 | 6.45 | 10.69 | 6.00 | 52.9 | 76.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.59 | 22.52 | 36.88 | 2.00 | 104.3 | 90.0 |
| Vice Captain | Bench | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.40 | 13.47 | 22.55 | 0.00 | 76.8 | 0.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.5 | 3.96 | 12.98 | 21.76 | 10.00 | 66.4 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 4.11 | 11.88 | 19.82 | 1.00 | 59.9 | 55.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 2.73 | 8.57 | 15.08 | 3.00 | 46.3 | 90.0 |