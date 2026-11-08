# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 306.58
- Total actual points: 267.00
- Average predicted points: 76.64
- Average actual points: 66.75
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
- Captain: Alexander Isak
- Vice captain: Jacob Murphy
- Effective captain: Alexander Isak
- Chip used: triple_captain
- Predicted score: 94.25
- Actual score: 81.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (15.25) beats the best remaining Triple Captain opportunity (15.89).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Alexander Isak. Optimizer chose Triple Captain here because the current estimated captain upside (15.25) beats the best remaining Triple Captain opportunity (15.89).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.5 | 3.91 | 11.38 | 18.44 | 2.00 | 90.0 | 90.0 |
| XI | XI | Dean Henderson | GK | 7 | 4.6 | 5.33 | 10.90 | 16.02 | 2.00 | 152.9 | 180.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 7.57 | 14.98 | 21.39 | -1.00 | 166.5 | 180.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 6.82 | 12.65 | 17.75 | 8.00 | 155.0 | 180.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.17 | 12.35 | 19.93 | 1.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Virgil van Dijk | DEF | 12 | 6.5 | 3.82 | 11.51 | 19.00 | 9.00 | 84.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.5 | 3.86 | 11.46 | 18.14 | 2.00 | 82.7 | 90.0 |
| Captain | Captain | Alexander Isak | FWD | 15 | 9.5 | 11.37 | 21.81 | 32.16 | 11.00 | 155.0 | 148.0 |
| Bench 3 | Bench | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.9 | 2.45 | 7.93 | 13.58 | 1.00 | 60.9 | 26.0 |
| Bench 4 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 2.20 | 6.15 | 10.62 | 1.00 | 43.8 | 45.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 8.30 | 25.06 | 42.17 | 6.00 | 90.0 | 84.0 |
| Vice Captain | XI | Jacob Murphy | MID | 15 | 5.2 | 9.04 | 15.98 | 22.31 | 19.00 | 161.6 | 138.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.6 | 4.70 | 14.49 | 24.70 | 2.00 | 90.0 | 81.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.0 | 4.46 | 14.09 | 23.66 | 2.00 | 89.7 | 90.0 |
| XI | XI | Ismaïla Sarr | MID | 7 | 5.8 | 5.89 | 13.89 | 20.54 | 7.00 | 128.8 | 165.0 |

## GW33

- Train rows: 156471
- Bank: 0.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: William Saliba
- Vice captain: Joško Gvardiol
- Effective captain: William Saliba
- Chip used: bench_boost
- Predicted score: 101.32
- Actual score: 82.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (21.34) beats the best remaining Bench Boost opportunity (13.47).
- Chip advisory: bench_boost (0.65): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (21.34) beats the best remaining Bench Boost opportunity (13.47).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 8.90 | 12.45 | 19.99 | 7.00 | 180.0 | 180.0 |
| Bench 1 | Bench Boost | Dean Henderson | GK | 7 | 4.6 | 7.25 | 10.70 | 16.94 | 10.00 | 180.0 | 180.0 |
| Captain | Captain | William Saliba | DEF | 1 | 6.5 | 10.05 | 13.78 | 21.79 | 7.00 | 180.0 | 180.0 |
| Vice Captain | XI | Joško Gvardiol | DEF | 13 | 6.2 | 9.20 | 13.29 | 21.36 | 7.00 | 180.0 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.5 | 4.51 | 12.62 | 20.76 | 7.00 | 90.0 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 8.42 | 12.34 | 19.29 | 6.00 | 180.0 | 180.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.51 | 10.40 | 16.39 | 0.00 | 90.0 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.91 | 17.14 | 28.50 | 2.00 | 90.0 | 75.0 |
| Bench 3 | Bench Boost | Paul Onuachu | FWD | 17 | 4.9 | 2.10 | 6.38 | 10.49 | 1.00 | 45.4 | 68.0 |
| Bench 4 | Bench Boost | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 1.88 | 6.12 | 10.32 | 1.00 | 47.3 | 27.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 8.32 | 23.92 | 40.11 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.40 | 13.70 | 23.01 | 1.00 | 81.7 | 31.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 4.74 | 13.51 | 22.62 | 18.00 | 83.4 | 90.0 |
| XI | XI | Ismaïla Sarr | MID | 7 | 5.8 | 8.68 | 12.39 | 19.88 | 3.00 | 180.0 | 117.0 |
| Bench 2 | Bench Boost | Jacob Murphy | MID | 15 | 5.2 | 3.41 | 10.54 | 17.23 | 2.00 | 72.7 | 64.0 |

## GW34

- Train rows: 157270
- Bank: 0.20 -> 0.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.94
- Actual score: 49.00
- Transfer: Ismaïla Sarr -> Alex Iwobi (projected gain 6.85, hit 0)
- Autosub: Norberto Bercique Gomes Betuncal replaced Paul Onuachu.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martin | GK | 1 | 5.5 | 0.00 | 9.52 | 18.46 | 0.00 | 0.0 | 0.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.6 | 0.00 | 8.26 | 16.21 | 0.00 | 0.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.5 | 4.76 | 13.07 | 20.97 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | William Saliba | DEF | 1 | 6.5 | 0.00 | 10.42 | 20.05 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 0.00 | 9.99 | 19.43 | 0.00 | 0.0 | 0.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.76 | 9.94 | 16.10 | 6.00 | 85.4 | 90.0 |
| Bench 3 | Bench | Joško Gvardiol | DEF | 13 | 6.2 | 0.00 | 9.90 | 19.39 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 7.28 | 19.25 | 30.97 | 6.00 | 90.0 | 76.0 |
| XI | Bench | Paul Onuachu | FWD | 17 | 4.9 | 1.88 | 5.98 | 9.57 | 0.00 | 41.6 | 0.0 |
| Bench 2 | Autosub In | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 1.71 | 5.73 | 9.78 | 2.00 | 47.6 | 63.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.47 | 23.40 | 38.13 | 8.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.0 | 7.01 | 19.92 | 31.81 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.41 | 13.55 | 22.92 | 4.00 | 75.6 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 5.11 | 13.19 | 21.72 | 6.00 | 79.0 | 66.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.6 | 4.79 | 12.23 | 19.37 | 5.00 | 90.0 | 85.0 |

## GW35

- Train rows: 158070
- Bank: 0.40 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.07
- Actual score: 55.00
- Transfer: Alex Iwobi -> Alejandro Garnacho (projected gain 3.30, hit 0)
- Autosub: Norberto Bercique Gomes Betuncal replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 2.51 | 7.87 | 13.77 | 1.00 | 57.2 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.6 | 1.67 | 5.95 | 10.30 | 3.00 | 64.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.6 | 3.31 | 10.55 | 17.67 | 6.00 | 79.7 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 3.04 | 9.70 | 16.67 | 8.00 | 67.3 | 90.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.56 | 9.31 | 14.96 | 2.00 | 83.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.5 | 2.93 | 9.26 | 16.14 | 1.00 | 59.3 | 90.0 |
| Bench 3 | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 2.16 | 7.30 | 12.53 | 1.00 | 59.0 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 6.45 | 17.46 | 28.06 | 9.00 | 82.7 | 90.0 |
| Bench 2 | Autosub In | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 2.42 | 6.55 | 10.80 | 6.00 | 53.9 | 76.0 |
| Bench 4 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 1.28 | 3.62 | 6.24 | 1.00 | 21.6 | 45.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.59 | 22.77 | 37.45 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.0 | 6.05 | 17.24 | 27.73 | 5.00 | 90.0 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.43 | 13.27 | 22.32 | 0.00 | 77.4 | 0.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 4.15 | 11.61 | 19.25 | 1.00 | 63.2 | 55.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 5.9 | 3.47 | 9.84 | 15.98 | 12.00 | 72.3 | 90.0 |