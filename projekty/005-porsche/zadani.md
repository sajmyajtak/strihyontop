# V005: Porsche 718 (model 982890): pohodová jízda, během které si vůz upravuješ podle sebe

| | |
|---|---|
| Datum zadání | 2026-11-04 |
| Platforma / formát | **16:9, 1920×1080, 60 fps** |
| Délka | **30,0 s** |
| Termín | – |
| Stav | příjem |

## Zadání (doslova od uživatele)
> tak ted umděláme video na porsche. https://porsche.cz/ posílam stránky klidně si je projdi, použij barvu kterou mají na stránkách, 30s video, 16:9 formát,
> hudbá bude velmi draha protože značka auta je drahá a zároveň odpočinková jako když sedíš na velkém hoře a koukáš dolu jaka je krajina rozmanita.
> použij veškeré dovednosti které si zapisoval, https://configurator.porsche.com/cs-CZ/mode/model/982890 přesněji tenhle model budem používat auta,
> koukni se do interieru maš tam fotky na stráckách a veškeré úpravy, zkus udělat reel o pohodovém jiýdní toho auta a že mužeš si modifikovat jak se ti
> zalíbí pro koho a to s bude odehravat behěm jízdy. kdyžtak se mě ptej na přesnější detaily ktere potřebuješ vědět jinak at to vše řeší hlavní agent
> ktery to má pod kontrolou.

## Pravidla pro toto video (od uživatele, mají přednost před vším ostatním)
1. **Vůz**: model z odkazu `configurator.porsche.com/cs-CZ/mode/model/982890` (přesně tento model, interiér a úpravy z konfigurátoru / webu).
2. **Barvy** grafiky z webu porsche.cz.
3. **30 s, 16:9.**
4. **Hudba**: velmi drahá (značka je drahá) a zároveň odpočinková („jako když sedíš na velké hoře a koukáš dolů, jaká je krajina rozmanitá“).
5. **Použít všechny zapsané dovednosti** (strih-vzor.md, pravidla-strihu.md, pouceni.md, chyby.md).
6. **Příběh**: pohodová jízda tím vozem + **během jízdy si ho upravuješ, jak se ti zalíbí** (konfigurace se mění za jízdy).
7. Uživatel se ptá jen na přesné detaily, které jsou potřeba; **ostatní rozhoduje hlavní agent (režisér)**.
8. Dál platí dosavadní vkus: anglicky, realisticky (nic kresleného, V002), vůz musí jet (V003), střih podle vzoru uživatele (V004 / strih-vzor.md).

## Reference
| ID | odkaz | co z ní převzít |
|---|---|---|
| R6 | reference/R6-packeta-zbox.md | jeden hrdina, stavy, semínko, přechody bez střihu, obraz předbíhá větu, podpis tvůrce |
| R7 | reference/R7-quokka-srovnani.md | spojovací hmota značky, odchody kratší než příchody, klid jen na přečtení |
| R4 | reference/R4-easing-edukace.md | kotva (rámec drží), kaskáda prvků, předveď → zopakuj pomaleji, kamera stojí, když pracuje objekt |
| V004 | projekty/004-bmw-jizda/zadani.md | skutečná stopáž výrobce jako jízda, rendry konfigurátoru, co uživatel nechtěl (kvantita střihů) |

## Rozhodnutí režiséra
- **Náš vůz = Vanadium šedá metalíza (1H)**, stříbrná kola, interiér **53 karmín**, střecha otevřená = barva a provedení skutečné stopáže jízdy.
  Uživatel poslal jen model (odkaz bez kódu konfigurace), výchozí bílá 0Q je jen předvolba konfigurátoru, ne jeho volba. Stopáž je tak jedna z konfigurací
  a přechod jízda ↔ render je poctivý (poučení V004: nesoulad barvy stopáže a konfigurace). Bílá 0Q a ostatní laky = **úpravy za jízdy**.
- **Úpravy za jízdy jen ty, které konfigurátor vizualizuje**: lak (10 barev, pixelově zarovnané pohledy 1–4 outdoor), kola (laky kol), interiér (41 / 51 / 53,
  sedadla P07 / P11, ciferníky), střecha. Weissach paket, hořčíková kola a Paint to Sample v CZ konfigurátoru nejsou k dispozici → nepoužít jako nabídku.
- **Přebarvení skutečné stopáže (cesta A kreativního ředitele) jen po úspěšném testu**: animátor otestuje přebarvení jedoucího vozu (maska po snímcích + LUT
  z pixelově zarovnaných rendrů) na 100% výřezech; režisér rozhodne podle kritérií: žádný lem masky, žádné blikání mezi snímky, odlesky krajiny v laku zachované,
  SPZ, sklo, světla a pneumatiky nedotčené, světlé laky jen v rychlém scrollu. Když test neprojde → **cesta B** (úpravy jen na pixelově zarovnaných rendrech
  konfigurátoru, D7), stopáž zůstává šedá. Bez testu se stopáž nepřebarvuje.
- **Odpovědi na otázky KŘ (2026-11-04)**: (1) cesta A s testem, při neúspěchu B, rozhoduje režisér na 100% výřezech; (2) výchozí Vanadium šedá ano, střecha se nemění;
  (3) EN názvy voleb ověřit na porsche.com běžným načtením (animátor / analytik ve výrobě), co nepůjde ověřit, zapsat jako neověřené a použít obecný tvar
  („Blue“, „Bronze wheels“) místo vymyšleného; (4) jen náš claim, oficiální „Unfiltered driving pleasure. Open top.“ ne, uvolněný čas (~1,1 s) dát jízdě;
  (5) řádek WLTP na kartě loga ano (malým písmem, doslova, není „číslo videa“); (6) podpis tvůrce zatím „strihyontop“, disclaimer
  „Concept ad · not affiliated with Porsche · Footage and renders © Porsche AG“; (7) hudba = **nová nálada „hora“** v hudba.py (pomalá, bez bicích, vrchol místo
  dropu), skládá zvukař až k partituře; (8) prezentace 9:16 = otázka uživateli v reportu, doručuje se 16:9.
- **Odpovědi na otázky oponenta (2026-11-04)**: (1) claim 2 vypuštěn – souhlas; (2) svět POV ano („ty řídíš“), ale **pilulka se nesmí dotýkat
  rukou ani volantu**: v POV zůstane jen semínko (podtrh) v klidné ploše krajiny / nebe, pilulka se rozvine až v dalším světě; (3) interiér jako fotka F1 (2,5D,
  1,72 s) – souhlas; (4) náhradní postup T8 (peří 40 px, když 1A na průjezdu neprojde) schválen předem, animátor nečeká; (5) EN názvy voleb ověřit běžným
  načtením porsche.com, jednotka „500 PS“ podle porsche.com international; co nepůjde ověřit, nahradit obecným tvarem („Blue“, „Bronze wheels“), nevymýšlet;
  (6) podpis tvůrce zatím „strihyontop“ (čeká na uživatele).
- **Fakta** jen doslova z „Vůz a fakta“; jedno číslo na video (G9). Povinný údaj spotřeby/CO₂ na end card (malým písmem), jako V004.
- **Disclaimer**: „Concept ad · not affiliated with Porsche · Footage and renders © Porsche AG“; uživatel bude v reportu upozorněn (jen nekomerční portfolio).
- **Písmo Barlow** (náhrada Porsche Next), barvy porsche.cz: tmavý podklad #010205, text #fafbff, akcent #d5001c jen bodově.
- **Podpis tvůrce**: zatím „strihyontop“ (čeká na uživatele, vyměnit před doručením, když pošle).
- Oprava `nastroje/materialy.py` (rozdělení `_prehled.jpg` nad 60 000 px) přijata → C049.

## Materiály
| soubor | kde je | použití |
|---|---|---|
| katalog všech materiálů V005 (vůz doslova, technické údaje, nabídka úprav s kódy, texty webu, tabulky videí a fotek, shoda barvy, podmínky) | `media/projekty/005-porsche/materialy/katalog.md` | číst před storyboardem |
| rendry konfigurátoru: základ Bílá 0Q (outdoor/studio, střecha otevřená/zavřená), 1920×1080 WebP | `media/projekty/005-porsche/materialy/konfigurator/zaklad/` (23) | stavy hrdiny, střecha |
| 10 laků × 5 pohledů (v1 3/4 předek, v2 bok, v3 3/4 záď, v5 čelo, v6 záď), pixelově zarovnané + 10 laků × 2 pohledy se zavřenou střechou | `…/konfigurator/barvy/` (50), `…/barvy_strecha-zavrena/` (20) | **proměna laku maskou (D7)** |
| laky kol (stříbrná, Satin hliník, Satin černá, Satin neodym, Indigo modrá) v pohledu bok | `…/konfigurator/kola/` (6) | proměna kol |
| interiéry 53 karmín / 51 arctic / 41 standard, sedadla P07, pásy Lizard, bílé ciferníky, kožený paket (v7 palubka, v8 sedadla) | `…/konfigurator/interier/` (16) | proměna interiéru (karta / výřez) |
| exteriérové detaily zádi: bez označení, logo PORSCHE stříbrné, loga Accent | `…/konfigurator/exterier/` (3) | doplněk |
| **náhrada tiskového vozu**: Vanadium šedá 1H + stříbrná kola + karmínový interiér, outdoor otevřená v1–8, zavřená v1–4, studio v1–4; + varianta 1H s výchozími koly/interiérem | `…/konfigurator/tiskovy-vuz/` (32) | **„náš“ vůz = barva stopáže**; přechod jízda ↔ render |
| 5 videí 1920×1080 25 fps: Moodcut 11,2 s (bez textu), porsche.com hero 10,0 s + mosaic 11,7 s (část s vypáleným disclaimerem), walkaround 509,6 s (jízdní prostřihy 6–9, 119–124, 206–215, 278–286, 352–356, 358–366 s), roof tutorial 384,8 s; + 720p verze | `media/projekty/005-porsche/materialy/videa/` | **skutečná jízda** (Vanadium šedá, Weissach, bez střechy) |
| archy videí (snímek po 0,5 / 2 s; walkaround po 1 s v jízdních úsecích) + detailní snímky | `…/videa/_archy/`, `…/videa/_detaily/` | výběr záběrů |
| 13 tiskových fotek 4 505–9 504 px (5 jízdních, 2 outdoor, 4 studio, 2 interiér) + 5 fotek chronografu; press kit zip + text.pdf | `media/projekty/005-porsche/materialy/fotky/newsroom/`, `…/fotky/_press_zip/` | 2,5D pohyb, interiér, detaily |
| 35 fotek z porsche.com (AVIF 820–3840 px: jízda, detaily, interiér, Weissach, schémata motoru/podvozku) | `…/fotky/porsche_com/` | doplněk, detaily |
| značka: `znacka.css` (barvy porsche.cz + PDS tokeny), Barlow Regular/Medium/SemiBold (latin-ext), znak Porsche SVG z porsche.cz, PDS erb WebP, nápis „718“ SVG | `media/projekty/005-porsche/znacka/` | grafika, titulky, end card |
| přehled a varování všech materiálů (`materialy.py`) | `media/projekty/005-porsche/materialy/_katalog.md`, `_prehled.jpg` | kontrola |

## Vůz a fakta (analytik, 2026-11-04; vše doslova z konfigurátoru / porsche.com / newsroom, zdroje v `media/projekty/005-porsche/materialy/katalog.md` 0 a 2)
- **982890 = Porsche 718 Spyder RS**, modelový rok 2025, roadster se středním motorem, 2 místa, ruční lehká střecha (odnímatelná). Cena výchozí konfigurace **4 214 780 Kč** vč. DPH.
- **Fakta** (konfigurátor, Technická data): **500 PS** (porsche.com: **368 kW / 500 PS**) · **0–100 km/h 3,4 s** · **308 km/h** · **450 Nm** · 6 válců · 3 996 cm³ · 1 410 kg (DIN) ·
  4 418 × 1 994 × 1 252 mm · PDK 7 st. (jediná převodovka) · 9 000 1/min (porsche.com) · 0–200 km/h 10,9 s (newsroom) · střecha 18,3 kg (newsroom).
  Povinný údaj: „Fuel consumption combined: 12.7 l/100 km; CO₂ emissions combined: 288 g/km; CO₂ class: G“ (WLTP). porsche.com international: „Model currently unavailable for order.“
- **Výchozí konfigurace** (uživatelův odkaz bez kódu konfigurace): lak **Bílá (0Q)**, střecha černá (1V), kola 20" kovaná hliníková 718 Cayman GT4 RS (421), interiér kůže/Race-Tex
  **černo-arktická šedá (41)**, skořepinová sedadla (P11), scéna outdoor, střecha otevřená.
- **Claimy (anglicky, doslova)**: „Unfiltered driving pleasure. Open top.“ · „Puristic, unfiltered, genuine.“ · „Bend after bend. Goosebump after goosebump.“ ·
  „Developed for circuits – tailored to winding mountain passes“ · „'Fun doesn't come from comfort, almost the opposite.' Ferry Porsche“ · newsroom: „a more relaxed,
  characteristically convertible-style set-up“, „maximum openness … unfiltered driving experience“.
- **Úpravy, které konfigurátor vizualizuje** (rendry 1920×1080, stejná kamera = pixelově zarovnané): 10 laků (Bílá, Černá, Guards červená, Racing žlutá, Vanadium šedá metalíza,
  GT stříbrná metalíza, Gentian modrá metalíza, Arctic šedá, Ruby Star Neo, Shark modrá), střecha otevřená/zavřená, 2 scény (outdoor hala / studio), laky kol (stříbrná, Satin hliník,
  Satin černá, Satin neodym, Indigo modrá; Satin bílo-zlatá hlásí „není k dispozici“), interiéry 41 / 51 / 53 (+ 61 / 63 s Weissach), sedadla P11 / P07, Weissach paket, karbonové víko,
  loga Accent… Hořčíková kola 422 samostatně hlásí „Vybraná možnost není v současné době k dispozici.“ (zkouší se v kombinaci s Weissach, viz katalog 1).

## Značka (analytik, 2026-11-04; `media/projekty/005-porsche/znacka/znacka.css`)
- **Barvy porsche.cz** (z CSS webu importéra, četnost): bílá #fff · **Porsche červená #d5001c** (akcent, 236×) · černá #000 · tmavé šedé #191f22, #313639 · světlé šedé #eff0f1, #e3e4e4, #c8cacb · text sekundární #959899.
- **Konfigurátor (Porsche Design System 4.9)**: canvas #fff / tmavý #010205, surface #f1f1f4 / #19191a, text #010205 / #fafbff, kontrast medium #11111399 / #f6f6f88f, backdrop #24242880,
  focus #1a44ea, rádiusy 4/6/8/12 px, stín `0 4px 16px #00000029`, easing `cubic-bezier(.25,.1,.25,1)`, doby .25/.4/.6/1.2 s. CTA jsou černá tlačítka, červená jen jako akcent.
- **Doporučení pro video**: tmavý podklad #010205, text #fafbff / tlumený #f6f6f8ab, akcent **#d5001c jen bodově** (bod, podtržení, značka 12 h na volantu je žlutá → nepoužívat žlutou jako
  akcent značky), bílé karty jen pokud chceme „konfigurátorový“ vzhled (canvas #fff, surface #f1f1f4, rádius 8 px).
- **Písmo**: web používá **Porsche Next** (proprietární, načítané z cdn.ui.porsche.com; bez licence do videa nepoužívat). **Náhrada Google Fonts: Barlow** (Regular 400 / Medium 500 /
  SemiBold 600, latin-ext ověřen na „Příliš žluťoučký kůň“), soubory v `znacka/Barlow-*.ttf`. Porsche Next je mírně užší a geometrický; Barlow mu odpovídá šířkou i tvarem.
- **Logo / znak** (jen to, co weby samy zobrazují): `znacka/porsche-logo_porsche-cz.svg` (znak Porsche 258×156 z porsche.cz, barevný erb), `znacka/porsche-crest@1x.webp` (PDS erb 30×40, malý),
  `znacka/model-signature-718.svg` (nápis „718“ z PDS). Nápis PORSCHE (wordmark) jako samostatný soubor web nenabízí → v obraze jen v rendrech / fotkách nebo text Barlow 600 s prostrkáním.
  **Vše © Porsche AG; spec reklama do portfolia s disclaimerem „Concept ad · not affiliated with Porsche“** (jako V004).
- **porsche.cz = web importéra** (Porsche Inter Auto CZ), stránka modelu neexistuje (404). Oficiální model page je jen porsche.com/international (EN). Nic neobcházeno (C024).

## Materiál jízdy (analytik, 2026-11-04; podrobně `media/projekty/005-porsche/materialy/katalog.md` 3)
- **Co máme (skutečná jízda, 1920×1080, 25 fps, bez DRM, vše běžnou cestou)**: NewsTV **Moodcut 718 Spyder RS** 11,2 s (bez textu; dron nad serpentinou, přední/zadní tracking,
  POV ruce na volantu s výhledem do krajiny, detaily za jízdy) · porsche.com **hero snippet** 10,0 s a **mosaic snippet** 11,7 s (částečně vypálený text „Professional driver in a closed area.
  Do not attempt this.“ → použít jen úseky bez textu nebo ořez dole) · **walkaround** 509,6 s s jízdními prostřihy bez moderátora: **6–9 s, 119–124 s, 206–215 s, 278–286 s, 352–356 s,
  358–366 s** (≈ 35 s dalších jízdních záběrů: západ slunce, serpentina shora, přední i zadní tracking, POV, detail kola) + studio bez lidí (258–270 s bok/kolo, 312–330 s interiér).
  Celkem **≈ 65 s čisté jízdy** v horách (vulkanická krajina, serpentiny, slunce), **žádný závodní okruh**, tempo klidné až svižné → sedí k „pohodové jízdě s výhledem“.
- **Barva a provedení stopáže**: ve všech záběrech **tentýž vůz: Vanadium šedá metalíza (1H), Weissach paket (karbonové víko s lakovaným pruhem, karbonové lišty), kovaná hořčíková
  kola stříbrná, interiér černý s karmínově červeným Race-Texem, bez střechy**, SPZ S PY 500. Fotky newsroom (8K) i porsche.com = tentýž vůz. Zcela otevřený vůz (bez střechy) =
  konfigurátor „střecha Otevřít“ (roll-bary odkryté) – shoda dobrá.
- **Kvalita**: 25 fps (výstup 60 fps → zdvojení snímků nebo 1,2×/2,4× jako V004; nezpomalovat), mírně tmavý filmový grade (studené stíny, teplé slunce), hodně pohybového rozmazání
  v detailech. Fotky 8192×4608 (newsroom) umožňují 2,5D pohyb bez ztráty ostrosti.
- **Podmínky**: newsroom „may not be duplicated, distributed … without the prior consent of the right holder“, porsche.com © Porsche AG. → **jen nekomerční spec reklama do portfolia s disclaimerem
  „Concept ad · not affiliated with Porsche“**, uživatele upozornit (stejně jako V004). Nic jsem neobcházel (C024); porsche.cz model page 404, Weissach paket a hořčíková kola v CZ
  konfigurátoru hlásí „Vybraná možnost není v současné době k dispozici.“
- **Doporučení pro koncept „úpravy za jízdy“** (co jde skutečně ukázat):
  1. **Jízda = tiskový vůz (Vanadium šedá)**, proto „výchozí“ konfigurace ve videu by měla být **Vanadium šedá metalíza 1H** (ne bílá 0Q z odkazu): pak je stopáž jedna z konfigurací a
     přechod jízda ↔ render je poctivý. Render 1H existuje ve všech pohledech (outdoor otevřená/zavřená střecha, studio).
  2. **Lak**: 10 barev, **stejná kamera, pixelově zarovnané** (pohledy 1 předek-3/4, 2 bok, 3 záď-3/4, 5 předek, 6 záď; outdoor i se zavřenou střechou) → proměna laku maskou (D7)
     na rendru; na skutečné stopáži lak neměnit (přebarvení videa = riziko nerealismu, V004). Postup: jízda (šedá) → „zmrazení“ do rendru 1H (shodný úhel: zadní tracking ≈ pohled 3/6,
     přední tracking ≈ pohled 1/5) → přebarvení → zpět do jízdy (šedá) = „vybral sis“ jen jako doplněk UI, nebo stopáž ukázat vždy šedou a barvy jen jako „zkoušky“ na kartě.
  3. **Střecha otevřít / zavřít**: outdoor pohledy 1–4 v obou stavech, pixelově zarovnané → jediná úprava, kterou skutečná stopáž podporuje i obsahově (otevřený vůz za jízdy).
  4. **Kola**: laky kol na standardních kolech 421 (stříbrná 346, Satin hliník 336, Satin černá XDK, Satin neodym 348, Indigo modrá 349) v pohledu 2 (bok) a 1 → proměna kola maskou.
     Stopáž má stříbrná kola → stříbrná = výchozí.
  5. **Interiér**: 41 (arctic šedá) ↔ 53 (karmínová) ↔ 51 v pohledech 7 (palubka) a 8 (sedadla), sedadla P11 ↔ P07, bílé ciferníky XFJ, pásy Lizard zelená 561, kožený paket EKD;
     stopáž má karmínový interiér → **53 = výchozí** pro shodu s POV záběrem (ruce na volantu, červené pásy viditelné). Interiérové pohledy jsou studiové (bílé pozadí), takže
     „za jízdy“ je lepší ukázat interiér přes skutečný POV záběr (moodcut 6,6–7,6 s; walkaround 211–213 s) a render jen jako kartu/výřez.
  6. **Pohledy 5 a 6 (čelo/záď) a interiéry jsou vždy studio** (bílé pozadí) → do „jízdy“ se hodí jen pohledy 1–4 outdoor (tmavá hala); tmavá hala ladí s tmavým podkladem #010205.
  7. Nejde: Weissach paket, hořčíková kola, Satin bílo-zlatá, Paint to Sample (bez rendru) → do videa nedávat.

## Režijní list (kreativní ředitel, 2026-11-04; oponentura zapracována 2026-11-04 večer; režisér doplní rozhodnutí)
- **Koncept jednou větou**: **Jedna nepřerušená jízda horami, při které červená linka konfigurátoru (semínko) přejíždí přes jedoucí vůz a mění mu lak, kola i interiér, a na konci ho
  jedním tahem zpět vrátí do Vanadium šedé, tedy do vozu, kterým divák celou dobu jel („Tried every colour. Kept the one you're driving.“).**
  Hrdina = **vůz v jízdě** (skutečná stopáž Porsche, Vanadium šedá 1H; včetně POV z kokpitu = „ty za volantem“). Jediný doplněk = **„spec pill“** (kotva, D13): tmavá skleněná
  pilulka vpravo dole ve stylu konfigurátoru PDS s tečkou aktuální volby a jedním řádkem textu; její **červený podtrh (#d5001c) je semínko** (D10): je na snímku 0, nakreslí pilulku,
  vyjíždí z ní jako **skenovací linka**, která proměňuje vůz, a na konci nakreslí erb Porsche. Úpravy za jízdy = **stavy hrdiny** (D8): lak (předveď rychle → zopakuj pomaleji, D15) →
  kola → interiér → výhled (jedno číslo 500 PS) → návrat k šedé (odkrytí původní stopáže = nejpoctivější proměna) → pilulka vyroste na celý obraz (= svět loga) → logo → podpis tvůrce.
  **Příčina každé změny** (G8, oponentura): před každou proměnou se tečka pilulky na 0,12 s rozvine do **řady vzorků** konfigurátoru (3–5 koleček Ø 18 px), podtrh (semínko) přejede
  pod vybraný vzorek = „klik“, řada se smrští do tečky nové barvy a teprve pak vyjede linka. Divák vidí volbu → linku → vůz (příčina → následek, D14).
- **Semínko**: červená linka 3 × 96 px vpravo dole (x 1728–1824, y 968) na snímku 0 → 0,08–0,32 s se natáhne a vyroste z ní pilulka (TAH) → v každé úpravě přejede pod vzorek a vyjede
  z pilulky jako linka 3 × 1080 px (svislá) nebo 1920 × 3 px (vodorovná) přes obraz (za linkou je nový stav vozu), po proměně se vrátí jako podtrh → 20,72 s pilulka i s podtrhem vyroste
  na celý obraz (MORF rámce) → 23,18 s podtrh nakreslí obrys erbu Porsche → erb (logo). Barva vždy #d5001c, bez záře, 1 px měkká hrana, při rychlém pohybu směrové rozmazání 10–20 px.
- **Vzhled**: písmo **Barlow** (500 na pilulku a věty, 600 na claim a podpis, `media/projekty/005-porsche/znacka/`), paleta porsche.cz: canvas #010205, pilulka #010205 @ 72 % s 1 px
  okrajem #f6f6f8 @ 20 %, rádius 8 px (PDS), **skutečné rozostření pozadí za sklem 12 px** (předpočítaná rozmazaná deska, ne jen ztmavení), text #fafbff, tlumený #f6f6f8ab, akcent
  **#d5001c jen linka, vzorky, tečka a tik**. Žádná žlutá (značka 12 h na volantu je žlutá, není to barva značky). Pilulka: výška 84 px, text 48 px, zarovnaná vpravo (pravá hrana x 1824,
  y 900–984), tečka Ø 18 px vlevo od textu; **kompaktní stav** (jen tečka + podtrh, 84 × 84 px, x 1740–1824) tam, kde pilulka nemá text (POV 2,60–4,22). Nejdelší věta („Kept the one
  you're driving.“) ≈ 790 px → levá hrana ≈ x 1034: **animátor změří skutečnou šířku v Barlow a zapíše ji** (kolize s vozem, Past 8). Kamera: **stopáž má vlastní kameru, digitálně nic
  nedotlačujeme** (výjimky: T2 nájezd do erbu na volantu, T3 nájezd ≤ 1,12×); fotka interiéru 2,5D (3 vrstvy) s posunem 1,00 → 1,05.
- **Rytmus**: řídí ho **věty na obrazovce** v pilulce (3–5 slov, slova z rozostření v tempu řeči, obraz předbíhá slovo o 0,1–0,35 s) a proměny vozu; událost každých ~0,6 s
  (≈ 52 událostí / 30 s), bez metronomu; po každé větě 0,4–0,9 s čisté jízdy (pohoda = ticho mezi větami). Hudba se skládá až k partituře (D12): pomalá, široká, bez dropu,
  vrchol = otevření výhledu 13,87 s, kadence do tóniky = návrat šedé 20,78 s, jediný úder = podpis 27,85 s.
- **Stopáž**: 25 fps → 60 fps **jen 1,2× (kadence 2:2)**, bez interpolace (V004). Všechny záběry Vanadium šedá, bez střechy, Weissach pruh na víku (je ve všech záběrech, nevadí).
  Rozpis úseků níže; každý úsek jen jednou (C044). **Jízda = 20,7 s z 30 (69 %)**: 0–22,44 stopáž, z toho fotka F1 1,72 s (jediný nejedoucí obraz) — číslo 78 % z první verze
  počítalo fotku jako jízdu, opraveno.
- **Prompt / šablona**: vlastní kostra z `prompt-motion/poznatky.md` 10 (+ 11.2 spojení s fotorealistickým produktem) a `strih-vzor.md`; zakázáno: záře, částice,
  prolínačky scén, třes kamery, text v rozích mimo kotvu, překreslený vůz, cokoli jako šablona.
- **Akceptační kritéria pro kritika**: 1920×1080, 60 fps, 30,00 s · −14 LUFS / ≤ −1 dBTP po AAC · pravidla uživatele 1–8 · partitura níže po snímcích (`strih-vzor.md` 6):
  v každém snímku 1 hrdina + 1 doplněk (pilulka), 0 tvrdých střihů v grafice, **8 střihů ve stopáži (T1–T8)** vždy s přežívající pilulkou a maskovaných proměnou (každá jiná: LET ·
  ZOOM skrz erb · EXPL · CLONA · LET svislý · WIPE · střih pod kartou · PRŮJEZD-WIPE · MORF rámce · TAH · ZÁBLESK), příchody z rozostření 0,1–0,25 s / odchody kratší, klid jen na
  přečtení, jedno číslo (500 PS, klid ≥ 1 s), semínko na snímku 0 a zpět v logu, podpis tvůrce 2 s + disclaimer · **pilulka nikdy neleží na laku vozu** (pás snímků po 0,25 s, Past 8) ·
  **realismus**: proměny laku jen uvnitř masky karoserie, měkkost hrany masky = délka pohybového rozmazání v daném snímku, odlesky a stín zachované, žádný lem, žádné blikání masky,
  barva vozu v každém záběru odpovídá tabulce stavů · **po 20,78 s rozdíl proti původní stopáži = 0 mimo UI** · **vůz jede** 20,7 s z 30 (69 %), fotka nejvýš 1,72 s · zakázané úseky
  stopáže nepoužity · interiér po 13,47 s nikde čitelně karmínový.

### Rozhodnutí kreativního ředitele (režisér potvrdí nebo přepíše)
1. **Výchozí konfigurace ve videu = Vanadium šedá metalíza 1H + stříbrná kola + karmínový interiér** (vůz ze stopáže), ne bílá 0Q z odkazu; odkaz uživatele určuje model, ne barvu.
2. **Střecha se nemění** (ruční střecha nejde zavřít za jízdy, a claim modelu je „Open top“). Rendry se zavřenou střechou nepoužít.
3. **Úpravy laku a kol se dějí přímo na jedoucím voze ve stopáži** (nová technika, test před stavbou, níže). Záložní cesta B: proměna na pixelově zarovnaných rendrech
   `konfigurator/barvy/` vstupujících do obrazu v pohybu (V004 P2), vůz ve stopáži zůstává šedý; příběh funguje v obou cestách („zkoušel jsi, nechal sis šedou“).
4. **Interiér** = skutečná tisková fotka `fotky/newsroom/BX24I3HOD0015.jpg` (sedadla shora, krajina) jako **2,5D ve 3 vrstvách** (krajina / karoserie / sedadla; paralaxa 6 px, posun
   krajiny 24 px, kamera 1,00 → 1,05) s odbarvením karmínu na Arctic šedou v masce; rendry v7/v8 nepoužít (studio). Oponentura prověřila alternativy: přelet nad kokpitem ve walkaroundu
   (W5 212,2–213,2) má sedadla jen jako rozmazanou červenou skvrnu ve švihu kamery, POV moodcut sedadla neukazuje → fotka zůstává, ale je **jediný nejedoucí obraz** a drží 1,72 s.
5. **Jedno číslo = 500 PS** (konfigurátor „Výkon (PS) 500 PS“); cena 4 214 780 Kč a další údaje do obrazu nejdou. Povinný údaj WLTP jen jako malý řádek na kartě loga.
   Karta čísla přichází **až po větě o výhledu** („Nowhere to be.“), ne hned po wipe: výhled nejdřív dýchá (pohoda), číslo pak přežije střih X1 → W11.
6. Názvy voleb anglicky podle konfigurátoru Porsche (EN): Vanadium Grey Metallic, Guards Red, Black, Shark Blue, Ruby Star Neo, GT Silver Metallic, Gentian Blue Metallic,
   Satin Neodyme (kola), Carmine Red / Arctic Grey (interiér; porsche.com: „The contrasting colours are Arctic Grey or Carmine Red“). Režisér ověří EN tvary na porsche.com (bez obcházení, C024).
7. Věty na obrazovce s tečkami jako claimy Porsche („Unfiltered driving pleasure. Open top.“): výjimka z E8 kvůli stylu značky.
8. **(oponentura) POV z kokpitu** (moodcut 6,68–8,60: ruce na volantu, krajina) hned po háčku = skutečný interiér za jízdy a „ty řídíš“; pilulka je v něm **kompaktní** (tečka + podtrh),
   žádný text (nádech před premisou). Premisa „Configure it. On the road.“ zůstává na W4.
9. **(oponentura) Scroll barev = 4 laky po 0,20 s** (Black · Shark Blue · Ruby Star Neo · GT Silver), ne 6 po 0,125 s: 8 Hz strobo odporuje „pohodě“ a Bílá / Racing žlutá z tmavě
   šedého zdroje jsou nejméně věrohodné LUTy (realismus 3×). Pořadí: tmavá → sytá → sytá → světlá, aby poslední (GT Silver → Gentian Blue) byla pomalá proměna s odlesky.
10. **(oponentura) Návrat k šedé** se posouvá na snímky, kde je vůz střední až velký a ostrý (W6 zdroj 280,45–281,41, výstup 19,98–20,78), ne na blízký rozmazaný průjezd; průjezd
    kolem kamery (282,16–283,20) pak běží **nezměněný** za sklem celoobrazové pilulky = pointa „the one you're driving“ projede kolem diváka ve skutečné barvě.
11. **(oponentura) Svět loga vzniká z kotvy**: pilulka vyroste na celý obraz (MORF rámce, D13 „nový svět = morf rámce“), ne ztmavení pod karoserií. Claim 2 „Unfiltered driving pleasure.
    Open top.“ **vypuštěn** (dva claimy za sebou + WLTP + název = přetížený konec; logo drží 5,2 s, z toho 1,1 s jen erb s názvem = luxusní klid). Režisér může vrátit, pak nahradí
    klid 26,30–27,40.
12. **(oponentura) Kolo**: svět M8 trvá jen 1,03 s (moodcut 8,64–9,88 je celý záběr), proto má jen **jednu proměnu a jeden popisek** („Satin Neodyme“); otázka „Wheels?“ vypuštěna.
    Satin Neodyme je lak kol 421; vůz ve stopáži má hořčíková kola 422 → měníme jen barvu ráfku, tvar nezmiňujeme.

## Storyboard / střihová partitura (kreativní ředitel, 2026-11-04; revize po oponentuře 2026-11-04 večer)
Časy = výstup (60 fps, s), zdroj = čas ve zdrojovém souboru (25 fps, rychlost 1,2×). Typy: TAH · PIS · ROZ-IN / ROZ-OUT · LET · WIPE · ZOOM · MORF · EXPL · CLONA · PRŮJEZD-WIPE · ODOMETR · ZÁBLESK.
**Stavy hrdiny** (barva vozu v obraze, musí sedět v každém snímku): 0,00–6,96 Vanadium šedá (originál) · 6,96–7,21 přechod → **Guards Red** 7,21–8,32 · 8,32 Black · 8,52 Shark Blue ·
8,72 Ruby Star Neo · 8,92–9,86 GT Silver · 9,86–10,76 přechod → **Gentian Blue** 10,76–19,98 (včetně kola M8, fotky F1, dronu X1, W11 i průjezdu T8 a dálky W6) · kola stříbrná →
**Satin Neodyme** od 11,24 do 19,98 (i malá / rozmazaná ve W11, T8, W6) · interiér karmín → **Arctic Grey** od 13,12 (po 13,47 nikde čitelný karmín) · 19,98–20,78 návrat → originál ·
**od 20,78 stopáž 1:1 originál** (rozdíl 0 mimo UI).
Kotva = pilulka vpravo dole (pravá hrana x 1824, y 900–984; kompaktní 84 × 84 px v POV 2,60–4,22) od 0,20 do 20,72, potom vyroste na celý obraz (= canvas loga) do 27,40 (91 % videa).
**Vzorky** = řada 3–5 koleček Ø 18 px, rozestup 8 px, vyjede z tečky doleva (0,12 s, ease-out), podtrh přejede pod vybraný (0,08 s), řada se smrští do tečky nové barvy (0,08 s).

| # | prvek | příchod | typ příchodu | klid (s) | odchod | typ odchodu | co ho spojuje s dalším | věta / slovo |
|---|---|---|---|---|---|---|---|---|
| **S0 HÁČEK** | **W1** walkaround 119,04–122,16 → **0,00–2,60**: západ slunce, vůz 3/4 zepředu vlevo, hory, protisvětlo, průjezd kolem kamery 2,05–2,45 | | | | | | | |
| 1 | stopáž W1 (vůz jede, projede kolem kamery) | 0,00 | hotový obraz od snímku 0 (B6) | – | 2,45–2,60 | **LET**: 9 snímků vodorovného rozmazání z průjezdu + expozice +0,3 EV | **T1**: rozmazaná karoserie kryje střih do POV | – |
| 2 | **semínko**: červená linka 3×96 px (x 1728–1824, y 968) | 0,00 | stojí od snímku 0 | 0,08 | 0,08–0,20 | MORF: natáhne se na 520 px (ease-out) | linka = podtrh pilulky | – |
| 3 | **pilulka (kotva)** 84 px, tmavé sklo | 0,20–0,32 | TAH/ROST z linky nahoru (0 → 84 px, kriticky tlumené) | do 20,72 na místě | 20,72–21,02 | **MORF rámce** na celý obraz | obsah se mění uvnitř (D13) | – |
| 4 | věta 1 „Still deciding? Keep driving.“ | 0,32 · 0,47 · 0,85 · 1,00 | ROZ-IN po slovech 0,15 s (pauza po „?“) | 1,15–2,50 | 2,50–2,58 | ROZ-OUT 0,08; pilulka se smrští do kompaktní 84×84 (2,58–2,70) | kompaktní kotva přežije střih | **věta 1** |
| **S1 TY ZA VOLANTEM** | **M7** moodcut 6,68–8,60 → **2,60–4,20**: POV ruce na volantu, krajina, erb na volantu (x 960–1090, y 960–1080) | | | | | | | |
| 5 | stopáž M7 (POV) | 2,60 | z rozmazání T1 (6 snímků dobrzdí, ease-out) | – | 4,05–4,30 | **ZOOM skrz erb**: nájezd 1,0 → 2,6 ease-in na erb na volantu (střed x 1025, y 1020) + ROZ 0 → 18 px; erb vyplní obraz 4,20 | **T2**: za rozostřeným erbem W4 z rozostření 14 → 0 px (4,22–4,30) | – |
| 6 | kompaktní pilulka (tečka Vanadium + podtrh), bez textu | 2,70 | z MORF (4) | 2,70–4,30 | 4,30–4,40 | MORF: rozvine se doleva pro větu 2 | nádech: jen jízda, žádné slovo | – |
| **S2 PREMISA + ČERVENÁ** | **W4** walkaround 206,28–210,84 → **4,22–8,02**: vůz 3/4 zepředu, serpentina se svodidlem, přijíždí, 7,9–8,0 blízko | | | | | | | |
| 7 | stopáž W4 | 4,22 | z rozostření T2 | – | 7,99–8,02 | – (kryje EXPL) | **T3**: plocha Guards Red → tečka nad W7 | – |
| 8 | věta 2 „Configure it. On the road.“ | 4,42 · 4,57 · 4,82 · 4,95 · 5,10 | ROZ-IN po slovech | 5,25–5,75 | 5,75–5,82 | ROZ-OUT | pilulka se přeznačí na konfigurační řádek | **věta 2** |
| 9 | tečka barvy Ø 18 px (Vanadium #6b7075) | 5,86 | ROZ-IN 0,10 | – | mění barvu | – | kaskáda: tečka → text +6 snímků (D14) | – |
| 10 | text „Vanadium Grey Metallic“ | 5,96 | ROZ-IN 0,15 | 6,10–6,60 | 6,60–6,66 | ROZ-OUT | stav = pravda (vůz je šedý); pak 0,0 s klid, jen jízda | popisek |
| 11 | **vzorky laku** (5: Vanadium ● · Guards Red · Gentian · Shark · GT Silver) | 6,60–6,72 | řada vyjede z tečky | – | 6,80–6,88 | smrští se do tečky Guards Red | podtrh přejede pod Guards Red 6,72–6,80 = „klik“ (příčina) | – |
| 12 | **skenovací linka 1 (předveď)** 3×1080 px | 6,88–6,96 | LET z pilulky k levé hraně vozu (rozmazání 20 px) | – | 6,96–7,21 přejede vůz zleva doprava (**0,25 s**, zdroj 209,57–209,87, vůz střední, ostrý), za ní lak Guards Red; 7,21–7,31 zpět do pilulky (ease-in) | MORF zpět na podtrh | stav vozu šedá → červená | – |
| 13 | text „Guards Red“ | 7,11 | ROZ-IN 0,12 | 7,25–7,90 | 7,90–7,96 | ROZ-OUT | popisek 0,15 s **po** začátku proměny (D1) | popisek |
| 14 | **EXPL**: tečka Guards Red → plná červená plocha (2 snímky 7,99–8,02) | 7,99 | EXPL | – | 8,02–8,05 | plocha se smrští zpět do tečky nad W7 | **T3** (barva = Guards Red, nic jiného) | – |
| **S2b HRA S BARVAMI** | **W7** walkaround 283,40–287,00 → **8,02–11,02**: zadní sledovací, vůz uprostřed, blíží se, SPZ S PY 500 čitelná od 10,5; pravá hrana vozu ≤ x 1380 (pilulka volná) | | | | | | | |
| 15 | stopáž W7 (vůz červený) | 8,02 | z EXPL | – | 10,92–11,02 | **CLONA**: kruh ze středu pravého zadního kola (zdroj 286,88–287,00; kolo ≈ x 1250, y 800), měkký okraj 8 px, 6 snímků | **T4**: v kruhu už běží M8 | – |
| 16 | **vzorky + scroll (předveď)**: řada 4 vzorků zůstane rozvinutá; podtrh skáče: 8,32 Black · 8,52 Shark Blue · 8,72 Ruby Star Neo · 8,92 GT Silver; vůz i tečka přepnou v 1 snímku s každým skokem | 8,22–8,32 | řada vyjede z tečky | 8,92–9,56 (GT Silver) | 9,00–9,08 | řada se smrští do tečky GT Silver | rychlá verze → pomalá verze (D15) | – |
| 17 | věta 3 „Try them all.“ | 8,47 · 8,59 · 8,71 | ROZ-IN | 8,82–9,20 | 9,20–9,26 | ROZ-OUT | 0,15 s po prvním přepnutí | **věta 3** |
| 18 | text „GT Silver Metallic“ | 9,32 | ROZ-IN | 9,45–9,62 | 9,62–9,68 | ROZ-OUT | – | popisek |
| 19 | vzorky (Gentian vybrán) | 9,56–9,66 | řada vyjede | – | 9,70–9,78 | smrští do tečky Gentian | podtrh pod Gentian 9,66 = příčina linky 2 | – |
| 20 | **skenovací linka 2 (zopakuj pomaleji)** | 9,78–9,86 | LET z pilulky k levé hraně vozu | – | 9,86–10,76 přejede vůz zleva doprava (**0,9 s = 3,6× pomaleji**, zdroj 285,63–286,71, vůz uprostřed, ostrý), za ní Gentian Blue Metallic (odlesky krajiny v laku zůstávají); 10,76–10,86 zpět | MORF na podtrh | stav stříbrná → modrá | – |
| 21 | tečka → Gentian Blue (9,98) + text „Gentian Blue Metallic“ | 10,08 | ROZ-IN | 10,22–10,86 | 10,86–10,92 | ROZ-OUT | 0,22 s po startu linky | popisek |
| **S3 KOLA** | **M8** moodcut 8,64–9,88 → **11,02–12,05**: přední kolo + blatník za jízdy (kolo vlevo dole), karoserie modrá od 1. snímku | | | | | | | |
| 22 | stopáž M8 | 11,02 | z CLONY | – | 11,95–12,05 | **LET svisle**: obraz odletí nahoru (−1080 px, 6 snímků, svislé rozmazání) | **T5**: fotka interiéru přijede zdola (jeden svislý pohyb = „pohled dolů do kokpitu“) | – |
| 23 | vzorky kol (3: stříbrná ● · Satin Neodyme · Satin černá) | 11,12–11,20 | řada vyjede | – | 11,24–11,30 | smrští do tečky Satin Neodyme (bronz) | podtrh pod Satin Neodyme 11,20 | – |
| 24 | **proměna ráfku**: kruh z náboje ven, stříbrná → Satin Neodyme | 11,24–11,54 | CLONA z náboje (0,3 s) | 11,54–11,95 | – | – | stav kol (platí do 19,98) | – |
| 25 | text „Satin Neodyme“ | 11,39 | ROZ-IN | 11,52–11,92 | 11,92–11,98 | ROZ-OUT | 0,15 s po startu proměny | popisek |
| **S4 INTERIÉR** | **F1** fotka newsroom BX24I3HOD0015 (sedadla shora, karmín, krajina; karoserie v záběru modrá, kolo bronz) → **12,05–13,77**; 2,5D 3 vrstvy, kamera 1,00 → 1,05 | | | | | | | |
| 26 | fotka interiéru | 12,05 | LET zdola (dojede ease-out 6 snímků) | – (2,5D pohyb) | 13,62–14,02 | **WIPE** pruhy padají shora (#313639, #191f22, #eff0f1, červená 3px náběžná hrana): 0,15 s nájezd · 0,10 s plná #191f22 · 0,15 s odjezd dolů | **T6**: konec wipe = otevření výhledu (nádech) | – |
| 27 | věta 5a „Carmine inside.“ | 12,20 · 12,40 | ROZ-IN | 12,55–12,95 | 12,95–13,01 | ROZ-OUT | 0,15 s po příchodu fotky | **věta 5** |
| 28 | vzorky interiéru (3: Carmine ● · Arctic · Black) | 12,90–13,02 | řada vyjede | – | 13,06–13,12 | smrští do tečky Arctic | podtrh pod Arctic 13,02 | – |
| 29 | **skenovací linka 3 vodorovná** | 13,04–13,12 | LET z pilulky k horní hraně sedadel | – | 13,12–13,47 sjede shora dolů přes sedadla (karmín → Arctic Grey: odbarvení v masce + jas +35 %, textura zůstává); 13,47–13,57 zpět | MORF na podtrh | stav interiéru | – |
| 30 | věta 5b „Or Arctic.“ | 13,22 · 13,37 | ROZ-IN | 13,50–13,77 | 13,77 | kryje wipe | 0,10 s po startu linky | věta 5 |
| **S5 VRCHOL (výhled)** | **X1** mosaic 0,00–2,56 → **13,87–16,00**: dron nad serpentinou, hory, vůz od 15,1 malý vpravo (modrý) · **W11** walkaround 363,00–365,00 → **16,00–17,67**: lávová pláň, rovná silnice, vůz z dálky blíží se (modrý, kola bronz), **končí ve střední velikosti před průjezdem** | | | | | | | |
| 31 | stopáž X1 | 13,87 (vidět pod odjíždějícím wipem) | z WIPE | – | 16,00 | tvrdý střih ve stopáži pod kartou | **T7**: karta 500 PS přežívá (číslo právě roluje), obě krajiny široké, vůz malý | – |
| 32 | **nádech**: nic, jen dron | 13,87 | – | 13,87–14,15 | – | – | výhled nejdřív dýchá (pohoda), věta až potom | – |
| 33 | věta 6 „Nowhere to be.“ | 14,17 · 14,37 · 14,52 | ROZ-IN | 14,67–15,27 | 15,27–15,33 | ROZ-OUT | věta výhledu → karta čísla | **věta 6** |
| 34 | **karta čísla**: pilulka vyroste na 420×200 px (pravá hrana 1824, y 784–984) | 15,40–15,60 | MORF rozměru (kriticky tlumené) | – | 17,45–17,60 | MORF zpět na pilulku | kotva mění rozměr, ne polohu | – |
| 35 | popisek „PS“ (48 px, vpravo od čísla) | 15,52 | ROZ-IN | 15,62–17,42 | 17,42 | s kartou | kaskáda karta → PS → číslice (po 7 + 6 snímcích) | – |
| 36 | **číslo 500** (Barlow 600, 150 px): roluje zdola 000 → 500, odometrické rozmazání | 15,62–16,32 | ODOMETR 0,7 s (jen horší hodnoty, G9); roluje **přes střih 16,00** | **16,32–17,42 (1,10 s)**, ding na 16,32 (ustálený snímek) | 17,42–17,52 | zblednutí | jediné číslo videa | **„500 PS“** |
| 37 | stopáž W11 | 16,00 | tvrdý střih pod kartou | – | 17,67–18,10 | **PRŮJEZD-WIPE**: vůz (modrý) projíždí vlevo kolem kamery (zdroj 365,00–365,52); kumulativní maska karoserie = kde už vůz prošel, je W6 (hrana = maska s peřím 24 px, bez přidaného rozmazání) | **T8**: vůz „smete“ pláň a odkryje skály W6 | – |
| **S6 ROZHODNUTÍ** | **W6** walkaround 277,68–283,40 → **17,67–22,44**: vůz 3/4 zepředu z dálky mezi skalami (modrý), přijíždí, střední 19,5–20,6, velký 20,6–21,4, **průjezd vlevo 21,40–22,25**, prázdná silnice 22,25–22,44 | | | | | | | |
| 38 | stopáž W6 | 17,67 (celá od 18,10) | z PRŮJEZD-WIPE | – | 22,27–22,44 | sklo celoobrazové pilulky → neprůhledné #010205 (vůz už projel, prázdná silnice) | **T9** dokončen: svět loga = vnitřek kotvy | – |
| 39 | věta 7 „Tried every colour.“ | 18,20 · 18,40 · 18,60 | ROZ-IN | 18,75–19,60 | 19,60–19,66 | ROZ-OUT | – | **věta 7** |
| 40 | vzorky laku (5, Vanadium vybrán) | 19,66–19,78 | řada vyjede | – | 19,84–19,90 | smrští do tečky Vanadium | podtrh pod Vanadium 19,80 = příčina návratu | – |
| 41 | **skenovací linka 4 zprava doleva** | 19,90–19,98 | LET z pilulky k pravé hraně vozu | – | 19,98–20,78 přejede vůz **zprava doleva** (0,8 s, zdroj 280,45–281,41: vůz střední → velký, ostrý, pravá hrana ≤ x 1200), za ní **původní stopáž** (šedý lak, stříbrná kola); 20,78–20,88 zpět | MORF na podtrh | návrat = odkrytí originálu (nejpoctivější proměna) | – |
| 42 | tečka → Vanadium (20,12) + text „Vanadium Grey Metallic“ | 20,22 | ROZ-IN | 20,36–20,62 | 20,62–20,69 | ROZ-OUT (dřív, než pravá hrana vozu dosáhne x 1174 ≈ zdroj 281,2) | popisek 0,24 s po startu linky | popisek |
| 43 | **MORF rámce**: pilulka (x 1034–1824, y 900–984) vyroste na 1920×1080, sklo 72 % + rozostření 12 px zůstává; tečka zbledne, podtrh se přesune pod střed (y 600) | 20,72–21,02 | MORF (kriticky tlumené, 0,30 s) | 21,02–22,27 sklo | 22,27–22,44 | sklo → 100 % #010205 | **T9**: nový svět = morf rámce (D13); za sklem projede skutečný šedý vůz 21,40–22,25 (rozmazaný stín pod větou) | – |
| 44 | věta 8 „Kept the one you're driving.“ (Barlow 600, 72 px, střed, y 540) | 20,92 · 21,07 · 21,22 · 21,37 · 21,52 | ROZ-IN po slovech, velikost 48 → 72 px roste s rámcem | 21,67–22,62 (průjezd za sklem) | 22,62–22,70 | ROZ-OUT (podtrh zůstane) | pointa = průjezd skutečného vozu za větou | **věta 8** |
| **S7 LOGO** | canvas #010205 (vnitřek kotvy) → **22,44–27,65** | | | | | | | |
| 45 | název „718 Spyder RS“ (SVG „718“ 120 px + Barlow 600 72 px, střed y 540) | 22,78 | PIS 0,30 | 23,08–24,05 | 24,08–24,28 | sjede o 60 px dolů (ease 0,2 s) a drží do 27,40 | – | název |
| 46 | **TAH erbu**: podtrh vyjede nahoru a nakreslí obrys štítu (180 px) nad názvem | 23,18–23,58 | TAH | – | 23,58–23,78 | výplň: barevný erb (SVG porsche.cz) uvnitř obrysu, červený obrys zbledne | **semínko → logo (D10)** | – |
| 47 | claim „Configured on the road.“ (Barlow 600, 56 px, pod názvem) | 24,32 · 24,52 · 24,67 · 24,87 | ROZ-IN | 25,02–26,22 | 26,22–26,30 | ROZ-OUT | jediný claim; po něm 1,1 s jen erb + název (luxusní klid) | **věta 9** |
| 48 | řádek WLTP (18 px, #f6f6f8ab, y 980): „718 Spyder RS (WLTP): Fuel consumption combined 12.7 l/100 km · CO₂ emissions combined 288 g/km · CO₂ class G“ | 24,62 | ROZ-IN | do 27,40 | 27,40–27,65 | s logem | povinný údaj, není to „číslo videa“ | – |
| 49 | erb + název: dotlačení 1,00 → 1,02 (24,0–27,4, kamera dýchá) | – | – | 26,30–27,40 jen erb + název | 27,40–27,65 | ROZ-OUT + zblednutí 0,25 s (C9) | → ticho | – |
| 50 | ticho (černá) | 27,65 | – | 0,20 | 27,85 | – | – | – |
| 51 | **boom + bílý záblesk** | 27,85 | ZÁBLESK 2 snímky bílá, bloom dozní 0,15 s | – | – | – | jediný hlasitý úder videa (I9) | – |
| 52 | **end card tvůrce** „strihyontop“ (Barlow 600, 96 px, prostrkání 0,12 em; režisér vymění jméno/logo) | 27,90–28,05 | ROZ-IN z bílé | 28,05–30,00 (dotlačení 1,00 → 1,02) | 30,00 | konec | – | – |
| 53 | disclaimer „Concept ad · not affiliated with Porsche AG · footage © Porsche AG“ (22 px, #f6f6f8ab) | 28,15 | ROZ-IN | do 30,00 | – | – | – | – |

**Čísla partitury**: 10 světů (W1 · POV · W4 · W7 · M8 · fotka · dron + pláň · W6 · logo · podpis) · 53 prvků, ≈ 52 událostí / 30 s = **jedna za 0,58 s** · nejdelší klid prvku 1,35 s (věta 1 nad jedoucím vozem), 1,20 s (claim) a 1,10 s (číslo) ·
tvrdých střihů v grafice **0**; střihů ve stopáži 8 (T1–T8), každý maskovaný jinou proměnou a vždy s přežívající pilulkou · přechody mezi světy: LET (průjezd) · ZOOM skrz erb · EXPL (Guards Red) · CLONA · LET svislý · WIPE · střih pod kartou · PRŮJEZD-WIPE · MORF rámce · TAH → logo · ZÁBLESK, **žádný dvakrát** ·
jízda 20,7 s z 30 (69 %; fotka 1,72 s jediný nejedoucí obraz) · jedno číslo (500 PS, klid 1,10 s) · obraz předbíhá každou větu o 0,10–0,24 s · kotva 91 % videa · ticho mezi větami (jen jízda): 2,70–4,30 · 5,82–5,86 · 6,66–7,11 · 13,87–14,17 · 17,60–18,20 ·
kaskády: vzorky → podtrh → tečka → linka → popisek (6–8 sn.), karta → PS → číslice (7 + 6 sn.), pilulka → rámec → název → obrys → erb → claim.

**WOW momenty (v pořadí síly)**: (1) 19,98–20,78 linka zprava doleva „odvolá“ všechny úpravy a odkryje skutečný vůz, který vzápětí 21,40–22,25 projede kolem diváka za sklem s větou „Kept the one you're driving.“ = pointa a zároveň nejrealističtější snímky videa ·
(2) 6,96–7,21 vůz v zatáčce zčervená pod linkou, krajina se nehne, a vzápětí 7,99 červená tečka exploduje do Guards Red plochy · (3) 8,32–8,92 čtyři laky za 0,6 s podtrhem po vzorcích + 9,86–10,76 totéž pomalu v modré s odlesky krajiny ·
(4) 13,62–14,15 wipe v šedých porsche.cz → dron nad serpentinou, 0,3 s ticha, „Nowhere to be.“ · (5) 13,12–13,47 sedadla z karmínu do Arctic pod vodorovnou linkou · (6) 20,72–21,02 pilulka vyroste na celý obraz a 23,18–23,78 podtrh nakreslí erb Porsche ·
(7) 4,05–4,30 nájezd skrz erb na volantu z POV do jízdy.

### Změny po oponentuře (nezávislý kreativní ředitel, 2026-11-04 večer; důkazy = snímky zdrojů v `media/projekty/005-porsche/materialy/videa/`)
Hodnocení první verze partitury: **střih 7,5 · realismus 7,0 · pohoda 7,0 · nápad + řemeslo 8,5 → celkem 7,5**. Cíl revize: střih 9, realismus 8,7 (závisí na testu A), pohoda 9.
1. **Kolize pilulky s vozem (střih, realismus)**: W7 zdroj 287,0–288,1 má pravou hranu vozu na x 1380–1480, popisek „Gentian Blue Metallic“ začíná na x ≈ 1200 → pilulka ležela na laku 0,9 s.
   Oprava: W7 končí na zdroji 287,00 (výstup 11,02), CLONA z kola 286,88–287,00. Totéž W6: návrat šedé byl na zdroji 281,04–282,0 (vůz velký, od 281,9 rozmazaný průjezd, pravá hrana
   x 1340 = pod pilulkou) a maska byla plánovaná jen do 281,1, ale modrá byla potřeba do 282,0. Oprava: návrat na 280,45–281,41 (vůz střední → velký, ostrý, hrana ≤ x 1200), popisek
   odchází 20,62 před dojezdem hrany na x 1174; maska W6 do 281,41 a dál nic (originál).
2. **Průjezd W11 (realismus)**: zdroj 365,0–365,4 je už velký rozmazaný průjezd vlevo (ne „před průjezdem“, jak stála první verze). Oprava: W11 končí ve střední velikosti na 365,00 a
   průjezd 365,00–365,52 se stává přechodem T8 PRŮJEZD-WIPE (kumulativní maska: kde vůz prošel, je W6). EXPL se přesouvá na T3 (W4 → W7), kde je tematický: tečka Guards Red → plocha Guards Red.
3. **Svět kola přetížený (střih)**: M8 = celý záběr moodcut 8,64–9,88 (1,03 s), první verze do něj dala 4 události (věta 4a, clona, věta 4b, odlet). Oprava: jedna proměna + jeden popisek.
4. **Pohoda**: (a) scroll 6 laků po 0,125 s (8 Hz) → 4 laky po 0,20 s, bez Bílé a Racing žluté (nejslabší LUTy z tmavě šedé); (b) karta 500 PS už 0,1 s po wipe na výhledu → výhled 0,3 s
   dýchá, věta „Nowhere to be.“, číslo až 15,40 a roluje přes střih do W11; (c) nový svět **POV ruce na volantu** (moodcut 6,68–8,60, 1,6 s, žádný text, kompaktní pilulka) hned po háčku:
   skutečný interiér za jízdy, „ty řídíš“, nádech před premisou; (d) claim 2 vypuštěn, logo končí 1,1 s klidu jen s erbem; (e) ticho mezi větami vyčísleno (5 úseků).
5. **Příčina proměn (G8, D14)**: tik tečky nestačil jako „klik“. Nově řada vzorků konfigurátoru z tečky (0,12 s) → podtrh pod vybraný → smrštění → linka. Scroll barev = podtrh skáče po vzorcích.
6. **Přechod do loga**: „ztmavnutí pod rozmazanou karoserií“ bylo prolnutí do černé. Nově MORF rámce: pilulka vyroste na celý obraz (sklo s rozostřením), skutečný vůz projede za sklem
   s větou 8, pak sklo zneprůhlední na prázdné silnici (D13 „nový svět = morf rámce“). Průjezd 282,16–283,20 zůstává 1:1 originál.
7. **Fotka interiéru**: prověřeny alternativy (přelet W5 212,2–213,2: sedadla = červená šmouha ve švihu; POV bez sedadel) → fotka zůstává, ale jako 2,5D ve 3 vrstvách a jediný nejedoucí
   obraz (1,72 s); podíl jízdy opraven z chybných 78 % na **69 %** (první verze počítala fotku jako jízdu).
8. **Realismus masek**: doplněno kritérium „měkkost hrany masky = délka pohybového rozmazání v daném snímku“ (jinak vzniká šedý lem kolem modré na rozmazaných hranách), LUT i pro průjezd
   T8, časový medián masky 3 snímky, kontrola rozdílem proti originálu po 20,78.
9. **Nevyužité, k dispozici jako náhrady**: desktop snippet 6,0–7,0 (onboard kamera na boku vozu, roll-bar, silnice; bez textu) = hezký „pohodový“ záběr, kdyby POV neprošel; W5 211,0–212,4
   (zadní sledovací → nálet nad vůz, bez švihu) jako náhrada W11.

### Rozpis úseků stopáže (každý jednou, rychlost 1,2×, začátky na hranici snímku zdroje = násobky 0,04 s; ověřeno snímky 2026-11-04 večer)
| kód | zdroj (`media/projekty/005-porsche/materialy/videa/`) | zdroj od–do | výstup od–do | obsah | stav vozu v obraze |
|---|---|---|---|---|---|
| W1 | `newstv_242104_walkaround_hls.mp4` | 119,04–122,16 | 0,00–2,60 | západ slunce, 3/4 zepředu, průjezd vpravo 121,5–121,98, 122,16 prázdná silnice | šedá (originál) |
| M7 | `newstv_249707_moodcut_hls.mp4` | 6,68–8,60 | 2,60–4,20 | **POV ruce na volantu**, krajina, erb na volantu x 960–1090 / y 960–1080, pravá ruka x 1440–1800 / y 700–1010 (kompaktní pilulka x 1740–1824 se jí dotýká jen okrajem) | originál (interiér černý, karmín nevidět) |
| W4 | walkaround | 206,28–210,84 | 4,22–8,02 | 3/4 zepředu, serpentina se svodidlem, vůz střední (209,5) → blízko (210,5–210,80); 210,84 už je jiný záběr | šedá → 6,96 Guards Red |
| W7 | walkaround | 283,40–287,00 | 8,02–11,02 | zadní sledovací, vůz uprostřed (283,4 záď shora zblízka, 284–286,7 střed, ostrý), SPZ S PY 500 čitelná od 286,5; **pravá hrana vozu ≤ x 1380** → pilulka volná; 287,0–288,1 **nepoužít** (vůz pod pilulkou) | červená → scroll → GT Silver → 9,86 Gentian Blue |
| M8 | moodcut | 8,64–9,88 | 11,02–12,05 | přední kolo + blatník za jízdy (celý záběr, 9,88 střih na záď) | Gentian Blue, kola 11,24 Satin Neodyme |
| F1 | `fotky/newsroom/BX24I3HOD0015.jpg` (9504×5346) | – | 12,05–13,77 | sedadla shora, krajina; 2,5D 3 vrstvy | karoserie v záběru Gentian Blue, kolo bronz, sedadla karmín → 13,12 Arctic |
| X1 | `porschecom_718spyderrsmosaicsnippetEN.mp4` | 0,00–2,56 | 13,87–16,00 | dron nad serpentinou, vůz malý od 1,5 s zdroje | Gentian Blue (malý) |
| W11 | walkaround | 363,00–365,52 | 16,00–18,10 | lávová pláň, vůz z dálky → střední (365,0); **365,00–365,52 = průjezd vlevo (PRŮJEZD-WIPE T8)**, dál nepoužít | Gentian Blue, kola bronz (i v průjezdu) |
| W6 | walkaround | 277,68–283,40 | 17,67–22,44 | 3/4 zepředu z dálky mezi skalami (277,7 vůz tečka), střední 280,0–281,0, velký 281,0–282,0, průjezd vlevo 282,16–283,20, 283,2–283,4 prázdná silnice | Gentian Blue + bronz → 19,98–20,78 originál → **originál 1:1** |
**Náhradní úseky** (jen po schválení režiséra, s kontrolou proti zakázaným, C044): W2 122,20–124,08 (kaňon, vůz přijíždí, průjezd vlevo) · W9 355,84–357,68 (silnice, vůz projede) ·
W10 357,68–360,16 (záď 3/4) · M6 moodcut 5,60–6,64 (zadní sledovací v zatáčce) · M9 moodcut 9,88–11,20 (zadní sledovací) · X 8,76–9,84 (přední sledovací z dálky) · D desktop 5,00–6,88 (6,0–7,0 =
onboard kamera na boku vozu, bez textu) a 6,88–10,04 (bez textu) · W5a 211,00–212,40 (zadní sledovací → nálet nad vůz, před švihem) · W8 352,16–355,84 jen **místo** W1 (totéž slunce, duplikát).
**Zakázané úseky**: walkaround 0–6,0 (intro NewsTV) a 6,0–119,04, 122,20–206,28, 216,04–277,68, 288,12–352,16, 360,16–363,00, 365,60–konec (moderátor, studio s růžovou stěnou,
outro) · **W5b 212,40–216,04** (švih nad kokpitem = červená sedadla po změně interiéru, rozmazané) · **W7 287,00–288,12** (vůz pod pilulkou) · desktop 1,36–5,00 a mosaic 3,00–7,00 (vypálený text) ·
mosaic 7,72–8,76 (roll-bar, sedadla) · roof tutorial celý · fotka 0675 (červené sedadlo) · rendry v5/v6/v7/v8 (studio) a se zavřenou střechou · rendry kol na bílém voze (`kola/`) · po 13,47 žádný záběr s čitelným karmínovým interiérem.

### Proměny na stopáži: nová technika (test PŘED stavbou, animátor; schválí kreativní ředitel na 100% výřezech)
**A. Přebarvení laku jedoucího vozu LUTem z rendrů (cesta A, preferovaná)**
1. Maska vozu po snímcích (BiRefNet / rembg jako V004 test B) na W4 209,0–210,84, W7 celý (283,40–287,00), M8, X1 (vůz malý), W11 363,0–365,52 (včetně průjezdu), W6 277,68–281,41;
   **měkkost hrany = délka pohybového rozmazání v daném snímku** (změřit posun vozu mezi snímky: peří = max(2 px, 0,5 × posun)), eroze 1 px, časový medián masky 3 snímky (proti blikání).
   Pro T8 navíc **kumulativní maska** (max přes čas) průjezdu 365,00–365,52.
2. Uvnitř masky jen **karoserie**: vyloučit pneumatiky a ráfky (sledovaná elipsa), sklo a světla (chroma červená / L > 0,92), SPZ (sledovaný obdélník), černé díly (L < 0,12). Co není lak, se nemění.
3. **1D LUT z pixelově zarovnaných rendrů** `konfigurator/barvy/1H_*_v3_zad-34.webp` × `<cíl>_v3_zad-34.webp` (pro zadní záběr W7) a `v1_predek-34` (pro W4, W6, W11): v Lab, v masce karoserie rendru,
   64 binů L zdroje → medián (L, a, b) cíle. Tím se přenese skutečná odezva laku (jak se mapují odlesky a stíny), ne plochá barva. Aplikovat uvnitř masky stopáže; mimo masku nic.
   Cíle: **G1** Guards Red, **A1** Black, **D7** Shark Blue, **N2** Ruby Star Neo, **U2** GT Silver, **1A** Gentian Blue (0Q a P3 už nejsou potřeba).
4. Test: W7 zdroj 285,0–286,0 (25 snímků) pro G1, 1A, A1, U2; W4 209,5–210,5 pro G1; W6 280,5–281,4 pro 1A (návrat: 1A → originál); M8 pro 1A + ráfek (bod 5); W11 365,0–365,5 pro 1A (rozmazaný průjezd).
   Výstup: pás snímků 100 % výřez + MP4 1 s.
   **Kritéria přijetí**: na 100 % výřezu žádný lem ani „vystřižený“ okraj (ani na rozmazaných hranách), odlesk slunce a odraz krajiny zůstávají ve tvaru (jen změní barvu podle LUT), žádné blikání
   (průměr L v masce mezi sousedními snímky < 2 %), SPZ a světla beze změny, barva vozu na snímku odpovídá tečce v pilulce (ΔE < 12 proti rendru). Pokud 1A na W11 průjezdu neprojde, T8 jde
   z originálu W11 jen s LUT na ostrých snímcích do 365,10 a od 365,10 maska s peřím 40 px (rozmazání kryje).
5. **Kola**: v M8 kruh z náboje (sledovaný střed), ráfek stříbrná → Satin Neodyme = chroma bronzu + L −12 %, rotační rozmazání zůstává; ve W11/W6/T8 malé elipsy kol tónovat stejně (jen chroma).
6. **Interiér (F1)**: statická maska karmínu (chroma), odbarvení + jas +35 % → Arctic; karoserie na fotce LUT 1A, kolo bronz; 3 vrstvy (krajina / karoserie / sedadla) vyříznuté jednou (statické masky,
   výplň pozadí za sedadly inpaint jen o 8 px přesahu). Jednoduché, bez testu.
7. **Sklo celoobrazové pilulky (T9)**: rozmazaná deska W6 282,0–283,40 (Gauss 12 px, předpočítat), ztmavení 72 %; za sklem zůstává viditelný pohyb projíždějícího vozu (stín).
8. Výkon: masky předpočítat jako PNG sekvence (30 fps), LUT jako 3 malé tabulky; scéna jen skládá; změřit 1 s výřezu (C027).
**B. Záloha** (když A neprojde): proměny jen na rendrech `barvy/` v3 / v1 (sweep linky = maska, D7) vstupujících v pohybu z W7 / W6 (švih P2 z V004: 4 snímky směrového rozmazání, render
přijíždí s dojezdem 0,2 s, zpět stejně), stopáž vždy šedá; kola vynechat (S3 → M6 zadní sledovací 5,60–6,64, bez popisku); interiér F1 zůstává; T8 beze změny (vůz šedý). Rendry nemají Weissach pruh na víku →
používat jen v3 (záď, pruh není vidět). Pointa „Kept the one you're driving“ platí beze změny.

### Hudba (pro zvukaře; skládá se až k hotové partituře, D12; časy se doladí k obrazu, ne naopak)
- **Nálada**: „na vrcholu hory“: velmi drahá a klidná. Pomalé, široké, bez bicích a bez dropu; nálada stoupá k jedinému vrcholu (otevření výhledu) a pak se uvolní do tóniky.
  Tempo **72 BPM** (nebo volně), durová tónina (F / D dur), akordy maj9 / m9 / add9 (jako `luxusni`, ale poloviční tempo), žádná marimba, žádný shaker, žádný kopák do 13,87; od 14,15 nejvýš
  měkký „tep“ (sub + taiko tiše na 1. dobu, −20 dB). Nástroje: smyčcová plocha (`plocha`, útok 0,6–1,0 s), tlumené piano (`klavir`, tiché), sub swell, dlouhý dozvuk rt60 3,0–3,5 s, předelay 30 ms,
  středy ≥ 30 % (I7). Rozsah −22 LUFS (úvod) → **−16 LUFS vrchol 14,15–17,60** → −20 LUFS logo.
- **Klíčové momenty**: 0,00 jediný tón piana (háček, bez plochy) · 2,60 nástup plochy (POV = první nádech plochy, široké) · 6,96 první proměna (jen SFX, hudba beze změny) · 7,99 EXPL (krátký
  měkký akcent plochy, ne úder) · 9,86–10,76 pomalá proměna = swell +2 dB · **13,62 nádech** (hudba −6 dB za 0,3 s pod wipem) · **13,87–14,15 vrchol**: plocha se rozevře o oktávu, melodie piana
  4 takty (ticho v obraze = hudba vede) · 16,00 pokračuje bez změny · 17,67–18,10 průjezd (jen SFX) · 19,98–20,78 návrat k šedé = kadence do tóniky (teplý durový akord přistane na 20,78) ·
  20,72–21,02 morf rámce: hudba se „zavře“ (low-pass na 2 kHz za 0,3 s = jsme uvnitř skla), 22,44 zpět otevřená, jen plocha + piano, decrescendo · 27,40 fade 0,25 s · **27,65–27,85 ticho** ·
  **27,85 boom** (jediný úder videa, plný, ne agresivní) · 28,0–30,0 dozvuk, tichý pad pod podpisem.
- **Existující nálady**: `luxusni` je harmonicky nejblíž (Am9 Fmaj7 Dm9 Em7, Rhodes), ale 120 BPM s kopákem a shakerem = moc rytmické; `pohodova` (96, marimba) moc hravé; `vazna` moc dramatické.
  Chybí: **pomalá nálada bez bicích se stoupáním k vrcholu místo dropu** → nová nálada `hora` (`--vrchol 13.87 --konec 27.65`, bez `--drop`), odvozená z akordů `luxusni` při 72 BPM: plocha + piano + sub,
  obrácený činel nahradit swellem plochy, konec bez `uder` (ten patří až na podpis).
- **SFX** (tiché, jen na stavy, ~1/s, `sfx.py`): 0,20 pilulka (měkký klik UI) · slova (bez zvuku) · 2,58 pilulka do kompaktní (tichý tik) · 4,05–4,30 nájezd skrz erb (tichý whoosh dolů) · 5,86 tik tečky ·
  6,60 vzorky (tichý „rozvinutí“ 3 tiky), 6,72 klik podtrhu · 6,96–7,21 sken (tichý „shimmer“ sklo, vrchol 7,08) · 7,99 EXPL (1 snímek tichý pop) · 8,32 · 8,52 · 8,72 · 8,92 čtyři kliky podtrhu
  (PDS klik, každý jiná výška) · 9,66 klik · 9,86–10,76 sken pomalý (shimmer delší) · 10,92 clona (měkký whoosh) · 11,20 klik · 11,24 kolo (kovový tón tichý) · 11,95 let nahoru (whoosh tichý) · 13,02 klik ·
  13,12–13,47 sken · 13,62 wipe (nádech, hudba dolů) · 15,62–16,32 tiky odometru jen na viditelné přenosy řádů, **ding 16,32** na ustálený snímek (C047) · 17,67–18,10 průjezd (tichý skutečný
  průjezd: šum vzduchu, ne motor naplno) · 19,80 klik · 19,98–20,78 sken obrácený (shimmer dolů) · 20,72 morf rámce (whoosh tichý + low-pass hudby) · 21,40–22,25 průjezd za sklem (tlumený) ·
  23,18–23,58 tah erbu (tenký tón) · 27,85 **boom + záblesk** (0 až −3 LU v okně 100 ms, hudba ztichlá).

### Kontrolní snímky (před plným renderem, z výřezu s podsnímky, C028) a kritéria odmítnutí
| čas | co musí být vidět | odmítnout, když |
|---|---|---|
| 0,000 | hotový plakát: západ slunce, šedý vůz 3/4 vlevo, červená linka 3×96 vpravo dole, nic jiného | linka chybí nebo má záři; text už na obrazovce; obraz zatmívá z černé; bloky komprese v nebi |
| 0,32 / 0,47 / 1,00 | pilulka hotová, slova věty 1 z rozostření po jednom | pilulka naskočí ostře; dvě slova v jednom snímku; text nad bezpečnou zónou (y > 984) |
| 2,45 / 2,52 / 2,60 / 2,68 / 2,75 | průjezd → rozmazání → POV dobrzdí; pilulka se smrští do kompaktní (tečka + podtrh) a zůstane na místě | střih vidět ostře; rozmazání v jiném směru než průjezd; pilulka blikne nebo zmizí |
| 3,40 / 4,05 / 4,20 / 4,25 / 4,30 | POV čistý bez textu, kompaktní pilulka vpravo dole; nájezd na erb na volantu, erb vyplní obraz rozostřený, za ním W4 z rozostření | kompaktní pilulka leží na erbu; nájezd s trhnutím; W4 naskočí ostře; erb překreslený nebo deformovaný |
| 4,42 / 5,10 / 5,86 / 5,96 | pilulka se rozvine doleva, věta 2 po slovech, tečka → popisek Vanadium (kaskáda 6 sn.) | věta naráz; tečka a text v jednom snímku |
| 6,60 / 6,72 / 6,80 / 6,88 / 6,96 / 7,08 / 7,21 / 7,31 | řada vzorků z tečky → podtrh pod Guards Red → smrštění → linka u levé hrany vozu → půl vozu červený s ostrou svislou hranicí → celý červený → linka zpět | červená mimo karoserii (silnice, svodidlo, kola, sklo, SPZ); lem; vůz „plave“; odlesk slunce zmizel; hranice není rovná; vzorky mimo pilulku |
| 7,97 / 7,99 / 8,00 / 8,02 / 8,05 | poslední snímek W4 (vůz blízko, červený) → plocha Guards Red 2 snímky → tečka nad W7 | plocha déle než 2 snímky; EXPL z jiného místa než tečka; W7 šedý v prvním snímku |
| 8,32 / 8,52 / 8,72 / 8,92 | čtyři barvy, každá i na tečce a vzorku s podtrhem; mezi snímky kroku nic nebliká mimo vůz | barva na okolí; GT Silver „plochá“ (bez odlesků); krok jiný než 0,20 s; podtrh jinde než pod aktuálním vzorkem |
| 9,86 / 10,30 / 10,76 / 10,86 | pomalá linka: stříbrná vlevo od linky, modrá vpravo (ne naopak), odlesky krajiny v modré; pilulka celou dobu mimo vůz | směr proměny opačný než popis; linka se zastaví; modrá mimo masku; pilulka na laku |
| 10,92 / 10,97 / 11,02 / 11,12 / 11,24 / 11,39 / 11,54 / 11,95 | kruh z pravého zadního kola W7 se otevře do M8; M8 modrý od 1. snímku; vzorky kol → kruh z náboje, ráfek bronzový, rotační rozmazání zůstává; popisek; odlet nahoru | střed kruhu mimo kolo; M8 šedý v prvním snímku; bronz na pneumatice nebo blatníku; ráfek ostřejší/plošší než originál; svislý let bez rozmazání |
| 12,05 / 12,20 / 13,02 / 13,12 / 13,30 / 13,47 | fotka dojede zdola (3 vrstvy, paralaxa vidět na hraně sedadla proti krajině), „Carmine inside.“, vzorky → vodorovná linka, sedadla nad linkou šedá / pod linkou červená, pak celá šedá | šedá bez textury (zalitá); změna i na pásech / madlech, které nejsou karmín (ověřit proti rendru 51); karoserie na fotce šedá místo modré; vrstvy s viditelným lemem |
| 13,62 / 13,77 / 13,87 / 14,02 / 14,15 | pruhy padají, plná #191f22 na 13,77–13,87 s červenou hranou, pod nimi už dron; 13,87–14,15 **nic nového** (nádech) | pruhy v jiných barvách než porsche.cz; wipe delší než 0,4 s; dron zatmívá z černé; text do 14,15 |
| 14,17 / 14,52 / 15,40 / 15,52 / 15,62 / 16,00 / 16,32 / 17,42 / 17,60 | „Nowhere to be.“ po slovech → karta roste → „PS“ → číslo roluje jen zdola (hodnoty < 500) **přes střih 16,00** (karta beze změny) → ustálí se na 500 → klid ≥ 1 s → zblednutí → karta se smrští | hodnota > 500 během rolování (G9); klid < 1 s (C046); ding mimo ustálený snímek (C047); karta přes vůz; karta blikne na střihu; vůz ve W11 šedý nebo bez bronzu kol (pokud ≥ 40 px) |
| 17,67 / 17,80 / 17,95 / 18,10 | průjezd W11: vůz modrý, za jeho zadní hranou už skály W6 (kumulativní maska), před ním ještě pláň; po 18,10 celé W6 | hrana průjezdu ostrá bez peří; W6 vidět mimo oblast, kudy vůz prošel; dvojitý obraz vozu |
| 19,80 / 19,98 / 20,40 / 20,78 / 20,88 | vzorky → linka zprava, **vlevo od linky modrá, vpravo šedý originál**, pak celý originál = 1:1 s nezměněnou stopáží (rozdíl snímků = 0 mimo pilulku) | po 20,78 jakýkoli rozdíl proti originálu; kola zůstala bronzová |
| 20,62 / 20,72 / 20,90 / 21,02 / 21,40 / 21,80 / 22,25 / 22,44 | popisek pryč dřív, než hrana vozu dojede pod pilulku; pilulka vyroste na celý obraz (sklo + rozostření 12 px), věta 8 po slovech ve středu roste 48 → 72 px, šedý vůz projede za sklem jako stín, prázdná silnice → sklo zneprůhlední | pilulka na laku před morfem; sklo bez rozostření (jen tmavý filtr); průjezd za sklem nevidět vůbec nebo naopak ostrý; věta 8 zmizí dřív, než se dočte; skok textu při změně velikosti |
| 22,78 / 23,18 / 23,38 / 23,58 / 23,78 / 24,32 / 24,87 | název psaný maskou; podtrh vyjede a kreslí obrys štítu; výplň barevným erbem; claim po slovech | erb deformovaný / jiné barvy než SVG (změřit v MP4); obrys kreslí jiná barva než #d5001c; erb naskočí bez tahu |
| 26,30 / 27,40 / 27,65 / 27,85 / 27,90 / 28,15 / 29,98 | jen erb + název (klid, dýchání 1,00 → 1,02), rozostření, černá, záblesk 2 snímky, podpis z bílé, disclaimer, poslední snímek s dotlačením | překlep; WLTP jinak než doslova nebo < 16 px; záblesk neviditelný kvůli závěrce (C028); zamrzlý poslední snímek; disclaimer chybí |

### Pasti stavby
1. **Kadence** 25 → 60 fps jen **1,2×** (2:2), nikdy 1,0× / 1,5× / `minterpolate` / `framerate` (V004). Výřezy začínat na hranici snímku zdroje; podsnímky závěrky neprolínat dva zdrojové snímky (hranice o 1/120 s).
2. **Stav vozu v každém záběru** podle tabulky stavů (nahoře): před stavbou vyplnit „barva · kola · interiér“ pro každý úsek; kritik kontroluje po snímcích. Žádný záběr po 13,47 s čitelným karmínem (W5b, mosaic 7,72–8,76 zakázány).
3. **Realismus proměn**: jen uvnitř masky karoserie, LUT z rendrů (ne plochá barva), časový medián masky; **peří masky = délka rozmazání** (ostrý snímek 2 px, průjezd až 40 px); odlesky a stín zůstávají; nikdy přebarvit silnici, svodidlo, SPZ, světla, sklo.
   Kontrola 100% výřezem a rozdílem proti originálu (po 20,78 musí být rozdíl 0 mimo UI).
4. **Grade jednotný** jedním filtrem pro všechny desky stopáže (stopáž je lehce studená, stíny +3 %, teplé výšky zachovat); fotka F1 je teplejší a sytější → dorovnat ke stopáži (změřit průměr Lab na nebi a asfaltu);
   zrno stejné (seed) na stopáži i fotce; canvas loga #010205 bez zrna. POV (moodcut) je tmavší a kontrastnější než walkaround → dorovnat střední jas (±5 %), ne vzhled.
5. **Zakázané úseky** (C044) hlídá autor i kritik u každé náhrady; čas zdroje v hlášení. Úseky neprodlužovat přes hranice střihů zdroje (122,20 · 210,84 · 287,00 · 365,52 · 283,40 · 8,60 · 9,88 · 2,56).
6. **Text jen jedna vrstva** v pilulce (odcházející zmizí dřív, než přijde další; C046: odchod ≤ 0,08 s, žádný prázdný rámec > 2 snímky); slova z rozostření, ne kurzorem; nikdy dvě nová slova v jednom snímku kromě pointy.
   Vzorky (řada koleček) a text smí být v pilulce zároveň (jeden doplněk = pilulka), ale řada nikdy nepřesahuje levou hranu pilulky.
7. **Číslo** (G9, C046, C047): 000 → 500 jen zdola, klid 1,10 s, ding na ustálený snímek (pohyb < 0,5 px), tiky jen na viditelné přenosy; rozmazání číslic v kódu, ne kopiemi (C040). Karta přežívá střih 16,00 beze změny.
8. **Pilulka vs. vůz** (změřeno 2026-11-04 večer): pilulka nikdy neleží na laku. Změřené pravé hrany vozu: W7 283,4–286,7 ≤ x 1380 (OK), 287,0+ x 1380–1480 (zakázáno) · W6 280,5 ≈ 1080, 281,0 ≈ 1160,
   281,3 ≈ 1200, 281,9 ≈ 1340, 282,2+ celý obraz (proto popisek pryč 20,62 a morf rámce 20,72) · W4 vpravo volno · M8 kolo vlevo · X1 skály · W11 silnice; POV: kompaktní pilulka x 1740–1824 se dotýká jen
   okraje pravé ruky (není lak). **Animátor změří skutečnou šířku každého textu v Barlow a zapíše levou hranu pilulky**; pás snímků po 0,25 s = důkaz pro kritika.
9. **Linka**: 3 px, #d5001c, bez záře, 1 px měkká hrana; při rychlém pohybu směrové rozmazání v kódu; nikdy se nezastaví mimo pilulku déle než 0,1 s (semínko „nikdy nezmizí, jen se mění“).
10. **Moduly scény** (C036): prefixy bloků `A_` (0–13,87) a `B_` (13,87–30); regrese i uvnitř přechodů (2,60 / 4,22 / 8,02 / 11,02 / 12,05 / 13,87 / 16,00 / 17,67 / 20,72 / 22,44).
11. **Výkon** (C027): masky a LUT předpočítané, desky stopáže jako 30fps sekvence, rozmazaná deska pro sklo (T9) předpočítaná; změřit 1 s nejtěžšího úseku (8,32–8,92 scroll, 13,62–14,02 wipe přes dron, 20,72–21,02 morf se sklem).
12. **Zvuk až po obrazu** (C045): po posledním renderu režisér posune SFX na skutečné časy; boom měřit vrcholem na 27,85; hudba 27,65–27,85 opravdu ticho.
13. **Erb a písmo**: erb jen ze SVG porsche.cz (bez deformace, barvy změřit v MP4, C034); nájezd skrz erb na volantu (T2) je nájezd do **stopáže**, ne do SVG (erb na volantu se smí rozmazat, nesmí se překreslit); Porsche Next nepoužívat, Barlow z `znacka/`; tenký text ≥ 16 px a barvy změřit po kódování (C041).
14. **Právní**: disclaimer na podpisu, WLTP řádek doslova; spec reklama jen do portfolia (podmínky newsroom).
15. **PRŮJEZD-WIPE (T8)**: kumulativní maska = max(maska(τ)) pro τ ≤ t; W6 pod ní běží od 17,67 (zdroj 277,68), i když je vidět jen v odkryté části; bez přidaného rozmazání (rozmazání je ve stopáži); žádný „duch“ vozu ve W6 (vůz W6 je v tu chvíli tečka v dálce).
16. **MORF rámce (T9)**: pilulka roste z (x 1034–1824, y 900–984) do celého obrazu s rádiusem 8 → 0 px, text se přelije z pravého zarovnání do středu bez skoku (interpolovat polohu i velikost 48 → 72 px); sklo = skutečné rozostření desky, ne jen ztmavení; po 22,44 už žádná stopáž pod canvasem.

### Pořadí stavby
1. **Test nové techniky** (animátor, ≤ 1 h): bod A 1–5 na W7 285,0–286,0 + W4 209,5–210,5 + W6 280,5–281,4 + M8 + W11 365,0–365,5; pás 100% výřezů + 1s MP4 → **kreativní ředitel rozhodne A / B** (kritéria v bodu 4).
2. **Desky stopáže** (animátor, ffmpeg): 9 úseků z rozpisu (W1, M7, W4, W7, M8, X1, W11, W6 + F1 vrstvy), 1,2× + zdvojení, jednotný grade, 30fps sekvence; masky vozu + kol + SPZ pro W4 (od 209,0), W7, M8, X1, W11 (včetně průjezdu, kumulativní), W6 (do 281,41);
   LUT pro 1H → G1, A1, D7, N2, U2, 1A (v3 i v1); F1 masky (karmín, karoserie, kolo, 3 vrstvy); rozmazaná deska W6 282,0–283,4 pro sklo. Pás snímků každého úseku (kontrola kadence, textu, moderátora).
3. **Blok A 0–13,87** (háček, pilulka, POV + nájezd skrz erb, W4 + vzorky + červená + EXPL, W7 scroll + modrá, M8 kola, F1 interiér, wipe) → kontrolní snímky bloku A → **kreativní ředitel schválí klíčové snímky**
   (0,00 · 1,00 · 3,40 · 4,22 · 7,08 · 8,52 · 10,30 · 11,39 · 13,30 · 13,77) před blokem B.
4. **Blok B 13,87–30** (dron + věta 6 + karta 500 PS přes střih, W11 + průjezd-wipe, W6 + návrat, morf rámce se sklem + průjezd za sklem, logo + tah erbu, claim, WLTP, ticho, boom, podpis) + plný render + spojení se zvukem
   (zvukař souběžně: nálada `hora` + SFX podle sloupce výše, pak posun na skutečné časy).
5. Kontrola: kritik (technika + zadání + partitura po snímcích + stav vozu + pilulka vs. vůz) a kreativní ředitel (wow, realismus, energie, střih, pohoda); opravy jeden animátor.

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
