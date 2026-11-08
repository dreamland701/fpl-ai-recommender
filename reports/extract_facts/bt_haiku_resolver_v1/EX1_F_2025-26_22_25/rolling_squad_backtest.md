# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW21
- Simulated weeks: GW22-GW25
- Total predicted points: 262.51
- Total actual points: 228.00
- Average predicted points: 65.63
- Average actual points: 57.00
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
- Vice captain: Declan Rice
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 65.96
- Actual score: 49.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Omar Alderete replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.69 | 10.75 | 17.52 | 6.00 | 86.5 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.02 | 0.23 | 0.00 | 4.1 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 4.89 | 13.60 | 19.55 | 8.00 | 77.3 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.3 | 4.51 | 12.69 | 20.39 | 0.00 | 90.0 | 0.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.30 | 12.65 | 19.96 | 8.00 | 87.1 | 90.0 |
| Bench 4 | Autosub In | Omar Alderete | DEF | 17 | 4.1 | 3.34 | 9.29 | 15.10 | 1.00 | 81.5 | 90.0 |
| Bench 3 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 3.36 | 9.27 | 14.26 | 0.00 | 83.6 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.30 | 24.32 | 39.48 | 2.00 | 90.0 | 79.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.51 | 15.02 | 23.67 | 2.00 | 83.7 | 90.0 |
| Bench 2 | Bench | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 3.99 | 12.39 | 19.51 | 2.00 | 75.6 | 90.0 |
| XI | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 5.62 | 15.75 | 25.04 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.3 | 5.74 | 15.62 | 25.41 | 3.00 | 84.9 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.22 | 14.56 | 23.60 | 10.00 | 77.5 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.99 | 14.51 | 24.03 | 2.00 | 83.4 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.89 | 13.86 | 22.33 | 2.00 | 90.0 | 87.0 |

## GW23

- Train rows: 177836
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 64.43
- Actual score: 44.00
- Transfer: Marc Guéhi -> Cristian Romero (projected gain 3.62, hit 0)
- Autosub: Dominic Calvert-Lewin replaced Bruno Guimarães Rodriguez Moura.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.84 | 10.91 | 17.65 | 1.00 | 86.2 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.46 | 0.55 | 0.87 | 0.00 | 5.7 | 0.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.89 | 13.34 | 21.58 | 4.00 | 89.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 4.59 | 13.33 | 19.91 | 1.00 | 79.0 | 90.0 |
| XI | XI | Cristian Romero | DEF | 18 | 5.0 | 4.25 | 11.77 | 17.89 | 11.00 | 88.1 | 90.0 |
| Bench 3 | Bench | Omar Alderete | DEF | 17 | 4.1 | 3.00 | 8.70 | 14.76 | 1.00 | 76.0 | 90.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 1.85 | 5.65 | 9.21 | 0.00 | 44.6 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.37 | 23.01 | 37.74 | 1.00 | 90.0 | 17.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.73 | 15.62 | 24.76 | 2.00 | 88.7 | 90.0 |
| Bench 2 | Autosub In | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 3.58 | 10.97 | 17.36 | 2.00 | 72.2 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.42 | 15.71 | 24.37 | 1.00 | 90.0 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.24 | 14.96 | 24.48 | 2.00 | 81.1 | 90.0 |
| XI | Bench | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 4.76 | 13.82 | 22.59 | 0.00 | 80.1 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.74 | 13.58 | 22.11 | 8.00 | 78.9 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.22 | 12.03 | 19.96 | 10.00 | 75.3 | 90.0 |

## GW24

- Train rows: 178639
- Bank: 0.20 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Morgan Rogers
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 66.07
- Actual score: 60.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.76) beats the best remaining Triple Captain opportunity (7.37).
- Transfer: Bruno Guimarães Rodriguez Moura -> Enzo Fernández (projected gain 3.78, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (6.76) beats the best remaining Triple Captain opportunity (7.37).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.85 | 10.90 | 17.60 | 6.00 | 85.4 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.18 | 0.34 | 0.00 | 4.4 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 4.95 | 14.16 | 22.35 | 8.00 | 86.1 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.02 | 11.98 | 19.65 | 2.00 | 82.2 | 90.0 |
| XI | XI | Cristian Romero | DEF | 18 | 5.0 | 3.80 | 11.24 | 17.84 | 0.00 | 87.8 | 45.0 |
| Bench 3 | Bench | Omar Alderete | DEF | 17 | 4.1 | 3.38 | 8.92 | 14.49 | 6.00 | 79.0 | 85.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 1.09 | 3.71 | 7.34 | 0.00 | 28.0 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.0 | 6.76 | 20.23 | 34.27 | 5.00 | 79.4 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.41 | 13.62 | 22.00 | 2.00 | 80.1 | 90.0 |
| Bench 2 | Bench | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 3.50 | 10.28 | 16.78 | 2.00 | 72.5 | 84.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.49 | 16.16 | 25.42 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Morgan Rogers | MID | 2 | 7.7 | 5.51 | 15.43 | 24.57 | 2.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 5.08 | 13.99 | 22.37 | 8.00 | 80.3 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 4.37 | 13.22 | 22.28 | 12.00 | 71.7 | 86.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.31 | 12.84 | 20.99 | 2.00 | 86.1 | 90.0 |

## GW25

- Train rows: 179450
- Bank: 0.70 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 66.05
- Actual score: 75.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.92) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Cristian Romero -> Trevoh Chalobah (projected gain 3.84, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.92) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.14 | 11.42 | 18.17 | 7.00 | 85.0 | 90.0 |
| Bench 1 | Bench Boost | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 3.1 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 5.49 | 15.13 | 23.89 | 6.00 | 88.4 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.7 | 4.30 | 12.12 | 19.00 | 4.00 | 84.8 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.09 | 11.82 | 19.40 | 2.00 | 82.5 | 90.0 |
| Bench 3 | Bench Boost | Omar Alderete | DEF | 17 | 4.1 | 2.71 | 8.32 | 13.33 | 1.00 | 78.1 | 90.0 |
| Bench 4 | Bench Boost | Jaka Bijol | DEF | 11 | 3.9 | 0.15 | 0.77 | 3.20 | 0.00 | 4.0 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 6.73 | 20.59 | 34.72 | 11.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.93 | 12.71 | 20.90 | 5.00 | 73.0 | 90.0 |
| Bench 2 | Bench Boost | Dominic Calvert-Lewin | FWD | 11 | 5.9 | 3.06 | 9.33 | 15.67 | 7.00 | 64.3 | 90.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.4 | 6.27 | 17.50 | 28.24 | 5.00 | 90.0 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.02 | 15.22 | 25.22 | 2.00 | 85.5 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 4.60 | 13.82 | 22.09 | 2.00 | 76.4 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 4.75 | 13.81 | 22.22 | 10.00 | 81.1 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.07 | 11.91 | 19.02 | 2.00 | 79.5 | 90.0 |