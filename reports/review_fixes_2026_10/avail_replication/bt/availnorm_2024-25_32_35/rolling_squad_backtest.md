# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 251.16
- Total actual points: 235.00
- Average predicted points: 62.79
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
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 74.51
- Actual score: 85.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (18.94) beats the best remaining Bench Boost opportunity (19.78).
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (18.94) beats the best remaining Bench Boost opportunity (19.78).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Dean Henderson | GK | 7 | 4.6 | 4.24 | 10.33 | 16.30 | 2.00 | 102.2 | 180.0 |
| Bench 1 | Bench Boost | David Raya Martin | GK | 1 | 5.5 | 3.45 | 9.95 | 16.00 | 2.00 | 93.6 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 5.59 | 13.96 | 21.44 | -1.00 | 111.1 | 180.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 5.34 | 12.30 | 18.47 | 8.00 | 106.8 | 180.0 |
| Bench 2 | Bench Boost | Joško Gvardiol | DEF | 13 | 6.2 | 3.70 | 10.83 | 17.42 | 1.00 | 97.0 | 90.0 |
| XI | XI | Fabian Schär | DEF | 15 | 5.5 | 4.62 | 10.57 | 16.18 | 16.00 | 101.8 | 180.0 |
| XI | XI | Dan Burn | DEF | 15 | 4.5 | 4.59 | 10.55 | 15.80 | 7.00 | 101.8 | 180.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.6 | 3.44 | 9.41 | 15.96 | 13.00 | 46.0 | 90.0 |
| Bench 3 | Bench Boost | Francisco Evanilson de Lima Barbosa | FWD | 3 | 5.8 | 3.43 | 9.31 | 14.94 | 2.00 | 64.2 | 90.0 |
| Bench 4 | Bench Boost | Rodrigo Muniz Carvalho | FWD | 9 | 5.5 | 3.17 | 8.91 | 14.79 | 1.00 | 53.9 | 56.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.13 | 21.40 | 35.61 | 6.00 | 108.3 | 84.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.7 | 5.60 | 16.31 | 28.03 | 4.00 | 63.8 | 90.0 |
| XI | XI | Ismaïla Sarr | MID | 7 | 5.8 | 4.87 | 13.91 | 22.04 | 7.00 | 89.2 | 165.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.6 | 4.07 | 12.73 | 22.05 | 2.00 | 91.5 | 81.0 |
| XI | XI | Luis Díaz | MID | 12 | 7.5 | 4.14 | 12.55 | 21.17 | 9.00 | 60.9 | 90.0 |

## GW33

- Train rows: 156471
- Bank: 0.60 -> 0.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Joško Gvardiol
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 69.66
- Actual score: 43.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (11.90) beats the best remaining Triple Captain opportunity (8.15).
- Transfer: Fabian Schär -> Jurriën Timber (projected gain 1.48, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (11.90) beats the best remaining Triple Captain opportunity (8.15).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 6.10 | 14.53 | 22.46 | 7.00 | 128.8 | 180.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.6 | 4.46 | 11.32 | 17.52 | 10.00 | 142.4 | 180.0 |
| Vice Captain | XI | Joško Gvardiol | DEF | 13 | 6.2 | 6.41 | 15.62 | 24.16 | 7.00 | 130.3 | 180.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 5.14 | 13.22 | 20.24 | 6.00 | 137.4 | 180.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 5.7 | 4.96 | 11.47 | 17.85 | 4.00 | 79.7 | 90.0 |
| Bench 2 | Bench | Tino Livramento | DEF | 15 | 4.6 | 3.03 | 9.37 | 15.04 | 0.00 | 101.3 | 90.0 |
| Bench 3 | Bench | Dan Burn | DEF | 15 | 4.5 | 3.01 | 9.09 | 14.63 | -2.00 | 106.8 | 90.0 |
| XI | XI | Francisco Evanilson de Lima Barbosa | FWD | 3 | 5.8 | 3.57 | 10.45 | 16.22 | 2.00 | 60.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.6 | 3.39 | 10.18 | 16.94 | -1.00 | 68.0 | 60.0 |
| Bench 4 | Bench | Rodrigo Muniz Carvalho | FWD | 9 | 5.5 | 2.97 | 8.49 | 13.66 | 0.00 | 52.4 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.30 | 20.71 | 34.54 | 3.00 | 105.9 | 90.0 |
| XI | XI | Ismaïla Sarr | MID | 7 | 5.8 | 5.40 | 13.81 | 21.58 | 3.00 | 129.8 | 117.0 |
| XI | XI | Luis Díaz | MID | 12 | 7.5 | 4.98 | 13.12 | 21.72 | 3.00 | 78.5 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 3.88 | 12.81 | 22.21 | 2.00 | 64.3 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 3.91 | 12.66 | 21.46 | 1.00 | 80.0 | 31.0 |

## GW34

- Train rows: 157270
- Bank: 0.40 -> 1.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Rayan Aït-Nouri
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 62.93
- Actual score: 62.00
- Transfer: Jurriën Timber -> Rayan Aït-Nouri (projected gain 7.02, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martin | GK | 1 | 5.5 | 3.04 | 9.27 | 15.19 | 0.00 | 101.2 | 0.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.6 | 2.48 | 7.61 | 12.87 | 0.00 | 108.1 | 0.0 |
| Vice Captain | XI | Rayan Aït-Nouri | DEF | 20 | 5.0 | 6.81 | 16.60 | 25.21 | 11.00 | 114.2 | 76.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.86 | 10.09 | 16.34 | 6.00 | 86.6 | 90.0 |
| Bench 2 | Bench | Joško Gvardiol | DEF | 13 | 6.2 | 3.11 | 9.71 | 16.17 | 0.00 | 100.8 | 0.0 |
| XI | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 3.27 | 9.60 | 15.99 | 0.00 | 110.9 | 0.0 |
| XI | XI | Dan Burn | DEF | 15 | 4.5 | 3.18 | 8.58 | 13.98 | 13.00 | 81.8 | 90.0 |
| XI | XI | Francisco Evanilson de Lima Barbosa | FWD | 3 | 5.8 | 4.10 | 11.31 | 17.94 | 2.00 | 69.1 | 69.0 |
| XI | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.6 | 3.40 | 9.87 | 16.97 | 0.00 | 49.9 | 0.0 |
| Bench 4 | Bench | Rodrigo Muniz Carvalho | FWD | 9 | 5.5 | 1.95 | 5.36 | 8.94 | 0.00 | 26.3 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.54 | 23.09 | 37.27 | 8.00 | 113.7 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 6.63 | 18.17 | 29.56 | 3.00 | 97.9 | 90.0 |
| XI | XI | Luis Díaz | MID | 12 | 7.5 | 6.59 | 17.28 | 27.08 | 7.00 | 102.1 | 75.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.98 | 15.37 | 25.87 | 4.00 | 77.4 | 90.0 |
| Bench 3 | Bench | Ismaïla Sarr | MID | 7 | 5.8 | 2.58 | 7.70 | 13.28 | 0.00 | 83.0 | 0.0 |

## GW35

- Train rows: 158070
- Bank: 1.10 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Yoane Wissa
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 44.06
- Actual score: 45.00
- Transfer: Rodrigo Muniz Carvalho -> Yoane Wissa (projected gain 5.11, hit 0)
- Autosub: Ismaïla Sarr replaced Bruno Borges Fernandes.
- Autosub: Daniel Muñoz replaced Luis Díaz.
- Autosub: Rayan Aït-Nouri replaced João Pedro Junqueira de Jesus.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 2.45 | 7.51 | 13.19 | 1.00 | 57.4 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.6 | 1.62 | 5.56 | 9.91 | 3.00 | 64.4 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 2.99 | 9.11 | 15.84 | 8.00 | 67.9 | 90.0 |
| XI | XI | Dan Burn | DEF | 15 | 4.5 | 3.24 | 8.86 | 14.12 | 2.00 | 88.4 | 90.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.19 | 8.40 | 13.62 | 2.00 | 82.8 | 90.0 |
| Bench 3 | Autosub In | Daniel Muñoz | DEF | 7 | 5.2 | 1.91 | 6.60 | 11.77 | 1.00 | 56.6 | 90.0 |
| Bench 4 | Autosub In | Rayan Aït-Nouri | DEF | 20 | 5.0 | -0.09 | 3.36 | 7.14 | 2.00 | 40.6 | 90.0 |
| Vice Captain | XI | Yoane Wissa | FWD | 4 | 6.6 | 4.10 | 11.76 | 19.11 | 7.00 | 85.1 | 90.0 |
| XI | XI | Francisco Evanilson de Lima Barbosa | FWD | 3 | 5.8 | 2.06 | 8.50 | 14.47 | 6.00 | 51.6 | 86.0 |
| XI | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 2.41 | 7.77 | 13.89 | 0.00 | 35.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 6.64 | 19.82 | 32.68 | 2.00 | 105.2 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.05 | 12.49 | 21.03 | 0.00 | 76.9 | 0.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.5 | 3.60 | 12.02 | 20.38 | 10.00 | 67.0 | 90.0 |
| XI | Bench | Luis Díaz | MID | 12 | 7.5 | 2.69 | 10.31 | 17.65 | 0.00 | 55.2 | 0.0 |
| Bench 2 | Autosub In | Ismaïla Sarr | MID | 7 | 5.7 | 2.00 | 6.92 | 12.25 | 2.00 | 44.9 | 90.0 |