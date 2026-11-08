# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW21
- Simulated weeks: GW22-GW25
- Total predicted points: 262.42
- Total actual points: 222.00
- Average predicted points: 65.61
- Average actual points: 55.50
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
- Predicted score: 64.45
- Actual score: 49.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: James Tarkowski replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.54 | 12.71 | 21.67 | 6.00 | 86.4 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 4.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 5.35 | 16.04 | 23.25 | 8.00 | 78.7 | 90.0 |
| Bench 2 | Autosub In | James Tarkowski | DEF | 9 | 5.7 | 4.18 | 13.09 | 21.11 | 8.00 | 86.9 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.3 | 4.68 | 12.86 | 20.56 | 0.00 | 90.0 | 0.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.6 | 4.64 | 11.90 | 18.49 | 0.00 | 82.5 | 90.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 3.05 | 8.58 | 13.17 | 0.00 | 83.6 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 7.23 | 20.64 | 33.53 | 2.00 | 90.0 | 79.0 |
| Bench 3 | Bench | Jarrod Bowen | FWD | 19 | 7.7 | 4.12 | 19.09 | 25.49 | 3.00 | 82.7 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.10 | 14.02 | 23.03 | 2.00 | 84.4 | 90.0 |
| Vice Captain | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 5.68 | 15.90 | 25.15 | 3.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.36 | 15.66 | 25.37 | 2.00 | 90.0 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.21 | 14.76 | 24.07 | 10.00 | 77.5 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.76 | 13.68 | 21.85 | 2.00 | 90.0 | 87.0 |
| XI | XI | James Garner | MID | 9 | 5.2 | 4.67 | 13.66 | 21.22 | 4.00 | 90.0 | 90.0 |

## GW23

- Train rows: 177836
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 63.31
- Actual score: 45.00
- Transfer: Harry Wilson -> Brenden Aaronson (projected gain 4.55, hit 0)
- Autosub: Brenden Aaronson replaced Bruno Guimarães Rodriguez Moura.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.44 | 12.89 | 21.47 | 1.00 | 86.0 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.20 | 0.05 | 0.00 | 0.00 | 5.7 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 4.88 | 15.15 | 22.38 | 1.00 | 79.4 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 5.21 | 13.94 | 22.61 | 4.00 | 89.5 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.6 | 3.93 | 10.73 | 17.15 | 7.00 | 82.9 | 90.0 |
| Bench 3 | Bench | Marc Guéhi | DEF | 8 | 5.2 | 2.97 | 7.60 | 12.93 | 6.00 | 49.6 | 90.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 1.79 | 5.45 | 9.07 | 0.00 | 44.5 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 7.20 | 20.04 | 33.48 | 1.00 | 90.0 | 17.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.6 | 4.08 | 16.69 | 26.88 | 12.00 | 85.5 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.26 | 15.02 | 24.42 | 2.00 | 89.0 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.53 | 15.46 | 24.70 | 8.00 | 90.0 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.49 | 15.43 | 25.16 | 2.00 | 80.8 | 90.0 |
| XI | XI | James Garner | MID | 9 | 5.2 | 4.99 | 14.31 | 22.28 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 5.09 | 14.03 | 23.20 | 0.00 | 79.3 | 0.0 |
| Bench 2 | Autosub In | Brenden Aaronson | MID | 11 | 5.4 | 3.96 | 11.69 | 18.26 | 4.00 | 85.2 | 84.0 |

## GW24

- Train rows: 178639
- Bank: 0.50 -> 0.00
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Morgan Rogers
- Effective captain: Antoine Semenyo
- Chip used: bench_boost
- Predicted score: 67.13
- Actual score: 68.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.21) beats the best remaining Bench Boost opportunity (9.62).
- Transfer: Bruno Guimarães Rodriguez Moura -> Morgan Rogers (projected gain 5.15, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.21) beats the best remaining Bench Boost opportunity (9.62).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.40 | 13.55 | 22.44 | 6.00 | 85.4 | 90.0 |
| Bench 1 | Bench Boost | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 4.4 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 5.74 | 16.01 | 25.47 | 8.00 | 86.7 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 3.95 | 11.85 | 19.58 | 2.00 | 81.9 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.2 | 3.85 | 10.99 | 17.61 | 3.00 | 75.1 | 90.0 |
| Bench 3 | Bench Boost | Micky van de Ven | DEF | 18 | 4.6 | 3.31 | 10.12 | 16.05 | 0.00 | 85.3 | 0.0 |
| Bench 4 | Bench Boost | Jaka Bijol | DEF | 11 | 3.9 | 1.12 | 3.47 | 7.10 | 0.00 | 27.7 | 0.0 |
| XI | XI | Erling Haaland | FWD | 13 | 15.0 | 5.51 | 16.58 | 29.45 | 5.00 | 79.0 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.6 | 5.62 | 15.94 | 28.09 | 8.00 | 84.8 | 80.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.09 | 13.17 | 19.85 | 2.00 | 79.6 | 90.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 7.7 | 5.80 | 15.91 | 25.44 | 7.00 | 90.0 | 90.0 |
| Vice Captain | XI | Morgan Rogers | MID | 2 | 7.7 | 5.75 | 15.87 | 25.30 | 2.00 | 90.0 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 4.43 | 13.44 | 22.77 | 12.00 | 71.1 | 86.0 |
| XI | XI | James Garner | MID | 9 | 5.2 | 3.98 | 12.68 | 20.29 | 4.00 | 84.3 | 90.0 |
| Bench 2 | Bench Boost | Brenden Aaronson | MID | 11 | 5.4 | 3.78 | 10.83 | 17.41 | 2.00 | 80.2 | 70.0 |

## GW25

- Train rows: 179450
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Jarrod Bowen
- Vice captain: Erling Haaland
- Effective captain: Jarrod Bowen
- Chip used: triple_captain
- Predicted score: 67.54
- Actual score: 60.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.39) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: James Tarkowski -> Trevoh Chalobah (projected gain 0.49, hit 0)
- Chip used: Triple Captain on Jarrod Bowen. Optimizer chose Triple Captain here because the current estimated captain upside (6.39) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.77 | 13.78 | 22.40 | 7.00 | 85.1 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 3.1 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 6.10 | 16.47 | 26.30 | 6.00 | 88.8 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.7 | 4.26 | 12.24 | 19.36 | 4.00 | 85.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.2 | 3.42 | 10.53 | 16.97 | 3.00 | 71.1 | 90.0 |
| Bench 3 | Bench | Micky van de Ven | DEF | 18 | 4.5 | 1.28 | 4.86 | 8.61 | 1.00 | 38.5 | 90.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 0.04 | 0.44 | 2.42 | 0.00 | 3.3 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.9 | 6.20 | 18.87 | 32.08 | 11.00 | 90.0 | 90.0 |
| Captain | Captain | Jarrod Bowen | FWD | 19 | 7.7 | 6.39 | 16.25 | 26.18 | 2.00 | 82.7 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.86 | 12.14 | 19.12 | 5.00 | 71.5 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.28 | 15.04 | 24.54 | 2.00 | 90.0 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 4.86 | 14.90 | 24.75 | 2.00 | 85.6 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 5.37 | 14.82 | 23.87 | 10.00 | 80.7 | 90.0 |
| XI | XI | James Garner | MID | 9 | 5.2 | 4.24 | 12.47 | 19.77 | 4.00 | 86.3 | 90.0 |
| Bench 2 | Bench | Brenden Aaronson | MID | 11 | 5.4 | 3.17 | 9.37 | 16.03 | 3.00 | 66.3 | 77.0 |