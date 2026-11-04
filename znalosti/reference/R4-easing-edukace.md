# R4: Proč animace vypadá roboticky (easing), vzdělávací video

| | |
|---|---|
| Odkaz | https://www.instagram.com/reel/De-LCYaRcC_/ |
| Autor | @ugoki.ai (kurz motion designu s AI) |
| Publikováno | 2026-10-26 |
| Metriky při analýze | 4 291 lajků, 144 komentářů |
| Formát | 1080×1920, **60 fps**, 48,5 s |
| Zvuk | lidský voiceover + hudba, −14,2 LUFS |
| Tvrdé střihy | žádné, vše je jedna souvislá animace |
| Analyzováno | 2026-10-30 |
| Znovu poslán uživatelem | 2026-11-04 (vzor střihu a prezentace), střihová partitura níže |

![náhled](nahledy/R4-easing-edukace.jpg)

## Popisek
> Want to learn AI-powered motion design? DM us UGOKI and we'll send you the link 🔥 #claude #motiondesign

## Přepis
```
[ 0.0] Does your animation look robotic? The problem is its speed.
[ 4.2] Nothing in the real world moves at a constant speed. Look at its trail. Every step is the same.
       It starts all at once, and it stops all at once.
[14.2] For everything that comes in, ease out. It arrives fast, then brakes for a long time,
       as if set down by a steady hand.
[23.4] For everything that leaves, the opposite. Ease in. It starts slowly, then it gets away.
[30.5] And for the interface, a spring. It overshoots its target just a little, then settles back.
[37.0] Tell Claude in exactly these words, and your animation jumps to a whole new level.
[43.2] Want to go further? DM me UGOKI.
```

## Časová osa (přibližně)
| čas | obraz |
|---|---|
| 0–4 s | Dva přepínače nad sebou: ROBOT (šedý, lineární) vs PRO (červený, s easingem), stejný pohyb vedle sebe |
| 4–14 s | Graf pozice/čas, lineární přímka, stopa bodů se stejnými rozestupy |
| 14–23 s | Karta „Entrances – ease out“: křivka strmě nahoru a pak dlouho dobržďuje |
| 23–30 s | Karta „Exits – ease in“: pomalý rozjezd, pak prudké zrychlení |
| 30–37 s | Karta „Interface – spring“: překmit nad cíl („slight overshoot“), tlačítko „Start render“, štítek „4× slower“ |
| 37–43 s | Okno Claude Code, píše se prompt (viz níže), přepínač se změní z ROBOT na PRO |
| 43–48,5 s | Zámek „The full method → inside the Ugoki course“, maketa DM chatu „UGOKI“, obří „DM me UGOKI“ |

## Prompt pro Clauda (doslova z videa)
```
Entrances: ease out.
Exits: ease in.
Interface: spring, slight overshoot.
Nothing linear.
```

## Techniky
- **Háček otázkou na bolest diváka** („Does your animation look robotic?“).
- **Titulky slovo po slově**: aktuální slovo má červený podklad (štítek), ostatní jsou bílá. Titulky jsou ve spodní třetině uprostřed.
- **Jednotný vizuální systém**: tmavé pozadí s červenou vinětou, karty se zaoblenými rohy a jemným okrajem, malé štítky, monospace popisky os.
- **Vysvětlení na vizualizaci** (graf + stopa bodů), ne jen slovy.
- **Srovnání vedle sebe** (ROBOT vs PRO) hned na začátku.
- **60 fps** kvůli plynulosti UI animací.
- **Okamžitě použitelný tip** (prompt), pak upsell: „chceš víc?“ → DM klíčové slovo.

## Co si beru
**Pravidla easingu, základ všech mých animací** (P-easing v pravidlech). Titulky slovo po slově se zvýrazněným aktivním slovem. 60 fps pro UI animace. Struktura vzdělávacího videa.

## Střihová partitura (doplněk 2026-11-04, uživatel poslal znovu jako vzor střihu)
Uživatel po V004: „zkus se zaměřit víc na ten střih a editaci videa… adaptuj se na tyhle střihy.“ Tento oddíl měří **střih**, ne easing.
Podklady: `media/reference/R4-easing-edukace/pasy/` (`pas_025s_01–10.jpg` = celé video po 0,25 s s časem v rohu, `husty_*.jpg` = každé 2–3 snímky
kolem každé změny), přepis po slovech Whisper medium (`prepis.py --slova`), obálka hlasu 300 Hz–4 kHz po 10 ms, spektrogram 0–8 kHz. 60 fps, 1 snímek = 0,017 s.

### 1. Titulky slovo po slově (změřený mechanismus)
Časy: první bledý snímek slova → plný červený štítek · skutečný začátek hlasu (obálka) · Whisper. „Předstih“ = plný štítek vs. hlas (kladné = obraz dřív).

| slovo | bledé | plný štítek | hlas (obálka) | Whisper | předstih |
|---|---|---|---|---|---|
| Does | 0,10 | 0,13 | 0,21 | 0,00 | +0,08 |
| your | 0,33 | 0,37 | – | 0,40 | +0,03 (vs. Whisper) |
| animation | 0,50 | 0,53 | – | 0,68 | +0,15 (vs. Whisper) |
| Nothing | 4,40 | 4,43 | 4,52 | 4,58 | +0,09 |
| moves | 5,70 | 5,73 | – | 5,72 | 0,00 |
| Look | 7,77 | 7,80 | 7,77 | 7,76 | −0,03 |
| It (starts) | 10,75 | 10,78 | 10,78 | 10,80 | 0,00 |
| For (14) | 14,30 | 14,33 | 14,30–14,42 | 14,38 | 0 až +0,09 |
| in: | 15,60 | 15,63 | – | 15,52 | −0,11 (jediné zpoždění) |
| ease | 16,25 | 16,30 | – | 16,32 | +0,02 |
| It (arrives) | 17,40 | 17,45 | 17,45 | 17,44 | 0,00 |
| For (23) | 23,37 | 23,40 | 23,46 | 23,50 | +0,06 |
| the | 25,15 | 25,20 | 25,19 | 25,18 | 0,00 |
| And | 30,60 | 30,63 | 30,65 | 30,00 (chybně) | +0,02 |
| a (spring) | 31,83 | 31,87 | 31,86 | 31,92 | 0,00 |
| then | 35,50 | 35,53 | 35,59 | 35,56 | +0,06 |
| Tell | 37,03 | 37,07 | 37,17 | 37,16 | +0,10 |
| and (39) | 39,60 | 39,63 | 39,56 | 39,60 | −0,07 |
| Want | 43,22 | 43,25 | 43,34 | 43,38 | +0,09 |
| DM | 44,70 | 44,75 | 44,80 | 44,90 | +0,05 |
| UGOKI | 45,45 | 45,50 | 45,49 | 45,54 | 0,00 |

**Pravidlo autora (21 slov):** štítek je hotový **0 až 0,10 s před hlasem** (medián +0,02 s, tj. 0–6 snímků dřív), zpoždění jen 2× a nejvýš 0,1 s.
Whisper má proti obálce rozptyl ±0,1 s a u „And“ 30,0 selhal (vzal pauzu), takže časy slov vždy ověřit obálkou nebo snímky.
- **Náběh slova = 2 snímky (0,033 s)**: snímek 1 bledé, lehce rozmazané a ~10 px vpravo od cílové polohy; snímek 2 plné. Celý řádek se **přecentruje** (posune doleva o půl šířky nového slova) v týchž 2 snímcích.
- **Štítek se přelije**: červená pilulka z předchozího slova zmizí a na novém naskočí v týchž 2 snímcích; předchozí slovo zbělá. Nikdy dvě pilulky naráz.
- **Pilulka drží na posledním slově přes pauzu**: „speed.“ 3,47–4,33 (0,87 s), „hand.“ 22,6–23,37 (0,8 s), „level.“ 42,0–42,93 (0,9 s). Interpunkce je uvnitř pilulky („speed.“, „robotic?“, „once,“, „"UGOKI".“).
- **Výměna řádku tvrdě**: starý řádek zmizí z jednoho snímku na druhý, 1–2 prázdné snímky (4,37; 7,70–7,73; 31,80), první slovo nového řádku naskočí svým 2snímkovým náběhem. Výjimka na koncích bloků: řádek odejde rozostřením (42,93–42,97 před zámkem, 46,70–46,75 poslední).
- **Řádky**: 42 řádků za 48,5 s, **1–5 slov (medián 3), ≤ 22 znaků**. Lámání na hranici věty nebo věty se dělí podle délky („Nothing in | the real world | moves at | a constant speed.“). Nikdy dva řádky nad sebou.
- **Geometrie (1080×1920)**: tučný grotesk (Inter / SF Pro Display Bold), výška verzálek 57 px ⇒ písmo ≈ 80 px; pilulka 93 px vysoká, zaoblení ≈ 14 px, vodorovný okraj ≈ 16 px, barva **RGB 252/56/31**, kolem měkká červená záře; bílý text s nepatrnou září. Pilulka y 1352–1445 ⇒ **střed 73 % výšky**, spodek 475 px nad okrajem = těsně nad bezpečnou zónou 400 px. Nejširší řádek ≈ 780 px („And for the interface,“).

### 2. Prvky UI: partitura
Typy: **FADE** = zjevení z lehkého rozostření, 2–4 snímky · **CUT** = z jednoho snímku na druhý · **MORF** = tentýž rámec změní rozměr nebo obsah ·
**ROST** = vyroste z bodu / obrysu s překmitem (pružina) · **LET** = pohyb s pohybovým rozmazáním · **KASKÁDA** = několik prvků po 0,07–0,15 s za sebou.
„Hlas“ = slovo, na které prvek sedí, a odchylka (kladné = obraz dřív).

| # | čas | prvek | příchod | klid | odchod | hlas / vazba |
|---|---|---|---|---|---|---|
| 1 | 0,00–4,13 | **Háček: dvě řady přepínačů** ROBOT (šedý knoflík krokuje po 7 políčkách, za ním zůstávají „duchové“ políček, krok ≈ 0,12 s, smyčka ≈ 2,5 s) vs PRO (červený knoflík přeletí dráhu za ≈ 0,3 s s rozmazáním a 3 duchy u cíle = dobrždění, pak stojí ≈ 2 s); u obou „SPEED“ proužek vpravo nahoře | stojí od **snímku 0** (hotový obraz, B6) | smyčka | 4,13–4,30 FADE-out, zároveň za nimi FADE-in rámec karty (křížení 0,17 s) | „Does“ 0,21 začíná 0,2 s po startu; „speed.“ 3,47 → přepínače odcházejí 0,65 s po posledním slově, v pauze |
| 2 | 4,13–4,50 | **Karta grafu** (x 60–940, y 280–1280 = 81 % šířky, střed ve 41 % výšky), osy POSITION / TIME, pilulka „linear“ | KASKÁDA: rámec 4,13 → osy se vykreslí 4,30–4,37 → pilulka 4,43–4,50 | rámec drží **do 42,5 s** (38 s), mění se jen obsah | 42,50–42,77 smrští se do bodu (zámek) | „Nothing“ 4,52: rámec 0,4 s před, pilulka 0,1 s před |
| 3 | 4,13–4,77 | **Šedý knoflík ROBOT = míček grafu**: sdílený objekt; při odchodu přepínačů zůstane, sjede po pravé hraně karty dolů do pravého dolního rohu | LET (ease-out, 0,64 s) | 4,77–5,55 | – | překrývá „Nothing in the“ |
| 4 | 5,57–7,00 | **Běh po přímce**: míček jede z počátku po diagonále, za ním **stopa teček** každých ≈ 0,1 s, vpravo sloupec **duchů** (svislá poloha) | start 5,57 | dojede 7,00, pak 7,0–8,9 stojí | 10,50 CUT (stopa, duchové i poloha vymazány) | „moves“ 5,72: start **0,15 s před** slovem; „speed.“ 6,78–7,24 = dojezd |
| 5 | 9,00–10,30 | **Měření**: zvýrazněná tečka + čárkované vodítko + pravítko se stejnými dílky u sloupce duchů | FADE 9,00 | – | 10,50 CUT | „every“ 9,02: 0,02 s před; „step is the same“ |
| 6 | 10,75–12,75 | **Start a stop**: 10,75 červený kroužek kolem počátku → 11,00 míček vystřelí **bez rozjezdu** → 12,30 dojede → 12,50 červený kroužek kolem cíle | kroužek FADE 0,05 s | 12,75–14,27 stojí (1,5 s) | 14,30 CUT | „It“ 10,78 kroužek 0,03 s před; „starts“ 11,06 → start 11,00; „stops“ 12,72 → kroužek **0,2 s před** |
| 7 | 14,30–14,63 | **Entrances**: 14,30 obsah vymazán (1 snímek) → 14,33–14,37 pilulka „linear“ ⇢ „Entrances“ (křížení) → 14,47 červený míček FADE vpravo dole → 14,60–14,63 celá **červená stopa** FADE naráz | KASKÁDA 4 kroků za 0,33 s | – | 23,40 | „For“ 14,30–14,42: vymazání přesně na nádech slova; „everything“ 14,62 = stopa |
| 8 | 15,40–17,55 | **Kurzor** vjede zprava zdola 15,40 → na čáře 15,65 → **2 úchyty** (kroužky) FADE 15,65 → tah 16,15–16,45 ohne přímku do ease-out (stopa se přerozdělí) → pilulka „→ ease out“ FADE 16,25–16,30 → kurzor odjede 17,25–17,55 | LET | – | LET ven | „comes“ 15,26–15,52 = kurzor; „in:“ 15,52 = úchyty; „ease“ 16,25 = tah (křivka se ohýbá **během** slova „ease out“) |
| 9 | 17,55–20,70 | **Dojezd**: červený čtverec ve sloupci vyletí nahoru 17,55–17,85 s rozmazáním a září, 17,85–20,7 se **pomalu dosouvá** o posledních pár px | LET | – | – | „arrives“ 17,60 = start (0,05 s před); „fast,“ 17,96 = vrchol rychlosti; „brakes for a long time“ 19,1–20,7 = dosouvání |
| 10 | 21,25–23,37 | **Měření 2**: pravítko s nestejnými dílky + zvýrazněná tečka | FADE | stojí do 23,37 | 23,40 CUT | „as if set down“ 21,0–21,9 |
| 11 | 23,40–23,73 | **Exits**: 23,40–23,47 pilulka „Entrances → ease out“ ⇢ „Exits“, obsah vymazán, křivka zůstane jako tenká linka → 23,60 míček FADE → 23,73 stopa FADE | KASKÁDA (stejný vzorec jako #7) | – | 30,55 | „For“ 23,46: přeznačení **0,06 s před**; „everything“ 23,74 = stopa |
| 12 | 25,00–26,30 | **Překlopení křivky bez kurzoru**: 25,00 úchyty FADE vlevo nahoře → 25,25–25,95 úchyty sjedou do pravého dolního rohu, křivka projde přímkou (25,65) a skončí jako ease-in → 26,30 pilulka „→ ease in“ | MORF 0,7 s | úchyty zmizí 27,50 | – | „the“ 25,19: úchyty 0,2 s před; **„opposite“ 25,36–25,78 = překlopení** (slovo a pohyb jsou totéž); „Ease“ 26,27 = pilulka |
| 13 | 29,00–30,00 | **Útěk**: míček se rozjíždí pomalu 29,0–29,6, 29,75 vystřelí nahoru s rozmazáním | LET | 30,0–30,5 | – | „then“ 29,1 = rozjezd; „away.“ 29,70 = výstřel |
| 14 | 30,53–30,93 | **Interface**: 30,53–30,57 stopa FADE-out → 30,60 pilulka FADE-out → **30,63–30,90 karta se zmenší na výšku** (1000 → 560 px, ease-out) a křivka se v ní **přemění v pružinu** s čárkovanou „TARGET“ (30,77–30,93) → 30,70 pilulka „Interface“ | MORF rámce | 31,0–31,85 | 36,95 | „And“ 30,65: morf začíná **0,02 s před** slovem, v pauze po „away.“ |
| 15 | 31,87–32,45 | **Tlačítko „Start render“**: 31,87 pilulka „→ spring“ → 32,03 čárkovaný obrys → 32,07–32,20 tlačítko **vyroste zevnitř obrysu s překmitem** → zároveň 32,13–32,45 se křivka v kartě **znovu vykreslí od počátku** sytě červeně (graf = živý pohyb tlačítka) | ROST + MORF | 32,5–33,6 | 33,65 | „a“ 31,86 = pilulka; **„spring“ ≈ 32,0–32,46 = růst tlačítka** |
| 16 | 33,60–35,00 | **Pointa „4× slower“**: 33,60 pilulka „4× slower“ vpravo nahoře → 33,65 tlačítko se **zhroutí do obrysu** (2 snímky) → 33,75–34,60 **vyroste znovu, 0,85 s místo 0,13 s** (~6,5× pomaleji), křivka se znovu kreslí 33,8–35,0 → 34,95 popisek „SLIGHT OVERSHOOT“ + tečka na vrcholu | ROST zpomaleně | 35,0–36,95 (1,95 s) | 36,95 | „overshoots“ 33,32–33,78 = pilulka + kolaps; „its target just a little,“ 33,7–35,2 = pomalý růst; „little,“ 34,85 = popisek |
| 17 | 36,95–39,00 | **Okno Claude Code**: 36,95–37,03 prolne se **přes stejný rámec** (x 60–940, horní hrana 300; výška 560 → 800), tlačítko zmizí 36,97–37,0; 37,03 pod oknem „ROBOT“ + šedý knoflík FADE; **psaní** 37,03–38,90 s kurzorem, ≈ 36 znaků/s: ř. 1 „Entrances: ease out.“ 37,03–37,45 · ř. 2 „Exits: ease in.“ 37,50–37,75 · ř. 3 „Interface: spring, slight overshoot.“ 37,75–38,50 · ř. 4 „Nothing linear.“ 38,60–38,90 **červeně s ikonou X** · 39,00 tlačítko odeslat zčervená | MORF + psaní | – | 42,50 | „Tell“ 37,17: okno **0,2 s před**; „words,“ 38,92–39,28 = odeslat |
| 18 | 37,25–41,75 | **Přepínač pod oknem**: 37,25–38,0 políčka dráhy přibývají, 38,0–39,5 šedý knoflík krokuje, **39,73 knoflík zčervená a přeletí** s rozmazáním, 40,0–41,5 červené smyčky, **41,75 popisek ROBOT → PRO** | LET | 41,75–42,5 | 42,63–42,73 FADE-out | „your“ 39,73 / „animation“ 39,87 = zčervenání; „jumps“ 40,40 = let; „new level.“ 41,58–42,16 = PRO |
| 19 | 42,50–43,25 | **Zámek**: okno se rozostří a **smrští do malého čtverce** (ease-in, 0,27 s) → 42,77 čtverec = tělo zámku → 42,83–42,93 otevřený zámek FADE → 42,97 text „The full method → inside the Ugoki course“ FADE → 43,0–43,25 **třmen zapadne** | MORF do bodu | 43,25–44,45 | 44,45–44,55 rozostření | pauza 42,2–43,3; „Want“ 43,34 = zapadnutí 0,1 s před |
| 20 | 44,55–44,85 | **DM maketa**: 44,55–44,65 „DM me“ (bílé, 68 px verzálky, y 284) FADE → 44,70 prázdný rámec karty → 44,75–44,85 obsah („ugoki · Active now“, pole „Message…“, odeslat) | KASKÁDA 3 kroků | – | 48,13 | „DM“ 44,80: nadpis 0,25 s před, karta 0,1 s před |
| 21 | 45,45–46,55 | **UGOKI**: 45,45–45,50 obří „UGOKI“ (červená, verzálky 167 px, x 166–845 = **63 % šířky**, záře) ROST pod „DM me“ → **psaní „U·G·O·K·I“ 45,50–45,75** (1 znak / 3 snímky) → 46,00–46,05 odeslání: pole se vyprázdní, bublina „UGOKI“ vpravo ROST → 46,50 odpověď „Here's the rest. · Ugoki course 2.2 · Motion curves“ vyjede zleva zdola (0,2 s) | ROST + psaní | 46,75–48,13 **úplný klid 1,38 s** (hudba sama) | 48,13 | **„UGOKI“ 45,49 = nápis, titulek i psaní v jednom snímku** |
| 22 | 48,13–48,43 | **Smyčka**: celý obraz **švihne nahoru** se svislým rozmazáním, zdola přijedou přepínače ze snímku 0 a dosednou 48,43 = snímek 0 | LET | – | konec 48,51 | bez hlasu |

**Čísla:**
- **Scén (světů) 8**: přepínače · lineární graf · Entrances · Exits · Interface · Claude Code · zámek · DM. Průměr 6,1 s. Ale **5 prostředních scén je výměna obsahu v jedné kartě** (rámec 4,13–42,5 = 38 s, 78 % videa): divák nikdy nemění „místo“, jen to, co je v rámu.
- **Přechody mezi světy**: FADE-křížení (přepínače → karta), 4× CUT obsahu + přeznačení pilulky uvnitř rámce (graf → Entrances → Exits), MORF rozměru (Exits → Interface), prolnutí přes stejný rámec (Interface → Claude), smrštění do bodu (Claude → zámek), rozostření (zámek → DM), švih (DM → smyčka). **Tvrdý střih celého obrazu: 0.**
- **Kaskáda je základní vzorec**: rámec → popisek → objekt → stopa, odstupy 0,07–0,15 s (4–9 snímků). V žádném snímku nenaskočí dva nové prvky zároveň (jediná výjimka: 45,45 nápis UGOKI + slovo titulku, záměr).
- **Sdílené objekty** drží kontinuitu: šedý knoflík = míček grafu (4,13); graf = živý záznam pohybu tlačítka (32,13); okno = zámek (42,77); konec = začátek (48,43).
- **Pauzy v hlase nejsou prázdné**: všech 6 přechodů světů leží v pauzách 0,3–1,1 s (4,13 · 14,30 · 23,40 · 30,63 · 36,95 · 42,50) a změna začne **0,02–0,4 s před prvním slovem** další věty.

### 3. Kamera
**Statická, celých 48 s.** Hrany karty jsou na týchž sloupcích (x 60–939) na snímcích 5,25 · 16,50 · 38,00; žádný drift, dotlačení ani paralaxa
(pozadí RGB 10/10/10 s červenou vinětou dole, RGB 45/16/11, se nemění). Jediný „pohyb kamery“ je švih celého obrazu nahoru 48,13–48,43 pro smyčku.
Energie vzniká **uvnitř rámu**: míček běží, kurzor táhne, tlačítko vyskočí, text se píše, titulky skáčou 3× za sekundu. Kompozice: karta nad středem
(střed 41 % výšky), titulky v 73 %, mezi nimi volno; bez čehokoli v rozích kromě pilulek uvnitř karty.

### 4. Hustota
- **UI událostí ≈ 60 / 48,5 s = 1,2 za sekundu** (příchod, odchod, změna stavu, bez titulků): 0–10 s 8 · 10–20 s 14 · 20–30 s 10 · 30–40 s 15 · 40–48,5 s 13.
  Nejhustší úsek 30,5–34 s (Interface: morf, 2 pilulky, tlačítko 2×, pointa = 9 událostí za 3,5 s).
- **Titulky 152 slov / 44 s hlasu = 3,5 slova za sekundu**, tedy ve spojení s UI ≈ **4,6 vizuálních změn za sekundu**. Většinu „energie“ dělají titulky.
- **Nejdelší klid UI** (žádný nový prvek, ale něco se hýbe): 18,0–21,25 dosouvání míčku (3,25 s, pohyb o pár px), 35,0–36,95 (1,95 s, jen titulky).
- **Nejdelší úplný klid** (nic se nehýbe, ani titulky): **46,75–48,13 = 1,38 s** na konci (DM maketa s odpovědí, hudba sama) a 12,75–14,27 jen s titulky.
- Typický klid prvku po příchodu: **0,5–1,5 s**, než přijde další změna. Tempo scén 6,1 s, ale uvnitř každé scény 3–5 dílčích kroků po 1–2 s.

### 5. Zvuk
- **Hlasitost**: celek −14,2 LUFS, po větách −13,6 až −14,5 LUFS (LRA 1,3–3,9 LU, velmi vyrovnané). **Hudba sama** (46,5–48,5) **−24,7 LUFS** ⇒ hlas
  ≈ **10–11 LU nad hudbou** (sedí s I2). Hudba se nehýbe (žádný slyšitelný ducking, úroveň pod hlasem stejná jako v pauzách).
- **Hudba = pad bez rytmu**: ve spektrogramu drží konstantní linky ≈ 640 Hz a 1,28 kHz celých 48 s, žádný kopák. Autokorelace onsetů v pásmu 40–150 Hz
  nedává stabilní vrchol (nejlepší 0,053 při 0,54 s), onsety v basu se kryjí s plozivami hlasu a SFX. **BPM nelze změřit, hudba střih neřídí** (stejně jako R6).
- **Hlas**: sebevědomý, rychlý, věty 0,8–5,5 s. Pauzy mezi větami 0,3–0,7 s, nejdelší 1,1 s (42,2–43,3 před CTA). Každá pauza nese přechod scény (oddíl 2).
- **SFX** (odhad ze spektrogramu: širokopásmové svislé čáry mimo sykavky + onsety v basu; s jistotou nejde oddělit od hlasu): 0,1–0,2 měkký whoosh (start) ·
  4,3–4,45 tlumený úder (karta) · 5,7 klik (start míčku) · 7,0 měkký dopad (dojezd) · 9,9 / 10,1 / 10,6 tiky (pravítko) · 11,0 úder (výstřel) · 12,3 dopad (stop) ·
  14,4 šum (Entrances) · 15,4 tik (kurzor) · 16,1–16,4 tik (tah úchytu) · **17,4–17,6 whoosh 1–5 kHz (dojezd „arrives fast“, nejzřetelnější efekt)** · 21,3 tik ·
  23,5 šum (Exits) · **25,3–25,6 stoupající sweep (překlopení křivky, přesně s pohybem)** · 26,3 tik (pilulka) · 29,7 whoosh (útěk) · 30,6 šum (morf) · 31,8 tik ·
  **32,1 pop do 8 kHz (tlačítko)** · 33,5 tik (4× slower) · 36,9 šum (okno) · 37,5–38,9 klávesnice (psaní) · 39,75 whoosh (knoflík zčervená) · 41,8 tik (PRO) ·
  42,5 whoosh dolů (smrštění) · 42,9 klik (zámek) · 44,5 šum (DM me) · **45,4 pop (UGOKI)** · 46,0 tik (odeslání) · 46,5 tik (odpověď) · 47,9–48,2 whoosh nahoru (švih).
  Úrovně: v pásmu 4–12 kHz vrcholy −15 až −20 dBFS, tj. na úrovni sykavek; **žádný efekt není hlasitější než hlas**. Vzorec: **každá UI událost má svůj tichý zvuk,
  hlas je vždy navrchu, hudba je jen podlaha.**

### 6. Srovnání s naším V004 (BMW i7, `projekty/004-bmw-jizda/zadani.md`)
| | R4 (vzor uživatele) | V004 (náš střih) |
|---|---|---|
| Co řídí střih | **hlas**: každá změna sedí na slovo, obraz 0–0,4 s před ním; hudba je pad bez rytmu | **hudba 120 BPM**: střihy na doby a čtvrtdoby, 15 taktů, drop 1 / zlom / drop 2 |
| Tvrdé střihy celého obrazu | **0** (1 švih na smyčku) | ≈ 25 (stopáž ↔ rendry ↔ salon ↔ mřížka ↔ písmena) |
| Kotva | **jedna karta 38 s** (78 % videa), 5 scén = výměna obsahu + 1 morf rozměru | každý takt nový svět (studio, silnice, dron, kostka, deska, mřížka, písmena, logo) |
| Prvků naráz | **1 nový prvek na snímek**, kaskáda po 0,07–0,15 s | T1: ledvinky + řez nadpisu + pulz bodu + oblouk; T9: mřížka 3×3 s 9 živými dlaždicemi + bod skáče |
| Kamera | statická | dotlačení v každém záběru, punch-in, švihy, průlet písmenem, log-zoom do mřížky |
| Text | 152 slov titulků slovo po slově (3,5/s) + 6 pilulek v kartě | bez hlasu: 6 karet faktů s rolujícími čísly, nadpis, pilulky výbavy, end card |
| Svět a barvy | **jeden tmavý svět**: #0A0A0A + červená 252/56/31 + bílá, 1 písmo, karty 59/57/58; **barva = význam** (šedá = robot, červená = pro / aktivní) | high-key studio + silnice + noční kokpit, grade se dorovnává; modrá bmw jen na akci |
| Hustota | 1,2 UI událostí/s + 3,5 slova/s; nejdelší klid 1,4 s (záměrný, CTA) | ≈ 2 události/s (doba) + střih na dobu; klid ≥ 0,5 s u karet se hlídal pravidlem G9 |
| Pointa | **totéž znovu, 6,5× pomaleji** („4× slower“), s popiskem | drop 2: 4 střihy za sekundu, nejhlasitější místo |
| Délka | 48,5 s (edukace) | 30 s (A4) |
| Konec | zámek → DM maketa s klíčovým slovem psaným živě → obří UGOKI → 1,4 s klid → smyčka | logo z clony bodu → claim → end card se spotřebou a disclaimerem |

**Jádro rozdílu:** R4 dělá energii **soustředěním** (jeden rám, jeden objekt, jedno slovo v jednom okamžiku, hodně malých kroků), V004 **střídáním**
(nový záběr a nový svět každou dobu, několik vrstev naráz). Uživatel po V004 řekl „zaměř se na střih a editaci“ a poslal R4 znovu, takže to, co chce,
je spíš první způsob: méně střihů celého obrazu, víc výměn uvnitř jednoho rámce, jeden prvek po druhém, pohyb objektů místo pohybu kamery.
Neodporuje to vkusu „energie“ (V001): R4 má 4,6 změn za sekundu, ale všechny jsou malé a čitelné.

## Co to znamená pro naše videa (střih)
Návrhy pro `pravidla-strihu.md` (zapíše režisér po všech rozborech; zdroj `[R4 střih]`):
1. **Kotva a výměna obsahu** (nové, D): hlavní rámec (karta, okno, telefon, deska) zůstane na obrazovce po většinu videa; scény jsou výměna obsahu uvnitř
   (vymazat 1 snímek → přeznačit pilulku → nový objekt → stopa, odstupy 0,1–0,15 s). Nový svět = morf rámce (rozměr, poloha), ne střih celého obrazu.
   Důkaz: R4 karta 4,13–42,5 s, 5 scén uvnitř, 0 tvrdých střihů; R6 telefon jako kotva 5 s. Upřesňuje D2/D3, odporuje praxi V004 (nový svět každý takt).
2. **Kaskáda místo „naráz“** (nové, D): prvky jedné scény přicházejí po jednom v odstupu 4–9 snímků v pořadí příčina → následek (rámec → popisek → objekt → stopa).
   Dva nové prvky v jednom snímku jen jako záměrná pointa (R4 jen 1× z ~60: UGOKI 45,45). Důkaz: 14,30/14,33/14,47/14,60 · 30,63/30,70/30,77 · 44,55/44,70/44,75.
   Zpřesňuje C7 (událost na každou dobu ≠ víc událostí v jednom snímku).
3. **Titulky slovo po slově, přesná mechanika** (upřesnění E1, E7): štítek hotový 0–0,10 s **před** hlasem (medián 2 snímky), nikdy po; náběh 2 snímky
   (bledé + 10 px zprava → plné), řádek se přecentruje, pilulka se přelije na nové slovo a předchozí zbělá; řádek 1–5 slov (medián 3, ≤ 22 znaků), výměna
   tvrdě s 1–2 prázdnými snímky na hranici věty nebo délky; pilulka drží na posledním slově přes pauzu; interpunkce uvnitř pilulky; písmo ≈ 80 px tučné,
   pilulka ≈ 93 px, střed 73 % výšky (9:16). Důkaz: tabulka 21 slov v oddíle 1. E7 (≥ 56 px) platí, R4 má 80 px.
4. **Obraz předbíhá hlas i u UI** (upřesnění D1): UI změna 0,02–0,4 s před slovem, které ji pojmenovává (karta 0,4 s před „Nothing“, úchyty 0,2 s před „the opposite“,
   okno 0,2 s před „Tell“, DM karta 0,1 s před „DM“); přechody světů leží v pauzách hlasu a začínají před prvním slovem další věty. Shoda s R6 (0,1–0,35 s).
5. **Předveď, pak zopakuj pomaleji** (nové, C/D): klíčový pohyb se ukáže v reálné rychlosti a hned znovu zpomaleně s popiskem v rohu („4× slower“ 0,13 s → 0,85 s),
   graf nebo stopa se při tom kreslí živě. Pro produktová videa: rozsvícení světel, dosednutí karty, otočka, jednou rychle a jednou pomalu. Důkaz: 32,07–32,20 vs. 33,75–34,60.
6. **Statická kamera je legitimní** (kontrast k F7 a k poučení V002 „pohyb od prvního snímku“): R4 nemá žádný pohyb kamery a žádný snímek nepůsobí mrtvě,
   protože v rámu stále něco jede. Návrh znění: dotlačení a drift jen tam, kde se v rámu nic nehýbe; když objekt pracuje, kamera stojí. **Odporuje** F7
   („pomalé dotlačení drží obraz živý“) jako výchozímu nastavení.
7. **Klidný konec před smyčkou** (upřesnění C6/D4): poslední karta (CTA) smí stát **úplně bez pohybu 1,4 s** a smyčka se uzavře švihem se svislým rozmazáním (0,3 s)
   do snímku 0. **Odporuje** C6 „nikdy zamrzlý obraz“ u CTA, kterou má divák přečíst (klíčové slovo, DM).
8. **Zvuk u videa s hlasem** (upřesnění I2, I3, I6): hudba = pad bez rytmu ≈ 10–11 LU pod hlasem, bez duckingu a bez dropů; každá UI událost má tichý klik / whoosh / pop,
   nikdy nad hlasem; nejzřetelnější SFX patří pohybu, který hlas pojmenovává („arrives fast“ 17,5, překlopení 25,3–25,6, tlačítko 32,1, UGOKI 45,4).
   I6 (vlastní hudba s dropy řídí animaci) platí jen pro videa bez hlasu.
9. **CTA jako sekvence** (rozšíření J1, C2): pointa → zámek (co je za ním) → maketa DM → klíčové slovo napsané živě (1 znak / 3 snímky) → odpověď bota →
   obří klíčové slovo (63 % šířky) nad maketou; klíčové slovo je na obrazovce 3× naráz (nadpis, pole, titulek) a zůstává až do konce. Důkaz: 42,5–48,1.
10. **Barva = význam** (rozšíření G4): jeden akcent pro všechno aktivní a správné (aktivní slovo, PRO, míček, stopa, ikona tlačítka, UGOKI), šedá pro „robot / špatně“;
    kategorie = bílá pilulka s černým textem, hodnota = tmavá pilulka s červenou tečkou a textem („→ ease out“). Důkaz: celé video, 3 barvy + 2 druhy pilulek.
