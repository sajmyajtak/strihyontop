# Koncept B: „Rozkrojené logo“ (pracovně SLICED LOGO)

Autor: kreativní ředitel, 2026-10-30. Alternativa ke konceptu A (ubrus, fine dining) v `projekty/001-bb-chill/zadani.md`.
Z A převzato jen: fakta o značce (barvy, font, texty, logo, 13 vrcholů, dělicí přímka) a časy hudby.
Časy událostí hudby nejsou odhad: jsou přečtené z aranže `pohodova` v `nastroje/hudba.py` a ověřené měřením RMS `hudba.wav`
(drop 7,5 s = nejhlasitější místo −10 dB, nádech 6,875 s = −18,5 dB).

## Koncept jednou větou
**Bílý štítek z loga BB je postavička na obědové pauze: spolkne, co mu vykukuje ze švu, setřese ze sebe nápis, stane se bublinou
a kuchařskou čepicí, a na dropu prozradí pointu: logo se podél čáry mezi BAGETERIE a BOULEVARD rozkrojí jako bageta a uvnitř je Caprese.
Logo byla celou dobu bageta.**

## Spojovací prvek
1. **Jeden kus papíru**: bílý štítek (13 vrcholů ze `znacka.json`) je jediný polygon, který se celé video proměňuje
   (štítek → bublina → čepice → štítek → dvě půlky bagety → cedulka menu → zavřený sendvič → štítek). Nikdy nezmizí, nikdy se nestřihne.
2. **Šev** = dělicí přímka mezi slovy loga `(0; 32,0) → (101,584; 22,9)`. Je to řez bagety. Vrací se v každém aktu:
   vykukující náplň (0 s), spolknutí (0,6 s), pootevření v nádechu (7,19 s), rozkrojení na dropu (7,5 s), cedulka, která vypučí z horní půlky (10 s),
   zaklapnutí (13,75 s), náplň, co nevydrží uvnitř (15–16,9 s), prázdné půlky (18,1 s), poslední „mrknutí“ švu na zvukové logo (22,2 s).
3. **Řez jako jazyk typografie**: každý nadpis odchází tak, že se rozkrojí vodorovně (horní půlky písmen nahoru, spodní dolů)
   a nový nadpis vyroste z linie řezu. Stejné gesto jako štítek, jen v menším měřítku. Žádná prolínačka, žádné písmeno po písmenu.
4. **Vystřiženo stejnými nůžkami**: všechny tvary (štítek, bublina, čepice, plátky rajčat, mozzarella, rukola) jsou ploché papírové
   výstřižky s rovnými řezy a nepravidelnými úhly jako hrany loga. Ploché hnědé stíny papíru na stole. Vlastní, ruční, „ne-AI“ vzhled.

## Proč je to „wow“ (3 konkrétní momenty)
1. **0,625 s, háček: logo polkne.** Na snímku 0 vykukuje ze švu loga okraj rajčete a tři lístky rukoly. Na první lusknutí šev cvakne,
   náplň zmizí dovnitř a štítek se „nevinně“ zhoupne. Logo je živé a něco skrývá. Divák nedoscrolluje, chce vědět co.
2. **7,500 s, drop: logo se rozkrojí.** Po nádechu (logo je zase celé a stojí) se štítek podél švu rozletí na dvě půlky jako rozkrojená bageta:
   BAGETERIE nahoru, BOULEVARD dolů, mezi nimi vyskočí jako vystřihovánka celá Caprese v 6 vrstvách. Ve stejném snímku se stejným řezem
   rozkrojí nadpis NOT FAST FOOD. a z řezu vyroste EXPRESS GOURMET. **Aha: logo BB vždycky byla bageta.** (Pointa typu „šipka ve FedEx“, která se sdílí.)
3. **18,125 s, ALWAYS FAST: sendvič je pryč.** Náplň zmizí doprava za 3 snímky (jediný švih a šmouha ve videu), dvě prázdné půlky zůstanou
   zírat, otočí se k sobě („kde je?“) a na dobu cvaknou zpátky do čistého loga. Gag + doslovné „vždy rychle“ + návrat k logu v jednom gestu.

Drobné radosti mezi tím (každá na dobu): štítek setřese nápis a oklepe se jako pes (1,25–1,9 s), bublina NOT FAST FOOD. kroutí „hlavou“
(3,1–3,8 s), z bubliny se nafouknou tři obláčky kuchařské čepice a čepice se ukloní (4,4–5,9 s), nápis spadne zpátky přesně na marimbu (6,875 s),
cedulka menu mění šířku podle každé suroviny (10–13,1 s), čerstvá náplň nevydrží uvnitř a vykukuje (15–16,9 s), druhé „polknutí“ jako ozvěna háčku (16,875 s).

## Proč sedí ke značce a k pohodové hudbě
- **Tón značky** (bb.cz/o-nas: „Zábava, nadsázka a humor“): logo jako postavička, gagy bez slov, nadsázka „logo je bageta“.
- **Slogan je kostra příběhu**: před dropem (napětí vi–ii–V) zní NOT FAST FOOD. (co nejsme), drop na tónice = EXPRESS GOURMET. (co jsme),
  pak ALWAYS FRESH / ALWAYS FAST jako dvě scény a na end cardu celý slogan. Texty jen ze značky (C8), nic vymyšleného.
- **Značka v každém snímku**: svět je celou dobu žlutý #F0B600 (žádná barevná proměna, žlutá = BB), hrdina je bílý štítek loga, písmo hnědé.
  Barvy jídla jen na surovinách. Logo se nikdy nedeformuje: písmena se jen posouvají a otáčejí jako tuhý celek, štítek se na konci vrátí přesně na 13 vrcholů.
- **Pohoda, ne hype**: štítek se hýbe se swingem hudby (šestnáctiny o 60 ms později), na tlesknutí 2 a 4 se lehce pohupuje, žádné údery
  na každou dobu, jediný švih za celé video. Nádech před dropem je opravdové ticho v obraze. „Jako když jdeš na oběd“: postavička má pauzu, kouká, hraje si, jí.
- **Proč by B mohl porazit A**: pointa je o **vlastním logu značky** (nepřenosná, A je známý kouzelnický trik s ubrusem), hrdina s charakterem
  (humor, empatie), ruční papírový styl je nejdál od AI vzhledu, render je levný (ploché polygony, žádná látka). Slabina proti A: trik s ubrusem pochopí
  každý okamžitě, rozkrojení loga musí být inscenované naprosto čitelně (viz pasti).

## Vzhled

### Kompozice 9:16 (1080×1920, platí celé video, kamera shora na „stůl“)
| pás | y (px) | co v něm je |
|---|---|---|
| horní bezpečná zóna | 0–250 | žádný text ani hlavní obraz (projede jí jen písmo loga, když v 6,25 s padá shora zpátky) |
| **nadpisy** | 300–600 | jeden nadpis v jednu chvíli, střed x = 540, šířka ≤ 840 px (x 120–960); cedulka menu (10–13,75 s) |
| **hrdina** | 650–1450 | štítek / bublina / čepice / sendvič. Logo ve stavu loga: šířka 820 px (měřítko 8,07 → 820 × 420 px), střed (530; 1000) → x 120–940 |
| drobný text | 1260–1460 | jen na konci: bb.cz (y ≈ 1290), disclaimer (y ≈ 1430) |
| spodní zóna | 1520–1920 | **žádný text**. Smí jí jen proletět grafika: padající nápis loga (1,25–1,9 s), kapka balsamica (13,1 s) |
| pravá zóna | x 960–1080 | žádný text. Grafika smí (náplň odlétá doprava v 18,125 s) |

Rozkrojený sendvič (7,5–13,75 s), přepočteno z vrcholů a švu (šev leží 258 px pod horní hranou vlevo a 185 px vpravo): horní půlka y ≈ 610–900, náplň = šikmý pruh podél švu vysoký ~270 px (y ≈ 825–1170), spodní půlka y ≈ 1095–1330. Celý blok se vejde do pásu hrdiny, nadpis nad ním končí na y ≈ 480.

### Barvy (max 3 barvy + bílá, barvy jídla jen na surovinách)
| barva | HEX | role |
|---|---|---|
| žlutá BB | #F0B600 | pozadí, **celé video beze změny** (B nemá barevný převrat, drop nese tvar) |
| bílá štítku | #FEFEFE | hrdina: štítek a všechny jeho proměny, cedulka menu |
| hnědá | #5A3218 | písmo, písmena loga, ploché stíny papíru (krytí 18 %) |
| krémová | #F7F0EB | rub papíru (když se štítek ukloní nebo převrátí), lem mozzarelly a mascarpone, aby nesplynuly s bílou |
| jídlo | ze `znacka.json` | rajče #D7362A / dužina #E8574A, mozzarella #FBF7EE / #EAE3D3, rukola #5B7F2B / #3E5A1C, pesto #6E8A2A, balsamico #3A1F10, mascarpone #FFF8EC |

Žádné gradienty, záře, odlesky, zrno ani textura. Stín = kopie polygonu v hnědé 18 %, posun (6; 10) px v klidu, až (18; 28) px, když se papír zvedne.

### Papírový jazyk tvarů (tohle dělá B vlastním)
- Všechny obrysy jsou **polygony s rovnými řezy** (žádné hladké bézierky), úhly nepravidelné jako hrany loga. Obláčky čepice = 9–11úhelníky,
  plátek rajčete = 10úhelník s vnitřním 10úhelníkem dužiny a 6 trojúhelníkovými semínky, mozzarella = 7–8úhelníky, rukola = zubatý výstřižek
  (12–16 vrcholů), pesto = 6 malých 6úhelníků, balsamico = jediná křivka (tah, ne plocha).
- Proměna štítku zachovává **plochu ± 25 %** (je to pořád stejný kus papíru, ne nafukovací balónek).
- Postavička nemá oči ani pusu. Charakter dělá jen načasování: náklon, předskok, dosednutí, zpoždění vrstev, pohled = natočení k cíli.

### Písmo a velikosti (Big Shoulders, latin-ext, variabilní)
| prvek | řez | velikost | poznámka |
|---|---|---|---|
| nadpisy NOT FAST FOOD. / EXPRESS GOURMET. / ALWAYS FRESH / ALWAYS FAST | Display 900 | 116–130 px | **změřeno skutečným fontem** (Chromium, canvas): EXPRESS GOURMET. 118 px = 838 px (na hraně 840), proto **116 px = 823 px**; NOT FAST FOOD. 130 px = 751 px; ALWAYS FRESH 130 px = 705 px. ALWAYS FRESH / FAST bez tečky (E8), slogan s tečkami = pointa značky |
| text v bublině (2,5–3,75 s) | Display 900 | 112 px | ten samý objekt jako nadpis, jen se přesune do bubliny (647 px, bublina ~840 px) |
| cedulka menu (suroviny) | Display 900 | 88 px | změřeno: PESTO GENOVESE 545 px, ROCKET 245 px; cedulka mění šířku podle slova (okraj 60 px z každé strany) |
| bb.cz | Text 800 | 70 px | 146 px |
| disclaimer | Text 600 | 30 px | 540 px, krytí 80 % |
| logo | oficiální SVG (path2 + path4) | – | nikdy nepřepisovat fontem |

### Jazyk kamery a pohybu
- **Jedna kamera shora, žádný střih, žádný reset**: celé video jen pomalé dotlačení 1,00 → 1,09 stálou rychlostí v log měřítku
  (jako `kamera()` v kostře; je to jediný rovnoměrný pohyb ve videu a nikdy se nezastaví ani neotočí; 1,06 ve 22,5 s, 1,09 ve 25 s). Na dropu se kamera **nehne** (energii nese rozkrojení). Žádný zoom tam a zpátky, žádný třes.
- Pohyb: příchod ease-out, odchod ease-in, papír dosedá pružinou s překmitem 3 %, velké posuny kriticky tlumené. Postavička smí v gagu
  (oklepání 1,875 s, „ne“ 3,125 s, úklona 5,625 s) do 5° náklonu s rychle tlumeným doběhem, nikdy houpání.
- **Překrývání (follow-through)**: vrstvy náplně a obláčky čepice dobíhají se zpožděním 30–40 ms za sebou. To je hlavní zdroj „živosti“.
- **Swing**: pohupování na 2 a 4 (tlesknutí); drobnosti mezi dobami padají na liché šestnáctiny o 0,06 doby později, přesně jako swing hudby.
- **Logo je tuhé**: všechno, co nese písmo loga (logo, obě půlky), se jen posouvá, natáčí a stejnoměrně škáluje, **nikdy nestlačuje ani neroztahuje**.
  Stlačení a roztažení („squash & stretch“) jen u papíru bez písma: bublina, čepice, cedulka.
- Rozmazání pohybem jen podle rychlosti a směru: svislé na dropu (půlky), vodorovné při vytržení náplně (18,125 s). Render `--sub 8`.

## Storyboard po taktech
96 BPM, doba 0,625 s, takt 2,5 s, 10 taktů. Akordy: T1 Dm7 · T2 Gm9 · T3 C9 · **T4 Fmaj9 (drop)** · T5 Dm7 · T6 Gm9 · T7 C9 · T8 Fmaj9 · T9 Gm9 → C9 (21,25) · T10 Fmaj9.
H = hudba (už je v `hudba.wav`, časy z aranže), SFX = návrh jemného zvuku pro zvukaře (vrchol přesně na událost, tiše pod hudbou, papír a chléb, žádné whooshe kromě 18,125 s).
Opakující se doby v hudbě po dropu (od začátku taktu t0): kopák t0, +0,506, +1,563 (v T4, T6, T8 i +2,381) · malý buben + tlesknutí +0,625 a +1,875 ·
marimba t0, +0,506, +0,938, +1,875, +2,188 · kytara +0,938 a +2,188.

### Akt 1: postavička (T1–T3, 0–7,5 s, napětí vi–ii–V)
| čas (takt · doba) | obraz | text na obrazovce | zvuk / událost |
|---|---|---|---|
| **0,000** (T1 · 1) | **Snímek 0 = náhled**: žlutá plocha, uprostřed velké logo BB (820 px, střed 530; 1000) s plochým stínem. **Z konců švu mezi BAGETERIE a BOULEVARD trčí náplň**: vpravo okraj plátku rajčete (červený 10úhelník, ~140 px), vlevo tři zubaté špičky rukoly (~90 px). Štítek sám je celý a zavřený (pixelově SVG), náplň leží „uvnitř“ pod ním a přečnívá jen za jeho okraje. Logo je o 2° nakloněné „provinile“ | „NOT FAST FOOD.“ (Display 900, 130 px, y 360–490) | H: Rhodes Dm7 + marimba · SFX: nic |
| **0,625** (T1 · 2) | **HÁČEK, spolknutí**: šev cvakne (0,18 s, ease-in), rajče a rukola zajedou dovnitř (horní půlka je přikryje), štítek poskočí o 8 px nahoru a pružinou (3 %) dosedne, náklon 2° → 0° („nic jsem neudělal“); jen posun a náklon, logo se nedeformuje | drží | H: lusknutí · SFX: měkké „glp“ + papírové cvaknutí |
| 0,938 (T1 · 2&) | dozvuk: stín se přitáhne zpět (6; 10 px), štítek dosedne | drží | H: marimba |
| **1,250** (T1 · 3) | **štítek setřese nápis**: celé písmo loga (tuhý celek, obě slova) se zvedne o 6 px (předskok 0,12 s) a pak vyklouzne dolů ze štítku a padá ease-in mimo obraz (do 1,85 s, natočení +4°, beze změny tvaru). Zůstane **prázdný bílý štítek** | nadpis drží | SFX: papírové „šššk“ |
| 1,875 (T1 · 4) | prázdný štítek se **oklepe jako pes**: náklon −4°, +3°, −1,5°, 0° za 0,45 s, kriticky tlumený doběh; stín se při tom trochu posouvá | drží | H: lusknutí · SFX: třepot papíru |
| **2,500** (T2 · 1) | **štítek → bublina**: dolní levý roh (vrchol 8) se vytáhne do ostrého ocásku doleva dolů, ostatní vrcholy se rozjedou do mírně širší bubliny (pořád rovné řezy). Nadpis NOT FAST FOOD. **sjede z horního pásu do bubliny** (sdílený prvek, 130 → 112 px, ease-out 0,4 s) | „NOT FAST FOOD.“ v bublině | H: Rhodes Gm9 + marimba · SFX: měkké „pop“ |
| 3,125 (T2 · 2) | bublina **kroutí hlavou**: náklon −5° (ease-out 0,15 s) | v bublině | H: lusknutí · SFX: tik |
| 3,438 (T2 · 2&) | … a na druhou stranu +5° | v bublině | H: marimba |
| **3,750** (T2 · 3) | bublina se srovná (pružina 3 %) a **vyplivne nadpis** zpět do horního pásu (ease-out 0,3 s, 112 → 130 px); ocásek zajede zpátky | „NOT FAST FOOD.“ nahoře | SFX: „pff“ papíru |
| 4,375 (T2 · 4) | horní hrana se začne **nafukovat**: vyboulí se první obláček (10úhelník roste z hrany) | drží | H: lusknutí · SFX: nádech „fff“ |
| **5,000** (T3 · 1) | **kuchařská čepice**: tři obláčky (9–11úhelníky) dorostou s rozestupem 40 ms, spodní pruh štítku zůstane jako páska čepice. Celá čepice +4 % a dosedne | drží | H: Rhodes C9, jemný kopák, marimba · SFX: „pomf“ |
| 5,625 (T3 · 2) | čepice se **ukloní** (náklon −8° a zpět, ukáže krémový rub papíru), obláčky dobíhají se zpožděním | drží | H: lusknutí · SFX: tichý třepot |
| 5,938 (T3 · 2&) | obláčky se jeden po druhém usadí (follow-through) | drží | H: marimba |
| **6,250** (T3 · 3) | **čepice splaskne** (obláčky se zatáhnou do hrany, ease-in 0,3 s) zpět přesně na 13 vrcholů štítku. Shora z obrazu padá **nápis loga** zpátky (tuhý celek) | drží | H: Rhodes, jemný kopák, začíná stoupající šum · SFX: „fffp“ vyfouknutí |
| **6,875** (T3 · 4) | **nápis dopadne přesně do štítku** = logo je celé a přesné podle SVG (dopad = celé logo klesne o 6 px a pružinou dosedne, od 7,03 s v klidu). **Nádech: všechno stojí** | „NOT FAST FOOD.“ drží (v tichu je co číst: nadpis + celé logo) | H: marimba A5, pak ticho + šum · SFX: měkké ťuknutí dopadu |
| 7,188 | šev se **pootevře o 2 px** (proužek červené) a hned zavře; stín se přitáhne (logo se „přikrčí“ = předskok) | drží | H: marimba G5 |

### Akt 2: rozkrojení a servírování (T4–T6, 7,5–15 s, drop na tónice)
| čas (takt · doba) | obraz | text na obrazovce | zvuk / událost |
|---|---|---|---|
| **7,500** (T4 · 1) **DROP** | **ROZKROJENÍ LOGA** (nejsilnější moment): štítek se podél švu rozletí na dvě půlky. Horní (BAGETERIE) vyskočí o 150 px a natočí se o −4°, spodní (BOULEVARD) klesne o 120 px a +2° (mezera ~270 px), obě pružinou 3 % (dosednou do 0,5 s). Písmena jedou s půlkami jako tuhé celky. **Mezi nimi se jako vystřihovánka z rozkládací knížky postaví Caprese v 6 vrstvách** (každá vrstva vyroste ze sklopení naplocho, odspodu nahoru po 30 ms): mascarpone (vlnitý krémový pruh), mozzarella (4 kusy), rajčata (4 plátky), pesto (6 teček), rukola (7 lístků přesahuje přes okraje). Stíny půlek odskočí na (18; 28) px. Svislá šmouha jen na půlkách podle rychlosti | **Stejný řez v nadpisu**: NOT FAST FOOD. se rozkrojí vodorovně (horní půlky písmen nahoru, spodní dolů, ease-in 0,25 s) a z linie řezu vyroste **„EXPRESS GOURMET.“** (116 px, maska se otevře od řezu nahoru i dolů, ease-out 0,35 s) | H: **drop Fmaj9**, kopák, činel, plná drážka, marimba C5 · SFX: křupnutí kůrky (vrchol přesně 7,50) + trhnutí papíru + 6 tichých papírových „pop“ po 30 ms |
| 8,125 (T4 · 2) | náplň se usadí: lístky rukoly dopadnou se zpožděním 40 ms za sebou, plátky rajčat se srovnají; půlky doznívají | „EXPRESS GOURMET.“ drží (čte se do 9,9 s) | H: tlesknutí · SFX: tiché ťukání papíru |
| 8,750 (T4 · 3) | **balsamico**: tenká tmavá klikatá čára se nakreslí přes náplň (stroke-dashoffset, 0,35 s, ease-out) | drží | H: hi-hat (tichá doba), Rhodes + kopák v 9,06 · SFX: tenké „sss“ |
| 9,375 (T4 · 4) | celý otevřený sendvič se **jednou pohoupne** do rytmu (dolů 10 px na tlesknutí a zpět), vrstvy jdou za ním s rozestupem 35 ms (jemná vlna, ne želé) | drží | H: tlesknutí, marimba F5 E5 |
| **10,000** (T5 · 1) | **cedulka menu**: z horní hrany horní půlky se podél řezu **oddělí malý bílý štítek** (silueta štítku loga, výška 220 px, šířka podle slova 400–665 px; je to dítě hrdiny, ne logo, takže se smí roztahovat) a vyplave do pásu nadpisů (střed y ≈ 440, spodní hrana ≈ 550, nad horní půlkou). Vrstva mascarpone povyskočí o 16 px a dosedne | EXPRESS GOURMET. se rozkrojí a odjede (0,25 s), v cedulce vyroste ze švu **„MASCARPONE“** (88 px) | H: Dm7, kopák, marimba D5 · SFX: odlepení papíru „tsk“ |
| 10,625 (T5 · 2) | cedulka změní šířku podle slova (pružina 3 %) a kývne o +2°; povyskočí mozzarella | „MOZZARELLA“ (staré slovo odjede horní hranou cedulky 0,12 s ease-in, nové přijede zespodu 0,2 s ease-out, vlastní maska) | H: tlesknutí · SFX: tik |
| 11,250 (T5 · 3) | cedulka kývne o −2°; plátky rajčat povyskočí a každý se pootočí o 10° | „TOMATOES“ | H: tichá doba (hi-hat) · SFX: tik |
| 11,875 (T5 · 4) | cedulka se roztáhne na nejširší slovo (545 px textu + okraje ≈ 665 px, pořád ≤ 840); 6 teček pesta naskočí po 40 ms | „PESTO GENOVESE“ | H: tlesknutí, marimba G5 · SFX: 6 drobných ťuků |
| **12,500** (T6 · 1) | lístky rukoly **cvrnknou nahoru** (+12°, dosednou), čerstvé | „ROCKET“ | H: Gm9, kopák, marimba D5 · SFX: šustnutí |
| 13,125 (T6 · 2) | z konce čáry balsamica se utvoří **kapka**, steče přes spodní okraj sendviče a spadne spodní zónou z obrazu (ease-in) | „BALSAMIC“ | H: tlesknutí · SFX: „plink“ |
| **13,750** (T6 · 3) | cedulka slétne dolů a **zacvakne zpět do horní půlky** (spojí se podél řezu, sdílený prvek). Horní půlka sjede a **zaklapne sendvič**: spodní půlka pod tím klesne o 6 px a dosedne (jen posun). Zavřený „logo-sendvič“: bílá, barevný pruh náplně 110 px, bílá; BAGETERIE / BOULEVARD čitelné | text odjede s cedulkou (ve chvíli spojení už žádný) | H: tichá doba, kopák v 14,06 · SFX: měkké „bum“ chleba |
| 14,375 (T6 · 4) | usazení; vpravo ze švu vykoukne špička rukoly a zhoupne se | – (pohyb pokračuje, pauza bez textu 1,25 s) | H: tlesknutí, kytara, otevřený hi-hat 14,69 |

### Akt 3: vždy čerstvé, vždy rychlé, návrat k logu (T7–T9, 15–22,5 s)
| čas (takt · doba) | obraz | text na obrazovce | zvuk / událost |
|---|---|---|---|
| **15,000** (T7 · 1) | čerstvá náplň **nevydrží uvnitř**: vpravo ze švu vyjede lístek rukoly a zhoupne se | **„ALWAYS FRESH“** vyroste z linie řezu (130 px, y 360–490) | H: C9, kopák, marimba E5 · SFX: šustnutí |
| 15,625 (T7 · 2) | vlevo vyklouzne okraj plátku rajčete | drží | H: tlesknutí · SFX: měkké klouznutí |
| 16,250 (T7 · 3) | pod rukolou vykoukne kousek mozzarelly | drží | H: tichá doba (hi-hat) · SFX: tik |
| 16,875 (T7 · 4) | **druhé polknutí** (ozvěna háčku): všechno naráz zajede dovnitř, sendvič cukne o 6 px | drží | H: tlesknutí, marimba A5 · SFX: stejné „glp“ jako v 0,625 |
| **17,500** (T8 · 1) | pruh náplně se posune o 8 px doleva (nápřah, předskok k vytržení) | ALWAYS FRESH se rozkrojí, z řezu vyroste **„ALWAYS FAST“** | H: Fmaj9, kopák, marimba C5 |
| **18,125** (T8 · 2) | **VYTRŽENÍ** (jediný švih ve videu): celá náplň vystřelí doprava za 3 snímky (ease-in, vodorovná šmouha jen na náplni, zmizí za pravým okrajem). Půlky zůstanou s prázdnou mezerou 110 px, horní sebou trhne o 10 px | drží | H: tlesknutí · SFX: krátké „zip“ 150 ms, vrchol v 18,15 |
| 18,750 (T8 · 3) | prázdné půlky se **natočí k sobě** (horní −6°, spodní +4°): „kde je?“ Jediná doba úplného klidu v aktu, stín ukazuje prázdnou mezeru | drží | H: tichá doba · SFX: nic (ticho je gag) |
| 19,375 (T8 · 4) | půlky **cvaknou k sobě**: čisté logo přesně podle SVG (13 vrcholů, písmena beze změny), poskok o 6 px a dosednutí | drží | H: tlesknutí, marimba F5 · SFX: suché papírové „cvak“ |
| **20,000** (T9 · 1) | logo se jedním pohybem přesune do polohy end cardu: střed (530; 1000) → (530; 960), měřítko 1,00 → 0,92 (0,6 s, ease-in-out, kriticky tlumené) | ALWAYS FAST se rozkrojí a odjede | H: Gm9, kopák, marimba B5 (b) |
| 20,625 (T9 · 2) | logo dosedne | **„NOT FAST FOOD.“** vyroste z linie řezu (116 px, y 330–450), ozvěna snímku 0 | H: tlesknutí (marimba A5 o 0,12 s dřív, 20,51) |
| **21,250** (T9 · 3) | – (logo v klidu, kamera dotlačuje) | **„EXPRESS GOURMET.“** (116 px) vyroste pod ním (y 470–590), slogan je celý | H: změna na C9, marimba E5 |
| 21,875 (T9 · 4) | pod logem se ze spodní hrany štítku vysune text (maska na hraně loga) | **„bb.cz“** (Text 800, 70 px, y ≈ 1290) | H: tlesknutí |
| 22,188 / 22,344 | **šev mrkne**: půlky se na tónech C5 a F5 rozestoupí o 2 px a hned zavřou (v 22,5 je logo zase přesné) | drží | H: zvukové logo marimby C5, F5 |
| **22,500–25,000** (T10) **END CARD** | na poslední tón A5 logo jemně „pípne“ (+3 % pružinou) a dosedne. Nahoře slogan, uprostřed logo, pod ním bb.cz, disclaimer. Drží 2,5 s, kamera dál dotlačuje 1,06 → 1,09, nic dalšího se nehýbe (žádný zamrzlý snímek) | „NOT FAST FOOD. / EXPRESS GOURMET.“ + logo + „bb.cz“ + **„Concept ad · not affiliated with Bageterie Boulevard“** (Text 600, 30 px, krytí 80 %, y ≈ 1430, najede eased 0,4 s v 22,5) | H: A5 přesně v 22,50, finální Fmaj9 + kopák + tlesknutí + jemný činel, doznění do 25,0 |
| 23,125 / 23,750 / 24,375 | end card drží (C6: na end cardu se nová událost nepřidává) | drží | H: doznívání |

**Texty ve videu (všechny doslova ze značky)**: NOT FAST FOOD. · EXPRESS GOURMET. · ALWAYS FRESH · ALWAYS FAST · MASCARPONE · MOZZARELLA · TOMATOES ·
PESTO GENOVESE · ROCKET · BALSAMIC · bb.cz · disclaimer. Žádná čísla, ceny ani jiná tvrzení. V jednu chvíli na obrazovce jen jeden nadpis.
„Fine dining without the white tablecloths“ záměrně **nepoužívám** (patří ke konceptu A).

## Kontrolní snímky před plným renderem
`node nastroje/render_html.cjs … --nahled casy --casy 0,0.72,1.6,2.9,3.2,5.1,6.9,7.56,7.62,8.4,10.3,11.9,13.9,15.7,18.13,18.17,18.9,19.6,21.4,23.5`
+ snímek na každou dobu (`--nahled doby --bpm 96`).
| čas | co musí být vidět | odmítnout, když |
|---|---|---|
| 0,0 | náhled: logo + vykukující rajče a rukola + NOT FAST FOOD. | náplň je tak malá, že na telefonu nejde poznat jídlo |
| 0,72 | uprostřed spolknutí | logo se jakkoli deformuje (povolen jen posun a náklon), náplň pod štítkem je vidět skrz |
| 1,6 | písmo loga padá jako tuhý celek, štítek prázdný | písmena se rozpadají nebo mění tvar |
| 2,9 / 3,2 | bublina s textem, náklon „ne“ | text přetéká z bubliny, ocásek se kříží s obrysem |
| 5,1 | čepice (3 obláčky + páska) | je to „mrak“, ne čepice; obrys se sám protíná |
| 6,9 | **logo přesně podle SVG** (překrýt `logo_bb_full_2000.png` s průhledností) | posun > 1 px, jiný tvar |
| 7,56 / 7,62 | rozkrojení: půlky v letu, náplň se staví, nadpis rozkrojený | šmouha smaže písmena loga, náplň vypadá jako výbuch částic |
| 8,4 | **klíčový snímek konceptu**: otevřený logo-sendvič + EXPRESS GOURMET. | nečitelné jako bageta / sendvič, přeplněné |
| 10,3 / 11,9 | cedulka MASCARPONE / PESTO GENOVESE | cedulka v bezpečné zóně, text se překrývá se starým slovem |
| 13,9 | zavřený logo-sendvič | BAGETERIE / BOULEVARD nečitelné |
| 15,7 | ALWAYS FRESH + vykukující náplň | – |
| 18,13 / 18,17 | vytržení (2 snímky) | duchové místo šmouhy, náplň je v půlce obrazu ještě ostrá |
| 18,9 | prázdné půlky natočené k sobě | gag nejde poznat bez zvuku |
| 19,6 | čisté logo | jakákoli odchylka od SVG |
| 21,4 / 23,5 | slogan / end card | text v bezpečné zóně, end card přeplněný |

## Stavba (pro animátora)
- Jedna scéna z `nastroje/vzory/scena.html`, 1080×1920, vše z času ve `window.seek(t)`. Nahoře `CASY` v dobách (`d(n) = n · 0,625`) a `TEXTY`.
- **Motor proměn**: každý stav štítku = obrys o **N = 120 bodech** se stejným pořadím (po směru hodinových ručiček v SVG) a stejným počátkem
  (vrchol 1 = 84,003; 0). 13 vrcholů loga má **pevné indexy**, mezi nimi body na přímkách, takže stav „logo“ je přesně původní polygon.
  Stavy: logo, bublina, čepice, horní půlka, spodní půlka (pro rozkrojení se obrys rozdělí přímkou švu na dva polygony po 60 bodech), cedulka.
  Přechod = interpolace bodů s **rozjezdem po obrysu** (vedoucí hrana o 40–60 ms dřív, trik „dvě hrany na dvou pružinách“ z `twoclipping-5cba86`),
  ne lineární prolnutí všech bodů naráz.
- Ve stavu loga (0–1,25 s, 6,875–7,5 s, 19,375–25 s) se místo 120bodového polygonu kreslí **originální `path2` a `path4` ze SVG** (pixelově přesné logo).
- Písmo loga = `path4` dvakrát, ořezané polorovinou podle švu (`clipPath`): BAGETERIE nad, BOULEVARD pod. Jen `translate` + `rotate` + stejnoměrné `scale`.
- Nadpisy: rozkrojení = dvě kopie textu s `clip-path: inset(…)` (horní a spodní polovina, překryv 1 px), příchod = maska otevřená od linie řezu.
- Jídlo: SVG polygony z tabulek bodů (rukola tvarově z `nahoda(seed)`), stíny = posunutá kopie v #5A3218 18 %, žádné SVG filtry kromě jednoho
  směrového rozmazání (`rozmazani()` z kostry) na dropu (půlky, svisle) a v 18,125 s (náplň, vodorovně).
- Fonty: `FONTY = ['900 130px "Big Shoulders Display"', '900 88px "Big Shoulders Display"', '800 70px "Big Shoulders Text"', '600 30px "Big Shoulders Text"']`.
- Render: `--fps 60 --sub 8 --dur 25` (kvůli dropu a vytržení). Odhad: ~32 s výpočtu na 1 s videa → **~13–14 min**.
- Vzory z prompt-motion: `twoclipping-5cba86` (jeden tvar bez střihu, text v měnícím se kontejneru má vlastní časování, rozjezd hran),
  `ultimaxbt-bbebf5` (jeden prvek spojuje všechny scény a vrací se na end card, oddělené časy odcházejícího a příchozího textu),
  `tdinh-me-815acb` (logo se nejdřív poskládá, pak odhalí), `ultimaxbt-2ddf1e` (jeden záběr, SFX podle změřeného vrcholu).

## Pasti stavby (co se může pokazit a jak tomu předejít)
1. **Morf se „rozteče“ nebo zkroutí** (body se při interpolaci prohodí, obrys se protne). Prevence: stejný počet bodů, stejný počátek a směr,
   ruční mezistavy u bubliny a čepice, kontrola obrysů v 25 / 50 / 75 % každého morfu (vykreslit obrys červeně v režimu `?debug`).
2. **Logo není přesné** na 6,875 s, 19,375 s a na end cardu. Prevence: v klidových úsecích kreslit originální SVG, ne interpolovaný polygon;
   kontrola překrytím s `logo_bb_full_2000.png`.
3. **Řez uřízne kus písmena**: dělicí přímka má vlevo rezervu jen ~0,2 jednotky viewBoxu. Prevence: oříznutí polorovinou přesně podle `znacka.json`,
   kontrola zvětšeniny levého konce (jako `logo_kontrola_deleni_vlevo.jpg`).
4. **Bílá na bílé**: mozzarella a mascarpone mezi bílými půlkami splynou. Prevence: krémový lem #F7F0EB / #EAE3D3 a vlastní plochý stín každé vrstvy.
5. **„Výbuch částic“ místo vystřihovánky**: vrstvy náplně se musí stavět z jedné roviny (sklopení), ne vyletět z bodu. Žádné drobky ani jiskry.
6. **Rozkrojený nadpis má mezeru nebo dvojitou hranu**: obě kopie stejný font, stejný `top`, překryv 1 px, celé pixely.
7. **Duchové při vytržení**: náplň musí odjet do 3–4 snímků celá za pravý okraj, šmouha podle rychlosti, `--sub 8`. Kdyby i tak byly duchy,
   prodloužit vytržení na 5 snímků, ne zesílit rozmazání.
8. **Charakter přejde v laciné houpání**: oklepání a „ne“ max 5°, doběh kriticky tlumený, každý gag na jednu dobu. Mimo gagy jen pružina 3 %.
9. **Pohyb bez příčiny**: písmo loga odchází dolů a vrací se shora (vidíme, kudy jde), cedulka vypučí z horní půlky a do ní se vrátí,
   náplň odchází na stranu, kam ji „vzal zákazník“. Nic se neobjeví ani nezmizí prolnutím.
10. **Text v zónách**: EXPRESS GOURMET. nejvýš 116 px (při 118 px je na hraně pravé zóny), cedulka nejširší (PESTO GENOVESE) ≈ 665 px; bb.cz a disclaimer nad y 1520; nic za x 960.
11. **Fonty**: načíst přes `document.fonts.load` před `seek(0)` (C016), jinak se rozkrojení měří na záložním písmu.
12. Žádné `will-change` na prvcích, které kamera škáluje (C004). Náhoda jen `nahoda(seed)`.
13. **Logo se nestlačuje**: prvky s písmem loga jen `translate` / `rotate` / stejnoměrné `scale`. Kritik kontroluje snímky dopadů (0,7 / 6,95 / 13,8 / 19,45 s).

## Rizika proveditelnosti v HTML na CPU (upřímně)
| riziko | pravděpodobnost | dopad | co s tím |
|---|---|---|---|
| **Kvalita morfů** (bublina, čepice, cedulka). Interpolace polygonů vypadá snadno „rozteklá“ a laciná, to je nejčastější znak šablonového shape-morph videa | vysoká | velký: celé video stojí na tom, že proměny jsou krásné | každý morf ručně navržený se 2–3 mezistavy a rozjezdem po obrysu; nejdřív postavit **jen morf štítek → čepice → štítek** a schválit ho na 12 snímcích, pak teprve zbytek |
| **Jídlo z papírových výstřižků vypadá jako klipart** | střední | velký na „wow“ i chuť | držet jeden jazyk (rovné řezy, 2 tóny na surovinu, plochý stín), postavit a schválit snímek 8,4 s jako první klíčový snímek před animací |
| **Pointa rozkrojení nemusí být bez zvuku a napoprvé čitelná** (divák uvidí „logo se rozpadlo“, ne „logo je bageta“) | střední | velký (je to drop) | půlky se rozestoupí jen o ~270 px a zůstanou rovnoběžné jako krajíce, náplň přesahuje přes okraje jako na fotkách bb.cz, rukola trčí ven; text EXPRESS GOURMET. přijde ve stejném snímku; ověřit na náhledu 8,4 s „testem 1 sekundy“ |
| Rozkrojení loga a „mrknutí“ švu v 22,2 s může značka brát jako zásah do loga | nízká (spec reklama) | střední | tvar ani písmena se nikdy nedeformují, jen se rozestoupí podél existující hranice slov; end card je pixelově přesné SVG. Otázka pro režiséra níž |
| Render: 1 500 snímků × 8 podsnímků | jistota | čas | ~13–14 min na 4 CPU (měřeno 16 s/s při `--sub 4`). Polygonů je ve scéně max ~60, žádné filtry kromě dvou směrových rozmazání, takže snímek je levný |
| Směrová šmouha přes SVG `feGaussianBlur` na skupině s mnoha polygony | nízká | malý | jen ve 2 úsecích po ~0,3 s; když bude pomalá, rasterizovat náplň do `<canvas>` a rozmazat jen ten |
| Swing a „charakter“ jsou jemné a na náhledech po dobách nejsou vidět | střední | střední | kritik kontroluje i pásy sousedních snímků u gagů 0,625 / 1,875 / 3,125 / 18,125 s |
| Délka stavby: B je náročnější na ruční návrh tvarů než A (8 stavů tvaru + 6 surovin) | jistota | čas animátora | odhad o ~30 % víc práce než A. Jde zjednodušit vynecháním bubliny (2,5–4,4 s): štítek rovnou nafoukne čepici a NOT FAST FOOD. zůstane nahoře |

**Co v HTML jde bez problému**: polygony v SVG, ořezy polorovinou, rozkrojení textu přes `clip-path`, pružiny v uzavřeném tvaru, stíny jako kopie,
stroke-dashoffset čáry balsamica, směrové rozmazání. Žádné 3D, žádná fyzika látky, žádné obrázky, žádné WebGL.

## Otázky pro režiséra
1. Snímek 0 je logo s vykukující náplní a nadpisem. Je to podle B6 přijatelné (není to „úvodní logo“, je to záhada), nebo chceš náhled bez loga?
2. Smí se logo během filmu rozkrojit podél hranice slov (tvar ani písmena se nedeformují, na konci přesné SVG)?
3. ALWAYS FRESH / ALWAYS FAST používá i A. Nechat v B (jinak inscenované), nebo T7–T8 postavit jen na gagu bez textu?
4. SFX (papír, křupnutí kůrky, „zip“): máme knihovnu s licencí, nebo je syntetizovat v kódu (I5)?
