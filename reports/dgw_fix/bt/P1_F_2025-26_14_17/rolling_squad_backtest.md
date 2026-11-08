# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW13
- Simulated weeks: GW14-GW17
- Total predicted points: 251.60
- Total actual points: 262.00
- Average predicted points: 62.90
- Average actual points: 65.50
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
- Predicted score: 60.69
- Actual score: 47.00
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.07 | 11.53 | 18.38 | 6.00 | 88.6 | 90.0 |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 4.8 | 3.35 | 9.40 | 15.14 | 1.00 | 82.8 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.74 | 13.50 | 21.19 | 1.00 | 86.8 | 46.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.50 | 12.65 | 19.86 | 14.00 | 83.7 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.45 | 12.60 | 20.15 | 1.00 | 86.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.41 | 11.99 | 19.44 | 4.00 | 89.3 | 90.0 |
| Bench 2 | Bench | Maxence Lacroix | DEF | 8 | 5.1 | 4.14 | 11.17 | 18.26 | 8.00 | 82.1 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 5.38 | 14.98 | 23.68 | 2.00 | 88.2 | 63.0 |
| Bench 3 | Bench | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.7 | 3.58 | 12.87 | 20.69 | 1.00 | 64.9 | 30.0 |
| Bench 4 | Bench | Danny Welbeck | FWD | 6 | 6.6 | 3.12 | 10.43 | 17.14 | 1.00 | 60.9 | 23.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 8.9 | 6.07 | 17.21 | 27.48 | 4.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.6 | 5.63 | 15.89 | 25.59 | 2.00 | 86.3 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.42 | 15.66 | 25.48 | 3.00 | 87.6 | 82.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.8 | 5.09 | 14.11 | 23.40 | 4.00 | 81.3 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.86 | 12.98 | 20.76 | 2.00 | 88.4 | 90.0 |

## GW15

- Train rows: 171608
- Bank: 0.50 -> 0.50
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Bryan Mbeumo
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 54.55
- Actual score: 79.00
- Transfer: Maxence Lacroix -> Marc Guéhi (projected gain 1.80, hit 0)
- Autosub: Elliot Anderson replaced Daniel Muñoz Mejía.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.88 | 11.35 | 18.29 | 2.00 | 88.4 | 90.0 |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 4.8 | 2.78 | 8.33 | 13.74 | 10.00 | 80.2 | 90.0 |
| XI | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.94 | 14.44 | 22.97 | 0.00 | 90.0 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.1 | 4.65 | 13.24 | 20.61 | 8.00 | 90.0 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 3.96 | 11.72 | 19.22 | 6.00 | 85.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.04 | 11.38 | 18.88 | 2.00 | 87.2 | 90.0 |
| Bench 3 | Bench | Jurriën Timber | DEF | 1 | 6.4 | 3.64 | 11.16 | 18.29 | 3.00 | 68.5 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.7 | 4.72 | 13.86 | 22.28 | 2.00 | 71.9 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 3.82 | 11.59 | 19.46 | 2.00 | 61.6 | 65.0 |
| Bench 4 | Bench | Danny Welbeck | FWD | 6 | 6.6 | 3.17 | 9.56 | 16.33 | 2.00 | 50.6 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.66 | 15.96 | 26.28 | 18.00 | 88.6 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.5 | 5.04 | 13.95 | 23.31 | 8.00 | 78.6 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.00 | 12.59 | 22.02 | 6.00 | 70.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 4.18 | 12.28 | 20.98 | 3.00 | 67.3 | 90.0 |
| Bench 2 | Autosub In | Elliot Anderson | MID | 16 | 5.4 | 3.81 | 11.73 | 19.09 | 4.00 | 74.7 | 90.0 |

## GW16

- Train rows: 172367
- Bank: 0.50 -> 0.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 70.78
- Actual score: 80.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.53) beats the best remaining Triple Captain opportunity (8.49).
- Transfer: Bryan Mbeumo -> Phil Foden (projected gain 7.53, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (7.53) beats the best remaining Triple Captain opportunity (8.49).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.91 | 12.76 | 20.08 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 4.8 | 3.13 | 9.17 | 15.08 | 6.00 | 88.6 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.1 | 4.85 | 13.83 | 21.92 | 1.00 | 90.0 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.26 | 12.61 | 20.43 | 6.00 | 90.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.41 | 11.60 | 18.98 | 2.00 | 80.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.08 | 11.60 | 18.80 | 6.00 | 83.9 | 90.0 |
| Bench 4 | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 0.60 | 3.59 | 8.29 | 0.00 | 14.2 | 0.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.9 | 6.69 | 18.04 | 28.17 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Danny Welbeck | FWD | 6 | 6.5 | 2.77 | 8.52 | 14.64 | 1.00 | 55.0 | 8.0 |
| Bench 3 | Bench | Jean-Philippe Mateta | FWD | 8 | 7.9 | 2.00 | 7.38 | 13.91 | 2.00 | 36.9 | 62.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.0 | 7.53 | 20.57 | 33.61 | 13.00 | 90.0 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.7 | 5.75 | 18.39 | 28.57 | 11.00 | 84.5 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.29 | 14.14 | 23.46 | 2.00 | 82.9 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.14 | 11.86 | 19.27 | 3.00 | 76.5 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 3.82 | 11.41 | 19.48 | 6.00 | 67.5 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 0.10 -> 0.40
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Bruno Borges Fernandes
- Effective captain: Phil Foden
- Chip used: bench_boost
- Predicted score: 65.59
- Actual score: 56.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.72) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Jean-Philippe Mateta -> Jarrod Bowen (projected gain 0.91, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.72) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.46 | 10.19 | 16.47 | 7.00 | 80.6 | 90.0 |
| Bench 1 | Bench Boost | Robert Lynch Sánchez | GK | 7 | 4.8 | 2.80 | 8.61 | 14.32 | 4.00 | 82.5 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.2 | 4.76 | 13.29 | 20.91 | 1.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.16 | 11.90 | 19.48 | 2.00 | 86.7 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 3.94 | 11.72 | 19.10 | 1.00 | 86.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 3.72 | 10.86 | 17.97 | 6.00 | 73.9 | 90.0 |
| Bench 4 | Bench Boost | Daniel Muñoz Mejía | DEF | 8 | 5.9 | 0.50 | 2.57 | 7.06 | 0.00 | 6.4 | 0.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 3.68 | 11.37 | 18.68 | 1.00 | 75.1 | 90.0 |
| Bench 2 | Bench Boost | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.9 | 3.30 | 10.73 | 17.13 | 2.00 | 45.3 | 90.0 |
| Bench 3 | Bench Boost | Danny Welbeck | FWD | 6 | 6.5 | 2.11 | 6.34 | 11.50 | 0.00 | 28.7 | 0.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.1 | 6.19 | 19.16 | 31.14 | 1.00 | 90.0 | 45.0 |
| Captain | Captain | Phil Foden | MID | 13 | 8.8 | 6.33 | 18.43 | 28.43 | 3.00 | 79.5 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 6.05 | 15.68 | 24.66 | 10.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.50 | 13.73 | 22.31 | 11.00 | 73.8 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.75 | 11.48 | 18.39 | 4.00 | 73.9 | 90.0 |