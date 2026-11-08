# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 278.63
- Total actual points: 233.00
- Average predicted points: 69.66
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
- Autosub: Dan Burn replaced Morgan Rogers.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.59 | 10.72 | 17.75 | 3.00 | 83.7 | 90.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 4.8 | 2.95 | 8.99 | 14.70 | 9.00 | 86.6 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.1 | 5.12 | 14.14 | 22.91 | 0.00 | 84.4 | 85.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.9 | 4.41 | 12.09 | 19.89 | 1.00 | 86.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.3 | 3.71 | 11.26 | 18.55 | 2.00 | 78.8 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.7 | 3.88 | 11.14 | 17.83 | 2.00 | 78.8 | 90.0 |
| Bench 2 | Autosub In | Dan Burn | DEF | 15 | 4.4 | 3.21 | 9.24 | 14.92 | 1.00 | 81.5 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.7 | 3.29 | 10.46 | 17.35 | 9.00 | 75.2 | 90.0 |
| Bench 4 | Bench | Jamie Vardy | FWD | 11 | 5.6 | 3.15 | 9.72 | 15.76 | 5.00 | 61.3 | 90.0 |
| Bench 3 | Bench | Raúl Jiménez | FWD | 9 | 5.5 | 3.16 | 8.31 | 13.23 | 13.00 | 55.1 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 10.23 | 28.40 | 46.24 | 7.00 | 113.2 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.23 | 21.38 | 35.58 | 10.00 | 98.5 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.6 | 4.93 | 14.28 | 23.49 | 19.00 | 87.4 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 4.72 | 13.96 | 22.22 | 7.00 | 76.7 | 77.0 |
| XI | Bench | Morgan Rogers | MID | 2 | 5.5 | 4.82 | 12.94 | 20.80 | 0.00 | 84.5 | 0.0 |

## GW21

- Train rows: 147195
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 61.35
- Actual score: 60.00
- Transfer: Morgan Rogers -> Amad Diallo (projected gain 0.39, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.82 | 10.89 | 17.87 | 2.00 | 83.9 | 90.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 4.8 | 2.85 | 9.27 | 15.27 | 3.00 | 85.5 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.1 | 3.71 | 11.98 | 19.87 | 2.00 | 75.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.9 | 4.03 | 11.64 | 19.19 | 7.00 | 82.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.3 | 3.92 | 10.86 | 17.66 | 2.00 | 81.3 | 90.0 |
| Bench 2 | Bench | Lewis Hall | DEF | 15 | 4.7 | 3.55 | 10.73 | 16.88 | 6.00 | 71.1 | 90.0 |
| Bench 4 | Bench | Dan Burn | DEF | 15 | 4.4 | 2.91 | 8.86 | 14.46 | 6.00 | 79.6 | 90.0 |
| XI | XI | Raúl Jiménez | FWD | 9 | 5.5 | 4.46 | 12.03 | 18.50 | 1.00 | 71.6 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.7 | 4.37 | 11.80 | 19.27 | 1.00 | 79.8 | 77.0 |
| Bench 3 | Bench | Jamie Vardy | FWD | 11 | 5.5 | 3.14 | 9.04 | 14.72 | 2.00 | 64.6 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 8.06 | 24.76 | 41.18 | 2.00 | 102.7 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.06 | 20.96 | 34.94 | 10.00 | 104.5 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.6 | 5.34 | 15.89 | 25.89 | 2.00 | 97.2 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 4.59 | 13.88 | 22.55 | 9.00 | 73.0 | 77.0 |
| XI | XI | Amad Diallo | MID | 14 | 5.3 | 3.92 | 11.03 | 18.37 | 20.00 | 73.1 | 90.0 |

## GW22

- Train rows: 147919
- Bank: 0.20 -> 1.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 71.84
- Actual score: 45.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.52) beats the best remaining Triple Captain opportunity (11.25).
- Transfer: William Saliba -> Ola Aina (projected gain 0.99, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.52) beats the best remaining Triple Captain opportunity (11.25).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.6 | 3.63 | 10.47 | 17.30 | 1.00 | 83.8 | 90.0 |
| XI | XI | Matz Sels | GK | 16 | 4.8 | 3.64 | 10.28 | 16.88 | 1.00 | 84.5 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.1 | 3.98 | 12.49 | 20.99 | 11.00 | 78.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.9 | 4.31 | 12.17 | 19.95 | 8.00 | 86.8 | 90.0 |
| XI | XI | Ola Aina | DEF | 16 | 5.2 | 4.12 | 11.46 | 18.68 | 4.00 | 81.4 | 90.0 |
| Bench 2 | Bench | Lewis Hall | DEF | 15 | 4.8 | 3.63 | 10.63 | 16.78 | 4.00 | 73.2 | 65.0 |
| Bench 4 | Bench | Dan Burn | DEF | 15 | 4.4 | 2.97 | 8.90 | 14.63 | 0.00 | 81.4 | 90.0 |
| XI | XI | Raúl Jiménez | FWD | 9 | 5.6 | 4.24 | 11.06 | 17.55 | 2.00 | 63.9 | 70.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.7 | 3.64 | 10.63 | 17.51 | 2.00 | 70.4 | 90.0 |
| Bench 3 | Bench | Jamie Vardy | FWD | 11 | 5.5 | 3.44 | 10.01 | 15.74 | 2.00 | 70.1 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 8.52 | 25.82 | 42.11 | 3.00 | 98.5 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.57 | 22.69 | 37.06 | 2.00 | 105.8 | 83.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.20 | 15.61 | 26.01 | 2.00 | 93.1 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.4 | 4.93 | 14.86 | 23.48 | 2.00 | 75.3 | 90.0 |
| XI | XI | Amad Diallo | MID | 14 | 5.3 | 4.65 | 13.57 | 21.80 | 2.00 | 91.2 | 90.0 |

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
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.58) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Jamie Vardy -> Yoane Wissa (projected gain 0.28, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.58) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.37 | 10.04 | 16.65 | 9.00 | 83.2 | 90.0 |
| Bench 1 | Bench Boost | Matz Sels | GK | 16 | 4.9 | 2.93 | 9.35 | 15.45 | 1.00 | 82.8 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.1 | 5.24 | 14.79 | 23.97 | 5.00 | 85.8 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.51 | 12.52 | 20.43 | 2.00 | 87.5 | 90.0 |
| Bench 2 | Bench Boost | Ola Aina | DEF | 16 | 5.2 | 3.78 | 11.40 | 18.53 | 1.00 | 87.5 | 78.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.09 | 10.84 | 17.18 | 2.00 | 68.9 | 90.0 |
| Bench 4 | Bench Boost | Dan Burn | DEF | 15 | 4.4 | 3.09 | 8.56 | 14.03 | 2.00 | 79.3 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.2 | 4.20 | 11.64 | 18.95 | 2.00 | 80.7 | 90.0 |
| XI | XI | Raúl Jiménez | FWD | 9 | 5.6 | 4.14 | 11.61 | 18.62 | 2.00 | 61.9 | 63.0 |
| Bench 3 | Bench Boost | João Pedro Junqueira de Jesus | FWD | 5 | 5.6 | 3.78 | 10.97 | 17.91 | 1.00 | 71.7 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.09 | 25.36 | 41.64 | 8.00 | 95.7 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 6.46 | 20.21 | 33.94 | 2.00 | 96.8 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.55 | 16.09 | 26.92 | 7.00 | 93.7 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.43 | 15.44 | 24.88 | 5.00 | 79.5 | 87.0 |
| XI | XI | Amad Diallo | MID | 14 | 5.4 | 4.55 | 13.49 | 22.02 | 3.00 | 87.5 | 90.0 |