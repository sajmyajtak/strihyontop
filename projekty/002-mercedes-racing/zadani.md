# V002: Mercedes-Benz: závodní spot (energický)

| | |
|---|---|
| Datum zadání | 2026-10-31 |
| Platforma / formát | **16:9, 1920×1080, 60 fps** |
| Délka | **30,0 s** (rozsah uživatele 25–35 s, zvoleno podle motionu a hudby) |
| Stav | příprava |

## Zadání (doslova od uživatele)
> okey hele není to špatný ale není to ono. potřebuju víc energetické at to není tak bez duši to video. tím myslím že at je to rychlejší a více zaživnější at má to více efektů. videa budeš dělat 16:9 a kolem 25-35 vteřin podle toho jaký si vybereš motion z strýnky. udělej jen vždy jedno video ale ted zkus s hudbou ale bez voiceover. udělej mi reklamu na https://www.mercedes-benz.cz/ maš tam i logo použij tam i barvy keteré jsou na stránkach a hudba bude sportovní a auto nebo ta reklama bude hlavně o závodění aut který má mercedes. motion at vybere hlavní agent a at jsou tam minimálně 3 ale můžeš použít i víc

## Pravidla pro toto video (od uživatele, mají přednost před vším ostatním)
1. **Víc energie než V001**: rychlejší, živější, **víc efektů**, „ať to není bez duše“.
2. **16:9**, délka **25–35 s** podle zvoleného motionu.
3. **Jedno video.** S **hudbou**, **bez voiceoveru**.
4. Reklama na **mercedes-benz.cz**: použít **logo** a **barvy z jejich webu**.
5. Hudba **sportovní**. Reklama je hlavně o **závodění aut, která Mercedes má**.
6. Motion vybere **hlavní agent**, **minimálně 3 motiony** z prompt-motion (víc je povoleno).

## Rozhodnutí režiséra
- **Spec reklama do portfolia**, Mercedes-Benz nezastupujeme → disclaimer na end card „Concept ad · not affiliated with Mercedes-Benz“
  + v popisku (J5), v popisku žádný @handle značky.
- **Závodění**: Mercedes-AMG motorsport (formule a závodní AMG GT) jako **stylizované vozy postavené v kódu** (siluety, lak, světla, stopy),
  žádné fotky, žádná loga sponzorů (např. Petronas), žádná jména jezdců ani čísla titulů, pokud nejsou doslova na mercedes-benz.cz (C8).
- **Texty anglicky**, krátké, jen ze značky nebo obecné závodní výrazy (např. „0 → 100“ jen pokud je to na webu; jinak bez čísel).
- **Hudba** (pevná struktura, aby zvukař a koncept mohli běžet souběžně): **128 BPM**, takt 1,875 s, **16 taktů = 30,0 s**.
  Úvod a nádech v taktech 1–2, **drop 1 = 3,75 s** (takt 3), plná jízda takty 3–8, **zlom (breakdown) 15,0 s** (takt 9),
  stoupání takt 10, **drop 2 = 18,75 s** (takt 11, nejsilnější moment), finále takty 11–14, **end card 26,25–30,0 s** (takty 15–16)
  s finálním úderem v 26,25 s. Nová nálada `sportovni` v `nastroje/hudba.py` (driving electro / racing: tvrdý kopák, distorzovaná basa,
  risery, údery, syntetický „motor“ jako zvukový motiv).
- **Zvolené motiony z prompt-motion (4)**:
  1. **Šablona showreel** (prompt-motion.com/templates/showreel): kostra na doby, **jedna technika na takt**, poslední celý takt nejsilnější,
     2D → 3D moment, end title, kontrola 1 snímku na dobu.
  2. **Taxtello app film** ([`daniel-haida-8691d4`](https://prompt-motion.com/daniel-haida-8691d4)): **agresivní kinetická typografie**,
     údery, švihy a glitch akcenty na doby.
  3. **UGC ad generator promo** ([`twoclipping-6dd14e`](https://prompt-motion.com/twoclipping-6dd14e)): **třes kamery na údery**, rozmazání
     pohybem, švihy, mřížka dob zkalibrovaná na skutečné údery kopáku.
  4. **Food craving launch film** ([`ultimaxbt-2ddf1e`](https://prompt-motion.com/ultimaxbt-2ddf1e)): souvislý záběr, **přechody zaplavením
     barvou z objektu**, zvuk na každou událost, 8 podsnímků u rychlých pohybů.

- **Web Mercedesu blokuje automatický přístup (403)** na mercedes-benz.cz, .com, group i amg. Obcházet ochranu nebudeme (pokus o to
  zastavila bezpečnostní pravidla prostředí a je to správně). Proto: **logo z Wikimedia Commons** (oficiální hvězda) a **předběžná paleta**
  (černá, bílá, stříbrná, modrý akcent #0078D6) jako CSS proměnné. Uživatel byl požádán o screenshot webu, podle něj se paleta ověří a případně
  vymění před finálním renderem. Texty jen obecné nebo vlastní claimy reklamy, žádná fakta (C8).

## Akceptační kritéria pro kritika
1. 1920×1080, 60 fps, 30,0 s ± 0,1 s, H.264 + AAC, BT.709
2. −14 LUFS ±1, true peak ≤ −1 dBTP (po AAC)
3. **Energie**: událost na každou dobu, úder každý takt, žádná „mrtvá“ pasáž > ~1 s, aspoň 6 různých energických efektů
   (rychlostní čáry, světelné stopy, záblesk/otřes na úderu, švih, zoom, glitch akcent…) synchronních s hudbou
4. Logo Mercedes-Benz z oficiálního zdroje, nedeformované. Barvy odpovídají webu mercedes-benz.cz
5. Je poznat, že jde o **závodění** (vozy, trať, rychlost) a o **Mercedes**
6. Hudba sportovní, drop 1 v 3,75 s a drop 2 v 18,75 s jsou vizuálně nejsilnější momenty, klíčové SFX slyšet (I3)
7. End card: logo + text + disclaimer, drží ~3,75 s, nezamrzlý
8. Texty anglicky, bez překlepů, bez vymyšlených faktů. Text v bezpečné zóně 16:9 (A5)
9. Aspoň 3 zvolené motiony jsou ve videu poznat (kreativní ředitel je pojmenuje s časy)

## Materiály
| soubor | kde je | použití |
|---|---|---|
| `Mercedes-Logo.svg` (originál, 1,5 MB, chromová 3D hvězda z ~1 250 plochých cest) | `media/projekty/002-mercedes-racing/znacka/` ← [Commons](https://commons.wikimedia.org/wiki/File:Mercedes-Logo.svg) | zdroj tvaru; do scény jen jako PNG (`mercedes-hvezda-original_1024.png`), když chceme chrom |
| `mercedes-hvezda-plocha.svg` (1 cesta, 610 B, `fill="currentColor"`) | tamtéž | hlavní logo do scény (maska, záblesk, obrys, end card). Shoda s originálem 97,75 % pixelů (rozdíl jen na hranách) |
| `mercedes-hvezda-fazety.svg` (7 cest, ramena dělená na světlou / tmavou plochu, barvy z CSS proměnných `--mb-hvezda-*`) | tamtéž | „kovová“ hvězda bez 1,5 MB SVG, světlo shora jako originál |
| PNG náhledy `*_1024.png`, `hvezda_generator.py` (geometrie změřená z originálu) | tamtéž | kontrola tvaru, znovuvytvoření |
| `znacka.css` (paleta jako CSS proměnné), `vzornik-znacky.html/.jpg` (paleta + fonty + hvězda na 1920×1080) | tamtéž | vložit do scény; vzorník pro kreativního ředitele a animátora |

**Licence loga**: soubor na Commons nahrál uživatel *Khaled* (2018-07-15, „own work“, podle *Mercedes-Benz Logo 2010.svg*), licence **CC BY-SA 4.0**.
Hvězda je zároveň **ochranná známka Mercedes-Benz Group AG** (licence Commons se týká jen kresby, ne práva ke známce).
Uvedení zdroje do popisku: „Mercedes star: Khaled / Wikimedia Commons, CC BY-SA 4.0“. Spec reklama s disclaimerem (J5).

## Režijní list
- **Koncept jednou větou** (kreativní ředitel, 2026-10-31): **„FOLLOW THE STAR: závodní linie kreslí hvězdu.“** Modrá světelná stopa, kterou stříbrný šíp táhne za sebou od zhasnutí startovních světel, je celou dobu **nedokončená hvězda Mercedes**: ve zlomu se okruh uzavře do prstence, ve druhém dropu do něj tři vozy vstřelí tři linie a vznikne **hvězda ze světla**, která pak rozdělí obraz na tři závodní výseče a nakonec se zacvakne do loga.
  Spojovací prvek: **jedna modrá linie** (stopa zadního světla) → okraj tratě → účaří textu → maska písma → mapa okruhu → prstenec → ramena hvězdy → podtržení na end card.
  Oblouk (podle Taxtella): napětí na startu → chaos závodu → klid zlomu → hvězda (značka).
- **Vzhled** (analytik, 2026-10-31). **Barvy jsou PŘEDBĚŽNÉ, NEOVĚŘENO z webu** (mercedes-benz.cz vrací 403, čeká se na screenshot od uživatele).
  Všechny barvy jen přes proměnné z `media/projekty/002-mercedes-racing/znacka/znacka.css`, ať jdou vyměnit na jednom místě.
  - Základ (digitální paleta MB): `--mb-cerna #000000` pozadí a end card · `--mb-bila #FFFFFF` hlavní text, záblesky, světlomety ·
    `--mb-modra #0078D6` **jediný akcent** (klíčové slovo, linka, UI prvek; modrá odkazů a tlačítek webu)
  - Stříbro a šedá (lak „stříbrných šípů“, kov hvězdy): `--mb-stribro-svetle #E6E8EA` odlesk · `--mb-stribro #C9CDD0` lak, prstenec, kovový text ·
    `--mb-seda #8E969B` stín laku, disclaimer · `--mb-grafit #1E2124` asfalt, střed vinětace
  - Závodní doplněk, odvozený z modré (ne nová barva, G1): `--mb-modra-zare #4DA8FF` světelné stopy, záře, rychlostní čáry · `--mb-modra-tmava #00508F` odlesk na asfaltu
  - Volitelně `--mb-brzdove-svetlo #FF2A2A`: jen fyzická zadní světla vozu, malé plochy, nikdy text. **Ne tyrkysová** (to je barva sponzora, C8).
  - Poměr: ~70 % černá / grafit, ~20 % stříbro a bílá, ~10 % modrá. Modrá na černé má kontrast ~4,6 : 1 → v textu jen velké nadpisy, menší text bílý.
  - **Font** (MB Corpo A / Corpo S jsou proprietární): **Archivo** (Google Fonts, latin-ext, osa šířky 62–125 %) jako jediná rodina (E4):
    nadpisy `font-stretch:125%; font-weight:900`, pro rychlost kurzíva, VERZÁLKY; podnadpisy 112 % / 800; „Mercedes-Benz“ na end card 100 % / 600 s prostrkáním.
    Proč: rozšířený grotesk = závodní / motorsport vzhled, přitom střídmý a „německy“ technický jako Corpo S; jedna proměnná rodina = nadpis i text.
    Text a disclaimer: **Inter Tight** 500 (nejbližší neutrálnímu Corpo S). Patkové Corpo A (slovní značka) **nenapodobovat**, nevypadalo by to jako falešné logo.
    Pozor: Archivo 125 % / 900 při 170 px má na řádek max. ~12 znaků v bezpečné zóně (A5), „FULL THROTTLE“ už přetéká → 140 px nebo šířka 112 %.
    Do `FONTY` ve scéně: `'900 italic 150px Archivo'`, `'800 150px Archivo'`, `'600 60px Archivo'`, `'500 40px "Inter Tight"'` (C016).
  - **Logo**: `mercedes-hvezda-plocha.svg` (hlavní, `currentColor`), `mercedes-hvezda-fazety.svg` (kov), chrom jen jako PNG. Hvězdu nedeformovat
    (jen jednotné měřítko a otočení), prostor kolem ≥ 25 % průměru, na end card průměr ~300–360 px.
  - **Hesla** (anglicky, bez tečky, bez faktů a čísel): LIGHTS OUT · FULL THROTTLE · BUILT TO RACE · CHASE THE LINE · FASTER BY DESIGN ·
    EVERY CORNER COUNTS · FOLLOW THE STAR (end card). Disclaimer: „Concept ad · not affiliated with Mercedes-Benz“.

## Storyboard / časová osa
**Storyboard S1** (kreativní ředitel, 2026-10-31), koncept „FOLLOW THE STAR: závodní linie kreslí hvězdu“. Časy z `media/projekty/002-mercedes-racing/hudba.json`:
128 BPM, doba 0,46875 s, takt 1,875 s, T<n> začíná v (n−1)·1,875 s, doby d1–d4 = +0 / +0,469 / +0,9375 / +1,406.
Hudební události, na které se obraz váže (animátor je bere z `udalosti_nastroju`, ne ručně): kopák od 1,875 na každou dobu (v T9 nic),
malý buben d2 a d4 od T3, **stab** na „a“ za každou dobou T11–T14 (18,984 + k·0,469; poslední 26,25), motor: rev 1,875 → vrchol 3,75,
průjezd 15,0 → vrchol 15,95, rev 16,875 → vrchol 18,75, odjezd 26,25; řazení 2,625 / 17,475 / 18,125 / 26,6; vír 2,81–3,75, 14,53–15,0,
16,875–18,75 (zrychluje), 25,78–26,25; obrácený činel do 3,75 / 18,75 / 26,25; úder + činel 3,75 / 18,75 / 26,25, činel 15,0.

**Svět a kamera**: noc, černá a grafit, vozy jen jako stříbrný lak s ostrým okrajovým světlem (rim light) a modré světlo; vše v kódu (SVG + canvas).
Jedna kamera (posun + otočení + log zoom), mezi scénami se neresetuje: každý přechod je pohyb skrz prvek, který už je v obraze (D2, Food craving).
**Knihovna vozů (4 kresby, znovu použité)**: `F1-předek` (formule zepředu: přední křídlo, nos, halo, airbox, široké pneu), `F1-shora` (půdorys formule,
délka 1 : 2,6 šířky), `GT-bok` (závodní kupé z boku: dlouhá kapota, nízká kabina, velké zadní křídlo, difuzor), `F1-záď` (formule zezadu: zadní křídlo,
dešťové světlo, difuzor, pneu). Hrdina = stříbrný lak (`--mb-stribro*`) + tenký modrý proužek, soupeři = grafit (`--mb-grafit`) se šedým okrajem.
**Žádná startovní čísla, jména, sponzoři ani tyrkysová** (C8). Hvězda na nose / boku jen jako malý odznak z `mercedes-hvezda-plocha.svg`.
**Text**: Archivo (nadpisy 900 kurzíva, šířka 112–125 %, VERZÁLKY), vždy **jen jedna vrstva textu v obraze**; tiker = střih slova na dobu (staré zmizí
ve stejném snímku, kdy přijde nové). Všechny texty uvnitř x 96–1824, y 54–940 (A5, spodních 140 px kryje přehrávač).
**SFX** = pro zvukaře, **změřený vrchol přesně na uvedeném čase**. H = hudba (už v `hudba.wav`). Klíčové SFX (drop 1, drop 2, logo) slyšet 0 až −3 LU (I3),
ostatní tiše pod hudbou. **Automatika hudby**: −9 dB 3,52–3,75 (nádech před LIGHTS OUT), −10 dB 18,40–18,75 (nádech před hvězdou), náběh 0,15 s, doběh 0,03 s.

| čas (takt · doba) | obraz | text | efekt | zvuk / událost (SFX s vrcholem na čase) |
|---|---|---|---|---|
| **0,000–1,875** (T1, ÚVOD: STARTOVNÍ ROŠT) | **Snímek 0 = náhled**: noční rošt, kamera nízko zepředu. `F1-předek` stříbrný, šířka **1 400 px** (73 %, A8), výška ~670 px, střed x 960, spodek pneu y 1 030 (airbox / halo nahoře v y ~370), nos s odznakem hvězdy (Ø 64 px) v (960; 760). Pod vozem mokrý asfalt, odraz vozu (krytí 22 %, modrý nádech) je skoro celý pod spodním okrajem. Nahoře **portál startovních světel**: 5 kulatých lamp Ø 84 px v řadě x 640–1280, střed y 110, tmavé čočky. Skladba odshora: lampy → nápis → vůz, mezi nápisem a vozem ≥ 40 px (ověřit na klíčovém snímku). Okrajové světlo zprava shora, modrá záře pod podlahou vozu. **d1 0,000**: po laku nosu a hvězdě začne jet **odlesk** (Taxtello glint, úzký bílý pruh 40 px pod 20°, zleva doprava, 0,00–0,90, ease-in-out; na snímku 0 je na levé třetině vozu). **d2 0,469**: lampa 1 se rozsvítí (červené světlo, záře, odraz na laku a na asfaltu) + kamera **cuk vpřed** 1,000 → 1,015 (kriticky tlumeně 0,2 s). **d3 0,938**: lampa 2 + cuk. **d4 1,406**: lampa 3 + cuk. | **0,469 „LIGHTS“** (Archivo 900 kurzíva 125 %, 150 px, bílá, účaří y 320 mezi portálem a vozem, celé „LIGHTS OUT“ ≤ 1 400 px a vystředěné; stojí na své konečné pozici vlevo, místo pro „OUT“ vpravo zůstává **prázdné** = napětí). Dopad: měřítko 1,25 → 1,00 + rozmazání 12 → 0 px za 0,12 s, ease-out, bez překmitu | odlesk (glint), rozsvícení lamp s odrazy, cuk kamery na dobu | H: arpeggio, tlesknutí 0,469 a 1,406 · SFX: elektrické „klonk“ relé lampy, vrchol **0,469 / 0,938 / 1,406** (tiše, ale čitelně) |
| **1,875–3,750** (T2, REV A NÁDECH) | **d1 1,875**: lampa 4 + cuk (první kopák, motor začne vytáčet). **d2 2,344**: lampa 5, **všech 5 svítí** + cuk. **2,625** (řazení / prošlápnutí plynu): vůz se přikrčí 6 px dolů a vrátí (0,18 s, kriticky tlumeně), z výfuku krátký tetelivý pruh. **d3 2,8125** (začíná vír): kamera **jeden pomalý nájezd** 1,06 → 1,20 (ease-in) k nosu vozu až do 3,75; vůz se chvěje (šum se seedem, amplituda 0 → 3 px), vinětace se stahuje 0 → 35 %. **3,52–3,75 NÁDECH**: chvění ustane, všechno stojí, svítí jen 5 lamp | „LIGHTS“ drží | stupňované chvění, stahující se vinětace, „zmrazení“ před dropem | H: kopák 1,875 / 2,344 / 2,8125, motor rev → 3,75, řazení 2,625, vír 2,81–3,75, obrácený činel · SFX: „klonk“ lamp vrchol **1,875 / 2,344**; 3,52–3,75 **ztlumení hudby −9 dB** |
| **3,750–5,625** (T3, **DROP 1: LIGHTS OUT**) | **3,750 (1 snímek)**: všech 5 lamp **zhasne naráz**, červená zmizí z laku i asfaltu. Bílý záblesk z portálu (krytí 60 % → 0 za 0,08 s, max. 3 snímky). Kamera **otřes 12 px** (seed, doznívá 0,5 s). **START**: zadní kola prokluzují (pruh kouře grafit), vůz se řítí do kamery: měřítko 1 → 3,2 za 3,75–4,15 (ease-in, kubicky), **radiální rychlostní čáry** vyrazí od hvězdy na nose (canvas, ~120 čar, bílé a `--mb-modra-zare`, délka podle rychlosti), chromatický posun okrajů 4 px. **4,05–4,219 ZOOM SKRZ HVĚZDU**: odznak na nose zaplní obraz, kamera proletí **prstencem hvězdy** (Ø 600 → 3 000 px) a vnitřek prstence se otevře jako kruh do nové scény (UGC promo: kruh z tlačítka do tmavé scény). **d2 4,219**: **POHLED SHORA**: noční trať, `F1-shora` hrdina délka 620 px, nos nahoru, střed (960; 640), kamera ho drží a trať ujíždí dolů; ze zadního světla se rodí **MODRÁ LINIE** (jádro 10 px bílá, záře 40 px `--mb-modra-zare`). Obrubníky (grafit/bílá) prolétají. **d3 4,6875**: hrdina projede mezi dvěma soupeři (grafit, F1-shora) a ti zůstanou za ním (předjetí, úkrok 30 px). **d4 5,156**: hrdina švihne doprava do ideální stopy, linie za ním nakreslí „S“; kamera se nakloní 0 → −4° (jediný pohyb scény) | **3,750 „OUT“** dopadne vpravo vedle „LIGHTS“ (stejný řez, **`--mb-modra`**, tvrdší: měřítko 1,40 → 1,00, rozmazání 20 → 0 za 0,10 s) → „LIGHTS OUT“ je jeden řádek, jedna vrstva. Text je součástí světa: jak vůz letí do kamery, nápis zrychlí nahoru a ven z obrazu (ease-in, **pryč do 4,00**), dřív než začne průlet hvězdou | záblesk, otřes, radiální rychlostní čáry, chromatický posun, **zoom skrz objekt (hvězda)**, zrod světelné stopy | H: **úder + činel 3,75**, kopák, malý buben 4,219 / 5,156 · SFX: **odpal: prásk + řev motoru, vrchol 3,750, 0 až −2 LU**; průlet prstencem „vššš“ vrchol **4,15**; projetí soupeřů (doppler, tiše) vrchol **4,70**; cvrknutí pneu vrchol **5,156** |
| **5,625–7,500** (T4, FULL THROTTLE: KINETICKÁ TYPOGRAFIE) | **d1 5,625 ŠVIH**: kamera se otočí o −90° za 0,18 s (ease-in-out, rotační rozmazání podle rychlosti, render `--sub 8`); pohled shora se rozmaže do pruhů a po švihu leží **modrá linie vodorovně** přes celý obraz v y 660 (od okraje k okraji), pozadí černé s jemným zrnem asfaltu. **d2 6,094**: po linii proběhne zprava doleva **světelný impuls** (0,3 s) a písmena nad ním nadskočí o 10 px (vlna po 15 ms, kriticky tlumeně = „plyn“). **d3 6,5625**: druhý, silnější impuls, linie ztloustne 10 → 16 px, kamera cuk 1,00 → 1,03. **d4 7,031**: po linii zprava doleva prosviští **`GT-bok`** hrdina (délka 900 px, kola na linii, průjezd 0,3 s, rozmazání podle rychlosti) a jeho proud vzduchu strhne text; linie zůstane a stane se **okrajem tratě** | **5,625 „FULL THROTTLE“** (Archivo 900 kurzíva 112 %, 140 px, „FULL“ bílá, „THROTTLE“ `--mb-modra`, účaří **na linii** y 640, max. šířka 1 600 px): přijede zprava po linii jako jeden objekt, roztažený vodorovně 180 % → 100 % s vodorovnou šmouhou, usadí se 5,625–5,95 (ease-out). **7,031–7,25** odchod: písmena se protáhnou doleva a zmizí (ease-in, za vozem) | **švih s rozmazáním (rotace)**, roztažení textu (E6), světelný impuls po linii, průjezd vozu | H: kopák na každou dobu, malý buben 6,094 / 7,031 · SFX: švih „vuš“ vrchol **5,70**; dopad textu (tupý kovový úder) vrchol **5,75**; elektrické „cink“ impulsu vrchol **6,094** a **6,5625** (tiše); průjezd GT (řev + doppler) vrchol **7,10** |
| **7,500–9,375** (T5, PRŮJEZD Z BOKU) | **d1 7,500**: kamera se „chytí“ vozu: `GT-bok` hrdina **1 400 px** (73 %), střed (960; 600), kola na modré linii (okraj tratě) y 760, jede zprava doleva, kamera ho drží a svět ujíždí doprava. **Paralaxa ve 4 vrstvách**: daleko rozmazané světla tribuny (bokeh bílé a modré tečky, pomalu), střed svislé sloupky plotu (rozmazané, rychle), blízko obrubník na linii (grafit/bílá, velmi rychle), popředí: na kopák 7,500 a 8,4375 přes celý obraz prosviští **tmavý sloup** (rytmický wipe, 3 snímky). Kola: rotace paprsků s rozmazáním. Na **každou dobu** přejede po laku **odlesk reflektoru** (bílý pruh zleva doprava, 0,25 s) = událost na dobu. **d2 7,969**: zprava se zezadu přisaje soupeř (`GT-bok` grafit, do 30 % obrazu). **d3 8,4375**: hrdina mu ujede (hrdina +80 px doleva, soupeř zpět ven z obrazu, ease-in-out 0,3 s). **d4 8,906**: kamera **švihne doleva** před vůz (0,15 s, vodorovné rozmazání) a ve švihu zůstane jen černá + linie | bez textu (oko si odpočine na voze) | paralaxa, vodorovné rychlostní čáry, odlesky reflektorů, předjetí, švih | H: kopák, malý buben 7,969 / 8,906 · SFX: průlet sloupu „fup“ vrchol **7,50** a **8,4375** (tiše); bok soupeře, doppler vrchol **8,00**; švih vrchol **8,95** |
| **9,375–11,250** (T6, BUILT · TO · RACE: TIKER) | **d1 9,375**: z pravého okraje proletí modrá stopa vozu a **odkryje první slovo** (linie jako hrana masky, 0,12 s). Každé slovo = **tvrdý střih na dobu** s dorazem kamery 1,08 → 1,00 (0,12 s, ease-out) a radiálním rozmazáním na prvních 2 snímcích (UGC promo: velký text na „push cuts“, tiker 3 slov). **d2 9,844** → TO. **d3 10,3125** → RACE: písmena jsou **okna**, uvnitř běží průjezd z boku (vrstva T5 znovu, rychle), obrys písmen 3 px `--mb-stribro`. **d4 10,781**: kamera **začne letět do vnitřku písmene „A“** (trojúhelníkový otvor, log zoom ×1 → ×9 do 11,25, ease-in); v otvoru se už od 10,78 kreslí pohled shora na vracečku (další scéna) | **9,375 „BUILT“ → 9,844 „TO“ → 10,3125 „RACE“** (Archivo 900 kurzíva 125 %, 300 px, šířka slova ≤ 1 600 px, střed obrazu; BUILT a TO bílé, RACE okna s obrysem). Výměna ve stejném snímku (staré slovo pryč, nové tam), **nikdy dvě slova naráz**. RACE odchází tím, že jím kamera proletí (pryč do 11,20) | tiker na doby, radiální rozmazání na dorazu, text jako maska (okna), **zoom skrz písmeno** (Taxtello: písmo jako přechod) | H: kopák, malý buben 9,844 / 10,781 · SFX: suché kovové údery slov vrchol **9,375 / 9,844 / 10,3125**; nasátí do písmene „vššš“ s vrcholem **11,20** |
| **11,250–13,125** (T7, VRACEČKA) | **d1 11,250**: z otvoru „A“ jsme **shora nad vracečkou** (U zatáčka): asfalt grafit s jemným šumem, bílé okraje tratě, obrubník na vrcholu zatáčky (grafit/bílé pruhy). `F1-shora` hrdina 520 px přijíždí shora dolů a **brzdí**: dešťové světlo bliká červeně, kotouče žhnou (malé teplé body, jen v kolech). Kamera se během taktu pootočí s vozem o −30° (jediný pohyb). **d2 11,719 APEX**: podlaha škrtne o obrubník → **sprška jisker** z titanové lyže pod vozem (~40 jisker se seedem, bílé až `--mb-modra-zare`, letí za vozem a dohasínají 0,4 s) + otřes 5 px. **d3 12,1875**: výjezd, plný plyn, vůz se srovná, za ním **modrá linie nakreslí čisté U**, zadní pneu zanechají slabé tmavé stopy. **d4 12,656**: vůz vystřelí dolů z obrazu, U z modré linie zůstane | bez textu | jiskry s příčinou (G6), otřes na apexu, brzdová světla, světelná stopa | H: kopák, malý buben 11,719 / 12,656 · SFX: kvílení brzd vrchol **11,40**; škrtnutí + praskání jisker vrchol **11,72**; zátah motoru vrchol **12,20** (pod hudbou); „vžum“ odjezdu vrchol **12,70** |
| **13,125–15,000** (T8, MAPA OKRUHU → PRSTENEC) | **d1 13,125**: kamera **oddálí** (jeden pohyb přes celý takt, log zoom 1 → 0,12, ease-in-out, nikdy zpět): vracečka se stane jednou zatáčkou celého okruhu, okruh je **grafická mapa** (obrys tratě 6 px `--mb-stribro` na černé, mapa ~1 100 × 640 px, střed (960; 600)), vůz je teď **jasná modrobílá tečka s ohonem**, která jede kolo stále rychleji a kreslí za sebou modrou linii. **Datový moment bez čísel**: 3 sektorové brány (krátké příčky) se rozsvítí bíle, když jimi tečka projede: **d2 13,594**, **d3 14,0625**, **d4 14,531**. **14,531–15,000 MORF** (vír): tečka dokončí kolo přesně v 15,000 a obrys okruhu se po krocích na údery víru (14,53 / 14,65 / 14,77 / 14,88) **narovná do dokonalého kruhu** Ø 700 px, střed (960; 540) | **13,20 „CHASE THE LINE“** (Archivo 900 kurzíva 112 %, 120 px, bílá, „LINE“ `--mb-modra`, účaří y 230 nad mapou, příchod maskou zdola 0,25 s ease-out). **Odchod 14,30–14,45** maskou nahoru (ease-in), před vírem | log zoom ven, kreslení linie po mapě, sektorové brány, **morf tvaru** (okruh → kruh) | H: kopák, malý buben 13,594 / 14,531, vír 14,53–15,0 · SFX: tiché elektronické „tik“ bran vrchol **13,594 / 14,0625 / 14,531**; uzavření kruhu kovové „ting“ vrchol **15,00** (s činelem H) |
| **15,000–16,875** (T9, **ZLOM: KONTRAST**) | **d1 15,000**: prstenec (Ø 700, linie 8 px stříbrná s modrou září) se uzavře a **po jeho obvodu jednou oběhne světlo** (0,4 s). Pak **klid**: černá, kamera jen dotlačuje 1,00 → 1,03. Za prstencem projíždí **zpomaleně makro boku** hrdinova vozu (jen ostré okrajové světlo na hranách karoserie a modrý proužek), zleva doprava, plynule. **d3 15,9375**: střed boku projede středem obrazu **přesně ve vrcholu dopplera 15,95** a po laku přejede široký **odlesk** (Taxtello: odlesk přes povrch). **d4 16,406**: prstenec se začne **naklánět do 3D** (rotateX 0 → 20°, příprava na T10) | **15,469 „FASTER BY DESIGN“** (Archivo 800, 112 %, 96 px, bílá, střed y 560 **přes** prstenec jako znak, příchod maskou od účaří 0,3 s ease-out, prostrkání se pomalu rozevírá 0,02 → 0,06 em). **Odchod 16,55–16,75** maskou dolů (ease-in) | běh světla po prstenci, zpomalený odlesk, **ticho jako kontrast** (jediný klidný takt, C7) | H: činel 15,0, motor průjezd → vrchol 15,95, bez kopáku · SFX: jen tichý vzduch zpomaleného průjezdu, vrchol **15,95**; nic dalšího (kontrast) |
| **16,875–18,750** (T10, STOUPÁNÍ: 2D → 3D) | **d1 16,875**: prstenec se dokloní (rotateX 20° → 78°) a **stane se klopenou oválnou tratí v perspektivě** (2D → 3D moment šablony showreel); kamera klesne za vůz: **`F1-záď`** hrdina šířka **900 px** (47 %), střed (960; 700), honička po oválu, po stranách tratě ubíhají k divákovi **modré světelné pásy**, rychlostní čáry se sbíhají do úběžníku (960; 470). Na **každý kopák** (16,875 / 17,344 / 17,8125 / 18,281) kamera cukne vpřed (2 %) a pásy pulzují. **17,475 ŘAZENÍ 1**: **glitch akcent** (3 vodorovné řezy posunuté ±24 px, 2 snímky) + chromatický posun 6 px + bliknutí dešťového světla. **18,125 ŘAZENÍ 2**: silnější (5 řezů ±40 px, 3 snímky), hustota čar ×2. Vír zrychluje: čáry se prodlužují, zorný úhel se rozšiřuje (jedním směrem). **18,40–18,75 NÁDECH**: obraz potemní na 50 % kromě dešťového světla, vůz ujede do úběžníku a zmenší se na **jediný svítící bod** ve středu (960; 540) v 18,72 | bez textu | **2D → 3D**, sbíhavé rychlostní čáry, **glitch akcent na řazení**, chromatický posun, potemnění (nádech) | H: kopák, motor rev → 18,75, řazení 17,475 / 18,125, vír zrychluje, obrácený činel 17,81 → 18,75 · SFX: kovové cvaknutí řazení + krátký digitální „zap“ vrchol **17,475** a **18,125**; nasátí vzduchu do **18,74**; **ztlumení hudby −10 dB 18,40–18,75** |
| **18,750–20,625** (T11, **DROP 2: HVĚZDA ZE SVĚTLA**, nejsilnější moment) | **18,750**: svítící bod ve středu se **rozštěpí na tři vozy**, které vystřelí od středu po třech osách hvězdy (nahoru, vpravo dolů 30°, vlevo dolů 150°) a za 0,10 s dojedou ke konci ramen; jejich **stopy jsou ramena hvězdy** (přesná geometrie z `hvezda_generator.py`, bílé jádro + záře `--mb-modra-zare`). Zároveň dopadne **prstenec** (ten z okruhu a zlomu): měřítko 1,6 → 1,0 za 0,12 s, ease-out. Hvězda ze světla **Ø 880 px** (81 % výšky, A8), střed (960; 540). **Bílý záblesk** ze středu (70 % → 0, 3 snímky), **otřes 16 px** (doznívá 0,6 s), radiální rychlostní čáry ze středu, chromatický posun 6 px. **18,80–19,10 ZAPLAVENÍ**: ze středu hvězdy se rozlije **modrá `--mb-modra`** a přesáhne všechny 4 rohy (kruh, 0,30 s, ease-out; Food craving). **19,10–19,22**: modrá se stáhne zpátky **do ramen**, ramena se protáhnou až k okrajům obrazu (čáry 18 px se září) a **rozdělí obraz na 3 výseče** (vlevo nahoře, vpravo nahoře, dole). **d2 19,219**: ve výsečích naskočí tři závody, každý s vlastní kamerou: vlevo nahoře `F1-shora` řítící se nahoru (z T3), vpravo nahoře `GT-bok` průjezd (z T5), dole `F1-předek` letící do kamery (z T3). **Stab 19,453 / 19,922 / 20,391**: jedna výseč po druhé (po směru hodin) **cukne** 1,00 → 1,06 (kriticky tlumeně 0,15 s) a její hrana blikne bíle. Na kopák mikro otřes 3 px | bez textu (obraz je pointa) | **zrod hvězdy ze stop**, záblesk, největší otřes, radiální čáry, chromatický posun, **zaplavení barvou**, rozdělení obrazu hvězdou | H: **úder + činel 18,75**, kopák, stab 18,984 … · SFX: **„světelný úder“ (elektrický třesk + hluboký dopad), vrchol 18,750, 0 až −2 LU**; tři krátké průlety od středu ven vrchol **18,80**; vlna zaplavení „vuff“ vrchol **18,95** |
| **20,625–22,500** (T12, REVOLVER) | **d1 20,625 ŠVIH**: celý rám hvězdy se **otočí o +120°** za 0,22 s (ease-in-out, rotační rozmazání, `--sub 8`) a výseče se vymění jako buben revolveru; nové obsahy: vlevo nahoře **vracečka s jiskrami** (T7), vpravo nahoře **honička zezadu** (`F1-záď`, T10), **dole formace tří vozů shora** (`F1-shora` ×3, hrdina stříbrný uprostřed, nosem dolů, za každým modrá stopa; připravuje T13). **Stab 20,859 / 21,328 / 21,797 / 22,266**: cuk výsečí po směru hodin (jako T11). **d3 21,5625**: **glitch akcent přes celý obraz** (řezy posunuté ve směru ramen, 2 snímky). Kopák = mikro otřes 3 px | bez textu | **švih rotací**, cuky výsečí na staby, glitch akcent | H: kopák, malý buben, staby · SFX: švih „vuš“ rotace vrchol **20,70**; glitch „zap“ vrchol **21,5625** (tiše) |
| **22,500–24,375** (T13, TŘI STOPY) | **d1 22,500 MORF**: dolní ramena se **vyklopí nahoru** (levé −120°, pravé +120°, ease-in-out 0,3 s) a posunou na x 600 a 1 320, horní rameno stojí v x 960: z hvězdy jsou **tři rovnoběžné svislé stopy**, dolní výseč (formace shora) se roztáhne na celý obraz a stopy jsou **stopy tří vozů** (kamera shora jede s nimi, trať ubíhá nahoru, vozy 460 px, nosem dolů, spodní třetina obrazu). **Stab 22,734 / 23,203 / 23,672 / 24,141**: na každý stab si dva vozy **vymění pruh** (boční přesun 360 px, ease-in-out 0,2 s), stopy se **splétají jako cop** (hrdina skončí uprostřed). **d3 23,4375**: pod formací přeletí **příčný světelný portál** (bílá příčka přes celou šířku) + cuk kamery 3 % | bez textu | splétání světelných stop, výměny pruhů na staby, průlet portálem | H: kopák, malý buben, staby · SFX: krátké svištění pneu při výměnách vrchol **22,734 / 23,203 / 23,672 / 24,141** (tiše, střídavě L/P); průlet portálem „fump“ vrchol **23,44** |
| **24,375–26,250** (T14, SBĚH DO HVĚZDY) | **d1 24,375**: tři stopy se **sklopí zpět do úhlů hvězdy** (obrácený morf z 22,5), vozy jedou od středu ven po ramenech. **Stab 24,609 / 25,078 / 25,547**: vozy jeden po druhém **vyletí z obrazu** na konci svého ramene (horní, pravý, levý), za každým zůstane plné rameno. **24,84–25,31**: po obvodu se znovu nakreslí **prstenec** (světlo oběhne kruh) → hvězda ze světla je zase celá (Ø 880). **25,3125–26,250 SMRŠTĚNÍ** (obrácený činel, vír 25,78–26,13): hvězda se zmenšuje Ø 880 → 340 px a posouvá do polohy loga (960; 380), jedno natočení +120° (ease-in, „natažení pružiny“), čáry tenčí, záře houstne; v **26,016** (poslední stab) vše kromě hvězdy potemní na černou | bez textu | vyletění vozů na staby, kreslení prstence světlem, smrštění hvězdy (napětí) | H: kopák, staby, obrácený činel → 26,25, vír · SFX: tři průlety ven „vžum“ vrchol **24,61 / 25,08 / 25,55** (P, L, střed); smrštění „sání“ do **26,24** |
| **26,250–28,125** (T15, **END CARD**: ZACVAKNUTÍ) | **26,250**: hvězda ze světla se **zacvakne do loga**: na jejím místě je `mercedes-hvezda-fazety.svg` (kov, **Ø 340 px**, střed (960; 380), natočení 0°, jen jednotné měřítko), světlo stéká do fazet (záře 100 → 15 % za 0,4 s, ease-out), tenký bílý kruh od okraje loga ven (0,1 s), **otřes 6 px** krátce. **26,25–26,72 POSLEDNÍ JÍZDA**: pod logem zleva doprava projede světlo vozu a **nakreslí modrou linii** y 735, délka 0 → 1 100 px, střed x 960 (ease-out); **26,6** (řazení) linie jednou blikne. Kamera **dotlačuje 1,00 → 1,04** až do 30,0 (ease-in-out, nikdy zamrzlý obraz). Kolem loga volno ≥ 85 px (25 % průměru) | **26,719 „Mercedes-Benz“** (Archivo 600, 100 %, 64 px, prostrkání 0,06 em, bílá, účaří y 690) se rozevře **maskou od osy loga ke krajům** (0,35 s, ease-out; obdoba Food craving „wordmark wipes out from behind the mark“). **27,1875 „FOLLOW THE STAR“** (Archivo 900 kurzíva 112 %, 88 px, „STAR“ `--mb-modra`, účaří y 840) vyroste **z modré linie** maskou (0,3 s, ease-out). **27,656 disclaimer** „Concept ad · not affiliated with Mercedes-Benz“ (Inter Tight 500, 26 px, `--mb-seda`, účaří y 920) najede krytím + 6 px nahoru (0,3 s). Každý vstup skončí dřív, než začne další | přerod světla v kov, kreslení linie, maskované vstupy textu | H: **úder + činel 26,25**, motor odjezd, řazení 26,6, basa A1, dozvuk · SFX: **měkký kovový dopad loga + „cink“, vrchol 26,250, 0 až −3 LU**; průjezd pod logem (odjezd, doppler) vrchol **26,45** |
| **28,125–30,000** (T16, END CARD: DRŽENÍ) | **d1 28,125**: po kovové hvězdě přejede **odlesk** (stejný jako na snímku 0, 0,6 s, ease-in-out) = rým se začátkem. **d2 28,594**: po modré linii proběhne slabý světelný impuls zleva doprava (0,5 s). Pak jen dotlačování kamery do 30,0 (žádný zamrzlý snímek, poslední snímek čistý, bez rozmazání) | vše drží: logo + Mercedes-Benz + FOLLOW THE STAR + disclaimer | odlesk na logu, impuls po linii, dotlačení | H: dozvuk do 30,0 · SFX: jemné „ting“ odlesku vrchol **28,20** (tiše) |

**Kde jsou 4 zvolené motiony** (kritik je má umět pojmenovat s časy, kritérium 9):
| motion | co z něj bereme (podle skutečného textu promptu) | kde ve videu |
|---|---|---|
| **Šablona showreel** | kostra na doby, „something happens on every beat“, **jedna technika na takt** a každá vzniká z předchozí, rozsah: kinetická typografie, morf tvaru, **2D → 3D moment**, datový moment, end title; poslední celý takt před end card nejsilnější; kontrola snímku na každou dobu | celá osa (T3 zoom, T4 typografie, T5 paralaxa, T6 tiker, T7 jiskry, T8 **data + morf** 13,1–15,0, T10 **2D → 3D** 16,9–18,75, T14 smrštění), end title 26,25–30 |
| **Taxtello app film** (`daniel-haida-8691d4`) | odlesk, který odhalí značku („a tiny glint“, „machined precision“), přechody z objektu („of course the next scene came from that“), **písmo jako přechod** (kamera skrz písmeno), odlesk přejíždějící po povrchu, klidnější scéna před pointou, oblouk CHAOS → CONTROL → CLARITY → ZNAČKA, prémiový snímek 0 | odlesk 0,0–0,9 a 28,125 (rým), zoom skrz „A“ 10,78–11,25, zpomalený odlesk boku 15,95, zlom 15,0–16,875, nájezd do hvězdy 2,81–4,2 |
| **UGC ad generator promo** (`twoclipping-6dd14e`) | na dropu **kruh, který se otevře z prvku do tmavé scény**, maskované odhalení textu, velký text na **„push cuts“** a **tiker 3 slov**, švih s rozmazáním na hrdinu, mřížka dob **zkalibrovaná na skutečné kopáky**, SFX podle změřeného vrcholu, past `preserve-3d` + opacity | průlet prstencem hvězdy 4,05–4,22, BUILT · TO · RACE 9,375–10,31, švihy 5,625 / 8,906 / 20,625, masky CHASE THE LINE / FASTER BY DESIGN / FOLLOW THE STAR |
| **Food craving launch film** (`ultimaxbt-2ddf1e`) | **jeden souvislý záběr bez střihů a prolínaček**, každá scéna roste z předchozí, **barva se rozlije z objektu a stáhne do jiného**, jeden plynulý pohyb kamery na scénu, nikdy zoom tam a zpět, bod/značka se promění v logo a wordmark se rozevře | modré zaplavení z hvězdy 18,80–19,22 (stáhne se do ramen), linie → účaří → okraj tratě → mapa → prstenec, svítící bod 18,72 → hvězda, end card 26,25–27,1 |
Vědomé odchylky od promptů (kvůli vkusu uživatele, G6, V001): šablona showreel, Taxtello i UGC promo **zakazují** třes kamery, glitch a záři.
My je používáme **jen na hudební údery a s příčinou v ději** (start, apex, řazení, drop 2, logo), ne plošně. Smyčka (poslední snímek = první) se nedělá,
end card je jen rýmovaný odleskem z 0,0 (D4 tu ustupuje end card podle zadání).

**Seznam efektů synchronních s hudbou** (≥ 6 různých, kritérium 3):
1. **Rychlostní čáry**: radiální 3,75–4,2 a 18,75; vodorovná paralaxa 7,5–9,3; sbíhavé do úběžníku 16,875–18,75.
2. **Světelné stopy**: modrá linie 4,22–15,0 (S, účaří, okraj tratě, U, kolo okruhu), tři stopy / ramena 18,75–26,25, podtržení 26,25–26,72.
3. **Záblesk + otřes kamery na úderu**: 3,75 (12 px), 11,719 (5 px, bez záblesku), 18,75 (16 px, nejsilnější), 26,25 (6 px); mikro otřes 3 px na kopáky T11–T12.
4. **Švih s rozmazáním**: rotace −90° 5,625; vodorovný 8,906; rotace revolveru +120° 20,625.
5. **Zoom skrz objekt**: prstenec hvězdy 4,05–4,22; otvor písmene „A“ 10,78–11,25.
6. **Zaplavení barvou**: modrá z hvězdy 18,80–19,22.
7. **Glitch akcent**: řazení 17,475 a 18,125, staby 21,5625.
8. **Chromatický posun** (jen na švihu a dropech): 3,75, 5,625, 17,475, 18,125, 18,75.
9. **Jiskry z dopadu** (s příčinou): apex 11,719.
10. **Cuky / push cuts na doby**: lampy 0,469–2,344, tiker 9,375–10,3125, výseče na staby 19,45–22,27.
11. **Odlesky**: glint 0,0 a 28,125, reflektory na laku T5 (na každou dobu), zpomalený odlesk 15,95.
12. **Morf tvaru**: okruh → kruh 14,53–15,0, prstenec → klopená trať 16,875, hvězda → 3 rovnoběžné stopy 22,5 a zpět 24,375, světlo → kov 26,25.
13. **Roztažení / maska písma**: FULL THROTTLE 5,625, písmena RACE jako okna 10,31.

**Kontrolní snímky a kritéria odmítnutí** (každý snímek posoudit i na zmenšenině **480 px šířky**; 16:9 se na telefonu dívá na šířku i v okně feedu):
| čas | co musí být vidět | odmítnout, když |
|---|---|---|
| **0,000** | hotový plakát: lampy → (prázdné místo) → formule zepředu, odlesk na levé třetině | je to tma / zatmívačka; vůz nejde na 480 px poznat jako formule (vypadá jako hračka, obecné auto nebo „AI render“); lampy splývají s vozem |
| 0,55 | „LIGHTS“ ostré, lampa 1 červená s odrazem | text se dotýká lamp nebo vozu (< 40 px); červená jinde než v lampě a jejích odrazech |
| 2,40 | 5 lamp, napětí | obraz se nehýbe (chvění a nájezd musí být znát v sousedních snímcích) |
| 3,70 | nádech: stojí, svítí jen lampy | cokoli se hýbe rychle; lampy už zhasly |
| **3,767** | LIGHTS OUT celé, lampy zhasnuté, záblesk doznívá, start | dva řádky textu; záblesk > 3 snímky nebo přes 70 %; „OUT“ nemá stejnou velikost a účaří jako „LIGHTS“ |
| 4,00 / 4,12 / 4,22 | text pryč; hvězda zaplňuje obraz; kruh se otvírá do pohledu shora | text je ještě vidět při průletu; hvězda je zdeformovaná (nejednotné měřítko); v průletu „prázdná“ černá > 2 snímky |
| 5,00 | shora: hrdina 620 px, modrá linie, soupeři za ním | linie je přerušená nebo „skáče“; vůz nečitelný jako formule shora |
| 5,72 / 6,20 | švih končí, FULL THROTTLE leží na linii | text pod linií nebo mimo 96–1 824 px; písmena animovaná po jednom místo jako blok při příchodu |
| 7,10 | GT prosviští, text se trhá | text ještě celý stojí, když vůz projíždí (nemá příčinu odchodu) |
| 8,00 | bok GT 1 400 px, paralaxa | GT nečitelné jako závodní kupé (chybí křídlo / difuzor), statické pozadí |
| 9,40 / 9,87 / 10,34 | BUILT / TO / RACE, vždy jen jedno slovo | ve snímku dvě slova; RACE bez obsahu v oknech |
| 11,00 | let do „A“, v otvoru už vracečka | otvor prázdný; skok místo plynulého zoomu |
| 11,75 | apex, jiskry od vozu | jiskry odjinud než zpod vozu, „ohňostroj“ bez směru |
| 13,60 / 14,40 | mapa okruhu, CHASE THE LINE, brána svítí | mapa jako generická „HUD“ grafika s čísly / popisky v rozích; text přes mapu |
| **15,00** | dokonalý kruh, světlo na obvodu | kruh není kruh (zbytky zatáček); obraz je černý bez prvku |
| 15,95 | FASTER BY DESIGN přes prstenec, bok s odleskem | text nečitelný přes bok (kontrast); zlom není klidnější než okolí |
| 17,49 / 18,14 | glitch na řazení, 3D honička | glitch déle než 3 snímky nebo mimo řazení; pohled nepůsobí 3D (plochý ovál) |
| 18,72 | jen svítící bod, potemnělý obraz | nádech není poznat (obraz stejně jasný jako 18,0) |
| **18,767 / 18,80 / 18,85** | **hvězda ze světla Ø 880**, prstenec, záblesk, otřes | hvězda neodpovídá geometrii loga; ramena nejsou stopy vozů (bez vozů na koncích); slabší dojem než 3,767; na 480 px to není hvězda Mercedes |
| 19,00 / 19,30 | zaplavení přes všechny rohy, pak 3 výseče se závody | zaplavení nepřesáhne rohy (vypadá jako záblesk); ve výsečích statické obrázky |
| 20,70 / 21,00 | revolver po švihu, nové obsahy | obsahy se jen vyměnily bez rotace |
| 22,65 / 23,30 | tři rovnoběžné stopy, splétání | morf skočil; vozy se překrývají |
| 25,20 / 26,00 | celá hvězda ze světla, smršťování k poloze loga | hvězda se deformuje; logo bliká |
| **26,30 / 27,80 / 29,98** | kovové logo Ø 340, linie, Mercedes-Benz, FOLLOW THE STAR, disclaimer | logo zdeformované / nedostatek volna (< 85 px); dva texty v pohybu naráz; zamrzlý obraz (29,98 = 29,0 pixel po pixelu); disclaimer pod y 940 |
Plus `--nahled doby --bpm 128` (64 snímků) a pásy sousedních snímků (`--sub 8`) u 3,75 / 4,15 / 5,625 / 10,78–11,25 / 17,475 / 18,75 / 20,625 / 26,25.

**Pasti stavby**:
- **Vozy jsou riziko č. 1.** Kreslit je jako prémiovou siluetu z okrajového světla (rim light) a několika ploch laku, ne jako detailní ilustraci. Každou kresbu
  ověřit samostatně na 480 px dřív, než jde do scény. Formule = halo, široké odhalené pneu, přední a zadní křídlo. GT = dlouhá kapota, zadní křídlo na stojkách, difuzor.
  Žádná čísla, jména, loga sponzorů, ani tyrkysová (C8).
- **Hvězda**: ramena, prstenec i výseče počítat z `hvezda_generator.py` (střed 0,0, R 283; ramena −90°, 30°, 150°). Hvězda ze světla smí mít záři, ale obrys
  ramen musí sedět na logo, aby zacvaknutí v 26,25 bylo bez skoku (porovnat 26,23 a 26,27 po pixelech). Logo jen jednotné měřítko + otočení.
- **Text**: nikdy dvě vrstvy textu v jednom snímku (V001). Tiker = výměna v jednom snímku. Odchod vždy skončí dřív, než začne příchod.
  Fonty změřit až po načtení (C016), šířky změřit v prohlížeči (FULL THROTTLE, FASTER BY DESIGN ≤ 1 600 px, jinak zmenšit blok celý).
- **Záblesky**: max. 3 snímky, max. 70 % krytí, nikdy víc než 3 záblesky za sekundu (fotosenzitivita). Staby = blik jen hrany výseče, ne celé plochy.
- **Otřes kamery**: šum se seedem (`nahoda(seed)`), doznívá exponenciálně, jen na uvedených časech; během čtení textu ≤ 3 px.
- **Červená** (`--mb-brzdove-svetlo`) jen v lampách, jejich odrazech, dešťovém světle a brzdách. Nikdy text, nikdy plocha.
- **Výkon (4 CPU, bez GPU)**: záře a rychlostní čáry kreslit do canvasu, záře jako předem rozmazaný sprite (ne CSS `filter: blur` na velké vrstvy v každém podsnímku).
  Výseče = 3 výřezy (`clip-path` / canvas clip) jedné sdílené knihovny vozů, ne 3 kopie celé scény. Rozmazání pohybem v kódu podle rychlosti + `--sub 4`, rychlé úseky `--sub 8`.
- **3D**: nikdy `opacity` / `filter` na prvku s `preserve-3d` (UGC promo); prolínat obal. `will-change` ne na prvky, které kamera škáluje.
- **Kamera**: jeden pohyb na scénu, žádný zoom tam a zpět (F7); otřes je přičtený zvlášť a nepočítá se jako pohyb kamery.
- **Zaplavení** musí přesáhnout všechny 4 rohy a trvat ~0,3 s, jinak vypadá jako záblesk.
- **Deterministika**: vše z `seek(t)`, jiskry, bokeh, šum asfaltu a glitch řezy se seedem; časy událostí z `hudba.json`, ne ručně.

**Pořadí stavby** (fáze 2):
1. **Knihovna vozů + hvězda**: 4 kresby vozů a hvězda ze světla na jednom testovacím listu 1920×1080 → zmenšenina 480 px → schválí kreativní ředitel. Bez schválení nic dál.
2. **Klíčové snímky jako statické obrazy**: **18,80 (drop 2: hvězda ze stop)** a **3,767 (drop 1: LIGHTS OUT + start)**, pak 0,000 (náhled), 19,30 (výseče) a 27,80 (end card). Schválit.
3. **Pohyb dropů**: 3,28–4,60 a 17,80–19,50 včetně pásů snímků `--sub 8`.
4. Zbytek po blocích: T1–T2, T3–T5, T6–T8, T9–T10, T11–T14, end card. Po každém bloku snímky na doby.
5. `--nahled doby --bpm 128` celého videa, oprava, pak plný render 60 fps.

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
