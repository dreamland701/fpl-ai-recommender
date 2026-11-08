# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW21
- Simulated weeks: GW22-GW25
- Total predicted points: 262.09
- Total actual points: 225.00
- Average predicted points: 65.52
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
- Predicted score: 65.53
- Actual score: 40.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Micky van de Ven replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.68 | 10.72 | 17.51 | 6.00 | 86.4 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.31 | 0.30 | 0.45 | 0.00 | 2.8 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 4.97 | 13.80 | 19.86 | 8.00 | 79.3 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.3 | 4.50 | 12.69 | 20.45 | 0.00 | 90.0 | 0.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.30 | 12.68 | 20.04 | 8.00 | 87.4 | 90.0 |
| Bench 2 | Autosub In | Micky van de Ven | DEF | 18 | 4.6 | 4.17 | 11.03 | 17.55 | 0.00 | 83.3 | 90.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 3.31 | 9.10 | 13.98 | 0.00 | 81.9 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.27 | 24.25 | 39.51 | 2.00 | 90.0 | 79.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.55 | 15.14 | 23.94 | 2.00 | 85.2 | 90.0 |
| Bench 3 | Bench | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 4.02 | 12.46 | 19.65 | 2.00 | 76.6 | 90.0 |
| Vice Captain | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 5.67 | 15.86 | 25.25 | 3.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.38 | 15.75 | 25.39 | 2.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.99 | 14.49 | 24.05 | 2.00 | 83.7 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.02 | 14.21 | 23.64 | 3.00 | 78.1 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.93 | 13.95 | 22.48 | 2.00 | 90.0 | 87.0 |

## GW23

- Train rows: 177836
- Bank: 0.10 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 64.79
- Actual score: 55.00
- Transfer: Marc Guéhi -> Cristian Romero (projected gain 1.63, hit 0)
- Autosub: Micky van de Ven replaced Bruno Guimarães Rodriguez Moura.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.82 | 10.87 | 17.63 | 1.00 | 86.1 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.00 | 0.19 | 0.00 | 4.8 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 4.61 | 13.37 | 20.02 | 1.00 | 79.8 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.90 | 13.36 | 21.66 | 4.00 | 90.0 | 90.0 |
| XI | XI | Cristian Romero | DEF | 18 | 5.0 | 4.28 | 11.84 | 18.03 | 11.00 | 88.9 | 90.0 |
| Bench 2 | Autosub In | Micky van de Ven | DEF | 18 | 4.6 | 3.69 | 10.27 | 16.91 | 7.00 | 83.7 | 90.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 1.81 | 5.50 | 8.96 | 0.00 | 43.1 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.33 | 22.91 | 37.73 | 1.00 | 90.0 | 17.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.76 | 15.71 | 24.99 | 2.00 | 89.9 | 90.0 |
| Bench 3 | Bench | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 3.58 | 10.95 | 17.34 | 2.00 | 72.5 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.69 | 15.80 | 25.15 | 8.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.43 | 15.73 | 24.45 | 1.00 | 90.0 | 90.0 |
| XI | Bench | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 4.71 | 13.69 | 22.48 | 0.00 | 79.7 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.71 | 13.47 | 22.00 | 8.00 | 78.5 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.22 | 12.02 | 19.98 | 10.00 | 75.8 | 90.0 |

## GW24

- Train rows: 178639
- Bank: 0.30 -> 0.80
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 67.53
- Actual score: 55.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.70) beats the best remaining Triple Captain opportunity (7.31).
- Transfer: Bruno Guimarães Rodriguez Moura -> Enzo Fernández (projected gain 4.06, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (6.70) beats the best remaining Triple Captain opportunity (7.31).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.84 | 10.88 | 17.61 | 6.00 | 85.5 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.05 | 0.10 | 0.17 | 0.00 | 3.3 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 4.98 | 14.23 | 22.49 | 8.00 | 86.9 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.01 | 11.97 | 19.69 | 2.00 | 82.3 | 90.0 |
| XI | XI | Cristian Romero | DEF | 18 | 5.0 | 3.81 | 11.28 | 17.96 | 0.00 | 88.5 | 45.0 |
| Bench 3 | Bench | Micky van de Ven | DEF | 18 | 4.6 | 3.23 | 9.72 | 16.32 | 0.00 | 86.0 | 0.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 1.04 | 3.54 | 7.05 | 0.00 | 26.4 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.0 | 6.70 | 20.07 | 34.14 | 5.00 | 78.4 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.39 | 13.59 | 22.09 | 2.00 | 80.5 | 90.0 |
| Bench 2 | Bench | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 3.47 | 10.18 | 16.66 | 2.00 | 72.2 | 84.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.89 | 16.70 | 26.77 | 7.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.52 | 16.22 | 25.57 | 3.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.50 | 15.37 | 24.54 | 2.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 5.14 | 14.15 | 22.64 | 8.00 | 81.9 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.33 | 12.89 | 21.10 | 2.00 | 87.0 | 90.0 |

## GW25

- Train rows: 179450
- Bank: 0.80 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 64.24
- Actual score: 75.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (4.42) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Cristian Romero -> Trevoh Chalobah (projected gain 5.61, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (4.42) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.14 | 11.39 | 18.15 | 7.00 | 85.1 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 1.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 5.51 | 15.14 | 23.94 | 6.00 | 88.8 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.7 | 4.33 | 12.18 | 19.12 | 4.00 | 85.5 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.08 | 11.79 | 19.39 | 2.00 | 82.5 | 90.0 |
| Bench 3 | Bench Boost | Micky van de Ven | DEF | 18 | 4.5 | 1.33 | 5.06 | 9.31 | 1.00 | 39.0 | 90.0 |
| Bench 4 | Bench Boost | Jaka Bijol | DEF | 11 | 3.9 | 0.08 | 0.53 | 2.81 | 0.00 | 1.8 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 6.64 | 20.37 | 34.52 | 11.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.85 | 12.52 | 20.75 | 5.00 | 72.4 | 90.0 |
| Bench 2 | Bench Boost | Dominic Calvert-Lewin | FWD | 11 | 5.9 | 3.02 | 9.22 | 15.53 | 7.00 | 63.9 | 90.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.4 | 5.84 | 16.54 | 26.48 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.34 | 15.77 | 25.73 | 2.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 4.65 | 13.93 | 22.28 | 2.00 | 77.8 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 4.71 | 13.72 | 22.14 | 10.00 | 80.7 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.08 | 11.95 | 19.12 | 2.00 | 80.3 | 90.0 |