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
- **Skutečná stopáž se nepřebarvuje** (riziko nerealismu); barva se mění jen na rendrech konfigurátoru (D7), stopáž zůstává šedá.
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

## Režijní list (vyplní režisér před delegací)
- **Koncept jednou větou**:
- **Vzhled**: písmo, paleta (z porsche.cz), jazyk kamery
- **Rytmus**: řízeno větami na scénu (bez VO) / hudba odpočinková, délka 30 s
- **Akceptační kritéria pro kritika**: formát 1920×1080 60 fps 30,0 s · −14 LUFS / ≤ −1 dBTP · pravidla uživatele 1–8 · kontrolní seznam střihu (strih-vzor.md 6)

## Storyboard / střihová partitura
(kreativní ředitel)

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
