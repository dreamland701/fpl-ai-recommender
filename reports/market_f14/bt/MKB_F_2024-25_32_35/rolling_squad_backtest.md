# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 303.58
- Total actual points: 272.00
- Average predicted points: 75.89
- Average actual points: 68.00
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
- Predicted score: 94.97
- Actual score: 81.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (14.83) beats the best remaining Triple Captain opportunity (15.44).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Alexander Isak. Optimizer chose Triple Captain here because the current estimated captain upside (14.83) beats the best remaining Triple Captain opportunity (15.44).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.94 | 11.42 | 18.32 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.46 | 0.77 | 1.06 | 0.00 | 5.7 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.22 | 12.52 | 20.06 | 1.00 | 90.0 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 7.20 | 12.25 | 18.91 | -1.00 | 168.5 | 180.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 6.92 | 11.17 | 16.77 | 8.00 | 154.7 | 180.0 |
| Bench 3 | Bench | Nikola Milenković | DEF | 16 | 5.1 | 3.59 | 10.62 | 16.76 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Toti António Gomes | DEF | 20 | 4.3 | 2.98 | 8.13 | 13.32 | 0.00 | 82.2 | 90.0 |
| Captain | Captain | Alexander Isak | FWD | 15 | 9.5 | 11.30 | 17.34 | 27.36 | 11.00 | 155.1 | 148.0 |
| XI | XI | Omar Marmoush | FWD | 13 | 7.6 | 4.58 | 13.46 | 21.54 | 7.00 | 77.5 | 81.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 7.76 | 13.31 | 20.58 | 2.00 | 146.2 | 100.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 8.23 | 24.20 | 40.21 | 6.00 | 90.0 | 84.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.6 | 4.63 | 14.32 | 24.71 | 2.00 | 90.0 | 81.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.0 | 4.43 | 14.10 | 23.71 | 2.00 | 89.7 | 90.0 |
| Vice Captain | XI | Jacob Murphy | MID | 15 | 5.2 | 9.14 | 13.98 | 20.81 | 19.00 | 161.3 | 138.0 |
| Bench 2 | Bench | Enzo Fernández | MID | 6 | 4.7 | 3.86 | 10.48 | 17.10 | 2.00 | 78.9 | 90.0 |

## GW33

- Train rows: 156471
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Omar Marmoush
- Vice captain: David Raya Martin
- Effective captain: Omar Marmoush
- Chip used: bench_boost
- Predicted score: 97.16
- Actual score: 80.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (15.31) beats the best remaining Bench Boost opportunity (9.99).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (15.31) beats the best remaining Bench Boost opportunity (9.99).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Vice Captain | XI | David Raya Martin | GK | 1 | 5.5 | 9.38 | 14.29 | 21.99 | 7.00 | 180.0 | 180.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.05 | 0.27 | 0.54 | 0.00 | 4.3 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 9.18 | 14.82 | 22.92 | 7.00 | 180.0 | 180.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 8.29 | 13.43 | 20.59 | 6.00 | 180.0 | 180.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.48 | 10.81 | 17.25 | 0.00 | 90.0 | 90.0 |
| Bench 3 | Bench Boost | Nikola Milenković | DEF | 16 | 5.1 | 3.11 | 9.22 | 15.08 | 2.00 | 83.4 | 90.0 |
| Bench 4 | Bench Boost | Toti António Gomes | DEF | 20 | 4.3 | 2.52 | 7.49 | 12.31 | 9.00 | 78.8 | 90.0 |
| Captain | Captain | Omar Marmoush | FWD | 13 | 7.6 | 11.83 | 18.02 | 27.84 | 4.00 | 180.0 | 180.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.82 | 16.82 | 28.04 | 2.00 | 90.0 | 75.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 7.61 | 13.02 | 20.03 | 10.00 | 148.0 | 84.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 8.24 | 23.10 | 38.44 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.37 | 13.64 | 23.05 | 1.00 | 81.6 | 31.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 4.64 | 13.35 | 22.38 | 18.00 | 83.8 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 3.42 | 11.08 | 18.39 | 2.00 | 72.6 | 64.0 |
| Bench 2 | Bench Boost | Enzo Fernández | MID | 6 | 4.7 | 3.38 | 10.03 | 16.59 | 5.00 | 76.7 | 90.0 |

## GW34

- Train rows: 157270
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 56.97
- Actual score: 62.00
- Transfer: Nikola Milenković -> Rayan Aït-Nouri (projected gain 5.37, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.5 | 0.00 | 12.56 | 20.34 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Killian Cahill | GK | 5 | 3.9 | 0.20 | 0.19 | 0.30 | 0.00 | 2.0 | 0.0 |
| XI | XI | Rayan Aït-Nouri | DEF | 20 | 5.0 | 5.94 | 15.82 | 23.99 | 11.00 | 90.0 | 76.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 0.00 | 13.33 | 21.88 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Joško Gvardiol | DEF | 13 | 6.2 | 0.00 | 13.15 | 21.63 | 0.00 | 0.0 | 0.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.81 | 10.26 | 16.63 | 6.00 | 85.4 | 90.0 |
| XI | XI | Toti António Gomes | DEF | 20 | 4.3 | 2.93 | 7.55 | 12.33 | 5.00 | 75.7 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 7.25 | 19.53 | 31.11 | 6.00 | 90.0 | 76.0 |
| Bench 4 | Bench | Omar Marmoush | FWD | 13 | 7.6 | 0.00 | 15.73 | 25.18 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Jean-Philippe Mateta | FWD | 7 | 7.8 | 0.00 | 11.17 | 19.12 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.40 | 22.99 | 37.17 | 8.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.0 | 6.96 | 20.60 | 32.64 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 5.17 | 13.75 | 22.53 | 6.00 | 78.9 | 66.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.32 | 13.60 | 22.98 | 4.00 | 75.9 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.7 | 3.59 | 10.51 | 16.99 | 6.00 | 77.9 | 90.0 |

## GW35

- Train rows: 158070
- Bank: 0.10 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 54.48
- Actual score: 49.00
- Transfer: Jean-Philippe Mateta -> Yoane Wissa (projected gain 3.66, hit 0)
- Autosub: Omar Marmoush replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 2.48 | 7.43 | 13.05 | 1.00 | 57.3 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.00 | 0.00 | 0.01 | 0.00 | 1.3 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 3.12 | 9.43 | 16.31 | 8.00 | 66.9 | 90.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.47 | 9.40 | 15.21 | 2.00 | 83.3 | 90.0 |
| Bench 4 | Bench | Rayan Aït-Nouri | DEF | 20 | 5.0 | 1.76 | 7.17 | 12.86 | 2.00 | 47.9 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 2.25 | 7.13 | 12.57 | 1.00 | 58.3 | 90.0 |
| Bench 3 | Bench | Toti António Gomes | DEF | 20 | 4.3 | 1.95 | 6.67 | 11.41 | 2.00 | 75.1 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 6.31 | 17.24 | 27.71 | 9.00 | 83.0 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.6 | 4.52 | 12.96 | 21.01 | 7.00 | 85.5 | 90.0 |
| Bench 2 | Autosub In | Omar Marmoush | FWD | 13 | 7.6 | 2.98 | 9.76 | 17.29 | 2.00 | 40.2 | 82.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.43 | 21.98 | 36.18 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.0 | 5.97 | 17.47 | 27.98 | 5.00 | 90.0 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.35 | 13.20 | 22.24 | 0.00 | 77.9 | 0.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 4.08 | 11.65 | 19.49 | 1.00 | 63.2 | 55.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.7 | 3.07 | 10.07 | 16.57 | 9.00 | 78.2 | 87.0 |