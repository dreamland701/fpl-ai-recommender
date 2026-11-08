# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 294.07
- Total actual points: 254.00
- Average predicted points: 73.52
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
- Predicted score: 95.91
- Actual score: 82.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (14.67) beats the best remaining Triple Captain opportunity (15.61).
- Chip advisory: triple_captain (0.69): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Alexander Isak. Optimizer chose Triple Captain here because the current estimated captain upside (14.67) beats the best remaining Triple Captain opportunity (15.61).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.85 | 11.15 | 17.92 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Will Dennis | GK | 3 | 3.9 | 0.34 | 0.86 | 1.40 | 0.00 | 11.0 | 0.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 7.45 | 12.58 | 19.34 | -1.00 | 164.0 | 180.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.15 | 12.27 | 19.67 | 1.00 | 90.0 | 90.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 6.78 | 10.98 | 16.53 | 8.00 | 154.2 | 180.0 |
| Bench 2 | Bench | Neco Williams | DEF | 16 | 4.5 | 3.17 | 9.19 | 14.90 | 2.00 | 86.5 | 90.0 |
| Bench 4 | Bench | Dara O'Shea | DEF | 10 | 3.9 | 2.29 | 7.26 | 11.93 | 1.00 | 89.0 | 90.0 |
| Captain | Captain | Alexander Isak | FWD | 15 | 9.5 | 11.15 | 17.10 | 27.01 | 11.00 | 150.3 | 148.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 8.22 | 13.88 | 21.37 | 2.00 | 144.7 | 100.0 |
| Bench 3 | Bench | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.9 | 2.45 | 8.06 | 13.53 | 1.00 | 60.8 | 26.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 8.35 | 24.42 | 40.54 | 6.00 | 90.0 | 84.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 5.25 | 14.92 | 25.59 | 4.00 | 65.5 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.6 | 4.81 | 14.72 | 25.26 | 2.00 | 90.0 | 81.0 |
| Vice Captain | XI | Jacob Murphy | MID | 15 | 5.2 | 8.81 | 13.61 | 20.31 | 19.00 | 156.7 | 138.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 4.80 | 12.59 | 20.11 | 6.00 | 87.9 | 84.0 |

## GW33

- Train rows: 156471
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Joško Gvardiol
- Vice captain: David Raya Martin
- Effective captain: Joško Gvardiol
- Chip used: bench_boost
- Predicted score: 88.19
- Actual score: 57.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.40) beats the best remaining Bench Boost opportunity (8.68).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.40) beats the best remaining Bench Boost opportunity (8.68).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Vice Captain | XI | David Raya Martin | GK | 1 | 5.5 | 8.76 | 13.53 | 20.95 | 7.00 | 180.0 | 180.0 |
| Bench 1 | Bench Boost | Will Dennis | GK | 3 | 3.9 | 0.12 | 0.63 | 1.06 | 0.00 | 9.0 | 0.0 |
| Captain | Captain | Joško Gvardiol | DEF | 13 | 6.2 | 8.95 | 14.48 | 22.43 | 7.00 | 180.0 | 180.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 8.13 | 13.28 | 20.33 | 6.00 | 180.0 | 180.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.38 | 10.55 | 16.81 | 0.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Neco Williams | DEF | 16 | 4.5 | 2.96 | 8.50 | 14.08 | 2.00 | 85.1 | 90.0 |
| Bench 3 | Bench Boost | Dara O'Shea | DEF | 10 | 3.9 | 2.20 | 7.08 | 11.71 | 0.00 | 87.4 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.71 | 16.52 | 27.52 | 2.00 | 89.8 | 75.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 7.72 | 13.08 | 20.03 | 10.00 | 145.1 | 84.0 |
| Bench 4 | Bench Boost | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 1.87 | 6.12 | 10.31 | 1.00 | 47.2 | 27.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 8.36 | 23.26 | 38.62 | 3.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 8.74 | 14.63 | 22.52 | 7.00 | 180.0 | 166.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.49 | 13.90 | 23.42 | 1.00 | 83.6 | 31.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 4.56 | 13.71 | 23.59 | 2.00 | 70.3 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 3.29 | 10.75 | 17.83 | 2.00 | 70.2 | 64.0 |

## GW34

- Train rows: 157270
- Bank: 0.10 -> 0.90
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.98
- Actual score: 59.00
- Transfer: Jean-Philippe Mateta -> Matheus Santos Carneiro Da Cunha (projected gain 3.40, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.5 | 0.00 | 12.10 | 19.61 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Will Dennis | GK | 3 | 3.9 | 0.47 | 0.84 | 1.37 | 0.00 | 8.7 | 0.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 0.00 | 12.69 | 20.89 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Joško Gvardiol | DEF | 13 | 6.2 | 0.00 | 12.64 | 20.81 | 0.00 | 0.0 | 0.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.73 | 10.00 | 16.18 | 6.00 | 84.9 | 90.0 |
| XI | XI | Neco Williams | DEF | 16 | 4.5 | 2.87 | 8.25 | 13.78 | 0.00 | 84.7 | 90.0 |
| XI | XI | Dara O'Shea | DEF | 10 | 3.9 | 2.05 | 6.63 | 11.13 | 1.00 | 84.5 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 7.11 | 19.17 | 30.51 | 6.00 | 90.0 | 76.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.0 | 5.65 | 14.77 | 22.11 | 15.00 | 90.0 | 88.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 1.72 | 5.70 | 9.77 | 2.00 | 47.7 | 63.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.44 | 22.99 | 37.13 | 8.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 5.95 | 16.92 | 27.47 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.50 | 13.98 | 23.52 | 4.00 | 77.5 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 5.06 | 13.47 | 22.06 | 6.00 | 78.0 | 66.0 |
| Bench 4 | Bench | Morgan Rogers | MID | 2 | 5.6 | 0.00 | 12.57 | 20.46 | 0.00 | 0.0 | 0.0 |

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
- Transfer: Matheus Santos Carneiro Da Cunha -> Yoane Wissa (projected gain 6.72, hit 0)
- Autosub: Norberto Bercique Gomes Betuncal replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 2.64 | 7.65 | 13.33 | 1.00 | 60.0 | 90.0 |
| Bench 1 | Bench | Will Dennis | GK | 3 | 3.9 | 0.00 | 0.40 | 0.96 | 0.00 | 9.3 | 0.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.54 | 9.56 | 15.43 | 2.00 | 82.8 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 3.17 | 9.42 | 16.26 | 8.00 | 69.8 | 90.0 |
| XI | XI | Neco Williams | DEF | 16 | 4.5 | 2.89 | 8.37 | 13.70 | 5.00 | 83.8 | 90.0 |
| Bench 3 | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 2.29 | 7.07 | 12.46 | 1.00 | 61.6 | 90.0 |
| Bench 4 | Bench | Dara O'Shea | DEF | 10 | 3.9 | 2.03 | 6.23 | 10.51 | 1.00 | 81.6 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 6.29 | 17.16 | 27.52 | 9.00 | 79.4 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.6 | 4.58 | 13.04 | 21.13 | 7.00 | 85.7 | 90.0 |
| Bench 2 | Autosub In | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 2.39 | 6.37 | 10.61 | 6.00 | 53.3 | 76.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.58 | 22.23 | 36.49 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.51 | 13.55 | 22.72 | 0.00 | 79.0 | 0.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.5 | 4.20 | 12.92 | 21.73 | 10.00 | 71.0 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 4.10 | 11.68 | 19.49 | 1.00 | 62.2 | 55.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 2.93 | 8.81 | 15.40 | 3.00 | 50.7 | 90.0 |