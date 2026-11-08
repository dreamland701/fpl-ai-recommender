# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW13
- Simulated weeks: GW14-GW17
- Total predicted points: 261.82
- Total actual points: 286.00
- Average predicted points: 65.45
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
- Predicted score: 64.42
- Actual score: 73.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.00 | 11.63 | 18.40 | 6.00 | 88.8 | 90.0 |
| Bench 1 | Bench | Dermot Mee | GK | 14 | 3.9 | 0.15 | 0.11 | 0.00 | 0.00 | 2.5 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.81 | 13.64 | 21.60 | 1.00 | 88.3 | 46.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.63 | 12.85 | 20.23 | 14.00 | 85.4 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 4.24 | 11.35 | 18.51 | 8.00 | 83.5 | 90.0 |
| Bench 3 | Bench | Nordi Mukiele | DEF | 17 | 4.2 | 3.12 | 9.52 | 15.05 | 0.00 | 81.8 | 90.0 |
| Bench 4 | Bench | Quilindschy Hartman | DEF | 3 | 4.0 | 2.91 | 8.15 | 13.06 | 2.00 | 79.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 7.62 | 23.57 | 38.47 | 14.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 5.28 | 14.74 | 23.59 | 2.00 | 86.3 | 63.0 |
| Bench 2 | Bench | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.7 | 3.74 | 12.94 | 21.70 | 1.00 | 69.8 | 30.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 6.01 | 17.13 | 27.21 | 4.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.50 | 15.80 | 25.86 | 3.00 | 89.4 | 82.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.6 | 5.60 | 15.74 | 25.29 | 2.00 | 86.6 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.73 | 12.48 | 20.13 | 2.00 | 88.2 | 90.0 |
| XI | XI | Kiernan Dewsbury-Hall | MID | 9 | 4.9 | 4.38 | 11.71 | 17.82 | 3.00 | 84.4 | 90.0 |

## GW15

- Train rows: 171608
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 59.64
- Actual score: 55.00
- Transfer: Jurriën Timber -> Marc Cucurella Saseta (projected gain 0.62, hit 0)
- Autosub: Nordi Mukiele replaced Daniel Muñoz Mejía.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.75 | 11.21 | 18.11 | 2.00 | 88.9 | 90.0 |
| Bench 1 | Bench | Dermot Mee | GK | 14 | 3.9 | 0.12 | 0.09 | 0.28 | 0.00 | 2.9 | 0.0 |
| XI | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.89 | 14.68 | 23.43 | 0.00 | 90.0 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 3.84 | 11.77 | 19.35 | 6.00 | 84.3 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.89 | 11.65 | 18.51 | 2.00 | 88.0 | 90.0 |
| Bench 3 | Autosub In | Nordi Mukiele | DEF | 17 | 4.2 | 2.92 | 9.02 | 14.40 | 1.00 | 81.3 | 90.0 |
| Bench 4 | Bench | Quilindschy Hartman | DEF | 3 | 4.0 | 2.71 | 7.61 | 12.47 | 0.00 | 78.1 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.21 | 24.70 | 39.87 | 2.00 | 90.0 | 68.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.7 | 4.67 | 13.56 | 22.35 | 2.00 | 70.2 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 3.76 | 11.58 | 19.78 | 2.00 | 60.4 | 65.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.70 | 15.76 | 26.00 | 18.00 | 88.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.5 | 4.95 | 13.87 | 23.23 | 8.00 | 79.3 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 3.99 | 12.64 | 22.31 | 6.00 | 74.1 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.78 | 11.48 | 18.82 | 4.00 | 77.8 | 90.0 |
| Bench 2 | Bench | Kiernan Dewsbury-Hall | MID | 9 | 4.9 | 3.74 | 10.81 | 17.61 | 16.00 | 78.9 | 90.0 |

## GW16

- Train rows: 172367
- Bank: 0.20 -> 1.30
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Erling Haaland
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 70.98
- Actual score: 72.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.76) beats the best remaining Bench Boost opportunity (7.55).
- Transfer: Daniel Muñoz Mejía -> Matty Cash (projected gain 4.43, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.76) beats the best remaining Bench Boost opportunity (7.55).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.69 | 12.31 | 19.20 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Dermot Mee | GK | 14 | 3.9 | 0.00 | 0.00 | 0.05 | 0.00 | 1.5 | 0.0 |
| XI | XI | Matty Cash | DEF | 2 | 4.9 | 5.00 | 13.66 | 21.38 | 0.00 | 90.0 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.14 | 12.67 | 20.57 | 6.00 | 90.0 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.47 | 10.26 | 17.24 | 1.00 | 84.3 | 90.0 |
| Bench 2 | Bench Boost | Nordi Mukiele | DEF | 17 | 4.2 | 3.26 | 9.45 | 14.74 | 8.00 | 79.3 | 90.0 |
| Bench 4 | Bench Boost | Quilindschy Hartman | DEF | 3 | 4.0 | 1.46 | 4.35 | 8.07 | 4.00 | 40.6 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.9 | 7.39 | 23.28 | 38.33 | 13.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.9 | 6.85 | 17.51 | 27.07 | 2.00 | 90.0 | 90.0 |
| Bench 3 | Bench Boost | Jean-Philippe Mateta | FWD | 8 | 7.9 | 2.04 | 8.34 | 15.27 | 2.00 | 42.6 | 62.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.0 | 7.43 | 20.03 | 32.68 | 13.00 | 90.0 | 90.0 |
| XI | XI | Kiernan Dewsbury-Hall | MID | 9 | 5.0 | 4.89 | 14.99 | 23.42 | 1.00 | 90.0 | 15.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.20 | 14.14 | 23.01 | 2.00 | 85.3 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.09 | 11.84 | 19.05 | 3.00 | 78.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 3.63 | 11.06 | 19.39 | 2.00 | 65.5 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 1.30 -> 0.60
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 66.77
- Actual score: 86.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.31) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Bryan Mbeumo -> Phil Foden (projected gain 8.06, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.31) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.28 | 9.60 | 15.46 | 7.00 | 80.5 | 90.0 |
| Bench 1 | Bench | Dermot Mee | GK | 14 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.5 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 3.84 | 11.67 | 18.69 | 1.00 | 86.5 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.80 | 10.96 | 17.75 | 1.00 | 83.0 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.2 | 3.15 | 9.54 | 14.80 | 6.00 | 81.7 | 90.0 |
| Bench 2 | Bench | Matty Cash | DEF | 2 | 4.9 | 3.13 | 9.33 | 14.90 | 2.00 | 67.4 | 90.0 |
| Bench 3 | Bench | Quilindschy Hartman | DEF | 3 | 4.0 | 2.25 | 6.86 | 10.98 | 0.00 | 64.6 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.31 | 23.87 | 38.15 | 16.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.9 | 3.53 | 10.80 | 16.87 | 2.00 | 52.1 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.8 | 3.19 | 8.99 | 15.49 | 2.00 | 54.1 | 76.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.1 | 6.16 | 18.14 | 30.33 | 1.00 | 90.0 | 45.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.9 | 6.52 | 17.29 | 26.73 | 3.00 | 81.8 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.57 | 13.60 | 22.04 | 11.00 | 77.5 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.79 | 11.78 | 18.54 | 4.00 | 76.6 | 90.0 |
| Bench 4 | Bench | Kiernan Dewsbury-Hall | MID | 9 | 5.0 | 1.93 | 7.22 | 13.00 | 0.00 | 34.0 | 0.0 |