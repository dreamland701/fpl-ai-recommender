# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW17
- Simulated weeks: GW18-GW21
- Total predicted points: 256.57
- Total actual points: 161.00
- Average predicted points: 64.14
- Average actual points: 40.25
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
- Predicted score: 67.39
- Actual score: 36.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Gabriel Gudmundsson replaced Jurriën Timber.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.46 | 12.89 | 21.26 | 2.00 | 87.9 | 90.0 |
| Bench 1 | Bench | Sam Proctor | GK | 2 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 2.3 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.68 | 15.19 | 23.68 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Jurriën Timber | DEF | 1 | 6.5 | 4.77 | 13.37 | 21.06 | 0.00 | 85.2 | 0.0 |
| XI | XI | Ibrahima Konaté | DEF | 12 | 5.4 | 4.56 | 12.39 | 19.92 | 2.00 | 80.4 | 90.0 |
| Bench 3 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 2.70 | 8.35 | 12.55 | 2.00 | 68.7 | 90.0 |
| Bench 2 | Autosub In | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.85 | 8.05 | 12.31 | 2.00 | 68.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 7.68 | 22.17 | 37.02 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 6.31 | 16.71 | 25.48 | 5.00 | 87.0 | 85.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.3 | 0.82 | 2.29 | 3.47 | 0.00 | 13.6 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.72 | 17.46 | 27.98 | 2.00 | 82.3 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 5.55 | 16.01 | 24.97 | 1.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 5.51 | 15.99 | 24.96 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.35 | 15.96 | 24.92 | 9.00 | 82.8 | 90.0 |
| XI | XI | Adam Wharton | MID | 8 | 5.0 | 4.11 | 11.33 | 17.83 | 2.00 | 76.1 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 58.95
- Actual score: 40.00
- Transfer: Jurriën Timber -> Reece James (projected gain 5.34, hit 0)
- Autosub: Jaka Bijol replaced Declan Rice.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.43 | 13.27 | 21.74 | 2.00 | 84.5 | 90.0 |
| Bench 1 | Bench | Sam Proctor | GK | 2 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 2.7 | 0.0 |
| XI | XI | Reece James | DEF | 7 | 5.7 | 4.60 | 13.29 | 20.63 | 1.00 | 84.6 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.46 | 12.50 | 20.83 | 6.00 | 82.8 | 90.0 |
| XI | XI | Ibrahima Konaté | DEF | 12 | 5.4 | 3.38 | 9.53 | 15.95 | 7.00 | 77.5 | 90.0 |
| Bench 2 | Autosub In | Jaka Bijol | DEF | 11 | 3.9 | 2.62 | 8.00 | 12.74 | 7.00 | 69.1 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.54 | 7.62 | 12.12 | 8.00 | 70.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 7.20 | 22.06 | 36.48 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.14 | 12.80 | 19.26 | 2.00 | 54.6 | 90.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.3 | 0.31 | 1.48 | 3.13 | 0.00 | 7.0 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.23 | 16.19 | 26.95 | 3.00 | 83.5 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.27 | 15.84 | 25.03 | 5.00 | 84.3 | 90.0 |
| XI | Bench | Declan Rice | MID | 1 | 7.2 | 4.50 | 13.45 | 21.69 | 0.00 | 73.5 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 4.10 | 13.25 | 21.70 | 1.00 | 74.8 | 81.0 |
| XI | XI | Adam Wharton | MID | 8 | 5.0 | 4.43 | 11.57 | 18.54 | 2.00 | 81.4 | 90.0 |

## GW20

- Train rows: 175452
- Bank: 0.70 -> 1.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Morgan Rogers
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 64.34
- Actual score: 30.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (4.85) beats the best remaining Bench Boost opportunity (5.72).
- Transfer: Declan Rice -> Rayan Cherki (projected gain 7.85, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (4.85) beats the best remaining Bench Boost opportunity (5.72).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.83 | 14.04 | 22.95 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Sam Proctor | GK | 2 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 3.8 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.35 | 12.42 | 20.25 | 1.00 | 86.1 | 90.0 |
| XI | XI | Ibrahima Konaté | DEF | 12 | 5.4 | 3.60 | 10.43 | 17.04 | 1.00 | 80.2 | 90.0 |
| Bench 3 | Bench Boost | Reece James | DEF | 7 | 5.7 | 2.04 | 8.93 | 14.96 | 1.00 | 64.8 | 90.0 |
| XI | XI | Jaka Bijol | DEF | 11 | 3.9 | 2.97 | 8.01 | 12.45 | 4.00 | 74.3 | 90.0 |
| Bench 2 | Bench Boost | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.81 | 7.64 | 11.78 | 2.00 | 78.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 7.18 | 21.47 | 36.65 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.46 | 13.34 | 21.97 | 0.00 | 67.1 | 0.0 |
| Bench 4 | Bench Boost | Marc Guiu Paz | FWD | 7 | 4.3 | 0.00 | 1.26 | 2.78 | 0.00 | 8.2 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 8.9 | 5.29 | 17.07 | 27.65 | 2.00 | 86.9 | 90.0 |
| Vice Captain | XI | Morgan Rogers | MID | 2 | 7.4 | 5.60 | 16.42 | 25.85 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.36 | 15.95 | 25.48 | 1.00 | 90.0 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.8 | 5.14 | 15.49 | 24.97 | 4.00 | 73.8 | 90.0 |
| XI | XI | Adam Wharton | MID | 8 | 5.0 | 3.55 | 11.33 | 17.80 | 4.00 | 80.7 | 86.0 |

## GW21

- Train rows: 176242
- Bank: 1.00 -> 2.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Rayan Cherki
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 65.89
- Actual score: 55.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.20) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Hugo Ekitiké -> Jarrod Bowen (projected gain 11.44, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (7.20) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.34 | 12.56 | 20.91 | 6.00 | 83.7 | 90.0 |
| Bench 1 | Bench | Sam Proctor | GK | 2 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 3.5 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.51 | 11.31 | 18.46 | 6.00 | 84.2 | 90.0 |
| XI | XI | Reece James | DEF | 7 | 5.7 | 3.68 | 10.93 | 17.84 | 1.00 | 79.7 | 25.0 |
| XI | XI | Ibrahima Konaté | DEF | 12 | 5.4 | 3.17 | 10.30 | 17.09 | 7.00 | 80.3 | 90.0 |
| Bench 2 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 2.89 | 7.89 | 12.87 | 3.00 | 78.7 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.54 | 6.87 | 10.82 | 0.00 | 75.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 7.20 | 21.46 | 35.12 | 6.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 4.86 | 19.25 | 25.85 | 2.00 | 79.4 | 90.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.3 | 0.33 | 1.05 | 1.93 | 0.00 | 8.7 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 8.8 | 5.14 | 15.69 | 26.03 | 2.00 | 82.2 | 72.0 |
| Vice Captain | XI | Rayan Cherki | MID | 13 | 6.8 | 5.48 | 15.52 | 24.75 | 1.00 | 82.2 | 17.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 5.28 | 14.80 | 24.18 | 6.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 4.89 | 13.57 | 22.21 | 3.00 | 75.7 | 90.0 |
| XI | XI | Adam Wharton | MID | 8 | 5.0 | 3.93 | 12.00 | 18.64 | 3.00 | 80.1 | 90.0 |