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
- **Koncept jednou větou**: (doplní kreativní ředitel)
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

## Storyboard / časová osa
(doplní kreativní ředitel)

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
