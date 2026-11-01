# V003: BMW řada 7: realistická reklama ve stylu SaaS motion

| | |
|---|---|
| Datum zadání | 2026-11-01 |
| Platforma / formát | **16:9, 1920×1080, 60 fps** |
| Délka | **25,0 s** (pokyn uživatele 2026-11-01) |
| Stav | příprava |

## Zadání (doslova od uživatele)
> není to špatný ale pted použij realný modely 3D od bmw který mají na stránkách a zkus udělat tu reklamu víc realičtnější tím co myslím je že at není to tak moc kreslený ale saas motion který je velice populárny ale použij realisticke modely aut který fakt vypadají jak v realitě
>
> https://www.bmw.cz/cs/index.html (+ parametry kampaně)
>
> https://configure.bmw.cz/cs_CZ/configure/G70/21HZ/FKVSW,P0300,S01CB,S01CE,S01DG,S01DH,S01F4,S0230,S0248,S02TB,S02VB,S02VD,S02VH,S0302,S0319,S03CK,S03DN,S0416,S0428,S0465,S04A2,S04D7,S04FL,S04FM,S04HA,S04HC,S0548,S05AT,S05AV,S05DN,S0617,S061B,S0654,S06AE,S06AF,S06D5,S06NY,S06WF,S0851,S0879,S08KA,S08R3,S08R9,S08TF,S09QX
>
> a udělej s fakt dobrou realisticko ureklamu kterou jen tak člověk nerozwezná že to je dělany přes ai claude a aby byl wow efekt
>
> (+ 5 obrázků z konfigurátoru: předek, záď, 3/4 zepředu, detail kola 2×)

Upřesnění (2026-11-01, doslova):
> reklama 16:9, 25 s video bude trvat, luxusní sportovní hudba, video bude a luxusu a pohodlí a ukázka výkonu na konci kolik to muže jet, bez voice over, 5 motion na přechody, ukazku, auta, výlonu, luxusu a muže být i více motion templetu

Další upřesnění (2026-11-01, doslova):
> na konci bude simpl skládací logo bmw

## Pravidla pro toto video (od uživatele, mají přednost před vším ostatním)
1. **Reálné vozy BMW** z jejich webu / konfigurátoru („reálné 3D modely od BMW, které mají na stránkách“), **nic kresleného**.
2. **Realistická** reklama: vozy „fakt vypadají jak v realitě“, **nepoznat, že to dělala AI**.
3. Styl **SaaS motion** („velice populární“).
4. **Wow efekt.**
5. **16:9, 25 s.** **Luxusní sportovní hudba**, **bez voiceoveru**.
6. Obsah: **luxus a pohodlí**, **na konci ukázka výkonu** („kolik to může jet“).
7. **Aspoň 5 motionů** z prompt-motion (na přechody, ukázku auta, výkonu a luxusu), může jich být víc.
8. **Na konci jednoduché skládací logo BMW** (logo se složí z částí: prstenec, čtvrtiny, písmena; čistě, bez efektů navíc).
9. Dál platí: jedno video, anglicky, energie (V001), barvy podle značky.

## Rozhodnutí režiséra
- **Vůz**: BMW řady 7 (G70, 740d) přesně v konfiguraci z odkazu uživatele (bílá, černá střecha, kola z detailu). Jiné modely ne.
- **3D modely z konfigurátoru stáhnout nejde** (jsou v něm jen jako obrázky, které vyrábí server BMW). Proto stavíme z **jejich rendrů**:
  4 obrázky od uživatele + další pohledy, které konfigurátor ukáže v běžném prohlížeči (360° exteriér, interiér). Web bmw.cz odpovídá (200),
  načítat **normálně** (Playwright jako běžný prohlížeč). Když se objeví blokace, captcha nebo 403, **nic neobcházet** (C024) a říct režisérovi.
- **Realismus**: produkt = jen skutečné rendry BMW, animace 2,5D (maska vozu, paralaxa, pomalá kamera, odlesk jen v masce karoserie, rotace kola
  z detailu, rozsvícení světel, kontaktní stín), pravidlo G7. UI prvky SaaS motion (karty, přepínače, kurzor, typografie) jsou grafika, ta smí být v kódu.
- **Spec reklama do portfolia**: BMW nezastupujeme → end card „Concept ad · not affiliated with BMW“, v popisku bez @handle. Obrázky jsou © BMW AG
  (rendry z konfigurátoru dodal uživatel). Jen portfolio, ne placená kampaň (upozornit uživatele).
- **Texty anglicky**, krátké. Fakta (výkon, rozměry, výbava) **jen doslova z bmw.cz** s odkazem na stránku v zadání (C8), jinak bez čísel.
- **Hudba** (pevná struktura, aby zvukař a koncept běželi souběžně): **120 BPM**, takt 2,0 s, **25,0 s = 12,5 taktu**.
  Úvod takty 1–2 (0–4, luxusní odhalení), **drop 1 = 4,0 s** (takt 3), design a exteriér takty 3–5 (4–10),
  **zlom 10,0 s** (takty 6–7: luxus a pohodlí, interiér, klidnější), stoupání 14,0–16,0 (takt 8),
  **drop 2 = 16,0 s** (takt 9, nejsilnější: **výkon**), výkon takty 9–11 (16–22, vrchol „kolik to může jet“),
  **end card 22,0–25,0 s** s finálním úderem v 22,0. Nová nálada `luxsport` (**luxusní sportovní**: elegantní a drahá, ale s tahem:
  hluboký čistý kopák, sub basa, smyčce / pad, klavír nebo Rhodes, sklenité staby, motor jako motiv před výkonem, risery, údery).
- **Výkon**: čísla (maximální rychlost, zrychlení 0–100, výkon) **jen doslova z bmw.cz / technických údajů konfigurátoru** pro tuto konfiguraci (740d),
  s odkazem. Když je nenajdeme, ukážeme výkon bez čísel.
- **Styl**: SaaS motion jako jazyk rozhraní (karty, čísla, popisky), produkt realisticky (G7).
- **Motiony z prompt-motion**: vybere analytik (**aspoň 5**: přechody, ukázka auta, luxus, výkon), zapíše sem.

- **Odpovědi režiséra analytikovi** (2026-11-01):
  - Exteriér **jen v konfiguraci uživatele** (galerie g01–g14, otočka 360° se světly zap/vyp, rendry od uživatele). Fotky z bmw.cz v jiných lacích ne.
    Interiérové fotky z webu (w14 zadní salonek, w15 místo řidiče) smí, jen když barva čalounění nebude bít do očí proti konfiguraci; přednost má interiér z konfigurátoru.
  - Texty jsou **vlastní anglická copy** (ne citace BMW). Fakta jen čísla doslova z bmw.cz: **250 km/h**, **0–100 km/h 5,7 s** (anglicky „0–100 km/h in 5.7 s“),
    **230 kW**; koně neuvádět (převod k → hp by byl náš). „Elektronicky omezeno“ neuvádět (na webu není).
  - Volitelné prvky (Theatre Screen, B&W, Light Carpet…) **neuvádět jako fakt**, v konfiguraci neověřeno.
  - End card **světlá** (studio #E7E2DC), logo Grey-Colour z bmw.cz, skládané z vrstev.

## Akceptační kritéria pro kritika
1. 1920×1080, 60 fps, 25,0 s ± 0,1 s, H.264 + AAC, BT.709; −14 LUFS ±1, true peak ≤ −1 dBTP (po AAC)
2. **Realismus**: vůz je ve všech záběrech skutečný render BMW (ne kresba), bez artefaktů masky (lem, schody, „vystřižený“ okraj), bez natažených
   nebo deformovaných částí, odlesky a stíny fyzikálně věrohodné. Divák nepozná, že video dělala AI.
3. **SaaS motion**: čisté UI prvky (karty, přepínače, kurzor, popisky s linkou k detailu vozu), plynulé pružné pohyby, kinetická typografie, produkt hrdina
4. **Energie a wow**: událost na každou dobu, žádná mrtvá pasáž > ~1 s, drop 1 a drop 2 nejsilnější momenty.
   **Obsah**: luxus a pohodlí (interiér, detaily) a na konci výkon (maximální rychlost; čísla jen z bmw.cz)
5. Logo BMW nedeformované, barvy podle bmw.cz, texty anglicky bez překlepů, fakta jen z bmw.cz, text v bezpečné zóně (A5)
6. End card: **jednoduché skládací logo BMW** (složí se z částí na finální úder 22,0, logo nedeformované, přesně podle oficiálního tvaru) + CTA + disclaimer
   „Concept ad · not affiliated with BMW“, drží ~3 s, nezamrzlý
7. Aspoň **5** zvolených motionů je ve videu poznat (kreativní ředitel je pojmenuje s časy)
8. Hudba luxusní sportovní, bez voiceoveru

## Materiály
| soubor | kde je | použití |
|---|---|---|
| `bmw7_predek.png`, `bmw7_zad.png`, `bmw7_tri-ctvrte-predek.png`, `bmw7_kolo-detail.png` (2000×1286, od uživatele, z konfigurátoru) | `media/projekty/003-bmw-rada7/materialy/` | jen záloha: stejné pohledy jsou v galerii konfigurátoru ve 2560×1646 (= g01, g08, g11, g06) |
| `katalog.md`: soubor, pohled, rozlišení, pozadí, vhodnost u všech obrázků níže | `media/projekty/003-bmw-rada7/materialy/` | **číst před storyboardem** |
| galerie konfigurátoru `g01`–`g14` (14 pohledů: předek, 3/4 předek ×2, záď, 3/4 záď, boky, kolo ×2, **noc s rozsvícenými světly ×2**, interiér ×3), 2560×1646 / 2560×1536 WebP | `…/materialy/konfigurator/galerie/` | hlavní záběry; páry den/noc g01–g02 a g03–g04 mají stejnou kameru (prolnutí = rozsvícení) |
| otočka 360° `uhel_000`–`uhel_350` po 10° (36 snímků), 2560×1440, dvě sady: světla zapnutá / vypnutá | `…/materialy/konfigurator/360_svetla_zap/`, `…/360_svetla_vyp/` | turntable, přechody; 000 = předek, 090 = levý bok, 180 = záď, 270 = pravý bok; páry zap/vyp pixelově zarovnané |
| interiér 360°: stěny kostky 2000×2000 (předek, 2 boky, záď, strop, podlaha) + náhled panoramatu 700×350 | `…/materialy/konfigurator/interier_kostka/` | pomalé panorama interiéru (luxus a pohodlí) |
| snímky obrazovky konfigurátoru (lišta s výkonem, technické údaje, rozměrové výkresy) | `…/materialy/konfigurator/_snimek_*.png` | zdroj faktů, inspirace UI, do videa ne |
| fotky z bmw.cz `w01`–`w15` (5 boků s průhledností v jiných barvách, jízda, krajina, interiér v 5 barvách čalounění, lidé) | `…/materialy/web/` | **jiné barvy než konfigurace**: do videa jen s rozhodnutím režiséra |
| logo `BMW_Grey-Colour_RGB_bmw-cz.svg` (bmw.cz) + `logo_original_2048.png`, `logo_bile-ctvrtiny_2048.png` | `media/projekty/003-bmw-rada7/znacka/logo/` | end card |
| vrstvy loga pro skládání `vrstvy/01`–`09` (prstenec, vnitřní kruh, 2 modré + 2 bílé čtvrtiny, B, M, W) + `00_slozene_*.svg` | `…/znacka/logo/vrstvy/` | skládací logo 22,0 s; stejný viewBox 0 0 340.16 340.16, cesty beze změny |
| `znacka.css` (barvy jako proměnné, @font-face), písmo Manrope `fonty/manrope-latin(ext).woff2`, `vzornik.jpg` (+ `vzornik.html`) | `media/projekty/003-bmw-rada7/znacka/` | barvy a písmo pro animátora |

## Režijní list
- **Koncept jednou větou**: (doplní kreativní ředitel)
- **Vzhled** (analytik 2026-11-01, vzorník `media/projekty/003-bmw-rada7/znacka/vzornik.jpg`, proměnné v `znacka.css`):
  - **Barvy (z CSS tokenů bmw.cz)**: `#1C69D4` modrá akcentu UI (bmw.cz `--cta`: tlačítka, aktivní přepínač, ukazatel, linka k detailu),
    `#0653B6` tmavší modrá (hover / stisk), `#262626` text a tmavé plochy (`--link`), `#FFFFFF` / `#F6F6F6` světlé plochy a karty,
    šedé `#4D4D4D` `#666666` (vedlejší text) `#8E8E8E` (popisky) `#BBBBBB` (linky) `#E6E6E6` (okraje karet), `#000000`.
    **Logo jen** `#0066B1` + `#6F6F6F` (na UI je nepoužívat). Studio z rendrů: stěna `#E7E2DC`, stín `#DBD4C9`, podlaha `#CAC2B5`, noc `#161616`.
    Web je světlý, střídmý, modrá jen na akci: v UI kartách stejně (bílá / světle šedá karta, tmavý text, modrý jen aktivní prvek).
  - **Písmo**: web používá proprietární **BMW Type Next** (Light 300 pro čísla a perex, Bold 700 velkými písmeny pro nadpisy, Medium 500 pro UI).
    Náhrada **Manrope** (Google Fonts, SIL OFL 1.1, latin + latin-ext, proměnné 200–800): ze srovnání (`znacka/fonty/_porovnani_pisma.jpg`)
    má nejbližší geometrii (zaoblené „hranaté“ oblouky, otevřené číslice, podobná šířka verzálek). Barlow je užší, Inter neutrálnější, Titillium techničtější.
    Soubory lokálně v `znacka/fonty/`, @font-face v `znacka.css`.
  - **Logo**: `BMW_Grey-Colour_RGB.svg`, které vkládá bmw.cz (`https://www.bmw.cz/content/dam/bmw/common/images/logo-icons/BMW/BMW_Grey-Colour_RGB.svg.asset.1756199978277.svg`),
    plochá varianta: prstenec a písmena `#6F6F6F`, čtvrtiny `#0066B1`, „bílé“ čtvrtiny průhledné. Licence: ochranná známka © BMW AG, bez volné licence,
    jen portfolio (spec reklama, disclaimer na end card). Wikimedia jsem nepotřeboval. Na světlém pozadí originál, na tmavém varianta s bílými čtvrtinami.
  - **Skládací logo**: 9 vrstev v `znacka/logo/vrstvy/` se stejným viewBoxem a beze změny cest z originálu (bílé čtvrtiny = výseč r 95,33 přesně
    po vnitřní hranu prstence). Složené vrstvy = originál: geometrie shodná, liší se jen antialiasing oblouků modrých čtvrtin (701 krajových pixelů z 1 mil. při 1024 px).
    Střed loga 170,08 / 170,08, vnější poloměr 170,08, vnitřní kruh 100,86.
  - **Claimy na bmw.cz (doslova, česky)**, stránka https://www.bmw.cz/cs/all-models/7-series/sedan/bmw-7-series-sedan.html:
    „NOVÉ BMW ŘADY 7 SEDAN“ · „DOKONALOST V KAŽDÉM DETAILU. VYTVOŘENO S ODHODLÁNÍM.“ · „Projev dokonalosti v automobilovém průmyslu.“ ·
    „Design, který inspiruje. Přední část BMW řady 7.“ · „Přesnost v každém detailu. Zadní část BMW řady 7.“ · „Interiér. Digitální dokonalost.“ ·
    „Váš prostor, Váš design osvětlení.“ · „Vnímejte jízdní dynamiku na každé trase.“ · „Dynamika a pohodlí pro individuální radost z jízdy.“ ·
    „Zažijte luxus: Váš soukromý salonek.“ · „Vaše osobní oáza klidu začíná právě zde.“
    Anglické verze ve videu budou **náš překlad**, ne citace BMW (anglický web BMW jsem neověřoval).
  - **Fakta z téže stránky (doslova)**: „mřížky ve tvaru ledvinek BMW Iconic Glow“ · „Adaptivní dvounápravové vzduchové odpružení nabízí mimořádně
    pohodlnou jízdu“ · „Inovativní systém BMW Panoramic Vision se rozprostírá po celé šířce čelního okna.“ · délka „5 395 mm“, zavazadlový prostor „540 l“
    (počítadlo na stránce; pro 740d potvrzeno i v technických údajích) · „Modely BMW 750e xDrive Sedan a BMW 740d xDrive Sedan bude možné objednávat
    od 30. září 2026.“ Pozor: „294 (400) kW (k)“ a „5,1 sekund“ na stránce patří **benzinovému 740 xDrive**, ne 740d. Volitelná výbava
    (Theatre Screen 31,3" 8K, integrální aktivní řízení 3,5°, Bowers & Wilkins) jen když ji konfigurace uživatele obsahuje (neověřeno, viz otázky).
  - **Autentický prvek webu pro SaaS motion**: počítadlo čísel s rolujícími číslicemi (0–9) a šikmými oddělovači „294 (400) kW (k) / 5 395 mm / 540 l“,
    čísla Light 300, jednotky menší (snímek `materialy/web/_snimek_web_uvod.jpg`).
- **Fakta o výkonu** (BMW 740d xDrive Sedan, kód modelu 21HZ = konfigurace uživatele; doslova):
  - Konfigurátor (odkaz uživatele, okno „Motor/Technické údaje“, snímek `materialy/konfigurator/_snimek_technicke-udaje.png`):
    „Výkon motoru **230 kW (313 k)***“ · „Maximální rychlost **250 km/h**“ · „Zrychlení (0–100 km/h) **5,7 s**“ ·
    „Maximální točivý moment motoru 670 Nm (1500 - 2500 1/min)**“ · „Druh pohonu Pohon všech kol“.
    Poznámka *: „„podle předpisu OSN č. 177. Jmenovité výkony podle předpisu OSN č. 85: spalovací motor (60 s) 210 kW, elektromotor (10 s) 13 kW.““
    Lišta konfigurátoru: „Max. výkon 230 kW (313 k)“, „0-100 km/h 5,7 s“.
  - bmw.cz technické údaje https://www.bmw.cz/cs/all-models/7-series/sedan/bmw-7-series-sedan-technical-data.html („740d xDrive Sedan“, 21HZ):
    „Výkon v kW (k) **230 (313)**“ (pozn. 16: „Podle UN R177. Uvedený jmenovitý výkon spalovacího motoru (60 s) a elektromotoru (10 s) podle UN R85.“) ·
    „Zrychlení 0–100 km/h v s **5,7**“ · „Maximální rychlost v km/h **250**“ · „Druh motoru Vznětový 48V mild hybrid“.
  - **„Elektronicky omezeno“ na žádné z obou stránek není** (hledáno „omezen“ v technických údajích: 0 výskytů), proto ve videu neuvádět.
    Pozn. 6 u hmotností: „Volitelná výbava může ovlivnit hmotnost, užitečné zatížení a nejvyšší rychlost, pokud ovlivní aerodynamiku vozu.“
  - Návrh anglického znění (překlad, čísla beze změny): „250 km/h“ · „0–100 km/h 5.7 s“ · „230 kW (313 hp)“ (pozn.: „k“ = koně DIN, anglicky BMW EU používá „hp“).

## Storyboard / časová osa
(doplní kreativní ředitel)

## Průběh výroby
| kolo | kdo | co se dělalo | verdikt kritika | hlavní nálezy |
|---|---|---|---|---|

## Chyby během výroby

## Spotřeba tokenů
| agent / úkol | tokeny | akce nástrojů | čas |
|---|---|---|---|

## Verze
| verze | datum | soubor / kam doručeno | změny |
|---|---|---|---|

## Zpětná vazba (doslova)

## Poučení
