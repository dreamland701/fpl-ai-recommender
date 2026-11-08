# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 278.75
- Total actual points: 229.00
- Average predicted points: 69.69
- Average actual points: 57.25
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
- Predicted score: 65.30
- Actual score: 43.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: James Hill replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dúbravka | GK | 3 | 4.0 | 2.92 | 11.09 | 13.56 | 2.00 | 85.0 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.94 | 1.64 | 0.00 | 0.0 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 4.42 | 16.43 | 19.50 | 1.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 5.64 | 16.35 | 25.92 | 3.00 | 90.0 | 90.0 |
| Bench 2 | Autosub In | James Hill | DEF | 4 | 4.2 | 3.91 | 14.64 | 17.87 | -1.00 | 86.7 | 90.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 5.38 | 13.58 | 20.73 | 0.00 | 90.0 | 36.0 |
| Bench 4 | Bench | Joe Rodon | DEF | 11 | 3.9 | 3.23 | 11.41 | 13.87 | 6.00 | 79.4 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.29 | 23.70 | 28.70 | 2.00 | 90.0 | 77.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.43 | 15.37 | 25.20 | 2.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.53 | 15.35 | 24.47 | 4.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.70 | 22.68 | 27.89 | 2.00 | 87.3 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.27 | 21.80 | 35.02 | 13.00 | 90.0 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 14.0 | 5.24 | 16.94 | 28.57 | 0.00 | 73.0 | 0.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 4.20 | 16.51 | 19.56 | 2.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Anton Stach | MID | 11 | 4.7 | 3.78 | 13.44 | 15.64 | 3.00 | 77.9 | 90.0 |

## GW32

- Train rows: 185188
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jarrod Bowen
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 57.73
- Actual score: 74.00
- Transfer: Malick Thiaw -> Jan Paul van Hecke (projected gain 2.43, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dúbravka | GK | 3 | 4.0 | 2.98 | 8.31 | 13.51 | 2.00 | 87.6 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.01 | 0.11 | 0.31 | 0.00 | 4.5 | 0.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 4.53 | 11.76 | 17.84 | 5.00 | 88.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.80 | 11.73 | 19.35 | 9.00 | 77.5 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.66 | 11.04 | 17.62 | 3.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Marcos Senesi Barón | DEF | 4 | 5.1 | 3.28 | 10.35 | 17.04 | 4.00 | 82.0 | 90.0 |
| Bench 4 | Bench | Joe Rodon | DEF | 11 | 3.9 | 3.08 | 9.05 | 14.64 | 0.00 | 82.5 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 4.78 | 15.09 | 25.45 | 2.00 | 78.3 | 81.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.14 | 14.12 | 23.08 | 14.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.66 | 13.77 | 22.23 | 13.00 | 85.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.07 | 21.77 | 34.97 | 4.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.14 | 15.79 | 26.20 | 4.00 | 86.4 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.0 | 4.61 | 14.44 | 24.86 | 8.00 | 53.0 | 89.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 4.27 | 11.87 | 18.95 | 6.00 | 88.9 | 90.0 |
| Bench 2 | Bench | Anton Stach | MID | 11 | 4.7 | 3.28 | 9.42 | 15.11 | 0.00 | 73.6 | 0.0 |

## GW33

- Train rows: 186014
- Bank: 0.60 -> 0.40
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Cole Palmer
- Chip used: bench_boost
- Predicted score: 104.47
- Actual score: 77.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (19.87) beats the best remaining Bench Boost opportunity (0.00).
- Chip advisory: bench_boost (0.56): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.69): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: James Hill -> Konstantinos Mavropanos (projected gain 8.63, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (19.87) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dúbravka | GK | 3 | 4.0 | 5.17 | 7.57 | 12.55 | 4.00 | 169.7 | 180.0 |
| Bench 1 | Bench Boost | Marcus Bettinelli | GK | 13 | 3.8 | 0.10 | 0.20 | 0.46 | 0.00 | 7.6 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 9.93 | 13.25 | 20.45 | 6.00 | 180.0 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.30 | 13.06 | 21.62 | 8.00 | 88.4 | 90.0 |
| Bench 2 | Bench Boost | Konstantinos Mavropanos | DEF | 19 | 4.4 | 4.17 | 12.69 | 19.86 | 6.00 | 90.0 | 90.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 8.32 | 11.15 | 17.06 | 12.00 | 160.1 | 180.0 |
| Bench 4 | Bench Boost | Joe Rodon | DEF | 11 | 3.9 | 3.67 | 5.58 | 9.77 | 1.00 | 89.8 | 46.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 10.57 | 15.77 | 25.80 | 0.00 | 173.7 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.77 | 13.93 | 22.83 | 2.00 | 86.0 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 4.29 | 13.21 | 21.84 | 2.00 | 86.2 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.61 | 19.58 | 32.69 | 6.00 | 90.0 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.5 | 12.31 | 17.18 | 27.69 | 2.00 | 180.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.0 | 5.51 | 16.65 | 28.15 | 10.00 | 77.2 | 90.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 8.55 | 11.97 | 19.00 | 16.00 | 175.4 | 180.0 |
| Bench 3 | Bench Boost | Anton Stach | MID | 11 | 4.7 | 3.88 | 5.69 | 9.93 | 0.00 | 66.2 | 0.0 |

## GW34

- Train rows: 186843
- Bank: 0.40 -> 0.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Mohamed Salah
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 51.25
- Actual score: 35.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.83) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Anton Stach -> Alex Scott (projected gain 23.48, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (5.83) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 0.00 | 7.92 | 15.45 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.92 | 2.06 | 0.00 | 0.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 6.18 | 17.14 | 27.23 | 4.00 | 90.0 | 90.0 |
| XI | XI | Konstantinos Mavropanos | DEF | 19 | 4.4 | 4.68 | 12.95 | 20.63 | 4.00 | 90.0 | 90.0 |
| XI | Bench | Marcos Senesi Barón | DEF | 4 | 5.1 | 0.00 | 10.17 | 19.67 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 6 | 4.5 | 0.00 | 10.07 | 19.60 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Joe Rodon | DEF | 11 | 3.9 | 0.00 | 5.22 | 11.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.6 | 6.29 | 16.94 | 27.06 | 10.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.53 | 15.97 | 25.84 | 1.00 | 90.0 | 90.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 0.00 | 8.18 | 17.55 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.33 | 20.88 | 34.78 | 5.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.0 | 6.58 | 19.25 | 31.92 | 1.00 | 90.0 | 58.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 0.00 | 10.36 | 21.20 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Pascal Groß | MID | 6 | 5.5 | 0.00 | 10.20 | 20.03 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Alex Scott | MID | 4 | 5.0 | 0.00 | 10.16 | 19.52 | 0.00 | 0.0 | 0.0 |