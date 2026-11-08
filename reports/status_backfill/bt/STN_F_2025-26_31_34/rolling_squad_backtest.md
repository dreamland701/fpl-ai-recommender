# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 279.78
- Total actual points: 220.00
- Average predicted points: 69.95
- Average actual points: 55.00
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
- Predicted score: 68.40
- Actual score: 42.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: James Hill replaced Gabriel dos Santos Magalhães.
- Autosub: Omar Alderete replaced Antoine Semenyo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martín | GK | 1 | 6.0 | 3.19 | 10.74 | 18.21 | 0.00 | 74.2 | 0.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 5.87 | 16.49 | 26.00 | 3.00 | 111.3 | 90.0 |
| XI | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.51 | 14.65 | 24.83 | 0.00 | 79.7 | 0.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 5.76 | 13.95 | 21.17 | 0.00 | 107.1 | 36.0 |
| Bench 2 | Autosub In | James Hill | DEF | 4 | 4.2 | 3.90 | 11.09 | 17.96 | -1.00 | 86.0 | 90.0 |
| Bench 3 | Autosub In | Omar Alderete | DEF | 17 | 4.1 | 3.62 | 10.36 | 16.07 | 1.00 | 92.9 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.49 | 18.26 | 29.27 | 2.00 | 96.7 | 77.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.76 | 15.55 | 24.63 | 4.00 | 99.7 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.50 | 15.37 | 25.09 | 2.00 | 98.9 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.52 | 21.79 | 35.09 | 13.00 | 125.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.84 | 17.26 | 28.21 | 2.00 | 90.1 | 90.0 |
| XI | Bench | Antoine Semenyo | MID | 13 | 8.3 | 5.09 | 16.06 | 26.98 | 0.00 | 73.3 | 0.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.36 | 15.65 | 24.53 | 3.00 | 103.3 | 90.0 |
| Bench 4 | Bench | Kobbie Mainoo | MID | 14 | 4.6 | 2.93 | 8.74 | 14.23 | 2.00 | 77.9 | 90.0 |

## GW32

- Train rows: 185188
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jarrod Bowen
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 67.25
- Actual score: 78.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.24) beats the best remaining Bench Boost opportunity (18.35).
- Transfer: Malick Thiaw -> Jan Paul van Hecke (projected gain 2.40, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.24) beats the best remaining Bench Boost opportunity (18.35).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 2.90 | 8.81 | 15.15 | 1.00 | 60.1 | 90.0 |
| Bench 1 | Bench Boost | Marcus Bettinelli | GK | 13 | 3.8 | 0.04 | 0.19 | 0.34 | 0.00 | 4.9 | 0.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 4.66 | 12.00 | 18.19 | 5.00 | 90.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 3.93 | 11.70 | 20.21 | 4.00 | 62.4 | 90.0 |
| Bench 3 | Bench Boost | Virgil van Dijk | DEF | 12 | 6.3 | 3.47 | 11.24 | 18.66 | 9.00 | 72.4 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.73 | 11.15 | 17.65 | 3.00 | 94.9 | 90.0 |
| Bench 2 | Bench Boost | Omar Alderete | DEF | 17 | 4.1 | 3.52 | 9.67 | 15.25 | 8.00 | 84.3 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 4.65 | 15.09 | 25.30 | 2.00 | 76.1 | 81.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.15 | 14.08 | 22.92 | 14.00 | 90.2 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.52 | 13.43 | 21.71 | 13.00 | 82.8 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.97 | 21.31 | 34.44 | 4.00 | 108.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.03 | 15.67 | 25.91 | 4.00 | 86.1 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.2 | 4.24 | 13.12 | 22.43 | 2.00 | 55.8 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.27 | 13.11 | 21.18 | 5.00 | 79.9 | 90.0 |
| Bench 4 | Bench Boost | Kobbie Mainoo | MID | 14 | 4.6 | 3.21 | 9.00 | 14.43 | 0.00 | 78.9 | 0.0 |

## GW33

- Train rows: 186014
- Bank: 0.60 -> 2.50
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 74.71
- Actual score: 58.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (12.51) beats the best remaining Triple Captain opportunity (6.28).
- Chip advisory: triple_captain (0.60): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Gabriel dos Santos Magalhães -> Marcos Senesi Barón (projected gain 1.95, hit 0)
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (12.51) beats the best remaining Triple Captain opportunity (6.28).
- Autosub: Virgil van Dijk replaced João Pedro Junqueira de Jesus.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 2.78 | 9.30 | 15.78 | 1.00 | 73.8 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 1.16 | 1.41 | 1.70 | 0.00 | 30.6 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.2 | 6.30 | 14.64 | 22.04 | 6.00 | 124.6 | 180.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 5.60 | 12.96 | 19.20 | 12.00 | 108.9 | 180.0 |
| Bench 2 | Autosub In | Virgil van Dijk | DEF | 12 | 6.3 | 4.14 | 12.78 | 21.15 | 8.00 | 85.4 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 5.04 | 11.92 | 18.42 | 5.00 | 111.3 | 180.0 |
| Bench 3 | Bench | Omar Alderete | DEF | 17 | 4.1 | 2.70 | 7.94 | 13.78 | 1.00 | 71.2 | 62.0 |
| Vice Captain | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.59 | 17.37 | 27.63 | 0.00 | 115.5 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.64 | 13.82 | 22.67 | 2.00 | 83.4 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 4.21 | 13.16 | 21.72 | 2.00 | 84.2 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.34 | 19.05 | 31.85 | 6.00 | 89.9 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.5 | 7.56 | 19.01 | 29.80 | 2.00 | 127.8 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.2 | 6.18 | 16.26 | 26.15 | 5.00 | 106.4 | 154.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.34 | 13.15 | 21.27 | 5.00 | 80.6 | 90.0 |
| Bench 4 | Bench | Kobbie Mainoo | MID | 14 | 4.6 | 1.79 | 5.60 | 9.55 | 4.00 | 44.1 | 90.0 |

## GW34

- Train rows: 186843
- Bank: 2.50 -> 1.50
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Ollie Watkins
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 69.42
- Actual score: 42.00
- Transfer: João Pedro Junqueira de Jesus -> Ollie Watkins (projected gain 6.21, hit 0)
- Autosub: Omar Alderete replaced Marcos Senesi Barón.
- Autosub: Kobbie Mainoo replaced Antoine Semenyo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.60 | 12.29 | 19.49 | 10.00 | 97.2 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 6.57 | 17.40 | 27.29 | 4.00 | 122.7 | 90.0 |
| XI | Bench | Marcos Senesi Barón | DEF | 4 | 5.2 | 4.36 | 13.51 | 22.11 | 0.00 | 99.2 | 0.0 |
| XI | Bench | Jan Paul van Hecke | DEF | 6 | 4.5 | 4.35 | 13.48 | 21.98 | 0.00 | 98.1 | 0.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.2 | 3.85 | 11.94 | 19.94 | 0.00 | 94.2 | 0.0 |
| Bench 3 | Autosub In | Omar Alderete | DEF | 17 | 4.1 | 2.79 | 7.74 | 13.22 | 0.00 | 69.1 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.7 | 7.16 | 18.01 | 27.50 | 2.00 | 119.4 | 79.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.6 | 6.79 | 17.51 | 27.59 | 10.00 | 121.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.76 | 16.19 | 26.03 | 1.00 | 104.5 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.61 | 21.01 | 34.81 | 5.00 | 121.4 | 90.0 |
| XI | Bench | Antoine Semenyo | MID | 13 | 8.2 | 5.22 | 16.22 | 26.85 | 0.00 | 87.7 | 0.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.15 | 14.09 | 22.74 | 1.00 | 92.3 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 4.25 | 13.84 | 23.76 | 0.00 | 63.9 | 0.0 |
| Bench 4 | Autosub In | Kobbie Mainoo | MID | 14 | 4.6 | 2.62 | 7.30 | 12.23 | 4.00 | 66.3 | 90.0 |