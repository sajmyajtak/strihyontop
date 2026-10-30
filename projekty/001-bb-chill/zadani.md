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
- **Výhrada režiséra k hudbě**: v nezávislém měření je mezi oktávami 1 kHz a 2 kHz propad ~13 dB (oktávy rel.: 500 Hz 0, 1 kHz −2,7,
  2 kHz −15,6, 4 kHz −13,9 dB). Jas na telefonu chybí → zvukař ve fázi 2 vyhladí (sousední oktávy 250 Hz–8 kHz max ~8 dB od sebe).

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
- **Koncept jednou větou** (návrh animátora, schvaluje režisér): **„Fine dining bez bílých ubrusů“ doslova: spot začne na bílém ubrusu
  s poklopem, na dropu ubrus strhneme jako kouzelník, gurmánská bageta zůstane ležet ve žlutém světě BB a ten samý ubrus se vrátí
  jako obal s sebou a nakonec se složí do bílého štítku loga.**
  - Spojovací prvek: **bílý ubrus** (ubrus → strhnutí → papír s sebou → štítek loga) a **bageta** jako jediná „postava“ na obrazovce od 0,6 s do konce.
  - Proč: je to vlastní věta značky (bb.cz/o-nas), humor odpovídá jejímu tónu („Zábava, nadsázka a humor“), drop má fyzický důvod
    (trik s ubrusem) a převrat bílá → žlutá je zároveň odhalení značky. Tři „wow“ momenty: strhnutí ubrusu s proměnou písma (drop),
    návrat ubrusu jako obalu (překvapivý návrat motivu), papír → štítek loga (pointa značky).
- **Prompt / šablona z prompt-motion**:
  1. **Food craving launch film** ([`ultimaxbt-2ddf1e`](https://prompt-motion.com/ultimaxbt-2ddf1e), @ultimaxbt), hlavní vzor metody:
     jeden souvislý záběr bez střihů a prolínaček, každá scéna roste z předchozí, **drop = zaplavení barvou z objektu**
     (u nás odjezd ubrusu odhalí žlutou), text vyjíždí z maskovací linky, sdílené prvky při předání, jedna kamera, nikdy zoom tam a zpět,
     SFX na každou událost podle změřeného vrcholu, 8 podsnímků u rychlých pohybů. Je to navíc příběh o jídle.
  2. **Negroni recipe animation** ([`ror-fly-9950f1`](https://prompt-motion.com/ror-fly-9950f1), @Ror_Fly): struktura „od prázdné sklenice
     po hotový drink“, suroviny pojmenované ve chvíli, kdy přibývají → u nás servírování bagety Caprese surovinu po surovině na doby.
  - Pasti převzaté: zaplavení musí dosáhnout nejvzdálenějšího rohu za ~0,3–0,35 s (jinak záblesk); z-index všech vrstev; 4 podsnímky
    dělají duchy → rychlé úseky `--sub 8`; proměnné deklarovat před prvním `seek()`; text měněný uvnitř měnícího se tvaru má vlastní
    masku a časování (`twoclipping-5cba86`: FRESH → FAST, papír → štítek); `will-change` nikdy na prvky, které kamera škáluje.
  - **Přeskládání 16:9 → 9:16 (A7)**: Food craving je 1920×1078 s telefonem uprostřed a bočními jízdami. U nás je celý svět **shora**
    (top-down jako produktové fotky bb.cz) a skládá se svisle do tří pevných pásů po celé video: **y 300–600 nadpisy**, **y 650–1400 talíř / bageta**,
    y 1380–1500 drobný text; spodních 400 px bez textu (tudy jen odjíždí a vrací se ubrus). Kamera nejezdí do stran.
- **Vzhled** (max 3 barvy + černá/bílá; barvy jídla jen na surovinách, viz otázka pro režiséra):
  - pozadí světa BB **žlutá #F0B600** (nejčastější barva CSS webu, 136×: nadpisy, odkazy, patička; header #E7B200 je varianta);
    úvod „fine dining“ **bílá #FFFFFF** se záhyby v **krémové #F7F0EB** (CSS --page-bg)
  - text **hnědá #5A3218** (CSS --brown a písmena loga; #583119 v textu webu je okem stejná)
  - akcent **bílá štítku #FEFEFE** (ubrus, papír, štítek loga); neutrální jen v úvodu stříbrná #C9CED3 / stín #9AA1A8 (poklop, příbory)
  - jídlo, stylizováno podle fotky Caprese z bb.cz: kůrka #D08B3A, stín #A8601E, zářez #EBC27E, střída #F3E3C3, rajče #D7362A
    (dužina #E8574A), mozzarella #FBF7EE (stín #EAE3D3), rukola #5B7F2B / #3E5A1C, pesto #6E8A2A, balsamico #3A1F10, mascarpone #FFF8EC
  - stíny ploché, hnědá #5A3218 s krytím ~18 %; žádné gradienty, záře, odlesky ani zrno
  - **font: Big Shoulders Display** (Google Fonts, variabilní wght 100–900, latin-ext) místo proprietárního „Boulevard“ z webu:
    při stejné výšce verzálek je řez 900 jen o 3 % užší, má stejně hranatě zaoblená O / G / U, plochá zakončení a podobnou tloušťku tahu
    (Mohave a Barlow Condensed vyšly širší a měkčí, Antonio a Bebas užší a slabší; `znacka/fonty_normalizovane.png`).
    Řezy: **200** s prostrkáním 0,14 em (elegantní „fine dining“) a **900** (hlas BB). **Na dropu proměna 200 → 900** po ose wght:
    šířka nadpisu zůstane ±1 %, písmena „ztloustnou“ na místě (`znacka/typo_test.png`). Drobný text (bb.cz, disclaimer):
    **Big Shoulders Text 600–800** (sesterská rodina pro malé velikosti).
  - velikosti: nadpisy 112–150 px, max šířka 900 px („EXPRESS GOURMET.“ nejvýš ~118 px, při 130 px zasahuje do pravé zóny),
    řádek menu 54 px (200, prostrkání 0,16 em), bb.cz 70 px, disclaimer 30 px
  - logo z oficiálního SVG beze změny tvaru; slova BAGETERIE / BOULEVARD jdou animovat zvlášť maskou podle dělicí přímky ze `znacka.json`
  - kamera: **jedno pomalé dotlačení přes celé video (1,00 → ~1,10)**, nic jiného; na dropu žádný pohyb kamery (energii nese ubrus,
    barva a ztučnění písma); detail náplně v taktu 5 = bageta se sama natočí a zvedne ke kameře
- **Rytmus**: hudba `pohodova` (`nastroje/hudba.py`), **96 BPM** (doba 0,625 s, takt 2,5 s), 25 s = přesně **10 taktů**;
  **drop 7,5 s** (začátek 4. taktu, 30 % délky), **konec 22,5 s** (end card 2,5 s). F dur, Fmaj9 – Dm7 – Gm9 – C9 počítané od dropu:
  úvod je obrat vi–ii–V (napětí, „fine dining“), drop přistane na tónice (uvolnění = žlutá). Poslední doba před dropem je nádech
  (ticho + stoupající šum) = napětí ubrusu. Událost v obraze na každou dobu, nová myšlenka každé 2–4 doby.
  Hudba: Rhodes, marimbový motiv, prstová basa, tlumená kytara na 2& a 4&, kopák + malý buben + tleskání na 2 a 4, hi-hat šestnáctiny se swingem;
  na konci zvukové logo marimby C5–F5–A5, poslední tón přesně v 22,5 s. Naměřeno: pásma sub 4,7 / basy 26,9 / středy 64,8 / horní středy 2,2 / výšky 1,2 %
  (bez varování I7), po `master_zvuk.sh` −13,9 LUFS / −2,4 dBTP po AAC.
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
Návrh animátora (fáze 1), časy z `media/projekty/001-bb-chill/hudba.json`: 96 BPM, doba 0,625 s, takt 2,5 s, drop 7,5 s, konec 22,5 s.
Pohled celou dobu **shora** (top-down). Pásy: nadpisy y 300–600, talíř / bageta y 650–1400, drobný text y 1380–1500.
Zvuk: H = hudba (už je v `hudba.wav`), SFX = návrh jemného efektu pro zvukaře (vrchol přesně na událost, tiše pod hudbou).

| čas (takt · doba) | obraz | text na obrazovce | zvuk / událost |
|---|---|---|---|
| **0,000** (T1 · 1) | **Snímek 0 = náhled**: bílý ubrus s jemnými krémovými záhyby přes celý obraz, uprostřed bílý talíř se stříbrným poklopem, vlevo vidlička, vpravo nůž | „FINE DINING“ (Big Shoulders 200, prostrkání 0,14 em, hnědá, ~150 px) | H: úvod Dm7, Rhodes, lusknutí, shaker, cinknutí marimby |
| 0,625 (T1 · 2) | **Háček**: poklop se zvedne ke kameře (zvětší se, stín se oddálí, odjede nahoru z obrazu, ease-in) → na talíři rozevřená bageta: spodní půlka střídou nahoru, vrchní kůrkou nahoru vedle ní | | SFX: kovové „cink“ poklopu |
| 1,250 (T1 · 3) | mascarpone: kuchařský „šmouh“ krému podél střídy (tah se nakreslí jedním pohybem) | pod talířem začne řádek menu „MASCARPONE“ (200, 54 px) | SFX: měkký šmouh |
| 1,875 (T1 · 4) | mozzarella: 3 plátky dopadnou shora (začnou větší a rozostřené, zmenší se na střídu, stín se přitáhne), po 60 ms | „· MOZZARELLA“ | SFX: 3 tiché plopy |
| 2,500 (T2 · 1) | rajčata: 3 plátky mezi mozzarellu (jako na fotce Caprese z bb.cz) | „· TOMATOES“ | H: Gm9 · SFX: plop |
| 3,125 (T2 · 2) | pesto genovese: řada přesných zelených teček (parodie na fine dining), naskakují zleva doprava | „· PESTO GENOVESE“ | SFX: drobné ťuky |
| 3,750 (T2 · 3) | rukola: 4 lístky dopadnou s mírným natočením | „· ROCKET“ | SFX: šustnutí |
| 4,375 (T2 · 4) | balsamico: tenká klikatá čára se nakreslí přes náplň | „· BALSAMIC“ (menu je kompletní, 2 řádky) | |
| 5,000 (T3 · 1) | vrchní půlka se překlopí kolem podélné osy a zavře bagetu; náplň vykukuje z boku jako na produktových fotkách bb.cz | | H: C9, jemný kopák · SFX: měkké „bum“ chleba |
| 5,625–6,250 (T3 · 2–3) | klid, kamera pomalu dotlačuje; v 6,25 se cípy ubrusu napnou a cuknou o 4 px dolů (první předzvěst) | „FINE DINING“ + menu | H: stoupající šum · SFX: šustnutí látky |
| 6,875 (T3 · 4) | druhé cuknutí (8 px), příbory se zachvějí | | H: předtakt marimby A5 G5 · SFX: cinknutí příborů |
| 7,19–7,50 | nádech: všechno stojí | | H: ticho + šum |
| **7,500** (T4 · 1) **DROP** | **STRHNUTÍ UBRUSU** (jediný švih ve videu): ubrus odjede dolů z obrazu za ~0,3 s se svislou šmouhou podle rychlosti; s ním talíř (lehce se pootočí, opožděně), příbory a řádek menu. Horní hrana ubrusu přejede celý obraz a odhalí **žlutou #F0B600** až do dolních rohů. Bageta zůstane ~2 snímky ve vzduchu a dopadne na žlutý stůl (~7,7 s, stlačení ≤ 4 %, stín se přitáhne) | „FINE DINING“ ztuční **200 → 900** a prostrkání 0,14 → 0 em za 0,3 s (šířka stejná) | H: drop Fmaj9, plná drážka, jemný činel · SFX: „fwip“ látky + vzdalující se cinknutí nádobí, žuchnutí bagety |
| 8,125 (T4 · 2) | bageta se usadí | pod nadpis vyjede z maskovací linky „WITHOUT THE WHITE / TABLECLOTHS“ (900, 112 px), čte se do 9,9 s | H: tlesknutí na 2 |
| 8,75–9,375 | kamera dotlačuje, nic nového (čte se) | | |
| **10,000** (T5 · 1) | nadpis odjede nahoru (ease-in 0,3 s); bageta se natočí do hrdinské úhlopříčky a zvedne ke kameře k boku s náplní | „ALWAYS FRESH“ vyjede z masky v 10,3 | H: Dm7 |
| 10,625 / 11,25 / 11,875 | na každou dobu drobná živá událost v náplni: lístek rukoly se narovná, plátek rajčete dosedne, druhý lístek | | SFX: jemné ťuky |
| **12,500** (T6 · 1) | **ubrus se vrátí** ze spodního okraje stejnou cestou, kudy odjel, podjede pod bagetu a zabalí ji jako papír s sebou: 12,5 levý cíp přes bagetu, 13,125 pravý cíp, 13,75 konce se zakroutí | „ALWAYS FRESH“ → „ALWAYS FAST“: ALWAYS zůstane, FRESH odjede dolů, FAST vyjede (vlastní maska) | H: Gm9 · SFX: šustnutí papíru na každý přehyb |
| 14,375 (T6 · 4) | zabalená bageta se usadí (pružina 3 %) | | |
| **15,000** (T7 · 1) | balíček leží ve středu, na doby se v drážce jemně pohupuje (≤ 2 %, žádné údery) | „ALWAYS“ odjede vlevo, „FAST“ se posune a z boků přijedou „NOT“ a „FOOD.“ → **„NOT FAST FOOD.“** (sdílené slovo FAST = přechod textu bez prolínačky) | H: C9 · SFX: ťuk |
| **17,500** (T8 · 1) | kamera dál pomalu dotlačuje | pod něj vyjede z masky **„EXPRESS GOURMET.“** (~118 px) → slogan kompletní, drží do konce | H: Fmaj9 |
| **20,000** (T9 · 1) | balíček se rozbalí (cípy odletí, konce se rozkroutí) a bageta leží naservírovaná; **papír se zvedne a cestou nahoru se složí do bílého štítku loga** (morf na 13 vrcholů ze SVG), bageta mezitím dosedne níž | slogan drží | H: obrat Gm9 → C9 · SFX: šustnutí + vzduch |
| 20,625 / 21,250 | na štítek dopadne „BAGETERIE“, pak „BOULEVARD“ (razítko, pružina 3 %, písmena z oficiálního SVG) | | SFX: dva měkké ťuky razítka |
| 21,875 (T9 · 4) | vše se usadí | | H: zvukové logo marimby C5 (22,19) F5 (22,34) A5 (**22,50**) |
| **22,500–25,0** (T10) **END CARD** | nahoře slogan, uprostřed logo, pod ním bageta úhlopříčně (packshot), pod ní bb.cz a disclaimer; drží 2,5 s, kamera dál jemně dotlačuje (žádný zamrzlý snímek) | „NOT FAST FOOD. / EXPRESS GOURMET.“ + logo + „bb.cz“ (Big Shoulders Text 800, 70 px) + „Concept ad · not affiliated with Bageterie Boulevard“ (600, 30 px, krytí 80 %) | H: finální akord Fmaj9 + kopák + tlesknutí + jemný činel, doznění do 25,0 s |

**Kontrolní snímky pro fázi 2** (`--nahled casy`): 0,0 (náhled) · 0,9 (háček) · 4,6 (hotové servírování) · 7,62 (uprostřed strhnutí) ·
8,9 (WITHOUT THE WHITE TABLECLOTHS) · 13,9 (ALWAYS FAST, zabaleno) · 18,5 (slogan) · 21,0 (štítek loga) · 23,5 (end card) + snímek na každou dobu (`--nahled doby --bpm 96`).

**Pasti projektu** (do `<pasti>` kostry, oddíl 10):
- Strhnutí ubrusu = jediný švih / šmouha ve videu (7,4–7,9 s), proto render s `--sub 8` (renderer má jeden počet podsnímků pro celé video).
  Šmouha jen svislá a jen na ubrusu a talíři, bageta a nadpis ostré.
- Horní hrana ubrusu musí přejet celý obraz (i dolní rohy) za ~0,3 s, jinak to vypadá jako záblesk. Kamera se na dropu nehýbe (žádný třes).
- Proměna tloušťky písma: Big Shoulders Display načíst jako variabilní (`wght@100..900`) a fonty vynutit před měřením a před `seek(0)`
  (`document.fonts.load('200 150px "Big Shoulders Display"')` i pro 900), jinak `document.fonts.ready` může skončit dřív, než se font stáhne.
- FRESH → FAST a papír → štítek: měnící se text a tvar mají vlastní masku a časování. Odcházející slovo zmizí dřív, než příchozí obsadí místo.
- Bílý ubrus / papír na bílém talíři (úvod) splývá: talíř má krémový okraj a jemný stín, papír na žluté je v pořádku.
- Bageta, suroviny a ubrus jako SVG z tvarů (žádné fotky). Barvy jídla jen na surovinách. Žádné drobky ani pára jako částice.
- Logo: tvar štítku a písmena přesně podle SVG; morf papíru končí přesně na 13 vrcholech ze `znacka.json`, pak už se mění jen poloha a měřítko (žádná deformace loga).

## Průběh výroby
| kolo | kdo | co se dělalo | verdikt kritika | hlavní nálezy |
|---|---|---|---|---|
| F1 | animator | značka z bb.cz (barvy z CSS, logo SVG + 13 vrcholů štítku, font Big Shoulders), nálada hudby `pohodova`, koncept + storyboard | režisér: **schváleno** s výhradou ke spektru hudby | barvy ověřeny v CSS (#F0B600 136×, #5A3218 = --brown), hudba 25,000 s, drop +7 dB, propad 2 kHz |

## Chyby během výroby
- C016 (fonty z Google se nestáhly před měřením, opraveno, prevence v `scena.html`), C017 (příliš tmavý mix pohodové hudby, kontrola pásem ho neodhalí)

## Spotřeba tokenů
| agent / úkol | tokeny | akce nástrojů | čas |
|---|---|---|---|
| animator: fáze 1 (značka, hudba, koncept) | 403 696 | 114 | 40,7 min |

## Verze
| verze | datum | soubor / kam doručeno | změny |
|---|---|---|---|

## Zpětná vazba (doslova)

## Poučení
