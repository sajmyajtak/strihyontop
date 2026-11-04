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

## Režijní list (kreativní ředitel, 2026-11-04; režisér doplní rozhodnutí)
- **Koncept jednou větou**: **Jedna nepřerušená jízda horami, při které červená linka konfigurátoru (semínko) přejíždí přes jedoucí vůz a mění mu lak, kola i interiér, a na konci ho
  jedním tahem zpět vrátí do Vanadium šedé, tedy do vozu, kterým divák celou dobu jel („Tried every colour. Kept the one you're driving.“).**
  Hrdina = **vůz v jízdě** (skutečná stopáž Porsche, Vanadium šedá 1H). Jediný doplněk = **„spec pill“** (kotva, D13): tmavá skleněná pilulka vpravo dole ve stylu
  konfigurátoru PDS s tečkou aktuální barvy a jedním řádkem textu; její **červený podtrh (#d5001c) je semínko** (D10): je na snímku 0, nakreslí pilulku, vyjíždí z ní jako
  **skenovací linka**, která proměňuje vůz, a na konci nakreslí erb Porsche. Úpravy za jízdy = **stavy hrdiny** (D8): lak (předveď rychle → zopakuj pomaleji, D15) →
  kola → interiér → výhled (jedno číslo 500 PS) → návrat k šedé (odkrytí původní stopáže = nejpoctivější proměna) → logo → podpis tvůrce.
- **Semínko**: červená linka 3 × 96 px vpravo dole (x 1728–1824, y 968) na snímku 0 → 0,08–0,32 s se natáhne a vyroste z ní pilulka (TAH) → v každé úpravě vyjede
  z pilulky jako svislá linka 3 × 1080 px přes obraz (za linkou je nový stav vozu), po proměně se vrátí jako podtrh → 23,10 s nakreslí obrys erbu Porsche → erb (logo).
  Barva vždy #d5001c, bez záře, 1 px měkká hrana, při rychlém pohybu směrové rozmazání 10–20 px.
- **Vzhled**: písmo **Barlow** (500 na pilulku a věty, 600 na claim a podpis, `media/projekty/005-porsche/znacka/`), paleta porsche.cz: canvas #010205, pilulka #010205 @ 72 % s 1 px
  okrajem #f6f6f8 @ 20 %, rádius 8 px (PDS), text #fafbff, tlumený #f6f6f8ab, akcent **#d5001c jen linka, tečka a tik**. Žádná žlutá (značka 12 h na volantu je žlutá, není to barva značky).
  Pilulka: výška 84 px, text 48 px, zarovnaná vpravo (pravá hrana x 1824, y 900–984), tečka Ø 18 px vlevo od textu. Kamera: **stopáž má vlastní kameru, digitálně nic nedotlačujeme**
  (výjimka T2: nájezd ≤ 1,12×); fotka interiéru jen pomalý posun 1,00 → 1,06.
- **Rytmus**: řídí ho **věty na obrazovce** v pilulce (3–5 slov, slova z rozostření v tempu řeči, obraz předbíhá slovo o 0,1–0,35 s) a proměny vozu; událost každých ~0,6 s
  (49 událostí / 30 s), bez metronomu. Hudba se skládá až k partituře (D12): pomalá, široká, bez dropu, vrchol = otevření výhledu 13,35 s, jediný úder = podpis 27,85 s.
- **Stopáž**: 25 fps → 60 fps **jen 1,2× (kadence 2:2)**, bez interpolace (V004). Všechny záběry Vanadium šedá, bez střechy, Weissach pruh na víku (je ve všech záběrech, nevadí).
  Rozpis úseků níže; každý úsek jen jednou (C044).
- **Prompt / šablona**: vlastní kostra z `prompt-motion/poznatky.md` 10 (+ 11.2 spojení s fotorealistickým produktem) a `strih-vzor.md`; zakázáno: záře, částice,
  prolínačky scén, třes kamery, text v rozích mimo kotvu, překreslený vůz, cokoli jako šablona.
- **Akceptační kritéria pro kritika**: 1920×1080, 60 fps, 30,00 s · −14 LUFS / ≤ −1 dBTP po AAC · pravidla uživatele 1–8 · partitura níže po snímcích (`strih-vzor.md` 6):
  v každém snímku 1 hrdina + 1 doplněk (pilulka), 0 tvrdých střihů v grafice, 7 střihů ve stopáži (T1–T8) vždy s přežívající pilulkou a maskovaných proměnou, příchody z rozostření
  0,1–0,25 s / odchody kratší, klid jen na přečtení, jedno číslo (500 PS, klid ≥ 1 s), přechody se neopakují, semínko na snímku 0 a zpět v logu, podpis tvůrce 2 s + disclaimer ·
  **realismus**: proměny laku jen uvnitř masky karoserie, odlesky a stín zachované, žádný lem, žádné blikání masky, barva vozu v každém záběru odpovídá aktuálnímu stavu
  (tabulka stavů níže) · **vůz jede** v 23,4 s z 30 (78 %) · zakázané úseky stopáže nepoužity.

### Rozhodnutí kreativního ředitele (režisér potvrdí nebo přepíše)
1. **Výchozí konfigurace ve videu = Vanadium šedá metalíza 1H + stříbrná kola + karmínový interiér** (vůz ze stopáže), ne bílá 0Q z odkazu; odkaz uživatele určuje model, ne barvu.
2. **Střecha se nemění** (ruční střecha nejde zavřít za jízdy, a claim modelu je „Open top“). Rendry se zavřenou střechou nepoužít.
3. **Úpravy laku a kol se dějí přímo na jedoucím voze ve stopáži** (nová technika, test před stavbou, níže). Záložní cesta B: proměna na pixelově zarovnaných rendrech
   `konfigurator/barvy/` vstupujících do obrazu v pohybu (V004 P2), vůz ve stopáži zůstává šedý; příběh funguje v obou cestách („zkoušel jsi, nechal sis šedou“).
4. **Interiér** = skutečná tisková fotka `fotky/newsroom/BX24I3HOD0015.jpg` (sedadla shora, krajina) s odbarvením karmínu na Arctic šedou v masce; rendry v7/v8 nepoužít (studio).
5. **Jedno číslo = 500 PS** (konfigurátor „Výkon (PS) 500 PS“); cena 4 214 780 Kč a další údaje do obrazu nejdou. Povinný údaj WLTP jen jako malý řádek na kartě loga.
6. Názvy voleb anglicky podle konfigurátoru Porsche (EN): Vanadium Grey Metallic, Guards Red, Black, Racing Yellow, Ruby Star Neo, Shark Blue, White, GT Silver Metallic,
   Gentian Blue Metallic, Satin Neodyme (kola), Black/Arctic Grey (interiér). Režisér ověří EN tvary na porsche.com (bez obcházení, C024).
7. Věty na obrazovce s tečkami jako claimy Porsche („Unfiltered driving pleasure. Open top.“): výjimka z E8 kvůli stylu značky.

## Storyboard / střihová partitura (kreativní ředitel, 2026-11-04)
Časy = výstup (60 fps, s), zdroj = čas ve zdrojovém souboru (25 fps, rychlost 1,2×). Typy: TAH · PIS · ROZ-IN / ROZ-OUT · LET · WIPE · ZOOM · MORF · EXPL · CLONA · ODOMETR · ZÁBLESK.
**Stavy hrdiny** (barva vozu v obraze, musí sedět v každém snímku): 0,00–5,30 Vanadium šedá (originál) · 5,30–5,55 přechod → **Guards Red** 5,55–6,70 · 6,70–7,325 scroll
(Black · Racing Yellow · Ruby Star Neo · Shark Blue · White · GT Silver, po 0,125 s) · 7,325–8,00 GT Silver · 8,00–8,90 přechod → **Gentian Blue** 8,90–20,20 (včetně fotky
interiéru, dronu, W11 a W6) · kola stříbrná → **Satin Neodyme** od 10,75 do 20,20 (i malé ve W11/W6) · interiér karmín → **Arctic Grey** od 12,40 · 20,20–21,00 návrat → originál.
Kotva = pilulka vpravo dole (pravá hrana x 1824, y 900–984) od 0,20 do 22,05, potom ve středu do 27,40 (91 % videa).

| # | prvek | příchod | typ příchodu | klid (s) | odchod | typ odchodu | co ho spojuje s dalším | věta / slovo |
|---|---|---|---|---|---|---|---|---|
| **S0 HÁČEK** | **W1** walkaround 119,04–122,16 → **0,00–2,60**: západ slunce, vůz 3/4 zepředu vlevo, hory, protisvětlo | | | | | | | |
| 1 | stopáž W1 (vůz jede, projede kolem kamery 2,05–2,45) | 0,00 | hotový obraz od snímku 0 (B6) | – | 2,45–2,60 | **LET**: 9 snímků vodorovného rozmazání z průjezdu + expozice +0,3 EV | **T1**: rozmazaná karoserie kryje střih do W4 | – |
| 2 | **semínko**: červená linka 3×96 px (x 1728–1824, y 968) | 0,00 | stojí od snímku 0 | 0,08 | 0,08–0,20 | MORF: natáhne se na 520 px (ease-out) | linka = podtrh pilulky | – |
| 3 | **pilulka (kotva)** 84 px, tmavé sklo | 0,20–0,32 | TAH/ROST z linky nahoru (0 → 84 px, kriticky tlumené) | do 22,05 na místě | 22,05–22,17 | MORF polohy do středu obrazu | obsah se mění uvnitř (D13) | – |
| 4 | věta 1 „Still deciding? Keep driving.“ | 0,32 · 0,47 · 0,85 · 1,00 | ROZ-IN po slovech 0,15 s (pauza po „?“) | 1,15–2,60 | 2,68–2,76 | ROZ-OUT 0,08 | nový text v téže pilulce | **věta 1** |
| **S1 PREMISA + ČERVENÁ** | **W4** walkaround 206,28–210,84 → **2,60–6,40**: vůz 3/4 zepředu, serpentina se svodidlem, přijíždí | | | | | | | |
| 5 | stopáž W4 | 2,60 | z rozmazání T1 (6 snímků dobrzdí, ease-out) | – | 6,20–6,40 | **ZOOM** 1,00 → 1,12 ease-in + ROZ 0 → 14 px (6 snímků) | **T2**: rozmazaná červená karoserie → rozmazaná červená záď W7 | – |
| 6 | věta 2 „Configure it. On the road.“ | 2,78 · 3,00 · 3,25 · 3,40 · 3,55 | ROZ-IN po slovech | 3,70–4,22 | 4,22–4,30 | ROZ-OUT | pilulka se přeznačí na konfigurační řádek | **věta 2** |
| 7 | tečka barvy Ø 18 px (Vanadium #6b7075) | 4,30 | ROZ-IN 0,10 | – | mění barvu | – | kaskáda: tečka → text +6 snímků (D14) | – |
| 8 | text „Vanadium Grey Metallic“ | 4,40 | ROZ-IN 0,15 | 4,55–5,38 | 5,38–5,45 | ROZ-OUT | stav = pravda (vůz je šedý) | popisek |
| 9 | tik: tečka → Guards Red, podtrh zabliká | 5,20 | 1 snímek | – | – | – | příčina pro linku | – |
| 10 | **skenovací linka 1 (předveď)** 3×1080 px | 5,22–5,30 | LET z pilulky k levé hraně vozu (rozmazání 20 px) | – | 5,30–5,55 přejede vůz zleva doprava (**0,25 s**), za ní lak Guards Red; 5,55–5,65 zpět do pilulky (ease-in) | MORF zpět na podtrh | stav vozu šedá → červená | – |
| 11 | text „Guards Red“ | 5,45 | ROZ-IN 0,12 | 5,57–6,52 | 6,52–6,58 | ROZ-OUT | popisek 0,15 s **po** začátku proměny (D1) | popisek |
| **S2 HRA S BARVAMI** | **W7** walkaround 283,40–288,10 → **6,40–10,32**: zadní sledovací, vůz uprostřed, blíží se, SPZ S PY 500 čitelná ke konci | | | | | | | |
| 12 | stopáž W7 (vůz červený) | 6,40 | z ROZ 14 → 0 px + 1,06 → 1,00 (6 snímků, ease-out) | – | 10,22–10,32 | **CLONA**: kruh ze středu pravého zadního kola, měkký okraj 8 px, 6 snímků | **T3**: v kruhu už běží M8 (zoom skrz kolo) | – |
| 13 | **scroll barev (předveď)**: tečka + celý vůz přepnou v 1 snímku: 6,70 Black · 6,825 Racing Yellow · 6,95 Ruby Star Neo · 7,075 Shark Blue · 7,20 White · 7,325 GT Silver | 6,70 | 6 kroků po 0,125 s, každý krok 1snímkový tik podtrhu | 7,325–8,00 (GT Silver) | – | – | rychlá verze → pomalá verze (D15) | – |
| 14 | věta 3 „Try them all.“ | 6,85 · 6,97 · 7,09 | ROZ-IN | 7,20–7,50 | 7,50–7,56 | ROZ-OUT | 0,15 s po prvním přepnutí | **věta 3** |
| 15 | text „GT Silver Metallic“ | 7,62 | ROZ-IN | 7,75–8,08 | 8,08–8,14 | ROZ-OUT | – | popisek |
| 16 | **skenovací linka 2 (zopakuj pomaleji)** | 7,92–8,00 | LET z pilulky k levé hraně vozu | – | 8,00–8,90 přejede vůz zleva doprava (**0,9 s = 3,6× pomaleji**), za ní Gentian Blue Metallic (odlesky krajiny v laku zůstávají); 8,90–9,00 zpět | MORF na podtrh | stav stříbrná → modrá | – |
| 17 | tečka → Gentian Blue + text „Gentian Blue Metallic“ | 8,20 | ROZ-IN | 8,35–10,42 (vůz se blíží, SPZ) | 10,42–10,48 | ROZ-OUT | 0,2 s po startu linky | popisek |
| **S3 KOLA** | **M8** moodcut 8,64–9,88 → **10,32–11,35**: přední kolo + blatník za jízdy (kolo vlevo dole), karoserie modrá od 1. snímku | | | | | | | |
| 18 | stopáž M8 | 10,32 | z CLONY | – | 11,25–11,35 | **LET svisle**: obraz odletí nahoru (−1080 px, 6 snímků, svislé rozmazání) | **T4**: fotka interiéru přijede zdola (jeden svislý pohyb = „pohled dolů do kokpitu“) | – |
| 19 | věta 4a „Wheels?“ | 10,42 | ROZ-IN | 10,55–11,22 | 11,22–11,28 | ROZ-OUT (s 4b) | slovo 0,1 s po objevení kola | **věta 4** |
| 20 | tečka → Satin Neodyme (bronz) + **proměna ráfku**: kruh z náboje ven, stříbrná → Satin Neodyme | 10,75–11,05 | CLONA z náboje (0,3 s) | 11,05–11,25 | – | – | stav kol (platí do 20,20) | – |
| 21 | věta 4b „Satin Neodyme.“ | 10,90 | ROZ-IN | 11,05–11,22 | 11,22–11,28 | ROZ-OUT | 0,15 s po startu proměny | věta 4 |
| **S4 INTERIÉR** | **F1** fotka newsroom BX24I3HOD0015 (sedadla shora, karmín, krajina; karoserie v záběru modrá, kolo bronz) → **11,35–13,35**; posun 1,00 → 1,06 + drift 20 px dolů | | | | | | | |
| 22 | fotka interiéru | 11,35 | LET zdola (dojede ease-out 6 snímků) | – (2,5D pohyb) | 13,20–13,55 | **WIPE** pruhy padají shora (#313639, #191f22, #eff0f1, červená 3px náběžná hrana): 0,15 s nájezd · 0,10 s plná #191f22 · 0,15 s odjezd dolů | **T5**: konec wipe = otevření výhledu (nádech) | – |
| 23 | věta 5a „Carmine inside.“ | 11,50 · 11,72 | ROZ-IN | 11,87–12,50 | 12,50–12,56 | ROZ-OUT | 0,15 s po příchodu fotky | **věta 5** |
| 24 | tečka → Arctic Grey; **skenovací linka 3 vodorovná** | 12,32–12,40 | LET z pilulky k horní hraně sedadel | – | 12,40–12,85 sjede shora dolů přes sedadla (karmín → Arctic Grey: odbarvení v masce + jas +35 %, textura zůstává); 12,85–12,95 zpět | MORF na podtrh | stav interiéru | – |
| 25 | věta 5b „Or Arctic.“ | 12,55 · 12,70 | ROZ-IN | 12,85–13,20 | 13,20 | kryje wipe | 0,15 s po startu linky | věta 5 |
| **S5 VRCHOL (výhled)** | **X1** mosaic 0,00–2,56 → **13,35–15,48**: dron nad serpentinou, hory, vůz od 14,6 malý vpravo (modrý) · **W11** walkaround 363,00–365,30 → **15,48–17,40**: lávová pláň, rovná silnice, vůz z dálky blíží se (modrý, kola bronz) | | | | | | | |
| 26 | stopáž X1 | 13,35 (vidět od 13,45 pod wipem) | z WIPE | – | 15,48 | tvrdý střih ve stopáži pod kartou | **T6**: karta 500 PS přežívá, obě krajiny široké, vůz malý | – |
| 27 | **karta čísla**: pilulka vyroste na 420×200 px (pravá hrana 1824, y 784–984) | 13,65–13,85 | MORF rozměru (kriticky tlumené) | – | 15,65–15,80 | MORF zpět na pilulku | kotva mění rozměr, ne polohu | – |
| 28 | popisek „PS“ (48 px, vpravo od čísla) | 13,78 | ROZ-IN | 13,88–15,65 | 15,65 | s kartou | kaskáda karta → PS → číslice (po 6–8 snímcích) | – |
| 29 | **číslo 500** (Barlow 600, 150 px): roluje zdola 000 → 500, odometrické rozmazání | 13,88–14,58 | ODOMETR 0,7 s (jen horší hodnoty, G9) | **14,58–15,65 (1,07 s)**, ding na 14,58 (ustálený snímek) | 15,65–15,78 | zblednutí | jediné číslo videa | **„500 PS“** |
| 30 | stopáž W11 | 15,48 | tvrdý střih pod kartou | – | 17,38–17,40 | **EXPL**: tečka pilulky exploduje do plné červené plochy (2 snímky) | **T7**: plocha se smrští zpět do tečky nad W6 (2 snímky) | – |
| 31 | věta 6 „Nowhere to be.“ | 15,85 · 16,05 · 16,20 | ROZ-IN | 16,35–17,30 | 17,30–17,36 | ROZ-OUT | – | **věta 6** |
| **S6 ROZHODNUTÍ** | **W6** walkaround 277,68–283,40 → **17,40–22,17**: vůz 3/4 zepředu z dálky mezi skalami (modrý), přijíždí, projede vpravo 21,70–22,17 | | | | | | | |
| 32 | stopáž W6 | 17,40 | z EXPL | – | 22,05–22,17 | **MORF kotvy**: pilulka sjede do středu, obraz pod rozmazanou karoserií ztmavne do #010205 (0,12 s) | **T8**: tmavá karoserie = tmavý canvas loga | – |
| 33 | věta 7 „Tried every colour.“ | 17,55 · 17,75 · 17,95 | ROZ-IN | 18,10–19,10 | 19,10–19,16 | ROZ-OUT | – | **věta 7** |
| 34 | tečka → Vanadium Grey; **skenovací linka 4 zprava doleva** | 20,12–20,20 | LET z pilulky k pravé hraně vozu | – | 20,20–21,00 přejede vůz **zprava doleva** (0,8 s), za ní **původní stopáž** (šedý lak, stříbrná kola); 21,00–21,10 zpět | MORF na podtrh | návrat = odkrytí originálu (nejpoctivější proměna) | – |
| 35 | text „Vanadium Grey Metallic“ | 20,40 | ROZ-IN | 20,55–21,02 | 21,02–21,08 | ROZ-OUT | 0,2 s po startu linky | popisek |
| 36 | věta 8 „Kept the one you're driving.“ | 21,15 · 21,30 · 21,45 · 21,60 · 21,75 | ROZ-IN | 21,90–22,60 (jede s pilulkou do středu) | 22,60–22,68 | ROZ-OUT | pointa přechází do světa loga uvnitř kotvy | **věta 8** |
| **S7 LOGO** | canvas #010205 → **22,17–27,65** | | | | | | | |
| 37 | pilulka ve středu (y 540) s větou 8 | 22,17 | z MORF polohy | 22,17–22,60 | 23,00–23,10 | obrys pilulky ROZ-OUT (text a podtrh zůstanou) | podtrh = linka, která kreslí erb | – |
| 38 | název „718 Spyder RS“ (SVG „718“ 120 px + Barlow 600 72 px) | 22,68 | PIS 0,30 | 22,98–24,05 | 24,05–24,13 | ROZ-OUT | – | název |
| 39 | **TAH erbu**: linka vyjede z podtrhu nahoru a nakreslí obrys štítu (180 px) nad textem | 23,10–23,50 | TAH | – | 23,50–23,70 | výplň: barevný erb (SVG porsche.cz) uvnitř obrysu, červený obrys zbledne | **semínko → logo (D10)** | – |
| 40 | text sjede o 60 px dolů (ease 0,2 s) a přepíše se na claim „Configured on the road.“ | 24,20 · 24,40 · 24,55 · 24,75 | ROZ-IN | 24,90–25,40 | 25,40–25,48 | ROZ-OUT | – | **věta 9** |
| 41 | řádek WLTP (18 px, #f6f6f8ab, y 980): „718 Spyder RS (WLTP): Fuel consumption combined 12.7 l/100 km · CO₂ emissions combined 288 g/km · CO₂ class G“ | 24,60 | ROZ-IN | do 27,40 | 27,40–27,65 | s logem | povinný údaj, není to „číslo videa“ | – |
| 42 | claim 2 (oficiální, doslova) „Unfiltered driving pleasure. Open top.“ | 25,55 · 25,75 · 25,95 · 26,15 · 26,30 | ROZ-IN | 26,45–27,40 | 27,40–27,65 | ROZ-OUT + zblednutí s erbem | – | **věta 10** (volitelná, rozhodne režisér) |
| 43 | erb + text: dotlačení 1,00 → 1,02 (24,0–27,4, kamera dýchá) | – | – | – | 27,40–27,65 | ROZ-OUT + zblednutí 0,25 s (C9) | → ticho | – |
| 44 | ticho (černá) | 27,65 | – | 0,20 | 27,85 | – | – | – |
| 45 | **boom + bílý záblesk** | 27,85 | ZÁBLESK 2 snímky bílá, bloom dozní 0,15 s | – | – | – | jediný hlasitý úder videa (I9) | – |
| 46 | **end card tvůrce** „strihyontop“ (Barlow 600, 96 px, prostrkání 0,12 em; režisér vymění jméno/logo) | 27,90–28,05 | ROZ-IN z bílé | 28,05–30,00 (dotlačení 1,00 → 1,02) | 30,00 | konec | – | – |
| 47 | disclaimer „Concept ad · not affiliated with Porsche AG · footage © Porsche AG“ (22 px, #f6f6f8ab) | 28,15 | ROZ-IN | do 30,00 | – | – | – | – |

**Čísla partitury**: 8 světů (W1 · W4 · W7 · M8 · fotka · dron + pláň · W6 · logo + podpis) · 47 prvků, ≈ 49 událostí / 30 s = **jedna za 0,61 s** · nejdelší klid prvku 1,45 s (věta 1 nad jedoucím vozem) a 1,07 s (číslo) ·
tvrdých střihů v grafice **0**; střihů ve stopáži 7 (T1–T7), každý maskovaný jinou proměnou a vždy s přežívající pilulkou · přechody mezi světy: LET (průjezd) · ZOOM+ROZ · CLONA · LET svislý · WIPE · střih pod kartou · EXPL · MORF kotvy · TAH → logo · ZÁBLESK, **žádný dvakrát** ·
jízda 23,4 s z 30 (78 %) · jedno číslo (500 PS, klid 1,07 s) · obraz předbíhá každou větu o 0,10–0,20 s · kotva 91 % videa · kaskády: tečka → text (6 sn.), karta → PS → číslice (8 + 6 sn.), pilulka → název → obrys → erb → claim.

**WOW momenty (v pořadí síly)**: (1) 20,20–21,00 linka zprava doleva „odvolá“ všechny úpravy a odkryje skutečný vůz = pointa, která je zároveň nejrealističtější snímek videa ·
(2) 5,30–5,55 vůz v zatáčce zčervená pod linkou, krajina se nehne · (3) 6,70–7,45 šest laků za 0,75 s na jedoucím voze + 8,00–8,90 totéž pomalu v modré s odlesky krajiny ·
(4) 13,20–13,55 wipe v šedých porsche.cz → dron nad serpentinou + 500 PS · (5) 12,40–12,85 sedadla z karmínu do Arctic pod vodorovnou linkou · (6) 23,10–23,70 červený podtrh nakreslí erb Porsche.

### Rozpis úseků stopáže (každý jednou, rychlost 1,2×, začátky na hranici snímku zdroje = násobky 0,04 s)
| kód | zdroj (`media/projekty/005-porsche/materialy/videa/`) | zdroj od–do | výstup od–do | obsah | stav vozu v obraze |
|---|---|---|---|---|---|
| W1 | `newstv_242104_walkaround_hls.mp4` | 119,04–122,16 | 0,00–2,60 | západ slunce, 3/4 zepředu, průjezd vpravo 121,5–121,98 | šedá (originál) |
| W4 | walkaround | 206,28–210,84 | 2,60–6,40 | 3/4 zepředu, serpentina se svodidlem, vůz střední velikost | šedá → 5,30 Guards Red |
| W7 | walkaround | 283,40–288,10 | 6,40–10,32 | zadní sledovací, SPZ S PY 500 | červená → scroll → GT Silver → 8,00 Gentian Blue |
| M8 | `newstv_249707_moodcut_hls.mp4` | 8,64–9,88 | 10,32–11,35 | přední kolo + blatník za jízdy | Gentian Blue, kola 10,75 Satin Neodyme |
| F1 | `fotky/newsroom/BX24I3HOD0015.jpg` (9504×5346) | – | 11,35–13,35 | sedadla shora, krajina | karoserie v záběru Gentian Blue, kolo bronz, sedadla karmín → 12,40 Arctic |
| X1 | `porschecom_718spyderrsmosaicsnippetEN.mp4` | 0,00–2,56 | 13,35–15,48 | dron nad serpentinou, vůz malý od 1,5 s zdroje | Gentian Blue (malý) |
| W11 | walkaround | 363,00–365,30 | 15,48–17,40 | lávová pláň, vůz z dálky; **končí před průjezdem** (365,4+ je rozmazaný průjezd vlevo) | Gentian Blue, kola bronz |
| W6 | walkaround | 277,68–283,40 | 17,40–22,17 | 3/4 zepředu z dálky mezi skalami, průjezd vpravo 282,9–283,4 | Gentian Blue + bronz → 20,20–21,00 originál |
**Náhradní úseky** (jen po schválení režiséra, s kontrolou proti zakázaným, C044): W2 122,20–124,08 (kaňon, vůz přijíždí, průjezd vlevo) · W9 355,84–357,68 (silnice, vůz projede) ·
W10 357,68–360,16 (záď 3/4) · M6 moodcut 6,20–7,44 (přední sledovací) · M9 moodcut 9,88–11,20 (zadní sledovací) · X 8,76–9,84 (přední sledovací z dálky) · D desktop 5,00–6,88 a 6,88–10,04 (bez textu) ·
W8 352,16–355,84 jen **místo** W1 (totéž slunce, duplikát).
**Zakázané úseky**: walkaround 0–6,0 (intro NewsTV) a 6,0–119,04, 122,20–206,28, 216,04–277,68, 288,12–352,16, 360,16–363,00, 367,16–konec (moderátor, studio s růžovou stěnou,
outro) · **W5 210,84–216,04** (pohled shora do kokpitu = červená sedadla po změně interiéru + whip pany) · desktop 1,36–5,00 a mosaic 3,00–7,00 (vypálený text) · mosaic 7,72–8,76 (roll-bar,
sedadla) · roof tutorial celý · fotka 0675 (červené sedadlo) · rendry v5/v6/v7/v8 (studio) a se zavřenou střechou · rendry kol na bílém voze (`kola/`) · po 12,85 žádný záběr s čitelným karmínovým interiérem.

### Proměny na stopáži: nová technika (test PŘED stavbou, animátor; schválí kreativní ředitel na 100% výřezech)
**A. Přebarvení laku jedoucího vozu LUTem z rendrů (cesta A, preferovaná)**
1. Maska vozu po snímcích (BiRefNet / rembg jako V004 test B) na W4 209,0–210,84, W7 celý, M8, X1 (vůz malý), W11, W6 277,68–281,1; měkká hrana 2 px, eroze 1 px, časový medián masky 3 snímky (proti blikání).
2. Uvnitř masky jen **karoserie**: vyloučit pneumatiky a ráfky (sledovaná elipsa), sklo a světla (chroma červená / L > 0,92), SPZ (sledovaný obdélník), černé díly (L < 0,12). Co není lak, se nemění.
3. **1D LUT z pixelově zarovnaných rendrů** `konfigurator/barvy/1H_*_v3_zad-34.webp` × `<cíl>_v3_zad-34.webp` (pro zadní záběr W7) a `v1_predek-34` (pro W4, W6): v Lab, v masce karoserie rendru,
   64 binů L zdroje → medián (L, a, b) cíle. Tím se přenese skutečná odezva laku (jak se mapují odlesky a stíny), ne plochá barva. Aplikovat uvnitř masky stopáže; mimo masku nic.
4. Test: W7 zdroj 285,0–286,0 (25 snímků) pro G1, 1A, A1, P3, 0Q; W4 209,5–210,5 pro G1; M8 pro 1A + ráfek (bod 5). Výstup: pás snímků 100 % výřez + MP4 1 s.
   **Kritéria přijetí**: na 100 % výřezu žádný lem ani „vystřižený“ okraj, odlesk slunce a odraz krajiny zůstávají ve tvaru (jen změní barvu podle LUT), žádné blikání (průměr L v masce
   mezi sousedními snímky < 2 %), SPZ a světla beze změny, barva vozu na snímku odpovídá tečce v pilulce (ΔE < 12 proti rendru). Bílá a žlutá smí být slabší (na obrazovce jen 0,125 s).
5. **Kola**: v M8 kruh z náboje (sledovaný střed), ráfek stříbrná → Satin Neodyme = chroma bronzu + L −12 %, rotační rozmazání zůstává; ve W11/W6 malé elipsy kol tónovat stejně (jen chroma).
6. **Interiér (F1)**: statická maska karmínu (chroma), odbarvení + jas +35 % → Arctic; karoserie na fotce LUT 1A, kolo bronz. Jednoduché, bez testu.
7. Výkon: masky předpočítat jako PNG sekvence (30 fps), LUT jako 3 malé tabulky; scéna jen skládá; změřit 1 s výřezu (C027).
**B. Záloha** (když A neprojde): proměny jen na rendrech `barvy/` v3 / v1 (sweep linky = maska, D7) vstupujících v pohybu z W7 / W6 (švih P2 z V004: 4 snímky směrového rozmazání, render
přijíždí s dojezdem 0,2 s, zpět stejně), stopáž vždy šedá; kola vynechat (S3 → M6 přední sledovací + věta „Hands on. Mind off.“); interiér F1 zůstává. Rendry nemají Weissach pruh na víku →
používat jen v3 (záď, pruh není vidět). Pointa „Kept the one you're driving“ platí beze změny.

### Hudba (pro zvukaře; skládá se až k hotové partituře, D12; časy se doladí k obrazu, ne naopak)
- **Nálada**: „na vrcholu hory“: velmi drahá a klidná. Pomalé, široké, bez bicích a bez dropu; nálada stoupá k jedinému vrcholu (otevření výhledu) a pak se uvolní do tóniky.
  Tempo **72 BPM** (nebo volně), durová tónina (F / D dur), akordy maj9 / m9 / add9 (jako `luxusni`, ale poloviční tempo), žádná marimba, žádný shaker, žádný kopák do 13,35; od 13,55 nejvýš
  měkký „tep“ (sub + taiko tiše na 1. dobu, −20 dB). Nástroje: smyčcová plocha (`plocha`, útok 0,6–1,0 s), tlumené piano (`klavir`, tiché), sub swell, dlouhý dozvuk rt60 3,0–3,5 s, předelay 30 ms,
  středy ≥ 30 % (I7). Rozsah −22 LUFS (úvod) → **−16 LUFS vrchol 13,55–17,40** → −20 LUFS logo.
- **Klíčové momenty**: 0,00 jediný tón piana (háček, bez plochy) · 2,60 nástup plochy · 5,30 první proměna (jen SFX, hudba beze změny) · 8,00–8,90 pomalá proměna = swell +2 dB ·
  **13,20 nádech** (hudba −6 dB za 0,3 s pod wipem) · **13,55 vrchol**: plocha se rozevře o oktávu, melodie piana 4 takty · 15,48 pokračuje bez změny · 20,20–21,00 návrat k šedé = kadence
  do tóniky (teplý durový akord přistane na 21,00) · 22,17 logo: jen plocha + piano, decrescendo · 27,40 fade 0,25 s · **27,65–27,85 ticho** · **27,85 boom** (jediný úder videa, plný, ne agresivní)
  · 28,0–30,0 dozvuk, tichý pad pod podpisem.
- **Existující nálady**: `luxusni` je harmonicky nejblíž (Am9 Fmaj7 Dm9 Em7, Rhodes), ale 120 BPM s kopákem a shakerem = moc rytmické; `pohodova` (96, marimba) moc hravé; `vazna` moc dramatické.
  Chybí: **pomalá nálada bez bicích se stoupáním k vrcholu místo dropu** → nová nálada `hora` (`--vrchol 13.55 --konec 27.65`, bez `--drop`), odvozená z akordů `luxusni` při 72 BPM: plocha + piano + sub,
  obrácený činel nahradit swellem plochy, konec bez `uder` (ten patří až na podpis).
- **SFX** (tiché, jen na stavy, ~1/s, `sfx.py`): 0,20 pilulka (měkký klik UI) · slova (bez zvuku) · 4,30 tik tečky · 5,20 tik · 5,30–5,55 sken (tichý „shimmer“ sklo, vrchol 5,42) · 6,70–7,325 šest tiků
  po 0,125 s (PDS klik, každý jiná výška) · 8,00–8,90 sken pomalý (shimmer delší) · 10,22 clona (měkký whoosh) · 10,75 kolo (kovový tón tichý) · 12,40–12,85 sken · 13,20 wipe (nádech, hudba dolů)
  · 13,88–14,58 tiky odometru jen na viditelné přenosy řádů, **ding 14,58** na ustálený snímek (C047) · 17,38 EXPL (1 snímek tichý pop) · 20,20–21,00 sken obrácený (shimmer dolů) · 22,05 morf kotvy
  (whoosh tichý) · 23,10–23,50 tah erbu (tenký tón) · 27,85 **boom + záblesk** (0 až −3 LU v okně 100 ms, hudba ztichlá).

### Kontrolní snímky (před plným renderem, z výřezu s podsnímky, C028) a kritéria odmítnutí
| čas | co musí být vidět | odmítnout, když |
|---|---|---|
| 0,000 | hotový plakát: západ slunce, šedý vůz 3/4 vlevo, červená linka 3×96 vpravo dole, nic jiného | linka chybí nebo má záři; text už na obrazovce; obraz zatmívá z černé; bloky komprese v nebi |
| 0,32 / 0,47 / 1,00 | pilulka hotová, slova věty 1 z rozostření po jednom | pilulka naskočí ostře; dvě slova v jednom snímku; text nad bezpečnou zónou (y > 984) |
| 2,45 / 2,52 / 2,60 / 2,68 | průjezd → rozmazání → W4 dobrzdí; pilulka celou dobu na místě | střih vidět ostře; rozmazání v jiném směru než průjezd; pilulka blikne |
| 5,20 / 5,30 / 5,42 / 5,55 / 5,65 | tik tečky → linka u levé hrany vozu → půl vozu červený s ostrou svislou hranicí → celý červený → linka zpět | červená mimo karoserii (silnice, svodidlo, kola, sklo, SPZ); lem; vůz „plave“; odlesk slunce zmizel; hranice není rovná |
| 6,20 / 6,40 / 6,50 | nájezd + rozostření na červené karoserii → rozmazaná červená záď → ostrá | rozdíl jasu rozmazaných snímků > 15 %; červená W7 jiný odstín než W4 (ΔE > 8) |
| 6,70 / 6,825 / 6,95 / 7,075 / 7,20 / 7,325 | šest barev, každá i na tečce; mezi snímky kroku nic nebliká mimo vůz | barva na okolí; bílá/žlutá „plochá“ (bez odlesků); scroll pomalejší nebo rychlejší než 0,125 s |
| 8,00 / 8,45 / 8,90 / 9,00 | pomalá linka: stříbrná vlevo od linky, modrá vpravo (ne naopak), odlesky krajiny v modré | směr proměny opačný než popis; linka se zastaví; modrá mimo masku |
| 10,22 / 10,27 / 10,32 / 10,42 | kruh z pravého zadního kola W7 se otevře do M8; M8 modrý od 1. snímku; „Wheels?“ až po kole | střed kruhu mimo kolo; M8 šedý v prvním snímku; slovo před obrazem |
| 10,75 / 10,90 / 11,05 / 11,30 | kruh z náboje, ráfek bronzový, rotační rozmazání zůstává; odlet nahoru | bronz na pneumatice nebo blatníku; ráfek ostřejší/plošší než originál; svislý let bez rozmazání |
| 11,35 / 11,50 / 12,40 / 12,62 / 12,85 | fotka dojede zdola, „Carmine inside.“, vodorovná linka, sedadla nad linkou šedá / pod linkou červená, pak celá šedá | šedá bez textury (zalitá); změna i na pásech / madlech, které nejsou karmín (ověřit proti rendru 51); karoserie na fotce šedá místo modré |
| 13,20 / 13,30 / 13,40 / 13,55 | pruhy padají, plná #191f22 na 13,30–13,40 s červenou hranou, pod nimi už dron | pruhy v jiných barvách než porsche.cz; wipe delší než 0,4 s; dron zatmívá z černé |
| 13,65 / 13,78 / 13,88 / 14,20 / 14,58 / 15,65 | karta roste → „PS“ → číslo roluje jen zdola (hodnoty < 500) → ustálí se na 500 → klid ≥ 1 s → karta se smrští | hodnota > 500 během rolování (G9); klid < 1 s (C046); ding mimo ustálený snímek (C047); karta přes vůz |
| 15,48 / 15,50 | střih X1 → W11 pod kartou; karta beze změny | karta blikne; vůz ve W11 šedý nebo bez bronzu kol (pokud ≥ 40 px) |
| 17,38 / 17,40 / 17,42 | tečka → červená plocha 2 snímky → tečka nad W6 | plocha déle než 2 snímky; EXPL z jiného místa než tečka |
| 20,20 / 20,60 / 21,00 / 21,10 | linka zprava, **vlevo od linky modrá, vpravo šedý originál**, pak celý originál = 1:1 s nezměněnou stopáží (rozdíl snímků = 0 mimo pilulku) | po 21,00 jakýkoli rozdíl proti originálu; kola zůstala bronzová |
| 21,15–21,90 / 22,05 / 22,17 / 22,60 | věta 8 po slovech; průjezd; pilulka sjede do středu, canvas #010205; věta 8 ještě čitelná ve středu | střih do loga vidět ostře; pilulka skočí; věta 8 zmizí dřív, než se dočte |
| 23,10 / 23,30 / 23,50 / 23,70 / 24,20 / 24,75 | podtrh vyjede a kreslí obrys štítu; výplň barevným erbem; claim po slovech | erb deformovaný / jiné barvy než SVG (změřit v MP4); obrys kreslí jiná barva než #d5001c; erb naskočí bez tahu |
| 25,55 / 26,45 / 27,40 / 27,65 / 27,85 / 27,90 / 28,15 / 29,98 | claim 2, klid, rozostření, černá, záblesk 2 snímky, podpis z bílé, disclaimer, poslední snímek s dotlačením | překlep; WLTP jinak než doslova nebo < 16 px; záblesk neviditelný kvůli závěrce (C028); zamrzlý poslední snímek; disclaimer chybí |

### Pasti stavby
1. **Kadence** 25 → 60 fps jen **1,2×** (2:2), nikdy 1,0× / 1,5× / `minterpolate` / `framerate` (V004). Výřezy začínat na hranici snímku zdroje; podsnímky závěrky neprolínat dva zdrojové snímky (hranice o 1/120 s).
2. **Stav vozu v každém záběru** podle tabulky stavů (nahoře): před stavbou vyplnit „barva · kola · interiér“ pro každý úsek; kritik kontroluje po snímcích. Žádný záběr po 12,85 s čitelným karmínem (W5, mosaic 7,72–8,76 zakázány).
3. **Realismus proměn**: jen uvnitř masky karoserie, LUT z rendrů (ne plochá barva), časový medián masky; odlesky a stín zůstávají; nikdy přebarvit silnici, svodidlo, SPZ, světla, sklo.
   Kontrola 100% výřezem a rozdílem proti originálu (po 21,00 musí být rozdíl 0 mimo pilulku).
4. **Grade jednotný** jedním filtrem pro všechny desky stopáže (stopáž je lehce studená, stíny +3 %, teplé výšky zachovat); fotka F1 je teplejší a sytější → dorovnat ke stopáži (změřit průměr Lab na nebi a asfaltu);
   zrno stejné (seed) na stopáži i fotce; canvas loga #010205 bez zrna.
5. **Zakázané úseky** (C044) hlídá autor i kritik u každé náhrady; čas zdroje v hlášení. Úseky neprodlužovat přes hranice střihů zdroje (122,20 · 210,84 · 288,12 · 365,60 · 283,40 · 9,88 · 2,56).
6. **Text jen jedna vrstva** v pilulce (odcházející zmizí dřív, než přijde další; C046: odchod ≤ 0,08 s, žádný prázdný rámec > 2 snímky); slova z rozostření, ne kurzorem; nikdy dvě nová slova v jednom snímku kromě pointy.
7. **Číslo** (G9, C046, C047): 000 → 500 jen zdola, klid 1,07 s, ding na ustálený snímek (pohyb < 0,5 px), tiky jen na viditelné přenosy; rozmazání číslic v kódu, ne kopiemi (C040).
8. **Pilulka vs. vůz**: vpravo dole je v každém úseku volno (W1 vůz vlevo, W7 uprostřed, M8 kolo vlevo, F1 krajina, X1 skály, W11 silnice, W6 vůz projede až při morfu). Ověřit pásem snímků, že pilulka nikdy neleží na laku.
9. **Linka**: 3 px, #d5001c, bez záře, 1 px měkká hrana; při rychlém pohybu směrové rozmazání v kódu; nikdy se nezastaví mimo pilulku déle než 0,1 s (semínko „nikdy nezmizí, jen se mění“).
10. **Moduly scény** (C036): prefixy bloků `A_` (0–13,35) a `B_` (13,35–30); regrese i uvnitř přechodů (2,60 / 6,40 / 10,32 / 11,35 / 13,35 / 15,48 / 17,40 / 22,17).
11. **Výkon** (C027): masky a LUT předpočítané, desky stopáže jako 30fps sekvence; změřit 1 s nejtěžšího úseku (6,70–7,45 scroll, 13,20–13,55 wipe přes dron).
12. **Zvuk až po obrazu** (C045): po posledním renderu režisér posune SFX na skutečné časy; boom měřit vrcholem na 27,85; hudba 27,65–27,85 opravdu ticho.
13. **Erb a písmo**: erb jen ze SVG porsche.cz (bez deformace, barvy změřit v MP4, C034); Porsche Next nepoužívat, Barlow z `znacka/`; tenký text ≥ 16 px a barvy změřit po kódování (C041).
14. **Právní**: disclaimer na podpisu, WLTP řádek doslova; spec reklama jen do portfolia (podmínky newsroom).

### Pořadí stavby
1. **Test nové techniky** (animátor, ≤ 1 h): bod A 1–5 na W7 285,0–286,0 + W4 209,5–210,5 + M8; pás 100% výřezů + 1s MP4 → **kreativní ředitel rozhodne A / B** (kritéria v bodu 4).
2. **Desky stopáže** (animátor, ffmpeg): 8 úseků z rozpisu, 1,2× + zdvojení, jednotný grade, 30fps sekvence; masky vozu + kol + SPZ pro W4 (od 209,0), W7, M8, X1, W11, W6 (do 281,1); LUT pro 1H → G1, A1, P3, N2, D7, 0Q, U2, 1A (v3 i v1); F1 masky (karmín, karoserie, kolo).
   Pás snímků každého úseku (kontrola kadence, textu, moderátora).
3. **Blok A 0–13,35** (háček, pilulka, W4 + červená, W7 scroll + modrá, M8 kola, F1 interiér, wipe) → kontrolní snímky bloku A → **kreativní ředitel schválí klíčové snímky** (0,00 · 1,00 · 5,42 · 7,075 · 8,45 · 10,90 · 12,62 · 13,30) před blokem B.
4. **Blok B 13,35–30** (dron + karta 500 PS, W11, EXPL, W6 + návrat, morf kotvy, logo + tah erbu, claimy, ticho, boom, podpis) + plný render + spojení se zvukem (zvukař souběžně: nálada `hora` + SFX podle sloupce výše, pak posun na skutečné časy).
5. Kontrola: kritik (technika + zadání + partitura po snímcích + stav vozu) a kreativní ředitel (wow, realismus, energie, střih); opravy jeden animátor.

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
