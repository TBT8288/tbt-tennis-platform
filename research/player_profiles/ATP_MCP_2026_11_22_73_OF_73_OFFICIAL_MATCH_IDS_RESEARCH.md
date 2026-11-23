# ATP Intelligence – 2026-11-22: 73/73 chartolt rekord hivatalos ATP meccsazonosítóval

**Státusz:** a korábban „73 potenciális ATP/GS-főtáblás chartolt mérkőzés” csoportot a hivatalos ATP eredményarchívumában **73/73 pár szerint, tornán és éven belül meccsazonosítóhoz** kötöttük. Ez **72 különálló mérkőzés**, nem 73 külön match: a 2026-os Madrid Masters Marco Trungelliti–Daniel Mérida találkozója mindkét rangsorbeli játékosnál szerepelt és ugyanarra az ATP `2026/1536/ms098` meccsazonosítóra mutat.

## Új, ellenőrzött forrásállományok

- **[Kanonikus összesített 73 soros ATP crosswalk](ATP_MCP_ALL_73_OFFICIAL_MATCH_ID_CROSSWALK_CANONICAL_2026_11_22.csv)** – egy CSV: rang, játékos, chartolt dátum és torna, eredeti MCP chart-link, hivatalos ATP meccsstatisztikai URL, H2H, hivatalos tornaeredmények, Grand Slam / M1000 / ATP500 / ATP250, borítás, ellenőrzési státusz.
- Első 30 rekord / 29 egyedi meccs: [11 hivatalos 2026-os ATP torna](ATP_MCP_2026_OFFICIAL_MATCH_ID_CROSSWALK_2026_11_22.csv).
- Második 22 rekord / 2026: [további hivatalos ATP tornák](ATP_MCP_2026_SECONDARY_ATP_MATCH_ID_CROSSWALK_2026_11_22.csv).
- Harmadik 21 rekord / 2025: [hivatalos ATP történeti eredményarchívum](ATP_MCP_2025_OFFICIAL_MATCH_ID_CROSSWALK_2026_11_22.csv).
- [Mind a 73 ATP versenykategória, borítás és hivatalos időablak ellenőrzése, ideértve a 2026 US Open augusztus 30-i, frissített kezdődátumát](ATP_MCP_73_OFFICIAL_EVENT_DATE_QA_USOPEN_CORRECTION_2026_11_22.csv).

## Valóban auditált lefedettség

| Vizsgálat | Darab | Státusz |
|---|---:|---|
| ATP/Slam főtábla-jelölt charting-index rekord | 73 | 73/73 azonosítható ATP párosítás |
| **Különálló meccsazonosító** (duplázás után) | **72** | 72/72 hivatalos match-stats hivatkozás |
| 2025-ös charting-rekord | 21 | ATP 2025 archívummal párosítva |
| 2026-os charting-rekord | 52 | ATP 2026 archívummal párosítva |
| Grand Slam | 20 | versenykategória ATP naptár szerint |
| ATP Masters 1000 | 25 | versenykategória ATP naptár szerint |
| ATP 500 | 7 | versenykategória ATP naptár szerint |
| ATP 250 | 21 | versenykategória ATP naptár szerint |
| **Meccsnap/forduló egyéni, teljes ATP eredmény sor szerinti QA** | 0/73 külön igazolt | A charting-link dátuma hivatalos tornaintervallumon belüli, de nem mértük végig a konkrét hivatalos napi draw sorát minden meccsnél |

**Fontos minőségi különbség:** a hivatalos H2H+Stats linknek ugyanazokat a játékosokat *ugyanazon a tornán és évben* kell mutatnia, és a chartolt dátumnak a hivatalos tornaidőablakon belül kell lennie. Mivel az egyes meccsek *pontos fordulóját, konkrét naptári napját* még nem ellenőriztük mind a 73-nál a naphoz szűrt ATP draw eredményből, a kanonikus CSV két oszlopában **`NOT_AT_INDIVIDUAL_MATCH_LEVEL`** marad a dátum- és fordulóigazolás. Ezért nem jelentünk „73/73 teljes meccs-meta validációt”.

### Miért 73/72?

A meccsszintű adatot nem szabad kétszeres súllyal belevenni a modellbe, ha a charting játékosindex mindkét résztvevőnél listázza. **Egyedi kulcs:** az ATP match-stats link stabil, pl. `/archive/2026/1536/ms098`. A 2026-os Madrid meccsen Daniel Mérida az eredménylista szerint 6–4, 1–6, 7–6(6) arányban győzött Marco Trungelliti ellen; a meccs H2H linkje és a hivatalos stats URL már összepárosítható. [ATP Madrid hivatalos mérkőzés](https://www.atptour.com/en/scores/stats-centre/archive/2026/1536/ms098).

### Források

**ATP 2025 és 2026 naptár + tornaeredmények:**
- [ATP 2025 versenynaptár](https://www.atptour.com/en/news/what-is-the-2025-atp-tour-calendar)
- [ATP 2026 versenynaptár](https://www.atptour.com/en/news/what-is-the-2026-atp-tour-calendar)
- [ATP 2026 Wimbledon eredmények](https://www.atptour.com/en/scores/current/wimbledon/540/results)
- [ATP 2026 Canada Masters eredmények](https://www.atptour.com/en/scores/current/toronto/421/results)
- [ATP 2026 Párizs eredmények](https://www.atptour.com/en/scores/current/paris/352/results)
- [ATP 2026 Umag eredmények](https://www.atptour.com/en/scores/current/umag/439/results)
- [ATP 2025 Wimbledon archívum](https://www.atptour.com/en/scores/archive/wimbledon/540/2025/results)
- [ATP 2025 Australian Open archívum](https://www.atptour.com/en/scores/archive/australian-open/580/2025/results)

**Külön adatminőségi megfigyelés:** az ATP saját Umag 2026 döntő **hivatalos meccseredmény-oldala** Daniel Mérida–Damir Džumhur eredményét **6–2, 5–7, 6–2** formában jelzi, míg egyes kapcsolódó sajtócikkek / összefoglalók eltérő elsőszettet közölnek. A hivatalos egyedi meccsrekord az irányadó; más cikk adatait a meccsnél külön figyelmeztetéssel kell kezelni, nem önkényesen összegezni.

## 150 fős profilkör és modellezhetőség

A kapcsolódó kutatási mátrix: [150/150 forrásolt technikai jellegű adat: 105 TDI seven-metric, 31 charting linkes, 11 vegyes scope 2026 szezonstatisztika, 1 tour main draw egy meccs, 2 selejtező egy meccs](ATP_TOP150_2026_TECHNICAL_EVIDENCE_COVERAGE_V2_150_SOURCED.csv). Ez **forráselérhetőség, nem 150 teljes, validált edzői dosszié.**

MCP (Tennis Abstract Match Charting Project) adat [CC BY-NC-SA 4.0](https://github.com/JeffSackmann/tennis_MatchChartingProject/blob/master/README.md), **nem kereskedelmi**, attribúció/sharealike; az ATP eredmény- és tracking-oldalak külön felhasználási feltételek alatt állnak. Az új kutatás egyedi forráslinkeket tárol, **nem archivál tömegesen nyers ATP vagy MCP ütéssorokat**.

Következő konkretizált ellenőrzés:
1. A 72 egyedi mérkőzéshez az ATP napi draw dátuma és fordulója, eredménye (és WO/retired státusza) egyenként.
2. 2025/26-os pontonkénti chartolt események elérhetősége, eltérő minták, borítás és esemény-ID egyeztetés.
3. Időben korrekt no-lookahead / `as_of` adatelérhetőség, licenc; csak ezután prediktív használat, Brier/log-loss és hamis momentumjelzés mérése.

A kutatási ág **PR #13**, `main` változatlan, a fejlesztési PR #14 ettől független.
