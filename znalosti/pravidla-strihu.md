# Pravidla střihu a tvorby videí

Živý dokument. Platí pro **každé** video, pokud zadání konkrétního videa neříká jinak.
Po každé referenci a po každém hotovém videu se doplňuje nebo upravuje.

**Priorita při konfliktu:** pravidla ze zadání konkrétního videa > `znacka.md` > tento dokument.
**Vkus uživatele (V001, 2026-10-31):** „potřebuju víc energetické, ať to není tak bez duši… rychlejší a více živější, ať má víc efektů.“
To má přednost před obecnými zdroji (prompt-motion, reference). Kreativní ředitel a kritici hodnotí **energii a živost** jako hlavní kritérium.
**Vkus uživatele (V002, 2026-11-01):** energie OK („není to špatný“), ale **nic kresleného**: produkty (auta…) **realisticky**, ze skutečných
rendrů / fotek výrobce, tak aby nikdo nepoznal, že video dělala AI. Oblíbený styl: **SaaS motion** (čisté UI prvky, karty, plynulá kamera,
kinetická typografie, produkt jako hrdina). Laťka: realismus + wow + energie.
**Vkus uživatele (V003, 2026-11-01):** u aut **vůz musí jet** (pohyb, rychlost, jízdní záběry), statické rendry posouvané kamerou nestačí
(„není to ono“). Rendry a fotky jsou jen doplněk; hlavní materiál je skutečný pohyb. Kritici hodnotí, jestli divák vidí jízdu.
**Vkus uživatele (V004, 2026-11-04):** „takhle není to špatný, ale zaměř se víc na ten **střih a editaci**… adaptuj se na tyhle střihy“ + 3 předlohy
(R6, R7, R4 znovu). Střihem myslí **kvalitu přechodů**, ne počet střihů: jeden hrdina na obrazovce, stavy místo záběrů, proměny místo tvrdých střihů,
vše z rozostření do rozostření, hlas nebo věta řídí střih, prezentace jako natočená obrazovka / mockup, podpis tvůrce na konci.
**Závazný výklad je v `strih-vzor.md`** (při rozporu má přednost před tímto dokumentem).
Předloha, kterou uživatel výslovně pošle k danému videu, smí přebít i výchozí zákazy (např. šmouhy v D2, záři v G2). Výjimku zapsat do zadání.

**Zdroje:** `[R1]`–`[R7]` = rozbory v `reference/` (R4, R6, R7 = předlohy střihu od uživatele, viz `strih-vzor.md`), `[PM]` = prompt-motion.com (`prompt-motion/poznatky.md`),
`[V001]…` = poučení z našich videí (`pouceni.md`), `[obecné]` = profesní praxe, kterou zatím nepotvrdila reference ani zpětná vazba.

---

## A. Formát a technika
- **A1** Výchozí formát **16:9, 1920×1080** (rozhodnutí uživatele 2026-10-31; 9:16 jen když to zadání řekne). **Animace z kódu 60 fps**,
  natočený materiál v nativních fps (obvykle 30). `[uživatel 2026-10-31, PM]`
- **A2** Hlasitost **−14 LUFS integrated**, true peak ≤ −1 dBTP, **měřeno po zakódování do AAC** (`nastroje/master_zvuk.sh`). Všech 5 referencí mělo −14,1 až −14,3 LUFS. `[R1–R5, PM]`
- **A3** Export H.264 (High), yuv420p, AAC 48 kHz, `+faststart`. `[obecné]`
- **A4** Délka **25–35 s** podle zvoleného motionu z prompt-motion (rozhodnutí uživatele 2026-10-31). Vždy **jedno video naráz**. `[uživatel 2026-10-31]`
- **A5** Bezpečné zóny: **16:9** = důležitý text uvnitř 90 % obrazu (okraj 96 px vlevo/vpravo, 54 px nahoře/dole), spodních ~140 px
  může zakrýt ovládání přehrávače. **9:16** = ne do horních ~250 px, spodních ~400 px ani k pravému okraji ~120 px. `[obecné]`
- **A6** 4:3 (1080×810) jde použít pro „čistou“ designovou ukázku. R3 v něm měla nejvíc dosahu, ale výchozí zůstává 9:16. `[R3]`
- **A8** **Hrdina musí být na telefonu velký**: hlavní objekt zabírá zhruba ≥ 75 % šířky obrazu nebo ≥ 45 % výšky v klíčových momentech
  a obraz je svisle vyvážený, bez prázdné poloviny (spodních ~400 px pro UI se nepočítá). Drobné změny (mezera 2 px, posun 4 px) na telefonu
  nikdo nevidí: stupňování musí být vidět na zmenšenině 270 px. `[V001 kontrola 1]`
- **A7** Předlohu 16:9 nebo 1:1 pro 9:16 **přeskládat, ne oříznout**: řady pod sebe, kamera svisle, souřadnice přepočítat. 81 % katalogu prompt-motion je 16:9. `[PM]`
- **A9** **Prezentace hotového videa**: animace 16:9 / 16:10 se pro reels nepřeskládává, ale ukazuje (a) jako **natočená obrazovka** (notebook natočený telefonem
  na výšku, H5) nebo (b) v **mockupu** (panel se stínem 85 % šířky, štítek, CTA v obraze; dvojice panelů před/po). Dodává se 16:9 originál + 9:16 prezentace. `[R6, R7]`

## B. Háček (první 1–3 s)
- **B1** Háček **v první sekundě**, obrazem i textem, ne až po úvodu. `[R2, R3, R4]`
- **B2** Osvědčené typy háčků:
  - šok / emoce: „Holy sh\*t, you are not ready for this“ `[R2]`
  - otázka na bolest diváka: „Does your animation look robotic?“ `[R4]`
  - rychlá sekvence slov: „See it, like it, save it, scroll…“ `[R3]`
  - POV situace z praxe: „POV: Client asked for "cool" logo animation 👀“ `[R5]`
  - provokativní tvrzení: „… just kil\*ed motion designers 🤯“ `[R1]`
- **B3** **Statický nadpis nahoře** patří k formátu „natočená obrazovka“ a POV/meme: jedna věta nesoucí háček, pod horní bezpečnou zónou.
  Styl: bílá zaoblená bublina, černé tučné písmo, emoji na konci, nebo bílý text se stínem.
  **Do čistých motion videí (showreel, logo, produktový film) ho nevkládat.** Nadpis dávat až ve střihu jako samostatnou vrstvu a vždy dodat i čistou verzi. Žádné drobné popisky, štítky ani „HUD“ v rozích. `[R1, R2, R5, PM]`
- **B4** Sporná slova cenzurovat hvězdičkou (kil\*ed, sh\*t), aby je algoritmus neomezil. `[R1, R2]`
- **B5** Video musí dávat smysl **bez zvuku** (titulky a text na obrazovce). `[R2, R4]`
- **B6** **Snímek 0 je hotový, silný obraz** (slouží jako náhled): žádné zatmívání z černé ani úvodní logo. První obsahový moment do ~2 s. `[PM]`

## C. Struktura
- **C1** Reklama / koncept produktu: problém → řešení → komplikace → emoce → slogan → logo. `[R1]`
- **C2** Vzdělávací: háček-otázka → proč to tak je → 2–3 pravidla s vizualizací → hned použitelný tip → CTA. `[R4]`
- **C3** Promo nástroje / služby: háček → tvrzení → důkaz → **před/po srovnání** → kroky návodu → CTA. `[R2]`
- **C4** Koncept / case study: běžná situace → „But what if…“ → řešení → **emoční zvrat** → podpis. `[R3]`
- **C5** Logo / showreel: krátká smyčka, ve videu zopakovaná 2–3×. `[R5]`
- **C6** Konec = **end card** (logo, podpis, @jméno, CTA). Drží **1,5–3 s**, ve smyčce stačí 1–1,5 s, s jemným pohybem (dotlačení 2–4 %), nikdy zamrzlý obraz.
  Dlouhý podpis (~10 s, R3) jen u konceptů, kde end card nese text nebo manifest. `[R1, R3, R4, PM]`
- **C9** **Podpis tvůrce**: u portfoliových videí po logu klienta: logo do rozostření → 0,2 s ticho → boom + bílý záblesk → end card tvůrce **2 s**
  + disclaimer v obraze („Spec ad · not affiliated with …“); kamera i na end card dýchá. `[R6, R1]`
- **C7** **Energie (vkus uživatele, V001)**: událost na **každou dobu**, nová myšlenka nebo scéna každých **~1–1,5 s**, aspoň jeden
  „úder“ (impakt, švih, záblesk, změna měřítka) na takt. Tempo hudby u energických zadání 120–140 BPM. Zpomalení jen jako krátký
  kontrast před dropem (max ~0,5 s). `[V001 zpětná vazba uživatele, R2, PM]`
  **Upřesnění (V004, R6, R7)**: událost = **změna stavu hrdiny** (každých ~0,6 s), ne nový prvek navíc; energie z proměn, ne z počtu střihů a prvků (`strih-vzor.md` 1–2).
- **C8** **Fakta a čísla nevymýšlet** (procenta, jména zákazníků, výsledky). Čísla jen ověřená od uživatele, jinak zjevně ukázková. Texty značky citovat doslova. `[PM]`

## D. Střih, rytmus, přechody
- **D1** **Hlas řídí střih**: každá vizuální změna sedí na slovo nebo přízvuk; **obraz předbíhá slovo o 0,1–0,35 s**, nikdy nezaostává; pauzy hlasu vyplňuje
  souvislý pohyb. Bez hlasu totéž pro **větu na obrazovce** (claim / titulek na scénu); doby hudby jsou až druhé v pořadí. `[R2, R4, R6, PM]`
- **D2** Přechody tak, že **další scéna vzniká z předchozí** (sdílený prvek, morf, zaplavení barvou, match cut, zoom skrz objekt),
  a k tomu **energické přechody na doby**: švihy s rozmazáním, světelné šmouhy, záblesky na úder, rychlé zoomy. Smí být **víckrát za video**,
  když sedí na rytmus (V001: střídmost působila „bez duše“). Nikdy líná prolínačka celých scén bez důvodu. `[R1, R2, R3, PM, V001]`
  **Výchozí příchod a odchod** prvků (text, karta, logo): **z rozostření do ostrosti 0,1–0,25 s, odchod do rozostření + zblednutí 0,05–0,2 s**, odchod kratší
  než příchod a nejlépe proměnou v další prvek; ostré naskočení maskou jen s důvodem. `[R6, R7]`
- **D3** Tvrdé střihy jen tam, kde dávají rytmus: kroky návodu (~4 s na krok), výčty, skutečná stopáž (jízda); v grafické vrstvě **žádné**
  a přes střih stopáže přežívá spojovací prvek (bod, linka). `[R2, R6, R7]`
- **D4** Krátké video stavět jako **smyčku**: poslední snímek navazuje na první včetně polohy a rychlosti prvků. `[R3, R5, PM]`
- **D5** Rozmazání pohybem: (1) v kódu podle rychlosti a směru (svislý švih = svislá šmouha), (2) render s podsnímky **4 u běžného pohybu, 6–8 u rychlých přechodů**
  (méně dělá „duchy“, C003). Statický text a UI zůstávají ostré a rozmazání nesmí tvar úplně smazat. `[R2, R3, PM]`
- **D6** **Žádný pohyb bez příčiny**: každá animace vychází z prvku, který už je na obrazovce, nebo do něj vede. Nic se nepřesouvá skokem.
  Odcházející text zmizí dřív, než příchozí obsadí jeho místo. `[PM]`
- **D7** **Přechod přímou manipulací**: když existují dva zarovnané snímky (den / noc, světla vyp / zap), druhý se odkrývá maskou vázanou na
  ovládací prvek (posuvník, přepínač), ne prolínačkou. `[V003, PM]`
- **D8** **Rozpočet prvků**: na obrazovce 1 hrdina + nejvýš 1 doplněk; hrdina drží 2–5 s a mění **stavy** (každých ~0,6 s), ne záběry.
  Mřížky, koláže a „všechno najednou“ jen se zdůvodněním v zadání. `[R6, R7]`
- **D9** **Střihová partitura před stavbou**: ke každému prvku příchod / typ / klid / odchod / typ / spojka s dalším / slovo hlasu (`strih-vzor.md` 2).
  Prvek bez spojky do videa nepatří. Klid: slovo ≤ 0,33 s, řádek ≤ 0,6 s, karta ≤ 1,2 s; kritik partituru kontroluje po snímcích. `[R6, R7]`
- **D10** **Semínko a spojovací hmota značky**: tvar v barvě značky (tah, tečka, kruh, plocha) je na snímku 0, kreslí z něj logo, vrací se během videa
  (UI, rámeček klíčového slova, pozadí explozí) a na konci se přemorfuje zpět do loga. Nikdy nezmizí, jen se mění. `[R6, R7]`
- **D11** **Přechody mezi světy, každý jiný, žádný dvakrát**: let, wipe pruhy v barvách značky (0,35 s plné barvy, konec = konec věty), zoom skrz objekt + rozostření,
  exploze tečky do plochy, kruhová clona ze středu, inverze plochy, morf do loga, záblesk + boom před end card. `[R6, R7]`
- **D12** **Rytmus z obrazu, zvuk podle něj**: pořadí stavby = partitura → obraz → zvuk. Střih se nestaví na mřížku BPM; hudba a SFX se doladí k proměnám. `[R6, R7, C045]`

## E. Typografie a titulky
- **E1** Slovo po slově **jen tam, kde text čte hlas** (titulky, háček). Slovo naskočí přesně s hlasem (`prepis.py --slova`, při nepřesnosti zarovnat po frázích).
  **Nadpisy a hesla bez hlasu se hýbou jako jeden navržený objekt** (maska, roztažení, morf). `[R2, R4, PM]`
  Claim bez hlasu: slova naskakují **z rozostření** v rytmu řeči; názvy a tvrzení v barvě značky smí **po znacích s pádem na linku** (0,4 s na řádek).
  Na obrazovce nikdy víc než 1 řádek textu naráz (kromě end card). `[R6, R7]`
- **E2** Klíčové slovo zvýraznit barvou, řezem nebo velikostí. Štítek jen jako **navržený** prvek: zaoblená pilulka, která přijede pružinou (R4),
  nebo tah zvýrazňovače přes frázi, nebo **rámeček, který nakreslí tah** (podtržení → hrana → uzavření ~0,35 s, slovo uvnitř z rozostření; rámeček může být
  semínkem loga, D10). **Nikdy ostrý obdélník přesně za písmeny** (vypadá jako označený text). `[R2, R3, R4, R6, PM]`
- **E3** Tučné, výrazné bezpatkové písmo, VERZÁLKY pro důraz („COLLECTION“, „HELL YES“). `[R2, R3]`
- **E4** Jedna rodina písma, max. 2 řezy + případně ruční písmo. Font musí mít českou diakritiku (latin-ext). `[R2, R4, PM]`
- **E5** **Ručně psané anotace** (šipky, kroužky, „like it“, „Forever“) dodají lidský dojem. `[R3]`
- **E6** Animace písma: roztažení (stretch), maska, rozmazání, změna prostrkání. `[R2]`
- **E7** Titulky ve spodní třetině uprostřed, nad bezpečnou zónou (A5). Hlavní nadpis ≥ 110 px, titulky ≥ 56 px při šířce 1080. `[R4, PM, obecné]`
- **E8** Krátká hesla a titulky **bez tečky na konci**. Tečka jen jako záměrná pointa. `[PM]`

## F. Pohyb (easing): platí pro každou animaci
- **F1** **Nic se nehýbe lineárně.** `[R4]`
- **F2** **Co přichází → ease-out** (přijede rychle, dlouho dobržďuje). `[R4]`
- **F3** **Co odchází → ease-in** (pomalu se rozjede, pak zmizí). `[R4]`
- **F4** **UI prvky** (tlačítka, karty, notifikace, pop loga) → pružina s překmitem **2–5 % (výchozí 3 %)**, jednou, bez houpání.
  Velké plochy, kamera, text a usazování → kriticky tlumené (bez překmitu). Výraznější překmit jen u hravých videí a postav. `[R1, R4, PM]`
- **F5** Kamera se hýbe plynule, s paralaxou a s přechodem z 2D do 3D, kde to dává smysl. `[R1]`
- **F6** Zadání pro animace v kódu vždy obsahuje: *„Entrances: ease out. Exits: ease in. Interface: spring, slight overshoot. Nothing linear.
  Springs are closed-form, tiny overshoot. Every frame is a pure function of time. Blur follows speed and direction.“* `[R4, PM]`
- **F7** **Jeden jazyk kamery**: jeden svět, jedna kamera (posun + zoom v logaritmické škále). Nikdy dva pohyby kamery naráz, nikdy zoom tam a hned zpátky.
  Kamera se mezi scénami neresetuje. Pomalé dotlačení během scény (1,00 → 1,04) drží obraz živý. `[PM]`

## G. Barvy a vzhled
- **G1** Omezená paleta: **neutrální pozadí + 1–2 akcenty** (max 3 barvy + černá/bílá). `[R2, R4, R5, PM]`
  - černá + limetkově žlutá + růžová `[R2]`
  - téměř černá + červená `[R4]`
  - tmavě fialová + neonově růžová `[R5]`
- **G2** Záře, světlo a lesk jsou **vítané, když nesou energii nebo značku** (světla aut, světelné stopy, lesk loga, odlesk na laku, akcentní barva).
  Nesmí jen zakrývat slabý nápad. `[R2, R4, R5, PM, V001]`
- **G3** Emoční momenty: teplé světlo, vinětace, zrnitost. `[R3]`
- **G4** Jednotný UI systém: karty se zaoblenými rohy, jemné okraje, malé štítky, monospace popisky. `[R4]`
- **G5** Barvy značky (`znacka.md`) mají přednost před paletami z referencí.
- **G6** **Efekty ano, laciný šablonovitý vzhled ne.** Uživatel chce **víc efektů a energie** (V001): rychlostní čáry, světelné stopy, záblesky
  a otřes kamery na údery, částice z dopadu, glitch jako akcent, chromatický posun na švihu jsou povolené, **když sedí na dobu a vycházejí
  z děje**. Zakázané zůstává jen to, co nic nevyjadřuje: náhodné částice bez příčiny, generické gradienty, text v rozích, vzhled jako
  z šablony (`prompt-motion/poznatky.md` oddíl 4 je seznam rizik, ne zákazů). Vkus uživatele má přednost před střídmostí z prompt-motion. `[V001, PM]`
- **G7** **Produkt realisticky, ne kreslený.** Auta, zařízení a jiné produkty stavět ze **skutečných rendrů nebo fotek výrobce** (konfigurátor,
  web, materiály od uživatele), ne kreslit v kódu. Pohyb 2,5D: vyříznutí (maska), paralaxa vrstev, pomalá kamera, odlesk po laku jen v masce
  karoserie, rotace kola z detailu, rozsvícení světel, kontaktní stín. Efekty nesmí prozradit AI (natažené okraje, plastový lesk, duhy, glitch na produktu).
  Grafika (UI karty, typografie) smí být kreslená, produkt ne. `[V002]`
  Render zvětšovat nejvýš do nativního rozlišení (~1,3× u 2560 px ve 1080p). Otočku z 36 snímků po 10° nikdy pomalu (trhá), jen rychlý oblouk
  s rozmazáním na úder. `[V003]`
- **G9** **Rolující čísla** smí cestou ukázat jen hodnoty **horší** než fakt (rychlost a výkon rostou zdola, čas zrychlení klesá shora),
  nikdy lepší (V003: „259 km/h“, V004: „3.7 s“). Konečná hodnota přesně podle zdroje. Hotová hodnota stojí čitelně **≥ 0,5 s** (u všech karet,
  rolování radši krátké a dřív), při odchodu karty zůstane **plně krycí** prázdný obdélník nejvýš 2 snímky (následné stažení do bodu se nepočítá) (C046).
  Zvuk „ding“ patří na **první ustálený snímek** hotové hodnoty (konec rolování, pohyb číslic < 0,5 px); když koliduje s jiným zvukem, posouvá se
  ten druhý, ne ding (C047). Tiky jen na přenosy, které jsou na obrazovce vidět. **Jedno skutečné číslo na video** (R6: 2 912; V004 mělo 4 za 8 s),
  rolování zdola 0,7 s s odometrickým rozmazáním, klid ≥ 1 s, odchod zblednutím. `[V003, V004, R6]`
- **G8** **SaaS motion**: neutrální světlé pozadí, karty s 1px okrajem a měkkým dvouvrstvým stínem, jeden akcent jen na akci, kurzor změny
  způsobuje a nikdy jen nepluje, nejvýš 1–2 skleněné prvky a nikdy přes produkt (detail `prompt-motion/poznatky.md` oddíl 11.1). `[V003, PM]`

## H. Formát „natočená obrazovka“
- **H1** Animaci přehrát na notebooku nebo monitoru a natočit telefonem v tmavé místnosti, barevné ambientní světlo ladí s paletou. Působí opravdově a „ne jako AI“. `[R1, R2, R5]`
- **H2** Pomalý ruční nájezd kamery, na začátku ruka zmáčkne klávesu (start). `[R1]`
- **H3** Ukázat software / časovou osu / prompt = důkaz řemesla. `[R2, R5]`
- **H4** Já sám natáčet neumím: buď natočí uživatel podle těchto pravidel, nebo to digitálně nasimuluju (maketa notebooku, perspektiva, odlesky, ambient). `[obecné]`
- **H5** **Parametry natočené obrazovky** (změřeno v R6): animace v okně přehrávače (Dock a menu bar vidět), displej 68–89 % šířky snímku; snímek 0 ruka na klávese,
  první obsah do 0,6 s; kamera 0–2,5 s natočení, 0–7 s nájezd ~+30 %, dál dýchání ±8 % s periodou ~8 s, nikdy zamrzlý snímek; místnost plynule zhasne během
  3.–5. s (jas stěny 67 → 11); barevný wipe obarví místnost. Totéž platí pro digitální maketu (H4). `[R6]`

## I. Zvuk
- **I1** Hlas: krátké věty, sebevědomý, rychlý. Pauzy a přeřeky vystřihnout. `[R2, R4]`
- **I2** Hudba pod hlasem s **duckingem** (ztlumení jen během řeči). Cíl: hlas **≈ 9–12 dB nad hudbou v pásmu řeči 300 Hz–4 kHz**, kontrolovat po frázích.
  Paušálních 15–20 dB jen u husté, hlasité hudby. `[PM, obecné]`, ověřit na prvním videu s hlasem
- **I3** SFX na každou **událost** v obraze (klik, dopad, pop, otevření, logo), ne na každý pohyb. Umístit tak, aby **změřený vrchol** zvuku padl na událost.
  Běžné efekty tiše pod hudbou. **Klíčové momenty (drop, pointa, gag, logo) musí být slyšet**: efekt na úrovni hudby nebo nad ní
  (cca 0 až −3 LU v okně 100 ms) a hudba kolem nich ustoupí. **Nádech před dropem a „ticho jako pointa“ = hudba opravdu ztichne**
  (ne jen řidší aranžmá). Výjimka [V002]: tichý souvislý **podklad v háčku** (např. volnoběh motoru, `sfx.py` typ PODKLAD) smí znít
  max. −8 LU pod hudbou a musí doznít před nádechem. **Stoupání musí hlasitostí růst a hlavní drop být nejhlasitější místo videa** [V002, C032].
  (ne jen řidší aranžmá). Hlavní nástroj je **automatika hudby v mixu** (ztlumení před dropem a v pointě, `sfx.py --automatika od-do:dB:náběh:doběh`),
  teprve potom hlasitější efekt (V001: drop +17,4 dB díky ztlumení). U prémiových značek jemné kliky a měkký dopad na logo, žádné hlasité whooshe všude. `[PM, V001 kontrola 1]`
- **I4** Trendy zvuky z IG/TikTok knihovny se přidávají až v aplikaci při publikaci → dodat i verzi **bez hudby**. `[obecné]`
- **I5** Hudba a SFX jen s **licencí pro komerční použití**, zdroje zapsat do zadání. Hudba z `nastroje/hudba.py` je naše vlastní (syntéza v kódu). `[PM]`
- **I6** Ke každému videu **vlastní hudba podle tónu** (vážný / drzý / luxusní …), nálada a BPM do režijního listu. Animace se řídí `hudba.json`
  (doby, takty, drop, konec): drop = nejsilnější vizuální moment, konec = end card. `[uživatel 2026-10-30]`
- **I7** Mix hudby musí znít i z **telefonu**: sub (20–60 Hz) max ~30 % energie, středy (250 Hz–2 kHz) ≥ 30 %, basa s vyššími harmonickými.
  `hudba.py` to hlídá a varuje. `[R5, C012]`
- **I8** Zatím **bez voiceoveru**. Hlas později přes ElevenLabs. Jazyk videí je **angličtina**. `[uživatel 2026-10-30]`
- **I9** **Zvuk u videí s hlasem (vzor uživatele R6, R4, R1)**: hlas nese všechno; hudba ≤ −25 LUFS nebo žádná, SFX tiché a jen na stavové změny (~1 za s),
  jediný hlasitý úder (boom + záblesk) na podpis tvůrce v tichu po hlase. I3 („drop nejhlasitější“) platí jen pro videa bez hlasu; i tam se zvuk dělá až podle
  hotového obrazu (D12) a hlasitost roste jen k jednomu dropu. `[R6, R7]`

## J. CTA, popisek, publikace
- **J1** CTA s **klíčovým slovem**: „Comment PROMPT“, „comment KATANA“, „DM me UGOKI“ (automatická DM); nejsilnější je **staticky v obraze** po celou dobu
  (R7: „Follow and comment “Quokka”“, 3 600 komentářů, poměr k lajkům 0,88). `[R1, R2, R4, R7]`
- **J2** Pro služby: „Need one? Open for commissions“. `[R5]`
- **J3** Popisek končí **otázkou** pro komentáře („What do you think?“). `[R3]`
- **J4** 3–5 relevantních hashtagů, ne desítky. `[R1, R4, R5]`
- **J5** Práce s cizí značkou (koncepty, spec reklamy) **vždy** s disclaimerem: „Spec ad, not affiliated with X“ / „Unofficial concept“. `[R1, R3]`
- **J6** Názor a postoj (např. „vyrobeno člověkem“) přináší komentáře a sdílení. `[R3]`

## K. Kontrola před odevzdáním
Technický podklad: `nastroje/kontrola.sh VIDEO media/kontrola/<projekt>/kolo<n>`. Pak nezávislý kritik.
- [ ] **Energie**: událost na každou dobu, úder každý takt, nikde „mrtvá“ pasáž delší než ~1 s (C7) — vkus uživatele
- [ ] Háček v 1. sekundě, snímek 0 je hotový obraz, funguje bez zvuku (B1, B5, B6)
- [ ] Před plným renderem: snímek na každou dobu (`--nahled doby --bpm …`) nebo každých 0,5 s + 4 klíčové snímky v plném rozlišení
- [ ] Rozlišení, fps a délka podle zadání (A1, A4)
- [ ] −14 LUFS ±1, true peak ≤ −1 dBTP, změřeno **po** zakódování do AAC (A2)
- [ ] Žádný text v bezpečných zónách (A5), titulky bez překlepů a správně načasované, česká diakritika
- [ ] Žádný lineární pohyb, přehnaná pružina ani pohyb bez příčiny (F1–F4, D6)
- [ ] Žádný zamrzlý úsek > 1 s bez textu, žádné prázdné snímky, žádné probliknutí (pásy snímků z `kontrola.sh` prohlédnuté)
- [ ] Hranice smyčky snímek po snímku (D4)
- [ ] Žádný AI poznávací znak bez zdůvodnění v zadání (G6)
- [ ] Čísla a fakta ověřená (C8)
- [ ] End card + CTA (C6, J1)
- [ ] **Střih podle vzoru uživatele** (`strih-vzor.md` 6): 1 hrdina + 1 doplněk, 0 tvrdých střihů v grafice, partitura sedí po snímcích, příchod z rozostření /
  odchod kratší a proměnou, klid jen na přečtení, obraz předbíhá slovo, přechody se neopakují, jedno číslo, zvuk podle obrazu, podpis tvůrce (D8–D12, C9, I9)
- [ ] Splněna všechna pravidla ze zadání videa
