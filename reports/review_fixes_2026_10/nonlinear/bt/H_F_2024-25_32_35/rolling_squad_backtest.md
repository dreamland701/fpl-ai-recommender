# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 285.92
- Total actual points: 314.00
- Average predicted points: 71.48
- Average actual points: 78.50
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
- Bank: 100.00 -> 0.40
- Free transfers: 1 -> 2
- Captain: Jacob Murphy
- Vice captain: Daniel Muñoz
- Effective captain: Jacob Murphy
- Chip used: bench_boost
- Predicted score: 97.75
- Actual score: 146.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (18.81) beats the best remaining Bench Boost opportunity (21.54).
- Chip advisory: bench_boost (0.58): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (18.81) beats the best remaining Bench Boost opportunity (21.54).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Nick Pope | GK | 15 | 4.9 | 6.37 | 14.46 | 18.88 | 15.00 | 160.8 | 180.0 |
| Bench 1 | Bench Boost | Jordan Pickford | GK | 8 | 5.1 | 2.94 | 10.11 | 17.78 | 9.00 | 83.5 | 90.0 |
| Vice Captain | XI | Daniel Muñoz | DEF | 7 | 5.2 | 8.40 | 17.32 | 26.67 | -1.00 | 162.1 | 180.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 7.29 | 13.48 | 19.80 | 8.00 | 164.0 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.5 | 4.46 | 12.62 | 22.26 | 9.00 | 83.7 | 90.0 |
| Bench 2 | Bench Boost | William Saliba | DEF | 1 | 6.5 | 4.04 | 11.35 | 19.27 | 2.00 | 86.3 | 90.0 |
| Bench 3 | Bench Boost | Rayan Aït-Nouri | DEF | 20 | 4.8 | 3.64 | 10.10 | 17.76 | 14.00 | 68.7 | 69.0 |
| XI | XI | Omar Marmoush | FWD | 13 | 7.6 | 5.68 | 12.26 | 21.31 | 7.00 | 84.7 | 81.0 |
| Bench 4 | Bench Boost | Yoane Wissa | FWD | 4 | 6.5 | 3.01 | 11.62 | 18.13 | 9.00 | 80.3 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.6 | 4.39 | 10.66 | 17.38 | 13.00 | 54.9 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 7.84 | 24.15 | 41.93 | 6.00 | 81.8 | 84.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 6.63 | 19.79 | 31.49 | 4.00 | 64.6 | 90.0 |
| XI | XI | Ismaïla Sarr | MID | 7 | 5.8 | 8.00 | 18.98 | 28.67 | 7.00 | 161.4 | 165.0 |
| XI | XI | Eberechi Eze | MID | 7 | 6.8 | 8.25 | 17.05 | 26.16 | 6.00 | 153.3 | 135.0 |
| Captain | Captain | Jacob Murphy | MID | 15 | 5.2 | 8.41 | 15.70 | 23.42 | 19.00 | 135.2 | 138.0 |

## GW33

- Train rows: 156471
- Bank: 0.40 -> 0.70
- Free transfers: 2 -> 2
- Captain: Omar Marmoush
- Vice captain: William Saliba
- Effective captain: Omar Marmoush
- Chip used: triple_captain
- Predicted score: 86.24
- Actual score: 61.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (14.17) beats the best remaining Triple Captain opportunity (8.66).
- Chip advisory: triple_captain (0.66): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Virgil van Dijk -> Joško Gvardiol (projected gain 4.94, hit 0)
- Chip used: Triple Captain on Omar Marmoush. Optimizer chose Triple Captain here because the current estimated captain upside (14.17) beats the best remaining Triple Captain opportunity (8.66).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.14 | 10.16 | 18.63 | 1.00 | 85.9 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | 15 | 4.9 | 3.08 | 8.76 | 16.68 | 2.00 | 86.5 | 90.0 |
| Vice Captain | XI | William Saliba | DEF | 1 | 6.5 | 8.24 | 17.51 | 23.43 | 7.00 | 168.9 | 180.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 6.96 | 15.22 | 20.50 | 7.00 | 168.4 | 180.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 5.76 | 14.94 | 23.39 | 6.00 | 160.5 | 180.0 |
| Bench 2 | Bench | Rayan Aït-Nouri | DEF | 20 | 4.8 | 3.13 | 10.75 | 17.91 | 5.00 | 72.3 | 81.0 |
| Bench 3 | Bench | Tino Livramento | DEF | 15 | 4.6 | 2.40 | 7.73 | 14.34 | 0.00 | 79.9 | 90.0 |
| Captain | Captain | Omar Marmoush | FWD | 13 | 7.6 | 9.57 | 20.70 | 25.93 | 4.00 | 154.6 | 180.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.6 | 3.80 | 12.45 | 20.42 | -1.00 | 74.5 | 60.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.27 | 10.84 | 18.83 | 11.00 | 83.7 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 7.69 | 19.91 | 37.25 | 3.00 | 75.7 | 90.0 |
| XI | XI | Ismaïla Sarr | MID | 7 | 5.8 | 7.05 | 14.42 | 23.65 | 3.00 | 160.0 | 117.0 |
| XI | XI | Eberechi Eze | MID | 7 | 6.8 | 6.83 | 12.90 | 21.01 | 10.00 | 153.4 | 107.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 3.77 | 12.75 | 21.39 | 2.00 | 68.4 | 90.0 |
| Bench 4 | Bench | Jacob Murphy | MID | 15 | 5.2 | 2.07 | 7.00 | 16.65 | 2.00 | 62.5 | 64.0 |

## GW34

- Train rows: 157270
- Bank: 0.70 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 49.22
- Actual score: 60.00
- Transfer: William Saliba -> Trent Alexander-Arnold (projected gain 7.22, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Nick Pope | GK | 15 | 4.9 | 3.51 | 11.61 | 19.58 | 6.00 | 87.2 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 5.1 | 2.90 | 11.21 | 19.16 | 4.00 | 89.7 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 4.38 | 14.47 | 18.78 | 5.00 | 69.4 | 75.0 |
| XI | XI | Rayan Aït-Nouri | DEF | 20 | 4.9 | 4.91 | 13.83 | 18.60 | 11.00 | 80.7 | 76.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.53 | 11.53 | 18.54 | 6.00 | 83.8 | 90.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 0.14 | 8.45 | 12.80 | 0.00 | 0.0 | 0.0 |
| Bench 4 | Bench | Joško Gvardiol | DEF | 13 | 6.2 | 0.00 | 8.13 | 11.82 | 0.00 | 2.4 | 0.0 |
| XI | Bench | Omar Marmoush | FWD | 13 | 7.6 | 0.17 | 17.53 | 23.61 | 0.00 | 1.3 | 0.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.54 | 11.29 | 17.12 | 7.00 | 83.4 | 90.0 |
| XI | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.6 | 1.45 | 5.29 | 12.44 | 0.00 | 20.6 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.05 | 21.53 | 33.19 | 8.00 | 83.2 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.6 | 5.78 | 18.59 | 24.68 | 3.00 | 83.2 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 5.71 | 10.63 | 22.75 | 6.00 | 74.1 | 66.0 |
| XI | Bench | Ismaïla Sarr | MID | 7 | 5.8 | 0.14 | 8.03 | 15.66 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Eberechi Eze | MID | 7 | 6.8 | 0.00 | 7.36 | 15.09 | 0.00 | 0.0 | 0.0 |

## GW35

- Train rows: 158070
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Jacob Murphy
- Vice captain: Mohamed Salah
- Effective captain: Jacob Murphy
- Chip used: none
- Predicted score: 52.71
- Actual score: 47.00
- Transfer: Trent Alexander-Arnold -> William Saliba (projected gain 6.86, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 5.1 | 3.66 | 10.97 | 18.55 | 2.00 | 88.7 | 90.0 |
| XI | XI | Nick Pope | GK | 15 | 4.9 | 3.95 | 7.78 | 15.56 | 2.00 | 64.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.6 | 4.46 | 12.95 | 21.01 | 1.00 | 73.9 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.27 | 11.47 | 19.11 | 8.00 | 85.5 | 90.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 4.35 | 11.06 | 17.25 | 2.00 | 83.3 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 3.80 | 10.50 | 15.06 | 1.00 | 71.6 | 90.0 |
| Bench 4 | Bench | Rayan Aït-Nouri | DEF | 20 | 4.9 | 1.31 | 5.37 | 11.53 | 2.00 | 45.0 | 90.0 |
| XI | XI | Omar Marmoush | FWD | 13 | 7.6 | 4.21 | 12.54 | 23.41 | 2.00 | 67.1 | 82.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.88 | 11.18 | 19.39 | 7.00 | 84.5 | 90.0 |
| Bench 2 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 2.28 | 6.33 | 11.39 | 0.00 | 43.3 | 0.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.8 | 5.12 | 20.82 | 36.96 | 2.00 | 80.8 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.5 | 4.35 | 15.62 | 22.54 | 10.00 | 67.1 | 90.0 |
| Captain | Captain | Jacob Murphy | MID | 15 | 5.2 | 5.47 | 12.32 | 14.58 | 1.00 | 65.8 | 55.0 |
| Bench 3 | Bench | Ismaïla Sarr | MID | 7 | 5.7 | 2.24 | 10.98 | 14.06 | 2.00 | 61.3 | 90.0 |
| XI | XI | Eberechi Eze | MID | 7 | 6.8 | 2.38 | 7.37 | 13.97 | 10.00 | 67.8 | 90.0 |