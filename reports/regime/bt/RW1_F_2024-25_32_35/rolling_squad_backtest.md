# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 294.75
- Total actual points: 241.00
- Average predicted points: 73.69
- Average actual points: 60.25
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
- Predicted score: 99.15
- Actual score: 83.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (15.14) beats the best remaining Triple Captain opportunity (15.82).
- Chip advisory: triple_captain (0.69): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Alexander Isak. Optimizer chose Triple Captain here because the current estimated captain upside (15.14) beats the best remaining Triple Captain opportunity (15.82).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.73 | 10.83 | 17.51 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.54 | 1.06 | 1.53 | 0.00 | 10.2 | 0.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 7.50 | 13.05 | 20.01 | -1.00 | 168.2 | 180.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.12 | 12.13 | 19.36 | 1.00 | 90.0 | 90.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 7.11 | 11.25 | 16.59 | 8.00 | 160.9 | 180.0 |
| Bench 2 | Bench | Djed Spence | DEF | 18 | 4.4 | 2.97 | 8.63 | 14.18 | -2.00 | 81.9 | 90.0 |
| Bench 4 | Bench | Dara O'Shea | DEF | 10 | 3.9 | 2.26 | 6.97 | 11.51 | 1.00 | 88.7 | 90.0 |
| Captain | Captain | Alexander Isak | FWD | 15 | 9.5 | 11.26 | 17.48 | 27.41 | 11.00 | 148.0 | 148.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 8.60 | 14.53 | 22.50 | 2.00 | 145.4 | 100.0 |
| Bench 3 | Bench | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.9 | 2.81 | 9.41 | 15.84 | 1.00 | 64.3 | 26.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 8.51 | 26.02 | 43.26 | 6.00 | 90.0 | 84.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 5.17 | 14.96 | 25.03 | 4.00 | 62.6 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.6 | 4.91 | 14.82 | 25.45 | 2.00 | 90.0 | 81.0 |
| Vice Captain | XI | Jacob Murphy | MID | 15 | 5.2 | 9.25 | 13.87 | 20.71 | 19.00 | 163.0 | 138.0 |
| XI | XI | Ismaïla Sarr | MID | 7 | 5.8 | 6.47 | 12.99 | 20.36 | 7.00 | 142.1 | 165.0 |

## GW33

- Train rows: 156471
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Ismaïla Sarr
- Vice captain: Joško Gvardiol
- Effective captain: Ismaïla Sarr
- Chip used: bench_boost
- Predicted score: 88.63
- Actual score: 48.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (12.98) beats the best remaining Bench Boost opportunity (8.42).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (12.98) beats the best remaining Bench Boost opportunity (8.42).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 8.62 | 13.58 | 20.99 | 7.00 | 180.0 | 180.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.26 | 0.71 | 1.20 | 0.00 | 8.8 | 0.0 |
| Vice Captain | XI | Joško Gvardiol | DEF | 13 | 6.2 | 8.75 | 14.44 | 22.43 | 7.00 | 180.0 | 180.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 8.65 | 14.02 | 21.33 | 6.00 | 180.0 | 180.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.50 | 10.35 | 16.40 | 0.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Djed Spence | DEF | 18 | 4.4 | 2.46 | 7.34 | 12.20 | 1.00 | 78.2 | 90.0 |
| Bench 3 | Bench Boost | Dara O'Shea | DEF | 10 | 3.9 | 2.11 | 6.55 | 10.82 | 0.00 | 87.0 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.61 | 15.98 | 26.83 | 2.00 | 89.3 | 75.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 7.63 | 13.26 | 20.33 | 10.00 | 141.0 | 84.0 |
| Bench 4 | Bench Boost | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 1.90 | 6.72 | 11.33 | 1.00 | 48.0 | 27.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 8.39 | 24.00 | 39.64 | 3.00 | 90.0 | 90.0 |
| Captain | Captain | Ismaïla Sarr | MID | 7 | 5.8 | 9.05 | 14.26 | 22.10 | 3.00 | 180.0 | 117.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.58 | 14.11 | 23.94 | 1.00 | 83.9 | 31.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 4.47 | 13.68 | 23.24 | 2.00 | 67.4 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 3.61 | 10.62 | 17.83 | 2.00 | 76.4 | 64.0 |

## GW34

- Train rows: 157270
- Bank: 0.00 -> 0.80
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.00
- Actual score: 59.00
- Transfer: Jean-Philippe Mateta -> Matheus Santos Carneiro Da Cunha (projected gain 4.54, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.5 | 0.00 | 12.13 | 19.61 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Killian Cahill | GK | 5 | 3.9 | 0.41 | 0.74 | 1.09 | 0.00 | 7.5 | 0.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 0.00 | 13.23 | 21.84 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Joško Gvardiol | DEF | 13 | 6.2 | 0.00 | 12.67 | 20.71 | 0.00 | 0.0 | 0.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.67 | 9.49 | 15.49 | 6.00 | 87.0 | 90.0 |
| XI | XI | Djed Spence | DEF | 18 | 4.4 | 2.18 | 6.88 | 11.54 | 0.00 | 76.0 | 90.0 |
| XI | XI | Dara O'Shea | DEF | 10 | 3.9 | 2.02 | 6.35 | 10.80 | 1.00 | 85.2 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 6.96 | 18.67 | 29.66 | 6.00 | 90.0 | 76.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.0 | 5.70 | 14.94 | 21.84 | 15.00 | 90.0 | 88.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 1.74 | 6.01 | 10.24 | 2.00 | 47.2 | 63.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.35 | 23.36 | 37.70 | 8.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 5.91 | 16.63 | 26.70 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.55 | 14.08 | 24.05 | 4.00 | 76.7 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 5.14 | 12.86 | 21.25 | 6.00 | 80.6 | 66.0 |
| Bench 4 | Bench | Ismaïla Sarr | MID | 7 | 5.8 | 0.00 | 11.59 | 19.73 | 0.00 | 0.0 | 0.0 |

## GW35

- Train rows: 158070
- Bank: 0.80 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 51.97
- Actual score: 51.00
- Transfer: Matheus Santos Carneiro Da Cunha -> Yoane Wissa (projected gain 6.21, hit 0)
- Autosub: Daniel Muñoz replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 2.38 | 7.40 | 13.24 | 1.00 | 57.1 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.08 | 0.39 | 0.64 | 0.00 | 7.3 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 2.98 | 9.18 | 16.11 | 8.00 | 68.1 | 90.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.52 | 9.04 | 14.57 | 2.00 | 84.9 | 90.0 |
| Bench 2 | Autosub In | Daniel Muñoz | DEF | 7 | 5.2 | 2.26 | 7.07 | 12.83 | 1.00 | 58.8 | 90.0 |
| XI | XI | Djed Spence | DEF | 18 | 4.4 | 2.38 | 6.58 | 10.54 | 2.00 | 73.9 | 90.0 |
| Bench 4 | Bench | Dara O'Shea | DEF | 10 | 3.9 | 2.01 | 6.04 | 10.18 | 1.00 | 82.2 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 5.94 | 16.05 | 25.84 | 9.00 | 77.4 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.6 | 4.66 | 13.25 | 21.41 | 7.00 | 86.6 | 90.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 2.52 | 6.74 | 11.01 | 6.00 | 54.4 | 76.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.42 | 22.36 | 36.57 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.61 | 14.12 | 23.70 | 0.00 | 78.2 | 0.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.5 | 3.94 | 12.56 | 21.12 | 10.00 | 67.3 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 4.18 | 11.34 | 18.69 | 1.00 | 64.9 | 55.0 |
| Bench 3 | Bench | Ismaïla Sarr | MID | 7 | 5.7 | 2.19 | 7.05 | 12.89 | 2.00 | 47.6 | 90.0 |