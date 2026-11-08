# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW17
- Simulated weeks: GW18-GW21
- Total predicted points: 234.70
- Total actual points: 173.00
- Average predicted points: 58.68
- Average actual points: 43.25
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
- Vice captain: Mohamed Salah
- Effective captain: Morgan Rogers
- Chip used: none
- Predicted score: 59.29
- Actual score: 40.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Joško Gvardiol replaced Jurriën Timber.
- Autosub: Wilson Isidor replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.81 | 11.03 | 17.91 | 2.00 | 89.5 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 5.5 | 3.62 | 10.02 | 16.23 | 6.00 | 88.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.10 | 13.76 | 21.59 | 2.00 | 96.2 | 90.0 |
| XI | Bench | Jurriën Timber | DEF | 1 | 6.5 | 4.66 | 12.58 | 20.13 | 0.00 | 90.9 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.11 | 11.93 | 19.02 | 2.00 | 80.5 | 90.0 |
| XI | XI | Ibrahima Konaté | DEF | 12 | 5.4 | 4.15 | 11.69 | 18.55 | 2.00 | 82.8 | 90.0 |
| Bench 2 | Autosub In | Joško Gvardiol | DEF | 13 | 6.0 | 3.97 | 11.67 | 19.26 | 8.00 | 82.4 | 90.0 |
| XI | XI | Zian Flemming | FWD | 3 | 5.3 | 3.24 | 9.54 | 15.77 | 1.00 | 61.1 | 2.0 |
| Bench 3 | Autosub In | Wilson Isidor | FWD | 17 | 5.4 | 2.92 | 8.09 | 13.03 | 1.00 | 25.0 | 22.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 1.92 | 6.10 | 10.28 | 1.00 | 17.0 | 45.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.84 | 18.32 | 29.42 | 2.00 | 83.4 | 90.0 |
| Vice Captain | Bench | Mohamed Salah | MID | 12 | 14.0 | 5.88 | 17.72 | 29.93 | 0.00 | 30.6 | 0.0 |
| Captain | Captain | Morgan Rogers | MID | 2 | 7.3 | 6.02 | 16.29 | 25.50 | 1.00 | 106.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 5.83 | 16.24 | 25.52 | 5.00 | 99.3 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.6 | 4.64 | 13.71 | 22.15 | 13.00 | 72.2 | 88.0 |

## GW19

- Train rows: 174672
- Bank: 0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Rayan Cherki
- Effective captain: Rayan Cherki
- Chip used: none
- Predicted score: 53.93
- Actual score: 34.00
- Transfer: Jurriën Timber -> Reece James (projected gain 2.91, hit 0)
- Autosub: Ibrahima Konaté replaced Mohamed Salah.
- Autosub: Wilson Isidor replaced Declan Rice.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.74 | 10.81 | 17.62 | 2.00 | 87.3 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 5.5 | 3.16 | 9.63 | 15.79 | 10.00 | 86.7 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.61 | 12.66 | 20.21 | 2.00 | 92.5 | 90.0 |
| XI | XI | Reece James | DEF | 7 | 5.7 | 4.55 | 12.40 | 19.54 | 1.00 | 90.3 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.20 | 12.20 | 20.08 | 6.00 | 84.3 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.12 | 11.82 | 19.30 | 1.00 | 89.2 | 33.0 |
| Bench 2 | Autosub In | Ibrahima Konaté | DEF | 12 | 5.4 | 3.37 | 9.63 | 15.73 | 7.00 | 80.4 | 90.0 |
| Bench 3 | Bench | Zian Flemming | FWD | 3 | 5.3 | 2.33 | 7.87 | 13.54 | 0.00 | 26.9 | 0.0 |
| XI | Bench | Junior Kroupi | FWD | 4 | 4.6 | 2.49 | 7.58 | 12.25 | 0.00 | 29.5 | 0.0 |
| Bench 4 | Autosub In | Wilson Isidor | FWD | 17 | 5.4 | 1.53 | 5.14 | 8.75 | 1.00 | 31.2 | 32.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.24 | 16.71 | 27.94 | 3.00 | 80.7 | 90.0 |
| Captain | Bench | Mohamed Salah | MID | 12 | 14.0 | 5.59 | 16.67 | 28.15 | 0.00 | 54.6 | 0.0 |
| Vice Captain | Captain | Rayan Cherki | MID | 13 | 6.6 | 5.44 | 14.97 | 23.99 | 5.00 | 94.6 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 4.02 | 13.42 | 21.80 | 1.00 | 76.9 | 81.0 |
| XI | Bench | Declan Rice | MID | 1 | 7.2 | 4.32 | 13.41 | 21.82 | 0.00 | 72.2 | 0.0 |

## GW20

- Train rows: 175452
- Bank: 0.70 -> 0.10
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Rayan Cherki
- Effective captain: Phil Foden
- Chip used: triple_captain
- Predicted score: 57.93
- Actual score: 41.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.94) beats the best remaining Triple Captain opportunity (7.29).
- Transfer: Zian Flemming -> Dominic Calvert-Lewin (projected gain 9.29, hit 0)
- Chip used: Triple Captain on Phil Foden. Optimizer chose Triple Captain here because the current estimated captain upside (5.94) beats the best remaining Triple Captain opportunity (7.29).
- Autosub: Reece James replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.89 | 11.32 | 18.24 | 1.00 | 95.2 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 5.5 | 3.42 | 10.11 | 16.43 | 1.00 | 92.3 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.15 | 12.69 | 20.84 | 1.00 | 71.6 | 50.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.40 | 12.47 | 19.94 | 2.00 | 93.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.05 | 11.86 | 19.64 | 1.00 | 87.8 | 90.0 |
| XI | XI | Ibrahima Konaté | DEF | 12 | 5.4 | 3.37 | 10.15 | 16.89 | 1.00 | 83.8 | 90.0 |
| Bench 2 | Autosub In | Reece James | DEF | 7 | 5.7 | 2.71 | 9.89 | 17.04 | 1.00 | 72.6 | 90.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 11 | 5.9 | 4.36 | 12.31 | 20.69 | 2.00 | 39.3 | 90.0 |
| Bench 3 | Bench | Wilson Isidor | FWD | 17 | 5.3 | 1.18 | 3.69 | 6.23 | 0.00 | 24.7 | 0.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 1.02 | 3.47 | 5.50 | 5.00 | 24.1 | 16.0 |
| Captain | Captain | Phil Foden | MID | 13 | 8.9 | 5.94 | 18.20 | 29.86 | 2.00 | 88.7 | 90.0 |
| Vice Captain | XI | Rayan Cherki | MID | 13 | 6.7 | 5.13 | 15.68 | 25.18 | 4.00 | 76.5 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 4.60 | 12.58 | 19.83 | 5.00 | 82.6 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.1 | 3.27 | 11.79 | 21.29 | 17.00 | 46.4 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 14.0 | 2.89 | 9.52 | 16.78 | 0.00 | 23.0 | 0.0 |

## GW21

- Train rows: 176242
- Bank: 0.10 -> 3.90
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Rayan Cherki
- Effective captain: Phil Foden
- Chip used: bench_boost
- Predicted score: 63.56
- Actual score: 58.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.04) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Mohamed Salah -> Bukayo Saka (projected gain 6.94, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.04) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench Boost | David Raya Martín | GK | 1 | 6.0 | 3.54 | 10.42 | 17.05 | 6.00 | 87.4 | 90.0 |
| XI | XI | Jordan Pickford | GK | 9 | 5.5 | 3.74 | 10.07 | 16.16 | 3.00 | 91.4 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.42 | 12.21 | 19.59 | 6.00 | 90.0 | 90.0 |
| XI | XI | Reece James | DEF | 7 | 5.7 | 3.87 | 11.30 | 18.30 | 1.00 | 85.3 | 25.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.54 | 11.13 | 19.02 | 0.00 | 64.7 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.38 | 10.81 | 18.12 | 6.00 | 85.9 | 90.0 |
| Bench 2 | Bench Boost | Ibrahima Konaté | DEF | 12 | 5.4 | 3.05 | 9.95 | 16.81 | 7.00 | 85.3 | 90.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 11 | 5.9 | 3.50 | 11.43 | 18.57 | 8.00 | 60.2 | 86.0 |
| Bench 3 | Bench Boost | Junior Kroupi | FWD | 4 | 4.6 | 1.37 | 4.27 | 6.98 | 7.00 | 27.3 | 63.0 |
| Bench 4 | Bench Boost | Wilson Isidor | FWD | 17 | 5.3 | 1.08 | 3.50 | 5.85 | 0.00 | 21.9 | 0.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.2 | 5.21 | 16.84 | 28.46 | 3.00 | 65.4 | 77.0 |
| Captain | Captain | Phil Foden | MID | 13 | 8.8 | 5.64 | 16.63 | 27.80 | 2.00 | 85.0 | 72.0 |
| Vice Captain | XI | Rayan Cherki | MID | 13 | 6.7 | 5.24 | 15.14 | 24.16 | 1.00 | 86.0 | 17.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 5.11 | 14.63 | 23.55 | 3.00 | 79.9 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 5.22 | 14.63 | 24.26 | 3.00 | 94.6 | 90.0 |