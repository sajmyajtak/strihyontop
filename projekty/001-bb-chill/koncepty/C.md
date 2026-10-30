# Koncept C: „GROOVE: The Caprese Session“

**Koncept jednou větou**: Každá surovina bagety Caprese je jeden nástroj pohodové skladby a hýbe se přesně ve chvíli, kdy ten nástroj
v `hudba.wav` opravdu hraje (rajče = marimba, mozzarella = Rhodes, pesto = shaker, rukola = kytara, balsamico = basa); rozevřená bageta
na tmavě hnědé „zvukové zkoušce“ sbírá kapelu nástroj po nástroji, na dropu se vrchní půlka překlopí a zaklapne přesně na první kopák,
z bagety vytryskne žlutá a celý svět BB (text, bageta, náplň) se rozhoupe v jedné drážce se swingem, až se bageta na konci znovu otevře
a její dvě půlky se stanou dvěma pruhy bílého štítku loga.

**Spojovací prvek**: **bageta = dvě půlky = dva pruhy štítku loga BB.** Bílý štítek loga je složený ze dvou nakloněných, posunutých pruhů
(`logo_arch.png`, dělicí přímka v `znacka.json`). Rozevřená bageta shora jsou přesně dva dlouhé světlé pruhy střídy. Snímek 0 ukazuje
siluetu štítku BB složenou z chleba, konec ukazuje skutečný štítek složený z téže bagety. Mezi tím je bageta „takt“: její čtyři šikmé
zářezy na kůrce jsou čtyři doby a nese celou choreografii. Smyčka (D4): poslední snímek má štítek ve stejné poloze a úhlu jako bageta ve snímku 0.

**Gramatika groove** (pravidlo pro animátora, z něj vychází každý pohyb): nic se nehýbe „na každou dobu stejně“ (zakázané beat-snapped slams,
poznatky odd. 4). Každý prvek poslouchá **jen svůj nástroj** a jeho skutečné časy z `nastroje/hudba.py` (nálada `pohodova`, viz tabulka
v oddílu Storyboard). Lichá šestnáctina je zpožděná o swing **+0,06 doby = +37,5 ms** stejně jako v hudbě. Kývnutí hlavou (nod) jen na
2 a 4 (malý buben + tlesknutí, +12 ms). Pohyb typu „tanec“ je vždy tuhá transformace (posun, natočení ≤ 4°, měřítko ≤ 3 %), nikdy
gumová deformace, žádné obličeje ani ruce: elegance motion designu, ne kreslený film.

## Proč „wow“ (3 momenty)
1. **Snímek 0 → 0,94 s: „to je logo… ne, to je bageta“.** Na tmavě hnědé leží dva světlé, šikmé, posunuté pruhy přesně v rozložení
   štítku BB (bez písmen). V 0,0 s na marimbu dopadne první plátek rajčete, na lusknutí v 0,625 s se pruhy ve 3D lehce pootočí kolem
   podélné osy a ukáže se kůrka: jsou to dvě půlky rozevřené bagety. Druhý tón marimby (0,94 s) = druhé rajče. Háček obrazem do 1 s
   a zároveň značka v 1. snímku, aniž by tam bylo logo.
2. **Drop 7,5 s: zaklapnutí + výron žluté + svět se rozjede.** Vrchní půlka visí během nádechu (7,19–7,5) ve vzduchu otevřená na 150°,
   v 7,5 s se dopne kolem pantu (rotateX, ease-in až do nárazu) a zaklapne **přesně na kopák a činel**. Z místa nárazu se rozjede žlutá
   #F0B600 ve tvaru siluety bagety a za 0,33 s pokryje všechny 4 rohy (zaplavení barvou z objektu, D2). Současně se text převrátí
   ze žlutého na hnědý a nastoupí „NOT FAST FOOD.“; od této chvíle se všechno houpe: na dropu písničky, která je schválně pomalá,
   říká značka „ne fast food“ (vtip v duchu „Zábava, nadsázka a humor“).
3. **Taneční vsuvka 15,0–17,5 s „ALWAYS FAST“ + konec na zvukové logo.** Celé video je laid-back, jen v taktu 7 se na slovo FAST
   bageta s textem na dvě doby „rozběhne“ do dvojnásobného tempa (dva krokové posuny na každou šestnáctinu hi-hatu) a hned se vrátí
   do pohody: vizuální vtip na slovo. Na konci (20,0–22,5) se bageta znovu otevře, půlky se natočí do úhlů štítku, střída zbělá
   na #FEFEFE a slova BAGETERIE / BOULEVARD dopadnou na poslední dva tóny zvukového loga (F5 22,34 s, A5 **22,50 s**).

## Proč sedí ke značce a k pohodové hudbě
- **Tón značky** („Zábava, nadsázka a humor“, bb.cz/o-nas): kapela ze surovin, drop na „NOT FAST FOOD.“ při 96 BPM, zrychlení na slovo FAST.
  Humor nese načasování, ne kreslené postavičky.
- **Pohoda „jako když jdeš na jídlo“**: tempo pohybu se řídí hudbou, ne střihem. Žádný švih, žádný třes, žádný zoom. Swing a kývnutí
  na 2 a 4 je přesně ta uvolněná fyzická reakce, kterou dělá člověk, když mu hraje dobrá písnička. Kontrast tmavá „zkouška“ → žlutý svět
  je uvolnění napětí obratu vi–ii–V do toniky Fmaj9 (hudba to tak už má).
- **Značka v každém snímku**: žlutá #F0B600 a hnědá #5A3218 jsou jediné plochy (krém a bílá jen na chlebu a štítku), písmo Big Shoulders
  (náhrada fontu webu), siluety a finálně skutečný štítek loga. Varianta loga na hnědém existuje i na webu (`logo_arch.png`), takže tmavý úvod je „on brand“.
- **Jiné než koncept A**: žádný ubrus, žádný poklop, žádný fine dining jako příběh, žádná proměna řezu písma 200 → 900 na dropu
  (C mění barvu a pohyb, ne řez). Společná zůstává jen fakta značky a časování hudby.

## Vzhled
**Kompozice 9:16** (1080×1920, souřadnice snímku; bezpečné zóny: y < 250, y > 1520 a x > 960 bez textu):
| pás | y | obsah |
|---|---|---|
| horní okraj | 0–250 | jen pozadí (a přesah žluté při výronu) |
| **nadpis** | 290–640 | 1–2 řádky hesla, zarovnání vlevo na x = 90, pravý okraj textu ≤ 940 |
| **bageta** | 690–1290 | bageta délky ~860 px, střed (515, 990), natočená **−6°** (stoupá doprava jako štítek loga); stín plochý dolů o 14 px |
| **tracklist** | 1330–1500 | v úvodu řádek názvu suroviny, po dropu volný (jen pohyb náplně přesahuje do 1330) |
| spodní okraj | 1520–1920 | bez textu, jen pozadí |
Bageta je posunutá o 25 px doleva od středu (aby pravých 120 px zůstalo vzdušných) a je vždy hlavní objekt; text ji nikdy nepřekrývá.

**Barvy** (role, max 3 + bílá):
- úvod 0–7,5 s: pozadí **hnědá #5A3218**, text **žlutá #F0B600**, chleba střída #F3E3C3 / kůrka #D08B3A, stín #A8601E, zářez #EBC27E
  (stín na hnědé = #491B13 s krytím 60 %, plochý)
- od dropu: pozadí **žlutá #F0B600**, text **hnědá #5A3218**, stín hnědá 18 %
- štítek loga **#FEFEFE**, písmena loga #5A3218; krémová #F7F0EB jen jako stín na mozzarelle a mascarpone
- barvy jídla jen na surovinách (výjimka G1 schválená v zadání): rajče #D7362A / #E8574A, mozzarella #FBF7EE / #EAE3D3,
  rukola #5B7F2B / #3E5A1C, pesto #6E8A2A, balsamico #3A1F10, mascarpone #FFF8EC
- žádné gradienty, záře, odlesky, zrno ani vinětace

**Písmo** (jedna rodina, E4):
- nadpisy **Big Shoulders Display 900**, verzálky, prostrkání 0, řádkování 0,92: „NOT FAST FOOD.“ 150 px, „EXPRESS GOURMET.“ 116 px
  (max šířka 850 px, měřit `getBBox` po načtení fontu a zmenšit, kdyby přesáhla), „ALWAYS FRESH.“ / „ALWAYS FAST.“ 140 px
- úvodní tracklist **Big Shoulders Display 700**, 64 px, prostrkání 0,12 em, žlutá na hnědé (jedna surovina naráz, ne seznam)
- end card bb.cz **Big Shoulders Text 800** 70 px, disclaimer **Big Shoulders Text 600** 30 px, krytí 80 %
- tečky na konci jen u sloganu značky (je to její doslovný text a pointa), ostatní řádky bez tečky (E8): „ALWAYS FRESH“ / „ALWAYS FAST“
- text se nikdy nerozpadá na písmena ani slova (E1, odd. 4): každý řádek je jeden objekt, vjíždí z maskovací linky a houpe se jako celek

**Jazyk kamery** (F7): **kamera stojí.** Shora (top-down) jako produktové fotky bb.cz, bez zoomu a bez posunu po celé video.
Groove nesou objekty, ne kamera (kamera, která by pulzovala do rytmu, = zakázaný zoom tam a zpět). Jediná 3D věc je pant bagety
(rotateX kolem podélné osy, perspektiva 1800 px, jen na bagetě) a lehké náklony kůrky. Jediný rychlý pohyb s rozmazáním = zaklapnutí v 7,5 s.

**Choreografie: kdo poslouchá který nástroj** (časy jsou spočítané z `nastroje/hudba.py` pro náladu `pohodova`, t0 = začátek taktu,
doba 0,625 s, swing lichých šestnáctin +37,5 ms; animátor je načte ze stejného vzorce, ne ručně):
| prvek | nástroj | úvod T1–T2 (t0 = 0; 2,5) | T3 nádech (t0 = 5) | hlavní část T4–T8 (t0 = 7,5 … 17,5) |
|---|---|---|---|---|
| plátky rajčete | marimba | t0, t0 + 0,9375 | 5,0; 5,9375; předtakt 6,875; 7,1875 | t0, +0,50625, +0,9375, +1,875, +2,1875 |
| mozzarella | Rhodes | t0, t0 + 1,5625 | 5,0; 6,25 | t0, +0,9375, +1,5625, +2,38125 |
| pesto (tečky) | shaker / hi-hat | šestnáctiny s swingem | šestnáctiny do 6,756 | jen při nástupu, pak klid (jinak blikání) |
| rukola | lusknutí → kytara | lusknutí t0 + 0,625, t0 + 1,875 | 5,625 | kytara t0 + 0,9375, t0 + 2,1875 |
| balsamico | basa | (není) | (není) | t0, +1,13125, +1,5625, +2,1875 |
| kůrka bagety (4 zářezy) | kopák | (není) | kopák 5,0; 6,25 | t0, +0,50625, +1,5625 (+2,38125 v T4, T6, T8) |
| text (nod) | malý buben + tlesknutí | lusknutí t0 + 0,625, + 1,875 (jen jemně) | 5,625 | t0 + 0,637, t0 + 1,887 |
Obrat T9 (t0 = 20): marimba 20,0; 20,50625; 20,9375; 21,25; 21,75625. Zvukové logo C5 22,1875 · F5 22,34375 · A5 **22,5**, tlesknutí 22,5.

**Amplitudy (aby to bylo elegantní)**: nod textu 9 px dolů (náběh 90 ms ease-in, návrat 420 ms kriticky tlumeně), řádky se zpožděním
40 ms pod sebou (překrývání pohybu). Kopák = bageta měřítko 1,000 → 0,985 → 1,000 (180 ms). Rajče na marimbu: plátek se pootočí o 8°
a vrátí (pružina 3 %). Rukola na kytaru: lístek švihne špičkou o 6° (pivot u stopky). Balsamico na basu: kapka přeteče přes okraj o 6 px
a vrátí se. Nic dalšího se nehýbe; když nástroj nehraje, prvek stojí.

## Storyboard
Časy z `media/projekty/001-bb-chill/hudba.json` (96 BPM, doba 0,625 s, takt 2,5 s, drop 7,5 s, konec 22,5 s) a z aranže v `hudba.py`.
Pohled shora, kamera stojí. H = co v tu chvíli hraje hudba (už je v `hudba.wav`), SFX = návrh velmi tichého efektu pro zvukaře
(jen tam, kde obraz dělá něco, co hudba nemá; vrchol přesně na událost). Geometrie: horní půlka = horní pruh štítku (BAGETERIE),
dolní půlka = dolní pruh (BOULEVARD), **pant = dělicí přímka ze `znacka.json`**.

| čas (takt · doba) | obraz | text na obrazovce | zvuk / událost |
|---|---|---|---|
| **0,000** (T1 · 1) | **Snímek 0 = náhled**: tmavě hnědé pozadí #5A3218, uprostřed dvě půlky rozevřené bagety ležící střídou nahoru (#F3E3C3) přesně v rozložení dvou pruhů štítku BB (horní kratší a vlevo, dolní delší a vpravo, −6°). Na dolní půlce právě dosedl **1. plátek rajčete** (stín se přitáhl, plátek dotáčí 8° → 0 pružinou 3 %). Mascarpone se začíná roztírat jedním tahem po horní půlce (do 1,09 s) | nahoře „CAPRESE“ (BSD 900, 150 px, žlutá #F0B600, x = 90, y ≈ 420) · dole „TOMATOES“ (BSD 700, 64 px, prostrkání 0,12 em, žlutá) | H: Dm7 Rhodes + marimba + shaker · rajče = marimba |
| 0,625 (T1 · 2) | **Háček**: na lusknutí se obě půlky ve 3D natočí kolem podélné osy o 16° a zpět (0,5 s, ease-out tam / kriticky tlumeně zpět), ukáže se tloušťka kůrky #D08B3A se zářezy: z „loga“ je bageta. Text kývne 9 px | | H: lusknutí · SFX: žádný |
| 0,9375 (T1 · 2&) | **2. plátek rajčete** dopadne na swingovou osminu (z 1,25× velikosti a rozostření 6 px na 1,0 a ostrost, stín se přitáhne), 1. plátek na stejný tón pootočí o 8° a vrátí („hraje“) | | H: marimba |
| 1,5625 (T1 · 3&) | **1. plátek mozzarelly** se položí mezi rajčata na Rhodes akord (měkce, bez odskoku: ease-out 0,35 s, krémový stín) | „TOMATOES“ ujede dolů do masky (ease-in 0,2 s), z masky vyjede „MOZZARELLA“ | H: Rhodes |
| 1,875 (T1 · 4) | lusknutí: „CAPRESE“ kývne; mascarpone tah dokončen, poslední milimetr dotře | | H: lusknutí |
| **2,500** (T2 · 1) | **3. plátek rajčete** + **2. plátek mozzarelly** naráz (akord = dva nástroje, dvě suroviny). Řada rajče / mozzarella jako na fotce Caprese z bb.cz | | H: Gm9 · Rhodes + marimba |
| 3,125 (T2 · 2) | **1. lístek rukoly** dopadne s natočením 20°, špička švihne o 6° (pivot u stopky) | „MOZZARELLA“ ven, „ROCKET“ dovnitř | H: lusknutí |
| 3,4375 (T2 · 2&) | všechna 3 rajčata se naráz pootočí o 8° a vrátí (marimba „zahrála“ podruhé) | | H: marimba |
| 3,75–4,31 (T2 · 3–4) | **pesto genovese**: 8 přesných zelených teček naskočí zleva doprava na šestnáctiny shakeru **se swingem** (lichá o 37,5 ms později), každá z 0 na 1 pružinou 3 % za 0,12 s. Je to jediné místo, kde je swing vidět „holý“ | „ROCKET“ ven, „PESTO GENOVESE“ dovnitř (3,75) | H: shaker šestnáctiny · Rhodes 4,0625 → **3. plátek mozzarelly** |
| 4,375 (T2 · 4) | **2. lístek rukoly**, špička švihne | | H: lusknutí |
| **5,000** (T3 · 1) | **balsamico**: tenká klikatá čára #3A1F10 se nakreslí přes náplň jedním tahem (0,9 s, ease-in-out, konec tahu se zúží). Na první kopák se celá bageta stáhne na 0,985 a vrátí (180 ms) | „PESTO GENOVESE“ ven, „BALSAMIC“ dovnitř | H: C9, Rhodes, marimba, **jemný kopák** |
| 5,625 (T3 · 2) | **3. lístek rukoly**, náplň je kompletní (všech 6 surovin z menu Caprese) | „BALSAMIC“ ven 5,9, řádek tracklistu zůstane prázdný (napětí) | H: lusknutí (poslední) |
| 5,9375 (T3 · 2&) | rajčata zahrají naposled (pootočení 8°) | | H: marimba |
| 6,250 (T3 · 3) | druhý kopák: **horní půlka se začne zvedat na pantu** (rotateX 0 → 55° za 0,62 s, ease-in-out), pod ní se protáhne její stín; začíná stoupající šum | „CAPRESE“ se pomalu rozjede v prostrkání 0 → 0,08 em (nádech) | H: kopák + Rhodes + reverse činel (6,25–7,5) |
| 6,875 (T3 · 4) | předtakt marimby A5: horní půlka vyskočí na 110° (ease-out 0,25 s) | | H: marimba A5 |
| 7,1875 (T3 · 4&) | G5: horní půlka dojede na **150°** (visí nad dolní, kůrkou ke kameře, zářezy vidět) | | H: marimba G5 |
| 7,19–7,50 | **nádech**: horní půlka visí, jen se driftem dotočí o 2° (živý obraz, žádné zamrznutí), nic jiného se nehýbe | | H: ticho + vrchol šumu |
| **7,500** (T4 · 1) **DROP** | **ZAKLAPNUTÍ + VÝRON ŽLUTÉ** (nejsilnější moment): 7,32–7,50 horní půlka dopadne 150° → 180° (ease-in až do nárazu, svislé rozmazání podle rychlosti, `--sub 8`) a **zaklapne přesně v 7,500**. Bageta je zavřená: shora kůrka se 4 zářezy, z boků vykukuje náplň (okraje rajčat, mozzarella, špičky rukoly). Náraz: bageta 0,975 a zpět (kriticky tlumeně 0,22 s), náplň vyhrkne z boků o 12 px a vrátí. **Z obrysu bagety se rozjede žlutá #F0B600** (tvar = silueta bagety zvětšovaná z 1× na 7×, ease-out), dolní rohy pokryje v 7,83. Stín se přebarví na hnědou 18 % | žlutý „CAPRESE“ a tracklist **zmizí v žluté** ve chvíli, kdy je přejede okraj výronu (žlutá na žluté, bez prolínačky). **„NOT FAST FOOD.“** (BSD 900, 150 px, hnědá) vyjede zdola z maskovací linky y = 560 v 7,62–8,05 (ease-out) | H: drop Fmaj9, kopák + činel, plná drážka, basa · SFX: dřevěný „klap“ chleba s vrcholem v 7,500 |
| 8,006 (T4 · 1a) | kopák „a“: bageta 0,985; rajčata v boku pootočí 4° na marimbu | | H: kopák, marimba |
| 8,137 (T4 · 2) | **první kývnutí světa**: „NOT FAST FOOD.“ kývne 9 px, bageta se zhoupne −6° → −4° → −6° (pivot v levém konci, 0,5 s). Od teď na každé 2 a 4 | | H: malý buben + tlesknutí |
| 8,4375 (T4 · 2&) | rukola v bocích švihne špičkami (kytara), tlumeně | | H: kytara |
| 7,5 / 8,125 / 8,75 / 9,375 | **jednorázově „odpočítá takt“**: 4 zářezy na kůrce se postupně rozevřou o 3 px (světlejší #EBC27E) a zavřou, jeden na každou dobu: bageta se představí jako takt. Dál už se zářezy neopakují (žádné mechanické údery) | | |
| 9,0625–9,88 (T4 · 3a–4a) | volno na čtení, jen nástroje: kopák (bageta 0,985), basa (balsamico kapka přeteče o 6 px a vrátí), nod na 9,387 | „NOT FAST FOOD.“ drží (čte se 2,4 s) | H: kopák 9,0625 a 9,881 |
| **10,000** (T5 · 1) | **první taneční krok**: na kopák bageta udělá krok 28 px doleva (ease-out 0,3 s), na 11,5625 (kopák 3&) krok zpět; na 2 a 4 dál houpe (−6° ↔ −4°). Kamera stojí, takže „tančí“ jen bageta | pod nadpis vyjede z masky **„EXPRESS GOURMET.“** (BSD 900, 116 px, max 850 px šířky) 10,0–10,45 → **slogan kompletní**; oba řádky kývají s odstupem 40 ms (horní první, dolní jako ozvěna) | H: Dm7, kopák |
| 10,506 / 10,9375 / 11,875 / 12,19 | rajčata v boku „hrají“ marimbový motiv (pootočení 4°), mozzarella na Rhodes (mírné vyhrknutí 5 px) | slogan drží do 12,5 (čte se 2,5 s) | H: marimba, Rhodes |
| **12,500** (T6 · 1) | **náplň dýchá s basou**: na každý basový tón (12,5; 13,63; 14,06; 14,69) všechny suroviny vyjedou z boků o 10 px a pomalu se vrátí (ease-out tam, kriticky tlumeně zpět), jako když basa „tahá“ celou písničku. Bageta jinak stojí | slogan odjede nahoru za horní masku (ease-in 0,22 s, 12,50–12,72), z dolní masky vyjede **„ALWAYS FRESH“** (BSD 900, 140 px) 12,75–13,2 | H: Gm9, basa |
| 13,125 / 14,375 (T6 · 2, 4) | nod textu, bageta zhoupne | | H: tlesknutí |
| 14,6875 (T6 · 4&) | otevřený hi-hat: lístek rukoly se natočí o 10° a zůstane natočený (připravuje „rychlost“) | | H: otevřený hi-hat |
| **15,000** (T7 · 1) | **„FAST“ = vtip na dvojnásobné tempo**: 15,0–16,25 se bageta (a s ní řádek textu) posune o 4 drobné kroky po 14 px doprava, **jeden krok na každou osminu hi-hatu** (15,0; 15,3125; 15,625; 15,9375; osminy jsou sudé šestnáctiny, swing je nemění), každý krok ease-out 0,12 s, pak stojí. Na 16,25 udělá jedním plynulým pohybem 0,5 s cestu zpět (kriticky tlumeně) a vrátí se do pohody. Jediné místo ve videu, kde je pohyb rychlejší než doba | „ALWAYS“ zůstane, **„FRESH“ ujede dolů ve vlastní masce** (ease-in 0,15 s), **„FAST“ vyjede** (ease-out 0,2 s, začne až po odchodu FRESH). „ALWAYS FAST“ dělá kroky s bagetou o 1/16 později (ozvěna) | H: C9, hi-hat šestnáctiny · SFX: 4 tiché „tap“ kroky (dřevo) |
| 15,625 / 16,875 (T7 · 2, 4) | nod textu a houpnutí bagety jako dřív (pohoda se vrací) | | H: tlesknutí |
| 16,25–17,5 | klid, nástroje hrají v náplni (rajče, mozzarella, rukola) | „ALWAYS FAST“ drží (čte se) | H: kopák 16,5625, Rhodes |
| **17,500** (T8 · 1) | **„celá kapela“**: jediný takt, kdy hrají v obraze všechny suroviny naráz, každá na svůj nástroj (rajčata, mozzarella, rukola, balsamico, kůrka na kopák). Je to vrchol drážky před koncem, ale amplitudy zůstávají stejně malé | „ALWAYS FAST“ odjede nahoru (ease-in), vyjede **„FINE DINING“** (900, 130 px) a pod ním **„WITHOUT THE WHITE / TABLECLOTHS“** (900, 92 px, 2 řádky), 17,6–18,2, tři řádky kývají kaskádou po 40 ms | H: Fmaj9, plná drážka, otevřený hi-hat 19,6875 |
| 18,125 / 19,375 (T8 · 2, 4) | nod | čte se do 20,0 | H: tlesknutí |
| 19,881 (T8 · 4a) | kopák před obratem: bageta se nadechne (0,985) | | H: kopák |
| **20,000** (T9 · 1) | **bageta se znovu otevře**: horní půlka se na pantu překlopí zpět 180° → 0° (0,45 s, ease-in-out, stejná cesta jako na dropu, jen pomaleji) a leží střídou nahoru v poloze horního pruhu štítku | text odjede nahoru (ease-in 0,25 s, 20,0–20,25) | H: obrat Gm9, marimba B5 |
| 20,506 / 20,9375 / 21,25 | **kapela se ukloní a odejde**: suroviny odjíždějí z dolní půlky dolů ze záběru, každá na svůj tón (20,506 rajčata, 20,9375 mozzarella + rukola na kytaru, 21,25 pesto + balsamico), ease-in, opožděně po sobě 40 ms. Obě půlky jsou zase prázdné jako ve snímku 0 | | H: marimba A5 G5 E5, kytara |
| 21,25–21,90 | **chleba → štítek**: obě půlky dojedou do přesné polohy a úhlu dvou pruhů štítku (kriticky tlumeně), kůrka po okrajích se zúží na 0, střída zbělá #F3E3C3 → #FEFEFE, obrys se zarovná přesně na 13 vrcholů ze `znacka.json`; od 21,90 už se tvar nemění | z horní masky vyjede **„NOT FAST FOOD. / EXPRESS GOURMET.“** (900, 104 px, 2 řádky) 21,4–21,85 | H: C9, marimba G5 21,756 |
| 21,875 (T9 · 4) | štítek dosedne (měřítko 1,02 → 1,00, pružina 3 %) | | H: tlesknutí |
| 22,1875 / 22,34375 | C5: štítek stojí · F5: **„BAGETERIE“** dosedne na horní pruh (razítko: z 1,06 na 1,00 a krytí 0 → 1 za 0,1 s, písmena z oficiálního SVG, maska podle dělicí přímky) | | H: zvukové logo C5, F5 |
| **22,500–25,0** (T10) **END CARD** | 22,5 A5: **„BOULEVARD“** dosedne na dolní pruh → logo kompletní, přesně v poloze a úhlu bagety ze snímku 0 (smyčka D4). Logo uprostřed (šířka 760 px, střed y ≈ 960), slogan nad ním, bb.cz a disclaimer pod ním. 22,5–25,0 drží, žádný zamrzlý snímek: po 22,5 už hudba nemá bicí (jen doznívá Fmaj9), proto žádné kývání; celá kompozice se během doznívání jen pomalu usadí o 6 px nahoru (ease-out 2,5 s) a štítek se jednou dotočí z −6,0° na −5,5° (logo se nedeformuje, jen natočení a poloha) | slogan nahoře (y 330–560) · logo · **„bb.cz“** (BS Text 800, 70 px, y ≈ 1300) vyjede z masky 22,5–22,8 · **„Concept ad · not affiliated with Bageterie Boulevard“** (BS Text 600, 30 px, krytí 80 %, y ≈ 1400) najede eased fadem 22,6–23,0 | H: zvukové logo A5 + tlesknutí v 22,5, finální Fmaj9 a doznění do 25,0 |

## Kontrolní časy a pasti stavby
**Kontrolní snímky** (`render_html.cjs --nahled casy --casy …`), před plným renderem:
0,0 (náhled: čte se silueta štítku z chleba?) · 0,78 (háček: vidět kůrku při natočení 16°) · 4,5 (náplň skoro hotová, tracklist) ·
6,9 a 7,2 (horní půlka na 110° a 150°, zadní strana = kůrka) · **7,45 / 7,50 / 7,55 / 7,65 / 7,83** (zaklapnutí, výron žluté v půli
a v rozích, „CAPRESE“ mizí ve žluté) · 8,6 (NOT FAST FOOD. čitelné) · 11,0 (slogan 2 řádky, šířka ≤ 850 px) · 13,5 (ALWAYS FRESH) ·
15,1 / 15,95 / 16,5 (FRESH→FAST, krokování, návrat) · 18,8 (3 řádky FINE DINING, nic v pravých 120 px) · 20,25 (otevřená bageta) ·
21,0 (odchod surovin) · 21,9 (štítek přesně na 13 vrcholech: překryv s `logo_bb_full_2000.png` v rozdílovém snímku) · 22,5 · 24,9 (end card).
Plus `--nahled doby --bpm 96` (každá doba) a `?mrizka` pro bezpečné zóny.

**Pasti stavby** (do `<pasti>` kostry, oddíl 10):
1. **Časy nástrojů nepsat ručně.** Do scény dát funkci, která ze stejných vzorců jako `hudba.py` (`sw(d) = d + 0,06` u lichých šestnáctin,
   vzory kopáku, basy, marimby, Rhodes, kytary podle taktu, rozdíl úvod / hlavní část / poslední takt před dropem / obrat) vygeneruje seznam
   událostí. Lepší: `hudba.py` ať je zapíše do `hudba.json` (`udalosti` po nástrojích), scéna je jen načte. Jinak drift o šestnáctinu = celé groove mimo.
2. **Událost = vrchol, ne začátek.** Kývnutí, pootočení a dopad mají vrchol přesně na čase úderu (+12 ms u tlesknutí). Náběh začíná před ním
   (dopad: pád 0,18 s končí v čase úderu; kývnutí: náběh 90 ms před a vrchol na úderu). Ověřit na snímcích 1 snímek před a po.
3. **Nemechanické groove**: kontrola, že žádný prvek nedělá stejný pohyb na všechny 4 doby (zakázané beat-snapped slams). Nod jen na 2 a 4,
   kopák jen bageta, ostatní jen svůj nástroj. Amplitudy z oddílu Vzhled jsou strop, ne minimum. Když to na náhledu vypadá „živě, ale neklidně“,
   zmenšit nejdřív rajčata a rukolu, ne text.
4. **Pant ve 3D**: horní půlka = `div` s `transform-origin` na dělicí přímce, `rotateX(θ)` v souřadnicích natočených o −6° (vnořit: vnější
   `rotate(-6deg)`, vnitřní `rotateX`). Přední strana (střída + mascarpone) a zadní strana (kůrka + zářezy) jako dvě vrstvy s `backface-visibility: hidden`,
   `transform-style: preserve-3d` jen na této skupině. Perspektiva 1800 px na rodiči bagety, ne na celé scéně. Stín horní půlky počítat 2D
   (posun a zúžení podle `cos θ`), ne 3D.
5. **Zaklapnutí v 7,5 s**: poslední 0,18 s je ease-in (zrychluje do nárazu), náraz bez odskoku (chleba neodskakuje), jen stlačení 0,975.
   Rozmazání jen na horní půlce ve směru pohybu, render celé scény `--sub 8` (renderer má jeden počet podsnímků).
6. **Výron žluté**: tvar = silueta bagety (zaoblený obdélník −6°) zvětšovaný kolem středu bagety; musí pokrýt i roh (0, 1920) a (1080, 0)
   do 7,83 s. Spočítat potřebné měřítko z nejvzdálenějšího rohu (cca 7×) a easing tak, aby okraj přejel text „CAPRESE“ až v ~7,62
   (aby zmizel ve žluté viditelně, ne v prvním snímku). Žlutá vrstva leží **pod** bagetou a nad hnědým pozadím (z-index).
7. **Text mizející ve žluté**: žlutý text musí mít přesně #F0B600 jako výron (jinak zůstane duch). Pak ho po 7,85 skrýt (`display:none`).
8. **FRESH → FAST a štítek**: odcházející slovo zmizí dřív, než příchozí obsadí místo (D6); každé má vlastní masku. Slova loga BAGETERIE /
   BOULEVARD maskovat podle dělicí přímky ze `znacka.json`.
9. **Chleba → štítek**: oba obrysy (půlka bagety, pruh štítku) jako polygony se stejným počtem bodů (převzorkovat na např. 64 bodů rovnoměrně
   po obvodu, začátek ve stejném rohu, stejný směr), morf interpolací bodů 21,25–21,90; poté nahradit přesnou cestou z oficiálního SVG
   (žádná deformace loga, rozdílový snímek proti `logo_bb_full_2000.png` musí být prázdný).
10. **Fonty**: `document.fonts.load('900 150px "Big Shoulders Display"')`, `700 64px` a oba řezy Big Shoulders Text vynutit před měřením a před `seek(0)` (C016).
11. **Náhoda**: natočení lístků rukoly a polohy teček pesta z `nahoda(seed)`, nikdy `Math.random`.
12. **Suroviny jako SVG z tvarů**, bez fotek; rajče = kruh s dužinou a 4–5 komůrkami semínek (bez detailních semínek, ať se vejde do čitelnosti),
    mozzarella = měkký nepravidelný kruh, rukola = lístek s laloky (jedna cesta, 3 varianty). Žádné drobky, pára ani částice.
13. **Hnědá na hnědé**: v úvodu je kůrka #D08B3A dost světlá proti #5A3218, ale stín bagety musí být tmavší (#491B13), jinak bageta „plave“.

## Rizika proveditelnosti (HTML, 4 CPU, bez GPU)
| riziko | jak velké | co s tím |
|---|---|---|
| **Groove vypadá jako „všechno se klepe“** (hodně malých pohybů naráz = neklid, ne pohoda) | **největší umělecké riziko** | přísná gramatika (každý prvek jen svůj nástroj), malé amplitudy, kriticky tlumené návraty; kontrola na videu, ne na snímcích (groove je vidět jen v pohybu). Záložní plán: v hlavní části nechat hrát jen rajčata (marimba), text (2 a 4) a bagetu (kopák), ostatní suroviny až v T8 |
| Ilustrace jídla z tvarů vypadá kresleně / levně | střední | plochý styl bez obrysů, barvy z fotky Caprese z bb.cz, stíny jen ploché; nejdřív 1 testovací snímek otevřené bagety se všemi surovinami (4,5 s) a schválení režisérem před stavbou zbytku |
| Silueta „štítku“ ve snímku 0 se nepozná (bageta má zaoblené konce, štítek ostré rohy) | střední | půlky bagety stavět jako polygony štítku se zaoblením rohů jen 18–24 px a kůrkou 10 px po obvodu: tvar čte jako štítek, materiál jako chleba. Když to nepůjde, wow moment 1 zůstane jen „bageta v rytmu“ a koncept funguje dál |
| CSS 3D (rotateX, backface) v headless Chromiu bez GPU | malé | Chromium kreslí 3D softwarově (SwiftShader); jde o jednu skupinu dvou vrstev. Záloha: pant simulovat 2D (`scaleY(cos θ)` + výměna přední/zadní strany při 90°), shora to vypadá skoro stejně |
| Výron žluté jako zvětšovaná SVG cesta 7× | malé | jedna plocha, levné. Pozor jen na hrany: `shape-rendering` výchozí, žádné rozmazání na výronu |
| Čas renderu se `--sub 8` | malé | 25 s × 60 fps × 8 podsnímků ≈ 2× čas proti `--sub 4` (~16 s výpočtu / 1 s videa) → odhad **~13–15 min** na 4 CPU. Scéna je jednoduchá (desítky SVG prvků), ne canvas částice |
| Přesné časy nástrojů nejsou v `hudba.json` (je tam jen drop a konec) | střední (drift = rozbitý groove) | past 1: buď dopsat do `hudba.py` export událostí po nástrojích (režisér commitne), nebo vzorce zkopírovat do scény; časy v tabulce Choreografie jsou spočítané z kódu a sedí na `hudba.wav` jen bez náhodného `jit()` (±pár ms, neviditelné) |
| Morf chleba → štítek (dva polygony různého počtu bodů) | střední | past 9 (převzorkování), morf trvá jen 0,65 s a končí výměnou za přesné SVG |
| Hodně textu (4 hesla + 6 surovin + end card) | střední | každé heslo ≥ 2,4 s na čtení, suroviny po jedné a malé; když kritik uvidí přeplnění, vypustit „FINE DINING / WITHOUT…“ (T8 pak drží „ALWAYS FAST“ a bageta má „celou kapelu“ bez textu) |
| Hnědé intro 7,5 s může na feedu působit tmavě (zadání „pohodová“) | malé–střední | hnědá je barva značky a teplá; náhled (snímek 0) obsahuje žlutý text a světlý chleba. Kdyby režisér chtěl žlutou od 0, varianta: intro na krémové #F7F0EB a výron žluté zůstane (slabší kontrast dropu) |

