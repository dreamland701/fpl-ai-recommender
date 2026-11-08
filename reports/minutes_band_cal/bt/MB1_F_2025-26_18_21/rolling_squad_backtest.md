# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW17
- Simulated weeks: GW18-GW21
- Total predicted points: 251.81
- Total actual points: 199.00
- Average predicted points: 62.95
- Average actual points: 49.75
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
- Predicted score: 64.64
- Actual score: 48.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Jaka Bijol replaced Daniel Ballard.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.5 | 3.48 | 9.59 | 15.42 | 6.00 | 83.1 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.22 | 11.90 | 18.83 | 2.00 | 79.8 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.04 | 11.43 | 17.88 | 2.00 | 80.8 | 90.0 |
| XI | Bench | Daniel Ballard | DEF | 17 | 4.7 | 4.08 | 11.07 | 17.55 | 0.00 | 81.1 | 0.0 |
| Bench 2 | Autosub In | Jaka Bijol | DEF | 11 | 3.9 | 2.76 | 8.25 | 12.88 | 2.00 | 72.1 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.65 | 7.89 | 12.63 | 2.00 | 72.3 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 7.89 | 23.16 | 38.76 | 2.00 | 83.1 | 90.0 |
| Vice Captain | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 6.33 | 16.82 | 25.30 | 5.00 | 80.0 | 85.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 1.32 | 4.15 | 7.15 | 1.00 | 27.2 | 45.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.77 | 18.00 | 28.77 | 2.00 | 81.5 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.37 | 15.57 | 24.42 | 9.00 | 82.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 5.22 | 14.77 | 23.47 | 5.00 | 83.1 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 5.11 | 14.67 | 23.24 | 1.00 | 83.1 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.1 | 5.25 | 13.92 | 21.75 | 10.00 | 78.0 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 58.51
- Actual score: 42.00
- Transfer: Daniel Ballard -> Diogo Dalot Teixeira (projected gain 3.35, hit 0)
- Autosub: Jaka Bijol replaced Declan Rice.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.5 | 3.13 | 9.30 | 15.14 | 10.00 | 82.9 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.9 | 0.00 | 0.00 | 0.18 | 0.00 | 1.1 | 0.0 |
| XI | XI | Diogo Dalot Teixeira | DEF | 14 | 4.5 | 4.48 | 11.31 | 17.15 | 2.00 | 84.3 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 3.96 | 10.82 | 17.66 | 2.00 | 83.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 3.33 | 9.51 | 15.16 | 3.00 | 80.0 | 90.0 |
| Bench 2 | Autosub In | Jaka Bijol | DEF | 11 | 3.9 | 2.62 | 8.02 | 13.07 | 7.00 | 72.5 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.54 | 7.86 | 12.80 | 8.00 | 74.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 7.50 | 22.23 | 37.56 | 2.00 | 83.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.55 | 13.84 | 21.49 | 2.00 | 57.9 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 1.70 | 5.19 | 8.51 | 0.00 | 39.5 | 0.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 9.0 | 5.47 | 16.88 | 28.06 | 3.00 | 82.8 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.20 | 15.13 | 24.16 | 5.00 | 83.6 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.1 | 5.00 | 14.03 | 22.11 | 3.00 | 80.6 | 65.0 |
| XI | Bench | Declan Rice | MID | 1 | 7.2 | 4.45 | 13.25 | 21.45 | 0.00 | 75.1 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.93 | 13.19 | 21.33 | 1.00 | 76.4 | 81.0 |

## GW20

- Train rows: 175452
- Bank: 0.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 62.18
- Actual score: 56.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.59) beats the best remaining Bench Boost opportunity (8.06).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.59) beats the best remaining Bench Boost opportunity (8.06).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.5 | 2.76 | 8.33 | 13.97 | 1.00 | 81.3 | 90.0 |
| Bench 1 | Bench Boost | Marcus Bettinelli | GK | 13 | 3.9 | 0.06 | 0.24 | 0.30 | 0.00 | 2.7 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 3.87 | 11.07 | 18.20 | 1.00 | 81.6 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 3.83 | 10.67 | 17.40 | 2.00 | 83.0 | 90.0 |
| Bench 2 | Bench Boost | Diogo Dalot Teixeira | DEF | 14 | 4.5 | 2.78 | 8.27 | 13.84 | 2.00 | 70.5 | 90.0 |
| XI | XI | Jaka Bijol | DEF | 11 | 3.9 | 3.00 | 8.07 | 13.22 | 4.00 | 75.9 | 90.0 |
| XI | XI | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.88 | 7.96 | 12.30 | 2.00 | 80.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 7.68 | 22.67 | 37.95 | 2.00 | 83.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.63 | 14.33 | 23.58 | 0.00 | 70.5 | 0.0 |
| Bench 4 | Bench Boost | Junior Kroupi | FWD | 4 | 4.6 | 1.01 | 3.48 | 5.61 | 5.00 | 23.9 | 16.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.9 | 5.30 | 16.23 | 27.06 | 2.00 | 79.9 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 5.23 | 14.97 | 23.90 | 5.00 | 83.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 4.73 | 13.73 | 22.30 | 1.00 | 83.0 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.1 | 4.00 | 12.19 | 20.48 | 10.00 | 64.0 | 75.0 |
| Bench 3 | Bench Boost | Declan Rice | MID | 1 | 7.1 | 2.73 | 8.97 | 16.12 | 17.00 | 37.6 | 90.0 |

## GW21

- Train rows: 176242
- Bank: 0.20 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Ollie Watkins
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 66.49
- Actual score: 53.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.52) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Hugo Ekitiké -> Ollie Watkins (projected gain 6.63, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (7.52) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.5 | 3.66 | 9.83 | 15.64 | 3.00 | 85.2 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.9 | 0.08 | 0.22 | 0.37 | 0.00 | 2.9 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 3.88 | 10.48 | 17.18 | 6.00 | 82.7 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 3.38 | 9.34 | 16.58 | 6.00 | 75.0 | 90.0 |
| XI | XI | Diogo Dalot Teixeira | DEF | 14 | 4.5 | 3.52 | 9.28 | 15.06 | 1.00 | 79.9 | 90.0 |
| Bench 2 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 3.12 | 8.47 | 14.02 | 3.00 | 80.3 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.56 | 7.44 | 11.86 | 0.00 | 76.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 7.52 | 22.28 | 36.78 | 6.00 | 83.0 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.7 | 5.64 | 15.01 | 23.68 | 2.00 | 84.8 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 1.28 | 4.05 | 6.74 | 7.00 | 25.8 | 63.0 |
| XI | XI | Phil Foden | MID | 13 | 8.8 | 5.61 | 16.18 | 26.91 | 2.00 | 81.5 | 72.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.1 | 4.27 | 13.81 | 23.45 | 3.00 | 72.6 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 4.78 | 13.81 | 22.20 | 3.00 | 77.2 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 4.57 | 13.25 | 22.42 | 3.00 | 81.5 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 4.63 | 12.92 | 21.48 | 6.00 | 83.0 | 90.0 |