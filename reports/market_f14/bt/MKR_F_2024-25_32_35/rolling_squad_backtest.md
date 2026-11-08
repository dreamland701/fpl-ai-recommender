# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 309.86
- Total actual points: 268.00
- Average predicted points: 77.47
- Average actual points: 67.00
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
- Captain: Alexander Isak
- Vice captain: Jacob Murphy
- Effective captain: Alexander Isak
- Chip used: triple_captain
- Predicted score: 94.23
- Actual score: 81.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (14.68) beats the best remaining Triple Captain opportunity (15.22).
- Chip advisory: triple_captain (0.69): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Alexander Isak. Optimizer chose Triple Captain here because the current estimated captain upside (14.68) beats the best remaining Triple Captain opportunity (15.22).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.07 | 11.65 | 18.63 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.31 | 0.42 | 0.66 | 0.00 | 6.5 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.29 | 12.74 | 20.36 | 1.00 | 90.0 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 7.06 | 12.24 | 19.03 | -1.00 | 168.9 | 180.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 7.31 | 12.00 | 17.52 | 8.00 | 147.8 | 180.0 |
| Bench 3 | Bench | Neco Williams | DEF | 16 | 4.5 | 3.50 | 9.52 | 15.13 | 2.00 | 84.7 | 90.0 |
| Bench 4 | Bench | Rayan Aït-Nouri | DEF | 20 | 4.8 | 3.29 | 9.23 | 15.23 | 14.00 | 74.1 | 69.0 |
| Captain | Captain | Alexander Isak | FWD | 15 | 9.5 | 11.16 | 17.21 | 26.88 | 11.00 | 153.0 | 148.0 |
| XI | XI | Omar Marmoush | FWD | 13 | 7.6 | 4.62 | 13.56 | 21.56 | 7.00 | 77.0 | 81.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 7.42 | 12.86 | 20.13 | 2.00 | 148.6 | 100.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 8.06 | 23.91 | 39.47 | 6.00 | 90.0 | 84.0 |
| Vice Captain | XI | Jacob Murphy | MID | 15 | 5.2 | 9.07 | 13.95 | 19.92 | 19.00 | 153.6 | 138.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.0 | 4.43 | 13.60 | 23.33 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.6 | 4.42 | 13.60 | 24.07 | 2.00 | 90.0 | 81.0 |
| Bench 2 | Bench | Enzo Fernández | MID | 6 | 4.7 | 4.03 | 11.23 | 17.81 | 2.00 | 76.2 | 90.0 |

## GW33

- Train rows: 156471
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Omar Marmoush
- Vice captain: David Raya Martin
- Effective captain: Omar Marmoush
- Chip used: bench_boost
- Predicted score: 105.92
- Actual score: 84.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (16.49) beats the best remaining Bench Boost opportunity (11.07).
- Transfer: Rayan Aït-Nouri -> Jakub Kiwior (projected gain 1.14, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (16.49) beats the best remaining Bench Boost opportunity (11.07).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Vice Captain | XI | David Raya Martin | GK | 1 | 5.5 | 11.27 | 16.96 | 25.42 | 7.00 | 180.0 | 180.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.12 | 0.25 | 0.50 | 0.00 | 4.4 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 9.98 | 16.29 | 24.83 | 7.00 | 180.0 | 180.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 8.89 | 14.38 | 21.72 | 6.00 | 180.0 | 180.0 |
| XI | XI | Jakub Kiwior | DEF | 1 | 4.8 | 7.53 | 11.47 | 15.94 | 13.00 | 114.2 | 180.0 |
| Bench 3 | Bench Boost | Tino Livramento | DEF | 15 | 4.6 | 3.39 | 10.60 | 17.04 | 0.00 | 90.0 | 90.0 |
| Bench 4 | Bench Boost | Neco Williams | DEF | 16 | 4.5 | 2.89 | 8.36 | 13.99 | 2.00 | 85.7 | 90.0 |
| Captain | Captain | Omar Marmoush | FWD | 13 | 7.6 | 12.38 | 18.92 | 28.00 | 4.00 | 175.2 | 180.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.68 | 16.36 | 27.60 | 2.00 | 90.0 | 75.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 7.70 | 13.01 | 19.96 | 10.00 | 148.1 | 84.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 8.05 | 23.13 | 38.12 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.39 | 13.57 | 23.00 | 1.00 | 82.5 | 31.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 4.46 | 12.94 | 22.10 | 18.00 | 85.9 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 3.42 | 10.98 | 18.38 | 2.00 | 73.5 | 64.0 |
| Bench 2 | Bench Boost | Enzo Fernández | MID | 6 | 4.7 | 3.39 | 9.97 | 16.53 | 5.00 | 77.4 | 90.0 |

## GW34

- Train rows: 157270
- Bank: 0.10 -> 1.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 56.60
- Actual score: 57.00
- Transfer: Joško Gvardiol -> Rayan Aït-Nouri (projected gain 5.85, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.5 | 0.00 | 9.91 | 16.96 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Killian Cahill | GK | 5 | 3.9 | 0.14 | 0.02 | 0.11 | 0.00 | 2.4 | 0.0 |
| XI | XI | Rayan Aït-Nouri | DEF | 20 | 5.0 | 5.73 | 15.38 | 23.51 | 11.00 | 90.0 | 76.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 4.12 | 11.82 | 18.53 | 6.00 | 81.1 | 90.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 0.00 | 10.73 | 18.85 | 0.00 | 0.0 | 0.0 |
| XI | XI | Neco Williams | DEF | 16 | 4.5 | 2.98 | 8.59 | 14.19 | 0.00 | 84.0 | 90.0 |
| Bench 3 | Bench | Jakub Kiwior | DEF | 1 | 4.8 | 0.00 | 6.45 | 10.84 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 7.19 | 19.68 | 31.08 | 6.00 | 90.0 | 76.0 |
| Bench 4 | Bench | Omar Marmoush | FWD | 13 | 7.6 | 0.00 | 13.82 | 24.06 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Jean-Philippe Mateta | FWD | 7 | 7.8 | 0.00 | 9.57 | 17.33 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.25 | 23.09 | 37.12 | 8.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.0 | 6.79 | 19.73 | 31.83 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 5.13 | 13.82 | 22.18 | 6.00 | 76.8 | 66.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.18 | 13.19 | 22.67 | 4.00 | 78.1 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.7 | 3.83 | 11.05 | 17.43 | 6.00 | 76.1 | 90.0 |

## GW35

- Train rows: 158070
- Bank: 1.30 -> 2.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 53.12
- Actual score: 46.00
- Transfer: Jean-Philippe Mateta -> Yoane Wissa (projected gain 3.33, hit 0)
- Autosub: Enzo Fernández replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 2.53 | 7.66 | 13.40 | 1.00 | 57.3 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.00 | 0.00 | 0.02 | 0.00 | 1.3 | 0.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.27 | 9.12 | 15.02 | 2.00 | 84.6 | 90.0 |
| XI | XI | Neco Williams | DEF | 16 | 4.5 | 2.97 | 8.30 | 13.66 | 5.00 | 84.4 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 2.67 | 7.66 | 13.11 | 1.00 | 57.8 | 90.0 |
| Bench 3 | Bench | Rayan Aït-Nouri | DEF | 20 | 5.0 | 1.63 | 6.94 | 12.92 | 2.00 | 50.0 | 90.0 |
| Bench 4 | Bench | Jakub Kiwior | DEF | 1 | 4.8 | 1.58 | 5.08 | 8.45 | 1.00 | 41.7 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 6.00 | 16.32 | 26.91 | 9.00 | 86.9 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.6 | 4.47 | 13.16 | 21.20 | 7.00 | 84.6 | 90.0 |
| XI | XI | Omar Marmoush | FWD | 13 | 7.6 | 3.21 | 10.62 | 17.67 | 2.00 | 35.7 | 82.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.14 | 21.27 | 35.48 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.0 | 5.79 | 17.09 | 27.42 | 5.00 | 90.0 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.11 | 12.71 | 21.91 | 0.00 | 80.3 | 0.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 3.80 | 10.80 | 18.68 | 1.00 | 66.6 | 55.0 |
| Bench 2 | Autosub In | Enzo Fernández | MID | 6 | 4.7 | 3.11 | 10.01 | 16.49 | 9.00 | 78.6 | 87.0 |