# ATP Intelligence – teljes Top150 játékosregiszter

**Aktuális forrásállapot:** 2026. november 21. `ranking_as_of = 2026-11-16`. A keret kizárólag férfi ATP-egyes Top150 játékosokat tartalmaz, nem az összes ATP-versenyen induló játékost.

## 2026-11-21 – új, teljesen összeszerelt Top150 statisztikai dossziék

**[Aktuális Top150 index](TOP150_EVIDENCE_PROFILES_INDEX_2026_11_21.md)** – 150 játékos egyenkénti, 2025–2026 eredmény/statisztika-vezérelt profilja, 2026.11.15-ig frissített H2H, 2025 és 2026 szerva/fogadás, tie-break és döntőszett kimenetek, borításonkénti rekordok, a korábbi 13 szakértői stílusjegyzet megkülönböztetve.

**Lefedettség:** 150/150 statisztikai profil; 148/150 2026-os friss meccsforrás; 146/150 TennisDB szezonrekord; 13/150 előzetes kvalitatív taktikai jegyzet; 0/150 többmeccses technikai és mentális **validált** profil. A szezonok közötti H2H-archívumot csak 2026-11-15-ig ellenőriztük, nem azonos az aktuális napi teljes H2H-val. H2H-hoz 2024 és korábbi közvetlen prediktív súly 0. A Pythia Elo történeti információ.

Adatforrás/credit: TennisDB; Min Maxxxer / Tennis Odds Actor (2026 meccsek, CC BY 4.0); Sackmann-archívum (2025 meccsek, CC BY-NC-SA 4.0); PythiaTennis. A 2026-os TennisDB és HF/Flashscore archív W/L definíciója eltérhet. A meccseredmény-alapú pressure mutatók nem mérik közvetlenül a mentális állapotot.

---

## Használható adatok és lefedettség

- [Magyar, 18 oszlopos, pontosvesszővel tagolt, Excelben is megnyitható áttekintő lista](ATP_TOP150_ATTEKINTHETO_LISTA_2026_11_21.csv): 150 játékos, kor, súly, magasság, jobb-/balkezesség, fonák, 2026 W/L, hard/clay/grass/indoor Elo, jegyzetek száma.
- [Részletes, 40+ oszlopos, forrásolt játékosregiszter](atp_top150_profile_register_2026_11_21.csv): a fentieken túl ATP-pontszámok, dátumozott források, szezon-Elo, Serve+, Return+, Pressure+, megjegyzések és ellenőrzési állapot.
- [Életrajzi alapállomány](../rosters/atp_top150_biography_2026_11_21.csv): ATP hivatalos média guide (2024/2025/2026), friss ATP player overview, TennisExplorer és Australian Open profilok.
- [Borításspecifikus Elo](../rosters/atp_top150_surface_elo_2026_11_20.csv): PythiaTennis, eredmények 2026-11-20-ig.
- [2026-os szezonmutatók](../rosters/atp_top150_season_stats_2026.csv): TennisDB, egyeztetett név és ATP-pont alapján.

| Adatcsoport | Lefedettség | Megjegyzés |
|---|---:|---|
| Név, ország, ATP-helyezés, ATP-pont | 150/150 | Dátumozott 2026-11-16 |
| Születési dátum és kor | 150/150 | 2026-11-21-re számolt kor |
| Jobb-/balkezesség | 150/150 | ATP és profiloldalak |
| Magasság, testsúly | 134/150 | 16 játékosnál a magasság és/vagy testsúly még hiányzik; nem becsüljük |
| Borításspecifikus modell-Elo | 150/150 | Hard, clay, grass, indoor; nem azonos egy specialista-besorolással |
| 2026-os szezonstatisztikai rekord | 146/150 | 4 további ellenőrzést igénylő játékos, nem becsült eredmények |
| Edző neve a vizsgált forrás időpontjában | 12/150 | A mai edzői kapcsolat külön ellenőrizendő |
| Rövid, dátumozott szakértői megfigyelés | 12 játékos / 18 rekord | Mérkőzésspecifikus, nem aktuális általánosítás |
| Validált mentális nyomásprofil | **0/150** | Nincs etikusan és szakmailag megalapozott kész minősítés |
| Előzetes, forrásolt stílus- és matchupjegyzet | **7/150** | Korábbi, dátumozott ATP és Hugh Clarke forrás; nem végleges többmeccses diagnózis |
| Teljes, többmeccsesen validált játékstílusprofil | **0/150** | Forrásolt kódolás és mérkőzések közötti ellenőrzés még szükséges |

## Amit a felhasználó jogosan kér, de még NINCS bizonyítva

Az életkor/súly/kezesség nem egyenlő az edzői profillal. Az egyéni taktikai profil szükséges mezői:
`serve_1st`, `serve_2nd`, `serve_toss_change`, `serve_plus_one`,
`return_plus_one`, `forehand`, `backhand`, `net_points`, `0_4_shot_rallies`,
`movement`, `defensive_recovery`, `hard_clay_grass_indoor`, `pressure_context`,
`momentum_change_point`, `fatigue_context`, `opponent_specific_weaknesses`.

Minden mezőhöz mérkőzés, dátum, forrás, objektív mérés/szakértői megfigyelés, bizonytalanság és *last_verified* tartozzon. Nyomás alatti mérhető teljesítmény (pl. breakpont, tie-break, döntő szett, erős ellenfélhez korrigálva) **nem bizonyítja önmagában** a belső pszichológiai tulajdonságot.

## Forrástorzítás és pontosság

A 2026-os média guide **Flavio Cobolli magasságát 173 cm-nek írta**, míg a jelenlegi hivatalos ATP overview **183 cm**; az utóbbit használtuk, és a konfliktust a dossziéban külön rögzítettük. Testsúly sportadatokban időben változhat, ezért az eredeti forrás évét megőrizzük.

A *PythiaTennis* felületenkénti Elo-modellje saját, 1500-ról induló értékelést készít, nem puszta megnyert meccsek száma. Borítások közötti összehasonlításnál mintaszám és ellenfélerő is számít. A *TennisDB* `Pressure+` mutatója nem automatikus pszichológiai diagnózis.

A működő appra a jelenlegi CSV **még nincs élőben bekötve**. A modell momentumelőnyét és egy-egy játékos állapotváltozását csak időzárt, folyamatosan tesztelt mérkőzéssorozatokkal lehet validálni.

## Fejlesztési tesztek

`python -m unittest discover -s tests -v` lefuttatja a `test_player_profile_register.py` validációit is: 150 helyes játékos, kor, kéz, forrás, Elo, nincs kitalált mentális címke és hiányzó adat nem nulla.

[Notion Top150 teljes lista](https://app.notion.com/p/41ff603f0d2e81f08d2bd1d2966d9ed3).

## 2026. november 22. – 150/150 kibővített scoutingdosszié

[**Teljes friss scouting-index**](ATP_COACH_SCOUTING_INDEX_2026_11_22.md) | [150 egyesített profil](ATP_TOP150_SCOUTING_EGYBEN_2026_11_22.md) | [150 fős strukturált scouting-regiszter](ATP_COACH_SCOUTING_REGISTER_2026_11_22.csv) | [Tételes validációs hiánylista](ATP_TOP150_VALIDATION_STATUS_2026_11_22.csv)

Mind a 150 játékoshoz van külön statisztikai elemzés és dátumhoz/forráshoz köthető rekord; 137 új, 2025–26-os forrásrészlet + 13 régebbi stílusforrás. A forrás hivatkozása NEM garantálja egy többmeccses, szakmailag validált stílus-/mentális profil meglétét (ilyen 0/150). Egyszeri eredményt és egy játékos önbevallott kedvenc ütését nem lehet önmagában megállapított technikai erősségnek tekinteni. A teljes, napi szintű H2H és edzői videós vizsgálat továbbra is hiányzik.

