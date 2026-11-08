# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 292.19
- Total actual points: 247.00
- Average predicted points: 73.05
- Average actual points: 61.75
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
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Virgil van Dijk
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 67.40
- Actual score: 62.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Caoimhín Kelleher | GK | 5 | 4.8 | 3.53 | 12.25 | 22.07 | 9.00 | 71.1 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Virgil van Dijk | DEF | 12 | 6.3 | 6.36 | 18.56 | 28.91 | 3.00 | 90.0 | 90.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 5.91 | 14.50 | 22.57 | 0.00 | 90.0 | 36.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 0.00 | 13.95 | 24.18 | 0.00 | 0.0 | 0.0 |
| XI | XI | Lewis Hall | DEF | 15 | 5.3 | 4.98 | 12.78 | 19.65 | 1.00 | 90.0 | 90.0 |
| Bench 3 | Bench | James Hill | DEF | 4 | 4.2 | 3.81 | 10.68 | 17.22 | -1.00 | 86.7 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.81 | 18.32 | 28.18 | 2.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 5.30 | 15.46 | 24.22 | 2.00 | 90.0 | 77.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.00 | 14.97 | 24.27 | 4.00 | 90.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.15 | 21.55 | 34.53 | 13.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.44 | 16.79 | 27.55 | 2.00 | 87.3 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.07 | 15.45 | 24.11 | 3.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 5.71 | 15.16 | 23.23 | 10.00 | 90.0 | 88.0 |
| Bench 2 | Bench | Pascal Groß | MID | 6 | 5.5 | 4.12 | 12.01 | 19.20 | 2.00 | 90.0 | 90.0 |

## GW32

- Train rows: 185188
- Bank: 0.10 -> 2.80
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 64.74
- Actual score: 77.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.66) beats the best remaining Bench Boost opportunity (16.10).
- Transfer: Gabriel dos Santos Magalhães -> Jan Paul van Hecke (projected gain 1.76, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.66) beats the best remaining Bench Boost opportunity (16.10).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Caoimhín Kelleher | GK | 5 | 4.8 | 4.36 | 13.45 | 24.68 | 2.00 | 79.8 | 90.0 |
| Bench 1 | Bench Boost | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 4.5 | 0.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 4.80 | 12.38 | 18.99 | 5.00 | 88.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.43 | 11.00 | 17.92 | 9.00 | 77.5 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.47 | 10.92 | 17.41 | 3.00 | 90.0 | 90.0 |
| Bench 3 | Bench Boost | Lewis Hall | DEF | 15 | 5.3 | 2.61 | 8.06 | 13.03 | 1.00 | 69.3 | 90.0 |
| Bench 4 | Bench Boost | Malick Thiaw | DEF | 15 | 5.1 | 1.29 | 5.69 | 9.67 | 2.00 | 46.6 | 90.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.28 | 15.80 | 25.10 | 13.00 | 85.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 4.11 | 13.14 | 21.76 | 2.00 | 78.3 | 81.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 4.01 | 13.06 | 22.18 | 14.00 | 90.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.94 | 21.08 | 34.26 | 4.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.91 | 15.02 | 25.25 | 4.00 | 86.4 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.68 | 13.65 | 21.87 | 5.00 | 81.7 | 90.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 4.16 | 11.73 | 18.47 | 6.00 | 88.9 | 90.0 |
| Bench 2 | Bench Boost | Anthony Gordon | MID | 15 | 7.3 | 3.76 | 10.78 | 17.65 | 3.00 | 67.9 | 70.0 |

## GW33

- Train rows: 186014
- Bank: 2.80 -> 1.80
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Marcos Senesi Barón
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 105.21
- Actual score: 70.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (16.98) beats the best remaining Triple Captain opportunity (7.20).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: James Hill -> Marcos Senesi Barón (projected gain 3.19, hit 0)
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (16.98) beats the best remaining Triple Captain opportunity (7.20).
- Autosub: Lewis Hall replaced João Pedro Junqueira de Jesus.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Caoimhín Kelleher | GK | 5 | 4.8 | 3.56 | 13.48 | 24.83 | 6.00 | 76.0 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.01 | 0.88 | 0.72 | 0.00 | 7.6 | 0.0 |
| Vice Captain | XI | Marcos Senesi Barón | DEF | 4 | 5.2 | 10.19 | 15.00 | 22.74 | 6.00 | 180.0 | 180.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 8.58 | 13.56 | 20.23 | 12.00 | 160.1 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.21 | 12.00 | 20.08 | 8.00 | 88.4 | 90.0 |
| Bench 2 | Autosub In | Lewis Hall | DEF | 15 | 5.3 | 3.17 | 9.11 | 14.68 | 1.00 | 75.0 | 45.0 |
| Bench 3 | Bench | Malick Thiaw | DEF | 15 | 5.1 | 3.07 | 8.85 | 14.53 | 1.00 | 75.5 | 90.0 |
| XI | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 9.56 | 16.03 | 24.72 | 0.00 | 173.7 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.48 | 15.84 | 25.78 | 2.00 | 86.0 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 6.13 | 15.35 | 25.05 | 2.00 | 86.2 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.09 | 19.96 | 32.93 | 6.00 | 90.0 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.5 | 12.38 | 19.17 | 29.95 | 2.00 | 180.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.70 | 13.61 | 21.78 | 5.00 | 82.7 | 90.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 8.56 | 13.20 | 20.21 | 16.00 | 175.4 | 180.0 |
| Bench 4 | Bench | Anthony Gordon | MID | 15 | 7.3 | 2.76 | 9.63 | 16.44 | 0.00 | 62.0 | 0.0 |

## GW34

- Train rows: 186843
- Bank: 1.80 -> 0.00
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Virgil van Dijk
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 54.84
- Actual score: 38.00
- Transfer: Lewis Hall -> Gabriel dos Santos Magalhães (projected gain 9.93, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Caoimhín Kelleher | GK | 5 | 4.8 | 5.29 | 15.42 | 22.46 | 2.00 | 80.8 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Virgil van Dijk | DEF | 12 | 6.2 | 6.86 | 17.99 | 29.07 | 4.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 6.49 | 17.64 | 28.46 | 8.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Marcos Senesi Barón | DEF | 4 | 5.2 | 0.00 | 13.68 | 21.74 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Jan Paul van Hecke | DEF | 6 | 4.5 | 0.00 | 13.54 | 21.82 | 0.00 | 0.0 | 0.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 2.91 | 9.30 | 15.60 | 2.00 | 77.4 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.6 | 6.33 | 19.17 | 30.53 | 10.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.80 | 18.08 | 28.68 | 1.00 | 90.0 | 90.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 0.00 | 8.98 | 17.34 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.40 | 21.40 | 34.97 | 5.00 | 90.0 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 0.00 | 14.34 | 24.40 | 0.00 | 0.0 | 0.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.00 | 13.91 | 22.33 | 1.00 | 89.9 | 90.0 |
| XI | Bench | Pascal Groß | MID | 6 | 5.5 | 0.00 | 12.56 | 21.27 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Anthony Gordon | MID | 15 | 7.3 | 1.37 | 6.46 | 12.62 | 0.00 | 35.1 | 0.0 |