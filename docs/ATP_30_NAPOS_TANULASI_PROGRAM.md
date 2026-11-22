# ATP Intelligence – 30 napos intuíció, rejtett jelek és előrejelzés program
**Forrás:** az eredeti, felhasználó által áthozott `ATP(1).txt` 1–73., 130–158., 238–312. sorának terve; helyreállítva 2026-11-22.
**Státusz:** korábbi tanulási terv, nem automatikusan elindított és nem bizonyított predikciós képesség. Opcionális személyes kutatási ág, nem az app fejlesztésének előfeltétele.

## Három, egymástól külön mérendő képesség
1. **Intuíció:** első benyomás statisztika/odds nélkül, az esemény előtt időbélyegezve; empirikusan vizsgáljuk, hozzáad-e előnyt.
2. **Rejtett jelek:** az eredményjelzőn még nem feltétlenül megjelenő technikai, taktikai és *megfigyelhető* viselkedési változások; külön vizsgálandó, mi következik valóban a feedből.
3. **Előrejelzés:** a következő pont, game, 2–3 game, szett és meccs eseményhez **előre megadott** valószínűség, visszatesztelhető formában.

**Napi időkeret**: az eredeti javaslat 30–45 perc. Ez javaslat, nem garantáltan szükséges vagy elegendő mennyiség. Általános módszer: 5 perc blind megfigyelés → rögzítés → rendelkezésre álló objektív bizonyíték → előrejelzés → a következő napon utólagos értékelés. Ha a meccset nem tudod nézni, alkalmazz külön **adat-only** kísérletet; az nem nevezhető vizuális Blind Predictionnek.

## Napokra bontott gyakorlatok
| Nap | Téma | Feladat | Mentendő eredmény |
|---|---|---|---|
| 1 | Első benyomás | 10 perc meccs, odds/statisztika nélkül | Első intuíció, eseményidő |
| 2 | A/B külön | Melyik változik jobban, mit látsz? | A és B külön megfigyelés |
| 3 | Első becslés | Következő game kimenete | 0–100%-os valószínűség |
| 4 | Visszajelzés | Előrejelzés vs. eredmény | Hibakategória, időbélyeg |
| 5 | Első audit | 1–4. napi rögzítések | Rövid tanulság |
| 6 | Szerva | Első szerva beütés és pontnyerés | Időablak, minta |
| 7 | Második szerva | Pontnyerés változása, ellenfélerő | Pontadat és trend |
| 8 | Mozgás/fáradás | Csak videón látható mozgás vagy meccshossz adat | Tény vs. hipotézis |
| 9 | Taktika | Támadó/védekező irányváltás, return pozíció | Megfigyelés + forrás |
| 10 | Korai jel | Tényleges break előtti esemény keresése | Jelzés előnye vagy fals riasztás |
| 11 | H1 | Következő pont előzetes becslése | p, tényleges eredmény |
| 12 | H2 | Következő game | p, eredmény |
| 13 | H3 | Következő 2–3 game, pontos célváltozó | p, eredmény |
| 14 | Break | Következő fogadójáték break-esélye | p, meccsállás |
| 15 | Audit | H1–H3 és break-jelzés külön | Brier, minta |
| 16 | Szett | Következő szett győztesének p-je | p, eredmény |
| 17 | Meccs | Győztes p; pre-match és live külön | p, eredmény |
| 18 | Borítás | 2025+2026 borításspecifikus teljesítmény | Ellenfél- és minta-korlát |
| 19 | Terhelés | Előző heti mérkőzések, utazás, pihenés | Forrásos pre-match kontextus |
| 20 | Audit | Rövid vs. hosszú célok külön | Kalibrációs megjegyzés |
| 21 | Odds | Decimális odds és implied p | Odds időbélyeg |
| 22 | Saját vs piac | Modell p összevetése margin/késés mellett | Bruttó és korrigált eltérés |
| 23 | Virtuális napló | Szimulált tét, valódi pénz nélkül | Virtuális kimenet |
| 24 | Hibavizsgálat | Rossz becslések és kihagyott jelek | Előzetes információk határa |
| 25 | EV | EV = p * odds − 1, bizonytalanság | EV és értelmezés |
| 26 | Csak intuíció | Blind becslés a részletes adatok előtt | Intuíció eredmény |
| 27 | Csak modell | Azonos eseményre független statisztikai becslés | Modell eredmény |
| 28 | Kombinált | Előre rögzített kombinációs szabály | Kombinált eredmény |
| 29 | Teljes meccs | Pre-match→live→jelzés→utólagos mérés | Időbélyeges napló |
| 30 | Áttekintés | Kalibráció, fals riasztás, minta, ROI csak virtuális | Következő tesztterv |

## Minimum 50 előre rögzített Blind Prediction próba
A **30 nap NEM helyettesíti az 50 kísérletet**. A 30 nap tanulási struktúra, az 50 esemény a korábbi kísérleti terv minimális induló mintája – statisztikai bizonyítéknak még ez is kevés. Lásd: [50 üres naplósor](../research/templates/blind_prediction_50_ures_sor.csv), [részletes protokoll](ATP_BLIND_PREDICTION_50_PROTOCCheck.md).

## Mérőszámok
Pontosság; Brier score és log loss (előrejelzési célonként); kalibrációs görbe; valódi változás előtti jelzési előny; fals riasztások; opcionális szimulált ROI. **Tilos** ugyanazt az eseményt a később megismert eredménnyel visszatölteni vagy eredetinek mutatni.

## Hogyan kapcsolódik a privát apphoz?
A naplózó és tréning modul későbbi UI-kiegészítés. **Nem előfeltétele** a teljesen automata, adatvezérelt ATP meccsfigyelésnek; a személyes intuíciós becslés külön analitikai réteg, amelynek többletértékét bizonyítani kell.
