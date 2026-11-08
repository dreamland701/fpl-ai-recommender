# Classic ridge with vs without the bookmaker market features, 84 walk-forward weeks

- 1GW (n 65505): base: RMSE 1.9592, MAE 0.9906, bias -0.012, top-decile actual 4.001 | mkt: RMSE 1.9555, MAE 0.9857, bias -0.016, top-decile actual 4.037
- 3GW (n 63824): base: RMSE 4.0481, MAE 2.3798, bias -0.021, top-decile actual 10.919 | mkt: RMSE 4.0388, MAE 2.3678, bias -0.029, top-decile actual 10.912
- 5GW (n 60494): base: RMSE 5.9256, MAE 3.6481, bias -0.028, top-decile actual 17.612 | mkt: RMSE 5.9144, MAE 3.6389, bias -0.031, top-decile actual 17.575
- Appearance AUC: base 0.9307 | mkt 0.9310
- 1GW GK+DEF (n 28754): RMSE base 1.8486 | mkt 1.8410
- 1GW MID+FWD (n 36491): RMSE base 1.9732 | mkt 1.9705
- 1GW price >= 10 (n 501): RMSE base 4.7419 | mkt 4.7569
- 1GW minutes_avg high (played 60+ this week) (n 16956): RMSE base 3.3967 | mkt 3.3872
- 1GW RMSE: market model better in 55/84 weeks

GK/DEF who played 60+, by market clean-sheet probability tercile: mean forecast (base / mkt) vs actual

| tercile | n | cs prob | base | mkt | actual |
|---|---|---|---|---|---|
| 1 | 2698 | 0.13 | 2.01 | 1.90 | 2.38 |
| 2 | 2696 | 0.25 | 2.38 | 2.36 | 3.36 |
| 3 | 2699 | 0.40 | 2.83 | 2.99 | 4.17 |

Mean standardized 1GW ridge coefficient of each market column across the 84 fits:

- mkt_team_xg: +0.0507
- mkt_opp_xg: +0.0292
- mkt_cs_prob: -0.0097
- mkt_win_prob: +0.0258
- mkt_available: +0.0000
- mkt_xg_x_xgi_5: -0.0242
- mkt_xg_x_minutes_3: -0.0772
- mkt_cs_x_minutes_3: +0.3344
