---
title: Příběh IceFlow
description: Jak jeden člověk za sedm měsíců postavil hlubokého online hokejového manažera - skoro celého v rozhovorech s AI.
lead: >-
  IceFlow je projekt jednoho člověka. Kromě některých úprav grafiky ve Photoshopu vzniklo zhruba
  99 % díky komunikaci s umělou inteligencí - většinou na procházkách s kočárkem. Nestálo to tedy
  volný čas, a přesto vznikl hotový produkt. Cílem bylo ukázat, co dnes s určitými znalostmi
  zvládne postavit i jeden člověk.
stats:
  - value: '1'
    label: vývojář
  - value: '7'
    label: měsíců, duben až listopad 2026
  - value: '4'
    label: repozitáře - engine, server, aplikace, editor animací
  - value: '1 700+'
    label: commitů
  - value: '~256 000'
    label: řádků kódu
  - value: '10'
    label: jazyků
timelineTitle: Jak hra rostla
milestones:
  - date: Duben 2026
    phase: idea
    phaseLabel: Nápad
    title: Jen povídání s AI
    text: >-
      Zatím žádný kód. Z procházek s kočárkem se staly dlouhé rozhovory s AI o tom, jaký má být
      mobilní hokejový manažer: živé koučování, hráči, kteří se vyvíjejí celou kariéru, trvalý
      online svět a férová ekonomika.
  - date: 27. dubna 2026
    phase: engine
    phaseLabel: Zápasový engine
    title: První prototyp zápasového enginu
    text: >-
      Prototyp v Pythonu simuluje hokejový zápas třetinu po třetině: střídání, výměny formací,
      hru v pásmech a góly. Stává se z něj laboratoř, ve které se ladí pravidla hry.
  - date: Květen 2026
    phase: engine
    phaseLabel: Zápasový engine
    title: Hloubka simulace
    text: >-
      Pokročilé statistiky, brankáři, vliv stavu skóre a zápasová forma. Engine se přepisuje a
      kalibruje, dokud čísla nezačnou vypadat jako skutečný hokej.
  - date: Začátek června 2026
    phase: engine
    phaseLabel: Zápasový engine
    title: Manažer a ekonomika
    text: >-
      Prototyp dostává manažerský modul: platy, údržbu zázemí, příjmy ze zápasů, únavu a zranění
      a ekonomiku, která musí vydržet mnoho sezón.
  - date: 10. června 2026
    phase: server
    phaseLabel: Server
    title: Vzniká online server
    text: >-
      Skutečný herní server startuje v Kotlinu a Quarkusu s PostgreSQL: generátor klubů, vývoj
      tréninkem a o čtyři dny později celá nasimulovaná ligová sezóna.
  - date: Konec června 2026
    phase: mobile
    phaseLabel: Mobilní aplikace
    title: Mobilní aplikace a přestupový trh
    text: >-
      Flutter aplikace začíná 24. června a už o dva dny později má překlady do dalších jazyků. Na
      serveru přibývá skauting juniorů, přestupový trh, Redis, zázemí klubu a formace s taktikou.
  - date: Červenec 2026
    phase: server
    phaseLabel: Server
    title: Nejnabitější měsíc
    text: >-
      Kolem 600 commitů na serveru a v aplikaci. Play-off, trh v reálném čase přes SSE, sponzoři,
      národnosti, klubová loga a barvy dresů, pohár Elite, aréna, botí kluby a zápasová forma
      z Python prototypu přenesená do serverového enginu.
  - date: Srpen 2026
    phase: animation
    phaseLabel: Animace
    title: Živý zápas a animace
    text: >-
      Objevuje se náhled živého zápasu a hned po něm změny sestavy, taktiky a brankáře během hry.
      24. srpna vzniká samostatný editor animací a jeho gólové oslavy jsou ještě týž den
      v aplikaci.
  - date: Září 2026
    phase: server
    phaseLabel: Server
    title: Aby to online drželo pohromadě
    text: >-
      Jeden společný serverový čas, žádné změny klubu během jeho zápasu, bot runner pro zátěž,
      opravy deadlocků, rychlejší dotazy a farmářská soutěž v aplikaci.
  - date: Říjen 2026
    phase: engine
    phaseLabel: Zápasový engine
    title: Kalibrace, tutoriál a férová monetizace
    text: >-
      Engine se znovu kalibruje proti číslům z NHL a taktiky se řídí podloženou chartou. Přichází
      tutoriál a registrace, potom měna Stars, denní a sezónní úkoly, Rapid liga, obchod za hvězdy
      a 25 celoživotních achievementů.
  - date: Začátek listopadu 2026
    phase: launch
    phaseLabel: Příprava spuštění
    title: Příprava na spuštění
    text: >-
      67 nových animací živého zápasu, mentalita, disciplína a forma hráčů, důležitost zápasu
      podle skutečné tabulky, přihlášení přes Google, srovnání s konkurencí, push notifikace - a
      tenhle web.
closingTitle: Férová už od návrhu
---

IceFlow je záměrně navržený tak, aby **nebyl hard pay-to-win**. Hráče ani soutěžní měny si nejde
přímo koupit a prémiové předměty se dají získat i hraním.

Jde to proto, že se neplatí velký tým. Hra od jednoho člověka nemusí ze svých hráčů ždímat
peníze - stačí, aby byla tak dobrá, že se k ní lidé rádi vracejí.
