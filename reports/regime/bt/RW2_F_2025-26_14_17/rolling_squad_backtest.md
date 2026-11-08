# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW13
- Simulated weeks: GW14-GW17
- Total predicted points: 264.00
- Total actual points: 286.00
- Average predicted points: 66.00
- Average actual points: 71.50
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
- Predicted score: 64.91
- Actual score: 73.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.02 | 11.55 | 18.28 | 6.00 | 87.6 | 90.0 |
| Bench 1 | Bench | James Wright | GK | 2 | 3.9 | 0.00 | 0.04 | 0.19 | 0.00 | 2.6 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.78 | 13.60 | 21.39 | 1.00 | 87.3 | 46.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.60 | 12.84 | 20.18 | 14.00 | 85.3 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 4.24 | 11.39 | 18.63 | 8.00 | 83.7 | 90.0 |
| Bench 3 | Bench | Nordi Mukiele | DEF | 17 | 4.2 | 3.07 | 9.30 | 14.75 | 0.00 | 81.7 | 90.0 |
| Bench 4 | Bench | Quilindschy Hartman | DEF | 3 | 4.0 | 2.86 | 8.08 | 12.93 | 2.00 | 79.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 7.77 | 23.67 | 38.51 | 14.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 5.36 | 14.93 | 23.66 | 2.00 | 87.3 | 63.0 |
| Bench 2 | Bench | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.7 | 3.73 | 13.05 | 21.41 | 1.00 | 69.4 | 30.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 6.10 | 17.33 | 27.57 | 4.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.6 | 5.63 | 15.86 | 25.50 | 2.00 | 86.7 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.48 | 15.75 | 25.70 | 3.00 | 88.5 | 82.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.84 | 12.87 | 20.70 | 2.00 | 88.9 | 90.0 |
| XI | XI | Kiernan Dewsbury-Hall | MID | 9 | 4.9 | 4.34 | 11.79 | 17.97 | 3.00 | 84.1 | 90.0 |

## GW15

- Train rows: 171608
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 60.54
- Actual score: 55.00
- Transfer: Jurriën Timber -> Marc Cucurella Saseta (projected gain 0.67, hit 0)
- Autosub: Nordi Mukiele replaced Daniel Muñoz Mejía.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.77 | 11.22 | 18.12 | 2.00 | 87.5 | 90.0 |
| Bench 1 | Bench | James Wright | GK | 2 | 3.9 | 0.00 | 0.02 | 0.02 | 0.00 | 2.3 | 0.0 |
| XI | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.95 | 14.63 | 23.31 | 0.00 | 90.0 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 3.94 | 11.85 | 19.44 | 6.00 | 84.9 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.92 | 11.61 | 18.48 | 2.00 | 88.0 | 90.0 |
| Bench 3 | Autosub In | Nordi Mukiele | DEF | 17 | 4.2 | 2.87 | 8.85 | 14.16 | 1.00 | 81.6 | 90.0 |
| Bench 4 | Bench | Quilindschy Hartman | DEF | 3 | 4.0 | 2.68 | 7.58 | 12.48 | 0.00 | 78.1 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.38 | 24.81 | 40.17 | 2.00 | 90.0 | 68.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.7 | 4.73 | 13.75 | 22.34 | 2.00 | 71.6 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 3.86 | 11.75 | 19.86 | 2.00 | 62.0 | 65.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.76 | 16.06 | 26.44 | 18.00 | 89.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.5 | 4.98 | 13.94 | 23.37 | 8.00 | 78.8 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.05 | 12.76 | 22.42 | 6.00 | 73.4 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.81 | 11.65 | 19.10 | 4.00 | 76.8 | 90.0 |
| Bench 2 | Bench | Kiernan Dewsbury-Hall | MID | 9 | 4.9 | 3.71 | 10.83 | 17.53 | 16.00 | 78.9 | 90.0 |

## GW16

- Train rows: 172367
- Bank: 0.20 -> 1.30
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Erling Haaland
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 71.50
- Actual score: 72.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.87) beats the best remaining Bench Boost opportunity (7.68).
- Transfer: Daniel Muñoz Mejía -> Matty Cash (projected gain 4.61, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.87) beats the best remaining Bench Boost opportunity (7.68).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.72 | 12.42 | 19.52 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | James Wright | GK | 2 | 3.9 | 0.00 | 0.00 | 0.09 | 0.00 | 1.2 | 0.0 |
| XI | XI | Matty Cash | DEF | 2 | 4.9 | 4.95 | 13.72 | 21.45 | 0.00 | 90.0 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.22 | 12.69 | 20.54 | 6.00 | 90.0 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.47 | 10.24 | 17.14 | 1.00 | 84.2 | 90.0 |
| Bench 2 | Bench Boost | Nordi Mukiele | DEF | 17 | 4.2 | 3.23 | 9.30 | 14.49 | 8.00 | 79.5 | 90.0 |
| Bench 4 | Bench Boost | Quilindschy Hartman | DEF | 3 | 4.0 | 1.51 | 4.44 | 8.20 | 4.00 | 42.3 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.9 | 7.37 | 23.32 | 38.48 | 13.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.9 | 6.67 | 17.49 | 27.25 | 2.00 | 90.0 | 90.0 |
| Bench 3 | Bench Boost | Jean-Philippe Mateta | FWD | 8 | 7.9 | 2.13 | 8.17 | 15.09 | 2.00 | 41.9 | 62.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.0 | 7.52 | 20.40 | 33.26 | 13.00 | 90.0 | 90.0 |
| XI | XI | Kiernan Dewsbury-Hall | MID | 9 | 5.0 | 4.92 | 14.98 | 23.29 | 1.00 | 90.0 | 15.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.29 | 14.25 | 23.41 | 2.00 | 85.0 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.16 | 11.98 | 19.43 | 3.00 | 78.3 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 3.81 | 11.14 | 19.65 | 2.00 | 64.7 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 1.30 -> 0.60
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 67.05
- Actual score: 86.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.46) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Bryan Mbeumo -> Phil Foden (projected gain 8.86, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.46) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.30 | 9.78 | 15.82 | 7.00 | 79.6 | 90.0 |
| Bench 1 | Bench | James Wright | GK | 2 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.7 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 3.89 | 11.70 | 18.92 | 1.00 | 86.5 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.78 | 10.97 | 17.77 | 1.00 | 83.5 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.2 | 3.13 | 9.46 | 14.72 | 6.00 | 81.4 | 90.0 |
| XI | XI | Matty Cash | DEF | 2 | 4.9 | 3.07 | 9.35 | 14.79 | 2.00 | 66.8 | 90.0 |
| Bench 3 | Bench | Quilindschy Hartman | DEF | 3 | 4.0 | 2.21 | 6.78 | 10.99 | 0.00 | 63.8 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.46 | 24.18 | 39.05 | 16.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.9 | 3.41 | 10.67 | 16.93 | 2.00 | 49.6 | 90.0 |
| Bench 2 | Bench | Jean-Philippe Mateta | FWD | 8 | 7.8 | 3.06 | 9.08 | 15.84 | 2.00 | 50.9 | 76.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.1 | 6.23 | 18.69 | 30.78 | 1.00 | 90.0 | 45.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.9 | 6.44 | 17.81 | 27.50 | 3.00 | 81.4 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.57 | 13.78 | 22.37 | 11.00 | 76.7 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.85 | 11.86 | 18.89 | 4.00 | 76.5 | 90.0 |
| Bench 4 | Bench | Kiernan Dewsbury-Hall | MID | 9 | 5.0 | 1.95 | 7.40 | 13.06 | 0.00 | 34.6 | 0.0 |