# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW13
- Simulated weeks: GW14-GW17
- Total predicted points: 259.77
- Total actual points: 297.00
- Average predicted points: 64.94
- Average actual points: 74.25
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
- Predicted score: 61.31
- Actual score: 88.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.54 | 10.03 | 16.21 | 6.00 | 80.3 | 90.0 |
| Bench 1 | Bench | Tommy Setford | GK | 1 | 3.9 | 0.00 | 0.14 | 0.16 | 0.00 | 1.1 | 0.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.56 | 12.71 | 19.82 | 14.00 | 83.0 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 4.24 | 11.34 | 18.42 | 8.00 | 82.1 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.1 | 4.14 | 11.03 | 18.07 | 14.00 | 77.3 | 90.0 |
| Bench 3 | Bench | Maxime Estève | DEF | 3 | 3.9 | 2.89 | 8.16 | 12.59 | 4.00 | 81.7 | 90.0 |
| Bench 4 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 2.43 | 6.78 | 11.36 | 0.00 | 75.5 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 7.48 | 22.24 | 36.53 | 14.00 | 83.4 | 90.0 |
| Bench 2 | Bench | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.7 | 3.78 | 13.39 | 21.59 | 1.00 | 71.1 | 30.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 4.56 | 13.18 | 21.92 | 2.00 | 68.0 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.69 | 16.01 | 25.89 | 4.00 | 83.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.6 | 5.21 | 14.61 | 23.84 | 2.00 | 80.4 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.99 | 14.36 | 23.72 | 3.00 | 81.4 | 82.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.8 | 5.10 | 14.14 | 23.29 | 4.00 | 79.6 | 90.0 |
| XI | XI | Kiernan Dewsbury-Hall | MID | 9 | 4.9 | 4.33 | 11.98 | 18.19 | 3.00 | 82.2 | 90.0 |

## GW15

- Train rows: 171608
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 59.50
- Actual score: 57.00
- Transfer: none
- No transfer was applied this week.
- Autosub: Maxime Estève replaced Daniel Muñoz Mejía.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.35 | 9.83 | 16.14 | 2.00 | 80.1 | 90.0 |
| Bench 1 | Bench | Tommy Setford | GK | 1 | 3.9 | 0.00 | 0.00 | 0.05 | 0.00 | 2.0 | 0.0 |
| XI | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.54 | 13.17 | 21.19 | 0.00 | 83.4 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.1 | 4.13 | 11.69 | 18.42 | 8.00 | 83.4 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.49 | 10.22 | 16.54 | 2.00 | 81.5 | 90.0 |
| Bench 3 | Autosub In | Maxime Estève | DEF | 3 | 3.9 | 3.38 | 9.27 | 14.79 | 3.00 | 83.4 | 90.0 |
| Bench 4 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 1.50 | 4.66 | 7.91 | 0.00 | 43.0 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.15 | 23.57 | 38.66 | 2.00 | 83.4 | 68.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.7 | 4.74 | 13.91 | 22.40 | 2.00 | 72.7 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 4.10 | 12.06 | 20.60 | 1.00 | 69.7 | 32.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.34 | 14.90 | 24.80 | 18.00 | 83.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.5 | 5.09 | 14.09 | 23.58 | 8.00 | 79.9 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.13 | 12.93 | 22.61 | 6.00 | 73.8 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 4.29 | 12.60 | 21.57 | 3.00 | 71.7 | 90.0 |
| Bench 2 | Bench | Kiernan Dewsbury-Hall | MID | 9 | 4.9 | 3.69 | 10.88 | 17.57 | 16.00 | 79.5 | 90.0 |

## GW16

- Train rows: 172367
- Bank: 0.00 -> 1.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Erling Haaland
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 70.14
- Actual score: 60.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.10) beats the best remaining Bench Boost opportunity (9.41).
- Transfer: Daniel Muñoz Mejía -> Matty Cash (projected gain 2.30, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.10) beats the best remaining Bench Boost opportunity (9.41).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.34 | 11.15 | 17.83 | 2.00 | 83.4 | 90.0 |
| Bench 1 | Bench Boost | Tommy Setford | GK | 1 | 3.9 | 0.33 | 0.30 | 0.53 | 0.00 | 1.7 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.1 | 4.33 | 12.29 | 19.70 | 1.00 | 83.4 | 90.0 |
| XI | XI | Matty Cash | DEF | 2 | 4.9 | 4.40 | 12.26 | 19.34 | 0.00 | 83.4 | 90.0 |
| Bench 2 | Bench Boost | Maxence Lacroix | DEF | 8 | 5.1 | 3.45 | 10.11 | 16.72 | 1.00 | 82.2 | 90.0 |
| XI | XI | Maxime Estève | DEF | 3 | 3.9 | 3.68 | 9.95 | 15.63 | 1.00 | 82.1 | 90.0 |
| Bench 4 | Bench Boost | Axel Tuanzebe | DEF | 3 | 3.9 | 1.06 | 3.24 | 5.72 | 1.00 | 30.8 | 76.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.9 | 6.99 | 21.94 | 36.70 | 13.00 | 83.4 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.9 | 6.10 | 16.36 | 25.77 | 2.00 | 83.4 | 90.0 |
| Bench 3 | Bench Boost | João Pedro Junqueira de Jesus | FWD | 7 | 7.3 | 3.27 | 10.19 | 18.01 | 2.00 | 54.9 | 80.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.0 | 7.12 | 19.30 | 31.77 | 13.00 | 83.4 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.39 | 14.31 | 23.58 | 2.00 | 82.8 | 90.0 |
| XI | XI | Kiernan Dewsbury-Hall | MID | 9 | 5.0 | 4.47 | 13.67 | 21.24 | 1.00 | 83.4 | 15.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 4.01 | 11.90 | 20.32 | 6.00 | 73.3 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 4.09 | 11.55 | 20.42 | 2.00 | 68.5 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 1.10 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 68.81
- Actual score: 92.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.27) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Bryan Mbeumo -> Phil Foden (projected gain 8.97, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.27) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Matty Cash replaced Maxime Estève.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.39 | 10.05 | 16.36 | 7.00 | 79.4 | 90.0 |
| Bench 1 | Bench | Tommy Setford | GK | 1 | 3.9 | 0.00 | 0.03 | 0.24 | 0.00 | 1.7 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.2 | 4.27 | 11.86 | 18.82 | 1.00 | 83.3 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.74 | 10.84 | 17.43 | 1.00 | 82.1 | 90.0 |
| Bench 2 | Autosub In | Matty Cash | DEF | 2 | 4.9 | 3.04 | 9.55 | 15.05 | 2.00 | 68.0 | 90.0 |
| XI | Bench | Maxime Estève | DEF | 3 | 3.9 | 3.12 | 9.10 | 14.59 | 0.00 | 80.0 | 0.0 |
| Bench 4 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 1.48 | 4.31 | 7.69 | 0.00 | 52.4 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.27 | 23.26 | 38.29 | 16.00 | 83.4 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.9 | 3.58 | 11.51 | 18.35 | 2.00 | 51.6 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.2 | 3.52 | 10.50 | 17.90 | 6.00 | 66.7 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.9 | 6.35 | 18.49 | 28.59 | 3.00 | 80.1 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.1 | 5.83 | 18.05 | 29.53 | 1.00 | 83.4 | 45.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 5.61 | 14.39 | 22.79 | 10.00 | 83.4 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.62 | 14.04 | 22.81 | 11.00 | 76.4 | 90.0 |
| Bench 3 | Bench | Kiernan Dewsbury-Hall | MID | 9 | 5.0 | 1.88 | 7.41 | 12.94 | 0.00 | 33.1 | 0.0 |