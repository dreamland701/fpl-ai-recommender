# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW13
- Simulated weeks: GW14-GW17
- Total predicted points: 269.47
- Total actual points: 262.00
- Average predicted points: 67.37
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
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 65.41
- Actual score: 60.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.34 | 12.38 | 19.70 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Mark Gillespie | GK | 15 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.2 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.52 | 12.99 | 20.42 | 1.00 | 83.6 | 46.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.44 | 12.59 | 20.18 | 1.00 | 85.3 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 4.14 | 11.15 | 18.28 | 8.00 | 82.1 | 90.0 |
| Bench 3 | Bench | Joe Rodon | DEF | 11 | 4.1 | 3.00 | 8.57 | 13.61 | 2.00 | 82.5 | 90.0 |
| Bench 4 | Bench | Maxime Estève | DEF | 3 | 3.9 | 2.85 | 8.17 | 12.79 | 4.00 | 82.3 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.01 | 23.80 | 38.76 | 14.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 5.47 | 15.26 | 24.16 | 2.00 | 88.6 | 63.0 |
| Bench 2 | Bench | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.7 | 3.91 | 13.75 | 22.16 | 1.00 | 69.7 | 30.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 6.15 | 17.46 | 27.97 | 4.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.44 | 15.77 | 25.73 | 3.00 | 87.1 | 82.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.6 | 5.49 | 15.58 | 25.17 | 2.00 | 84.4 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 5.11 | 13.71 | 21.99 | 2.00 | 90.0 | 90.0 |
| XI | XI | Kiernan Dewsbury-Hall | MID | 9 | 4.9 | 4.31 | 12.05 | 18.50 | 3.00 | 83.1 | 90.0 |

## GW15

- Train rows: 171608
- Bank: 0.00 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 61.85
- Actual score: 57.00
- Transfer: Jurriën Timber -> Daniel Muñoz Mejía (projected gain 3.17, hit 0)
- Autosub: Maxime Estève replaced Daniel Muñoz Mejía.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.14 | 12.17 | 19.65 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Mark Gillespie | GK | 15 | 3.9 | 0.28 | 0.19 | 0.25 | 0.00 | 0.2 | 0.0 |
| XI | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.1 | 4.71 | 13.80 | 21.97 | 0.00 | 90.0 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 3.89 | 11.55 | 18.98 | 6.00 | 83.7 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.84 | 11.33 | 18.07 | 2.00 | 86.5 | 90.0 |
| Bench 3 | Autosub In | Maxime Estève | DEF | 3 | 3.9 | 3.36 | 9.35 | 15.08 | 3.00 | 84.5 | 90.0 |
| Bench 4 | Bench | Joe Rodon | DEF | 11 | 4.1 | 2.73 | 7.55 | 12.52 | 1.00 | 77.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.68 | 25.18 | 40.98 | 2.00 | 90.0 | 68.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.7 | 5.04 | 14.76 | 23.74 | 2.00 | 75.1 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 3.93 | 11.91 | 20.00 | 2.00 | 63.0 | 65.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.83 | 16.43 | 27.03 | 18.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.5 | 4.92 | 13.68 | 22.94 | 8.00 | 77.3 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.12 | 12.95 | 22.64 | 6.00 | 72.5 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.05 | 12.45 | 20.27 | 4.00 | 76.8 | 90.0 |
| Bench 2 | Bench | Kiernan Dewsbury-Hall | MID | 9 | 4.9 | 3.64 | 10.80 | 17.44 | 16.00 | 77.8 | 90.0 |

## GW16

- Train rows: 172367
- Bank: 0.30 -> 1.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 73.91
- Actual score: 63.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.21) beats the best remaining Bench Boost opportunity (9.81).
- Transfer: Daniel Muñoz Mejía -> Matty Cash (projected gain 3.79, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.21) beats the best remaining Bench Boost opportunity (9.81).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 5.09 | 13.36 | 21.16 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Mark Gillespie | GK | 15 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Matty Cash | DEF | 2 | 4.9 | 4.77 | 13.46 | 21.06 | 0.00 | 90.0 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.16 | 12.37 | 20.05 | 6.00 | 89.6 | 90.0 |
| XI | XI | Maxime Estève | DEF | 3 | 3.9 | 3.69 | 10.10 | 16.02 | 1.00 | 83.8 | 90.0 |
| Bench 2 | Bench Boost | Maxence Lacroix | DEF | 8 | 5.1 | 3.31 | 9.83 | 16.40 | 1.00 | 82.0 | 90.0 |
| Bench 3 | Bench Boost | Joe Rodon | DEF | 11 | 4.1 | 2.63 | 7.81 | 12.29 | 2.00 | 75.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 7.60 | 23.75 | 39.37 | 13.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.9 | 6.83 | 18.55 | 29.08 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench Boost | Jean-Philippe Mateta | FWD | 8 | 7.9 | 2.27 | 8.07 | 14.99 | 2.00 | 41.8 | 62.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 7.58 | 20.75 | 33.89 | 13.00 | 90.0 | 90.0 |
| XI | XI | Kiernan Dewsbury-Hall | MID | 9 | 5.0 | 4.85 | 14.87 | 22.96 | 1.00 | 90.0 | 15.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.38 | 14.42 | 23.91 | 2.00 | 84.0 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.38 | 12.56 | 20.36 | 3.00 | 79.1 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 3.78 | 10.72 | 19.07 | 2.00 | 62.5 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 1.40 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 68.30
- Actual score: 82.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.81) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Bryan Mbeumo -> Phil Foden (projected gain 8.75, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.81) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Matty Cash replaced Maxime Estève.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.67 | 10.88 | 17.68 | 7.00 | 82.2 | 90.0 |
| Bench 1 | Bench | Mark Gillespie | GK | 15 | 3.9 | 0.08 | 0.00 | 0.02 | 0.00 | 0.4 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 3.86 | 11.53 | 18.81 | 1.00 | 84.5 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.60 | 10.52 | 17.06 | 1.00 | 81.7 | 90.0 |
| Bench 2 | Autosub In | Matty Cash | DEF | 2 | 4.9 | 2.89 | 9.20 | 14.47 | 2.00 | 63.3 | 90.0 |
| XI | Bench | Maxime Estève | DEF | 3 | 3.9 | 3.07 | 9.05 | 14.50 | 0.00 | 78.9 | 0.0 |
| Bench 3 | Bench | Joe Rodon | DEF | 11 | 4.1 | 2.80 | 8.21 | 12.88 | 2.00 | 74.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.81 | 24.89 | 40.71 | 16.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.9 | 3.75 | 12.01 | 19.19 | 2.00 | 50.7 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.8 | 2.91 | 9.50 | 16.83 | 2.00 | 47.2 | 76.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.1 | 6.32 | 19.56 | 31.77 | 1.00 | 90.0 | 45.0 |
| XI | XI | Phil Foden | MID | 13 | 8.9 | 6.11 | 17.91 | 27.67 | 3.00 | 77.6 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.60 | 14.09 | 22.89 | 11.00 | 75.4 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.98 | 12.14 | 19.43 | 4.00 | 76.4 | 90.0 |
| Bench 4 | Bench | Kiernan Dewsbury-Hall | MID | 9 | 5.0 | 1.81 | 7.18 | 12.54 | 0.00 | 32.6 | 0.0 |