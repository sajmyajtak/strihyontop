# V004: BMW řady 7: realistická reklama s jízdou (sport luxus, SaaS motion graphics)

| | |
|---|---|
| Datum zadání | 2026-11-01 |
| Platforma / formát | **16:9, 1920×1080, 60 fps** |
| Délka | **30,0 s** |
| Stav | výroba (koncept po oponentuře schválen režisérem) |

## Zadání (doslova od uživatele)
> není to ono ja jsem chtěl asi vybereš realistické auto jak vypada že animuješ aby to vypadalo realstické při ukázce auta i rychlosti výkonu a ty obrazky byly jen dopnění materialu. Udělej to na bmw : https://www.bmw.cz/cs/index.html (+ parametry kampaně)
>
> udělej to na tenhle vůz poslal jsem ti odkaz:
> https://configure.bmw.cz/cs_CZ/configure/G70/81HY/FVCSW,P0300,S01FE,S0230,S0248,S02PA,S02VB,S02VD,S02VH,S02Z4,S0302,S0319,S03CK,S03DM,S03DN,S03M3,S03MF,S0416,S0420,S0428,S043B,S0465,S04A2,S04FL,S04FM,S04HA,S04HC,S04T2,S04U6,S04U9,S04V1,S0548,S05AT,S05AV,S05DN,S0617,S061B,S0654,S06AE,S06AF,S06D5,S06NY,S06WF,S0710,S0760,S0775,S07M9,S0851,S0879,S08R3,S08R9,S08TF,S09QX,S09T1,S09T2,S09TB/SE000001
>
> a chci aby si z toho webu vybral fotky auta a máš tam i přístup 360 kameře kterou můžeš použit. Udělej fakt realistickou reklamu kde auto se bude pohybovat a ejt rychle i ukazka nového modelu a jeho salonu. 30s video dlouhé, hudba sport luxus, 16:9, bez voice over,dynamické, k tomu realistické záběry a saas motion graphics zaběry:
> https://prompt-motion.com/motiondsgnr-9dcfa6
> https://prompt-motion.com/lukasersil-0ed38e
> https://prompt-motion.com/souravbhar871-61f424
> https://prompt-motion.com/adamdesgns-478d6d

Upřesnění (2026-11-01, doslova):
> barvy použij jaký mají na stránkách a auto co jsem ti poslal.

Dotaz a rozhodnutí (2026-11-01): uživatel se zeptal, proč nemůžu generovat AI video. Vysvětleno: Higgsfield je v prostředí (umí video i z obrázku),
ale uživatel ho 2026-10-30 zakázal; jiný generátor není. Nabídnuto povolení pro V004 (cena předem). Odpověď uživatele (doslova):
> tak zkus sám a potom uvidíme

→ **V004 bez Higgsfieldu**, jen skutečný materiál BMW + vlastní animace. Po zpětné vazbě případně zvážit AI záběry.

## Pravidla pro toto video (od uživatele, mají přednost před vším ostatním)
1. **Vůz z odkazu uživatele** (konfigurace G70 / 81HY, přesně tato výbava a barva). **Barvy grafiky z webu bmw.cz.**
2. **Realistická reklama, kde vůz jede a jede rychle** (pohyb, rychlost, výkon). Fotky a rendry jsou **jen doplněk** materiálu.
3. Ukázka **nového modelu** a jeho **salonu** (interiér).
4. Fotky auta vybrat z webu BMW, smí se použít **360° kamera** konfigurátoru.
5. **30 s**, **16:9**, hudba **sport luxus**, **bez voiceoveru**, **dynamické**.
6. Kombinace **realistických záběrů** a **SaaS motion graphics záběrů** podle 4 předloh z prompt-motion (výše).
7. Dál platí: anglicky, energie (V001), nic kresleného na voze (V002), vůz musí jet (V003).

## Rozhodnutí režiséra
- **Generovat video AI nemůžeme** (Higgsfield zakázaný uživatelem, jiný generátor nemáme) a 3D model vozu od BMW stáhnout nejde.
  Realistickou jízdu proto stavíme ze **skutečného materiálu BMW**, který web načítá běžně (videa a fotky na bmw.cz a v konfigurátoru, případně
  tiskové materiály BMW Group, pokud jsou volně přístupné), a z **2,5D animace rendrů konfigurátoru** (vůz v uživatelově konfiguraci).
  Načítat jen normálně, nic neobcházet (C024). Videa chráněná DRM nestahovat.
- **Klíčová otázka pro přípravu**: existují záběry jízdy **v barvě a provedení vozu z odkazu**? Když ne, režisér rozhodne mezi:
  (a) jízdní záběry BMW v jiné barvě + konfigurace uživatele v rendrech (riziko: nesoulad s pravidlem 1), (b) „jízda“ z rendrů konfigurace
  (2,5D sledovací záběr: vyříznutý vůz, rotace kol, rozmazané pozadí, otřes), (c) dotaz na uživatele. Rozhodnutí zapsat sem.
- **Spec reklama do portfolia**: disclaimer „Concept ad · not affiliated with BMW“, materiály © BMW AG, jen portfolio (upozornit uživatele).
- **Hudba** (pevná struktura): nálada `luxsport` (V003), **120 BPM**, takt 2,0 s, **15 taktů = 30,0 s**: úvod / odhalení 0–4, **drop 1 = 4,0**
  (jízda), jízda a nový model 4–12, **zlom 12,0** (salon, klidnější), stoupání 16,0–18,0, **drop 2 = 18,0** (rychlost, výkon, nejsilnější),
  rychlost 18–26, **end card 26,0–30,0** (logo na finální úder 26,0).
- **Fakta** (výkon, zrychlení, max. rychlost, dojezd…) jen doslova z bmw.cz / konfigurátoru pro tuto konfiguraci.

- **Odpovědi režiséra analytikovi** (2026-11-01): tiskové materiály z newsroom.bmwgroup.com **smí** zůstat: stránky i soubory jsou veřejné a určené
  ke stažení, běžný curl s výchozí hlavičkou dostal 200 bez jakéhokoli obcházení (bez změny User-Agenta, bez stealth, bez captchy); 503 pro headless
  prohlížeč jsme neobcházeli jiným prohlížečem ani maskováním. Kdyby kterýkoli zdroj blokoval i běžný požadavek, končíme (C024).
  Podmínky: vše © BMW AG, jen nekomerční portfolio s disclaimerem, uživatel bude upozorněn. Vůz: **i7 M70 xDrive, Alpine White**, kola 21" 909 M.
  Fakta (doslova z konfigurátoru): 500 kW (680 k), 0–100 km/h 3,8 s, 250 km/h, dojezd 686 km (WLTP).
  **Rozpor**: žádný záběr jízdy v Alpine White / M70 neexistuje → otázka na uživatele (jízda stříbrné i7 z tiskového filmu vs. jen vůz uživatele
  v rendrech), odpověď sem.

- **ROZHODNUTÍ UŽIVATELE (2026-11-01, odpověď „1“ na varianty 1/2/3)**: **varianta 1**: jízdu a rychlost nesou **skutečné záběry stříbrné i7 60**
  z tiskového filmu press_PF0010152 (high-key grade, 1,2× se zdvojením snímků na 60 fps, převážně shora / zezadu / bokem v rozmazání / dron / u kola,
  **bez čelních pohledů s chromovými ledvinkami**). **Vůz uživatele (Alpine White i7 M70)** v rendrech konfigurátoru: odhalení, rozsvícení světel
  (pár vyp / zap), detail kola 909 M, předek s černou M maskou, salon (kostka 2000×2000, g12–g14, tmavá videa z kokpitu bmw.cz). 2,5D jízda z rendru
  jen jako střih do 1 s nebo vůbec. SaaS motion graphics přes jízdu (test C) podle 4 předloh, barvy bmw.cz. Fakta: 500 kW (680 k) → anglicky
  „680 hp“ ne (převod k → hp), použít **500 kW**, **0–100 km/h in 3.8 s**, **250 km/h**, **686 km range (WLTP)**.

- **Odpovědi režiséra ke konceptu „Bod, který nepustí vůz“** (2026-11-01): disclaimer **„Concept ad · not affiliated with BMW · Footage and renders © BMW AG ·
  Driving scenes: BMW i7 60 xDrive“** ano (poctivé, jízda je jiná verze) · povinný údaj o spotřebě **ano**, malým písmem na end card doslova z konfigurátoru
  („Energy consumption combined 18.6 kWh/100 km · CO₂ 0 g/km“) · páčka BOOST z M760e **ne** (funkce u této konfigurace neověřená), použít zálohu
  (ruce na M volantu) · pilulky v salonu nikdy přes detail, který ukazujeme, ano · názvy výbavy **jen vlastní jména BMW** (BMW Iconic Glow,
  BMW Panoramic Vision, CraftedClarity), popisné překlady z češtiny nepoužívat.

- **Odpovědi režiséra k oponentuře** (2026-11-01): doplněk W (web i7 driving_dynamics 8,40–10,80, 720p) na 8,25–10,0 **smí**, rozhodne klíčový snímek 9,5
  (žádné čelní chromové ledvinky, nesmí působit jako CGI; jinak záložní plán z pasti 14) · karty výkonu: **první úkol animátora v bloku 2** je změřit
  polohu vozu po 0,25 s v G 40,90–42,05, C 22,32–23,52 a D 29,20–30,40 a po snímcích ověřit, že karta nikdy nevjede na vůz · záblesky jízdy na 3,5 a 3,75
  jako předzvěst **ano**.

- **Odpovědi režiséra ke střihači** (2026-11-01, závazné pro animátora): slot 22,0–23,0 = **D_3008 + W_900** (X_0448 zůstává pro 25,0–25,75) ·
  slot 6,0–8,0: **J_5232 jen snímky 0–34** (do 53,72, kdy jsou ledvinky ještě nečitelné), **bez punch-inu**, zbytek do 8,0 doplnit čistým záběrem
  zezadu nebo shora (G_4088 / H_4508, bez čelního pohledu) · volant: dlaždice 4 začne v 14,77 · SPZ v tiskové stopáži nerozmazávat (skutečný materiál).

- **Zvuk v1b (režisér, 2026-11-01)**: na nález zvukaře (motiv motoru v hudbě měl barvu V8, i7 je elektromobil) přidána do `hudba.py` volba
  `--motor elektricky` (tón střídače, bez sudých harmonických a zapalování; výchozí chování všech nálad bit po bitu beze změny, ověřeno).
  `hudba.wav` přegenerována s `--motor elektricky`, časování i `udalosti_nastroju` shodné. `zvuk_v1.wav` a `zvuk_bez_hudby_v1.wav` přegenerovány
  stejným příkazem SFX (101 událostí, odchylka 0 ms), master −13,8 LUFS / −1,5 dBTP. Staré soubory ve `zvuk/zastarale_v8/` (C039).
  Odpovědi zvukaři: tikání číslic a dosednutí podle návrhu, po renderu je režisér případně posune na skutečné časy · logo −3,7 LU nechat (C032).

- **Odpovědi režiséra ke klíčovým snímkům** (2026-11-01, závazné pro bloky): začátek kostky 12,0 pohledem nahoru s −3 EV ano · slot 7,0–8,0: **ne X_0448**
  (opakoval by se v 25,0), použít **G_4088 nebo H_4508** (záď / shora, bez čelního pohledu) podle odpovědi režiséra střihači · slot 22,0–23,0 D_3008 + W_900 ano ·
  podržený poslední snímek volantu pod vinětací ano · karta 21″ / 909 M nad kapotou s linkou vedle přídě, vůz 77 % šířky ano · karty na stopáži
  bez stínu ano (G8 stín platí pro UI na neutrálním pozadí, ne přes video).

- **Odpovědi režiséra k bloku 1** (2026-11-01): dlaždice 2 mřížky = B_1100 ano · drop 2 = F s expozicí po snímcích (jas 80–133) ano, varianta (c) ne ·
  ochlazení studia i na tváři M70 ano (jedno studio) · bod u karty 686 km dát **před vůz do bezpečné zóny** (UI nikdy u okraje x > 1824) ·
  **stejný úsek záběru se ve videu nesmí opakovat** (X_0448 je buď v 7,0–8,0, nebo v 25,0–25,75, ne v obou; blok 2 to ověří a případně použije jiný čistý záběr).

- **ROZHODNUTÍ REŽISÉRA k rozporu kritiků (kolo 1, závazné)**: rolující čísla smí cestou ukázat jen hodnoty **horší** než fakt, nikdy lepší:
  rychlost a výkon rostou zdola (0 → 250 km/h, 0 → 500 kW), **zrychlení klesá shora** (9.9 → 3.8 s), dojezd roste zdola (0 → 686 km). Konečná hodnota přesně.
  Kritik to nehlásí jako chybu. Dál platí: **stejný úsek záběru se nesmí opakovat** (X_0448 jen jednou, v kole 1 porušeno), bod nikdy na karoserii
  a vždy v bezpečné zóně, číslice bez schodovitých ozvěn (C040: rozmazání v kódu, ne kopiemi).

## Akceptační kritéria pro kritika
1. 1920×1080, 60 fps, 30,0 s ± 0,1 s, H.264 + AAC, BT.709; −14 LUFS ±1, true peak ≤ −1 dBTP (po AAC)
2. **Vůz jede**: aspoň 40 % délky videa je vůz v pohybu (jízda, průjezd, rychlost) a divák to na první pohled pozná. Rychlost je cítit.
3. **Realismus**: žádný kreslený vůz, žádná koláž (lem masky, plovoucí vůz bez stínu, nesedící světlo nebo perspektiva). Divák nepozná AI.
4. **Vůz = konfigurace uživatele** (barva, kola, provedení) všude, kde je ve videu „náš“ vůz; výjimky jen podle rozhodnutí režiséra výše.
5. Nový model + **salon** (interiér) jsou poznat. Na konci výkon / rychlost (fakta jen z bmw.cz).
6. **SaaS motion graphics** záběry podle 4 předloh (kritik / kreativní ředitel je pojmenuje s časy), barvy z bmw.cz
7. Energie: dynamické, událost na každou dobu, drop 1 a drop 2 nejsilnější, žádná mrtvá pasáž > ~1 s
8. Logo BMW nedeformované, end card + disclaimer, texty anglicky bez překlepů, v bezpečné zóně (A5)

## Materiály
| soubor | kde je | použití |
|---|---|---|
| katalog všech materiálů V004 (konfigurace doslova, technické údaje, tabulky videí a fotek, shoda barvy, podmínky) | `media/projekty/004-bmw-jizda/materialy/katalog.md` | číst před storyboardem |
| galerie konfigurátoru, 14 pohledů (Alpine White, i7 M70, 909 M, Merino Black), 2560×1646 / 2560×1536 | `media/projekty/004-bmw-jizda/materialy/konfigurator/galerie/` | „náš“ vůz: hrdinské záběry, den → noc, detail kola, salon |
| otočka 360°, 36 × 10°, světla zap / vyp (pixelově zarovnané páry), 2560×1440 | `…/konfigurator/360_svetla_zap/`, `…/360_svetla_vyp/` | turntable, rozsvícení, 2,5D „jízda“ (varianta b) |
| interiér 360°: 6 stěn kostky 2000×2000 + náhled panoramatu | `…/konfigurator/interier_kostka/` | salon: panorama / paralaxa |
| snímky konfigurátoru a technických údajů, výpis výbavy | `…/konfigurator/_snimek_*.png`, `_souhrn_vybava.txt` | zdroj faktů (ne do videa) |
| 4 tisková videa BMW Group 1920×1080 25 fps (i7 60 stříbrná jízda, M760e modrá jízda, 740 dvoubarevná jízda, Individual výroba) | `media/projekty/004-bmw-jizda/materialy/videa/press_PF00101{51..54}_*.mp4` | **skutečná jízda** (jiná barva); oříznout titulní kartu 0–4,3 s |
| 39 videí z bmw.cz (i7, M modely, řada 7), 1646×720 a menší, 25 fps | `…/materialy/videa/i7web_*`, `m7web_*`, `7web_*` | salon (displeje, volant, ovladače), záběry jízdy v jiné barvě |
| náhledové archy všech videí (snímek po 2 s) | `…/materialy/videa/_archy/` | výběr záběrů |
| 10 tiskových fotek LCI 8K (stříbrná i7 60, jízda s rozmazaným pozadím) + 10 fotek z bmw.cz (2560 px) | `media/projekty/004-bmw-jizda/materialy/fotky/` | doplněk; jiná barva (kromě černého interiéru) |

## Materiál jízdy (analytik, 2026-11-01)
- **Vůz z odkazu**: BMW i7 M70 xDrive Sedan (81HY, M modely), **Nemetalický lak Alpine White** (P0300), 21" M aerodynamická kola 909 M Multicolour,
  BMW Individual kůže Merino Black (FVCSW), obložení M Carbon Fibre. **Fakta (konfigurátor, doslova)**: 500 kW (680 k), 1015 Nm, 0–100 km/h 3,8 s,
  max. rychlost 250 km/h, dojezd (WLTP) 686 km, baterie 112,4 kWh, DC 250 kW (10–80 % za 0:28 h). Podrobně v katalogu.
- **Co máme**: (1) přesný vůz jen jako **rendry konfigurátoru** (galerie, otočka 360° se světly zap/vyp, interiér 360°), kvalita výborná, ale vůz stojí ve studiu;
  (2) **skutečnou jízdu** v rozlišení 1080p z tiskové zprávy BMW Group „The new BMW 7 Series.“ (22. 4. 2026): i7 60 **stříbrná**, M760e **tmavě modrá**,
  740 **dvoubarevná**; (3) jízdu z bmw.cz jen 720p (stříbrná i7, modrá M760e, dvoubarevná 740, zčásti CGI); (4) salon: tmavá videa displejů a ovládání
  (Panoramic Vision, volant, skleněné ovladače), čalounění v nich skoro není vidět → použitelné pro náš černý interiér; videa zadních sedadel jsou koňaková / bílá.
- **Barva**: **žádný dostupný záběr jízdy není v Alpine White ani v provedení M70.** Nejblíž je **stříbrná i7 60** (`press_PF0010152`, 55,9 s, 1080p, dron,
  sledovací auto, nízké průjezdy, motion blur), světlá barva, stejná karoserie po faceliftu; liší se ledvinky (chromová mřížka vs. M černá), kola a M prvky.
- **Kvalita**: tisková videa 1920×1080, 25 fps (pro 60 fps výstup převzorkovat: zdvojení snímků nebo interpolace, rychlé pohyby raději s motion blur);
  web 1646×720 → na 16:9 zvětšení 1,5× (měkké). Fotky z tiskové zprávy 8K.
- **Podmínky**: bmw.cz: „Obsah těchto webových stránek nesmí být pro komerční účely kopírován, rozšiřován, pozměňován nebo zpřístupňován třetím osobám.“
  Newsroom bez výslovné licence, určeno médiím. → jen nekomerční portfolio s disclaimerem, © BMW AG.
- **Doporučení analytika** (rozhoduje režisér): kombinace (a)+(b). Rychlost a jízdu nést **skutečnými záběry stříbrné i7 60** tam, kde vůz není poznat
  zepředu (zadní a boční průjezdy, dron z dálky, nízko u kola, rozmazání, světla v noci), protože tam rozdíl barvy (stříbrná vs. bílá) i M prvků splývá;
  „náš“ vůz zepředu a v detailu ukazovat **jen rendry konfigurátoru** (2,5D sledovací záběr z otočky 360°, rozsvícení světel, salon z kostky).
  Žádné přebarvování cizí jízdy na bílou (riziko nerealistického vzhledu a nesouladu ledvinek M70). Tmavě modrou M760e a dvoubarevnou 740 nepoužívat
  (na první pohled jiný vůz). Pokud musí být všude přesně Alpine White, je to otázka na uživatele.

## Test realistické jízdy (animátor, 2026-11-01)
Výřezy 1920×1080, 60 fps, BT.709 v `media/projekty/004-bmw-jizda/test/` (+ pásy snímků `*_pas.jpg`), skripty a scény tamtéž (`skripty/`, `t_b_jizda.html`, `t_c_saas.html`).

| varianta | soubor | délka | výpočet | verdikt |
|---|---|---|---|---|
| A. skutečné záběry BMW (stříbrná i7 60, `press_PF0010152`) | `t_a_jizda.mp4` | 4,0 s, 7 střihů na doby | **21 s** (ffmpeg, `skripty/test_a.sh`) | **nejrealističtější, jasná rychlost**; jiná barva a maska ledvinek |
| B. 2,5D sledovací záběr z rendru `uhel_090` (Alpine White M70) | `t_b_jizda.mp4` | 4,0 s | maska BiRefNet 67 s + podklady 5 s + render **107 s** (`--sub 4`, ≈ 27 s na 1 s) | pohyb čte jako jízda, ale **je to poznat jako koláž**; jen krátce |
| C. SaaS karta přes jízdu (dron 31,0–34,6 s) | `t_c_saas.mp4` | 3,0 s | snímky 3 s + render **46 s** (≈ 15 s na 1 s) | **funguje**, čitelné, nic přes vůz |

**A. Skutečné záběry** (detail: `t_a_jizda_pas.jpg`, `t_a_interpolace_srovnani.jpg`, `t_a_grade_varianty.jpg`, `t_a_grade_srovnani.jpg`)
- Zdroj: tiskové video 1920×1080, 25 fps, H.264 ~2,6 Mb/s, bez textu po 4,48 s (první střih po titulní kartě), bez vodoznaku → ořez do 16:9 není potřeba.
  Komprese je vidět jen v tmavých plochách (stín pod vozem), na 1080p přijatelné. Web bmw.cz má jen 720p (zvětšení 1,5×) → tisková videa mají přednost.
- **Převod na 60 fps**: zrychlení **1,2×** (25 × 1,2 = 30 fps) + zdvojení snímků = **přesná kadence 2:2** (změřeno: každý zdrojový snímek přesně 2×).
  Při 1,0× vychází nepravidelná kadence 2/3 (trhání při panorámování). Interpolace `minterpolate` (4 min výpočtu na 4 s) **trhá předek vozu na bloky**,
  prolínání (`framerate`) dělá **dvojitá kola** → obojí nepoužívat. Zrychlení 1,2× je v rychlých záběrech nepoznatelné a rychlost přidá; čistá kadence vychází
  jen při 1,2× (2:2) a 2,4× (1:1, 60 fps); 1,5× = 37,5 fps → opět nepravidelná (vizuálně netestováno). Pro zpomalení nic: 25 fps materiál zpomalit nejde bez interpolace.
- **Nejlepší jízdní záběry** (zdroj s → výřez, kde není vidět čelní maska): 7,30 nízko u předního kola (bok, nejsilnější rychlost) · 22,25 střecha nad
  silnicí · 40,30–41,5 záď zezadu shora (sledovací) · 23,75 nakloněný průjezd bokem · 44,95 průjezd střechou · 50,45–51,1 průjezd bokem s rozmazáním ·
  31,0–34,6 dron nad vozem (vůz se vzdaluje do horské silnice, levá třetina volná pro UI). Střihy 0,5 / 1,0 s na doby 120 BPM drží energii (C7).
- **Barevné sjednocení**: grade „high-key“ (`eq=saturation=0.7`, teplé výšky, křivka zvedající světla) posune stříbrnou **shora a zezadu skoro k Alpine White**,
  sjednotí s teplými světlými rendry. Bokem a zepředu zůstane stříbrná metalíza + chromový rámeček ledvinek (náš M70 má černou M mřížku) → tyto úhly
  krátce nebo vůbec. Černá skleněná střecha i7 60 sedí s konfigurací. Přebarvování v masce jsem netestoval (riziko nerealistického vzhledu, analytik nedoporučil).
- Skripty: `skripty/test_a.sh VYSTUP RYCHLOST GRADE dup|mint|blend` (seznam záběrů `SHOTS`).

**B. 2,5D sledovací záběr z rendru** (`t_b_jizda_pas.jpg`, podklady `podklady/`, skripty `skripty/masky.py`, `skripty/podklady_b2.py`)
- Postup: `uhel_090` (svítí světla) vyříznutý BiRefNet (složení vs. originál 0,16/255), kola jako otáčivě rozmazané sprity (střed a poloměr změřeny
  fitováním leštěného ráfku: přední 576/993, zadní 1873/995, pneu r≈146 px; spodek pneumatiky doplněn zrcadlem, jinak se zářez masky točí s kolem),
  pozadí ze 3 vrstev tiskové fotky P90636154 (město = téměř stojí, zeleň + svodidlo 0,36×, silnice 1,05× rychlosti vozu), valení kol přesně podle dráhy,
  nástup výkonu na dobu 2,0 (+30 % rychlosti, záď dosedne, otřes), pérování a otřes ze seedovaného šumu, odlesky ubíhající po laku jen v masce,
  světlo prostředí (obloha shora, silnice zdola) násobením v masce, kontaktní stín ze studia + měkká elipsa, vinětace a zrno.
- **Poctivě: působí to jako koláž**, i když pohyb sám o sobě jízdu čte. Prozrazuje to: (1) vůz má rovnoměrné studiové světlo, pozadí ostré slunce
  (bez směru světla a tvrdého stínu na voze); (2) dokonale ostrý bok v ortografickém pohledu bez perspektivy sledovací kamery; (3) silnice je beztvará
  šmouha (zrcadlená šikmá čára dělala „stříšky“, musela pryč), skyline jako kulisa; (4) kola jsou uvěřitelná, ale rozmazaný ráfek je tmavší než ve skutečných záběrech.
  Kritik by B jako hlavní jízdu neschválil (kritérium 3 „žádná koláž“). Použitelné **jen na ≤ 1 s** jako rychlý střih mezi skutečnými záběry
  (např. „náš“ vůz bokem na úderu), nebo s tmavým / nočním pozadím, kde se rozdíl světla schová.
- Výkon: 27 s výpočtu na 1 s videa (`--sub 4`), canvas bez `filter: blur`, šmouhy předem v podkladech.

**C. SaaS motion přes jízdu** (`t_c_saas_pas.jpg`)
- Bílý bod s modrým středem vedle levé hrany vozu (sleduje vůz podle klíčových snímků změřených po 0,25 s, leží ve stínu, **nikdy na karoserii**) →
  linka 1 px → karta (rádius 24, okraj 1 px `#E6E6E6`, dvouvrstvý stín) roste z konce linky pružinou 3 %, rolující číslice **0–100 km/h 3.8 s**
  s modrou lištou (akcent `#1c69d4` jen na akci), kroužek na dokončení (1,5), na dobu 2,0 morf štítku maskou na **Top speed 250 km/h**, odchod
  do linky a bodu (ease-in). Fakta doslova z konfigurátoru. Karta stojí (neplave s vozem), pohyb vozu nese linka.
- Čitelnost: bílá karta na hnědém terénu výborná, text Manrope 300 / 500 v bezpečné zóně. Rolující číslice při rychlém přetočení na pár snímků
  rozmazané (odpovídá odometru, po dosednutí ostré). Pozadí: snímky 30 fps s hranicí posunutou o 1/120 s, aby podsnímky závěrky nemíchaly dva snímky zdroje.

**Doporučení (nejrealističtější jízda s vozem uživatele)**
1. **Jízdu a rychlost nést skutečnými záběry stříbrné i7 60** (A) v úhlech, kde barva a maska splývají: shora / dron, zezadu, bokem v rozmazání,
   detail kola, střecha. Vždy 1,2× + zdvojení snímků, grade „high-key“, střihy na doby 0,5–1,0 s. Čelní pohledy (chrom ledvinek) vynechat.
2. **Vůz uživatele (Alpine White M70) ukazovat jen v rendrech konfigurátoru** tam, kde má stát nebo se představit (odhalení, rozsvícení světel,
   detail kola 909 M, salon), ne jako jedoucí. 2,5D jízdu z rendru (B) nanejvýš jako ≤ 1s střih na úder.
3. **SaaS vrstvy (C) přes skutečné jízdní záběry s volnou třetinou obrazu** (dron 31,0–34,6, záď 40,3, průjezd 44,95): bod + linka + karta, čísla
   z konfigurátoru (3.8 s, 250 km/h, 680 hp / 500 kW, 686 km). Karta přes střih může zůstat jako spojka záběrů.
4. Kombinace pro 30 s: skutečná jízda ≥ 40 % délky (kritérium 2) + rendry pro odhalení a salon + SaaS karty přes jízdu. Rozpor „jiná barva při jízdě“
   je otázka na uživatele (viz Rozhodnutí režiséra).

## Předlohy od uživatele (kreativní ředitel, 2026-11-01)
Ukázková videa stažena do `media/prompt-motion/videa_v004/` (+ `arch_*.jpg` po 0,5 s), klíčové přechody prohlédnuté po 0,1 s. Všechny 4 jsou
showreely 1920×1080 / 60 fps (10–15 s), ne produktová videa: bereme z nich **techniky pohybu**, ne vzhled (barvy zůstávají bmw.cz, produkt skutečný).

| předloha | co dělá wow | co převezmeme | kde ve V004 |
|---|---|---|---|
| **motiondsgnr-9dcfa6** „Bold typographic motion showreel“ (15 s) | (1) **bod → linka → zaplavení**: tečka na 0,0 se na 0,3 s natáhne do vodorovné linky přes celý obraz a ta na 0,6 s otevře obraz do plné barvy; (2) písmena padají po jednom s rozmazáním a dosednou do slova; (3) tři **datové karty v řadě** („NUMBERS THAT MOVE“: sloupce, easing křivka, prstenec 57→60); (4) **mozaika všech předchozích scén** (12,3 s „ALL OF IT.“): dlaždice naskakují po dobách a kamera se pak vrhne do jedné z nich | bod jako spojovací prvek, bod → linka → karta; řada dlaždic se záběry a štítky; **mřížka 3×3 živých záběrů ve stoupání a skok kamery do dlaždice** | 0,0–1,0 bod; 12,0–16,0 salon jako deska s dlaždicemi; **16,0–17,5 mřížka „všechno najednou“** → skok do dlaždice |
| **lukasersil-0ed38e** „Motion techniques showreel“ (15 s) | (1) **bod světla → linka → svazek světelných stop** (0,0–1,4 s), čistá fyzika světla; (2) písmo **rozřezané na vodorovné pásy**, které se posouvají proti sobě (LINE, 2,0–3,0 s) = rychlost v typografii; (3) **clona: bílý kruh vyroste z bodu přes celý obraz**, uvnitř závěrečný nápis (13,0 s); (4) každý záběr vzniká z předchozího | bod, který se na dropu 2 **rozprskne do vodorovných světelných stop** (bílá + `#1c69d4`); název modelu **rozřezaný do pásů s jízdou uvnitř písmen** (maska); **bod → bílá clona → logo** | 17,75–18,25 nádech do bodu a výbuch stop; 24,0–25,0 „i7 M70“ s jízdou v písmenech; 25,75–26,0 clona do loga |
| **souravbhar871-61f424** „Kinetic type self-portrait“ (10 s) | kinetická typografie s charakterem: slovo **mění řez a tvar** (z neklidných písmen do rovného „straight“, z Light do Black), podtržení se dotáhne pružinou; **žádné texty a rámy v rozích** (jeho prompt: „avoid the frames and texts on the corners“) | nadpis jako jeden objekt, který **mění řez Light 300 → ExtraBold 800** a srovná prostrkání (ne slovo po slově); text pilulky se mění uvnitř jednoho tvaru; **nikde text v rozích ani HUD** | 0,0–1,5 „THE NEW i7 M70“ (řez naskočí s rozsvícením světel); štítky salonu 12,5–15,5 |
| **adamdesgns-478d6d** „Fitters Bible app promo“ (15 s) | (1) **linka se zářícím hrotem** se kreslí po trase (0,5–2,0 s); (2) **rolující číslice jako automat** (4,219 → 5,820, každá číslice ve vlastním sloupci s rozmazáním); (3) **jedna informace na každou dobu** (SEARCH / OFFSETS / DRAWING PDFS / NIGHT MODE, 10,5–12,0 s); (4) **logo se poskládá z prstence** s radiálními čarami (13,0 s) | rolující číslice faktů (686 / 500 / 3.8 / 250; cíl přesně, nikdy přes fakt, C8); linka se zářícím hrotem od bodu ke kartě; rytmus „jedna informace na dobu“; prstenec bodu → kruh loga | karty 6,0–8,0 (dojezd), 19,0–20,0 (výkon), 21,0–23,0 (0–100 → max. rychlost); 26,0 logo z prstence |

**Co z předloh NEbereme** (vkus uživatele, realismus): plné oranžové / žluté plochy (barvy jen bmw.cz), 3D koule a fluidní simulace
(lukasersil 5–10 s), částicové koule a mřížky teček v pozadí, časové kódy a popisky v rozích (motiondsgnr i lukasersil je mají, předloha souravbhar871
je zakazuje), konfety tvarů v závěru, glitch / RGB posun na textu a logu (C034). **Žádný efekt ani grafika přes vůz** (G7).

## Režijní list
- **Koncept jednou větou**: **„Bod, který nepustí vůz“**: jeden bílý bod s modrým středem (UI bmw.cz) stojí vedle bílého i7 M70 od první
  sekundy, roztočí jeho kola a na drop 1 s ním **vyjede ze studia na silnici** (střih póza na pózu: profil ve studiu = profil v jízdě), na záběrech
  jízdy vede linku ke kartě s faktem, v salonu ukazuje detaily, ve stoupání skáče mezi dlaždicemi, na dropu 2 se rozprskne do světelných stop,
  které **odkryjí** nejprudší průjezd kolem kamery, a na konci se rozevře v bílou clonu a poskládá logo BMW. Nikdy neleží na karoserii,
  vždy vedle vozu (stín, silnice, podlaha). *(revize po oponentuře 2026-11-01, viz „Změny po oponentuře“)*
- **Materiál**: **skutečná jízda** = tiskový film `press_PF0010152` (stříbrná i7 60, high-key grade, **jen 1,2×** + zdvojení snímků, jen úhly
  shora / zezadu / bokem v rozmazání / průlety; **úsek A (kola i7 60 a předek) a dron E (ledvinky zepředu) se nepoužijí**, viz Zakázané)
  + doplněk **W** = `i7web_g70_lci_bev_driving_dynamics_dsk_psf.mp4` src 8,40–10,80 (stříbrná i7 zezadu / bokem podél skály, 720p → 1,5×, 1,75 s);
  **náš vůz** (Alpine White i7 M70, černá M maska, 909 M) = rendry konfigurátoru ve studiu (odhalení, světla, kola, tvář s M maskou, salon);
  salon navíc tmavá videa kokpitu bmw.cz **v dlaždicích** (720p se tak nezvětšuje);
  **SaaS** = bod, linka, karty, pilulky, dlaždice, typografie (Manrope, `media/projekty/004-bmw-jizda/znacka/znacka.css`).
- **Podíl jízdy** (po oponentuře): celoobrazová skutečná jízda 4,0–10,0 + 11,0–12,0 + 18,0–23,0 + 25,0–25,75 = **12,75 s = 42,5 %** (kritérium 2),
  k tomu jízda uvnitř písmen (23,0–25,0), v dlaždicích mřížky (16,0–17,0) a záblesky 3,5 / 3,75 → vůz v pohybu na obrazovce ~15,8 s = 53 %.
  Rozpočet materiálu je napjatý: čistých úseků je jen ~13,3 s zdroje = 11 s výstupu, proto doplněk W a písmena o dobu dřív. 2,5D jízdu z rendru (test B) **nepoužíváme** (koláž).
- **Použitá pravidla**: B1 + B6 (snímek 0 = náš vůz v šeru + nadpis + bod), C7 (událost na každou dobu), D2 + D7 (záběr vzniká z předchozího,
  rozsvícení = rozdíl rendrů zap − vyp), F4 / F7 (pružina 3 % jen UI, kamera kriticky tlumená, jedna kamera), G7 (vůz jen skutečný, nic přes vůz),
  G8 (karty 1 px `#e6e6e6`, dvouvrstvý stín, akcent `#1c69d4` jen na aktivním prvku), I3 (klíčové údery slyšet, nádech 17,75 = hudba ztichne), C8 (fakta doslova).
- **Texty (anglicky, vždy jen jedna vrstva, bez tečky; výbava jen vlastními jmény BMW, odpověď režiséra)**: „THE NEW i7 M70“ · karta „21″“ / „909 M“ ·
  „Electric range (WLTP)“ / „686 km“ · pilulka „BMW Iconic Glow“ · „BMW Panoramic Vision“ · „CraftedClarity“ · „BMW Individual Merino“ ·
  „Power“ / „500 kW“ · „0–100 km/h“ / „3.8 s“ · „Top speed“ / „250 km/h“ · „i7 M70“ (maska) · end card „THE NEW BMW i7 M70 xDRIVE“ + spotřeba
  („Energy consumption combined 18.6 kWh/100 km · CO₂ 0 g/km“, doslova podle odpovědi režiséra) + disclaimer. Karty: popisek
  Manrope 500 22 px `#8e8e8e`, hodnota Manrope 300 72 px `#262626`, jednotka 500 32 px `#8e8e8e`, modrá lišta `#1c69d4` jen při dosednutí čísla.
- **Grade**: stopáž `eq=saturation=0.7` + teplé výšky + zvednutá světla (test A „high-key“), rendry studia lehce dorovnat k témuž (teplota výšek,
  kontrast, jemné zrno stejné velikosti na všem), aby střih render ↔ stopáž neskákal v barvě. Jas: stopáž má YAVG ~60–130, rendry ~200 (změřeno);
  rozdíl je přirozený (studio vs. silnice) a **schovává se jen ve švihu / světle** (P1, P2, P3), ne vyrovnáním (rendry neztmavovat, stopáž nepřepalovat).
  W (web, zlatavé zatažené světlo) dostane týž grade + o 0,2 EV méně teplé výšky, zrno stejné.

## Storyboard / časová osa
Kreativní ředitel, 2026-11-01. Hudba `hudba.json` (120 BPM, doba 0,5 s, takt 2,0 s). **Zdroj jízdy** = `press_PF0010152_sceneId20103_preview.mp4`,
čas „src“ = čas ve zdrojovém souboru (titulní karta 0–4,3 s se nepoužívá). Rychlost **1,2×** (výstup d s = zdroj 1,2·d s) nebo **2,4×** (zdroj 2,4·d s),
uvnitř jednoho záběru se rychlost nemění. **Hranice záběrů zdroje** (ffmpeg scdet): 4,48 · 7,08 · 9,28 · 13,52 · 18,2 · 21,68 · 25,0 · 28,08 · 30,6 · 34,6 · 37,56 · 40,28 · 42,08 · 44,44 · 51,44.
**Čisté úseky** (ověřeno snímky na začátku, uprostřed a na konci, bez čelního pohledu s chromovými ledvinkami): A 8,30–9,20 u kola · B 11,00–12,80 let nad kapotou ke střeše · C 21,70–24,95 záď 3/4 → střecha shora → nakloněný bok · D 28,60–30,55 silnice v protisvětle, vůz v dálce · E 30,65–34,55 dron nad vozem (ledvinky jen shora a malé, povoleno jako „dron“, test C) · F 39,97–40,27 průlet těsně kolem kamery · G 40,30–42,05 sledovací záběr zezadu shora · H 44,50–45,40 kamera přelétá těsně nad střechou · I 50,80–51,40 průjezd bokem, záď odjíždí z obrazu · J 52,30–55,85 dron nad pobřežím, vůz malý.
**Čisté úseky doplněné při opravě v4 (režisér, ověřeno po 0,04 s)**: B 12,80–13,40 (konec průletu nad střechou, střih zdroje 13,52; jen zrcadleně, odlesk slunce 12,80–13,12 ztlumit).
**Zakázané**: 7,08–8,25 · 9,28–10,95 · 13,52–21,65 · 25,0–28,05 · 37,56–39,95 · 42,08–44,45 · 45,45–50,75 (čelní pohledy).
**Po oponentuře zakázané i**: **A 8,30–9,20** (snímek 8,30: leštěné aero kolo i7 60 r ≈ 230 px přes čtvrtinu obrazu + nárazník i7 60 a hrana chromových ledvinek
na x ≈ 560–830, výřez 1,08× ani 1,15× je neschová; vedle karty „909 M“ by divák viděl jiná kola) · **E 30,65–34,55** (dron zepředu: ledvinky s chromovým rámem
a svislými lamelami čitelné na 31,80 / 32,20 / 33,35 / 33,80, vůz přes 15–30 % šířky; odporuje rozhodnutí uživatele „bez čelních pohledů s chromovými ledvinkami“).
**Rozpis úseků po oponentuře** (každý použit jednou, opakování jen v písmenech, dlaždicích a záblescích 3,5 / 3,75): B 11,00–11,60 · 11,60–11,90 · 11,90–12,20 · 12,20–12,80 ·
C 21,72–22,32 · 22,32–23,52 · 23,76–24,36 · 24,36–24,96 · D 28,60–29,20 · 29,20–30,40 · F 39,97–40,27 · G 40,30–40,90 · 40,90–42,05 · H 44,50–44,80 ·
44,80–45,10 · 45,10–45,40 · I 50,80–51,40 · J 52,32–54,72 · 54,72–55,62 · W (web) 8,40–9,00 · 9,60–10,80.

| čas (takt · doba) | záběr: zdroj a čas ve zdroji | pohyb a střih | SaaS grafika / text | zvuk / událost |
|---|---|---|---|---|
| **0,0–2,0** (T1 · 1–4) **probuzení** | `360_svetla_vyp/uhel_030` → `360_svetla_zap/uhel_030` (náš M70, 3/4 předek, příď vlevo), měřítko 0,80 (≤ nativní), vůz ≥ 75 % šířky; celý obraz −1,2 EV („studio před rozsvícením“) | **snímek 0 hotový**: tmavší studio, bílý vůz čitelný. Dotlačení 1,00 → 1,04 nepřetržitě. **0,5** ledvinky Iconic Glow se rozsvítí (rozdíl zap − vyp jen v oblasti ledvinek, maska ze středu ven 0,12 s, zisk rozdílu ×1,8). **1,0** světlomety (zbytek rozdílu). **1,0–1,5** studio se rozsvítí na plnou expozici (globální expozice, smootherstep 0,4 s). **1,5** rychlý oblouk otočky `uhel_030 → 090` (6 snímků za 0,25 s, směrové rozmazání mezi sousedy) + dotlačení na přední kolo | snímek 0: **„THE NEW i7 M70“** vlevo nahoře (Manrope 300, 88 px, bílá, bezpečná zóna), na 0,5 / 1,0 řez skočí 300 → 800 a prostrkání +6 % → −1 % (jeden objekt, souravbhar871). Bílý **bod** (14 px, modrý střed `#1c69d4`) na podlaze před předním kolem od snímku 0, na 1,0 krátce pulzne (kroužek 0,3 s). Nadpis odchází 1,4–1,5 maskou zdola (ease-in) | tlumený kopák 0,0 + klavír · lusknutí 0,5 = „cink“ rozsvícení ledvinek (sklo) · 1,0 nízký hukot světel · 1,5 lusknutí + krátký švih oblouku |
| **2,0–4,0** (T2 · 1–4) **kola 909 M → start** | `360_svetla_zap/uhel_090` (profil, příď vlevo) v měřítku **0,79 nativu** (ostré): na 2,0 celý vůz v obraze (x ≈ 150–1770), na **3,94** sedí **zadní kolo na (1275, 665), r ≈ 115 px** = poloha a velikost zadního kola v I src 50,80 (změřeno, P1) | 2,0–3,94 kamera klouže po boku, vůz se v obraze posune o ~165 px doleva (kriticky tlumeně, směr budoucí jízdy), dotlačení 1,00 → 1,03. 2,0–3,0 kola stojí. **3,0–3,94** **obě** kola se roztáčejí (sprity přední 576/993 a zadní 1873/995 z testu B, rotační rozmazání podle úhlové rychlosti, ease-in; od 3,8 plný rozmazaný disk bez čitelných paprsků, stejně tmavý jako kola v I 50,80), vůz lehce dosedne na záď (2 px, ne víc). **3,75–3,94** vodorovné světelné stopy v pásu podlahy a stěny (ne přes vůz). **3,5 a 3,75 záblesky dopředu**: 5 snímků (0,083 s) skutečné jízdy přes celý obraz (3,5 = C src 24,40–24,50, 3,75 = B src 11,10–11,20), pak zpět do studia (trailerový „flash cut“, předzvěst dropu). **3,94–4,0** švih: vodorovné směrové rozmazání doleva (4 snímky) | **2,0** bod na podlaze pod předním kolem → linka se zářícím hrotem doprava nahoru → karta **„21″“ / „909 M“** (pružina 3 %, roste z konce linky) na stěně studia nad zádí (nad vozem, ne přes něj). **3,0** karta odchází do linky a bodu (ease-in). Bod s roztáčením přeběhne pod zadní kolo a natáhne se do krátké vodorovné stopy | tlumený kopák 2,0 / 2,5 · 2,0 měkký klik karty · **3,0–3,94 elektrický nájezd motoru (stoupající tón) + vír** · 3,0 tick · **3,5 / 3,75 „cvak závěrky“ + krátký vzduch na záblescích** · obrácený činel do 4,0 |
| **4,0–6,0** (T3 · 1–4) **DROP 1: vůz vyjede ze studia** | **4,0** I src 50,80–51,40 (nízká kamera u boku, vůz v rozmazání projede profilem doleva a ujede z obrazu, zadní kolo na 50,80 ≈ (1275, 665)) · **4,5** C src 24,36–24,96 (nakloněný průjezd bokem nad svodidlem) · **5,0** B src 11,00–11,60 (kamera letí nad kapotou k čelnímu sklu) · **5,5** B src 11,60–11,90 (sklo → střecha, 0,25 s) · **5,75** H src 44,80–45,10 (kamera přeskočí hřeben, pod ní černá střecha vozu, 0,25 s) | **4,0 střih póza na pózu (P1)**: studiový profil s rozmazanými koly → týž profil na silnici, zadní kolo na stejném místě a ve stejné velikosti, směr pohybu doleva na obou stranách. 2 snímky expozice +12 % na 4,0. Tvrdé střihy na doby, 5,5–6,0 na čtvrtdoby. Jeden směr pohybu (doleva / od kamery). F a G (nejprudší dvojice) **šetříme na drop 2** | bez textu (čistá rychlost). Bod není | **úder + činel 4,0** · 4,0–4,4 průjezd (Doppler zprava doleva, vrchol 4,15) · 4,5 whoosh · 5,0 vzduch nad kapotou · 5,5 / 5,75 kopák + vzduch nad střechou · hi-hat osminy z hudby |
| **6,0–8,0** (T4 · 1–4) **dojezd** | **6,0** J src 52,32–54,72 (dron nad pobřežní silnicí, vůz malý jede po oblouku, moře nahoře), jeden záběr 2 s, **7,0 punch-in** výřez 1,00 → 1,15 tvrdě na kopák (nový rámec) | 6,0 tvrdý střih, dron klesá (ze zdroje), digitální dotlačení 1,00 → 1,03; 7,0 punch-in 1,15 (≤ 1,15× kvůli 1080p zdroji), karta stojí na místě, bod a linka se přepočítají na nový výřez | **6,0** bod na silnici vedle vozu (klíčové snímky polohy vozu po 0,25 s, bod ve stínu / na asfaltu, ne na laku) → **6,25** linka se zářícím hrotem → **6,5** karta **„Electric range (WLTP)“ / „686 km“** nad mořem vpravo nahoře, číslice rolují 6,5–7,25 (automat, sloupce 0–9, dosednou přesně na 686), **7,25** modrá lišta pod číslem. 7,0 linka se po punch-inu natáhne k bodu (bod dál na silnici vedle vozu). **7,75–8,0** karta odchází do linky a bodu | kopák na doby · 6,0 klik · 6,5–7,25 tiché tikání číslic · 7,25 „ding“ dosednutí (sklo, tiše) · 7,0 punch-in = kopák · 7,75 tick odchodu |
| **8,0–10,0** (T5 · 1–4) **jízda** | **8,0** B src 11,90–12,20 (0,25 s, let nad čelním sklem) · **8,25** W src 8,40–9,00 (web i7: sledovací záběr podél skalní stěny, rozmazané popředí, vůz bokem jede doleva) · **8,75** H src 44,50–44,80 (0,25 s, kamera nízko přeskakuje kamení, rychlost bez vozu = „pohled řidiče“) · **9,0** W src 9,60–10,80 (týž sledovací záběr, vůz blíž, záď 3/4, odjíždí doleva; konec před střihem zdroje 10,85) | tvrdé střihy na doby a čtvrtdoby; W bez punch-inu (720p už je 1,5×), jen dotlačení 1,00 → 1,03. **9,94–10,0** švih doleva ve směru vozu (směrové rozmazání 4 snímky) do rendru, viz P2 | bez textu | 8,0 vzduch přes sklo · 8,25 průjezd (stereo zprava doleva) · 8,75 kopák + šum kamení · 9,0 kopák · 9,5 klap · 9,94 švih (vrchol 10,0) |
| **10,0–12,0** (T6 · 1–4) **tvář M70 → nádech do salonu** | **10,0** `360_svetla_zap/uhel_000` (náš M70 zepředu: černé M ledvinky, Iconic Glow svítí) přijíždí obloukem `060 → 030 → 000` za 0,1 s; **10,5** `g01_predek_den` výřez 1,25× na ledvinky a logo (detail M masky); **11,0** D src 28,60–29,20 (protisvětlo, silný odraz slunce na asfaltu, vůz malý v dálce přijíždí) · **11,5** B src 12,20–12,80 (skutečná kamera přelétá nad černou skleněnou střechou, sklo vyplní ~75 % obrazu) | 10,0 vůz přijede ještě v pohybu (dobrzdí oblouk, dotlačení 1,00 → 1,03). **10,5** tvrdý střih na detail (punch-in na kopák). **10,94–11,0** záře Iconic Glow se na 2 snímky rozzáří (zisk rozdílu zap − vyp ×3) → střih do protisvětla (P3). **11,5–12,0** ponor do střechy **pohybem skutečné kamery** (B 12,20–12,80) + digitální dotlačení jen 1,00 → 1,15 (limit 1080p), od 11,85 vinětace zavírá zbylé ~25 % (poušť) do tmy → 12,0 tma skla = strop interiéru (P4) | **10,0** pilulka **„BMW Iconic Glow“** dole uprostřed (bod vlevo v pilulce, pružina 3 %), 10,25 text odkryt maskou; **10,45** pilulka odchází (text dřív než tvar). 10,5–12,0 bez textu | kopák 10,0 + švih · 10,5 kopák = střih · 10,94 záře „swell“ · 11,0 střih · **11,0–12,0 obrácený činel**, hluboký „ponor“ (vrchol 12,0) |
| **12,0–14,0** (T7 · 1–4) **ZLOM: salon** | **12,0** kostka interiéru (`interier_strop` → `interier_predni`, CSS 3D, FOV ~70°, stěna ~1,17×) · **13,0** deska: dlaždice 1 = totéž (živá kostka), dlaždice 2 = `m7web_g70_lci_mp_interior_cockpit_welcome_dsk_sl.mp4` src 2,0–4,0 (skleněné ovladače CraftedClarity se rozsvítí) | **12,0–12,75** kamera v kostce sklopí pohled ze stropu dolů na palubní desku (rotateX 80° → 0°, kriticky tlumeně), Panoramic Vision a M volant v obraze. **13,0** celý obraz se zmenší do dlaždice (rádius 28, x 96–1004) a odjede doleva, odkryje desku `#f6f6f6` (největší změna měřítka zlomu). **13,25** dlaždice 2 vyjede zdola vpravo (pružina 3 %, stín se zmenšuje s výškou). Kostka v dlaždici se dál pomalu otáčí (rotateY 0 → −12°) | **12,5** bod u spodní hrany Panoramic Vision (na hraně displeje, ne na něm) → linka nahoru → pilulka **„BMW Panoramic Vision“** v ploše čelního skla (pohled ven = světlá stěna studia, ne přes palubní desku). **13,0** pilulka se usadí pod dlaždici 1. **13,5** pilulka přeskočí pod dlaždici 2 a text se uvnitř vymění (vlastní časování odchodu / příchodu): **„CraftedClarity“** | **činel 12,0**, hudba na klavír, kopák tlumený 12,0 / 13,25 · lusknutí 12,5 = bod · 13,0 měkký swoosh zmenšení · 13,25 kopák = dlaždice · lusknutí 13,5 = sklo „ting“ (rozsvícení ovladačů) |
| **14,0–16,0** (T8 · 1–4) **salon: materiál a volant** | **14,0** dlaždice 3 = `g13_interier_sedadla-bok` (Merino Black, 2,5D dotlačení 1,00 → 1,04) · **14,5** dlaždice 4 = `m7web_g70_lci_mp_interior_cockpit_steering_wheel_dsk_sl.mp4` src 8,0–10,0 (ruce na M volantu za jízdy, noc) | **14,0** dlaždice 3 vyjede zprava, celá deska se posune doleva (kamera jede po desce, jeden směr), **14,5** dlaždice 4 vyjede zespodu. **15,0–15,75** kamera najíždí logaritmicky na dlaždici 4, **15,75–16,0** dlaždice 4 vyplní obraz (rohy se otevřou) | **14,0** pilulka přeskočí k dlaždici 3: **„BMW Individual Merino“** · **14,5** pilulka bez textu (popisné názvy nepoužíváme, odpověď režiséra) se stáhne do bodu a ten skočí do rohu dlaždice 4 jako „výběr“ (stisk −15 % + kroužek akcentu) | kopák tlumený 14,0 / 15,25 · lusknutí 14,5 / 15,5 · 14,0 / 14,5 měkké kliky dlaždic · 15,0–16,0 swoosh najetí + začátek stoupání |
| **16,0–18,0** (T9 · 1–4) **STOUPÁNÍ: všechno najednou** | **16,0** mřížka 3×3 (dlaždice ~560×315, mezera 32, rádius 20, pozadí `#262626`): (1) kostka interiéru (Panoramic Vision), (2) C src 24,0 bok, (3) `uhel_090` kola 909 M (točí se), (4) G src 41,2 záď, (5) **volant** `m7web_g70_lci_mp_interior_cockpit_steering_wheel_dsk_sl.mp4` (pokračuje z 15,75, střed mřížky), (6) J src 53,0 dron, (7) `g13`, (8) I src 50,9 průjezd, (9) `uhel_000` zap tvář · **17,0** dlaždice 5 přes celý obraz | **16,0–16,25** kamera odjede z celého obrazu volantu do mřížky (log zoom, kriticky tlumeně; volant je středová dlaždice, takže odjezd je čistý). Dlaždice se rozsvěcují po osminách (16,0 / 16,125 / … 16,875 = spiccato), každá s živým záběrem, statické rendry (3, 7, 9) s vlastním pohybem (kola se točí, dotlačení). **16,5 a 17,0** (řazení motoru) mřížka poskočí o 2 % měřítka. **17,0** kamera se vrhne zpět do středové dlaždice 5: ruce sevřou M volant, 17,0–17,5 přes celý obraz (720p → 1,5×, tma a pohyb, jen 0,5 s). **Páčka BOOST z M760e se nepoužije** (odpověď režiséra). **17,5–17,75** obraz se stáhne do tmy (vinětace se zavře do kruhu) | bod skáče po dlaždicích tak, jak se rozsvěcují (vždy v rohu dlaždice, ne na voze), na **17,0** dopadne do středu (dlaždice 5). **17,75–18,0 NÁDECH**: vše zmizí, zůstane **jen bod** uprostřed černé, bod se smrští na 8 px | **motor nájezd 16,0 → 18,0**, řazení 16,5 / 17,0, vír bubnu, kopák na doby, spiccato osminy · 17,0 stisk volantu (kůže, tichý „grip“) · **17,75–18,0 hudba ztichne** (automatika −12 dB), jen nádech |
| **18,0–20,0** (T10 · 1–4) **DROP 2: rychlost** | **18,0** F src 39,97–40,27 (vůz prolétne těsně kolem kamery v rozmazání, 0,25 s) · **18,25** G src 40,30–40,90 (hned zezadu shora: vůz, který právě prolétl, ujíždí) · **18,75** H src 45,10–45,40 (kamera přelétá těsně nad černou střechou, 0,25 s) · **19,0** G src 40,90–42,05 (pokračování sledovacího záběru zezadu shora, vůz v oblouku, kamera se na konci stočí k boku) | **18,0 bod vybuchne** do svazku vodorovných světelných stop (bílá + `#1c69d4`, směr doleva) a **stopy jsou maska**: záběr F se odkryje uvnitř stop, ty se za 0,12 s rozšíří přes celý obraz (lukasersil), od 18,12 je obraz čistá stopáž bez grafiky. 2 snímky expozice +15 %. **18,0–19,0 čtyři střihy (čtvrtdoby a doby)** = nejhustší střih videa, víc než drop 1. 19,0 dotlačení 1,00 → 1,04 | **19,0** bod na asfaltu vlevo od vozu (ve stínu) → linka → karta **„Power“ / „500 kW“** **vlevo nahoře** (x 96–500, y 110–330; vůz na 41,0 začíná až na x ≈ 0,38 šířky nahoře), číslice rolují 19,1–19,6, 19,6 modrá lišta. **19,875** karta odchází do bodu | **úder + činel 18,0 = nejhlasitější místo videa** (I3, C032), **18,0–18,3 průlet těsně kolem (Doppler, vrchol 18,1)** · 18,25 kopák · 18,75 vzduch nad střechou · 19,0 řazení + klik karty · 19,1–19,6 tikání · 19,6 ding |
| **20,0–22,0** (T11 · 1–4) **0–100** | **20,0** C src 21,72–22,32 (zezadu 3/4 za vozem na pobřeží, vůz se vrhá do zatáčky) · **20,5** C src 23,76–24,36 (nakloněný průjezd bokem, diagonála) · **21,0** C src 22,32–23,52 (střecha shora, vůz se stáčí a ujíždí nahoru; levá horní třetina je volná silnice) | tvrdé střihy na doby, 21,0 dotlačení 1,00 → 1,03 | **21,0** bod vlevo od vozu na asfaltu (klíčové snímky po 0,25 s) → linka → karta **„0–100 km/h“ / „3.8 s“** na **stejném místě vlevo nahoře** jako 500 kW (jedno místo pro fakta = rytmus adamdesgns), číslice rolují 21,25–21,75 (zdola nahoru na přesně 3.8), 21,75 modrá lišta + kroužek | kopák · 20,0 kopák + vzduch · 20,5 řazení + průjezd · 21,0 klik · 21,25–21,75 tikání · 21,75 ding |
| **22,0–23,0** (T12 · 1–2) **max. rychlost** | **22,0** D src 29,20–30,40 (protisvětlo: vůz přijíždí odleskem slunce po asfaltu a na ~22,7–22,9 projede v rozmazání doleva z obrazu) | tvrdý střih 22,0; dotlačení 1,00 → 1,04; průjezd vozu = vrchol záběru | **22,0** štítek karty se maskou přemění: **„Top speed“ / „250 km/h“**, karta zůstává vlevo nahoře **v obloze** (vůz projíždí ve výšce 0,40–0,70 obrazu), číslice rolují 22,0–22,6 (nikdy nad 250, C8), 22,6 lišta. **22,875** karta odchází do bodu, bod odjede s vozem | kopák · 22,0 přepnutí štítku (tick) · 22,0–22,6 tikání · 22,6 ding · **22,7–22,95 průjezd (Doppler)** |
| **23,0–26,0** (T12 d3 – T13) **i7 M70 → odjezd** | **23,0** písmena „i7 M70“ (Manrope 800, výška ~620 px, přes celou šířku) na `#f6f6f6`, **uvnitř písmen** (opakování povoleno jen tady, v masce písma): 23,0 G src 40,30–40,90 → 23,5 I src 50,80–51,40 → 24,0 F src 39,97–40,27 → 24,25 H src 44,80–45,40 · **25,0** J src 54,72–55,62 (dron, vůz malý odjíždí po pobřeží) | **23,0** písmena vjedou rozřezaná na 6 vodorovných pásů, sudé zprava, liché zleva (lukasersil LINE), dosednou na 23,25; 23,5 / 24,0 / 24,25 výměna záběru uvnitř písmen (střih uvnitř masky), 24,0 řez 800 → 700 → 800 „nádech“ písma. **24,75–25,0** kamera proletí otvorem písmene „7“ (měřítko 1 → 9, log), jízda uvnitř se stane celým obrazem = **karta → celý obraz** na 25,0. **25,5–25,75** dron, kamera klesá; **25,75–26,0** clona (P6) | 23,0–25,0 jediný text = „i7 M70“ (maska se stopáží). **25,0** bod u vozu na silnici (bez linky). **25,75** bod se rozevře v **bílý kruh** (clona z bodu přes celý obraz, ease-in, 0,25 s) | 23,0 švih pásů (stereo L/R) · kopák · 23,5 / 24,0 / 24,25 kopák = střih uvnitř · 24,75 nádech průletu · 25,0 průjezd · **25,5–26,0 vír + obrácený činel** |
| **26,0–28,0** (T14 · 1–4) **LOGO** | bílé pozadí `#ffffff`, logo BMW z `znacka/logo/vrstvy/01–09` (originální barvy `#0066b1`, `#6f6f6f`) | **26,0** prstenec bodu se stane vnějším kruhem loga (stejný střed a tloušťka), 26,0–26,5 čtvrtiny se poskládají (dvě modré dopadnou na 26,0 a 26,25, kriticky tlumeně, žádná deformace), 26,5 písmena BMW naskočí po obvodu (maska po oblouku). Dotlačení 1,00 → 1,03 nepřetržitě do 30,0 | **27,0** pod logem **„THE NEW BMW i7 M70 xDRIVE“** (`#262626`, 56 px) se odkryje maskou zdola jako celek v řezu **Manrope 300 s prostrkáním +8 %** a na **27,5** (doba) se srovná do **700 / 0 %** (jeden objekt mění řez, souravbhar871, zrcadlí háček 0,5–1,0) | **úder + činel + akord 26,0**, měkký dopad loga, 26,25 tick, 26,5 jemný „ting“, 27,5 tichý „klap“ řezu |
| **28,0–30,0** (T15 · 1–4) **end card** | totéž | 28,0 jediný glint přejede po vnějším kruhu loga (lesk, ne záře, max +12 % `screen`); pohyb dotlačení pokračuje, žádný zamrzlý snímek. Poslední snímek = klidné end card | **28,0** dole uprostřed dva řádky (Manrope 500, 18 px, `#666666` kompenzovat podle C041, jeden objekt, odkrytí maskou zdola): **„Energy consumption combined 18.6 kWh/100 km · CO₂ 0 g/km“** a **„Concept ad · not affiliated with BMW · Footage and renders © BMW AG · Driving scenes: BMW i7 60 xDrive“** (obojí potvrdil režisér) | doznívání akordu, 28,0 tichý glint, konec 30,0 bez ořízlého dozvuku |

### Přechody skutečný záběr ↔ render (musí být věrohodné)
Obecně: render je **studio** (produktový záběr), stopáž je **silnice**. Nepředstíráme, že jsou v jednom prostoru (to by byla koláž, test B);
spojujeme je **pohybem, polohou a světlem** jako ve skutečné reklamě, kde se střídá ateliér a jízda. Obě strany mají stejný grade (teplé výšky,
zvednutá světla, sytost 0,7 u stopáže / dorovnaný kontrast u rendru) a **stejné zrno** (seed, velikost 1,5 px, krytí ~3 %).
- **P1 póza na pózu: studio → silnice (3,94–4,0, drop 1)** *(po oponentuře; původní střih kolo → kolo na A src 8,30 zrušen: ve stopáži je leštěné aero
  kolo i7 60 o poloměru ≈ 230 px a nárazník i7 60, tedy na nejsledovanějším místě videa by se kola 909 M změnila v jiná a render by se musel zvětšit 1,6× nad nativ)*.
  Render `uhel_090` v měřítku 0,79 nativu má na 3,94 **zadní kolo na (1275, 665), r ≈ 115 px** = zadní kolo v I src 50,80 (změřeno na snímku: střed ≈ (1275, 665),
  ráfek tmavý, rozmazaný). Přední kolo rendru je u levého okraje uříznuté stejně jako ve stopáži (tam je perspektivou větší, r ≈ 250 px; rozdíl schová švih).
  Rotace v rendru 3,0–3,94 dojede do plného rozmazaného disku (paprsky nečitelné, jas disku jako kola v I). 3,94–4,0 render s **vodorovným směrovým
  rozmazáním doleva** (4 snímky, délka šmouhy jako rozmazání pozadí v I 50,80), na 4,0 tvrdý střih, 2 snímky expozice +12 %. Kontrola: zadní kolo
  4,0 vs. 3,983 ± 20 px, poloměr ± 10 %, linie prahu a spodní hrana oken ± 30 px. Divák vidí: vůz, který stál ve studiu, je najednou v plné rychlosti na silnici.
- **P2 švih stopáž → render (9,94–10,0)**: W končí vozem, který odjíždí doleva; přidat 4 snímky směrového rozmazání doleva (délka podle
  rychlosti pozadí ve zdroji) a v nich expozici +0,4 EV (rozmazaný světlý pás vede do světlého studia). Render přijede **už v pohybu**: oblouk otočky
  `060 → 030 → 000` za 0,1 s (6 snímků, rozmazání mezi sousedy) + posun obrazu zprava doleva, který dobrzdí kriticky tlumeně do 10,2. Směr rozmazání
  na obou stranách střihu stejný. Jas: měřit poslední a první **rozmazaný** snímek (rozdíl YAVG ≤ 15 %), ostré snímky smí mít rozdíl studio / silnice.
- **P3 záře → protisvětlo (10,94–11,0)**: rozdíl zap − vyp (skutečné světlo Iconic Glow) se na 2 snímky zesílí ×3 a lehce rozkvete (bloom jen
  ze světla ledvinek, v barvě světla, ne bílý záblesk celého obrazu) → tvrdý střih do D src 28,60 s nejsilnějším odrazem slunce na asfaltu (YAVG ~132)
  ve stejné výšce obrazu (střed záře rendru a odraz slunce ± 80 px, případně výřez stopáže ≤ 1,15× posunout). Světlo navazuje na světlo.
- **P4 ponor do střechy (11,5–12,0 → 12,0)** *(po oponentuře)*: B src 12,20–12,80 = skutečná kamera přelétá nad černou skleněnou střechou, na 12,70
  je sklo ~75 % obrazu (YAVG ~64). Digitálně jen dotlačení 1,00 → 1,15 (původní zoom 2,4× by na 1080p zdroji rozbil obraz na bloky, C037),
  od 11,85 vinětace zavře zbylou poušť do tmy (ease-in), na 11,983 průměrný jas < 20/255 a žádná hrana karoserie. Na 12,0 kostka interiéru začíná
  pohledem na `interier_strop` (tmavý strop, jas do 30/255) a sklápí se dolů. Tma skla = tma stropu: střih se schová v černé.
- **P5 dlaždice → celý obraz (13,0, 15,75–16,0, 17,0)**: SaaS změna měřítka, žádná prolínačka. Obsah dlaždice běží dál při změně velikosti
  (jeden čas, žádný reset), rohy se otevřou z rádiusu 28 na 0 až v posledních 0,1 s.
- **P6 bod → clona → logo (25,75–26,0)**: bod sleduje vůz v J (klíčové snímky po 0,25 s), na 25,75 se z něj rozevře bílý kruh přes celý obraz
  (ease-in, rozmazaný okraj 6 px), na 26,0 je obraz celý bílý a **prstenec bodu = vnější kruh loga** (stejný střed, plynulé zmenšení na velikost
  loga 26,0–26,25). Bod tak doslova „dojede“ do loga.

### Kontrolní snímky (před plným renderem, z výřezu s podsnímky, C028) a kritéria odmítnutí
| čas | co musí být vidět | odmítnout, když |
|---|---|---|
| 0,000 | hotový plakát: bílý M70 v šeru, nadpis, bod na podlaze | vůz pod 75 % šířky, obraz šedý / zašlý („hliněný model“, V003), text mimo bezpečnou zónu, viditelné bloky komprese (C037) |
| 0,55 / 1,05 | rozsvícené ledvinky / světlomety | světlo jako nakreslená čára nebo neon, lem kolem ledvinek, světlo mimo skutečné tvary rendru |
| 2,5 | celý profil M70, kola 909 M ostrá, karta „21″ / 909 M“ nad zádí, linka od bodu na podlaze | karta nebo linka přes vůz, render nad nativ (měkký), stín karty na rendru |
| 3,5 / 3,583 / 3,75 | záblesk jízdy 5 snímků, pak zpět studio; rotační rozmazání obou kol, stopy jen v podlaze / stěně | záblesk delší než 6 snímků nebo s ledvinkami, rozmazaný ráfek světlejší / tmavší než kola v I 50,80, stopy přes karoserii, vůz „plave“ |
| 3,983 / 4,000 / 4,017 | póza na pózu: zadní kolo na stejném místě a velikosti, směr doleva na obou stranách | skok zadního kola > 20 px, poloměr ± 10 %, na 4,0 čitelný design kol i7 60 nebo chrom ledvinek, dvojitá kola z prolínání (zákaz `framerate` / `minterpolate`) |
| 4,25 / 5,10 / 5,80 | vůz projíždí a ujíždí z obrazu, let nad kapotou, střecha pod kamerou | trhavá kadence (snímky se neopakují přesně 2×), jiný grade než 4,0, chrom ledvinek v prvním / posledním snímku |
| 6,75 / 7,05 | karta 686 km, bod vedle vozu na asfaltu, punch-in | bod na laku, číslo jiné než 686, karta přes vůz, punch-in > 1,15× |
| 8,5 / 9,5 / 9,983 / 10,05 / 10,25 | W bez bloků a ostrý jako stopáž (porovnat se 100% výřezem), švih do rendru, tvář M70 s černými M ledvinkami, pilulka | W viditelně měkčí než okolní stopáž nebo CGI vzhled (pak náhrada, viz Změny), rozdíl jasu rozmazaných snímků švihu > 15 %, rozmazání na obou stranách v jiném směru |
| 10,95 / 11,0 | záře ledvinek → odraz slunce | bílý záblesk přes celý obraz, duha / RGB lem (C034) |
| 11,6 / 11,9 / 11,983 / 12,05 / 12,5 | skutečný přelet nad střechou, ponor do skla, tma, kostka interiéru | dotlačení > 1,15×, ve tmě je vidět okraj skla nebo karoserie, střih nespadne do tmy, koláž dvou perspektiv v kostce (V003) |
| 13,5 / 14,25 / 14,75 | deska s dlaždicemi, pilulka s textem | dvě vrstvy textu naráz, 720p video zvětšené nad nativ (rozmazané), pilulka přes palubní desku v dlaždici |
| 16,6 / 17,0 / 17,6 | mřížka 3×3 živá, volant přes obraz, stahování do tmy | prázdné nebo stojící dlaždice, mřížka bez pohybu, bod přes vůz, páčka BOOST v obraze |
| 17,9 / 18,0 / 18,05 / 18,12 / 18,3 / 18,8 | bod sám v tmě → výbuch stop, uvnitř stop odkrytý průlet F → záď G → střecha H | stopy jako vrstva přes vůz po 18,12, záblesk neviditelný kvůli závěrce (C028), drop 2 slabší než drop 1 (méně střihů, slabší záběr, tišší vrchol) |
| 19,6 / 21,6 / 22,6 / 22,8 | karty 500 kW / 3.8 s / 250 km/h vlevo nahoře, průjezd D pod kartou | jakékoli číslo nad faktem během rolování (C8, V003 259), schodovité ozvěny číslic (C040), karta přes vůz (G 41,0 a D 30,1 kontrolovat po snímku), ledvinky zepředu v kterémkoli záběru |
| 23,25 / 24,1 / 24,6 / 24,9 | písmena i7 M70 s jízdou uvnitř, průlet otvorem „7“ | jízda v písmenech nečitelná (příliš tmavá), písmena deformovaná, čáry pásů nesrovnané po dosednutí |
| 25,9 / 26,0 / 26,3 / 27,25 / 27,6 / 28,5 / 29,98 | clona, prstenec → logo, nadpis mění řez 300 → 700, spotřeba + disclaimer, poslední snímek | logo deformované nebo v jiných barvách než `#0066b1` / `#6f6f6f` (změřit v MP4), překlep, spotřeba jinak než doslova, drobný text pod 16 px nebo mimo bezpečnou zónu, zamrzlý obraz |

### Pasti stavby
1. **Kadence 25 → 60 fps**: jen **1,2×** (přesně 2:2) nebo **2,4×** (1:1). Nikdy 1,0× ani 1,5× (nepravidelné opakování = trhání), nikdy `minterpolate`
   (bloky na přídi) ani `framerate` (dvojitá kola). Rychlost se nemění uvnitř záběru. Desky stopáže připravit ffmpegem (`test/skripty/test_a.sh`)
   jako 30 fps sekvence a ve scéně hranici snímku posunout o 1/120 s (test C), aby podsnímky závěrky (`--sub 4`) nemíchaly dva snímky zdroje.
2. **Začátky výřezů na hranici snímku zdroje** (25 fps → násobky 0,04 s). Ledvinky nesmí probliknout v prvním ani posledním snímku (hranice
   záběrů výše). Výřez stopáže nejvýš 1,15× (1080p zdroj), rendry nejvýš nativ (2560 → 1920 = 0,75; tedy měřítko ≤ 1,33 od základní velikosti).
3. **Grade jednotně** jedním filtrem pro všechny desky stopáže; rendry dorovnat k témuž (teplé výšky). Zrno na všem stejné (seed). Noční / tmavé
   rendry nepoužívat (V003 „hliněný model“): šero v háčku je globální expozice −1,2 EV denního rendru, ne noční render.
4. **Otočka 360° (komprese ~60 kB)**: jen rychlé oblouky na úder (≤ 0,25 s) a statické záběry ≤ 1,5 s; plochy studia jemně vyhladit + zrno (C037).
5. **Bod a karty nikdy na voze**: poloha vozu ve stopáži = ručně změřené klíčové snímky po 0,25 s (test C), bod 30–60 px od siluety ve stínu
   nebo na asfaltu; kontrola pásu snímků po 1 snímku, že bod nevjede na lak. Karty nemají stín na stopáži ani rendru (G8).
6. **Čísla** (C8, C040): rolování končí přesně na faktu, nikdy přes něj; rozměry pro pohyb měřit jednou ze stabilního stavu; rozmazání číslic v kódu,
   ne kopiemi. Fakta jen: 500 kW, 0–100 km/h 3.8 s, 250 km/h, 686 km (WLTP).
7. **Barvy tenkého textu** (C041) a loga (C034) změřit v hotovém MP4; logo bez RGB posunu a bez deformace.
8. **Moduly scény** (C036): klíče časů s prefixem bloku (`A_`, `B_`), regrese i uvnitř přechodů (3,983 / 4,0 / 4,017, 17,983 / 18,0).
9. **Záblesky na úder** (C028): 2 snímky, ověřit ve výřezu s podsnímky, ne staticky.
10. **Výkon renderu** (C027): změřit 1 s výřezu (nejtěžší úsek 16–18 s mřížkou 9 videí a 23,0–25 s maskou písmen). Videa v dlaždicích připravit
    předem jako sekvence snímků ve velikosti dlaždice (žádné dekódování 720p videa při seek).
11. **Zvuk** (C035, C039): SFX posunout na skutečné časy obrazu po stavbě, klíčové údery 4,0 / 18,0 / 26,0 měřit vrcholem; drop 2 nejhlasitější;
    17,75–18,0 hudba opravdu ztichne (automatika). Odvozené soubory při přegenerování smazat.
12. **Text jen jedna vrstva**: odcházející text zmizí dřív, než přijde další (pilulka mění text uvnitř s vlastním časováním).
13. **Zakázané úseky po oponentuře** (A 8,30–9,20, E 30,65–34,55) nepoužít ani v dlaždicích a záblescích. Rozpočet čistých úseků je napjatý:
    žádný úsek neprodlužovat přes hranici záběru zdroje (21,68 · 25,0 · 30,6 · 40,28 · 42,08 · 51,44) a W nepouštět za 10,84 (střih na čelní pohled).
14. **W (web 720p)**: jediné zvětšení 1,5× (1646×720 → 2470×1080, ořez na 1920), žádný další punch-in, doostření jen jemné (unsharp ≤ 0,4), zrno přes.
    Když W na 100 % výřezu vypadá měkce nebo jako CGI: náhrada 8,25–9,0 = H 44,50–44,80 + C 24,36–24,66 (opakování) a 9,0–10,0 = render `g11` / `uhel_060`
    s obloukem a švihem (podíl jízdy pak ~40 %), rozhodne kreativní ředitel na klíčových snímcích.

### Pořadí stavby
1. **Desky stopáže** (animátor, ffmpeg): 21 výřezů podle „Rozpisu úseků po oponentuře“ (B, C, D, F, G, H, I, J + W) + 2 záblesky (3,5 / 3,75)
   + výplně písmen, vše 1,2× + zdvojení, grade high-key, 30 fps sekvence; pás snímků každého výřezu (kontrola ledvinek a kadence). Klíčové snímky polohy vozu
   (po 0,25 s) pro J 52,32–55,62, G 40,90–42,05, C 22,32–23,52, D 29,20–30,40 (body a karty) a střed / poloměr zadního kola I 50,80 (P1).
2. **Podklady rendrů**: expozice −1,2 EV + maska ledvinek / světlometů z rozdílu zap − vyp (`uhel_030`, `uhel_000`), sprity **obou** kol z testu B,
   kostka interiéru, dlaždice salonu (videa jako sekvence ve velikosti dlaždice), vrstvy loga.
3. **Blok A 0–12 s** (háček, kolo, P1, drop 1, karta 686, P2, tvář M70, P3, P4) → kontrolní snímky bloku A → **kreativní ředitel schválí klíčové
   snímky** (0,0 · 2,5 · 3,983 / 4,0 · 6,75 · 9,5 (W) · 10,25 · 11,983) dřív, než se staví blok B.
4. **Blok B 12–30 s** (salon, mřížka, nádech, drop 2, karty, písmena, clona, logo, end card) + plný render celého videa a spojení se zvukem
   (zvukař souběžně: SFX podle sloupce zvuku, pak posun na skutečné časy).
5. Kontrola: kritik + kreativní ředitel (wow, realismus, energie), opravy jeden animátor.

### Změny po oponentuře (nezávislý kreativní ředitel, 2026-11-01)
Ověřeno na snímcích zdroje po 0,1–0,3 s (`press_PF0010152` 8,30 / 11,0–12,8 / 21,7–24,95 / 28,6–30,5 / 31,0–34,5 / 39,97–42,0 / 44,5–45,4 / 50,8–51,4 / 52,3–55,6,
web i7 7,8–11,0), na rendrech `uhel_030 / 090 / 000` a měřením jasu (YAVG). **Skóre původního storyboardu**: vůz jede 7 · realismus 6 · energie 7,5 ·
nápad 8,5 · řemeslo 7,5 → **celkem 7,4**. **Po revizi (odhad)**: vůz jede 9 · realismus 9 · energie 9 · nápad 8,5 · řemeslo 8,5 → **celkem 8,8**.
Seřazeno podle dopadu na „wow“:
1. **Drop 1 (4,0): kolo → kolo nahrazeno střihem póza na pózu studio → silnice.** A src 8,30 má leštěné aero kolo i7 60 (r ≈ 230 px, ne 146) a předek
   i7 60 s hranou chromových ledvinek na x ≈ 560–830, výřez ho neschová. Po kartě „909 M“ by divák na nejsilnějším místě viděl jiná kola. Nově: profil M70
   ve studiu (0,79 nativu, oba kola se roztočí) → I src 50,80 (stejný profil, zadní kolo změřeno na (1275, 665), r ≈ 115), vůz „vyjede ze studia“.
2. **Dron E (31,0–34,55) vyřazen celý.** Na 31,80 / 32,20 / 33,35 / 33,80 jsou ledvinky s chromovým rámem a svislými lamelami zepředu čitelné, a to
   v 3,6 s dropu 2 pod všemi třemi kartami výkonu. Odporuje rozhodnutí uživatele (varianta 1 „bez čelních pohledů s chromovými ledvinkami“).
   Karty teď stojí na G (zezadu shora), C (střecha shora) a D (protisvětlo), vždy **na stejném místě vlevo nahoře** (jedno místo pro fakta).
3. **Drop 2 je teď silnější než drop 1.** Nejprudší dvojice záběrů (F průlet těsně kolem kamery → G záď hned za ním) přesunuta z dropu 1 do dropu 2;
   původně drop 2 začínal H 44,80, kde je vůz jen pruh u spodní hrany. Světelné stopy z bodu jsou **maska, která průlet odkryje** (od 18,12 bez grafiky
   přes vůz), 18,0–19,0 čtyři střihy = nejhustší místo videa, 18,0 nejhlasitější.
4. **P4 ponor do střechy skutečnou kamerou** (B 12,20–12,80 sama přelétá nad černým sklem) místo digitálního zoomu 2,4× na C 22,70 (porušoval
   vlastní limit 1,15× a rozbil by 1080p zdroj na bloky).
5. **Háček 2,0–4,0 dostal pohyb a jízdu**: celý profil místo detailu jednoho kola, obě kola se roztáčejí, záblesky skutečné jízdy na 3,5 a 3,75
   (5 snímků, trailerový flash cut), takže skutečný pohyb je v obraze už před dropem (V003: „vůz musí jet“).
6. **Rozpočet materiálu**: po vyřazení A a E zbývá jen ~13,3 s čistého zdroje = 11 s výstupu. Řešení: rozpis úseků (každý jednou), písmena „i7 M70“
   o dobu dřív (23,0, opakování v masce povoleno), doplněk W (web i7, sledovací záběr podél skály, 8,25–10,0) s pravidlem náhrady, když na 100 %
   vypadá měkce (past 14). D 28,60 (vůz jako tečka) už nenese „jízdu“ v 9,0, jen světelný most P3.
7. **Jas render ↔ stopáž** změřen: rendry YAVG ~200, stopáž ~60–130. Kritérium „skok > 10 %“ by nesplnil žádný přechod; nově se měří rozmazané snímky švihu
   (≤ 15 %) a rozdíl se schovává ve švihu / světle, ne vyrovnáním (ztmavené rendry = „hliněný model“ z V003).
8. **Odpovědi režiséra zapracovány**: páčka BOOST z M760e pryč (střed mřížky a skok 17,0 = ruce na M volantu), pilulky jen vlastní jména BMW
   („BMW Iconic Glow“, „CraftedClarity“, „BMW Individual Merino“, karta „21″ / 909 M“, popisná pilulka volantu zrušena), spotřeba na end card.
9. **Předlohy čitelnější**: souravbhar871 teď i na end card (nadpis mění řez 300 → 700 a prostrkání na dobu 27,5, zrcadlí háček), adamdesgns jedním
   místem pro fakta a morfem štítku 500 kW → 3.8 s → 250 km/h, motiondsgnr mřížka 16–17,5 beze změny, lukasersil stopy jako odkrytí + pásy písmen + clona.
**Beze změny (funguje)**: snímek 0 s rozsvícením ledvinek z rozdílu zap − vyp, karta 686 km na dronu J s punch-inem, P3 záře → odraz slunce, salon
jako deska s dlaždicemi, mřížka 3×3, nádech 17,75 jen s bodem, bod → clona → prstenec loga, disclaimer.

## Záběry pro scénu (střihač, 2026-11-01)
Výstup `media/projekty/004-bmw-jizda/zabery/<id>/000.jpg…` (JPG q2, BT.709 → sRGB/JFIF převedeno explicitně), u každého `pas.jpg` (všechny snímky)
a `nahled.jpg` (první / střed / konec), přehled všech `_prehled_1–4.jpg`, seznam `zabery/seznam.json`, skript `zabery/_skript/zabery.py`
(znovu vyrobí jeden nebo všechny záběry). **32 záběrů, 718 snímků, 115 MB.**
- **Technika**: výřez podle **indexu snímku** zdroje (web videa mají rozbitá časová razítka kontejneru, `-ss` by tam vybral jiné snímky), takže začátky
  jsou vždy na mřížce 25 fps (časy ze storyboardu, které na ní neleží, posunuty o 0,02 s). Každý zdrojový snímek = 1 snímek sekvence 30 fps
  = **rychlost 1,2×**; ve scéně index `floor((t − t0 + 1/120)·30)` = přesná kadence 2:2 na 60 fps, žádná interpolace, ověřeno: žádné dva sousední
  snímky nejsou stejné. Grade = `test_a.sh` high-key (sytost 0,7, teplé výšky, křivka), převod do RGB s maticí BT.709 (o ~2/255 světlejší než
  test A, kde se převádělo výchozí maticí). Web W o něco méně teplé výšky. Zrno není zapečené (přidá scéna jednotně).
- **Ořezy**: tisk 1920×1080 beze změny (bez textu, bez vodoznaku) kromě `B_1100` a záblesku `Z_B1108`: **výřez 1,15× ukotvený vpravo nahoře**, protože
  v B 11,00–11,40 je u levého okraje shora vidět chromový rámeček ledvinek i7 60. Web W 1646×720 → okno 1280×720 od x = 360 → 1,5× lanczos + unsharp 0,35.
  Volant okno od x = 120 (texty displejů „48“, „Ind…“ zůstanou mimo), 1,5×. Ovladače CraftedClarity nativně 1280×720 (jen dlaždice). Dlaždice mřížky 960×540.
- **Rozpis** (id → slot): I_5080 → 4,0 · C_2436 → 4,5 · B_1100 → 5,0 · B_1160 → 5,5 · H_4480 → 5,75 · J_5232 → 6,0–8,0 · B_1188 → 8,0 · W_840 → 8,25 ·
  H_4448 → 8,75 · W_960 → 9,0–10,0 · D_2840 → 11,0 · B_1220 → 11,5 · F_4000 → 18,0 · G_4028 → 18,25 · H_4508 → 18,75 · G_4088 → 19,0–20,0 ·
  C_2172 → 20,0 · C_2376 → 20,5 · C_2232 → 21,0–22,0 · záblesky Z_C2440 → 3,5, Z_B1108 → 3,75 · písmena G_4028 / I_5080 / F_4000 / H_4480_L ·
  mřížka M2_C2376, M4_G4120, M6_J5300, M8_I5080 · salon S_ovladace → 13,25, S_volant → 14,5–17,23 · rezerva W_788, W_900, X_0448, D_3008.
- **Vyřazeno / změněno při prohlídce po snímcích** (rozhodnutí v kompetenci střihače, k potvrzení režisérem):
  1. **D 29,20–30,40 (22,0–23,0, karta Top speed) vyřazen**: vůz přijíždí **čelně**, chromové ledvinky i7 60 čitelné od 29,20 (vůz ~180 px) do 30,04
     (~260 px). Náhrada: `D_3008` (30,08–30,60, 13 snímků = 0,43 s: průjezd v rozmazání doleva, pak prázdná silnice v protisvětle), zbytek slotu viz otázky.
  2. **J 54,72–55,62 (25,0–25,75) vyřazen**: vůz jede **ke kameře** (ne „odjíždí“), na 55,00–55,40 je maska ledvinek shora čitelná. Náhrada `X_0448`
     (4,48–7,08, dosud nepoužitý dron nad útesem a pobřežní silnicí; vůz malý vjede vpravo dole od snímku 28 a **odjíždí** nahoru doleva), pro 25,0–25,75 snímky 42–64.
  3. **J_5232 (6,0–8,0) riziko**: od 53,72 (snímek 35) vůz přijíždí čelně 70–100 px a ledvinky jsou poznat jako tvar se světlem; punch-in 1,15× na 7,0
     to zesílí. Návrh: 7,0–8,0 střih na `X_0448` snímky 35–64 (nový rámec na kopák místo punch-inu).
  4. **F začíná 40,00** místo 39,97: snímek 39,96 ukazuje chromové ledvinky zepředu. F má tedy 7 snímků (0,233 s), poslední podržet o 1/60 s.
  5. **D (11,0) posunut na 28,40–29,00** (`D_2840`): na 29,04–29,16 je vůz zepředu už 70 px; odraz slunce na asfaltu je stejný (YAVG 145).
  6. **Ovladače CraftedClarity začínají 2,40**, ne 2,0 (do 2,36 je ve zdroji jiný záběr: lesklá lišta). 79 snímků = 2,63 s.
  7. **Volant má jen 82 čistých snímků (7,96–11,24) = 2,73 s**, storyboard chce 14,5–17,5 = 3,0 s (chybí 8 snímků), viz otázky.
- **Poznámky pro animátora**: W vůz jede **doprava od kamery** (sledovací záběr, pozadí ubíhá doleva), směr švihu P2 doleva tedy sedí s pozadím, ne s vozem.
  C_2172 a G_4028 / G_4088 mají čitelnou SPZ i7 60 (M DI 285E, skutečná stopáž, ponecháno). Jas desek (YAVG): B_1100 135 (1,9 % pixelů ≥ 254,
  bílá kapota), D_2840 145, I_5080 112, W_960 113, G_4088 88, B_1220 69.

## Zvuk v1 (zvukař, 2026-11-01)
101 SFX podle sloupce zvuku storyboardu (+ Změny po oponentuře) v `projekty/004-bmw-jizda/sfx_udalosti.json` → `media/projekty/004-bmw-jizda/zvuk/`:
`sfx.wav|json`, `sfx_log.txt`, **`zvuk_v1.wav`**, **`zvuk_bez_hudby_v1.wav`**, `zvuk_v1_master.m4a` (kontrola), spektrogramy. `hudba.wav` ani časování se nemění. Příkaz:
`python3 -I nastroje/sfx.py --udalosti projekty/004-bmw-jizda/sfx_udalosti.json --delka 30 --out …/zvuk/sfx.wav --hudba …/hudba.wav --mix …/zvuk/zvuk_v1.wav
--bez-hudby …/zvuk/zvuk_bez_hudby_v1.wav --automatika 3.94-3.99:-10:40:10 --automatika 17.75-17.99:-12:30:10 --automatika 18.0-18.04:-4:10:90
--zisk-hudby "16.0:0,17.5:2.5,17.74:2.5,17.75:0" --zisk-hudby "17.98:0,17.99:1.5,18.45:1.5,18.95:0" --saturace 3.99-4.2:4 --saturace 17.99-18.45:6
--saturace 25.99-26.2:4 --ticho 3.955-3.995 --ticho 17.76-17.995 --limiter -1.8`.
- **Nové typy v `sfx.py` (jen přidané, stávající beze změny)**: elektrický pohon i7 bez spalovacího motoru: `ev_prujezd(_tesny/_tichy)` (Doppler tónu dvou motorů
  + hukot pneumatik + vítr), `ev_najezd(_dlouhy)` (stoupající tón pohonu, vrchol na konci, pak utne), `ev_uder` (drop: náraz + závan + „výstřel“ tónu, vrchol na náběhu
  ≈ 2 ms, rezerva ≥ 1,4 dB, C035), `pneu_hukot`, `ponor` (P4), `zaverka` (záblesky 3,5 / 3,75), `kuze` (stisk volantu 17,0), `sterk` (kamení 8,75), `ding` (dosednutí čísla).
- **Rozhodnutí**: (1) nádech dropu 1 = krátké ztlumení hudby −10 dB 3,94–3,99 (švih), nájezd utne 3,95, efekty v 3,955–3,995 nic; (2) nádech dropu 2 −12 dB
  17,75–17,99 podle storyboardu, nájezd utne 17,745; (3) stoupání: hudba 16,0 → 17,5 +2,5 dB; (4) drop 2: hudba +1,5 dB (náběh schovaný v nádechu) a pod úderem
  krátce −4 dB (návrat 90 ms), aby byl úder slyšet (I3), měkké nasycení špiček na 4,0 / 18,0 / 26,0, limiter −1,8 dBFS; (5) tikání číslic na šestnáctinách / dvaatřicetinách
  (686: 6,5625–7,1875, 500 kW: 19,125–19,5, 3.8 s: 21,3125–21,6875, 250 km/h: 22,0625–22,5) = **návrh**, animátor naváže změny číslic, nebo se SFX posunou;
  (6) W (8,25 / 9,0): panorama podle střihače doprava (vůz jede od kamery doprava), časy beze změny; (7) mezi událostmi bez souvislého podkladu (ticho pod hudbou).
- **Naměřeno**: vrcholy 101/101 přesně na událostech (0,0 ms, ve stopě odchylky jen tam, kde se překrývá sousední zvuk: 4,15 / 6,5625 / 8,0 / 8,25 / 17,0 / 18,1 / 18,25 / 22,6 / 26,0);
  klíčové efekty proti hudbě (100 ms): drop 1 −1,9 LU, drop 2 −2,0 LU, logo −3,7 LU; žádný efekt hlasitější než hudba (max −1,5 LU / 100 ms, −2,9 LU / 400 ms).
  Master po AAC **−13,8 LUFS / −1,4 dBTP**. Pásma masteru: sub 19,8 % · basy 31,3 % · **středy 36,6 %** · 2–6 kHz 8,1 % · výšky 4,2 %.
  RMS 50 ms (max v půlsekundě, dB): jízda 4,5–12 −13,1 až −15,8 · salon −17 až −19 · **stoupání 16,0 −17,2 → 16,5 −15,1 → 17,0 −13,6 → 17,5 −10,7** · nádech 17,75 −20,9 ·
  **drop 2 18,0 −7,9 (nejhlasitější)** · jízda 18,5–25,5 −10,2 až −13,7 · logo 26,0 −9,1 · drop 1 4,0 −10,4.
- **Pro režiséra / spojení**: SFX po stavbě obrazu posunout na skutečné časy (karty, pilulky, tikání, průjezdy 8,25 / 22,8 podle polohy vozu). Verze bez hudby zůstává v úrovni
  mixu efektů (−23 LUFS), master obrazu dělat ze `zvuk_v1.wav`.

## Zvuk v2 (zvukař, kolo 1 oprav, 2026-11-01)
Nález kritika: průjezd 22,8 neodpovídal obrazu (vůz v D_3008 opouští obraz doleva už 22,0–22,12). SFX posunuty na skutečné časy podle `scena/ui.js`
(CASY, ease-out cubic rolování) a snímků `render/V004_obraz_v1.mp4` (výřezy karet po 1/60 s). Stejný příkaz jako v1, jen výstupy `sfx_v2.*`, `zvuk_v2.wav`,
`zvuk_bez_hudby_v2.wav`, `zvuk_v2_master.m4a`, `sfx_log_v2.txt`, `spektrogram_v2.png`. Hudba i časování beze změny. 98 událostí (bylo 101).
- **Průjezd T12**: 22,8 → **22,05** (od 21,9, panorama 0,2 → −0,9 doleva, `konec` 22,5 = kosinový doběh do střihu na W_900, jinak by končil tvrdě v 22,55).
  Na W_900 (22,5–23,0, vůz klidně jede) žádný průjezd.
- **Dosednutí čísel = první ostrý snímek**: 686 7,25 → 7,23 · 500 kW 19,6 → 19,58 · 3.8 s 21,75 → 21,68 · 250 km/h 22,6 → 22,55.
- **Tikání číslic** už ne po šestnáctinách, ale na skutečných přenosech číslic (sloupec desítek, u 3.8 jednotek), rozestup ≥ 50 ms:
  686 10× 6,56–7,10 · 500 7× 19,13–19,46 · 3.8 4× 21,28–21,59 · 250 6× 22,07–22,39 (první tři schová průjezd).
- **Odchody karet** jednotně na začátek odchodu: 500 kW 19,875 → 19,76, nově tick 22,8 (odchod karty 250).
- **C_2376 (20,5)**: příď vlevo, vůz jede doleva → panorama průjezdu otočeno na 0,5 → −0,5 (bylo zleva doprava).
- **Naměřeno**: vrcholy 98/98 přesně (0,0 ms); master po AAC **−13,8 LUFS / −1,6 dBTP**; pásma sub 19,9 · basy 31,0 · **středy 36,7** · 2–6 kHz 8,2 · výšky 4,0 %;
  RMS 50 ms: stoupání 16,0 −16,2 → 16,5 −15,4 → 17,0 −11,1 → 17,5 −9,9 · **drop 2 18,0 −8,2** · jízda 18,5–25,0 −10,9 až −13,8 · logo 26,0 −9,9 · drop 1 4,0 −10,6;
  nejhlasitější efekt proti hudbě −1,5 LU / 100 ms. Mix se proti v1 liší jen v 6,56–7,7 a 19,1–23,3 s.

## Zvuk v3 (zvukař, kolo 2 oprav, 2026-11-01)
Nález kritika: karta 686 zněla na časech z v1, ale obraz v2 ji má celou v J_5232 (6,0–7,0, `ui.js` U_karta686: linka 6,14 · karta 6,25 · roll 6,25–6,72 ·
lišta 6,72 · odchod 6,84) a v 7,0–8,0 je W_1788 (těsný průjezd bokem). Stejný příkaz jako v1/v2, výstupy `sfx_v3.*`, **`zvuk_v3.wav`**, **`zvuk_bez_hudby_v3.wav`**,
`zvuk_v3_master.m4a`, `sfx_log_v3.txt`, `spektrogram_v3.png`, `spektrogram_bez_hudby_v3_5.8-8.2.png`. Hudba i časování beze změny. 94 událostí (bylo 98).
- klik 6,0 → **6,14** (bod vyskočí 6,12, linka 6,14) · sklo_pop 6,5 → **6,25** · ding 7,23 → **6,72** (stovky dosednou na 6 + lišta), doznění utne do střihu 7,0 ·
  detent 7,75 → **6,84** (odchod karty, o 2 dB silnější, aby vystoupil z doznění dingu, utne 7,0).
- **Tikání 686** podle `polohySloupcu` (roll 6,25–6,72, sloupce dosedají zprava doleva): místo 10 tiků přes střih 5 tiků **6,309 / 6,394 / 6,461** (stovky 1→2, 3→4, 4→5)
  **· 6,532** (jednotky dosednou) **· 6,626** (desítky dosednou), rozestup ≥ 50 ms od sklo_popu i dingu; po 6,72 už žádný tik.
- **Nově 7,15 `ev_prujezd_tesny`** (náběh přesně na střihu 7,0, vrchol 7,15 = střed boku před kamerou, panorama −0,4 → 0,8, vůz jede doprava; doběhne 7,55, záď ujede ~7,6), −6 LU.
- **Naměřeno**: vrcholy 94/94 přesně (0,0 ms, změněné události ve stopě ≤ 0,2 ms); master po AAC **−13,8 LUFS / −1,6 dBTP**; pásma sub 19,8 · basy 31,0 · **středy 36,7** ·
  2–6 kHz 8,2 · výšky 4,0 % (bez varování); RMS 50 ms: stoupání 16,0 −17,4 → 16,5 −15,2 → 17,0 −13,5 → 17,5 −10,4 · **drop 2 18,0 −7,9** · jízda 18,5–25,5 −12,4 až −13,8 ·
  logo 26,0 −9,4 · drop 1 4,0 −10,5 · 6,0–8,0 −13,9 až −15,6; nejhlasitější efekt proti hudbě −1,5 LU / 100 ms (4,15, beze změny). Mix se proti v2 liší jen v 6,0–7,8 s.

## Oprava režiséra v4 (2026-11-01, bez agentů)
- **Záběr 22,0–22,5**: L_0816 (tisk 8,16–8,76 = zakázané úseky 7,08–8,25 a A) vyřazen. Náhrada **B_1280** = tisk 12,80–13,40 (15 snímků, 1,2×), konec průletu
  nad střechou před střihem zdroje 13,52: černé sklo, hrana střechy, silnice ubíhá v silném rozmazání. **Zrcadleno** (bez textu, SPZ a log), aby karta
  vlevo nahoře ležela nad silnicí, ne nad vozem. Úsek 12,80–13,52 nebyl v rozpisu ani v zakázaných (B končil 12,80); ověřeno po snímcích po 0,04 s.
  Navazuje na C_2232 (střecha shora) a D_3008 (průjezd v protisvětle). Prohledané a zamítnuté kandidáty: web 24,5–28 (kolo zblízka, pomalé, jiná kola),
  web 31,6–33,4 (město, maska ledvinek z boku), tisk 34,6–37,56 (čelní příjezd), 51,44–52,3 (dron bez vozu), X_0448 0–27 (bez vozu).
- **Karta 686**: růst 0,22 s, obsah 6,26–6,32, rolování 6,26–6,44, lišta 6,44, odchod 6,91 → „686“ čitelné od ~6,36 do 6,877 (~0,5 s, bylo ~0,38 s).
- **Karta 21″**: odchod `odK` 0,15 → 0,10 (prázdný obdélník nejvýš 2 snímky).
- **Zvuk v4** (`sfx_udalosti.json`, 93 událostí, stejný příkaz jako v1, výstupy `zvuk/sfx_v4.*`, `zvuk_v4.wav`, `zvuk_bez_hudby_v4.wav`, `zvuk_v4_master.m4a`,
  `sfx_log_v4.txt`; starší verze přesunuty do `zvuk/predchozi/`, C039): detent 21″ 3,0 → 2,8 · 686: sklo_pop 6,19, tiky 6,265 / 6,327 (přenosy stovek
  z funkce rolování), ding 6,38, detent 6,91 · 3.8 s shora: tiky 21,275 / 21,328 / 21,386 / 21,452 / 21,529 (přenosy 9→8 … 5→4), ding 21,64 (4→3) ·
  nový `vzduch` 22,1 (lu −13, průlet nad střechou) · `ev_prujezd` 22,05 → **22,52** (skutečný průjezd D_3008 22,5–22,62, lu −5, doběh do 23,0) · ding 250 22,55 → 22,6.
  Naměřeno: vrcholy 93/93 přesně (0,0 ms), master po AAC **−13,8 LUFS / −1,6 dBTP**, limiter mixu max 1,6 dB.
- Render `render/V004_obraz_v4.mp4` (stejný příkaz jako v3, 824 s výpočtu), `vystup/V004_v4.mp4` + `_bez_hudby` + plakát (2,6 s), `kontrola.sh` bez nálezů
  (žádné zamrzlé ani černé úseky, 1800 snímků).

## Průběh výroby
| kolo | kdo | co se dělalo | verdikt kritika | hlavní nálezy |
|---|---|---|---|---|
| příprava | analytik → animátor test → kreativní ředitel → oponent (revize) | materiál BMW, test jízdy, koncept „Bod, který nepustí vůz“ | oponent: původně jízda 7 / realismus 6 / energie 7,5 → po revizi odhad 9 / 9 / 9 | vyřazeny záběry s čelními chromovými ledvinkami (A 8,30, dron E), drop 2 silnější, ponor do střechy skutečnou kamerou |
| výroba | zvukař ∥ střihač (32 záběrů) → animátor klíčové snímky (neschváleno 7,6) → blok 1 s opravami → blok 2 + render + zvuk | render v1, mix v1b (elektrický motiv, režisér) | – | – |
| 1 | kritik · kreativní ředitel | kontrola V004_v1 | kritik **BLOKUJÍCÍ** (bod na karoserii 7,4–8,0), wow 7,3 / jízda 7,5 / realismus 7,5 / energie 7 | opakovaný záběr X_0448, ozvěny číslic (C040), slabý výbuch stop dropu 2, statický úvod 1,5–3,9 a end card, 250 km/h nad prázdnou silnicí, hrana rendru 10,5 |
| 2 | kritik · kreativní ředitel | kontrola V004_v2 (bod mimo karoserii, X_0448 jen jednou, číslice bez ozvěn, drop 2 svazek stop, úvod se záblesky jízdy) | wow 7,9 / jízda 8 / realismus 8 / energie 7,5, **BLOKUJÍCÍ: zrychlení roluje zdola (0,0 → 3,8), proti pokynu režiséra G9** | 250 km/h na už viděném záběru, statická end card, karta 686 krátká, prázdné obdélníky při odchodu karet |
| 3 | kritik · kreativní ředitel | kontrola V004_v3 (zrychlení shora 9.9 → 3.8, nový záběr 22,0–22,5, karta 686 větší, odchody karet) | KŘ **SCHVÁLENO** wow 8,2 / jízda 8,5 / realismus 8 / energie 8; kritik **BLOKUJÍCÍ**: nový záběr L_0816 (22,0–22,5) je ze zakázaného úseku A (aero kolo i7 60, lamely ledvinek) | zvuk nesedí na nový střih (průjezd 22,05), tiky 3.8 ze starého rolování, 686 jen ~0,4 s, prázdný obdélník karty 21″ 3 snímky |
| oprava režiséra (v4) | režisér sám, bez agentů | L_0816 → B_1280 (tisk 12,80–13,40, průlet nad střechou, zrcadleno, karta nad silnicí); karta 686 rychlejší růst a rolování (klid ~0,5 s); karta 21″ odchod 0,10; SFX přepočítané z funkce rolování (686, 3.8 shora), průjezd 22,52 na skutečný průjezd D_3008, vzduch 22,1, ding 250 22,6; render + master + kontrola | vlastní kontrola po snímcích (viz Verze) | – |

## Kolo 4 a oprava v4b (2026-11-01)
- **Kolo 4** (2 agenti, jen opravená místa + regrese): KŘ **SCHVÁLENO wow 8,3 / jízda 8,7 / realismus 8,2 / energie 8,2**; kritik **OPRAVIT** (nic blokujícího).
  Regrese: obraz mimo ohlášená místa bit po bitu shodný s v3 (oba agenti nezávisle). Nálezy: G9 ≥ 0,5 s porušují i karty 500 / 3.8 / 250 (závažná),
  dingy 250 a 500 mimo dosednutí (závažná), B_1280 připomíná B_1220 z 11,95 zrcadlově, hvězda odlesku (KŘ závažná), slabý zvuk nového záběru, sklo_pop 686 o 43 ms dřív.
- **Odpovědi režiséra na otázky**: (1) G9 „2 snímky“ platí pro plně krycí prázdný obdélník, stažení do bodu se nepočítá (pravidlo upřesněno);
  (2) ding 250 na 22,6 byl chyba režiséra (C047), patří na dosednutí; (3) G9 platí pro všechny karty → opraveno; (4) B 12,80–13,40 zapsán do čistých úseků;
  (5) verze bez hudby je záměrně jen stopa efektů v úrovni mixu (−23 LUFS), nenormalizovaná.
- **Oprava v4b (režisér)**: karty 500 kW (karta 19,06, růst 0,3, roll 19,08–19,30), 3.8 s (karta 21,06, roll 21,12–21,42), 250 km/h (roll2 22,0–22,3) a 686 (odchod 6,93,
  odK 0,07) → klid hotové hodnoty ≥ 0,5 s všude. Střih 22,0: švih podél diagonály silnice (C_2232 21,95–22,0 a B_1280 22,0–22,1, `svihSmer`, ≤ 130 px), záblesk +0,6 EV
  2 snímky, hvězda odlesku ztlumena −1,3 EV měkkou maskou (polohy změřené v sekvenci, do 22,3). Zvuk v4b (82 událostí): tiky a dingy z funkce rolování
  (500: 19,088 / 19,153, ding 19,21 · 3.8: 21,135 / 21,202 / 21,288, ding 21,35 · 250: 22,059 / 22,112, ding 22,17), sklo_pop 686 6,233, detent 686 6,93, švih 22,0,
  vzduch jako nápor 22,0 → vrchol 22,4 (−5 LU, panorama zleva doprava), hudba −2 dB 22,0–22,45 (`--automatika 22.0-22.45:-2:20:40`), průjezd 22,52 beze změny.

## Kolo 5 a oprava v4c (2026-11-01)
- **Kolo 5** (2 agenti, jen místa opravená ve v4b + regrese): KŘ **SCHVÁLENO wow 8,3 / jízda 8,8 / realismus 8,0 / energie 8,4**; kritik **OPRAVIT**.
  Regrese: mimo 6,15–7,0, 18,9–20,0, 20,92–22,8 bit po bitu shodné s v4. Shodný hlavní nález obou: maska ztlumení odlesku dělá na písku tmavou skvrnu (C048).
  Kritik dále: dingy na posledním přenosu, ne na ustálení (−50 až −97 ms); 500 kW ustálené 0,43–0,47 s; popisek 686 přečnívá nad tvar v podsnímcích 376–377
  (od v4); tik 500 před viditelnou kartou; detent 500 o 27 ms pozdě; schodovitý obrys při nástupu karet 500 / 3.8. KŘ: stupňování zvuku k 250 slabé
  (hudba ztlumená během švihu), švih tichý.
- **Odpovědi režiséra**: (1) „první ostrý snímek“ = první **ustálený** snímek (pravidlo G9 upřesněno); (2) popisek 686 opravit hned; (3) odlesk: ani ztlumení
  jasu, ani razítko neprošly kontrolou výřezu 1:1 (díra s prstencem, tmavý kotouč, zub hrany) → hvězda se jen měkce rozostří uvnitř skla; (4) v4 ani v4b
  uživatel nedostal, doručí se až konečná verze.
- **Oprava v4c (režisér)**: odlesk = `rozostriOdlesk` (blur 14 px, měkký kruh r 70, snímky 0–5, slábne 22,15–22,2); karta 500 roll 19,08–19,27 a odchod 19,80;
  obsah 686 až 6,29–6,34; podsnímky 8 i v nástupech karet (6,15–6,35 · 19,05–19,25 · 21,05–21,2). Zvuk v4c (85 událostí): dingy na ustálení (686 6,40 · 500 19,27 ·
  3.8 21,417 · 250 22,25), tiky 500 jen viditelné (19,17 / 19,22), + tik 21,35 a 22,163, detent 500 19,77, nádech hudby 21,88–22,0 −3 dB místo ztlumení
  během švihu, švih 22,0 +3 dB + nízký úder `fump`, vzduch +2 dB, průjezd +2 dB (−6 dBFS jako průlet 18,1).

## Kolo 6 a oprava v4d (2026-11-01)
- **Kolo 6** (2 agenti): KŘ **SCHVÁLENO wow 8,4 / jízda 8,8 / realismus 8,3 / energie 8,5** (odlesk působí jako přirozené světlo, stupňování zvuku k 250 funguje);
  kritik **OPRAVIT**: karta 686 klid 28 snímků (první ustálený 386), ding 686 o 2 snímky dřív; drobné: popisek 500 / 3.8 přečnívá 1 snímek nad tvar,
  tik 3.8 21,135 před viditelnými číslicemi, průjezd 22,52 málo vyčnívá nad zesílený vzduch. Regrese proti v4b žádná. Odlesk prošel u obou.
- **Odpovědi režiséra**: platí přísné čtení „první ustálený snímek“; popisky 500 / 3.8 opravit stejně jako 686; ding tolerance ±1 snímek; kontrast průjezdu = zvuk, ne vkus.
- **Oprava v4d (režisér)**: 686 roll 6,26–6,41 (ustálení ~6,39–6,40 → klid 30 snímků, ding 6,40 sedí); obsah karet 500 (19,15–19,21) a 3.8 (21,15–21,21) se odkrývá
  s tvarem; rozostření odlesku plynule 14 → 0 px 22,1–22,2 (místo slábnutí, KŘ); zvuk v4d (84 událostí): tik 21,135 vypuštěn, vzduch vrchol 22,32, konec 22,46, lu −5
  → krátké ztišení před průjezdem 22,52 (RMS 40 ms: 22,36–22,44 ≈ −12,4 dB → průjezd −9,3 dB).

## Kolo 7 a doručení (2026-11-02)
- **Kolo 7** (1 agent, kritik, jen opravená místa v4d + regrese proti v4c): **SCHVÁLENO**, regrese žádná. Drobné: karta 686 se v 386 přerastruje o 0,4 px
  (při prahu pohybu < 0,5 px je první ustálený 384 → klid 30 snímků, ding 6,40 přesně); průjezd 22,52 +3 dB nad ztišením před ním, +1,6 dB nad vrcholem vzduchu;
  686 se odkrývá až po tvaru (3 snímky prázdný tvar při nástupu).
- **Rozhodnutí režiséra**: „ustálený snímek“ = pohyb číslic < 0,5 px (stejně jako u 3.8 v kole 6, zapsáno do G9); kontrast průjezdu nad ztišením stačí;
  nástup 686 nechat (G9 omezuje prázdný obdélník jen při odchodu). Další kolo by podle laťky nic nepřidalo → **doručit v4d**.
- Konečné hodnocení: KŘ (kolo 6) **wow 8,4 / jízda 8,8 / realismus 8,3 / energie 8,5**, kritik (kolo 7) SCHVÁLENO.

## Chyby během výroby
Zapsáno v `znalosti/chyby.md`: **C042** motiv V8 v hudbě elektromobilu (→ `--motor elektricky`) · **C043** animátor dvakrát nedodržel pokyn režiséra
(opakovaný X_0448, zrychlení zdola) · **C044** náhradní záběr ze zakázaného úseku (L_0816) · **C045** zvuk nesledoval změny obrazu v opravném kole ·
**C046** karta 686 krátká, prázdný obdélník karty 3 snímky · **C047** ding posunutý z dosednutí · **C048** retuš odlesku udělala skvrnu. Další nálezy kritiků (bod na karoserii v1, ozvěny číslic, hrana rendru 10,5, slabý drop 2)
opraveny v kolech 1–2 podle stávajících pravidel (G7, G8, C040).

## Spotřeba tokenů
| agent / úkol | tokeny | akce nástrojů | čas |
|---|---|---|---|
| workflow podklady (2 agenti: analytik materiál, animátor test) | 446 446 | 214 | 61,6 min |
| workflow koncept (2 agenti: kreativní ředitel, oponent s revizí) | 451 382 | 110 | 31,4 min |
| workflow výroba (16 agentů: střihač, zvukař ×3, animátor ×5, kreativní ředitel ×4, kritik ×3) | 3 248 216 | 1 111 | 224 min |
| režisér: oprava v4 (záběr, karty, posuny SFX, render, master, kontrola) | neměřeno (hlavní chat) | – | – |
| workflow kolo 4 (2 agenti: kritik, kreativní ředitel) | 275 046 | 99 | 11,3 min |
| workflow kolo 5 (2 agenti: kritik, kreativní ředitel) | 311 587 | 114 | 11,8 min |
| workflow kolo 6 (2 agenti: kritik, kreativní ředitel) | 243 323 | 94 | 11,9 min |
| workflow kolo 7 (1 agent: kritik) | 178 666 | 76 | 17,6 min |
| **součet pomocných agentů (27)** | **5 154 666** | **1 818** | **369,5 min** |

## Verze
| verze | datum | soubor / kam doručeno | změny |
|---|---|---|---|
| v1 | 2026-11-01 | V004_v1.mp4 (interní) | první render, blokující bod na karoserii; wow 7,3 / jízda 7,5 / realismus 7,5 / energie 7 |
| v2 | 2026-11-01 | V004_v2.mp4 (interní) | bod mimo vůz, bez opakování X_0448, svazek stop; blokující zrychlení zdola; 7,9 / 8 / 8 / 7,5 |
| v3 | 2026-11-01 | V004_v3.mp4 (interní) | zrychlení shora, karty; KŘ schválil 8,2 / 8,5 / 8 / 8, kritik blokující L_0816 |
| v4 | 2026-11-01 | V004_v4.mp4 (interní) | oprava režiséra: B_1280 místo L_0816, karta 686, odchod karty 21″, zvuk podle obrazu; KŘ 8,3 / 8,7 / 8,2 / 8,2, kritik OPRAVIT (G9 u všech karet) |
| v4b | 2026-11-01 | V004_v4b.mp4 (interní) | G9 u všech karet, švih do 22,0, dingy; KŘ 8,3 / 8,8 / 8,0 / 8,4, oba: skvrna po masce odlesku |
| v4c | 2026-11-01 | V004_v4c.mp4 (interní) | odlesk rozostřením, dingy na ustálení, nádech hudby; KŘ 8,4 / 8,8 / 8,3 / 8,5, kritik OPRAVIT (686 o 2 snímky) |
| **v4d** | 2026-11-02 | **V004_v4d.mp4 → uživateli** + `_bez_hudby`, plakát 2,6 s (`V004_plakat.jpg`), `popisek.txt` | 686 klid 30 snímků, odkrytí obsahu karet, kontrast průjezdu; kritik SCHVÁLENO |

## Zpětná vazba (doslova)

## Poučení
