# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 311.22
- Total actual points: 268.00
- Average predicted points: 77.80
- Average actual points: 67.00
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
- Predicted score: 96.16
- Actual score: 85.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (14.90) beats the best remaining Triple Captain opportunity (15.89).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Alexander Isak. Optimizer chose Triple Captain here because the current estimated captain upside (14.90) beats the best remaining Triple Captain opportunity (15.89).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.91 | 11.34 | 18.23 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.39 | 0.80 | 1.32 | 0.00 | 7.2 | 0.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 7.57 | 12.70 | 19.52 | -1.00 | 166.5 | 180.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.17 | 12.37 | 19.87 | 1.00 | 90.0 | 90.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 6.82 | 11.02 | 16.59 | 8.00 | 155.0 | 180.0 |
| Bench 3 | Bench | Neco Williams | DEF | 16 | 4.5 | 3.13 | 9.11 | 14.79 | 2.00 | 85.7 | 90.0 |
| Bench 4 | Bench | Dara O'Shea | DEF | 10 | 3.9 | 2.32 | 7.38 | 12.14 | 1.00 | 89.8 | 90.0 |
| Captain | Captain | Alexander Isak | FWD | 15 | 9.5 | 11.37 | 17.39 | 27.46 | 11.00 | 155.0 | 148.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 8.19 | 13.83 | 21.29 | 2.00 | 144.0 | 100.0 |
| XI | XI | Omar Marmoush | FWD | 13 | 7.6 | 4.53 | 13.31 | 21.34 | 7.00 | 77.7 | 81.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 8.30 | 24.40 | 40.51 | 6.00 | 90.0 | 84.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.6 | 4.70 | 14.49 | 24.93 | 2.00 | 90.0 | 81.0 |
| Bench 2 | Bench | Bryan Mbeumo | MID | 4 | 8.0 | 4.46 | 14.13 | 23.74 | 2.00 | 89.7 | 90.0 |
| Vice Captain | XI | Jacob Murphy | MID | 15 | 5.2 | 9.04 | 13.84 | 20.64 | 19.00 | 161.6 | 138.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 4.82 | 12.65 | 20.20 | 6.00 | 88.2 | 84.0 |

## GW33

- Train rows: 156471
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Omar Marmoush
- Vice captain: Joško Gvardiol
- Effective captain: Omar Marmoush
- Chip used: bench_boost
- Predicted score: 102.51
- Actual score: 80.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (15.41) beats the best remaining Bench Boost opportunity (10.27).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (15.41) beats the best remaining Bench Boost opportunity (10.27).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 8.90 | 13.72 | 21.23 | 7.00 | 180.0 | 180.0 |
| Bench 1 | Bench Boost | Daniel Bentley | GK | 20 | 3.9 | 0.10 | 0.47 | 0.88 | 7.00 | 4.5 | 90.0 |
| Vice Captain | XI | Joško Gvardiol | DEF | 13 | 6.2 | 9.20 | 14.81 | 22.93 | 7.00 | 180.0 | 180.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 8.42 | 13.59 | 20.80 | 6.00 | 180.0 | 180.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.51 | 10.86 | 17.30 | 0.00 | 90.0 | 90.0 |
| Bench 3 | Bench Boost | Neco Williams | DEF | 16 | 4.5 | 2.95 | 8.51 | 14.10 | 2.00 | 85.0 | 90.0 |
| Bench 4 | Bench Boost | Dara O'Shea | DEF | 10 | 3.9 | 2.25 | 7.20 | 11.91 | 0.00 | 88.3 | 90.0 |
| Captain | Captain | Omar Marmoush | FWD | 13 | 7.6 | 11.84 | 17.99 | 27.83 | 4.00 | 180.0 | 180.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.91 | 17.03 | 28.31 | 2.00 | 90.0 | 75.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 7.84 | 13.30 | 20.41 | 10.00 | 147.6 | 84.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 8.32 | 23.28 | 38.67 | 3.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 8.90 | 14.85 | 22.85 | 7.00 | 180.0 | 166.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.40 | 13.72 | 23.16 | 1.00 | 81.7 | 31.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 4.74 | 13.58 | 22.69 | 18.00 | 83.4 | 90.0 |
| Bench 2 | Bench Boost | Jacob Murphy | MID | 15 | 5.2 | 3.41 | 11.06 | 18.35 | 2.00 | 72.7 | 64.0 |

## GW34

- Train rows: 157270
- Bank: 0.10 -> 0.90
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 56.87
- Actual score: 56.00
- Transfer: Jean-Philippe Mateta -> Matheus Santos Carneiro Da Cunha (projected gain 4.94, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.5 | 0.00 | 12.66 | 20.48 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Daniel Bentley | GK | 20 | 3.9 | 1.62 | 3.66 | 5.48 | 0.00 | 37.9 | 0.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 0.00 | 13.36 | 21.91 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Joško Gvardiol | DEF | 13 | 6.2 | 0.00 | 13.21 | 21.71 | 0.00 | 0.0 | 0.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.76 | 10.10 | 16.35 | 6.00 | 85.4 | 90.0 |
| XI | XI | Neco Williams | DEF | 16 | 4.5 | 2.87 | 8.27 | 13.81 | 0.00 | 84.7 | 90.0 |
| XI | XI | Dara O'Shea | DEF | 10 | 3.9 | 2.08 | 6.71 | 11.27 | 1.00 | 85.1 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 7.28 | 19.59 | 31.14 | 6.00 | 90.0 | 76.0 |
| Bench 4 | Bench | Omar Marmoush | FWD | 13 | 7.6 | 0.00 | 15.75 | 25.22 | 0.00 | 0.0 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.0 | 5.80 | 15.01 | 22.38 | 15.00 | 90.0 | 88.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.47 | 23.11 | 37.30 | 8.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.0 | 7.01 | 20.70 | 32.76 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.41 | 13.79 | 23.24 | 4.00 | 75.6 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 5.11 | 13.59 | 22.25 | 6.00 | 79.0 | 66.0 |
| XI | Bench | Morgan Rogers | MID | 2 | 5.6 | 0.00 | 13.09 | 21.26 | 0.00 | 0.0 | 0.0 |

## GW35

- Train rows: 158070
- Bank: 0.90 -> 1.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.68
- Actual score: 47.00
- Transfer: Matheus Santos Carneiro Da Cunha -> Yoane Wissa (projected gain 4.68, hit 0)
- Autosub: Morgan Rogers replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 2.51 | 7.49 | 13.15 | 1.00 | 57.2 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.06 | 0.71 | 1.50 | 0.00 | 11.5 | 0.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.56 | 9.63 | 15.55 | 2.00 | 83.2 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 3.04 | 9.24 | 16.05 | 8.00 | 67.3 | 90.0 |
| XI | XI | Neco Williams | DEF | 16 | 4.5 | 2.89 | 8.39 | 13.74 | 5.00 | 83.8 | 90.0 |
| Bench 3 | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 2.16 | 6.90 | 12.25 | 1.00 | 59.0 | 90.0 |
| Bench 4 | Bench | Dara O'Shea | DEF | 10 | 3.9 | 2.06 | 6.31 | 10.63 | 1.00 | 82.1 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 6.45 | 17.61 | 28.25 | 9.00 | 82.7 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.6 | 4.56 | 13.02 | 21.12 | 7.00 | 85.1 | 90.0 |
| XI | XI | Omar Marmoush | FWD | 13 | 7.6 | 2.88 | 9.51 | 16.95 | 2.00 | 40.6 | 82.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.59 | 22.32 | 36.64 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.0 | 6.05 | 17.65 | 28.26 | 5.00 | 90.0 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.43 | 13.40 | 22.50 | 0.00 | 77.4 | 0.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 4.15 | 11.84 | 19.77 | 1.00 | 63.2 | 55.0 |
| Bench 2 | Autosub In | Morgan Rogers | MID | 2 | 5.6 | 2.78 | 8.57 | 15.10 | 3.00 | 47.7 | 90.0 |