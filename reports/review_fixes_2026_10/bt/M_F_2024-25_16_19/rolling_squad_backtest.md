# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 259.49
- Total actual points: 232.00
- Average predicted points: 64.87
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
- Predicted score: 60.60
- Actual score: 47.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.51 | 10.22 | 16.64 | 6.00 | 80.9 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.4 | 2.66 | 8.30 | 14.03 | 2.00 | 79.3 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 3.95 | 11.64 | 19.48 | 6.00 | 83.0 | 62.0 |
| XI | XI | William Saliba | DEF | 1 | 6.1 | 4.08 | 11.56 | 17.63 | 6.00 | 73.8 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 3.89 | 11.37 | 18.82 | 7.00 | 76.0 | 90.0 |
| XI | XI | Milos Kerkez | DEF | 3 | 4.6 | 3.77 | 9.99 | 16.13 | 2.00 | 76.8 | 90.0 |
| Bench 4 | Bench | Daniel Muñoz | DEF | 7 | 4.7 | 2.98 | 9.42 | 15.41 | 1.00 | 78.2 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.5 | 3.83 | 11.72 | 18.81 | 1.00 | 84.6 | 58.0 |
| XI | XI | Francisco Evanilson de Lima Barbosa | FWD | 3 | 6.1 | 4.44 | 11.71 | 18.75 | 2.00 | 58.5 | 79.0 |
| Bench 3 | Bench | Yoane Wissa | FWD | 4 | 6.2 | 3.40 | 10.50 | 17.61 | 2.00 | 70.6 | 75.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.0 | 7.76 | 22.75 | 36.97 | 3.00 | 104.9 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.2 | 6.09 | 19.52 | 33.76 | 5.00 | 70.9 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 10.5 | 6.48 | 19.16 | 30.44 | 3.00 | 83.7 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.5 | 5.04 | 14.39 | 22.05 | 3.00 | 62.0 | 79.0 |
| Bench 2 | Bench | Enzo Fernández | MID | 6 | 4.9 | 3.71 | 11.49 | 18.67 | 5.00 | 80.1 | 90.0 |

## GW17

- Train rows: 144369
- Bank: 0.00 -> 0.30
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 60.12
- Actual score: 41.00
- Transfer: Yoane Wissa -> João Pedro Junqueira de Jesus (projected gain 1.48, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.67 | 10.78 | 17.60 | 3.00 | 85.0 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.4 | 2.44 | 8.08 | 13.60 | 0.00 | 81.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.1 | 4.08 | 11.96 | 18.64 | 2.00 | 78.3 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.1 | 3.90 | 11.92 | 20.01 | 0.00 | 84.8 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 3.18 | 10.66 | 17.99 | -1.00 | 73.5 | 90.0 |
| Bench 2 | Bench | Milos Kerkez | DEF | 3 | 4.6 | 2.99 | 8.88 | 14.78 | 6.00 | 78.3 | 90.0 |
| Bench 4 | Bench | Daniel Muñoz | DEF | 7 | 4.7 | 2.45 | 8.58 | 14.13 | 0.00 | 75.5 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.9 | 4.25 | 11.25 | 17.98 | 2.00 | 63.7 | 90.0 |
| XI | XI | Francisco Evanilson de Lima Barbosa | FWD | 3 | 6.1 | 3.47 | 10.26 | 16.77 | 2.00 | 60.2 | 70.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.5 | 3.54 | 10.03 | 16.53 | 2.00 | 71.8 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.0 | 8.36 | 24.27 | 39.01 | 3.00 | 101.3 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.3 | 6.76 | 22.02 | 36.94 | 21.00 | 90.0 | 86.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.5 | 6.32 | 18.69 | 30.57 | 1.00 | 85.6 | 23.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.9 | 4.22 | 12.32 | 19.66 | 3.00 | 75.5 | 90.0 |
| Bench 3 | Bench | Justin Kluivert | MID | 3 | 5.5 | 2.85 | 9.56 | 16.09 | 8.00 | 55.5 | 77.0 |

## GW18

- Train rows: 145070
- Bank: 0.30 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 69.39
- Actual score: 61.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.72) beats the best remaining Triple Captain opportunity (11.07).
- Transfer: Milos Kerkez -> Antonee Robinson (projected gain 2.15, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.72) beats the best remaining Triple Captain opportunity (11.07).
- Autosub: Pedro Porro replaced Bukayo Saka.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.04 | 11.10 | 18.11 | 6.00 | 84.3 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.4 | 2.40 | 7.25 | 12.09 | 7.00 | 78.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.73 | 12.55 | 19.91 | 7.00 | 81.5 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.8 | 3.70 | 11.47 | 18.34 | 1.00 | 84.0 | 90.0 |
| Bench 2 | Autosub In | Pedro Porro | DEF | 18 | 5.6 | 3.18 | 10.08 | 17.23 | 1.00 | 80.4 | 9.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.1 | 3.48 | 9.98 | 16.50 | 2.00 | 80.5 | 90.0 |
| Bench 4 | Bench | Daniel Muñoz | DEF | 7 | 4.7 | 1.41 | 5.39 | 9.74 | 6.00 | 40.9 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.9 | 3.67 | 10.43 | 17.02 | 2.00 | 66.5 | 90.0 |
| Bench 3 | Bench | Jamie Vardy | FWD | 11 | 5.5 | 3.07 | 10.17 | 16.80 | 0.00 | 71.2 | 0.0 |
| XI | XI | Francisco Evanilson de Lima Barbosa | FWD | 3 | 6.1 | 3.29 | 9.81 | 16.29 | 1.00 | 58.8 | 28.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.3 | 8.72 | 24.89 | 41.10 | 9.00 | 100.1 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 6.99 | 21.29 | 35.12 | 10.00 | 98.3 | 90.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 10.5 | 5.97 | 16.45 | 27.62 | 0.00 | 65.5 | 0.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.83 | 11.33 | 18.61 | 2.00 | 80.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.5 | 3.54 | 10.94 | 18.40 | 2.00 | 62.1 | 71.0 |

## GW19

- Train rows: 145775
- Bank: 0.10 -> 2.90
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 69.38
- Actual score: 83.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.05) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Bukayo Saka -> Bryan Mbeumo (projected gain 5.18, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.05) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.75 | 11.15 | 18.33 | 2.00 | 85.6 | 90.0 |
| Bench 1 | Bench Boost | Dean Henderson | GK | 7 | 4.4 | 3.22 | 8.59 | 13.87 | 2.00 | 83.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 3.87 | 11.76 | 19.33 | 2.00 | 79.5 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.8 | 3.80 | 11.06 | 18.36 | 4.00 | 87.4 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.55 | 10.33 | 16.95 | 6.00 | 73.4 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.7 | 3.19 | 8.50 | 13.87 | 2.00 | 69.6 | 90.0 |
| Bench 3 | Bench Boost | Pedro Porro | DEF | 18 | 5.5 | 2.59 | 8.49 | 15.00 | 4.00 | 50.7 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.8 | 3.46 | 10.35 | 17.41 | 9.00 | 69.5 | 90.0 |
| Bench 2 | Bench Boost | Francisco Evanilson de Lima Barbosa | FWD | 3 | 6.0 | 2.64 | 8.34 | 14.14 | 8.00 | 47.9 | 81.0 |
| Bench 4 | Bench Boost | Jamie Vardy | FWD | 11 | 5.5 | 1.60 | 5.80 | 9.98 | 2.00 | 29.9 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.3 | 9.10 | 25.01 | 40.91 | 16.00 | 107.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 7.92 | 22.13 | 36.86 | 2.00 | 94.3 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.6 | 4.07 | 13.31 | 22.16 | 7.00 | 84.8 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 4.44 | 11.99 | 19.49 | 1.00 | 81.4 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.5 | 3.09 | 9.25 | 15.13 | 0.00 | 62.7 | 0.0 |