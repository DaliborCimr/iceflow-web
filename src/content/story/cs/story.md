---
title: Příběh Ice Flow
description: Jak jeden vývojář ve spolupráci s AI navrhl a postavil online hokejového manažera pro mobil mezi dubnem a listopadem 2026.
lead: >-
  Ice Flow: Hockey Manager je online manažerská hra o ledním hokeji pro mobilní telefony, kterou vyvíjí jeden
  člověk. Kromě části grafiky, která byla dokončena ve Photoshopu, vzniklo zhruba 99 % práce -
  herní design, server, mobilní aplikace, nástroje i texty - v komunikaci s umělou inteligencí,
  z velké části během procházek s kočárkem. Projekt je praktickou zkouškou toho, kam až může jeden
  člověk s potřebnými znalostmi dotáhnout složitý produkt s dnešní AI.
stats:
  - value: '1'
    label: vývojář
  - value: '7'
    label: měsíců vývoje, duben - listopad 2026
  - value: '4'
    label: kódové báze - prototyp enginu, server, mobilní aplikace, editor animací
  - value: '1 700+'
    label: commitů
  - value: '~256 000'
    label: řádků kódu
  - value: '10'
    label: jazyků od začátku
storyTitle: Jak hra vznikala
areasTitle: Co hra obsahuje
areasIntro: >-
  Přehled hlavních systémů ke stavu v listopadu 2026. Čísla odpovídají současnému nastavení hry a
  při balancování se mohou měnit.
areas:
  - title: Živé koučování
    text: >-
      Zápasy se simulují na serveru a do aplikace se přenášejí průběžně. Trenér může zasáhnout
      kdykoli, nejen mezi třetinami.
    facts:
      - Čtyři kompletní formace, základní a náhradní brankář, dvě přesilovkové a dvě oslabené formace
      - 6 útočných a 6 obranných taktik a 5 úrovní rizika, nastavitelné pro každou formaci
      - Energie během střídání klesá a na střídačce se obnovuje; nahromaděná únava omezuje startovní energii
      - Střídání, míchání formací, odvolání brankáře a speciální formace lze měnit během hry
      - Odložené vyloučení, prodloužení 3 na 3 a prázdná branka jsou skutečné herní stavy
      - Stav zápasu posílá server každou sekundu přes SSE
  - title: Prezentace zápasu
    text: >-
      Góly a vybrané šance se zobrazují jako animované záběry odvozené ze skutečných událostí
      zápasu. Nejde o fyzikální záznam, ale zachovávají herní kontext.
    facts:
      - Všechny góly a další šance rovnoměrně rozložené v průběhu zápasu
      - Varianta animace podle početní situace (5 na 5, 6 na 5 s prázdnou brankou, přesilovka 5 na 3 a další)
      - Varianty pro góly bez asistence, s jednou nebo dvěma asistencemi
      - Záběry vznikají ve vlastním editoru animací vytvořeném pro tento projekt
  - title: Hráč jako dlouhodobý systém
    text: >-
      Hodnotu hráče neurčuje jediné číslo. Ratingy, zkušenosti, forma a předpoklady se během
      kariéry vyvíjejí různým tempem, takže dva hráči se stejnými ratingy se mohou výrazně lišit.
    facts:
      - Junioři se skautují v 17 letech; ratingy a předpoklady (TRT) se zobrazují jako rozsah, který skautské reporty zpřesňují
      - Vývoj od 18 let přes týmový a individuální trénink, na farmě s menšími přírůstky
      - Zkušenosti stabilizují výkon a hospodaření s energií; forma odráží zhruba posledních 10-20 zápasů
      - Mentalita roste s vystavením důležitým zápasům; disciplína ovlivňuje vyloučení a bitky
      - Odolnost proti zraněním klesá s věkem a po vážných zraněních
      - Veteráni hrají stabilněji, ale ztrácejí rychlost a kondici, až ukončí kariéru
  - title: Řízení klubu
    text: >-
      Trénink, farma, smlouvy, přestupový trh, zázemí a finance jsou propojené, takže rozhodnutí
      v jedné oblasti má důsledky v ostatních.
    facts:
      - Farma hraje vlastní soutěž souběžně s prvním týmem
      - Smlouvy až na 5 sezón; plat podle ratingů, věku a očekávaného vývoje, k tomu podpisový bonus
      - Přestupový trh s vyvolávací cenou 80-110 %, 8minutovou aukcí po prvním příhozu a 90sekundovým prodloužením
      - Dvě měny - Flow na provoz klubu, Gold Pucks na trh, skauting a juniory
      - Jeden sponzor na peníze a jeden na gold pucky za sezónu, každý vybraný ze tří druhů nabídek
      - Aréna a zázemí pro trenéry, zdravotníky, skauting, vedení a rozvoj hráčů, se stavem a opravami
  - title: Sezóna a soutěže
    text: >-
      Sezóna trvá 21 skutečných dní. Kalendář je krátký, ale každý blok dne přináší rozhodnutí.
    facts:
      - 63 bloků za sezónu - 21 dní, každý rozdělený na tři části
      - Ligy po 12 týmech, každý s každým čtyřikrát - 44 ligových zápasů
      - Play-off - čtvrtfinále na dvě vítězství, semifinále a finále na jeden zápas
      - Elite liga - 24 týmů, 6 kol švýcarským systémem, nejlepších 16 do vyřazovací části, ve stejném kalendáři jako liga
      - Rapid liga - 4 týmy, každý s každým, odehraje se okamžitě, bez únavy, zranění a vlivu na ligové statistiky
      - Důležitost zápasu vychází ze skutečné situace v tabulce a pro každý tým může být jiná
  - title: Kalibrace simulace
    text: >-
      Zápasový engine je kalibrovaný na dlouhodobé průměry skutečného hokeje a ověřovaný dlouhými
      simulacemi.
    facts:
      - Cíle na tým a zápas - zhruba 29 střel na branku, 3,1 gólu, úspěšnost zákroků 89,7 %, 2,8 přesilovky
      - Samostatné kontroly rozdílu síly týmů, vlivu brankáře, rizika, diváků, formy a únavy
      - Patnáctisezónní simulace hlídají, aby vývoj, mentalita a disciplína neujížděly
      - Stejný zápas se z uložených snapshotů přehraje za stejných podmínek
timelineTitle: Časová osa
milestones:
  - date: Duben 2026
    phase: idea
    phaseLabel: Koncept
    title: Koncept v rozhovorech
    text: >-
      Návrh začíná bez kódu: co má mobilní hokejový manažer nabízet, jak má fungovat živé koučování
      a dlouhodobý vývoj hráčů a jak udržet ekonomiku v rovnováze.
  - date: 27. dubna 2026
    phase: engine
    phaseLabel: Prototyp enginu
    title: První prototyp zápasového enginu
    text: >-
      Prototyp v Pythonu simuluje zápasy po třetinách - střídání, výměny formací, hru v pásmech a
      góly. Slouží jako prostředí pro ladění herních pravidel.
  - date: Květen 2026
    phase: engine
    phaseLabel: Prototyp enginu
    title: Hloubka simulace
    text: >-
      Pokročilé statistiky, model brankáře, vliv stavu skóre a zápasová forma. Engine se přepisuje
      a kalibruje proti skutečným číslům.
  - date: Začátek června 2026
    phase: engine
    phaseLabel: Prototyp enginu
    title: Model řízení klubu a ekonomiky
    text: >-
      Prototyp získává manažerský modul - platy, údržbu zázemí, příjmy ze zápasů, únavu a zranění -
      a ekonomiku testovanou přes mnoho sezón.
  - date: 10. června 2026
    phase: server
    phaseLabel: Server
    title: Herní server
    text: >-
      Začíná vývoj produkčního serveru v Kotlinu a Quarkusu s PostgreSQL - generátor klubů, vývoj
      tréninkem a během čtyř dnů celá nasimulovaná ligová sezóna.
  - date: Konec června 2026
    phase: mobile
    phaseLabel: Mobilní aplikace
    title: Mobilní aplikace a přestupový trh
    text: >-
      Aplikace ve Flutteru vzniká 24. června a o dva dny později je lokalizovaná. Na serveru
      přibývá skauting juniorů, přestupový trh, Redis, zázemí klubu a formace s taktikou.
  - date: Červenec 2026
    phase: server
    phaseLabel: Server
    title: Základní systémy
    text: >-
      Nejintenzivnější měsíc s přibližně 600 commity na serveru a v aplikaci - play-off, trh
      v reálném čase přes SSE, sponzoři, národnosti, klubová loga a barvy dresů, Elite liga, aréna,
      botí kluby a zápasová forma z prototypu přenesená do serverového enginu.
  - date: Srpen 2026
    phase: animation
    phaseLabel: Animace
    title: Živý zápas a editor animací
    text: >-
      Režim živého zápasu se změnami sestavy, taktiky a brankáře během hry. 24. srpna vzniká
      samostatný editor animací a jeho gólové animace jsou ještě týž den v aplikaci.
  - date: Září 2026
    phase: server
    phaseLabel: Server
    title: Stabilita online provozu
    text: >-
      Jeden autoritativní serverový čas, zamykání klubu během jeho zápasu, zátěžové testy s bot
      runnerem, opravy deadlocků, optimalizace dotazů a farmářská soutěž v aplikaci.
  - date: Říjen 2026
    phase: engine
    phaseLabel: Engine a ekonomika
    title: Kalibrace, onboarding a monetizace
    text: >-
      Nová kalibrace enginu podle dat z NHL a zdokumentovaný model taktik. Registrace a provázený
      tutoriál, potom měna Stars, denní a sezónní úkoly, Rapid liga, obchod a 25 celoživotních
      achievementů.
  - date: Začátek listopadu 2026
    phase: launch
    phaseLabel: Příprava spuštění
    title: Příprava na spuštění
    text: >-
      67 nových animací živého zápasu, mentalita, disciplína a forma, důležitost zápasu podle
      tabulky, přihlášení přes Google, srovnání s konkurencí na trhu, push notifikace a tento web.
notes:
  - title: Obchodní model
    paragraphs:
      - >-
        Hráče, Flow ani Gold Pucks nelze koupit za peníze. Prémiová měna Stars se získává hraním -
        za denní úkoly (8 denně, 168 za sezónu), sezónní úkoly (100 za sezónu), celoživotní
        achievementy (25 oblastí po 5 úrovních) a vstupy do Rapid ligy (1-5 hvězd, jedna reklama za
        vstup, nejvýše 10 denně).
      - >-
        Za Stars nebo skutečné peníze lze získat kosmetické položky, například nový název, klubové
        barvy nebo logo, a dva passy platné 21 dní. Ads Pass odstraní reklamy, ale denní limity
        nemění. Sponsor Pass zvyšuje příjmy od sponzorů ve Flow i Gold Pucks o 20 %, což je skutečná
        ekonomická výhoda; obnovitelný příjem hvězd sám nestačí na to, aby byl aktivní každou
        sezónu. Ice Flow tedy není pay-to-win ve smyslu nákupu hráčů nebo síly, placení ale přináší
        mírnou dlouhodobou ekonomickou výhodu.
      - >-
        Protože hru vyvíjí jeden člověk, jsou náklady na provoz nízké a hra nepotřebuje agresivní
        monetizaci, aby se udržela.
  - title: Současný stav
    paragraphs:
      - >-
        Technický základ je připravený na uzavřené nebo postupné spuštění - přihlášení přes Google,
        zátěžové testy s 288 botími kluby, živý zápas řízený serverem a deterministické přehrávání
        zápasů. Chybí zatím data ze skutečného provozu - opětovná připojení, hlášení pádů, retence
        a chování ekonomiky se skutečnými hráči. Další fází proto není přidávání funkcí, ale
        postupné spuštění, sběr telemetrie a balancování.
---

Nápad na Ice Flow vznikl v dubnu 2026, ještě než byl napsán první řádek kódu. První týdny
probíhaly v rozhovorech s AI, ve kterých se definovalo, čím má hra být: mobilní hokejový manažer,
ve kterém rozhodování pokračuje i během zápasu, hráči se vyvíjejí celou kariéru a online svět
běží dál i mezi hraním. Většina těchto rozhovorů probíhala na procházkách s kočárkem - v čase,
který by jinak na vývoj využít nešel.

Role byly od začátku jasně rozdělené. Autor vystupoval jako produktový vlastník a architekt:
rozhodoval o herním designu, prioritách a kompromisech a kontroloval výsledky. AI psala
implementaci, testy, kalibrační experimenty i dokumentaci. Typická iterace byla písemná
specifikace, implementace, automatické testy a vyhodnocení výsledků proti zamýšlenému chování.

### Od prototypu k online hře

Prvním funkčním kódem byl na konci dubna prototyp zápasového enginu v Pythonu. Sloužil jako
laboratoř: střídání, výměny formací, hra v pásmech, brankáři, forma i ekonomika se v něm
modelovaly a kalibrovaly dřív, než se cokoli dostalo do skutečné hry. V červnu začal vývoj
produkčního serveru v Kotlinu s Quarkusem, PostgreSQL a Redisem a o dva týdny později mobilní
aplikace ve Flutteru. Ověřené modely z prototypu se pak přenesly do serverového enginu.

Když živý zápas potřeboval vizuální záběry, vznikl v srpnu v Pythonu samostatný editor animací.
Aplikace jeho záběry používá přímo a ke každé události vybírá variantu podle početní situace a
počtu asistencí.

### Kvalita a ověřování

Jeden vývojář nemá k dispozici QA tým, proto je ověřování součástí samotného projektu. Server má
kolem 310 automatických testů, zápasový engine se kontroluje kalibračními běhy přes tisíce zápasů
a vícesezónními simulacemi a botí kluby zaplňují ligy a vytvářejí zátěž. Cílem je, aby šla každá
změna ověřit objektivně, nejen hraním. Texty nápovědy v aplikaci se navíc porovnávají s tím, co
server skutečně dělá - audit v říjnu 2026 našel a opravil 14 nesouladů ve všech deseti jazycích.
