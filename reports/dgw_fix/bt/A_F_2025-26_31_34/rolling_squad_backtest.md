# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 272.91
- Total actual points: 240.00
- Average predicted points: 68.23
- Average actual points: 60.00
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
- Bank: 100.00 -> 0.30
- Free transfers: 1 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Virgil van Dijk
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 66.76
- Actual score: 61.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Lewis Hall replaced Gabriel dos Santos Magalhães.
- Autosub: Junior Kroupi replaced Antoine Semenyo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martín | GK | 1 | 6.0 | 3.23 | 10.84 | 18.38 | 0.00 | 75.0 | 0.0 |
| XI | XI | Jordan Pickford | GK | 9 | 5.6 | 3.32 | 9.34 | 15.12 | 7.00 | 88.9 | 90.0 |
| Vice Captain | XI | Virgil van Dijk | DEF | 12 | 6.3 | 5.99 | 16.81 | 26.49 | 3.00 | 113.9 | 90.0 |
| XI | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.48 | 14.58 | 24.76 | 0.00 | 79.3 | 0.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 5.96 | 14.44 | 21.92 | 0.00 | 111.0 | 36.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 4.56 | 12.61 | 19.83 | 1.00 | 95.6 | 90.0 |
| Bench 2 | Autosub In | Lewis Hall | DEF | 15 | 5.3 | 4.46 | 11.42 | 17.69 | 1.00 | 97.3 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.81 | 15.67 | 24.83 | 4.00 | 100.6 | 90.0 |
| Bench 3 | Autosub In | Junior Kroupi | FWD | 4 | 4.7 | 2.90 | 8.14 | 12.81 | 5.00 | 60.2 | 17.0 |
| Bench 4 | Bench | Norberto Bercique Gomes Betuncal | FWD | 9 | 5.0 | 2.86 | 7.65 | 11.69 | 16.00 | 54.0 | 81.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.61 | 22.01 | 35.43 | 13.00 | 126.8 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.81 | 17.17 | 28.07 | 2.00 | 89.5 | 90.0 |
| XI | Bench | Antoine Semenyo | MID | 13 | 8.3 | 5.11 | 16.10 | 27.06 | 0.00 | 73.6 | 0.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.36 | 15.64 | 24.52 | 3.00 | 103.3 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 5.15 | 12.93 | 20.85 | 9.00 | 84.7 | 86.0 |

## GW32

- Train rows: 185188
- Bank: 0.30 -> 0.90
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Cole Palmer
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 53.00
- Actual score: 61.00
- Transfer: Malick Thiaw -> Jan Paul van Hecke (projected gain 3.03, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.6 | 3.11 | 9.27 | 15.23 | 0.00 | 87.3 | 90.0 |
| Bench 1 | Bench | David Raya Martín | GK | 1 | 6.0 | 2.91 | 8.87 | 15.22 | 1.00 | 60.4 | 90.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 4.71 | 12.11 | 18.35 | 5.00 | 91.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 3.94 | 11.75 | 20.26 | 4.00 | 62.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.43 | 11.12 | 18.47 | 9.00 | 71.5 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 3.25 | 10.40 | 17.07 | 4.00 | 81.9 | 90.0 |
| Bench 3 | Bench | Lewis Hall | DEF | 15 | 5.3 | 2.48 | 7.66 | 12.80 | 1.00 | 66.3 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.48 | 13.34 | 21.57 | 13.00 | 82.1 | 90.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 9 | 5.0 | 2.91 | 8.57 | 13.91 | 7.00 | 59.6 | 73.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.7 | 2.35 | 7.57 | 12.20 | 6.00 | 49.6 | 84.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.91 | 21.16 | 34.20 | 4.00 | 106.9 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.6 | 4.92 | 15.38 | 25.47 | 4.00 | 83.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.2 | 4.26 | 13.19 | 22.52 | 2.00 | 56.2 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.16 | 12.80 | 20.69 | 5.00 | 77.5 | 90.0 |
| Bench 2 | Bench | Harry Wilson | MID | 10 | 6.0 | 2.68 | 9.16 | 15.48 | 2.00 | 53.2 | 79.0 |

## GW33

- Train rows: 186014
- Bank: 0.90 -> 1.90
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Marcos Senesi Barón
- Effective captain: Cole Palmer
- Chip used: bench_boost
- Predicted score: 78.02
- Actual score: 75.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (18.52) beats the best remaining Bench Boost opportunity (0.94).
- Chip advisory: triple_captain (0.63): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Harry Wilson -> Alex Scott (projected gain 2.78, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (18.52) beats the best remaining Bench Boost opportunity (0.94).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench Boost | David Raya Martín | GK | 1 | 6.0 | 2.83 | 9.44 | 16.01 | 1.00 | 74.9 | 90.0 |
| XI | XI | Jordan Pickford | GK | 9 | 5.6 | 2.91 | 8.61 | 14.30 | 1.00 | 84.0 | 90.0 |
| Vice Captain | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 6.41 | 14.92 | 22.47 | 6.00 | 126.8 | 180.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 5.64 | 13.06 | 19.35 | 12.00 | 109.7 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.07 | 12.61 | 20.89 | 8.00 | 84.1 | 90.0 |
| Bench 2 | Bench Boost | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 3.42 | 11.30 | 19.69 | 0.00 | 65.7 | 90.0 |
| Bench 3 | Bench Boost | Lewis Hall | DEF | 15 | 5.3 | 3.05 | 8.61 | 14.10 | 1.00 | 76.3 | 45.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.55 | 13.57 | 22.28 | 2.00 | 81.5 | 90.0 |
| XI | XI | Junior Kroupi | FWD | 4 | 4.6 | 4.59 | 10.34 | 15.99 | 10.00 | 93.3 | 137.0 |
| Bench 4 | Bench Boost | Norberto Bercique Gomes Betuncal | FWD | 9 | 5.0 | 2.52 | 7.55 | 13.17 | 9.00 | 52.5 | 72.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.5 | 7.63 | 19.18 | 30.05 | 2.00 | 129.2 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.26 | 18.85 | 31.54 | 6.00 | 88.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.2 | 6.33 | 16.66 | 26.77 | 5.00 | 109.6 | 154.0 |
| XI | XI | Alex Scott | MID | 4 | 5.0 | 5.91 | 14.05 | 21.43 | 5.00 | 123.2 | 180.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.25 | 12.91 | 20.89 | 5.00 | 78.7 | 90.0 |

## GW34

- Train rows: 186843
- Bank: 1.90 -> 2.70
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Virgil van Dijk
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 75.14
- Actual score: 43.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.23) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Lewis Hall -> Konstantinos Mavropanos (projected gain 0.87, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (6.23) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.80 | 12.79 | 20.31 | 10.00 | 101.3 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 5.6 | 3.35 | 9.64 | 15.76 | 1.00 | 92.1 | 90.0 |
| Vice Captain | XI | Virgil van Dijk | DEF | 12 | 6.2 | 6.77 | 17.92 | 28.08 | 4.00 | 126.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 6.05 | 15.84 | 25.50 | 8.00 | 105.5 | 90.0 |
| XI | Bench | Marcos Senesi Barón | DEF | 4 | 5.1 | 4.45 | 13.76 | 22.43 | 0.00 | 101.1 | 0.0 |
| XI | Bench | Jan Paul van Hecke | DEF | 6 | 4.5 | 4.37 | 13.54 | 22.00 | 0.00 | 98.4 | 0.0 |
| XI | XI | Konstantinos Mavropanos | DEF | 19 | 4.5 | 4.86 | 13.05 | 20.64 | 4.00 | 99.4 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.76 | 16.21 | 26.06 | 1.00 | 104.7 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 2.73 | 9.02 | 15.60 | 0.00 | 59.5 | 0.0 |
| Bench 3 | Bench | Norberto Bercique Gomes Betuncal | FWD | 9 | 5.0 | 2.77 | 8.26 | 14.32 | 0.00 | 60.8 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.73 | 21.33 | 35.30 | 5.00 | 123.9 | 90.0 |
| XI | Bench | Antoine Semenyo | MID | 13 | 8.2 | 5.37 | 16.60 | 27.41 | 0.00 | 90.6 | 0.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.14 | 14.08 | 22.72 | 1.00 | 92.3 | 90.0 |
| XI | Bench | Alex Scott | MID | 4 | 5.0 | 4.37 | 13.58 | 21.90 | 0.00 | 98.8 | 0.0 |
| Bench 2 | Bench | Cole Palmer | MID | 7 | 10.5 | 4.14 | 13.57 | 23.32 | 0.00 | 61.8 | 0.0 |