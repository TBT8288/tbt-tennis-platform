# ATP Intelligence – 2026.11.22 kutatási V4 végállapot és QA-átadás

**Projekt:** saját, privát ATP/Grand Slam férfi egyes teniszintelligencia. **Kutatási ág / PR #13**, nem automatikus `main` merge. Az adatbázis 2026.11.16-i Top150-rangsorának játékosaira vonatkozik. 2025–2026 a közvetlen relevanciaablak; 2027-től 2026–2027-re vált.

## 1. Legfrissebb egyedi forráslefedettségi eredmény

A **[V3 technikai forrásmátrix](ATP_TOP150_2026_TECHNICAL_EVIDENCE_COVERAGE_V3_OFFICIAL_MATCH_IDS_2026_11_22.csv)** 150 egyedi játékost fed le, hat nem összemosható kutatási bizonyítékosztállyal:

| Forrástípus | Játékos | Mit bizonyít? | Mire nem jogosít? |
|---|---:|---|---|
| Hivatalos ATP/TDI tracking, **mind a hét mutatóval** | **105** | **735** mért érték, eltérő dátumú 52 hetes vagy tournament-to-date ablak | Nem friss novemberi forma, nem igazolt pszichológiai/biomechanikai diagnózis |
| Önkéntesen chartolt, ATP eredményarchívumban is azonosított főtáblás meccs | **26** | Összesen 73 játékos–mérkőzés asszociáció, **72 külön mérkőzés**, hivatalos ATP match ID és játékosazonosítók | Nem ATP/TDI 0–10 quality; a charting nem reprezentatív |
| Egyetlen ATP főtáblás mérkőzés statisztikája | **1** | Ilia Simakin, 2026 Shanghai, n=1 | Nem állandó játékosprofil |
| Vegyes versenykörű 2026 serve/return szezonadat | **11** | Első/második szerva, return, BP és mintanagyság | Nem tisztán ATP/GS főtáblás, meccsszintű bontás nélkül prediktív modellbe nem vehető |
| Csak más (Challenger/csapat stb.) meccsszintű charting a talált mintában | **5** | Létező chartolt mérkőzések, de nem a kiválasztott ATP/GS főtáblán | A V1 főtáblás modellbe közvetlenül nem vehető |
| Csak Grand Slam-selejtezős meccs részletes statisztikája | **2** | Max Alcalá Gurri és Nikolas Sánchez Izquierdo, n=1–1 | Nem főtáblás; mintaszám alacsony |
| **Összesen** | **150** | Minden játékoshoz legalább egy technikai jellegű forrás azonosítva | **0/150 teljes, többmeccses, önállóan validált mentális/edzői profil** |

**132/150** játékosnál létezik ATP/GS-főtábla körébe kapcsolható technikai forrás (105 TDI + 26 hivatalos meccsazonosítós charting + 1 single-match); **18/150** esetben az új technikai adatok kizárólag vegyes/nem főtáblás versenykörből jöttek. Ez **forrásazonosítási lefedettség**, nem valós élő találat/odds-előny és nem bevezetett kódos feature.

## 2. A 2025–2026 Match Charting állomány végleges, de auditálható deduplikálása

A korábbi fájlban **97 játékos–mérkőzés asszociáció** volt, **de csak 96 külön chartolt mérkőzés**. Ennek oka a 2026.04.23-i **Daniel Mérida–Marco Trungelliti** Madrid Masters R128 mérkőzés, amely mindkét játékoshoz fel volt véve, és **egyszer számítandó**. A korábbi „97 egyedi meccs” megfogalmazás hibás volt, pontosítása itt történik.

A 96 külön mérkőzésből:
- **72** ATP/GS főtáblás, a *pontos játékospár és forduló* az ATP hivatalos 2025/26 eredményarchívumában megtalálható, továbbá van **72 egyedi hivatalos ATP statisztikai match ID**, és eredeti MCP link.
- **20** Challenger/egyéb nem célzott eseménykör, **4** selejtező – mind explicit kizárandó a V1 főtáblás technikai feature-ökből.
- A 72 meccs **73** játékoshoz tartozó asszociációja a párosan listázott Merida–Trungelliti mérkőzés miatt nem jelent 73 külön eseményt.

**Kanonikus, dátum szerint rekonciliált 96 soros fájl: [ATP_MCP_96_UNIQUE_MATCHES_CANONICAL_DATES_OFFICIAL_IDS_FINAL_QA_2026_11_22.csv](ATP_MCP_96_UNIQUE_MATCHES_CANONICAL_DATES_OFFICIAL_IDS_FINAL_QA_2026_11_22.csv).** A 72 hivatalos match ID és két ATP player URL külön [73 asszociációs](ATP_MCP_73_PLAYER_LINKS_TO_72_OFFICIAL_MATCH_IDS_2026_11_22.csv) és [72 egyedi match](ATP_MCP_72_UNIQUE_OFFICIAL_ATP_MATCH_CROSSWALK_2026_11_22.csv) tábla formájában is rendelkezésre áll.

### Mérkőzésdátumok – 72 főtábla-meccs, három ellenőrzési kategória

| Dátumbizonyítás | Külön mérkőzés | Értelmezés |
|---|---:|---|
| ATP eredményarchívum: játékospár + forduló + mérkőzésdátum egyezik a chartinggal | **48** | ATP archívum az eredeti napot is mutatja |
| ATP archívum: játékospár + forduló + match ID egyezik; **19 régebbi archív rekordban nem jelenik meg a nap**, más, dátumozott forrás ellenőrizte | **19** | Játékospár/round/ID hivatalos, nap külön forrásból igazolt |
| ATP és charting nap eltér, plusz egyértelmű, független meccsnapi forrás segítségével kiválasztott dátum | **5** | Mindkét eredeti dátum megmarad; kanonikus dátum választása dokumentált |
| **Összesen** | **72** | Dátum és hivatalos ID minden főtábla-esethez forrásolva; nem igazolt pontszintű időbélyeg |

A 19-es táblázat: [ATP_MCP_19_ATP_2025_ARCHIVE_DATE_GAPS_INDEPENDENTLY_CROSSCHECKED_2026_11_22.csv](ATP_MCP_19_ATP_2025_ARCHIVE_DATE_GAPS_INDEPENDENTLY_CROSSCHECKED_2026_11_22.csv). Két megjegyzés: a 2025 Dallas Ruud–Mmoh és a 2025 Miami Cina–Comesaña eseteknél különböző összesítő oldalak **más dátumot** is megjelenítenek; a korabeli ATP dokumentum/beszámoló alapján választott napot ezért megőrzött hivatkozás kíséri.

### Az öt rekonciliált dátum – hivatalos meccs-ID változatlan

| Mérkőzés | ATP-archívum nap | MCP nap | Kiválasztott kanonikus nap | Dátum-megerősítés |
|---|---|---|---|---|
| Jannik Sinner – Shintaro Mochizuki, Wimbledon R16 | 2026-07-05 | 2026-07-06 | **2026-07-05** | [Aznap közölt ATP-tudósítás](https://www.atptour.com/en/news/sinner-mochizuki-wimbledon-2026-sunday) |
| Stefanos Tsitsipas – Martin Damm Jr, Montreal R128 | 2026-08-04 | 2026-08-05 | **2026-08-04** | [Dátumozott Tennis.com meccslap](https://www.tennis.com/tournaments/national-bank-open-presented-by-rogers-3/matches/m-damm-jr-vs-s-tsitsipas-2026-08-04) |
| Valentin Royer – Christopher O'Connell, Rotterdam R32 | 2026-02-10 | 2026-02-09 | **2026-02-09** | [L'Équipe ugyanazon meccs élőeredménye, február 9.](https://www.lequipe.fr/Tennis/rotterdam/epreuve-simple-messieurs/annee-2026/match-direct/valentin-royer-christopher-o-connell-live/413023) |
| Daniil Medvedev – Sho Shimabukuro, Almaty R16 | 2026-10-23 | 2026-10-22 | **2026-10-22** | [Almaty rendezői program](https://almatyopen.kz/en/schedule/) és [Tennis.com meccslap](https://www.tennis.com/tournaments/almaty-open/matches/d-medvedev-vs-s-shimabukuro-2026-10-22) |
| Stefanos Sakellaridis – Nuno Borges, Athén R32 | 2025-11-03 | 2025-11-02 | **2025-11-02** | [2025.11.01-én publikált görög mérkőzésnapi program](https://www.tennisnews.gr/tennis-world/atp-tennis/item/66070-atp-athens-schedule) |

Részletes [öt dátumforrásos konfliktus-CSV](ATP_MCP_FIVE_ATP_VS_CHARTING_DATE_DISCREPANCIES_RESOLVED_2026_11_22.csv). Ez *napot* bizonyít, nem labdamenetenkénti, utcai időzónára normalizált eredeti `event_time` adatot; történeti as-of rendszer csak a konkrét meccs zárása után ismerheti a meccs statisztikáját.

## 3. A maradék 14 kezdetben MCP/TDI-hiányos játékos statisztikája

- [**11 játékos 2026 szerva–fogadás statisztikai mintája**](ATP_2026_SERVE_RETURN_FOR_11_TDI_MCP_GAPS_2026_11_22.csv): 8–34 számszerű statot tartalmazó meccs/játékos, de a provider versenykörében ATP-főtábla, selejtező és csapatverseny is szerepelhet. A modell V1-be ezeket **ne importáljuk addig**, amíg eredeti match ID + főtábla-filter nincs meg.
- [**Ilia Simakin Shanghai Masters, 2026-10-08: egy főtáblás találkozó**](ATP_2026_LAST_THREE_PLAYERS_TENNISDB_SCOPE_AND_MATCH_STATS_2026_11_22.csv), n=1, csak kutatási jelzés.
- **Max Alcalá Gurri, US Open Q1, 2026-08-25:** hivatalos [IBM SlamTracker](https://www.usopen.org/en_US/scores/stats/11145.html) **26/43 első szerva a pályán**, 11/26 nyert első szervapont, 6/17 nyert második szervapont. A korábbi másodlagos 30/43 eltérést az adatminőségi auditban megőriztük, de **a hivatalos érték az elsőbbségi mérés**.
- **Nikolas Sánchez Izquierdo, US Open Q1, 2026-08-25:** 41/69 első szerva, 29/41 első szervapont megnyerve, 10/28 második; két másodlagos statforrás egyezik, a [US Open hivatalos videója](https://www.usopen.org/en_US/video/watch/2026/mikrut-vs-sanchez-izquierdo-2026-qualifying-round-1/17876832200954348) igazolja a Q1 meccs létezését. Mindkét játékos Q1 technikai adata a V1 ATP/GS **főtáblás** modellből kizárandó.

[Az utóbbi kettő forrásauditja](ATP_2026_USOPEN_2_QUALIFIERS_OFFICIAL_STATS_RESOLUTION_2026_11_22.csv). **Nem állítjuk, hogy a 150 játékosnak mindegyikéhez van többmeccses, tisztán főtáblás technikai minta.**

## 4. Kötelező integrációs korlátok

1. **Külön játékos-identitás:** ATP player ID külön mezőben, a Match Charting és TennisDB saját azonosítója külön. Martin Damm Jr nem azonos az idősebb Martin Damm édesapával; ezt a saját forrás [ATP-cikk](https://www.atptour.com/en/news/gea-wong-damm-top-100-august-2026) megerősíti.
2. **Időszabály:** 2026-ban csak 2025/26-os mérkőzések közvetlen előrejelző súllyal; a 105 TDI sorból **9** régi 2025-ös gördülő 52 hetes adat 2024-et is tartalmazhat, és ezért már `EXCLUDE_DIRECT_PREDICTOR_POSSIBLE_2024_MATCHES` jelzéssel tárolva.
3. **Pontos point event_time:** A charting `match_date` dátuma nem az egyes labdamenetek UTC vagy helyi időpontja. Az API-Tennis pont-adat késése, licencelt hitelessége és időbélyege nincs éles kulccsal mérve. **Nincs bevezetett, validált live előrejelzés.**
4. **Licencek:** A [Tennis Abstract Match Charting Project](https://github.com/JeffSackmann/tennis_MatchChartingProject/blob/master/README.md) **CC BY-NC-SA 4.0**. A jelenlegi, privát kutatási PR-ba meccslinkek és rövid, attribuált mutatók kerültek, **nem** a teljes charting nyers pont CSV. A későbbi kereskedelmi felhasználás nincs automatikusan engedélyezve.
5. **TDI ≠ MCP ≠ StatsNext:** nem szabad egymás minőségi skálájaként, pszichológiai ítéletként vagy közvetlen fogadási előnyként bemutatni. A 150/150 forráslefedettség **nem** jelent 150/150 validált profilt.
6. **GitHub kód/ágak:** a kutatási eredmények csak a nyitott PR #13 branch-en. A `main`, a B0 PR #12 és a külön V1 kódoló PR #14 nincs merge-elve vagy automatikusan újraírva.

## 5. Következő tényleges munkakapuk

- V1 kódfejlesztésnél a **72 egyedi ATP match-stats URL + hivatalos player-ID crosswalk** és a 96 soros scope/id/date audit legyen bemenet. Készítsünk deduplikált adatloader tesztet, forrásköri és időbeli no-lookahead tesztet, de **ne hivatkozzunk a charting adatokra kereskedelmi célra jogtisztázás nélkül**.
- Az élő API-Tennis szerződés és a licencelt `API_TENNIS_KEY` valós, privát smoke testje továbbra szükséges. Egyetlen meccs pont-időbélyegét vagy latency-előnyt sem szabad inventálni.
- A játékosok edzői, **többmérkőzéses megfigyeléseit, mentális attribútumokat** csak mérhető, ismétlődő, dátumozott jelek és bizonytalanság mellett lehet később ellenőrizni.
- 2026-11-22-i ranglista/master regisztert a kutatási PR nem írta felül, és a TDI nélküli 45 játékoshoz nem gyártottunk nem létező ATP 0–10 quality pontszámokat.

**Új ATP-beszélgetés átadása:** Olvasd a `PROJECT_MASTER.md`, `docs/ATP_START.md`, `docs/ATP_SESSION_LOG.md` fájlokat, majd a PR #13 ágon ezt a dokumentumot és a V3 150-es forrásmátrixot. **A 97/96 és 73/72 deduplikációs tény kötelező; ne kezdj régi kutatási körből.**
