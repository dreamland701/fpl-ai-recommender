# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 313.19
- Total actual points: 282.00
- Average predicted points: 78.30
- Average actual points: 70.50
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
- Vice captain: Jean-Philippe Mateta
- Effective captain: Alexander Isak
- Chip used: triple_captain
- Predicted score: 96.38
- Actual score: 81.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (14.86) beats the best remaining Triple Captain opportunity (15.31).
- Chip advisory: triple_captain (0.69): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Alexander Isak. Optimizer chose Triple Captain here because the current estimated captain upside (14.86) beats the best remaining Triple Captain opportunity (15.31).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.23 | 12.27 | 19.75 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Wayne Hennessey | GK | 16 | 4.0 | 0.34 | 0.89 | 1.37 | 0.00 | 8.4 | 0.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 7.51 | 12.48 | 19.09 | -1.00 | 168.2 | 180.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.13 | 12.24 | 19.66 | 1.00 | 90.0 | 90.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 6.98 | 11.25 | 16.94 | 8.00 | 156.7 | 180.0 |
| Bench 3 | Bench | Rayan Aït-Nouri | DEF | 20 | 4.8 | 3.42 | 9.51 | 15.61 | 14.00 | 72.5 | 69.0 |
| Bench 4 | Bench | Neco Williams | DEF | 16 | 4.5 | 3.15 | 9.06 | 14.68 | 2.00 | 86.7 | 90.0 |
| Captain | Captain | Alexander Isak | FWD | 15 | 9.5 | 11.34 | 17.43 | 27.56 | 11.00 | 152.2 | 148.0 |
| Vice Captain | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 8.89 | 14.79 | 22.79 | 2.00 | 150.8 | 100.0 |
| XI | XI | Omar Marmoush | FWD | 13 | 7.6 | 4.69 | 13.71 | 21.95 | 7.00 | 79.3 | 81.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 8.08 | 23.77 | 39.54 | 6.00 | 90.0 | 84.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.6 | 4.88 | 14.96 | 25.67 | 2.00 | 90.0 | 81.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.0 | 4.32 | 13.77 | 23.17 | 2.00 | 89.6 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 8.66 | 13.36 | 19.90 | 19.00 | 155.7 | 138.0 |
| Bench 2 | Bench | Enzo Fernández | MID | 6 | 4.7 | 3.92 | 10.66 | 17.42 | 2.00 | 82.0 | 90.0 |

## GW33

- Train rows: 156471
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Omar Marmoush
- Vice captain: David Raya Martin
- Effective captain: Omar Marmoush
- Chip used: bench_boost
- Predicted score: 98.57
- Actual score: 76.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (15.86) beats the best remaining Bench Boost opportunity (11.04).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (15.86) beats the best remaining Bench Boost opportunity (11.04).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Vice Captain | XI | David Raya Martin | GK | 1 | 5.5 | 9.44 | 14.53 | 22.55 | 7.00 | 180.0 | 180.0 |
| Bench 1 | Bench Boost | Wayne Hennessey | GK | 16 | 4.0 | 0.18 | 0.63 | 1.11 | 0.00 | 7.7 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 8.95 | 14.50 | 22.46 | 7.00 | 180.0 | 180.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 7.97 | 12.73 | 19.28 | 6.00 | 180.0 | 180.0 |
| XI | XI | Rayan Aït-Nouri | DEF | 20 | 4.8 | 3.54 | 10.79 | 17.87 | 5.00 | 74.2 | 81.0 |
| Bench 2 | Bench Boost | Tino Livramento | DEF | 15 | 4.6 | 3.35 | 10.48 | 16.71 | 0.00 | 90.0 | 90.0 |
| Bench 4 | Bench Boost | Neco Williams | DEF | 16 | 4.5 | 2.92 | 8.39 | 13.91 | 2.00 | 84.8 | 90.0 |
| Captain | Captain | Omar Marmoush | FWD | 13 | 7.6 | 12.22 | 18.59 | 28.82 | 4.00 | 180.0 | 180.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.70 | 16.59 | 27.67 | 2.00 | 89.5 | 75.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 8.18 | 13.80 | 21.20 | 10.00 | 149.1 | 84.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 8.03 | 22.47 | 37.41 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.52 | 14.05 | 23.69 | 1.00 | 84.4 | 31.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 4.68 | 13.41 | 22.43 | 18.00 | 84.5 | 90.0 |
| Bench 3 | Bench Boost | Jacob Murphy | MID | 15 | 5.2 | 3.17 | 10.40 | 17.31 | 2.00 | 69.5 | 64.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.7 | 3.50 | 10.33 | 17.11 | 5.00 | 79.9 | 90.0 |

## GW34

- Train rows: 157270
- Bank: 0.00 -> 0.80
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 61.59
- Actual score: 72.00
- Transfer: Jean-Philippe Mateta -> Matheus Santos Carneiro Da Cunha (projected gain 4.99, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.5 | 0.00 | 12.99 | 21.07 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Wayne Hennessey | GK | 16 | 4.0 | 0.28 | 0.58 | 1.02 | 0.00 | 6.2 | 0.0 |
| XI | XI | Rayan Aït-Nouri | DEF | 20 | 4.9 | 5.80 | 15.60 | 23.69 | 11.00 | 90.0 | 76.0 |
| Bench 3 | Bench | Joško Gvardiol | DEF | 13 | 6.2 | 0.00 | 12.34 | 20.38 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 0.00 | 12.07 | 19.73 | 0.00 | 0.0 | 0.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.78 | 9.96 | 16.03 | 6.00 | 87.0 | 90.0 |
| XI | XI | Neco Williams | DEF | 16 | 4.5 | 2.80 | 8.07 | 13.51 | 0.00 | 83.7 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 7.14 | 19.33 | 30.79 | 6.00 | 90.0 | 76.0 |
| Bench 4 | Bench | Omar Marmoush | FWD | 13 | 7.6 | 0.00 | 16.10 | 25.82 | 0.00 | 0.0 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.0 | 5.71 | 14.85 | 22.15 | 15.00 | 90.0 | 88.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.12 | 22.19 | 35.90 | 8.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.0 | 6.82 | 20.28 | 32.14 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.54 | 14.15 | 23.80 | 4.00 | 78.0 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 4.87 | 12.96 | 21.28 | 6.00 | 75.3 | 66.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.7 | 3.61 | 10.60 | 17.22 | 6.00 | 80.8 | 90.0 |

## GW35

- Train rows: 158070
- Bank: 0.80 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 56.66
- Actual score: 53.00
- Transfer: Matheus Santos Carneiro Da Cunha -> Yoane Wissa (projected gain 4.09, hit 0)
- Autosub: Enzo Fernández replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.06 | 8.91 | 15.39 | 1.00 | 64.9 | 90.0 |
| Bench 1 | Bench | Wayne Hennessey | GK | 16 | 4.0 | 0.06 | 0.44 | 0.76 | 0.00 | 6.2 | 0.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.59 | 9.52 | 15.27 | 2.00 | 84.9 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 3.15 | 9.41 | 16.29 | 8.00 | 70.7 | 90.0 |
| XI | XI | Neco Williams | DEF | 16 | 4.5 | 2.82 | 8.18 | 13.39 | 5.00 | 83.1 | 90.0 |
| Bench 4 | Bench | Rayan Aït-Nouri | DEF | 20 | 4.9 | 1.97 | 7.77 | 13.77 | 2.00 | 50.6 | 90.0 |
| Bench 3 | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 2.11 | 6.66 | 11.83 | 1.00 | 59.1 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 6.36 | 17.44 | 28.01 | 9.00 | 79.9 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.6 | 4.95 | 14.13 | 22.89 | 7.00 | 89.5 | 90.0 |
| XI | XI | Omar Marmoush | FWD | 13 | 7.6 | 3.43 | 10.97 | 19.23 | 2.00 | 48.0 | 82.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.34 | 21.70 | 35.69 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.0 | 5.97 | 17.48 | 28.01 | 5.00 | 90.0 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.62 | 13.93 | 23.34 | 0.00 | 79.9 | 0.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 4.02 | 11.52 | 19.27 | 1.00 | 60.7 | 55.0 |
| Bench 2 | Autosub In | Enzo Fernández | MID | 6 | 4.7 | 3.14 | 10.17 | 16.77 | 9.00 | 81.2 | 87.0 |