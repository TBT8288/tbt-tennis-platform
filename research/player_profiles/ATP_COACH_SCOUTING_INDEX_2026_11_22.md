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
