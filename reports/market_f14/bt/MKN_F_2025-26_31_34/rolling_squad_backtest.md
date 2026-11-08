# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 278.73
- Total actual points: 246.00
- Average predicted points: 69.68
- Average actual points: 61.50
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW30 are included before the first simulated week.
- League-average scores were not available for this run.

## GW31

- Train rows: 184363
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Anthony Gordon
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 67.85
- Actual score: 59.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez Romero | GK | 2 | 5.1 | 3.84 | 9.79 | 15.56 | 6.00 | 94.5 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.04 | 0.20 | 0.00 | 0.6 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 5.91 | 16.84 | 26.65 | 3.00 | 113.9 | 90.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 6.42 | 14.98 | 22.54 | 0.00 | 116.6 | 36.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 2.62 | 12.58 | 22.53 | 0.00 | 54.5 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 4.24 | 12.33 | 19.61 | 1.00 | 94.9 | 90.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.2 | 3.76 | 10.97 | 17.90 | -1.00 | 87.2 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 5.94 | 17.99 | 29.27 | 2.00 | 91.0 | 77.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.17 | 15.18 | 24.53 | 4.00 | 94.7 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 4.45 | 14.35 | 24.16 | 2.00 | 88.3 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.30 | 21.65 | 34.99 | 13.00 | 124.1 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.46 | 16.87 | 27.85 | 2.00 | 86.2 | 90.0 |
| Vice Captain | XI | Anthony Gordon | MID | 15 | 7.3 | 6.63 | 15.80 | 23.91 | 10.00 | 111.2 | 88.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.20 | 15.54 | 24.49 | 3.00 | 102.8 | 90.0 |
| Bench 3 | Bench | Pascal Groß | MID | 6 | 5.5 | 3.69 | 11.77 | 18.72 | 2.00 | 87.6 | 90.0 |

## GW32

- Train rows: 185188
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jarrod Bowen
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 57.39
- Actual score: 70.00
- Transfer: Malick Thiaw -> Jan Paul van Hecke (projected gain 1.61, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Emiliano Martínez Romero | GK | 2 | 5.1 | 2.52 | 7.74 | 12.82 | 0.00 | 77.6 | 0.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 4.80 | 12.28 | 18.62 | 5.00 | 93.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.02 | 11.84 | 19.38 | 9.00 | 80.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 3.94 | 11.75 | 20.29 | 4.00 | 63.8 | 90.0 |
| Bench 3 | Bench | James Hill | DEF | 4 | 4.2 | 3.29 | 10.72 | 17.24 | 3.00 | 89.2 | 90.0 |
| Bench 4 | Bench | Marcos Senesi Barón | DEF | 4 | 5.1 | 2.87 | 10.02 | 16.69 | 4.00 | 76.7 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 4.06 | 14.70 | 25.13 | 2.00 | 71.8 | 81.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.27 | 14.04 | 22.76 | 14.00 | 91.9 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.58 | 13.48 | 21.79 | 13.00 | 82.9 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.43 | 21.42 | 34.19 | 4.00 | 112.9 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.30 | 14.71 | 24.78 | 4.00 | 79.3 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.53 | 13.21 | 21.19 | 5.00 | 84.1 | 90.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 4.53 | 12.08 | 19.04 | 6.00 | 92.6 | 90.0 |
| Bench 2 | Bench | Anthony Gordon | MID | 15 | 7.3 | 3.51 | 10.70 | 17.20 | 3.00 | 63.7 | 70.0 |

## GW33

- Train rows: 186014
- Bank: 0.60 -> 2.90
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Cole Palmer
- Chip used: bench_boost
- Predicted score: 85.41
- Actual score: 73.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (18.61) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Anthony Gordon -> Alex Scott (projected gain 2.60, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (18.61) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez Romero | GK | 2 | 5.1 | 2.03 | 5.48 | 9.23 | 2.00 | 46.7 | 90.0 |
| Bench 1 | Bench Boost | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 3.3 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 7.24 | 16.13 | 24.31 | 6.00 | 146.4 | 180.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 6.35 | 13.95 | 20.58 | 12.00 | 124.8 | 180.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 6.24 | 13.45 | 20.49 | 5.00 | 134.5 | 180.0 |
| Bench 2 | Bench Boost | Virgil van Dijk | DEF | 12 | 6.3 | 4.25 | 12.83 | 21.18 | 8.00 | 86.1 | 90.0 |
| Bench 4 | Bench Boost | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 3.11 | 10.98 | 19.39 | 0.00 | 61.9 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 7.53 | 17.98 | 27.82 | 0.00 | 125.2 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.82 | 13.80 | 22.51 | 2.00 | 85.2 | 90.0 |
| Bench 3 | Bench Boost | Jarrod Bowen | FWD | 19 | 7.5 | 4.10 | 12.91 | 21.37 | 2.00 | 82.2 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.5 | 8.29 | 19.76 | 30.63 | 2.00 | 140.7 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 5.19 | 17.91 | 30.81 | 6.00 | 79.8 | 90.0 |
| XI | XI | Alex Scott | MID | 4 | 5.0 | 7.19 | 15.37 | 22.96 | 5.00 | 144.7 | 180.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 6.48 | 14.05 | 21.24 | 16.00 | 129.4 | 180.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.33 | 13.01 | 21.02 | 5.00 | 79.8 | 90.0 |

## GW34

- Train rows: 186843
- Bank: 2.90 -> 1.90
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Virgil van Dijk
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 68.07
- Actual score: 44.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.99) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: João Pedro Junqueira de Jesus -> Ollie Watkins (projected gain 6.62, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (5.99) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez Romero | GK | 2 | 5.1 | 2.62 | 7.65 | 12.54 | 3.00 | 73.8 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.05 | 0.00 | 1.1 | 0.0 |
| Vice Captain | XI | Virgil van Dijk | DEF | 12 | 6.2 | 6.85 | 18.15 | 28.45 | 4.00 | 130.2 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.92 | 15.76 | 25.48 | 8.00 | 103.0 | 90.0 |
| XI | Bench | Marcos Senesi Barón | DEF | 4 | 5.1 | 2.57 | 11.66 | 19.89 | 0.00 | 72.5 | 0.0 |
| XI | Bench | Jan Paul van Hecke | DEF | 6 | 4.5 | 2.28 | 11.18 | 19.09 | 0.00 | 66.8 | 0.0 |
| Bench 4 | Bench | James Hill | DEF | 4 | 4.2 | 2.11 | 10.14 | 17.78 | 0.00 | 67.9 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.7 | 6.52 | 17.65 | 27.35 | 2.00 | 113.6 | 79.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.6 | 6.13 | 16.95 | 27.03 | 10.00 | 114.7 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.94 | 15.65 | 25.74 | 1.00 | 97.4 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.49 | 20.97 | 34.78 | 5.00 | 122.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.50 | 14.54 | 23.31 | 1.00 | 98.8 | 90.0 |
| Bench 3 | Bench | Cole Palmer | MID | 7 | 10.5 | 2.12 | 11.72 | 21.50 | 0.00 | 37.3 | 0.0 |
| XI | Bench | Alex Scott | MID | 4 | 5.0 | 2.29 | 11.61 | 19.84 | 0.00 | 70.6 | 0.0 |
| Bench 2 | Bench | Pascal Groß | MID | 6 | 5.5 | 2.13 | 11.08 | 19.53 | 0.00 | 66.7 | 0.0 |