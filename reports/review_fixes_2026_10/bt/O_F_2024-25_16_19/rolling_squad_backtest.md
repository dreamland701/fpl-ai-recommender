# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 259.35
- Total actual points: 232.00
- Average predicted points: 64.84
- Average actual points: 58.00
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW15 are included before the first simulated week.
- League-average scores were not available for this run.

## GW16

- Train rows: 143668
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Cole Palmer
- Vice captain: Bukayo Saka
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 60.64
- Actual score: 47.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.49 | 10.21 | 16.68 | 6.00 | 80.9 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.4 | 2.64 | 8.23 | 13.85 | 2.00 | 79.3 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 3.97 | 11.65 | 19.44 | 6.00 | 83.0 | 62.0 |
| XI | XI | William Saliba | DEF | 1 | 6.1 | 4.07 | 11.52 | 17.86 | 6.00 | 73.8 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 3.91 | 11.38 | 18.75 | 7.00 | 75.9 | 90.0 |
| XI | XI | Milos Kerkez | DEF | 3 | 4.6 | 3.80 | 10.00 | 16.21 | 2.00 | 76.7 | 90.0 |
| Bench 4 | Bench | Daniel Muñoz | DEF | 7 | 4.7 | 2.96 | 9.35 | 15.33 | 1.00 | 78.2 | 90.0 |
| XI | XI | Francisco Evanilson de Lima Barbosa | FWD | 3 | 6.1 | 4.47 | 11.75 | 18.99 | 2.00 | 58.5 | 79.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.5 | 3.85 | 11.70 | 18.89 | 1.00 | 84.6 | 58.0 |
| Bench 3 | Bench | Yoane Wissa | FWD | 4 | 6.2 | 3.38 | 10.51 | 17.67 | 2.00 | 70.6 | 75.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.0 | 7.73 | 22.69 | 37.12 | 3.00 | 104.9 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.2 | 6.09 | 19.58 | 33.89 | 5.00 | 70.9 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 10.5 | 6.46 | 19.16 | 30.78 | 3.00 | 83.7 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.5 | 5.07 | 14.30 | 22.50 | 3.00 | 62.0 | 79.0 |
| Bench 2 | Bench | Enzo Fernández | MID | 6 | 4.9 | 3.68 | 11.47 | 18.73 | 5.00 | 80.1 | 90.0 |

## GW17

- Train rows: 144369
- Bank: 0.00 -> 0.30
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 60.10
- Actual score: 41.00
- Transfer: Yoane Wissa -> João Pedro Junqueira de Jesus (projected gain 1.63, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.66 | 10.83 | 17.70 | 3.00 | 85.0 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.4 | 2.41 | 8.04 | 13.50 | 0.00 | 82.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.07 | 11.98 | 18.79 | 2.00 | 78.4 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.1 | 3.87 | 11.93 | 20.04 | 0.00 | 84.8 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 3.19 | 10.62 | 17.91 | -1.00 | 73.5 | 90.0 |
| Bench 2 | Bench | Milos Kerkez | DEF | 3 | 4.6 | 3.00 | 8.92 | 14.81 | 6.00 | 78.3 | 90.0 |
| Bench 4 | Bench | Daniel Muñoz | DEF | 7 | 4.7 | 2.41 | 8.52 | 14.02 | 0.00 | 75.5 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.9 | 4.28 | 11.37 | 18.30 | 2.00 | 63.7 | 90.0 |
| XI | XI | Francisco Evanilson de Lima Barbosa | FWD | 3 | 6.1 | 3.49 | 10.26 | 16.87 | 2.00 | 60.2 | 70.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.57 | 10.06 | 16.54 | 2.00 | 71.7 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 8.34 | 24.08 | 39.04 | 3.00 | 101.4 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 6.79 | 21.94 | 36.99 | 21.00 | 89.9 | 86.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.30 | 18.83 | 30.94 | 1.00 | 85.6 | 23.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 4.21 | 12.30 | 19.73 | 3.00 | 75.5 | 90.0 |
| Bench 3 | Bench | Justin Kluivert | MID | 3 | 5.5 | 2.87 | 9.57 | 16.24 | 8.00 | 55.4 | 77.0 |

## GW18

- Train rows: 145070
- Bank: 0.30 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 69.26
- Actual score: 61.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.71) beats the best remaining Triple Captain opportunity (11.06).
- Transfer: Milos Kerkez -> Antonee Robinson (projected gain 2.22, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.71) beats the best remaining Triple Captain opportunity (11.06).
- Autosub outfielders: Pedro Porro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 4.04 | 11.19 | 18.26 | 6.00 | 84.3 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.4 | 2.37 | 7.31 | 12.16 | 7.00 | 78.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.3 | 4.72 | 12.60 | 20.08 | 7.00 | 81.5 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.8 | 3.68 | 11.56 | 18.37 | 1.00 | 84.0 | 90.0 |
| Bench 2 | Autosub In | Pedro Porro | DEF | 18 | 5.6 | 3.20 | 10.06 | 17.10 | 1.00 | 80.4 | 9.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.1 | 3.47 | 9.98 | 16.53 | 2.00 | 80.5 | 90.0 |
| Bench 4 | Bench | Daniel Muñoz | DEF | 7 | 4.7 | 1.38 | 5.46 | 9.83 | 6.00 | 40.9 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.9 | 3.65 | 10.44 | 17.05 | 2.00 | 66.5 | 90.0 |
| Bench 3 | Bench | Jamie Vardy | FWD | 11 | 5.6 | 3.08 | 10.16 | 16.77 | 0.00 | 71.2 | 0.0 |
| XI | XI | Francisco Evanilson de Lima Barbosa | FWD | 3 | 6.1 | 3.27 | 9.82 | 16.37 | 1.00 | 58.8 | 28.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.4 | 8.71 | 24.90 | 41.26 | 9.00 | 100.2 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 6.99 | 21.27 | 35.16 | 10.00 | 98.3 | 90.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 10.6 | 5.96 | 16.45 | 27.98 | 0.00 | 65.5 | 0.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.1 | 3.82 | 11.32 | 18.58 | 2.00 | 80.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.5 | 3.53 | 10.98 | 18.52 | 2.00 | 62.2 | 71.0 |

## GW19

- Train rows: 145775
- Bank: 0.20 -> 3.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 69.35
- Actual score: 83.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.11) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Bukayo Saka -> Bryan Mbeumo (projected gain 5.06, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.11) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.72 | 11.16 | 18.40 | 2.00 | 85.6 | 90.0 |
| Bench 1 | Bench Boost | Dean Henderson | GK | 7 | 4.4 | 3.24 | 8.63 | 13.94 | 2.00 | 83.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.3 | 3.85 | 11.88 | 19.65 | 2.00 | 79.6 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.9 | 3.77 | 11.04 | 18.31 | 4.00 | 87.5 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.55 | 10.42 | 17.05 | 6.00 | 73.4 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.7 | 3.21 | 8.52 | 13.91 | 2.00 | 69.6 | 90.0 |
| Bench 3 | Bench Boost | Pedro Porro | DEF | 18 | 5.5 | 2.63 | 8.44 | 14.79 | 4.00 | 50.6 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.8 | 3.43 | 10.34 | 17.51 | 9.00 | 69.5 | 90.0 |
| Bench 2 | Bench Boost | Francisco Evanilson de Lima Barbosa | FWD | 3 | 6.0 | 2.63 | 8.42 | 14.26 | 8.00 | 47.9 | 81.0 |
| Bench 4 | Bench Boost | Jamie Vardy | FWD | 11 | 5.6 | 1.61 | 5.84 | 10.11 | 2.00 | 29.9 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.5 | 9.12 | 24.57 | 40.69 | 16.00 | 107.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.3 | 7.90 | 21.63 | 36.96 | 2.00 | 94.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.6 | 4.04 | 13.27 | 22.12 | 7.00 | 84.9 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.1 | 4.43 | 11.72 | 19.35 | 1.00 | 81.4 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.5 | 3.08 | 9.32 | 15.30 | 0.00 | 62.7 | 0.0 |