# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW13
- Simulated weeks: GW14-GW17
- Total predicted points: 236.20
- Total actual points: 246.00
- Average predicted points: 59.05
- Average actual points: 61.50
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
- Captain: Bryan Mbeumo
- Vice captain: Bruno Borges Fernandes
- Effective captain: Bryan Mbeumo
- Chip used: none
- Predicted score: 57.00
- Actual score: 43.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.91 | 11.53 | 18.38 | 6.00 | 88.0 | 90.0 |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 4.8 | 2.95 | 9.40 | 15.14 | 1.00 | 86.9 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.68 | 13.50 | 21.19 | 1.00 | 85.0 | 46.0 |
| Bench 2 | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 3.76 | 12.65 | 19.86 | 14.00 | 85.7 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 3.94 | 12.60 | 20.15 | 1.00 | 85.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.48 | 11.99 | 19.44 | 4.00 | 90.2 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 4.06 | 11.17 | 18.26 | 8.00 | 87.9 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 4.80 | 14.98 | 23.68 | 2.00 | 81.5 | 63.0 |
| Bench 4 | Bench | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.7 | 3.15 | 12.87 | 20.69 | 1.00 | 75.9 | 30.0 |
| Bench 3 | Bench | Zian Flemming | FWD | 3 | 5.3 | 3.34 | 8.37 | 13.28 | 1.00 | 77.6 | 58.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.31 | 17.21 | 27.48 | 4.00 | 86.2 | 90.0 |
| Captain | Captain | Bryan Mbeumo | MID | 14 | 8.6 | 5.53 | 15.89 | 25.59 | 2.00 | 84.5 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.27 | 15.66 | 25.48 | 3.00 | 82.9 | 82.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.8 | 4.81 | 14.11 | 23.40 | 4.00 | 81.7 | 90.0 |
| XI | XI | Pedro Lomba Neto | MID | 7 | 7.2 | 4.67 | 13.09 | 20.98 | 6.00 | 80.8 | 45.0 |

## GW15

- Train rows: 171608
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Bryan Mbeumo
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 54.11
- Actual score: 68.00
- Transfer: none
- No transfer was applied this week.
- Autosub: Maxence Lacroix replaced Daniel Muñoz Mejía.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.51 | 11.35 | 18.29 | 2.00 | 87.3 | 90.0 |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 4.8 | 2.44 | 8.33 | 13.74 | 10.00 | 86.1 | 90.0 |
| XI | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.02 | 14.44 | 22.97 | 0.00 | 83.6 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 3.82 | 11.72 | 19.22 | 6.00 | 87.1 | 90.0 |
| Bench 2 | Autosub In | Maxence Lacroix | DEF | 8 | 5.1 | 3.58 | 11.44 | 18.24 | 2.00 | 84.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.12 | 11.38 | 18.88 | 2.00 | 85.5 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 3.62 | 11.16 | 18.29 | 3.00 | 74.8 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.7 | 4.41 | 13.86 | 22.28 | 2.00 | 83.8 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 3.81 | 11.59 | 19.46 | 2.00 | 53.3 | 65.0 |
| Bench 4 | Bench | Zian Flemming | FWD | 3 | 5.3 | 2.11 | 7.54 | 12.59 | 5.00 | 48.2 | 4.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 8.9 | 6.67 | 15.96 | 26.28 | 18.00 | 86.5 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.5 | 5.12 | 13.95 | 23.31 | 8.00 | 77.6 | 90.0 |
| Bench 3 | Bench | Declan Rice | MID | 1 | 7.0 | 3.31 | 12.59 | 22.02 | 6.00 | 66.7 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 4.76 | 12.28 | 20.98 | 3.00 | 81.3 | 90.0 |
| XI | XI | Pedro Lomba Neto | MID | 7 | 7.2 | 3.58 | 11.49 | 19.58 | 2.00 | 71.5 | 90.0 |

## GW16

- Train rows: 172367
- Bank: 0.00 -> 3.20
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Declan Rice
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 63.72
- Actual score: 73.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.02) beats the best remaining Triple Captain opportunity (7.07).
- Transfer: Bryan Mbeumo -> Kiernan Dewsbury-Hall (projected gain 4.09, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (6.02) beats the best remaining Triple Captain opportunity (7.07).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.84 | 12.76 | 20.08 | 2.00 | 87.6 | 90.0 |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 4.8 | 3.60 | 9.17 | 15.08 | 6.00 | 87.8 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.63 | 12.61 | 20.43 | 6.00 | 88.6 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 5.31 | 11.60 | 18.98 | 2.00 | 72.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.01 | 11.60 | 18.80 | 6.00 | 83.3 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.18 | 10.04 | 16.73 | 1.00 | 87.9 | 90.0 |
| Bench 4 | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 1.15 | 3.59 | 8.29 | 0.00 | 22.4 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.9 | 5.14 | 18.04 | 28.17 | 2.00 | 85.3 | 90.0 |
| Bench 3 | Bench | Zian Flemming | FWD | 3 | 5.3 | 2.95 | 7.69 | 13.07 | 1.00 | 57.8 | 28.0 |
| Bench 2 | Bench | Jean-Philippe Mateta | FWD | 8 | 7.9 | 3.01 | 7.38 | 13.91 | 2.00 | 46.9 | 62.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.0 | 6.02 | 20.57 | 33.61 | 13.00 | 85.6 | 90.0 |
| XI | XI | Kiernan Dewsbury-Hall | MID | 9 | 5.1 | 3.70 | 14.95 | 23.08 | 1.00 | 85.6 | 15.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.0 | 5.99 | 14.14 | 23.46 | 2.00 | 84.0 | 90.0 |
| XI | XI | Pedro Lomba Neto | MID | 7 | 7.2 | 4.93 | 12.42 | 20.62 | 6.00 | 81.5 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 3.94 | 11.41 | 19.48 | 6.00 | 80.7 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 3.20 -> 2.60
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Harry Wilson
- Effective captain: Antoine Semenyo
- Chip used: bench_boost
- Predicted score: 61.37
- Actual score: 62.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.33) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Kiernan Dewsbury-Hall -> Harry Wilson (projected gain 7.45, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.33) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.81 | 10.19 | 16.47 | 7.00 | 89.0 | 90.0 |
| Bench 1 | Bench Boost | Robert Lynch Sánchez | GK | 7 | 4.8 | 3.03 | 8.61 | 14.32 | 4.00 | 87.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.51 | 11.90 | 19.48 | 2.00 | 88.0 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.07 | 11.72 | 19.10 | 1.00 | 88.1 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.17 | 10.86 | 17.97 | 6.00 | 81.0 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.86 | 10.61 | 17.21 | 1.00 | 84.7 | 90.0 |
| Bench 4 | Bench Boost | Daniel Muñoz Mejía | DEF | 8 | 5.9 | 0.32 | 2.57 | 7.06 | 0.00 | 4.6 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.9 | 3.26 | 10.73 | 17.13 | 2.00 | 71.8 | 90.0 |
| Bench 2 | Bench Boost | Jean-Philippe Mateta | FWD | 8 | 7.8 | 2.96 | 8.73 | 15.59 | 2.00 | 60.0 | 76.0 |
| Bench 3 | Bench Boost | Zian Flemming | FWD | 3 | 5.3 | 2.01 | 7.07 | 12.07 | 1.00 | 52.0 | 64.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.1 | 4.60 | 19.16 | 31.14 | 1.00 | 85.1 | 45.0 |
| Vice Captain | XI | Harry Wilson | MID | 10 | 5.7 | 5.03 | 16.00 | 24.19 | 2.00 | 82.7 | 83.0 |
| Captain | Captain | Antoine Semenyo | MID | 4 | 7.6 | 5.38 | 15.68 | 24.66 | 10.00 | 85.9 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.48 | 13.73 | 22.31 | 11.00 | 84.3 | 90.0 |
| XI | XI | Pedro Lomba Neto | MID | 7 | 7.2 | 4.47 | 12.22 | 20.05 | 2.00 | 82.1 | 90.0 |