# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW21
- Simulated weeks: GW22-GW25
- Total predicted points: 254.76
- Total actual points: 233.00
- Average predicted points: 63.69
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
- Predicted score: 63.44
- Actual score: 50.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Pascal Struijk replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.61 | 10.62 | 16.97 | 6.00 | 89.7 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.09 | 0.00 | 4.4 | 0.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.3 | 4.39 | 12.65 | 19.94 | 0.00 | 90.0 | 0.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.28 | 12.56 | 20.10 | 8.00 | 86.5 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 4.40 | 12.31 | 18.93 | 5.00 | 88.2 | 90.0 |
| Bench 3 | Autosub In | Pascal Struijk | DEF | 11 | 4.3 | 3.41 | 9.67 | 15.28 | 6.00 | 83.8 | 90.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 3.41 | 9.45 | 14.64 | 0.00 | 84.1 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 7.89 | 23.76 | 38.67 | 2.00 | 90.0 | 79.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.21 | 13.12 | 21.28 | 2.00 | 84.9 | 90.0 |
| Bench 2 | Bench | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 4.08 | 12.88 | 20.55 | 2.00 | 79.1 | 90.0 |
| Vice Captain | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 5.60 | 15.24 | 24.29 | 3.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.17 | 15.07 | 24.09 | 2.00 | 90.0 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.05 | 14.36 | 23.45 | 10.00 | 76.5 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.98 | 14.25 | 23.65 | 2.00 | 86.1 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.98 | 14.21 | 22.99 | 2.00 | 90.0 | 87.0 |

## GW23

- Train rows: 177836
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 62.70
- Actual score: 51.00
- Transfer: Marc Guéhi -> Cristian Romero (projected gain 2.05, hit 0)
- Autosub: Dominic Calvert-Lewin replaced Bruno Guimarães Rodriguez Moura.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.76 | 10.67 | 17.00 | 1.00 | 89.7 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.43 | 0.52 | 0.76 | 0.00 | 5.5 | 0.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.87 | 13.14 | 21.37 | 4.00 | 90.0 | 90.0 |
| XI | XI | Cristian Romero | DEF | 18 | 5.0 | 4.29 | 11.88 | 18.10 | 11.00 | 87.8 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 4.20 | 11.88 | 18.67 | 1.00 | 87.6 | 90.0 |
| Bench 3 | Bench | Pascal Struijk | DEF | 11 | 4.3 | 3.43 | 9.88 | 15.98 | 4.00 | 85.1 | 90.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 1.82 | 5.61 | 9.35 | 0.00 | 41.3 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 7.97 | 22.54 | 36.79 | 1.00 | 90.0 | 17.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.36 | 13.71 | 21.89 | 2.00 | 88.5 | 90.0 |
| Bench 2 | Autosub In | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 3.70 | 11.24 | 18.53 | 2.00 | 75.1 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.59 | 14.96 | 23.74 | 8.00 | 90.0 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.15 | 14.90 | 23.97 | 2.00 | 80.9 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.76 | 13.61 | 22.30 | 8.00 | 81.0 | 90.0 |
| XI | Bench | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 4.50 | 12.81 | 20.93 | 0.00 | 79.3 | 0.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.29 | 11.83 | 19.78 | 10.00 | 77.8 | 90.0 |

## GW24

- Train rows: 178639
- Bank: 0.20 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 63.56
- Actual score: 56.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.20) beats the best remaining Triple Captain opportunity (7.07).
- Transfer: Bruno Guimarães Rodriguez Moura -> Declan Rice (projected gain 4.83, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (6.20) beats the best remaining Triple Captain opportunity (7.07).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.83 | 10.68 | 17.20 | 6.00 | 88.6 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.04 | 0.24 | 0.00 | 3.9 | 0.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.01 | 11.69 | 19.29 | 2.00 | 83.1 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 3.92 | 11.29 | 18.39 | 5.00 | 81.5 | 90.0 |
| XI | XI | Cristian Romero | DEF | 18 | 5.0 | 3.86 | 11.11 | 17.68 | 0.00 | 87.5 | 45.0 |
| Bench 3 | Bench | Pascal Struijk | DEF | 11 | 4.3 | 3.54 | 10.15 | 16.57 | 2.00 | 82.9 | 90.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 1.12 | 3.76 | 7.54 | 0.00 | 26.2 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.0 | 6.20 | 19.30 | 33.13 | 5.00 | 71.5 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.13 | 12.86 | 20.56 | 2.00 | 80.9 | 90.0 |
| Bench 2 | Bench | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 3.62 | 10.75 | 18.02 | 2.00 | 73.8 | 84.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.72 | 16.15 | 25.98 | 7.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.48 | 15.54 | 24.88 | 2.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.4 | 5.35 | 15.48 | 24.85 | 3.00 | 90.0 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 4.40 | 13.30 | 22.67 | 12.00 | 72.8 | 86.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.25 | 12.70 | 20.62 | 2.00 | 87.5 | 90.0 |

## GW25

- Train rows: 179450
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 65.07
- Actual score: 76.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.16) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Cristian Romero -> Marcos Senesi Barón (projected gain 1.05, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.16) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.12 | 11.30 | 17.82 | 7.00 | 88.4 | 90.0 |
| Bench 1 | Bench Boost | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 2.5 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 4.46 | 12.02 | 19.27 | 6.00 | 81.2 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 3.98 | 11.68 | 19.20 | 2.00 | 81.6 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 4.11 | 11.14 | 18.05 | 2.00 | 87.4 | 90.0 |
| Bench 2 | Bench Boost | Pascal Struijk | DEF | 11 | 4.3 | 3.61 | 10.19 | 16.32 | 4.00 | 81.8 | 90.0 |
| Bench 4 | Bench Boost | Jaka Bijol | DEF | 11 | 3.9 | 0.19 | 0.89 | 3.49 | 0.00 | 5.7 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 6.40 | 20.00 | 33.16 | 11.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.78 | 12.33 | 20.15 | 5.00 | 76.2 | 90.0 |
| Bench 3 | Bench Boost | Dominic Calvert-Lewin | FWD | 11 | 5.9 | 3.37 | 9.98 | 16.67 | 7.00 | 69.0 | 90.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.4 | 5.69 | 15.75 | 25.24 | 5.00 | 90.0 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.09 | 15.24 | 25.14 | 2.00 | 86.2 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.21 | 15.20 | 24.91 | 2.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 4.59 | 13.29 | 21.66 | 10.00 | 80.5 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.07 | 11.47 | 18.20 | 2.00 | 82.0 | 90.0 |