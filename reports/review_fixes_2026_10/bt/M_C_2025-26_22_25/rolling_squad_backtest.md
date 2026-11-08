# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW21
- Simulated weeks: GW22-GW25
- Total predicted points: 259.02
- Total actual points: 224.00
- Average predicted points: 64.75
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
- Predicted score: 59.59
- Actual score: 41.00
- Chip advisory: bench_boost (0.67): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Virgil van Dijk replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.80 | 11.38 | 18.78 | 6.00 | 87.9 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.5 | 3.68 | 11.05 | 18.14 | 1.00 | 93.3 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 13 | 5.3 | 4.81 | 13.91 | 22.51 | 0.00 | 95.8 | 0.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.44 | 13.06 | 20.58 | 8.00 | 88.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.6 | 4.45 | 12.91 | 19.33 | 8.00 | 73.0 | 90.0 |
| Bench 3 | Bench | Nathan Collins | DEF | 5 | 4.9 | 4.27 | 12.39 | 21.00 | 1.00 | 88.2 | 90.0 |
| Bench 2 | Autosub In | Virgil van Dijk | DEF | 12 | 5.9 | 4.36 | 12.00 | 19.64 | 2.00 | 86.8 | 90.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.73 | 15.90 | 25.41 | 2.00 | 89.4 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.7 | 4.89 | 13.95 | 21.62 | 2.00 | 75.6 | 90.0 |
| Bench 4 | Bench | Dominic Calvert-Lewin | FWD | 11 | 5.9 | 4.25 | 12.90 | 20.61 | 2.00 | 76.8 | 90.0 |
| Captain | Captain | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.1 | 5.75 | 16.25 | 26.14 | 3.00 | 96.3 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.21 | 15.89 | 25.99 | 2.00 | 92.2 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.8 | 4.87 | 15.02 | 25.32 | 1.00 | 77.1 | 45.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 4.97 | 14.41 | 24.29 | 2.00 | 82.2 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.8 | 4.92 | 14.15 | 23.37 | 2.00 | 90.2 | 87.0 |

## GW23

- Train rows: 177836
- Bank: 2.60 -> 4.00
- Free transfers: 2 -> 2
- Captain: Igor Thiago Nascimento Rodrigues
- Vice captain: Declan Rice
- Effective captain: Igor Thiago Nascimento Rodrigues
- Chip used: none
- Predicted score: 60.75
- Actual score: 48.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Phil Foden -> Declan Rice (projected gain 4.19, hit 0)
- Autosub: Dominic Calvert-Lewin replaced Bruno Guimarães Rodriguez Moura.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.12 | 12.12 | 19.81 | 1.00 | 88.7 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.5 | 3.34 | 9.88 | 16.45 | 1.00 | 85.4 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.7 | 5.02 | 14.41 | 21.86 | 1.00 | 81.8 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.62 | 12.73 | 21.00 | 4.00 | 84.1 | 90.0 |
| XI | XI | Nathan Collins | DEF | 5 | 4.9 | 3.98 | 11.44 | 19.02 | 1.00 | 86.7 | 90.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 12 | 5.9 | 3.73 | 11.42 | 18.81 | 9.00 | 86.2 | 90.0 |
| Bench 4 | Bench | Marc Guéhi | DEF | 13 | 5.3 | 3.30 | 9.21 | 15.89 | 6.00 | 53.0 | 90.0 |
| Captain | Captain | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.96 | 16.59 | 26.72 | 2.00 | 92.8 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.7 | 4.26 | 12.88 | 20.65 | 8.00 | 70.6 | 90.0 |
| Bench 2 | Autosub In | Dominic Calvert-Lewin | FWD | 11 | 5.9 | 4.16 | 12.10 | 19.25 | 2.00 | 79.2 | 90.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.3 | 5.63 | 16.27 | 25.54 | 1.00 | 93.4 | 90.0 |
| XI | Bench | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.1 | 5.55 | 16.22 | 26.17 | 0.00 | 90.6 | 0.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.58 | 15.83 | 25.68 | 8.00 | 86.8 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 5.27 | 14.97 | 24.32 | 8.00 | 84.9 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.8 | 4.82 | 13.68 | 22.74 | 10.00 | 81.7 | 90.0 |

## GW24

- Train rows: 178639
- Bank: 4.00 -> 1.90
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Morgan Rogers
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 65.31
- Actual score: 62.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.75) beats the best remaining Triple Captain opportunity (7.26).
- Chip advisory: bench_boost (0.62): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Bruno Guimarães Rodriguez Moura -> Bruno Borges Fernandes (projected gain 2.19, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (5.75) beats the best remaining Triple Captain opportunity (7.26).
- Autosub: Dominic Calvert-Lewin replaced Ollie Watkins.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.89 | 11.46 | 18.84 | 6.00 | 86.4 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.5 | 3.06 | 9.60 | 16.15 | 10.00 | 85.2 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.7 | 4.69 | 13.85 | 22.37 | 8.00 | 81.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.68 | 13.43 | 21.72 | 4.00 | 95.5 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.00 | 11.79 | 19.38 | 2.00 | 81.4 | 90.0 |
| Bench 3 | Bench | Marc Guéhi | DEF | 13 | 5.2 | 3.93 | 11.72 | 19.56 | 3.00 | 76.7 | 90.0 |
| Bench 4 | Bench | Nathan Collins | DEF | 5 | 4.9 | 3.33 | 10.44 | 17.57 | 1.00 | 84.8 | 30.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.29 | 16.07 | 25.76 | 2.00 | 90.2 | 90.0 |
| XI | Bench | Ollie Watkins | FWD | 2 | 8.7 | 4.57 | 13.41 | 22.27 | 0.00 | 74.7 | 0.0 |
| Bench 2 | Autosub In | Dominic Calvert-Lewin | FWD | 11 | 5.9 | 4.15 | 11.98 | 19.52 | 2.00 | 81.3 | 84.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 7.6 | 5.75 | 16.72 | 27.24 | 7.00 | 96.8 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.49 | 16.20 | 25.79 | 3.00 | 92.1 | 90.0 |
| Vice Captain | XI | Morgan Rogers | MID | 2 | 7.6 | 5.67 | 16.12 | 26.00 | 2.00 | 93.1 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.82 | 14.30 | 23.47 | 2.00 | 91.8 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.3 | 4.95 | 14.10 | 21.84 | 10.00 | 71.2 | 90.0 |

## GW25

- Train rows: 179450
- Bank: 1.90 -> 3.30
- Free transfers: 2 -> 2
- Captain: Declan Rice
- Vice captain: Antoine Semenyo
- Effective captain: Declan Rice
- Chip used: bench_boost
- Predicted score: 73.37
- Actual score: 73.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.84) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Ollie Watkins -> João Pedro Junqueira de Jesus (projected gain 1.96, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.84) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.34 | 12.24 | 19.86 | 7.00 | 87.8 | 90.0 |
| Bench 1 | Bench Boost | Caoimhín Kelleher | GK | 5 | 4.5 | 3.46 | 10.48 | 17.28 | 1.00 | 89.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 5.55 | 15.55 | 25.01 | 6.00 | 88.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.42 | 12.91 | 20.58 | 0.00 | 93.3 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.15 | 12.07 | 19.89 | 2.00 | 83.3 | 90.0 |
| Bench 2 | Bench Boost | Marc Guéhi | DEF | 13 | 5.2 | 3.96 | 11.71 | 19.45 | 3.00 | 77.6 | 90.0 |
| Bench 4 | Bench Boost | Nathan Collins | DEF | 5 | 4.9 | 2.96 | 9.55 | 16.49 | 0.00 | 65.1 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.48 | 14.74 | 24.16 | 5.00 | 79.6 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.3 | 4.75 | 13.56 | 21.64 | 8.00 | 64.3 | 74.0 |
| Bench 3 | Bench Boost | Dominic Calvert-Lewin | FWD | 11 | 5.9 | 3.46 | 10.34 | 17.34 | 7.00 | 69.4 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.60 | 16.59 | 27.33 | 2.00 | 96.8 | 90.0 |
| Captain | Captain | Declan Rice | MID | 1 | 7.3 | 5.70 | 16.52 | 26.85 | 5.00 | 87.4 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 5.29 | 15.60 | 25.12 | 10.00 | 88.2 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.4 | 5.22 | 14.96 | 22.84 | 10.00 | 73.0 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.34 | 12.77 | 20.64 | 2.00 | 83.0 | 90.0 |