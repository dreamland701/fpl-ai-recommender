# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW17
- Simulated weeks: GW18-GW21
- Total predicted points: 252.41
- Total actual points: 194.00
- Average predicted points: 63.10
- Average actual points: 48.50
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
- Predicted score: 64.18
- Actual score: 40.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Nordi Mukiele replaced Jurriën Timber.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Gianluigi Donnarumma | GK | 13 | 5.7 | 3.28 | 9.55 | 15.67 | 2.00 | 82.3 | 90.0 |
| Bench 1 | Bench | Callan McKenna | GK | 4 | 3.9 | 0.00 | 0.04 | 0.16 | 0.00 | 1.9 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.58 | 12.37 | 19.58 | 2.00 | 83.4 | 90.0 |
| XI | Bench | Jurriën Timber | DEF | 1 | 6.5 | 4.44 | 12.20 | 19.41 | 0.00 | 83.3 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.14 | 11.75 | 18.63 | 2.00 | 78.7 | 90.0 |
| Bench 2 | Autosub In | Nordi Mukiele | DEF | 17 | 4.2 | 3.51 | 9.51 | 14.82 | 4.00 | 82.2 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.64 | 7.86 | 12.58 | 2.00 | 72.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 7.99 | 23.47 | 39.12 | 2.00 | 83.4 | 90.0 |
| Vice Captain | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 6.43 | 17.12 | 25.67 | 5.00 | 80.4 | 85.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 1.36 | 4.24 | 7.26 | 1.00 | 27.9 | 45.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.68 | 17.85 | 28.56 | 2.00 | 80.5 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.28 | 15.43 | 24.21 | 9.00 | 80.9 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 5.32 | 15.07 | 23.84 | 5.00 | 83.4 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 5.22 | 14.97 | 23.61 | 1.00 | 83.4 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 4.8 | 3.83 | 11.45 | 18.13 | 4.00 | 79.6 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 57.98
- Actual score: 47.00
- Transfer: Jurriën Timber -> Reece James (projected gain 3.11, hit 0)
- Autosub: Nordi Mukiele replaced Declan Rice.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Gianluigi Donnarumma | GK | 13 | 5.7 | 3.05 | 9.06 | 14.96 | 7.00 | 80.0 | 90.0 |
| Bench 1 | Bench | Callan McKenna | GK | 4 | 3.9 | 0.00 | 0.15 | 0.21 | 0.00 | 2.8 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.13 | 11.86 | 19.40 | 6.00 | 80.9 | 90.0 |
| XI | XI | Reece James | DEF | 7 | 5.7 | 4.28 | 11.76 | 18.40 | 1.00 | 82.8 | 45.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.07 | 11.13 | 18.03 | 2.00 | 83.4 | 90.0 |
| Bench 2 | Autosub In | Nordi Mukiele | DEF | 17 | 4.2 | 3.00 | 8.75 | 14.17 | 11.00 | 80.6 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.52 | 7.82 | 12.75 | 8.00 | 74.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 7.60 | 22.54 | 37.93 | 2.00 | 83.4 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.60 | 13.98 | 21.70 | 2.00 | 59.1 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 1.74 | 5.28 | 8.62 | 0.00 | 40.2 | 0.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 9.0 | 5.39 | 16.73 | 27.85 | 3.00 | 81.7 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.11 | 14.98 | 23.95 | 5.00 | 82.4 | 90.0 |
| XI | Bench | Declan Rice | MID | 1 | 7.2 | 4.43 | 13.27 | 21.56 | 0.00 | 74.0 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.90 | 13.20 | 21.44 | 1.00 | 75.3 | 81.0 |
| XI | XI | Anton Stach | MID | 11 | 4.8 | 3.82 | 11.73 | 19.03 | 5.00 | 78.3 | 90.0 |

## GW20

- Train rows: 175452
- Bank: 0.70 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 64.54
- Actual score: 52.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.67) beats the best remaining Bench Boost opportunity (8.05).
- Transfer: Reece James -> Jurriën Timber (projected gain 4.13, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.67) beats the best remaining Bench Boost opportunity (8.05).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Gianluigi Donnarumma | GK | 13 | 5.7 | 3.05 | 8.99 | 14.82 | 2.00 | 80.2 | 90.0 |
| Bench 1 | Bench Boost | Callan McKenna | GK | 4 | 3.9 | 0.00 | 0.10 | 0.16 | 0.00 | 4.2 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.11 | 12.08 | 19.80 | 3.00 | 75.2 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 3.94 | 10.97 | 17.76 | 2.00 | 83.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.58 | 10.43 | 17.59 | 1.00 | 79.6 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.2 | 3.26 | 9.00 | 15.05 | 4.00 | 83.4 | 90.0 |
| Bench 2 | Bench Boost | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.85 | 7.97 | 12.40 | 2.00 | 79.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 7.79 | 22.97 | 38.31 | 2.00 | 83.4 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.62 | 14.30 | 23.53 | 0.00 | 70.5 | 0.0 |
| Bench 4 | Bench Boost | Junior Kroupi | FWD | 4 | 4.6 | 1.05 | 3.57 | 5.71 | 5.00 | 24.5 | 16.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.9 | 5.41 | 16.53 | 27.42 | 2.00 | 80.3 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 5.34 | 15.26 | 24.26 | 5.00 | 83.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 4.83 | 14.03 | 22.66 | 1.00 | 83.4 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 4.8 | 4.17 | 11.41 | 18.45 | 4.00 | 79.4 | 90.0 |
| Bench 3 | Bench Boost | Declan Rice | MID | 1 | 7.1 | 2.77 | 9.06 | 16.23 | 17.00 | 38.3 | 90.0 |

## GW21

- Train rows: 176242
- Bank: 0.00 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Ollie Watkins
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 65.71
- Actual score: 55.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.63) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Hugo Ekitiké -> Ollie Watkins (projected gain 6.46, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (7.63) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Gianluigi Donnarumma | GK | 13 | 5.7 | 2.88 | 8.59 | 14.36 | 1.00 | 79.7 | 90.0 |
| Bench 1 | Bench | Callan McKenna | GK | 4 | 3.9 | 0.11 | 0.17 | 0.30 | 0.00 | 3.1 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 3.99 | 10.78 | 17.54 | 6.00 | 83.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.35 | 10.44 | 17.37 | 6.00 | 82.3 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 3.46 | 10.29 | 17.02 | 6.00 | 70.8 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.2 | 2.99 | 8.47 | 14.26 | 3.00 | 80.8 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.53 | 7.47 | 11.96 | 0.00 | 75.6 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 7.63 | 22.57 | 37.14 | 6.00 | 83.4 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.7 | 5.55 | 14.85 | 23.49 | 2.00 | 83.6 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 1.32 | 4.13 | 6.84 | 7.00 | 26.4 | 63.0 |
| XI | XI | Phil Foden | MID | 13 | 8.8 | 5.52 | 16.03 | 26.72 | 2.00 | 80.3 | 72.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 4.76 | 13.83 | 22.30 | 3.00 | 76.1 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 4.68 | 13.55 | 22.78 | 3.00 | 81.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 4.74 | 13.22 | 21.84 | 6.00 | 83.4 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 4.8 | 3.91 | 10.89 | 18.09 | 2.00 | 78.3 | 79.0 |