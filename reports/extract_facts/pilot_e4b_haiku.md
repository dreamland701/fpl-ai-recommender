# Extractor pilot: e4b, haiku on 60 prose documents + 30 lineups team blocks

## Throughput and form

| arm | docs | parse ok | truncated | facts/doc (prose) | docs with 0 facts (prose) | tokens out p50 | s/doc |
|---|---|---|---|---|---|---|---|
| e4b | 90 | 99% | 1 | 8.1 | 14 | 268 | 22.2 |
| haiku | 90 | 100% | 0 | 1.8 | 20 | - | - |

## Team blocks against the parser truth (Subs from = bench, Doubtful = doubt, Injured/Suspended = out)

| arm | blocks | precision | recall | name recall | tp | fp | fn | main confusions |
|---|---|---|---|---|---|---|---|---|
| e4b | 30 | 0.75 | 0.23 | 0.30 | 220 | 75 | 748 | bench->missed 667, out->doubt 69, out->missed 6, doubt->missed 2 |
| haiku | 30 | 0.95 | 0.67 | 0.70 | 649 | 35 | 319 | bench->missed 284, doubt->bench 31, out->missed 2, out->bench 1 |

## Prose documents: agreement between arms (mean Jaccard per document, documents where either arm found facts)

| pair | docs | (name, status) | names only |
|---|---|---|---|
| e4b vs haiku | 49 | 0.18 | 0.26 |

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
| haiku | xi | 16 | 14 | 93% | 86% |
| haiku | bench | 5 | 5 | 40% | 0% |
| haiku | doubt | 11 | 9 | 67% | 67% |
| haiku | out | 46 | 39 | 10% | 8% |
| haiku | return | 19 | 17 | 71% | 53% |
| haiku | role | 11 | 8 | 100% | 88% |

## Disagreement cases for a hand audit (first 6)

**2022-23 GW31 guardian 134.1h** Aaron Ramsdale saves everything for Arsenal to keep title challenge alive  
- e4b: Aaron Ramsdale [xi] saved everything for Arsenal to keep title challenge alive; Ibrahima Konaté [xi] launched his chest at a cross and seemed certain to score; Mohamed Salah [xi] step inside and leaping claw-away as Mohamed Salah went for the far corner; Darwin Núñez [xi] block from Darwin Núñez, who ran on to the perfect pass from Salah; Gabriel Martinelli [xi] scored the opener, a goal made by a turn from Bukayo Saka; Bukayo Saka [xi] a goal made by a turn from Bukayo Saka; Andy Robertson [xi] fell over trying to follow him; Gabriel Jesus [xi] the header from Gabriel Jesus precise; Trent Alexander-Arnold [xi] stepped into midfield and began to unfurl those 30- to 40-yard passes; Oleksandr Zinchenko [xi] Alexander-Arnold made the difference deep into the second half, nutmegging Oleksandr Zinchenko  
- haiku: (none)  

**2022-23 GW3 guardian 136.2h** Kane snatches draw for Spurs at Chelsea as clashing Conte and Tuchel see red  
- e4b: Harry Kane [xi] Spurs had just rescued an undeserved draw through Harry Kane’s deflected header; Pierre-Emile Højbjerg [xi] controversial first equaliser by Pierre-Emile Højbjerg; Kalidou Koulibaly [xi] Kalidou Koulibaly’s wonderfully executed volley in the 19th minute; N’Golo Kanté [xi] several clones of N’Golo Kanté seem to have invaded the pitch; Kai Havertz [xi] challenge on a marauding Kai Havertz; Richarlison [xi] offside Richarlison had obscured Édouard Mendy’s line of sight; Édouard Mendy [xi] offside Richarlison had obscured Édouard Mendy’s line of sight; Reece James [xi] Havertz somehow failed to convert a Reece James cross; Raheem Sterling [xi] via Kanté and the impressive Raheem Sterling, the ball was spirited; Dejan Kulusevski [xi] Dejan Kulusevski was pressed into conceding possession  
- haiku: (none)  

**2022-23 GW4 guardian 12.5h** Harry Maguire not guaranteed return to Manchester United team, says Ten Hag  
- e4b: Harry Maguire [doubt] not guaranteed return to the team; Raphaël Varane [xi] impressed in central defence with Lisandro Martínez; Lisandro Martínez [xi] impressed in central defence with Raphaël Varane; Bruno Fernandes [role] captained United against Liverpool; Jadon Sancho [xi] United’s goals against Liverpool were scored by; Marcus Rashford [xi] United’s goals against Liverpool were scored by; Casemiro [role] Ten Hag may give Casemiro his debut at Southampton  
- haiku: Harry Maguire [bench] Maguire was dropped in favour of the Frenchman for Monday's 2-1 win; Casemiro [role] Ten Hag may give Casemiro his debut at Southampton  

**2022-23 GW14 guardian 108.9h** Bournemouth’s O’Neil fumes as Zouma and Benrahma strike for West Ham  
- e4b: Dominic Solanke [out] injuries to key striker Dominic Solanke; Neto [out] first-choice goalkeeper Neto; Thilo Kehrer [xi] handball in the buildup to Kurt Zouma’s opening goal; Kurt Zouma [xi] opening goal; Jordan Zemura [xi] handball that led to Saïd Benrahma’s late, decisive penalty; Saïd Benrahma [xi] late, decisive penalty; Jefferson Lerma [xi] high lunge on Gianluca Scamacca; Gianluca Scamacca [xi] Lerma’s high lunge on Gianluca Scamacca; Lukasz Fabianski [xi] came at the cost of injuries to key striker Dominic Solanke; Flynn Downes [xi] aggression and runs from deep in support of Scamacca  
- haiku: Dominic Solanke [out] we have to go without him  

**2022-23 GW30 guardian 159.3h** Gabriel Jesus has the spellbinding quality that keeps everyone watching  
- e4b: Gabriel Jesus [xi] This was Jesus’s first league start in almost four months.; Ben White [xi] ; Leandro Trossard [xi] ; Aaron Ramsdale [xi] ; Granit Xhaka [xi] ; Eddie Nketiah [xi] Occasionally it would be Eddie Nketiah holding the ball up  
- haiku: Gabriel Jesus [return] This was Jesus's first league start in almost four months  

**2022-23 GW30 guardian 12.5h** Pep Guardiola reveals shift in formation as reason for Kyle Walker’s City absence  
- e4b: Kyle Walker [bench] a change in formation and the form of others are keeping him on the bench.; Erling Haaland [return] returned from injury.; John Stones [role] has moved into defensive midfield alongside Rodri; Manuel Akanji [role] is the preferred choice on the right of the back three  
- haiku: Kyle Walker [bench] Walker looks unlikely to start at St Mary's; Erling Haaland [return] The striker returned to full training in midweek; John Stones [role] The centre-back John Stones has moved into defensive midfield alongside Rodri; Manuel Akanji [xi] Manuel Akanji is the preferred choice on the right  

