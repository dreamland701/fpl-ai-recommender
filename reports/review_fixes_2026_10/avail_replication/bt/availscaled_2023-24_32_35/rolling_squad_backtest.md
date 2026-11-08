# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 248.51
- Total actual points: 291.00
- Average predicted points: 62.13
- Average actual points: 72.75
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW31 are included before the first simulated week.
- League-average scores were not available for this run.

## GW32

- Train rows: 127681
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Cole Palmer
- Vice captain: Phil Foden
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 58.88
- Actual score: 50.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Luis Díaz replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.10 | 8.86 | 14.43 | 3.00 | 85.3 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 4.9 | 2.65 | 8.37 | 14.09 | 2.00 | 84.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.09 | 11.75 | 19.24 | 5.00 | 85.9 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 3.76 | 11.21 | 18.00 | 5.00 | 80.9 | 90.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 11 | 6.6 | 3.40 | 10.35 | 17.02 | 1.00 | 78.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.9 | 3.81 | 10.23 | 16.02 | 11.00 | 79.8 | 90.0 |
| Bench 4 | Bench | Alfie Doughty | DEF | 12 | 4.6 | 3.14 | 9.27 | 15.63 | 2.00 | 76.2 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 5.08 | 14.53 | 21.83 | 2.00 | 82.3 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.84 | 12.97 | 21.72 | 2.00 | 79.3 | 90.0 |
| XI | XI | Ivan Toney | FWD | 4 | 8.1 | 4.30 | 12.44 | 20.26 | 1.00 | 88.3 | 9.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.0 | 7.44 | 17.89 | 27.58 | 5.00 | 95.3 | 73.0 |
| Vice Captain | Bench | Phil Foden | MID | 13 | 8.2 | 5.67 | 16.23 | 26.69 | 0.00 | 95.3 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.99 | 14.28 | 23.54 | 1.00 | 95.1 | 53.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.36 | 13.24 | 22.07 | 3.00 | 80.2 | 88.0 |
| Bench 2 | Autosub In | Luis Díaz | MID | 11 | 7.6 | 4.08 | 12.06 | 20.37 | 7.00 | 70.5 | 90.0 |

## GW33

- Train rows: 128527
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Darwin Núñez Ribeiro
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 55.22
- Actual score: 76.00
- Transfer: Alexander Isak -> Darwin Núñez Ribeiro (projected gain 2.24, hit 0)
- Autosub: Pedro Porro replaced Phil Foden.
- Autosub: Alfie Doughty replaced Ivan Toney.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.8 | 2.94 | 8.78 | 14.24 | 9.00 | 84.9 | 90.0 |
| XI | XI | André Onana | GK | 14 | 4.9 | 3.03 | 8.68 | 14.22 | 2.00 | 89.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.56 | 12.40 | 19.82 | 1.00 | 90.0 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 4.24 | 11.72 | 18.55 | 5.00 | 83.6 | 66.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.6 | 4.02 | 11.00 | 17.48 | 2.00 | 85.3 | 90.0 |
| Bench 3 | Autosub In | Pedro Porro | DEF | 18 | 5.9 | 3.17 | 9.77 | 15.71 | 0.00 | 77.3 | 48.0 |
| Bench 4 | Autosub In | Alfie Doughty | DEF | 12 | 4.6 | 2.51 | 8.36 | 13.93 | 0.00 | 78.3 | 90.0 |
| Vice Captain | XI | Darwin Núñez Ribeiro | FWD | 11 | 7.7 | 5.06 | 13.76 | 21.31 | 2.00 | 46.8 | 65.0 |
| XI | Bench | Ivan Toney | FWD | 4 | 8.1 | 4.63 | 12.85 | 21.43 | 0.00 | 71.7 | 0.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.09 | 12.04 | 19.79 | 7.00 | 67.9 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.0 | 6.10 | 16.33 | 25.13 | 26.00 | 88.7 | 79.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 4.58 | 14.02 | 24.03 | 0.00 | 23.5 | 0.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.85 | 13.73 | 22.24 | 3.00 | 77.9 | 78.0 |
| Bench 2 | Bench | Jarrod Bowen | MID | 19 | 7.8 | 3.63 | 11.58 | 19.54 | 0.00 | 43.3 | 0.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.6 | 3.95 | 10.56 | 16.54 | 2.00 | 65.4 | 65.0 |

## GW34

- Train rows: 129378
- Bank: 0.20 -> 0.70
- Free transfers: 2 -> 2
- Captain: Martin Ødegaard
- Vice captain: William Saliba
- Effective captain: Martin Ødegaard
- Chip used: bench_boost
- Predicted score: 67.44
- Actual score: 99.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (16.16) beats the best remaining Bench Boost opportunity (14.89).
- Transfer: Benjamin White -> Gabriel dos Santos Magalhães (projected gain 7.30, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (16.16) beats the best remaining Bench Boost opportunity (14.89).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench Boost | Bernd Leno | GK | 10 | 4.8 | 2.92 | 8.93 | 14.84 | 2.00 | 86.3 | 90.0 |
| XI | XI | André Onana | GK | 14 | 4.9 | 3.21 | 8.76 | 14.30 | 1.00 | 88.8 | 90.0 |
| Vice Captain | XI | William Saliba | DEF | 1 | 5.8 | 6.61 | 15.96 | 24.89 | 14.00 | 137.2 | 180.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.4 | 6.48 | 15.25 | 23.15 | 12.00 | 133.9 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.6 | 3.61 | 8.31 | 12.78 | 2.00 | 95.0 | 180.0 |
| Bench 2 | Bench Boost | Alfie Doughty | DEF | 12 | 4.5 | 2.85 | 7.98 | 12.98 | -1.00 | 77.6 | 90.0 |
| Bench 4 | Bench Boost | Pedro Porro | DEF | 18 | 5.9 | 1.36 | 5.14 | 8.99 | 0.00 | 32.3 | 0.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.21 | 10.28 | 16.18 | 8.00 | 104.0 | 176.0 |
| Bench 3 | Bench Boost | Ivan Toney | FWD | 4 | 8.0 | 2.70 | 8.95 | 15.98 | 0.00 | 15.7 | 0.0 |
| XI | XI | Darwin Núñez Ribeiro | FWD | 11 | 7.7 | 3.66 | 8.65 | 13.13 | 2.00 | 73.0 | 106.0 |
| Captain | Captain | Martin Ødegaard | MID | 1 | 8.5 | 7.24 | 18.04 | 28.43 | 20.00 | 94.9 | 180.0 |
| XI | XI | Cole Palmer | MID | 7 | 6.1 | 4.80 | 16.02 | 25.24 | 0.00 | 72.3 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 8.2 | 3.35 | 12.22 | 22.02 | 16.00 | 16.3 | 71.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.7 | 3.30 | 11.94 | 21.74 | 0.00 | 52.6 | 0.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 3.93 | 9.31 | 14.12 | 3.00 | 77.0 | 163.0 |

## GW35

- Train rows: 130234
- Bank: 0.70 -> 0.40
- Free transfers: 2 -> 2
- Captain: Alexander Isak
- Vice captain: Martin Ødegaard
- Effective captain: Alexander Isak
- Chip used: triple_captain
- Predicted score: 66.97
- Actual score: 66.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (10.70) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Ivan Toney -> Alexander Isak (projected gain 11.42, hit 0)
- Chip used: Triple Captain on Alexander Isak. Optimizer chose Triple Captain here because the current estimated captain upside (10.70) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Alfie Doughty replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.9 | 3.17 | 8.76 | 14.30 | 4.00 | 87.1 | 90.0 |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.8 | 3.10 | 8.65 | 14.37 | 3.00 | 84.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.86 | 14.13 | 22.41 | 1.00 | 114.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.4 | 4.67 | 13.35 | 20.83 | 1.00 | 99.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.6 | 4.03 | 11.61 | 18.34 | 1.00 | 100.8 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 3.44 | 9.25 | 15.36 | 2.00 | 65.0 | 180.0 |
| Bench 2 | Autosub In | Alfie Doughty | DEF | 12 | 4.5 | 2.59 | 7.41 | 12.23 | 1.00 | 78.2 | 87.0 |
| Captain | Captain | Alexander Isak | FWD | 15 | 8.2 | 7.50 | 17.26 | 27.30 | 13.00 | 111.9 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.69 | 13.64 | 21.45 | 2.00 | 82.9 | 90.0 |
| Bench 4 | Bench | Darwin Núñez Ribeiro | FWD | 11 | 7.7 | 2.06 | 6.23 | 10.08 | 1.00 | 31.7 | 11.0 |
| Vice Captain | XI | Martin Ødegaard | MID | 1 | 8.5 | 6.03 | 17.51 | 28.00 | 2.00 | 101.2 | 88.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 5.75 | 16.58 | 26.96 | 0.00 | 51.2 | 0.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 4.48 | 12.85 | 20.13 | 5.00 | 55.0 | 78.0 |
| Bench 3 | Bench | Jarrod Bowen | MID | 19 | 7.7 | 2.42 | 9.72 | 17.67 | 13.00 | 19.2 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 6.1 | 3.35 | 9.55 | 15.42 | 8.00 | 59.4 | 180.0 |