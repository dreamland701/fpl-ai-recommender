# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW9
- Simulated weeks: GW10-GW13
- Total predicted points: 280.60
- Total actual points: 227.00
- Average predicted points: 70.15
- Average actual points: 56.75
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
- Predicted score: 67.47
- Actual score: 97.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.40 | 12.25 | 19.61 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.17 | 0.67 | 1.34 | 0.00 | 1.8 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.50 | 15.57 | 24.42 | 12.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 5.04 | 14.95 | 24.22 | 10.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.66 | 12.60 | 20.90 | 3.00 | 83.5 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.1 | 3.45 | 9.68 | 14.96 | 1.00 | 72.8 | 90.0 |
| Bench 4 | Bench | Maxime Estève | DEF | 3 | 4.0 | 2.81 | 8.96 | 14.96 | 1.00 | 76.3 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.00 | 23.72 | 38.67 | 13.00 | 90.0 | 81.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.8 | 5.85 | 16.58 | 25.73 | 9.00 | 90.0 | 89.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 3.32 | 10.79 | 17.20 | 2.00 | 81.4 | 61.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.3 | 7.25 | 20.40 | 31.39 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.54 | 17.59 | 29.14 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.05 | 14.58 | 23.39 | 5.00 | 83.3 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.62 | 14.40 | 22.98 | 9.00 | 88.1 | 61.0 |
| XI | XI | Declan Rice | MID | 1 | 6.7 | 4.57 | 13.60 | 22.03 | 13.00 | 76.9 | 90.0 |

## GW11

- Train rows: 168588
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 67.09
- Actual score: 38.00
- Transfer: Marcos Senesi Barón -> Maxence Lacroix (projected gain 0.18, hit 0)
- Autosub: Maxime Estève replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.09 | 12.00 | 19.30 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.16 | 0.60 | 1.25 | 0.00 | 2.3 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.32 | 17.09 | 27.14 | 1.00 | 90.0 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.0 | 5.32 | 15.21 | 24.01 | 0.00 | 90.0 | 0.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.0 | 4.01 | 11.76 | 18.50 | 6.00 | 88.9 | 90.0 |
| Bench 4 | Bench | Nordi Mukiele | DEF | 17 | 4.1 | 2.73 | 8.90 | 14.59 | 4.00 | 71.8 | 90.0 |
| Bench 3 | Autosub In | Maxime Estève | DEF | 3 | 4.0 | 3.04 | 8.54 | 13.51 | 3.00 | 80.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.69 | 24.65 | 40.43 | 4.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.58 | 16.74 | 25.71 | 2.00 | 84.4 | 90.0 |
| Bench 2 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 3.13 | 10.15 | 16.03 | 1.00 | 66.7 | 27.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.87 | 17.36 | 28.05 | 0.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 6.7 | 5.33 | 16.69 | 25.89 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 4.66 | 15.27 | 23.71 | 7.00 | 74.5 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.93 | 14.30 | 23.67 | 5.00 | 87.4 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.59 | 12.75 | 20.42 | 3.00 | 79.6 | 90.0 |

## GW12

- Train rows: 169340
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bryan Mbeumo
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 75.05
- Actual score: 47.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.74) beats the best remaining Bench Boost opportunity (10.47).
- Transfer: Gabriel dos Santos Magalhães -> Virgil van Dijk (projected gain 3.95, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.74) beats the best remaining Bench Boost opportunity (10.47).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.91 | 11.18 | 18.12 | 2.00 | 86.5 | 90.0 |
| Bench 1 | Bench Boost | Antonín Kinský | GK | 18 | 3.9 | 0.00 | 0.32 | 1.00 | 0.00 | 2.4 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.93 | 13.57 | 21.74 | 3.00 | 90.0 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.0 | 4.43 | 11.63 | 18.12 | 11.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 3.80 | 9.85 | 16.23 | 5.00 | 56.0 | 90.0 |
| Bench 2 | Bench Boost | Nordi Mukiele | DEF | 17 | 4.1 | 3.37 | 9.67 | 16.80 | 4.00 | 73.0 | 90.0 |
| Bench 3 | Bench Boost | Maxime Estève | DEF | 3 | 3.9 | 2.95 | 8.25 | 13.40 | 3.00 | 79.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.57 | 24.69 | 40.29 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.37 | 15.49 | 24.77 | 1.00 | 76.8 | 59.0 |
| Bench 4 | Bench Boost | Junior Kroupi | FWD | 4 | 4.6 | 2.42 | 7.76 | 13.25 | 2.00 | 34.3 | 85.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.4 | 6.80 | 19.21 | 30.05 | 1.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.43 | 15.51 | 24.54 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.0 | 5.39 | 15.25 | 25.33 | 0.00 | 83.6 | 0.0 |
| XI | XI | Declan Rice | MID | 1 | 6.8 | 5.04 | 15.11 | 23.17 | 6.00 | 85.1 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.08 | 12.52 | 21.06 | 3.00 | 77.7 | 80.0 |

## GW13

- Train rows: 170095
- Bank: 0.50 -> 1.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Morgan Rogers
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 70.98
- Actual score: 45.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.98) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Antoine Semenyo -> Morgan Rogers (projected gain 6.01, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.98) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.47 | 10.35 | 16.91 | 3.00 | 84.2 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.22 | 0.65 | 1.17 | 0.00 | 2.3 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 4.16 | 11.49 | 19.03 | 0.00 | 80.5 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.0 | 3.76 | 10.78 | 17.84 | 3.00 | 87.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 3.67 | 10.69 | 18.43 | 6.00 | 76.3 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.1 | 3.52 | 9.76 | 15.58 | 0.00 | 75.4 | 90.0 |
| Bench 3 | Bench | Maxime Estève | DEF | 3 | 3.9 | 3.07 | 8.77 | 13.72 | 3.00 | 81.3 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.98 | 25.10 | 40.43 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 3.99 | 12.95 | 21.64 | 6.00 | 62.7 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 2.20 | 8.97 | 15.25 | 1.00 | 46.5 | 10.0 |
| Vice Captain | XI | Morgan Rogers | MID | 2 | 6.9 | 5.94 | 15.70 | 24.24 | 3.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 6.8 | 5.05 | 15.66 | 24.10 | 4.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.4 | 4.91 | 15.30 | 24.46 | 1.00 | 79.7 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.01 | 14.72 | 24.88 | 11.00 | 87.4 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.09 | 11.11 | 19.18 | 2.00 | 70.7 | 79.0 |