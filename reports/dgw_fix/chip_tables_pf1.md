# Double-gameweek fix: closed-loop half-season totals

Planner = disciplined auto transfer + the 5-week chip rule, closed loop over the half. Chips = (week, chip) the planner played. Hindsight = best chip weeks knowing outcomes (TC+BB only / all four). DGW = weeks with >=20% of players doubling.

| half | DGW weeks | planner base | planner fix | Δ | no-chips base | no-chips fix | base chips | fix chips | hindsight TC+BB base / fix | hindsight all base / fix |
|---|---|---|---|---|---|---|---|---|---|---|
| 2020-21:1 | [19] | 1013 | 1009 | -4 | 1001 | 987 | [[2, 'bench_boost'], [5, 'triple_captain']] | [[2, 'bench_boost'], [4, 'triple_captain']] | 1035 / 1028 | 1102 / 1099 |
| 2020-21:2 | [26, 35] | 1129 | 1132 | +3 | 1118 | 1119 | [[21, 'triple_captain'], [23, 'bench_boost']] | [[20, 'triple_captain'], [21, 'bench_boost']] | 1156 / 1156 | 1201 / 1218 |
| 2021-22:1 | [] | 1000 | 1000 | +0 | 977 | 977 | [[2, 'triple_captain'], [9, 'bench_boost']] | [[2, 'triple_captain'], [9, 'bench_boost']] | 1018 / 1018 | 1093 / 1087 |
| 2021-22:2 | [26, 28, 29, 33, 36, 37] | 1095 | 1082 | -13 | 1074 | 1068 | [[22, 'triple_captain'], [23, 'bench_boost']] | [[20, 'triple_captain'], [23, 'bench_boost']] | 1112 / 1103 | 1306 / 1346 |
| 2022-23:1 | [] | 836 | 848 | +12 | 834 | 843 | [[2, 'triple_captain'], [11, 'bench_boost']] | [[2, 'triple_captain'], [10, 'bench_boost']] | 856 / 865 | 1092 / 1090 |
| 2022-23:2 | [29, 34, 37] | 1078 | 1088 | +10 | 1076 | 1072 | [[24, 'triple_captain'], [29, 'bench_boost']] | [[20, 'triple_captain'], [23, 'bench_boost']] | 1109 / 1105 | 1284 / 1287 |
| 2023-24:1 | [] | 1074 | 1067 | -7 | 1064 | 1063 | [[2, 'triple_captain'], [18, 'bench_boost']] | [[2, 'triple_captain'], [19, 'bench_boost']] | 1104 / 1103 | 1112 / 1112 |
| 2023-24:2 | [34, 37] | 1189 | 1203 | +14 | 1162 | 1178 | [[20, 'triple_captain'], [22, 'bench_boost']] | [[20, 'triple_captain'], [22, 'bench_boost']] | 1218 / 1234 | 1349 / 1369 |
| 2024-25:1 | [] | 1098 | 1118 | +20 | 1085 | 1105 | [[2, 'triple_captain'], [7, 'bench_boost']] | [[2, 'triple_captain'], [7, 'bench_boost']] | 1127 / 1147 | 1192 / 1212 |
| 2024-25:2 | [] | 1061 | 1067 | +6 | 1038 | 1044 | [[20, 'triple_captain'], [24, 'bench_boost']] | [[20, 'triple_captain'], [24, 'bench_boost']] | 1094 / 1100 | 1227 / 1233 |
| 2025-26:1 | [] | 999 | 998 | -1 | 988 | 984 | [[2, 'triple_captain'], [15, 'bench_boost']] | [[2, 'bench_boost'], [4, 'triple_captain']] | 1017 / 1013 | 1097 / 1110 |
| 2025-26:2 | [33] | 1206 | 1213 | +7 | 1192 | 1199 | [[20, 'triple_captain'], [23, 'bench_boost']] | [[20, 'triple_captain'], [23, 'bench_boost']] | 1235 / 1238 | 1297 / 1292 |

## Triple captain + bench boost, additive on the no-chip path

| half | variant | planner weeks | planner TC+BB | schedule-rule weeks | schedule-rule TC+BB | hindsight TC+BB |
|---|---|---|---|---|---|---|
| 2020-21:1 | base | TC 5, BB 2 | 12 | TC 19, BB 2 | 10 | 34 |
| 2020-21:1 | fix | TC 4, BB 2 | 22 | TC 19, BB 2 | 17 | 41 |
| 2020-21:2 | base | TC 21, BB 23 | 11 | TC 26, BB 35 | 25 | 38 |
| 2020-21:2 | fix | TC 20, BB 21 | 13 | TC 26, BB 35 | 24 | 37 |
| 2021-22:1 | base | TC 2, BB 9 | 23 | TC 2, BB 9 | 23 | 41 |
| 2021-22:1 | fix | TC 2, BB 9 | 23 | TC 2, BB 9 | 23 | 41 |
| 2021-22:2 | base | TC 22, BB 23 | 21 | TC 36, BB 26 | 34 | 38 |
| 2021-22:2 | fix | TC 20, BB 23 | 14 | TC 36, BB 26 | 34 | 35 |
| 2022-23:1 | base | TC 2, BB 11 | 2 | TC 2, BB 11 | 2 | 22 |
| 2022-23:1 | fix | TC 2, BB 10 | 5 | TC 2, BB 10 | 5 | 22 |
| 2022-23:2 | base | TC 24, BB 29 | 2 | TC 29, BB 34 | 14 | 33 |
| 2022-23:2 | fix | TC 20, BB 23 | 16 | TC 29, BB 34 | 14 | 33 |
| 2023-24:1 | base | TC 2, BB 18 | 10 | TC 2, BB 18 | 10 | 40 |
| 2023-24:1 | fix | TC 2, BB 19 | 4 | TC 2, BB 19 | 4 | 40 |
| 2023-24:2 | base | TC 20, BB 22 | 27 | TC 34, BB 37 | 21 | 56 |
| 2023-24:2 | fix | TC 20, BB 22 | 25 | TC 34, BB 37 | 22 | 56 |
| 2024-25:1 | base | TC 2, BB 7 | 13 | TC 2, BB 7 | 13 | 42 |
| 2024-25:1 | fix | TC 2, BB 7 | 13 | TC 2, BB 7 | 13 | 42 |
| 2024-25:2 | base | TC 20, BB 24 | 23 | TC 20, BB 24 | 23 | 56 |
| 2024-25:2 | fix | TC 20, BB 24 | 23 | TC 20, BB 24 | 23 | 56 |
| 2025-26:1 | base | TC 2, BB 15 | 11 | TC 2, BB 15 | 11 | 29 |
| 2025-26:1 | fix | TC 4, BB 2 | 14 | TC 4, BB 2 | 14 | 29 |
| 2025-26:2 | base | TC 20, BB 23 | 14 | TC 33, BB 23 | 15 | 43 |
| 2025-26:2 | fix | TC 20, BB 23 | 14 | TC 33, BB 23 | 14 | 39 |

Halves built: 12. Planner Δ total +47 (mean +3.9, 7 up / 4 down); no-chips Δ total +30 (transfers + captain only).
