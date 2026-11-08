# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 302.92
- Total actual points: 233.00
- Average predicted points: 75.73
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
- Predicted score: 86.68
- Actual score: 67.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.33) beats the best remaining Bench Boost opportunity (14.14).
- Chip advisory: triple_captain (0.63): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.33) beats the best remaining Bench Boost opportunity (14.14).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.91 | 11.30 | 18.07 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.75 | 1.37 | 1.88 | 0.00 | 14.1 | 0.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 7.52 | 12.62 | 19.30 | -1.00 | 166.3 | 180.0 |
| XI | XI | William Saliba | DEF | 1 | 6.5 | 4.24 | 12.54 | 19.95 | 2.00 | 90.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.19 | 12.39 | 19.78 | 1.00 | 90.0 | 90.0 |
| Bench 3 | Bench Boost | Dara O'Shea | DEF | 10 | 3.9 | 2.33 | 7.37 | 12.04 | 1.00 | 90.0 | 90.0 |
| Bench 4 | Bench Boost | Wout Faes | DEF | 11 | 3.9 | 1.53 | 5.50 | 9.37 | 0.00 | 68.6 | 0.0 |
| Captain | Captain | Alexander Isak | FWD | 15 | 9.5 | 9.91 | 15.96 | 26.75 | 11.00 | 131.3 | 148.0 |
| XI | XI | Omar Marmoush | FWD | 13 | 7.6 | 5.14 | 14.83 | 24.03 | 7.00 | 90.0 | 81.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 8.22 | 13.84 | 21.22 | 2.00 | 145.3 | 100.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 8.42 | 24.60 | 40.64 | 6.00 | 90.0 | 84.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.6 | 4.88 | 14.91 | 25.44 | 2.00 | 90.0 | 81.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.0 | 4.55 | 14.33 | 23.90 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Jacob Murphy | MID | 15 | 5.2 | 8.73 | 13.46 | 20.00 | 19.00 | 156.5 | 138.0 |
| Bench 2 | Bench Boost | Boubakary Soumaré | MID | 11 | 4.4 | 2.43 | 6.93 | 11.22 | 2.00 | 77.2 | 90.0 |

## GW33

- Train rows: 156471
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Omar Marmoush
- Vice captain: William Saliba
- Effective captain: Omar Marmoush
- Chip used: triple_captain
- Predicted score: 107.27
- Actual score: 75.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (16.43) beats the best remaining Triple Captain opportunity (9.64).
- Chip advisory: triple_captain (0.65): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Omar Marmoush. Optimizer chose Triple Captain here because the current estimated captain upside (16.43) beats the best remaining Triple Captain opportunity (9.64).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 8.78 | 13.53 | 20.88 | 7.00 | 180.0 | 180.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.40 | 0.94 | 1.44 | 0.00 | 13.0 | 0.0 |
| Vice Captain | XI | William Saliba | DEF | 1 | 6.5 | 10.80 | 16.99 | 27.23 | 7.00 | 180.0 | 180.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 8.96 | 14.49 | 22.37 | 7.00 | 180.0 | 180.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 8.07 | 13.23 | 20.21 | 6.00 | 180.0 | 180.0 |
| Bench 2 | Bench | Dara O'Shea | DEF | 10 | 3.9 | 2.24 | 7.17 | 11.79 | 0.00 | 88.6 | 90.0 |
| Bench 4 | Bench | Wout Faes | DEF | 11 | 3.8 | 0.26 | 2.53 | 5.09 | 2.00 | 36.5 | 90.0 |
| Captain | Captain | Omar Marmoush | FWD | 13 | 7.6 | 11.83 | 18.96 | 30.60 | 4.00 | 180.0 | 180.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.75 | 16.66 | 27.64 | 2.00 | 90.0 | 75.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 8.39 | 13.91 | 21.40 | 10.00 | 171.5 | 84.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 8.43 | 23.46 | 38.77 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 4.93 | 14.00 | 23.18 | 18.00 | 87.2 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.31 | 13.69 | 23.21 | 1.00 | 77.2 | 31.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 3.34 | 10.93 | 18.05 | 2.00 | 71.0 | 64.0 |
| Bench 3 | Bench | Boubakary Soumaré | MID | 11 | 4.4 | 2.04 | 6.36 | 10.50 | 2.00 | 79.1 | 90.0 |

## GW34

- Train rows: 157270
- Bank: 0.00 -> 0.80
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 53.79
- Actual score: 51.00
- Transfer: Jean-Philippe Mateta -> Matheus Santos Carneiro Da Cunha (projected gain 5.97, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.5 | 0.00 | 11.98 | 19.51 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Killian Cahill | GK | 5 | 3.9 | 0.55 | 0.92 | 1.31 | 0.00 | 11.3 | 0.0 |
| XI | Bench | William Saliba | DEF | 1 | 6.5 | 0.00 | 13.44 | 21.71 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Joško Gvardiol | DEF | 13 | 6.2 | 0.00 | 12.72 | 20.85 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 0.00 | 12.60 | 20.71 | 0.00 | 0.0 | 0.0 |
| XI | XI | Dara O'Shea | DEF | 10 | 3.9 | 2.08 | 6.69 | 11.18 | 1.00 | 85.5 | 90.0 |
| XI | XI | Wout Faes | DEF | 11 | 3.8 | 1.98 | 5.57 | 9.18 | 0.00 | 74.0 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 7.06 | 19.05 | 30.28 | 6.00 | 90.0 | 76.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.0 | 6.17 | 15.76 | 24.14 | 15.00 | 90.0 | 88.0 |
| Bench 4 | Bench | Omar Marmoush | FWD | 13 | 7.6 | 0.00 | 15.21 | 24.25 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.42 | 22.96 | 36.99 | 8.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.0 | 7.17 | 21.90 | 35.52 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.58 | 14.16 | 23.68 | 4.00 | 79.6 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 5.07 | 13.47 | 22.01 | 6.00 | 78.2 | 66.0 |
| XI | XI | Boubakary Soumaré | MID | 11 | 4.4 | 2.28 | 6.47 | 10.71 | 1.00 | 79.6 | 45.0 |

## GW35

- Train rows: 158070
- Bank: 0.80 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.18
- Actual score: 40.00
- Transfer: Matheus Santos Carneiro Da Cunha -> Yoane Wissa (projected gain 7.91, hit 0)
- Autosub: Boubakary Soumaré replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 2.79 | 8.04 | 13.81 | 1.00 | 63.3 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.18 | 0.52 | 0.85 | 0.00 | 10.7 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 3.26 | 9.65 | 16.54 | 8.00 | 71.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.5 | 2.96 | 8.91 | 15.69 | 1.00 | 57.4 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 2.39 | 7.38 | 12.85 | 1.00 | 63.8 | 90.0 |
| Bench 4 | Bench | Dara O'Shea | DEF | 10 | 3.9 | 2.08 | 6.35 | 10.61 | 1.00 | 83.1 | 90.0 |
| Bench 3 | Bench | Wout Faes | DEF | 11 | 3.8 | 2.33 | 5.83 | 9.37 | 7.00 | 72.4 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 6.35 | 17.34 | 27.70 | 9.00 | 80.2 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.6 | 4.39 | 13.81 | 21.77 | 7.00 | 90.0 | 90.0 |
| XI | XI | Omar Marmoush | FWD | 13 | 7.6 | 3.16 | 10.08 | 17.61 | 2.00 | 46.7 | 82.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.59 | 22.30 | 36.49 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.0 | 6.04 | 17.62 | 28.10 | 5.00 | 90.0 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.50 | 13.55 | 22.80 | 0.00 | 78.4 | 0.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 4.18 | 11.89 | 19.73 | 1.00 | 64.0 | 55.0 |
| Bench 2 | Autosub In | Boubakary Soumaré | MID | 11 | 4.4 | 2.38 | 5.93 | 9.61 | 1.00 | 64.4 | 6.0 |