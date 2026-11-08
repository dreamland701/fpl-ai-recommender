# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW21
- Simulated weeks: GW22-GW25
- Total predicted points: 256.75
- Total actual points: 233.00
- Average predicted points: 64.19
- Average actual points: 58.25
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW21 are included before the first simulated week.
- League-average scores were not available for this run.

## GW22

- Train rows: 177037
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Guimarães Rodriguez Moura
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 64.11
- Actual score: 50.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Pascal Struijk replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.63 | 10.60 | 17.13 | 6.00 | 87.9 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.14 | 0.00 | 4.4 | 0.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.29 | 12.60 | 20.06 | 8.00 | 86.7 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.3 | 4.39 | 12.55 | 20.01 | 0.00 | 90.0 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 4.40 | 12.36 | 19.18 | 5.00 | 86.3 | 90.0 |
| Bench 3 | Autosub In | Pascal Struijk | DEF | 11 | 4.3 | 3.39 | 9.66 | 15.26 | 6.00 | 83.9 | 90.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 3.38 | 9.37 | 14.48 | 0.00 | 84.3 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.06 | 24.03 | 39.05 | 2.00 | 90.0 | 79.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.34 | 13.91 | 22.29 | 2.00 | 85.0 | 90.0 |
| Bench 2 | Bench | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 4.10 | 12.81 | 20.27 | 2.00 | 78.6 | 90.0 |
| Vice Captain | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 5.65 | 15.59 | 24.82 | 3.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.25 | 15.35 | 24.58 | 2.00 | 90.0 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.14 | 14.50 | 23.61 | 10.00 | 77.1 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.95 | 14.29 | 23.75 | 2.00 | 84.5 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.95 | 14.08 | 22.77 | 2.00 | 90.0 | 87.0 |

## GW23

- Train rows: 177836
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 63.22
- Actual score: 51.00
- Transfer: Marc Guéhi -> Cristian Romero (projected gain 2.08, hit 0)
- Autosub: Dominic Calvert-Lewin replaced Bruno Guimarães Rodriguez Moura.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.74 | 10.66 | 17.14 | 1.00 | 87.4 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.43 | 0.51 | 0.78 | 0.00 | 5.7 | 0.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.87 | 13.20 | 21.43 | 4.00 | 89.7 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 4.22 | 12.03 | 18.90 | 1.00 | 86.1 | 90.0 |
| XI | XI | Cristian Romero | DEF | 18 | 5.0 | 4.29 | 11.86 | 18.05 | 11.00 | 88.0 | 90.0 |
| Bench 3 | Bench | Pascal Struijk | DEF | 11 | 4.3 | 3.39 | 9.82 | 15.76 | 4.00 | 84.8 | 90.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 1.86 | 5.70 | 9.38 | 0.00 | 43.5 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.11 | 22.73 | 37.18 | 1.00 | 90.0 | 17.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.50 | 14.46 | 23.10 | 2.00 | 89.0 | 90.0 |
| Bench 2 | Autosub In | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 3.67 | 11.19 | 18.06 | 2.00 | 74.3 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.61 | 15.31 | 24.25 | 8.00 | 90.0 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.21 | 14.90 | 24.21 | 2.00 | 80.5 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.70 | 13.48 | 22.06 | 8.00 | 79.3 | 90.0 |
| XI | Bench | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 4.62 | 13.25 | 21.69 | 0.00 | 79.6 | 0.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.24 | 11.87 | 19.81 | 10.00 | 76.8 | 90.0 |

## GW24

- Train rows: 178639
- Bank: 0.20 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 64.40
- Actual score: 56.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.44) beats the best remaining Triple Captain opportunity (7.16).
- Transfer: Bruno Guimarães Rodriguez Moura -> Declan Rice (projected gain 5.39, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (6.44) beats the best remaining Triple Captain opportunity (7.16).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.79 | 10.68 | 17.23 | 6.00 | 86.5 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.09 | 0.26 | 0.00 | 4.2 | 0.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 3.99 | 11.79 | 19.41 | 2.00 | 82.3 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 3.94 | 11.44 | 18.64 | 5.00 | 80.3 | 90.0 |
| XI | XI | Cristian Romero | DEF | 18 | 5.0 | 3.83 | 11.13 | 17.71 | 0.00 | 87.5 | 45.0 |
| Bench 3 | Bench | Pascal Struijk | DEF | 11 | 4.3 | 3.50 | 10.09 | 16.32 | 2.00 | 82.6 | 90.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 1.12 | 3.78 | 7.50 | 0.00 | 27.3 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.0 | 6.44 | 19.74 | 33.60 | 5.00 | 74.2 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.21 | 13.04 | 21.09 | 2.00 | 80.3 | 90.0 |
| Bench 2 | Bench | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 3.55 | 10.52 | 17.41 | 2.00 | 72.8 | 84.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.77 | 16.35 | 26.22 | 7.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.4 | 5.42 | 15.83 | 25.15 | 3.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.49 | 15.51 | 24.78 | 2.00 | 90.0 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 4.38 | 13.26 | 22.47 | 12.00 | 71.8 | 86.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.27 | 12.76 | 20.83 | 2.00 | 87.0 | 90.0 |

## GW25

- Train rows: 179450
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 65.01
- Actual score: 76.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.90) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Cristian Romero -> Marcos Senesi Barón (projected gain 1.14, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.90) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.10 | 11.30 | 17.91 | 7.00 | 86.4 | 90.0 |
| Bench 1 | Bench Boost | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 2.9 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 4.44 | 12.08 | 19.42 | 6.00 | 79.7 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.02 | 11.75 | 19.30 | 2.00 | 81.9 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 4.03 | 11.10 | 17.90 | 2.00 | 86.3 | 90.0 |
| Bench 2 | Bench Boost | Pascal Struijk | DEF | 11 | 4.3 | 3.56 | 10.06 | 16.18 | 4.00 | 81.7 | 90.0 |
| Bench 4 | Bench Boost | Jaka Bijol | DEF | 11 | 3.9 | 0.15 | 0.80 | 3.33 | 0.00 | 4.8 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 6.46 | 20.09 | 33.60 | 11.00 | 89.9 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.81 | 12.35 | 20.24 | 5.00 | 74.1 | 90.0 |
| Bench 3 | Bench Boost | Dominic Calvert-Lewin | FWD | 11 | 5.9 | 3.19 | 9.58 | 16.04 | 7.00 | 66.1 | 90.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.4 | 5.76 | 16.07 | 25.72 | 5.00 | 89.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.24 | 15.39 | 25.19 | 2.00 | 90.0 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.07 | 15.25 | 25.24 | 2.00 | 85.7 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 4.65 | 13.51 | 21.92 | 10.00 | 80.7 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.07 | 11.68 | 18.60 | 2.00 | 81.0 | 90.0 |