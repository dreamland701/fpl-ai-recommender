# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW17
- Simulated weeks: GW18-GW21
- Total predicted points: 252.35
- Total actual points: 163.00
- Average predicted points: 63.09
- Average actual points: 40.75
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
- Captain: Hugo Ekitiké
- Vice captain: Morgan Rogers
- Effective captain: Hugo Ekitiké
- Chip used: none
- Predicted score: 65.02
- Actual score: 45.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Dominic Calvert-Lewin replaced Jurriën Timber.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.81 | 11.03 | 17.91 | 2.00 | 89.5 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 5.5 | 3.48 | 9.62 | 15.57 | 6.00 | 85.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.10 | 13.76 | 21.59 | 2.00 | 96.2 | 90.0 |
| XI | Bench | Jurriën Timber | DEF | 1 | 6.5 | 4.60 | 12.44 | 19.89 | 0.00 | 88.9 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.11 | 11.93 | 19.02 | 2.00 | 80.5 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 3.87 | 11.30 | 17.89 | 2.00 | 80.5 | 90.0 |
| Bench 3 | Bench | Joško Gvardiol | DEF | 13 | 6.0 | 3.84 | 11.29 | 18.63 | 8.00 | 79.4 | 90.0 |
| Captain | Captain | Hugo Ekitiké | FWD | 12 | 9.0 | 7.46 | 18.80 | 28.09 | 5.00 | 97.9 | 85.0 |
| Bench 2 | Autosub In | Dominic Calvert-Lewin | FWD | 11 | 5.8 | 3.86 | 11.03 | 17.48 | 8.00 | 67.2 | 84.0 |
| Bench 4 | Bench | Igor Jesus Maciel da Cruz | FWD | 16 | 5.8 | 2.80 | 8.23 | 13.49 | 5.00 | 59.7 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.71 | 17.92 | 28.79 | 2.00 | 82.4 | 90.0 |
| Vice Captain | XI | Morgan Rogers | MID | 2 | 7.3 | 6.02 | 16.29 | 25.50 | 1.00 | 106.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 5.83 | 16.24 | 25.52 | 5.00 | 99.3 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.35 | 15.51 | 24.48 | 9.00 | 84.8 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.0 | 5.70 | 15.13 | 23.36 | 2.00 | 91.7 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 0.10 -> 0.80
- Free transfers: 2 -> 2
- Captain: Matheus Santos Carneiro da Cunha
- Vice captain: Phil Foden
- Effective captain: Matheus Santos Carneiro da Cunha
- Chip used: none
- Predicted score: 56.33
- Actual score: 30.00
- Transfer: Jurriën Timber -> Reece James (projected gain 0.94, hit 0)
- Autosub: Marcos Senesi Barón replaced Declan Rice.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.67 | 10.59 | 17.26 | 2.00 | 86.3 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 5.5 | 3.06 | 9.33 | 15.30 | 10.00 | 83.7 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.61 | 12.66 | 20.21 | 2.00 | 92.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.11 | 11.95 | 19.66 | 6.00 | 83.3 | 90.0 |
| XI | XI | Reece James | DEF | 7 | 5.7 | 4.37 | 11.91 | 18.76 | 1.00 | 86.3 | 45.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.08 | 11.70 | 19.10 | 1.00 | 88.2 | 33.0 |
| Bench 2 | Autosub In | Marcos Senesi Barón | DEF | 4 | 4.9 | 3.73 | 11.10 | 17.38 | 3.00 | 84.6 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.49 | 13.46 | 20.89 | 2.00 | 55.6 | 90.0 |
| Bench 4 | Bench | Dominic Calvert-Lewin | FWD | 11 | 5.8 | 3.03 | 9.80 | 16.47 | 1.00 | 53.7 | 20.0 |
| Bench 3 | Bench | Igor Jesus Maciel da Cruz | FWD | 16 | 5.8 | 3.23 | 9.69 | 15.57 | 2.00 | 69.5 | 61.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 9.0 | 5.24 | 16.71 | 27.94 | 3.00 | 80.7 | 90.0 |
| Captain | Captain | Matheus Santos Carneiro da Cunha | MID | 14 | 8.0 | 6.39 | 16.04 | 24.31 | 2.00 | 89.8 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 4.95 | 15.04 | 24.20 | 5.00 | 82.2 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.87 | 12.95 | 21.03 | 1.00 | 73.9 | 81.0 |
| XI | Bench | Declan Rice | MID | 1 | 7.2 | 4.16 | 12.91 | 21.00 | 0.00 | 69.2 | 0.0 |

## GW20

- Train rows: 175452
- Bank: 0.80 -> 0.10
- Free transfers: 2 -> 2
- Captain: Morgan Rogers
- Vice captain: Phil Foden
- Effective captain: Morgan Rogers
- Chip used: wildcard
- Predicted score: 59.76
- Actual score: 39.00
- Chip advisory: bench_boost (0.62): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Chip used: Wildcard — full rebuild projects +13.47 squad value (threshold 12).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.89 | 11.32 | 18.24 | 1.00 | 94.2 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.26 | 9.47 | 15.14 | 1.00 | 94.9 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.6 | 4.78 | 12.97 | 20.96 | 2.00 | 99.2 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.40 | 12.47 | 19.94 | 2.00 | 95.2 | 90.0 |
| XI | XI | Rúben dos Santos Gato Alves Dias | DEF | 13 | 5.7 | 3.99 | 11.77 | 19.53 | 5.00 | 85.2 | 80.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.00 | 11.74 | 19.44 | 1.00 | 86.8 | 90.0 |
| Bench 3 | Bench | Marcos Senesi Barón | DEF | 4 | 4.8 | 3.90 | 11.23 | 18.59 | 1.00 | 85.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.6 | 4.87 | 13.72 | 22.30 | 7.00 | 78.7 | 82.0 |
| Bench 2 | Bench | Richarlison de Andrade | FWD | 18 | 6.4 | 3.94 | 11.31 | 18.39 | 2.00 | 74.3 | 90.0 |
| Bench 4 | Bench | Raúl Jiménez Rodríguez | FWD | 10 | 6.2 | 3.82 | 10.44 | 17.08 | 5.00 | 76.4 | 84.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.9 | 5.82 | 17.83 | 29.26 | 2.00 | 86.7 | 90.0 |
| Captain | Captain | Morgan Rogers | MID | 2 | 7.5 | 6.13 | 16.77 | 26.43 | 5.00 | 102.6 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.3 | 5.63 | 16.41 | 26.73 | 4.00 | 80.6 | 23.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.22 | 15.33 | 24.54 | 1.00 | 92.6 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.8 | 4.89 | 14.95 | 24.00 | 4.00 | 73.5 | 90.0 |

## GW21

- Train rows: 176242
- Bank: 0.10 -> 0.90
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Phil Foden
- Effective captain: Ollie Watkins
- Chip used: bench_boost
- Predicted score: 71.25
- Actual score: 49.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.68) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Virgil van Dijk -> Malick Thiaw (projected gain 1.37, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.68) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.47 | 10.21 | 16.69 | 6.00 | 85.4 | 90.0 |
| Bench 1 | Bench Boost | Martin Dúbravka | GK | 3 | 4.0 | 3.21 | 8.92 | 14.48 | 3.00 | 90.9 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.6 | 5.06 | 13.14 | 20.19 | 4.00 | 93.9 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.42 | 12.21 | 19.59 | 6.00 | 91.0 | 90.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 4.46 | 11.90 | 19.76 | -1.00 | 92.9 | 45.0 |
| Bench 3 | Bench Boost | Rúben dos Santos Gato Alves Dias | DEF | 13 | 5.7 | 3.53 | 10.54 | 17.36 | 0.00 | 75.2 | 0.0 |
| Bench 4 | Bench Boost | Marcos Senesi Barón | DEF | 4 | 4.8 | 3.41 | 9.29 | 16.40 | 6.00 | 74.0 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.6 | 5.76 | 15.02 | 23.86 | 2.00 | 88.9 | 90.0 |
| XI | XI | Richarlison de Andrade | FWD | 18 | 6.4 | 3.89 | 11.46 | 17.50 | 1.00 | 79.5 | 23.0 |
| Bench 2 | Bench Boost | Raúl Jiménez Rodríguez | FWD | 10 | 6.2 | 3.54 | 10.26 | 16.92 | 5.00 | 69.4 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.8 | 5.46 | 16.10 | 26.92 | 2.00 | 82.0 | 72.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.8 | 5.13 | 14.82 | 23.66 | 1.00 | 84.0 | 17.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 5.11 | 14.53 | 23.72 | 6.00 | 91.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.83 | 13.81 | 22.23 | 3.00 | 75.9 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.2 | 4.21 | 13.62 | 23.02 | 3.00 | 53.4 | 77.0 |