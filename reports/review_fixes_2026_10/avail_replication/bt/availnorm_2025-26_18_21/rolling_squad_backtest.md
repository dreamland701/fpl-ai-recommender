# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW17
- Simulated weeks: GW18-GW21
- Total predicted points: 215.85
- Total actual points: 182.00
- Average predicted points: 53.96
- Average actual points: 45.50
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
- Captain: Morgan Rogers
- Vice captain: Declan Rice
- Effective captain: Morgan Rogers
- Chip used: none
- Predicted score: 52.64
- Actual score: 55.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Joško Gvardiol replaced Jurriën Timber.
- Autosub: Igor Jesus Maciel da Cruz replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.30 | 9.60 | 15.67 | 2.00 | 89.5 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 5.5 | 3.19 | 8.84 | 14.34 | 6.00 | 85.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.56 | 12.22 | 19.12 | 2.00 | 96.2 | 90.0 |
| XI | Bench | Jurriën Timber | DEF | 1 | 6.5 | 4.12 | 11.08 | 17.75 | 0.00 | 88.9 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 3.50 | 10.23 | 16.32 | 2.00 | 80.5 | 90.0 |
| Bench 2 | Autosub In | Joško Gvardiol | DEF | 13 | 6.0 | 3.43 | 10.13 | 16.80 | 8.00 | 79.4 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.5 | 3.60 | 10.07 | 16.29 | 8.00 | 84.5 | 90.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 11 | 5.8 | 3.64 | 10.40 | 16.50 | 8.00 | 67.2 | 84.0 |
| Bench 3 | Autosub In | Igor Jesus Maciel da Cruz | FWD | 16 | 5.8 | 2.84 | 8.35 | 13.67 | 5.00 | 59.7 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 1.70 | 5.43 | 9.18 | 1.00 | 28.0 | 45.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.08 | 16.01 | 25.73 | 2.00 | 82.4 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 14.0 | 4.87 | 14.66 | 24.75 | 0.00 | 35.6 | 0.0 |
| Captain | Captain | Morgan Rogers | MID | 2 | 7.3 | 5.41 | 14.52 | 22.67 | 1.00 | 106.0 | 90.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.2 | 5.21 | 14.42 | 22.59 | 5.00 | 99.3 | 90.0 |
| XI | XI | Ryan Gravenberch | MID | 12 | 5.6 | 3.93 | 10.67 | 17.02 | 11.00 | 82.8 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Phil Foden
- Effective captain: Phil Foden
- Chip used: none
- Predicted score: 46.15
- Actual score: 36.00
- Transfer: Jurriën Timber -> Reece James (projected gain 0.90, hit 0)
- Autosub: James Tarkowski replaced Mohamed Salah.
- Autosub: Dominic Calvert-Lewin replaced Declan Rice.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.27 | 9.46 | 15.46 | 2.00 | 86.3 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 5.5 | 2.74 | 8.42 | 13.86 | 10.00 | 83.7 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.03 | 11.04 | 17.65 | 2.00 | 92.5 | 90.0 |
| XI | XI | Reece James | DEF | 7 | 5.7 | 4.04 | 10.99 | 17.32 | 1.00 | 86.3 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.67 | 10.70 | 17.60 | 6.00 | 83.3 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.60 | 10.28 | 16.85 | 1.00 | 88.2 | 33.0 |
| Bench 2 | Autosub In | James Tarkowski | DEF | 9 | 5.5 | 3.39 | 10.20 | 16.95 | 9.00 | 84.1 | 90.0 |
| Bench 3 | Autosub In | Dominic Calvert-Lewin | FWD | 11 | 5.8 | 2.92 | 9.46 | 15.93 | 1.00 | 53.7 | 20.0 |
| XI | XI | Igor Jesus Maciel da Cruz | FWD | 16 | 5.8 | 3.08 | 9.28 | 14.92 | 2.00 | 69.5 | 61.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 2.14 | 6.53 | 10.56 | 0.00 | 41.5 | 0.0 |
| Vice Captain | Captain | Phil Foden | MID | 13 | 9.0 | 4.51 | 14.52 | 24.41 | 3.00 | 80.7 | 90.0 |
| Captain | Bench | Mohamed Salah | MID | 12 | 14.0 | 4.59 | 13.71 | 23.15 | 0.00 | 36.6 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.45 | 11.61 | 18.83 | 1.00 | 73.9 | 81.0 |
| XI | Bench | Declan Rice | MID | 1 | 7.2 | 3.71 | 11.58 | 18.83 | 0.00 | 69.2 | 0.0 |
| XI | XI | Ryan Gravenberch | MID | 12 | 5.6 | 3.60 | 10.06 | 16.43 | 5.00 | 81.4 | 90.0 |

## GW20

- Train rows: 175452
- Bank: 0.70 -> 4.40
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Phil Foden
- Effective captain: Bukayo Saka
- Chip used: triple_captain
- Predicted score: 54.78
- Actual score: 32.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.37) beats the best remaining Triple Captain opportunity (6.59).
- Transfer: Mohamed Salah -> Bukayo Saka (projected gain 6.19, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (5.37) beats the best remaining Triple Captain opportunity (6.59).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.49 | 10.18 | 16.42 | 1.00 | 94.2 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 5.5 | 3.06 | 9.13 | 14.89 | 1.00 | 90.3 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.5 | 4.25 | 11.46 | 18.55 | 2.00 | 99.2 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.67 | 11.21 | 18.40 | 1.00 | 61.6 | 50.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 3.86 | 10.86 | 17.37 | 2.00 | 95.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.55 | 10.46 | 17.35 | 1.00 | 86.8 | 90.0 |
| Bench 3 | Bench | Reece James | DEF | 7 | 5.7 | 2.39 | 8.70 | 15.00 | 1.00 | 63.6 | 90.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 11 | 5.8 | 3.81 | 10.77 | 18.08 | 2.00 | 49.3 | 90.0 |
| XI | XI | Igor Jesus Maciel da Cruz | FWD | 16 | 5.8 | 3.02 | 9.21 | 15.72 | 2.00 | 55.2 | 82.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 1.02 | 3.47 | 5.50 | 5.00 | 24.1 | 16.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.9 | 5.23 | 16.12 | 26.48 | 2.00 | 86.7 | 90.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 10.3 | 5.37 | 15.67 | 25.54 | 4.00 | 80.6 | 23.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 4.36 | 12.77 | 20.43 | 5.00 | 102.6 | 90.0 |
| Bench 2 | Bench | Declan Rice | MID | 1 | 7.1 | 2.89 | 10.22 | 18.36 | 17.00 | 30.4 | 90.0 |
| XI | XI | Ryan Gravenberch | MID | 12 | 5.6 | 3.44 | 10.11 | 16.91 | 2.00 | 81.5 | 90.0 |

## GW21

- Train rows: 176242
- Bank: 4.40 -> 1.50
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Declan Rice
- Effective captain: Ollie Watkins
- Chip used: bench_boost
- Predicted score: 62.28
- Actual score: 59.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.55) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Igor Jesus Maciel da Cruz -> Ollie Watkins (projected gain 5.53, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.55) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench Boost | David Raya Martín | GK | 1 | 6.0 | 3.12 | 9.22 | 15.11 | 6.00 | 85.4 | 90.0 |
| XI | XI | Jordan Pickford | GK | 9 | 5.5 | 3.43 | 9.22 | 14.82 | 3.00 | 88.4 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.6 | 4.52 | 11.62 | 17.84 | 4.00 | 93.9 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 3.89 | 10.71 | 17.16 | 6.00 | 91.0 | 90.0 |
| XI | XI | Reece James | DEF | 7 | 5.7 | 3.45 | 10.07 | 16.32 | 1.00 | 80.3 | 25.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.10 | 9.71 | 16.57 | 0.00 | 54.7 | 0.0 |
| Bench 3 | Bench Boost | Virgil van Dijk | DEF | 12 | 5.9 | 2.99 | 9.58 | 16.08 | 6.00 | 83.9 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.7 | 5.55 | 14.42 | 22.94 | 2.00 | 88.9 | 90.0 |
| Bench 2 | Bench Boost | Dominic Calvert-Lewin | FWD | 11 | 5.8 | 3.07 | 10.02 | 16.28 | 8.00 | 61.2 | 86.0 |
| Bench 4 | Bench Boost | Junior Kroupi | FWD | 4 | 4.6 | 1.37 | 4.27 | 6.98 | 7.00 | 27.3 | 63.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.2 | 4.61 | 14.79 | 24.94 | 3.00 | 53.4 | 77.0 |
| XI | XI | Phil Foden | MID | 13 | 8.8 | 4.97 | 14.71 | 24.65 | 2.00 | 82.0 | 72.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.2 | 4.99 | 13.94 | 23.09 | 3.00 | 89.6 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 4.55 | 12.95 | 20.85 | 3.00 | 75.9 | 90.0 |
| XI | XI | Ryan Gravenberch | MID | 12 | 5.6 | 3.13 | 10.03 | 16.24 | 3.00 | 81.5 | 90.0 |