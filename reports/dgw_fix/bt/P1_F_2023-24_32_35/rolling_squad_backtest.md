# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 281.11
- Total actual points: 346.00
- Average predicted points: 70.28
- Average actual points: 86.50
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
- Bank: 100.00 -> 0.80
- Free transfers: 1 -> 2
- Captain: Cole Palmer
- Vice captain: Phil Foden
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 57.22
- Actual score: 55.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Rodrigo Muniz Carvalho replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.12 | 8.76 | 14.28 | 3.00 | 85.3 | 90.0 |
| Bench 1 | Bench | Mark Flekken | GK | 4 | 4.6 | 2.66 | 8.07 | 13.57 | 1.00 | 88.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.05 | 11.38 | 18.63 | 5.00 | 83.0 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 3.52 | 10.45 | 16.79 | 5.00 | 75.3 | 90.0 |
| Bench 3 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.47 | 9.88 | 16.08 | 6.00 | 76.6 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.9 | 3.52 | 9.54 | 14.94 | 11.00 | 73.6 | 90.0 |
| Bench 4 | Bench | Virgil van Dijk | DEF | 11 | 6.6 | 3.15 | 9.51 | 15.65 | 1.00 | 71.5 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.33 | 13.25 | 19.90 | 2.00 | 70.7 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.39 | 11.79 | 19.75 | 2.00 | 71.2 | 90.0 |
| Bench 2 | Autosub In | Rodrigo Muniz Carvalho | FWD | 10 | 4.7 | 3.62 | 10.01 | 15.74 | 2.00 | 64.5 | 85.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.0 | 7.24 | 17.89 | 27.58 | 5.00 | 90.0 | 73.0 |
| Vice Captain | Bench | Phil Foden | MID | 13 | 8.2 | 5.65 | 16.23 | 26.69 | 0.00 | 90.0 | 0.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.1 | 5.49 | 16.22 | 26.36 | 5.00 | 85.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.02 | 14.28 | 23.54 | 1.00 | 90.0 | 53.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.2 | 3.64 | 11.38 | 19.43 | 9.00 | 76.5 | 90.0 |

## GW33

- Train rows: 128527
- Bank: 0.80 -> 1.30
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Luis Díaz
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 53.83
- Actual score: 104.00
- Transfer: Phil Foden -> Luis Díaz (projected gain 3.96, hit 0)
- Autosub: Virgil van Dijk replaced Jarrod Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.8 | 2.89 | 8.50 | 13.80 | 9.00 | 83.1 | 90.0 |
| XI | XI | Mark Flekken | GK | 4 | 4.6 | 2.93 | 8.16 | 13.46 | 7.00 | 81.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.56 | 12.28 | 19.63 | 1.00 | 87.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.23 | 11.30 | 17.60 | 0.00 | 82.0 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 4.05 | 11.21 | 17.75 | 5.00 | 78.8 | 66.0 |
| Bench 2 | Autosub In | Virgil van Dijk | DEF | 11 | 6.6 | 3.78 | 10.42 | 16.55 | 2.00 | 77.9 | 90.0 |
| Bench 3 | Bench | Pedro Porro | DEF | 18 | 5.9 | 3.00 | 9.20 | 14.79 | 0.00 | 72.3 | 48.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.22 | 13.08 | 19.91 | 12.00 | 73.2 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 3.95 | 11.30 | 18.58 | 7.00 | 70.1 | 90.0 |
| Bench 4 | Bench | Rodrigo Muniz Carvalho | FWD | 10 | 4.7 | 2.82 | 8.34 | 13.66 | 2.00 | 56.7 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.0 | 5.86 | 16.33 | 25.13 | 26.00 | 86.2 | 79.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.0 | 4.78 | 14.80 | 24.43 | 1.00 | 78.1 | 57.0 |
| Vice Captain | XI | Luis Díaz | MID | 11 | 7.7 | 5.17 | 14.34 | 22.46 | 2.00 | 81.7 | 65.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.2 | 4.43 | 12.57 | 20.97 | 15.00 | 88.5 | 90.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.8 | 3.79 | 11.11 | 18.74 | 0.00 | 68.6 | 0.0 |

## GW34

- Train rows: 129378
- Bank: 1.30 -> 2.90
- Free transfers: 2 -> 2
- Captain: Dominic Solanke
- Vice captain: Eberechi Eze
- Effective captain: Dominic Solanke
- Chip used: bench_boost
- Predicted score: 93.24
- Actual score: 116.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.41) beats the best remaining Bench Boost opportunity (11.46).
- Chip advisory: triple_captain (0.62): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Jarrod Bowen -> Eberechi Eze (projected gain 5.35, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.41) beats the best remaining Bench Boost opportunity (11.46).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 2.96 | 8.84 | 14.68 | 2.00 | 85.9 | 90.0 |
| Bench 1 | Bench Boost | Mark Flekken | GK | 4 | 4.6 | 2.76 | 7.86 | 12.93 | 2.00 | 78.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 8.75 | 13.31 | 20.75 | 14.00 | 177.3 | 180.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 8.16 | 12.48 | 18.95 | 12.00 | 169.4 | 180.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 7.83 | 12.29 | 19.11 | 26.00 | 153.7 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.6 | 8.05 | 12.10 | 18.61 | 2.00 | 168.5 | 180.0 |
| Bench 3 | Bench Boost | Pedro Porro | DEF | 18 | 5.9 | 0.00 | 7.18 | 12.57 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 9.75 | 14.79 | 23.27 | 8.00 | 180.0 | 176.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 5.00 | 14.58 | 23.02 | 2.00 | 83.2 | 90.0 |
| Bench 2 | Bench Boost | Rodrigo Muniz Carvalho | FWD | 10 | 4.6 | 2.32 | 7.47 | 12.25 | 5.00 | 50.1 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 6.1 | 4.85 | 16.02 | 25.24 | 0.00 | 86.4 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.2 | 5.32 | 14.36 | 23.18 | 18.00 | 90.0 | 90.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 8.75 | 13.61 | 20.63 | 3.00 | 130.9 | 163.0 |
| Vice Captain | XI | Eberechi Eze | MID | 8 | 6.1 | 8.99 | 13.52 | 20.13 | 14.00 | 171.2 | 162.0 |
| Bench 4 | Bench Boost | Son Heung-min | MID | 18 | 10.0 | 0.00 | 12.94 | 22.47 | 0.00 | 0.0 | 0.0 |

## GW35

- Train rows: 130234
- Bank: 2.90 -> 2.80
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Alexander Isak
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 76.83
- Actual score: 71.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (11.75) beats the best remaining Triple Captain opportunity (0.00).
- Chip advisory: triple_captain (0.61): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Mark Flekken -> Jordan Pickford (projected gain 2.51, hit 0)
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (11.75) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.7 | 3.84 | 10.85 | 17.45 | 10.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.8 | 3.03 | 8.37 | 13.91 | 3.00 | 80.9 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 5.21 | 14.89 | 23.73 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 5.02 | 14.13 | 22.41 | 1.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.74 | 13.35 | 20.83 | 1.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.6 | 4.17 | 11.61 | 18.34 | 1.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Pedro Porro | DEF | 18 | 5.8 | 2.96 | 6.61 | 10.97 | 2.00 | 78.8 | 180.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 8.0 | 7.02 | 17.26 | 27.30 | 13.00 | 90.0 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.95 | 13.64 | 21.45 | 2.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Rodrigo Muniz Carvalho | FWD | 10 | 4.5 | 3.14 | 8.76 | 13.42 | 6.00 | 55.8 | 84.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 5.85 | 17.42 | 28.05 | 4.00 | 90.0 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.1 | 8.20 | 14.97 | 24.19 | 8.00 | 108.9 | 180.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 4.62 | 12.85 | 20.13 | 5.00 | 77.9 | 78.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.9 | 6.83 | 12.55 | 20.76 | 9.00 | 102.9 | 180.0 |
| Bench 2 | Bench | Eberechi Eze | MID | 8 | 6.1 | 3.85 | 11.06 | 17.67 | 0.00 | 75.3 | 0.0 |