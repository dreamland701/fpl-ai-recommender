# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 227.52
- Total actual points: 348.00
- Average predicted points: 56.88
- Average actual points: 87.00
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
- Predicted score: 52.70
- Actual score: 56.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Bruno Borges Fernandes replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.8 | 2.79 | 7.98 | 13.01 | 3.00 | 84.3 | 90.0 |
| XI | XI | Guglielmo Vicario | GK | 18 | 5.3 | 2.85 | 7.82 | 12.57 | 4.00 | 81.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 3.69 | 10.57 | 17.31 | 5.00 | 82.9 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 3.39 | 10.12 | 16.25 | 5.00 | 74.9 | 90.0 |
| Bench 3 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.26 | 9.41 | 15.32 | 6.00 | 76.6 | 90.0 |
| Bench 4 | Bench | Virgil van Dijk | DEF | 11 | 6.6 | 3.08 | 9.36 | 15.41 | 1.00 | 72.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.9 | 3.44 | 9.24 | 14.48 | 11.00 | 74.8 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.62 | 13.23 | 19.87 | 2.00 | 74.3 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.39 | 11.74 | 19.67 | 2.00 | 72.3 | 90.0 |
| XI | XI | Rodrigo Muniz Carvalho | FWD | 10 | 4.7 | 3.44 | 9.34 | 14.68 | 2.00 | 63.5 | 85.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.0 | 6.76 | 16.06 | 24.77 | 5.00 | 96.3 | 73.0 |
| Vice Captain | Bench | Phil Foden | MID | 13 | 8.2 | 5.31 | 15.21 | 25.00 | 0.00 | 92.3 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.50 | 12.88 | 21.28 | 1.00 | 96.1 | 53.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.1 | 3.55 | 12.22 | 20.36 | 5.00 | 84.9 | 90.0 |
| Bench 2 | Autosub In | Bruno Borges Fernandes | MID | 14 | 8.2 | 3.38 | 11.01 | 18.83 | 9.00 | 74.0 | 90.0 |

## GW33

- Train rows: 128527
- Bank: 0.10 -> 0.30
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Darwin Núñez Ribeiro
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 48.73
- Actual score: 94.00
- Transfer: Alexander Isak -> Darwin Núñez Ribeiro (projected gain 1.67, hit 0)
- Autosub: Son Heung-min replaced Phil Foden.
- Autosub: Pedro Porro replaced Jarrod Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 2.65 | 7.94 | 12.90 | 9.00 | 82.9 | 90.0 |
| Bench 1 | Bench | Guglielmo Vicario | GK | 18 | 5.3 | 2.30 | 7.47 | 12.38 | 0.00 | 77.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.15 | 11.26 | 18.00 | 1.00 | 89.0 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 3.84 | 10.62 | 16.82 | 5.00 | 79.6 | 66.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.01 | 10.56 | 16.44 | 0.00 | 84.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.6 | 3.66 | 10.02 | 15.93 | 2.00 | 80.3 | 90.0 |
| Bench 3 | Autosub In | Pedro Porro | DEF | 18 | 5.9 | 2.84 | 8.80 | 14.18 | 0.00 | 72.3 | 48.0 |
| Vice Captain | XI | Darwin Núñez Ribeiro | FWD | 11 | 7.7 | 4.59 | 12.45 | 19.29 | 2.00 | 60.8 | 65.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 3.67 | 10.81 | 17.78 | 7.00 | 68.9 | 90.0 |
| Bench 4 | Bench | Rodrigo Muniz Carvalho | FWD | 10 | 4.7 | 2.78 | 8.34 | 13.66 | 2.00 | 54.5 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.0 | 5.48 | 14.63 | 22.53 | 26.00 | 89.7 | 79.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 4.06 | 12.36 | 21.13 | 0.00 | 41.5 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.2 | 3.99 | 11.52 | 19.28 | 15.00 | 86.9 | 90.0 |
| Bench 2 | Autosub In | Son Heung-min | MID | 18 | 10.0 | 2.89 | 10.80 | 18.43 | 1.00 | 76.4 | 57.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.8 | 3.17 | 10.23 | 17.31 | 0.00 | 63.3 | 0.0 |

## GW34

- Train rows: 129378
- Bank: 0.30 -> 2.40
- Free transfers: 2 -> 2
- Captain: William Saliba
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: William Saliba
- Chip used: bench_boost
- Predicted score: 60.23
- Actual score: 123.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.58) beats the best remaining Bench Boost opportunity (14.63).
- Transfer: Virgil van Dijk -> Tyrick Mitchell (projected gain 2.94, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.58) beats the best remaining Bench Boost opportunity (14.63).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 2.70 | 8.27 | 13.78 | 2.00 | 85.3 | 90.0 |
| Bench 1 | Bench Boost | Guglielmo Vicario | GK | 18 | 5.3 | 1.30 | 4.14 | 7.46 | 0.00 | 60.7 | 0.0 |
| Captain | Captain | William Saliba | DEF | 1 | 5.8 | 6.16 | 14.85 | 23.07 | 14.00 | 117.2 | 180.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 6.04 | 14.20 | 21.50 | 12.00 | 113.9 | 180.0 |
| XI | XI | Tyrick Mitchell | DEF | 8 | 4.5 | 4.98 | 11.04 | 16.70 | 6.00 | 111.4 | 180.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 3.17 | 8.29 | 13.11 | 26.00 | 106.4 | 180.0 |
| Bench 4 | Bench Boost | Pedro Porro | DEF | 18 | 5.9 | 1.29 | 4.15 | 7.47 | 0.00 | 44.3 | 0.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.07 | 10.79 | 17.27 | 8.00 | 124.0 | 176.0 |
| XI | XI | Darwin Núñez Ribeiro | FWD | 11 | 7.7 | 3.45 | 8.90 | 13.56 | 2.00 | 93.0 | 106.0 |
| Bench 3 | Bench Boost | Rodrigo Muniz Carvalho | FWD | 10 | 4.6 | 2.35 | 7.87 | 12.90 | 5.00 | 46.5 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 6.1 | 4.28 | 14.56 | 22.97 | 0.00 | 84.3 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.2 | 4.97 | 13.37 | 21.62 | 18.00 | 97.4 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.2 | 3.32 | 11.71 | 21.01 | 16.00 | 30.3 | 71.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.7 | 3.23 | 11.45 | 20.72 | 0.00 | 35.6 | 0.0 |
| Bench 2 | Bench Boost | Son Heung-min | MID | 18 | 10.0 | 2.75 | 8.94 | 16.47 | 0.00 | 55.3 | 0.0 |

## GW35

- Train rows: 130234
- Bank: 2.40 -> 1.90
- Free transfers: 2 -> 2
- Captain: Alexander Isak
- Vice captain: Bruno Borges Fernandes
- Effective captain: Alexander Isak
- Chip used: triple_captain
- Predicted score: 65.86
- Actual score: 75.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (11.42) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Darwin Núñez Ribeiro -> Alexander Isak (projected gain 10.51, hit 0)
- Chip used: Triple Captain on Alexander Isak. Optimizer chose Triple Captain here because the current estimated captain upside (11.42) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Rodrigo Muniz Carvalho replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.8 | 2.82 | 7.88 | 13.11 | 3.00 | 81.5 | 90.0 |
| XI | XI | Guglielmo Vicario | GK | 18 | 5.3 | 2.95 | 7.20 | 12.10 | 2.00 | 73.7 | 180.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 4.55 | 13.42 | 21.47 | 1.00 | 111.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.39 | 12.82 | 20.42 | 1.00 | 115.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.22 | 12.09 | 18.92 | 1.00 | 111.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 3.25 | 8.62 | 14.21 | 2.00 | 66.0 | 180.0 |
| Bench 3 | Bench | Tyrick Mitchell | DEF | 8 | 4.5 | 2.76 | 8.08 | 12.84 | 2.00 | 93.7 | 84.0 |
| Captain | Captain | Alexander Isak | FWD | 15 | 8.2 | 7.52 | 17.33 | 27.41 | 13.00 | 104.9 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.18 | 12.23 | 19.29 | 2.00 | 94.9 | 90.0 |
| Bench 2 | Autosub In | Rodrigo Muniz Carvalho | FWD | 10 | 4.5 | 3.21 | 8.83 | 13.53 | 6.00 | 55.9 | 84.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 5.62 | 15.98 | 25.78 | 4.00 | 111.2 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.9 | 5.53 | 15.79 | 25.99 | 9.00 | 77.8 | 180.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 5.36 | 15.55 | 25.38 | 0.00 | 70.2 | 0.0 |
| XI | XI | Cole Palmer | MID | 7 | 6.1 | 3.25 | 10.97 | 18.19 | 8.00 | 79.4 | 180.0 |
| Bench 4 | Bench | Jarrod Bowen | MID | 19 | 7.7 | 2.22 | 8.88 | 16.16 | 13.00 | 28.2 | 90.0 |