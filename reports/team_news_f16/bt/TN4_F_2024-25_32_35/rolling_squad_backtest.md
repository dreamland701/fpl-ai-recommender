# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 289.21
- Total actual points: 255.00
- Average predicted points: 72.30
- Average actual points: 63.75
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
- Captain: Jacob Murphy
- Vice captain: Mohamed Salah
- Effective captain: Jacob Murphy
- Chip used: bench_boost
- Predicted score: 83.67
- Actual score: 74.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (12.92) beats the best remaining Bench Boost opportunity (15.03).
- Chip advisory: bench_boost (0.56): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.62): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (12.92) beats the best remaining Bench Boost opportunity (15.03).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.86 | 11.22 | 18.05 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | John Ruddy | GK | 15 | 3.9 | 0.89 | 2.27 | 2.94 | 0.00 | 19.9 | 0.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 7.45 | 12.57 | 19.33 | -1.00 | 164.0 | 180.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.16 | 12.34 | 19.81 | 1.00 | 90.0 | 90.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 6.78 | 10.98 | 16.53 | 8.00 | 154.2 | 180.0 |
| Bench 4 | Bench Boost | Dara O'Shea | DEF | 10 | 3.9 | 2.29 | 7.31 | 12.02 | 1.00 | 89.1 | 90.0 |
| Bench 2 | Bench Boost | Ryan Sessegnon | DEF | 9 | 4.1 | 2.55 | 7.08 | 11.45 | 1.00 | 51.9 | 56.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 8.22 | 13.86 | 21.34 | 2.00 | 144.6 | 100.0 |
| XI | XI | Omar Marmoush | FWD | 13 | 7.6 | 4.52 | 13.28 | 21.29 | 7.00 | 77.4 | 81.0 |
| Bench 3 | Bench Boost | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.9 | 2.45 | 8.11 | 13.63 | 1.00 | 61.0 | 26.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.8 | 8.35 | 24.47 | 40.63 | 6.00 | 90.0 | 84.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 5.26 | 15.02 | 25.78 | 4.00 | 65.7 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.6 | 4.82 | 14.78 | 25.39 | 2.00 | 90.0 | 81.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.0 | 4.48 | 14.18 | 23.81 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Jacob Murphy | MID | 15 | 5.2 | 8.80 | 13.57 | 20.23 | 19.00 | 156.5 | 138.0 |

## GW33

- Train rows: 156471
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Omar Marmoush
- Vice captain: Joško Gvardiol
- Effective captain: Omar Marmoush
- Chip used: triple_captain
- Predicted score: 95.67
- Actual score: 68.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (15.82) beats the best remaining Triple Captain opportunity (9.55).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Omar Marmoush. Optimizer chose Triple Captain here because the current estimated captain upside (15.82) beats the best remaining Triple Captain opportunity (9.55).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 8.77 | 13.55 | 20.98 | 7.00 | 180.0 | 180.0 |
| Bench 1 | Bench | John Ruddy | GK | 15 | 3.9 | 0.02 | 0.50 | 1.04 | 0.00 | 6.4 | 0.0 |
| Vice Captain | XI | Joško Gvardiol | DEF | 13 | 6.2 | 8.95 | 14.51 | 22.49 | 7.00 | 180.0 | 180.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 8.12 | 13.26 | 20.29 | 6.00 | 180.0 | 180.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.38 | 10.60 | 16.90 | 0.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Dara O'Shea | DEF | 10 | 3.9 | 2.21 | 7.11 | 11.77 | 0.00 | 87.5 | 90.0 |
| Bench 3 | Bench | Ryan Sessegnon | DEF | 9 | 4.1 | 2.15 | 6.39 | 10.26 | 11.00 | 47.9 | 78.0 |
| Captain | Captain | Omar Marmoush | FWD | 13 | 7.6 | 11.57 | 17.66 | 27.33 | 4.00 | 180.0 | 180.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 7.75 | 13.19 | 20.25 | 10.00 | 145.7 | 84.0 |
| Bench 4 | Bench | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 1.88 | 6.20 | 10.46 | 1.00 | 47.4 | 27.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 8.37 | 23.34 | 38.76 | 3.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 4.58 | 13.84 | 23.83 | 2.00 | 70.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 4.82 | 13.79 | 23.01 | 18.00 | 85.2 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 2.93 | 12.34 | 21.90 | 1.00 | 54.5 | 31.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 3.31 | 10.84 | 18.02 | 2.00 | 70.4 | 64.0 |

## GW34

- Train rows: 157270
- Bank: 0.00 -> 0.80
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 56.54
- Actual score: 66.00
- Transfer: Jean-Philippe Mateta -> Matheus Santos Carneiro Da Cunha (projected gain 4.87, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.5 | 0.00 | 12.17 | 19.73 | 0.00 | 0.0 | 0.0 |
| XI | Bench | John Ruddy | GK | 15 | 3.9 | 0.26 | 0.57 | 0.97 | 0.00 | 4.4 | 0.0 |
| Bench 3 | Bench | Joško Gvardiol | DEF | 13 | 6.2 | 0.00 | 12.71 | 20.95 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 0.00 | 12.71 | 20.93 | 0.00 | 0.0 | 0.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.74 | 10.05 | 16.28 | 6.00 | 85.0 | 90.0 |
| XI | XI | Ryan Sessegnon | DEF | 9 | 4.1 | 3.85 | 10.04 | 15.11 | 11.00 | 70.5 | 90.0 |
| XI | XI | Dara O'Shea | DEF | 10 | 3.9 | 2.05 | 6.65 | 11.17 | 1.00 | 84.6 | 90.0 |
| Bench 4 | Bench | Omar Marmoush | FWD | 13 | 7.6 | 0.00 | 15.20 | 24.38 | 0.00 | 0.0 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.0 | 5.63 | 14.59 | 21.76 | 15.00 | 90.0 | 88.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 1.73 | 5.76 | 9.88 | 2.00 | 47.8 | 63.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.44 | 22.99 | 37.14 | 8.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.0 | 6.90 | 20.46 | 32.40 | 2.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 5.94 | 16.91 | 27.45 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.51 | 14.03 | 23.61 | 4.00 | 77.6 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 5.07 | 13.48 | 22.08 | 6.00 | 78.0 | 66.0 |

## GW35

- Train rows: 158070
- Bank: 0.80 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 53.33
- Actual score: 47.00
- Transfer: Matheus Santos Carneiro Da Cunha -> Yoane Wissa (projected gain 6.78, hit 0)
- Autosub: Norberto Bercique Gomes Betuncal replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 2.66 | 7.80 | 13.63 | 1.00 | 60.4 | 90.0 |
| Bench 1 | Bench | John Ruddy | GK | 15 | 3.9 | 0.04 | 0.40 | 0.84 | 0.00 | 4.3 | 0.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.55 | 9.62 | 15.53 | 2.00 | 83.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 3.18 | 9.52 | 16.47 | 8.00 | 70.1 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 2.30 | 7.21 | 12.71 | 1.00 | 62.0 | 90.0 |
| Bench 3 | Bench | Ryan Sessegnon | DEF | 9 | 4.1 | 2.13 | 6.93 | 11.83 | 0.00 | 56.3 | 56.0 |
| Bench 4 | Bench | Dara O'Shea | DEF | 10 | 3.9 | 2.03 | 6.26 | 10.56 | 1.00 | 81.7 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.6 | 4.59 | 13.10 | 21.25 | 7.00 | 85.8 | 90.0 |
| XI | XI | Omar Marmoush | FWD | 13 | 7.6 | 3.02 | 9.81 | 17.40 | 2.00 | 43.6 | 82.0 |
| Bench 2 | Autosub In | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 2.39 | 6.39 | 10.64 | 6.00 | 53.3 | 76.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.58 | 22.28 | 36.59 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.0 | 6.02 | 17.60 | 28.18 | 5.00 | 90.0 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.51 | 13.59 | 22.80 | 0.00 | 79.1 | 0.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.5 | 4.22 | 13.05 | 21.98 | 10.00 | 71.3 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 4.11 | 11.75 | 19.64 | 1.00 | 62.4 | 55.0 |