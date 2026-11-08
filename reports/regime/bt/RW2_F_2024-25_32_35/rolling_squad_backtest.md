# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 310.72
- Total actual points: 282.00
- Average predicted points: 77.68
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
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Alexander Isak
- Vice captain: Jacob Murphy
- Effective captain: Alexander Isak
- Chip used: triple_captain
- Predicted score: 95.40
- Actual score: 81.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (14.64) beats the best remaining Triple Captain opportunity (15.73).
- Chip advisory: triple_captain (0.69): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Alexander Isak. Optimizer chose Triple Captain here because the current estimated captain upside (14.64) beats the best remaining Triple Captain opportunity (15.73).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.78 | 10.99 | 17.73 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Steven Benda | GK | 9 | 3.9 | 0.18 | 0.69 | 1.22 | 0.00 | 10.1 | 0.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 7.50 | 12.81 | 19.69 | -1.00 | 166.4 | 180.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.12 | 12.17 | 19.47 | 1.00 | 90.0 | 90.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 6.94 | 11.06 | 16.50 | 8.00 | 157.4 | 180.0 |
| Bench 4 | Bench | Neco Williams | DEF | 16 | 4.5 | 3.24 | 9.33 | 15.14 | 2.00 | 87.6 | 90.0 |
| Bench 3 | Bench | Rayan Aït-Nouri | DEF | 20 | 4.8 | 3.37 | 9.33 | 15.46 | 14.00 | 73.9 | 69.0 |
| Captain | Captain | Alexander Isak | FWD | 15 | 9.5 | 11.12 | 17.22 | 27.07 | 11.00 | 148.2 | 148.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 8.43 | 14.19 | 21.92 | 2.00 | 145.7 | 100.0 |
| XI | XI | Omar Marmoush | FWD | 13 | 7.6 | 4.52 | 13.19 | 21.30 | 7.00 | 77.7 | 81.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 8.44 | 25.44 | 42.19 | 6.00 | 90.0 | 84.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.6 | 4.87 | 14.78 | 25.37 | 2.00 | 90.0 | 81.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.0 | 4.41 | 14.01 | 23.55 | 2.00 | 88.9 | 90.0 |
| Vice Captain | XI | Jacob Murphy | MID | 15 | 5.2 | 9.04 | 13.70 | 20.50 | 19.00 | 160.5 | 138.0 |
| Bench 2 | Bench | Enzo Fernández | MID | 6 | 4.7 | 3.77 | 10.40 | 17.23 | 2.00 | 81.3 | 90.0 |

## GW33

- Train rows: 156471
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Omar Marmoush
- Vice captain: Joško Gvardiol
- Effective captain: Omar Marmoush
- Chip used: bench_boost
- Predicted score: 97.19
- Actual score: 76.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (16.42) beats the best remaining Bench Boost opportunity (11.33).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (16.42) beats the best remaining Bench Boost opportunity (11.33).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 8.69 | 13.55 | 20.98 | 7.00 | 180.0 | 180.0 |
| Bench 1 | Bench Boost | Steven Benda | GK | 9 | 3.9 | 0.34 | 0.75 | 1.19 | 0.00 | 8.7 | 0.0 |
| Vice Captain | XI | Joško Gvardiol | DEF | 13 | 6.2 | 8.83 | 14.44 | 22.39 | 7.00 | 180.0 | 180.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 8.41 | 13.65 | 20.79 | 6.00 | 180.0 | 180.0 |
| XI | XI | Rayan Aït-Nouri | DEF | 20 | 4.8 | 3.58 | 10.70 | 17.74 | 5.00 | 76.0 | 81.0 |
| Bench 2 | Bench Boost | Tino Livramento | DEF | 15 | 4.6 | 3.45 | 10.43 | 16.56 | 0.00 | 90.0 | 90.0 |
| Bench 4 | Bench Boost | Neco Williams | DEF | 16 | 4.5 | 2.97 | 8.58 | 14.17 | 2.00 | 85.8 | 90.0 |
| Captain | Captain | Omar Marmoush | FWD | 13 | 7.6 | 11.57 | 17.50 | 27.37 | 4.00 | 180.0 | 180.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.63 | 16.18 | 27.06 | 2.00 | 88.9 | 75.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 7.62 | 13.13 | 20.16 | 10.00 | 143.9 | 84.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 8.35 | 23.71 | 39.23 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.55 | 14.04 | 23.79 | 1.00 | 83.9 | 31.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 4.77 | 13.67 | 22.76 | 18.00 | 84.3 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 3.46 | 10.67 | 17.83 | 2.00 | 73.9 | 64.0 |
| Bench 3 | Bench Boost | Enzo Fernández | MID | 6 | 4.7 | 3.40 | 10.11 | 17.02 | 5.00 | 79.3 | 90.0 |

## GW34

- Train rows: 157270
- Bank: 0.10 -> 0.90
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 62.69
- Actual score: 72.00
- Transfer: Jean-Philippe Mateta -> Matheus Santos Carneiro Da Cunha (projected gain 4.85, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.5 | 0.00 | 12.08 | 19.56 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Steven Benda | GK | 9 | 3.9 | 0.45 | 0.81 | 1.27 | 0.00 | 7.7 | 0.0 |
| XI | XI | Rayan Aït-Nouri | DEF | 20 | 4.9 | 5.96 | 15.80 | 23.83 | 11.00 | 90.0 | 76.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 0.00 | 12.99 | 21.36 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Joško Gvardiol | DEF | 13 | 6.2 | 0.00 | 12.60 | 20.67 | 0.00 | 0.0 | 0.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.72 | 9.79 | 15.91 | 6.00 | 86.1 | 90.0 |
| XI | XI | Neco Williams | DEF | 16 | 4.5 | 2.87 | 8.33 | 13.93 | 0.00 | 85.3 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 7.05 | 18.89 | 29.97 | 6.00 | 90.0 | 76.0 |
| Bench 4 | Bench | Omar Marmoush | FWD | 13 | 7.6 | 0.00 | 15.13 | 24.31 | 0.00 | 0.0 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.0 | 5.68 | 14.79 | 21.83 | 15.00 | 90.0 | 88.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.38 | 23.21 | 37.39 | 8.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.0 | 6.94 | 20.41 | 31.96 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.56 | 14.17 | 24.01 | 4.00 | 77.3 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 5.16 | 13.26 | 21.77 | 6.00 | 80.1 | 66.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.7 | 3.56 | 10.48 | 17.10 | 6.00 | 80.5 | 90.0 |

## GW35

- Train rows: 158070
- Bank: 0.90 -> 1.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.44
- Actual score: 53.00
- Transfer: Matheus Santos Carneiro Da Cunha -> Yoane Wissa (projected gain 3.76, hit 0)
- Autosub: Omar Marmoush replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 2.52 | 7.65 | 13.49 | 1.00 | 58.6 | 90.0 |
| Bench 1 | Bench | Steven Benda | GK | 9 | 3.9 | 0.05 | 0.38 | 0.76 | 0.00 | 8.2 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 3.08 | 9.37 | 16.28 | 8.00 | 69.1 | 90.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.53 | 9.27 | 15.00 | 2.00 | 83.7 | 90.0 |
| XI | XI | Neco Williams | DEF | 16 | 4.5 | 2.91 | 8.37 | 13.68 | 5.00 | 84.0 | 90.0 |
| Bench 4 | Bench | Rayan Aït-Nouri | DEF | 20 | 4.9 | 1.98 | 7.78 | 13.62 | 2.00 | 52.5 | 90.0 |
| Bench 3 | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 2.30 | 7.16 | 12.79 | 1.00 | 60.4 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 6.10 | 16.54 | 26.57 | 9.00 | 78.0 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.6 | 4.61 | 13.18 | 21.34 | 7.00 | 86.3 | 90.0 |
| Bench 2 | Autosub In | Omar Marmoush | FWD | 13 | 7.6 | 2.91 | 9.77 | 17.56 | 2.00 | 43.3 | 82.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.45 | 22.26 | 36.44 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.0 | 5.97 | 17.35 | 27.63 | 5.00 | 90.0 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.57 | 13.94 | 23.41 | 0.00 | 78.7 | 0.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 4.17 | 11.53 | 19.16 | 1.00 | 63.9 | 55.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.7 | 3.08 | 10.04 | 16.60 | 9.00 | 80.8 | 87.0 |