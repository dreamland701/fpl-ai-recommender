# Double-gameweek fix: closed-loop half-season totals

Planner = disciplined auto transfer + the 5-week chip rule, closed loop over the half. Chips = (week, chip) the planner played. Hindsight = best chip weeks knowing outcomes (TC+BB only / all four). DGW = weeks with >=20% of players doubling.

| half | DGW weeks | planner base | planner fix | Δ | no-chips base | no-chips fix | base chips | fix chips | hindsight TC+BB base / fix | hindsight all base / fix |
|---|---|---|---|---|---|---|---|---|---|---|
| 2020-21:1 | [19] | 1013 | 942 | -71 | 1001 | 931 | [[2, 'bench_boost'], [5, 'triple_captain']] | [[2, 'bench_boost'], [6, 'triple_captain']] | 1035 / 964 | 1102 / 1114 |
| 2020-21:2 | [26, 35] | 1129 | 1087 | -42 | 1118 | 1061 | [[21, 'triple_captain'], [23, 'bench_boost']] | [[21, 'bench_boost'], [24, 'triple_captain']] | 1156 / 1101 | 1201 / 1225 |
| 2021-22:1 | [] | 1000 | 1027 | +27 | 977 | 1010 | [[2, 'triple_captain'], [9, 'bench_boost']] | [[2, 'bench_boost'], [4, 'triple_captain']] | 1018 / 1047 | 1093 / 1094 |
| 2021-22:2 | [26, 28, 29, 33, 36, 37] | 1095 | 1157 | +62 | 1074 | 1148 | [[22, 'triple_captain'], [23, 'bench_boost']] | [[21, 'triple_captain'], [26, 'bench_boost']] | 1112 / 1194 | 1306 / 1427 |
| 2022-23:1 | [] | 836 | 890 | +54 | 834 | 883 | [[2, 'triple_captain'], [11, 'bench_boost']] | [[2, 'triple_captain'], [5, 'bench_boost']] | 856 / 910 | 1092 / 1116 |
| 2022-23:2 | [29, 34, 37] | 1078 | 1173 | +95 | 1076 | 1153 | [[24, 'triple_captain'], [29, 'bench_boost']] | [[22, 'bench_boost'], [23, 'triple_captain']] | 1109 / 1191 | 1284 / 1321 |
| 2023-24:1 | [] | 1074 | 1020 | -54 | 1064 | 1011 | [[2, 'triple_captain'], [18, 'bench_boost']] | [[2, 'triple_captain'], [17, 'bench_boost']] | 1104 / 1047 | 1112 / 1118 |
| 2023-24:2 | [34, 37] | 1189 | 1307 | +118 | 1162 | 1286 | [[20, 'triple_captain'], [22, 'bench_boost']] | [[20, 'triple_captain'], [22, 'bench_boost']] | 1218 / 1333 | 1349 / 1413 |
| 2024-25:1 | [] | 1098 | 1128 | +30 | 1085 | 1114 | [[2, 'triple_captain'], [7, 'bench_boost']] | [[2, 'triple_captain'], [3, 'bench_boost']] | 1127 / 1156 | 1192 / 1251 |
| 2024-25:2 | [] | 1061 | 1196 | +135 | 1038 | 1161 | [[20, 'triple_captain'], [24, 'bench_boost']] | [[24, 'triple_captain'], [26, 'bench_boost']] | 1094 / 1220 | 1227 / 1306 |
| 2025-26:1 | [] | 999 | 1000 | +1 | 988 | 986 | [[2, 'triple_captain'], [15, 'bench_boost']] | [[2, 'bench_boost'], [4, 'triple_captain']] | 1017 / 1036 | 1097 / 1134 |
| 2025-26:2 | [33] | 1206 | 1182 | -24 | 1192 | 1166 | [[20, 'triple_captain'], [23, 'bench_boost']] | [[20, 'triple_captain'], [23, 'bench_boost']] | 1235 / 1198 | 1297 / 1279 |

## Triple captain + bench boost, additive on the no-chip path

| half | variant | planner weeks | planner TC+BB | schedule-rule weeks | schedule-rule TC+BB | hindsight TC+BB |
|---|---|---|---|---|---|---|
| 2020-21:1 | base | TC 5, BB 2 | 12 | TC 19, BB 2 | 10 | 34 |
| 2020-21:1 | fix | TC 6, BB 2 | 11 | TC 19, BB 2 | 17 | 33 |
| 2020-21:2 | base | TC 21, BB 23 | 11 | TC 26, BB 35 | 25 | 38 |
| 2020-21:2 | fix | TC 24, BB 21 | 26 | TC 26, BB 35 | 27 | 40 |
| 2021-22:1 | base | TC 2, BB 9 | 23 | TC 2, BB 9 | 23 | 41 |
| 2021-22:1 | fix | TC 4, BB 2 | 17 | TC 4, BB 2 | 17 | 37 |
| 2021-22:2 | base | TC 22, BB 23 | 21 | TC 36, BB 26 | 34 | 38 |
| 2021-22:2 | fix | TC 21, BB 26 | 9 | TC 36, BB 26 | 6 | 46 |
| 2022-23:1 | base | TC 2, BB 11 | 2 | TC 2, BB 11 | 2 | 22 |
| 2022-23:1 | fix | TC 2, BB 5 | 7 | TC 2, BB 5 | 7 | 27 |
| 2022-23:2 | base | TC 24, BB 29 | 2 | TC 29, BB 34 | 14 | 33 |
| 2022-23:2 | fix | TC 23, BB 22 | 20 | TC 29, BB 34 | 15 | 38 |
| 2023-24:1 | base | TC 2, BB 18 | 10 | TC 2, BB 18 | 10 | 40 |
| 2023-24:1 | fix | TC 2, BB 17 | 9 | TC 2, BB 17 | 9 | 36 |
| 2023-24:2 | base | TC 20, BB 22 | 27 | TC 34, BB 37 | 21 | 56 |
| 2023-24:2 | fix | TC 20, BB 22 | 21 | TC 34, BB 37 | 22 | 47 |
| 2024-25:1 | base | TC 2, BB 7 | 13 | TC 2, BB 7 | 13 | 42 |
| 2024-25:1 | fix | TC 2, BB 3 | 14 | TC 2, BB 3 | 14 | 42 |
| 2024-25:2 | base | TC 20, BB 24 | 23 | TC 20, BB 24 | 23 | 56 |
| 2024-25:2 | fix | TC 24, BB 26 | 35 | TC 24, BB 26 | 35 | 59 |
| 2025-26:1 | base | TC 2, BB 15 | 11 | TC 2, BB 15 | 11 | 29 |
| 2025-26:1 | fix | TC 4, BB 2 | 14 | TC 4, BB 2 | 14 | 50 |
| 2025-26:2 | base | TC 20, BB 23 | 14 | TC 33, BB 23 | 15 | 43 |
| 2025-26:2 | fix | TC 20, BB 23 | 16 | TC 33, BB 23 | 13 | 32 |

Halves built: 12. Planner Δ total +331 (mean +27.6, 8 up / 4 down); no-chips Δ total +301 (transfers + captain only).
