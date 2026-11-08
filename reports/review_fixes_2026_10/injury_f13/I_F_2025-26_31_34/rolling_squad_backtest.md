# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 283.46
- Total actual points: 215.00
- Average predicted points: 70.86
- Average actual points: 53.75
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
- Predicted score: 69.00
- Actual score: 53.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Martin Dúbravka replaced David Raya Martín.
- Autosub: James Hill replaced Gabriel dos Santos Magalhães.
- Autosub: Raúl Jiménez Rodríguez replaced Antoine Semenyo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martín | GK | 1 | 6.0 | 3.23 | 10.84 | 18.37 | 0.00 | 75.0 | 0.0 |
| Bench 1 | Autosub In | Martin Dúbravka | GK | 3 | 4.0 | 3.01 | 8.60 | 13.99 | 2.00 | 87.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 6.02 | 16.85 | 26.54 | 3.00 | 113.8 | 90.0 |
| XI | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.45 | 14.49 | 24.64 | 0.00 | 79.5 | 0.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 5.96 | 14.45 | 21.91 | 0.00 | 111.1 | 36.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 4.58 | 12.63 | 19.83 | 1.00 | 95.6 | 90.0 |
| Bench 2 | Autosub In | James Hill | DEF | 4 | 4.2 | 3.88 | 11.03 | 17.87 | -1.00 | 85.1 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.72 | 18.81 | 30.07 | 2.00 | 98.8 | 77.0 |
| Bench 3 | Autosub In | Raúl Jiménez Rodríguez | FWD | 10 | 6.2 | 3.50 | 9.70 | 15.74 | 5.00 | 61.0 | 8.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.7 | 2.92 | 8.16 | 12.81 | 5.00 | 60.2 | 17.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.71 | 22.25 | 35.74 | 13.00 | 126.5 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.79 | 17.12 | 28.00 | 2.00 | 89.7 | 90.0 |
| XI | Bench | Antoine Semenyo | MID | 13 | 8.3 | 5.15 | 16.23 | 27.24 | 0.00 | 72.9 | 0.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.40 | 15.71 | 24.59 | 3.00 | 103.2 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 6.27 | 15.53 | 23.78 | 10.00 | 108.6 | 88.0 |

## GW32

- Train rows: 185188
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Cole Palmer
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 54.42
- Actual score: 48.00
- Transfer: Malick Thiaw -> Jan Paul van Hecke (projected gain 1.98, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martín | GK | 1 | 6.0 | 2.92 | 8.88 | 15.22 | 1.00 | 60.5 | 90.0 |
| XI | XI | Martin Dúbravka | GK | 3 | 4.0 | 3.09 | 8.62 | 13.91 | 2.00 | 90.5 | 90.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 4.72 | 12.11 | 18.32 | 5.00 | 91.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 3.91 | 11.67 | 20.15 | 4.00 | 62.9 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.73 | 11.16 | 17.67 | 3.00 | 94.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.46 | 11.16 | 18.51 | 9.00 | 71.4 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 3.27 | 10.41 | 17.06 | 4.00 | 81.9 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 4.80 | 15.46 | 25.81 | 2.00 | 76.8 | 81.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.7 | 2.37 | 7.58 | 12.20 | 6.00 | 49.6 | 84.0 |
| Bench 4 | Bench | Raúl Jiménez Rodríguez | FWD | 10 | 6.2 | 1.96 | 7.53 | 13.20 | 1.00 | 37.5 | 10.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.02 | 21.41 | 34.54 | 4.00 | 106.5 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.6 | 4.89 | 15.31 | 25.36 | 4.00 | 84.2 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.2 | 4.30 | 13.31 | 22.68 | 2.00 | 55.6 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.21 | 12.89 | 20.79 | 5.00 | 77.4 | 90.0 |
| Bench 2 | Bench | Anthony Gordon | MID | 15 | 7.3 | 3.24 | 10.27 | 16.56 | 3.00 | 61.0 | 70.0 |

## GW33

- Train rows: 186014
- Bank: 0.60 -> 1.10
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Cole Palmer
- Chip used: bench_boost
- Predicted score: 83.81
- Actual score: 74.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (21.35) beats the best remaining Bench Boost opportunity (0.00).
- Chip advisory: triple_captain (0.60): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Raúl Jiménez Rodríguez -> Dominic Calvert-Lewin (projected gain 1.13, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (21.35) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench Boost | David Raya Martín | GK | 1 | 6.0 | 2.86 | 9.48 | 16.04 | 1.00 | 74.9 | 90.0 |
| XI | XI | Martin Dúbravka | GK | 3 | 4.0 | 3.81 | 9.05 | 14.37 | 4.00 | 112.4 | 180.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 6.44 | 14.94 | 22.47 | 6.00 | 126.8 | 180.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 5.67 | 13.09 | 19.37 | 12.00 | 109.7 | 180.0 |
| Bench 2 | Bench Boost | Virgil van Dijk | DEF | 12 | 6.3 | 4.11 | 12.66 | 20.94 | 8.00 | 84.0 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 5.07 | 11.99 | 18.51 | 5.00 | 111.5 | 180.0 |
| Bench 3 | Bench Boost | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 3.41 | 11.26 | 19.64 | 0.00 | 66.0 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.84 | 17.96 | 28.47 | 0.00 | 117.9 | 0.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 11 | 5.6 | 5.79 | 13.64 | 19.88 | 8.00 | 114.5 | 180.0 |
| XI | XI | Junior Kroupi | FWD | 4 | 4.6 | 4.61 | 10.35 | 15.99 | 10.00 | 93.2 | 137.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.5 | 7.62 | 19.13 | 29.97 | 2.00 | 129.4 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.36 | 19.09 | 31.86 | 6.00 | 88.1 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.2 | 6.39 | 16.82 | 26.99 | 5.00 | 108.8 | 154.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.30 | 13.00 | 20.98 | 5.00 | 78.6 | 90.0 |
| Bench 4 | Bench Boost | Anthony Gordon | MID | 15 | 7.3 | 2.92 | 9.85 | 16.70 | 0.00 | 58.2 | 0.0 |

## GW34

- Train rows: 186843
- Bank: 1.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Ollie Watkins
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 76.22
- Actual score: 40.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.34) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: João Pedro Junqueira de Jesus -> Ollie Watkins (projected gain 6.63, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (6.34) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.82 | 12.83 | 20.34 | 10.00 | 101.3 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.34 | 10.68 | 17.61 | 0.00 | 109.6 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 6.80 | 17.96 | 28.11 | 4.00 | 126.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 6.05 | 15.81 | 25.46 | 8.00 | 105.6 | 90.0 |
| XI | Bench | Marcos Senesi Barón | DEF | 4 | 5.1 | 4.47 | 13.77 | 22.43 | 0.00 | 100.9 | 0.0 |
| XI | Bench | Jan Paul van Hecke | DEF | 6 | 4.5 | 4.38 | 13.54 | 21.98 | 0.00 | 98.3 | 0.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.2 | 3.93 | 12.16 | 20.23 | 0.00 | 95.6 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.7 | 7.41 | 18.63 | 28.45 | 2.00 | 122.6 | 79.0 |
| XI | Bench | Dominic Calvert-Lewin | FWD | 11 | 5.6 | 4.04 | 12.02 | 19.01 | 0.00 | 82.6 | 0.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 2.75 | 9.04 | 15.60 | 0.00 | 59.4 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.84 | 21.57 | 35.62 | 5.00 | 123.5 | 90.0 |
| XI | Bench | Antoine Semenyo | MID | 13 | 8.2 | 5.41 | 16.73 | 27.60 | 0.00 | 89.9 | 0.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.20 | 14.18 | 22.82 | 1.00 | 92.1 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 4.12 | 13.52 | 23.24 | 0.00 | 61.9 | 0.0 |
| Bench 4 | Bench | Anthony Gordon | MID | 15 | 7.3 | 1.26 | 6.52 | 12.79 | 0.00 | 28.9 | 0.0 |