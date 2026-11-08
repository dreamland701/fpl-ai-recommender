# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW1
- Simulated weeks: GW2-GW8
- Total predicted points: 441.99
- Total actual points: 389.00
- Average predicted points: 63.14
- Average actual points: 55.57
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW1 are included before the first simulated week.
- League-average scores were pulled from official FPL event metadata when available.

## GW2

- Train rows: 104659
- Bank: 100.00 -> 1.00
- Free transfers: 1 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 59.40
- Actual score: 46.00
- Chip advisory: bench_boost (0.62): Bench depth is strong enough that a Bench Boost is worth considering.
- League average score: 81.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 5.0 | 4.14 | 12.36 | 20.58 | 2.00 | 87.4 | 90.0 |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.5 | 3.83 | 11.62 | 20.02 | 2.00 | 99.8 | 90.0 |
| XI | XI | Raphaël Varane | DEF | 14 | 5.0 | 4.65 | 14.11 | 23.56 | 1.00 | 92.8 | 90.0 |
| XI | XI | Pervis Estupiñán | DEF | 5 | 5.0 | 4.30 | 13.79 | 23.65 | 11.00 | 86.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.5 | 3.62 | 11.77 | 19.86 | 2.00 | 83.9 | 90.0 |
| Bench 4 | Bench | Aaron Wan-Bissaka | DEF | 14 | 4.5 | 3.10 | 11.55 | 20.97 | 1.00 | 85.5 | 65.0 |
| Bench 3 | Bench | Emerson Leite de Souza Junior | DEF | 18 | 4.5 | 3.61 | 10.98 | 18.48 | 1.00 | 90.9 | 2.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.16 | 21.35 | 35.54 | 2.00 | 99.5 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.5 | 4.32 | 13.78 | 23.07 | 2.00 | 73.8 | 65.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.0 | 4.61 | 13.58 | 22.89 | 5.00 | 91.2 | 73.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.5 | 5.60 | 16.35 | 27.01 | 3.00 | 94.2 | 88.0 |
| XI | XI | Rodrigo Hernandez | MID | 13 | 5.5 | 4.98 | 14.50 | 23.81 | 3.00 | 93.3 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 4.84 | 14.20 | 23.58 | 12.00 | 87.3 | 80.0 |
| Bench 2 | Bench | James Maddison | MID | 18 | 7.5 | 3.71 | 13.01 | 23.17 | 3.00 | 84.1 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.5 | 4.05 | 12.06 | 20.22 | 1.00 | 76.7 | 80.0 |

## GW3

- Train rows: 105327
- Bank: 1.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bryan Mbeumo
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 58.92
- Actual score: 37.00
- League average score: 0.00
- Transfer: Rodrigo Hernandez -> Bryan Mbeumo (projected gain 6.18, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 5.0 | 3.81 | 11.28 | 18.35 | 0.00 | 85.5 | 90.0 |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.5 | 2.36 | 9.02 | 15.90 | 5.00 | 89.1 | 90.0 |
| XI | XI | Pervis Estupiñán | DEF | 5 | 5.1 | 5.84 | 17.48 | 28.12 | 1.00 | 96.4 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.5 | 3.52 | 11.30 | 18.56 | 0.00 | 82.9 | 90.0 |
| XI | XI | Raphaël Varane | DEF | 14 | 5.0 | 3.63 | 10.67 | 17.41 | 0.00 | 79.0 | 45.0 |
| Bench 3 | Bench | Aaron Wan-Bissaka | DEF | 14 | 4.5 | 2.75 | 8.81 | 15.19 | 0.00 | 64.2 | 90.0 |
| Bench 4 | Bench | Emerson Leite de Souza Junior | DEF | 18 | 4.5 | 1.89 | 6.24 | 10.78 | 0.00 | 39.0 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 6.68 | 20.66 | 32.23 | 4.00 | 91.6 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.0 | 4.15 | 12.63 | 20.92 | 5.00 | 70.1 | 85.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.6 | 3.32 | 11.22 | 17.55 | 2.00 | 56.2 | 71.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 6.5 | 6.13 | 17.21 | 26.00 | 2.00 | 96.7 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.6 | 5.49 | 16.29 | 24.90 | 8.00 | 82.0 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 5.29 | 16.11 | 26.49 | 1.00 | 86.6 | 90.0 |
| XI | XI | James Maddison | MID | 18 | 7.5 | 4.36 | 14.01 | 23.57 | 10.00 | 79.4 | 72.0 |
| Bench 2 | Bench | Pascal Groß | MID | 5 | 6.5 | 3.20 | 9.59 | 16.18 | 10.00 | 67.1 | 90.0 |

## GW4

- Train rows: 106012
- Bank: 0.10 -> -0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 57.58
- Actual score: 74.00
- League average score: 0.00
- Transfer: Raphaël Varane -> William Saliba (projected gain 2.69, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 5.0 | 2.92 | 9.81 | 16.65 | 0.00 | 84.3 | 90.0 |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.5 | 2.48 | 8.97 | 16.11 | 0.00 | 89.7 | 90.0 |
| XI | XI | Pervis Estupiñán | DEF | 5 | 5.2 | 5.34 | 16.30 | 26.45 | 2.00 | 85.7 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.5 | 3.48 | 10.90 | 18.28 | 1.00 | 81.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.2 | 3.56 | 10.73 | 17.07 | 2.00 | 80.0 | 90.0 |
| Bench 3 | Bench | Aaron Wan-Bissaka | DEF | 14 | 4.6 | 2.27 | 8.00 | 13.70 | 1.00 | 73.0 | 90.0 |
| Bench 4 | Bench | Emerson Leite de Souza Junior | DEF | 18 | 4.5 | 1.35 | 4.26 | 7.53 | 1.00 | 26.5 | 4.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.35 | 22.09 | 35.04 | 20.00 | 94.9 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.0 | 3.96 | 12.88 | 21.29 | 2.00 | 73.2 | 72.0 |
| Bench 2 | Bench | Alexander Isak | FWD | 15 | 7.7 | 3.38 | 10.76 | 17.37 | 2.00 | 57.9 | 73.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.6 | 6.18 | 18.66 | 29.95 | 4.00 | 92.7 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.6 | 4.84 | 14.93 | 24.39 | 5.00 | 77.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.7 | 4.58 | 14.37 | 21.87 | 8.00 | 67.8 | 90.0 |
| XI | XI | James Maddison | MID | 18 | 7.6 | 4.19 | 13.18 | 22.45 | 7.00 | 69.5 | 85.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.4 | 3.83 | 11.63 | 19.75 | 3.00 | 79.0 | 88.0 |

## GW5

- Train rows: 106715
- Bank: -0.00 -> 1.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 62.21
- Actual score: 54.00
- League average score: 0.00
- Transfer: Alexander Isak -> Julián Álvarez (projected gain 2.54, hit 0)
- Autosub outfielders: Aaron Wan-Bissaka.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 5.0 | 3.14 | 9.38 | 16.30 | 2.00 | 80.8 | 90.0 |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.5 | 2.59 | 8.06 | 13.95 | 6.00 | 80.8 | 90.0 |
| XI | Bench | Pervis Estupiñán | DEF | 5 | 5.3 | 5.17 | 15.61 | 25.57 | 0.00 | 92.1 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.2 | 3.65 | 10.85 | 17.70 | 6.00 | 83.5 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.5 | 3.63 | 10.72 | 17.80 | 8.00 | 80.6 | 90.0 |
| Bench 3 | Autosub In | Aaron Wan-Bissaka | DEF | 14 | 4.6 | 3.00 | 8.38 | 13.94 | 1.00 | 73.6 | 5.0 |
| Bench 4 | Bench | Emerson Leite de Souza Junior | DEF | 18 | 4.5 | 1.10 | 3.33 | 5.96 | 1.00 | 14.9 | 1.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 8.61 | 25.25 | 40.01 | 6.00 | 116.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.6 | 4.28 | 12.72 | 20.44 | 9.00 | 80.9 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.0 | 4.20 | 12.00 | 19.78 | 5.00 | 61.9 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.7 | 6.59 | 19.10 | 30.01 | 6.00 | 95.2 | 90.0 |
| XI | XI | James Maddison | MID | 18 | 7.7 | 5.12 | 14.95 | 23.24 | 1.00 | 68.4 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.6 | 4.66 | 14.62 | 24.45 | 2.00 | 82.7 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 4.56 | 14.57 | 23.54 | 2.00 | 81.3 | 90.0 |
| Bench 2 | Bench | Pascal Groß | MID | 5 | 6.4 | 3.12 | 10.32 | 17.67 | 10.00 | 75.2 | 90.0 |

## GW6

- Train rows: 107432
- Bank: 1.10 -> 2.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 62.07
- Actual score: 86.00
- League average score: 0.00
- Transfer: André Onana -> Alphonse Areola (projected gain 1.68, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.1 | 3.27 | 11.05 | 18.64 | 2.00 | 92.0 | 90.0 |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.6 | 3.15 | 9.38 | 15.46 | 10.00 | 82.6 | 90.0 |
| XI | XI | Pervis Estupiñán | DEF | 5 | 5.3 | 4.14 | 12.43 | 20.46 | 6.00 | 55.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.5 | 3.81 | 11.34 | 18.75 | 18.00 | 81.2 | 69.0 |
| XI | XI | William Saliba | DEF | 1 | 5.2 | 3.84 | 11.29 | 18.10 | 1.00 | 86.7 | 90.0 |
| Bench 3 | Bench | Aaron Wan-Bissaka | DEF | 14 | 4.6 | 1.90 | 6.04 | 10.49 | 0.00 | 46.0 | 0.0 |
| Bench 4 | Bench | Emerson Leite de Souza Junior | DEF | 18 | 4.5 | 0.66 | 3.37 | 6.06 | 0.00 | 17.5 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.1 | 9.16 | 26.16 | 40.87 | 6.00 | 119.9 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.7 | 4.60 | 13.38 | 21.09 | 1.00 | 78.4 | 56.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.0 | 4.23 | 12.64 | 20.69 | 9.00 | 71.3 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.7 | 6.22 | 18.48 | 29.26 | 13.00 | 96.6 | 90.0 |
| XI | XI | James Maddison | MID | 18 | 7.8 | 4.79 | 15.47 | 24.45 | 9.00 | 77.6 | 77.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 4.77 | 14.03 | 22.98 | 14.00 | 76.6 | 45.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 4.10 | 12.87 | 21.77 | 1.00 | 70.9 | 90.0 |
| Bench 2 | Bench | Pascal Groß | MID | 5 | 6.3 | 3.83 | 11.23 | 19.01 | 0.00 | 80.9 | 0.0 |

## GW7

- Train rows: 108150
- Bank: 2.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 71.49
- Actual score: 47.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (10.79) beats the best remaining Triple Captain opportunity (8.74).
- League average score: 0.00
- Transfer: Pascal Groß -> Phil Foden (projected gain 0.35, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (10.79) beats the best remaining Triple Captain opportunity (8.74).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Alphonse Areola | GK | 19 | 4.1 | 3.64 | 10.83 | 18.07 | 6.00 | 89.0 | 90.0 |
| XI | XI | Bernd Leno | GK | 10 | 4.6 | 3.73 | 10.63 | 16.72 | 1.00 | 86.9 | 90.0 |
| XI | XI | Pervis Estupiñán | DEF | 5 | 5.3 | 4.71 | 14.47 | 23.37 | -2.00 | 82.7 | 45.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.5 | 4.52 | 13.32 | 21.74 | 12.00 | 85.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.2 | 3.65 | 10.76 | 17.44 | 6.00 | 87.0 | 90.0 |
| Bench 3 | Bench | Aaron Wan-Bissaka | DEF | 14 | 4.6 | 1.22 | 3.68 | 6.88 | 0.00 | 32.9 | 0.0 |
| Bench 4 | Bench | Emerson Leite de Souza Junior | DEF | 18 | 4.5 | 0.85 | 2.99 | 5.33 | 0.00 | 16.9 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.1 | 8.74 | 25.44 | 41.24 | 2.00 | 115.9 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.26 | 12.99 | 20.42 | 8.00 | 63.3 | 90.0 |
| Bench 2 | Bench | Ollie Watkins | FWD | 2 | 7.9 | 3.97 | 11.81 | 20.17 | 23.00 | 72.1 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.7 | 6.57 | 18.72 | 30.79 | 9.00 | 93.6 | 75.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 4.98 | 14.67 | 23.90 | 1.00 | 73.6 | 90.0 |
| XI | XI | James Maddison | MID | 18 | 7.9 | 4.69 | 14.37 | 24.24 | 2.00 | 79.1 | 89.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 4.03 | 12.48 | 20.92 | 2.00 | 75.4 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 7.6 | 4.14 | 11.93 | 19.57 | 2.00 | 72.0 | 90.0 |

## GW8

- Train rows: 108872
- Bank: 0.70 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Ollie Watkins
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 70.33
- Actual score: 45.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.28) beats the best remaining Bench Boost opportunity (0.00).
- League average score: 0.00
- Transfer: Emerson Leite de Souza Junior -> Joachim Andersen (projected gain 1.07, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.28) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.95 | 11.56 | 19.21 | 1.00 | 97.1 | 90.0 |
| Bench 1 | Bench Boost | Bernd Leno | GK | 10 | 4.7 | 3.40 | 9.50 | 15.00 | 2.00 | 81.9 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.7 | 4.71 | 14.86 | 24.03 | 6.00 | 86.3 | 90.0 |
| XI | XI | Pervis Estupiñán | DEF | 5 | 5.3 | 3.87 | 11.98 | 19.54 | 0.00 | 65.9 | 0.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 4.7 | 4.14 | 11.40 | 18.09 | 6.00 | 93.2 | 90.0 |
| Bench 3 | Bench Boost | William Saliba | DEF | 1 | 5.2 | 3.36 | 10.46 | 17.20 | 7.00 | 86.8 | 90.0 |
| Bench 4 | Bench Boost | Aaron Wan-Bissaka | DEF | 14 | 4.5 | 1.10 | 3.33 | 5.99 | 0.00 | 23.1 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.1 | 7.15 | 22.96 | 38.32 | 2.00 | 99.3 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 7.9 | 5.72 | 16.21 | 26.34 | 5.00 | 93.6 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 7.0 | 4.06 | 13.58 | 22.79 | 2.00 | 80.2 | 67.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.7 | 5.29 | 17.13 | 29.34 | 0.00 | 75.7 | 0.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.6 | 4.62 | 13.72 | 21.98 | 2.00 | 74.6 | 90.0 |
| XI | XI | James Maddison | MID | 18 | 7.9 | 4.43 | 13.52 | 23.19 | 6.00 | 73.5 | 75.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 3.94 | 12.43 | 20.96 | 2.00 | 77.2 | 90.0 |
| Bench 2 | Bench Boost | Phil Foden | MID | 13 | 7.6 | 3.42 | 11.22 | 18.54 | 2.00 | 71.8 | 90.0 |