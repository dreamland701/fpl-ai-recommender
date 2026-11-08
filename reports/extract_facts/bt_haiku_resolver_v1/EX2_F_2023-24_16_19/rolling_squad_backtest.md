# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 235.47
- Total actual points: 206.00
- Average predicted points: 58.87
- Average actual points: 51.50
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW15 are included before the first simulated week.
- League-average scores were not available for this run.

## GW16

- Train rows: 114791
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 61.32
- Actual score: 56.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Auston Trusty replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.34 | 9.23 | 15.65 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Tom McGill | GK | 5 | 3.9 | 0.46 | 0.76 | 1.12 | 0.00 | 8.7 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.99 | 14.66 | 24.03 | -1.00 | 90.0 | 85.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.73 | 14.37 | 23.74 | 4.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 3.46 | 10.60 | 17.31 | 5.00 | 76.0 | 90.0 |
| Bench 3 | Bench | Teden Mengi | DEF | 12 | 3.9 | 1.84 | 6.34 | 10.64 | 1.00 | 75.6 | 90.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.37 | 6.25 | 10.15 | 5.00 | 76.1 | 90.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.0 | 8.31 | 24.47 | 39.69 | 0.00 | 90.0 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.67 | 10.10 | 16.30 | 9.00 | 80.5 | 90.0 |
| Bench 4 | Bench | William Osula | FWD | 17 | 4.3 | 1.80 | 4.45 | 6.67 | 0.00 | 40.1 | 52.0 |
| Vice Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.77 | 20.12 | 33.87 | 13.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 5.66 | 17.24 | 27.82 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.11 | 12.34 | 19.67 | 2.00 | 79.5 | 73.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.7 | 4.23 | 11.60 | 18.37 | 2.00 | 89.6 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.75 | 11.37 | 19.10 | 1.00 | 82.5 | 90.0 |

## GW17

- Train rows: 115549
- Bank: 0.00 -> 1.40
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Mohamed Salah
- Effective captain: Bukayo Saka
- Chip used: bench_boost
- Predicted score: 58.82
- Actual score: 69.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (2.18) beats the best remaining Bench Boost opportunity (4.97).
- Transfer: Kieran Trippier -> William Saliba (projected gain 2.54, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (2.18) beats the best remaining Bench Boost opportunity (4.97).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 2.59 | 8.72 | 14.32 | 10.00 | 85.8 | 90.0 |
| Bench 1 | Bench Boost | Tom McGill | GK | 5 | 3.9 | 0.00 | 0.49 | 0.63 | 0.00 | 9.9 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.59 | 14.71 | 24.15 | 9.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 4.58 | 13.03 | 20.97 | 8.00 | 87.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 4.09 | 11.53 | 18.13 | 7.00 | 85.2 | 90.0 |
| Bench 2 | Bench Boost | Auston Trusty | DEF | 17 | 3.9 | 2.26 | 6.68 | 10.62 | 1.00 | 77.1 | 90.0 |
| Bench 4 | Bench Boost | Teden Mengi | DEF | 12 | 3.9 | 0.00 | 5.41 | 9.31 | 0.00 | 0.0 | 0.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.0 | 2.92 | 10.94 | 22.50 | 0.00 | 0.8 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.51 | 10.73 | 17.27 | 2.00 | 82.9 | 90.0 |
| Bench 3 | Bench Boost | William Osula | FWD | 17 | 4.3 | 1.50 | 4.48 | 6.81 | 1.00 | 38.9 | 32.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.1 | 7.17 | 22.09 | 35.81 | 3.00 | 90.0 | 90.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 8.9 | 7.44 | 19.60 | 32.65 | 3.00 | 90.0 | 88.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.05 | 11.32 | 19.49 | 6.00 | 63.2 | 83.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.66 | 10.49 | 17.35 | 14.00 | 70.8 | 90.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.7 | 3.03 | 9.42 | 15.40 | 2.00 | 71.5 | 90.0 |

## GW18

- Train rows: 116314
- Bank: 1.40 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 52.31
- Actual score: 33.00
- Transfer: Teden Mengi -> Alexandre Moreno Lopera (projected gain 3.43, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.34 | 10.14 | 16.89 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Tom McGill | GK | 5 | 3.9 | 0.34 | 0.78 | 1.25 | 0.00 | 9.5 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.18 | 13.93 | 23.35 | 5.00 | 81.8 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 4.22 | 12.40 | 19.23 | 2.00 | 76.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 3.48 | 10.85 | 17.36 | 2.00 | 86.6 | 90.0 |
| XI | XI | Alexandre Moreno Lopera | DEF | 2 | 5.0 | 3.98 | 9.71 | 14.49 | 1.00 | 64.2 | 16.0 |
| Bench 2 | Bench | Auston Trusty | DEF | 17 | 3.9 | 1.93 | 6.35 | 10.44 | 1.00 | 76.7 | 90.0 |
| Bench 4 | Bench | Erling Haaland | FWD | 13 | 14.0 | 0.00 | 14.75 | 27.09 | 0.00 | 0.0 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.57 | 10.53 | 17.09 | 1.00 | 75.0 | 85.0 |
| Bench 3 | Bench | William Osula | FWD | 17 | 4.3 | 1.22 | 4.09 | 6.64 | 0.00 | 35.5 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.31 | 20.27 | 33.41 | 7.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 5.71 | 17.85 | 28.38 | 1.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 4.67 | 13.21 | 20.98 | 1.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.38 | 10.30 | 16.97 | 2.00 | 57.7 | 90.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.7 | 3.17 | 9.48 | 16.26 | 2.00 | 73.2 | 90.0 |

## GW19

- Train rows: 117083
- Bank: 0.30 -> 0.90
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 63.02
- Actual score: 48.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.36) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Cole Palmer -> Scott McTominay (projected gain 3.78, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.36) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Auston Trusty replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.52 | 9.48 | 16.79 | 1.00 | 88.7 | 90.0 |
| Bench 1 | Bench | Tom McGill | GK | 5 | 3.9 | 0.33 | 0.79 | 1.36 | 0.00 | 11.3 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.2 | 4.95 | 15.58 | 25.34 | 8.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 3.85 | 11.79 | 18.85 | 5.00 | 78.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 4.15 | 11.32 | 18.02 | 1.00 | 88.7 | 90.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.49 | 6.88 | 10.96 | 1.00 | 78.2 | 90.0 |
| Bench 4 | Bench | Alexandre Moreno Lopera | DEF | 2 | 5.0 | 1.19 | 4.68 | 7.52 | 0.00 | 30.3 | 40.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 13.9 | 3.96 | 11.39 | 22.61 | 0.00 | 25.4 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.7 | 3.13 | 9.65 | 15.81 | 5.00 | 67.6 | 90.0 |
| Bench 3 | Bench | William Osula | FWD | 17 | 4.3 | 1.22 | 3.13 | 5.24 | 1.00 | 25.7 | 4.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.2 | 7.36 | 20.93 | 35.83 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 6.08 | 17.26 | 27.79 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.63 | 12.68 | 20.80 | 1.00 | 79.3 | 90.0 |
| XI | XI | Scott McTominay | MID | 14 | 4.9 | 3.57 | 10.64 | 17.77 | 1.00 | 88.9 | 9.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.7 | 3.11 | 9.16 | 14.79 | 14.00 | 74.9 | 45.0 |