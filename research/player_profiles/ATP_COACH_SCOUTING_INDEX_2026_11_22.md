# ATP Intelligence – teljes Top150 scouting csomag
**Dátum:** 2026-11-22. **Az aktuális szakmai adatgyűjtési kör eredménye: 150/150 forráslinkkel ellátott statisztikai dosszié.**

## Mit jelent a készültség?
- **150/150** forrásra hivatkozó, 2025–2026-os statisztikai profil: egyéni személyi adat, W/L, borítás, first/second serve, return, 30/90 napos forma, tie-break és döntőszett eredmények, matchup-hipotézis.
- **137/150** esetében külön **2025–2026-os dátumozott, ebben a kutatási körben felvett** forrásrészlet. Az eredeti 13 esetében korábbi vagy külön ellenőrizendő stílusforrás, néhány 2024-es történeti.
- **0/150** több mérkőzésen validált teljes ütésfajtás, mozgásos, mentális személyiségprofil; nem állítunk mást.
- A 2026-os legfrissebb rendszeresen feldolgozott match archívum 2026-11-15-ig tart; az ATP-rangsor 2026-11-16-i.
- 2025/26 egymás elleni H2H friss kétidényes adat, 2024 és korábbi **0 közvetlen prediktív súly**.
- Minden játékosnak van eltérő bizonyítékszintet jelző forrástípusa; sok esetben a hivatkozás csak játékoséletrajz vagy egy konkrét mérkőzés eredménye, NEM technikai szakvélemény.

## Fájlok
- [**MIND A 150 JÁTÉKOS – EGYBEN, teljes scouting dosszié**](ATP_TOP150_SCOUTING_EGYBEN_2026_11_22.md)
- [1–50. játékos](ATP_COACH_SCOUTING_2026_11_22_001_050.md)
- [51–100. játékos](ATP_COACH_SCOUTING_2026_11_22_051_100.md)
- [101–150. játékos](ATP_COACH_SCOUTING_2026_11_22_101_150.md)
- [**150 játékos – 18 mezős scouting CSV, forrásminőség jelöléssel**](ATP_COACH_SCOUTING_REGISTER_2026_11_22.csv)
- [150 játékos – validációs hiánylista](ATP_TOP150_VALIDATION_STATUS_2026_11_22.csv)
- [69 mezős, részletes mérkőzésstatisztikai CSV](TOP150_EVIDENCE_PROFILE_REGISTER_2026_11_21.csv)
- [2025–2026 H2H-adatbázis, 2026.11.15-ig](TOP150_H2H_2025_2026_THROUGH_2026_11_15.csv)
- [36 első újonnan gyűjtött ATP-megfigyelés](ATP_2026_SOURCE_BACKED_COACHING_OBSERVATIONS_36.csv)
- [Wave2/A – 15 játékos](ATP_COACH_OBSERVATIONS_WAVE2_A_2026_11_22.csv)
- [Wave2/B – 15 játékos](ATP_COACH_OBSERVATIONS_WAVE2_B_2026_11_22.csv)
- [Wave3/A – 20 játékos](ATP_COACH_OBSERVATIONS_WAVE3_A_2026_11_22.csv)
- [Wave3/B – 15 játékos](ATP_COACH_OBSERVATIONS_WAVE3_B_2026_11_22.csv)
- [Wave4/A – 20 játékos](ATP_COACH_OBSERVATIONS_WAVE4_A_2026_11_22.csv)
- [Wave4/B – 16 játékos](ATP_COACH_OBSERVATIONS_WAVE4_B_2026_11_22.csv)

## Adatforrások és korlát
- TennisDB szezon: https://tennis-db.com/seasons-and-rankings?year=2026
- 2025 archívum: https://github.com/Aneeshers/tennis-sackmann-archive/blob/main/atp/atp_matches_2025.csv (forráshely CC BY-NC-SA 4.0 jelzéssel)
- 2026 archívum: https://huggingface.co/datasets/minmaxxxer/atp-wta-matches-with-odds (CC BY 4.0, 2026.11.15-ig ellenőrizve)
- Eltérhet a TennisDB és az archív match adat versenyköre. A Pythia-Elo többéves történeti rating: nem tiszta 2025–2026-os forma.
- A Pressure+, a tie-break és a döntőszett mérkőzéskimenet; **nem bizonyít mentális alkati jelzőt**.
- A taktikáról általános megállapítást csak több meccs objektív forrása alapján lehet véglegesíteni.

## A további validáció akadályai
Hiányzik a 150 játékos részletes 2025–2026-os ütésenkénti és rallyhossz, mozgás/footwork, közvetlen szerva+1 és fogadás+1 adatainak hozzáférhető többmeccses forrása, valamint a 2026.11.15 utáni teljes H2H. A meglevő jelentés ezeket **nem imitálja**. A scoutingdossziék az app működésébe még nincsenek automatikusan integrálva.


## 2026-11-22 – Új, hivatalos ATP TDI és H2H kutatás (PR #13 branch, még nem main)

**Forrásolt új adatcsomag – nem éles profilba importálva:**
- [26 Top150 játékos – ATP/TDI 2026 júniusi rolling-52-week tracking összehasonlító mutatók](ATP_TDI_INSIGHTS_VERIFIED_26_2026_11_22.csv). Két mért, dokumentumból kiolvasott indikátor / játékos, összesen 52 külön érték; **nem** 26 validált mentális profil.
- [12 új, 2026.11.16–21. között lezárt ATP Finals meccs](ATP_H2H_NEW_COMPLETED_ATP_FINALS_2026_11_16_TO_21.csv) – hivatalos és független eredményforrás. A korábbi H2H `2026-11-15` cutoffja után, de **nem** a 2026-11-22-i döntőre vonatkozik.
- [Négy 2026-os főtábla-/selejtezőadat újraellenőrzése](ATP_2026_SEASON_FOUR_GAPS_RECHECK_2026_11_22.csv) – Otto Virtanen, Clément Chidekh, Max Alcalá Gurri, Nikolas Sánchez Izquierdo; nem automatikus pótlás.
- [Teljes kutatási értelmezés, források és adatminőségi határok](ATP_2026_11_22_KOVETKEZO_FORRASOLT_KUTATAS.md).

**Védelmi szabály:** 2025–26 visszatekintő tracking mutatóit csak forrásdátummal és modellvalidációval használjuk; a 2026 júniusi 52 hetes adatot nem nevezzük 2026 novemberi aktuális formának. A 12 mérkőzést deduplikáció és provider player-ID egyeztetés nélkül tilos az összesített H2H-ba vakon beleszámolni. A korábbi 0/150 teljesen validált, többmeccses belső pszichológiai és részletes ütésenkénti profilstátusz változatlan.


### 2026-11-22 – Második hivatalos TDI-kutatási hullám: további 14 játékos

- [További 14 Top150 játékos (28 új mért tracking-adat)](ATP_TDI_INSIGHTS_NEW_14_2026_11_22.csv): ATP Doha 2026-02-18, Miami 2026-03-24, Indian Wells 2026-03-07, Róma 2026-05-06/09 és Halle 2026-06-17 dátumozott hivatalos ATP-médiaanyagok.
- A korábbi 26 játékossal **összesen 40 különböző Top150-játékos, 80 kiválasztott és forráshivatkozott ATP/TDI-mezőérték** szerepel az új két kutatási fájlban. Ezek az adott dátum előtti **gördülő 52 hetes mérési ablakok**, nem 2026. novemberi élő forma, nem minden mező és nem validált mentális/biomechanikai profil. A forrásméréseket a modellben csak a tényleges adatmegfigyelési dátumhoz igazítva szabad használni.


### 2026-11-22 – Harmadik hivatalos TDI-kutatási hullám / egységesített 70 játékos

- **[70 egyedi Top150 játékos TDI-adatainak kanonikus, egyesített kutatási táblája](ATP_TDI_TOP150_NORMALIZED_70_2026_11_22.csv)**, az öt egyedi forrás-CSV-ből automatizáltan összerakva: **290 tényleges számszerű TDI-érték**, 30 játékosnál 7/7, további 40 játékosnál 2/7 mutató, **80 játékosnál egyelőre nincs forrásolt TDI sor**. A nem létező mezők ÜRESEK, nem 0 értékek.
- [24 új játékos / 7-7 mutató](ATP_TDI_FULL7_NEW_24_PLAYERS_2026_11_22.csv), [további 3 játékos: Fils, Munar, Machac](ATP_TDI_FULL7_NEW_3_PLAYERS_2026_11_22.csv), [további 3 játékos: Korda, Navone, Ofner](ATP_TDI_FULL7_NEW_3_MORE_PLAYERS_2026_11_22.csv), 2026. február–június hivatalos ATP-media/TDI dokumentumokból.
- A harmonizált tábla megőrzi az eredeti PDF URL-t, a forrásban szereplő oldalszámot ahol ellenőrzött, a mérés napját, annak rolling-52-week / tournament-to-date jellegét, a mezőnkénti kitöltöttséget és a review státuszt. Tsitsipas dohai `tournament_to_date` értékeit NEM szabad a 69 másik rolling-52-week adatával azonos időablaknak tekinteni.
- **Ez kutatási overlay a PR #13-ban, NEM már automatikusan a `main`-be került forrás/regiszter-módosítás.** A teljes, többmeccses edzői technika/mentális profilstátusz továbbra nem validált, 0/150. Az ATP/TDI 0–10 minőségi és %-os taktikai mutatói objektív tracking-bemenetek, nem mentális diagnózisok, és az eltérő dátumok miatt nem egy homogén versenyen belüli benchmark.


## 2026-11-22 – Negyedik TDI-hullám: 105 játékos / 535 adat / külön időablak-szűrés

A korábbi 94 játékoson felül **11 különböző** Top150-játékos 77 forrásolt TDI-számértéke:
- [11 játékos új hétmutatós forrásai](ATP_TDI_FULL7_NEW_11_PLAYERS_2026_11_22.csv) – Alex Molcan, Roman Safiullin, Aleksandar Vukic, Nishesh Basavareddy, Hugo Gaston, Jaime Faria, Camilo Ugo Carabelli, James Duckworth, Pedro Martinez, Laslo Djere, Thiago Seyboth Wild.
- **[Egységes 105 fős TDI-kutatási CSV, temporal_source_scope mezővel](ATP_TDI_TOP150_NORMALIZED_105_2026_11_22.csv)**: **105/150 külön játékos**, **65 teljes 7/7**, **40 részleges 2/7**, összesen **535 ténylegesen közölt számérték**; az adatok továbbra kutatási rekordok, és nem validált előrejelzési funkciók.
- [Fennmaradó 45 fő célzott forráslistája](ATP_TDI_REMAINING_45_RESEARCH_QUEUE_2026_11_22.csv); a Top50-ből TDI nélkül maradt Arthur Fery, Luca Van Assche, Daniel Merida, Arthur Gea.
- [2026-os, forrásolt, játékhelyzeti megfigyelések a négy TDI nélküli Top50-játékoshoz és Martin Damm Jr identitásellenőrzése](ATP_TOP150_2026_FOUR_TOP50_CONTEXT_PLUS_DAMM_IDENTITY_2026_11_22.csv): 9 konkrét eseménymegfigyelés, nem 7 mutatós profil vagy pszichológiai diagnózis.

**Fontos időszűrés:** 9 új, 2025-ben közzétett gördülő 52 hetes mutató 2024-es mérkőzéseket is tartalmazhat, ezért `EXCLUDE_DIRECT_PREDICTOR_POSSIBLE_2024_MATCHES` jelölést kapott az új 105 soros fájlban. Jaime Faria 2025-ös Rio `tournament_to_date` mutatói tisztán 2025-ös tornakörre korlátozottak. A meglévő 2026-os rolling-52-week rekordok 2025–26-os ablakban vannak, de publikációjuk időpontjánál későbbi teljesítményt nem bizonyítanak. A `predictive_validated` mind a 105 sorban `NO`, amíg előzetesen időzárt backteszt nem készült.


## 2026-11-22 – Ötödik kutatási hullám: TDI 105 teljes + MCP 31 + 14

**A fenti, korábban leírt 40 kétmutatós TDI-profil már NEM aktuális állapot:** 27, majd 13 részleges játékos 5-5 hiányzó indikátora is hivatalos ATP 2026 PDF-ből forrásoltan kiegészült; összesen +200 mért TDI-mező.

**Jelenlegi hivatalos TDI kutatási forrás:** [**105/150 játékos, mindegyiknél 7/7 TDI-mutató, 735 forrásolt számszerű érték**](ATP_TDI_TOP150_NORMALIZED_105_FULL7_735_VALUES_2026_11_22.csv). Két forrásolt pótlási csomag: [27 játékos](ATP_TDI_27_EXISTING_2TO7_2026_11_22.csv) + [13 játékos](ATP_TDI_13_EXISTING_2TO7_2026_11_22.csv). **45/150** játékosnál továbbra nincs hivatalos TDI seven-metric sor.

**Új, független technikai kutatási forrás – Tennis Abstract Match Charting Project:**
- [**150 játékos teljes kutatási evidence coverage átadása**](ATP_TOP150_2026_TECHNICAL_EVIDENCE_COVERAGE_MASTER_RESEARCH.csv): **105 ATP/TDI teljes**, **31 TDI nélküli, de 2025–2026-os chartolt match-szintű forrással**, **14 csak általános statisztikai/eredményadattal** (nem nulla vagy ismeretlen teljesítmény).
- [**45 TDI-hiányos játékos charting elérhetősége**](ATP_MCP_45_TDI_MISSING_PLAYER_CHARTING_COVERAGE_2026_11_22.csv): 31/45 friss, 2025–26-os match charting link; 26/45-nél ATP/GS főtábla-jelölt meccs; 14-nél nincs ilyen 2025/26-os charting.
- [**97 dátumozott mérkőzésszintű MCP-link, versenykör szerint előszűrve**](ATP_MCP_2025_26_MATCH_LEVEL_SOURCE_LINKS_FOR_TDI_MISSING_2026_11_22.csv): 73 főtábla-jelölt (még match/round QA kell), 20 Challenger/ITF/NCAA/Davis Cup/stb. más kör, 4 selejtező.
- [**Négy korábban TDI nélküli Top50 technikai MCP-mérései**](ATP_MCP_2026_FOUR_MISSING_TDI_TOP50_TECHNICAL_CONTEXT.csv): Arthur Fery, Luca Van Assche, Daniel Mérida, Arthur Géa. [11 konkrét, 2026-ban chartolt meccs](ATP_MCP_2026_FOUR_TOP50_11_CHARTED_MATCH_LINKS.csv). Nem helyettesíti a hivatalos 7 TDI-mutatót.
- [**Teljes 150-es forrásminőségi audit, scope, licenc és 14 játékos név szerinti feljegyzése**](ATP_2026_11_22_150_PLAYER_TECHNICAL_SOURCE_AUDIT.md).

**Kötelező licenc:** Match Charting Project [CC BY-NC-SA 4.0](https://github.com/JeffSackmann/tennis_MatchChartingProject): attribúció + kizárólag nem kereskedelmi felhasználás + share alike; az adatok általában *önkéntesen kiválasztott, nem reprezentatív* mérkőzésekből származnak. A projektben csak rövid, forrásolt jegyzetek és eredeti charting linkek kerültek a PR-ba, **nem importáltunk nyers charting adatállományt**. A 105 TDI közül 9 régi 2025 rolling-52-week sor 2024-es mérkőzéseket is tartalmazhat; a direkt predikció tiltóflagja megmaradt.

**Fontos:** 136/150 esetében van forrásolt, 2025–26-os technikai követéshez *kutatási bemenet*, NEM 136 teljes többmeccsesen validált coach- vagy mentális profil; az utóbbi továbbra 0/150. Az appot és `main`-t ez a kutatás nem módosította.


## ATP V4 – 2026-11-22 végső deduplikált match-ID / Top150 kutatási átadás

**A fentiek korábbi kutatási mérföldkövek, a legújabb hiteles kutatási forráslefedettség:**
- [V4 kanonikus teljes kutatási átadás](ATP_DATA_RESEARCH_V4_CANONICAL_HANDOFF_2026_11_22.md) és [V3 150-es bizonyítékosztály-mátrix](ATP_TOP150_2026_TECHNICAL_EVIDENCE_COVERAGE_V3_OFFICIAL_MATCH_IDS_2026_11_22.csv).
- 105 játékos × 7 ATP/TDI = **735** mérés; 26 további játékoshoz **72 egyedi** főtáblás ATP match-ID-vel igazolt, 2025/26 chartolt meccs; 1 további Ilia Simakin tour main-draw n=1; más 18 játékos mixed/other/qualifying statisztika. **150 kutatási forrásazonosítás / 132 ATP/GS releváns technikai forrás / 0 garantált teljes mentális/technikai diagnózis.**
- [96 egyedi MCP-meccs nap/scope/official ID kanonikus, licencekkel](ATP_MCP_96_UNIQUE_MATCHES_CANONICAL_DATES_OFFICIAL_IDS_FINAL_QA_2026_11_22.csv). Az előző 97 MCP rekord **97 játékos-asszociáció**, nem 97 külön meccs; az előző 73 főtábla-rekord **72 külön meccs**.
- Az összes 72 ATP/GS matchhez dátumforrás: **48 ATP eredményarchívumban**, **19 történeti dátum nélküli archívumhoz külön hír/meccsforrásból**, **5 eltérő forrásdátumhoz külön manuális újraegyeztetést** rögzítő [19-es](ATP_MCP_19_ATP_2025_ARCHIVE_DATE_GAPS_INDEPENDENTLY_CROSSCHECKED_2026_11_22.csv) és [5-ös](ATP_MCP_FIVE_ATP_VS_CHARTING_DATE_DISCREPANCIES_RESOLVED_2026_11_22.csv) QA fájl.
- V1 ATP/GS modellelőrejelzésbe csak versenykör-, event-date-, match-ID-, licence- és no-lookahead ellenőrzés után importálható. Az időpontok mérkőzés**napok**, nem pontonkénti eseménytimestamp-ek; mentális állapotokra következtetni tilos. **Az app ág PR #14 nincs automatikusan frissítve a kutatás változásaival.**
