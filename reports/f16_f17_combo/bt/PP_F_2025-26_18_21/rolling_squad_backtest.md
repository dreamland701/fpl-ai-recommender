# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW17
- Simulated weeks: GW18-GW21
- Total predicted points: 259.68
- Total actual points: 186.00
- Average predicted points: 64.92
- Average actual points: 46.50
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
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Erling Haaland
- Vice captain: Hugo Ekitiké
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 67.89
- Actual score: 37.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 3.05 | 8.96 | 15.03 | 3.00 | 86.0 | 90.0 |
| Bench 1 | Bench | Callan McKenna | GK | 4 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.1 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.07 | 13.92 | 21.94 | 2.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.20 | 12.09 | 19.42 | 2.00 | 84.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 3.91 | 11.14 | 17.53 | 2.00 | 79.1 | 90.0 |
| Bench 2 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.50 | 7.47 | 11.89 | 2.00 | 65.9 | 90.0 |
| Bench 3 | Bench | Ayden Heaven | DEF | 14 | 3.8 | 2.16 | 5.63 | 8.21 | 8.00 | 57.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.36 | 24.50 | 40.53 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 6.84 | 18.39 | 27.49 | 5.00 | 85.9 | 85.0 |
| Bench 4 | Bench | Chido Obi | FWD | 14 | 4.2 | 0.21 | 0.59 | 0.91 | 0.00 | 1.1 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.64 | 17.70 | 28.39 | 2.00 | 80.3 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 5.72 | 16.57 | 26.03 | 1.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 5.78 | 16.48 | 25.91 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.37 | 15.89 | 25.23 | 9.00 | 87.4 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.0 | 5.57 | 15.46 | 23.94 | 2.00 | 90.0 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Matheus Santos Carneiro da Cunha
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 61.61
- Actual score: 37.00
- Transfer: Marcos Senesi Barón -> Michael Keane (projected gain 0.17, hit 0)
- Autosub: Ayden Heaven replaced Michael Keane.
- Autosub: Gabriel Gudmundsson replaced Declan Rice.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 3.54 | 9.92 | 16.09 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Callan McKenna | GK | 4 | 3.9 | 0.00 | 0.02 | 0.00 | 0.00 | 1.3 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.56 | 12.70 | 20.42 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.19 | 12.20 | 20.18 | 6.00 | 86.3 | 90.0 |
| XI | Bench | Michael Keane | DEF | 9 | 4.8 | 3.91 | 11.13 | 17.27 | 0.00 | 87.1 | 0.0 |
| Bench 3 | Autosub In | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.37 | 7.42 | 12.03 | 8.00 | 67.2 | 90.0 |
| Bench 2 | Autosub In | Ayden Heaven | DEF | 14 | 3.8 | 2.99 | 7.19 | 10.74 | 2.00 | 65.7 | 74.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 7.97 | 23.53 | 39.25 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.38 | 13.39 | 20.79 | 2.00 | 53.2 | 90.0 |
| Bench 4 | Bench | Chido Obi | FWD | 14 | 4.2 | 0.49 | 0.81 | 1.20 | 0.00 | 1.7 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.33 | 16.50 | 27.54 | 3.00 | 80.6 | 90.0 |
| Vice Captain | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.0 | 6.15 | 16.39 | 24.93 | 2.00 | 88.8 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.20 | 15.46 | 24.99 | 5.00 | 89.1 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.97 | 13.47 | 21.92 | 1.00 | 78.9 | 81.0 |
| XI | Bench | Declan Rice | MID | 1 | 7.2 | 4.45 | 13.37 | 21.75 | 0.00 | 75.5 | 0.0 |

## GW20

- Train rows: 175452
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Morgan Rogers
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 62.40
- Actual score: 47.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (4.49) beats the best remaining Bench Boost opportunity (5.99).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (4.49) beats the best remaining Bench Boost opportunity (5.99).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 2.50 | 8.68 | 14.61 | 0.00 | 90.0 | 0.0 |
| Bench 1 | Bench Boost | Callan McKenna | GK | 4 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 2.7 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.44 | 12.55 | 20.18 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.07 | 11.97 | 19.93 | 1.00 | 89.5 | 90.0 |
| XI | XI | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.76 | 7.72 | 11.92 | 2.00 | 75.2 | 90.0 |
| Bench 2 | Bench Boost | Ayden Heaven | DEF | 14 | 3.8 | 2.35 | 6.53 | 10.62 | 4.00 | 60.2 | 90.0 |
| Bench 3 | Bench Boost | Michael Keane | DEF | 9 | 4.8 | 1.94 | 6.04 | 10.45 | 0.00 | 40.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.15 | 23.95 | 39.63 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.47 | 13.94 | 22.93 | 0.00 | 64.2 | 0.0 |
| Bench 4 | Bench Boost | Chido Obi | FWD | 14 | 4.2 | 0.21 | 0.62 | 1.09 | 0.00 | 4.5 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 8.9 | 5.77 | 17.43 | 28.54 | 2.00 | 83.1 | 90.0 |
| Vice Captain | XI | Morgan Rogers | MID | 2 | 7.4 | 5.83 | 16.80 | 26.59 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.34 | 15.66 | 25.17 | 1.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.1 | 3.60 | 11.52 | 19.00 | 9.00 | 61.3 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.1 | 2.83 | 9.22 | 16.50 | 17.00 | 40.6 | 90.0 |

## GW21

- Train rows: 176242
- Bank: 0.10 -> 2.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 67.78
- Actual score: 65.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.00) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Hugo Ekitiké -> Igor Thiago Nascimento Rodrigues (projected gain 7.41, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.00) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 1.72 | 5.94 | 10.60 | 2.00 | 55.2 | 90.0 |
| Bench 1 | Bench | Callan McKenna | GK | 4 | 3.9 | 0.10 | 0.06 | 0.06 | 0.00 | 1.7 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.48 | 12.38 | 19.97 | 6.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.39 | 10.74 | 18.09 | 6.00 | 87.5 | 90.0 |
| XI | XI | Michael Keane | DEF | 9 | 4.8 | 3.25 | 8.49 | 13.68 | 5.00 | 68.0 | 82.0 |
| Bench 2 | Bench | Ayden Heaven | DEF | 14 | 3.8 | 3.06 | 8.01 | 12.76 | 0.00 | 67.3 | 60.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.45 | 7.21 | 11.49 | 0.00 | 71.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.00 | 23.62 | 38.57 | 6.00 | 90.0 | 90.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.57 | 15.32 | 24.29 | 12.00 | 90.0 | 81.0 |
| Bench 4 | Bench | Chido Obi | FWD | 14 | 4.2 | 0.33 | 0.75 | 1.28 | 0.00 | 4.3 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 8.8 | 5.44 | 15.75 | 26.30 | 2.00 | 78.9 | 72.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 5.12 | 14.82 | 24.59 | 3.00 | 89.1 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 5.22 | 14.76 | 24.16 | 6.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 4.82 | 14.11 | 22.82 | 3.00 | 79.8 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.1 | 4.77 | 13.61 | 22.40 | 2.00 | 80.9 | 73.0 |