# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW21
- Simulated weeks: GW22-GW25
- Total predicted points: 263.80
- Total actual points: 237.00
- Average predicted points: 65.95
- Average actual points: 59.25
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
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Guimarães Rodriguez Moura
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 65.61
- Actual score: 54.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Gabriel Gudmundsson replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.70 | 10.76 | 17.53 | 6.00 | 86.6 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.01 | 0.22 | 0.00 | 4.1 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 4.89 | 13.60 | 19.52 | 8.00 | 77.2 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.3 | 4.50 | 12.67 | 20.36 | 0.00 | 90.0 | 0.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.29 | 12.64 | 19.93 | 8.00 | 86.9 | 90.0 |
| Bench 2 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 3.35 | 9.25 | 14.23 | 0.00 | 83.5 | 0.0 |
| Bench 4 | Autosub In | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.56 | 7.37 | 12.10 | 6.00 | 76.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.28 | 24.28 | 39.43 | 2.00 | 90.0 | 79.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.50 | 15.00 | 23.60 | 2.00 | 83.4 | 90.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.5 | 2.92 | 8.13 | 12.29 | 2.00 | 68.5 | 90.0 |
| Vice Captain | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 5.62 | 15.74 | 25.00 | 3.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.37 | 15.71 | 25.24 | 2.00 | 90.0 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.22 | 14.54 | 23.54 | 10.00 | 77.4 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.98 | 14.49 | 23.98 | 2.00 | 83.2 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 4.98 | 14.14 | 23.44 | 3.00 | 77.0 | 90.0 |

## GW23

- Train rows: 177836
- Bank: 0.10 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 65.90
- Actual score: 42.00
- Transfer: Marc Guéhi -> Cristian Romero (projected gain 1.84, hit 0)
- Autosub: Mateus Mané replaced Bruno Guimarães Rodriguez Moura.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.84 | 10.91 | 17.66 | 1.00 | 86.3 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.45 | 0.54 | 0.85 | 0.00 | 5.7 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 4.59 | 13.33 | 19.90 | 1.00 | 78.9 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.89 | 13.33 | 21.56 | 4.00 | 89.5 | 90.0 |
| XI | XI | Cristian Romero | DEF | 18 | 5.0 | 4.26 | 11.77 | 17.89 | 11.00 | 88.0 | 90.0 |
| Bench 2 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.59 | 7.51 | 12.16 | 0.00 | 77.3 | 0.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 1.85 | 5.65 | 9.20 | 0.00 | 44.5 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.35 | 22.96 | 37.68 | 1.00 | 90.0 | 17.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.72 | 15.60 | 24.70 | 2.00 | 88.3 | 90.0 |
| Bench 3 | Autosub In | Mateus Mané | FWD | 20 | 4.5 | 2.55 | 7.96 | 12.76 | 2.00 | 69.8 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.6 | 6.23 | 17.71 | 27.80 | 8.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.41 | 15.70 | 24.34 | 1.00 | 90.0 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.24 | 14.95 | 24.45 | 2.00 | 81.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.73 | 13.55 | 22.06 | 8.00 | 78.7 | 90.0 |
| XI | Bench | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 4.28 | 12.80 | 21.90 | 0.00 | 72.4 | 0.0 |

## GW24

- Train rows: 178639
- Bank: 0.30 -> 0.80
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Erling Haaland
- Effective captain: Antoine Semenyo
- Chip used: bench_boost
- Predicted score: 64.41
- Actual score: 63.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.31) beats the best remaining Bench Boost opportunity (6.52).
- Transfer: Bruno Guimarães Rodriguez Moura -> Enzo Fernández (projected gain 6.50, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.31) beats the best remaining Bench Boost opportunity (6.52).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.85 | 10.91 | 17.61 | 6.00 | 85.5 | 90.0 |
| Bench 1 | Bench Boost | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.18 | 0.34 | 0.00 | 4.4 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 4.95 | 14.16 | 22.33 | 8.00 | 85.9 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.02 | 11.98 | 19.63 | 2.00 | 82.2 | 90.0 |
| XI | XI | Cristian Romero | DEF | 18 | 5.0 | 3.80 | 11.24 | 17.85 | 0.00 | 87.9 | 45.0 |
| Bench 3 | Bench Boost | Gabriel Gudmundsson | DEF | 11 | 3.8 | 1.25 | 4.09 | 7.27 | -1.00 | 40.8 | 90.0 |
| Bench 4 | Bench Boost | Jaka Bijol | DEF | 11 | 3.9 | 1.09 | 3.72 | 7.33 | 0.00 | 28.0 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 15.0 | 5.57 | 18.93 | 32.07 | 5.00 | 72.1 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.40 | 13.61 | 21.99 | 2.00 | 79.9 | 90.0 |
| Bench 2 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 2.97 | 8.05 | 13.32 | 2.00 | 67.5 | 90.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 7.7 | 5.87 | 16.67 | 26.66 | 7.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.49 | 16.17 | 25.41 | 3.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.50 | 15.40 | 24.53 | 2.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 5.38 | 14.44 | 23.27 | 8.00 | 88.5 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 4.38 | 13.21 | 22.27 | 12.00 | 71.6 | 86.0 |

## GW25

- Train rows: 179450
- Bank: 0.80 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 67.88
- Actual score: 78.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.72) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Cristian Romero -> Trevoh Chalobah (projected gain 6.27, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (6.72) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.15 | 11.43 | 18.18 | 7.00 | 85.2 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 3.1 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 5.49 | 15.13 | 23.87 | 6.00 | 88.3 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.7 | 4.31 | 12.13 | 18.99 | 4.00 | 84.7 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.09 | 11.82 | 19.38 | 2.00 | 82.4 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.19 | 5.90 | 9.78 | 2.00 | 62.9 | 90.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 0.15 | 0.76 | 3.19 | 0.00 | 4.1 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 6.72 | 20.56 | 34.68 | 11.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.92 | 12.68 | 20.87 | 5.00 | 72.9 | 90.0 |
| Bench 2 | Bench | Mateus Mané | FWD | 20 | 4.5 | 2.94 | 8.59 | 14.05 | 2.00 | 69.2 | 90.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.4 | 5.84 | 16.54 | 26.41 | 5.00 | 89.7 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.55 | 16.36 | 27.45 | 2.00 | 90.0 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.03 | 15.22 | 25.22 | 2.00 | 85.6 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 4.60 | 13.81 | 22.04 | 2.00 | 76.1 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 4.74 | 13.80 | 22.20 | 10.00 | 81.1 | 90.0 |