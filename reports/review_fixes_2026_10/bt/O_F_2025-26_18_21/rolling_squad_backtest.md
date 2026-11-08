# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW17
- Simulated weeks: GW18-GW21
- Total predicted points: 244.14
- Total actual points: 196.00
- Average predicted points: 61.04
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
- Captain: Phil Foden
- Vice captain: Bukayo Saka
- Effective captain: Phil Foden
- Chip used: none
- Predicted score: 59.88
- Actual score: 38.00
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub outfielders: João Pedro Junqueira de Jesus.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.01 | 11.57 | 18.88 | 2.00 | 88.8 | 90.0 |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 4.9 | 3.44 | 9.98 | 16.62 | 3.00 | 88.1 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.3 | 4.64 | 13.18 | 21.03 | 2.00 | 86.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.61 | 12.85 | 20.54 | 2.00 | 88.5 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.20 | 12.34 | 19.16 | 2.00 | 86.5 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.5 | 4.30 | 11.93 | 19.48 | 0.00 | 88.2 | 90.0 |
| Bench 3 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 4.07 | 11.01 | 17.61 | 0.00 | 83.3 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 4.22 | 12.68 | 20.82 | 5.00 | 78.0 | 90.0 |
| Bench 2 | Autosub In | João Pedro Junqueira de Jesus | FWD | 7 | 7.2 | 4.20 | 12.22 | 20.10 | 8.00 | 76.2 | 68.0 |
| Bench 4 | Bench | Dominic Calvert-Lewin | FWD | 11 | 5.7 | 3.90 | 11.19 | 17.96 | 8.00 | 70.5 | 84.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 9.3 | 5.86 | 18.02 | 30.04 | 0.00 | 83.3 | 0.0 |
| Captain | Captain | Phil Foden | MID | 13 | 8.9 | 5.99 | 17.68 | 28.43 | 2.00 | 86.4 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 10.3 | 5.87 | 16.51 | 26.98 | 7.00 | 82.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.1 | 5.32 | 15.32 | 24.14 | 5.00 | 89.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.1 | 4.87 | 14.26 | 23.10 | 1.00 | 91.6 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 0.10 -> 1.60
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Bukayo Saka
- Effective captain: Phil Foden
- Chip used: none
- Predicted score: 57.44
- Actual score: 35.00
- Transfer: Bruno Borges Fernandes -> Antoine Semenyo (projected gain 4.95, hit 0)
- Autosub outfielders: Igor Thiago Nascimento Rodrigues.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.77 | 10.96 | 18.07 | 2.00 | 85.8 | 90.0 |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 4.9 | 3.44 | 9.97 | 16.47 | 2.00 | 88.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.41 | 12.49 | 20.14 | 6.00 | 86.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.3 | 4.31 | 12.14 | 19.83 | 2.00 | 86.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.11 | 12.12 | 18.94 | 3.00 | 90.2 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.5 | 3.91 | 11.19 | 18.52 | 1.00 | 82.2 | 90.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.7 | 2.59 | 7.02 | 12.11 | 0.00 | 43.5 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.2 | 4.38 | 12.49 | 20.62 | 1.00 | 73.3 | 27.0 |
| Bench 2 | Autosub In | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.82 | 11.54 | 19.67 | 2.00 | 72.8 | 90.0 |
| Bench 3 | Bench | Dominic Calvert-Lewin | FWD | 11 | 5.8 | 3.62 | 11.18 | 18.70 | 1.00 | 65.9 | 20.0 |
| Captain | Captain | Phil Foden | MID | 13 | 9.0 | 5.91 | 18.17 | 29.90 | 3.00 | 90.1 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 10.3 | 5.73 | 16.57 | 27.39 | 6.00 | 81.9 | 82.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.59 | 16.43 | 26.29 | 5.00 | 91.6 | 90.0 |
| XI | Bench | Declan Rice | MID | 1 | 7.2 | 5.01 | 14.56 | 23.11 | 0.00 | 83.0 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 4.41 | 13.98 | 22.79 | 1.00 | 85.2 | 81.0 |

## GW20

- Train rows: 175452
- Bank: 1.60 -> 3.00
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Antoine Semenyo
- Effective captain: Phil Foden
- Chip used: triple_captain
- Predicted score: 60.68
- Actual score: 46.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.90) beats the best remaining Triple Captain opportunity (7.23).
- Transfer: Declan Rice -> Harry Wilson (projected gain 3.34, hit 0)
- Chip used: Triple Captain on Phil Foden. Optimizer chose Triple Captain here because the current estimated captain upside (5.90) beats the best remaining Triple Captain opportunity (7.23).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.55 | 10.76 | 17.91 | 1.00 | 87.8 | 90.0 |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 4.9 | 2.79 | 8.94 | 14.93 | 0.00 | 88.4 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.3 | 4.52 | 13.14 | 21.11 | 2.00 | 93.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.16 | 12.04 | 20.05 | 1.00 | 88.2 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 3.73 | 10.82 | 17.90 | 1.00 | 82.3 | 90.0 |
| Bench 2 | Bench | Trevoh Chalobah | DEF | 7 | 5.6 | 3.32 | 10.14 | 16.87 | 4.00 | 79.4 | 90.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.7 | 1.48 | 4.65 | 8.93 | 1.00 | 29.4 | 24.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 3.86 | 11.45 | 19.26 | 17.00 | 76.8 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.2 | 3.66 | 11.40 | 18.87 | 2.00 | 60.2 | 61.0 |
| Bench 3 | Bench | Dominic Calvert-Lewin | FWD | 11 | 5.8 | 3.25 | 9.68 | 16.70 | 2.00 | 48.3 | 90.0 |
| Captain | Captain | Phil Foden | MID | 13 | 9.0 | 5.90 | 17.95 | 29.79 | 2.00 | 86.9 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.3 | 5.11 | 15.61 | 25.69 | 4.00 | 76.7 | 23.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.14 | 15.58 | 25.33 | 1.00 | 90.7 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 4.80 | 14.19 | 23.43 | 5.00 | 83.9 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.8 | 4.47 | 13.47 | 22.06 | 6.00 | 81.1 | 84.0 |

## GW21

- Train rows: 176242
- Bank: 3.00 -> 3.00
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Antoine Semenyo
- Effective captain: Phil Foden
- Chip used: bench_boost
- Predicted score: 66.14
- Actual score: 77.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.23) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Trevoh Chalobah -> James Tarkowski (projected gain 2.36, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.23) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.64 | 10.72 | 17.65 | 6.00 | 85.0 | 90.0 |
| Bench 1 | Bench Boost | Robert Lynch Sánchez | GK | 7 | 4.9 | 1.81 | 6.23 | 11.16 | 2.00 | 52.1 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.3 | 4.57 | 13.09 | 20.87 | 6.00 | 90.3 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.6 | 4.80 | 13.03 | 20.06 | 4.00 | 90.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.37 | 10.78 | 18.17 | 6.00 | 84.5 | 90.0 |
| Bench 3 | Bench Boost | Marcos Senesi Barón | DEF | 4 | 4.8 | 3.35 | 9.43 | 16.36 | 6.00 | 72.7 | 90.0 |
| Bench 4 | Bench Boost | Daniel Ballard | DEF | 17 | 4.6 | 1.53 | 5.43 | 10.16 | 1.00 | 28.0 | 78.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.9 | 4.99 | 13.89 | 22.75 | 12.00 | 91.7 | 81.0 |
| Bench 2 | Bench Boost | Dominic Calvert-Lewin | FWD | 11 | 5.9 | 3.54 | 11.24 | 18.37 | 8.00 | 66.4 | 86.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.2 | 3.58 | 10.95 | 18.15 | 1.00 | 61.6 | 15.0 |
| Captain | Captain | Phil Foden | MID | 13 | 8.9 | 5.80 | 16.85 | 27.73 | 2.00 | 84.3 | 72.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.19 | 15.08 | 24.54 | 6.00 | 91.8 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.3 | 4.55 | 14.03 | 23.51 | 3.00 | 58.3 | 77.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.8 | 4.69 | 14.01 | 22.82 | 9.00 | 84.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.93 | 13.34 | 21.21 | 3.00 | 76.0 | 90.0 |