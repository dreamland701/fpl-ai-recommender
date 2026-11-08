# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 276.84
- Total actual points: 235.00
- Average predicted points: 69.21
- Average actual points: 58.75
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
- Bank: 100.00 -> 0.60
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Daniel Muñoz
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 85.29
- Actual score: 85.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (21.01) beats the best remaining Bench Boost opportunity (21.80).
- Chip advisory: bench_boost (0.63): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (21.01) beats the best remaining Bench Boost opportunity (21.80).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Dean Henderson | GK | 7 | 4.6 | 4.85 | 11.82 | 18.73 | 2.00 | 101.2 | 180.0 |
| Bench 1 | Bench Boost | David Raya Martin | GK | 1 | 5.5 | 3.93 | 11.34 | 18.23 | 2.00 | 94.6 | 90.0 |
| Vice Captain | XI | Daniel Muñoz | DEF | 7 | 5.2 | 6.33 | 15.79 | 24.26 | -1.00 | 99.1 | 180.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 6.10 | 14.00 | 21.07 | 8.00 | 105.8 | 180.0 |
| Bench 2 | Bench Boost | Joško Gvardiol | DEF | 13 | 6.2 | 4.23 | 12.37 | 19.87 | 1.00 | 97.0 | 90.0 |
| XI | XI | Dan Burn | DEF | 15 | 4.5 | 5.27 | 12.09 | 18.13 | 7.00 | 100.8 | 180.0 |
| XI | XI | Fabian Schär | DEF | 15 | 5.5 | 5.28 | 12.08 | 18.59 | 16.00 | 100.8 | 180.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.6 | 4.04 | 10.98 | 18.69 | 13.00 | 60.0 | 90.0 |
| Bench 3 | Bench Boost | Francisco Evanilson de Lima Barbosa | FWD | 3 | 5.8 | 4.00 | 10.82 | 17.28 | 2.00 | 70.2 | 90.0 |
| Bench 4 | Bench Boost | Rodrigo Muniz Carvalho | FWD | 9 | 5.5 | 3.67 | 10.38 | 17.34 | 1.00 | 66.9 | 56.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.16 | 24.40 | 40.51 | 6.00 | 107.3 | 84.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 6.26 | 18.10 | 31.16 | 4.00 | 77.8 | 90.0 |
| XI | XI | Ismaïla Sarr | MID | 7 | 5.8 | 5.59 | 16.11 | 25.61 | 7.00 | 109.2 | 165.0 |
| XI | XI | Luis Díaz | MID | 12 | 7.5 | 4.79 | 14.50 | 24.48 | 9.00 | 70.9 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.6 | 4.66 | 14.49 | 24.93 | 2.00 | 92.5 | 81.0 |

## GW33

- Train rows: 156471
- Bank: 0.60 -> 0.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Joško Gvardiol
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 78.92
- Actual score: 43.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (12.80) beats the best remaining Triple Captain opportunity (9.32).
- Transfer: Fabian Schär -> Jurriën Timber (projected gain 2.33, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (12.80) beats the best remaining Triple Captain opportunity (9.32).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 6.82 | 16.21 | 25.09 | 7.00 | 116.8 | 180.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.6 | 5.06 | 12.85 | 19.85 | 10.00 | 130.4 | 180.0 |
| Vice Captain | XI | Joško Gvardiol | DEF | 13 | 6.2 | 7.17 | 17.47 | 27.05 | 7.00 | 129.3 | 180.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 5.84 | 15.02 | 22.98 | 6.00 | 126.4 | 180.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 5.7 | 5.78 | 13.44 | 21.13 | 4.00 | 78.7 | 90.0 |
| Bench 2 | Bench | Tino Livramento | DEF | 15 | 4.6 | 3.55 | 10.86 | 17.30 | 0.00 | 89.3 | 90.0 |
| Bench 3 | Bench | Dan Burn | DEF | 15 | 4.5 | 3.50 | 10.48 | 16.76 | -2.00 | 95.8 | 90.0 |
| XI | XI | Francisco Evanilson de Lima Barbosa | FWD | 3 | 5.8 | 4.09 | 11.97 | 18.57 | 2.00 | 67.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.6 | 3.91 | 11.65 | 19.31 | -1.00 | 67.0 | 60.0 |
| Bench 4 | Bench | Rodrigo Muniz Carvalho | FWD | 9 | 5.5 | 3.33 | 9.68 | 15.74 | 0.00 | 39.4 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.20 | 23.28 | 38.67 | 3.00 | 104.9 | 90.0 |
| XI | XI | Ismaïla Sarr | MID | 7 | 5.8 | 6.14 | 15.69 | 24.51 | 3.00 | 117.8 | 117.0 |
| XI | XI | Luis Díaz | MID | 12 | 7.5 | 5.63 | 14.85 | 24.50 | 3.00 | 77.5 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 4.48 | 14.71 | 25.41 | 2.00 | 44.3 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.46 | 14.34 | 24.21 | 1.00 | 60.0 | 31.0 |

## GW34

- Train rows: 157270
- Bank: 0.40 -> 1.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Rayan Aït-Nouri
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 62.29
- Actual score: 62.00
- Transfer: Jurriën Timber -> Rayan Aït-Nouri (projected gain 6.29, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martin | GK | 1 | 5.5 | 3.01 | 9.50 | 15.36 | 0.00 | 81.2 | 0.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.6 | 2.49 | 7.94 | 13.22 | 0.00 | 88.1 | 0.0 |
| Vice Captain | XI | Rayan Aït-Nouri | DEF | 20 | 5.0 | 6.61 | 16.08 | 24.40 | 11.00 | 94.2 | 76.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.90 | 10.20 | 16.52 | 6.00 | 87.6 | 90.0 |
| XI | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 3.31 | 10.02 | 16.43 | 0.00 | 90.9 | 0.0 |
| Bench 2 | Bench | Joško Gvardiol | DEF | 13 | 6.2 | 3.06 | 9.91 | 16.28 | 0.00 | 80.8 | 0.0 |
| XI | XI | Dan Burn | DEF | 15 | 4.5 | 3.22 | 8.69 | 14.16 | 13.00 | 82.8 | 90.0 |
| XI | XI | Francisco Evanilson de Lima Barbosa | FWD | 3 | 5.8 | 4.16 | 11.52 | 18.34 | 2.00 | 76.1 | 69.0 |
| XI | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.6 | 3.43 | 10.12 | 17.57 | 0.00 | 58.9 | 0.0 |
| Bench 4 | Bench | Rodrigo Muniz Carvalho | FWD | 9 | 5.5 | 1.95 | 5.36 | 8.94 | 0.00 | 26.3 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.55 | 23.11 | 37.30 | 8.00 | 111.7 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 6.17 | 16.85 | 27.35 | 3.00 | 105.9 | 90.0 |
| XI | XI | Luis Díaz | MID | 12 | 7.5 | 6.37 | 16.68 | 26.15 | 7.00 | 101.1 | 75.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 5.01 | 15.40 | 25.94 | 4.00 | 86.4 | 90.0 |
| Bench 3 | Bench | Ismaïla Sarr | MID | 7 | 5.8 | 2.68 | 8.43 | 14.05 | 0.00 | 63.0 | 0.0 |

## GW35

- Train rows: 158070
- Bank: 1.10 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Yoane Wissa
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 50.34
- Actual score: 45.00
- Transfer: Rodrigo Muniz Carvalho -> Yoane Wissa (projected gain 5.23, hit 0)
- Autosub: Ismaïla Sarr replaced Bruno Borges Fernandes.
- Autosub: Daniel Muñoz replaced Luis Díaz.
- Autosub: Rayan Aït-Nouri replaced João Pedro Junqueira de Jesus.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 2.83 | 8.66 | 15.21 | 1.00 | 66.4 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.6 | 1.86 | 6.38 | 11.35 | 3.00 | 72.4 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 3.39 | 10.34 | 17.96 | 8.00 | 75.9 | 90.0 |
| XI | XI | Dan Burn | DEF | 15 | 4.5 | 3.69 | 10.11 | 16.06 | 2.00 | 87.4 | 90.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.64 | 9.63 | 15.55 | 2.00 | 83.8 | 90.0 |
| Bench 3 | Autosub In | Daniel Muñoz | DEF | 7 | 5.2 | 2.26 | 7.78 | 13.80 | 1.00 | 63.6 | 90.0 |
| Bench 4 | Autosub In | Rayan Aït-Nouri | DEF | 20 | 5.0 | 0.89 | 4.41 | 7.88 | 2.00 | 20.6 | 90.0 |
| Vice Captain | XI | Yoane Wissa | FWD | 4 | 6.6 | 4.66 | 13.30 | 21.57 | 7.00 | 87.1 | 90.0 |
| XI | XI | Francisco Evanilson de Lima Barbosa | FWD | 3 | 5.8 | 2.38 | 9.89 | 16.87 | 6.00 | 34.6 | 86.0 |
| XI | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 2.68 | 8.76 | 15.77 | 0.00 | 24.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.52 | 22.32 | 36.64 | 2.00 | 104.2 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.61 | 14.18 | 23.81 | 0.00 | 75.9 | 0.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.5 | 4.17 | 13.81 | 23.31 | 10.00 | 72.0 | 90.0 |
| XI | Bench | Luis Díaz | MID | 12 | 7.5 | 3.25 | 12.19 | 20.70 | 0.00 | 60.2 | 0.0 |
| Bench 2 | Autosub In | Ismaïla Sarr | MID | 7 | 5.7 | 2.33 | 8.15 | 14.50 | 2.00 | 55.9 | 90.0 |