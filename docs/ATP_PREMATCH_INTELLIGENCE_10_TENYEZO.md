# ATP Intelligence – kötelező 10 tényezős Pre-Match Intelligence
**Forrás:** eredeti `ATP(1).txt` 318–439, 486–500, 558–574. sor. Visszaállítva 2026-11-22.
**Állapot:** kötelező elemzési specifikáció; nem állítja, hogy mind a 10 tényező élő API-bekötése már megvan.

## Alapelvek
- A két játékost **külön-külön**, majd egymáshoz viszonyítva vizsgáljuk; az aktuális torna és borítás körülményei számítanak.
- Elsődleges közvetlen formavizsgálat: **tárgyév + előző év** (2026-ban 2025–2026, 2027-ben 2026–2027).
- A „motivált”, „fáradt”, „sérült”, „mentálisan gyenge” nem pusztán a ranglistából, pontszámból vagy vereségből következik. Állítás típusát különítsük el: **tény / megfigyelés / hipotézis / előrejelzés**.
- A nem elérhető adatok állapota `UNKNOWN`, **nem** `false` és nem 0. Érvénytelen tétel nem számíthat negatív pontnak.

## A kötelező 10 tényező
| # | Vizsgált tényező | Pontosan mi szükséges? | Nem szabad automatikusan állítani |
|---|---|---|---|
| 1 | Előző és következő versenynaptár | Tornák, események, helyszín, meccsnapok, kiesés/bejutás | A jövőbeli nevezés biztos megjelenést jelent |
| 2 | Egyéni tornaprioritás | Verseny kategória + játékos nyilatkozata + naptár és saját célok | ATP 250 biztosan érdektelen / Grand Slam mindig azonos fontosságú |
| 3 | Pontvédelem | Tavalyi esemény helyezés, aktuális 52 hetes ranglistapontok és kiesési szabály | Magas pontvédelem automatikusan rossz/extra erős játékot okoz |
| 4 | Előző heti terhelés | Meccsszám, játékpercek, döntő/elődöntő, döntő szettek, szünetnapok | Döntőzés egyenlő fáradtsággal |
| 5 | Regeneráció | Utolsó meccs befejezése és következő kezdés közti órák, éjszakai meccs | Visszaesés bizonyosan fáradtságból ered |
| 6 | Utazás és időzóna | Előző/jelenlegi helyszín, útvonal, időzónaváltás, helyszínek közti idő | Biztosan repült vagy jetlagje van forrás nélkül |
| 7 | Borítás és átállás | Hard/Clay/Grass/Indoor, borításcsere, kétidényes eredmények, ellenfélerő | Történeti Elo = aktuális forma vagy régi cím = mai specialista |
| 8 | Igazolt fizikai állapot | Sérüléshír, visszalépés, kezelés, visszatérés – dátumozott nyilvános forrás | Rejtett sérülés diagnosztizálása mozgás/eredmény alapján |
| 9 | Dokumentált nyomáshelyzetek | Break-labda, TB, döntő szett, szetthátrány, hosszú meccsek, mintaszám | Széteső személyiségtípus vagy mentális erősség egy meccsből |
| 10 | Motiváció és prioritás bizonyítékai | Nyilatkozat, szezonterv, célverseny, pontvédelem, terhelési döntés | Megjelenési díj = tudatos rossz teljesítmény, manipuláció |

## Minden tényező rekordjának kötelező mezői
`match_id`, `player_id`, `feature_id` (1..10), `value`, `units`, `evidence_type`, `source_url`, `source_timestamp_utc`, `ingested_at_utc`, `event_cutoff_utc`, `confidence`, `completeness`, `hypothesis_or_fact`, `opponent_context`, `data_window`. Ha a forrás a meccs kezdete után jött létre, **nem használható a meccs előtti előrejelzésben**.

[20 üres pre-match felvételi sor](../research/templates/prematch_10_tenyezo_A_B_ures_sor.csv) – A és B játékos 10–10 tényezője, kizárólag hiányzó/üres mezőkkel.

## Jelentésformátum
**A játékos:** tíz tényezőnként TÉNY – ELŐNY/HÁTRÁNY/HATÁS NEM IGAZOLT – forrás – hiány. **B játékos:** ugyanez; majd **matchup értékelés**, külön `NO PREDICTION` kimenet, ha a hiány miatt felelőtlen volna számszerű következtetést levonni.

### Mérkőzésfordulás – hat versengő magyarázat
1. Fizikai terhelés/mobilitás-romlás; 2. mérhető viselkedési és hibatrend; 3. ellenfél taktikai alkalmazkodása; 4. forrással igazolható sérülés/kezelés; 5. természetes rövid távú ingadozás; **6. az ellenfél szintemelkedése**. Ezek **alternatív hipotézisek**, egyszerre többet is alátámaszthat a mérkőzés. Nem olvassuk vissza automatikusan az eredményből a feltételezett okot.

### Manipuláció és motiváció
- Ne állítsunk bizonyíték nélkül meccsmanipulációt, „eladta a meccset” történetet.
- A játékos esetleges megjelenési díja nem bizonyít alacsony motivációt.
- A torna kategóriája és az egyéni prioritás két külön változó.
- A jelenlegi célmeccsek ATP Tour 250/500/Masters/Finals és férfi Grand Slam-főtáblák. Challenger/ITF adatok lehetséges kontextusok, de nem ugyanaz a mintakör.
