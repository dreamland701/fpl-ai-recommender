# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW17
- Simulated weeks: GW18-GW21
- Total predicted points: 251.54
- Total actual points: 196.00
- Average predicted points: 62.89
- Average actual points: 49.00
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW17 are included before the first simulated week.
- League-average scores were not available for this run.

## GW18

- Train rows: 173897
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Phil Foden
- Effective captain: Phil Foden
- Chip used: none
- Predicted score: 61.02
- Actual score: 38.00
- Chip advisory: bench_boost (0.67): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: João Pedro Junqueira de Jesus replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.12 | 11.97 | 19.60 | 2.00 | 91.7 | 90.0 |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 4.9 | 3.58 | 10.40 | 17.35 | 3.00 | 91.1 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.3 | 4.78 | 13.74 | 21.96 | 2.00 | 89.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.71 | 13.28 | 21.40 | 2.00 | 90.7 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.56 | 13.25 | 21.01 | 2.00 | 89.9 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.5 | 4.40 | 12.34 | 20.31 | 0.00 | 89.9 | 90.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 4.19 | 11.67 | 18.89 | 0.00 | 85.7 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 4.49 | 13.35 | 21.95 | 5.00 | 81.6 | 90.0 |
| Bench 2 | Autosub In | João Pedro Junqueira de Jesus | FWD | 7 | 7.2 | 4.35 | 12.61 | 20.83 | 8.00 | 78.6 | 68.0 |
| Bench 3 | Bench | Dominic Calvert-Lewin | FWD | 11 | 5.7 | 4.30 | 12.19 | 19.41 | 8.00 | 73.1 | 84.0 |
| Captain | Bench | Bruno Borges Fernandes | MID | 14 | 9.3 | 5.99 | 18.56 | 30.74 | 0.00 | 82.1 | 0.0 |
| Vice Captain | Captain | Phil Foden | MID | 13 | 8.9 | 5.89 | 17.99 | 28.98 | 2.00 | 83.7 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.3 | 5.52 | 15.89 | 26.32 | 7.00 | 79.3 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.1 | 5.30 | 15.41 | 24.81 | 1.00 | 92.9 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.1 | 5.25 | 15.34 | 24.63 | 5.00 | 89.3 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 0.10 -> 1.60
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Antoine Semenyo
- Effective captain: Phil Foden
- Chip used: none
- Predicted score: 59.02
- Actual score: 35.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Bruno Borges Fernandes -> Antoine Semenyo (projected gain 4.69, hit 0)
- Autosub: Igor Thiago Nascimento Rodrigues replaced Declan Rice.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.89 | 11.28 | 18.61 | 2.00 | 87.8 | 90.0 |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 4.9 | 3.58 | 10.38 | 17.15 | 2.00 | 91.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.45 | 12.90 | 21.12 | 6.00 | 86.9 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.36 | 12.58 | 19.99 | 3.00 | 93.1 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.3 | 4.31 | 12.50 | 20.62 | 2.00 | 86.4 | 90.0 |
| Bench 3 | Bench | Trevoh Chalobah | DEF | 7 | 5.5 | 4.02 | 11.70 | 19.39 | 1.00 | 84.1 | 90.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 2.28 | 6.87 | 12.13 | 0.00 | 44.5 | 0.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 11 | 5.7 | 4.16 | 12.58 | 20.63 | 1.00 | 69.2 | 20.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.2 | 4.50 | 12.57 | 20.84 | 1.00 | 75.8 | 27.0 |
| Bench 2 | Autosub In | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.13 | 12.40 | 21.16 | 2.00 | 77.9 | 90.0 |
| Captain | Captain | Phil Foden | MID | 13 | 8.9 | 6.07 | 18.50 | 30.45 | 3.00 | 89.4 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.81 | 17.01 | 27.37 | 5.00 | 92.5 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.3 | 5.57 | 16.38 | 27.30 | 6.00 | 79.8 | 82.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.2 | 4.84 | 15.09 | 24.25 | 1.00 | 85.3 | 81.0 |
| XI | Bench | Declan Rice | MID | 1 | 7.1 | 5.00 | 14.76 | 23.68 | 0.00 | 82.1 | 0.0 |

## GW20

- Train rows: 175452
- Bank: 1.60 -> 2.90
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Antoine Semenyo
- Effective captain: Phil Foden
- Chip used: triple_captain
- Predicted score: 62.82
- Actual score: 46.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.02) beats the best remaining Triple Captain opportunity (7.39).
- Transfer: Declan Rice -> Harry Wilson (projected gain 3.84, hit 0)
- Chip used: Triple Captain on Phil Foden. Optimizer chose Triple Captain here because the current estimated captain upside (6.02) beats the best remaining Triple Captain opportunity (7.39).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.68 | 11.16 | 18.50 | 1.00 | 90.1 | 90.0 |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 4.9 | 2.78 | 9.23 | 15.43 | 0.00 | 90.3 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.3 | 4.78 | 13.73 | 22.23 | 2.00 | 96.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.34 | 12.73 | 21.28 | 1.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 3.98 | 11.65 | 19.61 | 1.00 | 84.4 | 90.0 |
| Bench 3 | Bench | Trevoh Chalobah | DEF | 7 | 5.5 | 3.33 | 10.59 | 17.81 | 4.00 | 80.0 | 90.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 1.72 | 5.55 | 10.51 | 1.00 | 33.1 | 24.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 4.05 | 12.02 | 20.26 | 17.00 | 79.9 | 90.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 11 | 5.7 | 3.63 | 10.95 | 18.65 | 2.00 | 52.5 | 90.0 |
| Bench 2 | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.2 | 3.35 | 10.45 | 17.60 | 2.00 | 59.8 | 61.0 |
| Captain | Captain | Phil Foden | MID | 13 | 8.9 | 6.02 | 18.08 | 30.02 | 2.00 | 87.5 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.58 | 16.56 | 26.93 | 1.00 | 93.4 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.3 | 5.01 | 15.22 | 25.25 | 4.00 | 74.7 | 23.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.2 | 4.84 | 14.33 | 23.81 | 5.00 | 84.4 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.8 | 4.85 | 14.27 | 23.45 | 6.00 | 85.5 | 84.0 |

## GW21

- Train rows: 176242
- Bank: 2.90 -> 2.80
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Phil Foden
- Chip used: bench_boost
- Predicted score: 68.68
- Actual score: 77.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.93) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Trevoh Chalobah -> James Tarkowski (projected gain 2.21, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.93) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.79 | 11.14 | 18.23 | 6.00 | 87.7 | 90.0 |
| Bench 1 | Bench Boost | Robert Lynch Sánchez | GK | 7 | 4.9 | 1.94 | 6.61 | 11.75 | 2.00 | 54.5 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.6 | 4.99 | 13.21 | 20.54 | 4.00 | 91.4 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.3 | 4.68 | 13.18 | 21.16 | 6.00 | 91.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.59 | 11.32 | 19.11 | 6.00 | 86.8 | 90.0 |
| Bench 3 | Bench Boost | Marcos Senesi Barón | DEF | 4 | 4.8 | 3.57 | 10.11 | 18.02 | 6.00 | 75.9 | 90.0 |
| Bench 4 | Bench Boost | Daniel Ballard | DEF | 17 | 4.6 | 1.73 | 6.22 | 11.58 | 1.00 | 31.5 | 78.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.9 | 5.52 | 15.22 | 24.87 | 12.00 | 96.4 | 81.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 11 | 5.8 | 3.87 | 11.95 | 19.32 | 8.00 | 70.0 | 86.0 |
| Bench 2 | Bench Boost | João Pedro Junqueira de Jesus | FWD | 7 | 7.2 | 3.70 | 11.21 | 18.52 | 1.00 | 62.6 | 15.0 |
| Captain | Captain | Phil Foden | MID | 13 | 8.9 | 5.79 | 16.98 | 28.26 | 2.00 | 85.0 | 72.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.48 | 15.90 | 25.88 | 6.00 | 94.1 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.8 | 5.11 | 14.90 | 24.26 | 9.00 | 89.3 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.3 | 4.60 | 13.98 | 23.39 | 3.00 | 56.3 | 77.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 4.54 | 13.94 | 22.74 | 3.00 | 75.7 | 90.0 |