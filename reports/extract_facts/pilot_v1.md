# Extractor pilot: e4b, 31b, haiku, haiku_v2 on 60 prose documents + 30 lineups team blocks

## Throughput and form

| arm | docs | parse ok | truncated | facts/doc (prose) | docs with 0 facts (prose) | tokens out p50 | s/doc |
|---|---|---|---|---|---|---|---|
| e4b | 90 | 99% | 1 | 8.1 | 14 | 268 | 22.2 |
| 31b | 90 | 100% | 0 | 2.1 | 14 | 92 | 61.9 |
| haiku | 90 | 100% | 0 | 1.8 | 20 | - | - |
| haiku_v2 | 90 | 100% | 0 | 2.0 | 21 | - | - |

## Team blocks against the parser truth (Subs from = bench, Doubtful = doubt, Injured/Suspended = out)

| arm | blocks | precision | recall | name recall | tp | fp | fn | main confusions |
|---|---|---|---|---|---|---|---|---|
| e4b | 30 | 0.75 | 0.23 | 0.30 | 220 | 75 | 748 | bench->missed 667, out->doubt 69, out->missed 6, doubt->missed 2 |
| 31b | 30 | 0.99 | 0.29 | 0.29 | 281 | 2 | 687 | bench->missed 680, out->missed 6, not listed->out 1, out->doubt 1 |
| haiku | 30 | 0.95 | 0.67 | 0.70 | 649 | 35 | 319 | bench->missed 284, doubt->bench 31, out->missed 2, out->bench 1 |
| haiku_v2 | 30 | 0.95 | 0.95 | 1.00 | 918 | 50 | 50 | doubt->bench 45, out->bench 3, out->missed 2, not listed->out 1 |

## Prose documents: agreement between arms (mean Jaccard per document, documents where either arm found facts)

| pair | docs | (name, status) | names only |
|---|---|---|---|
| e4b vs 31b | 51 | 0.19 | 0.30 |
| e4b vs haiku | 49 | 0.18 | 0.26 |
| e4b vs haiku_v2 | 49 | 0.21 | 0.29 |
| 31b vs haiku | 48 | 0.52 | 0.59 |
| 31b vs haiku_v2 | 47 | 0.49 | 0.60 |
| haiku vs haiku_v2 | 42 | 0.74 | 0.78 |

## Outcome validity on prose documents (facts joined to the next gameweek's minutes)

| arm | status | facts | matched to a player | appeared | started |
|---|---|---|---|---|---|
| e4b | xi | 336 | 254 | 87% | 69% |
| e4b | bench | 21 | 13 | 85% | 54% |
| e4b | doubt | 21 | 17 | 59% | 47% |
| e4b | out | 59 | 51 | 29% | 22% |
| e4b | return | 16 | 12 | 83% | 67% |
| e4b | role | 28 | 21 | 81% | 48% |
| e4b | other | 5 | 4 | 75% | 75% |
| 31b | xi | 26 | 24 | 100% | 88% |
| 31b | bench | 7 | 7 | 57% | 0% |
| 31b | doubt | 24 | 18 | 61% | 39% |
| 31b | out | 40 | 38 | 13% | 5% |
| 31b | return | 16 | 15 | 80% | 60% |
| 31b | role | 12 | 10 | 100% | 60% |
| haiku | xi | 16 | 14 | 93% | 86% |
| haiku | bench | 5 | 5 | 40% | 0% |
| haiku | doubt | 11 | 9 | 67% | 67% |
| haiku | out | 46 | 39 | 10% | 8% |
| haiku | return | 19 | 17 | 71% | 53% |
| haiku | role | 11 | 8 | 100% | 88% |
| haiku_v2 | xi | 24 | 21 | 95% | 81% |
| haiku_v2 | bench | 4 | 4 | 50% | 0% |
| haiku_v2 | doubt | 17 | 12 | 58% | 58% |
| haiku_v2 | out | 41 | 34 | 9% | 6% |
| haiku_v2 | return | 19 | 17 | 71% | 53% |
| haiku_v2 | role | 17 | 14 | 100% | 79% |

## Disagreement cases for a hand audit (first 10)

**2022-23 GW31 guardian 134.1h** Aaron Ramsdale saves everything for Arsenal to keep title challenge alive  
- e4b: Aaron Ramsdale [xi] saved everything for Arsenal to keep title challenge alive; Ibrahima Konaté [xi] launched his chest at a cross and seemed certain to score; Mohamed Salah [xi] step inside and leaping claw-away as Mohamed Salah went for the far corner; Darwin Núñez [xi] block from Darwin Núñez, who ran on to the perfect pass from Salah; Gabriel Martinelli [xi] scored the opener, a goal made by a turn from Bukayo Saka; Bukayo Saka [xi] a goal made by a turn from Bukayo Saka; Andy Robertson [xi] fell over trying to follow him; Gabriel Jesus [xi] the header from Gabriel Jesus precise; Trent Alexander-Arnold [xi] stepped into midfield and began to unfurl those 30- to 40-yard passes; Oleksandr Zinchenko [xi] Alexander-Arnold made the difference deep into the second half, nutmegging Oleksandr Zinchenko  
- 31b: (none)  
- haiku: (none)  
- haiku_v2: (none)  

**2022-23 GW3 guardian 136.2h** Kane snatches draw for Spurs at Chelsea as clashing Conte and Tuchel see red  
- e4b: Harry Kane [xi] Spurs had just rescued an undeserved draw through Harry Kane’s deflected header; Pierre-Emile Højbjerg [xi] controversial first equaliser by Pierre-Emile Højbjerg; Kalidou Koulibaly [xi] Kalidou Koulibaly’s wonderfully executed volley in the 19th minute; N’Golo Kanté [xi] several clones of N’Golo Kanté seem to have invaded the pitch; Kai Havertz [xi] challenge on a marauding Kai Havertz; Richarlison [xi] offside Richarlison had obscured Édouard Mendy’s line of sight; Édouard Mendy [xi] offside Richarlison had obscured Édouard Mendy’s line of sight; Reece James [xi] Havertz somehow failed to convert a Reece James cross; Raheem Sterling [xi] via Kanté and the impressive Raheem Sterling, the ball was spirited; Dejan Kulusevski [xi] Dejan Kulusevski was pressed into conceding possession  
- 31b: (none)  
- haiku: (none)  
- haiku_v2: (none)  

**2022-23 GW4 guardian 12.5h** Harry Maguire not guaranteed return to Manchester United team, says Ten Hag  
- e4b: Harry Maguire [doubt] not guaranteed return to the team; Raphaël Varane [xi] impressed in central defence with Lisandro Martínez; Lisandro Martínez [xi] impressed in central defence with Raphaël Varane; Bruno Fernandes [role] captained United against Liverpool; Jadon Sancho [xi] United’s goals against Liverpool were scored by; Marcus Rashford [xi] United’s goals against Liverpool were scored by; Casemiro [role] Ten Hag may give Casemiro his debut at Southampton  
- 31b: Harry Maguire [bench] not guaranteed return to the team; Raphaël Varane [xi] dropped in favour of the Frenchman; Casemiro [role] may give Casemiro his debut at Southampton  
- haiku: Harry Maguire [bench] Maguire was dropped in favour of the Frenchman for Monday's 2-1 win; Casemiro [role] Ten Hag may give Casemiro his debut at Southampton  
- haiku_v2: Harry Maguire [bench] status as captain offers no guarantee of a return to the team; Casemiro [role] Ten Hag may give Casemiro his debut at Southampton  

**2022-23 GW14 guardian 108.9h** Bournemouth’s O’Neil fumes as Zouma and Benrahma strike for West Ham  
- e4b: Dominic Solanke [out] injuries to key striker Dominic Solanke; Neto [out] first-choice goalkeeper Neto; Thilo Kehrer [xi] handball in the buildup to Kurt Zouma’s opening goal; Kurt Zouma [xi] opening goal; Jordan Zemura [xi] handball that led to Saïd Benrahma’s late, decisive penalty; Saïd Benrahma [xi] late, decisive penalty; Jefferson Lerma [xi] high lunge on Gianluca Scamacca; Gianluca Scamacca [xi] Lerma’s high lunge on Gianluca Scamacca; Lukasz Fabianski [xi] came at the cost of injuries to key striker Dominic Solanke; Flynn Downes [xi] aggression and runs from deep in support of Scamacca  
- 31b: Dominic Solanke [out] we have to go without him; Neto [out] pulled up with a muscle injury  
- haiku: Dominic Solanke [out] we have to go without him  
- haiku_v2: Dominic Solanke [out] we have to go without him; Neto [doubt] pulled up with a muscle injury  

**2022-23 GW38 guardian 114.0h** Julen Lopetegui to hold more talks amid doubts over his future at Wolves  
- e4b: (none)  
- 31b: Ruben Neves [out] among those set to depart  
- haiku: (none)  
- haiku_v2: (none)  

**2022-23 GW30 guardian 159.3h** Gabriel Jesus has the spellbinding quality that keeps everyone watching  
- e4b: Gabriel Jesus [xi] This was Jesus’s first league start in almost four months.; Ben White [xi] ; Leandro Trossard [xi] ; Aaron Ramsdale [xi] ; Granit Xhaka [xi] ; Eddie Nketiah [xi] Occasionally it would be Eddie Nketiah holding the ball up  
- 31b: Gabriel Jesus [return] first league start in almost four months  
- haiku: Gabriel Jesus [return] This was Jesus's first league start in almost four months  
- haiku_v2: (none)  

**2022-23 GW35 guardian 164.2h** Josh Dasilva stuns Nottingham Forest to snatch late victory for Brentford  
- e4b: (none)  
- 31b: Danilo [doubt] off the pitch injured  
- haiku: (none)  
- haiku_v2: Danilo [doubt] With Danilo off the pitch injured  

**2022-23 GW30 guardian 12.5h** Pep Guardiola reveals shift in formation as reason for Kyle Walker’s City absence  
- e4b: Kyle Walker [bench] a change in formation and the form of others are keeping him on the bench.; Erling Haaland [return] returned from injury.; John Stones [role] has moved into defensive midfield alongside Rodri; Manuel Akanji [role] is the preferred choice on the right of the back three  
- 31b: Kyle Walker [bench] keeping him on the bench; Erling Haaland [return] returned to full training in midweek  
- haiku: Kyle Walker [bench] Walker looks unlikely to start at St Mary's; Erling Haaland [return] The striker returned to full training in midweek; John Stones [role] The centre-back John Stones has moved into defensive midfield alongside Rodri; Manuel Akanji [xi] Manuel Akanji is the preferred choice on the right  
- haiku_v2: Kyle Walker [bench] Walker looks unlikely to start at St Mary's; Erling Haaland [return] returned to full training in midweek; John Stones [role] has moved into defensive midfield alongside Rodri; Manuel Akanji [xi] the preferred choice on the right of the back three  

**2023-24 GW14 guardian 1.5h** Moisés Caicedo’s difficult start rooted in Chelsea’s puzzle-piece structure  
- e4b: Moisés Caicedo [bench] perhaps it was no coincidence that Caicedo was on the bench for the defeat at Newcastle.; Declan Rice [other:null] ; Lesley Ugochukwu [xi] you start Lesley Ugochukwu at Newcastle and lose 4-1.; Reece James [out] getting himself sent off for two yellow cards; Thiago Silva [other:null] giving away a comedy goal; Christopher Nkunku [return] impending return from a knee injury; Ivan Toney [other:null] possibility of Chelsea spending big on Ivan Toney; Victor Osimhen [other:null] possibility of Chelsea spending big on Victor Osimhen; Mykhailo Mudryk [other:null] pipped Arsenal to Mykhailo Mudryk.; Enzo Fernández [xi] energetic midfield trio with Enzo Fernández and Conor Gallagher.  
- 31b: Christopher Nkunku [return] impending return from a knee injury  
- haiku: Christopher Nkunku [return] Christopher Nkunku's impending return from a knee injury  
- haiku_v2: Christopher Nkunku [return] impending return from a knee injury  

**2023-24 GW15 guardian 49.5h** Ten-man Chelsea hold on to beat Brighton after Enzo Fernández double  
- e4b: Conor Gallagher [out] got himself sent off just before half-time; Levi Colwill [xi] almost giving away a penalty in the 110th minute; Thiago Silva [xi] making a crucial challenge as Brighton pushed for a late equaliser; Robert Sánchez [xi] made some important stops; Enzo Fernández [xi] score the hosts decisive third goal from the spot; James Milner [xi] challenge on Mykhailo Mudryk; Mykhailo Mudryk [xi] Mudryk had gone close; Axel Disasi [role] naming Axel Disasi at right-back; Moisés Caicedo [xi] ignored the boos from the away end and offered control; Raheem Sterling [xi] tested Brighton on the right  
- 31b: Conor Gallagher [out] got himself sent off just before half-time; Reece James [out] unavailable after his dismissal against Newcastle  
- haiku: (none)  
- haiku_v2: (none)  

