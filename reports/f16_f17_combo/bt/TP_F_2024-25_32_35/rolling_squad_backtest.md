# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 297.51
- Total actual points: 254.00
- Average predicted points: 74.38
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
- Predicted score: 96.47
- Actual score: 82.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (14.49) beats the best remaining Triple Captain opportunity (15.53).
- Chip advisory: triple_captain (0.69): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Alexander Isak. Optimizer chose Triple Captain here because the current estimated captain upside (14.49) beats the best remaining Triple Captain opportunity (15.53).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.98 | 11.43 | 18.30 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 12 | 4.0 | 1.75 | 4.66 | 7.00 | 0.00 | 45.2 | 0.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 7.72 | 12.84 | 19.69 | -1.00 | 172.6 | 180.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.24 | 12.44 | 19.88 | 1.00 | 90.0 | 90.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 6.90 | 10.94 | 16.29 | 8.00 | 156.3 | 180.0 |
| Bench 2 | Bench | Neco Williams | DEF | 16 | 4.5 | 3.20 | 9.09 | 14.61 | 2.00 | 86.6 | 90.0 |
| Bench 4 | Bench | Dara O'Shea | DEF | 10 | 3.9 | 2.45 | 7.76 | 12.76 | 1.00 | 90.0 | 90.0 |
| Captain | Captain | Alexander Isak | FWD | 15 | 9.5 | 10.96 | 17.32 | 27.76 | 11.00 | 145.9 | 148.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 8.46 | 14.05 | 21.53 | 2.00 | 151.7 | 100.0 |
| Bench 3 | Bench | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.9 | 2.47 | 7.92 | 13.13 | 1.00 | 60.3 | 26.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 8.29 | 23.94 | 39.50 | 6.00 | 90.0 | 84.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 5.43 | 15.34 | 26.16 | 4.00 | 70.6 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.6 | 4.88 | 14.80 | 25.27 | 2.00 | 90.0 | 81.0 |
| Vice Captain | XI | Jacob Murphy | MID | 15 | 5.2 | 8.88 | 13.45 | 19.86 | 19.00 | 157.6 | 138.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 4.81 | 12.38 | 19.58 | 6.00 | 86.8 | 84.0 |

## GW33

- Train rows: 156471
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Joško Gvardiol
- Vice captain: David Raya Martin
- Effective captain: Joško Gvardiol
- Chip used: bench_boost
- Predicted score: 90.12
- Actual score: 57.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (14.62) beats the best remaining Bench Boost opportunity (10.06).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (14.62) beats the best remaining Bench Boost opportunity (10.06).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Vice Captain | XI | David Raya Martin | GK | 1 | 5.5 | 9.01 | 13.77 | 21.25 | 7.00 | 180.0 | 180.0 |
| Bench 1 | Bench Boost | Caoimhin Kelleher | GK | 12 | 4.0 | 1.05 | 2.75 | 4.36 | 0.00 | 22.4 | 0.0 |
| Captain | Captain | Joško Gvardiol | DEF | 13 | 6.2 | 9.14 | 14.61 | 22.55 | 7.00 | 180.0 | 180.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 8.23 | 13.46 | 20.66 | 6.00 | 180.0 | 180.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.33 | 10.29 | 16.27 | 0.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Neco Williams | DEF | 16 | 4.5 | 2.98 | 8.39 | 13.76 | 2.00 | 85.0 | 90.0 |
| Bench 3 | Bench Boost | Dara O'Shea | DEF | 10 | 3.9 | 2.37 | 7.59 | 12.56 | 0.00 | 90.0 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.73 | 16.56 | 27.58 | 2.00 | 90.0 | 75.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 7.93 | 13.28 | 20.28 | 10.00 | 150.6 | 84.0 |
| Bench 4 | Bench Boost | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 1.97 | 6.21 | 10.28 | 1.00 | 49.1 | 27.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 8.31 | 22.88 | 37.80 | 3.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 8.67 | 14.30 | 21.82 | 7.00 | 177.0 | 166.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 4.70 | 14.03 | 24.04 | 2.00 | 74.1 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.31 | 13.60 | 23.05 | 1.00 | 77.7 | 31.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 3.27 | 10.52 | 17.32 | 2.00 | 68.5 | 64.0 |

## GW34

- Train rows: 157270
- Bank: 0.00 -> 0.80
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 56.23
- Actual score: 59.00
- Transfer: Jean-Philippe Mateta -> Matheus Santos Carneiro Da Cunha (projected gain 4.03, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.5 | 0.00 | 11.99 | 19.61 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Caoimhin Kelleher | GK | 12 | 4.0 | 0.65 | 1.84 | 3.11 | 0.00 | 16.2 | 0.0 |
| Bench 3 | Bench | Joško Gvardiol | DEF | 13 | 6.2 | 0.00 | 12.62 | 20.76 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 0.00 | 12.60 | 20.84 | 0.00 | 0.0 | 0.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.71 | 9.79 | 15.72 | 6.00 | 83.2 | 90.0 |
| XI | XI | Neco Williams | DEF | 16 | 4.5 | 2.62 | 7.73 | 13.05 | 0.00 | 76.5 | 90.0 |
| XI | XI | Dara O'Shea | DEF | 10 | 3.9 | 2.21 | 7.11 | 11.93 | 1.00 | 90.0 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 7.12 | 19.19 | 30.54 | 6.00 | 90.0 | 76.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.0 | 5.76 | 15.00 | 22.47 | 15.00 | 90.0 | 88.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 1.86 | 5.88 | 9.86 | 2.00 | 50.8 | 63.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.37 | 22.59 | 36.33 | 8.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 5.92 | 16.83 | 27.41 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.63 | 14.22 | 23.76 | 4.00 | 81.2 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 5.02 | 13.14 | 21.35 | 6.00 | 75.5 | 66.0 |
| Bench 4 | Bench | Morgan Rogers | MID | 2 | 5.6 | 0.00 | 12.17 | 19.73 | 0.00 | 0.0 | 0.0 |

## GW35

- Train rows: 158070
- Bank: 0.80 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 54.69
- Actual score: 56.00
- Transfer: Matheus Santos Carneiro Da Cunha -> Yoane Wissa (projected gain 6.83, hit 0)
- Autosub: Norberto Bercique Gomes Betuncal replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 2.83 | 8.14 | 14.06 | 1.00 | 65.5 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 12 | 4.0 | 0.21 | 1.24 | 2.53 | 0.00 | 12.4 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 3.29 | 9.68 | 16.62 | 8.00 | 73.1 | 90.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.53 | 9.38 | 14.99 | 2.00 | 81.3 | 90.0 |
| XI | XI | Neco Williams | DEF | 16 | 4.5 | 2.94 | 8.37 | 13.55 | 5.00 | 84.6 | 90.0 |
| Bench 3 | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 2.41 | 7.51 | 13.20 | 1.00 | 65.7 | 90.0 |
| Bench 4 | Bench | Dara O'Shea | DEF | 10 | 3.9 | 2.21 | 6.78 | 11.42 | 1.00 | 87.9 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 6.35 | 17.38 | 27.91 | 9.00 | 81.5 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.6 | 4.70 | 13.30 | 21.46 | 7.00 | 89.0 | 90.0 |
| Bench 2 | Autosub In | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 2.51 | 6.50 | 10.62 | 6.00 | 55.9 | 76.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.53 | 21.97 | 35.96 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.64 | 13.85 | 23.13 | 0.00 | 83.0 | 0.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.5 | 4.31 | 13.19 | 22.11 | 10.00 | 74.0 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 4.09 | 11.52 | 19.08 | 1.00 | 61.0 | 55.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 2.95 | 8.73 | 15.13 | 3.00 | 50.0 | 90.0 |