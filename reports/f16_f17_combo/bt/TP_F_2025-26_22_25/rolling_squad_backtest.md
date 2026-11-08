# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW21
- Simulated weeks: GW22-GW25
- Total predicted points: 263.35
- Total actual points: 225.00
- Average predicted points: 65.84
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
- Predicted score: 66.08
- Actual score: 40.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Micky van de Ven replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.80 | 11.02 | 17.98 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 5.00 | 13.92 | 20.08 | 8.00 | 81.2 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.3 | 4.61 | 13.01 | 20.95 | 0.00 | 90.0 | 0.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.37 | 12.85 | 20.27 | 8.00 | 90.0 | 90.0 |
| Bench 2 | Autosub In | Micky van de Ven | DEF | 18 | 4.6 | 4.15 | 10.86 | 17.16 | 0.00 | 81.5 | 90.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 3.30 | 9.02 | 13.78 | 0.00 | 80.5 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.24 | 24.02 | 39.05 | 2.00 | 90.0 | 79.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.50 | 14.86 | 23.34 | 2.00 | 82.1 | 90.0 |
| Bench 3 | Bench | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 4.06 | 12.52 | 19.68 | 2.00 | 77.7 | 90.0 |
| Vice Captain | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 5.75 | 16.16 | 25.76 | 3.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.48 | 16.03 | 25.83 | 2.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.09 | 14.80 | 24.58 | 2.00 | 88.1 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.11 | 14.40 | 23.91 | 3.00 | 81.1 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.89 | 13.72 | 22.01 | 2.00 | 89.9 | 87.0 |

## GW23

- Train rows: 177836
- Bank: 0.10 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 64.17
- Actual score: 55.00
- Transfer: Marc Guéhi -> Cristian Romero (projected gain 1.54, hit 0)
- Autosub: Micky van de Ven replaced Bruno Guimarães Rodriguez Moura.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.86 | 11.02 | 18.02 | 1.00 | 88.3 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.47 | 0.51 | 0.81 | 0.00 | 5.7 | 0.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.87 | 13.34 | 21.74 | 4.00 | 89.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 4.57 | 13.32 | 20.09 | 1.00 | 79.4 | 90.0 |
| XI | XI | Cristian Romero | DEF | 18 | 5.0 | 4.15 | 11.43 | 17.44 | 11.00 | 84.4 | 90.0 |
| Bench 2 | Autosub In | Micky van de Ven | DEF | 18 | 4.6 | 3.59 | 9.93 | 16.38 | 7.00 | 79.6 | 90.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 1.78 | 5.44 | 8.93 | 0.00 | 41.8 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.22 | 22.53 | 37.15 | 1.00 | 90.0 | 17.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.61 | 15.24 | 24.26 | 2.00 | 84.0 | 90.0 |
| Bench 3 | Bench | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 3.50 | 10.71 | 17.02 | 2.00 | 69.9 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.71 | 15.96 | 25.55 | 8.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.39 | 15.66 | 24.50 | 1.00 | 90.0 | 90.0 |
| XI | Bench | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 4.73 | 13.88 | 22.95 | 0.00 | 81.8 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.73 | 13.61 | 22.37 | 8.00 | 80.4 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.12 | 11.72 | 19.53 | 10.00 | 71.8 | 90.0 |

## GW24

- Train rows: 178639
- Bank: 0.30 -> 0.80
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 68.13
- Actual score: 55.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.75) beats the best remaining Triple Captain opportunity (7.36).
- Transfer: Bruno Guimarães Rodriguez Moura -> Enzo Fernández (projected gain 4.51, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (6.75) beats the best remaining Triple Captain opportunity (7.36).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.96 | 11.21 | 18.09 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 5.02 | 14.28 | 22.53 | 8.00 | 88.1 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.11 | 12.19 | 19.96 | 2.00 | 85.6 | 90.0 |
| XI | XI | Cristian Romero | DEF | 18 | 5.0 | 3.78 | 11.06 | 17.46 | 0.00 | 86.5 | 45.0 |
| Bench 3 | Bench | Micky van de Ven | DEF | 18 | 4.6 | 3.01 | 9.56 | 16.35 | 0.00 | 78.3 | 0.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 0.61 | 2.53 | 5.69 | 0.00 | 16.3 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.0 | 6.75 | 19.95 | 33.76 | 5.00 | 79.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.35 | 13.30 | 21.48 | 2.00 | 77.5 | 90.0 |
| Bench 2 | Bench | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 3.48 | 10.06 | 16.36 | 2.00 | 71.6 | 84.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.97 | 16.89 | 27.03 | 7.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.57 | 16.31 | 25.71 | 3.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.58 | 15.58 | 24.84 | 2.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 5.24 | 14.49 | 23.19 | 8.00 | 85.9 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.30 | 12.71 | 20.71 | 2.00 | 85.3 | 90.0 |

## GW25

- Train rows: 179450
- Bank: 0.80 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 64.97
- Actual score: 75.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (4.52) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Cristian Romero -> Trevoh Chalobah (projected gain 5.59, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (4.52) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.25 | 11.67 | 18.55 | 7.00 | 89.3 | 90.0 |
| Bench 1 | Bench Boost | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 5.54 | 15.13 | 23.82 | 6.00 | 89.5 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.7 | 4.34 | 12.08 | 18.82 | 4.00 | 85.3 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.16 | 11.97 | 19.62 | 2.00 | 85.4 | 90.0 |
| Bench 3 | Bench Boost | Micky van de Ven | DEF | 18 | 4.5 | 1.41 | 5.06 | 9.10 | 1.00 | 39.5 | 90.0 |
| Bench 4 | Bench Boost | Jaka Bijol | DEF | 11 | 3.9 | 0.14 | 0.65 | 3.02 | 0.00 | 2.5 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 6.68 | 20.25 | 34.14 | 11.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.83 | 12.23 | 20.10 | 5.00 | 69.5 | 90.0 |
| Bench 2 | Bench Boost | Dominic Calvert-Lewin | FWD | 11 | 5.9 | 2.98 | 9.03 | 15.25 | 7.00 | 61.7 | 90.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.4 | 5.88 | 16.64 | 26.61 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.42 | 15.93 | 25.94 | 2.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 4.75 | 14.25 | 22.82 | 2.00 | 81.8 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 4.82 | 14.02 | 22.59 | 10.00 | 85.1 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.09 | 11.82 | 18.81 | 2.00 | 79.3 | 90.0 |