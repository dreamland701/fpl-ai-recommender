# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 301.48
- Total actual points: 254.00
- Average predicted points: 75.37
- Average actual points: 63.50
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
- Predicted score: 88.62
- Actual score: 85.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (13.46) beats the best remaining Triple Captain opportunity (15.88).
- Chip advisory: triple_captain (0.66): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Alexander Isak. Optimizer chose Triple Captain here because the current estimated captain upside (13.46) beats the best remaining Triple Captain opportunity (15.88).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.85 | 12.22 | 20.30 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Cieran Slicker | GK | 10 | 3.9 | 0.10 | 0.34 | 0.60 | 0.00 | 5.4 | 0.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 7.22 | 12.52 | 19.00 | -1.00 | 170.4 | 180.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.06 | 12.13 | 19.37 | 1.00 | 90.0 | 90.0 |
| Bench 2 | Bench | William Saliba | DEF | 1 | 6.5 | 3.75 | 12.13 | 19.07 | 2.00 | 83.2 | 90.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 6.49 | 10.70 | 15.66 | 8.00 | 154.7 | 180.0 |
| Bench 4 | Bench | Neco Williams | DEF | 16 | 4.5 | 3.04 | 9.14 | 14.29 | 2.00 | 87.1 | 90.0 |
| Captain | Captain | Alexander Isak | FWD | 15 | 9.5 | 10.29 | 15.81 | 25.13 | 11.00 | 141.1 | 148.0 |
| XI | XI | Omar Marmoush | FWD | 13 | 7.6 | 4.57 | 13.63 | 21.99 | 7.00 | 77.3 | 81.0 |
| Bench 3 | Bench | Jamie Vardy | FWD | 11 | 5.3 | 3.54 | 9.42 | 15.37 | 2.00 | 76.2 | 60.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 8.29 | 24.61 | 40.82 | 6.00 | 90.0 | 84.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.6 | 4.88 | 14.58 | 25.13 | 2.00 | 90.0 | 81.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.0 | 4.54 | 14.27 | 23.91 | 2.00 | 88.7 | 90.0 |
| Vice Captain | XI | Jacob Murphy | MID | 15 | 5.2 | 8.94 | 13.74 | 20.08 | 19.00 | 150.6 | 138.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 4.92 | 12.91 | 20.06 | 6.00 | 86.9 | 84.0 |

## GW33

- Train rows: 156471
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Omar Marmoush
- Vice captain: William Saliba
- Effective captain: Omar Marmoush
- Chip used: bench_boost
- Predicted score: 102.56
- Actual score: 72.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (14.61) beats the best remaining Bench Boost opportunity (9.96).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (14.61) beats the best remaining Bench Boost opportunity (9.96).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 10.35 | 15.24 | 23.90 | 7.00 | 180.0 | 180.0 |
| Bench 1 | Bench Boost | Cieran Slicker | GK | 10 | 3.9 | 0.00 | 0.15 | 0.39 | 0.00 | 3.8 | 0.0 |
| Vice Captain | XI | William Saliba | DEF | 1 | 6.5 | 10.38 | 16.05 | 24.66 | 7.00 | 180.0 | 180.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 9.24 | 14.48 | 22.60 | 7.00 | 180.0 | 180.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 7.25 | 12.56 | 19.17 | 6.00 | 180.0 | 180.0 |
| Bench 3 | Bench Boost | Tino Livramento | DEF | 15 | 4.6 | 2.65 | 9.27 | 14.46 | 0.00 | 88.9 | 90.0 |
| Bench 4 | Bench Boost | Neco Williams | DEF | 16 | 4.5 | 2.61 | 8.00 | 13.14 | 2.00 | 83.6 | 90.0 |
| Captain | Captain | Omar Marmoush | FWD | 13 | 7.6 | 10.92 | 16.66 | 26.09 | 4.00 | 180.0 | 180.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.23 | 15.54 | 25.58 | 2.00 | 87.2 | 75.0 |
| Bench 2 | Bench Boost | Jamie Vardy | FWD | 11 | 5.3 | 2.66 | 8.75 | 14.40 | 2.00 | 65.0 | 61.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 8.50 | 23.42 | 38.98 | 3.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 8.92 | 14.34 | 21.69 | 7.00 | 176.1 | 166.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 4.83 | 14.08 | 23.36 | 18.00 | 84.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.40 | 13.50 | 23.42 | 1.00 | 85.3 | 31.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 3.71 | 10.70 | 18.01 | 2.00 | 73.5 | 64.0 |

## GW34

- Train rows: 157270
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 54.27
- Actual score: 51.00
- Transfer: Daniel Muñoz -> Rayan Aït-Nouri (projected gain 3.18, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martin | GK | 1 | 5.5 | 0.00 | 14.61 | 23.63 | 0.00 | 0.0 | 0.0 |
| Bench 1 | Bench | Cieran Slicker | GK | 10 | 3.9 | 0.00 | 0.15 | 0.36 | 0.00 | 3.1 | 0.0 |
| XI | XI | Rayan Aït-Nouri | DEF | 20 | 5.0 | 6.21 | 16.07 | 24.53 | 11.00 | 90.0 | 76.0 |
| Bench 2 | Bench | William Saliba | DEF | 1 | 6.5 | 0.00 | 14.10 | 22.35 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Joško Gvardiol | DEF | 13 | 6.2 | 0.00 | 12.11 | 19.94 | 0.00 | 0.0 | 0.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.58 | 8.85 | 14.33 | 6.00 | 83.1 | 90.0 |
| XI | XI | Neco Williams | DEF | 16 | 4.5 | 2.57 | 7.38 | 12.19 | 0.00 | 82.7 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 6.42 | 17.35 | 27.77 | 6.00 | 85.3 | 76.0 |
| Bench 4 | Bench | Omar Marmoush | FWD | 13 | 7.6 | 0.00 | 15.49 | 24.54 | 0.00 | 0.0 | 0.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.3 | 2.64 | 8.73 | 14.46 | 0.00 | 64.7 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.54 | 23.48 | 37.53 | 8.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.0 | 6.63 | 20.03 | 31.46 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.25 | 13.67 | 23.60 | 4.00 | 75.6 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 4.90 | 13.30 | 21.19 | 6.00 | 76.0 | 66.0 |
| XI | Bench | Morgan Rogers | MID | 2 | 5.6 | 0.00 | 12.22 | 19.81 | 0.00 | 0.0 | 0.0 |

## GW35

- Train rows: 158070
- Bank: 0.20 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 56.03
- Actual score: 46.00
- Transfer: David Raya Martin -> Jordan Pickford (projected gain 3.29, hit 0)
- Autosub: Omar Marmoush replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 4.07 | 12.02 | 19.16 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Cieran Slicker | GK | 10 | 3.9 | 0.08 | 0.20 | 0.42 | 0.00 | 3.0 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 3.29 | 9.59 | 16.27 | 8.00 | 74.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.5 | 3.01 | 8.83 | 15.49 | 1.00 | 65.3 | 90.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.30 | 7.70 | 12.56 | 2.00 | 78.4 | 90.0 |
| Bench 3 | Bench | Neco Williams | DEF | 16 | 4.5 | 2.54 | 6.53 | 10.99 | 5.00 | 82.7 | 90.0 |
| Bench 4 | Bench | Rayan Aït-Nouri | DEF | 20 | 5.0 | 0.75 | 5.02 | 8.44 | 2.00 | 37.1 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.37 | 15.00 | 24.71 | 9.00 | 69.4 | 90.0 |
| Bench 2 | Autosub In | Omar Marmoush | FWD | 13 | 7.6 | 2.84 | 9.59 | 16.09 | 2.00 | 45.6 | 82.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.3 | 3.55 | 9.07 | 14.58 | 9.00 | 72.2 | 84.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.78 | 22.59 | 36.98 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.0 | 6.21 | 17.44 | 27.54 | 5.00 | 90.0 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.35 | 13.69 | 23.26 | 0.00 | 78.2 | 0.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 4.33 | 11.66 | 19.50 | 1.00 | 63.0 | 55.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 2.99 | 8.67 | 15.24 | 3.00 | 52.9 | 90.0 |