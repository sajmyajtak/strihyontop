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
- **Motiony z prompt-motion**: vybral analytik (7 položek: přechody, ukázka auta, luxus, výkon, UI řemeslo, end card), viz oddíl **Zvolené motiony** níže.

- **Odpovědi režiséra analytikovi** (2026-11-01):
  - Exteriér **jen v konfiguraci uživatele** (galerie g01–g14, otočka 360° se světly zap/vyp, rendry od uživatele). Fotky z bmw.cz v jiných lacích ne.
    Interiérové fotky z webu (w14 zadní salonek, w15 místo řidiče) smí, jen když barva čalounění nebude bít do očí proti konfiguraci; přednost má interiér z konfigurátoru.
  - Texty jsou **vlastní anglická copy** (ne citace BMW). Fakta jen čísla doslova z bmw.cz: **250 km/h**, **0–100 km/h 5,7 s** (anglicky „0–100 km/h in 5.7 s“),
    **230 kW**; koně neuvádět (převod k → hp by byl náš). „Elektronicky omezeno“ neuvádět (na webu není).
  - Volitelné prvky (Theatre Screen, B&W, Light Carpet…) **neuvádět jako fakt**, v konfiguraci neověřeno.
  - End card **světlá** (studio #E7E2DC), logo Grey-Colour z bmw.cz, skládané z vrstev.

### Zvolené motiony (analytik 2026-11-01)
Zdroj: katalog `media/prompt-motion/polozky.json` (236 položek) + ukázková videa vybraných položek, prohlédnutá po 12 snímcích
(lokálně `media/prompt-motion/videa_v003/arch_*.jpg`, necommituje se). Plné texty promptů do gitu nepíšu, jen odkazy a vlastní poznatky.
**Lajky**: prompt-motion.com je u položek neukazuje (ověřeno na stránce položky i v datech). Známe jen čísla, která cituje blog,
a pořadí v seznamu „Most liked prompts“ na stránce Customize. U ostatních píšu „neuvedeno“.
Výběr: 1 přechody · 2 ukázka vozu · 3 luxus světlem · 4 výkon · 5 UI řemeslo (kurzor, sklo) · 6 luxus zdrženlivostí · 7 skládací logo.
Všech 7 je kompatibilních s G7: UI a typografie se kreslí v kódu, **vůz je vždy jen render BMW** (maska, posun, měřítko, odkryvy, nikdy deformace).

**M1 Přechody: [Shape morphing through UI states](https://prompt-motion.com/twoclipping-5cba86)** (@twoclipping, `twoclipping-5cba86`,
**12 103 lajků** podle blogu = 2. nejlajkovanější položka galerie, 2. v „Most liked“; 1440², 120 BPM).
- **Převzít**: **jeden prvek, nikdy střih**: modrá pilulka `#1C69D4` se bez přerušení mění (velikost, rádius, barva) a nese kapitoly.
  Návrh: segmentový přepínač **Design / Comfort / Performance**, jehož ukazatel přejede na 4,0 / 10,0 / 16,0 (drop 1, zlom, drop 2) a po cestě se
  promění v posuvník (M3) a v posuvník rychlosti (M4). **Obě hrany ukazatele na dvou různých pružinách** (náběžná předběhne a ukazatel se natáhne,
  pak se srovná), stejný trik u knoflíku přepínače. Obsah, který se uvnitř tvaru mění, má **vlastní masku a časování** a mění se s krátkým rozmazáním.
  Kurzor dělá skutečné kliky a tažení. Při tažení je hodnota přímo z polohy kurzoru, po puštění dojede pružinou. Kamera přiblíží tak, aby stav vyplnil obraz.
- **Vyvarovat se**: 12 stavů je na 25 s moc → max. 4–5 stavů. Žádný skákavý easing, záře, gradienty na UI, nesourodé tahy ikon, mrtvý čas.
  Čtverec → 16:9 (pilulka a karty vedle vozu, ne přes něj). `will-change` nikdy na prvcích, které kamera škáluje (rozmazaný text).

**M2 Ukázka vozu: [Spotify product film](https://prompt-motion.com/brainextends-e19ac3)** (@brainextends, `brainextends-e19ac3`, lajky neuvedeno;
**1920×1080, 60 fps, ~120 BPM, bez VO = přesně náš formát**).
- **Převzít**: **produkt v zaoblené „scéně“** (stage ~80 % šířky, ~75 % výšky, rádius ~24–32 px), kolem ní studio. Render vozu je „hrdinský obraz“:
  **jeho identita a poloha se drží přes všechny záběry** (match-position: další záběr začíná tam, kde vůz v předchozím skončil). Na drop 1 a 2 se scéna
  **rozšíří přes celý obraz** (full-bleed) = wow, ve zlomu se zase zmenší do karty. **Trvalá lišta jako spojka záběrů** (u nich přehrávač, u nás
  **lišta konfigurátoru**: miniatura vozu, „BMW 740d xDrive Sedan“, tenký ukazatel postupu podle kapitol), vizuálně podřízená vozu.
  Myšlenka ~1 s, UI vstupuje s jemným perspektivním náklonem, který se srovná do čelního pohledu. Kriticky tlumené pružiny.
  Odcházející titulek zmizí dřív, než příchozí obsadí jeho místo. Závěr: obrázky se **sbíhají do středu a ustoupí logu**, které vznikne
  ze stejného místa (předání do M7). Kontrola: rychlá předání nadpisů, předání hrdinského obrazu, zoom, sbíhání, mezery wordmarku.
- **Vyvarovat se**: zelený atmosférický gradient kolem scény (u nás studio `#E7E2DC` z rendrů nebo `#F6F6F6`), vymyšlené „artwork“ (u nás jen rendry),
  přerostlé prezentační nadpisy, částice, odlesky objektivu, třes kamery, náhodné prolínačky celého obrazu, reset kamery.

**M3 Luxus světlem + přechody zaplavením: [Photo print app launch film](https://prompt-motion.com/twoclipping-221cab)** (@twoclipping, `twoclipping-221cab`,
podle blogu **nejlajkovanější launch video galerie** (912slovní prompt, přesné číslo blog neuvádí), 5. v „Most liked“; 1440², 120 BPM, drop + tichý zlom).
- **Převzít**: (a) **přesvícení posuvníkem mezi dvěma zarovnanými snímky** (u nich den → zlatá hodinka) = u nás **přesně páry den/noc**
  `g01`→`g02`, `g03`→`g04` a otočka `360_svetla_vyp`→`_zap` (pixelově zarovnané): kurzor táhne skleněný posuvník „Lights“, hranice odkrytí jde
  s knobem (měkká svislá maska, ne prolínačka celého obrazu), světla vozu se „rozsvítí“ pod prstem. Ideální na stoupání 14,0–16,0.
  (b) **Zaplavení tvarem**: černý tvar (např. silueta vozu nebo kruh z kola) zaplaví obraz **přes všechny 4 rohy za ~0,3 s** a smrští se do další scény
  = přechod na drop 2 (16,0) do noční / výkonové části. (c) **Clona ze 6 lamel** (iris) jako přechod do interiéru na zlomu 10,0 (lamely se zavřou
  nad exteriérem a otevřou do `g12`). (d) „Apple keynote, 2D, jeden souvislý záběr, každá scéna vzniká z předchozí“, kurzor řídí každou změnu
  (klik, tažení, dlouhý stisk), kamera „screen studio“ přiblíží moment a kurzor se škáluje s ní. (e) Ukázka míchá **skutečné fotky a záběry** s UI,
  přesně náš případ (rendry BMW + UI).
- **Vyvarovat se**: liquid glass s `feDisplacementMap` a chromatickými hranami je na CPU drahý a duhové okraje prozrazují AI (G7): **sklo jen
  zjednodušené** (rozmazaný klon scény za kartou + 1 px světlý okraj), nikdy přes vůz. Zákazy z promptu převzít: prolínačky, „blur-in“,
  „developing“ jasu, 3D flipy, částice, záře, držení > 1 s. **Zúžení wordmarku (osa wdth) na BMW logo nepoužít** (logo se nedeformuje).
  Zaplavení kratší než ~0,3 s nebo bez přesahu rohů = probliknutí (pasti z promptu).

**M4 Výkon: [White ball UI motion loop](https://prompt-motion.com/rossaxbt-94583b)** (@rossaxbt, `rossaxbt-94583b`, lajky neuvedeno; **1920×1078 16:9, 120 BPM**).
- **Převzít**: **posuvník s bublinou hodnoty nad knobem, číslo se počítá z polohy knobu** a bublina drží nad knobem až do cíle; modrá výplň dráhy
  přilepená ke knobu, pod dráhou ryska po rysce, která se rozsvítí, když ji knob mine. U nás **0 → 250 km/h** na drop 2 (16,0–~17,5), cílová
  hodnota přesně „250 km/h“, mezihodnoty jen jako rolující číslice v pohybu (stejně jako počítadlo na bmw.cz). Po dosažení cíle **3 karty, každá
  na svou dobu**: „250 km/h“ · „0–100 km/h in 5.7 s“ · „230 kW“ (jen tato fakta, viz odpovědi režiséra). **Jeden svět, jedna kamera** (pozice +
  log zoom), kamera sleduje prvek, který nese pohyb. Dopady přesné, krátký squash jen u UI prvku (ne u vozu). Každý kontakt = tichý UI zvuk.
- **Vyvarovat se**: tmavé plátno s tečkovou mřížkou (šablonový dojem), klávesnice a „míček“ (dětské), teleport prvku mezi komponentami
  (vždy ukázat cestu), rozmazaný text při pohybu kamery, víc než malý překmit. Rychlostní čísla nikdy vymyšlená (C8): žádné „0–200“, „top speed reached 100 %“.

**M5 UI řemeslo (kurzor, sklo, nájezdy): [Frame by Frame launch video](https://prompt-motion.com/notdwd-7de38a)** (@notdwd, `notdwd-7de38a`, lajky neuvedeno;
1080², Apple-keynote „bílá, jasně modrá, skleněná“ = nejbližší paleta k bmw.cz).
- **Převzít**: **každý záběr přijíždí už v pohybu** (exponenciální ease-out, každý snímek ujede ~12–19 % zbývající dráhy) a odjíždí zrychlením
  nebo náběhem rozmazání, nikdy střih na stojícím snímku. **Kurzor jako postava**: černá macOS šipka s bílým okrajem, při letu se natočí
  ke směru, zpomaluje do cíle, při najetí na cíl se zvětší (u nich ×1,55, u nás ×1,2–1,3 kvůli eleganci), stisk = zmenšení o ~15 % na 2–3 snímky
  + kroužek akcentu kolem cíle. **Matná skleněná karta vyskočí pružinou zpod prvku, na který kurzor klikl** (šířka krátce přestřelí ~2–3 % a usadí se).
  Psaní textu ~1 znak za snímek s občasným zdržením a stále viditelným kurzorem. Rozmazání vždy podle rychlosti a směru.
- **Vyvarovat se**: end card „zoom smear“ + zářící wordmark na černé (uživatel chce jednoduché skládací logo na světlé end card),
  modrý „sky“ gradient s čárovou kresbou, záblesk při švihu, prolínačky s rozmazáním. Lineární rolování textu.

**M6 Luxus zdrženlivostí (kamera produktu, glint): [Taxtello bookkeeping app film](https://prompt-motion.com/daniel-haida-8691d4)**
(@daniel_haida, `daniel-haida-8691d4`, lajky neuvedeno; 1920×1080; ve V002 jsme z něj brali typografii, tady **prémiovost**).
- **Převzít**: „točíme fyzický prémiový předmět“: **kamera jako makro produktové natáčení** (pomalé dotlačení 1,00 → 1,04, paralaxa, hloubka
  ostrosti jen střídmě a jen na pozadí / UI, ne „rozmazaný render“). Easing `cubic-bezier(0.16, 1, 0.3, 1)`, překmit **pod ~2 %**, „ruthless restraint“:
  sebevědomí z ticha a prostoru. **Drobný teplý záblesk (glint)** jako drahý akcent, který odhalí značku nebo detail = u nás **jeden světelný přejezd
  po chromu masky ledvinek / liště** (jen v masce karoserie, G7) na zlomu 10,0 nebo těsně před end card. Přechody přes objekty (hrana karty /
  detail vozu otevře další scénu). První 1,5 s už musí vypadat draze. Hesla 2–4 slova, bez tečky (E8). Kontrolní otázka z promptu převzít:
  „působí akcent draze, nebo jako barevná záplava?“ → modrá `#1C69D4` jen na aktivním prvku.
- **Vyvarovat se**: zlatá barva Taxtella (u nás neutrální bílé / teplé studiové světlo), „fake glassmorphism everywhere“, každé slovo animované zvlášť,
  „cartoon springiness“, tmavé dashboardové plátno (u nás světlé studio jako web BMW; tmavé jen v noční / výkonové části).

**M7 Skládací logo (end card 22,0–25,0): [TypingMind logo reveal](https://prompt-motion.com/tdinh-me-815acb)** (@tdinh_me, `tdinh-me-815acb`, lajky neuvedeno;
1920×1080; prompt je jedna věta, cenný je princip z videa; v poznatcích 6.2 doporučený pro logo).
- **Převzít**: **pomalý přechod, který logo nejdřív poskládá a teprve potom odhalí**: nejdřív kontura, pak do ní dosedají díly, nakonec hotová značka
  a vedle ní text. U nás z 9 vrstev v `znacka/logo/vrstvy/` (stejný viewBox, cesty beze změny): **prstenec** se uzavře (tah po obvodu) →
  **čtvrtiny** se dotočí kolem středu do svých pozic (rotace kolem středu loga je u kruhové značky přirozená, ne deformace) → **B, M, W** dosednou
  po řadě → **poslední díl dosedne přesně na úder 22,0** (nebo celé složení 22,0–23,0 po dobách, viz otázky) → klid + dotlačení 2–4 % do 25,0,
  pod logem CTA a disclaimer „Concept ad · not affiliated with BMW“. Měkký dopad (SFX) na každé dosednutí, nejsilnější na 22,0.
- **Vyvarovat se**: low-poly trojúhelníky, barevné střepy a díly přilétající z náhodných směrů (vypadá jako částice), záře, odlesk přes logo,
  jakékoli škálování v jedné ose / squash, jiné barvy než `#0066B1` + `#6F6F6F` (+ bílé čtvrtiny na tmavém), psací stroj u wordmarku.
  „Jednoduché“ = max. 3 kroky skládání, žádné efekty navíc (pravidlo uživatele 8).

**Záloha (nepočítám do 7)**: [Prompt Motion site promo](https://prompt-motion.com/antonio-kodheli-490109) (@antonio_kodheli) pro zásadu
„postav to jen ze skutečného produktu a jeho webu, citace doslova, žádné vymyšlené funkce ani čísla“ (= naše C8 a rozhodnutí o faktech)
a pro kurzor s halo akcentu a tah zvýrazňovače. [Food craving launch film](https://prompt-motion.com/ultimaxbt-2ddf1e) (zaplavení přes rohy)
jsme použili ve V002, tady ho nahrazuje M3.

**Doporučené mapování na časovou osu** (návrh pro kreativního ředitele, rozhodne on):
| čas | hudba | motiony | co je vidět (návrh) |
|---|---|---|---|
| 0,0–4,0 | úvod | M6 + M2 + M5 | snímek 0 = hotový render `g01` ve scéně (stage), pomalé makro dotlačení, kurzor přilétá už v pohybu, lišta konfigurátoru vyjede |
| 4,0 | drop 1 | M1 + M2 | klik na „Design“: ukazatel přeskočí s natažením, scéna se rozšíří přes celý obraz (full-bleed), match-position na `g03` |
| 4,0–10,0 | exteriér | M2 + M1 + M5 | `g03` → `g11` → `g05` kolo → `g09`, každý záběr navazuje polohou vozu, karta s faktem na dobu, kurzor ukazuje detail linkou |
| 10,0 | zlom | M3 (c) + M6 | clona ze 6 lamel přes exteriér, otevře se do interiéru `g12`, ukazatel na „Comfort“, jeden glint po dřevu / chromu |
| 10,0–14,0 | luxus | M6 + M5 | interiér `g12` / `g13` / kostka, pomalá kamera, skleněné karty s krátkými hesly, klid, ale událost na každou dobu |
| 14,0–16,0 | stoupání | M3 (a) | návrat na `g03`, kurzor táhne posuvník „Lights“, noc `g04` se odkrývá s knobem, světla se rozsvítí na 15,5 |
| 16,0 | drop 2 | M3 (b) + M1 | tvar vozu zaplaví obraz přes rohy (~0,3 s) a smrští se do noční výkonové scény, ukazatel na „Performance“ |
| 16,0–22,0 | výkon | M4 + M2 | posuvník 0 → **250 km/h** (bublina nad knobem), pak karty „0–100 km/h in 5.7 s“ a „230 kW“ po dobách, otočka 360° se světly |
| 21,5–22,0 | nádech | M2 | rendry / karty se sbíhají do středu a ustoupí |
| 22,0–25,0 | end card | M7 | skládací logo na úder 22,0, světlé studio, CTA + disclaimer, dotlačení 2–4 % |

**Pasti pro animátora** (z vybraných promptů + materiálů): otočka 360° má jen 36 snímků po 10°, pomalý plynulý turntable bude trhavý
(jen rychlý oblouk s rozmazáním mezi sousedy, nebo krátký výsek na úder) · render zvětšovat max. ~1,3× (2560 px v 1080p) · zaplavení přes
všechny 4 rohy a ≥ 0,3 s · text uvnitř měnícího se tvaru má vlastní masku · `will-change` ne na škálovaných prvcích · sklo jen jako rozmazaný klon
scény (ne `backdrop-filter: url()`, Chromium čte posunovou mapu špatně) · kurzor na posledním snímku odpovídá stavu end card (ne smyčka, video končí logem).
Průvodce stylem SaaS motion: `znalosti/prompt-motion/poznatky.md` oddíl 11.

- **Odpovědi režiséra k motionům** (2026-11-01): skládací logo varianta **A** (21,0–22,0 po dobách, poslední díl přesně na úder 22,0, pak klid a dotlačení,
  max. 3 kroky) · vůz v zaoblené scéně jen v úvodu a ve zlomu, na drop 1 a drop 2 přes celý obraz · „Design / Comfort / Performance“ jako vlastní
  kapitoly je v pořádku, jinak v UI jen fakta · přechod do interiéru raději **přes objekt** (karta / hrana dveří, klidnější a luxusnější), clona jen
  když má kreativní ředitel silný důvod · otočka 360° jen jako rychlý oblouk s rozmazáním na úder, žádný pomalý turntable · ukázková videa motionů
  v `media/prompt-motion/videa_v003/` ponechat jako vizuální reference.

- **Odpovědi režiséra k testu realismu** (2026-11-01): den → noc (g01→g02, g03→g04) a rozsvícení světel z párů zap/vyp **smí** být hlavní wow
  přechod (např. do výkonu na drop 2) · otočka 360° **jen krokováním úhlů na doby tvrdým střihem** (klikání v konfigurátoru), vůz se plynule neotočí
  ani nerozjede, s tím počítat · interiér (luxus 10–14 s) stavět z g12–g14 s 2,5D nájezdem, panorama z kostky jen jako možnost (otestuje animátor
  ve výrobě) · popisek „BMW Iconic Glow“ smí (název z bmw.cz, prvek je vidět v rendru) · výkon **bez koní**: 230 kW, 0–100 km/h in 5.7 s, 250 km/h.

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
- **Koncept jednou větou** (kreativní ředitel 2026-11-01, pracovní název **„ONE CONTROL“**): **Konfigurátor, který ožívá:** jediný modrý ovladač z lišty konfigurátoru (ukazatel kapitol → posuvník noci → posuvník rychlosti → knob, který opíše prstenec loga) projde celým spotem a každý jeho pohyb pod kurzorem mění **skutečný render BMW řady 7**: otočí ho, probudí světla, otevře interiér, stáhne na něj noc a vytáhne ho na 250 km/h, až se z knobu složí logo BMW.
  Proč to funguje: všechno, co se děje s vozem, je skutečné chování konfigurátoru BMW (krokování otočky, světla zap/vyp, den/noc, interiér), takže realismus vzniká z materiálu, ne z kresby (G7). Spojovací prvek je jeden tvar (M1), kruh knobu se rýmuje s kruhem loga (koncept z geometrie loga, náš nejsilnější typ nápadu podle V001/V002).
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

## Technický test realismu (animátor, 2026-11-01)
Cíl: co z rendrů BMW jde rozpohybovat tak, aby to působilo jako skutečnost (G7). Všechno v `media/projekty/003-bmw-rada7/test/`
(scény `sceny/t*.html`, skripty `skripty/`, podklady `podklady/`, videa `t*.mp4`, pásy `*_pas.jpg`). Časy výpočtu: 1920×1080, 60 fps, `--sub 4`, 3 prohlížeče.

| # | technika | verdikt | důkaz | výpočet |
|---|---|---|---|---|
| 1 | maska vozu BiRefNet + čisté pozadí + stín | **funguje** | `t1_maska_birefnet_200.jpg`, `t1_masky_prehled.jpg`, vrstvy v `materialy/masky/` | ~45 s na pohled (CPU) |
| 2 | odlesk po laku | **s výhradou** | `t2b_odlesk_bok.mp4` (bok, dobré), `t2_odlesk.mp4` (3/4, slabé) | 4 s videa za 51–58 s |
| 3 | rotace kola | **s výhradou** | `t3_kolo.mp4`, `t3_kolo_pas.jpg` | 4 s za 70 s (`--sub-rychle 8`) |

**1. Maska vozu.** rembg nainstalován (`pip install rembg`, modely v `~/.rembg/`, přidat do `setup.sh`). Srovnání na g03 ve 200 %:
`isnet-general-use` (2 s) má vnitřek čistý, ale měkkou hranu 6–8 px a světlý béžový lem u nárazníku; zpřesnění closed-form mattingem
(pymatting) hranu na bílé proti béžové **roztřepilo** (zamítnuto); **`birefnet-general` (33 s, model 973 MB) má ostrou čistou hranu**
na střeše, zrcátku, pneumatikách i černé střeše proti béžové, bez lemu. Barvy hrany čistí `estimate_foreground_ml`.
Skript `test/skripty/masky.py` + `podlaha_stin.py` dělá pro každý pohled 3 vrstvy do `materialy/masky/`:
`*_vuz.png` (RGBA), `*_pozadi.png` (studio bez vozu: stěna a podlaha se doplňují zvlášť podle čáry styku, pod vozem stínová podlaha,
za vozem u stěny světlá), `*_stin.png` (kontaktní stín jako násobicí vrstva, pro vložení vozu na jiné pozadí).
Složení vozu zpět na pozadí = originál (průměrná odchylka 0,12–0,28/255). Hotovo: g01, g03, g08, g09, g10, g11.
Pozor: g05 (detail kola, vůz přes celý snímek) spadl na paměť (OOM 14 GB), vrstvy nemá a nepotřebuje. Spouštět **jeden pohled na proces**.

**2. Odlesk po laku.** Maska laku = maska vozu × světlý a nebarevný pixel, bez malých ostrůvků (ráfky) a s ruční výjimkou SPZ,
alfa vážená „tvarem“ (místní jas proti okolí), skládání `screen`. Na **boku g10** měkký svislý pruh po dveřích vypadá jako odraz softboxu:
**funguje**. Na 3/4 záběru g03 je na bílém laku slabý a spíš „zesvětlí“ přední partie (bílá + světlo = bílá). Tmavá „vlajka“ (odraz černé desky)
v pohybu působila jako rovná šedá čára přes blatník i dveře: **zamítnuto**. Pozor na easing: exponenciální `easeInOut` prohnal pruh přes vůz
za 0,4 s; pro pomalý průjezd `hladka` (smootherstep), 2,5–3 s.

**3. Rotace kola** (g05). Ráfek změřen fitem elipsy: střed (915,3; 953,5), poloměr 211 px (téměř kruh). Otáčí se jen kruh ráfku, pneumatika
stojí a podle rychlosti se prolínají 3 předem rozmazané verze (rozmazání po obvodu jen tmavých pixelů pneu, blatník a podlaha se nepřenesou),
ráfek má rozmazání kopiemi v kódu + podsnímky. **Rychlá rotace (≥ ~2 ot./s) je přesvědčivá.** Výhrada: **brzdový třmen je v ráfku a točí se s ním**,
při pomalém valení je to vidět (u skutečného auta stojí). Logo na středu se točí (u pevných středů ve skutečnosti taky). Kolo se točí na stojícím autě:
ve videu jen s pohybem okolí (kamera, rychlostní linky v UI) nebo jako detail na střih.

| # | technika | verdikt | důkaz | výpočet |
|---|---|---|---|---|
| 4 | rozsvícení světel | **funguje** | `t4_svetla.mp4`, `t4_svetla_pas.jpg`, `t4_svetla_detail_predek.jpg` | 7 s za 66 s |
| 5 | kamera 2,5D (stěna / podlaha / vůz) | **s výhradou** (malé posuny) | `t5_kamera.mp4`, `t5_kamera_detail.jpg` | 4 s za 40 s |
| 5b | otočka 360° (prolnutí / švih) | **nefunguje** plynule, jen krokování | `t5b_otocka_*_pas.jpg` | ffmpeg, sekundy |
| 6 | SaaS: skleněná karta, popisek s linkou, kurzor, přepínač Night | **funguje** | `t6_saas.mp4`, `t6_saas_pas.jpg`, `t6_nahled/` | **1 s výřezu = 12 s**, 4 s za 40 s |

**4. Světla.** Nic se nekreslí: k obrázku „vyp“ se přičte (`lighter`) kladný rozdíl zap − vyp z konfigurátoru (páry jsou pixelově zarovnané),
odhalený rostoucím kruhem od středu masky („uvítací“ náběh LED, 0,25–0,55 s), + slabá záře = rozmazaný rozdíl (`screen`, krátký nádech při zapnutí).
Zadní světla (úhel 180) naskočí červeně a jen ve svítilnách: velmi přesvědčivé. Předek ve dne (úhel 030): rozsvítí se obrys ledvinek Iconic Glow
a denní svícení, ve 100 % jasné, v celku jemné. Den → noc (g01 → g02, stejná kamera, prolnutí 1,6 s) působí jako stmívání studia, světla zůstanou:
nejsilnější „wow“ z rendrů. Mezi stavy je obraz chvíli šedivý (prolnutí v sRGB), na dobu ho zkrátit.

**5. Kamera 2,5D** (g03). Žádná mapa hloubky (MiDaS/torch tu není a natažené okraje by stejně vznikly), místo ní **známá geometrie studia**:
stěna = svislá rovina, podlaha = vodorovná rovina kreslená po pásech 4 px, každý pás ve své hloubce Z(y) = K / (y − yV) (úběžník yV ≈ 760),
vůz = karta v hloubce styku předního kola. Nájezd 12 % + boční posun ±90 px za 4 s: stěna se posouvá pomaleji, podlaha plynule, vržený stín jede
s podlahou, nic se nenatahuje. Výhrada: vůz je plochá karta (při velkém posunu by se neměnila perspektiva vozu) a při krajní výchylce je za pravým
rohem nárazníku u styku stěny a podlahy vidět drobná tmavší ploška z doplněného pozadí. **Držet boční posun do ~±60 px a nájezd do ~10 %.**
**5b. Otočka 360°** (36 snímků po 10°): prolnutí sousedních úhlů dělá dvojitá kola, švih 180° za 0,5 s (rozmazání z 6 kroků) taky. Plynulá rotace
z rendrů nejde. Použitelné: **krokování úhlů na doby** (tvrdý střih po 10–30°, jako klikání v konfigurátoru), případně krok schovaný za švihem UI.

**6. SaaS přes fotku.** Fotka v canvasu, UI v DOM nad ní (Manrope ze `znacka.css`): skleněná karta `backdrop-filter: blur(22px) saturate(1.25)`
s fakty doslova z bmw.cz (230 kW (313 hp), 0–100 km/h 5.7 s, 250 km/h), pružina 3 %, řádky postupně; tečka s pulzem na ledvince + linka, která
se vykreslí, a skleněná pilulka „BMW Iconic Glow“; kurzor přijede ease-out, klikne (zmáčknutí 12 %), přepínač zmodrá (#1C69D4) a fotka přejde
do noci (g03 → g04). Karta a popisek při nočním režimu plynule přejdou na tmavé sklo se světlým textem (na tmavém studiu byla světlá karta nečitelná).
Výkon v pořádku: 1 s výřezu 12 s výpočtu (V002 složitá scéna ~35 s). Drobnosti: bílá linka nad bílou kapotou má slabý kontrast (přidat jemný stín),
uprostřed prolnutí den/noc je text karty krátce málo kontrastní.

**Limity materiálu.** Statické rendry z pevných kamer: 14 pohledů galerie + 36 úhlů otočky (po 10°) + interiér (kostka). Žádný skutečný 3D model,
žádná jízda: vůz se nikdy nehne vůči podlaze (kola stojí na místě), pohyb jen kamerou 2,5D, světlem, UI a střihem. Páry den/noc existují jen
pro g01/g02 a g03/g04, páry světel zap/vyp pro všech 36 úhlů otočky. Detail kola jen g05/g06 (předek). Rendry mají studio, které nejde změnit
bez vyříznutí (na tmavé UI pozadí funguje vůz + `*_stin.png`, stín je tam ale málo vidět).

**Doporučení pro koncept.**
1. Stavět na tom, co je skutečné: **přepínače stavů z konfigurátoru** (světla zap/vyp, den/noc, úhel otočky) ovládané kurzorem a UI kartami.
   SaaS „konfigurátor jako zážitek“ je přirozený jazyk pro tenhle materiál a nic nevymýšlí. Den → noc s rozsvícením je kandidát na drop 2 (výkon).
2. Kamera: pomalé nájezdy 2,5D (do 10 %, posun do ±60 px), střih na dobu mezi pohledy galerie, otočka jen po krocích na doby.
3. Odlesk po laku jen na bocích (g07, g10) a na nočních záběrech, slabě a jednou za záběr. Na 3/4 bílém laku spíš ne.
4. Rotace kola jen rychlá (výkon, 16–22 s), jako detail g05 s rychlostními linkami v UI nebo na střih, ne pomalé valení.
5. Interiér (luxus, 10–14 s) zatím netestován: kostka 2000×2000 dovolí pomalé panorama (pohled z kostky v canvasu/WebGL), doporučuji samostatný krátký test.
6. Před plným renderem počítat ~10–17 s výpočtu na 1 s videa pro tyto scény (bez zrna a těžkých filtrů).

## Storyboard / časová osa
Kreativní ředitel 2026-11-01. Koncept „ONE CONTROL“ (viz Režijní list). Časy přesně podle `hudba.json` (120 BPM, doba 0,5 s, takt 2,0 s;
drop 1 = 4,0 · zlom 10,0 · stoupání 14,0 · drop 2 = 16,0 · logo 21,0–22,0 · end card 22,0–25,0). Snímek = 1/60 s.
Render: galerie `g*` = `materialy/konfigurator/galerie/`, otočka `vyp/uhel_*`, `zap/uhel_*` = `360_svetla_vyp|zap/`, masky `materialy/masky/`.

**Pevné rozvržení (pro animátora i kritika)**
- **Lišta konfigurátoru** (spojka záběrů, M2): střed x 960, y 900, 760×64, rádius 32, bílá 94 % + okraj 1 px `#E6E6E6` + dvouvrstvý měkký stín;
  v noci (od 15,875) tmavé sklo `#262626` 88 % se světlým textem. Vlevo miniatura vozu (výřez z `g03_*_vuz.png`, 64×36) + „BMW 740d xDrive Sedan“
  (Manrope 500, 20 px, `#262626`), vpravo segmentový přepínač **Design · Comfort · Performance** (Manrope 500, 18 px). **Ukazatel** `#1C69D4`
  (jediný akcent) je na snímku 0 sbalený do tečky 12 px vlevo od „Design“. Lišta je vidět 0,0–20,75, pak se stáhne do knobu.
- **Scéna (stage)** jen v úvodu a ve zlomu: x 192–1728, y 64–828 (1536×764), rádius 28, okolí `#F2EFEB`, stín scény měkký (60 px, 10 %).
- **Nadpisy**: Manrope 700, VERZÁLKY, 88 px, prostrkání −1 % → při pohybu −1 %…+3 %, `#262626` na světlém, `#FFFFFF` na tmavém; vždy v pravé nebo
  horní volné části stěny studia, nikdy přes vůz, celé v bezpečné zóně (96 / 54 px, nic důležitého pod y 940). Odkrytí maskou zdola **jako celek**
  (0,2 s, ease-out) + pomalé roztažení prostrkání po celou dobu; odchod maskou nahoru (0,125 s, ease-in), **příchozí text začne až po odchodu**.
- **Čísla**: Manrope 300, 140 px, rolující číslice (každá ve vlastním sloupci 0–9, jako počítadlo na bmw.cz), jednotka 40 px `#8E8E8E` (v noci `#BBBBBB`),
  popisek nad číslem Manrope 500, 22 px. **Jediný text na obrazovce v jednom okamžiku** (lišta = UI, nepočítá se).
- **Kurzor**: macOS šipka (černá, bílý okraj 1,5 px), přilétá už v pohybu (exponenciální ease-out), natočení ke směru letu, hover ×1,25, stisk −15 % na 3 snímky
  + kroužek akcentu `#1C69D4` (0,3 s), při tažení vozu ruka „grab“. Kurzor **jen způsobuje** změny (M5).

| čas (takt · doba) | obraz (který render, jaký pohyb) | text / UI | efekt | zvuk / událost |
|---|---|---|---|---|
| **0,0–2,0** (T1 · d1–4) úvod | Snímek 0 = hotový obraz: scéna se studiem, v ní `vyp/uhel_060` (vůz 3/4 zepředu), kamera už jede (makro dotlačení 1,00→1,03 do 2,0, M6). 0,5 kurzor (přiletěl zprava v pohybu) chytí vůz, **0,5–1,5 tažení doprava = krokování otočky** `060→050→…→350→340` (8 tvrdých kroků, rozestupy se prodlužují jako setrvačnost: 0,56 · 0,63 · 0,71 · 0,80 · 0,91 · 1,04 · 1,22 · **1,50**), žádné prolnutí ani rozmazání mezi úhly. 1,5 puštění. Vůz ≥ 45 % výšky obrazu (výřez ≤ 1,3×). | Snímek 0: „PERFECTION IN EVERY DETAIL“ (náš překlad claimu bmw.cz) nahoře na stěně scény nad vozem, prostrkání se stahuje 0,0–1,0; odchod 1,0–1,125. Lišta od snímku 0. | Háček = vůz se pod rukou otočí čelem k divákovi (skutečné chování konfigurátoru). Kamera neustále v pohybu. | klavír 0,0 · lusknutí 0,5 = měkký klik chycení · tiché „detent“ cvaknutí na každý krok (−12 LU) · lusknutí 1,5 = poslední krok |
| **2,0–4,0** (T2 · d1–4) úvod, náběh | `vyp/uhel_340` → **2,0 světla se probudí**: `zap/uhel_340` přes rozdíl (test 4: rostoucí kruh od středu masky 0,25–0,55 s + krátký nádech záře z rozmazaného rozdílu). Dotlačení 1,03→1,06. 3,0–4,0 nádech: scéna se zvedne 1,00→1,02 a stín pod ní se prohloubí. Kurzor letí po oblouku k liště, 3,5 hover nad „Design“, 3,875 stisk. | 2,25–3,25 „THE NEW BMW 7 SERIES“ (nahoře nad vozem, maska zdola + roztažení), odchod 3,25–3,375. 3,5 ukazatel (tečka) se při hoveru natáhne o 8 px k „Design“ (předtucha). | Uvítací světla = první „živý“ moment, motivovaný: vůz se otočil k divákovi a pozdraví. | kopák od 2,0 · „shimmer“ světel vrchol 2,1 · obrácený činel + vír 3,0–4,0 · tichý hover 3,5 |
| **4,0–6,0** (T3 · d1–4) **DROP 1** | **4,0 klik → scéna se rozšíří přes celý obraz** za 0,35 s (rohy 28→0, okraje se směrovým rozmazáním, kriticky tlumené, M2); uvnitř na 4,0 tvrdá výměna `uhel_340` → **`g03`** (galerie 2560: vůz na **stejném místě a ve stejné velikosti** podle bboxu masek = match-position, rozdíl schovaný v rozšíření). 4,0–6,0 kamera 2,5D z testu 5 (stěna / podlaha / vůz), nájezd 1,00→1,07, posun −50 px. Vůz ~70 % šířky, ≥ 45 % výšky. | Ukazatel přeskočí na „Design“ (náběžná hrana předběhne, dvě pružiny, M1). 4,25–5,0 „DESIGN THAT INSPIRES“ vpravo nahoře na stěně; odchod 5,0–5,125. 5,125 kurzor najede na masku ledvinek → tečka s pulzem, linka 1 px (+ jemný stín kvůli bílé kapotě) se vykreslí 5,125–5,3, pilulka „BMW Iconic Glow“ vyskočí z konce linky 5,25 (pružina 3 %); odchod 5,875–6,0 (linka se stáhne do tečky). | Největší změna měřítka (karta → celý obraz) přesně na drop. **5,75 glint**: jeden teplý přejezd světla po chromovém obrysu ledvinek, jen v masce, 0,4 s (M6). | úder + činel 4,0 = klik kurzoru · měkký „air“ swoosh rozšíření (vrchol 4,1) · hi-hat · UI pop 5,25 · třpyt 5,75 (= sklo 5,75) |
| **6,0–8,0** (T4 · d1–4) exteriér | **6,0 match cut kolo → kolo**: tvrdý střih na **`g05`**, střed ráfku g05 přesně tam, kde bylo přední kolo g03 na 5,98 (kolo se skokem ~2× zvětší = punch-in na kopák). 6,0–6,5 kamera klouže doleva; 6,5 navazuje **`g06`** (stejné studio, kamera posunutá: napojit podle polohy kola, švih 0,12 s se směrovým rozmazáním → působí jako jízda kamery). **7,0 švih doleva** (stejný směr kamery) → **`g10`** pravý bok, vůz ≥ 70 % šířky; 7,0–8,0 měkký odlesk softboxu přejede po dveřích (test 2b, smootherstep, 1,2 s). | 6,0–7,0 bez nadpisu (obraz mluví, kamera se hýbe). 7,0–7,4 kótovací linka (1 px `#262626`, koncové rysky) se vykreslí od zadního k přednímu nárazníku přesně podle bboxu `g10_*_vuz.png`, nad ní 7,15–7,6 rolující číslice **„5,395 mm“** (délka z bmw.cz, viz otázky); odchod 7,85–8,0 (linka se stáhne ke středu). | Jeden směr kamery přes 3 záběry (doleva), match cut kolo na kolo, odlesk po laku jen na boku (G7). | kopák + basa 6,0 = střih · tichý švih 6,5 · swoosh 7,0 · tiché tikání číslic 7,15–7,6 · sklo 6,75 / 7,75 |
| **8,0–10,0** (T5 · d1–4) záď | **8,0 tvrdý střih `g10` → `vyp/uhel_270`** (stejný profil, velikost a poloha vozu srovnané podle masky; ověřit, že u boku není vidět rozdíl světel). 8,0 kurzor chytí vůz a táhne: **krokování `270→260→…→180`** (9 kroků se setrvačností, poslední přesně **9,0**). **9,0 zadní světla naskočí červeně** (`zap/uhel_180` přes rozdíl, test 4). 9,0–10,0 dotlačení 1,00→1,05 (výřez ≤ 1,3×, vůz ≥ 45 % výšky). | 9,125–9,875 „PRECISE FROM EVERY ANGLE“ (nahoře nad vozem), odchod 9,875–10,0. | Druhé krokování otočky (rytmicky jinak: 9 kroků přes celý takt), rozsvícení zadních světel na obrácený činel. | klik chycení 8,0 · cvaknutí kroků · obrácený činel 9,0 → „shimmer“ zadních světel (vrchol 9,05) · sklo 9,75 |
| **10,0–12,0** (T6 · d1–4) **ZLOM: luxus a pohodlí** | **10,0 kurzor klikne na „Comfort“ → z lišty vyjede bílý list (sheet)** s horními rohy 28 px a za 0,5 s (ease-out, kriticky tlumené) zakryje obraz až na okraj 48 px nahoře a po stranách = zase zaoblená scéna (M2, kontrast k full-bleed). Exteriér pod ním ustoupí (0,96, ztmavne o 25 %). Na listu **`g12`** palubní deska (dřevo, displeje), pomalé dotlačení 1,00→1,05 + posun 30 px doprava. | Ukazatel přejede na „Comfort“ (dvě pružiny). 10,5–11,375 „YOUR PRIVATE LOUNGE“ (vlevo nahoře na světlém čalounění stropu; kontrast ověřit, jinak bílý text se stínem 1 px), odchod 11,375–11,5. | Ticho a prostor: pohyb jen kamery a listu, **11,0 glint** po dřevěné liště palubní desky (jen v masce dřeva, 0,5 s, teplý). Žádný třes, žádné zrychlení. | klik 10,0 · hudba přejde na klavír · měkký swoosh listu (vrchol 10,25) · lusknutí 10,5 / 11,5 · třpyt 11,0 |
| **12,0–14,0** (T7 · d1–4) luxus | **12,0 přechod přes hranu dveří**: **`g13`** (sedadla z boku, otevřené dveře) vjede zprava, náběžná hrana masky = svislá hrana dveřního sloupku v g13 (0,45 s, ease-out), `g12` odjíždí doleva pomaleji (paralaxa). 12,0–13,5 dotlačení 1,00→1,05. 13,0 kurzor přilétá k úchytu listu (krátká tečka nahoře uprostřed), **13,5 chytí, 13,625–14,0 list odhodí dolů** (ease-in) → pod ním **`g03` den** přes celý obraz, exteriér se srovná zpět na 1,0 a plný jas. | 12,5–13,375 „YOUR OASIS OF CALM“ (náš překlad „Vaše osobní oáza klidu“), odchod 13,375–13,5. | Přechod přes objekt (hrana dveří), ne clona ani prolínačka. Prošívání sedadel v g13 = hlavní detail pohodlí. | swoosh dveří (vrchol 12,1) · kopák 12,0 · lusknutí 12,5 / 13,5 · klik úchytu 13,5 · swoosh odhození (vrchol 13,9) |
| **14,0–16,0** (T8 · d1–4) **STOUPÁNÍ** | **`g03` den** přes celý obraz, dotlačení 1,00→1,08 (napětí, kamera jen dopředu). **14,0 kurzor chytí modrý ukazatel v liště a táhne doprava**: zadní hrana drží, náběžná hrana (= knob, bílý kruh 28 px s okrajem) jede a ukazatel se natáhne v dlouhou modrou výplň posuvníku (y 900, x 240→1680). **Za knobem se odkrývá `g04` noc** (svislá měkká hranice 80 px, poloha hranice = poloha knobu přepočtená na šířku obrazu, D7, M3a). Knob zrychluje (ease-in) s řazením. **15,5 hranice přejede přední světla → světla g04 vzplanou** (nádech záře z rozdílu g04 − g03 jen v masce světel, 0,3 s). 15,875 celý obraz je noc, lišta přejde na tmavé sklo. | 14,25–15,25 „DYNAMICS ON EVERY ROUTE“ (vpravo nahoře, zatím na světlé stěně), odchod 15,25–15,375 (před vzplanutím). Knob bez bubliny. | **Přímá manipulace den → noc** (skutečné světlo z rendrů BMW). Hudba i obraz rostou do dropu. | 14,0 startér + motor · řazení 14,5 / 15,0 · spiccato šestnáctiny · obrácený činel 15,0 + vír do 16,0 · „shimmer“ světel 15,5 · **hlasitost roste** (C032) |
| **16,0–18,0** (T9 · d1–4) **DROP 2: výkon** | **16,0 tvrdý střih s průnikem na `g02`** (předek v noci, světla), vůz výřezem posunutý doleva (pravá třetina volná pro UI), nástup měřítkem 1,10→1,04 kriticky tlumeně za 0,4 s (jeden pohyb, ne tam a zpět) + krátký puls záře nejjasnějších pixelů světel (0,25 s, jen v masce světel). **17,0 tvrdý střih na řazení → `g04`** (noc 3/4, vůz vlevo), dotlačení 1,00→1,05. Vůz ≥ 45 % výšky. | **16,0 výplň posuvníku se smrští a ukazatel dopadne na „Performance“** (dvě pružiny, M1 = úder). 16,25 z ukazatele se vysune **rychlostní posuvník** v pravé třetině (x 1200–1760, y 760, dráha 4 px, rysky po 50, M4); knob s bublinou: **číslo z polohy knobu**, rolující číslice + „km/h“. 16,25–17,0 knob rychle (1. stupeň), **17,0 řazení**: knob na 3 snímky zpomalí, bublina se nakloní o 2° proti směru, 17,0–18,0 dojíždí (ease-out). Rysky se rozsvítí modře, když je knob mine. | Nejsilnější kontrast videa: tma, světla, střih, start rychlosti. Mezihodnoty jen v pohybu (C8), cíl přesně 250. | **úder + činel + motor 16,0 = nejhlasitější místo videa** · hi-hat osminy · řazení 17,0 (+ klik bubliny) · tiché tikání rysek |
| **18,0–20,0** (T10 · d1–4) výkon | `g04` 18,0–19,0, **měkký světelný přejezd po noční karoserii** (odlesk z testu 2b, slabě, 18,0–18,8, smootherstep). **19,0 tvrdý střih na `g02` užší výřez** (1,2×: ledvinky + světla), dotlačení 1,20→1,25. | **18,0 knob dojede na 250**: bublina squash 3 % (jen UI), dráha 1× modře blikne; bublina se rozroste v číslo **„250 km/h“** + popisek „Top speed“ (18,0–18,15). 18,875–19,0 odjede nahoru (ease-in); 19,0 zdola **„5.7 s“** s popiskem „0–100 km/h“ (číslice dorolují 0.0→5.7 za 0,3 s). Knob a dráha zůstávají (knob na konci). | Každá karta na svůj takt, číslo vázané na fyzický prvek (knob). | kopák + basa + měkký „lock“ 18,0 · řazení 18,5 · kopák + swap 19,0 · sklo osminy |
| **20,0–22,0** (T11 · d1–4) výkon → **skládací logo** | **20,0 tvrdý střih na `g04`** jiný výřez (1,15×, posun 40 px), dotlačení. **21,0 přechod:** dráha i lišta se stáhnou do knobu (20,75–21,0), **knob letí do středu** (21,0–21,25, ease-in-out) a **rozlévá z sebe světlé studio `#E7E2DC` kruhem přes všechny 4 rohy** (21,0–21,35, zaplavení M3b, ≥ 0,3 s), noc zmizí pod ním. | 20,0 **„230 kW“** s popiskem „Power“ (výměna jako 19,0), odchod 20,75–20,875. **Logo (M7, max 3 kroky, vrstvy `znacka/logo/vrstvy/`, stejný viewBox, cesty beze změny):** ① 21,0–21,45 knob opíše **vnější prstenec** (01, `#6F6F6F`, tah po obvodu po směru hodin z horní polohy); ② 21,5–21,85 **vnitřní kruh + modré čtvrtiny** (02–04, `#0066B1`) se dotočí kolem středu o 90° do svých poloh, kriticky tlumeně, bez překmitu; ③ **B 21,875 · M 21,9375 · W 22,0** dosednou (posun 10 px dostředivě + krytí 0,12 s, bez škálování) = **poslední díl přesně na úder 22,0**. Logo ~360 px, střed (960, 470). | Kruh knobu → prstenec loga (rým celého konceptu). Čisté, bez záře, odlesku a částic. | kopák 20,0 · malý buben 20,5 · obrácený činel 21,0 + měkký swoosh zaplavení (vrchol 21,15) · tichý „ink“ tón tahu prstence · měkký dopad čtvrtin 21,5 · vír 21,5–22,0 · jemné kliky písmen 21,875 / 21,9375 |
| **22,0–24,0** (T12 · d1–4) **END CARD** | Světlé studio `#E7E2DC` (velmi jemná vinětace), hotové **originální logo** (`00_slozene_original.svg`, nedeformované). Souvislé dotlačení 1,00→1,03 až do 25,0 (kriticky tlumené, nikdy nestojí). | 22,5 pod logem „THE NEW 7 SERIES“ (Manrope 700, 44 px, `#262626`, maska zdola jako celek). 23,0 pod ním **modrá pilulka naposledy** (ukazatel z lišty, M1): roztáhne se z bodu do tlačítka „Configure yours“ (Manrope 500, 24 px, bílá, pružina 3 %). 22,5 dole disclaimer „Concept ad · not affiliated with BMW“ (Manrope 500, 18 px, `#8E8E8E`, y ≈ 990). End card je jedna navržená kompozice, prvky přicházejí po sobě. | Klid po výkonu, ale v pohybu (C6). | **22,0 úder + činel + klavírní akord = nejsilnější dopad loga** · tichý pop pilulky 23,0 |
| **24,0–25,0** (T13 · d1–2, půltakt) | Dotlačení pokračuje do 25,0. | 24,0 kurzor přilétá zdola zprava (v pohybu), **24,5 klikne na „Configure yours“** (stisk −15 %, kroužek akcentu, pilulka krátce `#0653B6` a zpět). Poslední snímek = hotová end card s kurzorem u tlačítka, nic nepřekrývá logo ani texty. | Poslední „akce“ diváka: konfigurátor zve ke konfiguraci. | klik 24,5 · doznění akordu do 25,0 |

### Motiony ve videu (kde přesně, pro kritika, kritérium 7)
| motion | kde (časy) | jak je ho poznat |
|---|---|---|
| **M1** Shape morphing (`twoclipping-5cba86`) | 3,5 · **4,0** · 10,0 · **14,0–16,0** · **16,0–16,25** · 21,0 · 23,0 | jeden modrý ukazatel: tečka → ukazatel kapitol (dvě pružiny) → výplň posuvníku noci → zpět do ukazatele „Performance“ → rychlostní posuvník → knob → prstenec loga → tlačítko CTA |
| **M2** Spotify product film (`brainextends-e19ac3`) | 0,0–4,0 scéna · **4,0** scéna → full-bleed · 10,0 list = zase karta · 0,0–20,75 trvalá lišta · 21,0 sbíhání do středu | hrdinský obraz drží polohu přes předání (4,0 match-position, 6,0 kolo → kolo, 8,0 profil → profil), lišta konfigurátoru jako spojka |
| **M3** Photo print app (`twoclipping-221cab`) | **14,0–15,875** (a) přesvícení posuvníkem den → noc · **21,0–21,35** (b) zaplavení kruhem přes 4 rohy | noc se odkrývá pod knobem, světla vzplanou pod prstem; světlé studio se rozlije z knobu |
| **M4** White ball UI loop (`rossaxbt-94583b`) | **16,25–21,0** | posuvník 0 → 250 s bublinou nad knobem, rysky se rozsvěcují, pak karty 250 km/h · 0–100 km/h 5.7 s · 230 kW po taktech |
| **M5** Frame by Frame (`notdwd-7de38a`) | kurzor 0,5 · 3,5–4,0 · 5,125 · 8,0 · 10,0 · 13,5 · 14,0 · 24,5; záběry přijíždějí v pohybu (6,5 · 7,0) | kurzor jako postava (let po oblouku, hover, stisk, tažení), pilulka vyskočí z bodu, který kurzor označil |
| **M6** Taxtello (`daniel-haida-8691d4`) | dotlačení kamery celé video · **glint 5,75** (ledvinky) · **glint 11,0** (dřevo) · zdrženlivost 10,0–14,0 | makro produktová kamera, překmit < 2 %, jeden drahý světelný akcent na sekci |
| **M7** TypingMind logo reveal (`tdinh-me-815acb`) | **21,0–22,0** | logo se nejdřív poskládá (prstenec → čtvrtiny → písmena), poslední díl na 22,0, pak klid a dotlačení |

### Kontrolní snímky (před plným renderem, z výřezu s podsnímky, C028) a kritéria odmítnutí
Každý snímek ve 100 % a ve zmenšenině 270 px (A8). Odmítnout, když platí kterékoli kritérium.
| čas | co musí být vidět | odmítnout, když |
|---|---|---|
| 0,000 | hotový obraz: scéna, vůz `uhel_060`, nadpis, lišta | prázdné místo, zatmívání, text přes vůz, vůz < 45 % výšky |
| 1,50 / 1,52 | poslední krok otočky na 340, kurzor „grab“ | dvojitá kola / prolnutí dvou úhlů, rozmazání vozu |
| 2,30 | světla probuzená (LED v přední masce, obrys ledvinek) | záře mimo světla, kreslený tvar světla, šedivý mezistav |
| 3,95 / 4,02 / 4,20 | před klikem scéna; drop: scéna se rozšiřuje, uvnitř už `g03`; 4,20 skoro přes celý obraz | skok polohy vozu mezi 340 a g03 > ~10 px, probliknutí, ukazatel teleportuje |
| 5,40 | linka + pilulka „BMW Iconic Glow“ u ledvinek | pilulka přes vůz, linka nečitelná na bílé kapotě, dva texty naráz |
| 5,98 / 6,02 | match cut kolo → kolo | střed kola se mezi snímky posune > 20 px |
| 7,60 | kóta od nárazníku k nárazníku + „5,395 mm“ | konce kóty mimo nárazníky o > 6 px, jiné číslo než z bmw.cz |
| 9,10 | zadní světla svítí červeně, nadpis | světla mimo svítilny, rozdíl zap/vyp na karoserii |
| 10,25 | list v půli cesty, exteriér pod ním ztmavlý | prolínačka celého obrazu, list bez stínu/okraje |
| 12,20 | hrana dveří g13 vede přechod | rovný stírací pruh bez vztahu k obrazu |
| 15,00 / 15,55 | hranice den/noc pod knobem; světla vzplanula | hranice tvrdá nebo šikmá, šedivé prolnutí celého obrazu, záře mimo světla |
| 15,98 / 16,02 / 16,30 | nádech; drop 2: g02 noc + ukazatel na „Performance“; posuvník rychlosti vyjíždí | drop slabší než drop 1 (měřit YDIF / jas), vůz < 45 % výšky, UI přes vůz |
| 18,02 | „250 km/h“ přesně, squash bubliny | jiná hodnota, rozmazané číslo při zastavení |
| 19,50 / 20,50 | „0–100 km/h“ „5.7 s“ · „Power“ „230 kW“ | koně / „hp“, „elektronicky omezeno“, dva texty naráz |
| 21,15 / 21,40 | zaplavení přes všechny 4 rohy; prstenec z poloviny | kraj zaplavení nepřekryje roh, probliknutí, prstenec jiné tloušťky než originál |
| 21,70 | čtvrtiny se dotáčejí kolem středu | čtvrtina deformovaná, změna měřítka v jedné ose, překmit |
| 22,00 / 22,02 | **logo hotové na úder** | logo ≠ originál (překrýt `00_slozene_original.svg`, rozdíl > antialiasing), záře, odlesk |
| 24,98 | end card + CTA + disclaimer, kurzor u tlačítka | zamrzlý obraz (porovnat s 23,98: dotlačení), text mimo bezpečnou zónu, kurzor přes text |

### Pasti stavby (realismus a AI znaky)
1. **Vůz se nikdy nedeformuje ani nepřekresluje**: jen posun, měřítko (≤ 1,3× nativního rozlišení), maska, odkrytí, střih. Žádné natažení, warp, chromatický posun,
   glitch, duhy, plastový lesk na voze (G7). Záře jen ze **skutečného rozdílu** zap − vyp / noc − den, nikdy kreslená.
2. **Otočka 360° jen tvrdými kroky** (0,5–1,5 a 8,0–9,0), nikdy prolnutí sousedních úhlů (dvojitá kola, test 5b) ani rozmazání mezi nimi. Komprese snímků otočky
   je silnější: do 1,3× v pořádku, větší výřez ne. Na 2,0 a 9,0 dvojice `vyp`/`zap` musí být přesně zarovnané (posun 0 px).
3. **Match-position (4,0, 6,0, 8,0)** měřit z bboxu masek / středu ráfku, ne od oka. Skok polohy vozu mezi snímky > ~10 px působí jako chyba, ne jako střih.
4. **Studio jiné barvy mezi rendry** (galerie vs. otočka mají nepatrně jiný odstín stěny): na 4,0 a 8,0 porovnat průměrnou barvu stěny, když se liší > 3/255,
   srovnat jen pozadí (vrstva `*_pozadi.png`), nikdy lak vozu.
5. **Kamera 2,5D** jen s geometrií z testu 5: nájezd ≤ 10 %, boční posun ≤ ±60 px; jinak tmavá ploška za nárazníkem. Nikdy dva pohyby kamery naráz, nikdy zoom tam a zpět.
6. **Den → noc (14–16)**: měkká **svislá** hranice vázaná na knob, nikdy prolnutí celého obrazu (šedivý mezistav sRGB, test 4). Bílá karoserie v noci je šedá: **nezesvětlovat**.
7. **Odlesk po laku** jen na boku `g10` (7,0) a slabě na `g04` (18,0), jednou za záběr, smootherstep. Na 3/4 bílém laku ne, tmavá „vlajka“ zakázaná (test 2).
8. **Kolo** se v tomto konceptu netočí (pomalé valení prozradí točící se třmen, na stojícím voze působí falešně). Výkon nesou světla, noc, střihy a číslo.
9. **UI nikdy přes vůz** a nevrhá na render stín; pilulky, nadpisy a čísla jen na volné stěně studia. Sklo max. 1–2 prvky (bublina, noční lišta), nikdy přes vůz,
   jako rozmazaný klon scény (ne `backdrop-filter: url()`), `will-change` ne na škálovaných prvcích.
10. **Text**: jen jeden text v jednom okamžiku, odcházející zmizí dřív, než přijde nový. Text se pořád hýbe (prostrkání, maska), nikdy nestojí. Bez teček (E8),
    anglicky, čísla přesně: `250 km/h`, `0–100 km/h` + `5.7 s` (pomlčka –), `230 kW`, žádné koně ani „electronically limited“ (C8).
11. **Kontrast**: bílá linka / tmavý text nad bílou kapotou a světlou stěnou ověřit ve 270 px; linka dostane stín 1 px. V noci text bílý.
12. **Zaplavení 21,0** přes všechny 4 rohy a ≥ 0,3 s, jinak probliknutí. Během zaplavení žádný text.
13. **Logo**: jen vrstvy `vrstvy/01–09` (stejný viewBox, cesty beze změny), rotace jen kolem středu loga (170,08 / 170,08), žádné škálování v jedné ose, žádná záře,
    odlesk ani barevné střepy. Barvy jen `#0066B1` + `#6F6F6F`. Na 22,0 musí složené vrstvy = originál.
14. **AI znaky obecně**: žádné částice, tečkové mřížky, gradienty na UI, třes kamery, text v rozích, každé slovo zvlášť, skákavé pružiny (UI ≤ 3 %, kamera a plochy bez překmitu),
    `Math.random` bez semínka, „cokoli, co vypadá jako šablona“.
15. **Energie (C7, V001)**: v každém taktu se něco hýbe nepřetržitě (kamera, kurzor, knob, prostrkání) a na každou dobu je událost (tabulka výše). Při kontrole
    hledat úseky > 0,5 s bez nové události a > 1 s bez změny obrazu.

### Pořadí stavby
1. **Kostra a tokeny**: rozvržení (lišta, scéna, typografie, kurzor) z `nastroje/vzory/scena.html`, načtení rendrů a masek, kamera 2,5D z testu 5.
2. **Klíčové snímky drop 1** (3,95 · 4,02 · 4,20 · 4,50) a **drop 2** (15,55 · 15,98 · 16,02 · 16,30 · 18,02) jako statické snímky z výřezu s podsnímky
   → schválení režisérem / kreativním ředitelem **před** stavbou zbytku (porovnat sílu dropů: drop 2 musí být silnější).
3. **Stoupání 14,0–16,0** (posuvník noci, nejsilnější realistický efekt) + přechod do dropu 2 jako krátký výřez videa (`--od 13.5`, 3 s).
4. **Logo a end card 20,75–25,0** (M7 podle vrstev, kontrola překrytím s originálem na 22,0).
5. **Úvod 0–4** (krokování otočky, probuzení světel, háček) → **exteriér 4–10** → **interiér 10–14** → **výkon 16–21**.
6. Změřit 1 s výřezu (odhad 12–17 s výpočtu na 1 s videa), pak `--nahled doby --bpm 120` (snímek na každou dobu) a teprve potom plný render
   s `--sub 4`, rychlé úseky `--sub-rychle 8 --rychle 3.9-4.4,5.9-6.1,6.9-7.1,15.9-16.5,20.9-21.4`.
7. Kritik dostane zadání a video, ne toto zdůvodnění (kontrola podle tabulky kontrolních snímků výše).

### Otevřené otázky kreativního ředitele (rozhodne režisér)
- „5,395 mm“ (délka z bmw.cz „5 395 mm“, anglický zápis s čárkou) smí? Jinak v 7,0–8,0 kóta bez čísla s popiskem „Length“ nebo jen odlesk.
- End card „THE NEW 7 SERIES“ + tlačítko „Configure yours“ (vlastní copy, CTA odkazuje na konfigurátor = koncept).
- Vlastní anglická hesla: „PERFECTION IN EVERY DETAIL“, „THE NEW BMW 7 SERIES“, „DESIGN THAT INSPIRES“, „PRECISE FROM EVERY ANGLE“, „YOUR PRIVATE LOUNGE“,
  „YOUR OASIS OF CALM“, „DYNAMICS ON EVERY ROUTE“ (překlady / volné verze claimů bmw.cz, žádná fakta).

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
