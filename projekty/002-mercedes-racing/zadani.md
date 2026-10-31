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

- **Odpovědi režiséra na otázky agentů po přípravě** (2026-10-31):
  - Logo z Commons stačí (tvar odpovídá oficiální hvězdě, spec reklama s disclaimerem). Do popisku uvést „Mercedes star: Khaled / Wikimedia Commons, CC BY-SA 4.0“.
  - Hlavní hvězda na end card = **fazetová kovová** (lesk na finálním úderu 26,25), plochá jen pro masky a záblesky.
  - Brzdová / dešťová světla `--mb-brzdove-svetlo` smí zůstat jako fyzické světlo vozu a lampy (malé plochy, nikdy text, nikdy plocha).
  - **Souhlas s revizí S2**: CTA **mercedes-benz.cz** místo nápisu Mercedes-Benz (uživatel chtěl reklamu na tento web, disclaimer zůstává),
    4 hesla (LIGHTS OUT, CHASE THE LINE, BUILT TO RACE, FOLLOW THE STAR), výseče = tři kamery na jeden okamžik.
  - Paleta: jedeme s předběžnou (#0078D6). Když uživatel pošle screenshot před finálním renderem, vymění se proměnné v `znacka.css`.
  - Varianta vozu A / B: rozhodne kreativní ředitel při schválení zkušebního listu (zmenšenina 480 px).
  - SFX: zvukař ve výrobě bere časy ze Storyboardu S2 (včetně nových a posunutých SFX), ne ze S1.
  - Zlom 15,0–16,875 zůstává bez rytmu (kontrast, nejdelší mezera ~0,95 s je v toleranci kritéria 3).
  - `master_zvuk.sh` limiter bez `latency=1` (posun 5 ms) opravil režisér (C025). Dynamický loudnorm u ostatních nálad = dluh (C026).

- **Odchylky od storyboardu S2 schválené režisérem při stavbě** (kritik je nehlásí jako chybu):
  zoom do otvoru „A“ ×74 místo ×24 (změřený otvor je menší, jinak by v 11,25 zůstal obrys písmene) · vůz z vracečky vystřelí nahoru (geometrie U) ·
  hranice bloků 18,75 (v 18,72 jen bod a slabé hrany tratě) · švih 5,625 vrcholí 5,695, v 5,72 dobíhá ~15° · soupeř v T5 ~10–15 % obrazu
  (kola hrdiny zůstávají na linii) · výseče: ramena prodloužená k okraji jako pás šířky špičky · prstenec mizí při odkrytí výsečí 19,453–19,553 ·
  GT-bok = varianta B (tmavá silueta s okrajovým světlem a stříbrnou horní plochou).
  Blok C: okamžik B (20,74–22,27) hrdina shora jen ~20 % šířky dolní výseče (plynulé přerostení do T13) · vozy v T14 jsou světelné (rým s drop 2) ·
  smrštění hvězdy ease-in, zacvaknutí v 26,25 je zastavení v plné rychlosti (tvar, střed a měřítko v 26,25 přesně).

## Akceptační kritéria pro kritika
1. 1920×1080, 60 fps, 30,0 s ± 0,1 s, H.264 + AAC, BT.709
2. −14 LUFS ±1, true peak ≤ −1 dBTP (po AAC)
3. **Energie**: událost na každou dobu, úder každý takt, žádná „mrtvá“ pasáž > ~1 s, aspoň 6 různých energických efektů
   (rychlostní čáry, světelné stopy, záblesk/otřes na úderu, švih, zoom, glitch akcent…) synchronních s hudbou
4. Hvězda Mercedes (tvar z Wikimedia Commons), nedeformovaná. Barvy jen z `znacka.css` (předběžná paleta webu, k ověření screenshotem)
5. Je poznat, že jde o **závodění** (vozy, trať, rychlost) a o **Mercedes**
6. Hudba sportovní, drop 1 v 3,75 s a drop 2 v 18,75 s jsou vizuálně nejsilnější momenty, klíčové SFX slyšet (I3)
7. End card: kovová hvězda + **mercedes-benz.cz** + FOLLOW THE STAR + disclaimer, drží ~3,75 s, nezamrzlý
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
- **Koncept jednou větou** (kreativní ředitel, 2026-10-31): **„FOLLOW THE STAR: závodní linie kreslí hvězdu.“** Modrá světelná stopa, kterou stříbrný šíp táhne za sebou od zhasnutí startovních světel, je celou dobu **nedokončená hvězda Mercedes**: ve zlomu se okruh uzavře do prstence, ve druhém dropu do něj tři vozy vstřelí tři ramena a vznikne **hvězda ze světla** (celou jednu dobu stojí čistá jako plakát), která pak rozdělí obraz na tři výseče = **tři kamery na jeden okamžik** hrdinova vozu, nakonec se zacvakne do loga a pod ním se otevře **mercedes-benz.cz**.
  **Duše** = člověk, který čeká: v hledí helmy jezdce se po jedné zrcadlí rozsvěcené startovní lampy a ve 3,75 v hledí zhasnou (oponentura S1).
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
    nadpisy `font-stretch:125%; font-weight:900`, pro rychlost kurzíva, VERZÁLKY; podnadpisy 112 % / 800; CTA „mercedes-benz.cz“ na end card 100 % / 600 s prostrkáním 0,04 em
    (**ne** „Mercedes-Benz“ pod hvězdou: to by byl napodobený lockup slovní značky).
    Proč: rozšířený grotesk = závodní / motorsport vzhled, přitom střídmý a „německy“ technický jako Corpo S; jedna proměnná rodina = nadpis i text.
    Text a disclaimer: **Inter Tight** 500 (nejbližší neutrálnímu Corpo S). Patkové Corpo A (slovní značka) **nenapodobovat**, nevypadalo by to jako falešné logo.
    Pozor: Archivo 125 % / 900 při 170 px má na řádek max. ~12 znaků v bezpečné zóně (A5), „CHASE THE LINE“ (14 znaků) proto 112 % / 140 px, změřit, při > 1 600 px celý blok 120 px.
    Do `FONTY` ve scéně: `'900 italic 150px Archivo'`, `'800 150px Archivo'`, `'600 60px Archivo'`, `'500 40px "Inter Tight"'` (C016).
  - **Logo**: `mercedes-hvezda-plocha.svg` (hlavní, `currentColor`), `mercedes-hvezda-fazety.svg` (kov), chrom jen jako PNG. Hvězdu nedeformovat
    (jen jednotné měřítko a otočení), prostor kolem ≥ 25 % průměru, na end card průměr ~300–360 px.
  - **Hesla** (po oponentuře S1 jen **4**, každé nese příběh konceptu, žádné obecné závodní fráze): **LIGHTS OUT** (3,75, drop 1) →
    **CHASE THE LINE** (5,625, leží na modré linii) → **BUILT TO RACE** (9,375, tiker) → **FOLLOW THE STAR** (27,19, end card).
    Vyřazeno: FULL THROTTLE, FASTER BY DESIGN, EVERY CORNER COUNTS (šablonovité). **CTA** na end card: **mercedes-benz.cz** (zadání: reklama na web).
    Disclaimer: „Concept ad · not affiliated with Mercedes-Benz“.

## Storyboard / časová osa
**Storyboard S2** (kreativní ředitel, 2026-10-31; S1 přepracovaný podle oponentury, viz „Změny po oponentuře“ na konci oddílu), koncept „FOLLOW THE STAR: závodní linie kreslí hvězdu“. Časy z `media/projekty/002-mercedes-racing/hudba.json`:
128 BPM, doba 0,46875 s, takt 1,875 s, T<n> začíná v (n−1)·1,875 s, doby d1–d4 = +0 / +0,469 / +0,9375 / +1,406.
Hudební události, na které se obraz váže (animátor je bere z `udalosti_nastroju`, ne ručně): kopák od 1,875 na každou dobu (v T9 nic),
malý buben d2 a d4 od T3, **stab** na „a“ za každou dobou T11–T14 (18,984 + k·0,469; poslední 26,25), motor: rev 1,875 → vrchol 3,75,
průjezd 15,0 → vrchol 15,95, rev 16,875 → vrchol 18,75, odjezd 26,25; řazení 2,625 / 17,475 / 18,125 / 26,6; vír 2,81–3,75, 14,53–15,0,
16,875–18,75 (zrychluje), 25,78–26,25; obrácený činel do 3,75 / 18,75 / 26,25; úder + činel 3,75 / 18,75 / 26,25, činel 15,0.

**Svět a kamera**: noc, černá a grafit, vozy jen jako stříbrný lak s ostrým okrajovým světlem (rim light) a modré světlo; vše v kódu (SVG + canvas).
Jedna kamera (posun + otočení + log zoom), mezi scénami se neresetuje: každý přechod je pohyb skrz prvek, který už je v obraze (D2, Food craving).
**Knihovna vozů (4 kresby, znovu použité)**: `F1-předek` (formule zepředu: přední křídlo, nos s odznakem Ø 110 px, halo **s helmou jezdce a lesklým hledím**, airbox, široké pneu), `F1-shora` (půdorys formule,
délka 1 : 2,6 šířky), `GT-bok` (závodní kupé z boku: dlouhá kapota, nízká kabina, velké zadní křídlo, difuzor), `F1-záď` (formule zezadu: zadní křídlo,
dešťové světlo, difuzor, pneu). Hrdina = stříbrný lak (`--mb-stribro*`) + tenký modrý proužek, soupeři = grafit (`--mb-grafit`) se šedým okrajem.
**Žádná startovní čísla, jména, sponzoři ani tyrkysová** (C8). Hvězda na nose / boku jako odznak z `mercedes-hvezda-plocha.svg` (na nose `F1-předek` Ø 110 px, jinde ≥ 5 % šířky vozu).
Každá kresba má na zkušebním listu **dvě varianty**: **A** podle storyboardu (lak + okrajové světlo + detaily) a **B** silueta z okrajového světla (~80 % vozu černé,
vidět jen hrany křídel, halo, pneu, světlo na nose / ostré hrany karoserie). Když A na 480 px vypadá jako hračka nebo klipart, jede B (rozhodne kreativní ředitel).
**Text**: Archivo (nadpisy 900 kurzíva, šířka 112–125 %, VERZÁLKY), vždy **jen jedna vrstva textu v obraze**; tiker = střih slova na dobu (staré zmizí
ve stejném snímku, kdy přijde nové). Všechny texty uvnitř x 96–1824, y 54–940 (A5, spodních 140 px kryje přehrávač).
**SFX** = pro zvukaře, **změřený vrchol přesně na uvedeném čase**. H = hudba (už v `hudba.wav`). Klíčové SFX (drop 1, drop 2, logo) slyšet 0 až −3 LU (I3),
ostatní tiše pod hudbou. **Automatika hudby**: −9 dB 3,52–3,75 (nádech před LIGHTS OUT), −10 dB 18,40–18,75 (nádech před hvězdou), náběh 0,15 s, doběh 0,03 s.

| čas (takt · doba) | obraz | text | efekt | zvuk / událost (SFX s vrcholem na čase) |
|---|---|---|---|---|
| **0,000–1,875** (T1, ÚVOD: STARTOVNÍ ROŠT) | **Snímek 0 = náhled**: noční rošt, kamera nízko zepředu. `F1-předek` stříbrný, šířka **1 400 px** (73 %, A8), výška ~670 px, střed x 960, spodek pneu y 1 030 (airbox / halo nahoře v y ~370), **odznak hvězdy na nose Ø 110 px** v (960; 760) (na 480 px = 27 px, Mercedes poznat i bez barvy). **V halo helma jezdce** (grafit se stříbrnou hranou, bez barev, jmen a čísel), tmavé lesklé **hledí** ~130 × 36 px. Pod vozem mokrý asfalt, odraz vozu (krytí 22 %, modrý nádech) skoro celý pod spodním okrajem. **Portál startovních světel = tmavá silueta v popředí** u horního okraje (nosník y 0–150, 5 pouzder Ø 84 px v řadě x 640–1280, střed y 110, k nám zadní stranou, protože lampy svítí na rošt): rozsvícená lampa je vidět jako **rozptýlené červené světlo** (záře kolem pouzdra, červený závoj dolů v jemném oparu) a jako **odrazy** na laku, asfaltu a v hledí. Skladba odshora: portál → nápis → vůz, mezi nápisem a vozem ≥ 40 px (ověřit na klíčovém snímku). Okrajové světlo zprava shora, modrá záře pod podlahou. **Odlesk** (Taxtello glint, bílý pruh 40 px pod 20°) jede **0,000–0,9375** ease-in-out souměrně z x 560 (levá třetina vozu, snímek 0) do x 1 360, **střed x 960 přesně v 0,469**: přejede přes hvězdu na nose spolu s „LIGHTS“ a první lampou → **hvězda blýskne** (jas odznaku 100 → 160 → 100 % za 3 snímky). **d2 0,469**: lampa 1 se rozsvítí (červená záře, odraz na laku a asfaltu, **1. červená tečka v hledí zleva**) + kamera **cuk vpřed** 1,000 → 1,015 (kriticky tlumeně 0,2 s). **d3 0,938**: lampa 2 + 2. tečka v hledí + cuk. **d4 1,406**: lampa 3 + 3. tečka + cuk. | **0,469 „LIGHTS“** (Archivo 900 kurzíva 125 %, 150 px, bílá, účaří y 320 mezi portálem a vozem, celé „LIGHTS OUT“ ≤ 1 400 px a vystředěné; stojí na své konečné pozici vlevo, místo pro „OUT“ vpravo zůstává **prázdné** = napětí). Dopad: měřítko 1,25 → 1,00 + rozmazání 12 → 0 px za 0,12 s, ease-out, bez překmitu | odlesk přes hvězdu na dobu, rozsvícení lamp s odrazy na laku a v hledí, cuk kamery na dobu | H: arpeggio, tlesknutí 0,469 a 1,406 · SFX: elektrické „klonk“ relé lampy, vrchol **0,469 / 0,938 / 1,406** (tiše, ale čitelně); drobné kovové „ting“ blýsknutí hvězdy vrchol **0,469** (pod klonkem) |
| **1,875–3,750** (T2, REV A NÁDECH) | **d1 1,875**: lampa 4 + 4. tečka v hledí + cuk (první kopák, motor začne vytáčet). **d2 2,344**: lampa 5, **všech 5 svítí**, v hledí řada 5 červených teček + cuk. **2,625** (řazení / prošlápnutí plynu): vůz se přikrčí 6 px dolů a vrátí (0,18 s, kriticky tlumeně), z výfuku krátký tetelivý pruh, helma se nepatrně zhoupne vpřed (3 px). **d3 2,8125** (začíná vír): kamera **jeden pomalý nájezd** 1,06 → 1,20 (ease-in) k nosu vozu až do 3,75; vůz se chvěje (šum se seedem, amplituda 0 → 3 px), vinětace se stahuje 0 → 35 %. **3,52–3,75 NÁDECH**: chvění ustane, všechno stojí, svítí jen červená záře lamp a 5 teček v hledí | „LIGHTS“ drží | stupňované chvění, stahující se vinětace, „zmrazení“ před dropem | H: kopák 1,875 / 2,344 / 2,8125, motor rev → 3,75, řazení 2,625, vír 2,81–3,75, obrácený činel · SFX: „klonk“ lamp vrchol **1,875 / 2,344**; 3,52–3,75 **ztlumení hudby −9 dB** |
| **3,750–5,625** (T3, **DROP 1: LIGHTS OUT**) | **3,750 (1 snímek)**: všech 5 lamp **zhasne naráz**, červená zmizí z portálu, laku, asfaltu **i z hledí** (5 teček zhasne v tomtéž snímku). Bílý záblesk z portálu (krytí 60 % → 0 za 0,08 s, max. 3 snímky). Kamera **otřes 12 px** (seed, doznívá 0,5 s). **START**: zadní kola prokluzují (pruh kouře grafit), vůz se řítí do kamery: měřítko 1 → 3,2 za 3,75–4,05 (ease-in, kubicky) **se středem měřítka v odznaku** (960; 760) a kamera odznak týmž pohybem dotlačí do středu (960; 540) do 4,05 (jeden pohyb, ne dva); **radiální rychlostní čáry** vyrazí od hvězdy na nose (canvas, ~120 čar, bílé a `--mb-modra-zare`, délka podle rychlosti) s chromatickým posunem 4 px **jen na čarách**. **4,05–4,219 ZOOM SKRZ HVĚZDU**: odznak (Ø ~350 px v 4,05) zaplní obraz, kamera proletí **prstencem hvězdy** (Ø 350 → 3 000 px, log zoom) a vnitřek prstence se otevře jako kruh do nové scény (UGC promo: kruh z tlačítka do tmavé scény). **d2 4,219**: **POHLED SHORA**: noční trať, `F1-shora` hrdina délka 620 px, nos nahoru, střed (960; 640), kamera ho drží a trať ujíždí dolů; ze zadního světla se rodí **MODRÁ LINIE** (jádro 10 px bílá, záře 40 px `--mb-modra-zare`). Obrubníky (grafit/bílá) prolétají. **d3 4,6875**: hrdina projede mezi dvěma soupeři (grafit, F1-shora) a ti zůstanou za ním (předjetí, úkrok 30 px). **d4 5,156**: hrdina švihne doprava do ideální stopy, linie za ním nakreslí „S“; kamera se nakloní 0 → −4° (jediný pohyb scény) | **3,750 „OUT“** dopadne vpravo vedle „LIGHTS“ (stejný řez, **`--mb-modra`**, tvrdší: měřítko 1,40 → 1,00, rozmazání 20 → 0 za 0,10 s) → „LIGHTS OUT“ je jeden řádek, jedna vrstva, **titulek celého videa**: stojí celý **3,75–4,05** (18 snímků, otřes na něm doznívá). **4,05–4,15** odjede ease-in nahoru z obrazu, v okamžiku, kdy rostoucí hvězda zakryje vůz (text je součástí světa, vůz ho „rozrazí“) | záblesk, otřes, radiální rychlostní čáry s chromatickým posunem, **zoom skrz objekt (hvězda)**, zrod světelné stopy | H: **úder + činel 3,75**, kopák, malý buben 4,219 / 5,156 · SFX: **odpal: prásk + řev motoru, vrchol 3,750, 0 až −2 LU**; průlet prstencem „vššš“ vrchol **4,15**; projetí soupeřů (doppler, tiše) vrchol **4,70**; cvrknutí pneu vrchol **5,156** |
| **5,625–7,500** (T4, CHASE THE LINE: KINETICKÁ TYPOGRAFIE NA LINII) | **d1 5,625 ŠVIH**: kamera se otočí o −90° za 0,18 s (ease-in-out, rotační rozmazání podle rychlosti, render `--sub 8`); pohled shora se rozmaže do pruhů a po švihu leží **modrá linie vodorovně** přes celý obraz v y 660 (od okraje k okraji), pozadí černé s jemným zrnem asfaltu. Je to **táž linie** ze zadního světla, jen otočená: nápis na ní doslova stojí. **d2 6,094**: po linii proběhne zprava doleva **světelný impuls** (0,3 s) a písmena nad ním nadskočí o 10 px (vlna po 15 ms, kriticky tlumeně = „plyn“). **d3 6,5625**: druhý, silnější impuls, linie ztloustne 10 → 16 px, „LINE“ se rozsvítí jako linie sama (bílé jádro 0,15 s), kamera cuk 1,00 → 1,03. **d4 7,031**: po linii zprava doleva prosviští **`GT-bok`** hrdina (délka 900 px, kola na linii, průjezd 0,3 s, rozmazání podle rychlosti) a jeho proud vzduchu strhne text; linie zůstane a stane se **okrajem tratě** | **5,625 „CHASE THE LINE“** (Archivo 900 kurzíva 112 %, 140 px, „CHASE THE“ bílá, **„LINE“ `--mb-modra`**, účaří = horní hrana linie y 655, max. šířka 1 600 px, jinak celý blok 120 px): přijede zprava po linii jako jeden objekt, roztažený vodorovně 180 % → 100 % s vodorovnou šmouhou, usadí se 5,625–5,95 (ease-out). „LINE“ leží přímo na modré linii a barvou s ní srůstá = nápis ukazuje spojovací prvek. **7,031–7,25** odchod: písmena se protáhnou doleva a zmizí (ease-in, za vozem) | **švih s rozmazáním (rotace)**, roztažení textu (E6), světelný impuls po linii, průjezd vozu | H: kopák na každou dobu, malý buben 6,094 / 7,031 · SFX: švih „vuš“ vrchol **5,70**; dopad textu (tupý kovový úder) vrchol **5,75**; elektrické „cink“ impulsu vrchol **6,094** a **6,5625** (tiše); průjezd GT (řev + doppler) vrchol **7,10** |
| **7,500–9,375** (T5, PRŮJEZD Z BOKU) | **d1 7,500**: kamera se „chytí“ vozu: `GT-bok` hrdina **1 400 px** (73 %), střed (960; 600), kola na modré linii (okraj tratě) y 760, jede zprava doleva, kamera ho drží a svět ujíždí doprava. **Paralaxa ve 4 vrstvách**: daleko rozmazané světla tribuny (bokeh bílé a modré tečky, pomalu), střed svislé sloupky plotu (rozmazané, rychle), blízko obrubník na linii (grafit/bílá, velmi rychle), popředí: na kopák 7,500 a 8,4375 přes celý obraz prosviští **tmavý sloup** (rytmický wipe, 3 snímky). Kola: rotace paprsků s rozmazáním. Na **každou dobu** přejede po laku **odlesk reflektoru** (bílý pruh zleva doprava, 0,25 s) = událost na dobu. **d2 7,969**: zprava se zezadu přisaje soupeř (`GT-bok` grafit, do 30 % obrazu). **d3 8,4375**: hrdina mu ujede (hrdina +80 px doleva, soupeř zpět ven z obrazu, ease-in-out 0,3 s). **d4 8,906**: kamera **švihne doleva** před vůz (0,15 s, vodorovné rozmazání) a ve švihu zůstane jen černá + linie | bez textu (oko si odpočine na voze) | paralaxa, vodorovné rychlostní čáry, odlesky reflektorů, předjetí, švih | H: kopák, malý buben 7,969 / 8,906 · SFX: průlet sloupu „fup“ vrchol **7,50** a **8,4375** (tiše); bok soupeře, doppler vrchol **8,00**; švih vrchol **8,95** |
| **9,375–11,250** (T6, BUILT · TO · RACE: TIKER) | **d1 9,375**: z pravého okraje proletí modrá stopa vozu a **odkryje první slovo** (linie jako hrana masky, 0,12 s). Každé slovo = **tvrdý střih na dobu** s dorazem kamery 1,08 → 1,00 (0,12 s, ease-out) a radiálním rozmazáním na prvních 2 snímcích (UGC promo: velký text na „push cuts“, tiker 3 slov). **d2 9,844** → TO. **d3 10,3125** → RACE: písmena jsou **okna**, uvnitř běží průjezd z boku (vrstva T5 znovu, rychle), obrys písmen 3 px `--mb-stribro`. **d4 10,781**: kamera **začne letět do vnitřku písmene „A“**: log zoom **×1 → ×24** do 11,25 (ease-in), **střed zoomu přesně v těžišti trojúhelníkového otvoru „A“** (otvor je při 300 px vysoký jen ~50–60 px, proto ×24; těžiště změřit v prohlížeči po načtení fontu, C016); v otvoru se už od 10,78 kreslí pohled shora na vracečku (další scéna). **Posledních 4 snímků (11,183–11,25)** radiální rozmazání 16 px ze středu otvoru (ne filtr: 5 zvětšených kopií canvasu s klesajícím krytím) | **9,375 „BUILT“ → 9,844 „TO“ → 10,3125 „RACE“** (Archivo 900 kurzíva 125 %, 300 px, šířka slova ≤ 1 600 px, střed obrazu; BUILT a TO bílé, RACE okna s obrysem). Výměna ve stejném snímku (staré slovo pryč, nové tam), **nikdy dvě slova naráz**. RACE odchází tím, že jím kamera proletí (pryč do 11,20; v 11,25 nesmí být vidět obrys písmene, jen vracečka) | tiker na doby, radiální rozmazání na dorazu, text jako maska (okna), **zoom skrz písmeno** (Taxtello: písmo jako přechod) | H: kopák, malý buben 9,844 / 10,781 · SFX: suché kovové údery slov vrchol **9,375 / 9,844 / 10,3125**; nasátí do písmene „vššš“ s vrcholem **11,20** |
| **11,250–13,125** (T7, VRACEČKA) | **d1 11,250**: z otvoru „A“ jsme **shora nad vracečkou** (U zatáčka): asfalt grafit s jemným šumem, bílé okraje tratě, obrubník na vrcholu zatáčky (grafit/bílé pruhy). `F1-shora` hrdina 520 px přijíždí shora dolů a **brzdí**: dešťové světlo bliká červeně, kotouče žhnou (malé teplé body, jen v kolech). Kamera se během taktu pootočí s vozem o −30° (jediný pohyb). **d2 11,719 APEX**: podlaha škrtne o obrubník → **sprška jisker** z titanové lyže pod vozem (~40 jisker se seedem, bílé až `--mb-modra-zare`, letí za vozem a dohasínají 0,4 s) + otřes 5 px. **d3 12,1875**: výjezd, plný plyn, vůz se srovná, za ním **modrá linie nakreslí čisté U**, zadní pneu zanechají slabé tmavé stopy. **d4 12,656**: vůz vystřelí dolů z obrazu, U z modré linie zůstane | bez textu | jiskry s příčinou (G6), otřes na apexu, brzdová světla, světelná stopa | H: kopák, malý buben 11,719 / 12,656 · SFX: kvílení brzd vrchol **11,40**; škrtnutí + praskání jisker vrchol **11,72**; zátah motoru vrchol **12,20** (pod hudbou); „vžum“ odjezdu vrchol **12,70** |
| **13,125–15,000** (T8, MAPA OKRUHU → PRSTENEC) | **d1 13,125**: kamera **oddálí** (jeden pohyb přes celý takt, log zoom 1 → 0,12, ease-in-out, nikdy zpět): vracečka se stane jednou zatáčkou celého okruhu, okruh je **grafická mapa** (obrys tratě 6 px `--mb-stribro` na černé, mapa ~1 100 × 700 px, střed (960; 540), bez textu je místo na větší mapu), vůz je teď **jasná modrobílá tečka s ohonem**, která jede kolo stále rychleji a kreslí za sebou modrou linii. **Datový moment bez čísel**: 3 sektorové brány (krátké příčky) se rozsvítí bíle, když jimi tečka projede: **d2 13,594**, **d3 14,0625**, **d4 14,531**. **14,531–15,000 MORF** (vír): tečka dokončí kolo přesně v 15,000 a obrys okruhu se po krocích na údery víru (14,53 / 14,65 / 14,77 / 14,88) **narovná do dokonalého kruhu** Ø 700 px, střed (960; 540) | **bez textu** (oponentura S1: mapa je datový moment, čte se jen tečka, brány a morf; text by mapu zakryl) | log zoom ven, kreslení linie po mapě, sektorové brány, **morf tvaru** (okruh → kruh) | H: kopák, malý buben 13,594 / 14,531, vír 14,53–15,0 · SFX: tiché elektronické „tik“ bran vrchol **13,594 / 14,0625 / 14,531**; uzavření kruhu kovové „ting“ vrchol **15,00** (s činelem H) |
| **15,000–16,875** (T9, **ZLOM: KONTRAST**) | **d1 15,000**: prstenec (Ø 700, linie 8 px stříbrná s modrou září) se uzavře a **po jeho obvodu jednou oběhne světlo** (0,4 s). Pak **klid**: černá, kamera jen dotlačuje 1,00 → 1,03. Za prstencem projíždí **zpomaleně makro boku** hrdinova vozu (jen ostré okrajové světlo na hranách karoserie a modrý proužek), zleva doprava, plynule. **d3 15,9375**: střed boku projede středem obrazu **přesně ve vrcholu dopplera 15,95** a po laku přejede široký **odlesk** (Taxtello: odlesk přes povrch). **d4 16,406**: prstenec se začne **naklánět do 3D** (rotateX 0 → 20°, příprava na T10) | **bez textu** (zlom dýchá: čistý obraz prstence a boku, kontrast před stoupáním) | běh světla po prstenci, zpomalený odlesk, **ticho jako kontrast** (jediný klidný takt, C7) | H: činel 15,0, motor průjezd → vrchol 15,95, bez kopáku · SFX: jen tichý vzduch zpomaleného průjezdu, vrchol **15,95**; nic dalšího (kontrast) |
| **16,875–18,750** (T10, STOUPÁNÍ: 2D → 3D) | **16,875–17,344 PRŮLET DO ROVINY PRSTENCE** (jeden pohyb, ease-in): kamera **klesne do roviny prstence** (náklon 20° → 78°) a zároveň se k němu přiblíží, takže prstenec **přeroste přes okraje obrazu**; jeho levý a pravý okraj se stanou **levou a pravou hranou klopené tratě**, která ubíhá do úběžníku (960; 470) (2D → 3D moment šablony showreel, žádný skok v měřítku: prvek, který byl v obraze, se stane prostorem). Z úběžníku se **vynoří `F1-záď`** hrdina (kamera ho dohání) a dorovná na šířku **900 px** (47 %), střed (960; 700) přesně v **17,344**; honička po klopené trati, po stranách tratě ubíhají k divákovi **modré světelné pásy**, rychlostní čáry se sbíhají do úběžníku (960; 470). Na **každý kopák** (16,875 / 17,344 / 17,8125 / 18,281) kamera cukne vpřed (2 %) a pásy pulzují. **17,475 ŘAZENÍ 1**: **glitch akcent** (3 vodorovné řezy posunuté ±24 px, 2 snímky) + chromatický posun 6 px + bliknutí dešťového světla. **18,125 ŘAZENÍ 2**: silnější (5 řezů ±40 px, 3 snímky), hustota čar ×2. Vír zrychluje: čáry se prodlužují, zorný úhel se rozšiřuje (jedním směrem). **18,40–18,75 NÁDECH**: obraz potemní na 50 % kromě dešťového světla, vůz ujede do úběžníku a zmenší se na **jediný svítící bod**; kamera se týmž pohybem zvedne do osy, takže bod je v 18,72 přesně ve středu (960; 540) | bez textu | **2D → 3D (průlet do roviny prstence)**, sbíhavé rychlostní čáry, **glitch akcent na řazení** (řezy = posunuté výřezy canvasu, žádný filtr), chromatický posun jen na světelných vrstvách, potemnění (nádech) | H: kopák, motor rev → 18,75, řazení 17,475 / 18,125, vír zrychluje, obrácený činel 17,81 → 18,75 · SFX: kovové cvaknutí řazení + krátký digitální „zap“ vrchol **17,475** a **18,125**; nasátí vzduchu do **18,74**; **ztlumení hudby −10 dB 18,40–18,75** |
| **18,750–20,625** (T11, **DROP 2: HVĚZDA ZE SVĚTLA**, nejsilnější moment) | **18,750**: svítící bod ve středu se **rozštěpí na tři vozy** (světelné `F1-shora` ~90 px), které vyjedou od středu po třech osách hvězdy (−90°, 30°, 150°). **Každý vůz za sebou odkrývá maskou přesný polygon svého ramene** z `hvezda_generator.py` (trojúhelník široký u středu, ostrý na špičce, vůz jede na čele odkrytí), **18,750–18,910 (0,16 s, ease-out)**, aby bylo odkrývání vidět. Ramena drží **světlou a tmavou fazetu** jako `mercedes-hvezda-fazety.svg` (světlá = bílé jádro, tmavá = `--mb-modra-zare` 55 %, záře jako předem rozmazaný sprite) → na 480 px je to **hvězda Mercedes, ne písmeno Y ani znak míru**, a zacvaknutí v 26,25 je bez skoku. Zároveň dopadne **prstenec** (ten z okruhu a zlomu): měřítko 1,6 → 1,0 za 0,12 s, ease-out. Hvězda ze světla **Ø 880 px** (81 % výšky, A8), střed (960; 540). **Bílý záblesk** ze středu (70 % → 0, 3 snímky), **otřes 16 px** (doznívá 0,6 s), radiální rychlostní čáry ze středu, chromatický posun 6 px jen na čarách a hvězdě. V 18,91 vozy na špičkách zhasnou do tří svítících bodů. **18,750–19,219 PLAKÁT (celá doba)**: hvězda stojí čistá a celá, doznívá jen otřes a letí radiální čáry. **Stab 18,984**: jeden **běh světla** ze středu po všech třech ramenech ke špičkám a dál jednou po prstenci dokola (0,23 s, ease-in-out). **19,219–19,453 ZAPLAVENÍ**: ze středu se rozlije **modrá `--mb-modra`** (kruh, ease-out) a do 19,40 přesáhne všechny 4 rohy; ramena svítí bíle skrz (Food craving). **Stab 19,453 ODKRYTÍ VÝSEČÍ**: modrá se za 0,10 s **stáhne do ramen**, ramena se protáhnou k okrajům obrazu (polygony se září) a odkryjí **3 výseče = tři kamery na jeden okamžik**: hrdinův vůz projíždí zatáčkou synchronně ze 3 úhlů: **vlevo nahoře zepředu** nízko od obrubníku (`F1-předek`), **vpravo nahoře shora** (`F1-shora`), **dole zezadu** (`F1-záď`); každý vůz zabírá **≥ 60 % šířky své výseče**. 19,453 nájezd a brzdění (dešťové světlo, žhnoucí kotouče ve všech 3 pohledech zároveň). **Stab 19,922 APEX**: kolo na obrubníku ve všech pohledech v tomtéž snímku, všechny tři výseče **cuk** 1,00 → 1,06 (kriticky tlumeně 0,15 s) a hrana levé horní výseče blikne bíle. **Stab 20,391 VÝJEZD**: plný plyn, modrá stopa za vozem ve všech pohledech, cuk + blik hrany pravé horní. Na kopák mikro otřes 3 px | bez textu (obraz je pointa) | **zrod hvězdy ze stop (odkrývání polygonů)**, záblesk, největší otřes, radiální čáry, chromatický posun, běh světla, **zaplavení barvou**, rozdělení obrazu hvězdou, synchronní více kamer | H: **úder + činel 18,75**, kopák, stab 18,984 … · SFX: **„světelný úder“ (elektrický třesk + hluboký dopad), vrchol 18,750, 0 až −2 LU**; tři průlety od středu ven vrchol **18,83**; běh světla jasné „šššink“ vrchol **18,99**; vlna zaplavení „vuff“ vrchol **19,30**; odkrytí výsečí kovový „klap“ vrchol **19,453**; škrtnutí na apexu vrchol **19,922** (tiše) |
| **20,625–22,500** (T12, REVOLVER) | **d1 20,625 ŠVIH**: celý rám hvězdy se **otočí o +120°** za 0,22 s (ease-in-out, rotační rozmazání, `--sub 8`) a výseče se točí jako buben revolveru; **každá kamera jede se svou výsečí** (zepředu: vlevo nahoře → vpravo nahoře, shora: vpravo nahoře → dole, zezadu: dole → vlevo nahoře). Obsah se točí s bubnem jen do vrcholu rozmazání **20,736**, v tom snímku se vymění na **okamžik B** a dobíhá už vzpřímeně (střih schovaný ve švihu). **Okamžik B = JISKRY NA APEXU ze 3 úhlů** (rým se 11,719): vlevo nahoře zezadu, vpravo nahoře zepředu, dole shora; vozy ≥ 60 % šířky výseče. **Stab 20,859**: podlaha škrtne o obrubník → **sprška jisker synchronně ve všech třech pohledech** (zezadu letí do kamery, zepředu pod nosem dozadu, shora vějíř za vozem; ~40 jisker na pohled ze sdíleného seedu = tytéž jiskry) + cuk všech výsečí. **Stab 21,328**: druhá, menší sprška + cuk. **d3 21,5625**: **glitch akcent přes celý obraz** (řezy posunuté ve směru ramen, 2 snímky, výřezy canvasu). **Stab 21,797**: výjezd, cuk, hrana výseče blikne. **Stab 22,266**: ve všech třech pohledech zároveň přijedou vedle hrdiny **dva soupeři** (grafit) zleva a zprava = **formace tří vozů**; dole shora: hrdina stříbrný uprostřed, nosem dolů, za každým modrá stopa (připravuje T13). Kopák = mikro otřes 3 px | bez textu | **švih rotací (buben)**, střih ve švihu, jiskry ze 3 úhlů na staby, cuky výsečí, glitch akcent | H: kopák, malý buben, staby · SFX: švih „vuš“ rotace vrchol **20,70**; škrtnutí + praskání jisker vrchol **20,86** a **21,33** (druhé tišší); glitch „zap“ vrchol **21,5625** (tiše); příjezd soupeřů (dvojitý doppler) vrchol **22,27** |
| **22,500–24,375** (T13, TŘI STOPY) | **d1 22,500 MORF**: dolní ramena se **vyklopí nahoru** (levé −120°, pravé +120°, ease-in-out 0,3 s) a posunou na x 600 a 1 320, horní rameno stojí v x 960: z hvězdy jsou **tři rovnoběžné svislé stopy**, dolní výseč (formace shora) se roztáhne na celý obraz a stopy jsou **stopy tří vozů** (kamera shora jede s nimi, trať ubíhá nahoru, vozy 460 px, nosem dolů, spodní třetina obrazu). **Stab 22,734 / 23,203 / 23,672 / 24,141**: na každý stab si dva vozy **vymění pruh** (boční přesun 360 px, ease-in-out 0,2 s), stopy se **splétají jako cop** (hrdina skončí uprostřed). **d3 23,4375**: pod formací přeletí **příčný světelný portál** (bílá příčka přes celou šířku) + cuk kamery 3 % | bez textu | splétání světelných stop, výměny pruhů na staby, průlet portálem | H: kopák, malý buben, staby · SFX: krátké svištění pneu při výměnách vrchol **22,734 / 23,203 / 23,672 / 24,141** (tiše, střídavě L/P); průlet portálem „fump“ vrchol **23,44** |
| **24,375–26,250** (T14, SBĚH DO HVĚZDY: nejsilnější celý takt) | **d1 24,375**: tři stopy se **sklopí zpět do úhlů hvězdy** (obrácený morf z 22,5), vozy jedou od středu ven po ramenech. Za hvězdou se rozběhne **rotující pole radiálních rychlostních čar** (canvas, ~90 čar, bílé a `--mb-modra-zare`, otáčení +15°/s, celý takt). **Stab 24,609 / 25,078 / 25,547**: vozy jeden po druhém **vyletí z obrazu** na konci svého ramene (horní, pravý, levý); každé vyletění = **bílý záblesk na špičce ramene** (sprite Ø ~220 px, 2 snímky), **otřes 4 px** a rameno se **rozjasní na 120 %** (doznívá 0,3 s); za každým vozem zůstane plné rameno. **24,84–25,31**: po obvodu se znovu nakreslí **prstenec** (světlo oběhne kruh) → hvězda ze světla je zase celá (Ø 880). **d3 25,3125**: celá hvězda pulzne 1,00 → 1,03 (kriticky tlumeně), čáry za ní zhoustnou. **25,78–26,25 VÍR / SMRŠTĚNÍ** (0,47 s, jen během víru): hvězda se smrští Ø 880 → 340 px a posune do polohy loga (960; 380), jedno natočení +120° (ease-in, „natažení pružiny“); rychlostní čáry se zrychlí a stáhnou dovnitř, ramena tenčí, záře houstne; ve **26,016** (poslední stab) vše kromě hvězdy potemní na černou | bez textu | rotující pole rychlostních čar, vyletění vozů se záblesky na špičkách a otřesy na staby, kreslení prstence světlem, pulz, smrštění ve víru (napětí) | H: kopák, staby, obrácený činel → 26,25, vír 25,78–26,25 · SFX: tři průlety ven „vžum“ s krátkým třeskem na špičce vrchol **24,61 / 25,08 / 25,55** (P, L, střed); smrštění „sání“ **25,78 → 26,24** |
| **26,250–28,125** (T15, **END CARD**: ZACVAKNUTÍ) | **26,250**: hvězda ze světla se **zacvakne do loga**: na jejím místě je `mercedes-hvezda-fazety.svg` (kov, **Ø 340 px**, střed (960; 380), natočení 0°, jen jednotné měřítko), světlo stéká do fazet (záře 100 → 15 % za 0,4 s, ease-out; fazety světla a loga jsou tytéž polygony, porovnat 26,23 a 26,27 po pixelech), tenký bílý kruh od okraje loga ven (0,1 s), **otřes 6 px** krátce. **26,25–26,72 POSLEDNÍ JÍZDA**: pod logem zleva doprava projede světlo vozu a **nakreslí modrou linii** y 735, délka 0 → 1 100 px, střed x 960 (ease-out); **26,6** (řazení) linie jednou blikne. Kamera **dotlačuje 1,00 → 1,04** až do 30,0 (ease-in-out, nikdy zamrzlý obraz). Kolem loga volno ≥ 85 px (25 % průměru) | **26,719 CTA „mercedes-benz.cz“** (Archivo 600, 100 %, 60 px, prostrkání 0,04 em, malými písmeny jako webová adresa; „mercedes-benz“ bílá, „.cz“ `--mb-seda`, účaří y 690, vystředěné) se rozevře **maskou od osy loga ke krajům** (0,35 s, ease-out; Food craving „wordmark wipes out from behind the mark“). **Ne** „Mercedes-Benz“ (napodobený lockup slovní značky). **27,1875 „FOLLOW THE STAR“** (Archivo 900 kurzíva 112 %, 88 px, „STAR“ `--mb-modra`, účaří y 840) vyroste **z modré linie** maskou (0,3 s, ease-out). **27,656 disclaimer** „Concept ad · not affiliated with Mercedes-Benz“ (Inter Tight 500, 26 px, `--mb-seda`, účaří y 920) najede krytím + 6 px nahoru (0,3 s). Každý vstup skončí dřív, než začne další | přerod světla v kov, kreslení linie, maskované vstupy textu | H: **úder + činel 26,25**, motor odjezd, řazení 26,6, basa A1, dozvuk · SFX: **měkký kovový dopad loga + „cink“, vrchol 26,250, 0 až −3 LU**; průjezd pod logem (odjezd, doppler) vrchol **26,45** |
| **28,125–30,000** (T16, END CARD: DRŽENÍ) | **d1 28,125**: po kovové hvězdě přejede **odlesk** (stejný jako na snímku 0, 0,6 s, ease-in-out) = rým se začátkem. **d2 28,594**: po modré linii proběhne slabý světelný impuls zleva doprava (0,5 s). **d3 29,0625**: za logem v hloubce projede **rozostřené světlo vozu** zleva doprava (bokeh `--mb-modra-zare`, Ø ~160 px, krytí 35 %, 0,6 s, ease-in-out, do 29,66) a odrazí se ve fazetách hvězdy jako slabý odlesk 15 %. Pak už nic, jen dotlačování kamery do 30,0 (žádný zamrzlý snímek, poslední snímek čistý, bez rozmazání a bez bokehu) | vše drží: logo + mercedes-benz.cz + FOLLOW THE STAR + disclaimer | odlesk na logu, impuls po linii, průjezd bokehu za logem, dotlačení | H: dozvuk do 30,0 · SFX: jemné „ting“ odlesku vrchol **28,20** (tiše); vzdálený průjezd (měkký doppler, hodně tiše) vrchol **29,36** |

**Kde jsou 4 zvolené motiony** (kritik je má umět pojmenovat s časy, kritérium 9):
| motion | co z něj bereme (podle skutečného textu promptu) | kde ve videu |
|---|---|---|
| **Šablona showreel** | kostra na doby, „something happens on every beat“, **jedna technika na takt** a každá vzniká z předchozí, rozsah: kinetická typografie, morf tvaru, **2D → 3D moment**, datový moment, end title; poslední celý takt před end card nejsilnější; kontrola snímku na každou dobu | celá osa (T3 zoom, T4 typografie, T5 paralaxa, T6 tiker, T7 jiskry, T8 **data + morf** 13,1–15,0, T10 **2D → 3D** 16,9–18,75, T11 plakát hvězdy + 3 kamery, T14 **nejsilnější celý takt** se záblesky na špičkách a rotujícím polem čar), end title 26,25–30 |
| **Taxtello app film** (`daniel-haida-8691d4`) | odlesk, který odhalí značku („a tiny glint“, „machined precision“), přechody z objektu („of course the next scene came from that“), **písmo jako přechod** (kamera skrz písmeno), odlesk přejíždějící po povrchu, klidnější scéna před pointou, oblouk CHAOS → CONTROL → CLARITY → ZNAČKA, prémiový snímek 0 | odlesk 0,0–0,9 a 28,125 (rým), zoom skrz „A“ 10,78–11,25, zpomalený odlesk boku 15,95, zlom 15,0–16,875, nájezd do hvězdy 2,81–4,2 |
| **UGC ad generator promo** (`twoclipping-6dd14e`) | na dropu **kruh, který se otevře z prvku do tmavé scény**, maskované odhalení textu, velký text na **„push cuts“** a **tiker 3 slov**, švih s rozmazáním na hrdinu, mřížka dob **zkalibrovaná na skutečné kopáky**, SFX podle změřeného vrcholu, past `preserve-3d` + opacity | průlet prstencem hvězdy 4,05–4,22, BUILT · TO · RACE 9,375–10,31, švihy 5,625 / 8,906 / 20,625, masky CHASE THE LINE / mercedes-benz.cz / FOLLOW THE STAR, odkrytí výsečí 19,453 |
| **Food craving launch film** (`ultimaxbt-2ddf1e`) | **jeden souvislý záběr bez střihů a prolínaček**, každá scéna roste z předchozí, **barva se rozlije z objektu a stáhne do jiného**, jeden plynulý pohyb kamery na scénu, nikdy zoom tam a zpět, bod/značka se promění v logo a wordmark se rozevře | modré zaplavení z hvězdy 19,219–19,55 (stáhne se do ramen), linie → účaří → okraj tratě → mapa → prstenec → klopená trať, svítící bod 18,72 → hvězda, end card 26,25–27,1 (CTA se rozevře od osy loga) |
Vědomé odchylky od promptů (kvůli vkusu uživatele, G6, V001): šablona showreel, Taxtello i UGC promo **zakazují** třes kamery, glitch a záři.
My je používáme **jen na hudební údery a s příčinou v ději** (start, apex, řazení, drop 2, logo), ne plošně. Smyčka (poslední snímek = první) se nedělá,
end card je jen rýmovaný odleskem z 0,0 (D4 tu ustupuje end card podle zadání).

**Seznam efektů synchronních s hudbou** (≥ 6 různých, kritérium 3):
1. **Rychlostní čáry**: radiální 3,75–4,2 a 18,75–19,22; vodorovná paralaxa 7,5–9,3; sbíhavé do úběžníku 16,875–18,75; rotující pole za hvězdou 24,375–26,25 (ve víru se stáhne dovnitř).
2. **Světelné stopy**: modrá linie 4,22–15,0 (S, účaří, okraj tratě, U, kolo okruhu), tři stopy / ramena 18,75–26,25, podtržení 26,25–26,72.
3. **Záblesk + otřes kamery na úderu**: 3,75 (12 px), 11,719 (5 px, bez záblesku), 18,75 (16 px, nejsilnější), záblesky na špičkách ramen 24,609 / 25,078 / 25,547 (2 snímky, otřes 4 px), 26,25 (6 px); mikro otřes 3 px na kopáky T11–T12.
4. **Švih s rozmazáním**: rotace −90° 5,625; vodorovný 8,906; rotace revolveru +120° 20,625.
5. **Zoom skrz objekt**: prstenec hvězdy 4,05–4,22; otvor písmene „A“ 10,78–11,25.
6. **Zaplavení barvou**: modrá z hvězdy 19,219–19,453, stažení do ramen 19,453–19,55.
7. **Glitch akcent**: řazení 17,475 a 18,125, staby 21,5625.
8. **Chromatický posun** (jen na švihu a dropech, **jen na světelných vrstvách**: rychlostní čáry, stopy, hvězda ze světla): 3,75, 5,625, 17,475, 18,125, 18,75.
9. **Jiskry z dopadu** (s příčinou): apex 11,719; tytéž jiskry ze 3 kamer 20,859 a 21,328.
10. **Cuky / push cuts na doby**: lampy 0,469–2,344, tiker 9,375–10,3125, výseče na staby 19,922–22,27.
11. **Odlesky a běhy světla**: glint přes hvězdu na nose 0,0–0,94 (střed v 0,469), běh světla po rameni a prstenci 18,984, reflektory na laku T5 (na každou dobu), zpomalený odlesk 15,95, glint 28,125, bokeh za logem 29,06.
12. **Morf tvaru**: okruh → kruh 14,53–15,0, prstenec → klopená trať 16,875, hvězda → 3 rovnoběžné stopy 22,5 a zpět 24,375, světlo → kov 26,25.
13. **Roztažení / maska písma**: CHASE THE LINE 5,625, písmena RACE jako okna 10,31, průlet otvorem „A“ ×24 10,78–11,25.
14. **Odkrývání maskou za vozem**: tři vozy odkryjí polygony ramen 18,75–18,91.

**Kontrolní snímky a kritéria odmítnutí** (každý snímek posoudit i na zmenšenině **480 px šířky**; 16:9 se na telefonu dívá na šířku i v okně feedu):
| čas | co musí být vidět | odmítnout, když |
|---|---|---|
| **0,000** | hotový plakát: tmavý portál s pouzdry lamp → (prázdné místo) → formule zepředu s helmou v halo, hvězda Ø 110 na nose, odlesk na levé třetině | je to tma / zatmívačka; vůz na 480 px nejde poznat jako formule (hračka, obecné auto, „AI render“) → varianta B; hvězda na nose na 480 px nečitelná; portál splývá s vozem |
| 0,469 / 0,55 | odlesk přesně přes hvězdu na nose (hvězda blýskne), „LIGHTS“ ostré, červená záře lampy 1, 1. tečka v hledí | odlesk mine hvězdu o > 3 snímky; text se dotýká portálu nebo vozu (< 40 px); červená jinde než v záři lamp a jejích odrazech (lak, asfalt, hledí) |
| 2,40 | 5 lamp, 5 teček v hledí, napětí | obraz se nehýbe (chvění a nájezd musí být znát v sousedních snímcích); tečky v hledí na 1 080 px nejsou vidět |
| 3,70 | nádech: stojí, svítí jen červená záře | cokoli se hýbe rychle; lampy už zhasly |
| **3,767** | LIGHTS OUT celé, lampy i hledí zhasnuté, záblesk doznívá, start | dva řádky textu; záblesk > 3 snímky nebo přes 70 %; „OUT“ nemá stejnou velikost a účaří jako „LIGHTS“; v hledí ještě svítí tečky |
| 3,90 / 4,05 | LIGHTS OUT stojí celé; odznak se blíží ke středu (960; 540), vůz roste | odznak odjíždí dolů z obrazu; text odjel dřív než 4,05; dva pohyby kamery místo jednoho |
| 4,12 / 4,17 / 4,22 | text odjíždí nahoru, hvězda zakrývá vůz; text pryč; kruh se otvírá do pohledu shora | text je ještě vidět po 4,15; hvězda zdeformovaná (nejednotné měřítko); v průletu „prázdná“ černá > 2 snímky |
| 5,00 | shora: hrdina 620 px, modrá linie, soupeři za ním | linie je přerušená nebo „skáče“; vůz nečitelný jako formule shora |
| 5,72 / 6,20 | švih končí, CHASE THE LINE stojí na linii, „LINE“ modře srůstá s linií | text pod linií, nad ní s mezerou nebo mimo 96–1 824 px; písmena animovaná po jednom místo jako blok při příchodu |
| 7,10 | GT prosviští, text se trhá | text ještě celý stojí, když vůz projíždí (nemá příčinu odchodu) |
| 8,00 | bok GT 1 400 px, paralaxa | GT nečitelné jako závodní kupé (chybí křídlo / difuzor), detaily panelů (klipart), statické pozadí |
| 9,40 / 9,87 / 10,34 | BUILT / TO / RACE, vždy jen jedno slovo | ve snímku dvě slova; RACE bez obsahu v oknech |
| 11,00 / 11,20 / 11,25 | let do „A“ se středem v těžišti otvoru, v otvoru vracečka; poslední snímky s radiálním rozmazáním; v 11,25 jen vracečka | otvor prázdný nebo ujíždí ze středu; skok místo plynulého zoomu; v 11,25 je vidět obrys písmene |
| 11,75 | apex, jiskry od vozu | jiskry odjinud než zpod vozu, „ohňostroj“ bez směru |
| 13,60 / 14,40 | mapa okruhu, brána svítí, žádný text | mapa jako generická „HUD“ grafika s čísly / popisky v rozích; jakýkoli text |
| **15,00** | dokonalý kruh, světlo na obvodu | kruh není kruh (zbytky zatáček); obraz je černý bez prvku |
| 15,95 | prstenec, bok s odleskem, žádný text | zlom není klidnější než okolí; text v obraze |
| 17,10 / 17,34 | kamera v rovině prstence, okraje prstence jsou hrany tratě, vůz roste z úběžníku; v 17,344 záď 900 px | skok v měřítku (prstenec zmizí a trať se objeví); vůz se objeví odjinud než z úběžníku |
| 17,49 / 18,14 | glitch na řazení, 3D honička | glitch déle než 3 snímky nebo mimo řazení; pohled nepůsobí 3D (plochý ovál) |
| 18,72 | jen svítící bod ve středu (960; 540), potemnělý obraz | nádech není poznat (obraz stejně jasný jako 18,0); bod mimo střed |
| **18,767 / 18,83 / 18,90** | odkrývání ramen za vozy (polygony široké u středu, ostré na špičce, světlá a tmavá fazeta), prstenec, záblesk, otřes | **na 480 px to v 18,90 není hvězda Mercedes ještě před čtením čehokoli jiného** (písmeno Y, znak míru, tři stejné čáry); ramena nejsou trojúhelníky z `hvezda_generator.py`; slabší dojem než 3,767 |
| **19,00 / 19,10** | čistá hvězda jako plakát, běh světla po ramenech a prstenci | do hvězdy už zasahuje modrá nebo výseče; hvězda se hýbe víc než doznívajícím otřesem |
| 19,30 / 19,50 | zaplavení přes všechny 4 rohy; pak 3 výseče, v nich **týž vůz ze 3 kamer** | zaplavení nepřesáhne rohy (vypadá jako záblesk); ve výsečích tři různé scény; vůz < 60 % šířky výseče; na 480 px „šum malých autíček“ |
| 19,92 | apex ve všech třech pohledech v tomtéž snímku, cuk | pohledy nejsou synchronní (kolo na obrubníku jen v jednom) |
| 20,70 / 20,74 / 21,00 | revolver ve švihu, výměna obsahu ve vrcholu rozmazání, okamžik B (jiskry ze 3 úhlů) | obsahy se vyměnily bez rotace nebo mimo vrchol rozmazání (viditelný skok); obsah po švihu vzhůru nohama |
| 22,40 | formace tří vozů ve všech výsečích | soupeři přijeli jen v jedné výseči |
| 22,65 / 23,30 | tři rovnoběžné stopy, splétání | morf skočil; vozy se překrývají |
| 24,62 / 25,20 / 25,60 | záblesk na špičce ramene, rameno 120 %, rotující pole čar; celá hvězda | záblesk > 2 snímky nebo přes celý obraz; pole čar stojí; hvězda se deformuje |
| 25,90 / 26,10 | smršťování ve víru k poloze loga | smršťování začalo před 25,78; logo bliká |
| **26,30 / 27,80 / 29,30 / 29,98** | kovové logo Ø 340, linie, **mercedes-benz.cz**, FOLLOW THE STAR, disclaimer; v 29,30 bokeh za logem | logo zdeformované / nedostatek volna (< 85 px); pod logem „Mercedes-Benz“ (falešný lockup); dva texty v pohybu naráz; zamrzlý obraz (29,98 = 29,0 pixel po pixelu); bokeh nebo rozmazání v posledním snímku; disclaimer pod y 940 |
Plus `--nahled doby --bpm 128` (64 snímků) a pásy sousedních snímků (`--sub 8`) u 3,75 / 4,15 / 5,625 / 10,78–11,25 / 16,875–17,34 / 17,475 / 18,75–18,91 / 19,22–19,55 / 20,625 / 24,61 / 26,25.

**Pasti stavby**:
- **Vozy jsou riziko č. 1.** Kreslit je jako prémiovou siluetu z okrajového světla (rim light) a několika ploch laku, ne jako detailní ilustraci. Každou kresbu
  ověřit samostatně na 480 px dřív, než jde do scény. Formule = halo, široké odhalené pneu, přední a zadní křídlo. GT = dlouhá kapota, zadní křídlo na stojkách, difuzor.
  Žádná čísla, jména, loga sponzorů, ani tyrkysová (C8). **Varianty A / B** (viz Knihovna vozů): nejtěžší kresby jsou `F1-předek` na 1 400 px (snímek 0)
  a `GT-bok` na 1 400 px (T5); GT obrys jen z ostrého okrajového světla a 2–3 ploch laku, žádné spáry panelů, kliky, nápisy. Helma: jednoduchý tvar + hledí, bez barev.
- **Hvězda**: ramena, prstenec i výseče počítat z `hvezda_generator.py` (střed 0,0, R 283; ramena −90°, 30°, 150°). Hvězda ze světla smí mít záři, ale obrys
  ramen musí sedět na logo, aby zacvaknutí v 26,25 bylo bez skoku (porovnat 26,23 a 26,27 po pixelech). Logo jen jednotné měřítko + otočení.
  **Ramena jsou polygony, ne čáry**: každé rameno = 2 trojúhelníky (světlá a tmavá fazeta, body jako `fac` v generátoru: střed, údolí, hrana, špička);
  vůz je na čele masky, která polygon odkrývá podél osy ramene (maska = obdélník kolmý na osu, posun 0 → R_END·měřítko). Ve výsečích protažení k okrajům
  obrazu = tentýž polygon s prodlouženou špičkou (hrany ve stejném úhlu), ne nová čára.
  **Těžiště otvoru „A“** (zoom ×24 v 10,78): změřit v prohlížeči po načtení fontu (vykreslit „A“ do canvasu, najít největší uzavřenou oblast uvnitř, spočítat těžiště), ne odhadem.
- **Text**: nikdy dvě vrstvy textu v jednom snímku (V001). Tiker = výměna v jednom snímku. Odchod vždy skončí dřív, než začne příchod.
  Fonty změřit až po načtení (C016), šířky změřit v prohlížeči (CHASE THE LINE, BUILT, RACE ≤ 1 600 px, jinak zmenšit blok celý).
  Jen 4 hesla + CTA + disclaimer, **žádný text v T5, T7, T8, T9 a T10–T14** (texty nesmí ležet přes prstenec ani vozy).
- **Záblesky**: max. 3 snímky, max. 70 % krytí, nikdy víc než 3 záblesky za sekundu (fotosenzitivita). Staby = blik jen hrany výseče, ne celé plochy.
- **Otřes kamery**: šum se seedem (`nahoda(seed)`), doznívá exponenciálně, jen na uvedených časech; během čtení textu ≤ 3 px.
- **Červená** (`--mb-brzdove-svetlo`) jen v lampách, jejich odrazech, dešťovém světle a brzdách. Nikdy text, nikdy plocha.
- **Výkon (4 CPU, bez GPU)**: záře a rychlostní čáry kreslit do canvasu, záře jako předem rozmazaný sprite (ne CSS `filter: blur` na velké vrstvy v každém podsnímku).
  **Na celý obraz nikdy SVG ani CSS filtr** (v softwarovém renderu s `--sub 8` by to trvalo minuty na snímek). **Chromatický posun** jen na světelných vrstvách
  (rychlostní čáry, stopy, hvězda ze světla): každou nakreslit 3× v canvasu s R / G / B nádechem a posunem, režim `lighter`. **Glitch** = posunuté výřezy
  canvasu (`drawImage` pruhů). **Radiální rozmazání** (11,18–11,25) = 4–6 zvětšených kopií canvasu s klesajícím krytím.
  Výseče = 3 výřezy (canvas clip) jednoho canvasu se sdílenou knihovnou vozů (týž vůz, 3 transformace kamery), ne 3 kopie celé scény. Rozmazání pohybem v kódu podle rychlosti + `--sub 4`, rychlé úseky `--sub 8`.
- **3D**: nikdy `opacity` / `filter` na prvku s `preserve-3d` (UGC promo); prolínat obal. `will-change` ne na prvky, které kamera škáluje.
- **Kamera**: jeden pohyb na scénu, žádný zoom tam a zpět (F7); otřes je přičtený zvlášť a nepočítá se jako pohyb kamery.
- **Zaplavení** musí přesáhnout všechny 4 rohy a trvat ~0,3 s, jinak vypadá jako záblesk.
- **Deterministika**: vše z `seek(t)`, jiskry, bokeh, šum asfaltu a glitch řezy se seedem; časy událostí z `hudba.json`, ne ručně.

**Pořadí stavby** (fáze 2):
1. **Knihovna vozů + hvězda**: 4 kresby vozů **ve variantách A a B**, helma s hledím, odznak Ø 110 a hvězda ze světla (polygony s fazetami, i rozpracovaná v 18,83 a 18,90)
   na jednom testovacím listu 1920×1080 → zmenšenina 480 px → schválí kreativní ředitel (vybere A nebo B u každého vozu). Bez schválení nic dál.
2. **Klíčové snímky jako statické obrazy**: **18,90 (drop 2: hvězda z polygonů)**, **19,10 (plakát)** a **3,767 (drop 1: LIGHTS OUT + start)**, pak 0,000 (náhled),
   19,50 (3 kamery na jeden okamžik) a 27,80 (end card s mercedes-benz.cz). Schválit.
3. **Pohyb dropů**: 3,28–4,60 a 17,80–19,95 včetně pásů snímků `--sub 8`.
4. Zbytek po blocích: T1–T2, T3–T5, T6–T8, T9–T10, T11–T14, end card. Po každém bloku snímky na doby.
5. `--nahled doby --bpm 128` celého videa, oprava, pak plný render 60 fps.

**Změny po oponentuře** (S1 → S2, kreativní ředitel 2026-10-31; oponent: energie 8/10, celkem 7,6/10; pevné časy hudby beze změny):
1. **Drop 2 jako plakát**: hvězda stojí čistá celou dobu 18,75–19,219; na stab 18,984 jeden běh světla po ramenech a prstenci; zaplavení 19,219–19,453;
   výseče se odkryjí až na stab 19,453 (modrá se stáhne do ramen); cuky výsečí 19,922 / 20,391.
2. **Ramena = polygony loga** z `hvezda_generator.py` se světlou a tmavou fazetou, vůz je odkrývá maskou na čele (0,16 s místo 0,10 s); kontrolní snímek 18,90 na 480 px.
3. **Výseče = tři kamery na jeden okamžik**: týž vůz synchronně zepředu / shora / zezadu (≥ 60 % šířky výseče); revolver nese kamery s výsečemi a přepne
   ve vrcholu rozmazání na okamžik B (jiskry na apexu ze 3 úhlů); na 22,266 soupeři přijedou ve všech pohledech = formace pro T13.
   Odchylka od oponenta: místo „z boku“ je „zepředu“, protože knihovna nemá formuli z boku (`GT-bok` je jiný vůz); nová kresba by stála čas a riziko klipartu.
4. **Jen 4 hesla**: LIGHTS OUT → CHASE THE LINE (přesunuto do T4 na modrou linii, „LINE“ modře) → BUILT TO RACE → FOLLOW THE STAR. Vyřazeno FULL THROTTLE,
   FASTER BY DESIGN, EVERY CORNER COUNTS. T8 a T9 bez textu.
5. **End card**: místo „Mercedes-Benz“ (falešný lockup) **CTA „mercedes-benz.cz“** (Archivo 600, 60 px, prostrkání 0,04 em, „.cz“ šedě), rozevření od osy loga 26,719.
6. **Snímek 0 a duše**: odznak na nose Ø 110 px; odlesk 0–0,9375 přejede hvězdu přesně v 0,469 (hvězda blýskne s první lampou); helma v halo a v hledí se po jedné
   zrcadlí červené lampy, ve 3,75 zhasnou; portál je tmavá silueta v popředí u horního okraje, lampy vidět jen jako rozptýlené červené světlo a odrazy.
7. **T14 nejsilnější takt**: záblesk na špičce ramene (2 snímky) + otřes 4 px + rameno 120 % na každé vyletění; rotující pole radiálních čar (+15°/s);
   smrštění jen ve víru 25,78–26,25.
8. **Zoom skrz „A“** ×1 → ×24 se středem v těžišti otvoru (změřit v prohlížeči), poslední 4 snímky radiální rozmazání 16 px.
9. **Přechod T9 → T10**: kamera klesne do roviny prstence, okraje prstence se stanou hranami klopené tratě, záď vozu se vynoří z úběžníku a dorovná na 900 px v 17,344;
   v nádechu se kamera zvedne, aby svítící bod byl v 18,72 přesně ve středu.
10. **Drop 1**: měřítko se středem v odznaku a jedním pohybem do středu obrazu; LIGHTS OUT stojí celé 3,75–4,05, odjede 4,05–4,15.
11. **Konec bez mrtvé pasáže**: 29,0625 (d3 T16; oponent psal d4, ale 29,0625 je d3) bokeh vozu za logem 0,6 s s odleskem 15 % ve fazetách; poslední snímek čistý.
12. **Výkon**: chromatický posun jen na světelných vrstvách (3× kresba R/G/B, `lighter`), žádný filtr na celý obraz, glitch a radiální rozmazání z výřezů a kopií canvasu.
13. **Vozy A / B**: na zkušebním listu varianta A (podle storyboardu) a B (silueta z okrajového světla); rozhoduje 480 px.
Nové a posunuté SFX pro zvukaře: ting hvězdy 0,469; průlety ramen 18,83 (dřív 18,80); běh světla 18,99; vuff zaplavení 19,30 (dřív 18,95); klap výsečí 19,453;
škrtnutí 19,922; jiskry 20,86 / 21,33; příjezd soupeřů 22,27; sání 25,78 → 26,24; vzdálený průjezd 29,36. Automatika hudby beze změny.
Beze změny (podle oponentury): spojovací prvek a koncept, LIGHTS OUT na 3,75 s nádechem, nádech před drop 2, revolver +120°, tiker BUILT · TO · RACE,
vracečka s jiskrami, mapa se sektorovými branami a morfem do kruhu, klidný zlom s odleskem 15,95, rým odlesku, zacvaknutí 26,25, glitch jen na řazení, pravidla značky, pořadí stavby.

**Zvuk v1 (zvukař, 2026-10-31)**: 61 SFX podle S2 ze `projekty/002-mercedes-racing/sfx_udalosti.json` (zdroj, v gitu) → `media/…/zvuk/sfx.wav|json`, `zvuk_v1.wav`, `zvuk_bez_hudby_v1.wav`.
Příkaz: `python3 -I nastroje/sfx.py --udalosti projekty/002-mercedes-racing/sfx_udalosti.json --delka 30 --out media/projekty/002-mercedes-racing/zvuk/sfx.wav --hudba media/projekty/002-mercedes-racing/hudba.wav --mix …/zvuk_v1.wav --bez-hudby …/zvuk_bez_hudby_v1.wav --automatika 3.52-3.72:-9:150:30 --automatika 18.40-18.72:-10:150:30 --ticho 16.70-17.35 --limiter -1.5`.
Rozhodnutí zvukaře: (1) automatika končí návratem **v 3,75 / 18,75** (plné ztlumení 3,52–3,72 a 18,40–18,72, doběh 30 ms), aby náběh úderu dropu nebyl ztlumený;
(2) T14 panorama podle obrazu (24,61 střed = horní rameno, 25,08 vpravo, 25,55 vlevo), ne „P, L, střed“ ze sloupce SFX; (3) startovní lampy panorama zleva doprava podle pozice pouzder;
(4) mix přes sběrnicový limiter −1,5 dBFS (hudba má rezervu jen 12,5 dB, efekty na úderech by jinak vynutily lineární −2 dB a master by skončil −14,7 LUFS / −1,0 dBTP).

**Zvuk v2 (zvukař, kolo 1, 2026-10-31)**: nález kritika „stoupání slabší než jízda, drop 2 nejtišší ze tří úderů“. `hudba.wav` ani časování beze změny,
jen obálka zisku hudby v mixu (nové volby `sfx.py --zisk-hudby` a `--saturace`). Výstupy `media/…/zvuk/zvuk_v2.wav`, `zvuk_bez_hudby_v2.wav`, `sfx_v2.wav|json`,
`sfx_v2_log.txt`, `zvuk_v2_master.m4a`, `zvuk_v2_spektrogram.png` (v1 soubory ponechány). Příkaz jako v1, navíc / jinak:
`--automatika 18.40-18.72:-13:150:30 --zisk-hudby "3.55:0,3.70:-1,14.97:-1,15.0:0,16.875:0,17.5:1,18.0:2.5,18.40:4,18.45:3,18.70:3,19.10:3,19.6:0"
--zisk-hudby "16.875:0,17.5:0.5,18.0:1.5,18.40:2,18.45:0@150" --saturace 18.72-19.35:6`, výstupy `sfx_v2.wav`, `zvuk_v2.wav`, `zvuk_bez_hudby_v2.wav`.
Rozhodnutí: (1) T3–T8 −1 dB (rampa schovaná v nádechu 3,55–3,70, návrat 14,97–15,0 před činelem zlomu); (2) stoupání 16,875–18,40 roste celé 0 → +4 dB
a pásmo nad 150 Hz (vír, riser, rev motoru, obrácený činel) dalších 0 → +2 dB, kopák a sub tedy jen +4 (pásma beze změny); (3) nádech ztlumení −13 dB proti
obálce +3 dB = −10 dB proti původní hudbě jako dřív; (4) drop 2 +3 dB 18,70–19,10, návrat do 19,6; SFX úrovně `lu` jdou s hudbou, takže i světelný úder
je o +3 dB silnější (+2 dB by nestačilo); (5) úder by limiter mačkal 445 ms o > 1 dB a zbylo by jen +1 dB → místo toho měkké nasycení špiček mixu
18,72–19,35 (4× převzorkování, koleno 6 dB pod stropem, zkreslení −24 dB = drsnost úderu), limiter pak > 1 dB jen 62 ms.
Mimo upravené úseky je mix v2 s v1 shodný bit po bitu (0–3,5 / 20–26 / 26,5–30 s).

## Průběh výroby
| kolo | kdo | co se dělalo | verdikt kritika | hlavní nálezy |
|---|---|---|---|---|
| příprava | analytik ∥ zvukař → kreativní ředitel → oponent → revize | logo, předběžná paleta, nálada `sportovni`, koncept FOLLOW THE STAR, storyboard S1 → S2 | oponent: energie 8, celkem 7,6 → revize 13 oprav (odhad autora ~9) | drop 2 musí stát jako plakát, ramena = polygony loga, výseče = 3 kamery, T14 nejsilnější, CTA mercedes-benz.cz |
| výroba | zvukař ∥ animátor (vozy, klíčové snímky → schválení 7/10, energie 6,5 → 12 oprav → pohyb A, B, C → render) | SFX 61 událostí, render v1 (24 min, 2× kvůli zesílení dropu 1), střih v1 | – | renderer zrychlen 5× (C027) |
| 1 | technika · wow · zadání | kontrola V002_v1 | technika SCHVÁLENO, zadání SCHVÁLENO (všech 6 pravidel uživatele splněno), **wow 7,8 / energie 7,5 → OPRAVIT** | mrtvých 0,4 s před BUILT, statický úvod 0–2,8 (push-cuts do hledí), stoupání a drop 2 hlasitěji, splétání stop jako srážky, hrana masky GT 7,3; drobné: barvy loga a zaplavení, tyrkysový přepal, glitch 17,475, RACE okna bez vozu |
| 2 | technika · wow · zadání | kontrola V002_v2 (opravy obrazu: push-cuts do hledí, drop 1 natvrdo, cop stop, sloup u GT; zvuk v2: stoupání a drop 2) | **wow 8,4 / energie 7,5**, technika OPRAVIT (GT couvá 7,13–7,5, LIGHTS přes helmu), zadání viz níže → 3. kolo | statická místa: CHASE THE LINE, tiker, stoupání T10, jiskry, T14; háček zvukově slabý |

## Chyby během výroby
- C024: první spuštění přípravy zamítnuto (pokyn obejít 403 na webu značky) → pokyn odstraněn, logo z Commons, paleta předběžně.
- C025: `alimiter` bez `latency=1` posunul hudbu o 5 ms → opraveno v `hudba.py` (zvukař) i `master_zvuk.sh` (režisér).
- C026: dynamický loudnorm zploštil kontrast dropů → `sportovni` lineární zisk, ostatní nálady jako dluh.
- Zvukař: první mix měl 91 % energie v kopáku a base (varování I7) → přemixováno (středy 45 %, sub 11 %).

## Spotřeba tokenů
| agent / úkol | tokeny | akce nástrojů | čas |
|---|---|---|---|
| workflow příprava (5 agentů: analytik, zvukař, kreativní ředitel koncept, oponent, revize) | 500 581 | 121 | 35,7 min |

## Verze
| verze | datum | soubor / kam doručeno | změny |
|---|---|---|---|

## Zpětná vazba (doslova)

## Poučení
