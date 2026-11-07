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

## Rozhodnutí režiséra po testu techniky (2026-11-05)
- **Cesta A schválena** (přebarvení skutečné stopáže LUTem v masce). Režisér prohlédl 100% výřezy (klic_v2_1.40, W6_spz_v2, pas_v2): odlesky krajiny v laku drží, SPZ, světla,
  mřížky a kola nedotčené, návrat = originál. Odstín změřen v Lab: test Gentian Blue hue 292°, C 26,8 · render konfigurátoru 1A hue 289°, C 29,8 → fialový nádech má i originální lak, věrné.
  **Podmínka**: W4, W7 (scroll 4 laků), M8 (kola) a X1 (malý vůz) projdou stejnými kritérii při přípravě desek; když některý záběr neprojde, pro něj cesta B (rendry), ostatní A.
- **T8 = střih v pohybu na zdroji 365,40** (výstup 18,00): W11 363,00–365,40, W6 od 278,08; pilulka přežívá. PRŮJEZD-WIPE se nedělá (šev přes nebe = vložený wipe).
- **Věta 8 začíná s MORF rámce**: slova 20,72 · 20,87 · 21,02 · 21,17 · 21,32 (C045: změna časů → zvuk).
- **Nájezd skrz erb 7×** (erb vyplní obraz). Render `--sub-rychle 16` v úsecích MORF a ZOOM.
- **Masky BiRefNet pro všechny úseky počítá režisér na pozadí** (`media/projekty/005-porsche/_skript/desky_masky.py`, log `desky_masky.log`): `desky/<kód>/src/NNNNN.png`
  (název = index snímku zdroje při 25 fps) a `desky/<kód>/maska/NNNNN.png`; úseky W4 5225–5270, W7 7085–7174, M8 216–246, X1 37–63, W11 9075–9135, W6 6952–7035;
  57 masek převzato z testu (pixelově ověřené mapování). Pořadí výpočtu W4 → W7 → M8 → X1 → W11 → W6, ~28 s na snímek.

## Rozhodnutí režiséra ke kolu kontroly 1 (2026-11-07, závazné pro opravy v2)
1. **T8 / W11 průjezd (KŘ blokující)**: výstupní střih zůstává na **18,00** a všechno za ním beze změny. Rozmazaný průjezd 365,00–365,40 se **nepřebarvuje** složitěji, ale vypadne:
   okno W11 posuň o 0,40 s dřív (zdroj **362,60–365,00**, snímky 9065–9124), T8 = střih na zdroji 365,00 (vůz středně velký a ostrý). Masky 9065–9074 dopočítej
   `_skript/desky_masky.py` (rozšiř USEKY W11; nikdy dva BiRefNet najednou, C051). Když by 362,60–365,00 obsahem nesedělo (vůz mimo záběr, jiný záběr), zkrať W11 zepředu a
   prodluž předchozí úsek; střih v pohybu na 18,00 zachovej v pohybu vozu, ne v rozmazání.
2. **W6 kola, pneu, černé plasty, Gentian Blue (KŘ závažné)**: podle návrhu KŘ (výluka kol + bronz na celý úsek 6952–7035, L < 20 ve spodní třetině vyloučit, `--detail 0.85`,
   bez tmavého lemu, odstín porovnat s W7 10,5). Stav hrdiny platí: ráfky Satin Neodyme od 11,24 všude, kde je kolo ≥ 40 px.
3. **CLONA 10,92, ODOMETR, MORF sklo, WIPE, erb, LET, linka 1, Arctic**: oprav podle návrhů KŘ. U MORF platí: vůz za větou musí být čitelný (sklo 35–40 %, rozostření 4–6 px, místní ztmavení pod textem).
4. **Klid loga 26,30–27,43**: je to záměrný klid z partitury (luxusní konec, „sedíš na hoře“), žádné nové prvky. Jen dýchání ať se **nezastaví**: plynulé 1,00 → 1,03 lineárně až do ROZ-OUT (bez ease-outu), aby obraz nikdy nestál (nález kritika).
5. **Průchod ROZ 3,233 (kaňon → interiér)**: když zůstává „rozmazaným střihem“, ztmav vrchol průchodu o −0,6 EV na 2 snímky (jako mrknutí). Jiný typ přechodu nezaváděj.
6. **W11 přebarvení (kritik)**: v novém okně 362,60–365,00 platí výluky SPZ, sklo, roll-bary, světla (sledované jako W6s) a odstín/kresba jako u W6 (bod 2).
7. Zvuk: posun SFX na skutečné časy dělá v tomto kole zvukař (workflow ho spustí po tvé opravě), proto **vypiš všechny časy změn** do zmeny_casu.

## Odpovědi režiséra animátorovi A (2026-11-05, platí pro animátora B a opravy)
1. **M7**: kaňon 2,60–3,23 + POV od zdroje 7,44 (3,23–4,20) se střihem ve stopáži a přežívající kompaktní pilulkou = přijato (D3: střih ve skutečné stopáži s přežívajícím
   spojovacím prvkem je povolen). Partituru nepřepisovat, jen zapsat jako T1b; zvuk na střih nic.
2. **X1**: vůz menší než 40 px (tečka) se **nepřebarvuje**, divák barvu nerozliší (pravidlo tabulky stavů „pokud ≥ 40 px“ platí i pro lak); přebarvit jen snímky s maskou 37–63.
3. OpenCV je v `nastroje/setup.sh` (commit 2026-11-05).
4. **W4 Guards Red** (režisér prohlédl realismus_W4_G1.jpg): lak působí věrohodně, ALE **červená na horním rámu čelního skla** (originál černý) a posunutá výluka kola
   v 5256–5263 (červený nádech na pneu, šedá skvrna na blatníku) jsou vady, které kritik najde. Opravit výlukou rámu skla (kotvy po 6 snímcích, homografie z karoserie) a kotvou kola
   v 5256–5263; když ani potom na 100 % výřezu neprojde, pro W4 cesta B. Rozhoduje verdikt kreativního ředitele bloku A.
5. **Kola v bronzu ve W11 a W6**: kde má kolo ≥ 40 px (W11 konec 364,6–365,4, W6 19,5–19,98 výstupu), kotvy kol ano; menší se neřeší.
6. Nástroje a skripty commituje režisér průběžně (`prebarvi.py` s novými volbami je v gitu).

## Odpovědi režiséra na otázky kreativního ředitele k bloku A (2026-11-05, závazné pro animátora B)
1. **Kotva v POV**: souhlas s návrhem KŘ. Na 3,15–3,23 se pilulka smrští do semínka a to odejde rozostřením (ROZ-OUT 0,08 s), POV 3,23–4,20 je bez UI. Na 4,22 (první snímek W4)
   se semínko znovu nakreslí (0,08 s) a z něj vyroste pilulka pro větu 2 stejným tahem jako 0,08–0,32 = rým s háčkem. Výjimka z D10 (semínko na ~1 s zmizí) je zdůvodněná:
   v POV není klidná plocha a pilulka na ruce řidiče je horší vada. Přesun semínka do nebe ne (pohyb bez příčiny, D6).
2. **Střih kaňon → POV 3,233**: maskovat průchodem rozostřením (oprava 5 KŘ: σ 0 → 16 px ease-in / 16 → 0 ease-out, +0,2 EV ve vrcholu, hranice na výstupním snímku C050) = schváleno,
   nový typ přechodu ROZ. Kaňon zůstává.
3. **Pásy a výšivka Weissach RS na F1** zůstávají červené (pásy jsou samostatná volba konfigurátoru, výšivku nejde konfigurovat). Kritérium „po 13,47 nikde čitelný karmín“ platí
   pro Race-Tex / kůži sedáků, ne pro pásy.
4. Postup: animátor B dělá opravy 1–10 KŘ souběžně s blokem B; opravené desky (W4, W7 U2, M8, F1) a snímky 3,10–4,30 a 7,95–8,06 zkontroluje kolo 1 kontroly na 100 %.
   GT Silver: když ani po opravě 1 nebude nárazník na 100 % čistý, místo stříbrné **Black** (A1), jak navrhl KŘ.

## Odpovědi režiséra zvukaři (2026-11-05)
(1) Boom nechat (RMS +4 dB nad vrcholem, +0,6 LU v okně 100 ms). (2) Tiky odometru přepočítá režisér z funkce rolování ve scéně po renderu bloku B, ding na první ustálený
snímek 500 (C045, C047). (3) Kliky podtrhu na dosednutí v obraze, průjezdy na nejbližší bod vozu, švihy CLONA / LET / WIPE / MORF na střed pohybu: posune režisér po renderu.
(4) sklo_pop 15,50 (růst karty čísla) nechat. (5) Tempo volně 69,5 BPM nechat. (6) `master_zvuk.sh` se samotnými efekty: verze bez hudby zůstává nenormalizovaná (jako V004);
oprava nástroje (snížit i TP loudnormu o přesah) zapsána jako C052, udělá ji režisér mimo výrobu.

## Test techniky (animátor, 2026-11-04 → 2026-11-05 po restartu kontejneru)
**Výstup**: `media/projekty/005-porsche/test/test_technika_v2.mp4` (1920×1080, 60 fps, 3,60 s = 216 snímků; v1 `test_technika.mp4` pro srovnání), varianty T8
`t8_strih.mp4` / `t8_most.mp4` / `t8_wipe.mp4`, scéna `test_technika_v2.html`, kontroly `test/kontrola/v2/` (pás `pas_v2.jpg`, klíčové snímky 100 %
`klic_v2_0.50.png` nájezd skrz erb · `klic_v2_1.40.png` návrat linkou · `klic_v2_2.55.png` MORF, srovnání `t8_srovnani.jpg`, `W6_spz_v2.jpg`, `W11_okraj_AB.jpg`, `morf_v2.jpg`),
stav a pořadí dávek `test/STAV.md`, skripty `test/_skript/` (`test_lut.py`, `test_maska.py`; z `nastroje/` přesunuty, C038).
**Výřez**: 0,00–0,70 POV M7 (moodcut 8,08–8,60) + ZOOM skrz erb → W4 · 0,70–1,07 W11 (365,00–365,40, Gentian Blue) + vzorky v pilulce · T8 · 1,07–1,13 W6a (278,04–)
· [testovací skok] 1,13–3,60 W6 280,44–283,40: návrat 1A → originál linkou (280,45–281,41), MORF rámce (282,0), sklo + průjezd za sklem.
**Čas výpočtu**: render 16 s na 1 s videa (`--sub 4`, `--sub-rychle 8`), 23 s na 1 s se `--sub-rychle 16` v rychlých úsecích (nutné pro MORF); celé video odhad 30 s × 16–23 s ≈ 8–12 min.
BiRefNet 25–32 s na snímek (CPU), LUT 2–3 s na snímek. Masky celé stavby (W4 od 209,0, W7, M8, X1, W11, W6 do 281,41 ≈ 330 snímků zdroje) ≈ 2,5–3 h → po dávkách se zápisem do STAV.md.

| technika | výsledek | měření | verdikt |
|---|---|---|---|
| **A: LUT v masce, W6 280,5–281,4 (návrat)** | lak vypadá jako lak, odlesky a stíny ve tvaru, SPZ, světla, sklo, pneu beze změny (v1 měla výluku SPZ o 60 px výš → modrá SPZ a ostrý šedý pruh na nárazníku, opraveno) | peří 2,0–5,3 px (posun 6–10,6 px/snímek zdroje) · blikání max ΔL 0,91 % (< 2 %) · ΔE proti rendru 1A **8,2** (v1 13,9, nad limitem) · **rozdíl proti originálu po návratu = 0** (max 0, 0 px mimo UI, 4 snímky 1,95–2,40 na PNG) | **projde** |
| **A: W11 rozmazaný průjezd 365,0–365,5** | v1 přesycená elektrická modrá (chroma 37 proti 22 v rendru) + modrý „opar“ v rozmazu střechy přes nebe + zrnitý okraj masky = vypadalo jako AI; v2 (chroma × 0,65, horní mez L 80 pro směs s nebem, uzavření masky 9 px, peří podle hran u okraje obrazu) věrohodná tmavá metalíza | ΔE 6,9 · peří 2–40 px · blikání relativně ke zdroji max 4,8 % (nad 2 %, ale v rozmazu neviditelné) · **snímky 365,44 a 365,48 BiRefNet nenajde** (maska 5 578 a 1 612 px) → vůz by na 2 snímky zešedl | **projde jen do 365,40**; mírně fialový nádech (a* 9 proti 5) |
| **(1) PRŮJEZD-WIPE T8** | **neprojde**: vůz ve W11 přijíždí zdálky a odjíždí vlevo dole, nikdy nekryje nebe ani pravou polovinu → kumulativní maska odkryje jen pás silnice; v1 to dořešila „závěsem“ za zadní hranou = svislý šev přes nebe po celou dobu průjezdu (čte se jako vložený wipe). Náhradní W2 / W9 mají průjezd stejně nízko | `t8_srovnani.jpg` (3 varianty) | nahradit **střihem v pohybu** (viz doporučení) |
| **(2) MORF rámce + sklo** | pilulka roste na celý obraz, uvnitř skutečně rozostřená deska (σ 6 = 12 px) + 72 %, šedý vůz projíždí za sklem jako rozmazaný stín; věta 8 se po slovech přelévá z pravého zarovnání do středu 48 → 72 px | bez rozmazání podle rychlosti se letící slovo rozpadlo na 8 kopií podsnímků (100 px/snímek); opraveno rozmazáním textu podle rychlosti + 16 podsnímků | **projde** |
| **(3) vzorky v pilulce** | řada 5 koleček z tečky 0,12 s, podtrh pod vybraný 0,08 s, smrštění 0,08 s, čitelné jako „klik“ v konfigurátoru; text uvnitř skla (v1 přetékal mimo pilulku, opraveno ořezem) | – | **projde**; barvy vzorků zatím odhad, změřit z rendrů |
| **(4) nájezd skrz erb (POV)** | v1: jen 2,6×, erb se prolínal přes ostrou W4 = dvojexpozice. v2: nájezd do stopáže 1 → 5 (mocnina 2,5), kotva erbu → (960, 900), σ desky 0 → 9 (efektivně 45 px), W4 přichází z σ 24 se zvětšením 1,25 → 1 a prolnutí jen mezi dvěma rozostřenými deskami (0,48–0,52) | erb vyplní ≈ 40 % obrazu, zbytek tmavý náboj volantu | **projde** jako jeden nepřerušený nájezd; erb nepřekreslen |

**Realismus celkem**: W6 návrat a MORF působí jako skutečná reklama (zásah se nepozná). W11 průjezd v pohybu projde, ve stopce je vidět mírně fialová modrá. Jako koláž působila jen
v1 (wipe se švem, přesycená modrá, zrnitý okraj masky).
**Nová obecná chyba (návrh C050)**: výměna desky 30 fps padá přesně na čas výstupního snímku, takže závěrka zprůměruje dva zdrojové snímky a na střihu ve stopáži vznikne 1 prolnutý snímek
obou záběrů (viděno u všech 3 variant T8). Oprava: desku i úsek vybírat z času zaokrouhleného na výstupní snímek (`casDesky` / `snimekDesky`, nově ve `nastroje/vzory/scena.html`).
**Doporučení pro stavbu**:
1. **T8 = střih v pohybu na zdroji 365,40** (poslední snímek s největším pokrytím rozmazanou karoserií), W11 363,00–365,40, W6 od 278,08 (= 18,00 výstupu); pilulka ho přežije. Varianta „most“
   (rozmazaný vůz z W11 1 snímek přes W6) nic nepřidá a hrozí koláží. Nebo KŘ zvolí jiný typ přechodu, protože „střih ve stopáži“ už je T7.
2. LUT: `CHROMA_S` 0,65 (rozmaz) až 0,8 (ostrý vůz), `LMAX` 80 u průjezdů přes nebe, `UZAVRENI` 5–9 px, `PERI_HRANY=1`; výluky SPZ změřit po snímcích (prahováním), ne odhadem.
3. Nájezd skrz erb zvětšit na 7×, aby erb vyplnil obraz (partitura „erb vyplní obraz“). Nad 5× je zdroj už jen rozmazaná skvrna, takže to nevadí.
4. Věta 8 začíná s MORF (20,72), ne 20,92 (jinak prázdná pilulka 14 snímků, C046, a přelití není vidět, protože MORF je z 90 % hotový).
5. Render: `--sub-rychle 16` v úsecích MORF a ZOOM; text v MORF rozmazávat podle rychlosti.
**Změny časů (C045)**: věta 8 slova 20,72 · 20,87 · 21,02 · 21,17 · 21,32 (bylo 20,92 + 0,15) · T8 průjezd-wipe 17,67–18,10 → střih 18,00 (W11 do zdroje 365,40, W6 od 278,08) — návrh, čeká na rozhodnutí.
**Nezpracováno v tomto testu**: W7 (masky 19/25, LUT G1 jen 5 snímků), W4 jen 1 snímek, M8 kola, X1. Patří do přípravy desek.

## Zvuk v1 (zvukař, 2026-11-05; k partituře + „Rozhodnutí režiséra po testu techniky“, obraz ještě není hotový → časy SFX posune režisér, C045)
**Výstupy** (`media/projekty/005-porsche/`): `hudba.wav` + `hudba.json` (30,0 s), `zvuk/sfx_v1.wav|json`, **`zvuk/zvuk_v1.wav`**, **`zvuk/zvuk_bez_hudby_v1.wav`**
(jen efekty v úrovni mixu, nenormalizovaná, jako V004), `zvuk/zvuk_v1_master.m4a` (kontrolní master), `zvuk/spektrogram_v1.png`, logy `zvuk/hudba_log_v1.txt`,
`zvuk/sfx_log_v1.txt`, stavba hlasitosti `zvuk/stavba_v1_mix.txt` a `zvuk/stavba_v1_master.txt`. Seznam událostí `projekty/005-porsche/sfx_udalosti.json` (v gitu, 35 událostí, u každé `popis` = na co v obraze sedí).
**Příkazy**:
`python3 -I nastroje/hudba.py --nalada hora --delka 30 --vrchol 13.87 --konec 27.65 --out media/projekty/005-porsche/hudba.wav` ·
`python3 -I nastroje/sfx.py --udalosti projekty/005-porsche/sfx_udalosti.json --delka 30 --out …/zvuk/sfx_v1.wav --hudba …/hudba.wav --mix …/zvuk/zvuk_v1.wav --bez-hudby …/zvuk/zvuk_bez_hudby_v1.wav --ticho 27.65-27.84` ·
`nastroje/master_zvuk.sh …/zvuk/zvuk_v1.wav …/zvuk/zvuk_v1_master.m4a`.

**Nálada `hora`** (nová v `nastroje/hudba.py`, samostatná cesta `aranzuj_hora` / `mixuj_hora` / `uloz_hora`; časy proměn `HORA_BODY`, přepisuje `--body jmeno=cas,…`):
F dur, akordy z `luxusni` v barvách maj9 / m9 / add9, **bez bicích a bez dropu**. Tempo volně: doba = (kadence − vrchol) / 8 = 0,864 s (**69,5 BPM**), doby pak padnou
i na 6,96 a 27,69. Nástroje: plocha (rozladěné pily + tělo kořen/kvinta kolem D3), smyčce od swellu, tlumený klavír, měkká basa se swellem (sinus + 2.–3. harmonická),
„vzduch na hoře“ (šum 1,5–7 kHz s poryvy, velmi tiše), dozvuk rt60 3,3 s, předzpoždění 30 ms; měkký „tep“ (taiko pod 900 Hz, −20 dB) jen 15,60 · 17,32 · 19,05.
Průběh: **0,00** jediný tón klavíru A4 (háček) · **2,60** plocha Fmaj9 · 4,22 Dm9 · 6,96 beze změny · **7,99** Bbmaj9 s měkkým akcentem (náběh 0,25 s, ne úder) ·
**9,86–10,76** Gm9 + swell **+2,0 dB** (změřeno) · 12,05 C9sus4 · **13,62 nádech −6,0 dB** (změřeno 13,40–13,60 → 13,75–13,86) · **13,87 VRCHOL** Bbmaj9 o oktávu výš,
melodie klavíru A5 G5 F5 | E5 C5 D5 | F5 E5 | D5 C5 Bb4 → **A4 na kadenci** · 15,60 Fmaj9/A · 17,32 Dm9 · 18,84 Gm9 · 19,98 C9sus4 → 20,35 C9 → **20,78 Fmaj9 (kadence do tóniky)** ·
**20,72–21,02 dolní propust → 2 kHz** (uvnitř skla; energie nad 2,5 kHz −13 dB proti okolí), 22,20–22,44 se otevře · 23,58 Bbmaj9/F (prodleva F v base, erb) · 25,96 Fadd9 ·
decrescendo · **fade 27,40–27,65** · **ticho 27,65–27,85 = digitální nula** (i dozvuk) · 27,85–30,00 tichý pad Fadd9 pod podpisem (náběh 0,5 s, fade 0,6 s na konci).
Uloženo lineárně: vrchol 13,87–17,60 = **−16,0 LUFS**, háček −25,4 (jeden doznívající tón), jízda −23,2, návrat −18,7, logo −19,7, podpis −28,0; integrálně −19,9 LUFS.
Měkké nasycení špiček (koleno −13, strop −8,5 dBFS, 4× převzorkování) jen na špičkách ploch ve vrcholu: bez něj by master nešel lineárně (viz chyby).
Pásma hudby: sub 5,4 · basy 37,9 · **středy 49,3** · horní středy 6,9 · výšky 0,5 %; oktávy 250 Hz–8 kHz bez skoku > 9 dB (nejvíc 4 → 8 kHz −7,4) → **bez VAROVÁNÍ (I7)**.
`hudba.json`: `bpm` 69,46 (`bpm_volne`), `doba`, `doby` (mřížka od vrcholu), `vrchol`, `konec`, `body` (všechny časy), `udalosti`, `udalosti_nastroju` (klavir, akord, basa, tep, podpis_pad).
**Ostatní nálady beze změny**: vazna, drza, luxusni, pohodova, sportovni, luxsport (+ `--motor elektricky`) vyrenderovány před a po změně (25 s, drop 7,5, konec 22,5): WAV i JSON **bit po bitu stejné** (sha256).
Hora je deterministická (2 rendery, stejný hash). `nastroje/sfx.py` jen přidané typy: výstup V004 (`projekty/004-bmw-jizda/sfx_udalosti.json`) před a po změně bit po bitu stejný.

**SFX** (tiché, jen na stavy, 35 událostí / 30 s; nové typy v `sfx.py`: `sken` 0,3 s, `sken_dlouhy` 0,9 s, `sken_svisly`, `sken_navrat` (pásmo dolů), `prujezd_mekky`
(vzduch + pneumatiky, motor tiše), `prujezd_za_sklem` (za dolní propustí 1,2 kHz), `boom_podpis`; tóny F dur jako hudba):
0,20 sklo_pop pilulka · 2,58 hover kompaktní pilulka · 4,22 ponor nájezd skrz erb (vrchol = první snímek W4) · 5,86 detent tečka · 6,61 / 6,665 tiky rozvinutí vzorků + 6,72 klik
podtrhu (= „3 tiky“, rozestup 55 ms) · 7,08 sken (střed linky 1) · 7,99 sklo_pop EXPL · 8,32 · 8,52 · 8,72 · 8,92 kliky scrollu (výšky 1 · 1,12 · 1,26 · 1,335) · 9,66 klik ·
10,31 sken_dlouhy (střed linky 2) · 10,98 měkký švih CLONA · 11,20 klik · 11,27 klik_kov ráfek (posunut 30 ms za klik, C047) · 12,00 švih LET svisle · 13,02 klik ·
13,30 sken_svisly (sedadla) · 13,77 švih WIPE (plné krytí, hudba v nádechu) · 15,50 sklo_pop karta čísla · **15,67 · 15,73 · 15,804 · 15,911 tiky přenosů stovek** ·
**16,32 ding** (první ustálený snímek 500) · 17,97 prujezd_mekky (W11 vůz projíždí vlevo, nejbližší bod před střihem 18,00) · 19,80 klik · 20,46 sken_navrat (60 % linky 4) ·
20,82 švih MORF rámce · 21,83 prujezd_za_sklem · 23,58 tah erbu (F6) · **27,85 boom_podpis**.
Změřené vrcholy: **odchylka 0,0 ms u všech 35** (ve stopě nejvýš 6,8 ms u CLONY, kde se překrývá s dozvukem), v tichu 27,65–27,84 žádný efekt (−240 dBFS).
Efekty proti hudbě v okně 100 ms −22,9 až −8,0 LU (vše pod hudbou); jediná výjimka je boom (hudba v tu chvíli ztichlá, varování `sfx.py` je záměrné).

**Mix a master**: `zvuk_v1.wav` 48 kHz stereo 24 bit, špička −8,0 dBFS (boom), −20,1 LUFS; master **lineárně +6,1 dB → −13,8 LUFS, −1,9 dBTP po AAC** (1. pokus, loudnorm v lineárním režimu,
stavba se nemění). Pásma mixu: sub 6,5 · **středy 47,8 %** (master stejně).
**Stavba hlasitosti (C032)**, master, LUFS po úsecích: háček −19,2 · 2,6–4,6 −20,7 · 4,6–6,6 −18,4 · 6,6–8,6 −17,7 · 8,6–10,6 −17,2 · 10,6–12,6 −14,9 · 12,6–13,6 −15,1 ·
**vrchol 13,87–15,87 −9,7** · 15,87–17,6 −10,4 · 17,6–19,6 −12,2 · 19,6–21,6 −12,3 · 21,6–23,6 −13,0 · 23,6–25,6 −13,6 · 25,6–27,4 −15,3 → stoupá k vrcholu, pak decrescendo.
RMS 50 ms max: háček −14,9 · jízda −16,3 · **vrchol −12,0** · návrat −13,2 · logo −14,5 · **boom −8,0 dB = nejhlasitější místo videa (+4,0 dB nad vrcholem)**;
K-vážená hlasitost 100 ms: boom −7,9 LUFS proti nejhlasitějšímu místu hudby −8,4 (+0,6 LU). Po 0,5 s v `zvuk/stavba_v1_master.txt`.

**Pro režiséra (C045)**: (1) tiky odometru jsou **odhad** z ease-out cubic 000 → 500 za 0,70 s (přenosy stovek 0→1…3→4); po scéně je přepočítat z funkce rolování, ding 16,32 nechat
na prvním ustáleném snímku. (2) Průjezdy 17,97 a 21,83 posunout na skutečný nejbližší bod vozu v obraze. (3) Kliky podtrhu jsou na časech ze sloupce SFX (6,72 · 9,66 · 11,20 ·
13,02 · 19,80); kdyby podtrh v obraze **dosedal** až na konci pohybu (např. 6,80), posunout na dosednutí. (4) Švihy (CLONA 10,98, LET 12,00, WIPE 13,77, MORF 20,82) jsou na středu
pohybu = nejvíc rozmazání; po renderu ověřit. (5) Hudbu kvůli posunům SFX neměnit; když se posune vrchol nebo kadence, přegenerovat s `--vrchol` / `--body`.

## Výroba: blok A (animátor, 2026-11-05)
**Co je hotové a kde**
- `nastroje/prebarvi.py` (nový ověřený nástroj z `test/_skript/test_lut.py`): `lut` (LUT 1H → cíl z pixelově zarovnaných rendrů, Lab, 64 binů; ověřeno: LUT bitově shodné s testem),
  `sekvence` (přebarvení v masce karoserie: medián masky 3 snímky, eroze 1 px, peří = max(2, k × posun), `--vnitrni` = peří uvnitř karoserie, výluky / `--jen-v`,
  výpočet jen ve výřezu bboxu; měří blikání proti zdroji a ΔE proti rendru), `sleduj` (výluky SPZ / světel / skla / kol / kapoty zadané na kotevních snímcích
  se sledují homografií z optického toku celé karoserie, mezi kotvami se prolnou), `propaguj` (oprava masky, kde BiRefNet selže), `nahled`. **Potřebuje OpenCV**
  (`pip install opencv-python-headless`, doplnit do `nastroje/setup.sh`).
- Projektové skripty `media/projekty/005-porsche/_skript/`: `desky.py` (desky orig + jednotný grade, `graduj` pro přebarvené varianty), `rozostreni.py`
  (předpočítané Gauss / vodorovné rozmazání pro T1, T2), `f1.py` (fotka F1 ve 3 vrstvách × 2 interiéry), `data_desky.py` (→ `scena/data_desky.js`),
  `w7_laky.sh`, `w7_sleduj.py`, `m8.sh`, `prebarvi_b.sh` (X1 / W11 / W6 pro blok B), `mrizka.py` (výřez s mřížkou pro zadávání kotev).
- Desky: `desky/<kód>/orig/NNNNN.jpg` všech 8 úseků (W1 78, M7 48, W4 114, W7 90, M8 31, X1 64, W11 60, W6 133; index = snímek zdroje 25 fps, ověřeno pixelově
  proti `src/` masek), přebarvené varianty `desky/<kód>/<lak>/` (+ `_png` bez gradu), LUT `desky/lut/`, kotvy `desky/kotvy.json`, výluky `desky/vyluky_sled.json`.
- Grade (Past 4): jedna křivka pro všechno (stíny +3 %: y = x + 0,03·(1−x)³, výšky beze změny), moodcut navíc gama 0,93 (střední jas +≈5 %, walkaround L 38–40 ×
  moodcut 24–28); fotka F1 chroma × 0,88, b* −2 + stejná křivka; zrno 3 dlaždice se seedem (overlay 6 %) na stopáži i fotce. Přebarvené varianty dostávají stejný grade,
  takže mimo masku je rozdíl proti orig 0.
- Scéna `media/projekty/005-porsche/scena/scena.html` (blok A hotový, moduly `A_`, kontrola kolize klíčů `pridejCasy`; blok B přidá `B_`): async `seek` dočítá jen desky,
  které čas potřebuje (mezipaměť ≤ 90 desek), C050 (`casDesky`), semínko, pilulka s tečkou / vzorky / podtrhem, věty po slovech z rozostření, 3 skenovací linky,
  LET (T1), ZOOM skrz erb 7× (T2), EXPL (T3), CLONA (T4), ráfek z náboje, LET svislý (T5), F1 2,5D, WIPE (T6, rozmazání pohybem analyticky po řádcích), X1 pod wipe.

**Přebarvení: měření (kritéria: blikání < 2 %, ΔE < 12, bez lemu, SPZ / světla / sklo / pneu beze změny)**
| záběr | lak | snímky zdroje | blikání max / medián | ΔE medián / max | peří | verdikt |
|---|---|---|---|---|---|---|
| W4 | G1 Guards Red | 5237–5270 | 0,75 / 0,20 % | 8,5 / 9,4 | 2–7,5 px | projde s výhradou (viz nedostatky) |
| W7 | G1 | 7085–7095 | 5,6 / 1,0 % (7085–7090 vůz uříznutý, malá plocha laku) | 6,8 / 21,7 (tamtéž) | 2–5,6 | projde |
| W7 | A1 Black | 7093–7101 | 1,8 / 0,5 % | 4,0 / 4,3 | 3–7 | projde |
| W7 | D7 Shark Blue | 7099–7107 | 0,3 / 0,2 % | 11,5 / 12,0 | 3–7 | projde (na hraně ΔE) |
| W7 | N2 Ruby Star Neo | 7105–7113 | 0,2 / 0,1 % | 6,4 / 6,6 | 2–5 | projde |
| W7 | U2 GT Silver (`--l-hladke 4 --detail 0,55`) | 7111–7168 | 0,67 / 0,12 % | 7,5 / 9,0 | 2–4,9 | projde (jemná tmavá textura na nárazníku) |
| W7 | 1A Gentian Blue | 7139–7174 | 0,91 / 0,21 % | 2,8 / 2,9 | 2–3,1 | projde |
| M8 | 1A (`--tma 6,14`: blatník ve stínu L ≈ 17) | 216–246 | 2,3 / 0,5 % (stín, rozmaz) | 9,2 / 10,5 | 2 | projde (blikání max těsně nad 2 %) |
| M8 | ráfek 348 Satin Neodyme (jen elipsa ráfku) | 216–246 | 1,9 / 0,5 % | 2,3 / 4,2 | 2 | projde, rotační rozmazání zůstává |
| F1 | lak 1A, ráfek 348, 53 → 51 | fotka | – | lak L 15 a 6,5 b −21 (render 1A v2: 9,7 / 2,5 / −16,4); interiér → L 68 a −3,4 b −3,5 (render 51: 66 / −5,8 / −2,1) | – | projde |

**Pilulka: změřené šířky (Barlow 500, 48 px) a levá hrana** (pravá hrana 1824; věta = 56 + text, popisek s tečkou = 91 + text, vzorek + 26 px)
| obsah | text px | šířka | levá hrana |
|---|---|---|---|
| Still deciding? Keep driving. | 577,7 | 634 | 1190 |
| Configure it. On the road. | 521,9 | 578 | 1246 |
| ● Vanadium Grey Metallic (+ 4 vzorky při odchodu) | 482,3 | 573 (677) | 1251 (1147) |
| ● Guards Red | 238,5 | 330 | 1494 |
| 4 vzorky + ● Try them all. | 255,3 | 450 | 1374 |
| ● GT Silver Metallic (+ 3 vzorky) | 355,8 | 447 (525) | 1377 (1299) |
| ● Gentian Blue Metallic | 436,1 | 527 | 1297 |
| ● Satin Neodyme | 317,2 | 408 | 1416 |
| ● Carmine inside. (+ 2 vzorky) | 322,8 | 414 (466) | 1410 (1358) |
| ● Or Arctic. | 197,3 | 288 | 1536 |
| kompaktní (● + podtrh) | – | 84 | 1740 |
| (blok B) Kept the one you're driving. | 565,6 | 622 | 1202 |

**Výkon**: výřez 12,95–13,95 (F1 3 vrstvy + sklo + linka + wipe, `--sub 4 --sub-rychle 8`) = 49 s výpočtu na 1 s (CPU sdílený s výpočtem masek);
přechody s `--sub 8 --sub-rychle 16`: 0,4 s ≈ 35–37 s. Odhad bloku A (13,9 s) ≈ 12–15 min.
Plný render: `--sub 4 --sub-rychle 16 --rychle 2.40-2.75,4.00-4.40,6.88-7.31,7.95-8.10,9.78-9.90,10.70-11.06,11.20-11.56,11.90-12.20,13.00-13.60,13.60-14.05`.

**Odchylky od partitury a proč**
1. **M7 není celý POV**: zdroj 6,68–7,40 je přední sledovací záběr v kaňonu (vůz přijíždí), POV ruce na volantu začíná až na 7,44 (střih ve zdroji, snímek 186).
   Rozpis jsem nezměnil (jiný POV bez textu v povolených úsecích není): **2,60–3,23 kaňon, 3,23–4,20 POV**, na 3,233 je ve stopáži střih bez proměny
   (kompaktní pilulka ho přežije, snímek přesně na hranici, C050). Otázka pro režiséra.
2. **M8 o 0,10 s dřív**: zdroj 8,64–9,88 → výstup **10,92–11,95** (bylo 11,02–12,05), aby v otevírající se CLONĚ už běžel pohyb, ne zamrzlý snímek;
   11,95–12,05 drží poslední snímek během odletu nahoru (rozmazaný, sotva vidět). Proměna ráfku, popisek a odlet beze změny časů.
3. **EXPL 7,975–8,05**, plná plocha na výstupních snímcích 8,000 a 8,017 (partitura 7,99–8,02; jinak závěrka rozpůlí plochu, C028).
4. **Střed CLONY** = pravé zadní kolo W7 změřené na zdroji 286,9: (1182, 600), ne (1250, 800). **Ráfek M8**: náboj (883, 650), elipsa ráfku 50 × 285 px (kolo uprostřed, ne vlevo dole).
5. **LET svislý** = jeden S-pohyb 11,95–12,15 (M8 nahoru, F1 přímo pod ním, dosedne 12,15).
6. **Řady vzorků** zleva doprava, tečka vpravo = aktuální stav: lak [GT Silver, Shark, Gentian, Guards Red | ● Vanadium] · scroll [GT Silver, Ruby, Shark, Black | ● Guards Red],
   podtrh skáče zprava doleva · [Guards Red, Shark, Gentian | ● GT Silver] · kola [Satin černá, Satin Neodyme | ● stříbrná] · interiér [Black, Arctic | ● Carmine].
   Tečka přebírá novou barvu po smrštění řady (6,88 · 9,78 · 11,30 · 13,12; partitura u Gentian 9,98), ve scrollu ve stejném snímku jako vůz.
7. **Věty 1 a 2 bez tečky** (tečka = stav konfigurace; kompaktní pilulka v POV tečku má, 2,62–4,36), od 5,86 tečka stále. Podtrh v klidu = 24 px pod tečkou / pod začátkem věty,
   semínko 0,08–0,20 se natáhne na šířku pilulky, 0,32–0,44 se stáhne do podtrhu.
8. **Wipe**: pruhy 4 / 40 / 110 px (3 / 26 / 70 se v rozmazání pohybem ztratily), příjezd ease-out, odjezd ease-in (pruhy čitelné, když hrana zpomalí); rozmazání pohybem analyticky.
9. **Pilulka po „Or Arctic.“** se smrští 13,83–13,93 (bylo 13,77–13,87), aby text při odchodu nebyl oříznutý.
10. **F1**: kamera 1,015 → 1,065 (rezerva na posun vrstev), krajina +18 px, vůz −6 px, sedadlo řidiče −12 px (paralaxa 24 / 6 px), linka 3 jede přes rozsah sedadel 241–1080 px.
11. **Linky 1 a 2** jezdí mezi hranami masky vozu ±14 px v aktuálním snímku (sledují jedoucí vůz).

**Kontrola (media/kontrola/005-porsche/blokA/)**: `kontrolni_nahled/` (56 časů z tabulky Kontrolní snímky do 13,87, arch `nahled.jpg`), výřezy s podsnímky
`vyrez_2.40.mp4` (T1) · `vyrez_4.00.mp4` (T2) · `vyrez_7.95.mp4` (T3 EXPL) · `vyrez_10.88.mp4` (T4 + ráfek) · `vyrez_12.95-13.95.mp4` (F1 + linka 3 + wipe, měření výkonu) ·
`vyrez_13.55.mp4` (T6), pásy `pas/pas_T1…T6.jpg`, 100% realismus `realismus_W4_G1.jpg`, `realismus_W7_A1.jpg`, `realismus_W7_U2_1A.jpg`, `realismus_M8.jpg`.

**Pro blok B připraveno**: desky orig X1 / W11 / W6, LUT, `_skript/prebarvi_b.sh X1|W11|W6` (parametry z testu; W6 výluky z testu převedené na indexy zdroje 7011–7034,
6952–7010 bez výluk, vůz malý), `scena.html` s kontrolou kolize klíčů `B_`. **X1: vůz je vidět už od snímku ≈ 10 (tečka ~10–30 px), masky jsou jen 37–63** → rozšířit.
Kola bronz ve W11 / W6 zatím nejsou (vyžádá si kotvy kol jako W4; vůz většinou < 40 px).

## Výroba: blok B a render v1 (animátor C = pokračování animátora B po restartu, 2026-11-07)
**Opravy bloku A (verdikt KŘ, C043)**
| # | oprava | stav | jak |
|---|---|---|---|
| 1 | W7 U2 GT Silver skvrnitý | **Black místo GT Silver** (podle KŘ a režiséra) | U2 v2 (`--l-baze 14 --detail 0.7 --l-strop 82`) měla na nárazníku pořád skvrny (`desky/W7/_U2_v2`). Scroll **GT Silver · Ruby Star Neo · Shark Blue · Black** (8,32 · 8,52 · 8,72 · 8,92), Black drží 8,92–9,86, linka 2 Black → Gentian, popisek „Black“, řada vzorků [Black, Shark, Ruby, GT Silver \| ● Guards Red]. Přepočteno U2 7093–7100, N2 7098–7105, D7 7103–7110 (uzavření 9 = oprava 10 KŘ), A1 7093–7168 (`_skript/w7_laky.sh c`). |
| 2 | M8 sklo / sání | hotovo (animátor B) | klíč M8b, `--cerna 12,6`, peří 3 |
| 3 | W4 G1 kapota / rám skla | částečně | W4b (zúžená kapota, rám skla, křidélko) + W4d: polygon předního kola zúžený (byl šedý pás za kolem). Zkouška výluky jen tmavších pixelů v kapotě (`tmave`, nová volba `obe` v `prebarvi.py`) **neprošla** (karbon je na slunci stejně světlý jako lak → červené šmouhy), proto zůstává polygon. Šedý pás lakovaného okraje víka vlevo vedle karbonu zůstává (známý nedostatek). |
| 4 | kotva v POV na ruce | hotovo | 2,52–2,66 pilulka → kompaktní, 3,07–3,15 se smrští do semínka (84 × 3 px), 3,15–3,23 ROZ-OUT, POV 3,23–4,22 bez UI, 4,22–4,30 semínko znovu TAH (0 → šířka věty 2), 4,30–4,42 z něj vyroste pilulka, 4,42–4,54 podtrh se stáhne pod začátek věty |
| 5 | střih kaňon → POV 3,233 | hotovo | ROZ: σ 0 → 16 px (kvadraticky) 3,15–3,2333 \| 16 → 0 do 3,31, +0,15 expozice ve vrcholu, hranice = výstupní snímek 194 (C050), desky `M7/roz/*_b4|b8|b16` |
| 6 | EXPL závoj + záře | hotovo | plný kruh z tečky pilulky, poloměr ease-in (kubicky) do 2200 px 7,975–7,995, plná plocha 7,995–8,025 (celé závěrky snímků 8,000 a 8,017), smrštění do tečky 8,025–8,05; měkká jen hrana (1 px + rozmazání pohybem, max 20 % poloměru) |
| 7 | erb na 4,20 mimo střed | hotovo | střed erbu na desce 212 změřen (1070, 973), výška 173 px; nájezd 1 → 8×, kotva dojede na (960, 540), erb ≈ 1,28 × výška obrazu |
| 8 | F1 skvrny karmínu | hotovo (animátor B) | `f1.py` |
| 9 | prázdná pilulka | hotovo | šířka se smršťuje se zblednutím textu (2,52 · 7,92 · 9,22 · 9,64 · 10,88 · 11,94) |
| 10 | D7 / N2 víko | hotovo v rámci 1 | uzavření masky 9 px (peří D7 beze změny) |

**Blok B (scéna `scena/scena.html`, prefix `B_`, kontrola kolize klíčů)**
- X1 13,87–16,00 (Gentian jen 44–63, menší vůz se nepřebarvuje), nádech 13,87–14,15, věta 6 „Nowhere to be.“ 14,17 · 14,37 · 14,52, ven 15,27.
- Karta 500 PS: pilulka roste 15,40–15,60 na 420 × 200 (pravá hrana 1824, y 784–984), „PS“ 15,52, ODOMETR 15,62–16,32 (000 → 500 jen zdola, ease-out kubicky,
  přenosy stovek **15,670 · 15,730 · 15,804 · 15,911**, první ustálený snímek **16,32**), klid 16,32–17,42, číslo ven 17,42–17,52, karta zpět 17,45–17,60. Rozmazání
  číslic v kódu (vzorky přes závěrku sečtené `lighter`, u velmi rychlého válce souvislá šmouha), žádné kopie podsnímků. Karta přežívá střih 16,00 beze změny.
- W11 16,00–18,00 (zdroj 363,00–365,40; Gentian 9075–9134, ráfky Satin Neodyme 9120–9134), **T8 = střih v pohybu 18,00** (W6 od 278,08).
- W6 18,00–22,44: věta 7 „Tried every colour.“ 18,20 · 18,40 · 18,60 (ven 19,60), vzorky [Vanadium, Guards Red, Shark, Black \| ● Gentian] 19,66, klik pod Vanadium 19,80,
  smrštění 19,84, tečka Vanadium 19,92, linka 4 19,90 → 19,98–20,78 zprava doleva mezi hranami masky vozu (vlevo Gentian + bronz, vpravo originál), zpět do podtrhu 20,78–20,88;
  popisek „Vanadium Grey Metallic“ 20,22, ven 20,62–20,69. Od 20,78 originál 1:1.
- MORF rámce 20,72–21,02: pilulka se 20,62–20,72 roztáhne na šířku věty 8, pak roste na celý obraz, sklo = předpočítaná deska W6 σ 6 (12 px) + 72 %, věta 8 po slovech
  20,72 · 20,87 · 21,02 · 21,17 · 21,32 (600, 48 → 72 px, rozmazání podle rychlosti), podtrh pod střed (960, 600); skutečný šedý vůz projede za sklem 21,40–22,27;
  sklo → #010205 22,27–22,44, věta 8 ven 22,62–22,70.
- Logo 22,44–27,65 (canvas bez zrna): název „718“ (PDS SVG, bílý) + „Spyder RS“ (Barlow 600 72 px), PIS maskou 22,78–23,08; TAH 23,18–23,30 podtrh se stáhne
  a vyjede ke špičce štítu, 23,30–23,58 kreslí obrys erbu (z SVG porsche.cz, `scena/erb.js`) oběma směry nahoru, 23,58–23,78 výplň barevným erbem, obrys zbledne;
  název 24,08–24,28 o 60 px dolů; claim „Configured on the road.“ 24,32 · 24,52 · 24,67 · 24,87 (ven 26,22); WLTP doslova 24,62 (18 px, y 980); dýchání 1,00 → 1,02
  24,00–27,40; ROZ-OUT 27,40–27,65; ticho 27,65–27,842; **záblesk 27,842–27,875** (plná bílá přes celé závěrky snímků 27,85 a 27,867), doznění do 28,03;
  podpis „strihyontop“ 27,90–28,05 z bílé, disclaimer 28,15, dotlačení 1,00 → 1,02 až do posledního snímku.
- **W6 přebarvení** (`_skript/prebarvi_b.sh W6c` + doběh 7011–7035 s W6b): v1 předchůdce (bez výluk v 6952–7010) měla modrou SPZ, světlomety, čelní sklo i ráfky a moc sytý lak →
  výluky sledované optickým tokem (klíč W6s: SPZ, oba světlomety zúžené 0,9, čelní sklo; kotvy 6985 / 6997 / 7011), kola W6k, sytost 0,7; ráfky Satin Neodyme (W6r) 6985–7035.
  Měření: 6952–7010 blikání max 3,2 % (vůz malý), 7011–7035 max 0,9 %, ΔE 6,7–7,0; ráfky ΔE 3,0.


**Render v1**: `media/projekty/005-porsche/render/V005_obraz_v1.mp4` (1920 × 1080, 60 fps, 1800 snímků, 30,00 s; části `_cast_A.mp4` 0–18 s, `_cast_B.mp4` 18–30 s,
`--sub 4 --sub-rychle 16`, rychlé úseky 2,40–2,75 · 3,10–3,35 · 4,00–4,40 · 6,88–7,31 · 7,95–8,10 · 9,78–9,90 · 10,70–11,06 · 11,20–11,56 · 11,90–12,20 · 13,00–14,05 ·
19,88–20,00 · 20,60–21,10 · 23,15–23,62 · 27,80–28,08). Výkon: blok A ≈ 54 s výpočtu na 1 s (3 prohlížeče, CPU sdílené s přebarvením W6), blok B ≈ 48 s na 1 s (2 prohlížeče).
EXPL po kontrole snímků přepracován (kruh po výstupních snímcích) a úsek 6–11 s přerenderován (`_cast_A2.mp4`), vložen přesně po snímcích 360–659 jedním překódováním
(CRF 14, stejné parametry jako renderer; rozdíl mimo úsek ≈ 0,2 úrovně jasu).
**Výstupy**: `media/projekty/005-porsche/vystup/V005_v1.mp4` (zvuk `zvuk/zvuk_v1.wav` → `master_zvuk.sh`: −13,8 LUFS, −1,9 dBTP po AAC), `V005_v1_bez_hudby.mp4`
(`zvuk/zvuk_bez_hudby_v1.wav`, nenormalizovaná, C039), plakát `V005_v1_plakat.jpg` (20,45: linka 4 vrací Gentian → Vanadium, půl vozu modrá, půl šedá).
Kontrola `media/kontrola/005-porsche/v1-animator/` (zprava.txt, arch.jpg, pásy): skoky jen na plánovaných přechodech (2,60 LET, 3,233 ROZ, 8,00 EXPL, 12,05 LET, 13,87 WIPE, 16,00, 18,00, logo, záblesk);
„zamrzlý úsek“ 26,30–27,43 = klid loga podle partitury (jen erb + název, dýchání 1,00 → 1,02 je pod prahem detektoru); černá 27,65–27,85 = ticho podle partitury.
**Zvuk v1 je ke starým časům partitury**: SFX posune režisér podle seznamu změn časů (C045).

## Opravy v2 (animátor, 2026-11-07; nálezy kola 1 kritik + KŘ, rozhodnutí režiséra ke kolu 1)
| nález | stav | jak |
|---|---|---|
| ODOMETR > 500 (blokující) | hotovo | jedna hodnota v(t) ≤ 500 (ease-out kubicky 15,62–16,32) a z ní mechanický válec: jednotky plynule, desítky / stovky jen během poslední jednotky nižšího řádu (přenos) → čtení vždy ≤ 500, přenos 4 → 5 až 16,25–16,32 spolu s ding. Poloha válců podle výstupního snímku (casDesky), rozmazání v kódu = 3 slábnoucí kopie pod číslicí, stopa ≤ 0,5 výšky číslice → obrys číslice čitelný v každém snímku (kontrola `media/kontrola/005-porsche/v2-animator/odo_v2.jpg`). |
| W11 průjezd + přebarvení (KŘ blokující, kritik závažná) | hotovo, **odchylka od rozhodnutí režiséra 1** | 362,60–363,00 je ve zdroji jiný záběr (rozhovor, střih na snímku 9075) a leží v zakázaném úseku 360,16–363,00; X1 prodloužit nejde (ve zdroji mosaic střih na snímku 64 → detail pádla). Proto W11 = zdroj **363,00–365,00** (9075–9124) na 16,00–17,667 a **T8 = 17,667**, W6 začíná od začátku záběru 277,68 (6942, povolený úsek). Od 18,00 je obraz W6 totožný s v1 (stejné mapování snímků). Rozmazaný průjezd 365,00–365,40 vypadl. Přebarvení W11 znovu: sledované výluky W11s (čelní sklo + roll-bar, SPZ, světla, obě kola; kotvy 9095 / 9112 / 9124), `--l-baze 14 --detail 0,85` (kresba odlesků), `--cerna 20,8` (černé plasty, pneu), `--chroma-s 0,47 --hue −5` (odstín jako W7: Lab medián C 16,5, h 287°; v1 C 23,8, h 293°), ráfky Satin Neodyme 9100–9124 (kolo ≥ 40 px). SPZ z originálu (`_skript/spz_orig.py`). |
| W6 kola, pneu, plasty, plochá Gentian, lem (KŘ) | hotovo | masky 6942–6951 dopočítány (BiRefNet, po W11), výluky W6v_lak = W6c / W6b protažené na 6942 sledováním, kola znovu ukotvena ručně (6967 / 6976 / 6985: sledování W6c se u kol posunulo), lak `--l-baze 14 --detail 0,85 --cerna 20,8 --chroma-s 0,58 --hue −4 --vnitrni 1` (bez tmavého lemu, C 18,7, h 289°), ráfky bronz 6960–7035 (W6v_rafky). |
| CLONA 10,92 dvojexpozice | hotovo | kruh po výstupních snímcích (casDesky), neprůhledný, hrana 1,5 px + mírné rozmazání pohybem ≤ 20 % poloměru, poloměr ease-in do 1300 px, střed = střed zádě W7 nad SPZ (880, 470) |
| F1 pilulka na laku | hotovo | výřez fotky přiblížen 1,30 → 1,35 se středem (874, 470) px fotky 2160 × 1215 (kotva na místě): pod pilulkou je boční polstr sedadla / tmavý otvor dveří, lak jen vpravo za hranou pilulky; krajina nahoře zůstává |
| prázdná pilulka (C046) | hotovo | kompaktní 84 px do 12,17 / 14,14 / 18,17, rozvinutí 0,12 s, první slovo 2 snímky po začátku rozvinutí |
| WIPE | hotovo | 13,68–14,01 (plná plocha 5 snímků 13,80–13,87), pohyb plynulý příjezd / rychlý odjezd, po výstupních snímcích s rozmazáním na ¼ závěrky → ostré pruhy, červená hrana 3 px |
| logo zamrzlé 26,30–27,43 | beze změny | rozhodnutí režiséra 4 (záměrný klid) |
| LET T1 | hotovo | rozmazání od 2,38 (vůz ještě v obraze) |
| LET svislý | hotovo | kompozice M8 + F1 v poloze výstupního snímku, svislé rozmazání analyticky 2 průchody × 8 kopií (64 vzorků) |
| GT Silver bloky na difuzoru | hotovo | U2 7093–7100 znovu s `--tma 18,34` (tmavé plasty se zvedají plynule méně; `--cerna` dělal skvrny ve stínu nárazníku) |
| T2 prolnutí 4,217 | hotovo | čistý střih na výstupním snímku 4,20 mezi rozostřeným erbem a W4 σ 24 |
| erb bloky (KŘ) | hotovo | nájezd jen do 6×, od ~4× rozostření desky σ 9 → 20 (nové desky M7 b14 / b20) + 0,2 EV |
| MORF sklo (KŘ) | hotovo | během průjezdu 21,28–22,27 sklo σ 3 (nové desky W6 b3) a 38 % místo 72 %, pod větou eliptické ztmavení ≈ 900 × 200 px 60 % |
| linka 1 růžový pás (KŘ) | hotovo | všechny linky po výstupních snímcích, jádro 3 px 100 %, stopa ≤ 2 × 8 px |
| Arctic příliš bílé (KŘ) | hotovo | `f1.py`: L → 40 + L (bylo 52 + 0,75 L), medián L 61,6 (render 51: 66), plný kontrast textury |
| ROZ 3,233 (režisér 5) | beze změny | oba hodnotitelé průchod přijali („elegantní“), proto bez −0,6 EV |

**Změny časů (C045, pro zvukaře)**: T1 rozmazání od 2,38 (bylo 2,45) · T2 bez prolnutí (střih 4,20) · WIPE 13,68–14,01, plná plocha 13,80–13,87, střed švihu ≈ 13,84 (bylo 13,62–14,02) ·
rozvinutí pilulky 12,17 / 14,14 / 18,17 (bylo 12,00 / 14,02 / 18,08; slova beze změny) · ODOMETR tiky přenosů stovek 15,670 · 15,730 · 15,804 · 15,911, přenos 4 → 5 = 16,25–16,32 splývá s ding 16,317 (žádný tik kolem 16,00) ·
**T8 = 17,667** (bylo 18,00): střih v pohybu W11 → W6, průjezd / švih T8 o −0,333 s; vše od 18,00 beze změny.
**Nové / upravené nástroje**: `nastroje/prebarvi.py --hue` (otočení odstínu výsledku), `_skript/spz_orig.py`, `_skript/rozostreni.py` (W6 b3, M7 b14/b20), `_skript/prebarvi_b.sh W6v2 | W11v2`, `_skript/w7_laky.sh d`, `_skript/f1.py` (Arctic), `_skript/desky_masky.py` / `desky.py` (W6 od 6942).

## Průběh výroby
| kolo | kdo | co se dělalo | verdikt kritika | hlavní nálezy |
|---|---|---|---|---|

## Chyby během výroby
- (zvukař, zvuk v1) **Kontrolní master přepnul loudnorm do dynamického režimu a srovnal stavbu**: první mix měl poměr špička / hlasitost 17 dB (pily ploch −5,8 dBFS
  při −19,9 LUFS + boom s ostrým transientem −3 dBFS); na −14 LUFS bylo třeba +6 dB, lineárně to nešlo, loudnorm přešel do dynamického režimu → háček (−10,3) hlasitější
  než vrchol (−12,4) a boom o 3,8 LU tišší než hudba. Oprava: `uloz_hora` měkce nasytí špičky ploch (strop −8,5 dBFS), `boom_podpis` má tělo nejsilnější na náběhu
  a malý transient, boom −8 dBFS → master lineárně (+6,1 dB), stavba beze změny. **Prevence (návrh C052)**: u dynamické hudby (tichý úvod, vrchol) ověřit, že
  `TP_mixu + (−14 − I_mixu) ≤ −1,5`, jinak master nejde lineárně; stavbu RMS měřit i na dekódovaném masteru, ne jen na mixu.
- (zvukař) `master_zvuk.sh` na samotných efektech (`zvuk_bez_hudby_v1.wav`, −28 LUFS, jediný boom) nezkonvergoval (4 pokusy −17,9 → −18,4 LUFS, TP −0,9 dBTP): smyčka snižuje jen
  cíl I, loudnorm v dynamickém režimu ale drží TP na −1 před AAC. Verze bez hudby zůstává podle V004 nenormalizovaná v úrovni mixu (odvozený m4a smazán, C039).

- (animátor C) **W6 přebarvení v1 bez výluk v 6952–7010**: modrá SPZ, světlomety, čelní sklo i ráfky a moc sytý lak (výluky z testu platily jen pro 7011–7034, sekvence je mimo rozsah
  „přidržela“ nepoužité). Oprava: výluky sledované optickým tokem pro celý rozsah (W6s, kotvy 6985 / 6997 / 7011), kola W6k, sytost 0,7. **Prevence**: každý přebarvený úsek
  před vložením do scény projít na 100 % (SPZ, světla, sklo, kola) v celém rozsahu, ne jen v testovaném výřezu.
- (animátor C) **Partitura měřila W6 špatně**: „pravá hrana vozu 280,5 ≈ 1080“, na deskách je vůz velký už od 279,9 (pravá hrana 1490–1700). Pilulka na laku neleží jen proto, že spodek
  vozu je nad y 900 (bbox masek ≤ 898). **Prevence**: polohu vozu v partituře brát z bboxu masek / desek po snímcích, ne z odhadu ze zdrojového videa.
- (animátor C) **EXPL rozmazaný závěrkou se četl jako záře**: kruh roste ~400 px za snímek, 16 podsnímků z něj udělalo měkký radiální přechod (7,983 / 8,033). Oprava: poloměr podle výstupního
  snímku (`casDesky`), hrana 1 px. **Prevence (doplnit C028)**: plošné grafické proměny rychlejší než ~100 px za snímek kreslit po snímcích, ne rozmazávat závěrkou.
- (animátor C) **Spojení `concat -c copy` s `outpoint` / `inpoint` přidalo 2 snímky** (1802 místo 1800) a posunulo obraz o snímek (B-snímky na hranici GOP). Oprava: výměna úseku přes `trim` +
  `concat` filtr s jedním překódováním (CRF 14). **Prevence**: po každém spojení ověřit počet snímků a rozdíl proti původní verzi mimo vyměněný úsek.
- (animátor C) W4 kapota: výluka „jen pixely tmavší než okolní lak“ (`tmave`) neprošla, karbon je na slunci stejně světlý jako lak → červené šmouhy. Zůstává polygon (známý nedostatek).

- (animátor v2) **Rozhodnutí T8 předpokládalo zdroj 362,60–363,00, který je jiný záběr (rozhovor) a navíc zakázaný úsek**: zjištěno až po spuštění BiRefNet na 9065–9074 (zbytečně 10 masek, smazány). **Prevence**: před rozšířením úseku ověřit střihy ve zdroji (rozdíl sousedních snímků) a seznam zakázaných úseků (C044).
- (animátor v2) **Sledované výluky kol W6c ujely** (optický tok bral karoserii, kolo se vůči ní posouvá/otáčí) → modré pneu 18,5–18,8. Oprava: kotvy kol ručně po 9 snímcích (6967 / 6976 / 6985). **Prevence**: kola kotvit hustěji než karoserii a kontrolovat výluky náhledem `prebarvi.py nahled` na každém 5.–10. snímku.
- (animátor v2) **Výluka SPZ v režimu `tmave/obe` modrala značku** v rozmazaných snímcích W6 → SPZ vrácena z originálu polygonem (`_skript/spz_orig.py`). **Prevence**: SPZ vždy plnou výlukou (ne podle jasu).
- (animátor v2) Komentář `//` vložený doprostřed řádku pole klíčových snímků zakomentoval zbytek řádku → stránka bez `window.seek` (timeout rendereru). **Prevence**: po úpravě scény `node --check` na skriptech scény.

## Spotřeba tokenů
| agent / úkol | tokeny | akce nástrojů | čas |
|---|---|---|---|
| příprava: analytik (web, konfigurátor, stopáž) | neměřeno (notifikace ztracena restartem kontejneru) | – | 41,6 min |
| příprava: kreativní ředitel (koncept + partitura) | neměřeno (restart) | – | 22,4 min |
| příprava: oponent (revize partitury) | neměřeno (restart) | – | 21,5 min |
| příprava: animátor test, 1. běh (přerušen restartem) | neměřeno (restart) | – | 32,2 min |
| příprava: animátor test, pokračování po restartu | 203 477 | 87 | 23,5 min |
| režisér: masky BiRefNet na pozadí (skript, ne agent) | 0 | – | ~2,2 h CPU |
| výroba běh 1 (zvukař, animátor A, KŘ blok A, animátor B přerušen limitem využití 5 h) | 1 157 970 | 476 | 97,8 min |

## Verze
| verze | datum | soubor / kam doručeno | změny |
|---|---|---|---|

## Zpětná vazba (doslova)

## Poučení
