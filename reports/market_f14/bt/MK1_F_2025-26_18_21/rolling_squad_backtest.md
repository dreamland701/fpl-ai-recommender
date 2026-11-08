# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW17
- Simulated weeks: GW18-GW21
- Total predicted points: 264.35
- Total actual points: 183.00
- Average predicted points: 66.09
- Average actual points: 45.75
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
- Predicted score: 67.85
- Actual score: 45.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Jaka Bijol replaced Jurriën Timber.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.14 | 11.87 | 19.07 | 2.00 | 88.9 | 90.0 |
| Bench 1 | Bench | Krisztián Hegyi | GK | 19 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.24 | 14.59 | 22.69 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Jurriën Timber | DEF | 1 | 6.5 | 4.78 | 13.25 | 20.84 | 0.00 | 85.2 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 3.94 | 11.34 | 18.06 | 2.00 | 81.5 | 90.0 |
| Bench 2 | Autosub In | Jaka Bijol | DEF | 11 | 3.9 | 2.87 | 8.28 | 12.72 | 2.00 | 67.8 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.85 | 7.96 | 12.54 | 2.00 | 70.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.26 | 24.30 | 40.14 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 6.89 | 18.39 | 27.38 | 5.00 | 90.0 | 85.0 |
| Bench 4 | Bench | Chido Obi | FWD | 14 | 4.2 | 0.06 | 0.14 | 0.18 | 0.00 | 0.0 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.67 | 17.92 | 28.61 | 2.00 | 82.3 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 5.87 | 16.95 | 26.42 | 5.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 5.30 | 15.41 | 24.67 | 1.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.07 | 14.81 | 23.79 | 9.00 | 85.6 | 90.0 |
| XI | XI | Ryan Gravenberch | MID | 12 | 5.6 | 4.43 | 12.47 | 19.66 | 11.00 | 80.6 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 0.00 -> 1.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 60.42
- Actual score: 40.00
- Transfer: Jurriën Timber -> Marc Guéhi (projected gain 5.42, hit 0)
- Autosub: Jaka Bijol replaced Declan Rice.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.04 | 11.33 | 18.18 | 2.00 | 85.5 | 90.0 |
| Bench 1 | Bench | Krisztián Hegyi | GK | 19 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 1.7 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.43 | 12.65 | 20.46 | 6.00 | 81.7 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.70 | 12.63 | 20.21 | 2.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 3.68 | 10.90 | 17.32 | 3.00 | 87.6 | 90.0 |
| Bench 2 | Autosub In | Jaka Bijol | DEF | 11 | 3.9 | 2.35 | 7.24 | 12.03 | 7.00 | 70.8 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.27 | 7.09 | 11.83 | 8.00 | 73.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.13 | 23.93 | 39.52 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.55 | 13.55 | 20.78 | 2.00 | 54.3 | 90.0 |
| Bench 4 | Bench | Chido Obi | FWD | 14 | 4.2 | 0.30 | 0.18 | 0.27 | 0.00 | 1.5 | 0.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 9.0 | 5.58 | 17.27 | 28.33 | 3.00 | 81.1 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 4.75 | 14.22 | 23.45 | 5.00 | 87.3 | 90.0 |
| XI | Bench | Declan Rice | MID | 1 | 7.2 | 4.57 | 13.73 | 21.92 | 0.00 | 68.7 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.61 | 12.32 | 20.60 | 1.00 | 76.0 | 81.0 |
| XI | XI | Ryan Gravenberch | MID | 12 | 5.6 | 4.24 | 11.86 | 19.02 | 5.00 | 79.5 | 90.0 |

## GW20

- Train rows: 175452
- Bank: 1.10 -> 1.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Morgan Rogers
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 68.27
- Actual score: 29.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.03) beats the best remaining Bench Boost opportunity (7.13).
- Transfer: Declan Rice -> Rayan Cherki (projected gain 7.05, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.03) beats the best remaining Bench Boost opportunity (7.13).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.08 | 11.87 | 18.98 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Krisztián Hegyi | GK | 19 | 3.9 | 0.04 | 0.07 | 0.02 | 0.00 | 2.9 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.22 | 12.10 | 19.81 | 1.00 | 85.7 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.24 | 11.86 | 19.32 | 2.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 3.77 | 10.97 | 18.36 | 1.00 | 85.5 | 90.0 |
| Bench 3 | Bench Boost | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.90 | 8.03 | 12.44 | 2.00 | 79.2 | 90.0 |
| Bench 2 | Bench Boost | Jaka Bijol | DEF | 11 | 3.9 | 2.98 | 7.97 | 13.12 | 4.00 | 75.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 7.97 | 23.98 | 39.62 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.78 | 14.50 | 23.60 | 0.00 | 68.2 | 0.0 |
| Bench 4 | Bench Boost | Chido Obi | FWD | 14 | 4.2 | 0.11 | 0.42 | 0.74 | 0.00 | 3.3 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 8.9 | 5.67 | 17.86 | 29.08 | 2.00 | 86.4 | 90.0 |
| Vice Captain | XI | Morgan Rogers | MID | 2 | 7.4 | 5.85 | 16.50 | 26.11 | 5.00 | 90.0 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.8 | 4.77 | 14.99 | 23.76 | 4.00 | 72.8 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 4.98 | 14.53 | 23.77 | 1.00 | 90.0 | 90.0 |
| XI | XI | Ryan Gravenberch | MID | 12 | 5.6 | 3.93 | 11.49 | 18.92 | 2.00 | 80.1 | 90.0 |

## GW21

- Train rows: 176242
- Bank: 1.40 -> 3.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 67.82
- Actual score: 69.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.86) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Hugo Ekitiké -> Igor Thiago Nascimento Rodrigues (projected gain 7.90, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (7.86) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.75 | 10.66 | 17.22 | 6.00 | 85.5 | 90.0 |
| Bench 1 | Bench | Krisztián Hegyi | GK | 19 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 2.1 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.42 | 12.04 | 19.47 | 6.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 3.58 | 9.92 | 17.23 | 6.00 | 72.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.10 | 9.77 | 16.70 | 6.00 | 85.7 | 90.0 |
| Bench 2 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 2.93 | 8.00 | 13.55 | 3.00 | 81.1 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.36 | 7.02 | 11.46 | 0.00 | 77.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 7.86 | 23.67 | 38.58 | 6.00 | 90.0 | 90.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.93 | 15.81 | 25.05 | 12.00 | 90.0 | 81.0 |
| Bench 4 | Bench | Chido Obi | FWD | 14 | 4.2 | 0.23 | 0.48 | 0.87 | 0.00 | 3.7 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 8.8 | 5.41 | 16.17 | 26.89 | 2.00 | 82.0 | 72.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.8 | 5.03 | 15.05 | 23.83 | 1.00 | 82.1 | 17.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 5.16 | 14.59 | 23.81 | 6.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 4.60 | 13.25 | 21.73 | 3.00 | 78.4 | 90.0 |
| XI | XI | Ryan Gravenberch | MID | 12 | 5.6 | 3.25 | 10.36 | 17.08 | 3.00 | 83.3 | 90.0 |