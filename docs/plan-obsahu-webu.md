# Plán obsahu webu Ice Flow

Stav: 10. 11. 2026, větev `dev`. Hotové části jsou shrnuté v kap. 1, zbývající práce v kap. 2-6.
Zdrojem je stav repozitářů `iceflow-server`, `iceflow_mobile`, `hockey_gm` a
`iceflow_animation_editor` k tomuto datu.

## 0. Pravidla pro veškerý obsah

1. **Jen to, co hráč vidí.** Popisují se obrazovky, hodnoty a rozhodnutí z aplikace. Žádné interní
   výpočty, váhy, prahy, matice vhodnosti ani pořadí modifikátorů.
   - OVR je skrytý výpočet. Web mluví o ratingech, které aplikace ukazuje (ATT, DEF, PHY, GOA, EXP),
     o atributech, formě, energii, únavě a předpokladech.
   - Síla týmu se popisuje pravdivě jako vyšší atributy („každý atribut vyšší o N bodů“), ne jako
     skryté hodnocení.
   - Zápas se popisuje jako princip: hra přechází mezi stavy a každý přechod je kalibrovaná
     pravděpodobnost, kterou posouvá, kdo je na ledě, s jakou taktikou a rizikem, v jakém početním
     stavu. Bez výčtu stavů (pásma, buly, střela) a bez hodnot pravděpodobností.
2. **Pojmy a čísla jen ze hry.** Terminologie z aplikace (`iceflow_mobile` l10n, klíče `rules.*`,
   `club.*`), čísla z kódu serveru - ne z prezentace ani z `docs/*.md`, které bývají zastaralé.
   Nic nevymýšlet: žádné poháry (jsou jen ligy: liga, Elite liga, Rapid liga, farmářská liga),
   sponzora si hráč jen vybírá, jednotně „play-off“ (ne „vyřazovací část“).
3. **Každé tvrzení o realitě má zdroj přímo v textu** nebo v boxu „Zdroje k této části“ pod
   kapitolou. U herních abstrakcí se píše, že ze zdroje je převzatý jen směr, ne čísla. Odkazy se
   před zveřejněním ověřují (jen odpovídající; 403 = blokování robotů, ponechat).
4. **Kalibrace jako výsledky, ne recept.** Cíle, naměřené hodnoty, velikost vzorku, verze enginu a
   datum, ne parametry enginu.
5. **Značka:** viditelně vždy „Ice Flow“ (dvě slova), plný název „Ice Flow: Hockey Manager“ tam, kde
   se člověk s hrou setká poprvé (úvodní stránka, první zmínka na stránce Příběh). Konstanty jsou
   v `src/brand.ts`.
6. **Bez populistických formulací** („férová už od návrhu“ apod.) - věcný, objektivní tón.

## 1. Hotovo

| Část | Stav | Kde |
|---|---|---|
| Kostra webu (Astro, 10 jazyků, přepínač, přesměrování podle jazyka) | hotovo | `src/i18n`, `src/pages` |
| Úvodní stránka | hotovo, 10 jazyků | `src/pages/[lang]/index.astro`, `src/i18n/ui.ts` |
| Příběh projektu (vznik, oblasti hry, časová osa, obchodní model, stav) | hotovo, EN + CS | `src/content/story` |
| Průvodce jako dokumentace (postranní obsah, „Na této stránce“, drobečková navigace, předchozí/další, vyhledávání Pagefind, karty pravidel s ikonami jako v aplikaci) | hotovo | `src/layouts/GuideLayout.astro`, `src/components/guide` |
| Články průvodce: Sezóna a soutěže, Pravidla, Zápas, Hráči, Typy hráčů, Trénink, Junioři, Přestupy a kádr, Klub a finance, Úkoly a Stars, Kalibrace, Zdroje | hotovo, EN + CS | `src/content/guide` |
| Grafy: zkušenosti (EXP 0-200), výhry podle rozdílu atributů, časová osa sezóny s Elite, tabulka vhodnosti taktik | hotovo | `src/components/guide` |
| Kalibrace z nového běhu (engine e60b4955, 10 000 zápasů na bod, 80 000 / 40 000) | hotovo | `calibration.mdx` |
| Pravidla NHL / IIHF s odkazy na konkrétní články IIHF | hotovo (NHL bez čísel článků, viz kap. 4) | `rules.mdx` |
| Kontrola všech čísel na webu proti kódu serveru | hotovo 10. 11. 2026 | - |
| Herní zjednodušení oproti realitě vysvětlená na místě (pětky, taktika jen v plném počtu, junioři místo draftu a cena útěchy jako draftová loterie, farma, nesouměrné počítání zápasů pro play-off, odstupné podle NHL, 44 hráčů) | hotovo 11. 11. 2026 | `match`, `juniors`, `season`, `market` |

## 2. Nutné před vydáním do obchodu

- [ ] **Ochrana soukromí - skutečný obsah.** Přihlášení přes Google (ID token), push tokeny, logy
      HTTP provozu na serveru (tokeny se maskují), push notifikace (začátek zápasu, novinky, úkoly
      dne, konec aukce, Rapid), později reklamy a platby. Při zapojení reklam souhlas podle
      GDPR / UMP. Dnes je jen koncept: `src/content/legal/en/privacy.md`.
- [ ] **Podmínky používání - skutečný obsah.** Účet, přijatelné chování, virtuální položky a nákupy,
      dostupnost služby, odpovědnost. Dnes koncept: `src/content/legal/en/terms.md`.
- [ ] **Smazání účtu.** Google Play vyžaduje veřejnou URL s postupem smazání účtu a dat. Funkce
      smazání účtu zatím **chybí v aplikaci i na serveru** - nejdřív ji doplnit tam, pak stránka na
      webu.
- [ ] **Kontakt a podpora.** Stránka s kontaktem pro hráče a pro žádosti o data.

## 3. Obsah webu

- [x] **Screenshoty z aplikace** (src/assets/screens/<jazyk>/, en + cs; video public/media). Svět pro
      snímky: databáze iceflow_screens, kluby „IceFlow <přezdívka podle loga>“ s ručně vybranými
      barvami, hráči „Name Surname“. Hotovo: živý zápas a video gólu (Zápas, úvodní stránka),
      karta taktiky (Typy hráčů), karta hráče a předpoklady (Hráči), junioři (Junioři), příprava
      s důležitostí zápasu (Zápas), domovská obrazovka (úvodní stránka), nápověda (i) (rozcestník
      průvodce).
      Nepotřebují je: Pravidla, Kalibrace, Zdroje, Sezóna (má časovou osu), Přestupy, Klub, Úkoly.
      Postup: lokální server s rozjetou sezónou (`iceflow.dev.presimulate-to`) → emulátor `Pixel_8` /
      `Pixel_9_Pro_XL` na šířku → `adb shell screencap` do souboru a `adb pull` → oříznutí a WebP do
      `src/assets/screens/<lang>/`. EN a CS; ostatní jazyky použijí EN.
- [ ] **Trénink s barvami vhodnosti** - ve světě pro snímky vycházely všechny šipky zeleně; nafotit,
      až bude formace se smíšenou vhodností.
- [ ] **Překlady do zbylých 8 jazyků** (de, fr, it, sv, fi, no, da, ru): průvodce, Příběh, právní
      stránky. Do té doby se zobrazuje angličtina s upozorněním. Názvy typů hráčů zůstávají anglicky.
- [ ] **Editor animací** - samostatný článek „Jak vznikají záběry zápasu“ (`iceflow_animation_editor`:
      schema v31, fyzika střel, odmítání nemožných konců, bránění).
- [ ] **Technický článek / devlog** - zátěžové testy s 288 botími kluby, kickoff, Redis 1 s, SSE
      (`iceflow-server/docs/benchmarks`, `iceflow_infrastructure_sizing.md`,
      `docs/sse-compression-and-proxies.md`), determinismus a přehrávání zápasů.
- [ ] **Push notifikace** v průvodci - co a kdy aplikace posílá.
- [ ] **FAQ**, **press kit** (logo, screenshoty, krátký popis, plný název), **changelog**.

## 4. K ověření

- [x] **Čísla článků pravidel NHL** - doplněná z NHL Official Rules 2026-27 (84.1, 84.3, 84.4,
      84.5, 15.1, 16.2, 19.1, 26.1, 46.14, 20).
- [ ] **Rapid liga - průběh zápasů.** Nápověda v aplikaci: „všech šest zápasů se odehraje najednou“.
      Komentář v `RapidLeagueService.ENTRY_CUTOFF`: „čtyři zápasy živě jeden po druhém“. Zjistit, co
      platí, a sjednotit web, aplikaci i komentář.
- [ ] **Drobnosti z nápovědy, které nebyly dohledané v kódu:** 2 až 6 picků zdarma za sezónu podle
      amatérského skautingu, postup 8 týmů do play-off ligy, boost pomáhá až od únavy 6.
- [ ] **Elite a trénink:** web podle upřesnění autora říká „klub, který v bloku Elite nehraje,
      dostane týmový trénink navíc“; v kódu nedohledáno, nápověda v aplikaci říká něco jiného (kap. 5).

Rozhodnuto: **pětky** jsou záměr - taktika, riziko a ice time patří celé pětce (`iceflow-server/docs/tactics.md`,
kap. 1); **junioři** jsou kompromis mezi draftem NHL a evropskou juniorkou a výběr je offline, aby nebylo nutné
být u telefonu v daný čas; **odvolání brankáře** jen při prohrávání v posledních pěti minutách, aby ho nešlo
zneužít (schválné inkasování, zesměšňování soupeře) - vysvětleno v článku Zápas. **Délka smlouvy** (nejvýše
5 sezón) je herní rozhodnutí a nevysvětluje se; **volba matchupů** se nevysvětluje (plyne z pětek).
Přestupy bez jednání s volnými hráči jsou budoucí práce - v časové ose Příběhu („Co přijde dál“, z
`iceflow-server/TODO.md`, včetně All-Star (soutěž jako Rapid liga, hraná na principu asociací) a výzkumu taktik mimo 5 na 5 a 4 na 4).

Rozhodnuto: **prodloužení v play-off 3 na 3 po 20 minutách** je záměr kvůli zrychlení hry; je to
uvedené v článku Pravidla.

## 5. Nesoulady k opravě v aplikaci (mimo web)

- [ ] Nápověda k achievementům (`rules.achievements.sport.body`) mluví o „three cups“ - ve hře nejsou
      poháry.
- [x] Název sponzora sjednocený (cs „Účast v zápase“, no a da „Kamptilstedeværelse“, ru „Присутствие
      на матчах“) - upraveno v `iceflow_mobile`, necommitnuto.
- [x] Nápověda k Elite (`rules.elite.schedule.body`) přepsaná ve všech 10 jazycích: Elite je součást
      kalendáře s vlastními bloky, kdo nehraje, dostane týmový trénink navíc - upraveno
      v `iceflow_mobile`, necommitnuto.
- [ ] Nepoužívaný klíč `juniors.visibleOvr` („OVR range“) - smazat, pokud se nikde nezobrazuje.
- [ ] `docs/challenges-store.md` v serveru uvádí zastaralé odměny (8 denně, 100 za sezónu); podle
      `ChallengeTaskCatalog.kt` je to 10 denně a 130 za sezónní úkoly.

## 6. Značka a nasazení

- [ ] **Logo** s dominantním ICE FLOW a malým podtitulem HOCKEY MANAGER (grafika autora).
- [ ] **Řádek © v patičce** - rozhodnout držitele (jméno autora, nebo vývojářská značka, např.
      CimulApps); dnes „© 2026 Ice Flow“.
- [ ] **Ochranná známka** ICE FLOW - až u veřejné bety; předtím dokončit rešerši dvou evropských
      známek ICEFLOWER.
- [ ] **Doména na Cloudflare** a nasazení (Cloudflare Pages). Potom nastavit `site`
      v `astro.config.ts`, mapu webu, `hreflang` odkazy mezi jazyky, `robots.txt` a náhledový
      obrázek pro sdílení (Open Graph).
