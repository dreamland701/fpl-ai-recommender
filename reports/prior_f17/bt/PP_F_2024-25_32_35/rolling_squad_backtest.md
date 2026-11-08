# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 294.44
- Total actual points: 254.00
- Average predicted points: 73.61
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
- Predicted score: 96.32
- Actual score: 82.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (14.75) beats the best remaining Triple Captain opportunity (15.46).
- Chip advisory: triple_captain (0.69): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Alexander Isak. Optimizer chose Triple Captain here because the current estimated captain upside (14.75) beats the best remaining Triple Captain opportunity (15.46).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.91 | 11.30 | 18.20 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Cieran Slicker | GK | 10 | 3.9 | 0.16 | 0.70 | 1.22 | 0.00 | 10.8 | 0.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 7.56 | 12.69 | 19.55 | -1.00 | 168.3 | 180.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.19 | 12.35 | 19.83 | 1.00 | 90.0 | 90.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 6.77 | 10.84 | 16.20 | 8.00 | 152.8 | 180.0 |
| Bench 2 | Bench | Neco Williams | DEF | 16 | 4.5 | 3.17 | 9.04 | 14.58 | 2.00 | 85.8 | 90.0 |
| Bench 4 | Bench | Dara O'Shea | DEF | 10 | 3.9 | 2.39 | 7.65 | 12.66 | 1.00 | 90.0 | 90.0 |
| Captain | Captain | Alexander Isak | FWD | 15 | 9.5 | 11.22 | 17.11 | 27.04 | 11.00 | 152.5 | 148.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 8.34 | 13.93 | 21.44 | 2.00 | 148.4 | 100.0 |
| Bench 3 | Bench | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.9 | 2.40 | 7.81 | 13.03 | 1.00 | 58.5 | 26.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 8.24 | 23.85 | 39.44 | 6.00 | 90.0 | 84.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 5.29 | 15.10 | 25.96 | 4.00 | 66.8 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.6 | 4.83 | 14.70 | 25.21 | 2.00 | 90.0 | 81.0 |
| Vice Captain | XI | Jacob Murphy | MID | 15 | 5.2 | 8.78 | 13.37 | 19.80 | 19.00 | 154.6 | 138.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 4.74 | 12.26 | 19.50 | 6.00 | 84.9 | 84.0 |

## GW33

- Train rows: 156471
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Joško Gvardiol
- Vice captain: David Raya Martin
- Effective captain: Joško Gvardiol
- Chip used: bench_boost
- Predicted score: 88.56
- Actual score: 57.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.39) beats the best remaining Bench Boost opportunity (8.68).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.39) beats the best remaining Bench Boost opportunity (8.68).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Vice Captain | XI | David Raya Martin | GK | 1 | 5.5 | 8.90 | 13.67 | 21.17 | 7.00 | 180.0 | 180.0 |
| Bench 1 | Bench Boost | Cieran Slicker | GK | 10 | 3.9 | 0.04 | 0.52 | 0.99 | 0.00 | 9.3 | 0.0 |
| Captain | Captain | Joško Gvardiol | DEF | 13 | 6.2 | 9.02 | 14.52 | 22.47 | 7.00 | 180.0 | 180.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 8.26 | 13.47 | 20.68 | 6.00 | 180.0 | 180.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.34 | 10.31 | 16.32 | 0.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Neco Williams | DEF | 16 | 4.5 | 2.94 | 8.32 | 13.71 | 2.00 | 84.1 | 90.0 |
| Bench 3 | Bench Boost | Dara O'Shea | DEF | 10 | 3.9 | 2.31 | 7.48 | 12.46 | 0.00 | 90.0 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.72 | 16.56 | 27.61 | 2.00 | 90.0 | 75.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 7.86 | 13.23 | 20.27 | 10.00 | 148.9 | 84.0 |
| Bench 4 | Bench Boost | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 1.85 | 6.02 | 10.10 | 1.00 | 45.8 | 27.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 8.28 | 22.84 | 37.80 | 3.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 8.63 | 14.26 | 21.81 | 7.00 | 175.8 | 166.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.52 | 13.92 | 23.43 | 1.00 | 84.5 | 31.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 4.60 | 13.86 | 23.90 | 2.00 | 71.5 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 3.26 | 10.51 | 17.36 | 2.00 | 68.3 | 64.0 |

## GW34

- Train rows: 157270
- Bank: 0.10 -> 0.90
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.52
- Actual score: 59.00
- Transfer: Jean-Philippe Mateta -> Matheus Santos Carneiro Da Cunha (projected gain 3.91, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.5 | 0.00 | 12.18 | 19.81 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Cieran Slicker | GK | 10 | 3.9 | 0.02 | 0.37 | 0.77 | 0.00 | 8.7 | 0.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 0.00 | 12.70 | 21.01 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Joško Gvardiol | DEF | 13 | 6.2 | 0.00 | 12.62 | 20.85 | 0.00 | 0.0 | 0.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.70 | 9.77 | 15.72 | 6.00 | 82.8 | 90.0 |
| XI | XI | Neco Williams | DEF | 16 | 4.5 | 2.86 | 8.11 | 13.49 | 0.00 | 83.9 | 90.0 |
| XI | XI | Dara O'Shea | DEF | 10 | 3.9 | 2.15 | 7.00 | 11.82 | 1.00 | 88.5 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 7.12 | 19.20 | 30.57 | 6.00 | 90.0 | 76.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.0 | 5.72 | 14.93 | 22.39 | 15.00 | 90.0 | 88.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 1.71 | 5.64 | 9.62 | 2.00 | 46.9 | 63.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.37 | 22.58 | 36.35 | 8.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 5.96 | 16.90 | 27.43 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.53 | 14.05 | 23.61 | 4.00 | 78.8 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 5.00 | 13.12 | 21.37 | 6.00 | 75.1 | 66.0 |
| Bench 4 | Bench | Morgan Rogers | MID | 2 | 5.6 | 0.00 | 12.22 | 19.87 | 0.00 | 0.0 | 0.0 |

## GW35

- Train rows: 158070
- Bank: 0.90 -> 1.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 54.05
- Actual score: 56.00
- Transfer: Matheus Santos Carneiro Da Cunha -> Yoane Wissa (projected gain 6.98, hit 0)
- Autosub: Norberto Bercique Gomes Betuncal replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 2.72 | 7.95 | 13.91 | 1.00 | 62.6 | 90.0 |
| Bench 1 | Bench | Cieran Slicker | GK | 10 | 3.9 | 0.25 | 0.62 | 1.12 | 0.00 | 8.7 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 3.21 | 9.55 | 16.52 | 8.00 | 71.1 | 90.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.50 | 9.35 | 14.99 | 2.00 | 80.7 | 90.0 |
| XI | XI | Neco Williams | DEF | 16 | 4.5 | 2.89 | 8.28 | 13.49 | 5.00 | 83.2 | 90.0 |
| Bench 3 | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 2.35 | 7.40 | 13.13 | 1.00 | 64.1 | 90.0 |
| Bench 4 | Bench | Dara O'Shea | DEF | 10 | 3.9 | 2.14 | 6.65 | 11.30 | 1.00 | 86.0 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 6.33 | 17.35 | 27.92 | 9.00 | 80.7 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.6 | 4.64 | 13.19 | 21.39 | 7.00 | 87.5 | 90.0 |
| Bench 2 | Autosub In | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 2.38 | 6.27 | 10.40 | 6.00 | 52.4 | 76.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.52 | 21.95 | 35.97 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.56 | 13.72 | 23.02 | 0.00 | 81.1 | 0.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.5 | 4.24 | 13.06 | 22.01 | 10.00 | 72.0 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 4.05 | 11.45 | 19.05 | 1.00 | 59.8 | 55.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 2.87 | 8.60 | 15.03 | 3.00 | 47.8 | 90.0 |