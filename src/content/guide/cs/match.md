---
title: Zápas a živé koučování
description: Jak se zápas simuluje, co dělají formace, taktiky a riziko a co jde měnit během hry.
order: 30
---

## Jak se zápas simuluje

Každý zápas se simuluje na serveru sekundu po sekundě a do aplikace se přenáší průběžně. Hra
přechází z jedné situace do další - puk se získá, posune dopředu, vznikne šance, brankář zasáhne
nebo se hra přeruší. Každý takový přechod je kalibrovaná pravděpodobnost.

Tyto pravděpodobnosti posouvá to, co je v danou chvíli na ledě:

- hráči na ledě a jejich atributy, energie a forma,
- taktika a úroveň rizika každé formace,
- jak se hráči k taktice hodí,
- početní stav - plný počet, přesilovka, oslabení, prázdná branka,
- důležitost zápasu, při které se projevuje mentalita hráčů.

Stejný zápas za stejných podmínek dá stejný výsledek, takže ho jde přehrát a zkontrolovat. Jak jsou
pravděpodobnosti kalibrované proti skutečnému hokeji, popisuje stránka Kalibrace.

## Formace

Nastavuješ čtyři formace po třech útočnících a dvou obráncích, základního a náhradního brankáře, dvě
přesilovkové a dvě oslabené formace.

- **Ice time.** Předvolba rozděluje čas na ledě mezi formace. Střídání se řídí energií hráčů:
  unavený hráč ztrácí energii rychleji a hraje hůř.
- **Přesilovka.** Dvě pětky: tři útočníci, obránce a volné místo. Na led jde pětka s nejvíc
  energie. Proti dvěma trestům hraje celá pětka; při 4 na 3 jeden hráč vynechá.
- **Oslabení.** Dvě čtveřice - dva útočníci a dva obránci. Při oslabení o dva hrají oba obránci a
  první útočník.
- **4 na 4 a 3 na 3.** Když jsou oslabené obě strany, formace na ledě se zmenší: dva obránci a dva
  útočníci, nebo dva útočníci a obránce.
- **Brankáři.** Chytá základní brankář; náhradník nastoupí, když se zraní. Únava brankáře se
  přenáší ze zápasu do zápasu.

## Taktiky a riziko

Každá formace má útočnou a obrannou taktiku, od každé je šest:

| Útok | | Obrana | |
|---|---|---|---|
| Quick Strike | rychlé vyjetí a útok dřív, než se obrana zformuje | Puck Hunt | napadání hráče s pukem ve všech pásmech |
| Stretch Counter | dlouhé přihrávky a okamžité protiútoky | Strong-Side Lock | vytlačení puku k jednomu mantinelu a jeho uzavření |
| Possession Cycle | dlouhé držení puku podél mantinelu | Man Marking | těsné osobní bránění |
| Direct Pressure | nahození, forčeking a fyzický tlak | Layered Zone | kompaktní vrstvy chránící nebezpečná místa |
| Point & Traffic | střely od modré, clonění a dorážky | Neutral Trap | uzavření středu středního pásma |
| Slot Overload | rychlé rotace a krátké přihrávky do slotu | Low Collapse | obrana blízko vlastní branky |

Taktiky vycházejí ze skutečných systémů popsaných v trenérských materiálech a analýzách (viz Zdroje).

Každá taktika některým typům hráčů sedí a několika nesedí; popis taktiky je vypisuje. Vhodnost se
měří proti průměrnému hráči, takže žádná taktika není sama o sobě lepší než jiná. Taktika se vyplatí
tehdy, když má formace víc hráčů, kterým sedí, než je obvyklé.

**Úroveň rizika** jde od Betonové obrany přes Kontrolu a Vyvážené po Presink a Vabank. Čím víc
formace riskuje, tím víc tlačí dopředu a střílí - a tím víc šancí soupeři dovolí.

## Příprava a skauting soupeře

Před zápasem můžeš soupeře jednou proskautovat. Skauting ukáže sílu jeho uložených formací, report
z až pěti posledních zápasů a důležitost zápasu pro oba týmy. Tvému týmu dá i malý bonus za
přípravu, který roste s profesionálním skautingem. Soupeř může sestavu před začátkem ještě změnit.

## Důležitost zápasu

Důležitost ukazuje, kolik zápas pro každý tým znamená - jeden dílek u běžného ligového zápasu, víc
v boji o play-off nebo lepší nasazení, všech pět v play-off. Pro oba týmy může být jiná. Čím vyšší
důležitost, tím víc ve vypjatých chvílích rozhoduje mentalita hráčů.

## Během zápasu

Během zápasu vidíš, kdo je na ledě, energii každého hráče, události tak, jak se stanou, a průběžné
statistiky. Sestavu i taktiku můžeš měnit; uložená změna platí od chvíle, kdy začne působit. V
posledních pěti minutách můžeš při prohrávání odvolat brankáře. Góly a vybrané šance se zobrazují
jako animované záběry vybrané podle skutečné události - početního stavu a počtu asistencí.
