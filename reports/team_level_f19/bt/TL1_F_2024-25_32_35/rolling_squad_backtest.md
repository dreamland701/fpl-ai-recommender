# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 296.73
- Total actual points: 265.00
- Average predicted points: 74.18
- Average actual points: 66.25
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
- Predicted score: 96.85
- Actual score: 82.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (14.72) beats the best remaining Triple Captain opportunity (15.53).
- Chip advisory: triple_captain (0.69): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Alexander Isak. Optimizer chose Triple Captain here because the current estimated captain upside (14.72) beats the best remaining Triple Captain opportunity (15.53).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.85 | 11.26 | 18.13 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.77 | 1.31 | 1.85 | 0.00 | 11.2 | 0.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 7.69 | 12.70 | 19.52 | -1.00 | 164.8 | 180.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.19 | 12.46 | 20.05 | 1.00 | 90.0 | 90.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 6.81 | 11.02 | 16.63 | 8.00 | 154.9 | 180.0 |
| Bench 2 | Bench | Toti António Gomes | DEF | 20 | 4.3 | 3.11 | 8.51 | 13.87 | 0.00 | 82.5 | 90.0 |
| Bench 3 | Bench | Noussair Mazraoui | DEF | 14 | 4.2 | 2.74 | 8.10 | 13.12 | 0.00 | 80.5 | 77.0 |
| Captain | Captain | Alexander Isak | FWD | 15 | 9.5 | 11.20 | 17.16 | 27.15 | 11.00 | 151.6 | 148.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 8.48 | 14.01 | 21.56 | 2.00 | 145.9 | 100.0 |
| Bench 4 | Bench | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.9 | 2.47 | 8.28 | 13.87 | 1.00 | 61.7 | 26.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 8.30 | 24.28 | 40.41 | 6.00 | 90.0 | 84.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 5.34 | 15.16 | 25.87 | 4.00 | 66.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.6 | 4.86 | 14.90 | 25.56 | 2.00 | 90.0 | 81.0 |
| Vice Captain | XI | Jacob Murphy | MID | 15 | 5.2 | 8.82 | 13.59 | 20.32 | 19.00 | 157.0 | 138.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 4.92 | 12.79 | 20.40 | 6.00 | 87.7 | 84.0 |

## GW33

- Train rows: 156471
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Joško Gvardiol
- Vice captain: David Raya Martin
- Effective captain: Joško Gvardiol
- Chip used: bench_boost
- Predicted score: 89.26
- Actual score: 66.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.56) beats the best remaining Bench Boost opportunity (8.66).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.56) beats the best remaining Bench Boost opportunity (8.66).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Vice Captain | XI | David Raya Martin | GK | 1 | 5.5 | 8.98 | 13.69 | 21.11 | 7.00 | 180.0 | 180.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.30 | 0.85 | 1.39 | 0.00 | 10.3 | 0.0 |
| Captain | Captain | Joško Gvardiol | DEF | 13 | 6.2 | 9.02 | 14.69 | 22.76 | 7.00 | 180.0 | 180.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 8.16 | 13.47 | 20.57 | 6.00 | 180.0 | 180.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.41 | 10.62 | 16.97 | 0.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Toti António Gomes | DEF | 20 | 4.3 | 2.58 | 7.68 | 12.65 | 9.00 | 79.6 | 90.0 |
| Bench 3 | Bench Boost | Noussair Mazraoui | DEF | 14 | 4.2 | 2.46 | 7.34 | 12.05 | 2.00 | 74.4 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.74 | 16.59 | 27.70 | 2.00 | 90.0 | 75.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 7.84 | 13.44 | 20.56 | 10.00 | 147.6 | 84.0 |
| Bench 4 | Bench Boost | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 1.97 | 6.25 | 10.60 | 1.00 | 47.6 | 27.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 8.42 | 23.30 | 38.60 | 3.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 8.92 | 14.85 | 22.86 | 7.00 | 180.0 | 166.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.51 | 14.02 | 23.71 | 1.00 | 84.2 | 31.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 4.57 | 13.86 | 23.86 | 2.00 | 71.2 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 3.34 | 10.86 | 18.10 | 2.00 | 70.5 | 64.0 |

## GW34

- Train rows: 157270
- Bank: 0.00 -> 0.80
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 57.04
- Actual score: 65.00
- Transfer: Jean-Philippe Mateta -> Matheus Santos Carneiro Da Cunha (projected gain 3.23, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.5 | 0.00 | 12.29 | 19.91 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Killian Cahill | GK | 5 | 3.9 | 0.44 | 0.74 | 1.22 | 0.00 | 8.6 | 0.0 |
| Bench 3 | Bench | Joško Gvardiol | DEF | 13 | 6.2 | 0.00 | 12.92 | 21.28 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 0.00 | 12.90 | 21.24 | 0.00 | 0.0 | 0.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.85 | 10.23 | 16.44 | 6.00 | 85.0 | 90.0 |
| XI | XI | Toti António Gomes | DEF | 20 | 4.3 | 3.14 | 7.99 | 12.96 | 5.00 | 76.6 | 90.0 |
| XI | XI | Noussair Mazraoui | DEF | 14 | 4.2 | 2.41 | 7.35 | 12.09 | 2.00 | 77.1 | 74.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 7.21 | 19.36 | 30.66 | 6.00 | 90.0 | 76.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.0 | 5.78 | 14.86 | 22.11 | 15.00 | 90.0 | 88.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 1.77 | 5.91 | 10.09 | 2.00 | 48.3 | 63.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.41 | 22.92 | 37.01 | 8.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 5.93 | 16.89 | 27.45 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.54 | 14.25 | 23.89 | 4.00 | 78.1 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 5.16 | 13.67 | 22.23 | 6.00 | 77.8 | 66.0 |
| Bench 4 | Bench | Morgan Rogers | MID | 2 | 5.6 | 0.00 | 12.82 | 20.86 | 0.00 | 0.0 | 0.0 |

## GW35

- Train rows: 158070
- Bank: 0.80 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 53.58
- Actual score: 52.00
- Transfer: Matheus Santos Carneiro Da Cunha -> Yoane Wissa (projected gain 6.57, hit 0)
- Autosub: Norberto Bercique Gomes Betuncal replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 2.65 | 7.94 | 13.79 | 1.00 | 59.9 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.11 | 0.41 | 0.82 | 0.00 | 7.9 | 0.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.54 | 9.70 | 15.65 | 2.00 | 83.1 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 3.19 | 9.63 | 16.72 | 8.00 | 69.5 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 2.33 | 7.41 | 12.98 | 1.00 | 62.2 | 90.0 |
| Bench 4 | Bench | Toti António Gomes | DEF | 20 | 4.3 | 2.14 | 7.03 | 12.01 | 2.00 | 76.0 | 90.0 |
| Bench 3 | Bench | Noussair Mazraoui | DEF | 14 | 4.2 | 2.25 | 6.86 | 11.40 | 0.00 | 71.1 | 0.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 6.29 | 17.38 | 27.83 | 9.00 | 79.8 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.6 | 4.59 | 13.08 | 21.25 | 7.00 | 86.5 | 90.0 |
| Bench 2 | Autosub In | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 2.52 | 6.57 | 10.82 | 6.00 | 53.6 | 76.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.56 | 22.17 | 36.42 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.56 | 13.76 | 23.07 | 0.00 | 79.5 | 0.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.5 | 4.27 | 13.15 | 22.04 | 10.00 | 71.7 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 4.08 | 11.85 | 19.74 | 1.00 | 62.4 | 55.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 2.96 | 9.08 | 15.85 | 3.00 | 51.1 | 90.0 |