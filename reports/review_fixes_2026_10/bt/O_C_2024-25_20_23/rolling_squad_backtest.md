# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 277.75
- Total actual points: 244.00
- Average predicted points: 69.44
- Average actual points: 61.00
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
- Predicted score: 64.72
- Actual score: 71.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub outfielders: Jacob Murphy, João Pedro Junqueira de Jesus.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.80 | 11.32 | 18.82 | 3.00 | 87.1 | 90.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 4.8 | 3.26 | 9.56 | 15.63 | 9.00 | 88.1 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.1 | 4.94 | 13.73 | 22.35 | 0.00 | 83.9 | 85.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.9 | 4.33 | 12.14 | 19.89 | 1.00 | 88.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.3 | 3.89 | 11.70 | 19.50 | 2.00 | 81.2 | 90.0 |
| XI | XI | Ola Aina | DEF | 16 | 5.1 | 3.78 | 11.26 | 18.32 | 6.00 | 84.9 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.7 | 3.81 | 11.13 | 17.88 | 2.00 | 80.5 | 90.0 |
| XI | Bench | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.08 | 13.06 | 21.67 | 0.00 | 72.0 | 0.0 |
| Bench 3 | Autosub In | João Pedro Junqueira de Jesus | FWD | 5 | 5.7 | 3.65 | 11.38 | 18.89 | 9.00 | 79.9 | 90.0 |
| Bench 4 | Bench | Jamie Vardy | FWD | 11 | 5.6 | 2.87 | 8.86 | 14.39 | 5.00 | 60.6 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.75 | 26.93 | 43.99 | 7.00 | 112.4 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 6.69 | 20.58 | 34.24 | 10.00 | 94.2 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.6 | 5.13 | 14.84 | 24.36 | 19.00 | 89.3 | 90.0 |
| XI | Bench | Morgan Rogers | MID | 2 | 5.5 | 4.76 | 13.03 | 20.94 | 0.00 | 86.4 | 0.0 |
| Bench 2 | Autosub In | Jacob Murphy | MID | 15 | 5.0 | 3.76 | 11.78 | 19.45 | 5.00 | 70.0 | 85.0 |

## GW21

- Train rows: 147195
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 62.92
- Actual score: 48.00
- Transfer: Matheus Santos Carneiro Da Cunha -> Chris Wood (projected gain 0.94, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 4.00 | 11.34 | 18.64 | 2.00 | 86.4 | 90.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 4.9 | 3.07 | 9.72 | 16.04 | 3.00 | 86.5 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 4.01 | 12.51 | 20.67 | 2.00 | 75.3 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.10 | 11.96 | 19.56 | 7.00 | 84.9 | 90.0 |
| Bench 2 | Bench | Ola Aina | DEF | 16 | 5.2 | 3.72 | 11.44 | 18.52 | 2.00 | 84.3 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 3.79 | 11.17 | 17.65 | 6.00 | 73.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.3 | 4.03 | 11.12 | 18.14 | 2.00 | 82.5 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.8 | 4.00 | 12.23 | 19.52 | 9.00 | 72.6 | 89.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.7 | 4.06 | 11.43 | 18.59 | 1.00 | 80.8 | 77.0 |
| Bench 3 | Bench | Jamie Vardy | FWD | 11 | 5.5 | 3.25 | 9.55 | 15.45 | 2.00 | 67.3 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 8.89 | 26.54 | 43.98 | 2.00 | 104.7 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.29 | 21.44 | 35.64 | 10.00 | 104.7 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.81 | 17.15 | 27.70 | 2.00 | 99.8 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.1 | 4.06 | 12.19 | 19.84 | 3.00 | 75.7 | 77.0 |
| Bench 4 | Bench | Morgan Rogers | MID | 2 | 5.5 | 2.23 | 7.67 | 13.49 | 6.00 | 40.2 | 90.0 |

## GW22

- Train rows: 147919
- Bank: 0.20 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 73.38
- Actual score: 57.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.65) beats the best remaining Triple Captain opportunity (11.43).
- Chip advisory: bench_boost (0.62): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Morgan Rogers -> Amad Diallo (projected gain 4.28, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.65) beats the best remaining Triple Captain opportunity (11.43).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.6 | 3.59 | 10.60 | 17.60 | 1.00 | 85.1 | 90.0 |
| XI | XI | Matz Sels | GK | 16 | 4.9 | 3.68 | 10.44 | 17.25 | 1.00 | 87.2 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.61 | 13.12 | 21.54 | 8.00 | 92.6 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 4.02 | 12.51 | 20.99 | 11.00 | 78.5 | 90.0 |
| XI | XI | Ola Aina | DEF | 16 | 5.2 | 4.23 | 11.84 | 19.37 | 4.00 | 85.1 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 3.90 | 11.08 | 17.60 | 4.00 | 75.9 | 65.0 |
| Bench 4 | Bench | William Saliba | DEF | 1 | 6.3 | 3.60 | 10.45 | 17.08 | 0.00 | 80.6 | 0.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.8 | 4.89 | 13.64 | 22.55 | 12.00 | 83.3 | 82.0 |
| Bench 3 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.7 | 3.64 | 10.72 | 17.74 | 2.00 | 72.2 | 90.0 |
| Bench 2 | Bench | Jamie Vardy | FWD | 11 | 5.5 | 3.69 | 10.33 | 16.63 | 2.00 | 74.3 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 8.65 | 25.77 | 42.57 | 3.00 | 99.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.48 | 21.78 | 36.03 | 2.00 | 104.7 | 83.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.8 | 5.56 | 16.69 | 27.71 | 2.00 | 95.5 | 90.0 |
| XI | XI | Amad Diallo | MID | 14 | 5.4 | 5.15 | 14.59 | 23.52 | 2.00 | 94.8 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.1 | 3.90 | 11.57 | 19.32 | 2.00 | 73.1 | 65.0 |

## GW23

- Train rows: 148648
- Bank: 0.30 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 76.73
- Actual score: 68.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (12.75) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Jamie Vardy -> Raúl Jiménez (projected gain 0.31, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (12.75) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.51 | 10.43 | 17.31 | 9.00 | 85.5 | 90.0 |
| Bench 1 | Bench Boost | Matz Sels | GK | 16 | 5.0 | 3.07 | 9.65 | 15.96 | 1.00 | 84.2 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 4.90 | 14.24 | 23.25 | 5.00 | 85.4 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 4.56 | 12.86 | 20.97 | 2.00 | 90.9 | 90.0 |
| XI | XI | Ola Aina | DEF | 16 | 5.3 | 3.99 | 11.86 | 19.30 | 1.00 | 90.0 | 78.0 |
| XI | XI | Lewis Hall | DEF | 15 | 5.0 | 4.19 | 11.35 | 18.10 | 2.00 | 72.9 | 90.0 |
| Bench 4 | Bench Boost | William Saliba | DEF | 1 | 6.3 | 2.18 | 6.92 | 11.91 | 9.00 | 44.9 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.0 | 4.96 | 14.68 | 23.65 | 2.00 | 82.2 | 90.0 |
| XI | XI | Raúl Jiménez | FWD | 9 | 5.7 | 4.02 | 11.15 | 18.21 | 2.00 | 63.2 | 63.0 |
| Bench 3 | Bench Boost | João Pedro Junqueira de Jesus | FWD | 5 | 5.6 | 3.59 | 10.59 | 17.43 | 1.00 | 73.8 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 8.34 | 24.45 | 40.25 | 8.00 | 92.3 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 6.62 | 20.31 | 34.21 | 2.00 | 95.3 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.8 | 5.74 | 16.80 | 28.18 | 7.00 | 97.0 | 90.0 |
| XI | XI | Amad Diallo | MID | 14 | 5.5 | 4.80 | 14.07 | 23.12 | 3.00 | 90.2 | 90.0 |
| Bench 2 | Bench Boost | Jacob Murphy | MID | 15 | 5.1 | 3.92 | 10.89 | 18.19 | 6.00 | 68.8 | 90.0 |