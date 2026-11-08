# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW21
- Simulated weeks: GW22-GW25
- Total predicted points: 250.78
- Total actual points: 217.00
- Average predicted points: 62.70
- Average actual points: 54.25
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
- Bank: 100.00 -> 0.20
- Free transfers: 1 -> 2
- Captain: Igor Thiago Nascimento Rodrigues
- Vice captain: Bruno Guimarães Rodriguez Moura
- Effective captain: Igor Thiago Nascimento Rodrigues
- Chip used: none
- Predicted score: 58.48
- Actual score: 48.00
- Chip advisory: bench_boost (0.62): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub outfielders: Virgil van Dijk.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.71 | 10.98 | 18.14 | 6.00 | 85.2 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.5 | 3.39 | 10.32 | 16.96 | 1.00 | 89.3 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.53 | 13.28 | 20.81 | 8.00 | 88.5 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 13 | 5.3 | 4.53 | 13.15 | 21.20 | 0.00 | 91.5 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.6 | 4.46 | 12.86 | 19.33 | 8.00 | 71.3 | 90.0 |
| Bench 2 | Autosub In | Virgil van Dijk | DEF | 12 | 5.9 | 4.37 | 11.83 | 19.19 | 2.00 | 84.8 | 90.0 |
| Bench 3 | Bench | Nathan Collins | DEF | 5 | 4.9 | 4.01 | 11.72 | 19.46 | 1.00 | 85.6 | 90.0 |
| Captain | Captain | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.47 | 15.13 | 24.06 | 2.00 | 86.9 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.7 | 5.15 | 14.87 | 22.97 | 2.00 | 78.1 | 90.0 |
| Bench 4 | Bench | Dominic Calvert-Lewin | FWD | 11 | 5.9 | 4.00 | 12.45 | 20.08 | 2.00 | 73.6 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 4.96 | 15.38 | 25.23 | 2.00 | 89.5 | 90.0 |
| Vice Captain | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.1 | 5.33 | 15.02 | 24.23 | 3.00 | 93.9 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.8 | 4.74 | 14.69 | 24.75 | 1.00 | 75.7 | 45.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.17 | 14.31 | 23.10 | 10.00 | 74.2 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 4.97 | 14.25 | 23.75 | 2.00 | 81.0 | 90.0 |

## GW23

- Train rows: 177836
- Bank: 0.20 -> 1.60
- Free transfers: 2 -> 2
- Captain: Igor Thiago Nascimento Rodrigues
- Vice captain: Bruno Guimarães Rodriguez Moura
- Effective captain: Igor Thiago Nascimento Rodrigues
- Chip used: none
- Predicted score: 59.01
- Actual score: 40.00
- Transfer: Phil Foden -> Declan Rice (projected gain 3.78, hit 0)
- Autosub outfielders: Dominic Calvert-Lewin.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.86 | 11.45 | 18.71 | 1.00 | 84.8 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.6 | 3.21 | 9.38 | 15.54 | 1.00 | 81.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 4.73 | 13.91 | 21.23 | 1.00 | 80.0 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.62 | 12.63 | 20.60 | 4.00 | 83.6 | 90.0 |
| XI | XI | Nathan Collins | DEF | 5 | 5.0 | 3.93 | 11.09 | 18.25 | 1.00 | 84.4 | 90.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 12 | 5.9 | 3.56 | 10.95 | 17.99 | 9.00 | 84.0 | 90.0 |
| Bench 4 | Bench | Marc Guéhi | DEF | 13 | 5.3 | 3.03 | 8.57 | 14.83 | 6.00 | 49.0 | 90.0 |
| Captain | Captain | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.95 | 16.42 | 26.20 | 2.00 | 90.2 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 4.21 | 12.92 | 20.89 | 8.00 | 72.4 | 90.0 |
| Bench 2 | Autosub In | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 4.04 | 11.84 | 18.81 | 2.00 | 76.9 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.32 | 15.60 | 24.61 | 1.00 | 91.8 | 90.0 |
| Vice Captain | Bench | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 5.44 | 15.45 | 24.76 | 0.00 | 88.3 | 0.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.30 | 15.21 | 24.75 | 8.00 | 83.9 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 4.71 | 14.44 | 23.74 | 2.00 | 78.4 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.00 | 14.18 | 23.11 | 8.00 | 81.8 | 90.0 |

## GW24

- Train rows: 178639
- Bank: 1.60 -> 2.90
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Declan Rice
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 62.87
- Actual score: 64.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.57) beats the best remaining Triple Captain opportunity (7.15).
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Bruno Guimarães Rodriguez Moura -> Harry Wilson (projected gain 2.48, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (5.57) beats the best remaining Triple Captain opportunity (7.15).
- Autosub outfielders: Dominic Calvert-Lewin.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.74 | 11.00 | 18.05 | 6.00 | 83.2 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.6 | 2.66 | 8.70 | 14.67 | 10.00 | 80.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 4.56 | 13.23 | 21.23 | 8.00 | 78.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.44 | 12.87 | 20.83 | 4.00 | 92.1 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.8 | 4.08 | 11.78 | 19.14 | 2.00 | 82.3 | 90.0 |
| Bench 3 | Bench | Marc Guéhi | DEF | 13 | 5.2 | 3.71 | 10.89 | 18.17 | 3.00 | 72.2 | 90.0 |
| Bench 4 | Bench | Nathan Collins | DEF | 5 | 5.0 | 2.99 | 9.67 | 16.33 | 1.00 | 81.8 | 30.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 5.04 | 14.67 | 23.46 | 2.00 | 87.0 | 90.0 |
| XI | Bench | Ollie Watkins | FWD | 2 | 8.8 | 4.42 | 13.26 | 22.11 | 0.00 | 75.0 | 0.0 |
| Bench 2 | Autosub In | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 3.78 | 10.96 | 17.92 | 2.00 | 77.0 | 84.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 7.7 | 5.57 | 16.19 | 26.43 | 7.00 | 93.6 | 90.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.4 | 5.42 | 15.87 | 25.00 | 3.00 | 91.2 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.32 | 15.35 | 24.73 | 2.00 | 89.0 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.3 | 4.67 | 13.88 | 23.25 | 12.00 | 76.5 | 86.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.46 | 13.38 | 22.00 | 2.00 | 87.6 | 90.0 |

## GW25

- Train rows: 179450
- Bank: 2.90 -> 4.40
- Free transfers: 2 -> 2
- Captain: Declan Rice
- Vice captain: Antoine Semenyo
- Effective captain: Declan Rice
- Chip used: bench_boost
- Predicted score: 70.42
- Actual score: 65.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.03) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Ollie Watkins -> João Pedro Junqueira de Jesus (projected gain 2.37, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.03) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.11 | 11.67 | 18.97 | 7.00 | 84.0 | 90.0 |
| Bench 1 | Bench Boost | Caoimhín Kelleher | GK | 5 | 4.6 | 3.23 | 9.84 | 16.25 | 1.00 | 85.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.0 | 5.32 | 14.96 | 23.89 | 6.00 | 85.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.27 | 12.55 | 19.94 | 0.00 | 90.9 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.8 | 4.16 | 11.90 | 19.25 | 2.00 | 83.5 | 90.0 |
| Bench 2 | Bench Boost | Marc Guéhi | DEF | 13 | 5.2 | 3.72 | 11.00 | 18.13 | 3.00 | 73.9 | 90.0 |
| Bench 4 | Bench Boost | Nathan Collins | DEF | 5 | 5.0 | 2.77 | 8.82 | 15.11 | 0.00 | 61.8 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 4.25 | 14.17 | 23.25 | 5.00 | 76.1 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.3 | 4.56 | 13.28 | 21.30 | 8.00 | 63.7 | 74.0 |
| Bench 3 | Bench Boost | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 3.32 | 9.80 | 16.44 | 7.00 | 66.4 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.8 | 5.36 | 16.00 | 26.36 | 2.00 | 93.8 | 90.0 |
| Captain | Captain | Declan Rice | MID | 1 | 7.4 | 5.58 | 15.95 | 25.75 | 5.00 | 85.9 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.98 | 14.75 | 23.76 | 10.00 | 84.7 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.3 | 5.04 | 14.55 | 24.14 | 2.00 | 83.6 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.1 | 4.19 | 12.19 | 19.66 | 2.00 | 80.7 | 90.0 |