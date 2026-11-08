# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 268.15
- Total actual points: 220.00
- Average predicted points: 67.04
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
- Predicted score: 76.52
- Actual score: 74.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (16.58) beats the best remaining Bench Boost opportunity (19.45).
- Chip advisory: bench_boost (0.58): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (16.58) beats the best remaining Bench Boost opportunity (19.45).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.93 | 11.34 | 18.23 | 2.00 | 93.6 | 90.0 |
| Bench 1 | Bench Boost | Matz Sels | GK | 16 | 5.1 | 3.41 | 10.11 | 16.45 | 3.00 | 92.6 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 5.09 | 12.70 | 19.52 | -1.00 | 111.1 | 180.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.23 | 12.37 | 19.87 | 1.00 | 97.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.5 | 3.93 | 11.65 | 18.37 | 2.00 | 84.5 | 90.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 4.80 | 11.02 | 16.59 | 8.00 | 106.8 | 180.0 |
| Bench 2 | Bench Boost | Nikola Milenković | DEF | 16 | 5.1 | 3.64 | 10.59 | 16.74 | 2.00 | 91.2 | 90.0 |
| XI | XI | Omar Marmoush | FWD | 13 | 7.6 | 4.64 | 13.31 | 21.34 | 7.00 | 80.6 | 81.0 |
| Bench 3 | Bench Boost | Jørgen Strand Larsen | FWD | 20 | 5.4 | 3.27 | 8.80 | 14.28 | 6.00 | 66.9 | 69.0 |
| Bench 4 | Bench Boost | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.9 | 2.42 | 8.10 | 13.63 | 1.00 | 60.2 | 26.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.16 | 24.40 | 40.51 | 6.00 | 108.3 | 84.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 5.11 | 14.77 | 25.42 | 4.00 | 63.8 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.6 | 4.66 | 14.49 | 24.93 | 2.00 | 91.5 | 81.0 |
| Vice Captain | XI | Jacob Murphy | MID | 15 | 5.2 | 6.16 | 13.84 | 20.64 | 19.00 | 114.2 | 138.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 4.93 | 12.65 | 20.20 | 6.00 | 89.1 | 84.0 |

## GW33

- Train rows: 156471
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Omar Marmoush
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 77.17
- Actual score: 52.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (13.15) beats the best remaining Triple Captain opportunity (9.32).
- Transfer: Matz Sels -> Dean Henderson (projected gain 0.08, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (13.15) beats the best remaining Triple Captain opportunity (9.32).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 5.77 | 13.72 | 21.23 | 7.00 | 128.8 | 180.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.6 | 4.65 | 11.80 | 18.23 | 10.00 | 142.4 | 180.0 |
| XI | XI | William Saliba | DEF | 1 | 6.5 | 6.41 | 15.25 | 23.37 | 7.00 | 130.9 | 180.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 6.08 | 14.81 | 22.93 | 7.00 | 130.3 | 180.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 5.29 | 13.59 | 20.80 | 6.00 | 137.4 | 180.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.55 | 10.86 | 17.30 | 0.00 | 101.3 | 90.0 |
| Bench 3 | Bench | Nikola Milenković | DEF | 16 | 5.1 | 3.06 | 9.25 | 15.11 | 2.00 | 81.0 | 90.0 |
| Vice Captain | XI | Omar Marmoush | FWD | 13 | 7.6 | 7.56 | 17.99 | 27.83 | 4.00 | 127.9 | 180.0 |
| Bench 2 | Bench | Jørgen Strand Larsen | FWD | 20 | 5.4 | 3.12 | 9.29 | 15.24 | 2.00 | 62.0 | 73.0 |
| Bench 4 | Bench | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 1.85 | 6.19 | 10.45 | 1.00 | 46.8 | 27.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.20 | 23.28 | 38.67 | 3.00 | 105.9 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 6.05 | 14.85 | 22.85 | 7.00 | 124.8 | 166.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.27 | 13.72 | 23.16 | 1.00 | 80.0 | 31.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 4.14 | 13.57 | 23.44 | 2.00 | 64.3 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 3.47 | 11.06 | 18.35 | 2.00 | 71.9 | 64.0 |

## GW34

- Train rows: 157270
- Bank: 0.50 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Rayan Aït-Nouri
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 65.81
- Actual score: 54.00
- Transfer: Nikola Milenković -> Rayan Aït-Nouri (projected gain 2.91, hit 0)
- Autosub: Tino Livramento replaced William Saliba.
- Autosub: Norberto Bercique Gomes Betuncal replaced Morgan Rogers.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martin | GK | 1 | 5.5 | 4.01 | 12.66 | 20.48 | 0.00 | 101.2 | 0.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.6 | 3.32 | 10.59 | 17.62 | 0.00 | 108.1 | 0.0 |
| Vice Captain | XI | Rayan Aït-Nouri | DEF | 20 | 5.0 | 6.61 | 16.08 | 24.40 | 11.00 | 114.2 | 76.0 |
| XI | Bench | William Saliba | DEF | 1 | 6.5 | 4.47 | 14.10 | 22.65 | 0.00 | 102.1 | 0.0 |
| XI | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 4.41 | 13.36 | 21.91 | 0.00 | 110.9 | 0.0 |
| Bench 2 | Bench | Joško Gvardiol | DEF | 13 | 6.2 | 4.08 | 13.21 | 21.71 | 0.00 | 100.8 | 0.0 |
| Bench 3 | Autosub In | Tino Livramento | DEF | 15 | 4.6 | 3.86 | 10.10 | 16.35 | 6.00 | 86.6 | 90.0 |
| XI | Bench | Omar Marmoush | FWD | 13 | 7.6 | 4.98 | 15.75 | 25.22 | 0.00 | 84.6 | 0.0 |
| XI | XI | Jørgen Strand Larsen | FWD | 20 | 5.4 | 4.14 | 10.15 | 16.38 | 6.00 | 67.3 | 76.0 |
| Bench 4 | Autosub In | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 1.64 | 5.73 | 9.83 | 2.00 | 46.2 | 63.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.55 | 23.11 | 37.30 | 8.00 | 113.7 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 6.17 | 16.85 | 27.35 | 3.00 | 97.9 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.49 | 13.79 | 23.24 | 4.00 | 77.4 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 5.30 | 13.59 | 22.25 | 6.00 | 81.1 | 66.0 |
| XI | Bench | Morgan Rogers | MID | 2 | 5.6 | 4.12 | 13.09 | 21.26 | 0.00 | 81.6 | 0.0 |

## GW35

- Train rows: 158070
- Bank: 0.60 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bruno Borges Fernandes
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 48.64
- Actual score: 40.00
- Transfer: Dean Henderson -> Jordan Pickford (projected gain 2.64, hit 0)
- Autosub: Norberto Bercique Gomes Betuncal replaced Bruno Borges Fernandes.
- Autosub: Daniel Muñoz replaced Jørgen Strand Larsen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.72 | 10.08 | 16.30 | 2.00 | 93.3 | 90.0 |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.5 | 2.44 | 7.49 | 13.15 | 1.00 | 57.4 | 90.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.64 | 9.63 | 15.55 | 2.00 | 82.8 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 3.03 | 9.24 | 16.05 | 8.00 | 67.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.5 | 2.86 | 8.76 | 15.44 | 1.00 | 59.4 | 90.0 |
| Bench 4 | Bench | Rayan Aït-Nouri | DEF | 20 | 5.0 | 1.48 | 7.36 | 13.14 | 2.00 | 40.6 | 90.0 |
| Bench 3 | Autosub In | Daniel Muñoz | DEF | 7 | 5.2 | 2.01 | 6.90 | 12.25 | 1.00 | 56.6 | 90.0 |
| XI | XI | Omar Marmoush | FWD | 13 | 7.6 | 2.73 | 9.51 | 16.95 | 2.00 | 38.6 | 82.0 |
| XI | Bench | Jørgen Strand Larsen | FWD | 20 | 5.4 | 2.57 | 8.64 | 14.51 | 0.00 | 54.3 | 0.0 |
| Bench 2 | Autosub In | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 2.37 | 6.45 | 10.74 | 6.00 | 52.9 | 76.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.52 | 22.32 | 36.64 | 2.00 | 105.2 | 90.0 |
| Vice Captain | Bench | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.36 | 13.40 | 22.50 | 0.00 | 76.9 | 0.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.5 | 3.86 | 12.78 | 21.57 | 10.00 | 67.0 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 4.11 | 11.84 | 19.77 | 1.00 | 60.4 | 55.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 2.72 | 8.57 | 15.10 | 3.00 | 46.3 | 90.0 |