# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW13
- Simulated weeks: GW14-GW17
- Total predicted points: 250.42
- Total actual points: 275.00
- Average predicted points: 62.60
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
- Vice captain: Bryan Mbeumo
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 65.08
- Actual score: 65.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.86 | 13.66 | 21.95 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Dermot Mee | GK | 14 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 5.29 | 15.53 | 24.33 | 1.00 | 90.0 | 46.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 5.11 | 14.20 | 22.42 | 1.00 | 90.0 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.93 | 14.18 | 22.22 | 14.00 | 87.0 | 90.0 |
| Bench 2 | Bench | Joe Rodon | DEF | 11 | 4.1 | 3.24 | 8.86 | 13.53 | 2.00 | 84.5 | 90.0 |
| Bench 3 | Bench | Quilindschy Hartman | DEF | 3 | 4.0 | 2.71 | 7.35 | 11.38 | 2.00 | 73.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 6.74 | 19.32 | 31.06 | 14.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 4.10 | 12.81 | 21.77 | 2.00 | 66.3 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 2.09 | 5.74 | 9.36 | 2.00 | 33.9 | 60.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.61 | 17.13 | 27.66 | 4.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.6 | 5.74 | 16.11 | 25.88 | 2.00 | 83.6 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.70 | 15.68 | 25.21 | 3.00 | 89.1 | 82.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 5.49 | 14.11 | 22.19 | 2.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 4.78 | 13.82 | 21.44 | 2.00 | 76.8 | 90.0 |

## GW15

- Train rows: 171608
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 59.52
- Actual score: 56.00
- Transfer: Enzo Fernández -> Jérémy Doku (projected gain 0.52, hit 0)
- Autosub: Joe Rodon replaced Daniel Muñoz Mejía.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.41 | 13.06 | 21.16 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Dermot Mee | GK | 14 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 5.38 | 16.13 | 24.99 | 0.00 | 90.0 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.33 | 12.83 | 20.68 | 6.00 | 88.9 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 3.75 | 12.51 | 20.37 | 3.00 | 72.8 | 90.0 |
| Bench 2 | Autosub In | Joe Rodon | DEF | 11 | 4.1 | 2.86 | 7.88 | 12.62 | 1.00 | 77.5 | 90.0 |
| Bench 3 | Bench | Quilindschy Hartman | DEF | 3 | 4.0 | 2.61 | 7.32 | 11.71 | 0.00 | 75.8 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 7.30 | 21.25 | 34.56 | 2.00 | 90.0 | 68.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 3.72 | 12.02 | 20.66 | 1.00 | 72.8 | 32.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 2.45 | 6.53 | 10.19 | 0.00 | 49.4 | 0.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 6.01 | 16.39 | 27.06 | 18.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.5 | 5.12 | 14.17 | 23.71 | 8.00 | 78.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.37 | 12.67 | 21.96 | 6.00 | 76.2 | 90.0 |
| XI | XI | Jérémy Doku | MID | 13 | 6.6 | 4.12 | 12.23 | 19.90 | 3.00 | 62.1 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.72 | 12.03 | 19.50 | 4.00 | 80.3 | 90.0 |

## GW16

- Train rows: 172367
- Bank: 0.10 -> 0.30
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Erling Haaland
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 64.86
- Actual score: 69.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (2.83) beats the best remaining Bench Boost opportunity (3.47).
- Transfer: João Pedro Junqueira de Jesus -> Igor Thiago Nascimento Rodrigues (projected gain 6.62, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (2.83) beats the best remaining Bench Boost opportunity (3.47).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 5.39 | 14.31 | 23.20 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Dermot Mee | GK | 14 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.69 | 13.98 | 21.99 | 6.00 | 90.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.67 | 12.47 | 20.06 | 2.00 | 86.1 | 90.0 |
| XI | XI | Joe Rodon | DEF | 11 | 4.1 | 3.21 | 8.59 | 13.16 | 2.00 | 76.2 | 90.0 |
| Bench 2 | Bench Boost | Quilindschy Hartman | DEF | 3 | 4.0 | 1.42 | 4.08 | 7.48 | 4.00 | 40.8 | 90.0 |
| Bench 4 | Bench Boost | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 0.27 | 3.67 | 7.90 | 0.00 | 15.9 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.9 | 6.18 | 19.83 | 33.00 | 13.00 | 85.5 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.21 | 16.60 | 26.33 | 2.00 | 90.0 | 90.0 |
| Bench 3 | Bench Boost | Junior Kroupi | FWD | 4 | 4.6 | 1.14 | 4.65 | 8.21 | 5.00 | 22.7 | 12.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.0 | 7.79 | 20.83 | 33.75 | 13.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.18 | 14.18 | 23.41 | 2.00 | 83.4 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.11 | 12.25 | 19.62 | 3.00 | 81.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 4.17 | 11.54 | 20.66 | 2.00 | 65.8 | 90.0 |
| XI | XI | Jérémy Doku | MID | 13 | 6.6 | 3.67 | 11.49 | 19.44 | 0.00 | 60.7 | 0.0 |

## GW17

- Train rows: 173127
- Bank: 0.30 -> 1.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 60.96
- Actual score: 85.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.19) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Jérémy Doku -> Harry Wilson (projected gain 8.27, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (7.19) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Junior Kroupi replaced Bryan Mbeumo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.23 | 11.19 | 18.87 | 7.00 | 87.0 | 90.0 |
| Bench 1 | Bench | Dermot Mee | GK | 14 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.09 | 12.43 | 19.78 | 1.00 | 88.9 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 3.89 | 11.54 | 19.46 | 6.00 | 79.2 | 90.0 |
| XI | XI | Joe Rodon | DEF | 11 | 4.1 | 3.44 | 9.25 | 14.15 | 2.00 | 75.2 | 90.0 |
| Bench 2 | Bench | Quilindschy Hartman | DEF | 3 | 4.0 | 2.23 | 6.47 | 10.56 | 0.00 | 62.8 | 0.0 |
| Bench 4 | Bench | Daniel Muñoz Mejía | DEF | 8 | 5.9 | 1.02 | 3.06 | 8.53 | 0.00 | 22.0 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 7.19 | 20.93 | 35.07 | 16.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 2.75 | 11.09 | 17.61 | 2.00 | 59.1 | 90.0 |
| Bench 3 | Autosub In | Junior Kroupi | FWD | 4 | 4.6 | 1.89 | 5.52 | 9.55 | 1.00 | 25.0 | 26.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.1 | 6.84 | 19.90 | 32.12 | 1.00 | 90.0 | 45.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.7 | 5.09 | 14.88 | 22.58 | 2.00 | 90.0 | 83.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.02 | 13.31 | 21.48 | 11.00 | 75.9 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.52 | 11.59 | 18.36 | 4.00 | 74.4 | 90.0 |
| XI | Bench | Bryan Mbeumo | MID | 14 | 8.2 | 2.51 | 9.03 | 17.42 | 0.00 | 48.0 | 0.0 |