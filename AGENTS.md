## KÖTELEZŐ AI-ALVÁLLALKOZÓI MUNKAREND – CLAUDE / CURSOR (2026-11-22)

**A fő ATP projekt kizárólag a jelen ChatGPT-ben és ebben a GitHub repóban működik.** A Claude és Cursor segítő, korlátozott feladatvégrehajtó. **Kötelező: [ATP_AI_COLLABORATION_GOVERNANCE.md](docs/ATP_AI_COLLABORATION_GOVERNANCE.md).**

- **Alapértelmezés: READ-ONLY.** Ne módosíts kódot, ne végezz scrapinget, ne futtass autonóm ügynököt, ha nincs aktuális, ChatGPT által írásban meghatározott `ATP GO: <task_id>` és a felhasználó saját hozzájárulása.
- Feladat esetén csak saját, elkülönített branch, Pull Request; **soha ne push/merge közvetlenül a `main` ágra**. Ne kapcsolj be auto-merge/auto-approve folyamatot.
- Forrás: `PROJECT_MASTER.md`, `ATP_START.md`, `ATP_SESSION_LOG.md`. Régi Claude HWK `tbt/` kódot és történeti 77 tesztet ne tekints jelenlegi `main` kódnak.
- A ChatGPT `GO` szakmai eljárási jelzés, **nem technikailag kikényszerített GitHub-védelmi szabály**; végső engedélyt a felhasználó ad, a GitHub branch ruleset/PR védelem a gyakorlati zár.

# ATP Intelligence – folyamatos projektkontextus az AI-kódolóknak
**A felhasználói hívószó egyszerűen: `ATP`.** Amikor a beszélgetésben `ATP` szerepel projektfolytatási értelemben, olvasd el a GitHub verziókezelt projektállapotát.

**Mindig olvasd először:**
1. [PROJECT_MASTER.md](PROJECT_MASTER.md) – jelenlegi scope és munkastátusz
2. [docs/ATP_START.md](docs/ATP_START.md) – új beszélgetés átadási szerződés, [ChatGPT projektutasítás](docs/ATP_PROJECT_INSTRUCTIONS.md)
3. [docs/ATP_SESSION_LOG.md](docs/ATP_SESSION_LOG.md) – legutóbbi munka és döntések
4. [docs/ATP_9_HIANYZOTT_TERULET_POTLASA_2026_11_22.md](docs/ATP_9_HIANYZOTT_TERULET_POTLASA_2026_11_22.md) – eredetileg kimaradt követelmények
5. [docs/TEMPORAL_RELEVANCE_POLICY.md](docs/TEMPORAL_RELEVANCE_POLICY.md) – időbeli relevancia
6. [research/player_profiles/ATP_COACH_SCOUTING_INDEX_2026_11_22.md](research/player_profiles/ATP_COACH_SCOUTING_INDEX_2026_11_22.md) – Top150 scoutrendszer

**Őrizd meg:** a két játékos független állapotát; ATP/GS férfi egyes fókuszt; Top150 alapadatokat; 2025–2026 időablakot (évente fordul); valódi break előtti jelzés validációját; a nem megfigyelhető pszichológiai/technikai jelek bizonytalanságát; a felhasználó által lezártnak megerősített Tennis API felhasználási engedélyt.

**Valódi munkafolyamat:** forrás -> implementáció/teszt -> ellenőrzött GitHub commit -> `PROJECT_MASTER.md` és `docs/ATP_SESSION_LOG.md` frissítés. Ne állíts be meg nem valósított funkciót késznek. Minden jelentős döntés/fájlállapot legyen tartósan rögzítve.

**Bizalmasság:** a nyilvános repóba ne másolj teljes személyes beszélgetést vagy titkot. Az eredeti 1006 soros `ATP(1).txt` **bájthű fájlmásolata** a felhasználó személyes ChatGPT Library `ATP/Conversation_Archive/ATP(1)_eredeti_2026-11-22.txt` útvonalán van, valamint a tulajdonos privát ChatGPT Space-ében (`ATP – Privát projektarchívum`) megtalálható az olvasható szöveges átírás is. Mindkettő jogosultságot igényel; a nyilvános GitHubra nem kerül a privát teljes chat.

A `ATP` hívószó nem garantált automatikus chatmemória; csak az ellenőrizhető projektfolytonosság indítója.
