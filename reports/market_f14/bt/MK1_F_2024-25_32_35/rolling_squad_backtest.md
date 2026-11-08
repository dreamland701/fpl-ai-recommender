# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 311.54
- Total actual points: 282.00
- Average predicted points: 77.89
- Average actual points: 70.50
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
- Predicted score: 94.38
- Actual score: 81.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (14.73) beats the best remaining Triple Captain opportunity (15.70).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Alexander Isak. Optimizer chose Triple Captain here because the current estimated captain upside (14.73) beats the best remaining Triple Captain opportunity (15.70).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.03 | 11.66 | 18.65 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Karl Hein | GK | 1 | 4.0 | 0.20 | 0.54 | 0.93 | 0.00 | 6.9 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.27 | 12.74 | 20.37 | 1.00 | 90.0 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 7.13 | 12.31 | 19.03 | -1.00 | 168.6 | 180.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 7.28 | 12.01 | 17.52 | 8.00 | 147.7 | 180.0 |
| Bench 3 | Bench | Neco Williams | DEF | 16 | 4.5 | 3.44 | 9.53 | 15.15 | 2.00 | 84.6 | 90.0 |
| Bench 4 | Bench | Rayan Aït-Nouri | DEF | 20 | 4.8 | 3.37 | 9.22 | 15.20 | 14.00 | 74.2 | 69.0 |
| Captain | Captain | Alexander Isak | FWD | 15 | 9.5 | 11.20 | 17.22 | 26.88 | 11.00 | 153.0 | 148.0 |
| XI | XI | Omar Marmoush | FWD | 13 | 7.6 | 4.61 | 13.57 | 21.56 | 7.00 | 77.0 | 81.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 7.52 | 12.92 | 20.12 | 2.00 | 148.3 | 100.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 8.17 | 23.90 | 39.43 | 6.00 | 90.0 | 84.0 |
| Vice Captain | XI | Jacob Murphy | MID | 15 | 5.2 | 9.02 | 13.96 | 19.93 | 19.00 | 153.5 | 138.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.0 | 4.31 | 13.62 | 23.38 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.6 | 4.43 | 13.60 | 24.07 | 2.00 | 90.0 | 81.0 |
| Bench 2 | Bench | Enzo Fernández | MID | 6 | 4.7 | 4.03 | 11.23 | 17.80 | 2.00 | 76.2 | 90.0 |

## GW33

- Train rows: 156471
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Omar Marmoush
- Vice captain: David Raya Martin
- Effective captain: Omar Marmoush
- Chip used: bench_boost
- Predicted score: 101.10
- Actual score: 76.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (16.38) beats the best remaining Bench Boost opportunity (10.72).
- Chip advisory: bench_boost (0.56): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (16.38) beats the best remaining Bench Boost opportunity (10.72).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Vice Captain | XI | David Raya Martin | GK | 1 | 5.5 | 11.06 | 16.98 | 25.47 | 7.00 | 180.0 | 180.0 |
| Bench 1 | Bench Boost | Karl Hein | GK | 1 | 4.0 | 0.09 | 1.16 | 1.69 | 0.00 | 12.2 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 9.90 | 16.36 | 24.86 | 7.00 | 180.0 | 180.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 8.72 | 14.34 | 21.75 | 6.00 | 180.0 | 180.0 |
| Bench 3 | Bench Boost | Tino Livramento | DEF | 15 | 4.6 | 3.34 | 10.60 | 17.06 | 0.00 | 90.0 | 90.0 |
| XI | XI | Rayan Aït-Nouri | DEF | 20 | 4.8 | 3.45 | 10.33 | 17.34 | 5.00 | 75.3 | 81.0 |
| Bench 4 | Bench Boost | Neco Williams | DEF | 16 | 4.5 | 2.88 | 8.37 | 14.00 | 2.00 | 85.7 | 90.0 |
| Captain | Captain | Omar Marmoush | FWD | 13 | 7.6 | 12.27 | 18.99 | 28.04 | 4.00 | 174.6 | 180.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.68 | 16.36 | 27.60 | 2.00 | 90.0 | 75.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 7.60 | 12.97 | 19.97 | 10.00 | 148.3 | 84.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 8.18 | 23.11 | 38.06 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.42 | 13.57 | 22.99 | 1.00 | 82.5 | 31.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 4.48 | 12.94 | 22.09 | 18.00 | 86.0 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 3.38 | 10.99 | 18.39 | 2.00 | 73.5 | 64.0 |
| Bench 2 | Bench Boost | Enzo Fernández | MID | 6 | 4.7 | 3.37 | 9.97 | 16.54 | 5.00 | 77.3 | 90.0 |

## GW34

- Train rows: 157270
- Bank: 0.00 -> 0.80
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 62.07
- Actual score: 72.00
- Transfer: Jean-Philippe Mateta -> Matheus Santos Carneiro Da Cunha (projected gain 5.57, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.5 | 0.00 | 9.91 | 16.96 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Karl Hein | GK | 1 | 4.0 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Rayan Aït-Nouri | DEF | 20 | 4.9 | 5.84 | 15.37 | 23.47 | 11.00 | 90.0 | 76.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 4.13 | 11.82 | 18.52 | 6.00 | 81.1 | 90.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 0.00 | 10.73 | 18.84 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Joško Gvardiol | DEF | 13 | 6.2 | 0.00 | 10.72 | 18.65 | 0.00 | 0.0 | 0.0 |
| XI | XI | Neco Williams | DEF | 16 | 4.5 | 2.96 | 8.59 | 14.20 | 0.00 | 83.9 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 7.22 | 19.68 | 31.07 | 6.00 | 90.0 | 76.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.0 | 5.48 | 13.93 | 21.03 | 15.00 | 90.0 | 88.0 |
| Bench 4 | Bench | Omar Marmoush | FWD | 13 | 7.6 | 0.00 | 13.82 | 24.05 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.31 | 23.08 | 37.10 | 8.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.0 | 6.73 | 19.73 | 31.86 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 5.13 | 13.82 | 22.18 | 6.00 | 76.8 | 66.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.21 | 13.19 | 22.66 | 4.00 | 78.2 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.7 | 3.75 | 11.06 | 17.46 | 6.00 | 75.9 | 90.0 |

## GW35

- Train rows: 158070
- Bank: 0.80 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 53.98
- Actual score: 53.00
- Transfer: Matheus Santos Carneiro Da Cunha -> Yoane Wissa (projected gain 3.24, hit 0)
- Autosub: Enzo Fernández replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 2.52 | 7.67 | 13.40 | 1.00 | 57.3 | 90.0 |
| Bench 1 | Bench | Karl Hein | GK | 1 | 4.0 | 0.03 | 0.00 | 0.19 | 0.00 | 1.9 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 3.35 | 10.22 | 17.27 | 8.00 | 65.3 | 90.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.28 | 9.12 | 15.01 | 2.00 | 84.6 | 90.0 |
| XI | XI | Neco Williams | DEF | 16 | 4.5 | 2.92 | 8.30 | 13.68 | 5.00 | 84.3 | 90.0 |
| Bench 3 | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 2.50 | 7.68 | 13.18 | 1.00 | 57.5 | 90.0 |
| Bench 4 | Bench | Rayan Aït-Nouri | DEF | 20 | 4.9 | 1.70 | 6.94 | 12.89 | 2.00 | 50.1 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 6.03 | 16.32 | 26.90 | 9.00 | 86.9 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.6 | 4.51 | 13.16 | 21.18 | 7.00 | 84.7 | 90.0 |
| XI | XI | Omar Marmoush | FWD | 13 | 7.6 | 3.22 | 10.62 | 17.66 | 2.00 | 35.7 | 82.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.16 | 21.28 | 35.47 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.0 | 5.83 | 17.09 | 27.40 | 5.00 | 90.0 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.20 | 12.70 | 21.88 | 0.00 | 80.4 | 0.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 3.80 | 10.80 | 18.68 | 1.00 | 66.6 | 55.0 |
| Bench 2 | Autosub In | Enzo Fernández | MID | 6 | 4.7 | 2.95 | 10.03 | 16.56 | 9.00 | 78.3 | 87.0 |