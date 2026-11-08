# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW13
- Simulated weeks: GW14-GW17
- Total predicted points: 260.79
- Total actual points: 247.00
- Average predicted points: 65.20
- Average actual points: 61.75
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
- Bank: 100.00 -> 0.20
- Free transfers: 1 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Bukayo Saka
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 61.41
- Actual score: 50.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.20 | 11.66 | 18.61 | 6.00 | 91.4 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.42 | 9.36 | 15.05 | 2.00 | 96.5 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.94 | 13.61 | 21.38 | 1.00 | 90.4 | 46.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.41 | 12.61 | 20.25 | 1.00 | 88.9 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.38 | 12.56 | 19.86 | 14.00 | 86.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.47 | 12.09 | 19.61 | 4.00 | 91.5 | 90.0 |
| Bench 2 | Bench | Marc Guéhi | DEF | 8 | 5.1 | 4.20 | 11.32 | 18.55 | 14.00 | 81.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 5.52 | 15.10 | 24.00 | 2.00 | 94.3 | 63.0 |
| Bench 3 | Bench | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.7 | 3.89 | 12.85 | 20.63 | 1.00 | 64.1 | 30.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 2.33 | 7.41 | 12.71 | 2.00 | 35.4 | 60.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 8.9 | 6.05 | 17.07 | 27.31 | 4.00 | 99.3 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 10.1 | 5.85 | 16.98 | 27.28 | 6.00 | 89.8 | 29.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.6 | 5.59 | 15.87 | 25.59 | 2.00 | 87.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.8 | 5.19 | 14.16 | 23.49 | 4.00 | 84.5 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.76 | 13.02 | 20.92 | 2.00 | 90.8 | 90.0 |

## GW15

- Train rows: 171608
- Bank: 0.20 -> 0.80
- Free transfers: 2 -> 2
- Captain: Nick Woltemade
- Vice captain: Bruno Borges Fernandes
- Effective captain: Nick Woltemade
- Chip used: none
- Predicted score: 57.45
- Actual score: 61.00
- Transfer: Jean-Philippe Mateta -> Nick Woltemade (projected gain 3.07, hit 0)
- Autosub: Marc Cucurella Saseta replaced Daniel Muñoz Mejía.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.97 | 11.50 | 18.53 | 2.00 | 90.4 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.26 | 9.00 | 14.50 | 3.00 | 91.4 | 90.0 |
| XI | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.93 | 14.40 | 23.02 | 0.00 | 97.1 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.1 | 4.64 | 13.31 | 20.81 | 8.00 | 96.1 | 90.0 |
| Bench 2 | Autosub In | Marc Cucurella Saseta | DEF | 7 | 6.2 | 3.86 | 11.92 | 19.60 | 6.00 | 86.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 3.94 | 11.48 | 19.11 | 2.00 | 88.4 | 90.0 |
| Bench 3 | Bench | Jurriën Timber | DEF | 1 | 6.4 | 3.73 | 11.28 | 18.49 | 3.00 | 69.9 | 90.0 |
| Captain | Captain | Nick Woltemade | FWD | 15 | 7.5 | 5.78 | 14.89 | 23.08 | 2.00 | 96.0 | 73.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.7 | 4.73 | 13.60 | 22.10 | 2.00 | 75.2 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 2.88 | 7.99 | 12.71 | 0.00 | 50.8 | 0.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.68 | 16.42 | 26.94 | 18.00 | 92.5 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.1 | 4.98 | 15.62 | 25.61 | 4.00 | 68.2 | 78.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.5 | 4.96 | 14.30 | 23.81 | 8.00 | 80.5 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 4.06 | 12.42 | 21.25 | 3.00 | 67.2 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.99 | 11.90 | 19.33 | 4.00 | 75.6 | 90.0 |

## GW16

- Train rows: 172367
- Bank: 0.80 -> 0.40
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Bukayo Saka
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 74.74
- Actual score: 89.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.75) beats the best remaining Triple Captain opportunity (9.08).
- Transfer: Bryan Mbeumo -> Phil Foden (projected gain 7.63, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (7.75) beats the best remaining Triple Captain opportunity (9.08).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 5.13 | 13.01 | 20.47 | 2.00 | 103.2 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.37 | 9.22 | 14.68 | 1.00 | 91.6 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.1 | 4.93 | 13.81 | 21.97 | 1.00 | 101.7 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.45 | 12.92 | 20.89 | 6.00 | 94.6 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.33 | 11.87 | 19.39 | 2.00 | 80.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.02 | 11.70 | 18.99 | 6.00 | 84.1 | 90.0 |
| Bench 4 | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 0.00 | 3.55 | 8.33 | 0.00 | 4.6 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.9 | 6.87 | 17.98 | 28.15 | 2.00 | 107.7 | 90.0 |
| Bench 2 | Bench | Nick Woltemade | FWD | 15 | 7.5 | 3.36 | 10.62 | 17.43 | 0.00 | 57.7 | 74.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 1.30 | 4.67 | 8.77 | 5.00 | 25.1 | 12.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.0 | 7.75 | 21.12 | 34.40 | 13.00 | 121.6 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 10.1 | 7.16 | 19.46 | 30.56 | 11.00 | 94.2 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.7 | 6.87 | 18.74 | 28.93 | 11.00 | 93.3 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.05 | 12.09 | 19.61 | 3.00 | 76.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 3.70 | 11.65 | 19.84 | 6.00 | 66.9 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 0.40 -> 0.20
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Bruno Borges Fernandes
- Effective captain: Phil Foden
- Chip used: bench_boost
- Predicted score: 67.20
- Actual score: 47.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.43) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Nick Woltemade -> Jarrod Bowen (projected gain 0.72, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.43) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.60 | 10.61 | 17.06 | 7.00 | 83.7 | 90.0 |
| Bench 1 | Bench Boost | Martin Dúbravka | GK | 3 | 4.0 | 2.96 | 8.54 | 13.67 | 2.00 | 88.8 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.2 | 4.88 | 13.48 | 21.23 | 1.00 | 95.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.14 | 12.07 | 19.76 | 2.00 | 87.9 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.06 | 12.05 | 19.57 | 1.00 | 88.4 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 3.88 | 11.16 | 18.38 | 6.00 | 76.3 | 90.0 |
| Bench 4 | Bench Boost | Daniel Muñoz Mejía | DEF | 8 | 5.9 | 0.30 | 2.59 | 7.14 | 0.00 | 2.8 | 0.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 3.65 | 11.42 | 18.75 | 1.00 | 74.3 | 90.0 |
| Bench 2 | Bench Boost | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.9 | 3.17 | 11.00 | 17.58 | 2.00 | 43.8 | 90.0 |
| Bench 3 | Bench Boost | Junior Kroupi | FWD | 4 | 4.6 | 2.00 | 5.39 | 9.27 | 1.00 | 27.9 | 26.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.1 | 6.33 | 18.74 | 30.55 | 1.00 | 90.5 | 45.0 |
| Captain | Captain | Phil Foden | MID | 13 | 8.8 | 6.48 | 18.42 | 28.46 | 3.00 | 81.7 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.2 | 5.44 | 16.26 | 26.59 | 3.00 | 72.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 6.22 | 15.70 | 24.70 | 10.00 | 98.6 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.62 | 11.33 | 18.23 | 4.00 | 73.6 | 90.0 |