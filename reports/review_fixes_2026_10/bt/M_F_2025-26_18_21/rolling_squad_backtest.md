# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW17
- Simulated weeks: GW18-GW21
- Total predicted points: 245.36
- Total actual points: 202.00
- Average predicted points: 61.34
- Average actual points: 50.50
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
- Predicted score: 59.91
- Actual score: 38.00
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Marcos Senesi Barón replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.03 | 11.51 | 18.76 | 2.00 | 88.8 | 90.0 |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 4.9 | 3.47 | 9.95 | 16.55 | 3.00 | 88.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.3 | 4.61 | 13.35 | 21.34 | 2.00 | 87.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.58 | 12.96 | 20.91 | 2.00 | 88.5 | 90.0 |
| Bench 2 | Autosub In | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.22 | 12.45 | 19.76 | 2.00 | 86.4 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.5 | 4.33 | 12.09 | 19.89 | 0.00 | 88.1 | 90.0 |
| Bench 3 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 4.07 | 11.27 | 18.18 | 0.00 | 83.3 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 4.25 | 12.74 | 20.94 | 5.00 | 78.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.2 | 4.23 | 12.24 | 20.20 | 8.00 | 76.1 | 68.0 |
| Bench 4 | Bench | Dominic Calvert-Lewin | FWD | 11 | 5.7 | 3.87 | 11.24 | 17.99 | 8.00 | 70.5 | 84.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 9.3 | 5.84 | 18.38 | 30.57 | 0.00 | 83.3 | 0.0 |
| Captain | Captain | Phil Foden | MID | 13 | 8.9 | 5.97 | 17.94 | 28.90 | 2.00 | 86.4 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 10.3 | 5.89 | 16.58 | 27.32 | 7.00 | 82.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.1 | 5.34 | 15.46 | 24.80 | 5.00 | 88.9 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.1 | 4.88 | 14.42 | 23.37 | 1.00 | 91.6 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 0.10 -> 1.60
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Bukayo Saka
- Effective captain: Phil Foden
- Chip used: none
- Predicted score: 57.60
- Actual score: 35.00
- Transfer: Bruno Borges Fernandes -> Antoine Semenyo (projected gain 5.16, hit 0)
- Autosub: Igor Thiago Nascimento Rodrigues replaced Declan Rice.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.80 | 10.94 | 18.01 | 2.00 | 85.8 | 90.0 |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 4.9 | 3.47 | 9.94 | 16.39 | 2.00 | 88.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.41 | 12.75 | 20.88 | 6.00 | 86.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.3 | 4.31 | 12.29 | 20.27 | 2.00 | 86.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.12 | 11.98 | 19.05 | 3.00 | 90.2 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.5 | 3.94 | 11.45 | 18.98 | 1.00 | 82.2 | 90.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 2.57 | 7.27 | 12.67 | 0.00 | 43.5 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.2 | 4.40 | 12.64 | 20.88 | 1.00 | 73.3 | 27.0 |
| Bench 2 | Autosub In | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.79 | 11.52 | 19.74 | 2.00 | 72.8 | 90.0 |
| Bench 3 | Bench | Dominic Calvert-Lewin | FWD | 11 | 5.7 | 3.61 | 11.33 | 18.77 | 1.00 | 65.9 | 20.0 |
| Captain | Captain | Phil Foden | MID | 13 | 8.9 | 5.88 | 18.30 | 30.28 | 3.00 | 90.1 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 10.3 | 5.77 | 16.67 | 27.71 | 6.00 | 81.9 | 82.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.61 | 16.61 | 26.83 | 5.00 | 91.5 | 90.0 |
| XI | Bench | Declan Rice | MID | 1 | 7.1 | 5.05 | 14.84 | 23.83 | 0.00 | 82.9 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.2 | 4.44 | 14.32 | 23.22 | 1.00 | 85.1 | 81.0 |

## GW20

- Train rows: 175452
- Bank: 1.60 -> 1.70
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Antoine Semenyo
- Effective captain: Phil Foden
- Chip used: triple_captain
- Predicted score: 61.29
- Actual score: 50.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.91) beats the best remaining Triple Captain opportunity (7.25).
- Transfer: Declan Rice -> Bruno Guimarães Rodriguez Moura (projected gain 3.10, hit 0)
- Chip used: Triple Captain on Phil Foden. Optimizer chose Triple Captain here because the current estimated captain upside (5.91) beats the best remaining Triple Captain opportunity (7.25).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.57 | 10.79 | 17.84 | 1.00 | 87.8 | 90.0 |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 4.9 | 2.78 | 8.91 | 14.79 | 0.00 | 88.4 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.3 | 4.50 | 13.05 | 21.16 | 2.00 | 93.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.16 | 12.28 | 20.62 | 1.00 | 88.2 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 3.77 | 11.07 | 18.77 | 1.00 | 82.2 | 90.0 |
| Bench 2 | Bench | Trevoh Chalobah | DEF | 7 | 5.5 | 3.31 | 10.43 | 17.47 | 4.00 | 79.4 | 90.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 1.45 | 4.89 | 9.45 | 1.00 | 29.4 | 24.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 3.86 | 11.55 | 19.50 | 17.00 | 76.8 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.2 | 3.65 | 11.48 | 19.01 | 2.00 | 60.2 | 61.0 |
| Bench 3 | Bench | Dominic Calvert-Lewin | FWD | 11 | 5.7 | 3.24 | 9.83 | 16.94 | 2.00 | 48.3 | 90.0 |
| Captain | Captain | Phil Foden | MID | 13 | 8.9 | 5.91 | 18.11 | 30.12 | 2.00 | 86.8 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.3 | 5.14 | 15.60 | 25.85 | 4.00 | 76.7 | 23.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.17 | 15.59 | 25.55 | 1.00 | 90.6 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.2 | 4.78 | 14.27 | 23.74 | 5.00 | 84.0 | 90.0 |
| XI | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.0 | 4.96 | 13.51 | 21.96 | 10.00 | 84.1 | 90.0 |

## GW21

- Train rows: 176242
- Bank: 1.70 -> 1.60
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Antoine Semenyo
- Effective captain: Phil Foden
- Chip used: bench_boost
- Predicted score: 66.55
- Actual score: 79.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.20) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Trevoh Chalobah -> James Tarkowski (projected gain 1.94, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.20) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.63 | 10.71 | 17.50 | 6.00 | 85.0 | 90.0 |
| Bench 1 | Bench Boost | Robert Lynch Sánchez | GK | 7 | 4.9 | 1.81 | 6.23 | 11.10 | 2.00 | 52.1 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.3 | 4.61 | 13.13 | 21.06 | 6.00 | 90.3 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.6 | 4.77 | 12.74 | 19.88 | 4.00 | 90.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.40 | 10.90 | 18.47 | 6.00 | 84.5 | 90.0 |
| Bench 3 | Bench Boost | Marcos Senesi Barón | DEF | 4 | 4.8 | 3.33 | 9.60 | 17.20 | 6.00 | 72.8 | 90.0 |
| Bench 4 | Bench Boost | Daniel Ballard | DEF | 17 | 4.6 | 1.55 | 5.76 | 10.79 | 1.00 | 28.0 | 78.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.9 | 4.97 | 13.88 | 22.89 | 12.00 | 91.7 | 81.0 |
| Bench 2 | Bench Boost | Dominic Calvert-Lewin | FWD | 11 | 5.8 | 3.52 | 11.27 | 18.31 | 8.00 | 66.5 | 86.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.2 | 3.58 | 10.97 | 18.17 | 1.00 | 61.6 | 15.0 |
| Captain | Captain | Phil Foden | MID | 13 | 8.9 | 5.82 | 17.01 | 28.21 | 2.00 | 84.3 | 72.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.16 | 15.10 | 24.73 | 6.00 | 91.8 | 90.0 |
| XI | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.0 | 5.09 | 14.35 | 23.52 | 11.00 | 87.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.3 | 4.54 | 14.09 | 23.69 | 3.00 | 58.3 | 77.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 4.95 | 13.44 | 21.60 | 3.00 | 76.0 | 90.0 |