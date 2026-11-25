---
title: Príbeh Ice Flow
description: Ako jeden vývojár v spolupráci s AI navrhol a postavil online hokejového manažéra pre mobil medzi aprílom a novembrom 2026.
lead: >-
  Ice Flow: Hockey Manager je online manažérska hra o ľadovom hokeji pre mobilné telefóny, ktorú vyvíja jeden
  človek. Okrem časti grafiky, ktorá bola dokončená vo Photoshope, vzniklo zhruba 99 % práce -
  herný dizajn, server, mobilná aplikácia, nástroje aj texty - v komunikácii s umelou inteligenciou,
  z veľkej časti počas prechádzok s kočíkom. Projekt je praktickou skúškou toho, kam až môže jeden
  človek s potrebnými znalosťami dotiahnuť zložitý produkt s dnešnou AI.
stats:
  - value: '1'
    label: vývojár
  - value: '7'
    label: mesiacov vývoja, apríl - november 2026
  - value: '4'
    label: kódové bázy - prototyp enginu, server, mobilná aplikácia, editor animácií
  - value: '2 000+'
    label: commitov
  - value: '~290 000'
    label: riadkov kódu
  - value: '11'
    label: jazykov v aplikácii aj na webe
storyTitle: Ako hra vznikala
areasTitle: Čo hra obsahuje
areasIntro: >-
  Prehľad hlavných systémov k stavu v novembri 2026. Čísla zodpovedajú súčasnému nastaveniu hry a
  pri balancovaní sa môžu meniť.
areas:
  - title: Živé koučovanie
    text: >-
      Zápasy sa simulujú na serveri a do aplikácie sa prenášajú priebežne. Tréner môže zasiahnuť
      kedykoľvek, nielen medzi tretinami.
    facts:
      - Štyri kompletné formácie, základný a náhradný brankár, dve presilovkové a dve oslabovacie formácie
      - 6 útočných a 6 obranných taktík a 5 úrovní rizika, nastaviteľné pre každú formáciu
      - Energia počas striedania klesá a na striedačke sa obnovuje; nahromadená únava obmedzuje štartovú energiu
      - Striedanie, miešanie formácií, odvolanie brankára a špeciálne formácie sa dajú meniť počas hry, aj v predĺžení
      - Oneskorené vylúčenie, predĺženie 3 na 3 a prázdna bránka sú skutočné herné stavy
      - Stav zápasu posiela server každú sekundu cez SSE
      - Prítomnosť manažéra pri živom zápase - aj od rozcvičky a počas prestávok - dáva tímu malú výhodu
  - title: Prezentácia zápasu
    text: >-
      Góly a vybrané šance sa zobrazujú ako animované zábery odvodené zo skutočných udalostí
      zápasu. Nejde o fyzikálny záznam, ale zachovávajú herný kontext.
    facts:
      - Všetky góly a ďalšie šance rovnomerne rozložené počas zápasu
      - 71 rôznych gólových akcií v 194 klipoch v šiestich druhoch útoku - od brejku po obídenie bránky
      - Akcia sa vyberá podľa skutočného početného stavu, brankárov a počtu asistencií (5 na 5, 6 na 5 s prázdnou bránkou, presilovka 5 na 3 a ďalšie)
      - Šanca končí podľa skutočnej strely - zákrokom, dorážkou alebo strelou mimo bránku - a obrancovia sa v záberoch snažia akciu zastaviť
      - Zábery vznikajú vo vlastnom editore animácií vytvorenom pre tento projekt
  - title: Hráč ako dlhodobý systém
    text: >-
      Hodnotu hráča neurčuje jediné číslo. Ratingy, skúsenosti, forma a predpoklady sa počas
      kariéry vyvíjajú rôznym tempom, takže dvaja hráči s rovnakými ratingmi sa môžu výrazne líšiť.
    facts:
      - Juniori sa skautujú v 17 rokoch; ratingy a predpoklady (TRT) sa zobrazujú ako rozsah, ktorý skautské reporty spresňujú
      - Vývoj od 18 rokov cez tímový a individuálny tréning, na farme s menšími prírastkami
      - Skúsenosti stabilizujú výkon a hospodárenie s energiou; forma odráža zhruba posledných 10-20 zápasov
      - Mentalita rastie s vystavením dôležitým zápasom; disciplína ovplyvňuje vylúčenia a bitky
      - Odolnosť voči zraneniam klesá s vekom a po vážnych zraneniach
      - Ambícia a lojalita rozhodujú, ako hráč prijme ponuku zmluvy
      - Veteráni hrajú stabilnejšie, ale strácajú rýchlosť a kondíciu, až ukončia kariéru
  - title: Riadenie klubu
    text: >-
      Tréning, farma, zmluvy, prestupový trh, zázemie a financie sú prepojené, takže rozhodnutie
      v jednej oblasti má dôsledky v ostatných.
    facts:
      - Farma hrá vlastnú súťaž súbežne s prvým tímom
      - Zmluvy až na 5 sezón; plat sa vyjednáva (podľa plánu od 4. sezóny) a nie je to pevný cenník - hráč na ponuku reaguje podľa svojej ambície a lojality
      - Na každého hráča 3 pokusy; po odmietnutí sa manažér dozvie len približne, ako ďaleko bola ponuka od hráčovej predstavy
      - Zohratosť vzniká medzi konkrétnymi dvojicami spoluhráčov na ľade - rastie so spoločnými minútami a bez nich slabne; popri atribútoch, vhodnosti taktiky, skúsenostiach a stave hráčov je ďalšou časťou sily formácie (podľa plánu od 5. sezóny)
      - Hľadanie na trhu ponúkne až päť kariet, o ktoré môžu súperiť aj ostatní manažéri
      - Prestupový trh s vyvolávacou cenou 80-110 %, 8-minútovou aukciou po prvom príhode a 90-sekundovým predĺžením
      - Dve meny - Flow na prevádzku klubu, Gold Pucks na trh, skauting a juniorov
      - Jeden sponzor na peniaze a jeden na gold pucky za sezónu, každý vybraný z troch druhov ponúk
      - Aréna so stavom a opravami a personál - tréneri, zdravotníci, skauting, vedenie a rozvoj hráčov
      - Voliteľné výdavky (podľa plánu od 3. sezóny) - sústredenie a školenie pre tréning, VIP logistika na zápas vonku, prémia do kabíny, ktorá rastie s dôležitosťou zápasu, a špeciálna regenerácia zraneného hráča; manažér volí, kedy minúť Flow na krátkodobú výhodu a kedy ich nechať na platy a dlhodobý rozvoj
  - title: Sezóna a súťaže
    text: >-
      Sezóna trvá 21 skutočných dní. Kalendár je krátky, ale každý blok dňa prináša rozhodnutia.
    facts:
      - 63 blokov za sezónu - 21 dní, každý rozdelený na tri časti
      - Ligy po 12 tímoch, každý s každým štyrikrát - 44 ligových zápasov
      - Play-off - štvrťfinále na dve víťazstvá, semifinále a finále na jeden zápas
      - Elite liga - 24 tímov, 6 kôl švajčiarskym systémom, najlepších 16 do play-off, v rovnakom kalendári ako liga
      - Rapid liga - 4 tímy, každý s každým, odohrá sa okamžite, bez únavy, zranení a vplyvu na ligové štatistiky
      - Dôležitosť zápasu vychádza zo skutočnej situácie v tabuľke a pre každý tím môže byť iná
      - Plán postupného odomykania podľa sezón klubu - 2. Elite a podpis juniorov, 3. herné predpoklady (talent, profesionalita, odolnosť voči zraneniu, disciplína, mentalita) a voliteľné výdavky, 4. ambícia, lojalita a vyjednávanie zmlúv, 5. zohratosť formácií; od 3. sezóny len pri aktívnom hraní. Testovacia verzia odomyká rýchlejšie, v 2. a 3. sezóne
  - title: Kalibrácia simulácie
    text: >-
      Zápasový engine je kalibrovaný na dlhodobé priemery skutočného hokeja a overovaný dlhými
      simuláciami.
    facts:
      - Ciele na tím a zápas - zhruba 29 striel na bránku, 3,1 gólu, úspešnosť zákrokov 89,7 %, 2,8 presilovky
      - Samostatné kontroly rozdielu sily tímov, vplyvu brankára, rizika, divákov, formy, únavy, zohratosti a vhodnosti taktiky
      - Pätnásťsezónne simulácie strážia, aby vývoj, mentalita a disciplína neutekali
      - Rovnaký zápas sa z uložených snapshotov prehrá za rovnakých podmienok
timelineTitle: Časová os
milestones:
  - date: Apríl 2026
    phase: idea
    phaseLabel: Koncept
    title: Koncept v rozhovoroch
    text: >-
      Návrh začína bez kódu: čo má mobilný hokejový manažér ponúkať, ako má fungovať živé koučovanie
      a dlhodobý vývoj hráčov a ako udržať ekonomiku v rovnováhe.
  - date: 27. apríla 2026
    phase: engine
    phaseLabel: Prototyp enginu
    title: Prvý prototyp zápasového enginu
    text: >-
      Prototyp v Pythone simuluje zápasy po tretinách - striedania, výmeny formácií, hru v pásmach a
      góly. Slúži ako prostredie na ladenie herných pravidiel.
  - date: Máj 2026
    phase: engine
    phaseLabel: Prototyp enginu
    title: Hĺbka simulácie
    text: >-
      Pokročilé štatistiky, model brankára, vplyv stavu skóre a zápasová forma. Engine sa prepisuje
      a kalibruje voči skutočným číslam.
  - date: Začiatok júna 2026
    phase: engine
    phaseLabel: Prototyp enginu
    title: Model riadenia klubu a ekonomiky
    text: >-
      Prototyp získava manažérsky modul - platy, údržbu zázemia, príjmy zo zápasov, únavu a zranenia -
      a ekonomiku testovanú cez mnoho sezón.
  - date: 10. júna 2026
    phase: server
    phaseLabel: Server
    title: Herný server
    text: >-
      Začína vývoj produkčného servera v Kotline a Quarkuse s PostgreSQL - generátor klubov, vývoj
      tréningom a počas štyroch dní celá nasimulovaná ligová sezóna.
  - date: Koniec júna 2026
    phase: mobile
    phaseLabel: Mobilná aplikácia
    title: Mobilná aplikácia a prestupový trh
    text: >-
      Aplikácia vo Flutteri vzniká 24. júna a o dva dni neskôr je lokalizovaná. Na serveri
      pribúda skauting juniorov, prestupový trh, Redis, zázemie klubu a formácie s taktikou.
  - date: Júl 2026
    phase: server
    phaseLabel: Server
    title: Základné systémy
    text: >-
      Najintenzívnejší mesiac s približne 600 commitmi na serveri a v aplikácii - play-off, trh
      v reálnom čase cez SSE, sponzori, národnosti, klubové logá a farby dresov, Elite liga, aréna,
      botie kluby a zápasová forma z prototypu prenesená do serverového enginu.
  - date: August 2026
    phase: animation
    phaseLabel: Animácie
    title: Živý zápas a editor animácií
    text: >-
      Režim živého zápasu so zmenami zostavy, taktiky a brankára počas hry. 24. augusta vzniká
      samostatný editor animácií a jeho gólové animácie sú ešte v ten istý deň v aplikácii.
  - date: September 2026
    phase: server
    phaseLabel: Server
    title: Stabilita online prevádzky
    text: >-
      Jeden autoritatívny serverový čas, zamykanie klubu počas jeho zápasu, záťažové testy s bot
      runnerom, opravy deadlockov, optimalizácia dopytov a farmárska súťaž v aplikácii.
  - date: Október 2026
    phase: engine
    phaseLabel: Engine a ekonomika
    title: Kalibrácia, onboarding a monetizácia
    text: >-
      Nová kalibrácia enginu podľa dát z NHL a zdokumentovaný model taktík. Registrácia a sprevádzaný
      tutoriál, potom mena Stars, denné a sezónne úlohy, Rapid liga, obchod a 25 celoživotných
      achievementov.
  - date: November 2026
    phase: server
    phaseLabel: Server
    title: Zmluvy, prítomnosť a animácie
    text: >-
      Mentalita, disciplína a forma, dôležitosť zápasu podľa tabuľky, vyjednávanie zmlúv s ambíciou
      a lojalitou, zohratosť dvojíc na ľade, voliteľné výdavky klubu, bonus za manažéra pri živom
      zápase, 71 gólových animácií v 194 klipoch, prihlásenie cez Google, push notifikácie,
      slovenčina ako jedenásty jazyk a nezávislý audit servera.
  - date: December 2026
    phase: launch
    phaseLabel: Plán
    title: Testovanie matematiky
    text: >-
      Overovanie hernej matematiky - ekonomiky, vývoja hráčov a zápasov - a dolaďovanie balansu.
  - date: Január 2027
    phase: launch
    phaseLabel: Plán
    title: Testovanie v cloude
    text: >-
      Prevádzka na cloudových serveroch s napojením na skutočné knižnice pre platby a reklamy.
  - date: Február 2027
    phase: launch
    phaseLabel: Plán
    title: Vydanie
    text: >-
      Vydanie Ice Flow: Hockey Manager.
  - date: Po spustení
    phase: launch
    phaseLabel: Plány
    title: Čo príde ďalej
    text: Plánované, zatiaľ bez termínu.
    todo:
      - All-Star - nová súťaž vedľa Rapid ligy, hraná na princípe asociácií klubov
      - Výskum taktík pre presilovku, oslabenie, hru 3 na 3 a hru bez brankára - dnes taktika platí len pri 5 na 5 a 4 na 4; nové systémy pribudnú, až budú podložené zdrojmi a vyvážené
      - Trestné strieľanie počas zápasu
      - Vylepšovanie animácií a grafiky zápasu
      - Servery pre Európu, Áziu a Ameriku
notes:
  - title: Obchodný model
    paragraphs:
      - >-
        Hráčov, Flow ani Gold Pucks nemožno kúpiť za peniaze. Prémiová mena Stars sa získava hraním -
        za denné úlohy (10 denne, až 210 za sezónu), sezónne úlohy (130 za sezónu), celoživotné
        achievementy (25 oblastí po 5 úrovniach) a umiestnenie v Rapid lige (1-5 hviezd, jedna reklama za
        vstup, najviac 10 denne).
      - >-
        Za Stars možno získať nový názov alebo klubové farby, logo, nové meno alebo vzhľad hráča a dva
        passy platné 21 dní. Platby skutočnými peniazmi nie sú v aktuálnej aplikácii zapnuté; plánované
        sú platené logá a passy a príspevok Podporiť hru, ktorý je len poďakovaním bez hernej
        výhody. Ads Pass odstráni reklamy, ale denné limity nemení. Sponsor Pass zvyšuje počas
        platnosti len príjmy od sponzorov vo Flow aj Gold Pucks, a to o 10 %. Je to ekonomické
        zrýchlenie, nie exkluzívna sila: rovnaký pass sa dá získať aj za Stars zarobené hraním.
        Obnoviteľný príjem hviezd sám však nestačí na to, aby bol aktívny každú sezónu, takže keď bude
        platenie zapnuté, platiaci hráč ho bude môcť mať častejšie a získa tým malú dlhodobú
        ekonomickú výhodu. Ice Flow teda nie je pay-to-win v zmysle nákupu hráčov alebo sily.
      - >-
        Keďže hru vyvíja jeden človek, sú náklady na prevádzku nízke a hra nepotrebuje agresívnu
        monetizáciu, aby sa udržala.
  - title: Súčasný stav
    paragraphs:
      - >-
        Technický základ je pripravený na uzavreté alebo postupné spustenie - prihlásenie cez Google,
        záťažové testy s 288 botími klubmi, živý zápas riadený serverom a deterministické prehrávanie
        zápasov. Chýbajú zatiaľ dáta zo skutočnej prevádzky - opätovné pripojenia, hlásenia pádov, retencia
        a správanie ekonomiky so skutočnými hráčmi. Ďalšou fázou preto nie je pridávanie funkcií, ale
        postupné spustenie, zber telemetrie a balancovanie.
---

Nápad na Ice Flow vznikol v apríli 2026, ešte predtým, než bol napísaný prvý riadok kódu. Prvé týždne
prebiehali v rozhovoroch s AI, v ktorých sa definovalo, čím má hra byť: mobilný hokejový manažér,
v ktorom rozhodovanie pokračuje aj počas zápasu, hráči sa vyvíjajú celú kariéru a online svet
beží ďalej aj medzi hraním. Väčšina týchto rozhovorov prebiehala na prechádzkach s kočíkom - v čase,
ktorý by sa inak na vývoj využiť nedal.

Role boli od začiatku jasne rozdelené. Autor vystupoval ako produktový vlastník a architekt:
rozhodoval o hernom dizajne, prioritách a kompromisoch a kontroloval výsledky. AI písala
implementáciu, testy, kalibračné experimenty aj dokumentáciu. Typická iterácia bola písomná
špecifikácia, implementácia, automatické testy a vyhodnotenie výsledkov voči zamýšľanému správaniu.

### Od prototypu k online hre

Prvým funkčným kódom bol na konci apríla prototyp zápasového enginu v Pythone. Slúžil ako
laboratórium: striedania, výmeny formácií, hra v pásmach, brankári, forma aj ekonomika sa v ňom
modelovali a kalibrovali skôr, než sa čokoľvek dostalo do skutočnej hry. V júni začal vývoj
produkčného servera v Kotline s Quarkusom, PostgreSQL a Redisom a o dva týždne neskôr mobilnej
aplikácie vo Flutteri. Overené modely z prototypu sa potom preniesli do serverového enginu.

Keď živý zápas potreboval vizuálne zábery, vznikol v auguste v Pythone samostatný editor animácií.
Aplikácia jeho zábery používa priamo a ku každej udalosti vyberá variant podľa početnej situácie a
počtu asistencií.

### Kvalita a overovanie

Jeden vývojár nemá k dispozícii QA tím, preto je overovanie súčasťou samotného projektu. Server má
viac než 900 automatizovaných testovacích prípadov, zápasový engine sa kontroluje kalibračnými behmi cez tisíce zápasov
a viacsezónnymi simuláciami a botie kluby zapĺňajú ligy a vytvárajú záťaž. Cieľom je, aby sa každá
zmena dala overiť objektívne, nielen hraním. Texty nápovedy v aplikácii sa navyše porovnávajú s tým, čo
server skutočne robí - audit v októbri 2026 našiel a opravil 14 nesúladov vo všetkých desiatich jazykoch. V novembri
prešiel server nezávislý audit v 13 sekciách a každé závažné zistenie má teraz svoj test.
