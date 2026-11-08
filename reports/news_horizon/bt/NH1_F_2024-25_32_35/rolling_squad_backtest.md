# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 296.00
- Total actual points: 261.00
- Average predicted points: 74.00
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
- Predicted score: 96.06
- Actual score: 82.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (14.68) beats the best remaining Triple Captain opportunity (15.65).
- Chip advisory: triple_captain (0.69): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Alexander Isak. Optimizer chose Triple Captain here because the current estimated captain upside (14.68) beats the best remaining Triple Captain opportunity (15.65).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.88 | 11.18 | 17.92 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.60 | 1.35 | 2.20 | 0.00 | 11.5 | 0.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 7.45 | 12.58 | 19.33 | -1.00 | 164.2 | 180.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.16 | 12.29 | 19.68 | 1.00 | 90.0 | 90.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 6.77 | 10.98 | 16.53 | 8.00 | 153.9 | 180.0 |
| Bench 2 | Bench | Neco Williams | DEF | 16 | 4.5 | 3.18 | 9.20 | 14.90 | 2.00 | 86.7 | 90.0 |
| Bench 4 | Bench | Dara O'Shea | DEF | 10 | 3.9 | 2.30 | 7.28 | 11.92 | 1.00 | 89.4 | 90.0 |
| Captain | Captain | Alexander Isak | FWD | 15 | 9.5 | 11.15 | 17.10 | 27.00 | 11.00 | 150.5 | 148.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 8.22 | 13.87 | 21.36 | 2.00 | 144.6 | 100.0 |
| Bench 3 | Bench | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.9 | 2.48 | 8.09 | 13.51 | 1.00 | 61.7 | 26.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 8.38 | 24.44 | 40.49 | 6.00 | 90.0 | 84.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 5.30 | 14.96 | 25.54 | 4.00 | 66.6 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.6 | 4.85 | 14.75 | 25.23 | 2.00 | 90.0 | 81.0 |
| Vice Captain | XI | Jacob Murphy | MID | 15 | 5.2 | 8.77 | 13.59 | 20.33 | 19.00 | 155.7 | 138.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 4.82 | 12.60 | 20.10 | 6.00 | 88.2 | 84.0 |

## GW33

- Train rows: 156471
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Joško Gvardiol
- Vice captain: David Raya Martin
- Effective captain: Joško Gvardiol
- Chip used: bench_boost
- Predicted score: 88.54
- Actual score: 64.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.67) beats the best remaining Bench Boost opportunity (8.99).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.67) beats the best remaining Bench Boost opportunity (8.99).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Vice Captain | XI | David Raya Martin | GK | 1 | 5.5 | 8.77 | 13.54 | 20.95 | 7.00 | 180.0 | 180.0 |
| Bench 1 | Bench Boost | Daniel Bentley | GK | 20 | 3.9 | 0.32 | 1.06 | 1.83 | 7.00 | 9.1 | 90.0 |
| Captain | Captain | Joško Gvardiol | DEF | 13 | 6.2 | 8.96 | 14.49 | 22.43 | 7.00 | 180.0 | 180.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 8.09 | 13.27 | 20.36 | 6.00 | 180.0 | 180.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.37 | 10.56 | 16.84 | 0.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Neco Williams | DEF | 16 | 4.5 | 2.97 | 8.52 | 14.08 | 2.00 | 85.5 | 90.0 |
| Bench 3 | Bench Boost | Dara O'Shea | DEF | 10 | 3.9 | 2.22 | 7.09 | 11.70 | 0.00 | 87.8 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.69 | 16.53 | 27.57 | 2.00 | 89.4 | 75.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 7.73 | 13.10 | 20.06 | 10.00 | 145.4 | 84.0 |
| Bench 4 | Bench Boost | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 1.90 | 6.16 | 10.30 | 1.00 | 47.9 | 27.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 8.38 | 23.28 | 38.60 | 3.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 8.73 | 14.63 | 22.54 | 7.00 | 180.0 | 166.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.54 | 13.94 | 23.39 | 1.00 | 84.6 | 31.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 4.61 | 13.76 | 23.56 | 2.00 | 71.4 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 3.29 | 10.77 | 17.89 | 2.00 | 70.1 | 64.0 |

## GW34

- Train rows: 157270
- Bank: 0.10 -> 0.90
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 57.25
- Actual score: 59.00
- Transfer: Jean-Philippe Mateta -> Matheus Santos Carneiro Da Cunha (projected gain 3.33, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.5 | 0.00 | 12.12 | 19.64 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Daniel Bentley | GK | 20 | 3.9 | 1.66 | 3.89 | 5.94 | 0.00 | 38.7 | 0.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 0.00 | 12.69 | 20.95 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Joško Gvardiol | DEF | 13 | 6.2 | 0.00 | 12.65 | 20.84 | 0.00 | 0.0 | 0.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.74 | 10.02 | 16.20 | 6.00 | 85.1 | 90.0 |
| XI | XI | Neco Williams | DEF | 16 | 4.5 | 2.88 | 8.27 | 13.79 | 0.00 | 85.0 | 90.0 |
| XI | XI | Dara O'Shea | DEF | 10 | 3.9 | 2.06 | 6.65 | 11.13 | 1.00 | 84.9 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 7.09 | 19.16 | 30.53 | 6.00 | 90.0 | 76.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.0 | 5.59 | 14.70 | 22.12 | 15.00 | 89.4 | 88.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 1.74 | 5.73 | 9.76 | 2.00 | 48.2 | 63.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.44 | 22.99 | 37.13 | 8.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 5.99 | 16.94 | 27.41 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.54 | 14.02 | 23.49 | 4.00 | 78.3 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 5.07 | 13.47 | 22.07 | 6.00 | 78.1 | 66.0 |
| Bench 4 | Bench | Morgan Rogers | MID | 2 | 5.6 | 0.00 | 12.58 | 20.52 | 0.00 | 0.0 | 0.0 |

## GW35

- Train rows: 158070
- Bank: 0.90 -> 1.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 54.16
- Actual score: 56.00
- Transfer: Matheus Santos Carneiro Da Cunha -> Yoane Wissa (projected gain 6.72, hit 0)
- Autosub: Norberto Bercique Gomes Betuncal replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 2.68 | 7.70 | 13.33 | 1.00 | 60.9 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.25 | 1.20 | 2.28 | 0.00 | 15.3 | 0.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.54 | 9.58 | 15.46 | 2.00 | 82.9 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 3.19 | 9.45 | 16.26 | 8.00 | 70.4 | 90.0 |
| XI | XI | Neco Williams | DEF | 16 | 4.5 | 2.90 | 8.38 | 13.69 | 5.00 | 84.1 | 90.0 |
| Bench 3 | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 2.32 | 7.12 | 12.48 | 1.00 | 62.3 | 90.0 |
| Bench 4 | Bench | Dara O'Shea | DEF | 10 | 3.9 | 2.05 | 6.25 | 10.50 | 1.00 | 82.0 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 6.27 | 17.17 | 27.57 | 9.00 | 79.0 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.6 | 4.60 | 13.06 | 21.13 | 7.00 | 86.0 | 90.0 |
| Bench 2 | Autosub In | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 2.41 | 6.39 | 10.59 | 6.00 | 53.7 | 76.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.58 | 22.24 | 36.51 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.53 | 13.57 | 22.71 | 0.00 | 79.5 | 0.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.5 | 4.24 | 12.96 | 21.72 | 10.00 | 71.8 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 4.10 | 11.69 | 19.52 | 1.00 | 62.3 | 55.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 2.95 | 8.84 | 15.42 | 3.00 | 51.2 | 90.0 |