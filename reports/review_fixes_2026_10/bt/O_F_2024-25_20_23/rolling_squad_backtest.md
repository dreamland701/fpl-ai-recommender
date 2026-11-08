# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 278.83
- Total actual points: 233.00
- Average predicted points: 69.71
- Average actual points: 58.25
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW19 are included before the first simulated week.
- League-average scores were not available for this run.

## GW20

- Train rows: 146484
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 66.15
- Actual score: 68.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub outfielders: Dan Burn.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.57 | 10.73 | 17.87 | 3.00 | 83.8 | 90.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 4.8 | 2.98 | 9.00 | 14.75 | 9.00 | 86.5 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.1 | 5.13 | 14.24 | 23.12 | 0.00 | 84.4 | 85.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.9 | 4.40 | 12.02 | 19.70 | 1.00 | 86.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.3 | 3.69 | 11.27 | 18.81 | 2.00 | 78.8 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.7 | 3.91 | 11.21 | 17.97 | 2.00 | 78.8 | 90.0 |
| Bench 2 | Autosub In | Dan Burn | DEF | 15 | 4.4 | 3.24 | 9.32 | 15.08 | 1.00 | 81.4 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.7 | 3.26 | 10.47 | 17.43 | 9.00 | 75.3 | 90.0 |
| Bench 4 | Bench | Jamie Vardy | FWD | 11 | 5.6 | 3.11 | 9.63 | 15.56 | 5.00 | 61.4 | 90.0 |
| Bench 3 | Bench | Raúl Jiménez | FWD | 9 | 5.5 | 3.15 | 8.36 | 13.32 | 13.00 | 55.1 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 10.24 | 28.44 | 46.21 | 7.00 | 113.2 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.21 | 21.32 | 35.56 | 10.00 | 98.5 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.6 | 4.95 | 14.31 | 23.55 | 19.00 | 87.3 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 4.75 | 14.06 | 22.45 | 7.00 | 76.6 | 77.0 |
| XI | Bench | Morgan Rogers | MID | 2 | 5.5 | 4.82 | 12.94 | 20.79 | 0.00 | 84.6 | 0.0 |

## GW21

- Train rows: 147195
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 61.58
- Actual score: 60.00
- Transfer: Morgan Rogers -> Amad Diallo (projected gain 0.33, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.85 | 10.91 | 17.94 | 2.00 | 83.9 | 90.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 4.9 | 2.86 | 9.28 | 15.37 | 3.00 | 85.5 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 3.74 | 12.00 | 19.88 | 2.00 | 74.9 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.06 | 11.68 | 19.12 | 7.00 | 82.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.3 | 3.95 | 10.88 | 17.75 | 2.00 | 81.2 | 90.0 |
| Bench 2 | Bench | Lewis Hall | DEF | 15 | 4.8 | 3.59 | 10.85 | 17.15 | 6.00 | 71.1 | 90.0 |
| Bench 4 | Bench | Dan Burn | DEF | 15 | 4.4 | 2.95 | 8.93 | 14.69 | 6.00 | 79.6 | 90.0 |
| XI | XI | Raúl Jiménez | FWD | 9 | 5.6 | 4.49 | 12.02 | 18.84 | 1.00 | 71.5 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.7 | 4.37 | 11.82 | 19.20 | 1.00 | 79.8 | 77.0 |
| Bench 3 | Bench | Jamie Vardy | FWD | 11 | 5.5 | 3.13 | 9.09 | 14.76 | 2.00 | 64.6 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 8.09 | 24.84 | 41.32 | 2.00 | 102.6 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.03 | 20.96 | 34.89 | 10.00 | 104.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.35 | 15.96 | 25.87 | 2.00 | 97.2 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.4 | 4.63 | 13.93 | 22.71 | 9.00 | 72.9 | 77.0 |
| XI | XI | Amad Diallo | MID | 14 | 5.3 | 3.94 | 11.09 | 18.34 | 20.00 | 73.0 | 90.0 |

## GW22

- Train rows: 147919
- Bank: 0.20 -> 1.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 71.80
- Actual score: 45.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.49) beats the best remaining Triple Captain opportunity (11.22).
- Transfer: William Saliba -> Ola Aina (projected gain 1.00, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.49) beats the best remaining Triple Captain opportunity (11.22).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.6 | 3.59 | 10.44 | 17.29 | 1.00 | 83.8 | 90.0 |
| XI | XI | Matz Sels | GK | 16 | 4.9 | 3.66 | 10.29 | 16.98 | 1.00 | 84.4 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 3.95 | 12.47 | 20.92 | 11.00 | 78.1 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.31 | 12.21 | 20.07 | 8.00 | 86.9 | 90.0 |
| XI | XI | Ola Aina | DEF | 16 | 5.2 | 4.14 | 11.48 | 18.77 | 4.00 | 81.3 | 90.0 |
| Bench 2 | Bench | Lewis Hall | DEF | 15 | 4.9 | 3.60 | 10.61 | 16.88 | 4.00 | 73.3 | 65.0 |
| Bench 4 | Bench | Dan Burn | DEF | 15 | 4.4 | 2.94 | 8.85 | 14.64 | 0.00 | 81.5 | 90.0 |
| XI | XI | Raúl Jiménez | FWD | 9 | 5.7 | 4.24 | 11.07 | 17.78 | 2.00 | 63.9 | 70.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.7 | 3.66 | 10.66 | 17.60 | 2.00 | 70.4 | 90.0 |
| Bench 3 | Bench | Jamie Vardy | FWD | 11 | 5.5 | 3.44 | 9.96 | 15.95 | 2.00 | 70.1 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 8.49 | 25.76 | 42.53 | 3.00 | 98.6 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.60 | 22.66 | 37.29 | 2.00 | 105.7 | 83.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.8 | 5.21 | 15.61 | 26.11 | 2.00 | 93.1 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.6 | 4.91 | 14.84 | 23.80 | 2.00 | 75.4 | 90.0 |
| XI | XI | Amad Diallo | MID | 14 | 5.4 | 4.63 | 13.50 | 21.85 | 2.00 | 91.2 | 90.0 |

## GW23

- Train rows: 148648
- Bank: 1.30 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 79.30
- Actual score: 60.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.53) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Jamie Vardy -> Yoane Wissa (projected gain 0.66, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.53) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.41 | 10.10 | 16.76 | 9.00 | 83.1 | 90.0 |
| Bench 1 | Bench Boost | Matz Sels | GK | 16 | 5.0 | 2.91 | 9.34 | 15.51 | 1.00 | 82.9 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.24 | 14.84 | 24.08 | 5.00 | 85.8 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 4.53 | 12.60 | 20.49 | 2.00 | 87.5 | 90.0 |
| Bench 3 | Bench Boost | Ola Aina | DEF | 16 | 5.3 | 3.75 | 11.39 | 18.57 | 1.00 | 87.5 | 78.0 |
| XI | XI | Lewis Hall | DEF | 15 | 5.0 | 4.11 | 10.92 | 17.36 | 2.00 | 68.8 | 90.0 |
| Bench 4 | Bench Boost | Dan Burn | DEF | 15 | 4.4 | 3.11 | 8.62 | 14.16 | 2.00 | 79.3 | 90.0 |
| XI | XI | Raúl Jiménez | FWD | 9 | 5.7 | 4.15 | 11.67 | 18.90 | 2.00 | 61.9 | 63.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.2 | 4.19 | 11.62 | 19.14 | 2.00 | 80.7 | 90.0 |
| Bench 2 | Bench Boost | João Pedro Junqueira de Jesus | FWD | 5 | 5.6 | 3.76 | 10.99 | 17.91 | 1.00 | 71.7 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 9.08 | 25.59 | 41.93 | 8.00 | 95.7 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 6.47 | 20.22 | 34.15 | 2.00 | 96.8 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.8 | 5.53 | 16.04 | 27.01 | 7.00 | 93.7 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.7 | 5.45 | 15.52 | 25.08 | 5.00 | 79.5 | 87.0 |
| XI | XI | Amad Diallo | MID | 14 | 5.5 | 4.54 | 13.44 | 22.15 | 3.00 | 87.5 | 90.0 |