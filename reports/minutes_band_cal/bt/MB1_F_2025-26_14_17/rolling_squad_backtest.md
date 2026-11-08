# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW13
- Simulated weeks: GW14-GW17
- Total predicted points: 254.71
- Total actual points: 320.00
- Average predicted points: 63.68
- Average actual points: 80.00
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
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 60.61
- Actual score: 72.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.8 | 3.40 | 9.45 | 14.99 | 1.00 | 81.3 | 90.0 |
| Bench 1 | Bench | James Wright | GK | 2 | 3.9 | 0.00 | 0.00 | 0.14 | 0.00 | 1.5 | 0.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.64 | 12.87 | 20.03 | 14.00 | 84.1 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 4.33 | 11.49 | 18.63 | 8.00 | 83.3 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.2 | 4.23 | 11.43 | 17.96 | 1.00 | 84.9 | 90.0 |
| Bench 2 | Bench | Maxime Estève | DEF | 3 | 3.9 | 2.98 | 8.32 | 12.80 | 4.00 | 82.9 | 90.0 |
| Bench 4 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 2.46 | 6.77 | 11.25 | 0.00 | 76.7 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 7.37 | 21.89 | 36.14 | 14.00 | 82.9 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.7 | 3.79 | 13.40 | 21.62 | 1.00 | 70.9 | 30.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 4.57 | 13.19 | 21.95 | 2.00 | 67.8 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.57 | 15.66 | 25.51 | 4.00 | 82.9 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.1 | 5.29 | 15.30 | 25.02 | 6.00 | 81.7 | 29.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.8 | 5.19 | 14.30 | 23.50 | 4.00 | 80.7 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.87 | 14.01 | 23.34 | 3.00 | 81.0 | 82.0 |
| Bench 3 | Bench | Lewis Miley | MID | 15 | 4.4 | 2.47 | 6.94 | 10.83 | 2.00 | 51.8 | 90.0 |

## GW15

- Train rows: 171608
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 58.41
- Actual score: 70.00
- Transfer: Maxence Lacroix -> Marc Guéhi (projected gain 1.29, hit 0)
- Autosub: Trevoh Chalobah replaced Daniel Muñoz Mejía.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.8 | 2.79 | 8.31 | 13.67 | 10.00 | 81.1 | 90.0 |
| Bench 1 | Bench | James Wright | GK | 2 | 3.9 | 0.00 | 0.00 | 0.02 | 0.00 | 1.3 | 0.0 |
| XI | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.42 | 12.83 | 20.81 | 0.00 | 83.0 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.1 | 4.02 | 11.35 | 18.03 | 8.00 | 83.0 | 90.0 |
| Bench 2 | Autosub In | Trevoh Chalobah | DEF | 7 | 5.2 | 3.44 | 10.07 | 15.82 | 11.00 | 78.8 | 90.0 |
| XI | XI | Maxime Estève | DEF | 3 | 3.9 | 3.46 | 9.41 | 14.98 | 3.00 | 84.5 | 90.0 |
| Bench 4 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 1.46 | 4.56 | 7.79 | 0.00 | 42.3 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.04 | 23.23 | 38.28 | 2.00 | 83.0 | 68.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.7 | 4.77 | 13.90 | 22.30 | 2.00 | 73.8 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 4.11 | 12.08 | 20.63 | 1.00 | 69.5 | 32.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.1 | 5.08 | 16.02 | 26.33 | 4.00 | 72.5 | 78.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.23 | 14.56 | 24.42 | 18.00 | 83.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.16 | 12.92 | 22.50 | 6.00 | 74.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 4.31 | 12.62 | 21.60 | 3.00 | 71.5 | 90.0 |
| Bench 3 | Bench | Lewis Miley | MID | 15 | 4.4 | 3.12 | 7.75 | 12.06 | 1.00 | 57.3 | 27.0 |

## GW16

- Train rows: 172367
- Bank: 0.00 -> 0.80
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Erling Haaland
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 67.77
- Actual score: 88.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.37) beats the best remaining Bench Boost opportunity (7.52).
- Transfer: Daniel Muñoz Mejía -> Nico O'Reilly (projected gain 2.15, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.37) beats the best remaining Bench Boost opportunity (7.52).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.8 | 2.54 | 7.45 | 12.79 | 6.00 | 80.8 | 90.0 |
| Bench 1 | Bench Boost | James Wright | GK | 2 | 3.9 | 0.00 | 0.00 | 0.04 | 0.00 | 0.0 | 0.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 3.97 | 12.01 | 18.53 | 6.00 | 81.1 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.1 | 4.22 | 11.95 | 19.29 | 1.00 | 83.0 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.3 | 4.03 | 11.40 | 18.69 | 9.00 | 83.0 | 90.0 |
| XI | XI | Maxime Estève | DEF | 3 | 3.9 | 3.76 | 10.10 | 15.84 | 1.00 | 83.2 | 90.0 |
| Bench 4 | Bench Boost | Axel Tuanzebe | DEF | 3 | 3.9 | 1.02 | 3.15 | 5.60 | 1.00 | 30.1 | 76.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.9 | 6.88 | 21.60 | 36.30 | 13.00 | 83.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.9 | 5.99 | 16.02 | 25.37 | 2.00 | 83.0 | 90.0 |
| Bench 2 | Bench Boost | João Pedro Junqueira de Jesus | FWD | 7 | 7.3 | 3.23 | 10.06 | 17.82 | 2.00 | 53.7 | 80.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.0 | 7.01 | 18.96 | 31.36 | 13.00 | 83.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.1 | 6.53 | 17.64 | 28.03 | 11.00 | 81.1 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.47 | 14.46 | 23.79 | 2.00 | 83.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 4.01 | 11.93 | 20.36 | 6.00 | 73.2 | 90.0 |
| Bench 3 | Bench Boost | Lewis Miley | MID | 15 | 4.4 | 2.12 | 6.34 | 10.49 | 2.00 | 43.1 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 0.80 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 67.92
- Actual score: 90.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.16) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: João Pedro Junqueira de Jesus -> Jarrod Bowen (projected gain 1.07, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.16) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.8 | 2.82 | 8.59 | 14.19 | 4.00 | 80.6 | 90.0 |
| Bench 1 | Bench | James Wright | GK | 2 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.2 | 4.16 | 11.53 | 18.44 | 1.00 | 82.9 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 4.09 | 11.50 | 17.57 | 6.00 | 79.9 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.3 | 3.76 | 11.03 | 17.65 | 3.00 | 80.5 | 90.0 |
| Bench 2 | Bench | Maxime Estève | DEF | 3 | 3.9 | 3.15 | 9.09 | 14.49 | 0.00 | 81.1 | 0.0 |
| Bench 4 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 1.43 | 4.18 | 7.50 | 0.00 | 51.2 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.16 | 22.94 | 37.91 | 16.00 | 83.0 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 3.81 | 11.59 | 19.01 | 1.00 | 78.3 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.9 | 3.53 | 11.38 | 18.16 | 2.00 | 50.4 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.1 | 5.73 | 17.73 | 29.15 | 1.00 | 83.0 | 45.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.2 | 5.40 | 16.16 | 26.65 | 3.00 | 74.7 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 5.50 | 14.07 | 22.41 | 10.00 | 83.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.65 | 14.03 | 22.71 | 11.00 | 77.4 | 90.0 |
| Bench 3 | Bench | Lewis Miley | MID | 15 | 4.4 | 2.71 | 7.92 | 12.34 | 4.00 | 58.5 | 90.0 |