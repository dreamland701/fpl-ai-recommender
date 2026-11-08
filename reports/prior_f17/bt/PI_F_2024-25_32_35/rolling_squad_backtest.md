# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 307.73
- Total actual points: 279.00
- Average predicted points: 76.93
- Average actual points: 69.75
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
- Predicted score: 95.61
- Actual score: 81.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (14.68) beats the best remaining Triple Captain opportunity (15.88).
- Chip advisory: triple_captain (0.69): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Alexander Isak. Optimizer chose Triple Captain here because the current estimated captain upside (14.68) beats the best remaining Triple Captain opportunity (15.88).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.88 | 11.22 | 18.02 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.70 | 1.65 | 2.73 | 0.00 | 13.0 | 0.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 7.48 | 12.57 | 19.29 | -1.00 | 163.2 | 180.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.19 | 12.42 | 19.93 | 1.00 | 90.0 | 90.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 6.81 | 11.02 | 16.56 | 8.00 | 154.0 | 180.0 |
| Bench 3 | Bench | Nikola Milenković | DEF | 16 | 5.1 | 3.60 | 10.66 | 16.83 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Toti António Gomes | DEF | 20 | 4.3 | 3.03 | 8.25 | 13.48 | 0.00 | 82.0 | 90.0 |
| Captain | Captain | Alexander Isak | FWD | 15 | 9.5 | 11.16 | 17.12 | 27.05 | 11.00 | 150.4 | 148.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 8.38 | 14.07 | 21.63 | 2.00 | 143.9 | 100.0 |
| XI | XI | Omar Marmoush | FWD | 13 | 7.6 | 4.59 | 13.46 | 21.56 | 7.00 | 77.1 | 81.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 8.55 | 24.99 | 41.41 | 6.00 | 90.0 | 84.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.6 | 4.87 | 14.93 | 25.61 | 2.00 | 90.0 | 81.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.0 | 4.55 | 14.38 | 24.10 | 2.00 | 89.6 | 90.0 |
| Vice Captain | XI | Jacob Murphy | MID | 15 | 5.2 | 8.84 | 13.61 | 20.29 | 19.00 | 155.8 | 138.0 |
| Bench 2 | Bench | Enzo Fernández | MID | 6 | 4.7 | 3.75 | 10.21 | 16.69 | 2.00 | 79.5 | 90.0 |

## GW33

- Train rows: 156471
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Omar Marmoush
- Vice captain: Joško Gvardiol
- Effective captain: Omar Marmoush
- Chip used: bench_boost
- Predicted score: 97.22
- Actual score: 87.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (15.71) beats the best remaining Bench Boost opportunity (10.44).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (15.71) beats the best remaining Bench Boost opportunity (10.44).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 8.80 | 13.56 | 20.96 | 7.00 | 180.0 | 180.0 |
| Bench 1 | Bench Boost | Daniel Bentley | GK | 20 | 3.9 | 0.43 | 1.37 | 2.36 | 7.00 | 10.5 | 90.0 |
| Vice Captain | XI | Joško Gvardiol | DEF | 13 | 6.2 | 9.01 | 14.58 | 22.57 | 7.00 | 180.0 | 180.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 8.15 | 13.27 | 20.27 | 6.00 | 180.0 | 180.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.41 | 10.64 | 16.94 | 0.00 | 90.0 | 90.0 |
| Bench 3 | Bench Boost | Nikola Milenković | DEF | 16 | 5.1 | 3.17 | 9.31 | 15.18 | 2.00 | 83.3 | 90.0 |
| Bench 4 | Bench Boost | Toti António Gomes | DEF | 20 | 4.3 | 2.53 | 7.51 | 12.33 | 9.00 | 79.1 | 90.0 |
| Captain | Captain | Omar Marmoush | FWD | 13 | 7.6 | 11.69 | 17.82 | 27.57 | 4.00 | 180.0 | 180.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.71 | 16.56 | 27.61 | 2.00 | 90.0 | 75.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 7.92 | 13.41 | 20.56 | 10.00 | 144.8 | 84.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 8.57 | 23.88 | 39.58 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.55 | 14.11 | 23.75 | 1.00 | 83.5 | 31.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 4.90 | 14.00 | 23.32 | 18.00 | 84.6 | 90.0 |
| Bench 2 | Bench Boost | Jacob Murphy | MID | 15 | 5.2 | 3.33 | 10.91 | 18.12 | 2.00 | 70.2 | 64.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.7 | 3.34 | 9.90 | 16.41 | 5.00 | 77.6 | 90.0 |

## GW34

- Train rows: 157270
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 58.87
- Actual score: 62.00
- Transfer: Nikola Milenković -> Rayan Aït-Nouri (projected gain 5.21, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.5 | 0.00 | 12.19 | 19.72 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Daniel Bentley | GK | 20 | 3.9 | 1.78 | 4.19 | 6.39 | 0.00 | 40.3 | 0.0 |
| XI | XI | Rayan Aït-Nouri | DEF | 20 | 5.0 | 5.81 | 15.56 | 23.59 | 11.00 | 90.0 | 76.0 |
| Bench 3 | Bench | Joško Gvardiol | DEF | 13 | 6.2 | 0.00 | 12.77 | 21.02 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 0.00 | 12.68 | 20.86 | 0.00 | 0.0 | 0.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.75 | 10.05 | 16.25 | 6.00 | 84.8 | 90.0 |
| XI | XI | Toti António Gomes | DEF | 20 | 4.3 | 2.99 | 7.75 | 12.64 | 5.00 | 76.2 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 7.10 | 19.15 | 30.47 | 6.00 | 90.0 | 76.0 |
| Bench 4 | Bench | Omar Marmoush | FWD | 13 | 7.6 | 0.00 | 15.37 | 24.62 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Jean-Philippe Mateta | FWD | 7 | 7.8 | 0.00 | 11.08 | 18.96 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.65 | 23.58 | 38.03 | 8.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.0 | 6.99 | 20.71 | 32.76 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.57 | 14.20 | 23.86 | 4.00 | 77.4 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 5.07 | 13.48 | 22.08 | 6.00 | 77.9 | 66.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.7 | 3.51 | 10.30 | 16.73 | 6.00 | 78.8 | 90.0 |

## GW35

- Train rows: 158070
- Bank: 0.10 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 56.04
- Actual score: 49.00
- Transfer: Jean-Philippe Mateta -> Yoane Wissa (projected gain 3.34, hit 0)
- Autosub: Enzo Fernández replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 2.66 | 7.79 | 13.57 | 1.00 | 60.1 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.36 | 1.54 | 2.87 | 0.00 | 16.7 | 0.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.56 | 9.63 | 15.54 | 2.00 | 82.8 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 3.20 | 9.56 | 16.51 | 8.00 | 69.8 | 90.0 |
| Bench 4 | Bench | Rayan Aït-Nouri | DEF | 20 | 5.0 | 1.97 | 7.75 | 13.71 | 2.00 | 50.5 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 2.29 | 7.16 | 12.61 | 1.00 | 61.7 | 90.0 |
| Bench 3 | Bench | Toti António Gomes | DEF | 20 | 4.3 | 2.05 | 6.94 | 11.80 | 2.00 | 75.7 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 6.29 | 17.20 | 27.62 | 9.00 | 79.8 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.6 | 4.60 | 13.12 | 21.26 | 7.00 | 85.7 | 90.0 |
| XI | XI | Omar Marmoush | FWD | 13 | 7.6 | 3.05 | 9.90 | 17.53 | 2.00 | 43.5 | 82.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.79 | 22.87 | 37.49 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.0 | 6.12 | 17.86 | 28.57 | 5.00 | 90.0 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.57 | 13.76 | 23.06 | 0.00 | 78.9 | 0.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 4.10 | 11.74 | 19.63 | 1.00 | 62.3 | 55.0 |
| Bench 2 | Autosub In | Enzo Fernández | MID | 6 | 4.7 | 3.05 | 9.92 | 16.36 | 9.00 | 79.4 | 87.0 |