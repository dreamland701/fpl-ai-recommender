# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 299.82
- Total actual points: 271.00
- Average predicted points: 74.96
- Average actual points: 67.75
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
- Captain: Alexander Isak
- Vice captain: Jacob Murphy
- Effective captain: Alexander Isak
- Chip used: triple_captain
- Predicted score: 95.09
- Actual score: 74.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (14.77) beats the best remaining Triple Captain opportunity (15.95).
- Chip advisory: triple_captain (0.69): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Alexander Isak. Optimizer chose Triple Captain here because the current estimated captain upside (14.77) beats the best remaining Triple Captain opportunity (15.95).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.86 | 11.19 | 18.00 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.61 | 1.33 | 2.12 | 0.00 | 11.9 | 0.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 7.40 | 12.43 | 19.04 | -1.00 | 163.3 | 180.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.14 | 12.18 | 19.51 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.5 | 3.85 | 11.55 | 18.15 | 2.00 | 82.6 | 90.0 |
| Bench 2 | Bench | Noussair Mazraoui | DEF | 14 | 4.2 | 2.67 | 7.92 | 12.82 | 0.00 | 79.8 | 77.0 |
| Bench 4 | Bench | Dara O'Shea | DEF | 10 | 3.9 | 2.28 | 7.26 | 11.93 | 1.00 | 89.0 | 90.0 |
| Captain | Captain | Alexander Isak | FWD | 15 | 9.5 | 11.25 | 17.35 | 27.55 | 11.00 | 150.8 | 148.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 8.17 | 13.85 | 21.30 | 2.00 | 143.8 | 100.0 |
| Bench 3 | Bench | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.9 | 2.43 | 7.96 | 13.34 | 1.00 | 60.8 | 26.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 8.35 | 24.37 | 40.45 | 6.00 | 90.0 | 84.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.6 | 4.86 | 15.15 | 26.07 | 2.00 | 90.0 | 81.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.0 | 4.53 | 14.42 | 24.32 | 2.00 | 90.0 | 90.0 |
| XI | XI | Eberechi Eze | MID | 7 | 6.8 | 7.48 | 13.37 | 21.28 | 6.00 | 155.9 | 135.0 |
| Vice Captain | XI | Jacob Murphy | MID | 15 | 5.2 | 8.73 | 13.36 | 19.82 | 19.00 | 155.8 | 138.0 |

## GW33

- Train rows: 156471
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: William Saliba
- Vice captain: Eberechi Eze
- Effective captain: William Saliba
- Chip used: bench_boost
- Predicted score: 95.84
- Actual score: 90.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.54) beats the best remaining Bench Boost opportunity (8.31).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.54) beats the best remaining Bench Boost opportunity (8.31).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 8.75 | 13.51 | 20.91 | 7.00 | 180.0 | 180.0 |
| Bench 1 | Bench Boost | Daniel Bentley | GK | 20 | 3.9 | 0.34 | 1.04 | 1.74 | 7.00 | 9.4 | 90.0 |
| Captain | Captain | William Saliba | DEF | 1 | 6.5 | 9.86 | 14.93 | 22.81 | 7.00 | 180.0 | 180.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 8.90 | 14.36 | 22.19 | 7.00 | 180.0 | 180.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 8.07 | 13.08 | 19.94 | 6.00 | 180.0 | 180.0 |
| Bench 2 | Bench Boost | Noussair Mazraoui | DEF | 14 | 4.2 | 2.44 | 7.23 | 11.79 | 2.00 | 73.7 | 90.0 |
| Bench 3 | Bench Boost | Dara O'Shea | DEF | 10 | 3.9 | 2.20 | 7.08 | 11.71 | 0.00 | 87.4 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.76 | 16.82 | 28.14 | 2.00 | 90.0 | 75.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 7.69 | 13.15 | 20.17 | 10.00 | 145.1 | 84.0 |
| Bench 4 | Bench Boost | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 1.87 | 6.09 | 10.23 | 1.00 | 47.2 | 27.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 8.37 | 23.26 | 38.63 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Eberechi Eze | MID | 7 | 6.8 | 9.06 | 14.98 | 23.56 | 10.00 | 180.0 | 107.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.55 | 14.36 | 24.29 | 1.00 | 85.0 | 31.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 4.87 | 14.02 | 23.51 | 18.00 | 85.3 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 3.26 | 10.56 | 17.46 | 2.00 | 69.8 | 64.0 |

## GW34

- Train rows: 157270
- Bank: 0.00 -> 0.80
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 54.04
- Actual score: 54.00
- Transfer: Jean-Philippe Mateta -> Matheus Santos Carneiro Da Cunha (projected gain 2.96, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.5 | 0.00 | 12.17 | 19.73 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Daniel Bentley | GK | 20 | 3.9 | 1.69 | 3.88 | 5.82 | 0.00 | 39.4 | 0.0 |
| XI | Bench | William Saliba | DEF | 1 | 6.5 | 0.00 | 13.49 | 21.68 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Joško Gvardiol | DEF | 13 | 6.2 | 0.00 | 12.60 | 20.75 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 0.00 | 12.54 | 20.60 | 0.00 | 0.0 | 0.0 |
| XI | XI | Noussair Mazraoui | DEF | 14 | 4.2 | 2.37 | 7.12 | 11.79 | 2.00 | 76.6 | 74.0 |
| XI | XI | Dara O'Shea | DEF | 10 | 3.9 | 2.04 | 6.61 | 11.10 | 1.00 | 84.5 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 7.16 | 19.42 | 31.02 | 6.00 | 90.0 | 76.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.0 | 5.65 | 14.89 | 22.33 | 15.00 | 90.0 | 88.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 1.71 | 5.67 | 9.69 | 2.00 | 47.6 | 63.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.46 | 23.04 | 37.25 | 8.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.0 | 6.93 | 20.56 | 32.63 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.54 | 14.37 | 24.26 | 4.00 | 78.8 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 5.03 | 13.23 | 21.59 | 6.00 | 77.4 | 66.0 |
| Bench 4 | Bench | Eberechi Eze | MID | 7 | 6.8 | 0.00 | 13.13 | 22.51 | 0.00 | 0.0 | 0.0 |

## GW35

- Train rows: 158070
- Bank: 0.80 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 54.84
- Actual score: 53.00
- Transfer: Matheus Santos Carneiro Da Cunha -> Yoane Wissa (projected gain 6.94, hit 0)
- Autosub: Norberto Bercique Gomes Betuncal replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 2.66 | 7.80 | 13.63 | 1.00 | 60.4 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.27 | 1.23 | 2.30 | 0.00 | 15.8 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 3.17 | 9.45 | 16.33 | 8.00 | 69.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.5 | 3.09 | 9.01 | 15.77 | 1.00 | 62.5 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 2.28 | 7.05 | 12.41 | 1.00 | 61.5 | 90.0 |
| Bench 3 | Bench | Noussair Mazraoui | DEF | 14 | 4.2 | 2.21 | 6.66 | 11.09 | 0.00 | 70.6 | 0.0 |
| Bench 4 | Bench | Dara O'Shea | DEF | 10 | 3.9 | 2.03 | 6.24 | 10.51 | 1.00 | 81.6 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 6.36 | 17.50 | 28.22 | 9.00 | 80.1 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.6 | 4.61 | 13.19 | 21.43 | 7.00 | 86.0 | 90.0 |
| Bench 2 | Autosub In | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 2.38 | 6.31 | 10.48 | 6.00 | 53.1 | 76.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.59 | 22.28 | 36.61 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.0 | 6.05 | 17.72 | 28.46 | 5.00 | 90.0 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.54 | 13.91 | 23.40 | 0.00 | 80.2 | 0.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 4.07 | 11.50 | 19.14 | 1.00 | 61.7 | 55.0 |
| XI | XI | Eberechi Eze | MID | 7 | 6.8 | 2.83 | 9.68 | 17.18 | 10.00 | 57.1 | 90.0 |