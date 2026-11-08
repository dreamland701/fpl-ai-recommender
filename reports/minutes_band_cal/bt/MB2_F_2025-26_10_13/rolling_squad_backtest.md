# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW9
- Simulated weeks: GW10-GW13
- Total predicted points: 266.42
- Total actual points: 219.00
- Average predicted points: 66.60
- Average actual points: 54.75
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW9 are included before the first simulated week.
- League-average scores were not available for this run.

## GW10

- Train rows: 167841
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Erling Haaland
- Vice captain: Bryan Mbeumo
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 62.67
- Actual score: 95.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.83 | 10.61 | 17.28 | 6.00 | 83.3 | 90.0 |
| Bench 1 | Bench | Brandon Austin | GK | 18 | 3.9 | 0.11 | 0.32 | 0.66 | 0.00 | 4.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.01 | 14.23 | 22.66 | 12.00 | 83.3 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 4.51 | 13.39 | 21.95 | 10.00 | 83.3 | 90.0 |
| Bench 3 | Bench | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.25 | 11.58 | 19.59 | 3.00 | 80.6 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.1 | 3.57 | 10.13 | 15.92 | 1.00 | 78.7 | 90.0 |
| Bench 4 | Bench | Maxime Estève | DEF | 3 | 4.0 | 2.87 | 9.14 | 15.09 | 1.00 | 78.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 7.53 | 22.39 | 36.90 | 13.00 | 83.3 | 81.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.8 | 5.30 | 14.88 | 23.23 | 9.00 | 82.2 | 89.0 |
| Bench 2 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 3.33 | 10.64 | 16.70 | 2.00 | 79.9 | 61.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.3 | 6.75 | 18.76 | 28.90 | 2.00 | 83.3 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.01 | 16.11 | 27.04 | 2.00 | 83.3 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.99 | 14.33 | 23.04 | 5.00 | 80.3 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 6.7 | 4.50 | 13.43 | 21.75 | 13.00 | 74.3 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.15 | 13.00 | 20.93 | 9.00 | 81.0 | 61.0 |

## GW11

- Train rows: 168588
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Jean-Philippe Mateta
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 63.11
- Actual score: 38.00
- Transfer: Marcos Senesi Barón -> Maxence Lacroix (projected gain 0.79, hit 0)
- Autosub: Maxime Estève replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.51 | 10.35 | 17.01 | 1.00 | 81.4 | 90.0 |
| Bench 1 | Bench | Brandon Austin | GK | 18 | 3.9 | 0.09 | 0.22 | 0.53 | 0.00 | 4.3 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 4.84 | 15.81 | 25.45 | 1.00 | 83.3 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.0 | 4.78 | 13.63 | 21.76 | 0.00 | 83.3 | 0.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.0 | 3.88 | 11.34 | 17.63 | 6.00 | 82.3 | 90.0 |
| Bench 4 | Bench | Nordi Mukiele | DEF | 17 | 4.1 | 2.84 | 9.34 | 15.45 | 4.00 | 77.3 | 90.0 |
| Bench 3 | Autosub In | Maxime Estève | DEF | 3 | 4.0 | 3.11 | 8.71 | 13.70 | 3.00 | 82.3 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.22 | 23.34 | 38.68 | 4.00 | 83.3 | 90.0 |
| Vice Captain | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.49 | 16.36 | 25.04 | 2.00 | 79.8 | 90.0 |
| Bench 2 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 3.26 | 10.35 | 16.28 | 1.00 | 71.5 | 27.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.33 | 15.80 | 25.86 | 0.00 | 83.3 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 6.7 | 4.83 | 15.18 | 23.69 | 2.00 | 83.3 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 4.59 | 15.00 | 23.28 | 7.00 | 72.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.85 | 14.01 | 23.12 | 5.00 | 82.6 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.56 | 12.66 | 20.32 | 3.00 | 78.8 | 90.0 |

## GW12

- Train rows: 169340
- Bank: 0.00 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bryan Mbeumo
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 72.79
- Actual score: 50.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.10) beats the best remaining Bench Boost opportunity (10.90).
- Transfer: Gabriel dos Santos Magalhães -> Marc Cucurella Saseta (projected gain 2.52, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.10) beats the best remaining Bench Boost opportunity (10.90).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.77 | 10.82 | 17.48 | 2.00 | 80.2 | 90.0 |
| Bench 1 | Bench Boost | Brandon Austin | GK | 18 | 3.9 | 0.00 | 0.00 | 0.25 | 0.00 | 4.1 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.1 | 4.58 | 12.55 | 20.40 | 6.00 | 80.4 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.0 | 4.32 | 11.20 | 17.26 | 11.00 | 84.0 | 90.0 |
| Bench 2 | Bench Boost | Nordi Mukiele | DEF | 17 | 4.1 | 3.49 | 10.09 | 17.66 | 4.00 | 78.3 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 3.80 | 9.88 | 16.30 | 5.00 | 54.1 | 90.0 |
| Bench 3 | Bench Boost | Maxime Estève | DEF | 3 | 3.9 | 3.01 | 8.43 | 13.63 | 3.00 | 80.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.12 | 23.41 | 38.59 | 2.00 | 83.3 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.29 | 15.21 | 24.36 | 1.00 | 74.4 | 59.0 |
| Bench 4 | Bench Boost | Junior Kroupi | FWD | 4 | 4.6 | 2.61 | 8.10 | 13.74 | 2.00 | 40.4 | 85.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.4 | 6.28 | 17.57 | 27.62 | 1.00 | 83.3 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 6.8 | 4.98 | 14.83 | 22.49 | 6.00 | 81.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.0 | 5.46 | 14.82 | 24.04 | 0.00 | 83.1 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.92 | 13.99 | 22.39 | 2.00 | 83.3 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.03 | 12.45 | 21.04 | 3.00 | 76.3 | 80.0 |

## GW13

- Train rows: 170095
- Bank: 0.40 -> 0.60
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 67.85
- Actual score: 36.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.53) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Antoine Semenyo -> Eberechi Eze (projected gain 3.86, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.53) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.36 | 10.09 | 16.59 | 3.00 | 80.3 | 90.0 |
| Bench 1 | Bench | Brandon Austin | GK | 18 | 3.9 | 0.16 | 0.27 | 0.41 | 0.00 | 3.9 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.1 | 4.07 | 11.93 | 19.88 | 1.00 | 79.1 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 4.03 | 11.14 | 18.57 | 0.00 | 76.0 | 90.0 |
| Bench 2 | Bench | Maxence Lacroix | DEF | 8 | 5.0 | 3.63 | 10.35 | 17.08 | 3.00 | 80.7 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.1 | 3.65 | 10.12 | 16.11 | 0.00 | 78.8 | 90.0 |
| Bench 3 | Bench | Maxime Estève | DEF | 3 | 3.9 | 3.15 | 8.97 | 13.97 | 3.00 | 82.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.53 | 23.80 | 38.67 | 2.00 | 83.4 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 4.02 | 13.06 | 21.79 | 6.00 | 61.7 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 2.59 | 9.79 | 16.35 | 1.00 | 57.5 | 10.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.4 | 4.79 | 14.92 | 23.84 | 1.00 | 75.1 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.93 | 14.45 | 24.32 | 11.00 | 82.6 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 6.8 | 4.58 | 14.27 | 22.13 | 4.00 | 83.4 | 90.0 |
| XI | XI | Eberechi Eze | MID | 1 | 7.7 | 4.75 | 14.14 | 22.84 | 2.00 | 83.4 | 71.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.08 | 11.17 | 19.46 | 2.00 | 71.7 | 79.0 |