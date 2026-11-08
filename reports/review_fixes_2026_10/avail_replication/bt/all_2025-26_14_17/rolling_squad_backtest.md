# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW13
- Simulated weeks: GW14-GW17
- Total predicted points: 207.97
- Total actual points: 261.00
- Average predicted points: 51.99
- Average actual points: 65.25
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
- Captain: Bryan Mbeumo
- Vice captain: Bruno Borges Fernandes
- Effective captain: Bryan Mbeumo
- Chip used: none
- Predicted score: 51.90
- Actual score: 45.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.45 | 10.13 | 15.78 | 6.00 | 93.3 | 90.0 |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 4.8 | 2.58 | 7.90 | 12.94 | 1.00 | 86.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.01 | 12.50 | 19.19 | 1.00 | 92.9 | 46.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 3.61 | 11.65 | 17.86 | 14.00 | 86.3 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 3.69 | 11.50 | 17.85 | 1.00 | 89.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 3.92 | 10.59 | 17.44 | 4.00 | 91.4 | 90.0 |
| Bench 2 | Bench | Maxence Lacroix | DEF | 8 | 5.1 | 3.54 | 9.77 | 16.06 | 8.00 | 84.4 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 4.51 | 13.48 | 21.58 | 2.00 | 93.9 | 63.0 |
| Bench 4 | Bench | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.7 | 2.43 | 10.87 | 19.59 | 1.00 | 63.5 | 30.0 |
| Bench 3 | Bench | Danny Welbeck | FWD | 6 | 6.6 | 2.63 | 9.23 | 14.94 | 1.00 | 69.4 | 23.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.05 | 16.31 | 26.18 | 4.00 | 100.5 | 90.0 |
| Captain | Captain | Bryan Mbeumo | MID | 14 | 8.6 | 5.16 | 14.69 | 23.49 | 2.00 | 89.4 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.72 | 14.46 | 23.88 | 3.00 | 90.3 | 82.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.8 | 4.20 | 12.01 | 22.10 | 4.00 | 90.4 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.43 | 11.68 | 18.36 | 2.00 | 89.2 | 90.0 |

## GW15

- Train rows: 171608
- Bank: 0.50 -> 1.50
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Bryan Mbeumo
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 44.40
- Actual score: 80.00
- Transfer: Jurriën Timber -> James Tarkowski (projected gain 0.01, hit 0)
- Autosub: James Tarkowski replaced Daniel Muñoz Mejía.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.20 | 10.05 | 16.29 | 2.00 | 91.4 | 90.0 |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 4.8 | 2.34 | 6.93 | 11.24 | 10.00 | 81.7 | 90.0 |
| XI | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 3.82 | 12.34 | 21.97 | 0.00 | 93.7 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 3.10 | 10.22 | 17.22 | 6.00 | 84.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 3.16 | 9.88 | 16.58 | 2.00 | 86.4 | 90.0 |
| Bench 2 | Autosub In | James Tarkowski | DEF | 9 | 5.4 | 2.84 | 9.80 | 15.74 | 9.00 | 88.7 | 90.0 |
| Bench 3 | Bench | Maxence Lacroix | DEF | 8 | 5.1 | 2.81 | 7.94 | 12.94 | 2.00 | 85.9 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.7 | 4.17 | 12.36 | 19.88 | 2.00 | 81.2 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 2.90 | 10.59 | 17.46 | 2.00 | 67.2 | 65.0 |
| Bench 4 | Bench | Danny Welbeck | FWD | 6 | 6.6 | 2.41 | 8.36 | 13.93 | 2.00 | 36.5 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.90 | 14.46 | 23.98 | 18.00 | 91.6 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.5 | 4.45 | 12.85 | 21.11 | 8.00 | 79.8 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 3.31 | 11.39 | 19.82 | 6.00 | 72.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 3.41 | 11.08 | 18.78 | 3.00 | 67.1 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.09 | 10.33 | 16.99 | 4.00 | 76.8 | 90.0 |

## GW16

- Train rows: 172367
- Bank: 1.50 -> 0.40
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 59.41
- Actual score: 75.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.36) beats the best remaining Triple Captain opportunity (8.02).
- Transfer: Antoine Semenyo -> Phil Foden (projected gain 7.98, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (6.36) beats the best remaining Triple Captain opportunity (8.02).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.54 | 11.46 | 17.98 | 2.00 | 101.3 | 90.0 |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 4.8 | 2.30 | 7.57 | 12.98 | 6.00 | 88.9 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 3.74 | 11.61 | 18.13 | 6.00 | 92.3 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.4 | 3.23 | 10.59 | 16.73 | 1.00 | 86.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.46 | 10.30 | 16.20 | 6.00 | 82.8 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 2.44 | 7.54 | 12.63 | 1.00 | 84.8 | 90.0 |
| Bench 4 | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.0 | -0.48 | 1.59 | 4.49 | 0.00 | 17.2 | 0.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.9 | 6.32 | 17.04 | 25.97 | 2.00 | 114.5 | 90.0 |
| Bench 2 | Bench | Danny Welbeck | FWD | 6 | 6.5 | 2.12 | 7.12 | 12.44 | 1.00 | 61.1 | 8.0 |
| Bench 3 | Bench | Jean-Philippe Mateta | FWD | 8 | 7.9 | 0.69 | 6.08 | 11.11 | 2.00 | 27.0 | 62.0 |
| XI | XI | Phil Foden | MID | 13 | 8.7 | 5.93 | 17.09 | 26.47 | 11.00 | 99.9 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.0 | 6.36 | 16.57 | 27.61 | 13.00 | 116.9 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.31 | 11.34 | 18.86 | 2.00 | 85.1 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.68 | 10.76 | 16.87 | 3.00 | 76.9 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 2.67 | 9.46 | 16.99 | 2.00 | 56.6 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 0.40 -> 1.00
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Bruno Borges Fernandes
- Effective captain: Antoine Semenyo
- Chip used: bench_boost
- Predicted score: 52.27
- Actual score: 61.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.58) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Bryan Mbeumo -> Antoine Semenyo (projected gain 9.30, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.58) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 2.73 | 8.69 | 14.07 | 7.00 | 82.6 | 90.0 |
| Bench 1 | Bench Boost | Robert Lynch Sánchez | GK | 7 | 4.8 | 2.35 | 7.51 | 12.32 | 4.00 | 83.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.33 | 10.90 | 17.38 | 2.00 | 87.0 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 3.10 | 10.42 | 16.50 | 1.00 | 86.4 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.14 | 9.01 | 14.31 | 1.00 | 85.0 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.4 | 2.67 | 8.27 | 14.31 | 3.00 | 79.9 | 90.0 |
| Bench 4 | Bench Boost | Daniel Muñoz Mejía | DEF | 8 | 5.9 | -0.23 | 0.57 | 3.26 | 0.00 | 0.0 | 0.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.8 | 2.54 | 7.23 | 12.69 | 2.00 | 59.8 | 76.0 |
| Bench 2 | Bench Boost | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.9 | 1.89 | 6.73 | 11.13 | 2.00 | 21.7 | 90.0 |
| Bench 3 | Bench Boost | Danny Welbeck | FWD | 6 | 6.5 | 1.56 | 4.84 | 8.80 | 0.00 | 15.3 | 0.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.1 | 5.18 | 17.16 | 29.64 | 1.00 | 88.8 | 45.0 |
| Captain | Captain | Antoine Semenyo | MID | 4 | 7.6 | 5.88 | 14.48 | 22.66 | 10.00 | 100.8 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.8 | 5.09 | 14.43 | 22.43 | 3.00 | 81.4 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.04 | 12.13 | 20.31 | 11.00 | 78.5 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.11 | 9.98 | 15.69 | 4.00 | 77.5 | 90.0 |