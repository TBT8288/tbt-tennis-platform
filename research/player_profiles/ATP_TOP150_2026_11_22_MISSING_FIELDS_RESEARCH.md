# ATP Top150 – hiányzó játékosadatok forrásellenőrzése (2026-11-22)

**Státusz: kutatási JAVASLAT, nem összevont adatbázis-frissítés.** Az eredeti `main` regisztert, a `PROJECT_MASTER.md` dokumentumot és az `app.py` alkalmazást ez a PR nem módosítja.

## Cél és rögzített keret

- A Top150 rangsor `ranking_as_of=2026-11-16` állapotából indulunk; az itt szereplő rank NEM élő ATP-helyezés.
- Kiinduló regiszter: `research/player_profiles/atp_top150_profile_register_2026_11_21.csv`.
- Kiinduló kitöltöttség: **134/150 magasság**, **134/150 testsúly**, **104/150 fonáktípus**, **146/150 2026-os TennisDB-szezonrekord**.
- Az új, forrásonként ellenőrizhető javasolt kiegészítések külön overlay CSV-kben vannak. A két metaadat-CSV egyeztetése és elfogadása UTÁN válhatnak a regiszter részévé.

## 1. Fizikai adatok: 16 forrásolt rekord

**Fájl:** [ATP_TOP150_2026_11_22_PHYSICAL_MISSING_CANDIDATES.csv](ATP_TOP150_2026_11_22_PHYSICAL_MISSING_CANDIDATES.csv)

A 16 korábban üres rekordhoz magasság és testsúly érhető el hivatalos Australian Open, Roland-Garros és ATP-versenyoldalakon. A jelölt kiegészítések alapján a **potenciális** lefedettség 150/150, de az eredeti CSV nem módosult.

**Forráskonfliktus:** Ilia Simakinnál a Roland-Garros 84 kg-t közöl, míg a hivatalos sanghaji ATP-versenyoldal 85 kg-t; mindkét forrás megőrzendő. Nem állítjuk, hogy az eltérés adatbázishiba: a mérési időpont vagy változó testsúly is okozhatja. A 84 kg jelölt adat, a használat előtt kiválasztott forrás-dátum alapján megerősítendő. A többi profilhoz is szükséges időpont és névazonosság ellenőrzése a végső átemeléskor.

## 2. Fonáktípus: 46 forrásolt kétkezes jelölt

**Fájl:** [ATP_TOP150_2026_11_22_BACKHAND_MISSING_CANDIDATES.csv](ATP_TOP150_2026_11_22_BACKHAND_MISSING_CANDIDATES.csv)

A korábban üres 46 mezőhöz egyenként konkrét forrás-URL került. A források eltérő bizonyítékerősek: ATP hivatalos játékosoldal/hír, az LTA hivatalos profilja, illetve Tennis Abstract/TennisDB vagy szaklap. A jelölt kitöltöttség ezzel **potenciálisan 150/150**, nem többmeccses ütésminőség-validálás. A fonák kétkezes volta *nem bizonyítja*, hogy az adott játékos fonákja erős/gyenge.

## 3. 2026-os szezonstatisztika: 4 nyitott, eltérő versenykör

**Fájl:** [ATP_TOP150_2026_11_22_SEASON_GAPS_RESEARCH.csv](ATP_TOP150_2026_11_22_SEASON_GAPS_RESEARCH.csv)

A négy hiányzó hely: Otto Virtanen, Clement Chidekh, Max Alcala Gurri és Nikolas Sanchez Izquierdo. Forrásonként eltérhet, hogy ATP Tour főtábla, selejtező, Challenger, ITF vagy Grand Slam szerepel a W/L-ben. A TennisDB 2026-os versenyösszesítések és egyéni oldalak nem mindenhol fedik az eredeti 2026.11.21-i regiszter versenykörét/snapshotját. **Nem írunk be találomra nulla vagy átvett W/L értéket.** A különböző versenyszintek szabályozott összefésülése a következő adatfeldolgozási feladat.

## 4. Továbbra is hiányzik

- 150/150 játékosnál a több mérkőzésen alátámasztott szerva+1, fogadás+1, fonák/tenyeres, lábmunka és mozgásváltozás;
- 150/150 játékosnál a többmérkőzéses validált mentális nyomásprofil – **nem készíthető eredményjelzőből önmagában**;
- a 2026.11.15. utáni H2H és mérkőzés-adatbázis rendszeres, licencszempontból megengedett frissítése;
- az egyéni források ATP player ID / Tennis API player ID összerendelése, korábbi és aktuális szezon elkülönítése és no-lookahead validáció;
- a források felhasználási engedélyének, a feed mezőinek, az időbélyegeknek és a hozzáférésnek az ellenőrzése, még az edzői momentumjelzések építése előtt.

**Nem tartalmaz scrapinget vagy élő API-hívást, sem játékosok belső pszichológiai állapotának feltételezett minősítését.** A forrásoldalak nyilvánosan olvasható, hivatkozható metaadatok; nem másolunk át védett szövegeket.

**Kritikus:** e javasolt overlay adatokat a későbbi jóváhagyott integrációkor kell a tényleges Top150 adatfájlban egyeztetni; ez a research PR önmagában nem tölti ki a főág regiszterét.
