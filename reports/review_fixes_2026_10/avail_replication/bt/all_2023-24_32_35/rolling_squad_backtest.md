# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 201.59
- Total actual points: 292.00
- Average predicted points: 50.40
- Average actual points: 73.00
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
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Cole Palmer
- Vice captain: Phil Foden
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 48.55
- Actual score: 44.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Rodrigo Muniz Carvalho replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 2.66 | 7.76 | 12.18 | 3.00 | 85.3 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 4.9 | 2.33 | 6.61 | 11.38 | 2.00 | 84.0 | 90.0 |
| Bench 3 | Bench | William Saliba | DEF | 1 | 5.8 | 2.56 | 9.28 | 15.53 | 5.00 | 85.9 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 2.90 | 9.15 | 14.79 | 5.00 | 80.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.9 | 3.05 | 8.24 | 12.34 | 11.00 | 79.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.6 | 2.83 | 8.11 | 13.05 | 1.00 | 78.0 | 90.0 |
| Bench 4 | Bench | Alfie Doughty | DEF | 12 | 4.6 | 2.56 | 7.73 | 12.81 | 2.00 | 76.2 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.23 | 11.45 | 16.80 | 2.00 | 82.3 | 90.0 |
| XI | XI | Ivan Toney | FWD | 4 | 8.1 | 3.53 | 10.64 | 17.44 | 1.00 | 88.3 | 9.0 |
| Bench 2 | Autosub In | Rodrigo Muniz Carvalho | FWD | 10 | 4.7 | 2.88 | 8.91 | 13.74 | 2.00 | 62.5 | 85.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.0 | 6.14 | 15.89 | 24.48 | 5.00 | 95.3 | 73.0 |
| Vice Captain | Bench | Phil Foden | MID | 13 | 8.2 | 4.87 | 14.43 | 23.09 | 0.00 | 95.3 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.19 | 12.68 | 20.64 | 1.00 | 95.1 | 53.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.1 | 4.33 | 12.22 | 20.36 | 5.00 | 64.9 | 90.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 3.67 | 11.25 | 18.59 | 3.00 | 80.2 | 88.0 |

## GW33

- Train rows: 128527
- Bank: 0.10 -> 1.00
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Martin Ødegaard
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 43.31
- Actual score: 87.00
- Transfer: Ivan Toney -> Dominic Solanke (projected gain 1.49, hit 0)
- Autosub: Pedro Porro replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.9 | 2.70 | 7.39 | 11.98 | 2.00 | 89.7 | 90.0 |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.8 | 2.55 | 7.30 | 11.70 | 9.00 | 84.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 3.71 | 10.98 | 17.63 | 1.00 | 90.0 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 3.36 | 9.91 | 15.25 | 5.00 | 83.6 | 66.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.6 | 3.30 | 8.92 | 13.95 | 2.00 | 85.3 | 90.0 |
| Bench 4 | Bench | Alfie Doughty | DEF | 12 | 4.6 | 2.17 | 6.78 | 11.64 | 0.00 | 78.3 | 90.0 |
| Bench 3 | Autosub In | Pedro Porro | DEF | 18 | 5.9 | 2.18 | 6.60 | 10.69 | 0.00 | 77.3 | 48.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 3.12 | 11.28 | 17.51 | 12.00 | 56.2 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 3.04 | 10.00 | 16.48 | 7.00 | 67.9 | 90.0 |
| XI | XI | Rodrigo Muniz Carvalho | FWD | 10 | 4.7 | 2.28 | 7.24 | 11.66 | 2.00 | 62.5 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.0 | 5.90 | 15.33 | 23.23 | 26.00 | 88.7 | 79.0 |
| Vice Captain | XI | Martin Ødegaard | MID | 1 | 8.5 | 3.74 | 11.55 | 18.32 | 3.00 | 77.9 | 78.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.0 | 3.55 | 10.80 | 18.43 | 1.00 | 56.4 | 57.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 2.70 | 9.11 | 15.45 | 0.00 | 23.5 | 0.0 |
| Bench 2 | Bench | Jarrod Bowen | MID | 19 | 7.8 | 2.18 | 9.01 | 15.74 | 0.00 | 43.3 | 0.0 |

## GW34

- Train rows: 129378
- Bank: 1.00 -> 1.40
- Free transfers: 2 -> 2
- Captain: Luis Díaz
- Vice captain: Martin Ødegaard
- Effective captain: Luis Díaz
- Chip used: bench_boost
- Predicted score: 51.81
- Actual score: 85.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (12.84) beats the best remaining Bench Boost opportunity (13.54).
- Transfer: Phil Foden -> Luis Díaz (projected gain 3.19, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (12.84) beats the best remaining Bench Boost opportunity (13.54).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.9 | 2.78 | 7.67 | 12.06 | 1.00 | 88.8 | 90.0 |
| Bench 1 | Bench Boost | Bernd Leno | GK | 10 | 4.8 | 1.79 | 5.84 | 9.88 | 2.00 | 86.3 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.31 | 11.01 | 17.65 | 14.00 | 137.2 | 180.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 3.44 | 8.69 | 14.01 | 26.00 | 86.4 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.6 | 3.65 | 8.50 | 13.61 | 2.00 | 95.0 | 180.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.5 | 2.39 | 6.52 | 10.33 | -1.00 | 77.6 | 90.0 |
| Bench 4 | Bench Boost | Pedro Porro | DEF | 18 | 5.9 | 1.40 | 4.58 | 8.37 | 0.00 | 32.3 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 3.71 | 11.78 | 19.02 | 2.00 | 86.8 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.35 | 11.19 | 18.17 | 8.00 | 104.0 | 176.0 |
| Bench 3 | Bench Boost | Rodrigo Muniz Carvalho | FWD | 10 | 4.6 | 1.71 | 6.47 | 10.25 | 5.00 | 35.5 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 6.1 | 3.40 | 12.02 | 19.24 | 0.00 | 72.3 | 0.0 |
| Vice Captain | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.60 | 11.61 | 19.20 | 20.00 | 94.9 | 180.0 |
| Captain | Captain | Luis Díaz | MID | 11 | 7.8 | 4.63 | 11.11 | 16.73 | 3.00 | 77.0 | 163.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.0 | 2.95 | 9.84 | 17.97 | 0.00 | 42.3 | 0.0 |
| Bench 2 | Bench Boost | Jarrod Bowen | MID | 19 | 7.7 | 2.06 | 7.53 | 12.93 | 0.00 | 52.6 | 0.0 |

## GW35

- Train rows: 130234
- Bank: 1.40 -> 0.70
- Free transfers: 2 -> 2
- Captain: Alexander Isak
- Vice captain: Martin Ødegaard
- Effective captain: Alexander Isak
- Chip used: triple_captain
- Predicted score: 57.92
- Actual score: 76.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (10.25) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Jarrod Bowen -> Bruno Borges Fernandes (projected gain 6.16, hit 0)
- Chip used: Triple Captain on Alexander Isak. Optimizer chose Triple Captain here because the current estimated captain upside (10.25) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.9 | 2.77 | 7.49 | 11.76 | 4.00 | 87.1 | 90.0 |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.8 | 2.60 | 7.17 | 11.01 | 3.00 | 84.5 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 3.99 | 11.59 | 18.73 | 1.00 | 110.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 3.76 | 11.53 | 18.41 | 1.00 | 114.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.6 | 3.23 | 10.11 | 15.14 | 1.00 | 100.8 | 90.0 |
| Bench 3 | Bench | Alfie Doughty | DEF | 12 | 4.5 | 2.27 | 5.87 | 9.06 | 1.00 | 78.2 | 87.0 |
| Bench 4 | Bench | Pedro Porro | DEF | 18 | 5.8 | 2.16 | 5.81 | 9.37 | 2.00 | 65.0 | 180.0 |
| Captain | Captain | Alexander Isak | FWD | 15 | 8.0 | 6.70 | 15.36 | 24.10 | 13.00 | 111.9 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 3.69 | 10.64 | 16.45 | 2.00 | 82.9 | 90.0 |
| Bench 2 | Bench | Rodrigo Muniz Carvalho | FWD | 10 | 4.5 | 2.78 | 7.36 | 10.52 | 6.00 | 62.9 | 84.0 |
| Vice Captain | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.83 | 14.51 | 23.00 | 2.00 | 101.2 | 88.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.22 | 13.42 | 22.05 | 4.00 | 91.2 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 6.1 | 3.95 | 12.47 | 20.09 | 8.00 | 59.4 | 180.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.9 | 4.10 | 11.25 | 17.76 | 9.00 | 76.8 | 180.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.8 | 3.28 | 8.85 | 14.13 | 5.00 | 55.0 | 78.0 |