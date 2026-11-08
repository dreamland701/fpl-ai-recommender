# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 294.53
- Total actual points: 254.00
- Average predicted points: 73.63
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
- Predicted score: 96.02
- Actual score: 82.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (14.71) beats the best remaining Triple Captain opportunity (15.56).
- Chip advisory: triple_captain (0.69): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Alexander Isak. Optimizer chose Triple Captain here because the current estimated captain upside (14.71) beats the best remaining Triple Captain opportunity (15.56).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.87 | 11.25 | 18.12 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.60 | 1.05 | 1.50 | 0.00 | 9.7 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.17 | 12.39 | 19.91 | 1.00 | 90.0 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 7.32 | 12.27 | 18.76 | -1.00 | 159.0 | 180.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 6.85 | 11.06 | 16.64 | 8.00 | 156.2 | 180.0 |
| Bench 2 | Bench | Neco Williams | DEF | 16 | 4.5 | 3.20 | 9.28 | 15.06 | 2.00 | 87.3 | 90.0 |
| Bench 4 | Bench | Dara O'Shea | DEF | 10 | 3.9 | 2.32 | 7.42 | 12.24 | 1.00 | 89.9 | 90.0 |
| Captain | Captain | Alexander Isak | FWD | 15 | 9.5 | 11.18 | 17.17 | 27.16 | 11.00 | 151.5 | 148.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 8.28 | 13.94 | 21.45 | 2.00 | 146.3 | 100.0 |
| Bench 3 | Bench | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.9 | 2.45 | 8.10 | 13.61 | 1.00 | 61.0 | 26.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 8.31 | 24.34 | 40.41 | 6.00 | 90.0 | 84.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 5.26 | 15.06 | 25.89 | 4.00 | 65.8 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.6 | 4.81 | 14.77 | 25.36 | 2.00 | 90.0 | 81.0 |
| Vice Captain | XI | Jacob Murphy | MID | 15 | 5.2 | 8.86 | 13.62 | 20.29 | 19.00 | 158.1 | 138.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 4.74 | 12.37 | 19.71 | 6.00 | 85.4 | 84.0 |

## GW33

- Train rows: 156471
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Joško Gvardiol
- Vice captain: David Raya Martin
- Effective captain: Joško Gvardiol
- Chip used: bench_boost
- Predicted score: 88.46
- Actual score: 57.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.60) beats the best remaining Bench Boost opportunity (8.93).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.60) beats the best remaining Bench Boost opportunity (8.93).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Vice Captain | XI | David Raya Martin | GK | 1 | 5.5 | 8.81 | 13.60 | 21.05 | 7.00 | 180.0 | 180.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.25 | 0.64 | 1.08 | 0.00 | 8.7 | 0.0 |
| Captain | Captain | Joško Gvardiol | DEF | 13 | 6.2 | 8.99 | 14.56 | 22.57 | 7.00 | 180.0 | 180.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 8.02 | 13.01 | 19.81 | 6.00 | 180.0 | 180.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.40 | 10.62 | 16.93 | 0.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Neco Williams | DEF | 16 | 4.5 | 2.98 | 8.59 | 14.23 | 2.00 | 85.8 | 90.0 |
| Bench 3 | Bench Boost | Dara O'Shea | DEF | 10 | 3.9 | 2.24 | 7.23 | 12.00 | 0.00 | 88.4 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.71 | 16.61 | 27.72 | 2.00 | 90.0 | 75.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 7.82 | 13.26 | 20.35 | 10.00 | 147.5 | 84.0 |
| Bench 4 | Bench Boost | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 1.89 | 6.23 | 10.52 | 1.00 | 47.6 | 27.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 8.34 | 23.26 | 38.64 | 3.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 8.64 | 14.39 | 22.05 | 7.00 | 176.9 | 166.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.50 | 13.96 | 23.54 | 1.00 | 83.7 | 31.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 4.58 | 13.89 | 23.96 | 2.00 | 70.8 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 3.32 | 10.84 | 17.99 | 2.00 | 70.8 | 64.0 |

## GW34

- Train rows: 157270
- Bank: 0.10 -> 0.90
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.96
- Actual score: 59.00
- Transfer: Jean-Philippe Mateta -> Matheus Santos Carneiro Da Cunha (projected gain 3.55, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.5 | 0.00 | 12.20 | 19.88 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Killian Cahill | GK | 5 | 3.9 | 0.40 | 0.63 | 0.96 | 0.00 | 7.1 | 0.0 |
| Bench 3 | Bench | Joško Gvardiol | DEF | 13 | 6.2 | 0.00 | 12.75 | 21.11 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 0.00 | 12.42 | 20.49 | 0.00 | 0.0 | 0.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.75 | 10.09 | 16.35 | 6.00 | 85.5 | 90.0 |
| XI | XI | Neco Williams | DEF | 16 | 4.5 | 2.89 | 8.34 | 13.95 | 0.00 | 85.5 | 90.0 |
| XI | XI | Dara O'Shea | DEF | 10 | 3.9 | 2.08 | 6.77 | 11.39 | 1.00 | 85.6 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 7.11 | 19.21 | 30.62 | 6.00 | 90.0 | 76.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.0 | 5.65 | 14.71 | 21.98 | 15.00 | 90.0 | 88.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 1.74 | 5.83 | 9.99 | 2.00 | 48.3 | 63.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.41 | 22.93 | 37.07 | 8.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 5.94 | 16.94 | 27.54 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.50 | 14.04 | 23.61 | 4.00 | 77.7 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 5.07 | 13.49 | 22.08 | 6.00 | 78.3 | 66.0 |
| Bench 4 | Bench | Morgan Rogers | MID | 2 | 5.6 | 0.00 | 12.36 | 20.16 | 0.00 | 0.0 | 0.0 |

## GW35

- Train rows: 158070
- Bank: 0.90 -> 1.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 54.08
- Actual score: 56.00
- Transfer: Matheus Santos Carneiro Da Cunha -> Yoane Wissa (projected gain 6.76, hit 0)
- Autosub: Norberto Bercique Gomes Betuncal replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 2.67 | 7.86 | 13.75 | 1.00 | 60.9 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.03 | 0.23 | 0.51 | 0.00 | 6.6 | 0.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.56 | 9.65 | 15.58 | 2.00 | 83.3 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 3.20 | 9.58 | 16.59 | 8.00 | 70.6 | 90.0 |
| XI | XI | Neco Williams | DEF | 16 | 4.5 | 2.91 | 8.48 | 13.90 | 5.00 | 84.7 | 90.0 |
| Bench 3 | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 2.25 | 7.00 | 12.34 | 1.00 | 59.7 | 90.0 |
| Bench 4 | Bench | Dara O'Shea | DEF | 10 | 3.9 | 2.07 | 6.40 | 10.82 | 1.00 | 82.8 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 6.31 | 17.31 | 27.85 | 9.00 | 79.9 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.6 | 4.61 | 13.16 | 21.35 | 7.00 | 86.4 | 90.0 |
| Bench 2 | Autosub In | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 2.41 | 6.45 | 10.75 | 6.00 | 53.8 | 76.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.56 | 22.25 | 36.56 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.52 | 13.62 | 22.86 | 0.00 | 79.3 | 0.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.5 | 4.22 | 13.09 | 22.09 | 10.00 | 71.4 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 4.11 | 11.77 | 19.66 | 1.00 | 62.6 | 55.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 2.88 | 8.67 | 15.19 | 3.00 | 48.3 | 90.0 |