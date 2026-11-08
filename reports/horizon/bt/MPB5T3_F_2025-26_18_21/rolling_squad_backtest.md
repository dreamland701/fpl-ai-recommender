# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW17
- Simulated weeks: GW18-GW21
- Total predicted points: 264.85
- Total actual points: 193.00
- Average predicted points: 66.21
- Average actual points: 48.25
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
- Predicted score: 67.22
- Actual score: 38.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Jaka Bijol replaced Jurriën Timber.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.77 | 11.01 | 18.02 | 2.00 | 87.9 | 90.0 |
| Bench 1 | Bench | Benjamin Lecomte | GK | 10 | 3.9 | 0.00 | 0.00 | 0.03 | 0.00 | 2.5 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.01 | 13.81 | 21.79 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Jurriën Timber | DEF | 1 | 6.5 | 4.43 | 12.20 | 19.76 | 0.00 | 85.2 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.13 | 11.87 | 19.02 | 2.00 | 80.6 | 90.0 |
| Bench 2 | Autosub In | Jaka Bijol | DEF | 11 | 3.9 | 2.67 | 8.08 | 12.54 | 2.00 | 68.7 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.57 | 7.65 | 12.23 | 2.00 | 68.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.42 | 25.36 | 42.16 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 6.87 | 17.46 | 26.55 | 5.00 | 87.0 | 85.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 1.39 | 4.30 | 7.34 | 1.00 | 28.4 | 45.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.68 | 17.68 | 28.48 | 2.00 | 82.3 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 5.75 | 16.31 | 25.73 | 5.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 5.65 | 15.74 | 24.81 | 1.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.28 | 15.28 | 24.27 | 9.00 | 82.8 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 4.8 | 3.81 | 11.40 | 17.92 | 4.00 | 79.0 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 0.00 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 59.35
- Actual score: 38.00
- Transfer: Jurriën Timber -> Joško Gvardiol (projected gain 13.42, hit 0)
- Autosub: Jaka Bijol replaced Declan Rice.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.63 | 10.59 | 17.44 | 2.00 | 84.5 | 90.0 |
| Bench 1 | Bench | Benjamin Lecomte | GK | 10 | 3.9 | 0.00 | 0.07 | 0.18 | 0.00 | 3.5 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.50 | 12.50 | 19.99 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.12 | 12.10 | 20.00 | 6.00 | 82.8 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.01 | 11.62 | 19.00 | 1.00 | 87.3 | 33.0 |
| Bench 2 | Autosub In | Jaka Bijol | DEF | 11 | 3.9 | 2.54 | 7.68 | 12.44 | 7.00 | 69.1 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.45 | 7.48 | 12.23 | 8.00 | 70.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.04 | 24.47 | 40.85 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.41 | 12.88 | 20.04 | 2.00 | 54.6 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 1.76 | 5.16 | 8.48 | 0.00 | 40.7 | 0.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 9.0 | 5.39 | 16.92 | 28.25 | 3.00 | 83.5 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.11 | 15.21 | 24.49 | 5.00 | 84.3 | 90.0 |
| XI | Bench | Declan Rice | MID | 1 | 7.2 | 4.41 | 13.36 | 21.79 | 0.00 | 73.5 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.89 | 12.73 | 20.70 | 1.00 | 74.8 | 81.0 |
| XI | XI | Anton Stach | MID | 11 | 4.8 | 3.80 | 11.45 | 18.45 | 5.00 | 77.8 | 90.0 |

## GW20

- Train rows: 175452
- Bank: 0.40 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 69.79
- Actual score: 42.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.04) beats the best remaining Bench Boost opportunity (8.36).
- Transfer: Declan Rice -> Bruno Guimarães Rodriguez Moura (projected gain 19.26, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.04) beats the best remaining Bench Boost opportunity (8.36).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.75 | 11.06 | 18.10 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Benjamin Lecomte | GK | 10 | 3.9 | 0.17 | 0.37 | 0.60 | 0.00 | 5.6 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.37 | 12.39 | 19.98 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.01 | 11.80 | 19.69 | 1.00 | 86.1 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.68 | 11.12 | 18.34 | 1.00 | 64.2 | 50.0 |
| Bench 2 | Bench Boost | Jaka Bijol | DEF | 11 | 3.9 | 2.95 | 7.89 | 13.00 | 4.00 | 74.3 | 90.0 |
| Bench 3 | Bench Boost | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.84 | 7.89 | 12.27 | 2.00 | 78.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.22 | 24.72 | 41.24 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.54 | 14.11 | 23.12 | 0.00 | 67.1 | 0.0 |
| Bench 4 | Bench Boost | Junior Kroupi | FWD | 4 | 4.6 | 1.08 | 3.70 | 6.01 | 5.00 | 25.1 | 16.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.9 | 5.84 | 17.48 | 28.97 | 2.00 | 86.9 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 5.77 | 16.06 | 25.59 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.26 | 15.41 | 24.70 | 1.00 | 90.0 | 90.0 |
| XI | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.0 | 4.94 | 13.80 | 22.37 | 10.00 | 89.0 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 4.8 | 4.16 | 11.30 | 18.26 | 4.00 | 81.2 | 90.0 |

## GW21

- Train rows: 176242
- Bank: 0.50 -> 2.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 68.49
- Actual score: 75.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.05) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Hugo Ekitiké -> Igor Thiago Nascimento Rodrigues (projected gain 22.02, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.05) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Jaka Bijol replaced Joško Gvardiol.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.42 | 10.16 | 16.64 | 6.00 | 83.7 | 90.0 |
| Bench 1 | Bench | Benjamin Lecomte | GK | 10 | 3.9 | 0.11 | 0.28 | 0.43 | 0.00 | 4.2 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.41 | 12.20 | 19.74 | 6.00 | 89.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.33 | 10.59 | 17.86 | 6.00 | 84.2 | 90.0 |
| XI | Bench | Joško Gvardiol | DEF | 13 | 6.0 | 3.19 | 9.66 | 16.42 | 0.00 | 58.4 | 0.0 |
| Bench 2 | Autosub In | Jaka Bijol | DEF | 11 | 3.9 | 3.08 | 8.33 | 13.82 | 3.00 | 78.7 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.52 | 7.32 | 11.67 | 0.00 | 75.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.05 | 24.36 | 40.00 | 6.00 | 90.0 | 90.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.66 | 15.14 | 24.40 | 12.00 | 90.0 | 81.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 1.35 | 4.13 | 6.86 | 7.00 | 27.0 | 63.0 |
| XI | XI | Phil Foden | MID | 13 | 8.8 | 5.50 | 15.89 | 26.70 | 2.00 | 82.2 | 72.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 5.17 | 14.78 | 24.08 | 6.00 | 90.0 | 90.0 |
| XI | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.0 | 5.02 | 14.14 | 22.91 | 11.00 | 88.6 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 4.74 | 13.42 | 21.57 | 3.00 | 75.7 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 4.8 | 3.90 | 10.65 | 17.81 | 2.00 | 80.2 | 79.0 |