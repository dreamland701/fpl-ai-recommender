# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW9
- Simulated weeks: GW10-GW13
- Total predicted points: 279.49
- Total actual points: 227.00
- Average predicted points: 69.87
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
- Predicted score: 67.27
- Actual score: 97.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.36 | 12.17 | 19.56 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Freddie Woodman | GK | 12 | 3.9 | 0.16 | 0.40 | 0.71 | 0.00 | 4.9 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.47 | 15.54 | 24.41 | 12.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 5.02 | 14.93 | 24.13 | 10.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.64 | 12.58 | 20.70 | 3.00 | 82.9 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.1 | 3.44 | 9.69 | 15.09 | 1.00 | 72.6 | 90.0 |
| Bench 4 | Bench | Maxime Estève | DEF | 3 | 4.0 | 2.79 | 8.93 | 14.76 | 1.00 | 75.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 7.98 | 23.71 | 38.73 | 13.00 | 90.0 | 81.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.8 | 5.85 | 16.61 | 25.83 | 9.00 | 90.0 | 89.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 3.32 | 10.80 | 17.14 | 2.00 | 81.2 | 61.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.3 | 7.29 | 20.46 | 31.44 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.49 | 17.52 | 28.97 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.02 | 14.55 | 23.44 | 5.00 | 82.6 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.62 | 14.40 | 22.87 | 9.00 | 88.1 | 61.0 |
| XI | XI | Declan Rice | MID | 1 | 6.7 | 4.53 | 13.54 | 21.89 | 13.00 | 75.8 | 90.0 |

## GW11

- Train rows: 168588
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 66.77
- Actual score: 38.00
- Transfer: Marcos Senesi Barón -> Maxence Lacroix (projected gain 0.10, hit 0)
- Autosub: Maxime Estève replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.04 | 11.91 | 19.24 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Freddie Woodman | GK | 12 | 3.9 | 0.00 | 0.00 | 0.34 | 0.00 | 4.9 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.30 | 17.06 | 27.04 | 1.00 | 90.0 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.0 | 5.29 | 15.18 | 23.94 | 0.00 | 90.0 | 0.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.0 | 3.97 | 11.69 | 18.35 | 6.00 | 87.9 | 90.0 |
| Bench 4 | Bench | Nordi Mukiele | DEF | 17 | 4.1 | 2.71 | 8.91 | 14.60 | 4.00 | 71.4 | 90.0 |
| Bench 3 | Autosub In | Maxime Estève | DEF | 3 | 4.0 | 3.04 | 8.54 | 13.48 | 3.00 | 80.3 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.67 | 24.62 | 40.44 | 4.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.57 | 16.75 | 25.74 | 2.00 | 84.2 | 90.0 |
| Bench 2 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 3.15 | 10.20 | 16.06 | 1.00 | 66.9 | 27.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.83 | 17.30 | 27.99 | 0.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 6.7 | 5.33 | 16.70 | 25.83 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 4.63 | 15.22 | 23.65 | 7.00 | 73.7 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.91 | 14.26 | 23.68 | 5.00 | 86.8 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.56 | 12.71 | 20.40 | 3.00 | 78.8 | 90.0 |

## GW12

- Train rows: 169340
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bryan Mbeumo
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 75.02
- Actual score: 47.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.96) beats the best remaining Bench Boost opportunity (10.73).
- Transfer: Gabriel dos Santos Magalhães -> Virgil van Dijk (projected gain 3.96, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.96) beats the best remaining Bench Boost opportunity (10.73).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.84 | 11.06 | 18.03 | 2.00 | 85.0 | 90.0 |
| Bench 1 | Bench Boost | Freddie Woodman | GK | 12 | 3.9 | 0.11 | 0.25 | 0.62 | 0.00 | 4.9 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.90 | 13.52 | 21.69 | 3.00 | 90.0 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.0 | 4.39 | 11.56 | 18.03 | 11.00 | 89.4 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 3.69 | 9.65 | 16.04 | 5.00 | 53.0 | 90.0 |
| Bench 2 | Bench Boost | Nordi Mukiele | DEF | 17 | 4.1 | 3.35 | 9.63 | 16.76 | 4.00 | 72.3 | 90.0 |
| Bench 3 | Bench Boost | Maxime Estève | DEF | 3 | 3.9 | 2.92 | 8.21 | 13.36 | 3.00 | 78.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.57 | 24.70 | 40.34 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.31 | 15.40 | 24.69 | 1.00 | 75.2 | 59.0 |
| Bench 4 | Bench Boost | Junior Kroupi | FWD | 4 | 4.6 | 2.58 | 8.05 | 13.62 | 2.00 | 39.0 | 85.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.4 | 6.80 | 19.22 | 30.05 | 1.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.41 | 15.48 | 24.50 | 2.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 6.8 | 5.04 | 15.11 | 23.15 | 6.00 | 85.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.0 | 5.52 | 15.07 | 24.63 | 0.00 | 87.4 | 0.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.03 | 12.46 | 21.02 | 3.00 | 76.5 | 80.0 |

## GW13

- Train rows: 170095
- Bank: 0.50 -> 1.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Morgan Rogers
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 70.43
- Actual score: 45.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.98) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Antoine Semenyo -> Morgan Rogers (projected gain 5.98, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.98) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.40 | 10.22 | 16.81 | 3.00 | 82.5 | 90.0 |
| Bench 1 | Bench | Freddie Woodman | GK | 12 | 3.9 | 0.01 | 0.18 | 0.39 | 0.00 | 5.3 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 4.07 | 11.34 | 18.89 | 0.00 | 78.3 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.0 | 3.70 | 10.67 | 17.74 | 3.00 | 86.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 3.59 | 10.54 | 18.31 | 6.00 | 74.3 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.1 | 3.52 | 9.76 | 15.61 | 0.00 | 75.4 | 90.0 |
| Bench 3 | Bench | Maxime Estève | DEF | 3 | 3.9 | 3.06 | 8.76 | 13.73 | 3.00 | 81.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.98 | 25.12 | 40.48 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 3.89 | 12.80 | 21.50 | 6.00 | 60.1 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 2.35 | 9.24 | 15.55 | 1.00 | 51.1 | 10.0 |
| Vice Captain | XI | Morgan Rogers | MID | 2 | 6.9 | 5.94 | 15.69 | 24.22 | 3.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 6.8 | 5.05 | 15.68 | 24.12 | 4.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.4 | 4.86 | 15.21 | 24.37 | 1.00 | 78.2 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.97 | 14.64 | 24.81 | 11.00 | 86.3 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.02 | 11.00 | 19.09 | 2.00 | 68.8 | 79.0 |