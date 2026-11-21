# ATP Intelligence – követett játékosok: Top 150

**Jelenleg hatályos döntés: 2026-11-21.** Az összes, az ATP férfi egyesranglista **1–150. helyén álló játékos** kap saját, tartós Player Intelligence alaprekordot. A ranglistahelyezés elegendő a bekerüléshez: **nem kötelező, hogy a játékos a 2026-os ATP-főtáblán már szerepelt legyen**.

A régebbi Top 100-as hatókör ezzel **megszűnt**; a történeti Top100 CSV változatlan archív pillanatképként marad meg.

## Ellenőrzött alapállományok

- [ATP Top150 – 2026. november 16.](atp_top150_2026_11_16.csv): **150 játékos**, ranghely, név, ország, ranglistapont, rangsor dátuma, forrás és ellenőrzési státusz.
- [2026-os szezonstatisztika](atp_top150_season_stats_2026.csv): **150 rekord**, ebből **146** játékosra ellenőrzött, játékosnév + ranglistapont szerint megfelelő TennisDB idénystatisztika. A 146 rekordban győzelem/vereség és – ha a forrásban létezik – Win%, Elo, Serve+, Return+, Pressure+, szett-győzelmi arány. A hiányzó mező üres, **nem 0**.
- **Négy további ellenőrzést igénylő statisztikai sor:** 107 Otto Virtanen (570 pont), 116 Clément Chidekh (512 pont), 130 Max Alcalá Gurri (446 pont), 132 Nikolas Sánchez Izquierdo (438 pont). A ranghelyüket több rangsorforrás egyezteti, de a TennisDB eltérő ranghely-/pontállapota alapján nem kerülhet hozzájuk bizonytalan 2026-os statisztikai érték.

## A források és a pontosság

- [Ranglista 1–100](https://www.tennis.esp.br/en/rankings?date=2026-11-16&tour=ATP)
- [Ranglista 101–200](https://tennis.esp.br/en/rankings?date=2026-11-16&page=2&tour=ATP)
- [Független rangsorellenőrzés](https://www.sportscore.es/tennis/rankings/atp/)
- [TennisDB 2026 szezonstatisztika](https://tennis-db.com/seasons-and-rankings?year=2026)

A forrásokat **azonos érvényességi dátumhoz** kell kötni. A TennisDB helyezési sorrendje egyes játékosoknál eltér a másik két ranglistától (pl. Virtanen). **Nem rendeljük a statisztikát pusztán ugyanahhoz a sorszámhoz!** Ha név és ranglistapont nem támasztja alá az egyezést, üresen hagyjuk és ellenőrzésre jelöljük.

**A statisztikai összesítések nem jelentenek automatikusan játékstílus- vagy sérülésdiagnózist.** A 150 játékos egyedi technikai/taktikai erősség- és gyengeségprofilját további, mérkőzés- és forrásidőhöz kötött adatokkal fogjuk felépíteni.

## A célversenyek

- **Elemzendő mérkőzések:** férfi egyes főtábla ATP 250, ATP 500, Masters 1000, ATP Finals és Grand Slam.
- **150 részletes játékosprofil:** a legutolsó elfogadott, dátumozott ATP Top150-rangsor alapján.
- **Eseti meccspartner 150-en kívül:** ideiglenes, minimális mérkőzésadat, hogy a releváns ATP/Grand Slam-főtáblás mérkőzés értelmezhető maradjon. Nem indítunk külön, egész évben követett profilt.
- **Challenger/ITF:** nincs önálló élő eseményfigyelés; csak a jelenlegi Top150 játékos történeti múltjának bizonyító adatai használhatók, ha ténylegesen indokolt.

## Implementáció – 2026. november 21.

- [`ATPTop150` validálás](../../atp_intelligence/roster.py) – 150 név, 1–150 helyezés, forrás és dátum ellenőrzése, eltérő szezonstatisztikai hiány kezelésével.
- [`ExpertArchive` SQLite import](../../atp_intelligence/archive.py) – a 150 játékos és a rendelkezésre álló forrásolt szezonstatisztikák tárolása; a szakértői megfigyelések a követett játékosokra szűrve.
- [Automatizált tesztek](../../tests/test_expert_archive.py) – Top150, előző 100-as DB-séma migrációja, import és adatminőség.

**Nem kész:** stabil provider-független ATP player ID összerendelés, heti ranglistafrissítés, a 4 vitás statisztika feloldása, minden játékoshoz részletes ütés- és taktikai profil, Streamlit élő feed szűrőbe való bekötése. Ezek külön fejlesztési feladatok.

*Az itt szereplő rank- és statadatok 2026. november 16-i ranglistapillanatképre és 2026. november 21-én ellenőrzött forrásokra vonatkoznak. Nem jövőbeli garanciák.*
