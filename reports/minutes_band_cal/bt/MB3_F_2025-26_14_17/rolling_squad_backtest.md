# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW13
- Simulated weeks: GW14-GW17
- Total predicted points: 270.38
- Total actual points: 275.00
- Average predicted points: 67.59
- Average actual points: 68.75
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
- Predicted score: 65.17
- Actual score: 60.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.99 | 11.39 | 18.12 | 6.00 | 86.9 | 90.0 |
| Bench 1 | Bench | Remi Matthews | GK | 8 | 3.9 | 0.03 | 0.16 | 0.28 | 0.00 | 2.6 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.70 | 13.45 | 21.11 | 1.00 | 86.1 | 46.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.51 | 12.73 | 20.37 | 1.00 | 87.2 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 4.24 | 11.42 | 18.70 | 8.00 | 84.0 | 90.0 |
| Bench 3 | Bench | Joe Rodon | DEF | 11 | 4.1 | 3.11 | 8.85 | 14.04 | 2.00 | 84.9 | 90.0 |
| Bench 4 | Bench | Maxime Estève | DEF | 3 | 3.9 | 2.90 | 8.25 | 12.87 | 4.00 | 83.6 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 7.94 | 23.60 | 38.44 | 14.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 5.37 | 14.98 | 23.68 | 2.00 | 87.9 | 63.0 |
| Bench 2 | Bench | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.7 | 3.79 | 13.40 | 21.62 | 1.00 | 70.9 | 30.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 6.14 | 17.38 | 27.80 | 4.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.6 | 5.66 | 15.97 | 25.75 | 2.00 | 87.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.44 | 15.73 | 25.63 | 3.00 | 88.0 | 82.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.91 | 13.11 | 20.99 | 2.00 | 89.5 | 90.0 |
| XI | XI | Kiernan Dewsbury-Hall | MID | 9 | 4.9 | 4.33 | 12.06 | 18.47 | 3.00 | 84.1 | 90.0 |

## GW15

- Train rows: 171608
- Bank: 0.00 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 60.67
- Actual score: 56.00
- Transfer: Jurriën Timber -> Virgil van Dijk (projected gain 0.05, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.79 | 11.19 | 18.09 | 2.00 | 86.7 | 90.0 |
| Bench 1 | Bench | Remi Matthews | GK | 8 | 3.9 | 0.00 | 0.03 | 0.13 | 0.00 | 2.2 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 3.99 | 11.80 | 19.36 | 6.00 | 85.6 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.94 | 11.59 | 18.48 | 2.00 | 88.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.05 | 11.41 | 18.94 | 2.00 | 87.3 | 90.0 |
| Bench 3 | Bench | Maxime Estève | DEF | 3 | 3.9 | 3.37 | 9.34 | 15.05 | 3.00 | 85.2 | 90.0 |
| Bench 4 | Bench | Joe Rodon | DEF | 11 | 4.1 | 2.88 | 7.87 | 12.94 | 1.00 | 81.6 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.60 | 24.93 | 40.60 | 2.00 | 90.0 | 68.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.7 | 4.77 | 13.90 | 22.30 | 2.00 | 73.8 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 3.96 | 11.96 | 20.13 | 2.00 | 66.1 | 65.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.79 | 16.26 | 26.75 | 18.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.5 | 5.12 | 14.08 | 23.48 | 8.00 | 81.1 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.16 | 12.92 | 22.50 | 6.00 | 74.9 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.90 | 11.89 | 19.31 | 4.00 | 77.6 | 90.0 |
| Bench 2 | Bench | Kiernan Dewsbury-Hall | MID | 9 | 4.9 | 3.72 | 10.87 | 17.46 | 16.00 | 80.7 | 90.0 |

## GW16

- Train rows: 172367
- Bank: 0.40 -> 0.00
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Erling Haaland
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 74.56
- Actual score: 78.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.42) beats the best remaining Bench Boost opportunity (10.01).
- Transfer: Bryan Mbeumo -> Phil Foden (projected gain 6.71, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.42) beats the best remaining Bench Boost opportunity (10.01).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.78 | 12.48 | 19.75 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Remi Matthews | GK | 8 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 1.6 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.26 | 12.61 | 20.44 | 6.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.09 | 11.64 | 18.88 | 6.00 | 84.1 | 90.0 |
| Bench 2 | Bench Boost | Maxence Lacroix | DEF | 8 | 5.1 | 3.44 | 10.19 | 16.98 | 1.00 | 84.1 | 90.0 |
| XI | XI | Maxime Estève | DEF | 3 | 3.9 | 3.67 | 10.02 | 15.90 | 1.00 | 84.0 | 90.0 |
| Bench 3 | Bench Boost | Joe Rodon | DEF | 11 | 4.1 | 2.79 | 8.14 | 12.76 | 2.00 | 79.7 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.9 | 7.43 | 23.27 | 38.63 | 13.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.9 | 6.53 | 17.69 | 27.70 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench Boost | Jean-Philippe Mateta | FWD | 8 | 7.9 | 2.18 | 7.89 | 14.79 | 2.00 | 40.7 | 62.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.0 | 7.55 | 20.63 | 33.69 | 13.00 | 90.0 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.7 | 5.68 | 18.28 | 28.47 | 11.00 | 83.2 | 90.0 |
| XI | XI | Kiernan Dewsbury-Hall | MID | 9 | 5.0 | 4.91 | 15.00 | 23.16 | 1.00 | 90.0 | 15.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.38 | 14.39 | 23.85 | 2.00 | 84.7 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.28 | 12.12 | 19.61 | 3.00 | 80.1 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 0.00 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 69.98
- Actual score: 81.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.70) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Jean-Philippe Mateta -> Jarrod Bowen (projected gain 2.51, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.70) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.42 | 10.04 | 16.27 | 7.00 | 80.4 | 90.0 |
| Bench 1 | Bench | Remi Matthews | GK | 8 | 3.9 | 0.00 | 0.00 | 0.02 | 0.00 | 1.8 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.22 | 12.05 | 19.73 | 2.00 | 87.8 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 3.96 | 11.80 | 19.23 | 1.00 | 86.5 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.74 | 10.90 | 17.66 | 1.00 | 84.0 | 90.0 |
| Bench 2 | Bench | Maxime Estève | DEF | 3 | 3.9 | 3.15 | 9.09 | 14.49 | 0.00 | 81.1 | 0.0 |
| Bench 3 | Bench | Joe Rodon | DEF | 11 | 4.1 | 2.97 | 8.54 | 13.38 | 2.00 | 78.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.70 | 24.57 | 40.21 | 16.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 3.81 | 11.59 | 19.01 | 1.00 | 78.3 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.9 | 3.53 | 11.38 | 18.16 | 2.00 | 50.4 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.1 | 6.27 | 19.36 | 31.45 | 1.00 | 90.0 | 45.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.8 | 6.38 | 18.48 | 28.50 | 3.00 | 81.1 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.65 | 14.03 | 22.71 | 11.00 | 77.4 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.92 | 11.79 | 18.83 | 4.00 | 77.9 | 90.0 |
| Bench 4 | Bench | Kiernan Dewsbury-Hall | MID | 9 | 5.0 | 1.84 | 7.32 | 12.82 | 0.00 | 32.4 | 0.0 |