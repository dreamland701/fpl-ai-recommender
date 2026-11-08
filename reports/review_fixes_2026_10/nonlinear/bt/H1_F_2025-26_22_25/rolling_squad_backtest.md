# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW21
- Simulated weeks: GW22-GW25
- Total predicted points: 243.19
- Total actual points: 199.00
- Average predicted points: 60.80
- Average actual points: 49.75
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
- Captain: Declan Rice
- Vice captain: Morgan Rogers
- Effective captain: Declan Rice
- Chip used: none
- Predicted score: 54.30
- Actual score: 36.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Nathan Collins replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.75 | 11.10 | 18.06 | 6.00 | 91.0 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.6 | 3.01 | 9.77 | 15.94 | 1.00 | 85.2 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.3 | 4.02 | 12.85 | 20.66 | 0.00 | 89.2 | 0.0 |
| Bench 3 | Bench | Jurriën Timber | DEF | 1 | 6.3 | 3.71 | 12.62 | 19.74 | 5.00 | 80.8 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.21 | 12.56 | 19.85 | 8.00 | 85.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.88 | 12.02 | 19.38 | 2.00 | 85.1 | 90.0 |
| Bench 2 | Autosub In | Nathan Collins | DEF | 5 | 5.0 | 3.87 | 11.36 | 19.18 | 1.00 | 79.7 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 15.1 | 4.71 | 24.48 | 39.81 | 2.00 | 85.0 | 79.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 4.01 | 12.54 | 19.75 | 2.00 | 79.8 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.5 | 3.21 | 8.10 | 12.27 | 2.00 | 76.2 | 90.0 |
| XI | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 4.90 | 15.79 | 25.15 | 3.00 | 83.8 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 4.30 | 15.77 | 25.40 | 2.00 | 85.5 | 90.0 |
| Vice Captain | XI | Morgan Rogers | MID | 2 | 7.7 | 4.95 | 14.61 | 24.21 | 2.00 | 84.6 | 90.0 |
| Captain | Captain | Declan Rice | MID | 1 | 7.3 | 5.31 | 14.21 | 23.60 | 3.00 | 82.0 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 3.96 | 14.11 | 22.72 | 2.00 | 84.3 | 87.0 |

## GW23

- Train rows: 177836
- Bank: 0.00 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Guimarães Rodriguez Moura
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 61.24
- Actual score: 42.00
- Transfer: Virgil van Dijk -> Trevoh Chalobah (projected gain 1.88, hit 0)
- Autosub: Nathan Collins replaced Bruno Guimarães Rodriguez Moura.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.74 | 11.19 | 18.08 | 1.00 | 86.6 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.6 | 2.78 | 9.01 | 14.91 | 1.00 | 85.4 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 5.01 | 13.36 | 21.62 | 4.00 | 85.3 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.6 | 4.62 | 12.48 | 19.29 | 4.00 | 86.1 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 4.62 | 12.32 | 19.37 | 1.00 | 86.1 | 90.0 |
| Bench 2 | Autosub In | Nathan Collins | DEF | 5 | 5.0 | 3.46 | 10.61 | 17.61 | 1.00 | 83.2 | 90.0 |
| Bench 3 | Bench | Marc Guéhi | DEF | 8 | 5.2 | 2.13 | 7.79 | 13.48 | 6.00 | 51.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 7.17 | 23.22 | 38.14 | 1.00 | 66.9 | 17.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 3.88 | 11.05 | 17.50 | 2.00 | 80.2 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.5 | 1.80 | 7.95 | 12.77 | 2.00 | 77.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.01 | 15.71 | 25.01 | 8.00 | 88.1 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.12 | 15.59 | 24.26 | 1.00 | 87.7 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.67 | 13.47 | 21.99 | 8.00 | 83.7 | 90.0 |
| Vice Captain | Bench | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 5.35 | 13.37 | 21.97 | 0.00 | 79.7 | 0.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.89 | 12.10 | 20.08 | 10.00 | 82.6 | 90.0 |

## GW24

- Train rows: 178639
- Bank: 0.30 -> 0.80
- Free transfers: 2 -> 2
- Captain: Morgan Rogers
- Vice captain: Enzo Fernández
- Effective captain: Morgan Rogers
- Chip used: triple_captain
- Predicted score: 57.78
- Actual score: 50.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.32) beats the best remaining Triple Captain opportunity (6.60).
- Transfer: Bruno Guimarães Rodriguez Moura -> Enzo Fernández (projected gain 1.57, hit 0)
- Chip used: Triple Captain on Morgan Rogers. Optimizer chose Triple Captain here because the current estimated captain upside (5.32) beats the best remaining Triple Captain opportunity (6.60).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.62 | 11.21 | 18.07 | 6.00 | 85.6 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.6 | 2.47 | 8.31 | 13.96 | 10.00 | 85.1 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.6 | 4.62 | 13.04 | 20.19 | 3.00 | 87.1 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 3.64 | 12.04 | 19.74 | 2.00 | 85.4 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 3.91 | 11.81 | 19.20 | 5.00 | 79.9 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.2 | 3.54 | 10.90 | 17.83 | 3.00 | 84.6 | 90.0 |
| Bench 4 | Bench | Nathan Collins | DEF | 5 | 5.0 | 2.94 | 9.08 | 15.45 | 1.00 | 76.7 | 30.0 |
| XI | XI | Erling Haaland | FWD | 13 | 15.0 | 4.15 | 20.32 | 34.46 | 5.00 | 56.3 | 90.0 |
| Bench 3 | Bench | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 2.99 | 10.22 | 16.71 | 2.00 | 73.3 | 84.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.5 | 3.13 | 8.04 | 13.30 | 2.00 | 80.7 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.04 | 16.76 | 26.85 | 7.00 | 87.5 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 4.97 | 16.15 | 25.46 | 3.00 | 85.4 | 90.0 |
| Captain | Captain | Morgan Rogers | MID | 2 | 7.7 | 5.32 | 15.41 | 24.60 | 2.00 | 86.3 | 90.0 |
| Vice Captain | XI | Enzo Fernández | MID | 7 | 6.7 | 5.20 | 14.33 | 22.88 | 8.00 | 84.5 | 90.0 |
| Bench 2 | Bench | Harry Wilson | MID | 10 | 6.0 | 3.12 | 12.88 | 21.07 | 2.00 | 84.5 | 90.0 |

## GW25

- Train rows: 179450
- Bank: 0.80 -> 1.00
- Free transfers: 2 -> 2
- Captain: Declan Rice
- Vice captain: Marcos Senesi Barón
- Effective captain: Declan Rice
- Chip used: bench_boost
- Predicted score: 69.86
- Actual score: 71.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (14.26) beats the best remaining Bench Boost opportunity (0.00).
- Chip advisory: bench_boost (0.62): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Nathan Collins -> Marcos Senesi Barón (projected gain 2.22, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (14.26) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.39 | 11.69 | 18.58 | 7.00 | 87.9 | 90.0 |
| Bench 1 | Bench Boost | Caoimhín Kelleher | GK | 5 | 4.6 | 3.22 | 8.92 | 14.70 | 1.00 | 86.6 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.6 | 4.43 | 12.33 | 19.34 | 4.00 | 85.9 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 4.49 | 12.30 | 19.81 | 6.00 | 84.2 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.28 | 11.79 | 19.37 | 2.00 | 85.4 | 90.0 |
| Vice Captain | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 4.83 | 11.38 | 18.29 | 2.00 | 87.5 | 90.0 |
| Bench 4 | Bench Boost | Marc Guéhi | DEF | 8 | 5.2 | 3.16 | 10.47 | 17.25 | 3.00 | 80.1 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.9 | 4.64 | 20.55 | 34.74 | 11.00 | 78.0 | 90.0 |
| Bench 2 | Bench Boost | Dominic Calvert-Lewin | FWD | 11 | 5.9 | 3.96 | 9.24 | 15.56 | 7.00 | 76.5 | 90.0 |
| Bench 3 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 3.92 | 8.60 | 14.06 | 2.00 | 86.6 | 90.0 |
| Captain | Captain | Declan Rice | MID | 1 | 7.4 | 5.22 | 16.32 | 26.14 | 5.00 | 85.5 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.7 | 4.81 | 15.89 | 25.92 | 2.00 | 87.4 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 4.43 | 13.95 | 22.31 | 2.00 | 85.4 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 4.63 | 13.74 | 22.18 | 10.00 | 82.9 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.23 | 11.95 | 19.11 | 2.00 | 86.1 | 90.0 |