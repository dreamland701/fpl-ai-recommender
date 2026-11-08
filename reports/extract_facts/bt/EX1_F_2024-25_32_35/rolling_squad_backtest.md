# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 292.29
- Total actual points: 254.00
- Average predicted points: 73.07
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
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Alexander Isak
- Vice captain: Jacob Murphy
- Effective captain: Alexander Isak
- Chip used: triple_captain
- Predicted score: 92.07
- Actual score: 82.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (13.83) beats the best remaining Triple Captain opportunity (15.97).
- Chip advisory: bench_boost (0.56): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.63): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Alexander Isak. Optimizer chose Triple Captain here because the current estimated captain upside (13.83) beats the best remaining Triple Captain opportunity (15.97).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.87 | 11.24 | 18.05 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Matt Turner | GK | 7 | 3.9 | 1.18 | 3.11 | 4.58 | 0.00 | 28.6 | 0.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 7.40 | 12.52 | 19.22 | -1.00 | 163.0 | 180.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.16 | 12.35 | 19.79 | 1.00 | 90.0 | 90.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 6.71 | 10.91 | 16.40 | 8.00 | 153.0 | 180.0 |
| Bench 2 | Bench | Neco Williams | DEF | 16 | 4.5 | 3.18 | 9.21 | 14.93 | 2.00 | 86.5 | 90.0 |
| Bench 4 | Bench | Dara O'Shea | DEF | 10 | 3.9 | 2.30 | 7.32 | 12.03 | 1.00 | 89.2 | 90.0 |
| Captain | Captain | Alexander Isak | FWD | 15 | 9.5 | 9.96 | 16.36 | 26.67 | 11.00 | 134.1 | 148.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 8.11 | 13.76 | 21.14 | 2.00 | 142.8 | 100.0 |
| Bench 3 | Bench | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.9 | 2.47 | 8.16 | 13.68 | 1.00 | 61.4 | 26.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 8.36 | 24.51 | 40.58 | 6.00 | 90.0 | 84.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 5.31 | 15.15 | 25.85 | 4.00 | 66.5 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.6 | 4.86 | 14.88 | 25.47 | 2.00 | 90.0 | 81.0 |
| Vice Captain | XI | Jacob Murphy | MID | 15 | 5.2 | 8.62 | 13.37 | 19.90 | 19.00 | 153.5 | 138.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 4.78 | 12.57 | 20.05 | 6.00 | 87.5 | 84.0 |

## GW33

- Train rows: 156471
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Joško Gvardiol
- Vice captain: David Raya Martin
- Effective captain: Joško Gvardiol
- Chip used: bench_boost
- Predicted score: 89.02
- Actual score: 57.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (14.62) beats the best remaining Bench Boost opportunity (9.09).
- Chip advisory: bench_boost (0.56): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (14.62) beats the best remaining Bench Boost opportunity (9.09).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Vice Captain | XI | David Raya Martin | GK | 1 | 5.5 | 8.71 | 13.49 | 20.87 | 7.00 | 180.0 | 180.0 |
| Bench 1 | Bench Boost | Matt Turner | GK | 7 | 3.9 | 0.85 | 2.69 | 3.87 | 0.00 | 23.2 | 0.0 |
| Captain | Captain | Joško Gvardiol | DEF | 13 | 6.2 | 8.88 | 14.43 | 22.33 | 7.00 | 180.0 | 180.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 8.12 | 13.27 | 20.27 | 6.00 | 180.0 | 180.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.40 | 10.64 | 16.94 | 0.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Neco Williams | DEF | 16 | 4.5 | 2.96 | 8.53 | 14.12 | 2.00 | 85.1 | 90.0 |
| Bench 3 | Bench Boost | Dara O'Shea | DEF | 10 | 3.9 | 2.21 | 7.11 | 11.77 | 0.00 | 87.5 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.75 | 16.68 | 27.70 | 2.00 | 90.0 | 75.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 7.78 | 13.24 | 20.26 | 10.00 | 146.1 | 84.0 |
| Bench 4 | Bench Boost | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 1.91 | 6.26 | 10.52 | 1.00 | 47.8 | 27.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 8.40 | 23.42 | 38.78 | 3.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 8.63 | 14.51 | 22.32 | 7.00 | 179.2 | 166.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.54 | 14.07 | 23.65 | 1.00 | 84.4 | 31.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 4.67 | 14.05 | 24.06 | 2.00 | 72.0 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 3.35 | 10.96 | 18.12 | 2.00 | 71.1 | 64.0 |

## GW34

- Train rows: 157270
- Bank: 0.10 -> 0.90
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 56.79
- Actual score: 59.00
- Transfer: Jean-Philippe Mateta -> Matheus Santos Carneiro Da Cunha (projected gain 2.72, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martin | GK | 1 | 5.5 | 0.00 | 12.20 | 19.75 | 0.00 | 0.0 | 0.0 |
| Bench 1 | Bench | Matt Turner | GK | 7 | 3.9 | 0.00 | 0.00 | 0.42 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Joško Gvardiol | DEF | 13 | 6.2 | 0.00 | 12.75 | 20.98 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 0.00 | 12.71 | 20.92 | 0.00 | 0.0 | 0.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.75 | 10.07 | 16.29 | 6.00 | 85.2 | 90.0 |
| XI | XI | Neco Williams | DEF | 16 | 4.5 | 2.87 | 8.27 | 13.82 | 0.00 | 84.7 | 90.0 |
| XI | XI | Dara O'Shea | DEF | 10 | 3.9 | 2.04 | 6.63 | 11.15 | 1.00 | 84.4 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 7.58 | 20.04 | 32.08 | 6.00 | 90.0 | 76.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.0 | 5.45 | 14.17 | 21.17 | 15.00 | 87.3 | 88.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 1.74 | 5.80 | 9.93 | 2.00 | 48.1 | 63.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.93 | 23.94 | 38.79 | 8.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 5.92 | 16.83 | 27.31 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.52 | 14.05 | 23.61 | 4.00 | 77.8 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 5.05 | 13.45 | 22.00 | 6.00 | 77.8 | 66.0 |
| Bench 4 | Bench | Morgan Rogers | MID | 2 | 5.6 | 0.00 | 12.64 | 20.55 | 0.00 | 0.0 | 0.0 |

## GW35

- Train rows: 158070
- Bank: 0.90 -> 1.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 54.41
- Actual score: 56.00
- Transfer: Matheus Santos Carneiro Da Cunha -> Yoane Wissa (projected gain 6.78, hit 0)
- Autosub: Norberto Bercique Gomes Betuncal replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 2.71 | 7.93 | 13.77 | 1.00 | 61.1 | 90.0 |
| Bench 1 | Bench | Matt Turner | GK | 7 | 3.9 | 0.00 | 0.08 | 0.34 | 0.00 | 0.0 | 0.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.57 | 9.66 | 15.58 | 2.00 | 83.3 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 3.20 | 9.57 | 16.51 | 8.00 | 70.3 | 90.0 |
| XI | XI | Neco Williams | DEF | 16 | 4.5 | 2.90 | 8.41 | 13.77 | 5.00 | 84.0 | 90.0 |
| Bench 3 | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 2.36 | 7.34 | 12.88 | 1.00 | 62.7 | 90.0 |
| Bench 4 | Bench | Dara O'Shea | DEF | 10 | 3.9 | 2.04 | 6.26 | 10.56 | 1.00 | 81.7 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 6.32 | 17.30 | 27.68 | 9.00 | 79.6 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.6 | 4.60 | 13.12 | 21.24 | 7.00 | 85.9 | 90.0 |
| Bench 2 | Autosub In | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 2.39 | 6.39 | 10.63 | 6.00 | 53.3 | 76.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.58 | 22.28 | 36.52 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.54 | 13.65 | 22.85 | 0.00 | 79.5 | 0.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.5 | 4.29 | 13.23 | 22.19 | 10.00 | 72.5 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 4.14 | 11.84 | 19.74 | 1.00 | 62.9 | 55.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 2.99 | 9.05 | 15.77 | 3.00 | 51.8 | 90.0 |