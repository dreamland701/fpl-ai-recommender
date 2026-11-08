# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 291.87
- Total actual points: 245.00
- Average predicted points: 72.97
- Average actual points: 61.25
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
- Predicted score: 97.27
- Actual score: 83.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (14.84) beats the best remaining Triple Captain opportunity (15.75).
- Chip advisory: triple_captain (0.69): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Alexander Isak. Optimizer chose Triple Captain here because the current estimated captain upside (14.84) beats the best remaining Triple Captain opportunity (15.75).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.81 | 11.04 | 17.76 | 2.00 | 88.8 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 6 | 3.9 | 0.52 | 1.30 | 1.99 | 0.00 | 8.3 | 0.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 7.43 | 12.72 | 19.55 | -1.00 | 168.7 | 180.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.10 | 12.11 | 19.39 | 1.00 | 90.0 | 90.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 6.99 | 11.15 | 16.64 | 8.00 | 158.6 | 180.0 |
| Bench 2 | Bench | Djed Spence | DEF | 18 | 4.4 | 2.94 | 8.57 | 14.00 | -2.00 | 83.0 | 90.0 |
| Bench 4 | Bench | Dara O'Shea | DEF | 10 | 3.9 | 2.22 | 6.97 | 11.49 | 1.00 | 90.0 | 90.0 |
| Captain | Captain | Alexander Isak | FWD | 15 | 9.5 | 10.96 | 16.96 | 26.64 | 11.00 | 148.7 | 148.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 8.35 | 14.04 | 21.65 | 2.00 | 144.7 | 100.0 |
| Bench 3 | Bench | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.9 | 2.62 | 8.73 | 14.63 | 1.00 | 62.6 | 26.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 8.45 | 25.53 | 42.38 | 6.00 | 90.0 | 84.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 5.20 | 15.04 | 25.47 | 4.00 | 64.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.6 | 4.85 | 14.74 | 25.32 | 2.00 | 90.0 | 81.0 |
| Vice Captain | XI | Jacob Murphy | MID | 15 | 5.2 | 8.95 | 13.58 | 20.29 | 19.00 | 160.1 | 138.0 |
| XI | XI | Ismaïla Sarr | MID | 7 | 5.8 | 6.24 | 12.52 | 19.76 | 7.00 | 137.4 | 165.0 |

## GW33

- Train rows: 156471
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: David Raya Martin
- Vice captain: Joško Gvardiol
- Effective captain: David Raya Martin
- Chip used: bench_boost
- Predicted score: 87.43
- Actual score: 52.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.01) beats the best remaining Bench Boost opportunity (8.41).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.01) beats the best remaining Bench Boost opportunity (8.41).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Captain | Captain | David Raya Martin | GK | 1 | 5.5 | 8.75 | 13.61 | 21.03 | 7.00 | 180.0 | 180.0 |
| Bench 1 | Bench Boost | Marcus Bettinelli | GK | 6 | 3.9 | 0.33 | 1.03 | 1.71 | 0.00 | 6.6 | 0.0 |
| Vice Captain | XI | Joško Gvardiol | DEF | 13 | 6.2 | 8.75 | 14.33 | 22.23 | 7.00 | 180.0 | 180.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 8.38 | 13.62 | 20.74 | 6.00 | 180.0 | 180.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.46 | 10.46 | 16.59 | 0.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Djed Spence | DEF | 18 | 4.4 | 2.46 | 7.35 | 12.17 | 1.00 | 79.2 | 90.0 |
| Bench 3 | Bench Boost | Dara O'Shea | DEF | 10 | 3.9 | 2.11 | 6.64 | 11.01 | 0.00 | 88.7 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.56 | 15.96 | 26.69 | 2.00 | 89.2 | 75.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 7.56 | 13.02 | 19.96 | 10.00 | 142.7 | 84.0 |
| Bench 4 | Bench Boost | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 1.86 | 6.36 | 10.65 | 1.00 | 47.0 | 27.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 8.37 | 23.82 | 39.44 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.53 | 14.01 | 23.75 | 1.00 | 84.2 | 31.0 |
| XI | XI | Ismaïla Sarr | MID | 7 | 5.8 | 8.66 | 13.83 | 21.51 | 3.00 | 180.0 | 117.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 4.49 | 13.77 | 23.57 | 2.00 | 68.7 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 3.41 | 10.50 | 17.55 | 2.00 | 73.6 | 64.0 |

## GW34

- Train rows: 157270
- Bank: 0.00 -> 0.80
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 54.96
- Actual score: 59.00
- Transfer: Jean-Philippe Mateta -> Matheus Santos Carneiro Da Cunha (projected gain 4.60, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.5 | 0.00 | 12.16 | 19.64 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Marcus Bettinelli | GK | 6 | 3.9 | 0.41 | 1.03 | 1.67 | 0.00 | 5.1 | 0.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 0.00 | 12.87 | 21.18 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Joško Gvardiol | DEF | 13 | 6.2 | 0.00 | 12.43 | 20.42 | 0.00 | 0.0 | 0.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.71 | 9.76 | 15.85 | 6.00 | 86.7 | 90.0 |
| XI | XI | Djed Spence | DEF | 18 | 4.4 | 2.16 | 6.90 | 11.51 | 0.00 | 76.8 | 90.0 |
| XI | XI | Dara O'Shea | DEF | 10 | 3.9 | 1.98 | 6.31 | 10.69 | 1.00 | 86.5 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 6.98 | 18.67 | 29.60 | 6.00 | 90.0 | 76.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.0 | 5.66 | 14.67 | 21.62 | 15.00 | 89.8 | 88.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 1.68 | 5.67 | 9.67 | 2.00 | 46.5 | 63.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.40 | 23.34 | 37.63 | 8.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 5.93 | 16.72 | 26.97 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.57 | 14.21 | 24.09 | 4.00 | 77.4 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 5.08 | 13.00 | 21.33 | 6.00 | 80.0 | 66.0 |
| Bench 4 | Bench | Ismaïla Sarr | MID | 7 | 5.8 | 0.00 | 11.27 | 18.97 | 0.00 | 0.0 | 0.0 |

## GW35

- Train rows: 158070
- Bank: 0.80 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 52.21
- Actual score: 51.00
- Transfer: Matheus Santos Carneiro Da Cunha -> Yoane Wissa (projected gain 5.91, hit 0)
- Autosub: Daniel Muñoz replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 2.55 | 7.73 | 13.57 | 1.00 | 56.0 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 6 | 3.9 | 0.08 | 0.67 | 1.29 | 0.00 | 4.8 | 0.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.52 | 9.23 | 14.93 | 2.00 | 84.3 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 3.02 | 9.18 | 16.00 | 8.00 | 70.7 | 90.0 |
| Bench 2 | Autosub In | Daniel Muñoz | DEF | 7 | 5.2 | 2.25 | 7.05 | 12.63 | 1.00 | 61.8 | 90.0 |
| XI | XI | Djed Spence | DEF | 18 | 4.4 | 2.32 | 6.43 | 10.38 | 2.00 | 74.1 | 90.0 |
| Bench 4 | Bench | Dara O'Shea | DEF | 10 | 3.9 | 1.96 | 5.94 | 10.05 | 1.00 | 83.6 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 6.06 | 16.40 | 26.32 | 9.00 | 78.1 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.6 | 4.55 | 12.93 | 20.90 | 7.00 | 86.1 | 90.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 2.41 | 6.34 | 10.42 | 6.00 | 52.7 | 76.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.49 | 22.45 | 36.79 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.63 | 14.12 | 23.70 | 0.00 | 78.5 | 0.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.5 | 4.05 | 12.78 | 21.52 | 10.00 | 69.0 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 4.11 | 11.33 | 18.82 | 1.00 | 63.7 | 55.0 |
| Bench 3 | Bench | Ismaïla Sarr | MID | 7 | 5.7 | 2.15 | 6.89 | 12.39 | 2.00 | 49.4 | 90.0 |