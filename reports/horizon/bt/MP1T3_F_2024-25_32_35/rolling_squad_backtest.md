# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 293.99
- Total actual points: 254.00
- Average predicted points: 73.50
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
- Predicted score: 95.94
- Actual score: 82.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (14.67) beats the best remaining Triple Captain opportunity (15.61).
- Chip advisory: triple_captain (0.69): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Alexander Isak. Optimizer chose Triple Captain here because the current estimated captain upside (14.67) beats the best remaining Triple Captain opportunity (15.61).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.86 | 11.22 | 18.05 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Alfie Whiteman | GK | 18 | 3.9 | 0.35 | 0.99 | 1.64 | 0.00 | 12.1 | 0.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 7.45 | 12.57 | 19.33 | -1.00 | 164.0 | 180.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.16 | 12.34 | 19.81 | 1.00 | 90.0 | 90.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 6.78 | 10.98 | 16.53 | 8.00 | 154.2 | 180.0 |
| Bench 2 | Bench | Neco Williams | DEF | 16 | 4.5 | 3.18 | 9.20 | 14.94 | 2.00 | 86.6 | 90.0 |
| Bench 4 | Bench | Dara O'Shea | DEF | 10 | 3.9 | 2.29 | 7.31 | 12.02 | 1.00 | 89.1 | 90.0 |
| Captain | Captain | Alexander Isak | FWD | 15 | 9.5 | 11.15 | 17.11 | 27.03 | 11.00 | 150.3 | 148.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 8.22 | 13.86 | 21.34 | 2.00 | 144.6 | 100.0 |
| Bench 3 | Bench | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.9 | 2.45 | 8.11 | 13.63 | 1.00 | 61.0 | 26.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 8.35 | 24.47 | 40.63 | 6.00 | 90.0 | 84.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 5.26 | 15.02 | 25.78 | 4.00 | 65.7 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.6 | 4.82 | 14.78 | 25.39 | 2.00 | 90.0 | 81.0 |
| Vice Captain | XI | Jacob Murphy | MID | 15 | 5.2 | 8.80 | 13.57 | 20.23 | 19.00 | 156.5 | 138.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 4.81 | 12.62 | 20.16 | 6.00 | 87.9 | 84.0 |

## GW33

- Train rows: 156471
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Joško Gvardiol
- Vice captain: David Raya Martin
- Effective captain: Joško Gvardiol
- Chip used: bench_boost
- Predicted score: 88.42
- Actual score: 57.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.53) beats the best remaining Bench Boost opportunity (8.87).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.53) beats the best remaining Bench Boost opportunity (8.87).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Vice Captain | XI | David Raya Martin | GK | 1 | 5.5 | 8.77 | 13.55 | 20.98 | 7.00 | 180.0 | 180.0 |
| Bench 1 | Bench Boost | Alfie Whiteman | GK | 18 | 3.9 | 0.23 | 0.74 | 1.23 | 0.00 | 9.7 | 0.0 |
| Captain | Captain | Joško Gvardiol | DEF | 13 | 6.2 | 8.95 | 14.51 | 22.49 | 7.00 | 180.0 | 180.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 8.12 | 13.26 | 20.29 | 6.00 | 180.0 | 180.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.38 | 10.60 | 16.90 | 0.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Neco Williams | DEF | 16 | 4.5 | 2.96 | 8.52 | 14.12 | 2.00 | 85.2 | 90.0 |
| Bench 3 | Bench Boost | Dara O'Shea | DEF | 10 | 3.9 | 2.21 | 7.11 | 11.77 | 0.00 | 87.5 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.71 | 16.58 | 27.64 | 2.00 | 89.9 | 75.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 7.75 | 13.19 | 20.25 | 10.00 | 145.7 | 84.0 |
| Bench 4 | Bench Boost | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 1.88 | 6.20 | 10.46 | 1.00 | 47.4 | 27.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 8.37 | 23.34 | 38.76 | 3.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 8.75 | 14.65 | 22.55 | 7.00 | 180.0 | 166.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.50 | 13.97 | 23.54 | 1.00 | 83.8 | 31.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 4.58 | 13.84 | 23.83 | 2.00 | 70.6 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 3.31 | 10.84 | 18.02 | 2.00 | 70.4 | 64.0 |

## GW34

- Train rows: 157270
- Bank: 0.10 -> 0.90
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.50
- Actual score: 59.00
- Transfer: Jean-Philippe Mateta -> Matheus Santos Carneiro Da Cunha (projected gain 3.90, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martin | GK | 1 | 5.5 | 0.00 | 12.17 | 19.73 | 0.00 | 0.0 | 0.0 |
| Bench 1 | Bench | Alfie Whiteman | GK | 18 | 3.9 | 0.00 | 0.43 | 0.84 | 0.00 | 8.2 | 0.0 |
| Bench 3 | Bench | Joško Gvardiol | DEF | 13 | 6.2 | 0.00 | 12.71 | 20.95 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 0.00 | 12.71 | 20.93 | 0.00 | 0.0 | 0.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.74 | 10.05 | 16.28 | 6.00 | 85.0 | 90.0 |
| XI | XI | Neco Williams | DEF | 16 | 4.5 | 2.87 | 8.27 | 13.82 | 0.00 | 84.7 | 90.0 |
| XI | XI | Dara O'Shea | DEF | 10 | 3.9 | 2.05 | 6.65 | 11.17 | 1.00 | 84.6 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 7.11 | 19.16 | 30.49 | 6.00 | 90.0 | 76.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.0 | 5.63 | 14.59 | 21.76 | 15.00 | 90.0 | 88.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 1.73 | 5.76 | 9.88 | 2.00 | 47.8 | 63.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.44 | 22.99 | 37.14 | 8.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 5.94 | 16.91 | 27.45 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.51 | 14.03 | 23.61 | 4.00 | 77.6 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 5.07 | 13.48 | 22.08 | 6.00 | 78.0 | 66.0 |
| Bench 4 | Bench | Morgan Rogers | MID | 2 | 5.6 | 0.00 | 12.62 | 20.56 | 0.00 | 0.0 | 0.0 |

## GW35

- Train rows: 158070
- Bank: 0.90 -> 1.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 54.12
- Actual score: 56.00
- Transfer: Matheus Santos Carneiro Da Cunha -> Yoane Wissa (projected gain 13.14, hit 0)
- Autosub: Norberto Bercique Gomes Betuncal replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 2.66 | 7.80 | 13.63 | 1.00 | 60.4 | 90.0 |
| Bench 1 | Bench | Alfie Whiteman | GK | 18 | 3.9 | 0.32 | 0.64 | 1.09 | 0.00 | 7.4 | 0.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.55 | 9.62 | 15.53 | 2.00 | 83.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 3.18 | 9.52 | 16.47 | 8.00 | 70.1 | 90.0 |
| XI | XI | Neco Williams | DEF | 16 | 4.5 | 2.89 | 8.40 | 13.75 | 5.00 | 83.9 | 90.0 |
| Bench 3 | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 2.30 | 7.21 | 12.71 | 1.00 | 62.0 | 90.0 |
| Bench 4 | Bench | Dara O'Shea | DEF | 10 | 3.9 | 2.03 | 6.26 | 10.56 | 1.00 | 81.7 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 6.30 | 17.24 | 27.68 | 9.00 | 79.6 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.6 | 4.59 | 13.10 | 21.25 | 7.00 | 85.8 | 90.0 |
| Bench 2 | Autosub In | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 2.39 | 6.39 | 10.64 | 6.00 | 53.3 | 76.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.58 | 22.28 | 36.59 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.51 | 13.59 | 22.80 | 0.00 | 79.1 | 0.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.5 | 4.22 | 13.05 | 21.98 | 10.00 | 71.3 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 4.11 | 11.75 | 19.64 | 1.00 | 62.4 | 55.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 2.95 | 8.93 | 15.63 | 3.00 | 51.0 | 90.0 |