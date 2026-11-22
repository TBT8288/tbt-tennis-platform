# ATP – AI együttműködési és változtatás-engedélyezési szabályzat

**Státusz:** 2026-11-22, a felhasználó kifejezett irányítási döntése. **Hívószó:** `ATP`.
**Hivatalos repo:** [TBT8288/tbt-tennis-platform](https://github.com/TBT8288/tbt-tennis-platform), **`main`** a jelenlegi hiteles projektállapot.
**Forrás:** a felhasználó üzenete: „A FÖ PROJEKT AZ AMI ITT FUT MOSTANTOL ES AMI GITHUBON VAN EZT MAJD A CLAUDE ES A CURSOR JAVITHATJA KI MIKOR KODOLAS LESZ VAGY ADAT SCRAPPING STB DE AZT IS UGY HOGY TE ADSZ RA ENGEDELJT!”

## 1. Központi projekt és szerepek
- **Projektgazda, végső döntés és tényleges jogosultságok tulajdonosa:** a felhasználó.
- **ChatGPT itt, az ATP projektben:** fő tervező/koordinátor, egyetlen verziókezelt projektterv karbantartója, más AI-feladatok **szakmai előzetes jóváhagyási pontja**. A ChatGPT szakmai „GO”-ja feladatindítási ajánlás, **nem GitHub-jogosultság, nem technikailag kikényszerített ACL**, és nem helyettesíti a felhasználó végső jóváhagyását.
- **Cursor:** meghatározott fejlesztési feladatra kódírás, tesztelés, hibakeresés, és ellenőrzésre javasolt PR.
- **Claude:** meghatározott kódellenőrzés, adatfeldolgozás, adatkutatás és technikai alternatívák; változtatás csak ugyanezzel a munkafolyamattal.
- **GitHub:** a kód és aktuális projektállapot hiteles fő forrása (`PROJECT_MASTER.md`, `docs/ATP_START.md`, `docs/ATP_SESSION_LOG.md`, `AGENTS.md`).
- **Notion:** kutatási archívum és közös olvasási kapu; történeti Claude-adat **nem** írja felül a GitHub döntéseit.

## 2. Nem engedélyezett önálló eljárások
- **TILOS** a `main` közvetlen szerkesztése/push/merge a Claude/Cursor által; csak célra kijelölt branch és Pull Request.
- **TILOS** az AI-ügynökök önálló, általános projekt-átalakítása, back-end/API cseréje, adatbázis reset, kód törlése, privát SaaS-sá alakítása.
- **TILOS** adatforrás megkerülése, jogosulatlan scraping, a Tennis API engedélyének újratárgyalása, ellenőrizetlen új 1,95-ös szorzó vagy fals stílus/mentálcímke éles beépítése.
- **TILOS** token, API-kulcs, felhasználói beszélgetés vagy privát adat a mostani **public** GitHub repóba.
- **TILOS** automatikus PR-összevonás, agent write-to-main, kontrollálatlan háttérügynök és automatikus PR-jóváhagyás – az ilyen Cursor/GitHub funkciókat ne kapcsoljuk be.
- **TILOS** külön, másik „fő ATP repo” létrehozása vagy a kód más szolgáltató Origin tárhelyére tükrözésének elsődlegesre állítása, hacsak a felhasználó és a ChatGPT közösen külön nem döntött róla.

## 3. Feladatkiadás és engedélyezés
1. A felhasználó az ATP-projektben meghatározza a kért változtatást.
2. ChatGPT elolvassa a GitHub aktuális `main` ágát, tisztázza a technikai követelményt, és **írásban kiadja a feladattervet**: `task_id`, scope, források, módosítható útvonalak, tiltott útvonalak, tesztek, eredmény, kockázatok.
3. **A felhasználó jóváhagyja** a feladatot; a ChatGPT kifejezetten `ATP GO: <task_id>` szakmai engedélyt ad. Ez még nem önálló technikai jogosultság.
4. Cursor vagy Claude a megfelelő repón **külön branch-en** dolgozik, a konkrét `task_id` alapján. A PR leírja a módosításokat és ellenőrzéseket. Nincs main merge.
5. ChatGPT – amikor a felhasználó visszahozza a PR-t vagy linket – ellenőrzi diff, tesztek, no-lookahead, adatforrások és hatókör alapján, és **jóváhagyást javasol** (`REVIEW PASS` vagy `CHANGES REQUIRED`).
6. **A felhasználó véglegesen engedélyezi a merge-et**. Frissülnek a dokumentumok és a munkanapló; új tényleges GitHub állapotból dolgozunk tovább.

**Technikai fontos tény:** a ChatGPT nem állandóan futó engedélyező szerver, nem fog automatikusan érzékelni minden Cursor-műveletet. Az összes külső eszköz tételes engedélyezése GitHub branch/ruleset, távoli hozzáférés és a felhasználó jóváhagyása révén kényszeríthető ki. A `ATP GO` szöveg folyamatjelző, önmagában nem security control.

## 4. Első Cursor csatlakozás pontos folyamata
1. [Cursor Settings / Integrations](https://cursor.com/dashboard/integrations) → **GitHub Connect** (hivatalos beállítás: https://prod.cursor.com/docs/integrations/github).
2. **Csak** `Selected repositories` → `TBT8288/tbt-tennis-platform`; ne `All repositories`, és ne új Cursor Origin repó.
3. A Cursorban a meglévő repositoryt nyisd/clone-old; **a `main` olvasása és a saját branch-szerkesztés** történjen. Ne kérj automatikus `main` írási engedélyt.
4. Automations / Cloud Agents / auto-approve / auto-merge funkciók **ne legyenek beállítva** addig, amíg a fenti átadás és GitHub technikai védelme nincs kipróbálva.
5. A felhasználó **egyszer** állítson be megfelelő GitHub branch védelmet / rulesetet a `main`-re: pull request nélkül nincs merge, force push és branch törlés tiltva, a tesztek legyenek kötelezők, ha a repo és a GitHub csomag ezt engedi. **Ezt az asszisztens nem állította be**.
6. Első próbafeladat: Cursor csak olvassa el `PROJECT_MASTER.md`, `AGENTS.md`, `docs/ATP_AI_COLLABORATION_GOVERNANCE.md` és írja le, mit lát. Semmi kódmódosítás.

## 5. A Claude 2026-10-01-i történeti anyag integrációjának státusza
A [Claude eredeti 10-es Notion oldal](https://app.notion.com/p/420f603f0d2e819e90e7d0e988039fe5) módszertani adattárként megőrizve; [audit](ATP_CLAUDE_HWK_2026_10_01_IMPORT_AUDIT.md), [feature-terv](ATP_CLAUDE_MODEL_FEATURE_ADOPTION.md), [kimenetek és validáció](ATP_CLAUDE_PREDICTION_AND_VALIDATION_REQUIREMENTS.md), [stílusok](../research/player_profiles/CLAUDE_HWK_2026_10_01_STYLE_CANDIDATES.csv) és [forrásellenőrzés](../research/CLAUDE_HWK_RESEARCH_CLAIMS_TO_VALIDATE.csv). A korábbi `tbt/` fájlok a mostani GitHubon nem találhatók; a régi 77 teszt nem bizonyíték a jelenlegi kód működésére. Claude/Cursor ezeket csak előzetes kifejezett feladat után kódolhatja be.

## 6. Engedélyezett első lépés
**Most kizárólag GitHubhoz való technikai csatlakozás és a meglévő kód olvasása engedélyezett.** Nem adunk általános engedélyt kódmódosításra. Az első implementációra külön `ATP GO` és felhasználói jóváhagyás szükséges.
