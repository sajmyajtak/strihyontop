# V001: Bageterie Boulevard: pohodový chill spot

| | |
|---|---|
| Datum zadání | 2026-10-30 |
| Platforma / formát | IG Reels / TikTok / Shorts, 1080×1920 (9:16), 60 fps |
| Délka | **25 s** |
| Termín | co nejdřív |
| Stav | výroba |

## Zadání (doslova od uživatele)
> hele vem si od tehle stranky barvu na vide logo hudbu takovou když jdeš jíst například od mekače což znamená pohodová chill. https://www.bb.cz
>
> a motion nechám na tebe pohraj si to stím zadej to hlavně agentovi at vybere fákt dobry motion a i hudbu at uděla a vše řešil pokud bude něco potřeba. Hlavní mozek to bude a když si nebude moc radit at se mě zeptá. delká vide 25 vteřin

## Pravidla pro toto video
Pravidla od uživatele (mají přednost před vším ostatním):
1. Barvy a logo **z webu bb.cz** (Bageterie Boulevard).
2. Hudba **pohodová, chill**, „jako když jdeš jíst do McDonald's“: feel-good, uvolněná, příjemná.
3. Motion necháno na nás: **„fakt dobrý motion“**, pohrát si s tím.
4. Délka **25 s**.
5. Když si agent nebude vědět rady → zeptat se uživatele (přes režiséra).

Výchozí nastavení (`znalosti/znacka.md`): angličtina na obrazovce, bez voiceoveru, CTA podle zadání (není zadáno → rozhodl režisér, viz níže).

Obecná pravidla, která se tu hlavně uplatní: A1, A2, A5, A7, B1, B6, C1, C6, C7, C8, D2, D4, D5, D6, E1–E8, F1–F7, G1–G6, I3, I5–I8, J5, K.

## Rozhodnutí režiséra (uživatel je nechal na nás)
- **Typ videa**: spec / konceptová reklama pro portfolio (jako R1 Waze). Značku nezastupujeme → **disclaimer** malým písmem na end card
  „Concept ad · not affiliated with Bageterie Boulevard“ + v popisku příspěvku (pravidlo J5).
- **Jazyk**: angličtina (I8). Slogan značky přeložen věrně: „Not fast food. Express gourmet.“ (originál: „Nejsme fastfood. Jsme exprès gourmet!“).
  Žádná vymyšlená čísla, ceny ani tvrzení (C8).
- **CTA**: není zadané → end card = logo BB + slogan + „bb.cz“.
- **Vizuál**: přednostně motion design postavený v kódu (tvary, typografie, ilustrace surovin a bagety z tvarů), logo z oficiálního SVG.
  Produktové fotky z webu jen tehdy, když jsou kvalitní a slouží konceptu.
- **Hudba**: vlastní z `nastroje/hudba.py`. Chybí nálada „pohodová“ (chill feel-good) → agent ji doplní jako nový preset.
- **Odpovědi na otázky animátora (fáze 1)**:
  1. **Výjimka z G1** schválena: barvy jídla (rajče, rukola, pesto, kůrka…) **jen na surovinách**. Bez nich jídlo nevypadá chutně a bb.cz
     samo ukazuje jídlo v přirozených barvách na žluté. Zbytek obrazu drží paletu žlutá / hnědá / bílá (+ stříbrná jen v úvodu).
  2. End card podle storyboardu (slogan nahoře, logo uprostřed, bageta pod ním, bb.cz, disclaimer) schválen. Když bude na kontrolních
     snímcích přeplněný, bagetu vynechat.
  3. Materiály BB patří do tohoto projektu (tabulka Materiály), ne do `znalosti/znacka.md`, kde je naše vlastní značka.
  4. Finální `hudba.py` commitne režisér po kontrole.
- **Rozhodnutí režiséra k finálnímu konceptu (F1b)**:
  1. Rozkrojení loga podél dělicí přímky slov a náklon `rotateX` horní půlky (max 18°, v klidu 10°) **schváleno**: tuhý pohyb, obrys ani písmena
     se nedeformují, v klidu a na end card je pixelově přesné SVG. Ve spec reklamě s disclaimerem je to běžná kreativní práce se značkou.
  2. Výjimka z C6 pro drobnou pointu v 24,375 s (vykoukne špička rukoly 30 px) **schválena**: end card nezamrzne a pomáhá smyčce (D4).
  3. Snímek 0 = logo s vykukující náplní + NOT FAST FOOD. **schválen jako háček-záhada** (B6), ne jako úvodní logo.
     Podmínka: na zmenšenině 270 px musí být jídlo čitelné.
  4. SFX syntetizovat v kódu (I5). Žádná knihovna s licencí není.
  5. `hudba.py` vyexportuje události po nástrojích do `hudba.json` (zvukař, první krok fáze 2), zvuk se nesmí změnit.
- **Rozhodnutí režiséra k otázkám zvukaře (fáze 2)**: (1) spektrum nálad vážná / luxusní se vyrovná, až je použije nějaký projekt
  (známý dluh, pouceni.md); (2) pesto v 11,25 zůstává přesně podle vzorce storyboardu, obraz i zvuk mají stejné časy; (3) časy SFX, které
  zvukař doplnil (3,75 + 3,79; pesto 5,04–5,20; popy 7,53–7,68; rukola 8,125 / 8,165 / 8,205; pesto 16,25–16,33), jsou schválené a platí
  pro obraz (sfx.json); (4) hudba.py zůstává u jednoprůchodového loudnormu, finální hlasitost řeší master_zvuk.sh; (5) sfx.py zapsán do nástrojů.
- **Rozhodnutí k opravám zvuku (kolo 1 → v2)**: hlavní momenty nese ztlumení hudby (drop +17,4 dB), efekty křupnutí a polknutí zesíleny o +5 až +6 dB.
  Předztlumení −6 dB v 6,95–7,19 schváleno. Když kritik v kole 2 bude chtít víc, povolit efekt zhruba na úrovni hudby (I3).
- **Výhrada režiséra k hudbě**: v nezávislém měření je mezi oktávami 1 kHz a 2 kHz propad ~13 dB (oktávy rel.: 500 Hz 0, 1 kHz −2,7,
  2 kHz −15,6, 4 kHz −13,9 dB). Jas na telefonu chybí → zvukař ve fázi 2 vyhladí (sousední oktávy 250 Hz–8 kHz max ~8 dB od sebe).

## POKYN REŽISÉRA PRO KOLO 3 (poslední, má přednost před storyboardem)
Řezy nadpisů selhaly dvakrát (kolo 1 i 2: „NXT EAST“, dvojtisk). Teď platí:
1. **Řezy nadpisů 7,8125 / 12,5 / 17,5 s přísně po sobě, nikdy dvě vrstvy textu ve stejném snímku:**
   (a) linka řezu se nakreslí (0,10 s); (b) horní půlka starého textu odjede nahoru, spodní dolů, každá **úplně ven ze své masky** (ease-in 0,12 s),
   linka zmizí s nimi; (c) **teprve potom** nový text vyroste z linie řezu (ease-out 0,25 s). Ověřit pásem 12 snímků po 1/60 s kolem každého řezu
   (render --nahled casy) a **prohlédnout**: v žádném snímku nesmí být starý a nový text zároveň.
   **Když to nejde čistě, nahraď to jednodušším**: starý text odjede nahoru maskou, nový vyjede z linky. Čitelnost má přednost před efektem.
2. **Text se nikdy nerozmazává**: posuny textu (dorovnání ALWAYS FAST 17,97 s, FAST → NOT FAST FOOD. 20,2–20,4 s) jen kriticky tlumené
   (≥ 0,35 s, bez skoků), `rozmazani()` jen na náplň. Žádné cuknutí o 22 px ve 2 snímcích.
3. **Polknutí 0,625 s**: 0,18 s ease-in, pohyb **skončí současně s vrcholem zvuku „glp“ (0,62–0,64 s)**, ne o 75 ms dřív.
4. **Drop**: šmouha písmen loga slabší (šmouha v kódu na půlkách max 2 px), BAGETERIE musí zůstat čitelné v každém snímku.
5. Plakát (barva) řeší režisér při doručení, zkratka smyčky 24,98 → 0 je přijatá (end card je záměrně jiný než snímek 0).

## Reference
| ID | odkaz | co z ní převzít |
|---|---|---|
| R1 | znalosti/reference/R1-waze-koncept.md | spec reklama na značku, příběh za 25 s, přechody bez střihů, end card s logem |
| PM | znalosti/prompt-motion/poznatky.md | metoda, kostra zadání (oddíl 10), zakázané AI znaky, výběr promptu (oddíl 6) |

## Materiály
Vše staženo z bb.cz 2026-10-30 (animátor, fáze 1). Cesty jsou relativně k `media/projekty/001-bb-chill/` (necommituje se).

| soubor | kde je | použití |
|---|---|---|
| logo SVG: bílý nepravidelný štítek ze dvou nakloněných pruhů (#FEFEFE) + ručně řezané úzké verzálky BAGETERIE / BOULEVARD (#5A3218) | https://www.bb.cz/assets/cs/images/bb_logo_full.svg → `znacka/web/bb_logo_full.svg`, PNG 2000 px `znacka/logo_bb_full_2000.png` | end card, morf ubrus → štítek loga |
| další varianty loga | `znacka/web/`: `logo.png` (183×91), `android-chrome-512x512.png` (logo na žluté), `insta_logo.png` (monogram BB: dva bílé štítky na žlutém kruhu), `safari-pinned-tab.svg` (silueta štítku), přehled `znacka/logo_arch.png` | jen reference |
| data značky pro scénu | `znacka/znacka.json`: barvy s rolemi, fonty, texty, **13 vrcholů bílého štítku** (absolutně ve viewBoxu, ověřeno `logo_kontrola_vrcholu.jpg`), **dělicí přímka** mezi slovy loga (animace slov zvlášť) | podklad pro fázi 2 |
| CSS a HTML webu | `znacka/web/global.css` (barvy, fonty), `fonts.css`, `index.html`, `o-nas.html`, `bagety.html` | zdroj barev, fontů a textů |
| screenshoty webu | `znacka/screeny/` (hlavní, Bagety, O nás; desktop + mobil; cizí domény zablokované) | vzhled a tón značky |
| font „Boulevard“ (proprietární, Boulevard-betaoneBold) | `znacka/font-boulevard-jen-srovnani/` | **jen pro srovnání**, ve videu se nepoužije |
| srovnání fontů | `znacka/fonty_srovnani.png`, `fonty_detail.png`, `fonty_normalizovane.png` (stejná výška verzálek), `typo_test.png` (proměna 200 → 900, šířky textů) | výběr náhrady |
| produktová fotka bagety Caprese | `znacka/produkty-jen-reference/caprese_800.jpg` | **jen reference** kompozice (bageta shora úhlopříčně, náplň vykukuje z boku) a barev jídla, ve videu se nepoužije |
| texty značky (doslova) | titulek a JSON-LD webu: „Nejsme fastfood. Jsme exprès gourmet!“; bb.cz/o-nas: „Fine dining bez bílých ubrusů“, „Vždy čerstvé. Vždy rychlé.“, „Zábava, nadsázka a humor“; bb.cz/produkty/bagety: Caprese = mozzarella, rajčata, pesto genovese, mascarpone, rukola, balsamico | texty na obrazovce (anglicky) |
| hudba | `hudba.wav` + `hudba.json` (nálada `pohodova`, 96 BPM, drop 7,5 s, konec 22,5 s), `hudba_spektrogram.png` | zvuk, časy do `CASY` |

## Režijní list
- **Koncept jednou větou** (finální, F1b: vítěz poroty B + vylepšení): **„Logo BB byla celou dobu bageta.“ Bílý štítek loga
  nedokáže ve švu mezi BAGETERIE a BOULEVARD udržet čerstvou náplň (tlak roste s každou dobou), na dropu jeden tah nože rozkrojí
  logo podél skutečné dělicí přímky slov, na řezu je vidět střída a kůrka a uvnitř stojí Caprese; po servírování náplň zmizí
  rychlostí ALWAYS FAST, prázdné půlky se po sobě podívají a cvaknou zpátky do pixelově přesného loga.**
  - Spojovací prvek: **šev = řez** (dělicí přímka `(0; 32,0) → (101,584; 22,9)` ze `znacka.json`). Je ve všech scénách: náplň z něj
    utíká (0–6,9 s), nůž po něm jede (7,19–7,5 s), rozkrojení (7,5 s), zaklapnutí (13,75 s), druhé polknutí (16,875 s), vytržení
    a prázdné půlky (18,1–19,4 s), mrknutí na zvukové logo (22,34 s), špička rukoly na posledním úderu (24,375 s).
    Stejný řez je jazykem nadpisů (vodorovné rozkrojení, nový nadpis roste z linie řezu) a sdílená slova
    (ALWAYS FRESH → ALWAYS FAST → NOT FAST FOOD.) nesou text bez prolínačky.
  - Logo je **tuhé** celé video: písmena ani obrys se nikdy nedeformují a nikdy neopustí štítek. Půlky se jen posouvají a otáčejí,
    v klidu (0–0,6 · 6,9–7,5 · 19,4–25 s) se kreslí originální `path2` + `path4`.
  - Proč: pointa typu „šipka ve FedEx“ stojí na geometrii vlastního loga (nepřenosná, sdílitelná), humor bez slov odpovídá tónu značky
    („Zábava, nadsázka a humor“), svět je žlutý od snímku 0. Tři „wow“: háček 0,625 s (logo polkne, co mu vykukuje), drop 7,5 s
    (logo se rozkrojí a je to chleba), gag 18,125–19,375 s (náplň je pryč, „kde je?“, cvak zpátky do loga).
  - Porota F1b: B 7,05 (2 hlasy z 3), A 6,98, C 6,38. Převzato: z A přechod přes sdílené slovo FAST, z C groove „každý prvek jen svůj
    nástroj“ (zúžený na servírování v T5), pant / 3D náklon horní půlky a časy událostí z `hudba.json`.
- **Prompt / šablona z prompt-motion** (upraveno režisérem pro finální koncept B):
  1. **Food craving launch film** ([`ultimaxbt-2ddf1e`](https://prompt-motion.com/ultimaxbt-2ddf1e), @ultimaxbt), vzor metody:
     jeden souvislý záběr bez střihů a prolínaček, každá scéna roste z předchozí (u nás vše vychází ze švu loga), text vyjíždí
     z maskovací linky (u nás linka řezu), jedna kamera, nikdy zoom tam a zpět, SFX na každou událost podle změřeného vrcholu, 8 podsnímků u rychlých pohybů.
  2. **Negroni recipe animation** ([`ror-fly-9950f1`](https://prompt-motion.com/ror-fly-9950f1), @Ror_Fly): suroviny pojmenované ve chvíli,
     kdy se objeví → u nás názvy surovin pod logem v aktu 1, jak náplň tlačí na šev.
  3. **Shape morphing through UI states** ([`twoclipping-5cba86`](https://prompt-motion.com/twoclipping-5cba86)): text měněný uvnitř
     měnícího se tvaru má vlastní masku a časování (FRESH → FAST, ALWAYS → NOT FAST FOOD.).
  - **Přeskládání pro 9:16 (A7)**: pohled shora na žlutý „stůl“, pevné pásy podle Vzhledu (nadpisy y 330–600, logo / sendvič y 816–1184,
    názvy surovin y 1360–1440), spodních 400 px a pravých 120 px bez textu. Kamera jen pomalé dotlačení, žádné jízdy do stran.
- **Vzhled** (finální F1b; max 3 barvy + bílá; barvy jídla jen na surovinách, výjimka z G1 schválena):
  - **pozadí žlutá #F0B600 celé video beze změny** (žádný bílý ani stříbrný úvod, žádný barevný převrat; drop nese tvar, ne barva)
  - text a písmena loga **hnědá #5A3218**; ploché stíny = kopie polygonu v hnědé 18 %, posun (6; 10) px v klidu, až (18; 28) px u zvednuté půlky
  - **bílá štítku #FEFEFE** = jen logo a jeho dvě půlky; **krémová #F7F0EB** = lem mozzarelly a mascarpone (aby nesplynuly s bílou)
  - chleba se ukáže **jen na řezu** (nikdy na štítku): pás kůrky #D08B3A 12 px u hrany štítku + pás střídy #F3E3C3 40 px směrem do mezery,
    ve střídě 4 póry #EBC27E (5–7úhelníky 8–14 px); ostatní jídlo: rajče #D7362A / dužina #E8574A, mozzarella #FBF7EE / #EAE3D3,
    rukola #5B7F2B / #3E5A1C, pesto #6E8A2A, balsamico #3A1F10, mascarpone #FFF8EC
  - **jazyk vystřihovánky** (proti klipartu a low-poly): všechny tvary jídla jsou ploché papírové výstřižky s rovnými řezy a nepravidelnými
    úhly jako hrany loga. Rajče max 9 vrcholů, komůrky = 3 vystřižené otvory, ve kterých je vidět vrstva pod nimi (žádná semínka);
    mozzarella 7–8úhelník; rukola 10–12 vrcholů s jedním hlavním zubem; pesto = 6úhelníčky 18 px; balsamico = jediný tah 5 px (ne plocha).
    Dva tóny na surovinu + jeden plochý stín 18 %, žádné fasety, gradienty, záře, odlesky, zrno ani textura. Přesahy přes okraj půlek ≥ 60 px.
  - **font Big Shoulders Display 900** (nadpisy) a **800** (názvy surovin) + **Big Shoulders Text 800 / 600** (bb.cz / disclaimer).
    Velikosti změřené skutečným fontem: NOT FAST FOOD. 130 px = 751 px, ALWAYS FRESH / ALWAYS FAST 130 px (≤ 705 px),
    **EXPRESS GOURMET. 108 px = 767 px** (s kamerou 1,09 = 836 px, nikdy nepřekročí x 960; s NOT FAST FOOD. 130 px tvoří blok stejné šířky),
    názvy surovin Display 800, 64 px (nejdelší PESTO GENOVESE ≈ 400 px), bb.cz Text 800 70 px, disclaimer Text 600 30 px krytí 80 %.
    Řez 200 ani proměna 200 → 900 se v tomto konceptu nepoužívá. Slogan s tečkami (záměrná pointa značky), ALWAYS FRESH / FAST bez tečky (E8).
  - **kompozice 9:16** (souřadnice před kamerou): nadpisy y 330–600 (jeden nadpis, ve finále dvouřádkový slogan), střed x 540;
    **logo / sendvič** šířka 720 px (měřítko 7,088, výška 368 px), střed (540; 1000) → x 180–900, y 816–1184; šev vlevo (201; 1043), vpravo (899; 978);
    názvy surovin pás y 1360–1440 (jen 1,25–6,875 s); bb.cz y ≈ 1275, disclaimer y ≈ 1400; spodních 400 px a pravých 120 px bez textu
    (projede jimi jen grafika: kapka balsamica, vytržená náplň)
  - logo z oficiálního SVG beze změny tvaru; písmo = `path4` dvakrát, ořezané polorovinou podle dělicí přímky (BAGETERIE nad, BOULEVARD pod)
  - kamera: **jedno pomalé dotlačení 1,00 → 1,09** (log měřítko, střed (540; 1000), 1,06 ve 22,5 s), nic jiného; na dropu se nehne,
    žádný zoom tam a zpět, žádný třes. Jediný 3D prvek = náklon `rotateX` horní půlky (perspektiva jen na její skupině).
  - pohyb: příchod ease-out, odchod ease-in, papír dosedá pružinou s překmitem 3 %, velké posuny kriticky tlumené, follow-through vrstev
    náplně 30–40 ms. Swing: události na lichých šestnáctinách +37,5 ms jako v hudbě. Jediný švih + šmouha = vytržení náplně 18,125 s
    (svislá šmouha půlek na dropu je jen podle rychlosti, slabá).
- **Rytmus** (upraveno režisérem pro finální koncept B): hudba `pohodova` (`nastroje/hudba.py`), **96 BPM** (doba 0,625 s, takt 2,5 s),
  25 s = přesně **10 taktů**; **drop 7,5 s** (začátek 4. taktu = rozkrojení loga), **konec 22,5 s** (end card 2,5 s).
  F dur, Fmaj9 – Dm7 – Gm9 – C9 od dropu: úvod obrat vi–ii–V = **stoupající tlak ve švu**, drop přistane na tónice = **rozkrojení**.
  Poslední doba před dropem je nádech (ticho + stoupající šum) = **tah nože po švu**. Událost v obraze na každou dobu.
  Hudba: Rhodes, marimbový motiv (servírování v T5 jde po jeho tónech), prstová basa, tlumená kytara, kopák + malý buben + tleskání na 2 a 4,
  hi-hat se swingem (liché šestnáctiny +37,5 ms), na konci zvukové logo marimby C5–F5–A5 s posledním tónem přesně v 22,5 s.
  Naměřeno ve F1: pásma sub 4,7 / basy 26,9 / středy 64,8 / horní středy 2,2 / výšky 1,2 % (bez varování I7), po `master_zvuk.sh` −13,9 LUFS / −2,4 dBTP po AAC.
  **Úkoly pro zvukaře ve fázi 2**: (1) export událostí po nástrojích do `hudba.json` (zvuk bit po bitu beze změny), (2) vyhladit propad
  1–2 kHz bez změny časování, (3) syntetické SFX podle storyboardu, vrchol přesně na událost.
- **Akceptační kritéria pro kritika**:
  1. 1080×1920, 60 fps, 25,0 s ± 0,1 s, H.264 + AAC
  2. −14 LUFS ±1, true peak ≤ −1 dBTP (po AAC)
  3. Barvy a logo odpovídají bb.cz (logo nezdeformované, barvy z CSS webu)
  4. Snímek 0 je hotový obraz, háček do 1 s, žádný text v bezpečných zónách
  5. Žádné AI poznávací znaky (G6), žádný lineární pohyb, žádné zamrznutí > 1 s bez textu
  6. Hudba je pohodová (≈ 95–105 BPM, durová / feel-good), pásma v mezích (I7), obraz sedí na doby a drop
  7. End card: logo + slogan + bb.cz + disclaimer, drží 1,5–3 s
  8. Texty anglicky, bez překlepů, bez vymyšlených tvrzení

## Storyboard / časová osa
**Finální storyboard F1b** (koncept B „Logo byla celou dobu bageta“ + vylepšení poroty). Časy z `media/projekty/001-bb-chill/hudba.json`:
96 BPM, doba 0,625 s, takt 2,5 s, drop 7,5 s, konec 22,5 s. Akordy: T1 Dm7 · T2 Gm9 · T3 C9 · **T4 Fmaj9 (drop)** · T5 Dm7 · T6 Gm9 ·
T7 C9 · T8 Fmaj9 · T9 Gm9 → C9 (21,25) · T10 Fmaj9. Pohled celou dobu shora na žlutý „stůl“, jedna kamera (dotlačení 1,00 → 1,09).
Souřadnice jsou před kamerou (kamera škáluje kolem (540; 1000)). „Normála švu“ = kolmice na dělicí přímku (sklon −5,1° v SVG).
H = hudba (už je v `hudba.wav`), **SFX = zvukový efekt pro zvukaře, změřený vrchol přesně na čas řádku**, tiše pod hudbou (papír, chléb,
žádné whooshe kromě 18,125 s). SFX syntetizovat v kódu (I5), dokud režisér nerozhodne jinak.
Hudební události po dropu (t0 = začátek taktu): kopák t0, +0,506, +1,563 · tlesknutí +0,625, +1,875 · marimba t0, +0,50625, +0,9375,
+1,875, +2,1875 · kytara +0,9375, +2,1875 · basa t0, +1,13125, +1,5625, +2,1875. Animátor je počítá z `hudba.json` / vzorců `hudba.py`, ne ručně.

| čas (takt · doba) | obraz | text na obrazovce | zvuk / událost |
|---|---|---|---|
| **0,000** (T1 · 1) | **Snímek 0 = náhled** (hotový obraz, test 270 px šířky): žlutá plocha, logo BB 720 px (střed 540; 1000) nakloněné o +2° „provinile“, plochý stín (6; 10). Náplň leží pod štítkem a **přečnívá jen za jeho obrys v koncích švu**: vpravo plátek rajčete Ø 220 px (střed 950; 985, přes okraj ~120 px, natočený 14°), vlevo 3 lístky rukoly ~160 px vějířem (−20° / 0° / +18°) ze (201; 1043) doleva, pod pravým koncem švu visí kapka balsamica Ø 22 px (905; 1012). Štítek je zavřený, pixelově SVG | **„NOT FAST FOOD.“** (Display 900, 130 px, hnědá, střed x 540, účaří y 470) | H: Rhodes Dm7 + marimba · SFX: nic |
| **0,625** (T1 · 2) | **HÁČEK, polknutí**: náplň zajede po směru švu dovnitř pod štítek (rajče doleva 140 px, rukola doprava 170 px, kapka nahoru; 0,18 s ease-in, maska = obrys štítku). Logo poskočí o 8 px nahoru a pružinou 3 % dosedne, náklon +2° → 0° („nic jsem neudělal“). Jen posun a otočení | drží | H: lusknutí · SFX: měkké „glp“ + papírové cvaknutí (vrchol 0,625) |
| 0,9375 (T1 · 2&) | dosednutí, stín se přitáhne na (6; 10) | drží | H: marimba · SFX: nic |
| **1,250** (T1 · 3) | **tlak 1**: z pravého konce švu vyjede plátek rajčete o 110 px (ease-out 0,2 s, po směru švu) a zůstane trčet | z masky pod spodní hranou loga (vodorovná linka y 1230) vyjede dolů **„TOMATOES“** (Display 800, 64 px, účaří y 1430, ease-out 0,25 s) | H: Rhodes · SFX: měkké klouznutí (vrchol 1,25) |
| 1,875 (T1 · 4) | logo rajče **cvakne** zpátky (0,12 s ease-in) a šev zůstane pootevřený o **2 px** (půlky posunuté jen po normále švu; v mezeře je vidět červený proužek náplně = ukazatel tlaku) | drží | H: lusknutí · SFX: papírové „cvak“ |
| **2,500** (T2 · 1) | **tlak 2**: z levého konce švu vyjedou 3 lístky rukoly vějířem (rozjezd 40 ms za sebou, ease-out) | „TOMATOES“ zajede nahoru pod logo (ease-in 0,15 s), pak vyjede **„ROCKET“** (začne až po odchodu starého slova) | H: Gm9, Rhodes + marimba · SFX: šustnutí (vrchol 2,5) |
| 3,125 (T2 · 2) | cvak zpátky, mezera **4 px** (zelený proužek) | drží | H: lusknutí · SFX: cvak (o něco rychlejší) |
| **3,750** (T2 · 3) | **tlak 3**: naráz vpravo jazyk mozzarelly (90 px) a vlevo znovu rukola. Logo se **přikrčí**: posun o 4 px dolů, stín se zkrátí na (3; 5) | **„MOZZARELLA“** (výměna stejně: staré slovo nahoru pod logo, nové dolů) | H: Rhodes · SFX: dvojité klouznutí |
| **4,375** (T2 · 4) | cvak zpátky, mezera **7 px**, ale z pravého konce švu zůstane viset **kapka balsamica**, protáhne se a v 4,55 se odtrhne a padá ease-in spodní zónou z obrazu (pryč do 4,95) | **„BALSAMIC“** | H: lusknutí, marimba · SFX: cvak (4,375) + „plink“ při odtržení (vrchol 4,55) |
| **5,000** (T3 · 1) | **tlak 4**: šev se po celé délce nafoukne na **11 px** (na kopák), v mezeře zelený pruh pesta a podél švu vystrčí 5 šestiúhelníčků pesta po 40 ms zleva doprava | **„PESTO GENOVESE“** | H: C9, jemný kopák, marimba · SFX: tupé „pumf“ (5,0) + 5 drobných ťuků |
| **5,625** (T3 · 2) | **poklička**: horní půlka (BAGETERIE) se nadzvedne o +1,5° kolem levého konce švu (tuhá rotace, kriticky tlumená), z levého konce vyboulí krémový jazyk mascarpone (60 px) | **„MASCARPONE“** (6. surovina, Caprese je kompletní) | H: lusknutí · SFX: tiché „klap“ pokličky |
| **6,250** (T3 · 3) | horní půlka zpět, spodní (BOULEVARD) −1,5° kolem pravého konce; v **6,5625** (swing) znovu horní +2°: chrastění zrychluje | drží | H: Rhodes, začíná stoupající šum · SFX: dvě klepnutí papíru (6,25 a 6,5625) |
| **6,875** (T3 · 4) | **logo se vší silou zavře**: mezera 11 → 0 px (0,15 s, ease-in), všechna náplň zajede dovnitř, logo klesne o 4 px a dosedne (od 7,03 s **originální SVG**, náklon 0°). **Nádech: všechno stojí** | název suroviny zajede nahoru pod logo (pás surovin zůstane prázdný). Na obrazovce jen „NOT FAST FOOD.“ + logo | H: marimba A5, pak ticho + šum · SFX: pevné „cvak“ (6,875), pak nic |
| **7,188–7,500** (T3 · 4&) | **NŮŽ = příčina řezu**: z levého konce švu se po švu kreslí hnědá linka řezu 4 px s trojúhelníkovým hrotem 18 px (stroke-dashoffset, ease-in), hrot doběhne do pravého konce **přesně v 7,500** a vyjede z obrysu o 20 px. Nic jiného se nehýbe | drží | H: marimba G5 (7,188), ticho + šum · SFX: tiché stoupající „sssk“ nože po kůrce, crescendo do 7,5 |
| **7,500** (T4 · 1) **DROP** | **ROZKROJENÍ LOGA**: horní půlka (BAGETERIE) vyskočí po normále švu o 150 px a natočí se −4°, spodní (BOULEVARD) klesne o 120 px a +2°, obě pružinou 3 % (dosednou do 8,0). Horní půlka se zároveň **odklopí `rotateX` 0° → 18°** (vrchol 7,62) **→ 10°** (drží, dokud je sendvič otevřený). **Na řezu obou půlek se ukáže chleba**: pás kůrky 12 px + střídy 40 px s póry (roste z 0 spolu s rozestupem, 7,50–7,62). Mezi půlkami se **postaví Caprese jako vystřihovánka z rozkládací knížky** (vrstvy se sklopí z roviny odspodu nahoru po 30 ms): mascarpone (vlnitý pruh), mozzarella 3×, rajčata 3×, pesto 6×, rukola 5× (přesahy ≥ 60 px přes okraje). Blok y ≈ 660–1310. Stíny půlek odskočí na (18; 28). Slabá svislá šmouha jen na půlkách podle rychlosti. Kamera stojí | „NOT FAST FOOD.“ zatím drží (oko dostane nejdřív pointu loga) | H: **drop Fmaj9**, kopák, činel, marimba C5 · SFX: **křupnutí kůrky (vrchol přesně 7,500)** + trhnutí papíru + 6 tichých papírových „pop“ 7,53–7,68 |
| **7,8125** (T4 · 1&, swing) | sendvič doznívá | **řez nadpisu**: přes střed výšky písmen se 7,70 → 7,8125 nakreslí stejná linka řezu s hrotem (zleva doprava, ease-in); v 7,8125 horní půlky písmen ujedou nahoru, spodní dolů (ease-in 0,25 s, každá ve své masce) a z linie řezu vyroste **„EXPRESS GOURMET.“** (Display 900, **108 px**, účaří y 470; maska se otevírá od řezu oběma směry, ease-out do 8,20) | H: marimba · SFX: menší suché „tsk“ řezu papíru (7,8125) |
| 8,125 (T4 · 2) | náplň se usadí: lístky rukoly dopadnou se zpožděním 40 ms za sebou, plátky se srovnají | „EXPRESS GOURMET.“ drží (čte se do 12,5) | H: tlesknutí · SFX: tiché ťukání papíru |
| 8,750 (T4 · 3) | **balsamico**: tenký klikatý tah 5 px se nakreslí přes náplň zleva doprava (0,35 s, ease-out, konec se zúží) | drží | H: hi-hat, kopák 9,0625 · SFX: tenké „sss“ |
| 9,375 (T4 · 4) | celý otevřený sendvič **kývne** na tlesknutí (10 px dolů a zpět kriticky tlumeně), vrstvy jdou za ním po 35 ms (vlna, ne želé) | drží | H: tlesknutí, marimba F5 E5 · SFX: nic (nese hudba) |
| **10,000** (T5 · 1) | **EXPRESS GOURMET = servírování na marimbu** (groove z C, jen 3 prvky): z rozkládací „hromádky“ se náplň srovná do gurmánské řady Caprese podél řezu. Na každý tón marimby dojede jeden plátek na své místo (ease-out 0,18 s, vrchol dojezdu přesně na tónu, dotočení na 0° pružinou 3 %): **10,000 rajče** | drží | H: Dm7, kopák, basa, marimba · SFX: měkké „tup“ plátku (10,0) |
| 10,50625 / 10,9375 (T5 · 1a / 2&) | 10,506 mozzarella, 10,9375 rajče (střídavá řada rajče / mozzarella jako na fotce Caprese z bb.cz). Mezi tím **10,625 sendvič kývne** na tlesknutí (10 px) | drží | H: marimba, tlesknutí 10,625, kytara 10,9375 · SFX: „tup“ na 10,506 a 10,9375 |
| 11,250 (T5 · 3) | **pesto se srovná** do přesné řady 6 teček nad řadou plátků (každá tečka poskočí o 12 px na své místo po 30 ms, lichá o 37,5 ms později = swing), parodie na fine dining | drží | H: hi-hat, basa 11,13 · SFX: 6 drobných ťuků |
| 11,875 / 12,1875 (T5 · 4 / 4&) | 11,875 mozzarella na místo + sendvič kývne (10 px), 12,1875 poslední rajče dosedne: **řada je dokonale naservírovaná** | drží | H: tlesknutí, marimba, kytara 12,1875 · SFX: „tup“ (11,875) a o tón vyšší „tup“ (12,1875) |
| **12,500** (T6 · 1) | lístky rukoly **cvrnknou nahoru** (+12° a zpět pružinou, 5 lístků po 40 ms) = čerstvost obrazem | **řez nadpisu** (stejně jako 7,8125: linka s hrotem 12,40 → 12,50, půlky písmen ven ease-in 0,25 s), z řezu vyroste **„ALWAYS FRESH“** (Display 900, 130 px, účaří y 470, ease-out do 12,88) | H: Gm9, kopák, marimba · SFX: svěží šustnutí (12,5) + „tsk“ řezu |
| 13,125 (T6 · 2) | z pravého konce tahu balsamica se utvoří kapka, protáhne se a v 13,30 odkápne přes spodní půlku dolů z obrazu (ease-in, pryč do 13,7) = ozvěna 4,55 | drží | H: tlesknutí · SFX: „plink“ při odtržení (13,30) |
| **13,750** (T6 · 3) | **ZAKLAPNUTÍ**: horní půlka se překlopí zpět (`rotateX` 10° → 0°) a sjede po normále švu o 150 px dolů (0,3 s, ease-in, náraz přesně 13,75), spodní půlka se vrátí o 120 px nahoru; pásy chleba se zúží na 0. Náplň se stlačí zpět pod štítek a **přečnívá přesně jako ve snímku 0** (rajče vpravo 120 px, rukola vlevo), jen bez náklonu. Spodní půlka při nárazu klesne o 6 px a dosedne | drží | H: kopák 14,06 · SFX: měkké „bum“ chleba (vrchol 13,75) |
| 14,375 (T6 · 4) | usazení (stín zpět na (6; 10)); v **14,6875** se lístky rukoly vlevo jednou zhoupnou na kytaru (6°) | drží | H: tlesknutí, kytara 14,6875, otevřený hi-hat · SFX: nic |
| **15,000** (T7 · 1) | **čerstvé to uvnitř nevydrží**: rukola vlevo vyjede o dalších 70 px a zhoupne se | „ALWAYS FRESH“ drží | H: C9, kopák, marimba · SFX: šustnutí |
| 15,625 (T7 · 2) | vpravo pod rajčetem vyklouzne jazyk mozzarelly (80 px) | drží | H: tlesknutí · SFX: měkké klouznutí |
| 16,250 (T7 · 3) | šev se pootevře o 4 px a podél něj vystrčí 3 šestiúhelníčky pesta | drží | H: hi-hat · SFX: 3 ťuky |
| **16,875** (T7 · 4) | **druhé polknutí** (ozvěna háčku): všechno naráz zajede dovnitř (0,18 s ease-in), šev 0 px, logo poskočí o 6 px a dosedne. Od 17,0 s je to čisté logo bez náplně | drží | H: tlesknutí, marimba A5 · SFX: **stejné „glp“ jako 0,625** |
| **17,500** (T8 · 1) | **servírováno**: horní půlka se odklopí jako víko (`rotateX` 0° → 10°) a zvedne o 110 px po normále švu (ease-out 0,3 s); pásy chleba se ukážou a uvnitř leží naservírovaná řada Caprese (stav z 12,19) | **sdílené slovo ALWAYS**: ALWAYS stojí, jen FRESH se vodorovně rozkrojí (linka 17,40 → 17,50) a z řezu vyroste **FAST** (ease-out do 17,85); pak se řádek dorovná na střed (posun ~20 px, ease-in-out 0,3 s) | H: Fmaj9, kopák, marimba C5 · SFX: papírové „tsk“ víka (17,5) |
| **17,8125** (T8 · 1&) | **nápřah**: celá náplň se posune o 8 px doleva (ease-out 0,12 s) a stojí | drží | H: marimba · SFX: tiché „ťk“ |
| **18,125** (T8 · 2) | **VYTRŽENÍ** (jediný švih a jediná výrazná šmouha ve videu): celá náplň jako jeden celek vystřelí doprava a **za 4 snímky (18,125–18,192) je celá za pravým okrajem** (ease-in, vodorovná šmouha podle rychlosti jen na náplni, `--sub 8`). Půlky zůstanou s prázdnou mezerou 110 px a pásy prázdné střídy; horní sebou trhne o 10 px doprava a pružinou se vrátí | drží | H: tlesknutí · SFX: krátké „zip“ 150 ms, **vrchol 18,15** |
| **18,750** (T8 · 3) | **„kde je?“**: prázdné půlky se natočí k sobě (horní −6°, spodní +4°, ease-out 0,25 s) a **stojí přesně 1 dobu** v naprostém klidu (stín ukazuje prázdnou mezeru) | drží | H: tichá doba · SFX: **nic, ticho je pointa** |
| **19,375** (T8 · 4) | půlky **cvaknou k sobě** (horní `rotateX` 10° → 0°, pásy chleba na 0, ease-in 0,15 s): **čisté logo přesně podle SVG**, poskok o 6 px a dosednutí (od 19,55 kreslit originální `path2` + `path4`) | drží | H: tlesknutí, marimba F5 · SFX: suché papírové „cvak“ (19,375) |
| **20,000** (T9 · 1) | logo jedním pohybem do polohy end cardu: střed (540; 1000) → (540; 960), měřítko 1,00 → 1,06 (0,6 s, ease-in-out, kriticky tlumené, bez překmitu) | **sdílené slovo FAST** (z konceptu A): ALWAYS odjede ease-in doleva za okraj (20,00–20,30), FAST se posune na své místo v novém řádku (20,15–20,55, ease-in-out), NOT přijede zleva (start až 20,30) a FOOD. zprava, ease-out, vše stojí v 20,625 → **„NOT FAST FOOD.“** (130 px, účaří y 470) = ozvěna snímku 0 | H: Gm9, kopák, marimba B5 · SFX: dvě měkká papírová posunutí (vrchol 20,3 a 20,625) |
| 20,625 (T9 · 2) | logo dosedne (stín (6; 10)) | drží | H: tlesknutí, marimba · SFX: nic |
| **21,250** (T9 · 3) | logo v klidu, kamera dotlačuje | pod NOT FAST FOOD. se v y 561 nakreslí linka řezu s hrotem (21,15 → 21,25) a z ní vyroste **„EXPRESS GOURMET.“** (108 px, účaří y 600, ease-out do 21,64): slogan je celý, oba řádky stejně široké (751 / 767 px) | H: C9, marimba E5 · SFX: „tsk“ řezu (21,25) |
| 21,875 (T9 · 4) | ze spodní hrany loga vyjede (stejné gesto jako názvy surovin v aktu 1: maska pod logem) | **„bb.cz“** (Text 800, 70 px, účaří y 1290, ease-out 0,3 s) | H: tlesknutí · SFX: tiché papírové „šk“ |
| 22,188 / **22,344** | 22,188: nic nového (čte se). **22,344 (F5): šev mrkne**: půlky se po normále rozestoupí o 2 px a za 0,15 s zavřou (od 22,5 přesné SVG) | drží | H: zvukové logo marimby C5 (22,188), F5 (22,344) · SFX: drobné „ťk“ na 22,344 |
| **22,500–25,000** (T10) **END CARD** | na A5 logo jen dosedne (4 px dolů a zpět, kriticky tlumeně). Pak drží: nahoře slogan, uprostřed logo (pixelově SVG), pod ním bb.cz a disclaimer; kamera dál dotlačuje 1,06 → 1,09 (žádný zamrzlý snímek). **Tečka (button) 24,375**: z pravého konce švu vykoukne špička jednoho lístku rukoly o 30 px (ease-out 0,25 s, pak stojí) = poslední úsměv a návrat ke snímku 0 (D4). *Podmíněno výjimkou z C6, viz otázka pro režiséra; bez výjimky se vynechá.* | „NOT FAST FOOD. / EXPRESS GOURMET.“ + logo + „bb.cz“ + **„Concept ad · not affiliated with Bageterie Boulevard“** (Text 600, 30 px, krytí 80 %, účaří y 1400; najede 22,5–22,9: krytí 0 → 80 % + posun 6 px nahoru, ease-out) | H: A5 přesně 22,500, finální Fmaj9 + kopák + tlesknutí + jemný činel, doznění do 25,0 · SFX: měkký dopad loga (22,5), na 24,375 tiché šustnutí lístku |

**Pořadí stavby (fáze 2)**: nejdřív jen statické klíčové snímky **0,0** a **8,4** (schválit test 1 sekundy: přečte se jídlo / přečte se bageta?),
pak drop 7,19–8,2, pak zbytek. Bez schválení 8,4 nevzniká žádný pohyb.

**Kontrolní snímky pro fázi 2** (`--nahled casy --casy 0,0.72,1.4,2.7,3.9,4.55,5.1,5.8,6.4,7.0,7.4,7.52,7.56,7.62,7.95,8.4,10.7,12.3,12.7,13.9,16.4,17.7,18.13,18.15,18.17,18.19,18.9,19.6,20.4,21.7,22.36,23.5,24.98`)
+ snímek na každou dobu (`--nahled doby --bpm 96`) + pás sousedních snímků u 0,625 / 7,5 / 13,75 / 18,125 / 19,375.

| čas | co musí být vidět | odmítnout, když |
|---|---|---|
| 0,0 (+ zmenšenina 270 px) | žlutá, logo s jasně vykukujícím rajčetem, rukolou a kapkou, NOT FAST FOOD. | na zmenšenině nejde poznat jídlo; vypadá to jako „úvodní logo“ |
| 0,72 | uprostřed polknutí | logo se deformuje (povolen jen posun a otočení), náplň prosvítá štítkem |
| 1,4 / 2,7 / 3,9 / 5,1 | stoupající tlak: náplň v koncích švu, mezera 2 / 4 / 7 / 11 px, název suroviny pod logem | písmena opustí štítek, název je v zóně y > 1520, dvě slova naráz |
| 7,0 | **logo přesně podle SVG** (překrýt `logo_bb_full_2000.png` s průhledností 50 %) | posun > 1 px, jiný tvar, zbytky náplně |
| 7,4 | linka nože v půlce švu, hrot čitelný | linka přejede písmeno, hrot vypadá jako šipka UI |
| 7,52 / 7,56 / 7,62 | rozkrojení: půlky v letu, pás kůrky a střídy roste, vrstvy náplně se stavějí; nadpis ještě celý | šmouha smaže písmena loga, náplň vypadá jako výbuch částic, pás chleba zasahuje do bílého štítku |
| 7,95 | nadpis rozkrojený, EXPRESS GOURMET. roste z řezu | dvojitá hrana nebo mezera mezi půlkami písmen |
| **8,4** | **klíčový snímek**: otevřený logo-sendvič (chleba na řezu, Caprese, rukola přes okraje) + EXPRESS GOURMET. | čte se jako papír / rozpadlé logo, ne jako bageta; low-poly fasety; přeplněné |
| 10,7 / 12,3 | servírování v půlce / hotová střídavá řada rajče–mozzarella + pesto v řadě | plátky se překrývají chaoticky, řada není rovnoběžná s řezem |
| 12,7 | ALWAYS FRESH roste z řezu, rukola v cvrnknutí | starý a nový nadpis naráz |
| 13,9 | zavřeno, náplň přečnívá jako ve snímku 0 | BAGETERIE / BOULEVARD nečitelné, mezera ve švu |
| 16,4 | pesto a mozzarella vykukují, ALWAYS FRESH | – |
| 17,7 | víko otevřené, řada Caprese, ALWAYS FAST | FRESH a FAST přes sebe |
| 18,13–18,19 | 4 snímky vytržení: šmouha jen vodorovně a jen na náplni, v 18,19 náplň celá za pravým okrajem | duchové, náplň v půlce obrazu ještě ostrá, šmouha na půlkách |
| 18,9 | prázdné půlky natočené k sobě, prázdná střída | gag nejde poznat bez zvuku |
| 19,6 | čisté logo (překrytí s PNG) | jakákoli odchylka od SVG |
| 20,4 | přechod přes FAST: ALWAYS mimo, NOT / FOOD. na cestě | NOT překrývá odcházející ALWAYS |
| 22,36 | mrknutí švu 2 px | víc než 2 px, tvar loga jiný |
| 23,5 / 24,98 | end card: slogan, logo, bb.cz, disclaimer v zónách (s kamerou 1,09 nic za x 960, nic nad y 250 a pod y 1520) | přeplněné, disclaimer nečitelný, logo jiné než SVG |

**Pasti projektu** (do `<pasti>` kostry, oddíl 10):
1. **Logo je tuhé.** Prvky s písmem loga jen `translate` / `rotate` / stejnoměrné `scale` (+ `rotateX` horní půlky max 18°, jen v otevřeném stavu
   7,5–13,75 a 17,5–19,375). V klidu (0–0,6 · 7,03–7,5 · 19,55–25 s) kreslit originální `path2` + `path4`, ne interpolovaný polygon.
   Žádný 120bodový morf, žádná bublina ani čepice: obrys štítku se nikdy nemění, jen se rozdělí na dvě půlky.
2. **Půlky** = 13úhelník ze `znacka.json` rozdělený dělicí přímkou na dva polygony + `path4` dvakrát s `clipPath` polorovinou. Vlevo má přímka
   rezervu jen ~0,2 jednotky viewBoxu: kontrolní zvětšenina levého konce (jako `logo_kontrola_deleni_vlevo.jpg`), nesmí se uříznout kus písmena.
3. **Pořadí vrstev (z-index)**: stín → náplň (celá pod štítkem, přečnívá jen za obrys, v mezeře švu je vidět) → pásy kůrky a střídy →
   bílé půlky → písmena → linka nože. Nadpisy, názvy surovin a bb.cz ve vlastní vrstvě nad tím. Díky pořadí není potřeba maska náplně.
4. **Chleba jen na řezu**: pásy kůrky a střídy leží vně bílého štítku na straně mezery, jejich tloušťka = min(52 px, polovina mezery);
   v zavřeném stavu 0. Na bílý štítek se nikdy nekreslí kůrka ani zářezy.
5. **Mezera ve švu v aktu 1** (2 / 4 / 7 / 11 px) = posun půlek po normále švu, ne roztažení. Proužek v mezeře = barva suroviny, která právě tlačí.
6. **Jeden švih**: jen vytržení 18,125 (4 snímky, celá náplň za pravým okrajem v 18,192). Rozmazání v kódu jen vodorovně na skupině náplně
   (`rozmazani()`), když bude SVG filtr pomalý, rasterizovat náplň do `<canvas>`. Na dropu jen slabá svislá šmouha půlek podle rychlosti.
   Render celého videa `--fps 60 --sub 8 --dur 25` (~13–14 min). Duchy řešit prodloužením na 5 snímků, ne silnějším rozmazáním.
7. **Dva řezy nikdy ve stejném snímku**: logo 7,500, nadpis 7,8125. Odcházející text zmizí dřív, než příchozí obsadí místo (FRESH → FAST,
   ALWAYS → NOT, názvy surovin pod logem). Každý měněný text má vlastní masku a časování.
8. **Rozkrojený nadpis**: dvě kopie stejného textu s `clip-path: inset(…)`, stejný `top`, překryv 1 px, celé pixely; linka řezu má tutéž
   tloušťku 4 px a hrot 18 px jako nůž na logu (jeden jazyk). Linka zmizí s půlkami písmen, nezůstává viset.
9. **Velikosti a zóny s kamerou**: kamera končí na 1,09, proto EXPRESS GOURMET. nejvýš **108 px** (767 px → 836 px), nic za x 960,
   nad y 250 a pod y 1520 ani ve 24,98 s. Ověřit `?mrizka` na snímcích 8,4 / 12,7 / 23,5 / 24,98.
10. **Bílá na bílé**: mozzarella a mascarpone mají krémový lem #F7F0EB / #EAE3D3 a vlastní plochý stín, jinak splynou s půlkami.
11. **Vystřihovánka, ne klipart ani low-poly**: limity vrcholů (rajče ≤ 9, rukola 10–12, mozzarella 7–8), 2 tóny na surovinu, žádné fasety,
    tvary rukoly z `nahoda(seed)`. Náplň se staví sklopením z roviny, nikdy nevyletí z bodu (žádný výbuch částic, drobky, pára).
12. **Groove bez „klepání“**: v T5 se hýbou jen 3 věci (plátky na marimbu, pesto jednou, sendvič kývne na 2 a 4). Když nástroj nehraje,
    prvek stojí. Časy z `hudba.json` / vzorců `hudba.py` (swing lichých šestnáctin +37,5 ms), nikdy ručně přepsané.
13. **Fonty**: `document.fonts.load` pro `900 130px` a `800 64px "Big Shoulders Display"`, `800 70px` a `600 30px "Big Shoulders Text"`
    před měřením a před `seek(0)` (C016). Žádné `will-change` na prvky, které kamera škáluje (C004). Náhoda jen `nahoda(seed)`.
14. **3D jen jedna skupina**: `perspective` (1600 px) jen na skupině horní půlky, osa `rotateX` = její vzdálenější (horní) hrana; kamera
    zůstává 2D. Kontrola, že v SwiftShaderu nevznikají zubaté hrany (případně `rotateX` nahradit svislým `scaleY` jen u pásu chleba, ne u písma).
15. **SFX podle změřeného vrcholu**, ne začátku souboru (křupnutí 7,500, zip 18,15, cvak 19,375, glp 0,625 a 16,875). Ticho 18,75–19,375
    nesmí nic vyplnit. Mix −14 LUFS / ≤ −1 dBTP po AAC (`master_zvuk.sh`), zvukař zároveň vyhladí propad 1–2 kHz z výhrady režiséra.

## Průběh výroby
| kolo | kdo | co se dělalo | verdikt kritika | hlavní nálezy |
|---|---|---|---|---|
| F1 | animator | značka z bb.cz (barvy z CSS, logo SVG + 13 vrcholů štítku, font Big Shoulders), nálada hudby `pohodova`, koncept + storyboard | režisér: **schváleno** s výhradou ke spektru hudby | barvy ověřeny v CSS (#F0B600 136×, #5A3218 = --brown), hudba 25,000 s, drop +7 dB, propad 2 kHz |
| F1b | porota (3 kreativní ředitelé) + syntéza | výběr konceptu ze 3 návrhů (A ubrus, B rozkrojené logo, C kapela surovin) + finální storyboard | vítěz **B** (2 hlasy ze 3) | skóre B 7,05 · A 6,98 · C 6,38; zapracováno: akt 1 = stoupající tlak ve švu místo bubliny a čepice (logo tuhé), nůž jako příčina řezu, chleba na řezu, řez nadpisu o swingovou osminu později, servírování na marimbu místo cedulky menu, sdílená slova ALWAYS / FAST, větší náplň ve snímku 0, EXPRESS GOURMET. 108 px |
| V1 (kolo 1) | zvukař, animátor (klíčové snímky → kreativní ředitel 7,1 → oprava → pohyb a render), střihač, 3 kritici | první celé video 25 s | **OPRAVIT** (wow 6,9; technika, zadání: OPRAVIT) | hrdina malý na telefonu a prázdná spodní polovina; zvuk nenese drop, zip ani ticho gagu (SFX o 11–15 dB pod hudbou, hudba nemlčí); tlak ve švu v aktu 1 neviditelný; servírování nečitelné; zaklapnutí zplácne náplň; řezy nadpisů se kříží do „NXT EAST“; polknutí 3 snímky; šmouha na textu 20,1–20,4; pesto přes písmena loga. Všechna pravidla uživatele splněna. Režisér upravil I3 a přidal A8 |

## Chyby během výroby
- C016 (fonty z Google se nestáhly před měřením, opraveno, prevence v `scena.html`), C017 (příliš tmavý mix pohodové hudby, kontrola pásem ho neodhalí)

## Spotřeba tokenů
| agent / úkol | tokeny | akce nástrojů | čas |
|---|---|---|---|
| animator: fáze 1 (značka, hudba, koncept) | 403 696 | 114 | 40,7 min |
| workflow koncept (obnovený běh: návrhy B + C, 3 porotci, syntéza) | 486 830 | 81 | 20,6 min |
| zastavený agent C v prvním běhu (3× limit výstupu, nic nezapsal, C018) | ~694 000 (z transkriptu: výstup 386 590 + vstup 307 903) | – | 70 min, ztráta |
| workflow výroba, 1. pokus (zvukař + animátor, přerušeno limitem účtu po ~7 min, C020) | 234 247 | 52 | 7,6 min |

## Verze
| verze | datum | soubor / kam doručeno | změny |
|---|---|---|---|

## Zpětná vazba (doslova)

## Poučení
