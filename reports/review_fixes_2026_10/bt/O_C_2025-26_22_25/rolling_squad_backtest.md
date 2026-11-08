# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW21
- Simulated weeks: GW22-GW25
- Total predicted points: 259.48
- Total actual points: 224.00
- Average predicted points: 64.87
- Average actual points: 56.00
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
- Bank: 100.00 -> 2.60
- Free transfers: 1 -> 2
- Captain: Bruno Guimarães Rodriguez Moura
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Bruno Guimarães Rodriguez Moura
- Chip used: none
- Predicted score: 59.70
- Actual score: 41.00
- Chip advisory: bench_boost (0.67): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub outfielders: Virgil van Dijk.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.82 | 11.38 | 18.80 | 6.00 | 87.8 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.5 | 3.67 | 11.01 | 18.04 | 1.00 | 93.3 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 13 | 5.3 | 4.83 | 13.88 | 22.33 | 0.00 | 95.8 | 0.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.41 | 12.99 | 20.40 | 8.00 | 88.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.6 | 4.47 | 12.97 | 19.52 | 8.00 | 73.0 | 90.0 |
| Bench 3 | Bench | Nathan Collins | DEF | 5 | 4.9 | 4.25 | 12.24 | 20.26 | 1.00 | 88.2 | 90.0 |
| Bench 2 | Autosub In | Virgil van Dijk | DEF | 12 | 5.9 | 4.33 | 11.91 | 19.40 | 2.00 | 86.9 | 90.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.72 | 15.83 | 25.10 | 2.00 | 89.4 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.7 | 4.89 | 13.89 | 21.55 | 2.00 | 75.6 | 90.0 |
| Bench 4 | Bench | Dominic Calvert-Lewin | FWD | 11 | 5.9 | 4.25 | 12.85 | 20.63 | 2.00 | 76.8 | 90.0 |
| Captain | Captain | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.1 | 5.78 | 16.19 | 25.92 | 3.00 | 96.2 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.22 | 15.83 | 25.85 | 2.00 | 92.1 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.8 | 4.89 | 14.97 | 25.15 | 1.00 | 77.1 | 45.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 4.96 | 14.38 | 24.04 | 2.00 | 82.2 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.8 | 4.92 | 14.13 | 23.24 | 2.00 | 90.2 | 87.0 |

## GW23

- Train rows: 177836
- Bank: 2.60 -> 4.00
- Free transfers: 2 -> 2
- Captain: Igor Thiago Nascimento Rodrigues
- Vice captain: Declan Rice
- Effective captain: Igor Thiago Nascimento Rodrigues
- Chip used: none
- Predicted score: 60.87
- Actual score: 48.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Phil Foden -> Declan Rice (projected gain 4.16, hit 0)
- Autosub outfielders: Dominic Calvert-Lewin.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.14 | 12.12 | 19.76 | 1.00 | 88.6 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.6 | 3.37 | 9.92 | 16.44 | 1.00 | 85.4 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 5.04 | 14.38 | 21.83 | 1.00 | 81.8 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.62 | 12.66 | 20.68 | 4.00 | 84.1 | 90.0 |
| XI | XI | Nathan Collins | DEF | 5 | 5.0 | 4.00 | 11.38 | 18.75 | 1.00 | 86.7 | 90.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 12 | 5.9 | 3.71 | 11.35 | 18.63 | 9.00 | 86.2 | 90.0 |
| Bench 4 | Bench | Marc Guéhi | DEF | 13 | 5.3 | 3.34 | 9.26 | 15.89 | 6.00 | 52.9 | 90.0 |
| Captain | Captain | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.97 | 16.47 | 26.39 | 2.00 | 92.8 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 4.27 | 12.82 | 20.53 | 8.00 | 70.6 | 90.0 |
| Bench 2 | Autosub In | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 4.15 | 12.06 | 19.21 | 2.00 | 79.2 | 90.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.3 | 5.64 | 16.20 | 25.41 | 1.00 | 93.4 | 90.0 |
| XI | Bench | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 5.52 | 16.08 | 25.85 | 0.00 | 90.6 | 0.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.61 | 15.80 | 25.56 | 8.00 | 86.8 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.28 | 14.92 | 24.21 | 8.00 | 84.9 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.80 | 13.62 | 22.54 | 10.00 | 81.7 | 90.0 |

## GW24

- Train rows: 178639
- Bank: 4.00 -> 2.00
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Morgan Rogers
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 65.33
- Actual score: 62.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.78) beats the best remaining Triple Captain opportunity (7.26).
- Chip advisory: bench_boost (0.62): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Bruno Guimarães Rodriguez Moura -> Bruno Borges Fernandes (projected gain 2.31, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (5.78) beats the best remaining Triple Captain opportunity (7.26).
- Autosub outfielders: Dominic Calvert-Lewin.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.89 | 11.49 | 18.84 | 6.00 | 86.4 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.6 | 3.03 | 9.59 | 16.11 | 10.00 | 85.3 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 4.69 | 13.61 | 21.84 | 8.00 | 81.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.70 | 13.44 | 21.69 | 4.00 | 95.4 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.8 | 3.98 | 11.66 | 18.98 | 2.00 | 81.4 | 90.0 |
| Bench 3 | Bench | Marc Guéhi | DEF | 13 | 5.2 | 3.96 | 11.55 | 19.21 | 3.00 | 76.6 | 90.0 |
| Bench 4 | Bench | Nathan Collins | DEF | 5 | 5.0 | 3.30 | 10.38 | 17.47 | 1.00 | 84.8 | 30.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 5.26 | 15.93 | 25.47 | 2.00 | 90.3 | 90.0 |
| XI | Bench | Ollie Watkins | FWD | 2 | 8.8 | 4.55 | 13.32 | 22.08 | 0.00 | 74.7 | 0.0 |
| Bench 2 | Autosub In | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 4.12 | 11.94 | 19.42 | 2.00 | 81.4 | 84.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 7.7 | 5.78 | 16.63 | 27.10 | 7.00 | 96.8 | 90.0 |
| Vice Captain | XI | Morgan Rogers | MID | 2 | 7.7 | 5.65 | 16.15 | 25.94 | 2.00 | 93.1 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.4 | 5.49 | 16.01 | 25.21 | 3.00 | 92.1 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.84 | 14.23 | 23.26 | 2.00 | 91.8 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.3 | 4.95 | 14.19 | 21.80 | 10.00 | 71.2 | 90.0 |

## GW25

- Train rows: 179450
- Bank: 2.00 -> 3.50
- Free transfers: 2 -> 2
- Captain: Declan Rice
- Vice captain: Antoine Semenyo
- Effective captain: Declan Rice
- Chip used: bench_boost
- Predicted score: 73.59
- Actual score: 73.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.90) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Ollie Watkins -> João Pedro Junqueira de Jesus (projected gain 2.10, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.90) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.36 | 12.30 | 19.98 | 7.00 | 87.7 | 90.0 |
| Bench 1 | Bench Boost | Caoimhín Kelleher | GK | 5 | 4.6 | 3.48 | 10.50 | 17.31 | 1.00 | 89.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.0 | 5.57 | 15.48 | 24.67 | 6.00 | 88.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.43 | 13.02 | 20.74 | 0.00 | 93.3 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.8 | 4.14 | 11.85 | 19.19 | 2.00 | 83.3 | 90.0 |
| Bench 2 | Bench Boost | Marc Guéhi | DEF | 13 | 5.2 | 3.96 | 11.62 | 19.10 | 3.00 | 77.6 | 90.0 |
| Bench 4 | Bench Boost | Nathan Collins | DEF | 5 | 5.0 | 2.98 | 9.35 | 15.94 | 0.00 | 65.1 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 4.50 | 14.71 | 24.07 | 5.00 | 79.5 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.3 | 4.78 | 13.61 | 21.69 | 8.00 | 64.2 | 74.0 |
| Bench 3 | Bench Boost | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 3.49 | 10.34 | 17.30 | 7.00 | 69.3 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.8 | 5.61 | 16.54 | 27.17 | 2.00 | 96.8 | 90.0 |
| Captain | Captain | Declan Rice | MID | 1 | 7.4 | 5.73 | 16.35 | 26.30 | 5.00 | 87.4 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.27 | 15.63 | 25.08 | 10.00 | 88.3 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.5 | 5.24 | 15.07 | 23.00 | 10.00 | 72.9 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.1 | 4.34 | 12.73 | 20.55 | 2.00 | 83.0 | 90.0 |