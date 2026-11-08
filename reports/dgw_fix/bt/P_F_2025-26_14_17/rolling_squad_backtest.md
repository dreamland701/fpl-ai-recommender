# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW13
- Simulated weeks: GW14-GW17
- Total predicted points: 252.41
- Total actual points: 251.00
- Average predicted points: 63.10
- Average actual points: 62.75
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
- Predicted score: 61.05
- Actual score: 50.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.07 | 11.53 | 18.50 | 6.00 | 88.6 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.28 | 9.15 | 14.73 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.74 | 13.28 | 20.99 | 1.00 | 86.8 | 46.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.50 | 12.67 | 19.91 | 14.00 | 83.7 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.45 | 12.66 | 20.37 | 1.00 | 86.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.41 | 12.09 | 19.67 | 4.00 | 89.3 | 90.0 |
| Bench 2 | Bench | Maxence Lacroix | DEF | 8 | 5.1 | 4.14 | 11.27 | 18.43 | 8.00 | 82.1 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 5.38 | 14.70 | 23.36 | 2.00 | 88.2 | 63.0 |
| Bench 3 | Bench | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.7 | 3.58 | 12.37 | 19.92 | 1.00 | 64.9 | 30.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 2.40 | 7.23 | 12.30 | 2.00 | 37.1 | 60.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 8.9 | 6.07 | 17.33 | 27.75 | 4.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 10.1 | 5.78 | 16.76 | 26.94 | 6.00 | 87.2 | 29.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.6 | 5.63 | 15.96 | 25.85 | 2.00 | 86.3 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.8 | 5.09 | 13.74 | 22.92 | 4.00 | 81.3 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.86 | 12.96 | 20.69 | 2.00 | 88.4 | 90.0 |

## GW15

- Train rows: 171608
- Bank: 0.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Bryan Mbeumo
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 55.42
- Actual score: 77.00
- Transfer: Maxence Lacroix -> Marc Guéhi (projected gain 1.92, hit 0)
- Autosub: Elliot Anderson replaced Daniel Muñoz Mejía.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.88 | 11.37 | 18.48 | 2.00 | 88.4 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.24 | 8.91 | 14.49 | 3.00 | 90.0 | 90.0 |
| XI | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.94 | 14.57 | 23.20 | 0.00 | 90.0 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.1 | 4.65 | 13.47 | 21.12 | 8.00 | 90.0 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 3.96 | 11.92 | 19.45 | 6.00 | 85.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.04 | 11.64 | 19.31 | 2.00 | 87.2 | 90.0 |
| Bench 3 | Bench | Jurriën Timber | DEF | 1 | 6.4 | 3.64 | 11.23 | 18.45 | 3.00 | 68.5 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.7 | 4.72 | 13.57 | 21.89 | 2.00 | 71.9 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 3.82 | 11.71 | 19.69 | 2.00 | 61.6 | 65.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 2.82 | 7.85 | 12.64 | 0.00 | 49.7 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.66 | 16.05 | 26.28 | 18.00 | 88.6 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.1 | 4.88 | 15.56 | 25.63 | 4.00 | 66.8 | 78.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.5 | 5.04 | 14.03 | 23.53 | 8.00 | 78.6 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 4.18 | 12.57 | 21.57 | 3.00 | 67.3 | 90.0 |
| Bench 2 | Autosub In | Elliot Anderson | MID | 16 | 5.4 | 3.81 | 11.60 | 18.74 | 4.00 | 74.7 | 90.0 |

## GW16

- Train rows: 172367
- Bank: 0.20 -> 3.40
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Bukayo Saka
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 71.70
- Actual score: 79.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.53) beats the best remaining Triple Captain opportunity (8.49).
- Transfer: Bryan Mbeumo -> Kiernan Dewsbury-Hall (projected gain 3.56, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (7.53) beats the best remaining Triple Captain opportunity (8.49).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.91 | 12.75 | 20.17 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.37 | 9.20 | 14.74 | 1.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.1 | 4.85 | 13.93 | 22.32 | 1.00 | 90.0 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.26 | 12.77 | 20.60 | 6.00 | 90.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.41 | 11.89 | 19.33 | 2.00 | 80.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.08 | 11.88 | 19.36 | 6.00 | 83.9 | 90.0 |
| Bench 4 | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 0.60 | 4.36 | 9.20 | 0.00 | 14.2 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.9 | 6.69 | 17.33 | 27.31 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Jean-Philippe Mateta | FWD | 8 | 7.9 | 2.00 | 7.81 | 14.37 | 2.00 | 36.9 | 62.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 1.26 | 4.63 | 8.92 | 5.00 | 23.5 | 12.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.0 | 7.53 | 20.45 | 33.38 | 13.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 10.1 | 7.07 | 19.10 | 30.05 | 11.00 | 88.0 | 90.0 |
| XI | XI | Kiernan Dewsbury-Hall | MID | 9 | 5.1 | 4.89 | 14.81 | 22.96 | 1.00 | 90.0 | 15.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.14 | 11.88 | 19.16 | 3.00 | 76.5 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 3.82 | 11.49 | 19.52 | 6.00 | 67.5 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 3.40 -> 2.80
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Antoine Semenyo
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 64.24
- Actual score: 45.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.12) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Kiernan Dewsbury-Hall -> Harry Wilson (projected gain 7.51, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.12) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.46 | 10.17 | 16.43 | 7.00 | 80.6 | 90.0 |
| Bench 1 | Bench Boost | Martin Dúbravka | GK | 3 | 4.0 | 2.92 | 8.42 | 13.59 | 2.00 | 86.7 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.2 | 4.76 | 13.08 | 20.64 | 1.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.16 | 11.97 | 19.58 | 2.00 | 86.7 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 3.94 | 11.76 | 19.17 | 1.00 | 86.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 3.72 | 10.52 | 17.35 | 6.00 | 73.9 | 90.0 |
| Bench 4 | Bench Boost | Daniel Muñoz Mejía | DEF | 8 | 5.9 | 0.50 | 2.00 | 5.84 | 0.00 | 6.4 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.9 | 3.30 | 10.21 | 16.24 | 2.00 | 45.3 | 90.0 |
| Bench 2 | Bench Boost | Jean-Philippe Mateta | FWD | 8 | 7.8 | 2.66 | 7.84 | 14.01 | 2.00 | 42.2 | 76.0 |
| Bench 3 | Bench Boost | Junior Kroupi | FWD | 4 | 4.6 | 2.04 | 5.31 | 9.22 | 1.00 | 28.3 | 26.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.1 | 6.19 | 18.64 | 30.40 | 1.00 | 90.0 | 45.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.2 | 5.21 | 15.43 | 25.28 | 3.00 | 69.3 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.6 | 6.05 | 15.18 | 24.02 | 10.00 | 90.0 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.7 | 5.39 | 14.99 | 22.69 | 2.00 | 90.0 | 83.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.75 | 11.38 | 18.48 | 4.00 | 73.9 | 90.0 |