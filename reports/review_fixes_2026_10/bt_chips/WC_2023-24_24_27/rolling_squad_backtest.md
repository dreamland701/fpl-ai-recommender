# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 255.76
- Total actual points: 261.00
- Average predicted points: 63.94
- Average actual points: 65.25
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW23 are included before the first simulated week.
- League-average scores were not available for this run.

## GW24

- Train rows: 121022
- Bank: 100.00 -> 1.20
- Free transfers: 1 -> 2
- Captain: Ollie Watkins
- Vice captain: Phil Foden
- Effective captain: Ollie Watkins
- Chip used: none
- Predicted score: 58.33
- Actual score: 50.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Martin Dubravka replaced Alisson Ramses Becker.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alisson Ramses Becker | GK | 11 | 5.7 | 3.52 | 9.56 | 15.52 | 0.00 | 83.3 | 0.0 |
| Bench 1 | Autosub In | Martin Dubravka | GK | 15 | 4.2 | 2.78 | 8.80 | 14.97 | 1.00 | 85.1 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.71 | 13.15 | 21.15 | 4.00 | 90.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.9 | 3.86 | 11.27 | 18.78 | 2.00 | 78.8 | 90.0 |
| Bench 4 | Bench | William Saliba | DEF | 1 | 5.6 | 3.44 | 10.33 | 16.61 | 12.00 | 81.0 | 90.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 11 | 6.3 | 3.66 | 10.09 | 16.41 | 2.00 | 83.7 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 3.77 | 9.87 | 15.67 | 1.00 | 72.4 | 86.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.8 | 5.87 | 16.44 | 27.25 | 2.00 | 94.2 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.8 | 4.86 | 12.40 | 20.24 | 1.00 | 85.0 | 19.0 |
| Bench 2 | Bench | Julián Álvarez | FWD | 13 | 6.8 | 3.77 | 11.19 | 19.09 | 2.00 | 51.1 | 76.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.15 | 16.36 | 26.75 | 15.00 | 75.6 | 66.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.0 | 5.84 | 15.79 | 25.39 | 3.00 | 93.1 | 90.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 4.99 | 14.23 | 23.33 | 2.00 | 87.4 | 90.0 |
| XI | XI | Diogo Teixeira da Silva | MID | 11 | 8.2 | 5.18 | 13.90 | 22.09 | 7.00 | 83.3 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.9 | 4.71 | 13.64 | 22.05 | 10.00 | 81.8 | 90.0 |

## GW25

- Train rows: 121836
- Bank: 1.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: Darwin Núñez Ribeiro
- Vice captain: Phil Foden
- Effective captain: Darwin Núñez Ribeiro
- Chip used: wildcard
- Predicted score: 67.17
- Actual score: 64.00
- Transfer: none
- Chip used: Wildcard — full rebuild projects +13.36 squad value (threshold 12).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.16 | 9.19 | 15.03 | 3.00 | 80.7 | 90.0 |
| Bench 1 | Bench | Martin Dubravka | GK | 15 | 4.2 | 2.78 | 8.23 | 13.89 | 2.00 | 79.1 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 4.65 | 12.74 | 20.81 | 1.00 | 85.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.4 | 5.60 | 12.71 | 19.58 | 10.00 | 118.8 | 180.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.42 | 11.97 | 19.07 | 6.00 | 88.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.1 | 4.44 | 11.88 | 18.71 | 6.00 | 86.8 | 90.0 |
| XI | XI | Nathan Aké | DEF | 13 | 5.1 | 4.88 | 10.90 | 16.39 | 2.00 | 110.1 | 90.0 |
| Captain | Captain | Darwin Núñez Ribeiro | FWD | 11 | 7.6 | 7.18 | 16.68 | 25.30 | 5.00 | 105.6 | 45.0 |
| Bench 4 | Bench | Elijah Adebayo | FWD | 12 | 4.9 | 4.02 | 10.21 | 15.93 | 0.00 | 93.1 | 0.0 |
| Bench 3 | Bench | Carlton Morris | FWD | 12 | 5.0 | 4.05 | 9.65 | 14.26 | 10.00 | 89.0 | 180.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 6.21 | 17.51 | 28.80 | 15.00 | 78.1 | 68.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.0 | 6.81 | 17.16 | 26.31 | 5.00 | 109.1 | 180.0 |
| XI | XI | Diogo Teixeira da Silva | MID | 11 | 8.3 | 6.78 | 16.04 | 23.99 | 4.00 | 106.0 | 43.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 10.8 | 5.86 | 15.19 | 23.83 | 2.00 | 81.9 | 90.0 |
| Bench 2 | Bench | Bruno Borges Fernandes | MID | 14 | 8.2 | 4.24 | 11.92 | 19.80 | 2.00 | 80.3 | 90.0 |

## GW26

- Train rows: 122659
- Bank: 0.20 -> 1.00
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Phil Foden
- Effective captain: Bukayo Saka
- Chip used: triple_captain
- Predicted score: 68.87
- Actual score: 57.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.48) beats the best remaining Triple Captain opportunity (10.14).
- Transfer: Diogo Teixeira da Silva -> Luis Díaz (projected gain 4.13, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (6.48) beats the best remaining Triple Captain opportunity (10.14).
- Autosub: Nathan Aké replaced Virgil van Dijk.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.68 | 10.03 | 16.41 | 2.00 | 90.5 | 90.0 |
| Bench 1 | Bench | Martin Dubravka | GK | 15 | 4.2 | 1.90 | 6.75 | 11.49 | 0.00 | 78.2 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 3.96 | 13.17 | 21.30 | 0.00 | 94.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.60 | 12.56 | 19.69 | 2.00 | 89.4 | 90.0 |
| XI | Bench | Virgil van Dijk | DEF | 11 | 6.4 | 3.93 | 12.55 | 20.51 | 0.00 | 99.8 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.1 | 4.32 | 11.92 | 18.63 | 2.00 | 79.0 | 90.0 |
| Bench 3 | Autosub In | Nathan Aké | DEF | 13 | 5.1 | 2.62 | 7.70 | 12.22 | 6.00 | 63.2 | 90.0 |
| XI | Bench | Carlton Morris | FWD | 12 | 5.0 | 3.61 | 10.90 | 17.75 | 0.00 | 84.0 | 0.0 |
| Bench 2 | Bench | Darwin Núñez Ribeiro | FWD | 11 | 7.6 | 2.88 | 10.56 | 17.68 | 0.00 | 28.6 | 0.0 |
| Bench 4 | Bench | Elijah Adebayo | FWD | 12 | 4.9 | 0.71 | 4.35 | 8.26 | 0.00 | 12.6 | 0.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 7.98 | 21.36 | 32.94 | 10.00 | 104.8 | 75.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.0 | 6.67 | 18.25 | 28.89 | 11.00 | 110.7 | 90.0 |
| XI | Bench | Luis Díaz | MID | 11 | 7.5 | 4.88 | 14.53 | 22.82 | 0.00 | 86.4 | 0.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 10.8 | 4.84 | 14.45 | 23.95 | 0.00 | 63.3 | 6.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.2 | 4.44 | 12.91 | 21.15 | 4.00 | 84.0 | 90.0 |

## GW27

- Train rows: 123487
- Bank: 1.00 -> 1.50
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Phil Foden
- Effective captain: Bukayo Saka
- Chip used: bench_boost
- Predicted score: 61.39
- Actual score: 90.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.54) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Darwin Núñez Ribeiro -> Dominic Solanke (projected gain 6.58, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.54) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.54 | 9.97 | 16.09 | 13.00 | 92.9 | 90.0 |
| Bench 1 | Bench Boost | Martin Dubravka | GK | 15 | 4.2 | 1.33 | 3.84 | 7.00 | 7.00 | 40.2 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 4.46 | 13.01 | 21.49 | 1.00 | 88.5 | 51.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.43 | 12.04 | 18.91 | 6.00 | 82.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.2 | 4.24 | 11.21 | 17.45 | 6.00 | 77.2 | 90.0 |
| XI | XI | Nathan Aké | DEF | 13 | 5.1 | 2.90 | 8.47 | 13.98 | 2.00 | 75.4 | 90.0 |
| Bench 2 | Bench Boost | Virgil van Dijk | DEF | 11 | 6.4 | 2.74 | 8.23 | 14.00 | 6.00 | 55.2 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.1 | 4.73 | 12.83 | 19.68 | 2.00 | 73.1 | 88.0 |
| Bench 3 | Bench Boost | Carlton Morris | FWD | 12 | 5.0 | 2.10 | 6.52 | 11.08 | 8.00 | 43.1 | 90.0 |
| Bench 4 | Bench Boost | Elijah Adebayo | FWD | 12 | 4.9 | 0.37 | 2.85 | 5.72 | 0.00 | 8.1 | 0.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.1 | 7.45 | 20.00 | 32.83 | 7.00 | 85.1 | 45.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.0 | 5.62 | 16.63 | 26.78 | 15.00 | 88.6 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.2 | 3.28 | 11.70 | 19.60 | 5.00 | 75.1 | 90.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 10.7 | 3.19 | 11.04 | 19.21 | 2.00 | 32.5 | 90.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.5 | 3.57 | 10.52 | 16.66 | 3.00 | 42.2 | 90.0 |