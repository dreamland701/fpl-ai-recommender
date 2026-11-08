# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 294.88
- Total actual points: 254.00
- Average predicted points: 73.72
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
- Predicted score: 96.03
- Actual score: 82.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (14.41) beats the best remaining Triple Captain opportunity (15.68).
- Chip advisory: triple_captain (0.69): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Alexander Isak. Optimizer chose Triple Captain here because the current estimated captain upside (14.41) beats the best remaining Triple Captain opportunity (15.68).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.92 | 11.31 | 18.11 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | João Neves Virgínia | GK | 8 | 3.9 | 0.03 | 0.63 | 1.13 | 0.00 | 4.7 | 0.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 7.59 | 12.69 | 19.43 | -1.00 | 167.8 | 180.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.20 | 12.41 | 19.84 | 1.00 | 90.0 | 90.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 6.90 | 11.09 | 16.61 | 8.00 | 157.5 | 180.0 |
| Bench 2 | Bench | Neco Williams | DEF | 16 | 4.5 | 3.21 | 9.26 | 14.96 | 2.00 | 87.3 | 90.0 |
| Bench 4 | Bench | Dara O'Shea | DEF | 10 | 3.9 | 2.34 | 7.39 | 12.07 | 1.00 | 90.0 | 90.0 |
| Captain | Captain | Alexander Isak | FWD | 15 | 9.5 | 10.89 | 17.33 | 27.80 | 11.00 | 79.2 | 148.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 8.32 | 13.95 | 21.40 | 2.00 | 147.4 | 100.0 |
| Bench 3 | Bench | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.9 | 2.52 | 8.23 | 13.73 | 1.00 | 62.9 | 26.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 8.41 | 24.55 | 40.67 | 6.00 | 90.0 | 84.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 5.39 | 15.22 | 25.93 | 4.00 | 69.1 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.6 | 4.86 | 14.86 | 25.42 | 2.00 | 90.0 | 81.0 |
| Vice Captain | XI | Jacob Murphy | MID | 15 | 5.2 | 8.90 | 13.65 | 20.29 | 19.00 | 159.5 | 138.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 4.88 | 12.74 | 20.24 | 6.00 | 89.9 | 84.0 |

## GW33

- Train rows: 156471
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Joško Gvardiol
- Vice captain: David Raya Martin
- Effective captain: Joško Gvardiol
- Chip used: bench_boost
- Predicted score: 88.69
- Actual score: 57.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.56) beats the best remaining Bench Boost opportunity (8.92).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.56) beats the best remaining Bench Boost opportunity (8.92).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Vice Captain | XI | David Raya Martin | GK | 1 | 5.5 | 8.85 | 13.62 | 21.02 | 7.00 | 180.0 | 180.0 |
| Bench 1 | Bench Boost | João Neves Virgínia | GK | 8 | 3.9 | 0.07 | 0.49 | 1.01 | 0.00 | 3.8 | 0.0 |
| Captain | Captain | Joško Gvardiol | DEF | 13 | 6.2 | 9.05 | 14.59 | 22.54 | 7.00 | 180.0 | 180.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 8.07 | 13.22 | 20.24 | 6.00 | 180.0 | 180.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.37 | 10.59 | 16.87 | 0.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Neco Williams | DEF | 16 | 4.5 | 2.99 | 8.58 | 14.17 | 2.00 | 86.1 | 90.0 |
| Bench 3 | Bench Boost | Dara O'Shea | DEF | 10 | 3.9 | 2.25 | 7.19 | 11.83 | 0.00 | 88.7 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.71 | 16.57 | 27.59 | 2.00 | 89.9 | 75.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 7.79 | 13.22 | 20.24 | 10.00 | 146.9 | 84.0 |
| Bench 4 | Bench Boost | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 2.00 | 6.39 | 10.63 | 1.00 | 50.6 | 27.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 8.40 | 23.37 | 38.76 | 3.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 8.80 | 14.69 | 22.56 | 7.00 | 180.0 | 166.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 4.66 | 13.97 | 23.93 | 2.00 | 72.9 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.28 | 13.63 | 23.15 | 1.00 | 50.0 | 31.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 3.32 | 10.86 | 18.00 | 2.00 | 70.8 | 64.0 |

## GW34

- Train rows: 157270
- Bank: 0.10 -> 0.90
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.54
- Actual score: 59.00
- Transfer: Jean-Philippe Mateta -> Matheus Santos Carneiro Da Cunha (projected gain 3.24, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martin | GK | 1 | 5.5 | 0.00 | 11.96 | 19.51 | 0.00 | 0.0 | 0.0 |
| Bench 1 | Bench | João Neves Virgínia | GK | 8 | 3.9 | 0.00 | 0.39 | 0.86 | 0.00 | 3.1 | 0.0 |
| Bench 3 | Bench | Joško Gvardiol | DEF | 13 | 6.2 | 0.00 | 12.70 | 20.86 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 0.00 | 12.61 | 20.76 | 0.00 | 0.0 | 0.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.76 | 10.08 | 16.28 | 6.00 | 85.5 | 90.0 |
| XI | XI | Neco Williams | DEF | 16 | 4.5 | 2.63 | 7.90 | 13.39 | 0.00 | 50.4 | 90.0 |
| XI | XI | Dara O'Shea | DEF | 10 | 3.9 | 2.09 | 6.72 | 11.23 | 1.00 | 85.7 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 7.10 | 19.15 | 30.45 | 6.00 | 90.0 | 76.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.0 | 5.64 | 14.64 | 21.81 | 15.00 | 90.0 | 88.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 1.87 | 5.99 | 10.10 | 2.00 | 51.7 | 63.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.44 | 23.00 | 37.12 | 8.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 5.90 | 16.82 | 27.41 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.59 | 14.17 | 23.72 | 4.00 | 79.8 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 5.09 | 13.51 | 22.08 | 6.00 | 78.6 | 66.0 |
| Bench 4 | Bench | Morgan Rogers | MID | 2 | 5.6 | 0.00 | 12.60 | 20.45 | 0.00 | 0.0 | 0.0 |

## GW35

- Train rows: 158070
- Bank: 0.90 -> 1.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 54.62
- Actual score: 56.00
- Transfer: Matheus Santos Carneiro Da Cunha -> Yoane Wissa (projected gain 6.62, hit 0)
- Autosub: Norberto Bercique Gomes Betuncal replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 2.76 | 7.95 | 13.73 | 1.00 | 62.9 | 90.0 |
| Bench 1 | Bench | João Neves Virgínia | GK | 8 | 3.9 | 0.24 | 0.52 | 0.98 | 0.00 | 2.8 | 0.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.58 | 9.66 | 15.54 | 2.00 | 83.7 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 3.25 | 9.62 | 16.53 | 8.00 | 71.9 | 90.0 |
| XI | XI | Neco Williams | DEF | 16 | 4.5 | 2.94 | 8.48 | 13.81 | 5.00 | 85.2 | 90.0 |
| Bench 3 | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 2.35 | 7.28 | 12.75 | 1.00 | 63.3 | 90.0 |
| Bench 4 | Bench | Dara O'Shea | DEF | 10 | 3.9 | 2.09 | 6.35 | 10.62 | 1.00 | 83.1 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 6.33 | 17.26 | 27.66 | 9.00 | 80.2 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.6 | 4.64 | 13.18 | 21.29 | 7.00 | 87.0 | 90.0 |
| Bench 2 | Autosub In | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 2.52 | 6.60 | 10.84 | 6.00 | 56.7 | 76.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.59 | 22.30 | 36.57 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.47 | 13.49 | 22.75 | 0.00 | 78.1 | 0.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.5 | 4.28 | 13.15 | 22.04 | 10.00 | 73.0 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 4.16 | 11.82 | 19.68 | 1.00 | 63.8 | 55.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 3.03 | 9.06 | 15.72 | 3.00 | 53.4 | 90.0 |