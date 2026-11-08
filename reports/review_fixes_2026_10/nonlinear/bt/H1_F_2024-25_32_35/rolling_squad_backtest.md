# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 267.92
- Total actual points: 268.00
- Average predicted points: 66.98
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
- Bank: 100.00 -> 0.20
- Free transfers: 1 -> 2
- Captain: Jacob Murphy
- Vice captain: Daniel Muñoz
- Effective captain: Jacob Murphy
- Chip used: triple_captain
- Predicted score: 82.00
- Actual score: 101.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (11.59) beats the best remaining Triple Captain opportunity (15.26).
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Jacob Murphy. Optimizer chose Triple Captain here because the current estimated captain upside (11.59) beats the best remaining Triple Captain opportunity (15.26).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.5 | 3.41 | 11.34 | 18.23 | 2.00 | 88.2 | 90.0 |
| XI | XI | Dean Henderson | GK | 7 | 4.6 | 6.57 | 9.35 | 14.81 | 2.00 | 152.0 | 180.0 |
| Vice Captain | XI | Daniel Muñoz | DEF | 7 | 5.2 | 8.40 | 12.70 | 19.52 | -1.00 | 162.1 | 180.0 |
| Bench 2 | Bench | Joško Gvardiol | DEF | 13 | 6.2 | 3.39 | 12.37 | 19.87 | 1.00 | 86.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.5 | 4.04 | 11.65 | 18.37 | 2.00 | 86.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.5 | 4.46 | 11.06 | 18.18 | 9.00 | 83.7 | 90.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 7.29 | 11.02 | 16.59 | 8.00 | 164.0 | 180.0 |
| Bench 3 | Bench | Yoane Wissa | FWD | 4 | 6.5 | 3.01 | 10.82 | 18.12 | 9.00 | 80.3 | 90.0 |
| XI | XI | Jørgen Strand Larsen | FWD | 20 | 5.4 | 3.48 | 8.80 | 14.28 | 6.00 | 67.5 | 69.0 |
| Bench 4 | Bench | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.9 | 2.08 | 8.10 | 13.63 | 1.00 | 45.6 | 26.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 7.84 | 24.40 | 40.51 | 6.00 | 81.8 | 84.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 6.63 | 14.77 | 25.42 | 4.00 | 64.6 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.6 | 3.95 | 14.49 | 24.93 | 2.00 | 82.3 | 81.0 |
| Captain | Captain | Jacob Murphy | MID | 15 | 5.2 | 8.41 | 13.84 | 20.64 | 19.00 | 135.2 | 138.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 4.11 | 12.65 | 20.20 | 6.00 | 83.7 | 84.0 |

## GW33

- Train rows: 156471
- Bank: 0.20 -> 0.00
- Free transfers: 2 -> 2
- Captain: David Raya Martin
- Vice captain: William Saliba
- Effective captain: David Raya Martin
- Chip used: bench_boost
- Predicted score: 84.35
- Actual score: 77.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (17.58) beats the best remaining Bench Boost opportunity (10.36).
- Chip advisory: bench_boost (0.56): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Transfer: Jørgen Strand Larsen -> João Pedro Junqueira de Jesus (projected gain 1.63, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (17.58) beats the best remaining Bench Boost opportunity (10.36).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Captain | Captain | David Raya Martin | GK | 1 | 5.5 | 8.44 | 13.72 | 21.23 | 7.00 | 177.3 | 180.0 |
| Bench 1 | Bench Boost | Dean Henderson | GK | 7 | 4.6 | 4.49 | 11.80 | 18.23 | 10.00 | 156.2 | 180.0 |
| Vice Captain | XI | William Saliba | DEF | 1 | 6.5 | 8.24 | 15.25 | 23.37 | 7.00 | 168.9 | 180.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 6.96 | 14.81 | 22.93 | 7.00 | 168.4 | 180.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 5.76 | 13.59 | 20.80 | 6.00 | 160.5 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.5 | 4.42 | 12.21 | 19.94 | 7.00 | 84.7 | 90.0 |
| Bench 2 | Bench Boost | Tino Livramento | DEF | 15 | 4.6 | 2.40 | 10.86 | 17.30 | 0.00 | 79.9 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.27 | 11.35 | 18.68 | 11.00 | 83.7 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.6 | 3.80 | 10.92 | 18.11 | -1.00 | 74.5 | 60.0 |
| Bench 4 | Bench Boost | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 1.91 | 6.19 | 10.45 | 1.00 | 41.1 | 27.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 7.69 | 23.28 | 38.67 | 3.00 | 75.7 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 8.05 | 14.85 | 22.85 | 7.00 | 161.1 | 166.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 3.63 | 13.72 | 23.16 | 1.00 | 73.9 | 31.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 3.77 | 13.57 | 23.44 | 2.00 | 68.4 | 90.0 |
| Bench 3 | Bench Boost | Jacob Murphy | MID | 15 | 5.2 | 2.07 | 11.06 | 18.35 | 2.00 | 62.5 | 64.0 |

## GW34

- Train rows: 157270
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 46.95
- Actual score: 46.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martin | GK | 1 | 5.5 | 0.12 | 12.66 | 20.48 | 0.00 | 1.8 | 0.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.6 | 0.00 | 10.59 | 17.62 | 0.00 | 0.9 | 0.0 |
| Bench 2 | Bench | William Saliba | DEF | 1 | 6.5 | 0.13 | 14.10 | 22.65 | 0.00 | 2.8 | 0.0 |
| XI | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 0.14 | 13.36 | 21.91 | 0.00 | 0.0 | 0.0 |
| Bench 4 | Bench | Joško Gvardiol | DEF | 13 | 6.2 | 0.00 | 13.21 | 21.71 | 0.00 | 2.4 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.5 | 4.26 | 13.02 | 20.72 | 2.00 | 86.2 | 90.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.53 | 10.10 | 16.35 | 6.00 | 83.8 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.54 | 12.70 | 20.77 | 7.00 | 83.4 | 90.0 |
| XI | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.6 | 1.45 | 8.57 | 14.89 | 0.00 | 20.6 | 0.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 1.66 | 5.73 | 9.83 | 2.00 | 52.5 | 63.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.05 | 23.11 | 37.30 | 8.00 | 83.2 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.6 | 5.78 | 16.85 | 27.35 | 3.00 | 83.2 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.66 | 13.79 | 23.24 | 4.00 | 78.8 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 5.71 | 13.59 | 22.25 | 6.00 | 74.1 | 66.0 |
| Bench 3 | Bench | Morgan Rogers | MID | 2 | 5.6 | 0.03 | 13.09 | 21.26 | 0.00 | 0.0 | 0.0 |

## GW35

- Train rows: 158070
- Bank: 0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Jacob Murphy
- Vice captain: Mohamed Salah
- Effective captain: Jacob Murphy
- Chip used: none
- Predicted score: 54.62
- Actual score: 44.00
- Transfer: Daniel Muñoz -> Dan Burn (projected gain 3.21, hit 0)
- Autosub: Norberto Bercique Gomes Betuncal replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.56 | 7.49 | 13.15 | 1.00 | 74.5 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.6 | 3.28 | 5.66 | 10.08 | 3.00 | 85.7 | 90.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 12 | 6.6 | 2.53 | 10.36 | 17.56 | 6.00 | 79.5 | 90.0 |
| XI | XI | Dan Burn | DEF | 15 | 4.5 | 4.30 | 10.11 | 16.06 | 2.00 | 82.7 | 90.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 4.35 | 9.63 | 15.55 | 2.00 | 83.3 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.27 | 9.24 | 16.05 | 8.00 | 85.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.5 | 4.46 | 8.76 | 15.44 | 1.00 | 73.9 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.88 | 13.02 | 21.12 | 7.00 | 84.5 | 90.0 |
| Bench 2 | Autosub In | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 3.32 | 6.45 | 10.74 | 6.00 | 54.9 | 76.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 2.28 | 6.26 | 11.26 | 0.00 | 43.3 | 0.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.8 | 5.12 | 22.32 | 36.64 | 2.00 | 80.8 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.5 | 3.74 | 13.40 | 22.50 | 0.00 | 84.2 | 0.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.5 | 4.35 | 12.78 | 21.57 | 10.00 | 67.1 | 90.0 |
| Captain | Captain | Jacob Murphy | MID | 15 | 5.2 | 5.47 | 11.84 | 19.77 | 1.00 | 65.8 | 55.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 4.64 | 8.57 | 15.10 | 3.00 | 71.0 | 90.0 |