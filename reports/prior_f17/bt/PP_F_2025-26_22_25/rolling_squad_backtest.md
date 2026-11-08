# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW21
- Simulated weeks: GW22-GW25
- Total predicted points: 262.13
- Total actual points: 225.00
- Average predicted points: 65.53
- Average actual points: 56.25
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
- Predicted score: 65.68
- Actual score: 40.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Micky van de Ven replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.73 | 10.89 | 17.84 | 6.00 | 89.3 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.33 | 0.45 | 0.73 | 0.00 | 3.9 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 5.00 | 13.93 | 20.12 | 8.00 | 81.3 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.3 | 4.55 | 12.91 | 20.88 | 0.00 | 90.0 | 0.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.33 | 12.77 | 20.23 | 8.00 | 88.9 | 90.0 |
| Bench 2 | Autosub In | Micky van de Ven | DEF | 18 | 4.6 | 4.13 | 10.83 | 17.16 | 0.00 | 80.8 | 90.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 3.27 | 9.00 | 13.78 | 0.00 | 79.8 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.23 | 24.01 | 39.07 | 2.00 | 90.0 | 79.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.49 | 14.86 | 23.40 | 2.00 | 81.5 | 90.0 |
| Bench 3 | Bench | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 4.02 | 12.44 | 19.61 | 2.00 | 76.6 | 90.0 |
| Vice Captain | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 5.72 | 16.11 | 25.74 | 3.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.42 | 15.93 | 25.74 | 2.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.05 | 14.72 | 24.51 | 2.00 | 87.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.05 | 14.31 | 23.83 | 3.00 | 79.6 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.88 | 13.73 | 22.05 | 2.00 | 89.7 | 87.0 |

## GW23

- Train rows: 177836
- Bank: 0.10 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 64.85
- Actual score: 55.00
- Transfer: Marc Guéhi -> Cristian Romero (projected gain 1.62, hit 0)
- Autosub: Micky van de Ven replaced Bruno Guimarães Rodriguez Moura.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.87 | 11.05 | 17.98 | 1.00 | 89.1 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.14 | 0.52 | 0.00 | 6.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 4.63 | 13.44 | 20.16 | 1.00 | 81.1 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.92 | 13.44 | 21.81 | 4.00 | 90.0 | 90.0 |
| XI | XI | Cristian Romero | DEF | 18 | 5.0 | 4.23 | 11.59 | 17.55 | 11.00 | 86.6 | 90.0 |
| Bench 2 | Autosub In | Micky van de Ven | DEF | 18 | 4.6 | 3.64 | 10.02 | 16.44 | 7.00 | 80.9 | 90.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 1.79 | 5.47 | 8.91 | 0.00 | 41.9 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.29 | 22.67 | 37.26 | 1.00 | 90.0 | 17.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.69 | 15.42 | 24.43 | 2.00 | 86.0 | 90.0 |
| Bench 3 | Bench | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 3.56 | 10.82 | 17.09 | 2.00 | 71.6 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.74 | 16.01 | 25.56 | 8.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.46 | 15.80 | 24.60 | 1.00 | 90.0 | 90.0 |
| XI | Bench | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 4.77 | 13.96 | 23.00 | 0.00 | 83.0 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.76 | 13.66 | 22.38 | 8.00 | 81.4 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.18 | 11.84 | 19.64 | 10.00 | 73.5 | 90.0 |

## GW24

- Train rows: 178639
- Bank: 0.30 -> 0.80
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 67.48
- Actual score: 55.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.67) beats the best remaining Triple Captain opportunity (7.32).
- Transfer: Bruno Guimarães Rodriguez Moura -> Enzo Fernández (projected gain 4.50, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (6.67) beats the best remaining Triple Captain opportunity (7.32).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.89 | 11.07 | 17.96 | 6.00 | 88.5 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.08 | 0.27 | 0.50 | 0.00 | 4.6 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 4.98 | 14.22 | 22.49 | 8.00 | 87.2 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.04 | 12.09 | 19.89 | 2.00 | 84.0 | 90.0 |
| XI | XI | Cristian Romero | DEF | 18 | 5.0 | 3.76 | 11.03 | 17.46 | 0.00 | 85.9 | 45.0 |
| Bench 3 | Bench | Micky van de Ven | DEF | 18 | 4.6 | 3.17 | 9.45 | 15.80 | 0.00 | 82.9 | 0.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 1.01 | 3.48 | 6.95 | 0.00 | 25.0 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.0 | 6.67 | 19.81 | 33.64 | 5.00 | 76.7 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.31 | 13.27 | 21.48 | 2.00 | 76.4 | 90.0 |
| Bench 2 | Bench | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 3.44 | 10.00 | 16.32 | 2.00 | 70.6 | 84.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.93 | 16.81 | 26.99 | 7.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.54 | 16.28 | 25.67 | 3.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.54 | 15.51 | 24.78 | 2.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 5.20 | 14.42 | 23.16 | 8.00 | 84.8 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.28 | 12.69 | 20.72 | 2.00 | 84.7 | 90.0 |

## GW25

- Train rows: 179450
- Bank: 0.80 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 64.12
- Actual score: 75.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (4.34) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Cristian Romero -> Trevoh Chalobah (projected gain 5.69, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (4.34) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.18 | 11.54 | 18.43 | 7.00 | 87.7 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.08 | 0.21 | 0.00 | 2.3 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 5.50 | 15.07 | 23.79 | 6.00 | 88.4 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.7 | 4.30 | 12.02 | 18.79 | 4.00 | 84.3 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.10 | 11.89 | 19.56 | 2.00 | 84.1 | 90.0 |
| Bench 3 | Bench Boost | Micky van de Ven | DEF | 18 | 4.5 | 1.28 | 4.83 | 8.87 | 1.00 | 36.4 | 90.0 |
| Bench 4 | Bench Boost | Jaka Bijol | DEF | 11 | 3.9 | 0.06 | 0.52 | 2.81 | 0.00 | 1.0 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 6.60 | 20.10 | 33.99 | 11.00 | 89.2 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.77 | 12.14 | 20.02 | 5.00 | 67.6 | 90.0 |
| Bench 2 | Bench Boost | Dominic Calvert-Lewin | FWD | 11 | 5.9 | 2.99 | 9.06 | 15.22 | 7.00 | 62.4 | 90.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.4 | 5.86 | 16.61 | 26.61 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.36 | 15.84 | 25.87 | 2.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 4.71 | 14.19 | 22.78 | 2.00 | 80.7 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 4.76 | 13.91 | 22.49 | 10.00 | 83.5 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.04 | 11.76 | 18.77 | 2.00 | 78.1 | 90.0 |