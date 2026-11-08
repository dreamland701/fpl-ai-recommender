# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 281.22
- Total actual points: 211.00
- Average predicted points: 70.30
- Average actual points: 52.75
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
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 69.04
- Actual score: 44.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: James Hill replaced Gabriel dos Santos Magalhães.
- Autosub: Anton Stach replaced Antoine Semenyo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martín | GK | 1 | 6.0 | 3.23 | 10.84 | 18.38 | 0.00 | 75.0 | 0.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.04 | 0.00 | 1.9 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 5.99 | 16.81 | 26.49 | 3.00 | 113.9 | 90.0 |
| XI | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.48 | 14.58 | 24.76 | 0.00 | 79.3 | 0.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 5.96 | 14.44 | 21.92 | 0.00 | 111.0 | 36.0 |
| Bench 2 | Autosub In | James Hill | DEF | 4 | 4.2 | 3.88 | 11.04 | 17.89 | -1.00 | 85.6 | 90.0 |
| Bench 4 | Bench | El Hadji Malick Diouf | DEF | 19 | 4.0 | 3.09 | 8.99 | 14.37 | 1.00 | 78.2 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.61 | 18.57 | 29.75 | 2.00 | 99.2 | 77.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.81 | 15.67 | 24.83 | 4.00 | 100.6 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.47 | 15.27 | 24.95 | 2.00 | 98.1 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.61 | 22.01 | 35.43 | 13.00 | 126.8 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.81 | 17.17 | 28.07 | 2.00 | 89.5 | 90.0 |
| XI | Bench | Antoine Semenyo | MID | 13 | 8.3 | 5.11 | 16.10 | 27.06 | 0.00 | 73.6 | 0.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.36 | 15.64 | 24.52 | 3.00 | 103.3 | 90.0 |
| Bench 3 | Autosub In | Anton Stach | MID | 11 | 4.7 | 3.79 | 10.18 | 15.94 | 3.00 | 77.7 | 90.0 |

## GW32

- Train rows: 185188
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jarrod Bowen
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 56.72
- Actual score: 61.00
- Transfer: Malick Thiaw -> Jan Paul van Hecke (projected gain 1.08, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 2.91 | 8.87 | 15.22 | 1.00 | 60.4 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.21 | 0.19 | 0.17 | 0.00 | 1.7 | 0.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 4.71 | 12.11 | 18.35 | 5.00 | 91.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 3.94 | 11.75 | 20.26 | 4.00 | 62.6 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.74 | 11.17 | 17.69 | 3.00 | 95.2 | 90.0 |
| Bench 2 | Bench | Virgil van Dijk | DEF | 12 | 6.3 | 3.43 | 11.12 | 18.47 | 9.00 | 71.5 | 90.0 |
| Bench 3 | Bench | El Hadji Malick Diouf | DEF | 19 | 4.0 | 3.31 | 8.70 | 14.23 | 6.00 | 78.1 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 4.70 | 15.24 | 25.51 | 2.00 | 77.2 | 81.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.07 | 13.88 | 22.60 | 14.00 | 88.7 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.48 | 13.34 | 21.57 | 13.00 | 82.1 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.91 | 21.16 | 34.20 | 4.00 | 106.9 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.92 | 15.38 | 25.47 | 4.00 | 83.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.2 | 4.26 | 13.19 | 22.52 | 2.00 | 56.2 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.16 | 12.80 | 20.69 | 5.00 | 77.5 | 90.0 |
| Bench 4 | Bench | Anton Stach | MID | 11 | 4.7 | 3.21 | 9.57 | 15.30 | 0.00 | 72.2 | 0.0 |

## GW33

- Train rows: 186014
- Bank: 0.60 -> 2.50
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Cole Palmer
- Chip used: bench_boost
- Predicted score: 77.24
- Actual score: 61.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (16.93) beats the best remaining Bench Boost opportunity (0.00).
- Chip advisory: bench_boost (0.56): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.60): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Gabriel dos Santos Magalhães -> Marcos Senesi Barón (projected gain 2.39, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (16.93) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 2.83 | 9.44 | 16.01 | 1.00 | 74.9 | 90.0 |
| Bench 1 | Bench Boost | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 2.2 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.2 | 6.41 | 14.92 | 22.47 | 6.00 | 126.8 | 180.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 5.64 | 13.06 | 19.35 | 12.00 | 109.7 | 180.0 |
| Bench 2 | Bench Boost | Virgil van Dijk | DEF | 12 | 6.3 | 4.07 | 12.61 | 20.89 | 8.00 | 84.1 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 5.07 | 11.99 | 18.52 | 5.00 | 111.9 | 180.0 |
| Bench 3 | Bench Boost | El Hadji Malick Diouf | DEF | 19 | 4.0 | 2.90 | 8.54 | 14.17 | 5.00 | 78.7 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.73 | 17.73 | 28.18 | 0.00 | 118.3 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.55 | 13.57 | 22.28 | 2.00 | 81.5 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 4.12 | 12.92 | 21.36 | 2.00 | 82.4 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.5 | 7.63 | 19.18 | 30.05 | 2.00 | 129.2 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.26 | 18.85 | 31.54 | 6.00 | 88.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.2 | 6.33 | 16.66 | 26.77 | 5.00 | 109.6 | 154.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.25 | 12.91 | 20.89 | 5.00 | 78.7 | 90.0 |
| Bench 4 | Bench Boost | Anton Stach | MID | 11 | 4.7 | 2.81 | 6.68 | 10.87 | 0.00 | 57.0 | 0.0 |

## GW34

- Train rows: 186843
- Bank: 2.50 -> 1.50
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Ollie Watkins
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 78.22
- Actual score: 45.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.23) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: João Pedro Junqueira de Jesus -> Ollie Watkins (projected gain 6.38, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (6.23) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: El Hadji Malick Diouf replaced Marcos Senesi Barón.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.80 | 12.79 | 20.31 | 10.00 | 101.3 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.11 | 0.10 | 0.18 | 0.00 | 3.2 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 6.77 | 17.92 | 28.08 | 4.00 | 126.7 | 90.0 |
| XI | Bench | Marcos Senesi Barón | DEF | 4 | 5.2 | 4.45 | 13.76 | 22.43 | 0.00 | 101.1 | 0.0 |
| XI | Bench | Jan Paul van Hecke | DEF | 6 | 4.5 | 4.37 | 13.54 | 22.00 | 0.00 | 98.4 | 0.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.2 | 3.94 | 12.18 | 20.26 | 0.00 | 96.0 | 0.0 |
| Bench 3 | Autosub In | El Hadji Malick Diouf | DEF | 19 | 4.0 | 3.40 | 9.35 | 15.01 | 2.00 | 84.0 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.7 | 7.33 | 18.44 | 28.19 | 2.00 | 122.9 | 79.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.6 | 6.89 | 17.77 | 27.98 | 10.00 | 123.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.76 | 16.21 | 26.06 | 1.00 | 104.7 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.73 | 21.33 | 35.30 | 5.00 | 123.9 | 90.0 |
| XI | Bench | Antoine Semenyo | MID | 13 | 8.2 | 5.37 | 16.60 | 27.41 | 0.00 | 90.6 | 0.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.14 | 14.08 | 22.72 | 1.00 | 92.3 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 4.14 | 13.57 | 23.32 | 0.00 | 61.8 | 0.0 |
| Bench 4 | Bench | Anton Stach | MID | 11 | 4.7 | 0.47 | 2.98 | 6.82 | 0.00 | 1.7 | 0.0 |