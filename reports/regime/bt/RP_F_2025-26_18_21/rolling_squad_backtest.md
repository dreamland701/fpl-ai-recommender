# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW17
- Simulated weeks: GW18-GW21
- Total predicted points: 260.18
- Total actual points: 180.00
- Average predicted points: 65.04
- Average actual points: 45.00
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
- Predicted score: 67.99
- Actual score: 40.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Gabriel Gudmundsson replaced Daniel Ballard.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.5 | 3.45 | 9.67 | 15.74 | 6.00 | 81.5 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.9 | 0.19 | 0.50 | 0.85 | 0.00 | 1.2 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.99 | 13.60 | 21.35 | 2.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 3.95 | 11.36 | 17.97 | 2.00 | 81.7 | 90.0 |
| XI | Bench | Daniel Ballard | DEF | 17 | 4.7 | 4.01 | 11.06 | 17.73 | 0.00 | 82.3 | 0.0 |
| Bench 2 | Autosub In | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.59 | 7.76 | 12.40 | 2.00 | 69.4 | 90.0 |
| Bench 3 | Bench | Ayden Heaven | DEF | 14 | 3.8 | 2.20 | 5.83 | 8.61 | 8.00 | 60.6 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.40 | 24.70 | 40.90 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 6.92 | 18.62 | 27.88 | 5.00 | 86.8 | 85.0 |
| Bench 4 | Bench | Chido Obi | FWD | 14 | 4.2 | 0.12 | 0.27 | 0.31 | 0.00 | 1.9 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.66 | 17.84 | 28.70 | 2.00 | 82.3 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 5.74 | 16.31 | 25.60 | 5.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 5.64 | 16.25 | 25.46 | 1.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.0 | 5.58 | 15.48 | 23.94 | 2.00 | 88.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.26 | 15.42 | 24.34 | 9.00 | 82.1 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Matheus Santos Carneiro da Cunha
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 59.52
- Actual score: 46.00
- Transfer: none
- No transfer was applied this week.
- Autosub: Gabriel Gudmundsson replaced Declan Rice.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.5 | 3.10 | 9.38 | 15.44 | 10.00 | 81.1 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.9 | 0.19 | 0.57 | 0.91 | 0.00 | 1.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.11 | 11.87 | 19.57 | 6.00 | 83.6 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 3.88 | 11.14 | 17.44 | 3.00 | 87.4 | 90.0 |
| Bench 2 | Autosub In | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.47 | 7.71 | 12.55 | 8.00 | 71.1 | 90.0 |
| XI | XI | Ayden Heaven | DEF | 14 | 3.8 | 3.05 | 7.45 | 11.24 | 2.00 | 69.8 | 74.0 |
| Bench 3 | Bench | Daniel Ballard | DEF | 17 | 4.7 | 1.77 | 5.82 | 10.67 | 0.00 | 41.0 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.02 | 23.78 | 39.70 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.46 | 13.61 | 21.18 | 2.00 | 54.4 | 90.0 |
| Bench 4 | Bench | Chido Obi | FWD | 14 | 4.2 | 0.41 | 0.49 | 0.61 | 0.00 | 2.4 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.35 | 16.67 | 27.90 | 3.00 | 83.4 | 90.0 |
| Vice Captain | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.0 | 6.18 | 16.40 | 24.91 | 2.00 | 85.5 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.08 | 14.94 | 24.02 | 5.00 | 84.0 | 90.0 |
| XI | Bench | Declan Rice | MID | 1 | 7.2 | 4.41 | 13.21 | 21.43 | 0.00 | 72.4 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.88 | 13.14 | 21.32 | 1.00 | 74.8 | 81.0 |

## GW20

- Train rows: 175452
- Bank: 0.00 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 64.44
- Actual score: 35.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (4.19) beats the best remaining Bench Boost opportunity (5.21).
- Transfer: Declan Rice -> Rayan Cherki (projected gain 6.38, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (4.19) beats the best remaining Bench Boost opportunity (5.21).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.5 | 3.35 | 10.03 | 16.37 | 1.00 | 85.6 | 90.0 |
| Bench 1 | Bench Boost | Hákon Rafn Valdimarsson | GK | 5 | 3.9 | 0.21 | 0.73 | 1.17 | 0.00 | 2.6 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.98 | 11.64 | 19.30 | 1.00 | 87.1 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 3.79 | 11.02 | 18.28 | 1.00 | 82.3 | 90.0 |
| XI | XI | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.85 | 8.00 | 12.45 | 2.00 | 79.2 | 90.0 |
| Bench 2 | Bench Boost | Ayden Heaven | DEF | 14 | 3.8 | 2.41 | 6.79 | 11.12 | 4.00 | 64.0 | 90.0 |
| Bench 3 | Bench Boost | Daniel Ballard | DEF | 17 | 4.6 | 1.45 | 4.83 | 9.16 | 1.00 | 32.6 | 24.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.21 | 24.22 | 40.11 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.58 | 14.22 | 23.39 | 0.00 | 67.0 | 0.0 |
| Bench 4 | Bench Boost | Chido Obi | FWD | 14 | 4.2 | 0.12 | 0.30 | 0.50 | 0.00 | 5.3 | 0.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.9 | 5.80 | 17.67 | 29.02 | 2.00 | 86.8 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 5.74 | 16.47 | 25.99 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.21 | 15.16 | 24.25 | 1.00 | 90.0 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.8 | 4.91 | 15.01 | 24.12 | 4.00 | 72.4 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.1 | 3.60 | 11.46 | 18.85 | 9.00 | 57.6 | 90.0 |

## GW21

- Train rows: 176242
- Bank: 0.30 -> 2.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 68.22
- Actual score: 59.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.06) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Hugo Ekitiké -> Igor Thiago Nascimento Rodrigues (projected gain 7.95, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.06) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.5 | 3.62 | 9.90 | 15.95 | 3.00 | 83.4 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.9 | 0.42 | 0.83 | 1.19 | 0.00 | 0.5 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.30 | 10.40 | 17.45 | 6.00 | 85.3 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 3.31 | 9.15 | 16.25 | 6.00 | 72.1 | 90.0 |
| XI | XI | Ayden Heaven | DEF | 14 | 3.8 | 3.13 | 8.36 | 13.44 | 0.00 | 71.8 | 60.0 |
| Bench 2 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.53 | 7.48 | 11.98 | 0.00 | 75.8 | 90.0 |
| Bench 3 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 1.52 | 5.42 | 10.05 | 1.00 | 31.4 | 78.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.06 | 23.88 | 39.02 | 6.00 | 90.0 | 90.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.55 | 15.39 | 24.47 | 12.00 | 90.0 | 81.0 |
| Bench 4 | Bench | Chido Obi | FWD | 14 | 4.2 | 0.25 | 0.44 | 0.71 | 0.00 | 5.0 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 8.8 | 5.48 | 15.99 | 26.77 | 2.00 | 81.9 | 72.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.8 | 5.04 | 14.73 | 23.52 | 1.00 | 80.8 | 17.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 5.10 | 14.29 | 23.30 | 6.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 4.73 | 13.75 | 22.17 | 3.00 | 75.8 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.1 | 4.78 | 13.62 | 22.39 | 2.00 | 79.3 | 73.0 |