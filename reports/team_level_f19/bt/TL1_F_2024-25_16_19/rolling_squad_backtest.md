# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 267.32
- Total actual points: 296.00
- Average predicted points: 66.83
- Average actual points: 74.00
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
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 63.58
- Actual score: 59.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.76 | 10.80 | 17.38 | 6.00 | 87.2 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 6 | 3.9 | 0.11 | 0.32 | 0.59 | 0.00 | 4.6 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.26 | 12.81 | 19.88 | 6.00 | 85.3 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.24 | 11.45 | 19.03 | 6.00 | 88.1 | 62.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.7 | 3.06 | 9.52 | 15.35 | 1.00 | 80.9 | 90.0 |
| Bench 2 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.34 | 6.24 | 10.26 | 0.00 | 72.3 | 90.0 |
| Bench 3 | Bench | Sepp van den Berg | DEF | 4 | 4.1 | 1.90 | 6.21 | 10.21 | 1.00 | 73.6 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.6 | 6.21 | 17.18 | 27.34 | 11.00 | 90.0 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.41 | 12.88 | 20.97 | 9.00 | 81.0 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.67 | 10.81 | 17.38 | 1.00 | 84.1 | 58.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 8.19 | 23.71 | 38.11 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.37 | 22.26 | 37.62 | 5.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.27 | 18.88 | 30.09 | 3.00 | 87.2 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.95 | 12.26 | 19.43 | 5.00 | 85.2 | 90.0 |
| Bench 4 | Bench | Yehor Yarmoliuk | MID | 4 | 4.4 | 1.85 | 5.60 | 8.83 | 2.00 | 50.1 | 74.0 |

## GW17

- Train rows: 144369
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 59.86
- Actual score: 70.00
- Transfer: Daniel Muñoz -> Lewis Hall (projected gain 5.35, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.73 | 10.83 | 17.52 | 3.00 | 85.7 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 6 | 3.9 | 0.11 | 0.33 | 0.63 | 0.00 | 4.6 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 3.92 | 11.84 | 18.95 | 2.00 | 80.1 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.95 | 11.19 | 17.68 | 7.00 | 87.2 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 3.04 | 9.64 | 16.31 | -1.00 | 73.6 | 90.0 |
| Bench 2 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 1.98 | 5.85 | 9.76 | 8.00 | 72.6 | 90.0 |
| Bench 4 | Bench | Sepp van den Berg | DEF | 4 | 4.1 | 1.48 | 4.95 | 8.31 | 0.00 | 66.1 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.7 | 5.94 | 17.97 | 28.26 | 17.00 | 85.7 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.77 | 12.91 | 21.51 | 9.00 | 79.1 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.40 | 9.37 | 15.57 | 2.00 | 71.7 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 7.31 | 22.98 | 36.86 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.12 | 22.77 | 37.82 | 21.00 | 90.0 | 86.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.25 | 18.89 | 30.85 | 1.00 | 85.7 | 23.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.13 | 11.10 | 17.61 | 3.00 | 72.2 | 90.0 |
| Bench 3 | Bench | Yehor Yarmoliuk | MID | 4 | 4.4 | 1.91 | 5.63 | 8.78 | 0.00 | 50.9 | 0.0 |

## GW18

- Train rows: 145070
- Bank: 0.10 -> 2.90
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 69.40
- Actual score: 75.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (4.32) beats the best remaining Bench Boost opportunity (4.90).
- Transfer: Bukayo Saka -> Bryan Mbeumo (projected gain 7.96, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (4.32) beats the best remaining Bench Boost opportunity (4.90).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 4.21 | 11.35 | 18.25 | 6.00 | 87.4 | 90.0 |
| Bench 1 | Bench Boost | Marcus Bettinelli | GK | 6 | 3.9 | 0.25 | 0.48 | 0.76 | 0.00 | 6.0 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.71 | 13.09 | 21.03 | 7.00 | 87.4 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.16 | 9.51 | 15.37 | 6.00 | 72.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 2.97 | 9.30 | 15.61 | 1.00 | 79.0 | 9.0 |
| Bench 2 | Bench Boost | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.48 | 6.54 | 10.71 | 2.00 | 79.1 | 90.0 |
| Bench 4 | Bench Boost | Sepp van den Berg | DEF | 4 | 4.1 | 0.48 | 2.21 | 4.33 | 0.00 | 32.6 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 7.35 | 21.34 | 33.36 | 8.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.61 | 13.03 | 21.96 | 12.00 | 82.0 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 2.67 | 8.82 | 14.60 | 0.00 | 66.4 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.4 | 9.78 | 25.87 | 42.50 | 9.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.56 | 23.09 | 37.42 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.6 | 4.90 | 14.39 | 23.78 | 3.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.37 | 10.44 | 17.04 | 2.00 | 75.3 | 90.0 |
| Bench 3 | Bench Boost | Yehor Yarmoliuk | MID | 4 | 4.4 | 1.11 | 3.51 | 5.95 | 0.00 | 28.5 | 18.0 |

## GW19

- Train rows: 145775
- Bank: 2.90 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 74.48
- Actual score: 92.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.68) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Yehor Yarmoliuk -> Anthony Gordon (projected gain 7.82, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.68) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.88 | 11.20 | 18.15 | 2.00 | 88.7 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 6 | 3.9 | 0.43 | 0.82 | 1.16 | 0.00 | 8.5 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.32 | 12.76 | 21.16 | 2.00 | 88.7 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 4.06 | 11.79 | 19.26 | 12.00 | 84.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 2.48 | 7.67 | 13.52 | 4.00 | 52.7 | 90.0 |
| Bench 2 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.40 | 6.94 | 11.24 | 0.00 | 80.4 | 90.0 |
| Bench 4 | Bench | Sepp van den Berg | DEF | 4 | 4.1 | 0.38 | 1.80 | 3.69 | 1.00 | 27.6 | 74.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 7.12 | 20.71 | 32.33 | 7.00 | 78.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 5.47 | 15.65 | 25.74 | 1.00 | 90.0 | 45.0 |
| Bench 3 | Bench | Jamie Vardy | FWD | 11 | 5.6 | 1.02 | 4.10 | 7.24 | 2.00 | 20.8 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.5 | 8.68 | 25.30 | 41.18 | 16.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.88 | 22.91 | 37.68 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 5.05 | 14.59 | 23.35 | 6.00 | 81.4 | 84.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.6 | 4.16 | 13.56 | 22.28 | 7.00 | 87.3 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 4.01 | 11.18 | 18.01 | 1.00 | 79.3 | 90.0 |