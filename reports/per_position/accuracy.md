# Classic ridge with vs without [], 84 walk-forward weeks

- 1GW (n 65505): base: RMSE 1.9491, MAE 0.9972, bias +0.011, top-decile actual 4.053 | mkt: RMSE 1.9455, MAE 0.9909, bias +0.011, top-decile actual 4.045
- 3GW (n 63824): base: RMSE 4.0189, MAE 2.3854, bias +0.031, top-decile actual 11.005 | mkt: RMSE 4.0021, MAE 2.3614, bias +0.029, top-decile actual 11.043
- 5GW (n 60494): base: RMSE 5.8840, MAE 3.6511, bias +0.045, top-decile actual 17.685 | mkt: RMSE 5.8490, MAE 3.6057, bias +0.036, top-decile actual 17.775
- Appearance AUC: base 0.9356 | mkt 0.9364
- 1GW GK+DEF (n 28754): RMSE base 1.8431 | mkt 1.8410
- 1GW MID+FWD (n 36491): RMSE base 1.9658 | mkt 1.9610
- 1GW price >= 10 (n 501): RMSE base 4.6445 | mkt 4.5842
- 1GW minutes_avg high (played 60+ this week) (n 16956): RMSE base 3.3846 | mkt 3.3775
- 1GW RMSE: market model better in 57/84 weeks

GK/DEF who played 60+, by market clean-sheet probability tercile: mean forecast (base / mkt) vs actual

| tercile | n | cs prob | base | mkt | actual |
|---|---|---|---|---|---|
| 1 | 0 | nan | nan | nan | nan |
| 2 | 0 | nan | nan | nan | nan |
| 3 | 8093 | 0.00 | 2.43 | 2.51 | 3.31 |

Mean standardized 1GW ridge coefficient of each market column across the 84 fits:

