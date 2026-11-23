# ATP – tartós munkanapló és döntésnapló
**Cél:** új beszélgetésben azonnal látható legyen, mi történt, milyen bizonyítékokkal, és mi a következő munkafolyamat. A forrásfájlok GitHubban és a privát ChatGPT Space-ben külön megvannak.

## 2026-11-21 – projektalap, kód, játékosadatok
- `PROJECT_MASTER.md` létrejött; kódaudit: létező Streamlit/Sportscore RapidAPI/Gemini/Discord prototípus; `atp_intelligence/` külön B0-val, esemény/SQLite alappal és tesztekkel.
- A végleges, felhasználói cél **privát Top150** ATP férfi egyes profil + korai változásérzékelés, nem SaaS.
- Az időbeli relevancia aktuális + előző év, 2024 és régebbi H2H közvetlen súlya nulla; elkészült a `docs/TEMPORAL_RELEVANCE_POLICY.md`.

## 2026-11-22 – 150 játékos dosszié és tartalmi audit
- 150/150 statisztikai/scouting dosszié és forráshivatkozás a GitHub `research/player_profiles/` útvonalán. Meccsarchívum aktuálisan 2026-11-15-ig. **Nincs** 150/150 többmeccsesen validált technikai, biomechanikai vagy mentális profil, és a teljes appintegráció hiányzik.
- Az áthozott `ATP(1).txt` alapján tételes audit: [az eredeti beszélgetés hiányai](ORIGINAL_ATP_THREAD_GAP_AUDIT_2026_11_22.md), [kilenc visszanyert követelmény](ATP_9_HIANYZOTT_TERULET_POTLASA_2026_11_22.md).
- 30 napos intuíciós/előrejelzési tanulási terv, Blind Prediction 50 próbás sablon, virtuális EV-napló, 10 tényezős pre-match, automatikus szűrés, PWA architektúra **dokumentált**. Ezek nem éles, működő modulok.
- A Tennis API korábban egyeztetett felhasználási engedélyét a felhasználó **ellenőrzött és lezárt** döntésként ismét megerősítette; az API tényleges integrációs státusza ettől külön.
- Korábbi új chat hívószó `ATP-MASTER-150` -> **végleg `ATP`** a felhasználó utasítására.
- **Privát teljes szövegarchívum:** új, kizárólag tulajdonosi hozzáférésű ChatGPT Space `ATP – Privát projektarchívum`; az oldal `ATP – Eredeti beszélgetés teljes szövegarchívuma (ATP(1).txt)` az áthozott 1006 sor szöveges változatával, nem nyilvános GitHubon. Eredeti fájl SHA-256 `ffceb2da5985304084e7d4d26ad9982d260106ae31198eede17d503404d24f01`.
- **Bájthű személyes Library-mentés:** a felhasználó korábban feltöltött eredeti `ATP(1).txt` fájlját 2026-11-22-én a saját ChatGPT Library-jába is feltöltöttük, `/ATP/Conversation_Archive/ATP(1)_eredeti_2026-11-22.txt` néven. Ez az eredeti TXT 36 620 bájtos forrás megőrzését szolgálja, szemben a Space-ben megjelenített, szerkesztett blokkszerkezetű szöveggel. A tartós Library-mentés sikeres visszaigazolást adott; a következő beszélgetésben fájlkereséssel elérhető, ha a hozzáférés rendelkezésre áll.
- **Jelenlegi handoff protokoll:** `docs/ATP_START.md`; új beszélgetésben a `ATP` hívószóra beolvasandó a PROJECT_MASTER, session log, a kilenc pótolt téma, a scouting index és szükség szerint a privát archívum. A további lényeges új döntéseket és munkát **GitHubra írjuk, nem kizárólag chatben hagyjuk**.

## Nyitott feladatok
1. A 12 edzői tudásterület 48 konkrét jelének eredeti, pontos listája még nincs meg ebben az áthozott TXT-ben; nem szabad kitalálni és eredetinek címkézni.
2. A kiválasztott Tennis API provider tényleges technikai végpontjai, feed sémája és live adatminősége auditálandó (az engedély **nem** vitás).
3. A 150 játékos részletes többmeccses technikai/mentális mintáinak és a korai, ponttörténetes modellnek a validálása.
4. A funkciók valódi appintegrációja, időbélyegzett előrejelzés/kalibráció, mobilos használhatóság és értesítések.
5. Újabb hosszú beszélgetés végén a lényeges döntések naplózása kötelező; teljes szó szerinti további chatarchívumhoz új export szükséges, ha a platform nem ad közvetlen olvasási hozzáférést.

## 2026-11-22 – projektutasítás a chatmemória-csúszás megelőzésére
- [Egyszeri ChatGPT-projektutasítás](ATP_PROJECT_INSTRUCTIONS.md) elkészült; a felhasználó az ATP Project utasításaihoz helyezheti, hogy új szálban az **ATP** hívószóra a csatlakozók ténylegesen olvassák be a GitHubot, a privát Library-beszélgetést és a Space-t. A projektutasítást az asszisztens nem tudta automatikusan módosítani a ChatGPT projekt UI-jában; ez egyszeri felhasználói beállítás.

## 2026-11-22 – Teljes szöveg automatikus megőrzése: kötelező új feladat

A felhasználó kérésére új, elsődleges adatbiztonsági követelmény: **minden új ATP-beszélgetés teljes szövegének automatizált, időbélyeges, forrásazonosított eltárolása**, nem csupán kivonat vagy kézi emlékeztető. Megvalósítási terv és egyértelmű ChatGPT webUI-korlát: [ATP_FULL_CONVERSATION_ARCHIVE_ARCHITECTURE.md](ATP_FULL_CONVERSATION_ARCHIVE_ARCHITECTURE.md). Kész alap-archívum van a 2026.11.22-ig áthozott szövegekhez; automatikus minden üzenetes archiválás **még nincs bekötve**. A javasolt megoldás a teljes üzenetet rögzítő saját privát chatfrontend + DB + backup; az Open WebUI ellenőrzött alternatíva, de a tényleges átállás nem történt meg.


## 2026-11-22 – Natív több AI-ból használható ATP Memory Hub kötelező feltétel
- Felhasználó: **„egy saját ATP-felület csak akkor jo ha integralni lehet ide vagy claude ai ban cursorba stb”** – az eredeti döntést szó szerint is rögzítve.
- A külön UI-fejlesztés felfüggesztve addig, amíg a közös memória nem működik a natív ChatGPT/Claude/Cursor kliensekben.
- [Platformfüggetlen memória/MCP terv](ATP_CROSS_AI_SHARED_MEMORY_MCP_ARCHITECTURE.md); ChatGPT aktuális Notion/GitHub plugin hozzáférése már működik, Claude/Cursor remote MCP hivatalos támogatása ismert, de a három kliens közös ATP-memória tényleges próba **még nincs meg**.
- **Szigorú korlát:** natív ChatGPT Plus custom MCP támogatást nem tekintünk bizonyítottnak; a Notion/GitHub app csatorna elsődleges. MCP nem interceptál automatikusan teljes beszélgetéseket. Minden platform teljes beszélgetésrögzítése külön megoldandó.


## 2026-11-22 – Első közös AI memória-kapu Notionban: LÉTREHOZVA ÉS CHATGPT-BŐL VISSZAOLVASVA

Létrehoztuk a meglévő Notion ATP Intelligence projektközpontban a **[09 · ATP – közös AI memória-kapu (ChatGPT / Claude / Cursor)](https://app.notion.com/p/420f603f0d2e81a28c89de2837019cde)** oldalt. Az új oldal `ATP-CROSSAI-001` verzió 1 tesztrekordot, az ATP indítókódot, a 2025–2026 időablakot, a lezárt Tennis API felhasználási engedélyt és a GitHub PROJECT_MASTER/ATP_START/SESSION_LOG forráshivatkozásokat tartalmazza. **ChatGPT Notion visszaolvasási ellenőrzés: PASS**, a rekord, évszabály és API-státusz megtalálható. **Claude: NOT TESTED, Cursor: NOT TESTED.** Ezeket a felhasználónak a megfelelő Notion kapcsolatok csatlakoztatása után ugyanazzal az oldal- és rekordteszttel kell kipróbálnia. A Notion oldalt nem tekintjük egyelőre automatikus, minden natív AI-üzenetet mentő archiválónak; arra külön capture-re van szükség.


## 2026-11-22 – ChatGPT irányítás, Cursor GitHub-szűkítés és Claude HWK import

- Felhasználó kimondta: **ez a ChatGPT-ben futó és GitHubon tárolt ATP a fő projekt**. Claude és Cursor **csak előzetes ChatGPT szakmai engedély + felhasználói jóváhagyás** után kódolhat, végezhet adatgyűjtést vagy módosíthat dokumentációt. Az AI-k felhatalmazását nem kezeljük technikai hozzáférési garanciának; a branch-protection és a felhasználói döntés kikényszerítendő.
- [AI-együttműködési és PR-engedélyezési rend](ATP_AI_COLLABORATION_GOVERNANCE.md) elkészült; `AGENTS.md` első részében az AI-k számára azonos szabály található. A Cursor GitHub-csatlakoztatása a Cursor felületén, **Selected repositories** és kizárólag `TBT8288/tbt-tennis-platform` kiválasztásával történjen. **A kapcsolat megtörténtét és branch-védelmet még nem ellenőriztük**; az első engedély csak olvasási teszt.
- Claude által újonnan feltöltött [Notion 10 – HWK AI/TBT történeti projekt](https://app.notion.com/p/420f603f0d2e819e90e7d0e988039fe5) feldolgozva: [23 pontos tartalmi audit](ATP_CLAUDE_HWK_2026_10_01_IMPORT_AUDIT.md), [feature-ötletek](ATP_CLAUDE_MODEL_FEATURE_ADOPTION.md), [kimeneti és backtest-követelmények](ATP_CLAUDE_PREDICTION_AND_VALIDATION_REQUIREMENTS.md), 12 historikus stílusjelölt, 18 forrásellenőrzendő állítás; külön alap `atp_intelligence/legacy_research.py` és `tests/test_claude_adoption.py` Githubra mentve. A történeti 77 teszt és hiányzó `tbt/` kód nem tekinthető átültetett, validált alkalmazásnak.
- [Notion 11 – import eredménye](https://app.notion.com/p/420f603f0d2e81978957e9cd225a8569) külön közös AI-olvasási kapuként létrejött. Az eredeti Claude forrásoldal megmaradt, a GitHub fő forrás.
- **Nyitott:** felhasználói Cursor-GitHub integráció engedélyezése csak kiválasztott repohoz; `main` branch védelme; első olvasási próba; a Claude-adaptáció új GitHub CI futásának ellenőrzése.


## 2026-11-22 – Cursor GitHub-csatlakozás: FELHASZNÁLÓ JELENTETTE, OLVASÁSI PRÓBA KÖVETKEZIK
- Felhasználó megerősítette: **„Cursor összekötve”**. A GitHub-integráció tényleges Cursor-oldali működését **még nem ellenőriztük**, ezért külön nincs `VERIFIED` státusz.
- Elkészült a [ATP-READ-001 kizárólag olvasási ellenőrzőfeladat](tasks/ATP-READ-001_CURSOR_CONNECTION_CHECK.md). **Csak repo/branch/commit és dokumentált jelenlegi modullista**, nincs kódmódosítás, commit, PR, scraping vagy terminálfuttatás.
- A Cursor első jelentését ide, a fő ChatGPT ATP-projektbe kell visszahozni. A GitHub `main` ágon történő írást/merge-et a felhasználói engedély és megfelelő branch-védelem nélkül továbbra sem engedélyezzük. A tényleges main-ág technikai branchvédelmét **nem állítottuk még be**.


## 2026-11-22 – ATP-READ-001 Cursor első olvasási jelentés értékelése

**Státusz: PASS (olvasási feladat), nincs implementációs ATP GO.**

- A felhasználó bemásolta a Cursor `ATP-READ-001` olvasási jelentését. A Cursor saját állítása szerint `origin = https://github.com/TBT8288/tbt-tennis-platform.git`, `main` branch, lokális `e470bb517b978e805d7ff71cdc7f47f34a27cce3` commit; nem futtatott kódot, nem módosított fájlt, és nem nyitott Pull Requestet.
- **Közvetlen GitHub-ellenőrzés ChatGPT-ből:** a jelzett `e470bb5` commit valóban létezik, és a korábbi `ATP-READ-001` átadási naplóbejegyzéshez tartozik. A repository neve, `main` alapértelmezett ága, valamint `atp_intelligence/probability.py`, `events.py`, `storage.py`, `legacy_research.py`, `tests/test_claude_adoption.py` és `app.py` létezése megerősítve.
- A Cursor cél- és hiányosság-összefoglalója megfelel a GitHub fő projektállapotának: privát ATP férfi egyes; 2025–2026 relevanciaablak; Top150 tartós profil; a korai coach-momentumdetektor, appintegráció és validált előrejelzési előny nincs késznek nyilvánítva.
- **Korlát:** a helyi munkakönyvtár változatlansága és a tényleges Cursor-oldali hozzáférés használata csak a felhasználó által átadott Cursor-jelentésből ismert; ezt a GitHub API nem tudja önmagában igazolni. A commit egyezése és a fájlok megléte viszont ellenőrzött.
- **Következő ellenőrzési pont:** mielőtt a Cursor/Claude első érdemi kódolófeladatot kap, a GitHub `main` ágának branch-védelme/PR-korlátja beállítandó és ellenőrizendő. `ATP GO: <task_id>` szakmai feladatkiadás és a projektgazda külön jóváhagyása nélkül nincs Cursor/Claude kódmódosítás, adat-scraping vagy merge.


## 2026-11-22 – ATP TDI kutatási folytatás (94 → 105)
- **Research PR #13** kizárólagos változtatások, `main` nem módosult. `research/player_profiles/ATP_TDI_TOP150_NORMALIZED_105_2026_11_22.csv`: **105 egyedi játékos**, **535 TDI-számérték**, **65 hétmutatós**, **40 kétmutatós**, **45 hiányzó**. A 11 új hétmutatós játékos külön forrásfájlban; a hiánylista `ATP_TDI_REMAINING_45_RESEARCH_QUEUE_2026_11_22.csv`.
- A 2025-ben publikált gördülő 52 hetes források **9 játékosnál esetleg 2024-es mérkőzést tartalmaznak**, ezért az új egységes CSV-ben `EXCLUDE_DIRECT_PREDICTOR_POSSIBLE_2024_MATCHES` időbeli tiltójelzést kaptak. Ez a felhasználó által választott 2025–2026 prediktív ablakot védi.
- A négy hiányzó TDI Top50 (Arthur Fery, Luca Van Assche, Daniel Merida, Arthur Gea) 2026-os ATP-torna eseménykontektsusa és Martin Damm Jr / édesapja névazonosítás 9 datált megfigyelésként mentve `ATP_TOP150_2026_FOUR_TOP50_CONTEXT_PLUS_DAMM_IDENTITY_2026_11_22.csv`; nem szabad ebből mentális diagnózist csinálni.
- Teljes forrásjegyzék, bemutatás és minőségi korlát: `research/player_profiles/ATP_TDI_105_PLAYER_AND_TOP50_CONTEXT_RESEARCH_2026_11_22.md`.
- Következő: 45/150 még hiányzó, forrásolt TDI érték, a meglévő 40 részleges játékos további öt mutatója; 2025/26 egyedi meccsszintű helyzetvalidáció; **nem módosult a forrás `main` és a fejlesztési PR #14**.


## 2026-11-22 – 105 teljes TDI + 31 friss MCP játékos = 150 forrásszintű audit

- A kutatási PR #13-on 27 + 13 korábban részleges játékos ATP/TDI hétmutatós sora is hivatalos 2026-os PDF-ek alapján teljessé vált. **Kanonikus TDI-végállapot jelenleg:** `research/player_profiles/ATP_TDI_TOP150_NORMALIZED_105_FULL7_735_VALUES_2026_11_22.csv` = 105/150 játékos × 7/7 érték = 735 mért érték, 45 TDI-hiányos.
- A TDI-hiányos 45 játékosra a Tennis Abstract Match Charting Project friss 2025–26 mérkőzésindexét kerestük: **31/45 friss match charting**, 97 datált match forráslink (38 db 2025, 59 db 2026), 73 scope-ellenőrzésre váró ATP/GS főtábla-jelölt, 20 más eseménykör, 4 selejtező; **14 játékoshoz ilyen match charting sincs**.
- Új kulcsfájl: `research/player_profiles/ATP_TOP150_2026_TECHNICAL_EVIDENCE_COVERAGE_MASTER_RESEARCH.csv`: 150/150 egyedi játékos technikai forrásátadása (105 TDI, 31 MCP-only, 14 csak korábbi általános statisztika), egyetlen sorban rang, source snapshot, scope/QA-gate.
- Név szerinti hiánylista + 150 játékos auditleírása: `research/player_profiles/ATP_2026_11_22_150_PLAYER_TECHNICAL_SOURCE_AUDIT.md`. A négy Top50 Fery, Van Assche, Mérida, Géa match-szintű technikai kontextusa és 11 külön chartolt 2026-os meccs URL-je külön CSV-ben.
- **CC BY-NC-SA 4.0** MCP; a nem kereskedelmi attribúciós és share-alike feltételek mellett csak linkek + rövid mért kivonatok kerültek a nyilvános kutatási PR-ba, nem másoltuk a nyers pontszintű CSV-ket. Privát használat jelenleg; későbbi SaaS-ra NEM automatikusan engedélyezett. 
- Az MCP önkéntes, nem reprezentatív minta; nem egyenlő ATP/TDI optikai 0–10 quality-val. A 2025-ös rolling 52 hét részben 2024-et érhet: 9 TDI rekord prediktív közvetlen súly tiltva. Pszichológiai/mentális 0/150 továbbra nem validált, sem a live edge.
- **Csak a PR #13 research ága változott.** A `main` és a külön kódos PR #14 továbbra nem lett módosítva/merge-elve. Új ATP chatben a fenti kanonikus 150/105/31/14 adatokat olvasd, ne kezdd újra a teljes játékoskutatást.


## 2026-11-22 – V4 kutatási záró QA: 72 ATP ID + dátumforrások

- Az előző **73 MCP főtábla-jelölt** valójában **73 játékos–mérkőzés asszociáció / 72 egyedi meccs**; az eredeti **97 MCP link** ugyanígy **96 egyedi match**, mert Daniel Mérida és Marco Trungelliti 2026-04-23-i Madrid Masters találkozója mindkét játékosnál megvolt. A duplikációt és hibaeredetet dokumentáltuk.
- Hivatalos 2025/26 ATP eredményarchívumokat személyenként, pontos fordulóval visszakerestünk: **72/72 külön main-draw MCP-meccshez** hivatalos meccsstatisztikai ID, két játékos ATP-profil URL, forduló visszanyerve. `research/player_profiles/ATP_MCP_72_UNIQUE_OFFICIAL_ATP_MATCH_CROSSWALK_2026_11_22.csv`.
- A 72 naptári nap QA: **48** ATP day + charting azonos; **19** 2025 archívum-dátum hiánya (külön 19 fős dátumozott source QA); **5** archívum és charting eltérő nap (korabeli ATP/tornaszervezői/Tennis.com/L'Équipe bizonyítás alapján rekonciliált). Így a 96 egyedi charting sorban a 72 célkör meccseinek match-ID-je és napja is egyenként hivatkozva van: `research/player_profiles/ATP_MCP_96_UNIQUE_MATCHES_CANONICAL_DATES_OFFICIAL_IDS_FINAL_QA_2026_11_22.csv`. Nincs bizonyított pontonkénti eseményidő.
- A 150 fős **V3 forrásátadás** osztályai: 105 TDI (735 mért szám), 26 MCP főtáblás, 1 főtáblás egyedi, 11 vegyes versenykörű season, 5 csak más scope, 2 csak selejtező. Tehát 150/150 kutatási forrás, de **nem 150/150 tiszta/validált főtáblás coaching-profil**.
- A külön erre szolgáló [V4 átadás](../research/player_profiles/ATP_DATA_RESEARCH_V4_CANONICAL_HANDOFF_2026_11_22.md) az ELSŐ kutatási olvasmány új chatben. PR #13 tovább draft/open, nem merge; main és PR #14 kód változatlan. MCP CC BY-NC-SA 4.0. A TDI 9 régi rolling 52 hét potenciális 2024-es szennyezésre tiltva.


## 2026-11-22 – 73/73 MCP charting ATP meccsazonosító ellenőrzés

- A korábbi 73 lehetséges ATP/GS főtáblás Tennis Abstract MCP match charting hivatkozást **73/73 meccspár szintjén** hivatalos ATP 2025/26 archív eredménylistából match-stats és H2H URL-hez párosítottuk (30 + 22 + 21 kutatási rekord).
- **73 rekord, de 72 egyedi mérkőzés**: Daniel Mérida–Marco Trungelliti 2026 Madrid Masters két játékosindex-hivatkozása ugyanarra a `/archive/2026/1536/ms098` match ID-re mutat.
- Új kanonikus dokumentum: `research/player_profiles/ATP_MCP_ALL_73_OFFICIAL_MATCH_ID_CROSSWALK_CANONICAL_2026_11_22.csv`; audit: `research/player_profiles/ATP_MCP_2026_11_22_73_OF_73_OFFICIAL_MATCH_IDS_RESEARCH.md`.
- **Év / kategória:** 21 db 2025, 52 db 2026; 20 GS, 25 M1000, 7 ATP500, 21 ATP250 charting-index rekord.
- **QA maradék:** a konkrét charting dátumának és fordulójának a hivatalos *meccsnap/draw* megfeleltetése még külön folyamat; a torna évének/kategóriájának, résztvevőinek és match ID-jának egyenlősége igazolt. Nem használható kontrollálatlanul modellbe, MCP licenc nem kereskedelmi, mintavétel önkéntes.
- A kutatási PR #13 külön ágán írva, `main` és PR #14 nem módosítva. **Új ATP szál** e CSV-kből folytassa, ne a 150 fős általános kutatást ismételje.


## 2026-11-23 – A november 22-i privát források leltára

A visszaolvasott fájllistában három szöveges bejegyzés (az archivált példánnyal együtt), két képernyőkép és két generált ZIP található. A Macen készült teljes mentés útvonalát a korábbi beszélgetés terminálkimenete azonosította; annak helyi tartalmát ebből a munkamenetből nem ellenőriztük. A személyes fájlokhoz tartozó linkek a tulajdonos ChatGPT-beszélgetésében érhetők el. A 72 mérkőzés eredményellenőrzése a következő kutatási feladat.


## 2026-11-23 · Kapcsolatok ellenőrzése

GitHub: a projektleírás és a #13, #14 PR olvasható. Notion: az ATP-CROSSAI-001 rekord visszaolvasható. Firecrawl: a hivatalos Jannik Sinner ATP-profil lekérése sikeres (https://www.atptour.com/en/players/jannik-sinner/s0ag/overview). Claude: a bejelentkezési műveletet az automatikus jóváhagyás használati limitje megállította. Cursor: a webes felület biztonsági ellenőrzést mutatott. A Claude és Cursor saját Notion- és GitHub-visszaolvasása egyelőre ellenőrizetlen.

A kutatás folytatási pontja a 72 azonosított főtáblás meccs győztesének, szetteredményének és feladási státuszának egyeztetése.
