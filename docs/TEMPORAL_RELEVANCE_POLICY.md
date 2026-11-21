# ATP Intelligence – időbeli relevancia és H2H (2026-11-21)

**Kötelező termékszabály:** az ATP Top 150 játékosainak **aktuális meccsre vonatkozó prediktív teljesítményadatai** mindig az adott évből és az azt megelőző évből származhatnak. 2026. november 21-én tehát **2026 + 2025**, 2027. január 1-jétől **2027 + 2026**. Az időablak automatikusan az `as_of` előrejelzés dátumával vált, és soha nem tartalmazhat még meg nem történt vagy ugyanazon a napon nem igazoltan lezárult eredményt.

## A különböző adatok eltérő kezelése

| Adat | 2026/2025 prediktív felhasználás | 2024 és régebbi |
|---|---|---|
| Aktuális ATP/GS meccseredmények, serve/return, W/L, forma, borítás | Fő bemenet, dátum és ellenfélerő szerint súlyozva | Archív; közvetlen friss forma-feature-be nem kerül |
| H2H | **Kiegészítő**, kis mintaszám miatt erős óvatossággal, friss mérkőzések súlya nagyobb | **0 közvetlen H2H prediktív súly**; csak történeti taktikai jelzés |
| Játékos stílusa, erősségek, gyengeségek, edzői elemzések | Frissen ellenőrzött megfigyelések a 2026/25-ös meccsekről | Kutatási hipotézis/fejlődési előzmény; friss meccs nem igazolja automatikusan |
| Karrier- vagy minden korábbi meccsből képzett Elo | Csak **külön jelölt historikus előzetes/baseline** lehet, nem „2026-os forma” | Nem vethető össze önmagában 2-szezonos, tiszta teljesítményként |
| Születési dátum, magasság, kezesség | Forrásolt életrajzi állomány, nem függ az év szabályától | Megőrzendő, ha a tény nem változik; testsúly/edző/friss sérülés külön újraellenőrizendő |

**Az évhatáros szűrés a felhasználó által választott konzervatív V1 szabály, NEM kutatással bizonyított matematikai optimum.** Idősúlyok és ablakok összehasonlítandók időrendben korrekt out-of-sample tesztben: friss 90 nap, 365 nap, aktuális+előző naptári év, 24 hónap; mérőszámok: log-loss, Brier-score, kalibráció, külön borítás és meccsminta. Régebbi meccsek historikus tárolása megengedett, de a friss prediktív adatnézetből szűrve.

## Kezdő súlyozási szabály (hiperparaméter, nem bizonyított optimum)

A `atp_intelligence/time_relevance.py` modul a két naptári éven belül csak az **`as_of` dátum előtti** mérkőzésekből számol súlyt, a korábbi évekre pontosan nullát ad. A félidők jelenlegi kísérleti induló beállításai:
- általános teljesítmény: **270 nap**
- H2H: **180 nap**
- rövid távú forma: **45 nap**

Idősúly = `0.5 ** (napok_száma / félidő)`. Az egyenlet nem a győzelem esélye; a súly egy mérkőzés adatrészletének jelenidejű relevanciáját jelzi. A túl kevés H2H előfordulásnál a win-rate 50% felé simít (3 meccsnyi előzetes kiegyensúlyozó súly). A hiányzó vagy csak régi H2H **nem hátrány**: jelzése `no_recent_h2h`, nem negatív mentális minősítés. Az eddig beírt félidő-számok tesztelendők és optimalizálandók, nincs validált prediktív teljesítményük.

## Példa

Ha 2026 novemberében egy játékos 2022–2024-ben 3–0-ra vezetett, de 2025–2026-ban nem találkozott az ellenfelével, a **prediktív H2H-mutató semleges 0.5** és az effektív kétidényes meccsszám **0**. Az eredeti 3–0 történeti archív tényként megmarad; de sem az esélybecslést, sem a pszichológiai diagnózist nem torzíthatja közvetlenül.

## Források (elméleti háttér, nem a konkrét félidő-számok bizonyítása)

- [Time-varying player skills and surface-specific dynamic prediction (2019)](https://doi.org/10.1111/rssa.12464)
- [Weighted Elo rating for tennis match predictions (2022)](https://doi.org/10.1016/j.ejor.2021.04.011) — a friss forma és legutóbbi meccs hatása
- [Boosting markovian tennis prediction (2026)](https://doi.org/10.1177/22150218251412670) — a H2H külön modell-inputja és az adatmennyiség vs. relevancia vitája
- [Tennis forecasting calibration and in-play modelling](https://www.sciencedirect.com/science/article/pii/S0169207017301395)

## Megvalósítottság

- **Kész:** `atp_intelligence/time_relevance.py` relevanciaszűrő és H2H simítás; `tests/test_time_relevance.py` idő- és információszivárgás-gátló tesztek.
- **Még nincs kész:** az app alapfolyamatába integrált, kétidényes match dataset, 2025-ös teljes meccstörténet, optimalizált/kalibrált súlyok és valós live eredménymodell. A 2026-11-20 Pythia all-history Elo és a 2026 TennisDB season stat **eltérő adatidő-ablakú**, ezeket nem szabad egyformán friss formának nevezni.
