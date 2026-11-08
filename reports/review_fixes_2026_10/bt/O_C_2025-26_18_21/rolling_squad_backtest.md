# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW17
- Simulated weeks: GW18-GW21
- Total predicted points: 253.23
- Total actual points: 198.00
- Average predicted points: 63.31
- Average actual points: 49.50
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
- Predicted score: 60.99
- Actual score: 38.00
- Chip advisory: bench_boost (0.67): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub outfielders: Dominic Calvert-Lewin.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.11 | 12.01 | 19.64 | 2.00 | 91.8 | 90.0 |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 4.9 | 3.54 | 10.40 | 17.34 | 3.00 | 91.2 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.3 | 4.81 | 13.57 | 21.64 | 2.00 | 89.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.74 | 13.17 | 21.04 | 2.00 | 90.6 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.54 | 13.15 | 20.38 | 2.00 | 89.9 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.5 | 4.37 | 12.18 | 19.91 | 0.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 4.19 | 11.41 | 18.30 | 0.00 | 85.7 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 4.47 | 13.29 | 21.77 | 5.00 | 81.6 | 90.0 |
| Bench 3 | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.2 | 4.32 | 12.58 | 20.70 | 8.00 | 78.7 | 68.0 |
| Bench 2 | Autosub In | Dominic Calvert-Lewin | FWD | 11 | 5.7 | 4.32 | 12.14 | 19.29 | 8.00 | 73.0 | 84.0 |
| Captain | Bench | Bruno Borges Fernandes | MID | 14 | 9.3 | 6.01 | 18.24 | 30.22 | 0.00 | 82.1 | 0.0 |
| Vice Captain | Captain | Phil Foden | MID | 13 | 8.9 | 5.91 | 17.73 | 28.50 | 2.00 | 83.7 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.3 | 5.50 | 15.81 | 26.01 | 7.00 | 79.4 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.1 | 5.29 | 15.26 | 24.49 | 1.00 | 92.9 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.1 | 5.23 | 15.22 | 24.04 | 5.00 | 89.3 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 0.10 -> 1.60
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Antoine Semenyo
- Effective captain: Phil Foden
- Chip used: none
- Predicted score: 58.89
- Actual score: 35.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Bruno Borges Fernandes -> Antoine Semenyo (projected gain 4.49, hit 0)
- Autosub outfielders: Dominic Calvert-Lewin.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.86 | 11.28 | 18.60 | 2.00 | 87.8 | 90.0 |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 4.9 | 3.56 | 10.38 | 17.14 | 2.00 | 92.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.34 | 12.74 | 19.88 | 3.00 | 93.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.45 | 12.63 | 20.37 | 6.00 | 86.9 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.3 | 4.31 | 12.36 | 20.20 | 2.00 | 86.4 | 90.0 |
| Bench 3 | Bench | Trevoh Chalobah | DEF | 7 | 5.5 | 3.99 | 11.43 | 18.90 | 1.00 | 84.2 | 90.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.7 | 2.29 | 6.61 | 11.62 | 0.00 | 44.5 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.2 | 4.47 | 12.42 | 20.56 | 1.00 | 75.9 | 27.0 |
| Bench 2 | Autosub In | Dominic Calvert-Lewin | FWD | 11 | 5.8 | 4.16 | 12.41 | 20.44 | 1.00 | 69.2 | 20.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.16 | 12.40 | 21.02 | 2.00 | 77.9 | 90.0 |
| Captain | Captain | Phil Foden | MID | 13 | 9.0 | 6.09 | 18.36 | 30.01 | 3.00 | 89.3 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.79 | 16.83 | 26.83 | 5.00 | 92.5 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.3 | 5.54 | 16.29 | 27.00 | 6.00 | 79.9 | 82.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 4.80 | 14.75 | 23.75 | 1.00 | 85.3 | 81.0 |
| XI | Bench | Declan Rice | MID | 1 | 7.2 | 4.97 | 14.51 | 23.03 | 0.00 | 82.2 | 0.0 |

## GW20

- Train rows: 175452
- Bank: 1.60 -> 3.00
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Antoine Semenyo
- Effective captain: Phil Foden
- Chip used: triple_captain
- Predicted score: 62.70
- Actual score: 46.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.00) beats the best remaining Triple Captain opportunity (7.37).
- Transfer: Declan Rice -> Harry Wilson (projected gain 3.94, hit 0)
- Chip used: Triple Captain on Phil Foden. Optimizer chose Triple Captain here because the current estimated captain upside (6.00) beats the best remaining Triple Captain opportunity (7.37).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.66 | 11.11 | 18.49 | 1.00 | 90.2 | 90.0 |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 4.9 | 2.80 | 9.25 | 15.52 | 0.00 | 90.2 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.3 | 4.80 | 13.82 | 22.16 | 2.00 | 96.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.34 | 12.48 | 20.70 | 1.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 3.94 | 11.37 | 18.73 | 1.00 | 84.5 | 90.0 |
| Bench 3 | Bench | Trevoh Chalobah | DEF | 7 | 5.6 | 3.35 | 10.29 | 17.19 | 4.00 | 79.9 | 90.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.7 | 1.74 | 5.28 | 9.91 | 1.00 | 33.0 | 24.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 4.05 | 11.89 | 19.96 | 17.00 | 79.9 | 90.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 11 | 5.8 | 3.65 | 10.78 | 18.37 | 2.00 | 52.5 | 90.0 |
| Bench 2 | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.2 | 3.36 | 10.37 | 17.45 | 2.00 | 59.7 | 61.0 |
| Captain | Captain | Phil Foden | MID | 13 | 9.0 | 6.00 | 17.89 | 29.62 | 2.00 | 87.5 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.55 | 16.55 | 26.73 | 1.00 | 93.5 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.3 | 4.98 | 15.23 | 25.10 | 4.00 | 74.8 | 23.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.8 | 4.86 | 14.30 | 23.26 | 6.00 | 85.5 | 84.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 4.87 | 14.24 | 23.49 | 5.00 | 84.4 | 90.0 |

## GW21

- Train rows: 176242
- Bank: 3.00 -> 2.00
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Phil Foden
- Chip used: bench_boost
- Predicted score: 70.65
- Actual score: 79.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (12.79) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Daniel Ballard -> James Tarkowski (projected gain 3.63, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (12.79) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.80 | 11.12 | 18.29 | 6.00 | 87.7 | 90.0 |
| Bench 1 | Bench Boost | Robert Lynch Sánchez | GK | 7 | 4.9 | 1.94 | 6.58 | 11.72 | 2.00 | 54.5 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.6 | 5.03 | 13.47 | 20.69 | 4.00 | 91.4 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.3 | 4.65 | 13.13 | 20.96 | 6.00 | 91.9 | 90.0 |
| Bench 4 | Bench Boost | Virgil van Dijk | DEF | 12 | 5.9 | 3.56 | 11.20 | 18.79 | 6.00 | 86.8 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.6 | 3.68 | 10.86 | 18.18 | 3.00 | 81.1 | 90.0 |
| Bench 3 | Bench Boost | Marcos Senesi Barón | DEF | 4 | 4.8 | 3.59 | 9.92 | 17.11 | 6.00 | 75.8 | 90.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.9 | 5.55 | 15.21 | 24.67 | 12.00 | 96.4 | 81.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 11 | 5.9 | 3.89 | 11.91 | 19.31 | 8.00 | 69.9 | 86.0 |
| Bench 2 | Bench Boost | João Pedro Junqueira de Jesus | FWD | 7 | 7.2 | 3.70 | 11.18 | 18.47 | 1.00 | 62.6 | 15.0 |
| Captain | Captain | Phil Foden | MID | 13 | 8.9 | 5.77 | 16.82 | 27.79 | 2.00 | 85.1 | 72.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.51 | 15.88 | 25.70 | 6.00 | 94.0 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.8 | 5.10 | 14.89 | 24.15 | 9.00 | 89.3 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.3 | 4.60 | 13.92 | 23.18 | 3.00 | 56.3 | 77.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.53 | 13.81 | 22.43 | 3.00 | 75.7 | 90.0 |