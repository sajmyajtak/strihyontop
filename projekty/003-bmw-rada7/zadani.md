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

- **Odpovědi režiséra ke konceptu „ONE CONTROL“** (2026-11-01): délka „5,395 mm“ smí, jen když je doslova v technických údajích **740d xDrive Sedan**
  na bmw.cz (jinak jen popisek bez čísla) · end card: skládací logo je hrdina, pod ním „THE NEW 7 SERIES“ (volný překlad „NOVÉ BMW ŘADY 7“) + „Configure yours“
  + disclaimer, nic víc · vlastní anglická hesla smí (bez faktů), ale **méně textu**: nejvýš ~4–5 textových momentů za 25 s, energii nese pohyb ·
  logo varianta A (21,0–22,0) platí · kolo ve výkonu vynechat je v pořádku · klíčové snímky obou dropů schválí kreativní ředitel dřív, než se staví zbytek.

- **Odpovědi režiséra k oponentuře** (2026-11-01): nová stavba dropu 2 **ano** (noc dokončená do 15,5, 15,75–16,0 zatmění se skutečným tichem, na 16,0 z černé
  nejdřív světla g02, pak karoserie). Ticho udělá zvukař **automatikou v mixu** (`sfx.py --automatika`), hudba.wav a její časování se nemění ·
  barevná úprava nočních rendrů g02/g04 (hlubší černá, kontrast, chlad, vinětace) **ano**, je to grading, ne změna tvaru vozu · test kostky interiéru
  jako CSS 3D (natočení ~35°) **ano**, udělá ho animátor ve výrobě v bloku interiéru; když neprojde (ostrost, výpočet), luxus zůstane na g12–g14 se střihy ·
  „skládací logo“ = **skládání z dílů** (prstenec → čtvrtiny → písmena), ne origami.

- **Odpovědi režiséra k revizi** (2026-11-01): 5 textových momentů + end card platí · světla na g03 z rozdílu g04 − g03 jen v masce světel **ano**
  (skutečné pixely BMW, ve dne rozsvícené denní svícení je věrohodné) · posun nočních rendrů doleva s doplněním černé **ano**, šev kontrolovat ve 100 %
  · lišta smí během luxusu 10,0–13,75 zmizet (nahrazuje ji list z ukazatele), kritik na ní netrvá · zvukař: automatika −18 dB 3,875–4,0 a 15,75–16,0
  záměrně ztlumí poslední údery víru, vír a obrácený činel mají doznít před těmito časy.

- **Synchronizace obrazu se zvukem v1 (pro animátora, režisér 2026-11-01)**: rysky rychloměru 50/100/150/200/250 se rozsvítí v **16,5 · 16,75 · 17,0 (řazení)
  · 17,1875 · 17,875** (knob na 250): průběh knobu 0 → 150 km/h v 16,25–17,0, pak ease-out do 250 v 17,875. Rolující číslice tikají v **7,15–7,525**
  (zámek 7,6), **18,875 · 18,9 · 18,928 · 18,96** (zámek 19,0) a **19,875 · 19,9 · 19,928 · 19,96** (zámek 20,0). Další tiché zvuky: stisk myši 3,875,
  přepínač 16,25, zámky 7,6 / 9,0 / 17,875, třpyt 5,75. Když animátor zvolí jiný průběh, napíše skutečné časy do zadání a zvukař je přesune.
  Verze bez hudby zůstává v úrovni mixu efektů (pro trendový zvuk v aplikaci), nenormalizovat na −14 LUFS.

- **Odpovědi režiséra ke klíčovým snímkům** (2026-11-01, po prohlédnutí archu): síla dropu 2 se měří **expozicí a kontrastem** (EV, std jasu), ne YDIF
  (odhalení z tmy nemůže přerůst změnu na světlé scéně) · **noční karoserie nesmí působit jako šedý hliněný model**: v masce karoserie smí grade zvednout
  světla laku o ~0,3–0,5 EV a přidat jemnou S-křivku, aby bílý lak četl jako bílý v noci (studio zůstává ~#060606, tvar beze změny); k tomu jemný
  odlesk po laku na 18,0 (past 7) · A8 na 0,0 stačí přes šířku (76 %), scénu nezvětšovat · kostka interiéru: pitch −6° ano (víc palubní desky a dřeva) ·
  kurzor „grab“ jako sevřená ruka (macOS styl), ne otevřená dlaň · banding v černé: jemný šum ze spritu ano.

- **Odpovědi režiséra k bloku B1** (2026-11-01): zaplavení 21,0–21,3 smí zůstat v minimální verzi, blok loga (B2) ho smí přestavět, hlavně ať knob
  plynule navazuje na oblouk prstence · návrat lišty odložit na 13,83 (nepřekrývat list) · **zvuk se přizpůsobí obrazu**: časy SFX přesune režisér
  podle skutečných časů v obraze (dosednutí „Performance“ 16,13, švih knobu 20,875, dopad pilulky 13,875, náraz knobu 15,5) po dokončení všech bloků;
  bloky B2 a B3 ať skutečné časy událostí, které se liší od sloupce zvuku, zapíšou sem do zadání stejně.

- **Odpovědi režiséra k bloku B2** (2026-11-01): disclaimer v 23,5 **ano** · rychlý úsek pro oběh prstence **20.7-21.7** (opraveno v příkazu renderu výše)
  · tichý švih na přílet kurzoru 24,0 **ano** (doplní režisér do SFX spolu s posuny z B1).

- **Zvuk v1b (režisér, 2026-11-01, po blocích B1–B3)**: SFX přesunuty na skutečné časy obrazu: přepínač Performance 16,25 → **16,13**, švih knobu
  20,95 → **20,875**; přidány dopad pilulky **13,875**, náraz knobu **15,5**, tichý švih kurzoru **24,0**, lišta pod okraj **5,875** a zpět **7,0** (82 událostí).
  Přegenerováno stejným příkazem do stejných souborů (`zvuk_v1.wav`, `zvuk_bez_hudby_v1.wav`), master −13,9 LUFS / −1,2 dBTP, hudba posun 0 vzorků,
  změny jen v okolí těchto časů. Odpovědi k B3: studio otočky o ~7/255 chladnější než galerie na střizích 4,0 a 8,0 nechat · výkon kostky (~24 s na 1 s) stačí ·
  švih 6,44–6,56 přidán do rychlých úseků renderu.

- **Odchylky schválené režisérem (pro kritiky, kolo 1)**: na dropu 2 **16,0–16,5 je vůz uprostřed** (symetrický „obličej“ z tmy, požadavek kreativního
  ředitele při schválení klíčových snímků); pravidlo „vůz vlevo, x ≤ 1000“ platí až od 16,5 (střihy výkonu). Verze bez hudby smí mít úroveň efektů (nenormalizovat).
  Přepis řeči netřeba (bez voiceoveru). Noční lak: grade v masce karoserie **+0,4 EV a S-křivka už od 14,0** (lak musí číst jako bílý), viz odpovědi výše.

- **Pokyn režiséra k artefaktům na stěně studia (kolo 1, nález kritika zadání)**: příčinou jsou hlavně silně komprimované zdrojové snímky otočky 360°
  (~60 kB WebP) a CRF 16. Režisér přepnul renderer na CRF 14 + aq-mode 3 (C037). Animátor: snímky otočky před použitím jemně vyhladit
  (ffmpeg `deblock` nebo `hqdn3d` slabě, jen na pozadí studia, ne na voze) a přes celý obraz dát velmi jemné zrno ze spritu (±1/255), které schová
  zbytkové bloky i banding. Kde to jde, místo otočky použít ostřejší galerii.

- **Odpovědi režiséra k opravám v2** (2026-11-01): hranice noci ~150 px před knobem (lineární přepočet) zatím nechat, rozhodne kolo 2 kontroly ·
  nájezd dropu 1 na 1,11 stačí · zaplavení dál z knobu (rým konceptu) · nové tiché SFX pro 1,875 (ztlumení studia), 14,0 (knob na začátek dráhy)
  a lety kurzoru netřeba, světlomet v 15,0 kryje zvuk řazení.

- **Odpovědi režiséra ke kolu 2** (2026-11-01, závazné pro opravy v3): (1) hranice noci **svázat přímo s knobem (±20 px)**, nikdy nepředběhne knob ani konec
  dráhy (když je potřeba, prodloužit dráhu) · (2) **celoplošné ztlumení 1,875–2,6 zrušit**; na 2,000 úder: celý rozdíl zap − vyp (denní svícení i hlavní
  světlomety) naskočí za 2 snímky, smí se jen mírně ztlumit pozadí studia (ne vůz, ne lišta) · (3) „YOUR PRIVATE LOUNGE“ **přesunout nahoru na světlý strop**
  podle storyboardu, text nikdy přes produkt · (4) přechod do g13 ve 12,0: když nejde čistá maska podle siluety, **tvrdý střih na dobu 12,0 s dotlačením**
  (realismus má přednost před efektem) · (5) drop 1 větší úder podle kreativního ředitele (stažení 1,00 → 0,94 v nádechu, pak rozšíření) · přesah vozu
  do x ≈ 1060–1120 ve výřezech 16,5 a 20,0 je přijatelný (UI vůz nepřekrývá).

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
- **Revize po oponentuře** (kreativní ředitel 2026-11-01, oponent 7,5 → cíl 9+): koncept beze změny, mění se **energie dropů a výkonu**.
  (1) Drop 2 = tma a ticho 15,75–16,0, na 16,0 jen světla na černé a karoserie vystoupí z tmy (nejsilnější obraz videa se nevypálí ve stoupání).
  (2) Výkon 16–18 střih na každou dobu se souvislým rychloměrem, 18–20,75 obří čísla jako typografické údery. (3) Noční rendry barevně upravené
  (studio ~`#060606`, kontrast, chladnější), nic nepřikreslené. (4) Drop 1 = přiznaný střih + nájezd na hrdinu 1,00→1,18. (5) Snímek 0 je uprostřed tažení.
  (6) M1 viditelně: ukazatel vyroste v list interiéru a list se smrští zpět do ukazatele. (7) Interiér: otočení hlavy v kostce + vložený detail voliče.
  (8) Předání do loga po krocích, logo hotové přesně na 22,000. (9) Méně textu: 5 textových momentů + end card (pokyn režiséra „nejvýš ~4–5“).
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
  v noci (od 15,5, revize) tmavé sklo `#262626` 88 % se světlým textem. Vlevo miniatura vozu (výřez z `g03_*_vuz.png`, 64×36) + „BMW 740d xDrive Sedan“
  (Manrope 500, 20 px, `#262626`), vpravo segmentový přepínač **Design · Comfort · Performance** (Manrope 500, 18 px). **Ukazatel** `#1C69D4`
  (jediný akcent) je na snímku 0 sbalený do tečky 12 px vlevo od „Design“. **Revize:** lišta je vidět 0,0–10,0 a 13,75–20,75. 10,0–13,75 je ukazatel
  rozrostlý v list (M1), lišta proto 10,0–10,15 zajede dolů pod okraj obrazu (ease-in) a 13,75–14,0 se vrátí (ease-out). 16,25–16,5 se lišta
  promění v **rychlostní posuvník** (x 1064–1824, dráha 8 px). 20,5–20,75 se stáhne do knobu. Když na 6,02 / 6,6 pneumatika g05/g06 sahá pod y 850,
  lišta 5,875–6,0 zajede dolů a vrátí se 7,0 se švihem na g10.
- **Scéna (stage)** jen v úvodu a ve zlomu: x 192–1728, y 64–828 (1536×764), rádius 28, okolí `#F2EFEB`, stín scény měkký (60 px, 10 %).
- **Nadpisy**: Manrope 700, VERZÁLKY, 88 px, prostrkání −1 % → při pohybu −1 %…+3 %, `#262626` na světlém, `#FFFFFF` na tmavém; vždy v pravé nebo
  horní volné části stěny studia, nikdy přes vůz, celé v bezpečné zóně (96 / 54 px, nic důležitého pod y 940). Odkrytí maskou zdola **jako celek**
  (0,2 s, ease-out) + pomalé roztažení prostrkání po celou dobu; odchod maskou nahoru (0,125 s, ease-in), **příchozí text začne až po odchodu**.
- **Čísla**: rolující číslice (každá ve vlastním sloupci 0–9, jako počítadlo na bmw.cz). **V bublině** nad knobem Manrope 300, 40 px.
  **Velká čísla výkonu 18,0–20,75** (revize): Manrope 300, písmo ~420 px (výška číslic ~300–360 px podle šířky sloupce), sloupec vpravo x 1064–1824,
  zarovnané doprava na konec rychlostní dráhy, účaří y ≈ 780. Jednotka („km/h“, „s“, „kW“) Manrope 500, 60 px, `#BBBBBB`, popisek nad číslem
  („Top speed“, „0–100 km/h“, „Power“) Manrope 500, 28 px, `#BBBBBB`. **Jediný text na obrazovce v jednom okamžiku** (lišta = UI, nepočítá se).
- **Textové momenty (revize, pokyn režiséra „nejvýš ~4–5“)**: ① „THE NEW BMW 7 SERIES“ 1,0 · ② popisek „BMW Iconic Glow“ 5,25 · ③ kóta „5,395 mm“ 7,15 ·
  ④ „YOUR PRIVATE LOUNGE“ 12,5 · ⑤ výkon 250 km/h / 5.7 s / 230 kW 18,0–20,75 · end card. Jiné nadpisy ne, energii nese pohyb.
- **Výkon 16,0–21,0 (revize)**: vůz (bbox masky) vždy jen v x ≤ 1000 a y ≤ 840, UI jen v pravém sloupci x 1064–1824. Noční studio je po úpravě
  jednolité `#060606`, takže render smí být posunutý doleva a za jeho levý okraj se doplní stejná barva (přechod 200 px, změřit, že není vidět šev).
- **Noční grade (revize, platí 15,5–21,0 pro g02 / g04)**: jen barevná úprava, nic nepřikreslovat. Úroveň černé posunout tak, aby studio mělo ~`#060606`,
  S-křivka (stíny dolů, střední tóny karoserie ±0, světla max. +8 %), ochlazení R × 0,97 / B × 1,03, vinětace 15 % v rozích. Záře jen
  ze skutečného rozdílu g02 − g01 / g04 − g03 v masce světel. Kontrola ve 270 px: světla nejjasnější v obraze, karoserie čitelná, nikde kreslený tvar.
- **Kurzor**: macOS šipka (černá, bílý okraj 1,5 px), přilétá už v pohybu (exponenciální ease-out), natočení ke směru letu, hover ×1,25, stisk −15 % na 3 snímky
  + kroužek akcentu `#1C69D4` (0,3 s), při tažení vozu ruka „grab“. Kurzor **jen způsobuje** změny (M5).

| čas (takt · doba) | obraz (který render, jaký pohyb) | text / UI | efekt | zvuk / událost |
|---|---|---|---|---|
| **0,0–2,0** (T1 · d1–4) úvod | **Snímek 0 = uprostřed tažení** (revize): scéna se studiem, v ní `vyp/uhel_060`, kurzor ve stavu „grab“ na karoserii už táhne doprava. **Krokování otočky `060→050→…→350→340` = 8 tvrdých kroků na mřížce 0,0625 s se setrvačností: 0,0625 · 0,125 · 0,1875 · 0,3125 · 0,4375 · 0,5625 · 0,75 · 1,0** (poslední = puštění). Žádné prolnutí ani rozmazání mezi úhly. Pod kroky scéna jemně driftuje 2,5D (+20 px doprava, ease-in-out 0,0–2,0) + makro dotlačení 1,00→1,03 (M6). Vůz ≥ 45 % výšky (výřez ≤ 1,3×). **Nepřetržitě**: drift, dotlačení, kurzor. | Lišta s „BMW 740d xDrive Sedan“ od snímku 0 (značka čitelná hned). **1,0–1,875 „THE NEW BMW 7 SERIES“** nahoře na stěně scény nad vozem (maska zdola jako celek 0,2 s + roztažení prostrkání), odchod 1,875–2,0. | Háček = vůz se pod rukou otáčí čelem k divákovi od 1. snímku (skutečné chování konfigurátoru). | klavír 0,0 · tiché „detent“ cvaknutí na každý krok (−12 LU, vrchol přesně na čase kroku) · lusknutí 0,5 · basa + měkký klik puštění 1,0 · lusknutí 1,5 |
| **2,0–4,0** (T2 · d1–4) úvod, náběh | `vyp/uhel_340` → **2,0 světla se probudí**: `zap/uhel_340` přes rozdíl (test 4: rostoucí kruh od středu masky 0,25–0,55 s + krátký nádech záře z rozmazaného rozdílu). Dotlačení 1,03→1,06. **2,5 kurzor se odlepí od vozu** a letí po oblouku k liště (natočení ke směru, zpomaluje do cíle). 3,0–4,0 nádech: scéna se zvedne 1,00→1,02 a stín pod ní se prohloubí. 3,5 hover nad „Design“, 3,875 stisk. **3,875–4,0 obraz drží dech** (pohyb jen dotlačení). **Nepřetržitě**: dotlačení, kurzor, zdvih scény. | Bez nadpisu. 3,5 ukazatel (tečka) se při hoveru natáhne o 8 px k „Design“ (předtucha). | Uvítací světla = první „živý“ moment, motivovaný: vůz se otočil k divákovi a pozdraví. | kopák od 2,0 · „shimmer“ světel vrchol 2,1 · lusknutí 2,5 · obrácený činel + vír 3,0–3,875 (dozní do 3,875) · tichý hover 3,5 · **3,875–4,0 automatika hudby −18 dB (náběh 20 ms) = ticho před dropem** |
| **4,0–6,0** (T3 · d1–4) **DROP 1** | **4,000 klik → přiznaný tvrdý střih `uhel_340 zap` → `g03` se světly** (přesně na snímku 4,000, nikdy o snímek vedle; srovnaný podle bboxu masky, ale jiná výška kamery a ohnisko: neviditelný match to není). `g03` = den + **max(0, g04 − g03) jen v masce světel** (denní svícení a obrys Iconic Glow zůstanou rozsvícené jako na 340, spojitost, viz past 16). Zároveň **scéna se rozšíří přes celý obraz** za 0,35 s (rohy 28→0, okraje se směrovým rozmazáním, kriticky tlumené, M2) **a kamera dotlačí celý kompozit jednotně 1,00→1,18** (4,0–4,35, kriticky tlumeně, bez paralaxy; g03 je v šířce 1920 0,75× nativní, 1,18× = 0,885× nativní). 4,35–6,0 od 1,18 pokračuje 2,5D drift (paralaxa z testu 5, posun ≤ ±60 px, další nájezd ≤ 5 %). 4,5 kurzor se odlepí od lišty a letí k vozu (oblouk). Vůz ~70 % šířky. **Nepřetržitě**: drift, kurzor. | Ukazatel přeskočí na „Design“ (náběžná hrana předběhne, dvě pružiny, M1). **5,0 tečka s pulzem** na obrysu ledvinek, 5,125–5,3 linka 1 px (+ jemný stín kvůli bílé kapotě) se vykreslí, **5,25 pilulka „BMW Iconic Glow“** vyskočí z konce linky (pružina 3 %) na volné stěně vpravo nahoře; odchod 5,875–6,0 (linka se stáhne do tečky). | Největší změna měřítka (karta → celý obraz) a zároveň nájezd na hrdinu. **5,75 glint** jen v pixelech obrysu Iconic Glow (L > 0,9, sytost < 0,08), max. +12 % `screen`, 0,4 s, smootherstep. Kontrola ve 100 % na 5,85: když na bílé kapotě splývá nebo je kreslený, glint vypustit a na 5,75 nechat jen druhý pulz tečky. | **úder + činel + kopák 4,0 = klik kurzoru** · měkký „air“ swoosh rozšíření (vrchol 4,1) · hi-hat · klik tečky 5,0 · UI pop 5,25 · sklo 5,75 (třpyt / pulz) |
| **6,0–8,0** (T4 · d1–4) exteriér | **6,0 match cut kolo → kolo**: tvrdý střih na **`g05`**, střed ráfku g05 přesně tam, kde bylo přední kolo g03 na 5,98 (kolo se skokem ~2× zvětší = punch-in na kopák). 6,0–6,5 kamera klouže doleva; 6,5 navazuje **`g06`** (napojit podle polohy kola, švih 0,12 s se směrovým rozmazáním). **7,0 švih doleva** (stejný směr kamery) → **`g10`** pravý bok, vůz ≥ 70 % šířky; 7,0–8,0 měkký odlesk softboxu přejede po dveřích (test 2b, smootherstep, 1,2 s). Ověřit 6,02 a 6,6: lišta (y 868–932) nesmí zakrýt pneumatiku, jinak lišta 5,875–7,0 pod okrajem (viz rozvržení). **Nepřetržitě**: kamera doleva, odlesk. | 6,0–7,0 bez textu. 7,0–7,4 kótovací linka (1 px `#262626`, koncové rysky) od zadního k přednímu nárazníku přesně podle bboxu `g10_*_vuz.png`, nad ní 7,15–7,6 rolující číslice **„5,395 mm“**; odchod 7,85–8,0 (linka se stáhne ke středu). | Jeden směr kamery přes 3 záběry (doleva), match cut kolo na kolo, odlesk po laku jen na boku (G7). | kopák + basa 6,0 = střih · tichý švih 6,5 · swoosh 7,0 · tiché tikání číslic 7,15–7,6 · sklo 6,75 / 7,75 |
| **8,0–10,0** (T5 · d1–4) záď | **8,0 tvrdý střih `g10` → `vyp/uhel_270`** (stejný profil, velikost a poloha srovnané podle masky). 8,0 kurzor chytí vůz a **švihne**: krokování `270→260→…→180` = 9 kroků, **rytmicky jinak než úvod**: 6 rychlých kroků 8,125 · 8,1875 · 8,25 · 8,3125 · 8,375 · 8,4375 (švih) a **poslední 3 na hi-hat 8,5 · 8,75 · 9,0** (dosednutí). **9,0 zadní světla naskočí červeně** (`zap/uhel_180` přes rozdíl, test 4). 9,0–10,0 dotlačení 1,00→1,05 (výřez ≤ 1,3×, vůz ≥ 45 % výšky). 9,5 kurzor se odlepí a letí k liště, 9,875 hover nad „Comfort“. **Nepřetržitě**: dotlačení, kurzor. | Bez nadpisu (revize: méně textu). | Druhé krokování otočky jako švih s dosednutím, rozsvícení zadních světel na úder. | klik chycení 8,0 · cvaknutí kroků (rychlé tišší, 8,5 / 8,75 / 9,0 hlasitější) · obrácený činel 9,0 → „shimmer“ zadních světel (vrchol 9,05) · sklo 9,75 |
| **10,0–12,0** (T6 · d1–4) **ZLOM: luxus a pohodlí** | **10,0 klik na „Comfort“ → modrý ukazatel sám vyroste v list** (M1, jeden tvar): pilulka ~120×40, rádius 20 → list 1824×1032 (x 48–1872, y 48–1080), rádius 28, barva `#1C69D4` → `#FFFFFF` během prvních 0,15 s, **dvě hrany na dvou pružinách** (horní hrana předběhne, list se krátce natáhne a srovná, kriticky tlumeně), celé 10,0–10,5. Lišta 10,0–10,15 zajede dolů. Exteriér pod listem ustoupí (0,96, ztmavne o 25 %; pod listem se `g03` vymění za čistý den bez světel). **10,15–10,4 uvnitř listu se otevře interiér** vlastní maskou (zaoblený obdélník ze středu, ne prolínačka). **Kostka interiéru** (`interier_predni_a` + `interier_bok1_a`, CSS 3D, FOV ~70°, zvětšení stěny ~1,17×): kamera **otáčí hlavou rotateY 0 → −35° v 10,25–12,0** (ease-in-out, otočení kolem jednoho bodu = fyzikálně správně). **11,0 tvrdý střih na dobu → `g14`** výřez 1,2× na středový tunel (volič, chromový lem), dotlačení 1,00→1,03; **11,5 tvrdý střih zpět do kostky**, která se mezitím otáčela dál (průběžný čas = vložený detail, kamera se neresetuje). Když test kostky selže: `g12` s 2,5D nájezdem 1,00→1,05 + posun 30 px, vložka g14 zůstává. **Nepřetržitě**: rotace kostky / dotlačení. | Bez textu (pohyb a prostor). | Kontrast měřítka: celý obraz → karta (M2). **11,0–11,4 glint** jen po chromovém lemu voliče v g14: pixely L > 0,9 a sytost < 0,08, max. +12 % `screen`, smootherstep. Glint po dřevě zrušen (dýha není lesklá). | klik 10,0 + cinel · hudba přejde na klavír · měkký swoosh listu (vrchol 10,25) · lusknutí 10,5 · třpyt 11,0 (= klavír 11,0) · kopák 11,25 · lusknutí 11,5 = střih |
| **12,0–14,0** (T7 · d1–4) luxus | **12,0 přechod přes hranu dveří**: **`g13`** (sedadla z boku, otevřené dveře) vjede zprava, náběžná hrana masky = svislá hrana dveřního sloupku v g13 (0,45 s, ease-out), kostka / g12 odjíždí doleva pomaleji (paralaxa). 12,0–13,0 dotlačení 1,00→1,05. **13,0 „screen studio“ přiblížení na prošívání sedadla** 1,05→1,15 (kriticky tlumeně 0,35 s, výřez ≤ 1,3× nativního). 13,25 kurzor přilétá k horní hraně listu, **13,5 chytí list** (list se pod prstem stiskne na 0,98) a **13,5–14,0 ho táhne dolů: list se smrští zpět do modré pilulky** (13,625–13,875 ease-in, šířka 1824 → 120, výška 1032 → 40, rádius 28 → 20, barva bílá → `#1C69D4` v posledních 0,1 s, dvě hrany na dvou pružinách), pilulka dosedne do lišty, která se 13,75–14,0 vrátí. Pod listem **`g03` den** (bez světel) přes celý obraz, srovná se zpět na 1,0 a plný jas. Kurzor celou dobu drží: **na 14,0 už drží ukazatel** (jedno souvislé gesto 13,5–15,75). **Nepřetržitě**: dotlačení, gesto kurzoru. | **12,5–13,375 „YOUR PRIVATE LOUNGE“** (vlevo nahoře na světlém stropu g13, `#262626`, kontrast ověřit ve 270 px, jinak bílý text se stínem 1 px), odchod 13,375–13,5. | Přechod přes objekt (hrana dveří) a zpětný morf listu do ukazatele = M1 viditelně na dvou místech. Prošívání sedadel = hlavní detail pohodlí. | swoosh dveří (vrchol 12,1) · kopák 12,0 · lusknutí 12,5 · klavír 13,0 = přiblížení · kopák 13,25 · klik úchopu 13,5 · měkký „whoosh“ smrštění (vrchol 13,85) |
| **14,0–16,0** (T8 · d1–4) **STOUPÁNÍ** | **`g03` den** přes celý obraz, dotlačení 1,00→1,08 (napětí, kamera jen dopředu). **14,0 kurzor táhne ukazatel doprava**: zadní hrana drží, náběžná hrana (= knob, bílý kruh 28 px s okrajem) jede a ukazatel se natáhne v dlouhou modrou výplň posuvníku (y 900, x 240→1680). **Za knobem se odkrývá `g04` noc** (svislá měkká hranice 80 px, D7, M3a), **14,0–15,5 odkryje g04 celé**: poloha hranice = poloha knobu přepočtená na šířku obrazu, průběh zvolit tak, aby **hranice přejela přední světla přesně v 15,25** (x světel změřit z masky). Knob zrychluje (ease-in) s řazením 14,5 / 15,0 (na řazení 3 snímky zaváhání). **15,25 světla g04 vzplanou** pod hranicí (nádech záře z rozdílu g04 − g03 jen v masce světel, 0,3 s). Od 15,5 noční grade (rozvržení). **15,5–15,75 knob drží napětí** (vibruje ±1 px na šestnáctiny, ne vůz), kamera se jen tlačí dopředu. **15,75–16,0 nádech: celý obraz kromě modré výplně a knobu zčerná** (ease-in 0,25 s, jako když se ve studiu zhasne; vůz, studio i lišta). **Nepřetržitě**: dotlačení, knob, hranice. | Bez textu (revize). Knob bez bubliny. | **Přímá manipulace den → noc** dokončená před nádechem (skutečné světlo z rendrů BMW). Hudba i obraz rostou, pak ticho a tma. | 14,0 startér + motor · řazení 14,5 / 15,0 · spiccato šestnáctiny · obrácený činel 15,0 + vír, **oba dozní do 15,75** · „shimmer“ světel 15,25 · **hlasitost roste** (C032) · **15,75–16,0 automatika hudby −18 dB (náběh 20 ms) = ticho a tma** |
| **16,0–18,0** (T9 · d1–4) **DROP 2: výkon** | **16,000 tvrdý střih na `g02` (noční grade), kde je na čistě černém vidět jen vrstva světel**: pixely g02 nad prahem jasu v masce světel + obrys Iconic Glow na 100 % + puls záře z rozmazaného rozdílu g02 − g01 (0,25 s, odeznívá). **16,0–16,35 z tmy vystoupí karoserie** (ease-out, náběh expozice celé vrstvy kromě světel 0 → 100 %; světla zůstávají na 100 %, nejde o prolínačku dvou obrazů). Vůz posunutý doleva (bbox x ≤ 1000). **Střih na každou dobu, každý záběr přijede v pohybu a na dobu dostane krátké dotlačení 1,00→1,04 (kriticky tlumeně)**: 16,0 `g02` celek → **16,5 `g02` výřez 1,25× na ledvinky a Iconic Glow** → **17,0 `g04` celek** (řazení, tah motoru) → **17,5 `g04` výřez 1,25× na přední světlo**. Výřez 1,25× + dotlačení 1,04 = 0,975× nativního (pod limitem). **Nepřetržitě**: dotlačení, knob, číslo. | **16,0–16,25 výplň se smrští a ukazatel dopadne na „Performance“** (dvě pružiny, M1 = úder; lišta se vrátí jako tmavé sklo). **16,25–16,5 lišta se promění v rychlostní posuvník** (obsah lišty odjede maskou, tělo lišty se zúží na dráhu 8 px, x 1064–1824, y 900, rysky po 50, ukazatel = knob s bublinou, M4). **Rychloměr běží souvisle přes všechny střihy** (číslo a knob = spojovací prvek, jeden svět): 16,25–17,0 knob rychle, **17,0 řazení**: knob na 3 snímky zpomalí, bublina se nakloní o 2° proti směru, 17,0–17,875 dojíždí (ease-out) a **17,875 knob na 250** (squash bubliny 3 %, dráha 1× modře blikne). Rysky se rozsvítí modře, když je knob mine. Mezihodnoty jen v pohybu (C8). | Nejsilnější moment videa: tma → světla → karoserie z tmy, pak střih na každou dobu a souvislé číslo. | **16,0 úder + činel + nízký náraz motoru synchronní se světly = nejhlasitější místo videa** (0 až −3 LU nad hudbou v okně 100 ms) · hi-hat · kopák na každou dobu = střih · sklo 16,25 · řazení 17,0 (+ klik bubliny) · tiché tikání rysek |
| **18,0–20,0** (T10 · d1–4) výkon: typografické údery | **18,0 tvrdý střih na `g04` celek** posunutý doleva (bbox x ≤ 1000, doplnění `#060606` vpravo, šev neviditelný), slabý odlesk po noční karoserii 18,0–18,75 (test 2b, smootherstep). **18,5 řazení: dotlačení 1,00→1,04** (kriticky tlumeně 0,25 s). **19,0 tvrdý střih na `g02` celek** posunutý doleva. **19,5 dotlačení 1,00→1,04**. **Nepřetržitě**: dotlačení, prostrkání čísel. | **17,875–18,0 číslo z bubliny vyroste do pravého sloupce** (log. měřítko, svislé rozmazání podle rychlosti) a **na 18,0 dopadne „250“** (Manrope 300, výška ~300–360 px, x 1064–1824, zarovnáno doprava nad koncem dráhy), „km/h“ 60 px `#BBBBBB`, popisek „Top speed“ 28 px. Knob a dráha zůstávají. Odchod 18,75–18,875 maskou nahoru (ease-in). **18,875–19,0 „5.7“ dorolují 0.0 → 5.7 a zamknou se na 19,0** + „s“, popisek „0–100 km/h“, stejné měřítko. Odchod 19,75–19,875. | Typografický úder na takt: obří čísla jako hlavní obraz, vůz vlevo, UI nikdy přes vůz. | **18,0 kopák + basa + sub náraz + měkký „lock“** · řazení 18,5 · **19,0 kopák + swap + tikání číslic 18,875–19,0** · hi-hat · sklo osminy |
| **20,0–22,0** (T11 · d1–4) výkon → **skládací logo** | **20,0 tvrdý střih na `g04` výřez 1,15×** posunutý doleva, dotlačení 1,00→1,04. **20,5–20,75 dráha i lišta se stáhnou do knobu.** **20,75–21,0 knob letí** (ease-in-out, oblouk) do horního bodu budoucího prstence (960, 290). **21,0–21,3 z knobu se rozlije světlé studio `#E7E2DC` kruhem přes všechny 4 rohy** (zaplavení M3b, ≥ 0,3 s, bez textu), noc zmizí pod ním. | **19,875–20,0 „230“ dorolují a zamknou se na 20,0** + „kW“, popisek „Power“; odchod 20,625–20,75 (před letem knobu). **Logo (M7, 3 kroky, vrstvy `znacka/logo/vrstvy/`, stejný viewBox, cesty beze změny), logo ~360 px, střed (960, 470):** ① **21,25–21,6 knob oběhne po směru hodin vnější prstenec** (01, `#6F6F6F`) a odkrývá ho za sebou (kuželová maska), na 21,6 se knob rozplyne do prstence (0,06 s); ② **21,6–21,85 vnitřní kruh + modré čtvrtiny** (02–04, `#0066B1`) se dotočí kolem středu o 90° do svých poloh, kriticky tlumeně, bez překmitu; ③ **B 21,875 · M 21,9375 · W 22,0** (posun 10 px dostředivě + krytí 0,12 s, bez škálování). **Snímek 22,000 = pixelově `00_slozene_original.svg`** (dotlačení end card začíná od 1,00 přesně na 22,0). Žádná pružina, která by po 22,0 dosedala. | Kruh knobu → prstenec loga (rým celého konceptu). Každý krok sám, čitelně za sebou. Čisté, bez záře, odlesku a částic. | kopák 20,0 · malý buben 20,5 · whoosh knobu (vrchol 20,95) · obrácený činel 21,0 + měkký swoosh zaplavení (vrchol 21,15) · tichý „ink“ tón tahu prstence 21,25–21,6 · měkký dopad čtvrtin 21,85 · vír 21,5–22,0 · jemné kliky písmen 21,875 / 21,9375 |
| **22,0–24,0** (T12 · d1–4) **END CARD** | Světlé studio `#E7E2DC` (velmi jemná vinětace), hotové **originální logo** (`00_slozene_original.svg`, nedeformované). Souvislé dotlačení 1,00→1,03 od 22,0 do 25,0 (kriticky tlumené, nikdy nestojí). | 22,5 pod logem „THE NEW 7 SERIES“ (Manrope 700, 44 px, `#262626`, maska zdola jako celek, y ≈ 720). 23,0 pod ním **modrá pilulka naposledy** (M1): roztáhne se z bodu do tlačítka „Configure yours“ (Manrope 500, 24 px, bílá, pružina 3 %, y ≈ 810). 22,5 dole disclaimer „Concept ad · not affiliated with BMW“ (Manrope 500, 18 px, `#8E8E8E`, **y ≤ 940**, revize kvůli A5). End card je jedna navržená kompozice, prvky přicházejí po sobě. | Klid po výkonu, ale v pohybu (C6). | **22,0 úder + činel + klavírní akord = nejsilnější dopad loga** (W) · tichý pop pilulky 23,0 |
| **24,0–25,0** (T13 · d1–2, půltakt) | Dotlačení pokračuje do 25,0. | 24,0 kurzor přilétá zdola zprava (v pohybu), **24,5 klikne na „Configure yours“** (stisk −15 %, kroužek akcentu, pilulka krátce `#0653B6` a zpět). Poslední snímek = hotová end card s kurzorem u tlačítka, nic nepřekrývá logo ani texty. | Poslední „akce“ diváka: konfigurátor zve ke konfiguraci. | klik 24,5 · doznění akordu do 25,0 |

### Motiony ve videu (kde přesně, pro kritika, kritérium 7)
| motion | kde (časy) | jak je ho poznat |
|---|---|---|
| **M1** Shape morphing (`twoclipping-5cba86`) | 3,5 · **4,0** · **10,0–10,5** · **13,5–14,0** · **14,0–15,75** · **16,0–16,5** · 20,5–21,6 · 23,0 | jeden modrý ukazatel: tečka → ukazatel kapitol (dvě pružiny) → **vyroste v bílý list interiéru** → **list se smrští zpět do ukazatele** → výplň posuvníku noci → ukazatel „Performance“ → rychlostní posuvník s knobem → knob oběhne prstenec loga → tlačítko CTA |
| **M2** Spotify product film (`brainextends-e19ac3`) | 0,0–4,0 scéna · **4,0** scéna → full-bleed + nájezd 1,18 · 10,0 list = zase karta · lišta 0,0–10,0 a 13,75–20,75 · 20,75–21,0 sbíhání do středu loga | hrdinský obraz drží polohu přes předání (4,0 podle bboxu, 6,0 kolo → kolo, 8,0 profil → profil), lišta konfigurátoru jako spojka |
| **M3** Photo print app (`twoclipping-221cab`) | **14,0–15,5** (a) přesvícení posuvníkem den → noc, světla vzplanou 15,25 · **21,0–21,3** (b) zaplavení kruhem přes 4 rohy | noc se odkrývá pod knobem, světla vzplanou pod hranicí; světlé studio se rozlije z knobu |
| **M4** White ball UI loop (`rossaxbt-94583b`) | **16,25–20,75** | posuvník 0 → 250 s bublinou nad knobem souvisle přes střihy, rysky se rozsvěcují, číslo z bubliny vyroste v obří „250“, pak „5.7 s“ a „230 kW“ na takty |
| **M5** Frame by Frame (`notdwd-7de38a`) | kurzor 0,0 (grab) · 2,5 · 3,5–4,0 · 4,5–5,0 · 8,0 · 9,5–10,0 · 13,25–15,75 · 24,5; záběry přijíždějí v pohybu (6,5 · 7,0 · 16,0–18,0) | kurzor jako postava (tažení, let po oblouku, hover, stisk, jedno gesto 13,5–15,75), pilulka vyskočí z bodu, který kurzor označil |
| **M6** Taxtello (`daniel-haida-8691d4`) | dotlačení kamery celé video · **glint 5,75** (Iconic Glow, podmíněně) · **glint 11,0** (chrom voliče g14) · zdrženlivost 10,0–14,0 | makro produktová kamera, překmit < 2 %, jeden drahý světelný akcent na sekci |
| **M7** TypingMind logo reveal (`tdinh-me-815acb`) | **21,25–22,0** | logo se nejdřív poskládá (prstenec → čtvrtiny → písmena), poslední díl na 22,0, pak klid a dotlačení |

### Kontrolní snímky (před plným renderem, z výřezu s podsnímky, C028) a kritéria odmítnutí
Každý snímek ve 100 % a ve zmenšenině 270 px (A8). Odmítnout, když platí kterékoli kritérium.
| čas | co musí být vidět | odmítnout, když |
|---|---|---|
| 0,000 / 0,07 | hotový obraz uprostřed tažení: scéna, vůz `uhel_060` → 0,07 už `050`, kurzor „grab“ na karoserii, lišta | prázdné místo, zatmívání, vůz < 45 % výšky, kurzor jen pluje, scéna bez driftu (porovnat 0,00 a 0,50) |
| 1,50 / 1,52 | poslední krok otočky na 340, kurzor „grab“ | dvojitá kola / prolnutí dvou úhlů, rozmazání vozu |
| 1,10 / 2,30 | nadpis „THE NEW BMW 7 SERIES“ nad vozem; světla probuzená (LED v přední masce, obrys ledvinek) | nadpis přes vůz, záře mimo světla, kreslený tvar světla, šedivý mezistav |
| 3,95 / 4,000 / 4,02 / 4,35 | před klikem scéna; **střih přesně na snímku 4,000** na `g03` se světly (denní svícení svítí jako na 340); 4,35 scéna přes celý obraz a vůz o 18 % větší než na 3,98 | střih o snímek vedle, světla na g03 zhasnutá nebo kreslená, skok polohy vozu na 4,000 > ~10 px proti bboxu, probliknutí, ukazatel teleportuje, vůz na 4,35 stejně velký jako na 3,98 |
| 5,40 / 5,85 | linka + pilulka „BMW Iconic Glow“ u ledvinek; glint ve 100 % | pilulka přes vůz, linka nečitelná na bílé kapotě, dva texty naráz, glint mimo obrys Iconic Glow nebo kreslený přejezd (pak glint vypustit) |
| 5,98 / 6,02 | match cut kolo → kolo | střed kola se mezi snímky posune > 20 px |
| 6,02 / 6,60 | lišta proti pneumatice g05 / g06 | lišta zakrývá pneumatiku (pak lišta 5,875–7,0 pod okrajem) |
| 7,60 | kóta od nárazníku k nárazníku + „5,395 mm“ | konce kóty mimo nárazníky o > 6 px, jiné číslo než z bmw.cz |
| 8,30 / 8,75 | druhé krokování: rychlý švih, pak dosednutí na 8,5 / 8,75 / 9,0 | stejný rytmus jako úvod, prolnutí úhlů |
| 9,10 | zadní světla svítí červeně, nadpis | světla mimo svítilny, rozdíl zap/vyp na karoserii |
| 10,07 / 10,25 / 11,02 / 11,52 | ukazatel roste v list (ještě modrý → bílý); list v půli cesty, interiér se otevírá; střih na g14 (tunel, glint); zpět v kostce dál otočené | list nevychází z ukazatele (vyjíždí odjinud), prolínačka celého obrazu, natažené okraje stěn kostky, viditelný šev hran kostky, glint na dřevě |
| 12,20 / 13,20 / 13,80 | hrana dveří g13 vede přechod; přiblížení na prošívání; list se smršťuje do pilulky pod kurzorem | rovný stírací pruh bez vztahu k obrazu, prošívání měkké (výřez > 1,3×), list mizí jinam než do ukazatele |
| 15,00 / 15,27 / 15,50 | hranice den/noc pod knobem; světla vzplanula pod hranicí; celý obraz noc (noční grade) | hranice tvrdá nebo šikmá, šedivé prolnutí celého obrazu, záře mimo světla, světla vzplanou jinde než pod hranicí |
| 15,90 / 15,98 / 16,02 / 16,20 / 16,40 | tma kromě výplně a knobu; na 16,02 jen světla na černé + ukazatel dopadá na „Performance“; karoserie z tmy; 16,40 hotová | na 15,98 je vidět vůz nebo studio, na 16,02 je vidět karoserie, světla během náběhu slábnou (= prolínačka), vůz za x 1000 nebo < 45 % výšky, UI přes vůz. **Měřit**: max. jas v masce světel 16,02 ≥ 235 při průměru obrazu 15,98 ≤ 12; YDIF 15,98 → 16,40 musí být výrazně vyšší než YDIF 3,98 → 4,35 |
| 16,52 / 17,02 / 17,52 | střih na každou dobu (g02 výřez, g04 celek, g04 výřez), číslo v bublině souvislé přes střihy | stojící záběr bez dotlačení, číslo skočí / vynuluje se na střihu, výřez měkký, vůz pod bublinou |
| 18,02 | obří „250“ v pravém sloupci (výška ~300–360 px), „km/h“, vůz vlevo; ve 270 px čitelné | jiná hodnota, rozmazané číslo po dopadu, číslo přes vůz, šev doplněného černého pozadí |
| 19,50 / 20,50 | „0–100 km/h“ „5.7 s“ · „Power“ „230 kW“ | koně / „hp“, „elektronicky omezeno“, dva texty naráz |
| 20,80 / 21,15 / 21,40 | knob letí k hornímu bodu prstence, bez textu; zaplavení přes všechny 4 rohy; knob v půli oběhu prstence | text během letu nebo zaplavení, kraj zaplavení nepřekryje roh, probliknutí, prstenec jiné tloušťky než originál |
| 21,70 | čtvrtiny se dotáčejí kolem středu | čtvrtina deformovaná, změna měřítka v jedné ose, překmit |
| 22,00 / 22,02 | **logo hotové na úder** | logo ≠ originál (překrýt `00_slozene_original.svg`, rozdíl > antialiasing), záře, odlesk |
| 24,98 | end card + CTA + disclaimer, kurzor u tlačítka | zamrzlý obraz (porovnat s 23,98: dotlačení), text mimo bezpečnou zónu, kurzor přes text |

### Pasti stavby (realismus a AI znaky)
1. **Vůz se nikdy nedeformuje ani nepřekresluje**: jen posun, měřítko (≤ 1,3× nativního rozlišení), maska, odkrytí, střih. Žádné natažení, warp, chromatický posun,
   glitch, duhy, plastový lesk na voze (G7). Záře jen ze **skutečného rozdílu** zap − vyp / noc − den, nikdy kreslená.
2. **Otočka 360° jen tvrdými kroky** (0,0–1,0 a 8,0–9,0, časy kroků v tabulce, mřížka 0,0625 s), nikdy prolnutí sousedních úhlů (dvojitá kola, test 5b) ani rozmazání mezi nimi. Komprese snímků otočky
   je silnější: do 1,3× v pořádku, větší výřez ne. Na 2,0 a 9,0 dvojice `vyp`/`zap` musí být přesně zarovnané (posun 0 px).
   **Podsnímky (revize)**: výběr úhlu otočky i každý tvrdý střih se počítá z času **snímku** (zaokrouhleno na snímek 1/60), ne z času podsnímku,
   jinak závěrka 180° slije dva úhly / dva rendry do jednoho snímku (dvojitá kola). Kroky na mřížce 0,0625 s padnou mezi snímky: krok platí od nejbližšího
   následujícího snímku (0,0625 → snímek 4 = 0,0667). Kontrola: 0,05 / 0,07 / 0,98 / 1,02 a 8,12 / 8,14 bez dvojitého obrysu.
3. **Match-position (4,0, 6,0, 8,0)** měřit z bboxu masek / středu ráfku, ne od oka. Skok polohy vozu mezi snímky > ~10 px působí jako chyba, ne jako střih.
   **4,0 je přiznaný střih** (340 a g03 mají jinou výšku kamery a ohnisko): přesně na snímku 4,000, s klikem a kopákem, nikdy o snímek vedle.
4. **Studio jiné barvy mezi rendry** (galerie vs. otočka mají nepatrně jiný odstín stěny): na 4,0 a 8,0 porovnat průměrnou barvu stěny, když se liší > 3/255,
   srovnat jen pozadí (vrstva `*_pozadi.png`), nikdy lak vozu.
5. **Kamera 2,5D** jen s geometrií z testu 5: nájezd ≤ 10 %, boční posun ≤ ±60 px; jinak tmavá ploška za nárazníkem. Výjimka: nájezd 1,00→1,18 na dropu 1
   je **jednotné měřítko celého kompozitu bez paralaxy** (žádná ploška nevznikne), paralaxa se zapíná až od 4,35. Nikdy dva pohyby kamery naráz, nikdy zoom tam a zpět.
6. **Den → noc (14–16)**: měkká **svislá** hranice vázaná na knob, nikdy prolnutí celého obrazu (šedivý mezistav sRGB, test 4). Bílá karoserie v noci je šedá: **nezesvětlovat** plošně; noční grade (rozvržení) smí jen S-křivku (střední tóny ±0, světla max. +8 %), studio na ~`#060606`.
7. **Odlesk po laku** jen na boku `g10` (7,0) a slabě na `g04` (18,0), jednou za záběr, smootherstep. Na 3/4 bílém laku ne, tmavá „vlajka“ zakázaná (test 2).
8. **Kolo** se v tomto konceptu netočí (pomalé valení prozradí točící se třmen, na stojícím voze působí falešně). Výkon nesou světla, noc, střihy a číslo.
9. **UI nikdy přes vůz** a nevrhá na render stín; pilulky, nadpisy a čísla jen na volné stěně studia. Sklo max. 1–2 prvky (bublina, noční lišta), nikdy přes vůz,
   jako rozmazaný klon scény (ne `backdrop-filter: url()`), `will-change` ne na škálovaných prvcích.
10. **Text**: jen jeden text v jednom okamžiku, odcházející zmizí dřív, než přijde nový. Text se pořád hýbe (prostrkání, maska), nikdy nestojí. Bez teček (E8),
    anglicky, čísla přesně: `250 km/h`, `0–100 km/h` + `5.7 s` (pomlčka –), `230 kW`, žádné koně ani „electronically limited“ (C8).
11. **Kontrast**: bílá linka / tmavý text nad bílou kapotou a světlou stěnou ověřit ve 270 px; linka dostane stín 1 px. V noci text bílý.
12. **Zaplavení 21,0–21,3** z knobu (960, 290) přes všechny 4 rohy (poloměr ≥ 1300 px) a ≥ 0,3 s, jinak probliknutí. Během letu knobu a zaplavení žádný text.
13. **Logo**: jen vrstvy `vrstvy/01–09` (stejný viewBox, cesty beze změny), rotace jen kolem středu loga (170,08 / 170,08), žádné škálování v jedné ose, žádná záře,
    odlesk ani barevné střepy. Barvy jen `#0066B1` + `#6F6F6F`. Na 22,0 musí složené vrstvy = originál.
14. **AI znaky obecně**: žádné částice, tečkové mřížky, gradienty na UI, třes kamery, text v rozích, každé slovo zvlášť, skákavé pružiny (UI ≤ 3 %, kamera a plochy bez překmitu),
    `Math.random` bez semínka, „cokoli, co vypadá jako šablona“.
15. **Energie (C7, V001)**: v každém taktu se něco hýbe nepřetržitě (kamera, kurzor, knob, prostrkání) a na každou dobu je událost (tabulka výše). Při kontrole
    hledat úseky > 0,5 s bez nové události a > 1 s bez změny obrazu.
16. **Světla na g03 při dropu 1 (revize)**: na 340 svítí denní světla (od 2,0), g03 je den se zhasnutými světly. Na 4,0–6,0 proto
    `g03` + max(0, g04 − g03) **jen v masce světel** (vlastní maska světlometů a obrysu Iconic Glow, okraj 2 px). Mimo masku žádný rozdíl.
    Test před stavbou: 4,02 vedle `zap/uhel_340` ve 100 %; když rozdíl tvoří šedý lem nebo noční odlesk mimo LED, světla už na 3,5–3,875 zhasnou
    s nádechem (rozdíl zap − vyp ubývá) a g03 je čistý den. Od 10,15 (pod listem) je g03 vždy čistý den bez světel, aby mohla světla vzplanout na 15,25.
17. **Kostka interiéru (10,25–12,0)**: CSS 3D krychle, kamera ve středu, otáčí se jen rotateY (jeden bod), FOV ~70°, stěny 2000 px se zvětší ~1,17×.
    Zakázané: posun kamery uvnitř kostky (natažené okraje), viditelný šev nebo rozdíl jasu na hraně stěn, rotace jiná než kolem svislé osy.
    Nejdřív krátký test (10 s výřez není potřeba, stačí 3 snímky 10,3 / 11,2 / 11,9 ve 100 %), při neúspěchu `g12` s 2,5D nájezdem.
18. **Výkon 16–21: posun vozu doleva** jen u nočních rendrů po gradu (studio ~`#060606`), doplnění stejnou barvou s přechodem 200 px. Kontrola
    ve 100 % na 18,02 / 19,02 / 20,02: šev, rozdíl podlahy nebo vinětace nesmí být vidět. Když je vidět, místo posunu výřez (měřítko ≤ 1,3× nativního).
19. **Ticho a tma 15,75–16,0**: obraz zčerná ease-in (ne skokem), zůstane jen modrá výplň a knob, hudba −18 dB. Na 16,000 nesmí být vidět karoserie,
    jen světla (jinak drop 2 vypadá jako prolínačka). Světla během 16,0–16,35 nikdy neslábnou.

### Pořadí stavby
1. **Kostra a tokeny**: rozvržení (lišta, scéna, typografie, kurzor) z `nastroje/vzory/scena.html`, načtení rendrů a masek, kamera 2,5D z testu 5.
0. **Krátké testy (revize)**: g03 se světly z rozdílu (past 16), kostka interiéru (past 17), noční grade g02 / g04 + doplnění černé (rozvržení, past 18),
   každý jako 2–3 snímky ve 100 % a 270 px. Výsledek zapsat do zadání.
2. **Klíčové snímky drop 1** (3,95 · 4,000 · 4,02 · 4,35 · 4,50) a **drop 2** (15,50 · 15,90 · 15,98 · 16,02 · 16,20 · 16,40 · 17,02 · 18,02) jako statické snímky z výřezu s podsnímky
   → schválení režisérem / kreativním ředitelem **před** stavbou zbytku (porovnat sílu dropů: drop 2 musí být silnější).
3. **Gesto 13,5–16,5** (smrštění listu → posuvník noci → tma → světla z tmy) jako krátký výřez videa (`--od 13.5`, 3 s) a změřit YDIF / jas podle tabulky.
4. **Logo a end card 20,75–25,0** (M7 podle vrstev, kontrola překrytím s originálem na 22,0).
5. **Úvod 0–4** (krokování otočky, probuzení světel, háček) → **exteriér 4–10** → **interiér 10–14** → **výkon 16–21**.
6. Změřit 1 s výřezu (odhad 12–17 s výpočtu na 1 s videa), pak `--nahled doby --bpm 120` (snímek na každou dobu) a teprve potom plný render
   s `--sub 4`, rychlé úseky `--sub-rychle 8 --rychle 0-1.05,3.9-4.4,5.9-6.1,6.4-6.6,6.9-7.1,8.1-8.45,15.9-17.6,17.85-18.05,20.7-21.7`.
7. Kritik dostane zadání a video, ne toto zdůvodnění (kontrola podle tabulky kontrolních snímků výše).

### Výroba kroky 0–2 (animátor 2026-11-01): testy, kostra, klíčové snímky dropů
Scéna `media/projekty/003-bmw-rada7/scena/` (`index.html` + `jadro.js`, `foto.js`, `ui.js`, `kostka.js`, `hlavni.js`, `styl.css`),
podklady z rendrů `scena/skripty/priprava.py` → `scena/podklady/`, klíčové snímky s podsnímky `scena/skripty/klicove.sh` → `scena/kontrolni/` (100 % + 480 px).
- **Test 0a, světla g03 (past 16): funguje, jen denní svícení.** Maska z rozdílu g04 − g03 omezená na horní LED pásy. Spodní světlomety vynechány:
  na `zap/uhel_340` nesvítí a noční záře kolem nich by ve dne působila jako šmouha. Obrys ledvinek je v g03 už ve dne jasnější než v noci
  (241 vs 227), takže rozsvícený vzhled drží bez úprav. 4,017 vedle 3,95 ve 100 %: DRL i obrys svítí stejně, bez šedého lemu.
- **Test 0b, kostka interiéru (past 17): funguje, ale ve WebGL, ne v CSS 3D.** Chromium v CSS 3D nekreslí stěny, které protínají rovinu kamery
  (černé klíny), a softwarové GL rozmaže velké ořezané trojúhelníky (stěny proto jako mřížka 24×24). Obrázky z file:// WebGL nepřijme
  (cizí původ) → stěny jako data URL v `podklady/kostka_tex.js`. Orientace ověřená na švech: **bok1 = vlevo** (strana řidiče), bok2 = vpravo.
  Ohnisko 1170 px = stěna 1,17×, vodorovné FOV ~79°. Snímky 10,3 / 11,2 / 11,9 (yaw 0 → −35° doleva) bez švu, okraj u kraje obrazu mírně měkčí
  (přirozený širokoúhlý vzhled). Doporučení: pitch −6° (víc palubní desky, méně čelního skla), rozhodne se v bloku interiéru.
- **Test 0c, noční grade + doplnění černé (past 18): funguje.** Studio g02/g04 je jednolité #161616 → po gradu #060606 (medián 6,0), karoserie
  ±0 (g04 82 → 82, g02 63 → 60). Doplnění stejnou barvou je bezešvé (sloupce u hrany rendru 5,0/255 všude, zesílení ×12 bez švu);
  vinětace se kreslí přes celý snímek, ne přes rendr. Maska světel v noci = jasné pixely vozu (> 140): LED pásy, světlomety **i obrys Iconic Glow** (SPZ pod prahem).
- **Nalezeno a opraveno**: vrstvy 2,5D g03 (maska + pozadí) dávaly u pneumatik světlý lem (doplněné pozadí pod vozem je světlé, odchylka až 156/255).
  Vrstva vozu teď nese pixely rendru s alfou u podlahy rozšířenou o 16 px (kontaktní stín jede s vozem): p99,9 odchylky 43 → 4,8/255.
  Bez paralaxy se kreslí celý rendr (přesně originál).
- **Rozhodnutí v kostře**: zmenšení otočky S0 = 0,73 (uhel_060 na 0,0 = 76 % šířky, A8 přes šířku; 45 % výšky by znamenalo vůz 1517 px v scéně 1536 px,
  na krajích bez vzduchu) · střih 4,000 srovnaný podle středu a spodku bboxu a **stejné výšky** vozu (340 vs g03 mají jiný poměr stran: šířka +9 %),
  g03 vlevo doplněný o 140 px studia (jen první snímky rozšíření scény) · nájezd 4,0–4,35 kolem bodu tak, aby vůz skončil na (820, 850), 0,937× nativního ·
  karoserie na dropu 2 vystupuje až od 16,035 (kubický ease-out; exponenciální by na 16,02 ukázal 28 % karoserie) · g02 na dropu 2 větší (0,98×, 65 % výšky,
  bbox x 59–997, dotlačení kolem pravé hrany vozu) · velké číslo: jednotka „km/h“ pod číslem vpravo (vedle čísla by blok přesáhl sloupec a sahal na vůz) ·
  písmena loga dosedají 1/240 s před dobou, takže snímek 22,000 = originál bit po bitu (ověřeno na podsnímcích).
- **Síla dropů** (snímky z MP4, `kontrolni/100`): drop 1 3,95 → 4,35 YDIF 38,7, změna expozice 1,06 EV · drop 2 15,983 → 16,40 YDIF 18,2, **2,0 EV**,
  jas 0,9 → 18,0, kontrast (std) 8 → 33 · 15,983 průměr 0,9 (≤ 12 ✓) · 16,017 max 255, 5 905 px > 235 (✓), karoserie 0 %.
  YDIF (průměrný absolutní rozdíl jasu) u odhalení z tmy do noční scény nemůže přerůst změnu na světlé scéně: drop 2 je silnější v expozici a kontrastu, ne v YDIF (otázka pro režiséra).
- **Oprava klíčových snímků po řediteli (7,8, animátor 2026-11-01)**, výstup `scena/kontrolni_v2/` (100 %, 480 px, `vyrezy_100.jpg`, `mrizka/`):
  (1) noční grade v2 `scena/skripty/noc_grade.py` (priprava.py už `_noc.png` nepíše): karoserie −0,4 EV (EV v hodnotách obrazu, jak měří kritik), g04 příď ±0 → záď −1,2 EV,
  g02 radiálně od ledvinek −0,8 EV, spodních 20 % −1 EV, jasné odlesky ztlumené méně; studio nad linií podlahy #060606 + halo světlometů z rendru, pod ní podlaha
  z rendru (22/255) v elipse světla před přídí, k okraji plynule do #060606 (okraj rendru přesně #060606), kontaktní stín z masky stínu. Naměřeno: kapota 64,
  g04c příď 68 / záď 33, podlaha 100 px před nárazníkem 21,3 (16,40 i 17,02), mezi pneumatikami 1,0. Odlesk 18,0–18,75 = pás +15 % screen v masce laku
  `g04_lak.png` (bílý lak z denního g03, váha na ramenní linii a kapotu, SPZ a ráfky mimo), ostré jádro ~110 px, smootherstep zezadu dopředu (ověřeno rozdílem: +32/255).
  (2) tma 15,75–15,85 exponenciální ease-out, kurzor pryč do 15,85; průměr 15,85 / 15,90 / 15,983 = 0,6. (3) 16,0–16,5 `NOC.g02s` souměrně: střed ledvinek x 960,
  vůz y ~80–804 (67 % výšky), dotlačení kolem středu vozu; bublina (od y 810) vozu nekoliduje. (4) 17,0 `NOC.g04c` = celek ×1,38 (0,883× nativního), příď x ≤ 987,
  záď ~300 px mimo obraz (při ×1,38 a přídi ≤ 1000 to jinak nejde), pneumatiky y ~840; 18,0 zůstává menší záběr pod „250“. (5) drop 1: exponenciální ease-out k = 7
  s předsunutím o půl snímku (start 3,9917), 4,05 = 55 %, 4,15 = 89 %, dosed 4,35 bez překmitu; okraje scény na spojitém čase (rozmaže je závěrka), vůz 4,0–4,15
  na čase snímku (ostrý). (6) bublina plné krytí, celá do 16,33 (usazení, bez překmitu); hodnota i poloha bubliny na čase snímku (žádné duchy z podsnímků,
  číslice ostré na každém snímku, na dobách zaokrouhlené); knob stojí od 16,25 na x 1064 a dráha se dotvoří kolem něj; knob okraj 1 px + neutrální stín.
  (7) ukazatel na „Performance“ dosedne do 16,13 (obě hrany i výška), na 16,2 bez zdvojeného obrysu. (8) end card: vinětace předem ve float + jasový dither
  rozmazaný ~1 px (sd 0,5/255, semínko), bílý šum ±0,5 x264 crf 16 smaže (reziduum schodů 0,73 → 0,57), rozmazaný 0,69 → 0,31.

### Výroba B1: pohyb 13,5–21,0 (animátor 2026-11-01)
Kontrolní snímky s podsnímky `scena/kontrolni_b1/` (100 %, 480 px, `arch_480.jpg`), pásy sousedních snímků `kontrolni_b1/pasy/` (15,9–16,5 · 20,9–21,4 · 13,6–14,05 · 17,4–17,6).
Časy nové části jsou v `CASY` (`jadro.js`): `uchop`, `smrstList`, `listModra`, `listaNavrat`, `rysky`, `karty`, `stazeni`, `letKnobu`, `knobCil`, `zaplaveni`.
- **13,5–14,0 list → ukazatel (M1)**: kurzor přilétá 13,25 zprava zdola po oblouku (hover ×1,2), 13,5 úchop (stisk −15 % na 3 snímky + kroužek akcentu), list 0,98 a povolí 34 px dolů,
  13,625–13,875 smrštění: horní hrana (táhne ji kurzor) ease-in a dojede dřív, boky a spodek pomaleji; interiér se 13,74–13,83 zavře do středu listu vlastní maskou,
  bílá → `#1C69D4` až 13,835–13,875 (dřív by se barvila velká plocha), **13,875 dopad** do „Comfort“ (squash pilulky ±6 %, tlumený), lišta se vrací zdola 13,75–14,0, pod listem `g03` 0,96 → 1,0 a ztmavení 25 % → 0.
  Obsah listu = `g13` s přiblížením na prošívání (`kresliObsahListu` ve `foto.js`), **blok interiéru ho smí nahradit**; tvar listu je `listB1` (`ui.js`).
- **14,0–16,0 opraveno**: hranice den/noc se dřív počítala od začátku dráhy, ale knob startuje na „Comfort“, takže **na 14,0 byla noc skokem přes levých ~1 290 px**. Teď je hranice
  vázaná na postup knobu od startu (`UI_STAV.postupNoc`): 14,0 mimo obraz vlevo, pravý světlomet přejede 15,25 (exponent 1,25), celé g04 15,5. Obsah lišty při proměně v dráhu
  stojí na obrazovce a jen se odmaskuje (dřív jel s levým okrajem lišty → vodorovná šmouha textu na 16,267).
- **16,25–16,5 (připomínka 16,333 vyřešena)**: levý konec lišty dojede ke knobu do 16,33, výška do 16,36, pravý konec se vytáhne pružinou do 16,5; pilulka „Performance“ se stáhne doleva do knobu do 16,34.
  Na 16,333 už není nic vlevo od knobu ani modrá napravo.
- **Rychloměr podle zvuku**: 0 v 16,3, **rysky 50 / 100 / 150 / 200 / 250 přesně v 16,5 · 16,75 · 17,0 · 17,1875 · 17,875** (Hermite + řazení 17,0–17,05 + ease-out s exponentem 3,72). Dráha 17,875 jednou modře blikne.
- **17,5 výřez** na přední světlo: `NOC.g04v` byl 0,80× (menší než celek 17,0 0,883×, takže skok na místě), teď 1,12× nativního = 1,27× celku, příď x ≤ 994.
- **Velká čísla = 3 karty** (`TEXTY.karty`, vzor počítadla s desetinnou tečkou): 250 vyroste přímo z číslic bubliny (číslice bubliny se od 17,875 skryjí, dřív se překrývaly „25250“), dopad 18,0;
  5.7 a 230 přijedou zdola v masce a dorolují z nuly (hodnota na čase snímku), zámek 19,0 / 20,0; během držení roste prostrkání; odchody maskou nahoru 18,75 / 19,75 / 20,625.
  Vedoucí číslice 5.7 se mění na snímcích 18,883 · 18,9 · 18,917 · 18,95 (zvuk 18,875 · 18,9 · 18,928 · 18,96 = v toleranci 1 snímku).
- **20,5–21,0**: dráha, výplň a rysky se stáhnou do knobu (ease-in, knob se „nabije“ na 1,15), 20,75–21,0 knob letí po oblouku (smootherstep, nejrychlejší 20,875) do (960, 290), lišta skrytá od 20,75.
  Záběr 20,0 se tlačí až do 21,3 (dřív stál 20,5–21,0). **Zaplavení 21,0–21,3** v minimální verzi (kruh studia z knobu, poloměr do 1 320 px, všechny 4 rohy kryté v 21,25), aby šlo zkontrolovat předání; blok loga ho smí doladit. Knob zůstává v (960, 290) do 21,25.
- **Měření**: 15,983 průměr 0,6 (≤ 12 ✓) · 16,017 max 255, 7 778 px > 235 ✓ · 16,40 průměr 15,5, std 24,2 · YDIF 15,983 → 16,40 = 15,8. Výkon (C027): 1 s výřezu 18–19 `--sub 4` = 16 s, 16,5–17,5 `--sub 8` = 21 s (včetně startu prohlížečů).
- **Pro zvukaře (posunuté nebo nové časy)**: dopad pilulky do lišty 13,875 (nové), knob narazí na konec dráhy noci 15,5 (= kopák), stažení dráhy 20,5–20,75, švih knobu nejrychlejší 20,875 (ve zvuku 20,95), ukazatel dosedá na „Performance“ už 16,13 (ve zvuku 16,25).

### Výroba B2: logo a end card 20,75–25,0 + úvod 0,0–4,0 (animátor 2026-11-01)
Kontrolní snímky s podsnímky `scena/kontrolni_b2/` (38 časů, 100 % + 480 px, `arch_480.jpg`), pásy `kontrolni_b2/pasy/` (3,9–4,4 a 21,8–22,2 celé,
3,97–4,02 a 21,97–22,02 ve 100 %). Nové časy v `CASY`: `nadpis`, `zareUvod`, `prstenec`, `knobSplyne`, `ctvrtiny`, `pismena`, `endNadpis`, `cta`, `disclaimerOd`, `kurzorEnd`, `klikEnd`.
- **Úvod**: kurzor „grab“ = sevřená ruka (macOS closedhand, 4 klouby, palec přitisknutý). Nadpis ① „THE NEW BMW 7 SERIES“ 1,0–2,0 nahoře na stěně scény
  (y 128–232, vůz od y ~300), maska zdola jako celek 0,2 s, prostrkání −1 % → +3 %, odchod maskou nahoru 1,875–2,0. Probuzení světel 2,0 doplněno o **nádech záře**
  z rozmazaného rozdílu `zap − vyp` úhlu 340 (`skripty/zare_uvod.py` → `podklady/u340_zare.png`, práh 20/255, `screen`, max 0,7, vrchol 2,1 = „shimmer“), ve stejné kruhové masce.
  Kroky otočky na 0,05 / 0,067 / 0,983 / 1,017 ostré, bez dvojitých kol.
- **Logo (M7)**: `knobCil` (960, 296) = horní bod střednice prstence. ① 21,25–21,6 knob **oběhne prstenec a vede hranu odkrytí** (smoothstep, 28 → 22 px, bílý s okrajem,
  aby byl na světlém studiu vidět), 21,56–21,66 se zúží na tloušťku prstence a rozplyne. ② čtvrtiny se neobjevují krytím (poloprůhledná světle modrá = mimo paletu),
  ale **kruhem ze středu** (maska 0,12 s) a dotáčejí se o 90°. ③ B / M / W dosedají **dostředivě po své radiále** (dřív B a W jely tečně). **Snímek 22,000 = originál
  bit po bitu** na všech 5 podsnímcích (porovnání s čistým SVG, max. rozdíl 0). Barvy v MP4: modrá (0, 101, 176), prstenec (111, 108, 110) = #0066B1 / #6F6F6F ±4.
- **End card**: logo + texty v kontejneru `#endSvet`, dotlačení 1,00 → 1,03 od 22,0 + 1/240 do 25,0 (nenulová rychlost na konci, nikdy nestojí). 22,5 „THE NEW 7 SERIES“
  (44 px, y 692–748), 23,0 modrá tečka se roztáhne do „Configure yours“ (dvě hrany na dvou pružinách, text vlastní maskou až 23,2–23,42), 23,5 disclaimer (y 912–939 i po dotlačení),
  24,0 kurzor přilétá zdola zprava v pohybu, hover ×1,25, **24,5 klik** (stisk −15 % na 3 snímky, kroužek, tlačítko krátce #0653B6 a −2 %). 24,983 ≠ 23,983 (průměr 1,1).
- **Rozhodnutí**: disclaimer 23,5 místo 22,5 (událost na každou dobu: 22,0 · 22,5 · 23,0 · 23,5 · 24,0 · 24,5, nikdy dva texty naráz přicházející) ·
  text tlačítka bez roztahování prostrkání (skutečné UI; dřív text dojel k okraji a kurzor ho překryl) · rychlé úseky pro render **20,7–21,7** (oběh prstence je rychlý,
  peak ~78 px/snímek), upraveno v `skripty/klicove.sh`; do příkazu plného renderu dát `…,20.7-21.7` místo `20.7-21.35`.
- **Nalezeno a opraveno**: prázdný celoobrazový kontejner `#endSvet` (a z-index knobu) měnil v Chromiu skládání vrstev a tím jemně pixely **celého obrazu i v hotových
  blocích** (13,8 / 18,017 / 20,5 průměr 0,16–0,35, max 73 na hranách). Kontejner se teď kreslí jen od 21,25, z-index knobu jen při oběhu prstence → 3,95 / 4,0 / 4,017 / 4,35
  (proti `kontrolni_v2`) a 13,8 / 16,4 / 18,017 / 20,5 (proti `kontrolni_b1`) **bit po bitu shodné**.
- **Výkon (C027)**: 1 s výřezu, 3 prohlížeče: 21,0–22,0 (`--sub 8` do 21,7) 22 s · 23,0–24,0 14 s · 0,0–1,0 (`--sub 8`) 17 s (včetně startu prohlížečů), pod limitem 25 s.
- **Pro zvukaře**: nové vizuální události bez SFX: nádech záře 2,0–2,45 (vrchol 2,1 = stávající „svetla“) · disclaimer 23,5 (tichý, zvuk netřeba) · kurzor vlétá 24,0 (případně tichý švih).
  Knob se rozplyne 21,6–21,66 (= „tah_prstence“ 21,6 sedí).

### Výroba B3: pohyb 4,0–14,0 (animátor 2026-11-01)
Nový modul `scena/b3.js` (časy v `CASY`: `tecka`, `linka`, `pilulka`, `puls2`, `popisekPryc`, `svih1/2`, `odleskBok`, `kota*`, `krokyZad`, `uhlyZad`, `svetlaZad`,
`listRust`, `listBila`, `interier`, `kostka`, `volic`, `glintVolic`, `dvere`, `prosivani`, `lounge`), podklady `skripty/b3_podklady.py` → `podklady/g14_chrom.png`,
`podklady/g10_lak.png` (z testu 2b). Kontrolní snímky s podsnímky `scena/kontrolni_b3/` (31 časů, 100 % + 480 px, `arch_480.jpg`), pásy `kontrolni_b3/pasy/` (5,9–6,1 a 6,9–7,1).
- **4,35–6,0**: kurzor letí k obrysu ledvinek, 5,0 klik → modrá tečka s pulzem, linka 1 px, 5,25 pilulka „BMW Iconic Glow“ (kruh → pilulka, pružina 3 %) na stěně vpravo nahoře,
  5,5 kurzor odjede zrychlením, 5,75 druhý pulz, 5,875–6,0 odchod do tečky; lišta 5,875–6,0 pod okraj (pneumatika g05 by ji jinak křížila).
- **Glint 5,75 vypuštěn** (povolená záloha): obrys Iconic Glow má v g03 jas 224 (lak 197), +12 % screen = +3,7/255, neviditelné. Na 5,75 jen druhý pulz tečky.
- **6,0–7,0**: g06 je g05 posunutý přesně o 220 px (průměrný rozdíl 0,28/255), proto jeden záběr g05 (1,15× nativního) se dvěma švihy doleva (6,44–6,56 a 6,86–7,0).
  Match cut: náboj kola 5,983 (727, 737) → 6,017 (720, 737), posun 7 px.
- **7,0–8,0**: g10 1,1×, přijede po švihu exponenciálně (1002 → 912), odlesk softboxu v masce laku, kóta od nárazníku k nárazníku nad střechou + „5,395 mm“ (sloupce číslic odstupňovaně, na čase snímku), lišta se vrací 7,0–7,3.
- **8,0–10,0**: otočka 270 → 180 srovnaná na bbox g10 (šířka, střed, spodek), kroky na čase snímku (8,133 ostré), kurzor „ruka“ chytí bok 8,0 a táhne doprava (švih, dosednutí 9,0),
  9,0 zadní světla rostoucím kruhem z rozdílu zap/vyp, dotlačení 1,00 → 1,05 + srovnání na střed (912 → 960), 9,5 kurzor k liště, 9,875 hover „Comfort“, 10,0 klik.
- **10,0–13,5**: ukazatel přeskočí na „Comfort“ a vyroste v list (horní hrana napřed, kriticky tlumeně, modrá → bílá do 10,15; do 10,15 DOM nad lištou, pak plátno), lišta 10,0–10,15 dolů,
  zadní pohled pod listem 0,96 a −25 %, od 11,0 (střih uvnitř listu) g03 den = stav B1 na 13,5. Interiér se otevře ze středu 10,15–10,4, kostka (WebGL, pitch −6°) yaw 0 → −40° 10,25–12,45 (sinusová ease-in-out),
  11,0 g14 výřez 0,855× nativního + glint po chromu voliče (maska jas + bez barvy, dřevo mimo), 11,5 zpět do kostky, 12,0 g13 vjede zprava (náběžná hrana = levý okraj rendru, otevřené dveře), kostka odjíždí pomaleji,
  13,0 přiblížení na prošívání; rámování g13 (`g13Pohled`) končí na 13,5 přesně v rámování B1 (`kresliObsahListu` beze změny výstupu).
- **„YOUR PRIVATE LOUNGE“ dole vlevo bílým** (y 816–920) se stínem 1 px: nahoře je světlý strop přerušený tmavou opěrkou hlavy, tmavý ani bílý text by tam nebyl čitelný (záloha ze storyboardu).
- **Regrese**: 1,5 / 3,95 / 4,0 / 4,017 / 4,35 / 13,5 / 13,8 / 14,0 / 16,4 / 18,017 / 20,5 / 22,0 / 24,983 bit po bitu shodné s `kontrolni_b2` / `kontrolni_b1`.
- **Výkon (C027)**: 1 s 6,4–7,4 = 19 s, 10,6–11,6 = 27 s (vč. startu), 2 s 10,6–12,6 = 51 s → ~24 s na 1 s (kostka WebGL), na hranici limitu.
- **Pro plný render**: přidat rychlý úsek `6.4-6.6` (švih 6,44–6,56). **Pro zvukaře**: kurzor odjíždí 5,5 a 10,05 (případně tichý švih), lišta zajíždí 5,875 a vrací se 7,0, kostka bez nové SFX.

### Celková kontrola pohybu a plný render v1 (animátor 2026-11-01)
Kontrolní snímky na doby a po 0,25 s `media/…/render/doby_nahled/`, okolí dropu 2 `render/k16_nahled/`, render `render/V003_obraz_v1.mp4`
(25,0 s, 1920×1080, 60 fps, zvuk = `hudba.wav` podle zadání úkolu, 361 s výpočtu), technická kontrola `media/kontrola/003-bmw-rada7/animator-v1/`.
- **Nalezeno a opraveno (regrese z B3)**: `b3.js` přidával do `CASY` klíč `listaZpet: [7.0, 7.3]` a tím přepsal `listaZpet: [16.05, 16.28]` dropu 2.
  Tmavá lišta se proto na 16,000 objevila skokem s textem a výplň posuvníku přes text přejela (16,0–16,03). Klíče B3 přejmenované na `listaPrycB3` / `listaZpetB3`
  (nikde se nečtou, lištu 5,875–7,3 počítá `listaDY`), kontrola kolizí klíčů `jadro.js` × `b3.js`: žádné další. Teď na 16,000 jen světla na černé + výplň,
  lišta se odkrývá od ukazatele 16,05–16,28. Naměřeno v MP4: 15,983 průměr 0,6 · 16,000 max 255, 7 964 px > 235.
- **Nalezeno a opraveno**: ve stoupání 14,1–14,9 byl u levého okraje svislý pruh ~10 px `#060606` vedle nočního studia `#161616` (g04 se kreslil od x 0 rendru,
  rámování g03 má vlevo 140 px doplněného studia). Levý sloupec g04 / g04_noc se teď protáhne přes −EXT…0 (`kresliStoupani`, `foto.js`). Kontrola okrajů všech snímků po 0,25 s: bez švu.
- **Rychlé úseky**: podle Pořadí stavby a B3, ne podle starého příkazu: `0-1.05,3.9-4.4,5.9-6.1,6.4-6.6,6.9-7.1,8.1-8.45,15.9-17.6,17.85-18.05,20.7-21.7`.
- **Kontrola MP4**: −14,1 LUFS / −1,2 dBFS (jen hudba), bez zamrzlých ani černých úseků; skoky = plánované střihy a kroky otočky; 10,183 „probliknutí“ = otevírání interiéru
  maskou ze středu listu (pás snímků), ne chyba. Logo na 22,000: modrá (0, 101, 176), šedá (111, 110, 110) = `#0066B1` / `#6F6F6F` ±4. Návaznosti 4,0 / 10,0 / 13,5 / 16,0 / 21,0 bez skoku, vždy nejvýš jeden text.

### Opravy obrazu kolo 1 → v2 (animátor 2026-11-01)
Render `media/…/render/V003_obraz_v2.mp4` (25,0 s, 8,6 Mbit/s, −14,1 LUFS / −1,2 dBFS, ~8 min výpočtu), kontrola `media/kontrola/003-bmw-rada7/animator-v2/`.
Rychlé úseky (sub 8): `0-1.05,3.9-4.4,5.9-6.1,6.4-6.6,6.9-7.1,7.3-8.0,8.1-8.45,9.95-10.55,11.95-12.55,13.45-14.3,15.9-17.6,17.85-18.05,18.7-18.9,19.7-19.9,20.6-21.7` (i v `skripty/klicove.sh`).
- **Počitadlo (blokující „259 km/h“)**: `nastavPocitadlo` jako počítadlo kilometrů s přenosem (vyšší řád se hne jen když jsou nižší číslice 9, přechod jen v posledních 0,35 jednotky)
  a hodnota omezená stropem (250 / 57 / 230). Ověřeno po snímcích 17,52–17,95, 18,8–19,05, 19,8–20,05: sled 245 → 249 → 249/250 → 250, nikdy nad cílem.
- **Posuvník noci (M3a)**: 14,0–14,25 ukazatel → posuvník na nule (knob s kurzorem odjede na začátek dráhy, nádech), 14,25–15,5 tah; hranice = (x_knob − 240) / 1440 × 2000 − 40
  (měkký okraj 80 px celý mimo obraz na začátku i konci). Klíče z rámování stoupání: levý světlomet přejede **15,0** (řazení), pravý **15,25** (shimmer), 15,5 konec dráhy;
  zaváhání 14,5 / 15,0 = časová deformace (3 snímky na ~25 % rychlosti, bez couvání). Odchylka hranice od knobu: 15,0 −21 px, 15,25 +151 px (lineární přepočet podle storyboardu).
- **Noční lak** (`skripty/noc_grade.py` v3): v masce vozu S-křivka se středem ~70 (lak 92 → 112), +0,4 EV ve světlech laku, přechodový filtr střecha +0,4 → prahy −0,4 EV, úbytek k zádi −0,3 EV.
  Nový `podklady/g04_nocA.png` (stejná karoserie, studio rendru) pro 14,0–15,5. Rendr g04 v bodech: dveře 92 → 126, horní blatník 147, spodek dveří 104, kapota 190. Odlesk 18,0 jádro 0,15 → 0,26.
- **Rychlé pohyby (C003)**: vjezd g13 12,0–12,5 kubický ease-out + rozmazání v kódu (`rozmazX`, 6 kopií v rámci podsnímku, kostka WebGL jen jednou); let kurzoru 7,3–8,0 a 9,25–9,855 mocninný dojezd.
- **Úvod**: 1,875–2,0 studio −1 EV (celý obraz, maska vozu pro otočku není), světla 340 jako rozdíl zap − vyp (`podklady/u340_rozdil.png`) přičtený po ztlumení, návrat 2,2–2,6;
  záře 0,7 → 1,0. Dotlačení na doby 2,5 / 3,0 / 3,5 (+1,6 %, 0,3 s) + podklad 0,6 %/s, zdvih scény 1,045 a hlubší stín. **Rámování g03 od 4,35 je pevně z v1**
  (popisek, match cut, stoupání), proto nájezd dropu 1 je teď 1,00 → 1,11 (dřív 1,18).
- **9,0–10,0**: 9,5–9,95 dotlačení 1,05 → 1,12 na zadní světla, kurzor odstartuje 9,25, hover „Comfort“ 9,875 natáhne ukazatel o 8 px (navazuje na list).
- **Výkon a logo**: bublina měkce omezená k x ≤ 1824, dráha končí 1810; knob při letu naroste na ~42 px; zaplavení 21,0–21,33 poloměrem na čase snímku (ostrý okraj),
  r = 14 + 1250·x^1,25; knob na světlém studiu s okrajem #6F6F6F a stínem; logo se 21,25–22,0 dotlačí 0,94 → 1,00 (knob obíhá ve stejném měřítku, cíl letu (960, 311,8)),
  snímek 22,000 beze změny (statický snímek bit po bitu = v1). Disclaimer `#666666`. Noční zrno ±1/255 ze dvou spritů (lighter + difference), posun podle snímku.
- **YDIF po čtvrtsekundách (480×270, v1 → v2)**: 2,0 0,12 → 0,41 · 2,25 0,09 → 4,93 · 2,5 0,12 → 1,23 · 2,75 0,10 → 0,08 · 3,0 0,10 → 0,46 · 3,25 0,21 → 0,37 · 3,5 0,22 → 0,74 ·
  9,5 0,15 → 0,58 · 9,75 0,09 → 0,15 · 21,25 0,04 → 2,17 · 21,75 0,03 → 0,06. Cíl ≥ 0,6 všude splněn není (2,75 a 9,75).
- **Beze změny (vědomě)**: drop 2 16,0–16,5 vůz uprostřed (schválená odchylka režiséra), plakát 0,0 (odpověď režiséra: A8 přes šířku stačí), „YOUR PRIVATE LOUNGE“ dole bílým,
  zaplavení z knobu (storyboard, past 12), časy čtvrtin a písmen loga (zvuk), CRF 16 v nástroji (bitrate je teď 8,6 Mbit/s).
- **Pro zvukaře**: levý světlomet se odkryje 15,0 (= řazení), ztlumení studia 1,875–2,0 (případně tichý „zhasnutí“ dozvuk), knob 14,0–14,25 odjede doleva (nádech), let kurzoru od 7,3 a 9,25.

### Opravy obrazu kolo 2 → v3 (animátor 2026-11-01)
Podle nálezů kritiků kola 2 a závazných odpovědí režiséra ke kolu 2. Záloha v2b scény jen ve scratchpadu. Render `render/V003_obraz_v3.mp4`.
- **Úvod 1,875–2,6**: celoplošné ztlumení −1 EV zrušeno. Na 2,000 úder: `zap/uhel_340` přes `vyp` za 2 snímky (celý rozdíl rendru BMW: denní svícení,
  obrys ledvinek; moduly světlometů v denním rendru konfigurátoru skoro nesvítí) + nádech záře (screen, vrchol 2,1, pak trvale 0,22) + dotlačení ~1,04 → ~1,08
  (kriticky tlumeně 0,3 s). Dotlačení na doby 2,5 / 3,0 / 3,5 prodloužena 0,3 → 0,35 s. Nadpis odchází maskou nahoru mocninou 2,2 přes celých 1,875–2,0.
- **Drop 1 (odpověď 5)**: nádech 3,875–3,983 scéna i vůz 1,00 → 0,94 (kriticky tlumeně), rozšíření na 4,0 startuje z menší scény (D1 se přepočítá samo).
- **Posuvník noci (odpověď 1)**: dráha přes celou šířku x 20–1900, primární je poloha knobu (monotónní kubika, klíče 15,0 levý a 15,25 pravý světlomet),
  hranice = x knobu −20 → +20 px úměrně dráze, měkký okraj ±40 px se u krajů obrazu zúží k nule → 14,25 celý den, 15,5 celá noc, hranice nikdy před knobem ani za koncem dráhy.
- **10,0 list**: modrá → bílá za 4 snímky v lineárním světle; interiér se otevírá až 10,25–10,45 maskou na čase snímku (ostrá hrana, list ≥ 85 %).
- **12,0 (odpověď 4)**: přechod maskou podle siluety zrušen → **tvrdý střih na dobu 12,0 na g13** s dotlačením 1,00 → 1,035 (0,3 s) a pak do 1,05 v 13,0.
- **„YOUR PRIVATE LOUNGE“ (odpověď 3)**: nahoře vlevo na stropu / zadním okně g13, #262626, 42 px, jemné světlé halo; 88 px se mezi okraj listu a opěrku hlavy nevejde.
- **13,5–14,0**: interiér se zavře do středu 13,56–13,70, pak se smršťuje bílý tvar, 13,80–13,86 bílá → modrá (lineární světlo); lišta jede pod listem
  (clip-path evenodd = vyříznutý tvar listu), přes list se už nekreslí.
- **9,0–10,0**: 9,0 dotlačení 1,00 → 1,04 (0,25 s), nájezd 9,5 1,05 → 1,18 (celkem ~0,97× nativního).
- **Švih 7,0**: g05 rozmazaný v kódu ve směru pohybu (rozmazX, mezera kopií ≤ 2 px). Logo: čtvrtiny v plné velikosti, jen dotočení + kuželová výseč 0,2 s (ne rostoucí kruh).
- **Bublina**: 249 → 250 se odroluje 17,79–17,867 (poslední snímek s číslicemi bubliny), dřív v 17,75.
- **Výkon**: výřez 16,5 o 120 px a záběr 20,0 o 55 px doleva (vůz x ≤ ~1005). Lišta 760 → 860 px, písmo 20/18 → 24/22 px, pilulka popisku 52 → 60 px / 29 px.
- **Render**: rychlé úseky rozšířené o 6.45-6.75, 6.85-7.1, 9.95-10.3, 13.6-13.9, 18.7-18.9, 19.7-19.9, 21.55-21.9 (duchové při rychlých odchodech).

### Střih v2 (střihač 2026-11-01): nálezy kritiků 6,5 a 12,0 + export
Opraveno ve scéně (`scena/b3.js`, záloha původního souboru jen ve scratchpadu), přerenderováno celé `render/V003_obraz_v2b.mp4` (490 s, stejný příkaz,
rychlé úseky `6.45-6.75,6.85-7.1` a `11.95-12.6` místo `6.4-6.6,6.9-7.1` a `11.95-12.55`, i v `skripty/klicove.sh`). PSNR proti v2: změna jen 6,000–6,983 a 12,000–12,533, jinde beze změny.
- **6,5 (závažná)**: švih na „g06“ (= týž záběr g05 posunutý) zrušen, místo něj **punch-in na náboj g05 1,00 → 1,25** (kriticky tlumeně 6,5–6,7, náboj na obrazovce stojí).
  Kvůli G7 (≤ 1,3× nativního) je výchozí měřítko g05 sníženo 1,15 → **1,04** (konec 1,30); poloha match cutu 6,0 beze změny (náboj = kolo g03 na 5,983), kolo je na střihu ~1,5× větší místo ~1,7×.
  Pokrytí obrazu ověřeno včetně švihu 7,0. Zvuk 6,5 (tichý švih) sedí i na punch-in.
- **12,0 (drobná)**: g13 **nemá blízký B-sloupek** (dveře otevřené, pohled z boku), vzdálený sloupek je krátký, za opěrkou, a vpravo od něj je jen 1 120 px rendru (posun by nepokryl list).
  Náběžná hrana masky proto = **levá silueta opěrky a opěradla předního sedadla** (lomená čára změřená ve 100 %, `G13_HRANA`), g13 vjíždí zprava 12,0–12,45 (kubický ease-out),
  kostka odjíždí doleva 0,6× (paralaxa) a zbytek vlevo od siluety (zadní sedadla) odkryje odjezd kostky ease-in do 12,55. Rozmazání pohybem zkrácenou závěrkou přechodu
  (`G13_ZAV` 0,15 → ≤ ~11 px při ~140 px/snímek), rozmazání v kódu (`rozmazX`) tu už nepoužito. Stín hrany 0,22 / 28 px.
- **Export**: `vystup/V003_v2.mp4` (video stopa kopírovaná z renderu, zvuk `zvuk_v1.wav` přes MOV → `master_zvuk.sh`: −13,9 LUFS / −1,2 dBTP, zisk z −14,34),
  `vystup/V003_v2_bez_hudby.mp4` (zvuk = `zvuk_bez_hudby_v1_stejny_zisk.m4a` beze změny, −23,2 LUFS / −2,0 dBTP: podle rozhodnutí „verze bez hudby v úrovni mixu efektů, nenormalizovat“),
  plakát 18,45 s (noční vůz se světly + 250 km/h), `popisek.txt` (otázka přesunuta za disclaimer, před hashtagy, J3). Kontrola `media/kontrola/003-bmw-rada7/strih-v2/`.
- Pozor (C-kandidát): mezikontejner MKV zaokrouhlí časy snímků na 1 ms (60 fps → kroky 16/17 ms, délka stopy 24,999 s). Pro spojení obrazu s PCM zvukem použít MOV.

### Střih v3 (střihač 2026-11-01): drop 1 + export
- **Drop 1 (závažná)**: nádech 3,875–3,983 na 0,94 už byl ve v3 animátora. Doplněno ve scéně (`foto.js` `drop1O`, `drift1`; `b3.js` `g03Bod` sdílí `drift1`;
  záloha původních souborů jen ve scratchpadu): **překmit vozu** `1 + 0,03·sin²(π·u)` na 4,0–4,35 kolem stejného pevného bodu jako nájezd → vrchol +2,2 % ve 4,2,
  na 4,35 přesně původní rámování (`D1_KONEC` beze změny, stoupání 14,0 se nemění). **Drift 4,35–6,0**: posun vozu 40 → 64 px rendru (~61 px na obrazovce),
  kubický ease-out s náběhem přes časovou deformaci τ 0,04 (rychlost hned po dosednutí, bez hrbu), hloubka D 0,05 smootherstep beze změny.
  Šířka vozu 3,983 ≈ 1 074 px → vrchol 4,2 ≈ 1 354 px (1,26×) → 4,35 ≈ 1 325 px; g03 nejvýš ~0,95× nativního (G7). YDIF (plné rozlišení) 4,35–4,5 medián 0,04 → **1,07**,
  4,35–5,0 0,34 → 1,14, snímků < 0,1 v 4,35–5,0: 7 → 0. Popisek „BMW Iconic Glow“ i match cut kola (kolo0 = g03Bod 5,983) jedou s driftem, g05 6,0–7,0 se proto
  posunul o ~22 px (pokrytí obrazu ověřeno, PSNR proti v3 jinde než 3,4–7,0 = beze změny; 3,4–4,0 jen šum kodéru ~58 dB).
- **12,0 (drobná)**: ve v3 už je tvrdý střih na g13 (odpověď 4), koláž dvou perspektiv nevzniká (pás 11,9–12,6 ověřen) → beze změny.
- Render `render/V003_obraz_v3b.mp4` stejným příkazem jako v3 (416 s). Export: `vystup/V003_v3.mp4` (video stopa bit po bitu z renderu, `zvuk_v3.wav` přes MOV →
  `master_zvuk.sh`: −13,9 LUFS / −1,2 dBTP, posun 0 vzorků), `vystup/V003_v3_bez_hudby.mp4` (`zvuk_bez_hudby_v3_stejny_zisk.m4a` kopírováno, −23,2 LUFS / −1,4 dBTP,
  korelace s `zvuk_bez_hudby_v3.wav` 0,997, posun 0; rozhodnutí „nenormalizovat“), plakát 18,45 s, popisek beze změny. Kontrola `media/kontrola/003-bmw-rada7/strih-v3/`.

### Otevřené otázky kreativního ředitele (rozhodne režisér)
- ~~„5,395 mm“~~ vyřešeno: délka 5 395 mm je pro 740d potvrzená v technických údajích (Režijní list), zůstává jako kóta 7,0–8,0.
- End card „THE NEW 7 SERIES“ + tlačítko „Configure yours“ (vlastní copy, CTA odkazuje na konfigurátor = koncept).
- Vlastní anglická hesla po revizi jen dvě: „THE NEW BMW 7 SERIES“ (1,0) a „YOUR PRIVATE LOUNGE“ (12,5). Vypuštěno: „PERFECTION IN EVERY DETAIL“,
  „DESIGN THAT INSPIRES“, „PRECISE FROM EVERY ANGLE“, „YOUR OASIS OF CALM“, „DYNAMICS ON EVERY ROUTE“.

### Změny po oponentuře (kreativní ředitel 2026-11-01)
Oponent: realismus 8, energie 6,5, celkem 7,5. Opravy 1–11 zapracované do rozvržení, tabulky, motionů, kontrolních snímků, pastí a pořadí stavby.
Pevné časy hudby beze změny (4,0 · 10,0 · 14,0 · 16,0 · 22,0 · 25,0).
| # | oprava | kde | co se změnilo |
|---|---|---|---|
| 1 | drop 2 | 14,0–16,35 | den → noc dokončený do 15,5 (světla vzplanou 15,25 pod hranicí), 15,5–15,75 napětí, **15,75–16,0 tma + ticho −18 dB**, 16,000 jen světla na černé, karoserie z tmy za 0,35 s, ukazatel na „Performance“. Měření jasu a YDIF v kontrolních snímcích |
| 2 | výkon | 16,0–20,75 | střih na každou dobu 16,0 / 16,5 / 17,0 / 17,5 (celek, výřez 1,25×), rychloměr souvisle přes střihy, 18,0 / 19,0 / 20,0 obří čísla ~300–360 px v pravém sloupci, číslice rolují na dobu, dotlačení i na 18,5 / 19,5. Posuvník z lišty: dráha 8 px, 760 px |
| 3 | noční rendry | 15,5–21,0 | noční grade (studio `#060606`, S-křivka, ochlazení, vinětace), záře jen z rozdílu v masce světel, vůz posunutý doleva s doplněním černé |
| 4 | drop 1 | 4,0–4,35 | přiznaný střih přesně na 4,000 + jednotný nájezd 1,00→1,18 spolu s rozšířením scény, pak 2,5D drift |
| 5 | úvod | 0,0–2,0 | snímek 0 uprostřed tažení, 8 kroků 0,0625–1,0 na mřížce 0,0625 s, drift +20 px, nadpis 1,0–1,875, světla dál na 2,0 |
| 6 | M1 | 10,0–10,5 / 13,5–14,0 | ukazatel vyroste v list (barva modrá → bílá do 0,15 s, dvě pružiny), list se pod kurzorem smrští zpět do ukazatele, jedno gesto 13,5–15,75 |
| 7 | luxus | 10,0–14,0 | kostka interiéru rotateY 0 → −35° (test, záloha g12), 11,0 střih na g14 (tunel, glint po chromu voliče), 11,5 zpět, glint po dřevě zrušen, 13,0 přiblížení na prošívání |
| 8 | předání do loga | 20,5–22,0 | 230 kW 20,0–20,625 · stažení 20,5–20,75 · let knobu 20,75–21,0 · zaplavení 21,0–21,3 · oběh prstence 21,25–21,6 · čtvrtiny 21,6–21,85 · B/M/W 21,875 / 21,9375 / 22,0, snímek 22,000 = originál |
| 9 | glint 5,75 | 5,75–6,15 | jen pixely obrysu Iconic Glow, +12 % `screen`, 0,4 s; kontrola 5,85, jinak jen pulz tečky |
| 10 | zvuk | 3,875 / 15,75 / 16,0 | automatika −18 dB (náběh 20 ms) 3,875–4,0 a 15,75–16,0, obrácený činel a vír dozní před tím, drop 2 nejhlasitější + nízký náraz motoru se světly |
| 11 | drobnosti | 6,0–7,0 · 8,0–9,0 · end card | disclaimer y ≤ 940, kontrola lišty proti pneumatice 6,02 / 6,6 (záloha: lišta pod okrajem), druhé krokování = švih 6 kroků po 0,0625 + dosednutí 8,5 / 8,75 / 9,0 |
| + | vlastní nálezy | 4,0 · 10,15 · celé video | **spojitost světel**: na 340 svítí, g03 je zhasnutý → g03 + rozdíl g04 − g03 v masce světel (past 16) · **podsnímky** nesmí slít dva úhly nebo dva rendry (výběr obrazu podle času snímku, past 2) · **méně textu** (5 momentů) |

**Energie po revizi (co se hýbe nepřetržitě / kolik událostí)**: každý takt má souvislý pohyb (drift, dotlačení, rotace kostky, knob, gesto kurzoru) a událost na každou dobu.
Tvrdé střihy obrazu: 0,0–1,0 osm kroků · 4,0 · 6,0 · 6,5 · 7,0 · 8,0 + devět kroků · 11,0 · 11,5 · 12,0 · 16,0 · 16,5 · 17,0 · 17,5 · 18,0 · 19,0 · 20,0.
Nejhustší úsek je teď výkon (16,0–18,0 střih na dobu), ne úvod. Odhad po revizi: realismus 8,5–9, energie 8,5–9, celkem ~8,8. Na 9+ rozhodnou testy (pasti 16–18)
a provedení dropu 2 (tma → světla). Ověřit hned na klíčových snímcích, ne až v plném renderu.

## Průběh výroby
| kolo | kdo | co se dělalo | verdikt kritika | hlavní nálezy |
|---|---|---|---|---|
| příprava | analytik ∥ zvukař → analytik ∥ animátor → kreativní ředitel → oponent → revize | rendry z konfigurátoru, fakta, logo ve vrstvách, hudba luxsport, 7 motionů, test realismu, koncept ONE CONTROL | oponent: realismus 8, energie 6,5, celkem 7,5 → revize 11 oprav | drop 2 tma → světla, výkon střih na každou dobu, noční grading, kostka interiéru, úvod v pohybu |
| výroba | zvukař ∥ animátor (kostra a klíčové snímky → neschváleno 7,8 / realismus 7,5 / energie 7,5 → 8 oprav → bloky B1, B2, B3 → render) | SFX 77 → v1b 82 (režisér posunul na obraz), render v1 | – | kolize klíčů CASY (C036) |
| 1 | technika · wow · zadání | kontrola V003_v1 | **BLOKUJÍCÍ** (259 km/h), wow 7,5 / realismus 8 / energie 6,5 | mrtvé úseky 1–3,75 a 9–10, noc neodkrývá knob, šedý noční lak, duchové u rychlých pohybů, přechod do loga |
| 2 | technika · wow · zadání | kontrola V003_v2 (259 pryč, noc pod knobem, noční lak +0,4 EV, duchové, energie úvodu; střihač přerenderoval 6,5 a 12,0) | wow 8 / realismus 8 / energie 7,5, technika OPRAVIT | celoplošné ztlumení ve 2 s, koláž ve 12,3–12,5, hranice noci předbíhá knob, malý drop 1 |
| 3 | technika · wow · zadání | kontrola V003_v3 (noc ±20 px s knobem, světla úder 2,0, lounge nahoru, tvrdý střih 12,0; střihač v3b: drop 1 překmit a drift) | **SCHVÁLENO všemi 3**, wow 8,3 / realismus 8,5 / energie 8, všech 17 pravidel splněno | 0 závažných, 14 drobných → režisérská oprava v4 (list 10,1, ozvěny čísel 18,0, lounge 60 px, odchody textu, end card, stoupání) |

**Zvuk v1 (zvukař, 2026-11-01)**: 77 SFX podle storyboardu (sloupec zvuku + Změny po oponentuře) ze `projekty/003-bmw-rada7/sfx_udalosti.json` → `media/…/zvuk/sfx.wav|json`, `zvuk_v1.wav`,
`zvuk_bez_hudby_v1.wav`, `sfx_log.txt`, `zvuk_v1_master.m4a`, `zvuk_bez_hudby_v1_stejny_zisk.m4a`, spektrogramy. `hudba.wav` ani časování beze změny. Příkaz:
`python3 -I nastroje/sfx.py --udalosti projekty/003-bmw-rada7/sfx_udalosti.json --delka 25 --out media/projekty/003-bmw-rada7/zvuk/sfx.wav --hudba media/projekty/003-bmw-rada7/hudba.wav
--mix …/zvuk/zvuk_v1.wav --bez-hudby …/zvuk/zvuk_bez_hudby_v1.wav --automatika 3.875-3.99:-18:20:10 --automatika 15.75-15.99:-18:20:10 --zisk-hudby "15.98:0,15.99:1,16.45:1,16.9:0"
--zisk-hudby "20.5:0,20.9:-1,25:-1" --saturace 15.99-16.45:6 --saturace 21.99-22.15:6 --ticho 3.975-3.996 --ticho 15.73-15.996 --limiter -1.8`.
Rozhodnutí: (1) nové prémiové typy v `sfx.py` (detent, klik, hover, prepinac, sklo_pop, trpyt, svetla, tik_cislo, zamek, radeni_lux, zapaleni, klik_uder, svetla_uder,
svih_mekky, tah_prstence, dosednuti, klik_kov, logo_lux; dolní propust 11 kHz, tóny v D moll jako hudba) + klíče `od` / `konec` (efekt nezačne / nedozní v tichu);
(2) kroky otočky na **prvním snímku nového úhlu** (0,0667 · 0,1333 · 0,2 · 0,3167 · 0,45 · 0,5667 · 0,75 · 1,0 a 8,1333 · 8,2 · 8,25 · 8,3167 · 8,3833 · 8,45, past 2);
(3) automatika nádechů končí návratem přesně v 4,000 / 16,000 (plné −18 dB do 3,99 / 15,99, návrat 10 ms); (4) drop 2 hudba +1 dB (náběh schovaný v tichu) a finále od 20,9 −1 dB,
aby drop 2 byl nejhlasitější o ≥ 1 dB (C032), špičky úderů 16,0 a 22,0 měkce nasycené, limiter −1,8 dBFS (rezerva TP po AAC); (5) navíc oproti sloupci zvuku: tichý stisk myši 3,875
v nádechu (−34 dBFS, utnutý 3,97), dosednutí ukazatele na „Performance“ 16,25, lock čísla 5,395 mm 7,6 a knobu na 250 17,875, zámek posledního kroku otočky 9,0;
(6) **tiky rysek** rychloměru 16,5 · 16,75 · 17,1875 (+ řazení 17,0 a 250 na 17,875) = návrh, kdy knob míjí rysky 50/100/150/200: animátor je má na tyto časy navázat.
Naměřeno: vrcholy 0,0 ms od událostí (ve stopě max 0,2 ms, překryté jen 4,1 a 16,25 dozvukem úderu), klíčové efekty 4,0 / 16,0 / 22,0 = −2,0 / −3,0 / −2,2 LU proti hudbě (100 ms),
master po AAC −13,9 LUFS / −1,2 dBTP, pásma sub 21 % · středy 36 %, RMS 50 ms: stoupání −17,4 → −16,8 → −16,0 → −13,0, drop 2 −7,0 (finále −9,8, výkon −10,7, drop 1 −11,8, jízda −13,9).

**Zvuk v3 (zvukař, kolo 2 → v3, 2026-11-01)**: nález kritika (verze bez hudby se starou stopou, C039) opraven přegenerováním obou WAV ze stejného zdroje
stejným příkazem (jen výstupy `sfx_v3.wav|json`, `zvuk_v3.wav`, `zvuk_bez_hudby_v3.wav`, log `sfx_v3_log.txt`). Změny zdroje `sfx_udalosti.json`: (1) **světla 2,1 → 2,0**
(odpověď ke kolu 2 bod 2: rozdíl zap − vyp naskočí na úder 2,000; hum 1,88–2,0, ping D6 na 2,000 s kopákem a basou); (2) náraz knobu 15,5 `konec` 15,72 (dozvuk −101 dBFS
zasahoval do ticha 15,73–16,0, teď −240). Proti v1b se mix liší jen v 1,86–2,66 a 15,715–15,724; hudba a její časování beze změny. Odvozené soubory: `zvuk_v3_master.m4a`
(−13,9 LUFS / −1,2 dBTP, zisk +0,29 dB), `zvuk_bez_hudby_v3_stejny_zisk.m4a` (stejný zisk +0,29 dB, dolní propust 19 kHz + strop −1,4 dBFS jen na úderu 16,0 (≤ 0,55 dB),
−23,2 LUFS / −1,4 dBTP, posun 0 vzorků). Staré odvozeniny ze 4:36 přesunuty do `zvuk/zastarale_pred_v1b/`.

**Zvuk v4 (zvukař, režisérská oprava po kole 3, 2026-11-01)**: nález „stoupání 14,5–15,25 tišší než exteriér“. Příkaz v3 beze změny + jediná volba navíc
`--zisk-hudby "14.05:0,14.3:2,15.73:2,15.745:0"` (výstupy `sfx_v4.wav|json`, `zvuk_v4.wav`, `zvuk_bez_hudby_v4.wav`, log `sfx_v4_log.txt`; `sfx_udalosti.json` beze změny).
**Odchylka od zadání režiséra** (rampa 14,0 → 15,5 na +2 dB): změřeno předem na mixu v3, lineární rampa nechá dobu 14,0–14,5 na −16,7 LUFS (exteriér −16,3)
a okna M v 14,5 a 15,0 na −17,1 / −17,0. Proto rychlý náběh na +2 dB už mezi kopákem 14,0 a 14,3, pak držet. Začátek 14,05 kvůli zážehu 14,0: jeho úroveň `lu`
se měří proti hudbě v 13,95–14,05, takže zůstane beze změny. Konec 15,745 leží v sestupu automatiky do ticha: 15,75 by kvůli převzorkování limiteru změnil 8 vzorků za 15,75 o 1 LSB.
Výsledek: mix se proti v3 liší jen v 14,050–15,745 s (zbytek bit po bitu shodný), verze bez hudby jen v 15,11–15,72 (světla 15,25 drží `lu` −7 proti hudbě, tedy +1,8 dB).
Ticho 15,73–16,0 má špičku SFX −240 dBFS, limiter ubírá nejvýš 0,21 dB, vrcholy efektů jsou 0,0 ms od událostí.
Master `zvuk_v4_master.m4a` −13,9 LUFS / −1,4 dBTP (zisk +0,17 dB, posun 0). `zvuk_bez_hudby_v4_stejny_zisk.m4a` vznikl stejným postupem jako v3 (zisk +0,17 dB,
dolní propust 19 kHz ×2, alimiter −1,4 dBFS) a má −23,2 LUFS / −1,4 dBTP. Pásma: sub 21 %, středy 36 %. Spektrogram `zvuk_v4_spektrogram_12.5-17.png`.
Hlasitost M masteru po 0,25 s (v3 → v4), okno 400 ms končící v čase: 13,5 −16,6 → −16,7 · 13,75 −17,1 → −17,2 · 14,0 −16,1 → −16,2 · 14,25 −16,2 → −16,0 · 14,5 −17,5 → −16,0 ·
14,75 −16,8 → −14,9 · 15,0 −18,1 → −16,2 · 15,25 −16,1 → −14,2 · 15,5 −14,7 → −12,9 · 15,75 −12,0 → −10,2 · 16,0 −15,9 → −14,3 · 16,25 −8,7 → −8,9 · 16,5 −8,5 → −8,7.
Po dobách (0,5 s): 13,5 −16,4 · 14,0 −15,9 · 14,5 −15,1 · 15,0 −12,9, roste monotónně (v3: −16,2 · −17,0 · −17,0 · −14,8). Okno M končící v 15,0 (14,6–15,0) leží mezi kopáky,
proto zůstává zub −1,3 dB proti 14,75. Odstranit by ho šlo jen zesílením přes +3 dB nebo pumpováním do rytmu, a pak by se stoupání přiblížilo dropu.
C032, max RMS 50 ms: stoupání 14,0 / 14,5 / 15,0 = −15,9 / −14,7 / −13,0 (v3 −17,1 / −16,6 / −14,9), drop 2 −6,7 zůstává nejhlasitější
(výkon −10,5, finále −9,6, jízda −14,0, drop 1 −11,6). Úsek stoupání 14,0–15,75 má −13,2 LUFS (v3 −14,9), exteriér 12–14 −16,2, drop 2 −7,8.

## Chyby během výroby

## Spotřeba tokenů
| agent / úkol | tokeny | akce nástrojů | čas |
|---|---|---|---|
| workflow příprava (7 agentů: analytik ×2, zvukař, animátor test, kreativní ředitel ×3) | 1 184 196 | 409 | 86,5 min |
| workflow výroba (23 agentů: zvukař ×2, animátor ×10, kreativní ředitel ×4, střihač ×3, kritici ×6…) | 4 501 603 | 1 621 | 302 min |

## Verze
| verze | datum | soubor / kam doručeno | změny |
|---|---|---|---|

## Zpětná vazba (doslova)

## Poučení
