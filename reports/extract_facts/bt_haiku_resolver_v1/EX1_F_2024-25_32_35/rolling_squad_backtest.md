# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 301.75
- Total actual points: 233.00
- Average predicted points: 75.44
- Average actual points: 58.25
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
- Chip used: bench_boost
- Predicted score: 86.24
- Actual score: 67.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.25) beats the best remaining Bench Boost opportunity (14.03).
- Chip advisory: triple_captain (0.66): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.25) beats the best remaining Bench Boost opportunity (14.03).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.86 | 11.22 | 18.03 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.63 | 1.17 | 1.70 | 0.00 | 10.5 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.5 | 4.23 | 12.53 | 19.99 | 2.00 | 90.0 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 7.39 | 12.51 | 19.21 | -1.00 | 162.7 | 180.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.16 | 12.33 | 19.77 | 1.00 | 90.0 | 90.0 |
| Bench 3 | Bench Boost | Dara O'Shea | DEF | 10 | 3.9 | 2.29 | 7.30 | 12.00 | 1.00 | 89.0 | 90.0 |
| Bench 4 | Bench Boost | Wout Faes | DEF | 11 | 3.9 | 1.67 | 5.24 | 8.60 | 0.00 | 72.6 | 0.0 |
| Captain | Captain | Alexander Isak | FWD | 15 | 9.5 | 10.01 | 15.72 | 26.17 | 11.00 | 133.9 | 148.0 |
| XI | XI | Omar Marmoush | FWD | 13 | 7.6 | 5.13 | 14.82 | 24.06 | 7.00 | 90.0 | 81.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 8.12 | 13.76 | 21.15 | 2.00 | 142.5 | 100.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 8.38 | 24.54 | 40.61 | 6.00 | 90.0 | 84.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.6 | 4.85 | 14.85 | 25.43 | 2.00 | 90.0 | 81.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.0 | 4.51 | 14.26 | 23.87 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Jacob Murphy | MID | 15 | 5.2 | 8.62 | 13.37 | 19.94 | 19.00 | 153.3 | 138.0 |
| Bench 2 | Bench Boost | Boubakary Soumaré | MID | 11 | 4.4 | 2.38 | 6.84 | 11.16 | 2.00 | 75.7 | 90.0 |

## GW33

- Train rows: 156471
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Omar Marmoush
- Vice captain: William Saliba
- Effective captain: Omar Marmoush
- Chip used: triple_captain
- Predicted score: 107.00
- Actual score: 75.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (16.33) beats the best remaining Triple Captain opportunity (9.62).
- Chip advisory: triple_captain (0.65): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Omar Marmoush. Optimizer chose Triple Captain here because the current estimated captain upside (16.33) beats the best remaining Triple Captain opportunity (9.62).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 8.70 | 13.48 | 20.85 | 7.00 | 180.0 | 180.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.28 | 0.74 | 1.25 | 0.00 | 9.4 | 0.0 |
| Vice Captain | XI | William Saliba | DEF | 1 | 6.5 | 10.73 | 16.92 | 27.16 | 7.00 | 180.0 | 180.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 8.87 | 14.42 | 22.32 | 7.00 | 180.0 | 180.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 8.12 | 13.26 | 20.26 | 6.00 | 180.0 | 180.0 |
| Bench 2 | Bench | Dara O'Shea | DEF | 10 | 3.9 | 2.20 | 7.10 | 11.75 | 0.00 | 87.4 | 90.0 |
| Bench 4 | Bench | Wout Faes | DEF | 11 | 3.8 | 0.34 | 2.18 | 4.22 | 2.00 | 38.7 | 90.0 |
| Captain | Captain | Omar Marmoush | FWD | 13 | 7.6 | 11.73 | 18.88 | 30.52 | 4.00 | 180.0 | 180.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.76 | 16.67 | 27.69 | 2.00 | 90.0 | 75.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 8.43 | 13.95 | 21.48 | 10.00 | 172.6 | 84.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 8.42 | 23.44 | 38.79 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.54 | 14.04 | 23.61 | 1.00 | 84.3 | 31.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 4.89 | 13.94 | 23.16 | 18.00 | 86.2 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 3.34 | 10.92 | 18.08 | 2.00 | 70.8 | 64.0 |
| Bench 3 | Bench | Boubakary Soumaré | MID | 11 | 4.4 | 2.00 | 6.28 | 10.44 | 2.00 | 77.8 | 90.0 |

## GW34

- Train rows: 157270
- Bank: 0.00 -> 0.80
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 53.46
- Actual score: 51.00
- Transfer: Jean-Philippe Mateta -> Matheus Santos Carneiro Da Cunha (projected gain 5.94, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.5 | 0.00 | 12.17 | 19.71 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Killian Cahill | GK | 5 | 3.9 | 0.42 | 0.71 | 1.12 | 0.00 | 7.7 | 0.0 |
| XI | Bench | William Saliba | DEF | 1 | 6.5 | 0.00 | 13.65 | 21.93 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Joško Gvardiol | DEF | 13 | 6.2 | 0.00 | 12.74 | 20.95 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 0.00 | 12.68 | 20.87 | 0.00 | 0.0 | 0.0 |
| XI | XI | Dara O'Shea | DEF | 10 | 3.9 | 2.04 | 6.62 | 11.13 | 1.00 | 84.4 | 90.0 |
| XI | XI | Wout Faes | DEF | 11 | 3.8 | 1.91 | 5.46 | 9.08 | 0.00 | 72.1 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 7.07 | 19.06 | 30.30 | 6.00 | 90.0 | 76.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.0 | 6.12 | 15.71 | 24.12 | 15.00 | 90.0 | 88.0 |
| Bench 4 | Bench | Omar Marmoush | FWD | 13 | 7.6 | 0.00 | 15.24 | 24.36 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.42 | 22.96 | 37.01 | 8.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.0 | 7.25 | 22.05 | 35.60 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.51 | 14.04 | 23.59 | 4.00 | 77.7 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 5.05 | 13.44 | 22.01 | 6.00 | 77.7 | 66.0 |
| XI | XI | Boubakary Soumaré | MID | 11 | 4.4 | 2.23 | 6.38 | 10.64 | 1.00 | 78.3 | 45.0 |

## GW35

- Train rows: 158070
- Bank: 0.80 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.05
- Actual score: 40.00
- Transfer: Matheus Santos Carneiro Da Cunha -> Yoane Wissa (projected gain 8.01, hit 0)
- Autosub: Boubakary Soumaré replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 2.70 | 7.91 | 13.73 | 1.00 | 61.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.05 | 0.31 | 0.65 | 0.00 | 7.2 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 3.20 | 9.56 | 16.49 | 8.00 | 70.3 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.5 | 3.15 | 9.24 | 16.09 | 1.00 | 63.5 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 2.35 | 7.31 | 12.82 | 1.00 | 62.6 | 90.0 |
| Bench 4 | Bench | Dara O'Shea | DEF | 10 | 3.9 | 2.03 | 6.26 | 10.55 | 1.00 | 81.7 | 90.0 |
| Bench 3 | Bench | Wout Faes | DEF | 11 | 3.8 | 2.25 | 5.70 | 9.27 | 7.00 | 70.2 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 6.33 | 17.32 | 27.72 | 9.00 | 79.8 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.6 | 4.37 | 13.80 | 21.80 | 7.00 | 90.0 | 90.0 |
| XI | XI | Omar Marmoush | FWD | 13 | 7.6 | 3.08 | 9.97 | 17.54 | 2.00 | 44.5 | 82.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.58 | 22.29 | 36.50 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.0 | 6.02 | 17.59 | 28.10 | 5.00 | 90.0 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.54 | 13.66 | 22.84 | 0.00 | 79.5 | 0.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 4.14 | 11.83 | 19.69 | 1.00 | 62.8 | 55.0 |
| Bench 2 | Autosub In | Boubakary Soumaré | MID | 11 | 4.4 | 2.31 | 5.81 | 9.53 | 1.00 | 62.2 | 6.0 |