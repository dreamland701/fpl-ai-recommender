# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW13
- Simulated weeks: GW14-GW17
- Total predicted points: 222.12
- Total actual points: 242.00
- Average predicted points: 55.53
- Average actual points: 60.50
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW13 are included before the first simulated week.
- League-average scores were not available for this run.

## GW14

- Train rows: 170850
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Bryan Mbeumo
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 54.77
- Actual score: 53.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.83 | 10.66 | 17.00 | 6.00 | 90.3 | 90.0 |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 4.8 | 3.15 | 8.76 | 14.15 | 1.00 | 83.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.60 | 12.60 | 19.76 | 1.00 | 89.9 | 46.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.15 | 11.62 | 18.21 | 14.00 | 83.3 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.11 | 11.51 | 18.39 | 1.00 | 87.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.1 | 3.92 | 10.42 | 17.01 | 14.00 | 77.6 | 90.0 |
| Bench 2 | Bench | Maxence Lacroix | DEF | 8 | 5.1 | 3.88 | 10.42 | 17.00 | 8.00 | 81.4 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 6 | 6.6 | 3.18 | 10.60 | 17.40 | 1.00 | 60.4 | 23.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 2.94 | 9.01 | 15.31 | 2.00 | 35.3 | 60.0 |
| Bench 4 | Bench | Zian Flemming | FWD | 3 | 5.3 | 2.55 | 8.12 | 12.90 | 1.00 | 65.8 | 58.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.1 | 5.10 | 16.11 | 27.76 | 1.00 | 43.7 | 45.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.65 | 15.76 | 25.12 | 4.00 | 99.5 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.6 | 5.17 | 14.49 | 23.34 | 2.00 | 87.4 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.99 | 14.11 | 22.93 | 3.00 | 89.3 | 82.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.44 | 11.61 | 18.50 | 2.00 | 89.2 | 90.0 |

## GW15

- Train rows: 171608
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bruno Borges Fernandes
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 49.47
- Actual score: 82.00
- Transfer: none
- No transfer was applied this week.
- Autosub: Maxence Lacroix replaced Daniel Muñoz Mejía.
- Autosub: Zian Flemming replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.48 | 10.12 | 16.33 | 2.00 | 89.4 | 90.0 |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 4.8 | 2.47 | 7.57 | 12.54 | 10.00 | 78.7 | 90.0 |
| XI | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.28 | 12.58 | 20.03 | 0.00 | 94.7 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.1 | 4.02 | 11.52 | 17.89 | 8.00 | 93.8 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 3.53 | 10.76 | 17.63 | 3.00 | 68.9 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 3.46 | 10.43 | 17.16 | 6.00 | 83.7 | 90.0 |
| Bench 2 | Autosub In | Maxence Lacroix | DEF | 8 | 5.1 | 3.35 | 10.07 | 16.06 | 2.00 | 84.9 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 6 | 6.6 | 3.55 | 10.56 | 18.02 | 2.00 | 50.5 | 90.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 3.16 | 8.87 | 14.08 | 0.00 | 49.5 | 0.0 |
| Bench 4 | Autosub In | Zian Flemming | FWD | 3 | 5.3 | 2.70 | 7.68 | 12.80 | 5.00 | 61.4 | 4.0 |
| Captain | Bench | Mohamed Salah | MID | 12 | 14.1 | 5.33 | 16.27 | 28.16 | 0.00 | 59.0 | 0.0 |
| Vice Captain | Captain | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.15 | 14.36 | 23.70 | 18.00 | 89.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.5 | 4.43 | 12.51 | 21.00 | 8.00 | 77.8 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 3.47 | 11.22 | 19.72 | 6.00 | 69.9 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.46 | 10.71 | 17.40 | 4.00 | 73.8 | 90.0 |

## GW16

- Train rows: 172367
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Declan Rice
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 60.90
- Actual score: 65.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.10) beats the best remaining Triple Captain opportunity (7.74).
- Transfer: Maxence Lacroix -> Matty Cash (projected gain 3.33, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (7.10) beats the best remaining Triple Captain opportunity (7.74).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.56 | 11.45 | 18.05 | 2.00 | 100.3 | 90.0 |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 4.8 | 2.73 | 8.10 | 13.39 | 6.00 | 87.9 | 90.0 |
| XI | XI | Matty Cash | DEF | 2 | 4.9 | 4.72 | 12.34 | 19.25 | 0.00 | 107.5 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.1 | 4.32 | 12.09 | 19.16 | 1.00 | 100.4 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 3.74 | 11.15 | 18.10 | 6.00 | 91.3 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 3.81 | 10.22 | 16.82 | 2.00 | 78.5 | 90.0 |
| Bench 4 | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 0.47 | 5.02 | 10.68 | 0.00 | 3.2 | 0.0 |
| XI | XI | Zian Flemming | FWD | 3 | 5.3 | 2.99 | 8.81 | 14.90 | 1.00 | 46.2 | 28.0 |
| Bench 2 | Bench | Danny Welbeck | FWD | 6 | 6.5 | 2.63 | 8.53 | 14.66 | 1.00 | 52.1 | 8.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 1.22 | 4.52 | 8.54 | 5.00 | 23.1 | 12.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.0 | 7.10 | 18.41 | 30.15 | 13.00 | 119.9 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.0 | 4.05 | 13.22 | 23.46 | 7.00 | 29.1 | 64.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.0 | 4.80 | 12.70 | 21.07 | 2.00 | 83.1 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.69 | 10.72 | 17.42 | 3.00 | 74.9 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 2.93 | 9.31 | 16.75 | 2.00 | 54.6 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 0.20 -> 2.70
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Mohamed Salah
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 56.99
- Actual score: 42.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.28) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Bryan Mbeumo -> Harry Wilson (projected gain 6.34, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.28) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.06 | 9.12 | 14.78 | 7.00 | 80.6 | 90.0 |
| Bench 1 | Bench Boost | Robert Lynch Sánchez | GK | 7 | 4.8 | 2.47 | 7.75 | 12.92 | 4.00 | 81.3 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.2 | 4.33 | 11.69 | 18.38 | 1.00 | 93.1 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 3.46 | 10.40 | 16.97 | 1.00 | 85.4 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 3.55 | 10.26 | 16.98 | 6.00 | 74.0 | 90.0 |
| Bench 2 | Bench Boost | Matty Cash | DEF | 2 | 4.9 | 2.60 | 8.45 | 13.25 | 2.00 | 61.0 | 90.0 |
| Bench 4 | Bench Boost | Daniel Muñoz Mejía | DEF | 8 | 5.9 | -0.34 | -0.30 | 1.07 | 0.00 | 2.2 | 0.0 |
| XI | XI | Zian Flemming | FWD | 3 | 5.3 | 2.83 | 8.74 | 14.79 | 1.00 | 42.0 | 64.0 |
| XI | XI | Danny Welbeck | FWD | 6 | 6.5 | 2.64 | 8.09 | 14.57 | 0.00 | 27.3 | 0.0 |
| Bench 3 | Bench Boost | Junior Kroupi | FWD | 4 | 4.6 | 2.55 | 6.72 | 11.49 | 1.00 | 28.3 | 26.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.1 | 5.58 | 17.03 | 27.69 | 1.00 | 90.8 | 45.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.0 | 5.57 | 16.60 | 28.06 | 0.00 | 58.7 | 0.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.7 | 5.45 | 14.72 | 22.22 | 2.00 | 106.7 | 83.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.22 | 12.75 | 20.65 | 11.00 | 74.5 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.44 | 10.66 | 17.02 | 4.00 | 73.5 | 90.0 |