# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 294.23
- Total actual points: 261.00
- Average predicted points: 73.56
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
- Predicted score: 92.56
- Actual score: 82.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (13.38) beats the best remaining Triple Captain opportunity (15.68).
- Chip advisory: triple_captain (0.63): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Alexander Isak. Optimizer chose Triple Captain here because the current estimated captain upside (13.38) beats the best remaining Triple Captain opportunity (15.68).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.92 | 11.31 | 18.09 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.46 | 1.09 | 1.83 | 0.00 | 7.1 | 0.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 7.53 | 12.64 | 19.31 | -1.00 | 166.6 | 180.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.20 | 12.40 | 19.80 | 1.00 | 90.0 | 90.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 6.83 | 11.01 | 16.48 | 8.00 | 156.3 | 180.0 |
| Bench 2 | Bench | Neco Williams | DEF | 16 | 4.5 | 3.20 | 9.26 | 14.94 | 2.00 | 87.2 | 90.0 |
| Bench 4 | Bench | Dara O'Shea | DEF | 10 | 3.9 | 2.34 | 7.39 | 12.07 | 1.00 | 90.0 | 90.0 |
| Captain | Captain | Alexander Isak | FWD | 15 | 9.5 | 9.86 | 16.61 | 27.31 | 11.00 | 131.4 | 148.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 8.21 | 13.84 | 21.20 | 2.00 | 145.5 | 100.0 |
| Bench 3 | Bench | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.9 | 2.54 | 8.26 | 13.75 | 1.00 | 63.1 | 26.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 8.40 | 24.57 | 40.60 | 6.00 | 90.0 | 84.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 5.42 | 15.31 | 25.97 | 4.00 | 69.5 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.6 | 4.89 | 14.93 | 25.48 | 2.00 | 90.0 | 81.0 |
| Vice Captain | XI | Jacob Murphy | MID | 15 | 5.2 | 8.74 | 13.46 | 19.97 | 19.00 | 156.7 | 138.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 4.85 | 12.68 | 20.11 | 6.00 | 89.3 | 84.0 |

## GW33

- Train rows: 156471
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Joško Gvardiol
- Vice captain: David Raya Martin
- Effective captain: Joško Gvardiol
- Chip used: bench_boost
- Predicted score: 88.68
- Actual score: 64.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.69) beats the best remaining Bench Boost opportunity (9.04).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.69) beats the best remaining Bench Boost opportunity (9.04).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Vice Captain | XI | David Raya Martin | GK | 1 | 5.5 | 8.78 | 13.55 | 20.90 | 7.00 | 180.0 | 180.0 |
| Bench 1 | Bench Boost | Daniel Bentley | GK | 20 | 3.9 | 0.18 | 0.78 | 1.42 | 7.00 | 4.6 | 90.0 |
| Captain | Captain | Joško Gvardiol | DEF | 13 | 6.2 | 8.97 | 14.49 | 22.38 | 7.00 | 180.0 | 180.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 8.07 | 13.23 | 20.22 | 6.00 | 180.0 | 180.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.39 | 10.63 | 16.91 | 0.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Neco Williams | DEF | 16 | 4.5 | 2.99 | 8.59 | 14.15 | 2.00 | 86.0 | 90.0 |
| Bench 3 | Bench Boost | Dara O'Shea | DEF | 10 | 3.9 | 2.25 | 7.18 | 11.81 | 0.00 | 88.7 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.75 | 16.66 | 27.65 | 2.00 | 90.0 | 75.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 7.81 | 13.26 | 20.25 | 10.00 | 147.0 | 84.0 |
| Bench 4 | Bench Boost | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 2.01 | 6.42 | 10.66 | 1.00 | 50.8 | 27.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 8.41 | 23.44 | 38.76 | 3.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 8.69 | 14.56 | 22.34 | 7.00 | 180.0 | 166.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 4.73 | 14.15 | 24.12 | 2.00 | 73.9 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.31 | 13.71 | 23.24 | 1.00 | 77.3 | 31.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 3.36 | 10.96 | 18.10 | 2.00 | 71.4 | 64.0 |

## GW34

- Train rows: 157270
- Bank: 0.10 -> 0.90
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 58.19
- Actual score: 59.00
- Transfer: Jean-Philippe Mateta -> Matheus Santos Carneiro Da Cunha (projected gain 2.83, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.5 | 0.00 | 12.00 | 19.54 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Daniel Bentley | GK | 20 | 3.9 | 1.48 | 3.51 | 5.38 | 0.00 | 33.0 | 0.0 |
| Bench 3 | Bench | Joško Gvardiol | DEF | 13 | 6.2 | 0.00 | 12.73 | 20.87 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 0.00 | 12.62 | 20.75 | 0.00 | 0.0 | 0.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.76 | 10.09 | 16.28 | 6.00 | 85.5 | 90.0 |
| XI | XI | Neco Williams | DEF | 16 | 4.5 | 2.63 | 7.90 | 13.39 | 0.00 | 77.5 | 90.0 |
| XI | XI | Dara O'Shea | DEF | 10 | 3.9 | 2.08 | 6.70 | 11.20 | 1.00 | 85.5 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 7.54 | 19.99 | 32.01 | 6.00 | 90.0 | 76.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.0 | 5.48 | 14.24 | 21.25 | 15.00 | 88.3 | 88.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 1.87 | 6.01 | 10.12 | 2.00 | 51.8 | 63.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.90 | 23.90 | 38.73 | 8.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 5.87 | 16.74 | 27.28 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.59 | 14.17 | 23.70 | 4.00 | 79.7 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 5.07 | 13.48 | 22.00 | 6.00 | 78.3 | 66.0 |
| Bench 4 | Bench | Morgan Rogers | MID | 2 | 5.6 | 0.00 | 12.62 | 20.44 | 0.00 | 0.0 | 0.0 |

## GW35

- Train rows: 158070
- Bank: 0.90 -> 1.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 54.80
- Actual score: 56.00
- Transfer: Matheus Santos Carneiro Da Cunha -> Yoane Wissa (projected gain 6.63, hit 0)
- Autosub: Norberto Bercique Gomes Betuncal replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 2.79 | 8.05 | 13.84 | 1.00 | 63.4 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.10 | 0.93 | 1.91 | 0.00 | 10.5 | 0.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.59 | 9.69 | 15.58 | 2.00 | 83.8 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 3.26 | 9.66 | 16.56 | 8.00 | 72.0 | 90.0 |
| XI | XI | Neco Williams | DEF | 16 | 4.5 | 2.95 | 8.49 | 13.81 | 5.00 | 85.3 | 90.0 |
| Bench 3 | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 2.40 | 7.40 | 12.90 | 1.00 | 63.9 | 90.0 |
| Bench 4 | Bench | Dara O'Shea | DEF | 10 | 3.9 | 2.09 | 6.35 | 10.62 | 1.00 | 83.1 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 6.33 | 17.31 | 27.66 | 9.00 | 80.1 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.6 | 4.63 | 13.18 | 21.26 | 7.00 | 86.9 | 90.0 |
| Bench 2 | Autosub In | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 2.51 | 6.58 | 10.81 | 6.00 | 56.7 | 76.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.58 | 22.29 | 36.50 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.50 | 13.55 | 22.81 | 0.00 | 78.4 | 0.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.5 | 4.34 | 13.30 | 22.22 | 10.00 | 73.8 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 4.18 | 11.90 | 19.77 | 1.00 | 64.1 | 55.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 3.07 | 9.16 | 15.84 | 3.00 | 53.9 | 90.0 |