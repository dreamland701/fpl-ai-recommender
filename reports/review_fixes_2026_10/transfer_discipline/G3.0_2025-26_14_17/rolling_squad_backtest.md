# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW13
- Simulated weeks: GW14-GW17
- Total predicted points: 249.89
- Total actual points: 257.00
- Average predicted points: 62.47
- Average actual points: 64.25
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
- Vice captain: Bryan Mbeumo
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 61.59
- Actual score: 47.00
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.15 | 11.53 | 18.38 | 6.00 | 90.3 | 90.0 |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 4.8 | 3.38 | 9.40 | 15.14 | 1.00 | 83.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.91 | 13.50 | 21.19 | 1.00 | 89.9 | 46.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.51 | 12.65 | 19.86 | 14.00 | 83.3 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.49 | 12.60 | 20.15 | 1.00 | 87.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.42 | 11.99 | 19.44 | 4.00 | 90.4 | 90.0 |
| Bench 2 | Bench | Maxence Lacroix | DEF | 8 | 5.1 | 4.14 | 11.17 | 18.26 | 8.00 | 81.4 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 5.51 | 14.98 | 23.68 | 2.00 | 90.9 | 63.0 |
| Bench 3 | Bench | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.7 | 3.53 | 12.87 | 20.69 | 1.00 | 62.5 | 30.0 |
| Bench 4 | Bench | Danny Welbeck | FWD | 6 | 6.6 | 3.13 | 10.43 | 17.14 | 1.00 | 60.4 | 23.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 8.9 | 6.15 | 17.21 | 27.48 | 4.00 | 99.5 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.6 | 5.66 | 15.89 | 25.59 | 2.00 | 87.4 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.52 | 15.66 | 25.48 | 3.00 | 89.3 | 82.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.8 | 5.20 | 14.11 | 23.40 | 4.00 | 84.4 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.93 | 12.98 | 20.76 | 2.00 | 89.2 | 90.0 |

## GW15

- Train rows: 171608
- Bank: 0.50 -> 0.50
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Bryan Mbeumo
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 53.32
- Actual score: 73.00
- Transfer: none
- No transfer was applied this week.
- Autosub: Jean-Philippe Mateta replaced Daniel Muñoz Mejía.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.90 | 11.35 | 18.29 | 2.00 | 89.4 | 90.0 |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 4.8 | 2.74 | 8.33 | 13.74 | 10.00 | 78.7 | 90.0 |
| XI | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.92 | 14.44 | 22.97 | 0.00 | 94.7 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 3.90 | 11.72 | 19.22 | 6.00 | 83.7 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.81 | 11.44 | 18.24 | 2.00 | 84.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 3.96 | 11.38 | 18.88 | 2.00 | 86.4 | 90.0 |
| Bench 3 | Bench | Jurriën Timber | DEF | 1 | 6.4 | 3.66 | 11.16 | 18.29 | 3.00 | 68.9 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.7 | 4.87 | 13.86 | 22.28 | 2.00 | 73.2 | 90.0 |
| Bench 2 | Autosub In | Jean-Philippe Mateta | FWD | 8 | 8.1 | 3.70 | 11.59 | 19.46 | 2.00 | 60.2 | 65.0 |
| Bench 4 | Bench | Danny Welbeck | FWD | 6 | 6.6 | 3.21 | 9.56 | 16.33 | 2.00 | 50.5 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.70 | 15.96 | 26.28 | 18.00 | 89.6 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.5 | 4.95 | 13.95 | 23.31 | 8.00 | 77.8 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 3.91 | 12.59 | 22.02 | 6.00 | 69.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 3.91 | 12.28 | 20.98 | 3.00 | 64.1 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.79 | 11.73 | 19.09 | 4.00 | 73.8 | 90.0 |

## GW16

- Train rows: 172367
- Bank: 0.50 -> 0.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 71.02
- Actual score: 80.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.86) beats the best remaining Triple Captain opportunity (9.16).
- Transfer: Bryan Mbeumo -> Phil Foden (projected gain 7.53, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (7.86) beats the best remaining Triple Captain opportunity (9.16).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 5.04 | 12.76 | 20.08 | 2.00 | 100.3 | 90.0 |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 4.8 | 3.10 | 9.17 | 15.08 | 6.00 | 87.9 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.24 | 12.61 | 20.43 | 6.00 | 91.3 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.30 | 11.60 | 18.98 | 2.00 | 78.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.96 | 11.60 | 18.80 | 6.00 | 82.8 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.34 | 10.04 | 16.73 | 1.00 | 81.8 | 90.0 |
| Bench 4 | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 0.02 | 3.59 | 8.29 | 0.00 | 3.2 | 0.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.9 | 7.22 | 18.04 | 28.17 | 2.00 | 109.5 | 90.0 |
| Bench 2 | Bench | Danny Welbeck | FWD | 6 | 6.5 | 2.62 | 8.52 | 14.64 | 1.00 | 52.1 | 8.0 |
| Bench 3 | Bench | Jean-Philippe Mateta | FWD | 8 | 7.9 | 1.49 | 7.38 | 13.91 | 2.00 | 28.0 | 62.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.0 | 7.86 | 20.57 | 33.61 | 13.00 | 119.9 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.7 | 6.33 | 18.39 | 28.57 | 11.00 | 93.9 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.31 | 14.14 | 23.46 | 2.00 | 83.1 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.08 | 11.86 | 19.27 | 3.00 | 74.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 3.62 | 11.41 | 19.48 | 6.00 | 65.0 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Antoine Semenyo
- Effective captain: Phil Foden
- Chip used: bench_boost
- Predicted score: 63.96
- Actual score: 57.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.93) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.93) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.43 | 10.19 | 16.47 | 7.00 | 80.6 | 90.0 |
| Bench 1 | Bench Boost | Robert Lynch Sánchez | GK | 7 | 4.8 | 2.75 | 8.61 | 14.32 | 4.00 | 81.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.13 | 11.90 | 19.48 | 2.00 | 86.0 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 3.90 | 11.72 | 19.10 | 1.00 | 85.4 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 3.75 | 10.86 | 17.97 | 6.00 | 74.0 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.64 | 10.61 | 17.21 | 1.00 | 82.0 | 90.0 |
| Bench 4 | Bench Boost | Daniel Muñoz Mejía | DEF | 8 | 5.9 | 0.37 | 2.57 | 7.06 | 0.00 | 2.2 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.9 | 3.19 | 10.73 | 17.13 | 2.00 | 41.7 | 90.0 |
| Bench 2 | Bench Boost | Jean-Philippe Mateta | FWD | 8 | 7.8 | 2.74 | 8.73 | 15.59 | 2.00 | 42.8 | 76.0 |
| Bench 3 | Bench Boost | Danny Welbeck | FWD | 6 | 6.5 | 2.06 | 6.34 | 11.50 | 0.00 | 27.3 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.1 | 6.28 | 19.16 | 31.14 | 1.00 | 90.8 | 45.0 |
| Captain | Captain | Phil Foden | MID | 13 | 8.8 | 6.59 | 18.43 | 28.43 | 3.00 | 82.4 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.6 | 6.28 | 15.68 | 24.66 | 10.00 | 98.8 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.54 | 13.73 | 22.31 | 11.00 | 74.5 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.71 | 11.48 | 18.39 | 4.00 | 73.5 | 90.0 |