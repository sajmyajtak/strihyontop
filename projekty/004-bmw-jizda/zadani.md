# V004: BMW řady 7: realistická reklama s jízdou (sport luxus, SaaS motion graphics)

| | |
|---|---|
| Datum zadání | 2026-11-01 |
| Platforma / formát | **16:9, 1920×1080, 60 fps** |
| Délka | **30,0 s** |
| Stav | příprava |

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

## Režijní list
- **Koncept jednou větou**: (doplní kreativní ředitel)

## Storyboard / časová osa
(doplní kreativní ředitel)

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
