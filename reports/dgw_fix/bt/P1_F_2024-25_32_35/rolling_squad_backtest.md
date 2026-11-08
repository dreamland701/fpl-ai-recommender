# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 291.92
- Total actual points: 285.00
- Average predicted points: 72.98
- Average actual points: 71.25
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
- Chip used: triple_captain
- Predicted score: 83.92
- Actual score: 87.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (12.22) beats the best remaining Triple Captain opportunity (15.89).
- Chip advisory: bench_boost (0.58): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.62): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Jacob Murphy. Optimizer chose Triple Captain here because the current estimated captain upside (12.22) beats the best remaining Triple Captain opportunity (15.89).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.91 | 11.34 | 18.23 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 5.1 | 3.45 | 10.11 | 16.45 | 3.00 | 90.0 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 7.57 | 12.70 | 19.52 | -1.00 | 166.5 | 180.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.17 | 12.37 | 19.87 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.5 | 3.86 | 11.65 | 18.37 | 2.00 | 82.7 | 90.0 |
| Bench 2 | Bench | Virgil van Dijk | DEF | 12 | 6.5 | 3.82 | 11.06 | 18.18 | 9.00 | 84.0 | 90.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 6.82 | 11.02 | 16.59 | 8.00 | 155.0 | 180.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 8.19 | 13.83 | 21.29 | 2.00 | 144.0 | 100.0 |
| Bench 3 | Bench | Yoane Wissa | FWD | 4 | 6.5 | 3.16 | 10.82 | 18.12 | 9.00 | 75.1 | 90.0 |
| Bench 4 | Bench | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.9 | 2.45 | 8.10 | 13.63 | 1.00 | 60.9 | 26.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.8 | 8.30 | 24.40 | 40.51 | 6.00 | 90.0 | 84.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.6 | 4.70 | 14.49 | 24.93 | 2.00 | 90.0 | 81.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.0 | 4.46 | 14.13 | 23.74 | 2.00 | 89.7 | 90.0 |
| Captain | Captain | Jacob Murphy | MID | 15 | 5.2 | 9.04 | 13.84 | 20.64 | 19.00 | 161.6 | 138.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 4.82 | 12.65 | 20.20 | 6.00 | 88.2 | 84.0 |

## GW33

- Train rows: 156471
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: William Saliba
- Vice captain: Joško Gvardiol
- Effective captain: William Saliba
- Chip used: bench_boost
- Predicted score: 105.40
- Actual score: 104.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (23.20) beats the best remaining Bench Boost opportunity (14.76).
- Chip advisory: bench_boost (0.70): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Transfer: Matz Sels -> Dean Henderson (projected gain 0.20, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (23.20) beats the best remaining Bench Boost opportunity (14.76).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 8.90 | 13.72 | 21.23 | 7.00 | 180.0 | 180.0 |
| Bench 1 | Bench Boost | Dean Henderson | GK | 7 | 4.6 | 7.25 | 11.80 | 18.23 | 10.00 | 180.0 | 180.0 |
| Captain | Captain | William Saliba | DEF | 1 | 6.5 | 10.05 | 15.25 | 23.37 | 7.00 | 180.0 | 180.0 |
| Vice Captain | XI | Joško Gvardiol | DEF | 13 | 6.2 | 9.20 | 14.81 | 22.93 | 7.00 | 180.0 | 180.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 8.42 | 13.59 | 20.80 | 6.00 | 180.0 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.5 | 4.51 | 12.21 | 19.94 | 7.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Tino Livramento | DEF | 15 | 4.6 | 3.51 | 10.86 | 17.30 | 0.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 7.84 | 13.30 | 20.41 | 10.00 | 147.6 | 84.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.02 | 11.35 | 18.68 | 11.00 | 78.6 | 90.0 |
| Bench 4 | Bench Boost | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 1.88 | 6.19 | 10.45 | 1.00 | 47.3 | 27.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 8.32 | 23.28 | 38.67 | 3.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 8.90 | 14.85 | 22.85 | 7.00 | 180.0 | 166.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.40 | 13.72 | 23.16 | 1.00 | 81.7 | 31.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 4.74 | 13.58 | 22.69 | 18.00 | 83.4 | 90.0 |
| Bench 3 | Bench Boost | Jacob Murphy | MID | 15 | 5.2 | 3.41 | 11.06 | 18.35 | 2.00 | 72.7 | 64.0 |

## GW34

- Train rows: 157270
- Bank: 0.50 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 50.19
- Actual score: 50.00
- Transfer: Tino Livramento -> Rayan Aït-Nouri (projected gain 5.98, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martin | GK | 1 | 5.5 | 0.00 | 12.66 | 20.48 | 0.00 | 0.0 | 0.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.6 | 0.00 | 10.59 | 17.62 | 0.00 | 0.0 | 0.0 |
| XI | XI | Rayan Aït-Nouri | DEF | 20 | 5.0 | 6.03 | 16.08 | 24.40 | 11.00 | 90.0 | 76.0 |
| Bench 3 | Bench | William Saliba | DEF | 1 | 6.5 | 0.00 | 14.10 | 22.65 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 0.00 | 13.36 | 21.91 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Joško Gvardiol | DEF | 13 | 6.2 | 0.00 | 13.21 | 21.71 | 0.00 | 0.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.5 | 4.76 | 13.02 | 20.72 | 2.00 | 90.0 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.23 | 12.70 | 20.77 | 7.00 | 88.3 | 90.0 |
| Bench 4 | Bench | Jean-Philippe Mateta | FWD | 7 | 7.8 | 0.00 | 11.27 | 19.26 | 0.00 | 0.0 | 0.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 1.71 | 5.73 | 9.83 | 2.00 | 47.6 | 63.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.47 | 23.11 | 37.30 | 8.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.0 | 7.01 | 20.70 | 32.76 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.41 | 13.79 | 23.24 | 4.00 | 75.6 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 5.11 | 13.59 | 22.25 | 6.00 | 79.0 | 66.0 |
| XI | Bench | Morgan Rogers | MID | 2 | 5.6 | 0.00 | 13.09 | 21.26 | 0.00 | 0.0 | 0.0 |

## GW35

- Train rows: 158070
- Bank: 0.10 -> 0.80
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 52.41
- Actual score: 44.00
- Transfer: Jean-Philippe Mateta -> Chris Wood (projected gain 3.87, hit 0)
- Autosub: Norberto Bercique Gomes Betuncal replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 2.51 | 7.49 | 13.15 | 1.00 | 57.2 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.6 | 1.67 | 5.66 | 10.08 | 3.00 | 64.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.6 | 3.31 | 10.36 | 17.56 | 6.00 | 79.7 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 3.04 | 9.24 | 16.05 | 8.00 | 67.3 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.5 | 2.93 | 8.76 | 15.44 | 1.00 | 59.3 | 90.0 |
| Bench 4 | Bench | Rayan Aït-Nouri | DEF | 20 | 5.0 | 1.80 | 7.36 | 13.14 | 2.00 | 47.7 | 90.0 |
| Bench 3 | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 2.16 | 6.90 | 12.25 | 1.00 | 59.0 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.56 | 13.02 | 21.12 | 7.00 | 85.1 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.0 | 3.48 | 10.24 | 16.38 | 2.00 | 66.4 | 90.0 |
| Bench 2 | Autosub In | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 2.42 | 6.45 | 10.74 | 6.00 | 53.9 | 76.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.59 | 22.32 | 36.64 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.0 | 6.05 | 17.65 | 28.26 | 5.00 | 90.0 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.43 | 13.40 | 22.50 | 0.00 | 77.4 | 0.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 4.15 | 11.84 | 19.77 | 1.00 | 63.2 | 55.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 2.78 | 8.57 | 15.10 | 3.00 | 47.7 | 90.0 |