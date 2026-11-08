# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 294.86
- Total actual points: 261.00
- Average predicted points: 73.72
- Average actual points: 65.25
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
- Predicted score: 95.44
- Actual score: 82.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (14.54) beats the best remaining Triple Captain opportunity (15.65).
- Chip advisory: triple_captain (0.69): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Alexander Isak. Optimizer chose Triple Captain here because the current estimated captain upside (14.54) beats the best remaining Triple Captain opportunity (15.65).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.87 | 11.21 | 17.99 | 2.00 | 89.0 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.70 | 1.55 | 2.47 | 0.00 | 9.2 | 0.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 7.42 | 12.54 | 19.30 | -1.00 | 166.5 | 180.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.15 | 12.32 | 19.80 | 1.00 | 90.0 | 90.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 6.84 | 11.09 | 16.71 | 8.00 | 155.6 | 180.0 |
| Bench 2 | Bench | Neco Williams | DEF | 16 | 4.5 | 3.19 | 9.24 | 15.01 | 2.00 | 87.5 | 90.0 |
| Bench 4 | Bench | Dara O'Shea | DEF | 10 | 3.9 | 2.26 | 7.23 | 11.90 | 1.00 | 90.0 | 90.0 |
| Captain | Captain | Alexander Isak | FWD | 15 | 9.5 | 11.02 | 16.89 | 26.67 | 11.00 | 150.8 | 148.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 8.14 | 13.70 | 21.04 | 2.00 | 143.0 | 100.0 |
| Bench 3 | Bench | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.9 | 2.41 | 7.95 | 13.34 | 1.00 | 60.2 | 26.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 8.39 | 24.61 | 40.90 | 6.00 | 90.0 | 84.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 5.31 | 15.23 | 26.17 | 4.00 | 66.8 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.6 | 4.81 | 14.75 | 25.32 | 2.00 | 90.0 | 81.0 |
| Vice Captain | XI | Jacob Murphy | MID | 15 | 5.2 | 8.73 | 13.47 | 20.07 | 19.00 | 156.2 | 138.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 4.73 | 12.38 | 19.75 | 6.00 | 87.8 | 84.0 |

## GW33

- Train rows: 156471
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Joško Gvardiol
- Vice captain: David Raya Martin
- Effective captain: Joško Gvardiol
- Chip used: bench_boost
- Predicted score: 88.27
- Actual score: 64.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.64) beats the best remaining Bench Boost opportunity (8.95).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.64) beats the best remaining Bench Boost opportunity (8.95).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Vice Captain | XI | David Raya Martin | GK | 1 | 5.5 | 8.80 | 13.57 | 20.97 | 7.00 | 180.0 | 180.0 |
| Bench 1 | Bench Boost | Daniel Bentley | GK | 20 | 3.9 | 0.42 | 1.27 | 2.08 | 7.00 | 6.8 | 90.0 |
| Captain | Captain | Joško Gvardiol | DEF | 13 | 6.2 | 8.91 | 14.46 | 22.41 | 7.00 | 180.0 | 180.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 8.14 | 13.30 | 20.39 | 6.00 | 180.0 | 180.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.39 | 10.62 | 16.93 | 0.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Neco Williams | DEF | 16 | 4.5 | 2.96 | 8.53 | 14.15 | 2.00 | 86.2 | 90.0 |
| Bench 3 | Bench Boost | Dara O'Shea | DEF | 10 | 3.9 | 2.17 | 7.02 | 11.65 | 0.00 | 88.9 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.66 | 16.39 | 27.31 | 2.00 | 90.0 | 75.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 7.69 | 13.07 | 20.03 | 10.00 | 144.1 | 84.0 |
| Bench 4 | Bench Boost | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 1.84 | 6.05 | 10.17 | 1.00 | 46.3 | 27.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 8.40 | 23.48 | 39.04 | 3.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 8.61 | 14.44 | 22.19 | 7.00 | 180.0 | 166.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 4.61 | 13.99 | 24.11 | 2.00 | 71.5 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.49 | 13.93 | 23.49 | 1.00 | 83.9 | 31.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 3.26 | 10.69 | 17.77 | 2.00 | 70.1 | 64.0 |

## GW34

- Train rows: 157270
- Bank: 0.10 -> 0.90
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 57.15
- Actual score: 59.00
- Transfer: Jean-Philippe Mateta -> Matheus Santos Carneiro Da Cunha (projected gain 3.26, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.5 | 0.00 | 12.18 | 19.69 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Daniel Bentley | GK | 20 | 3.9 | 1.77 | 4.09 | 6.12 | 0.00 | 36.5 | 0.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 0.00 | 12.67 | 20.89 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Joško Gvardiol | DEF | 13 | 6.2 | 0.00 | 12.60 | 20.79 | 0.00 | 0.0 | 0.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.74 | 10.03 | 16.25 | 6.00 | 85.6 | 90.0 |
| XI | XI | Neco Williams | DEF | 16 | 4.5 | 2.87 | 8.27 | 13.84 | 0.00 | 85.8 | 90.0 |
| XI | XI | Dara O'Shea | DEF | 10 | 3.9 | 2.02 | 6.57 | 11.06 | 1.00 | 86.1 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 7.05 | 18.96 | 30.14 | 6.00 | 90.0 | 76.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.0 | 5.60 | 14.46 | 21.51 | 15.00 | 89.1 | 88.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 1.68 | 5.57 | 9.53 | 2.00 | 46.7 | 63.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.47 | 23.16 | 37.46 | 8.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 5.97 | 17.02 | 27.66 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.52 | 14.06 | 23.66 | 4.00 | 77.5 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 4.99 | 13.24 | 21.67 | 6.00 | 77.8 | 66.0 |
| Bench 4 | Bench | Morgan Rogers | MID | 2 | 5.6 | 0.00 | 12.40 | 20.19 | 0.00 | 0.0 | 0.0 |

## GW35

- Train rows: 158070
- Bank: 0.90 -> 1.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 54.00
- Actual score: 56.00
- Transfer: Matheus Santos Carneiro Da Cunha -> Yoane Wissa (projected gain 6.73, hit 0)
- Autosub: Norberto Bercique Gomes Betuncal replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 2.67 | 7.81 | 13.59 | 1.00 | 57.8 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.35 | 1.44 | 2.59 | 0.00 | 13.0 | 0.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.54 | 9.58 | 15.47 | 2.00 | 83.5 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 3.14 | 9.39 | 16.27 | 8.00 | 71.7 | 90.0 |
| XI | XI | Neco Williams | DEF | 16 | 4.5 | 2.89 | 8.40 | 13.78 | 5.00 | 85.0 | 90.0 |
| Bench 3 | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 2.29 | 7.19 | 12.72 | 1.00 | 63.6 | 90.0 |
| Bench 4 | Bench | Dara O'Shea | DEF | 10 | 3.9 | 2.00 | 6.18 | 10.45 | 1.00 | 83.4 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 6.27 | 17.11 | 27.44 | 9.00 | 79.8 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.6 | 4.52 | 12.85 | 20.80 | 7.00 | 85.2 | 90.0 |
| Bench 2 | Autosub In | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 2.35 | 6.20 | 10.29 | 6.00 | 52.0 | 76.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.64 | 22.50 | 37.00 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.56 | 13.73 | 23.03 | 0.00 | 78.7 | 0.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.5 | 4.24 | 13.15 | 22.17 | 10.00 | 71.9 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 4.05 | 11.56 | 19.30 | 1.00 | 62.0 | 55.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 2.85 | 8.61 | 15.10 | 3.00 | 51.3 | 90.0 |