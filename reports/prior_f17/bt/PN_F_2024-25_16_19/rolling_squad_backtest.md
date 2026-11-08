# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 269.23
- Total actual points: 301.00
- Average predicted points: 67.31
- Average actual points: 75.25
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
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 63.69
- Actual score: 60.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.76 | 10.77 | 17.26 | 6.00 | 87.9 | 90.0 |
| Bench 1 | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 0.00 | 0.34 | 0.66 | 0.00 | 3.4 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.26 | 12.79 | 19.75 | 6.00 | 86.2 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.22 | 11.60 | 19.24 | 6.00 | 88.6 | 62.0 |
| XI | XI | Milos Kerkez | DEF | 3 | 4.6 | 3.25 | 9.18 | 14.67 | 2.00 | 74.9 | 90.0 |
| Bench 4 | Bench | Dara O'Shea | DEF | 10 | 4.0 | 2.11 | 6.33 | 10.40 | 2.00 | 78.2 | 90.0 |
| Bench 2 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.34 | 6.19 | 10.26 | 0.00 | 70.7 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.6 | 6.10 | 16.88 | 26.94 | 11.00 | 90.0 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.28 | 12.64 | 20.60 | 9.00 | 81.5 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.70 | 10.97 | 17.61 | 1.00 | 82.0 | 58.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 8.23 | 23.85 | 38.39 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.39 | 22.27 | 37.62 | 5.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.24 | 18.82 | 29.91 | 3.00 | 87.7 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 4.02 | 12.41 | 19.70 | 5.00 | 85.3 | 90.0 |
| Bench 3 | Bench | Tyler Dibling | MID | 17 | 4.5 | 2.16 | 5.57 | 8.91 | 2.00 | 58.5 | 90.0 |

## GW17

- Train rows: 144369
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 59.67
- Actual score: 70.00
- Transfer: Milos Kerkez -> Lewis Hall (projected gain 2.66, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.70 | 10.74 | 17.32 | 3.00 | 86.1 | 90.0 |
| Bench 1 | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 0.17 | 0.64 | 1.01 | 0.00 | 5.5 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 3.89 | 11.77 | 18.75 | 2.00 | 80.8 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.86 | 11.04 | 17.45 | 7.00 | 88.2 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 3.05 | 9.78 | 16.54 | -1.00 | 73.9 | 90.0 |
| Bench 2 | Bench | Dara O'Shea | DEF | 10 | 4.0 | 2.08 | 6.34 | 10.45 | 0.00 | 78.7 | 90.0 |
| Bench 3 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.00 | 5.83 | 9.76 | 8.00 | 71.2 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.7 | 5.84 | 17.79 | 27.97 | 17.00 | 86.7 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.66 | 12.65 | 21.18 | 9.00 | 79.8 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.47 | 9.56 | 15.84 | 2.00 | 69.7 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 7.35 | 23.27 | 37.19 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.10 | 22.66 | 37.65 | 21.00 | 90.0 | 86.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.21 | 18.80 | 30.62 | 1.00 | 86.1 | 23.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.20 | 11.35 | 17.90 | 3.00 | 72.5 | 90.0 |
| Bench 4 | Bench | Tyler Dibling | MID | 17 | 4.5 | 1.91 | 5.42 | 8.86 | 1.00 | 60.5 | 45.0 |

## GW18

- Train rows: 145070
- Bank: 0.10 -> 2.90
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 71.41
- Actual score: 79.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.54) beats the best remaining Bench Boost opportunity (7.77).
- Transfer: Bukayo Saka -> Bryan Mbeumo (projected gain 7.95, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.54) beats the best remaining Bench Boost opportunity (7.77).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 4.10 | 11.21 | 18.03 | 6.00 | 88.1 | 90.0 |
| Bench 1 | Bench Boost | Hákon Valdimarsson | GK | 4 | 3.9 | 0.21 | 0.64 | 1.02 | 1.00 | 5.7 | 54.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.61 | 12.94 | 20.78 | 7.00 | 88.2 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.15 | 9.49 | 15.27 | 6.00 | 73.1 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 3.04 | 9.44 | 15.86 | 1.00 | 79.2 | 9.0 |
| Bench 2 | Bench Boost | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.50 | 6.56 | 10.74 | 2.00 | 77.2 | 90.0 |
| Bench 4 | Bench Boost | Dara O'Shea | DEF | 10 | 4.0 | 1.81 | 5.99 | 10.07 | 2.00 | 79.6 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 7.32 | 21.31 | 33.26 | 8.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.59 | 12.92 | 21.80 | 12.00 | 82.2 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 2.67 | 8.83 | 14.69 | 0.00 | 65.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.4 | 9.71 | 25.70 | 42.35 | 9.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.60 | 23.31 | 37.75 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.6 | 4.93 | 14.42 | 23.90 | 3.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.43 | 10.57 | 17.23 | 2.00 | 75.4 | 90.0 |
| Bench 3 | Bench Boost | Tyler Dibling | MID | 17 | 4.5 | 2.02 | 5.36 | 8.79 | 1.00 | 54.6 | 17.0 |

## GW19

- Train rows: 145775
- Bank: 2.90 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 74.46
- Actual score: 92.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.70) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Tyler Dibling -> Anthony Gordon (projected gain 7.61, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.70) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.87 | 11.10 | 17.98 | 2.00 | 88.8 | 90.0 |
| Bench 1 | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 1.01 | 3.00 | 4.49 | 0.00 | 33.0 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.32 | 12.67 | 20.99 | 2.00 | 89.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 4.06 | 11.74 | 19.18 | 12.00 | 84.1 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 2.56 | 7.90 | 13.81 | 4.00 | 53.1 | 90.0 |
| Bench 2 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.41 | 7.01 | 11.31 | 0.00 | 78.5 | 90.0 |
| Bench 3 | Bench | Dara O'Shea | DEF | 10 | 4.0 | 2.28 | 6.63 | 10.72 | 5.00 | 80.6 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 7.14 | 20.66 | 32.32 | 7.00 | 78.7 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 5.42 | 15.42 | 25.48 | 1.00 | 90.0 | 45.0 |
| Bench 4 | Bench | Jamie Vardy | FWD | 11 | 5.6 | 0.98 | 4.23 | 7.33 | 2.00 | 19.2 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.5 | 8.70 | 25.37 | 41.21 | 16.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.85 | 22.96 | 37.89 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 5.06 | 14.56 | 23.31 | 6.00 | 81.6 | 84.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.6 | 4.11 | 13.61 | 22.32 | 7.00 | 87.6 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.98 | 11.22 | 18.14 | 1.00 | 79.6 | 90.0 |