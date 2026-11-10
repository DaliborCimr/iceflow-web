# Plán obsahu webu IceFlow

Stav: 10. 11. 2026. Plán pro sekce „Jak hra funguje“, „Kalibrace“ a doplňky. Zdrojem je stav
repozitářů `iceflow-server`, `iceflow_mobile`, `hockey_gm` a `iceflow_animation_editor` k tomuto
datu.

## 0. Pravidla pro veškerý obsah

1. **Jen to, co hráč vidí.** Popisují se obrazovky, hodnoty a rozhodnutí z aplikace. Žádné interní
   výpočty, váhy, prahy, matice vhodnosti ani pořadí modifikátorů.
   - OVR je skrytý výpočet. Web mluví jen o ratingech, které aplikace ukazuje (ATT, DEF, PHY,
     GOA, EXP), o atributech, formě, energii, únavě a předpokladech.
   - Zápas se popisuje jako **princip**: hra přechází mezi stavy a každý přechod je kalibrovaná
     pravděpodobnost. Tu posouvá to, kdo je zrovna na ledě (atributy, energie, forma), s jakou
     taktikou a rizikem a v jakém početním stavu. Bez výčtu konkrétních stavů (pásma, buly,
     střela) a bez konkrétních hodnot pravděpodobností nebo velikosti posunů.
2. **Každé tvrzení o realitě má zdroj.** Reálné hodnoty (NHL průměry, výzkum osobnosti, zranění,
   taktické systémy) se citují. U herních abstrakcí se píše, že ze zdroje je převzatý jen směr,
   ne čísla (jak to dělá specifikace formy).
3. **Kalibrace jako výsledky, ne recept.** Zveřejňují se cíle, naměřené hodnoty, velikost vzorku
   a interval spolehlivosti, ne parametry enginu.
4. **Čísla odpovídají současné verzi.** Každá stránka má datum a verzi enginu (hash z reportu).
   Čísla se berou z aktuálního reportu, ne z paměti.

## 1. Oprava stávající stránky Příběh

Stránka zatím mluví o „celkovém hodnocení“ a „křivce OVR“, což je v rozporu s pravidlem 0.1.

- [ ] Přepsat kartu „Hráč jako dlouhodobý systém“: junioři mají **rozsah ratingů a TRT**, ne OVR.
- [ ] Přepsat kartu „Kalibrace simulace“: místo „křivka hodnocení“ → „rozdíl síly týmů“.
- [ ] Ověřit čísla z prezentace proti aktuálnímu reportu (viz kap. 3), u každého uvést datum.

## 2. Sekce „Jak hra funguje“ (průvodce)

Zdroj textu: 336 klíčů `rules.*` v `iceflow_mobile/lib/src/l10n/iceflow_l10n_en.dart` (a `_cs`),
zkontrolovaných proti serveru auditem `iceflow_mobile/docs/rules-help-audit-2026-10-23.md`. Pop-upy
jsou krátké; web je rozvede do souvislého textu, přidá příklady a screenshot.

Navržené články (`src/content/guide/<lang>/<slug>.md`) podle sekcí aplikace:

| # | Článek | Zdrojové klíče `rules.*` | Doplňkový podklad |
|---|---|---|---|
| 1 | Sezóna a kalendář (21 dní, 63 bloků) | `league`, `schedule`, `section` | prezentace, sl. 9 |
| 2 | Soutěže: liga, play-off, Elite, farma, Rapid | `league`, `playoff`, `elite`, `group`, `table`, `farm`, `challenges` | audit pravidel (postup do Elite) |
| 3 | Živý zápas a koučování | `live`, `match`, `lines`, `tactics`, `report` | `docs/league-live-match.md`, `docs/manpower-plan.md` |
| 4 | Formace, ice time a početní stavy | `lines`, `team` | `docs/manpower-plan.md` |
| 5 | Taktiky a riziko | `tactics` | `docs/tactics.md` (popisy systémů + zdroje, bez matice) |
| 6 | Příprava na zápas a skauting soupeře | `report`, klíče `preMatch`/`scout` | `docs/match-scouting.md` |
| 7 | Hráč: atributy, ratingy, typy hráčů | `players`, `player` | archetypy podle Identity Shift Hockey |
| 8 | Energie, únava, zranění | `player.energy/fatigue/injury` | specifikace formy (odolnost) |
| 9 | Forma, zkušenosti, předpoklady, mentalita, disciplína | `form`, `predispositions` | `IceFlow_specifikace_formy_a_predpokladu_2026-11-02.md`, zadání Mentalita |
| 10 | Důležitost zápasu | — | `docs/IceFlow_zadani_..._mentalita_a_vyznam_zapasu.md` (jen princip) |
| 11 | Trénink týmový a individuální, boost | `training`, `teamTraining`, `individualTraining` | |
| 12 | Junioři a skauting | `juniors` | audit (pevný rozsah 18letých) |
| 13 | Smlouvy, platy, konec kariéry | `contract` | audit (prodlužování, termín 15. dne) |
| 14 | Přestupový trh a aukce | `transfers`, `bid`, `sell` | audit (rychlý prodej 70 % × 75 %) |
| 15 | Finance, Flow a Gold Pucks, sponzoři | `finance`, `sponsor`, `gpSponsor` | `docs/challenges-store.md` |
| 16 | Zázemí klubu | `facilities`, `club` | |
| 17 | Úkoly, achievementy, Stars a obchod | `challenges`, `achievements` | `docs/challenges-store.md`, prezentace, sl. 10-11 |
| 18 | Historie a novinky | `history`, `news`, `overview` | |

Postup pro každý článek: vytáhnout EN+CS klíče → ověřit proti auditu a kódu → napsat text →
screenshot → kontrola, že článek neprozrazuje nic z pravidla 0.1.

### Screenshoty

- Aplikace má jen Android/iOS. K dispozici je Flutter a emulátory `Pixel_8` a `Pixel_9_Pro_XL`.
- Postup: lokální server s dev seedem (`iceflow.dev.presimulate-to`, rozjetá sezóna se zápasy,
  trhem a juniory) → aplikace na emulátoru na šířku → `adb exec-out screencap -p` → oříznutí a
  WebP do `src/assets/screens/<lang>/`.
- Pořídit EN a CS; ostatní jazyky použijí EN screenshot.
- Kluby na screenech nesmí pocházet z generátoru. Pro focení připravit vlastní sadu s pevnými
  názvy (IceFlow Tigers, IceFlow Wolves ...), aby screeny nevypadaly jako skutečné kluby nebo
  hráči. Vyžaduje úpravu dev seedu nebo přejmenování klubů v dev databázi před focením.

## 3. Sekce „Kalibrace“ (samostatná stránka)

Zdroj: `iceflow-server/experiment-results/match-calibration/report-latest.md` a
`src/test/kotlin/.../MatchCalibrationGuardrailTest.kt`. Nejnovější report v repozitáři je
z 2. 10. 2026 (engine `d78a6762`, 10 000 zápasů na bod). Od té doby proběhly rekalibrace (taktiky
27. 10., OVR křivka a riziko 28. 10., stamina 19. 10.), proto **report vygenerovat znovu** na
aktuálním enginu a teprve ten publikovat.

Co zveřejnit (herní výstupy):

| Oblast | Metriky | Reálná reference |
|---|---|---|
| Zápas | góly, pokusy o střelu, střely na branku, úspěšnost zákroků na tým a zápas, po třetinách | NHL 2024/25 průměry ligy |
| Výsledky | výhry vyrovnaných týmů, remízy po 60 min, prodloužení, nájezdy | NHL 2024/25 |
| Početní stavy | přesilovky na zápas, úspěšnost přesilovek, góly v oslabení, 3 na 3 v prodloužení | NHL 2024/25 |
| Vyloučení a bitky | menší tresty na zápas, souběžné 2+2, bitky | NHL 2024/25 (už v komentářích testu) |
| Asistence | podíl gólů s 0/1/2 asistencemi při 5 na 5, v přesilovce, v oslabení | NHL 2024/25 |
| Ice time | minuty na hráče podle formace | NHL průměry TOI |
| Síla týmů | % výher a úspěšnost zákroků podle rozdílu síly týmů (bez slova OVR, osa „rozdíl síly“) | — (herní cíl) |
| Nezávislost na úrovni | stejné statistiky při slabší a silnější lize | — (herní cíl) |
| Domácí prostředí | výhra domácích | NHL home win % (`analyze-home-advantage.py`, `experiment-results/home-zone-*`) |
| Dlouhodobý vývoj | vývoj hráčů a ekonomiky přes 15 sezón (stabilita, bez driftu) | — |

Co nezveřejnit: hierarchii vlivů (atributy > taktiky > riziko > archetyp), efekty jednotlivých
taktik a archetypů, matice, sweep parametrů, váhy.

Formát: tabulka cíl / naměřeno / reference se zdrojem, velikost vzorku, 95% CI, verze enginu a
datum. Graf „výhry podle rozdílu síly“ (data jsou v reportu).

**Co chybí:** reálné reference jsou zatím jen v komentářích kódu (např. „NHL 2024/25: 7 895
menších trestů hráčů a 267 trestů lavičky v 1 305 zápasech“). Je potřeba je dohledat a citovat
(NHL.com Stats, Hockey-Reference) s přesnou sezónou a datem stažení.

## 3b. Pravidla hry (samostatný článek průvodce)

Hra kombinuje pravidla NHL a IIHF. Článek má u každého pravidla říct, podle koho je, a odkázat
na konkrétní článek pravidel (NHL Official Rules 2025-26, IIHF Official Rule Book 2023-2026).
Stav podle kódu serveru (`match/service/MatchSimulationConfig.kt`, `MatchSimulator.kt`,
`MatchEngineMath.kt`, `season/simulation/LeagueStandings.kt`):

| Pravidlo | Ve hře | Podle | V kódu |
|---|---|---|---|
| Hrací doba | 3 × 20 min | obojí | `PERIOD_SECONDS = 1200` |
| Body v tabulce | výhra 3, výhra po prodl./nájezdech 2, prohra po prodl./nájezdech 1 | IIHF (NHL dává 2-2-1) | `LeagueStandings.applyResult` |
| Prodloužení v základní části | 5 min, 3 na 3, náhlá smrt | NHL (3 na 3) | `overtimeSkaters = 3`, `300 s` |
| Vyloučení v prodloužení | 3 na 3 → 4 na 3 → 5 na 3 | NHL pravidlo 84.3 | `MatchEngineMath.kt:181` |
| Nájezdy | 5 sérií, pak náhlá smrt | IIHF (NHL má 3) | `shootoutRegulationRounds = 5` |
| Prodloužení ve vyřazovací části | 20min třetiny do gólu, bez nájezdů | NHL play-off | `PLAYOFF_OVERTIME_PERIOD_SECONDS = 1200` |
| Souběžné menší tresty při plném počtu | hraje se 4 na 4 | NHL (IIHF zůstává 5 na 5) | `coincidentalMinorsPlayFourOnFour = true` |
| Odložené vyloučení | hra pokračuje do dotyku, šestý hráč místo brankáře | obojí | `delayedPenalties = true`, NHL 15.4 |
| Nejméně 3 hráči v poli | další trest čeká | NHL 16.3 | `MatchEngineMath.kt:154` |
| Konec trestu po gólu | jen u gólu v přesilovce | NHL | `MatchSimulator.kt:1175` |
| Druh trestů | menší, souběžné, 5 min za bitku, 5 min + do konce zápasu | obojí | `PenaltyKind` |
| Kontumace | 5:0 | IIHF | `MatchSimulationService.kt:981` |
| Čisté konto | jen brankář, který odchytal celý zápas sám | NHL | `MatchSimulationService.kt:985` |
| Pořadí při rovnosti bodů | rozdíl skóre, pak vzájemné zápasy | ověřit proti NHL i IIHF | `LeagueStandings.rank` |

Úkoly:

- [ ] Ověřit každý řádek proti aktuálnímu textu pravidel a doplnit číslo článku (NHL i IIHF).
- [ ] Ověřit, které herní situace engine jako pravidla vůbec nemodeluje (např. zakázané uvolnění,
      postavení mimo hru) a v článku to napsat otevřeně: jsou součástí abstrakce, ne samostatné
      pravidlo.
- [ ] Doplnit formáty soutěží: play-off ligy (čtvrtfinále na dvě výhry, dál jeden zápas), Elite a
      farma (všechna kola na jeden zápas), Rapid (každý s každým, pořadí podle rozdílu skóre a
      vstřelených gólů).

## 4. Rešerše a zdroje

Výzkum je v repozitářích, ale roztroušený. Vytvořit stránku **Zdroje** (a odkazy z článků):

- **Taktiky:** registr 13 zdrojů v `docs/tactics-audit-2026-10-27.md` (NHL.com, USA Hockey
  handbook, Barry Smith / left wing lock, Sound of Hockey o systému Hakstola, icehockeysystems.com
  ...). Na web jen popis systémů a citace, ne vhodnost archetypů.
- **Typy hráčů:** Identity Shift Hockey, 14 archetypů (mapování 10 herních typů je v
  `docs/tactics.md`, kap. 4).
- **Předpoklady, forma, zranění:** `IceFlow_specifikace_formy_a_predpokladu_2026-11-02.md`, kap.
  10: Roberts & DelVecchio (2000), meta-analýza 2014, Gupta & McCarthy (2022), Safe2Play (2024),
  Grossman et al. (2022), meta-analýza motivace 2026, výzkum brankářských sérií („hot goalie“
  bez podpory; chybí přesná citace).
- **Kalibrace zápasu:** NHL 2024/25 (dohledat, viz kap. 3).
- **Úkol:** každý zdroj ověřit (odkaz funguje, rok, autor), sjednotit citační formát, uvést, co se
  ze zdroje převzalo (směr vs. číslo).

## 5. Co je v repozitářích a hodí se na web

Témata, která zatím nejsou v plánu ani na stránce Příběh:

1. **Botí kluby.** Ligy doplňují boti, kteří hrají, nakupují a prodávají podle stejných pravidel.
   Hráč by to měl vědět (transparentnost); Rapid liga to už zmiňuje.
2. **Párování lig podle síly.** Jen co do zařazení vstupuje (síla týmu, úroveň ligy, volná místa,
   boti jako doplnění), bez vzorců a bez konkrétních rozsahů.
3. **Zátěžové testy a technika.** `docs/benchmarks/` (288 botích klubů, kickoff, Redis 1 s, SSE),
   `iceflow_infrastructure_sizing.md`, `docs/sse-compression-and-proxies.md`. Vhodné jako technický
   článek nebo devlog.
4. **Determinismus a přehrávání zápasů.** Stejný zápas za stejných podmínek dává stejný výsledek
   (snapshoty, `experiment-results/match-replays/`). Argument férovosti simulace.
5. **Editor animací.** `iceflow_animation_editor` (schema v31, fyzika střel, odmítání nemožných
   konců, validace bránění). Samostatný článek „Jak vznikají highlighty“.
6. **Kontrola nápovědy proti kódu.** Jedna věta do sekce o kvalitě na stránce Příběh: texty
   v aplikaci se pravidelně porovnávají s tím, co server skutečně dělá
   (`rules-help-audit-2026-10-23.md` našel a opravil 14 nesouladů ve všech 10 jazycích).
7. **Push notifikace.** Co a kdy aplikace posílá (začátek zápasu, novinky, úkoly dne, konec aukce,
   Rapid). Patří do nápovědy i do Ochrany soukromí.

Povinné nebo skoro povinné stránky, které chybí:

8. **Smazání účtu.** Google Play vyžaduje veřejnou URL s postupem smazání účtu a dat. V aplikaci
    ani na serveru jsem funkci smazání účtu nenašel.
9. **Ochrana soukromí - skutečný obsah.** Přihlášení přes Google (ID token), push tokeny, logy
    HTTP provozu (tokeny se maskují), reklamy (zatím testovací dialog, SDK ještě není), platby.
    Při zapojení reklam bude potřeba souhlas (GDPR/UMP).
10. **Kontakt a podpora**, **FAQ**, **press kit** (logo, screenshoty, krátký popis), **changelog**.

## 6. Nesoulady k opravě v aplikaci (mimo web)

- `rules.challenges.rapidOpponents.body` zmiňuje OVR („at most 6 apart“), přestože OVR v aplikaci
  není vidět.
- Klíč `juniors.visibleOvr` („OVR range“) - ověřit, zda se ještě zobrazuje.

## 7. Pořadí prací

1. Kap. 1 - oprava stránky Příběh (malá, hned).
2. Kap. 4 - stránka Zdroje z toho, co už je v repozitářích, + dohledání NHL referencí.
   Kap. 3b - článek Pravidla (ověření proti pravidlům NHL a IIHF).
3. Kap. 3 - nový kalibrační běh na aktuálním enginu a stránka Kalibrace.
4. Kap. 2 - články průvodce po skupinách (zápas a taktika → hráč → klub → soutěže → ekonomika),
   screenshoty průběžně.
5. Kap. 5 - smazání účtu a Ochrana soukromí dřív, než aplikace půjde do obchodu; ostatní průběžně.
6. Překlady do zbylých 8 jazyků až po ustálení EN a CS.
