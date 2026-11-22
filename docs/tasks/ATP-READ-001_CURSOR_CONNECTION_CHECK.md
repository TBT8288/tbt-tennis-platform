# ATP-READ-001 – Cursor GitHub kapcsolat első, kizárólag olvasási tesztje

**Kiadó:** ChatGPT ATP projekt; **felhasználói bejelentés:** Cursor–GitHub kapcsolat létrejött (2026-11-22).
**Szakmai engedély:** kizárólag READ-ONLY ellenőrzés; nem implementációs `ATP GO`.
**Hivatalos repository:** `TBT8288/tbt-tennis-platform`; célág: `main`.

## Cél
Bizonyítani, hogy a Cursor az **aktuális** GitHub projektből dolgozik, nem egy korábbi Claude-projektből, nem másolt vagy kitalált kódból.

## A Cursor feladata
1. Csak olvasási műveletet végezzen. Nyissa meg a projektet a GitHubról, és ellenőrizze a repository pontos `owner/repo` nevét, a megnyitott aktuális branch-et és lehetőség szerint a legutóbbi commit rövid SHA-ját.
2. Olvassa el: `PROJECT_MASTER.md`, `AGENTS.md`, `docs/ATP_START.md`, `docs/ATP_SESSION_LOG.md`, `docs/ATP_AI_COLLABORATION_GOVERNANCE.md`.
3. Ellenőrizze létező fájlok alapján a `app.py`, `atp_intelligence/`, `tests/` területeket. Ne állítsa késznek azt, amire nincs megfelelő kód és teszt.
4. Készítsen rövid **CSAK CHATBEN** olvasási jelentést: repository/branch/commit; olvasott fájlok; aktuális cél; három valóban meglévő modul; három hiányzó vagy nem validált funkció; a módosítások engedélyezési rendje.
5. Külön válaszoljon: **„Módosítottam-e fájlt vagy nyitottam-e Pull Requestet?”** A helyes válasz ennél a feladatnál `NEM`, ha az olvasási tesztet betartotta.

## Szigorú korlátok
- NINCS fájlszerkesztés, nincs új fájl/branch/commit, sem PR, nincs törlés, nincs dependency install, nincs kódfuttatás vagy script/scraper futtatás.
- NINCS automatikus agent-módosítás, terminálparancs, rebase, push, merge vagy titokkezelési művelet.
- A korábbi Claude `tbt/...` történeti moduljait nem nevezzük jelenlegi GitHub-kódnak.
- A jelentést másolja vissza a felhasználó a ChatGPT ATP szálba, **vagy** adja meg a Cursor megtekinthető beszélgetés-hivatkozását, ha az ténylegesen elérhető.
- A ChatGPT elemzi az ellenőrizhető állításokat, és csak külön felhasználói engedéllyel ad később konkrét kódolási munkát.

**Elfogadási feltétel:** egyetlen fájl sem változott; a Cursor helyesen azonosította a projektet és a kötelező szabályokat; a felhasználó megkapta a tényszerű jelentést.
