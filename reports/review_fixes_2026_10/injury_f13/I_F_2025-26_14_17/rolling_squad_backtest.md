# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW13
- Simulated weeks: GW14-GW17
- Total predicted points: 254.87
- Total actual points: 263.00
- Average predicted points: 63.72
- Average actual points: 65.75
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
- Bank: 100.00 -> 0.50
- Free transfers: 1 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Declan Rice
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 61.61
- Actual score: 47.00
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.10 | 11.44 | 18.28 | 6.00 | 91.0 | 90.0 |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 4.8 | 3.36 | 9.38 | 15.13 | 1.00 | 82.7 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.89 | 13.49 | 21.18 | 1.00 | 89.5 | 46.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.53 | 12.68 | 20.22 | 1.00 | 86.8 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.47 | 12.58 | 19.79 | 14.00 | 83.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.38 | 11.90 | 19.32 | 4.00 | 90.9 | 90.0 |
| Bench 2 | Bench | Maxence Lacroix | DEF | 8 | 5.1 | 4.12 | 11.14 | 18.23 | 8.00 | 81.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 5.44 | 14.82 | 23.48 | 2.00 | 91.6 | 63.0 |
| Bench 3 | Bench | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.7 | 3.63 | 13.06 | 20.91 | 1.00 | 61.9 | 30.0 |
| Bench 4 | Bench | Danny Welbeck | FWD | 6 | 6.6 | 3.08 | 10.33 | 17.02 | 1.00 | 61.0 | 23.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 8.9 | 6.26 | 17.45 | 27.75 | 4.00 | 98.8 | 90.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.0 | 5.58 | 15.79 | 25.62 | 3.00 | 88.3 | 82.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.6 | 5.53 | 15.59 | 25.21 | 2.00 | 88.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.8 | 5.23 | 14.18 | 23.48 | 4.00 | 83.7 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.92 | 12.98 | 20.75 | 2.00 | 88.6 | 90.0 |

## GW15

- Train rows: 171608
- Bank: 0.50 -> 0.50
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 54.19
- Actual score: 80.00
- Transfer: Maxence Lacroix -> Marc Guéhi (projected gain 1.81, hit 0)
- Autosub: Jurriën Timber replaced Daniel Muñoz Mejía.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.85 | 11.26 | 18.19 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 4.8 | 2.72 | 8.31 | 13.72 | 10.00 | 78.4 | 90.0 |
| XI | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.89 | 14.36 | 22.88 | 0.00 | 95.2 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.1 | 4.58 | 13.22 | 20.61 | 8.00 | 93.5 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 3.94 | 11.79 | 19.28 | 6.00 | 83.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 3.91 | 11.27 | 18.75 | 2.00 | 86.9 | 90.0 |
| Bench 2 | Autosub In | Jurriën Timber | DEF | 1 | 6.4 | 3.64 | 11.14 | 18.28 | 3.00 | 68.6 | 90.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.7 | 4.94 | 14.00 | 22.44 | 2.00 | 72.8 | 90.0 |
| Bench 3 | Bench | Jean-Philippe Mateta | FWD | 8 | 8.1 | 3.63 | 11.44 | 19.27 | 2.00 | 60.8 | 65.0 |
| Bench 4 | Bench | Danny Welbeck | FWD | 6 | 6.6 | 3.28 | 9.69 | 16.47 | 2.00 | 50.1 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.79 | 16.14 | 26.48 | 18.00 | 89.1 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.5 | 4.83 | 13.66 | 22.95 | 8.00 | 78.8 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 3.97 | 12.72 | 22.17 | 6.00 | 68.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 3.91 | 12.30 | 21.02 | 3.00 | 63.6 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.79 | 11.74 | 19.10 | 4.00 | 73.2 | 90.0 |

## GW16

- Train rows: 172367
- Bank: 0.50 -> 0.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 72.83
- Actual score: 80.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.95) beats the best remaining Triple Captain opportunity (9.27).
- Transfer: Bryan Mbeumo -> Phil Foden (projected gain 7.52, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (7.95) beats the best remaining Triple Captain opportunity (9.27).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 5.00 | 12.67 | 19.98 | 2.00 | 100.9 | 90.0 |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 4.8 | 3.09 | 9.16 | 15.07 | 6.00 | 87.6 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.1 | 4.89 | 13.81 | 21.91 | 1.00 | 100.2 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.29 | 12.69 | 20.50 | 6.00 | 91.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.26 | 11.55 | 18.93 | 2.00 | 78.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.92 | 11.50 | 18.69 | 6.00 | 83.2 | 90.0 |
| Bench 4 | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 0.00 | 3.52 | 8.21 | 0.00 | 3.7 | 0.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.9 | 7.30 | 18.22 | 28.38 | 2.00 | 109.1 | 90.0 |
| Bench 2 | Bench | Danny Welbeck | FWD | 6 | 6.5 | 2.58 | 8.43 | 14.53 | 1.00 | 52.6 | 8.0 |
| Bench 3 | Bench | Jean-Philippe Mateta | FWD | 8 | 7.9 | 1.44 | 7.26 | 13.76 | 2.00 | 28.5 | 62.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.0 | 7.95 | 20.76 | 33.84 | 13.00 | 119.4 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.7 | 6.23 | 18.14 | 28.26 | 11.00 | 94.6 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.37 | 14.28 | 23.61 | 2.00 | 82.1 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.07 | 11.85 | 19.26 | 3.00 | 74.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 3.64 | 11.47 | 19.56 | 6.00 | 64.4 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 0.10 -> 0.40
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Bruno Borges Fernandes
- Effective captain: Phil Foden
- Chip used: bench_boost
- Predicted score: 66.24
- Actual score: 56.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.57) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Jean-Philippe Mateta -> Jarrod Bowen (projected gain 0.57, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.57) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.39 | 10.13 | 16.40 | 7.00 | 81.0 | 90.0 |
| Bench 1 | Bench Boost | Robert Lynch Sánchez | GK | 7 | 4.8 | 2.74 | 8.60 | 14.31 | 4.00 | 81.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.2 | 4.86 | 13.29 | 20.93 | 1.00 | 92.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.10 | 11.83 | 19.39 | 2.00 | 86.4 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 3.95 | 11.81 | 19.17 | 1.00 | 85.2 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 3.75 | 10.87 | 17.99 | 6.00 | 73.6 | 90.0 |
| Bench 4 | Bench Boost | Daniel Muñoz Mejía | DEF | 8 | 5.9 | 0.39 | 2.60 | 7.11 | 0.00 | 2.4 | 0.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 3.59 | 11.17 | 18.43 | 1.00 | 75.8 | 90.0 |
| Bench 2 | Bench Boost | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.9 | 3.31 | 10.96 | 17.42 | 2.00 | 41.1 | 90.0 |
| Bench 3 | Bench Boost | Danny Welbeck | FWD | 6 | 6.5 | 2.14 | 6.48 | 11.66 | 0.00 | 27.0 | 0.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.1 | 6.40 | 19.42 | 31.45 | 1.00 | 90.2 | 45.0 |
| Captain | Captain | Phil Foden | MID | 13 | 8.8 | 6.49 | 18.17 | 28.09 | 3.00 | 83.1 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 6.31 | 15.76 | 24.76 | 10.00 | 98.2 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.61 | 13.90 | 22.50 | 11.00 | 73.5 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.71 | 11.51 | 18.41 | 4.00 | 72.9 | 90.0 |