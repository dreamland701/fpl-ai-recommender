# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 289.22
- Total actual points: 238.00
- Average predicted points: 72.31
- Average actual points: 59.50
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
- Predicted score: 97.21
- Actual score: 83.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (15.02) beats the best remaining Triple Captain opportunity (15.61).
- Chip advisory: triple_captain (0.69): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Alexander Isak. Optimizer chose Triple Captain here because the current estimated captain upside (15.02) beats the best remaining Triple Captain opportunity (15.61).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.86 | 11.26 | 18.25 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.61 | 1.38 | 2.21 | 0.00 | 11.8 | 0.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 7.45 | 14.79 | 21.14 | -1.00 | 164.0 | 180.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 6.78 | 12.59 | 17.66 | 8.00 | 154.2 | 180.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.16 | 12.31 | 19.88 | 1.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Djed Spence | DEF | 18 | 4.4 | 2.89 | 8.20 | 13.45 | -2.00 | 81.5 | 90.0 |
| Bench 4 | Bench | Dara O'Shea | DEF | 10 | 3.9 | 2.29 | 7.36 | 12.04 | 1.00 | 89.1 | 90.0 |
| Captain | Captain | Alexander Isak | FWD | 15 | 9.5 | 11.15 | 21.42 | 31.59 | 11.00 | 150.3 | 148.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 8.22 | 16.31 | 23.40 | 2.00 | 144.6 | 100.0 |
| Bench 3 | Bench | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.9 | 2.45 | 7.95 | 13.59 | 1.00 | 61.0 | 26.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 8.35 | 25.20 | 42.33 | 6.00 | 90.0 | 84.0 |
| Vice Captain | XI | Jacob Murphy | MID | 15 | 5.2 | 8.80 | 15.59 | 21.76 | 19.00 | 156.5 | 138.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 5.26 | 15.27 | 26.17 | 4.00 | 65.7 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.6 | 4.82 | 14.80 | 25.19 | 2.00 | 90.0 | 81.0 |
| XI | XI | Ismaïla Sarr | MID | 7 | 5.8 | 6.08 | 14.23 | 20.99 | 7.00 | 132.8 | 165.0 |

## GW33

- Train rows: 156471
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Joško Gvardiol
- Vice captain: David Raya Martin
- Effective captain: Joško Gvardiol
- Chip used: bench_boost
- Predicted score: 87.68
- Actual score: 59.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.09) beats the best remaining Bench Boost opportunity (8.53).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.09) beats the best remaining Bench Boost opportunity (8.53).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Vice Captain | XI | David Raya Martin | GK | 1 | 5.5 | 8.77 | 12.28 | 19.72 | 7.00 | 180.0 | 180.0 |
| Bench 1 | Bench Boost | Daniel Bentley | GK | 20 | 3.9 | 0.34 | 1.10 | 1.79 | 7.00 | 9.4 | 90.0 |
| Captain | Captain | Joško Gvardiol | DEF | 13 | 6.2 | 8.95 | 12.97 | 20.87 | 7.00 | 180.0 | 180.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 8.12 | 11.97 | 18.71 | 6.00 | 180.0 | 180.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.38 | 10.09 | 15.93 | 0.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Djed Spence | DEF | 18 | 4.4 | 2.42 | 7.12 | 11.68 | 1.00 | 77.7 | 90.0 |
| Bench 3 | Bench Boost | Dara O'Shea | DEF | 10 | 3.9 | 2.21 | 7.09 | 11.67 | 0.00 | 87.5 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.71 | 16.65 | 27.75 | 2.00 | 89.9 | 75.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 7.75 | 11.51 | 18.21 | 10.00 | 145.7 | 84.0 |
| Bench 4 | Bench Boost | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 1.88 | 6.13 | 10.33 | 1.00 | 47.4 | 27.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 8.37 | 24.03 | 40.23 | 3.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 4.58 | 14.39 | 24.60 | 2.00 | 70.6 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.50 | 13.96 | 23.42 | 1.00 | 83.8 | 31.0 |
| XI | XI | Ismaïla Sarr | MID | 7 | 5.8 | 8.44 | 12.10 | 19.43 | 3.00 | 180.0 | 117.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 3.31 | 10.28 | 16.85 | 2.00 | 70.4 | 64.0 |

## GW34

- Train rows: 157270
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 50.80
- Actual score: 44.00
- Transfer: Ismaïla Sarr -> Morgan Rogers (projected gain 3.38, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.5 | 0.00 | 9.19 | 17.83 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Daniel Bentley | GK | 20 | 3.9 | 1.69 | 3.64 | 5.34 | 0.00 | 39.4 | 0.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.74 | 9.89 | 16.01 | 6.00 | 85.0 | 90.0 |
| Bench 3 | Bench | Joško Gvardiol | DEF | 13 | 6.2 | 0.00 | 9.56 | 18.75 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 0.00 | 9.56 | 18.59 | 0.00 | 0.0 | 0.0 |
| XI | XI | Djed Spence | DEF | 18 | 4.4 | 2.10 | 6.72 | 11.09 | 0.00 | 75.5 | 90.0 |
| XI | XI | Dara O'Shea | DEF | 10 | 3.9 | 2.05 | 6.70 | 11.09 | 1.00 | 84.6 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 7.11 | 18.78 | 30.24 | 6.00 | 90.0 | 76.0 |
| Bench 4 | Bench | Jean-Philippe Mateta | FWD | 7 | 7.8 | 0.00 | 8.30 | 16.76 | 0.00 | 0.0 | 0.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 1.73 | 5.77 | 9.84 | 2.00 | 47.8 | 63.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.44 | 23.31 | 37.97 | 8.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 5.94 | 16.58 | 27.05 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.51 | 13.81 | 23.32 | 4.00 | 77.6 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 5.07 | 13.07 | 21.53 | 6.00 | 78.0 | 66.0 |
| XI | Bench | Morgan Rogers | MID | 2 | 5.7 | 0.00 | 9.33 | 18.07 | 0.00 | 0.0 | 0.0 |

## GW35

- Train rows: 158070
- Bank: 0.10 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 53.54
- Actual score: 52.00
- Transfer: Jean-Philippe Mateta -> Yoane Wissa (projected gain 18.91, hit 0)
- Autosub: Norberto Bercique Gomes Betuncal replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 2.66 | 8.23 | 14.32 | 1.00 | 60.4 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.27 | 1.12 | 2.02 | 0.00 | 15.8 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 3.18 | 10.03 | 17.16 | 8.00 | 70.1 | 90.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.55 | 9.28 | 14.94 | 2.00 | 83.0 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 2.30 | 7.65 | 13.06 | 1.00 | 62.0 | 90.0 |
| Bench 4 | Bench | Dara O'Shea | DEF | 10 | 3.9 | 2.03 | 6.37 | 10.52 | 1.00 | 81.7 | 90.0 |
| Bench 3 | Bench | Djed Spence | DEF | 18 | 4.4 | 2.22 | 6.20 | 9.91 | 2.00 | 72.3 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 6.30 | 17.05 | 27.44 | 9.00 | 79.6 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.6 | 4.59 | 12.90 | 21.03 | 7.00 | 85.8 | 90.0 |
| Bench 2 | Autosub In | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 2.39 | 6.48 | 10.68 | 6.00 | 53.3 | 76.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.58 | 22.74 | 37.40 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.51 | 13.48 | 22.65 | 0.00 | 79.1 | 0.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.5 | 4.22 | 13.38 | 22.41 | 10.00 | 71.3 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 4.11 | 11.50 | 19.10 | 1.00 | 62.4 | 55.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.7 | 2.95 | 9.23 | 15.96 | 3.00 | 51.0 | 90.0 |