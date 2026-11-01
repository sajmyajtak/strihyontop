# V004: BMW řady 7: realistická reklama s jízdou (sport luxus, SaaS motion graphics)

| | |
|---|---|
| Datum zadání | 2026-11-01 |
| Platforma / formát | **16:9, 1920×1080, 60 fps** |
| Délka | **30,0 s** |
| Stav | příprava: koncept a storyboard hotové (kreativní ředitel), čeká na oponenturu |

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
  sekundy, roztočí jeho kolo, které se střihem na drop změní ve skutečnou jízdu, na záběrech jízdy vede linku ke kartě s faktem, v salonu
  ukazuje detaily, ve stoupání skáče mezi dlaždicemi, na dropu 2 se rozprskne do světelných stop rychlosti a na konci se rozevře v bílou clonu
  a poskládá logo BMW. Nikdy neleží na karoserii, vždy vedle vozu (stín, silnice, podlaha).
- **Materiál**: **skutečná jízda** = tiskový film `press_PF0010152` (stříbrná i7 60, high-key grade, 1,2× nebo 2,4× + zdvojení snímků, jen úhly
  shora / zezadu / bokem v rozmazání / dron / u kola); **náš vůz** (Alpine White i7 M70, černá M maska, 909 M) = rendry konfigurátoru ve studiu
  (odhalení, světla, kolo, tvář s M maskou, salon); salon navíc tmavá videa kokpitu bmw.cz **v dlaždicích** (720p se tak nezvětšuje);
  **SaaS** = bod, linka, karty, pilulky, dlaždice, typografie (Manrope, `media/projekty/004-bmw-jizda/znacka/znacka.css`).
- **Podíl jízdy**: celoobrazová skutečná jízda 4,0–10,0 + 11,0–12,0 + 18,0–23,5 + 25,0–25,75 = **13,25 s = 44 %** (kritérium 2), k tomu jízda
  v dlaždicích mřížky (16,0–17,0) a uvnitř písmen (23,5–25,0) → vůz v pohybu na obrazovce ~15,5 s = 52 %. 2,5D jízdu z rendru (test B) **nepoužíváme** (koláž).
- **Použitá pravidla**: B1 + B6 (snímek 0 = náš vůz v šeru + nadpis + bod), C7 (událost na každou dobu), D2 + D7 (záběr vzniká z předchozího,
  rozsvícení = rozdíl rendrů zap − vyp), F4 / F7 (pružina 3 % jen UI, kamera kriticky tlumená, jedna kamera), G7 (vůz jen skutečný, nic přes vůz),
  G8 (karty 1 px `#e6e6e6`, dvouvrstvý stín, akcent `#1c69d4` jen na aktivním prvku), I3 (klíčové údery slyšet, nádech 17,75 = hudba ztichne), C8 (fakta doslova).
- **Texty (anglicky, vždy jen jedna vrstva, bez tečky)**: „THE NEW i7 M70“ · karta „21″ M wheels / 909 M“ · „Electric range (WLTP) / 686 km“ ·
  pilulka „BMW Iconic Glow kidney grille“ · „BMW Panoramic Vision“ · „CraftedClarity glass applications“ · „BMW Individual Merino Black leather“ ·
  „M sport leather steering wheel“ · „Power / 500 kW“ · „0–100 km/h / 3.8 s“ · „Top speed / 250 km/h“ · „i7 M70“ (maska) · end card
  „THE NEW BMW i7 M70 xDRIVE“ + disclaimer. Názvy výbavy = překlad doslovného znění z konfigurátoru (`katalog.md` oddíl 0). Karty: popisek
  Manrope 500 22 px `#8e8e8e`, hodnota Manrope 300 72 px `#262626`, jednotka 500 32 px `#8e8e8e`, modrá lišta `#1c69d4` jen při dosednutí čísla.
- **Grade**: stopáž `eq=saturation=0.7` + teplé výšky + zvednutá světla (test A „high-key“), rendry studia lehce dorovnat k témuž (teplota výšek,
  kontrast, jemné zrno stejné velikosti na všem), aby střih render ↔ stopáž neskákal v barvě.

## Storyboard / časová osa
Kreativní ředitel, 2026-11-01. Hudba `hudba.json` (120 BPM, doba 0,5 s, takt 2,0 s). **Zdroj jízdy** = `press_PF0010152_sceneId20103_preview.mp4`,
čas „src“ = čas ve zdrojovém souboru (titulní karta 0–4,3 s se nepoužívá). Rychlost **1,2×** (výstup d s = zdroj 1,2·d s) nebo **2,4×** (zdroj 2,4·d s),
uvnitř jednoho záběru se rychlost nemění. **Hranice záběrů zdroje** (ffmpeg scdet): 4,48 · 7,08 · 9,28 · 13,52 · 18,2 · 21,68 · 25,0 · 28,08 · 30,6 · 34,6 · 37,56 · 40,28 · 42,08 · 44,44 · 51,44.
**Čisté úseky** (ověřeno snímky na začátku, uprostřed a na konci, bez čelního pohledu s chromovými ledvinkami): A 8,30–9,20 u kola · B 11,00–12,80 let nad kapotou ke střeše · C 21,70–24,95 záď 3/4 → střecha shora → nakloněný bok · D 28,60–30,55 silnice v protisvětle, vůz v dálce · E 30,65–34,55 dron nad vozem (ledvinky jen shora a malé, povoleno jako „dron“, test C) · F 39,97–40,27 průlet těsně kolem kamery · G 40,30–42,05 sledovací záběr zezadu shora · H 44,50–45,40 kamera přelétá těsně nad střechou · I 50,80–51,40 průjezd bokem, záď odjíždí z obrazu · J 52,30–55,85 dron nad pobřežím, vůz malý.
**Zakázané**: 7,08–8,25 · 9,28–10,95 · 13,52–21,65 · 25,0–28,05 · 37,56–39,95 · 42,08–44,45 · 45,45–50,75 (čelní pohledy). Každý úsek se ve videu použije nejvýš jednou (kromě malých dlaždic mřížky a výplně písmen).

| čas (takt · doba) | záběr: zdroj a čas ve zdroji | pohyb a střih | SaaS grafika / text | zvuk / událost |
|---|---|---|---|---|
| **0,0–2,0** (T1 · 1–4) **probuzení** | `360_svetla_vyp/uhel_030` → `360_svetla_zap/uhel_030` (náš M70, 3/4 předek, příď vlevo), měřítko 0,80 (≤ nativní), vůz ≥ 75 % šířky; celý obraz −1,2 EV („studio před rozsvícením“) | **snímek 0 hotový**: tmavší studio, bílý vůz čitelný. Dotlačení 1,00 → 1,04 nepřetržitě. **0,5** ledvinky Iconic Glow se rozsvítí (rozdíl zap − vyp jen v oblasti ledvinek, maska ze středu ven 0,12 s, zisk rozdílu ×1,8). **1,0** světlomety (zbytek rozdílu). **1,0–1,5** studio se rozsvítí na plnou expozici (globální expozice, smootherstep 0,4 s). **1,5** rychlý oblouk otočky `uhel_030 → 090` (6 snímků za 0,25 s, směrové rozmazání mezi sousedy) + dotlačení na přední kolo | snímek 0: **„THE NEW i7 M70“** vlevo nahoře (Manrope 300, 88 px, bílá, bezpečná zóna), na 0,5 / 1,0 řez skočí 300 → 800 a prostrkání +6 % → −1 % (jeden objekt, souravbhar871). Bílý **bod** (14 px, modrý střed `#1c69d4`) na podlaze před předním kolem od snímku 0, na 1,0 krátce pulzne (kroužek 0,3 s). Nadpis odchází 1,4–1,5 maskou zdola (ease-in) | tlumený kopák 0,0 + klavír · lusknutí 0,5 = „cink“ rozsvícení ledvinek (sklo) · 1,0 nízký hukot světel · 1,5 lusknutí + krátký švih oblouku |
| **2,0–4,0** (T2 · 1–4) **kolo 909 M** | `360_svetla_zap/uhel_090` výřez 1,0× nativně (1920 z 2560) na přední kolo: střed ráfku (576, 993) zdroje → obraz (≈ 620, 700), r ≈ 146 px = stejná velikost jako kolo ve stopáži src 8,30 | 2,0–3,0 kolo stojí, kamera klouže doleva 40 px (směr budoucí jízdy). **3,0–3,94** kolo se roztáčí (sprity `test/podklady/kolo0_ostre/rozmaz`, rotační rozmazání podle úhlové rychlosti, valení zrychluje ease-in), dotlačení 1,00 → 1,08; studio stojí (vůz „na místě před startem“). **3,75–3,94** vodorovné světelné stopy v pásu podlahy a stěny (ne přes vůz), **3,94–4,0** švih: vodorovné směrové rozmazání celého obrazu doleva (4 snímky) | **2,0** bod na podlaze pod pneumatikou → linka 1 px se zářícím hrotem vede doprava nahoru → karta **„21″ M wheels“ / „909 M“** (pružina 3 %, roste z konce linky) v pravé horní třetině na stěně studia. **3,0** karta se stáhne do linky a bodu (ease-in). Bod zůstává na podlaze a s roztáčením kola se natahuje do krátké vodorovné stopy | tlumený kopák 2,0 / 2,5 · 2,0 měkký klik karty · **3,0–3,94 elektrický nájezd motoru (stoupající tón) + vír bubnu z hudby** · 3,0 karta odchází „tick“ · obrácený činel do 4,0 |
| **4,0–6,0** (T3 · 1–4) **DROP 1: jízda** | **4,0** A src 8,30–8,90 (nízko u předního kola, bok, příď vlevo; výřez 1,08× posunutý doprava, aby světlomet a hrana ledvinek zůstaly mimo obraz) · **4,5** C src 23,75–24,35 (nakloněný průjezd bokem) · **5,0** F src 39,97–40,27 (průlet těsně kolem kamery, 0,25 s) · **5,25** G src 40,30–40,90 (hned zezadu shora: vůz, který právě prolétl, ujíždí) · **5,75** H src 44,50–44,80 (kamera přelétne nad střechou, 0,25 s) | **4,0 match cut kolo → kolo** (viz Přechody P1): střed a velikost kola sedí, rotace pokračuje, z ateliéru je silnice. Tvrdé střihy na doby, 5,0–6,0 zrychlení na **čtvrtdoby** (F → G je jedna akce: průlet a hned pohled za vozem). Směr pohybu na obrazovce doleva / od kamery (jeden směr = jedna jízda). 2 snímky expozice +12 % na 4,0 (záblesk na úder, C028 ověřit se závěrkou) | bez textu (čistá rychlost). Bod není (první dávka jízdy bez UI) | **úder + činel 4,0** (nejhlasitější dosud) · průjezd 4,5 (whoosh vlevo) · **5,0 průlet těsně kolem (Doppler, vrchol 5,05)** · 5,25 kopák · 5,75 vzduch nad střechou · hi-hat osminy z hudby |
| **6,0–8,0** (T4 · 1–4) **dojezd** | **6,0** J src 52,30–54,70 (dron nad pobřežní silnicí, vůz malý jede po oblouku, moře nahoře), jeden záběr 2 s, **7,0 punch-in** výřez 1,00 → 1,15 tvrdě na kopák (nový rámec) | 6,0 tvrdý střih, dron klesá (ze zdroje), digitální dotlačení 1,00 → 1,03; 7,0 punch-in 1,15 (≤ 1,15× kvůli 1080p zdroji), karta stojí na místě, bod a linka se přepočítají na nový výřez | **6,0** bod na silnici vedle vozu (klíčové snímky polohy vozu po 0,25 s, bod ve stínu / na asfaltu, ne na laku) → **6,25** linka se zářícím hrotem → **6,5** karta **„Electric range (WLTP)“ / „686 km“** nad mořem vpravo nahoře, číslice rolují 6,5–7,25 (automat, sloupce 0–9, dosednou přesně na 686), **7,25** modrá lišta pod číslem. 7,0 linka se po punch-inu natáhne k bodu (bod dál na silnici vedle vozu). **7,75–8,0** karta odchází do linky a bodu | kopák na doby · 6,0 klik · 6,5–7,25 tiché tikání číslic · 7,25 „ding“ dosednutí (sklo, tiše) · 7,0 punch-in = kopák · 7,75 tick odchodu |
| **8,0–10,0** (T5 · 1–4) **jízda** | **8,0** B src 11,00–11,60 (kamera letí nad kapotou → čelní sklo) · **8,5** C src 22,10–22,70 (shora za vozem, střecha) · **9,0** D src 28,60–29,20 (silnice v protisvětle, vůz v dálce) · **9,5** I src 50,80–51,40 (průjezd bokem, záď odjíždí doleva z obrazu) | tvrdé střihy na doby; I končí vozem, který odjede doleva z obrazu → **9,94–10,0** švih doleva (směrové rozmazání 4 snímky) do rendru, viz P2 | bez textu | kopák · 8,0 vzduch přes kapotu · 8,5 kopák · 9,0 vzdálený průjezd · 9,5 průjezd bokem · 9,94 švih (vrchol 10,0) |
| **10,0–12,0** (T6 · 1–4) **tvář M70 → nádech do salonu** | **10,0** `360_svetla_zap/uhel_000` (náš M70 zepředu: černé M ledvinky, Iconic Glow svítí) přijíždí obloukem `060 → 030 → 000` za 0,1 s; **10,5** `g01_predek_den` výřez 1,25× na ledvinky a logo (detail M masky); **11,0** D src 29,30–29,90 (protisvětlo, odraz slunce na asfaltu, vůz projede v rozmazání) · **11,5** C src 22,70–23,30 (střecha shora: černá skleněná střecha velká v obraze) | 10,0 vůz přijede ještě v pohybu (dobrzdí oblouk, dotlačení 1,00 → 1,03). **10,5** tvrdý střih na detail (punch-in na kopák). **10,94–11,0** záře Iconic Glow se na 2 snímky rozzáří (zisk rozdílu zap − vyp ×3) → střih do protisvětla (P3). **11,5–12,0** kamera se **noří do černé skleněné střechy** (digitální zoom 1,0 → 2,4 na střed skla, radiální rozmazání jen ve tmavé ploše, ease-in) → 12,0 tma skla = strop interiéru (P4) | **10,0** pilulka **„BMW Iconic Glow kidney grille“** dole uprostřed (bod vlevo v pilulce, pružina 3 %), 10,25 text odkryt maskou; **10,45** pilulka odchází (text dřív než tvar). 10,5–12,0 bez textu | kopák 10,0 + švih · 10,5 kopák = střih · 10,94 záře „swell“ · 11,0 střih · **11,0–12,0 obrácený činel**, hluboký „ponor“ (vrchol 12,0) |
| **12,0–14,0** (T7 · 1–4) **ZLOM: salon** | **12,0** kostka interiéru (`interier_strop` → `interier_predni`, CSS 3D, FOV ~70°, stěna ~1,17×) · **13,0** deska: dlaždice 1 = totéž (živá kostka), dlaždice 2 = `m7web_g70_lci_mp_interior_cockpit_welcome_dsk_sl.mp4` src 2,0–4,0 (skleněné ovladače CraftedClarity se rozsvítí) | **12,0–12,75** kamera v kostce sklopí pohled ze stropu dolů na palubní desku (rotateX 80° → 0°, kriticky tlumeně), Panoramic Vision a M volant v obraze. **13,0** celý obraz se zmenší do dlaždice (rádius 28, x 96–1004) a odjede doleva, odkryje desku `#f6f6f6` (největší změna měřítka zlomu). **13,25** dlaždice 2 vyjede zdola vpravo (pružina 3 %, stín se zmenšuje s výškou). Kostka v dlaždici se dál pomalu otáčí (rotateY 0 → −12°) | **12,5** bod u spodní hrany Panoramic Vision (na hraně displeje, ne na něm) → linka nahoru → pilulka **„BMW Panoramic Vision“** v ploše čelního skla (pohled ven = světlá stěna studia, ne přes palubní desku). **13,0** pilulka se usadí pod dlaždici 1. **13,5** pilulka přeskočí pod dlaždici 2 a text se uvnitř vymění (vlastní časování odchodu / příchodu): **„CraftedClarity glass applications“** | **činel 12,0**, hudba na klavír, kopák tlumený 12,0 / 13,25 · lusknutí 12,5 = bod · 13,0 měkký swoosh zmenšení · 13,25 kopák = dlaždice · lusknutí 13,5 = sklo „ting“ (rozsvícení ovladačů) |
| **14,0–16,0** (T8 · 1–4) **salon: materiál a volant** | **14,0** dlaždice 3 = `g13_interier_sedadla-bok` (Merino Black, 2,5D dotlačení 1,00 → 1,04) · **14,5** dlaždice 4 = `m7web_g70_lci_mp_interior_cockpit_steering_wheel_dsk_sl.mp4` src 8,0–10,0 (ruce na M volantu za jízdy, noc) | **14,0** dlaždice 3 vyjede zprava, celá deska se posune doleva (kamera jede po desce, jeden směr), **14,5** dlaždice 4 vyjede zespodu. **15,0–15,75** kamera najíždí logaritmicky na dlaždici 4, **15,75–16,0** dlaždice 4 vyplní obraz (rohy se otevřou) | **14,0** pilulka přeskočí k dlaždici 3: **„BMW Individual Merino Black leather“** · **14,5** k dlaždici 4: **„M sport leather steering wheel“** · **15,25** pilulka odchází do bodu, bod zůstane v rohu dlaždice 4 jako „výběr“ | kopák tlumený 14,0 / 15,25 · lusknutí 14,5 / 15,5 · 14,0 / 14,5 měkké kliky dlaždic · 15,0–16,0 swoosh najetí + začátek stoupání |
| **16,0–18,0** (T9 · 1–4) **STOUPÁNÍ: všechno najednou** | **16,0** mřížka 3×3 (dlaždice ~560×315, mezera 32, rádius 20, pozadí `#262626`): (1) volant (pokračuje), (2) C src 24,0 bok, (3) `uhel_090` kolo 909 M, (4) G src 41,2 záď, (5) `m7web_g70_lci_mp_driving_dynamics_overlay_m_sport_boost_shfv.mp4` src 1,0–2,0 (palec na páčce BOOST), (6) J src 53,0 dron, (7) `g13`, (8) I src 50,9 průjezd, (9) `uhel_000` zap tvář · **17,0** dlaždice 5 přes celý obraz | **16,0–16,25** kamera odjede z celého obrazu dlaždice 1 do mřížky (log zoom, kriticky tlumeně). Dlaždice se rozsvěcují po osminách (16,0 / 16,125 / … 16,875 = spiccato), každá s živým záběrem. **16,5 a 17,0** (řazení motoru) mřížka poskočí o 2 % měřítka. **17,0** kamera se vrhne do středové dlaždice 5 (palec, páčka BOOST), 17,0–17,5 přes celý obraz (720p → 1,5×, tma a pohyb, jen 0,5 s). **17,5–17,75** obraz kolem páčky se stáhne do tmy (vinětace se zavře do kruhu) | bod skáče po dlaždicích tak, jak se rozsvěcují (vždy v rohu dlaždice, ne na voze), na **17,0** dopadne do středu (dlaždice 5). **17,75–18,0 NÁDECH**: vše zmizí, zůstane **jen bod** uprostřed černé, bod se smrští na 8 px | **motor nájezd 16,0 → 18,0**, řazení 16,5 / 17,0, vír bubnu, kopák na doby, spiccato osminy · 17,0 klik páčky (cvak) · **17,75–18,0 hudba ztichne** (automatika −12 dB), jen nádech |
| **18,0–20,0** (T10 · 1–4) **DROP 2: rychlost** | **18,0** H src 44,80–45,40 (kamera prolétne těsně nad střechou, vůz pod ní) · **18,5** C src 24,35–24,95 (nakloněný průjezd bokem) · **19,0** E src 33,35–34,55 (dron, vůz malý ujíždí po silnici) | **18,0 bod vybuchne** do svazku vodorovných světelných stop (bílá + `#1c69d4`, směr jízdy doleva, 0,0–0,25 s, pak odletí ven z obrazu), pod nimi hned záběr přeletu (stopy přes celý obraz jen 0,2 s jako přechod, vůz pak čistý). 2 snímky expozice +15 %. Tvrdé střihy na doby, 19,0 dron s dotlačením 1,00 → 1,04 | **19,0** bod u vozu na silnici → linka → karta **„Power“ / „500 kW“** vlevo (na svahu vedle silnice), číslice rolují 19,1–19,6, 19,6 modrá lišta. **19,875** karta odchází do bodu | **úder + činel 18,0 = nejhlasitější místo videa** (I3, C032), stopy = světelný „vzduch“ · 18,5 průjezd · 19,0 řazení + klik karty · 19,1–19,6 tikání · 19,6 ding |
| **20,0–22,0** (T11 · 1–4) **0–100** | **20,0** G src 41,20–41,80 (zezadu shora, vůz v oblouku) · **20,5** B src 12,20–12,80 (let nad střechou dozadu) · **21,0** E src 31,00–32,20 (dron nad vozem, levá třetina volná; test C) | tvrdé střihy na doby, 21,0 dron s dotlačením 1,00 → 1,03 | **21,0** bod vlevo od vozu ve stínu (klíčové snímky z testu C) → linka → karta **„0–100 km/h“ / „3.8 s“** vlevo, číslice rolují 21,25–21,75 (zdola nahoru na přesně 3.8), 21,75 modrá lišta + kroužek | kopák · 20,0 kopák + vzduch · 20,5 řazení · 21,0 klik · 21,25–21,75 tikání · 21,75 ding |
| **22,0–24,0** (T12 · 1–4) **max. rychlost** | **22,0** E src 32,20–33,35 (pokračování dronu, výřez 1,12× = punch-in na kopák) · **23,0** D src 29,90–30,50 (protisvětlo, vůz projíždí) · **23,5** písmena (řádek T13 začíná o dobu dřív) | 22,0 punch-in jako nový záběr; tvrdý střih 23,0; **23,5** přechod do písmen (viz T13) | **22,0** štítek karty se maskou přemění: **„Top speed“ / „250 km/h“**, číslice rolují 22,0–22,6 (nikdy nad 250, C8), 22,6 lišta. **22,875** karta odchází do bodu, bod odjede s vozem | kopák · 22,0 přepnutí štítku (tick) · 22,0–22,6 tikání · 22,6 ding · 23,0 průjezd · 23,5 švih pásů (stereo L/R) |
| **23,5–26,0** (T12 d4 – T13) **i7 M70 → odjezd** | **23,5** písmena „i7 M70“ (Manrope 800, výška ~620 px, přes celou šířku) na `#f6f6f6`, **uvnitř písmen** F src 39,97–40,27 → 24,0 I src 50,80–51,40 → 24,5 H src 44,50–45,10 (opakování povoleno jen tady, v masce písma) · **25,0** J src 54,70–55,60 (dron, vůz malý odjíždí po pobřeží) | **23,5** písmena vjedou rozřezaná na 6 vodorovných pásů, sudé zprava, liché zleva (lukasersil LINE), dosednou na 23,75; 24,0 a 24,5 výměna záběru uvnitř písmen (střih uvnitř masky), 24,0 řez 800 → 700 → 800 „nádech“ písma. **24,75–25,0** kamera proletí otvorem písmene „7“ (měřítko 1 → 9, log), jízda uvnitř se stane celým obrazem = **karta → celý obraz** na 25,0. **25,5–25,75** dron, kamera klesá; **25,75–26,0** clona (P6) | 23,5–25,0 jediný text = „i7 M70“ (maska se stopáží). **25,0** bod u vozu na silnici (bez linky). **25,75** bod se rozevře v **bílý kruh** (clona z bodu přes celý obraz, ease-in, 0,25 s) | kopák · 24,0 / 24,5 kopák = střih uvnitř · 24,75 nádech průletu · 25,0 průjezd · **25,5–26,0 vír + obrácený činel** |
| **26,0–28,0** (T14 · 1–4) **LOGO** | bílé pozadí `#ffffff`, logo BMW z `znacka/logo/vrstvy/01–09` (originální barvy `#0066b1`, `#6f6f6f`) | **26,0** prstenec bodu se stane vnějším kruhem loga (stejný střed a tloušťka), 26,0–26,5 čtvrtiny se poskládají (dvě modré dopadnou na 26,0 a 26,25, kriticky tlumeně, žádná deformace), 26,5 písmena BMW naskočí po obvodu (maska po oblouku). Dotlačení 1,00 → 1,03 nepřetržitě do 30,0 | **27,0** pod logem **„THE NEW BMW i7 M70 xDRIVE“** (Manrope 700, 56 px, `#262626`, odkrytí maskou zdola jako celek) | **úder + činel + akord 26,0**, měkký dopad loga, 26,25 tick, 26,5 jemný „ting“ |
| **28,0–30,0** (T15 · 1–4) **end card** | totéž | 28,0 jediný glint přejede po vnějším kruhu loga (lesk, ne záře, max +12 % `screen`); pohyb dotlačení pokračuje, žádný zamrzlý snímek. Poslední snímek = klidné end card | **28,0** disclaimer dole uprostřed (Manrope 500, 18 px, `#666666` kompenzovat podle C041): **„Concept ad · not affiliated with BMW · Footage and renders © BMW AG · Driving scenes: BMW i7 60 xDrive“** (poslední část viz otázka režisérovi) | doznívání akordu, 28,0 tichý glint, konec 30,0 bez ořízlého dozvuku |

### Přechody skutečný záběr ↔ render (musí být věrohodné)
Obecně: render je **studio** (produktový záběr), stopáž je **silnice**. Nepředstíráme, že jsou v jednom prostoru (to by byla koláž, test B);
spojujeme je **pohybem, polohou a světlem** jako ve skutečné reklamě, kde se střídá ateliér a jízda. Obě strany mají stejný grade (teplé výšky,
zvednutá světla, sytost 0,7 u stopáže / dorovnaný kontrast u rendru) a **stejné zrno** (seed, velikost 1,5 px, krytí ~3 %).
- **P1 match cut kolo → kolo (3,94–4,0, drop 1)**: render `uhel_090` a stopáž src 8,30 mají **příď vlevo**. Kolo rendru ve výřezu 1,0× nativně
  (r ≈ 146 px) postavit přesně na střed a poloměr kola ve snímku src 8,30 (změřit fitováním ráfku jako v testu B). Rotace v rendru 3,0–3,94 zrychluje
  na úhlovou rychlost, která odpovídá rozmazání ráfku ve stopáži (porovnat délku oblouku rozmazání). 3,94–4,0 obě strany s **vodorovným směrovým
  rozmazáním doleva** (render ve 4 snímcích před střihem, stopáž má vlastní). Na 4,0 tvrdý střih, 2 snímky expozice +12 %. Kontrola: střed kola
  4,0 vs. 3,983 ± 12 px, poloměr ± 8 %.
- **P2 švih stopáž → render (9,94–10,0)**: stopáž I končí vozem, který odjíždí doleva; přidat 4 snímky směrového rozmazání doleva (délka podle
  rychlosti pozadí ve zdroji). Render přijede **už v pohybu**: oblouk otočky `060 → 030 → 000` za 0,1 s (6 snímků, rozmazání mezi sousedy)
  + posun obrazu zprava doleva, který dobrzdí kriticky tlumeně do 10,2. Směr rozmazání na obou stranách střihu stejný.
- **P3 záře → protisvětlo (10,94–11,0)**: rozdíl zap − vyp (skutečné světlo Iconic Glow) se na 2 snímky zesílí ×3 a lehce rozkvete (bloom jen
  ze světla ledvinek, v barvě světla, ne bílý záblesk celého obrazu) → tvrdý střih do D src 29,30 s odrazem slunce na asfaltu ve stejné výšce
  obrazu (střed záře rendru a odraz slunce ± 80 px, případně výřez stopáže posunout). Světlo navazuje na světlo.
- **P4 ponor do střechy (11,5–12,0 → 12,0)**: C src 22,70 má černou skleněnou střechu přes ~40 % obrazu. Digitální zoom 1,0 → 2,4 na střed skla
  (ease-in), od 11,85 radiální rozmazání jen v tmavé ploše skla, na 11,983 je obraz ≥ 95 % tmavé sklo (průměrný jas < 20/255). Na 12,0 kostka
  interiéru začíná pohledem na `interier_strop` (tmavý strop, jas do 30/255) a sklápí se dolů. Tma skla = tma stropu: střih se schová v černé.
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
| 2,5 | kolo 909 M ostré, karta vpravo nahoře, linka od bodu na podlaze | karta nebo linka přes vůz, kolo zvětšené > 1,0× nativu (měkké), stín karty na rendru |
| 3,75 | rotační rozmazání ráfku, stopy jen v podlaze / stěně | rozmazaný ráfek tmavší než ve stopáži (test B), stopy přes karoserii, vůz „plave“ |
| 3,983 / 4,000 / 4,017 | match cut: kolo na stejném místě a velikosti | skok středu kola > 12 px, v obraze stopáže chromový rámeček ledvinek, dvojitá kola z prolínání (zákaz `framerate` / `minterpolate`) |
| 5,10 / 5,30 | průlet a záď ihned za ním | trhavá kadence (snímky se neopakují přesně 2×), jiný grade než 4,0 |
| 6,75 / 7,05 | karta 686 km, bod vedle vozu na asfaltu, punch-in | bod na laku, číslo jiné než 686, karta přes vůz, punch-in > 1,15× |
| 9,983 / 10,05 / 10,25 | švih do rendru, tvář M70 s černými M ledvinkami, pilulka | skok jasu / barvy mezi stopáží a rendrem > 10 % průměru, rozmazání na obou stranách v jiném směru |
| 10,95 / 11,0 | záře ledvinek → odraz slunce | bílý záblesk přes celý obraz, duha / RGB lem (C034) |
| 11,9 / 11,983 / 12,05 / 12,5 | ponor do skla, tma, kostka interiéru | ve tmě je vidět okraj skla nebo karoserie, střih nespadne do tmy, koláž dvou perspektiv v kostce (V003) |
| 13,5 / 14,25 / 14,75 | deska s dlaždicemi, pilulka s textem | dvě vrstvy textu naráz, 720p video zvětšené nad nativ (rozmazané), pilulka přes palubní desku v dlaždici |
| 16,6 / 17,0 / 17,6 | mřížka 3×3 živá, dlaždice 5 přes obraz, stahování do tmy | prázdné nebo stojící dlaždice, mřížka bez pohybu, bod přes vůz |
| 17,9 / 18,0 / 18,05 / 18,25 | bod sám v tmě → výbuch stop → přelet nad střechou | stopy zakrývají vůz po 18,25, záblesk neviditelný kvůli závěrce (C028), drop 2 vizuálně slabší než drop 1 |
| 19,6 / 21,6 / 22,6 | karty 500 kW / 3.8 s / 250 km/h | jakékoli číslo nad faktem během rolování (C8, V003 259), schodovité ozvěny číslic (C040), karta přes vůz |
| 23,75 / 24,6 / 24,9 | písmena i7 M70 s jízdou uvnitř, průlet otvorem „7“ | jízda v písmenech nečitelná (příliš tmavá), písmena deformovaná, čáry pásů nesrovnané po dosednutí |
| 25,9 / 26,0 / 26,3 / 27,5 / 29,98 | clona, prstenec → logo, nadpis, disclaimer, poslední snímek | logo deformované nebo v jiných barvách než `#0066b1` / `#6f6f6f` (změřit v MP4), překlep, disclaimer pod 16 px nebo mimo bezpečnou zónu, zamrzlý obraz |

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
10. **Výkon renderu** (C027): změřit 1 s výřezu (nejtěžší úsek 16–18 s mřížkou 9 videí a 23,5–25 s maskou písmen). Videa v dlaždicích připravit
    předem jako sekvence snímků ve velikosti dlaždice (žádné dekódování 720p videa při seek).
11. **Zvuk** (C035, C039): SFX posunout na skutečné časy obrazu po stavbě, klíčové údery 4,0 / 18,0 / 26,0 měřit vrcholem; drop 2 nejhlasitější;
    17,75–18,0 hudba opravdu ztichne (automatika). Odvozené soubory při přegenerování smazat.
12. **Text jen jedna vrstva**: odcházející text zmizí dřív, než přijde další (pilulka mění text uvnitř s vlastním časováním).

### Pořadí stavby
1. **Desky stopáže** (animátor, ffmpeg): 22 výřezů z úseků A–J podle storyboardu, 1,2× + zdvojení, grade high-key, 30 fps sekvence;
   pás snímků každého výřezu (kontrola ledvinek a kadence). Klíčové snímky polohy vozu (po 0,25 s) pro J 52,30–55,60, E 31,00–34,55 a střed kola A 8,30.
2. **Podklady rendrů**: expozice −1,2 EV + maska ledvinek / světlometů z rozdílu zap − vyp (`uhel_030`, `uhel_000`), sprity kola z testu B,
   kostka interiéru, dlaždice salonu (videa jako sekvence ve velikosti dlaždice), vrstvy loga.
3. **Blok A 0–12 s** (háček, kolo, P1, drop 1, karta 686, P2, tvář M70, P3, P4) → kontrolní snímky bloku A → **kreativní ředitel schválí klíčové
   snímky** (0,0 · 2,5 · 4,0 · 6,75 · 10,25 · 11,983) dřív, než se staví blok B.
4. **Blok B 12–30 s** (salon, mřížka, nádech, drop 2, karty, písmena, clona, logo, end card) + plný render celého videa a spojení se zvukem
   (zvukař souběžně: SFX podle sloupce zvuku, pak posun na skutečné časy).
5. Kontrola: kritik + kreativní ředitel (wow, realismus, energie), opravy jeden animátor.

## Průběh výroby
| kolo | kdo | co se dělalo | verdikt kritika | hlavní nálezy |
|---|---|---|---|---|

## Chyby během výroby

## Spotřeba tokenů
| agent / úkol | tokeny | akce nástrojů | čas |
|---|---|---|---|
| workflow podklady (2 agenti: analytik materiál, animátor test) | 446 446 | 214 | 61,6 min |

## Verze
| verze | datum | soubor / kam doručeno | změny |
|---|---|---|---|

## Zpětná vazba (doslova)

## Poučení
