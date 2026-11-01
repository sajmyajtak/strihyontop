# prompt-motion.com: poznatky pro tvorbu

Vlastní rozbor celého webu (stav 2026-10-30): **236 položek** (231 promptů, 6 skillů, 1 položka má obojí), 2 šablony, 5 článků blogu, stránka Customize.
Plné texty leží jen lokálně v `media/prompt-motion/polozky.json` a `media/prompt-motion/stranky/` (necommituje se).
Metadata a odkazy jsou v `katalog.md`. Aktualizace: `python3 -I nastroje/prompt_motion.py --jen-nove`.

**Licence:** prompty patří autorům, web povoluje jen použití jako reference (`use=reference`, `ai-train=no`).
Sem proto píšu jen odkaz, autora, vlastní shrnutí a krátké citace. Položky označuju **slugem**, tj. koncem URL
`https://prompt-motion.com/<slug>`, protože pořadí v JSON se při každém stažení mění.

---

## 1. Co to je a jak s tím pracovat

- Galerie motion-graphics videí, která vytvořil **Claude Opus 5.5** (platí pro všech 236). Ke každému videu je přesný prompt nebo skill. Videa pocházejí ze 216 autorů a vyšla na X mezi 23. 9. a 21. 10. 2026.
- Web dál nabízí **šablony** (showreel, 3D) s poli k vyplnění, **Customize** (prompt se doplní v prohlížeči) a **blog** s rozbory celé galerie.
- **Hlavní lekce:** stejný 26slovní prompt spustilo 33 lidí a výsledky měly od 0 do 17 023 lajků. Krátký prompt je loterie.
  Nejlepší videa vznikla z dlouhých strukturovaných promptů, které za Clauda rozhodnou to podstatné:
  **jeden koncept, seznam zakázaných efektů, mřížku dob (BPM), metodu renderu a kontrolu snímků.**
- **Postup u nás:**
  1. Podle typu videa vybrat 2–3 položky (oddíl 6). Plný text je v `polozky.json`, výběr pomůže `katalog.md`.
  2. Prompt nikdy nepoužít 1:1. Převést ho do naší kostry (oddíl 10): 9:16, značka, čeština, naše pravidla.
  3. Ze zvoleného promptu převzít hlavně koncept, zakázané efekty a „pasti“ (gotchas), nepřebírat jeho formát a barvy.
  4. Po videu zapsat do `pouceni.md`, co z promptu fungovalo.
- Lajky v našich datech nejsou. Popularitu ukazuje jen blog (citované počty) a pořadí „Most liked prompts“ na stránce Customize.

---

## 2. Metoda tvorby

### 2.1 Jak se renderuje (pipeline)
Video se vždy vyrábí stejně: kód nakreslí snímek pro čas t, headless prohlížeč udělá snímek obrazovky, ffmpeg poskládá video.
Protože se každý snímek počítá z času, nic se „nezasekne“ a obraz drží doby i na pomalém stroji.

| přístup | výskyt | kdy použít |
|---|---|---|
| **Čisté HTML / canvas + `seek(t)` + Playwright + ffmpeg** | blog: 23 z 56 videí, u kterých autor uvedl nástroj; v promptech `seek(` 13×, Playwright 12× | **náš výchozí přístup** (`render_html.cjs`). Nejjednodušší, jde v něm CSS, SVG, canvas i WebGL. Metodu ale musí prompt výslovně popsat. |
| **Remotion** (React) | blog 13, prompty 5 (`antonio-kodheli-490109`, `daniel-haida-8691d4`, `aschapmann-131210`, `wani-shola-16ca7a`, `lester-tyy-f897f7`) + skill product-film | když má klient produkt v Reactu (jeho skutečné komponenty) nebo chce upravitelný zdroj. **Licence** je u některých firem placená. |
| **HyperFrames** (HeyGen, Apache 2.0) | blog 10 (z toho 6 launch videí; nejlajkovanější z nich má 1 415), prompty `ik-builds-b8bdcf`, `danilowm-d3720d` + skill session-story | HTML s data atributy + GSAP, hotový renderer pro AI agenty. Pro nás je to alternativa bez přínosu navíc. |
| **three.js / WebGL2** | blog 5; `templates/realtime`, `pankajstwt-49978ed`, `twoclipping-d89be5`, `gorden-sun-041f56`, `nft-chen-5f8bb0` | jen pro skutečné 3D. **Náš stroj nemá GPU (4 CPU)**, takže 3D s hloubkou ostrosti a 16 podsnímky by se renderovalo velmi pomalu. |
| **Manim** (+ edge-tts) | `linearuncle-5d2bae` (258 lajků) | matematika a grafy funkcí s hlasem zdarma |
| Python + ffmpeg | `kloss-xyz-15182a` (9:16 „brain rot“) | chaotický, rychlý sociální styl |

Blog radí: **metodu renderu vždy napsat do promptu**, jinak si ji Claude zvolí pokaždé jinak a výsledky nejdou zopakovat.

### 2.2 Zásady deterministické scény (shodují se ve všech nejlepších promptech)
- Každý styl se počítá z času uvnitř `seek(t)`. **Žádné CSS animace ani přechody, časovače ani stav mezi snímky.** Snímky se musí dát vyrenderovat v libovolném pořadí.
- **Pružiny v uzavřeném tvaru** (step response). Hodnota, která během videa míří k více cílům, je **součet jedné pružiny na každou změnu**, takže zůstává čistou funkcí času (`twoclipping-5cba86`, `twoclipping-221cab`).
- **Náhoda jen se seedem**, `Math.random` je zakázané (`notdwd-7de38a`, šablona 3D). Hodnoty musí být v čase spojité, žádné `Math.floor` na pohybu. Jinak nefungují podsnímky ani poloviční snímky.
- **Tabulky klíčových snímků** `kf(t, [[t, hodnota], …], easing)` (`notdwd-7de38a`).
- **Všechny časy v jednom souboru (v dobách), všechny texty v druhém, ve scénách žádná „magická čísla“** (`antonio-kodheli-490109`: timeline.ts + copy.ts).
- **Jeden svět a jedna kamera**: transformace (x, y, zoom v **logaritmické** škále) na jednom kontejneru. Každý detail je pohyb kamery po tomtéž světě (`rossaxbt-94583b`, `ultimaxbt-2ddf1e`).
- **Sdílené prvky při předání scény**: plocha barvy nese kopii textu bubliny, tlačítko si nese popisek do stránky (`ultimaxbt-2ddf1e`).
- Před časováním **zamknout rozvržení**, protože změna výšky jedné sekce posune všechno za ní (`twoclipping-d89be5`).
- **Výchozí stavy nastavit už v t = 0** („seek-safe“) a **nikdy nezakrýt odchod** jiného prvku (`ik-builds-b8bdcf`).
- Materiály: `seek` je asynchronní a **čeká na dekódování obrázků**. Video se rozloží na **sekvenci JPEG** (30 fps) a obrázky se střídají po snímcích (`twoclipping-6dd14e`).
  Druhá cesta: kódovat všechny snímky jako klíčové (`ffmpeg -g 1`), načíst jako blob URL a čekat na `seeked` (`twoclipping-221cab`).
  **Text měřit až po načtení fontů** (`notdwd-7de38a`) a proměnné deklarovat před prvním voláním `seek()` (`ultimaxbt-2ddf1e`).

### 2.3 Rozmazání pohybem
| počet podsnímků | kde | poznámka |
|---|---|---|
| 3 | šablona showreel (rozložení neupřesňuje) | standard |
| 3, **vystředěné** (t − 1/240 s, t, t + 1/240 s při 60 fps = závěrka 180°) | `twoclipping-6dd14e` | vzorky kolem času snímku, ne dopředu |
| 3–5 „zdrženlivě“ | `brainextends-e19ac3` | statický text a artwork musí zůstat ostré |
| 4 | `twoclipping-221cab`, `twoclipping-5cba86` | |
| **8** | `ultimaxbt-2ddf1e`, `rossaxbt-3085b7` | „Four subframes leave ghost copies on fast moves, so render 8 and slow the move down.“ (stejné zjištění jako naše C003) |
| 16 přes 0,7 snímku | `twoclipping-d89be5` (WebGL, GPU) | |

K tomu **rozmazání v kódu podle rychlosti a směru**. Kruhové rozmazání přes CSS `filter: blur`, směrová šmouha přes SVG `feGaussianBlur` se zvlášť nastaveným x/y.
„Zoom smear“ na end card = 20–30 zvětšených, slábnoucích kopií slova (`notdwd-7de38a`). Každý záběr tam „přijíždí už v pohybu a odjíždí se zrychlením nebo s rozmazáním“.
Pozor: příliš silné rozmazání tvar úplně smaže. Když je snímek prázdný, rozmazání ubrat.

### 2.4 Zvuk v kódu a mix
- **Syntéza ve stránce** (šablona showreel): Web Audio `OfflineAudioContext` → WAV. Kick na každou dobu, riser do posledního celého taktu, úder na každou změnu scény.
  To přesně odpovídá našemu `--audio-z-kodu`. Syntetické SFX s přesnými časy má i `notdwd-7de38a`.
- **Stažené SFX** (Mixkit) na každou událost, „never synthesized“ (`twoclipping-221cab`). Každý zvuk se **umístí tak, aby jeho změřený vrchol, ne začátek souboru, padl na událost** (`twoclipping-6dd14e`).
  Dlouhé risery (často 4 s) zkrátit kolem vrcholu (`rossaxbt-3085b7`).
- **Hudba**: bez autorských práv, s jasným dropem. Rozebrat ji přes numpy (tempo, mřížka dob, energie taktů, drop) a mřížku **zkalibrovat na skutečné údery kicku** (`twoclipping-6dd14e`).
  Skladbu přizpůsobit na 120 BPM (`antonio-kodheli-490109`) nebo ji pustit 12 dob před dropem (`ultimaxbt-2ddf1e`).
- **Mix**: SFX tiše pod hudbou. **−14 LUFS** (8 promptů), true peak −1 dBTP (`notdwd-7de38a`), nebo −2 dBTP **změřené znovu po zakódování do AAC** (`ik-builds-b8bdcf`). Fade jen posledních 60 ms.
- **Hlas** (`rossaxbt-3085b7`, ElevenLabs): 4 celé verze najednou, jednotlivou větu přegenerovat 4× a vybrat. Pauzy delší než 0,28 s zkrátit na 0,2 s a úroveň frází srovnat.
  **Časy slov**: rozdělit nahrávku v pauzách ≥ 100 ms a každý úsek přepsat Whisperem zvlášť, protože jeden průchod Whisperu dá slova až o 0,5 s později.
  Ducking: třípásmový sidechain, hlas ~9 dB nad hudbou v pásmu 300 Hz–4 kHz. Hlas zdarma: edge-tts (`linearuncle-5d2bae`).
- **Licence**: jen hudba a SFX povolené pro komerční užití, zdroje zapsat (`ik-builds-b8bdcf`). Když bezpečná hudba není, dodat video bez hudby + seznam míst pro údery (cue sheet, `daniel-haida-8691d4`).

### 2.5 Mřížka dob (BPM)
- Nejčastěji **120 BPM**: doba 0,5 s, takt 2 s, 15 s ≈ 7,5 taktu. Dál 124 (`notdwd-7de38a`), 130 (`ultimaxbt-2ddf1e`), 115–120 „premium, not frantic“ (`daniel-haida-8691d4`).
- Místo slova „dynamic“ napsat tempo a počet taktů: „120 BPM, 7 bars, something happens on every beat“ (`twoclipping-5cba86`).
- Rozvržení ze šablony showreel: **1. takt háček → 1 technika na takt → poslední celý takt nejsilnější moment → poslední půltakt end title**, poslední snímek = první.
- Drop = největší změna (zaplavení barvou, tvrdé střihy). Tvrdý střih může doby předběhnout o 2 snímky (`notdwd-7de38a`), pak působí „na dobu“.
- **S hlasem se neřídí taktem, ale frázemi**: „Do not force the speech onto a dance beat.“ (`gdgtify-287ddf`). Změny scén padají na začátky frází a drop na klíčovou větu (`rossaxbt-3085b7`).
- Nová myšlenka každých 1,5–2 s, vizuální událost na každou dobu (`ik-builds-b8bdcf`).

### 2.6 Storyboard a kontrola
- **Před kódem**: storyboard se všemi časy na mřížce dob (`twoclipping-6dd14e`) nebo seznam stavů na mřížce (`twoclipping-5cba86`). Prompt Taxtello chce časy, klíčový obraz, logiku přechodu, text a emoční rytmus.
- **Před plným renderem**: 4 klíčové snímky ke schválení (`ultimaxbt-bbebf5`, `rossaxbt-94583b`, `twoclipping-221cab`, `notdwd-7de38a`), **1 snímek na dobu** (šablona showreel), ≥ 20 snímků (`twoclipping-6dd14e`),
  8 reprezentativních snímků (`gdgtify-287ddf`) nebo 10 pevných časů (`daniel-haida-8691d4`). Opravit nepořádek, překryvy, nečitelnost a cokoli mimo dobu.
- **Po renderu**: arch snímků **z dekódovaného MP4**, ne ze snímků prohlížeče (`daniel-haida-8691d4`). Dál vyhledat **jednosnímkové skoky** (rozdíl snímku ≥ 3× proti sousedům), zamrzlý čas, rychlé pohyby a hranici smyčky snímek po snímku.
  U kamery přes optical flow ověřit, že rychlost neklesá (`twoclipping-d89be5`), zkontrolovat poměr hlasu a hudby po frázích (`rossaxbt-3085b7`) a rovnoměrné časové značky snímků (`brainextends-e19ac3`).
- **Nezávislý kritik**: „have a fresh critic who didn't build it review the render“ (`antonio-kodheli-490109`). U nás je to agent kritik.
- **Sebekritika v promptu**: „Reject your own result if it feels like … a SaaS template“ (`daniel-haida-8691d4`), „question your strategy … start over“ (`heyiammallik-e72d17`).

### 2.7 Co už máme a co chybí (`nastroje/render_html.cjs`, `nastroje/vzory/scena.html`)
> **Stav po opravách režiséra (2026-10-30):** vyřešeno: vystředěné podsnímky + `--zaverka`, výchozí `--sub 4`, `will-change`, stavba po `fonts.ready`,
> překmit 3 % + `usazeni()`, `kf()`, `nahoda()`, `kamera()`, `rozmazani()`, `--nahled doby|casy`, loudnorm (`nastroje/master_zvuk.sh`),
> skoky a zamrznutí (`nastroje/kontrola.sh`). **Zbývá:** `doby.py` (rozbor hudby), `mix.py` (SFX podle vrcholu), ukázková `renderAudio()` ve scéně,
> sekvence JPEG pro video uvnitř scény. Doplnit, až to bude potřeba v prvním projektu.

| prvek | prompt-motion | u nás | co doplnit (konkrétně) |
|---|---|---|---|
| `seek(t)` → Playwright → ffmpeg, H.264 yuv420p faststart | standard | ✅ | – |
| asynchronní `seek` | čeká na obrázky | ✅ (`page.evaluate` čeká na Promise) | zmínit ve `scena.html` |
| fonty | měřit po načtení | ⚠️ renderer čeká na `document.fonts.ready`, ale `scena.html` volá `window.seek(0)` hned při načtení | stavbu scény a měření textu spouštět až po `document.fonts.ready` |
| podsnímky | **vystředěné**, závěrka ~180° | ⚠️ `(f + s/SUB)/FPS` = vzorky jen dopředu přes celý snímek (360°, obraz posunutý o ~⅓ snímku, silná šmouha) | parametr `--zaverka 0.5` a vystředění: `t = (f + ((s+0.5)/SUB − 0.5)·zaverka)/FPS` |
| počet podsnímků | 8 u rychlých pohybů | 3 výchozí, `--sub 6` (C003) | výchozí 4, u rychlých 8. Volitelně proměnný počet jen v rychlých úsecích (míchání v Node místo `tmix`) |
| směrové rozmazání | SVG blur x/y podle rychlosti | jen v instrukcích animátora | pomocná funkce `rozmazani(el, vx, vy)` do `scena.html` |
| pružina | uzavřený tvar, překmit „tiny“ / < 2 % | ✅ `pruzina(x, prekmit = 0.08)` | výchozí překmit **0,03**, přidat kriticky tlumenou variantu a „součet pružin“ pro více cílů |
| tabulky klíčových snímků, kamera | `kf()`, kamera (x, y, log zoom) | ❌ | pomocné funkce `kf()` a `kamera(t, klice)` |
| náhoda se seedem | povinné | jen pravidlo | funkce `nahoda(seed)` (mulberry32) |
| `will-change` | „Never put will-change on anything the camera scales“ (rozmazaný text) | ❌ `.prvek { will-change: transform, opacity, filter }` ve `scena.html` | odstranit z výchozí třídy |
| kontrolní snímky | 1 na dobu, pevné časy | ✅ `--nahled krok` + arch | `--casy 0,1.6,2.5` a `--bpm 120 --offset 0.05` (snímek na každou dobu) |
| zvuk z kódu | Web Audio → WAV | ✅ `--audio-z-kodu` (`window.renderAudio()`) | ukázková `renderAudio()` do `scena.html` (kick na dobu, riser, úder na scénu) |
| rozbor hudby | numpy: tempo, doby, drop | ❌ | `nastroje/doby.py` → JSON dob a dropu, který scéna načte |
| SFX podle vrcholu | ano | ❌ | `nastroje/mix.py`: seznam (čas, soubor, zesílení), zarovnání podle vrcholu, mix s hudbou |
| −14 LUFS / −1 dBTP | všude | ❌ v rendereru (dělá ho střihač) | `--loudnorm` (dva průchody), pak změřit znovu po AAC |
| skoky a zamrznutí | rozdíl snímků 3×, „frozen time“ | jen ruční kontrola kritikem | `ffmpeg … -vf signalstats` (YDIF po snímcích), `freezedetect`, `scdet` → skript pro kritika |
| video uvnitř scény | sekvence JPEG | – | Chromium v Playwrightu nejspíš neumí H.264 v `<video>` (proprietární kodeky, **ověřit**). Proto jako PM: sekvence JPEG |
| 60 fps | téměř všechny prompty | ✅ `--fps 60` | čas: ~8 s výpočtu na 1 s videa při 30 fps a 3 podsnímcích. 60 fps a 8 podsnímků ≈ 5× déle (15s video ≈ 10–12 min) |
| bezpečné zóny | jen „safe area“ (`antonio-kodheli-490109`) | ✅ `?mrizka` | – |
| storyboard, nezávislý kritik | ano | ✅ (`zadani.md`, agent kritik) | do storyboardu sloupec „takt / doba“ |

---

## 3. Anatomie silného promptu

Blog uvádí pět věcí, které rozhodují: **jeden koncept, seznam zakázaných efektů, časování na doby, metodu renderu a kontrolu.**
Nejlepší prompty (twoclipping, ultimaxbt, rossaxbt, notdwd, antonio_kodheli) k tomu mají jednotnou strukturu se značkami
`<inputs> <direction> <structure> <build> <gotchas> <start>`. Prompt Taxtello (`daniel-haida-8691d4`) je delší a psaný jako text, ale obsahuje totéž.

| část | co obsahuje | příklad formulace (zkráceno) |
|---|---|---|
| **Vstupy** (`<inputs>`) | co si má Claude vyžádat a **výchozí hodnoty**, když chybí | „If I skip anything, use 100, … and electric blue.“ (`rossaxbt-94583b`) |
| **Koncept / spojovací prvek** | jedna myšlenka, která dává každému záběru důvod | „One shape, never cut“ (`twoclipping-5cba86`) · „The orange dot connects every scene“ (`ultimaxbt-bbebf5`) · „CHAOS → CONTROL → CLARITY“ (`daniel-haida-8691d4`) |
| **Formát** | px, fps, délka, poměr | „1080×1080, targeting 60fps“ (`gdgtify-287ddf`). Jen ~5 promptů výslovně chce 9:16 |
| **Vzhled** | paleta v HEX **s rolemi**, jeden font (pojmenovaný), světlé/tmavé, materiál | „Taxtello's gold should feel like a precious accent, not a yellow UI flood.“ (`daniel-haida-8691d4`) |
| **Kamera** | jeden jazyk kamery | „One continuous camera … Never two camera moves at once.“ (`antonio-kodheli-490109`) · „never zoom in and out consecutively“ (`ultimaxbt-2ddf1e`) |
| **Pohyb** | easing, překmit, překrývání | „Springs everywhere, a tiny overshoot at most.“ (`twoclipping-5cba86`) · „overshoot below ~2%“, `cubic-bezier(0.16, 1, 0.3, 1)` (`daniel-haida-8691d4`) |
| **Rytmus** | BPM, takty, drop | „120 BPM, 7 bars, something happens on every beat.“ (`twoclipping-5cba86`) |
| **Struktura** | storyboard po taktech nebo časech, každá scéna jako proměna předchozí | „b13–16: the music drops. Three full-res reels … hard cuts“ (`antonio-kodheli-490109`) |
| **Text** | doslovné znění, zákaz vymýšlení | „EXACT WORDS, EXACT ORDER“ (`gdgtify-287ddf`) · „No invented results: no %, multipliers, customer names or figures.“ (`ik-builds-b8bdcf`) · „No full stops in on-screen text.“ (`twoclipping-6dd14e`) |
| **Zakázáno** | 5–9 položek + obecná pojistka | „…, anything that looks like a template.“ (7 promptů) |
| **Stavba** (`<build>`) | renderer, `seek(t)`, pružiny, materiály, podsnímky, zvuk, loudness | „Place each sound effect so its measured peak, not its file start, lands on the event.“ (`twoclipping-6dd14e`) |
| **Pasti** (`<gotchas>`) | známé technické chyby | „Text that swaps inside a morphing container needs its own enter and exit timing“ (`twoclipping-5cba86`) |
| **Kontrola** | snímky před renderem, sken po renderu | „Render one frame per beat before the full render. Fix anything off the grid, cramped or hard to read.“ (`twoclipping-5cba86`) |
| **Start / postup** | ptát se → storyboard → 4 snímky → render, nebo „bez otázek“ | „Ask me for the inputs, then show me the beat map and four stills … before building“ (`ultimaxbt-bbebf5`) |
| **Výstupy** | co přesně odevzdat | MP4, zdroj, plakátový snímek, arch, délka, použité materiály, kompromisy, příkazy k renderu (`daniel-haida-8691d4`) |
| **Poctivost** | co dělat, když něco nejde | „If you can't run code on my computer, tell me straight away…“ (`twoclipping-d89be5`) |
| **Měřítko kvality** | proti čemu se hodnotí | „I would rather have 3 extraordinary visual moments than 10 mediocre feature animations.“ (`daniel-haida-8691d4`) |

Další osvědčené formulace:
- Produkt: „Name what the product learns, never the abstraction.“ (`ik-builds-b8bdcf`). Screenshoty nepoužívat surové, „break them down into components/icons“ (`ho-ba-f3f0e9`). Do produktu přidat „only the motion“ (`bthreeagency-b9b8d9`).
- Úvod: „hook in the first second“ (`jhylee95-e1152f`, `reflex-cloud-72ffe5`). Prvních 1,5 s musí vypadat prémiově, první produktový moment do ~2 s, žádné 5sekundové logo intro (`daniel-haida-8691d4`).
- Výzkum: nejdřív nastudovat dřívější vizuální styl značky a najít vhodné fotky (`lexnlin-038035`). Pravdivé texty z webu citovat doslova (`antonio-kodheli-490109`).
- Vysvětlovací video: „from start to finish (empty glass to completed cocktail)“ (`ror-fly-9950f1`) dá videu strukturu ještě před prvním snímkem.
- Svislá verze: „Do not merely crop the desktop composition.“ (`daniel-haida-8691d4`).

---

## 4. AI poznávací znaky (zakázané efekty)

Seznam zakázaných efektů má podle blogu **16 z 230 promptů** od 12 autorů a můj sken dnešních dat našel také 16. Mezi 20 nejlajkovanějšími jsou 4 z nich a jejich medián je 56 lajků proti 7 v celé galerii.
Blog počítá výskyty takto: záře 7, „cokoli jako šablona“ 7, výbuchy částic 6, dlouhé zastavení / mrtvý čas 6, prolínačky 5, skákavý easing 3, gradienty 3, 3D efekty 3, stock záběry a UI kity 3, text v rozích 2, `Math.random` 2.
V tabulce je moje vlastní počítání ve všech 236 položkách včetně šablon. Smysl je vždy stejný: **efekt, který nic nevyjadřuje, prozradí, že video nikdo nenavrhoval.**

| znak | kolikrát zakázán | proč prozrazuje AI | kdy je v pořádku |
|---|---|---|---|
| **Záře / glow, neon** | 8 promptů úplně + 3 částečně (jen na UI textu, „NOT: neon“) + obě šablony („glows on everything“) | nejlevnější „bohatý“ vzhled, dekorace bez důvodu | když je sama konceptem: neonové logo (R5), záře kolem AI vstupu jako u Apple Intelligence (`ultimaxbt-2ddf1e`), záře wordmarku na černé end card (`notdwd-7de38a`, který zároveň zakazuje záři na UI textu), slabá záře za **jedním** zvýrazněným slovem (`rossaxbt-3085b7`), jemný ambientní bloom (`daniel-haida-8691d4`) |
| **Výbuchy částic** | 9 + šablona | výplň bez původu a cíle | když nesou význam: zlaté částice při odemčení odznaku (`bthreeagency-b9b8d9`), oslava úspěchu. Vždy vychází z objektu |
| **Prolínačka celých scén / „fades on everything“** | 9 + šablona | přechod, který nikdo nenavrhl | jednotlivý prvek smí najet eased fadem ≥ 0,3 s (`rossaxbt-3085b7`), cílený blur-dissolve (`notdwd-7de38a`) |
| **Mrtvý čas, zastavení > 0,5–1 s, zamrzlé snímky** | 9 + šablona (> 0,5 s) | 15s video působí pomalu | když je co číst. Záměrné ticho 400 ms (`gdgtify-287ddf`), držení end card 2 s (`rossaxbt-3085b7`), klid posledního snímku (`daniel-haida-8691d4`) |
| **„Cokoli, co vypadá jako šablona“** | 8 + obě šablony | obecná pojistka, efekty mimo seznam dostanou stejnou kontrolu | – (vždy na konec seznamu) |
| **Skákavý / pružný easing** | 8 + šablona | kreslený, levný dojem | pružina s malým překmitem (≤ 2–5 %), kriticky tlumené usazení |
| **Stock záběry, stock UI kity, výchozí materiály** | 6 + šablona 3D | generický vzhled | – (vlastní nebo skutečné materiály klienta) |
| **Gradienty** (generické, na UI, „AI fialová“, duhové) | 5 + šablona | typický AI vzhled | atmosférický gradient pozadí v barvách značky (`brainextends-e19ac3`), gradient na jednom zvýrazněném slově (`rossaxbt-3085b7`) |
| **Samoúčelné 3D** (otáčení karet, 3D flipy) | 4 | „pointless 3D spinning cards“ | když je 3D koncept (šablona 3D, průlet stránkou) |
| **Text a popisky v rozích, HUD, časový kód, vodoznak, počítadla** | 5 (`souravbhar871-61f424` = `1littlecoder-9fef89`, `brainextends-e19ac3`, `ik-builds-b8bdcf`, `lexnlin-038035` „eyebrow labels“) + šablona 3D („floating text labels“) | naznačuje detail, ale nenese informaci | – (informace patří do středu kompozice) |
| **Třes kamery** | 3 + šablona | laciná dynamika | – („pressure comes from the layout, not camera shake“, `gdgtify-287ddf`) |
| **Odlesky objektivu, shockwave kruhy, RGB split, mřížka podlahy, blikající pozadí, bílé záblesky** | 1–2 každý + šablona | „efekty z balíčku“ | krátký záblesk jako součást švihového přechodu (`notdwd-7de38a`) |
| **`Math.random` / nesemínkovaná náhoda** | 3 + šablona 3D | každý render jinak, opravený snímek se změní | – (seed) |
| **Kamera: neustálé zoomování, zoom tam a zpět, reset zoomu, dva pohyby naráz** | 6 | neklidná, nenavržená kamera | – |
| **Pohyb bez vazby na prvek na obrazovce, teleport objektu, náhodné přechody (wipe, spin, glitch, generický posun doleva, whip každé 2 s, zoom-blur)** | 4 | výplň | jeden whip jako akcent (`twoclipping-6dd14e`) |
| **Zvýrazňovací obdélník přesně za slovem** | 1 (`rossaxbt-3085b7`: „looks like a Windows text selection“) | vypadá jako označený text | tah zvýrazňovače přes frázi (`antonio-kodheli-490109`) |
| **Úder přesně na každou dobu („beat-snapped slams“)** | 1 | mechanické | – |
| **Každé slovo animované zvlášť** (u nadpisů) | 1 (`daniel-haida-8691d4`) | generické motion chování | titulky slovo po slově s hlasem |
| **Odborný animátorský žargon na obrazovce, vymyšlená čísla, parafrázované slogany, funkce, které produkt nemá** | 3 | nedůvěryhodné | – |
| **Béžový „artsy“ vzhled, „generic AI purple“, sklo (glassmorphism) všude, 20 různých stylů animace, odstavec marketingového textu** | 1–2 | AI estetika | liquid glass jako záměrný materiál jedné značky (`twoclipping-221cab`) |
| **Tečky na konci hesel na obrazovce** | 2 (`twoclipping-6dd14e`, `rossaxbt-3085b7`) | „slidový“ dojem | záměrná pointa |

**Jak psát vlastní seznam (blog):** začít běžnými znaky (záře, částice, prolínačky, skákavý easing, text v rozích), přidat, co se pokazilo v minulém běhu,
**ke každému zákazu napsat, co místo něj** („no crossfades: every scene grows out of the one before“), končit „anything that looks like a template“ a vejít se do jednoho řádku s 5–9 položkami.

---

## 5. Statistika katalogu

**Štítky obsahu** (položka může mít víc): product-ui 105 · kinetic-type 96 · music 50 · particles 43 · shapes 42 · charts 34 · diagrams 31 · characters 27 · photos 23 · phone 22 · code 21 · bez štítku 4.
Typy podle blogu: launch / promo 94, showreely 78, vysvětlovací videa 27.

**Formáty**
| poměr | počet | rozlišení |
|---|---|---|
| 16:9 | **192** (81 %) | 150× 1920×1080, 36× 1280×720, zbytek drobné odchylky (1920×1078, 854×480…) |
| **9:16** | **16** (7 %) | 11× 1080×1920, 5× 720×1280 |
| 1:1 | 14 | 1080, 1440, 720 |
| 4:5 / 5:4 | 2 / 2 | 1080×1350, 720×900 / 1440×1152 |
| jiné | 10 | 886×1920 (telefon ~9:19,5), 1920×816 (cinemascope), 1920×982 … |

Na výšku je celkem 19 položek (8 %). Galerie je tedy hlavně na šířku a **pro naši praxi 9:16 skoro všechno musíme přeskládat** (oddíl 6).
Formát v promptu uvádí jen 12 z 92 launch promptů, výslovně 9:16 asi 5 promptů (`ndhabarde11-f155b4` „in portrait mode“, `kloss-xyz-15182a`, `x4b47x-9cc84f`, `palashbagchi11-0a4b6b`, `daniel-haida-8691d4`).

**Effort**: neuvedeno 200, Max 22, High 7, Medium 7. Max je u showreelů na obou koncích žebříčku lajků, takže kvalitu prompt nezachrání. Šablony doporučují Max.

**Délky promptů** (231 textů): medián 151 znaků / **26 slov** (kvartily 18–37 slov), průměr 563 znaků. 18 promptů je v čínštině, japonštině nebo korejštině.
Rozložení: < 100 znaků 64 · 100–199 104 · 200–499 37 · 500–999 8 · 1 000–2 999 6 · ≥ 3 000 12. Nejdelší je Taxtello (15 306 znaků ≈ 2 082 slov).
Podle blogu mají prompty nad 100 slov (tehdy 19, v dnešních datech 22) medián 56 lajků, prompty do 26 slov 5.

**Požadovaná délka videa** (z textu promptů): 15 s jasně nejčastěji (~85×), 30 s 16×, 20 s 12×, 10 s 7×, 40 s 4×, 60 s 3×.

**Šablona showreel**: web k ní přiřadil 49 videí od 49 autorů. Doslovně nebo skoro doslovně ji použilo 30–33 promptů,
větu „incredible motion designer you are“ obsahuje 73 promptů a 86 začíná „make a dynamic …“.
Formáty showreelů: 34× 1920×1080, 12× 1280×720, **2× 1080×1920**, 1× 1080×1080. Štítky: kinetic-type 41, shapes 31, particles 19, music 16.

**Metody v textu promptů**: kontrola snímků 16 · BPM 14 · `seek(` 13 · pružiny 11 · canvas 11 · Playwright 12 · podsnímky / tmix 9 · Mixkit 9 · LUFS 8 · rozbor dob 8 · Remotion 5 · three.js 4 · HyperFrames 2 · Web Audio 0 (jen šablona).

**Autoři s více položkami**: twoclipping 4 (všechny patří k nejlepším strukturovaným promptům), sudo_kiran 4, ajith_io 4, LexnLin 3, KamStudioLabs 3.
**Popularita (blog)**: nejlajkovanější je jeden běh showreel promptu (17 023), pak Shape morphing (12 103), Engraving ad (1 344), Negroni (1 028), UGC promo (607), Dub (394), Manim derivace (258).

---

## 6. Doporučené prompty podle typu videa

**Obecný převod 16:9 / 1:1 → 9:16**
- Kompozici **přeskládat, ne oříznout**: vodorovné řady dát pod sebe, kamera jezdí svisle (scroll, jeřáb), ne do stran.
- **Telefon / mobilní UI na výšku vyplní celý obraz**, takže app videa jsou pro 9:16 ideální.
- Čtvercové prompty (1440×1440) umístit do středového čtverce 1080×1080 (y 420–1500). Horní a dolní pás zůstane pro háček a titulky, ale mimo bezpečné zóny A5.
- Souřadnice v px z promptu (`notdwd-7de38a`, `twoclipping-d89be5`) **přepočítat podle nové kompozice**, ne přeškálovat.
- Text je relativně větší (nadpis 110–160 px, 12–16 znaků na řádek). Česká slova jsou delší než anglická: rozvržení počítat podle nejdelšího řádku a celý blok (logo + název + štítek) zmenšit, aby se vešel (`notdwd-7de38a`).
- Fonty s **latin-ext** (č, ř, ů…). Geist, Inter, Anton, Caveat, Archivo i Instrument Serif ho na Google Fonts mají, ale vždy ověřit na snímku.
- Bez teček za hesly. Čísla jen ověřená.

### 6.1 Portfolio showreel (naše vlastní ukázka)
| položka | autor | proč | úpravy pro nás |
|---|---|---|---|
| [Šablona showreel](https://prompt-motion.com/templates/showreel) | Prompt Motion | jediná otestovaná verze se všemi pěti částmi. Na nic se neptá, Web Audio zvuk sedí na náš `--audio-z-kodu`, má 1 snímek na dobu | 1080×1920, koncept pojmenovat česky, end title = naše značka + CTA. Techniky (kinetický text, morf tvaru, 2D→3D, UI/data, end title) skládat svisle. Smyčka ×2–3 (R5) |
| [Orange dot motion system](https://prompt-motion.com/ultimaxbt-bbebf5) | @ultimaxbt | jeden prvek (tečka) projde všemi scénami: UI → písmeno → graf pružiny → tvar → end card. Zakazuje „motion not connected“, je to smyčka, mapa dob + 4 snímky | tečka = akcent značky. Slova přeložit nebo nahradit naším oborem, „+22 %“ jen se skutečným číslem. Halftone pole v 9:16 přetáhnout přes všechny rohy |
| [Reflex brand motion reel](https://prompt-motion.com/reflex-cloud-72ffe5) | @reflex_cloud | krátké, dobře formulované zadání značkového reelu: háček v 1. s, řada různých technik, čistý závěrečný snímek, střih „jako na hudbu“ | doplnit build a kontrolu z naší kostry (oddíl 10). Výhodné, když chceme volnost a máme málo času |

Doplňky: [Developer portfolio site showreel](https://prompt-motion.com/wani-shola-16ca7a) (@wani_shola) pro portfolio konkrétního člověka nebo webu:
skutečné stránky v rámečku prohlížeče a telefonu, „one idea per shot, key objects centred, space to breathe“, 120 BPM, střih na dobu.
Svislé showreely: `ndhabarde11-f155b4`, `jesscaroline7-1ff7cb`.
**Negativní vzor pro kritika**: [Deliberately terrible motion showreel](https://prompt-motion.com/henkpoley-3d3407) (@HenkPoley), kde Claude schválně dělá všechno špatně.

### 6.2 Logo animace / reveal
| položka | autor | proč | úpravy pro nás |
|---|---|---|---|
| [TypingMind logo reveal](https://prompt-motion.com/tdinh-me-815acb) | @tdinh_me | jednoduchý a silný koncept: pomalý přechod, který logo **poskládá** a teprve pak odhalí | logo jako SVG (rada `aschapmann-131210`: „trace the logo to SVG so it stays sharp and can be animated“). Výstupy 9:16, 1:1 a s průhledností. Smyčka 3–4 s ×3 (R5) |
| [Photo print app launch film](https://prompt-motion.com/twoclipping-221cab) (jen úvod a závěr) | @twoclipping | wordmark se jako harmonika smrskne do vlastní tečky, tečka se změní v pilulku a nakonec písmena vyskočí zpátky. Dokonalá smyčka loga. Technika: písmena se k tečce přibližují stejným poměrem a zužuje se osa `wdth` variabilního fontu | potřebuje variabilní font s osou šířky (Archivo) a latin-ext. Vybrat jen tuto sekvenci, 3–4 s |
| [Frame by Frame launch video](https://prompt-motion.com/notdwd-7de38a) (S7–S8) | @notdwd | end card: wordmark přiletí s vodorovnou zoom šmouhou (20–30 kopií), pomalu se zmenšuje ~1 px za snímek a zhroutí se do rozmazání. Záře je tu povolená, protože je to wordmark na černé | tabulky snímků přepočítat na 30/60 fps a střed 9:16. Logo disk místo FF značky |

Doplněk: [Taxtello](https://prompt-motion.com/daniel-haida-8691d4), úvod a závěr. Drobný zlatý záblesk odhalí značku, „machined precision“, „no generic logo fade“, na konci wordmark + jedna krátká věta. Vzor pro prémiové klienty.
Pro neonová loga podle R5 v katalogu přímý vzor není. Záře je u nich koncept (G2 v oddílu 9).

### 6.3 Kinetická typografie s hlasem
| položka | autor | proč | úpravy pro nás |
|---|---|---|---|
| [Ora 2 image model launch film](https://prompt-motion.com/rossaxbt-3085b7) | @rossaxbt | nejúplnější **hlasová** pipeline: scénář s pevnou strukturou, 4 verze hlasu, úprava pauz, časy slov přes Whisper po úsecích, titulky psané přesně s hlasem, drop na klíčovou větu, třípásmový ducking | ElevenLabs je placený, takže **jen po souhlasu uživatele**. Češtinu u modelu a hlasu ověřit, jinak edge-tts. Časy slov z `prepis.py --slova --model medium --jazyk cs`. 1440² → 1080×1920, titulky nad spodní zónou, žádný obdélník za slovem |
| [Speech built as architecture](https://prompt-motion.com/gdgtify-287ddf) | @Gdgtify | text **staví** kompozici (slova mají role nosníku, podpěry, podlahy), časuje se podle frází, ne podle taktu. Má 400 ms ticha, periodickou smyčku a kontrolu pořadí čtení | **9:16 se sem hodí přirozeně** (stavba roste vzhůru). České glyfy s háčky převést na cesty a zkontrolovat čitelnost při deformaci. Hlas volitelný |
| [Paper-style product launch film](https://prompt-motion.com/ik-builds-b8bdcf) | @ik_builds | obří kinetický text (Anton), ručně psané poznámky, které se kreslí (Caveat přes `stroke-dashoffset`, odpovídá našemu E5), nová myšlenka každých 1,5–2 s, zvuk na každý úder, přísná pravidla pro text (žádná vymyšlená čísla, žádný žargon) | HyperFrames + GSAP nahradit naším `seek(t)`. −14 LUFS / −2 dBTP po AAC ponechat |

Doplněk: [Synced lyrics motion video](https://prompt-motion.com/samaote-5e2fc2) (@samaote), krátký prompt na text písně synchronizovaný s vokálem.

### 6.4 Promo produktu / aplikace (UI)
| položka | autor | proč | úpravy pro nás |
|---|---|---|---|
| [Food craving launch film](https://prompt-motion.com/ultimaxbt-2ddf1e) | @ultimaxbt | celý příběh aplikace v telefonu v jednom záběru bez střihu: napsat požadavek → odeslat → „přemýšlí“ → drop (zaplavení barvou) → výsledky → objednat → logo. Mapa dob, SFX na každou událost, zaplavení přes rohy za ~0,35 s | **telefon na výšku = přirozeně 9:16**. Požadavek česky na pevných řádcích. Skutečné obrazovky klienta. Mixkit SFX jen s licencí. Duhová záře jen jako AI koncept |
| [Shape morphing through UI states](https://prompt-motion.com/twoclipping-5cba86) | @twoclipping (12 103 lajků; `demonugc-4c5753` má stejný text) | jeden tvar se bez střihu mění přes 12 UI stavů, pružiny s malým překmitem, kurzor, smyčka, mřížka dob | čtverec → střed 9:16. Stavy z aplikace klienta. Na mobilu místo kurzoru klepnutí prstem (kruh) |
| [Taxtello bookkeeping app film](https://prompt-motion.com/daniel-haida-8691d4) | @daniel_haida | vzor **zdrženlivosti a prémiovosti**: 19 pravidel, přechody přes objekty, jen skutečný produkt, kontrola v 10 časech, seznam výstupů. Navíc **lokalizovaný text** (německé fráze do 3–4 slov) = přímý vzor pro češtinu | 16:9 master → **u nás 9:16 jako master**. Barvy a fonty klienta. Fráze typu „Alles im Blick.“ psát česky stejně krátce (bez tečky, E8) |

Alternativy: [UGC ad generator promo](https://prompt-motion.com/twoclipping-6dd14e) (@twoclipping, 607 lajků) míchá skutečné **svislé klipy** s UI na mřížce 10 taktů a má nejlepší seznam zakázaných efektů. Hodí se pro hybrid střihu a motion grafiky.
[SaaS launch video](https://prompt-motion.com/aschapmann-131210) (@aschapmann) shrne celé launch zadání do jednoho odstavce: příběh trh → bolest → řešení → co dostanete, 4–5 scén, logo do SVG, kontrola snímků.

### 6.5 Vysvětlující / vzdělávací video
| položka | autor | proč | úpravy pro nás |
|---|---|---|---|
| [Negroni recipe animation](https://prompt-motion.com/ror-fly-9950f1) | @Ror_Fly (1 028 lajků) | **proces od začátku do konce** dá video s jasnou strukturou. Popisky a míry jsou tam, kde se děje akce | česky. Sklenice na výšku sedí do 9:16. Přidat háček-otázku (R4, C2) a kontrolu faktů |
| [Animated business explainer](https://prompt-motion.com/alex-prompter-1ea044) | @alex_prompter | šablona 5 scén: problém, co dělám, jak to funguje ve 3 krocích, jeden důkaz, jméno. Na 30 s vychází ~6 s na scénu (odpovídá našemu C2/C3) | doplnit hlas + titulky, bezpečné zóny, CTA klíčovým slovem (J1) |
| [Token bucket rate limiter](https://prompt-motion.com/parkerrex-1a54fe) | @ParkerRex | vysvětlení **mechanismu** (canvas, žádné knihovny, každý snímek čistá funkce času) | čtverec → 9:16. U technických témat určit publikum (blog) |

Doplněk: [Derivative concept explainer](https://prompt-motion.com/linearuncle-5d2bae) (@LinearUncle) = Manim + edge-tts pro matematiku.
Kontrolní seznam podle blogu: téma **a publikum**, posloupnost kroků, délka (~5 s na myšlenku), styl, **přesnost faktů** (žádný z 27 promptů ji nechtěl), zvuk.

### 6.6 Data a grafy
| položka | autor | proč | úpravy pro nás |
|---|---|---|---|
| [Taxtello](https://prompt-motion.com/daniel-haida-8691d4) (scéna Finanzcockpit) | @daniel_haida | hlavní číslo se ostře „usadí“, graf se nakreslí, vedlejší metriky dosednou později se zpožděním. Čísla v monospace, zelená jen pro skutečně kladný stav, **žádná vymyšlená data** | česká čísla (mezera jako oddělovač tisíců, čárka), ukázková data viditelně ukázková |
| [Orange dot motion system](https://prompt-motion.com/ultimaxbt-bbebf5) (scéna Spring) | @ultimaxbt | **graf je pohyb**: křivku kreslí stejná funkce, která hýbe tečkou | – |
| [Shape morphing through UI states](https://prompt-motion.com/twoclipping-5cba86) (záložky → graf) | @twoclipping | graf se otevře z UI prvku, sám se nakreslí a ukáže tooltip | – |

Krátké „datové“ prompty (`viktoroddy-98c1d8` milník návštěvnosti, `triglyceee-bd5b08` časová osa, `gigabit-million-16b3a0` přehled zpráv) jsou jen téma. Je potřeba k nim dopsat posloupnost.

### 6.7 Postavy a příběhy
| položka | autor | proč | úpravy pro nás |
|---|---|---|---|
| [Shadow theatre home story](https://prompt-motion.com/x4b47x-9cc84f) | @x4b47x | **nativně 9:16**, čistý JS, papírové stínové divadlo, jemný zvuk v kódu, téma jako otázka | české téma, 25–40 s (A4), háček textem |
| [Lighthouse keeper silent short](https://prompt-motion.com/kamstudiolabs-0b0824) | @KamStudioLabs | „sound tells half the story“: příběh bez dialogů | originál je 1920×816 → přeskládat. **Na sítích se kouká bez zvuku** (B5), takže klíčové momenty musí jít poznat i z obrazu |
| [Cycle of life animation](https://prompt-motion.com/loicrambo-ad6830) | @loicRambo | jedna postava od dětství po stáří a návrat na začátek = smyčka (D4) | 20 s, 9:16 |

Doplňky: [Sketchbook animals come alive](https://prompt-motion.com/abderrahmen-g-9e8ed0) oživuje kresby od uživatele.
[Scrabble tile character story](https://prompt-motion.com/anilraok-eff262) (9:16) je příběh, který nenápadně propaguje aplikaci.
[Recursion explained in genres](https://prompt-motion.com/emollick-8661a8): každé vysvětlení má jiný styl videa, takže koncept nahradí seznam scén.

### 6.8 Fotky (a natočený materiál)
| položka | autor | proč | úpravy pro nás |
|---|---|---|---|
| [Engraving-style Claude ad](https://prompt-motion.com/lexnlin-038035) | @LexnLin (1 344 lajků) | **nativně 1080×1920**. Postup: výzkum vizuálního stylu značky → směr → pravidla → nápady. Kreslí přes fotky, morfuje text, rychlé tempo, konec na logu. Zakazuje „beige artsy“ a „eyebrow labels“ | značka klienta, fotky s licencí, disclaimer u cizí značky (J5) |
| [Ora 2 image model launch film](https://prompt-motion.com/rossaxbt-3085b7) | @rossaxbt | koláž, fotky se střídají na šestnáctinové noty s klikem, 120 fotek se nakonec složí do loga, rozmazaná fotka za sklem | 1440² → 9:16 |
| [Photo print app launch film](https://prompt-motion.com/twoclipping-221cab) | @twoclipping (nejlajkovanější launch video) | skutečné fotky, liquid glass (přesný technický recept), clona z 6 lamel, přesvícení ze dne do zlaté hodinky (dvě srovnané fotky) | liquid glass na CPU je náročné na výpočet, proto zjednodušit |

Doplněk pro střihače: [Talking-head clip edit](https://prompt-motion.com/sab8a-364a5a) (@sab8a). Surový záznam mluvící hlavy sestříhat do svižné verze s titulky, grafikou a hudbou.

### 6.9 Všechny svislé položky (výška > šířka)
| slug | název | autor | rozměr | štítky | prompt | k čemu nám |
|---|---|---|---|---|---|---|
| `lexnlin-038035` | Engraving-style Claude ad | @LexnLin | 1080×1920 | kinetic-type, photos | 994 zn., strukturovaný | **nejlepší svislý prompt**, reklama s fotkami (6.8) |
| `x4b47x-9cc84f` | Shadow theatre home story | @x4b47x | 720×1280 | characters | 184 zn. | příběh, zvuk v kódu (6.7) |
| `anilraok-eff262` | Scrabble tile character story | @Anilraok | 1080×1920 | characters | 316 zn. | nenápadná propagace příběhem |
| `kloss-xyz-15182a` | Chaotic Claude POV video | @kloss_xyz | 1080×1920 | kinetic-type, code | 326 zn. | POV formát (R5), Python + ffmpeg, chaotický „brain rot“ styl |
| `gizakdag-cf4ae6` | Overthinking motion study | @gizakdag | 1080×1920 | kinetic-type | 201 zn. | kinetický text na abstraktní pojem podle přiložené grafiky |
| `ndhabarde11-f155b4` | Motion designer portrait showreel | @ndhabarde11 | 1080×1920 | kinetic-type, shapes, particles | showreel + „in portrait mode“ | nejjednodušší žádost o svislou verzi |
| `jesscaroline7-1ff7cb` | Ondefica app motion reel | @jesscaroline7 | 1080×1920 | product-ui, phone, charts, kinetic-type | showreel (Max) | app reel bez konkrétního zadání |
| `thilina-a-891c09` | sweetRegret app update reel | @thilina_a | 1080×1920 | product-ui, phone, characters | 176 zn. | nápad: **reel z novinek verze** (changelog) |
| `davidmarcus-a28a60` | Lightspark social promo video | @davidmarcus | 1080×1920 | kinetic-type, code | 127 zn. | „punchy … for social … production grade with sound“ |
| `micheleharmonic-77628e` | GravityDEX anime hype edit | @MicheleHarmonic | 1080×1920 | kinetic-type | 51 zn. | „hype edit“ (fan edit styl) |
| `mehul4795-4a7007` | ocrX app launch video | @mehul4795 | 1080×1920 | product-ui | 51 zn. | jen téma |
| `l3d1c-0e35a3` | PicTwin AI app ad | @l3d1c | 1080×1920 | product-ui, photos | 52 zn. | dvoukrokový postup: Claude nejdřív napíše prompt, pak video |
| `gautam-mer1-2ae354` | Matra caption app promo | @gautam_mer1 | 720×1280 | product-ui, phone, photos | 34 zn. | „Apple-style 30s“, jen téma |
| `gonzalomacagno-2de1a9` | Festival lineup promo reel | @GonzaloMacagno | 720×1280 | kinetic-type | 74 zn. (ES) | **pozvánka na akci / line-up** za 10 s |
| `kantamk-61f410` | Ball escaping twelve rings | @kantamk | 720×1280 | shapes, music | 33 zn. | „satisfying“ fyzikální smyčka (virální žánr) |
| `allforbigfire-86ff3c` | Anime robot combining sequence | @allforbigfire | 720×1280 | characters | 56 zn. (JA) | 3D anime transformace, pro nás okrajové |
| `francoxavier33-d2dfd2` | Parenting app hype video | @francoxavier33 | 886×1920 | product-ui, phone, kinetic-type | 44 zn. | poměr obrazovky telefonu, ne 9:16 |
| `marklaunches-3b9492` | Step race app promo | @marklaunches | 1080×1350 (4:5) | product-ui | 59 zn. | „make it emotional“ |
| `anas0ra-e57aea` | Shop chatbot mascot promo | @anas0ra | 720×900 (4:5) | characters | 46 zn. (FR) | maskot |

Svislé verze **na přání** mají i `palashbagchi11-0a4b6b` (jedna verze na šířku a jedna na výšku) a `daniel-haida-8691d4` (přeskládaná svislá varianta).

---

## 7. Skilly (všech 6)

Skilly jsou cizí kód. **Instalovat jen po souhlasu uživatele a po přečtení repozitáře.** Nic z nich zatím nemáme nainstalované.

| skill | autor / položka | k čemu je | instalace | repozitář |
|---|---|---|---|---|
| **html-demo** | @MengTo · `mengto-a7f4679` | živé HTML demo produktu: okno aplikace ve stylu Macu přehrává aplikaci krok za krokem, vše z jednoho času (smyčka, posun, skok na krok, zastavení) | `npx skills add MengTo/Skills --skill html-demo` | github.com/MengTo/Skills/tree/main/agent-skills/web-design/html-demo |
| **design-taste-frontend** (TasteSkill) | @LexnLin · `lexnlin-f9b3bd8` | výtvarné vedení pro kódující agenty: skutečné obrázky a kontroly v prohlížeči pro weby, dashboardy a obrazovky aplikací | `npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"` | github.com/Leonxlnx/taste-skill |
| **cinetic** | @LexnLin · `lexnlin-6161a6` | agent vymyslí koncept, značku a hudbu a z kódu vyrenderuje krátký filmový launch nebo motion klip | `npx skills add Leonxlnx/cinetic` | github.com/Leonxlnx/cinetic |
| **product-film** | @anthonyriera · `anthonyriera-9b1b2a` | naučí se design systém produktu, vyzpovídá zadavatele a postaví launch video v **Remotionu** ze skutečných komponent, loga a hudby | `/plugin marketplace add Rieranthony/product-film-skill` a pak `/plugin install product-film@product-film-skill` | github.com/Rieranthony/product-film-skill |
| **session-story** | @jake11moran · `jake11moran-a269c4` | přečte **lokální historii Claude Code** a udělá z typické session krátký animovaný film s hudbou v HyperFrames (pozor na soukromí) | `npx skills add heygen-com/hyperframes-community-skills --skill session-story` | github.com/heygen-com/hyperframes-community-skills/tree/master/skills/session-story |
| **generative-film-skill** | @BuildFastWithAI · `buildfastwithai-53234e` | animované MP4 na libovolné téma, každý snímek z kódu, syntetizovaná hudba sladěná s dobami | `npx skills@latest add https://github.com/buildfastwithai/buildfast-skills` | github.com/buildfastwithai/buildfast-skills/tree/main/generative-film-skill |

Pro nás jsou nejzajímavější **cinetic** a **generative-film-skill** (stejný princip jako náš renderer, mohou mít hotové postupy), dál **product-film** u klientů s Reactem
a **html-demo** pro ukázky aplikací ve smyčce.

---

## 8. Šablony a blog: hlavní poučení

**Šablony (`templates`)**: „každá část, kterou bys měnil, je pole“. Každá šablona byla spuštěná a video na webu je výsledek bez úprav.
Web ohlašuje další šablony: explainer, product film a short film. **Při aktualizaci katalogu je hlídat.**

**Šablona showreel** (přepis nejpoužívanějšího promptu): úplná osnova `<direction> <structure> <build> <start>`.
Koncept se pojmenuje jednou větou a každý záběr vzniká z předchozího. Jeden font, max 3 barvy + černá/bílá, jeden jazyk kamery.
Rozsah technik má mít každá stejný čas: kinetický text, morf tvaru, 2D→3D, data/UI, end title. Zakazuje i zastavení delší než 0,5 s.
Doby 120 BPM, zvuk z Web Audio, 60 fps, 3 podsnímky, 1 snímek na dobu před renderem. Start: koncept + storyboard, pak stavět bez otázek. Doporučený effort Max.
→ **Nejbližší vzor naší kostry.**

**Šablona 3D (realtime)**: three.js v jednom HTML. Nejdřív se navrhne **„signature shot“** a všechno k němu směřuje.
Filmová kamera s jedním pojmenovaným pohybem na záběr (dolly, jeřáb, orbit, nájezd, přeostření), ne orbit controls. Kamera nikdy neprojede geometrií.
Světla klíč + výplň + kontra, mapa prostředí, PBR materiály, ACES. Věci na sebe reagují (pružiny, jednoduchá fyzika).
Zakazuje výchozí materiály, plovoucí popisky, „spinning object as the whole idea“ a vzhled tech dema. Režim `?render` se seedem.
Pasti: shadow bias, úzké near/far roviny, seedovat náhodu. Stojí na ní 5 položek (`nft-chen-5f8bb0`, `mandelduck-95fd08`, `gorden-sun-041f56`, @BuildFastWithAI (nejspíš `buildfastwithai-ed9447`, web to neupřesňuje), `allforbigfire-86ff3c`).
→ Pro nás jen jednoduché 3D, protože nemáme GPU.

**Customize**: doplnění promptu v prohlížeči (účel, formát, barvy). Seznam „Most liked prompts“ je náhrada žebříčku popularity. Vede ho showreel (@stephanlivera), Shape morphing, Bold kinetic type, Abstract reel, Photo print app a Landing page 3D scroll.

**Blog: Remotion vs HyperFrames vs HTML**: všechny tři renderují stejně (prohlížeč → čas → snímek → ffmpeg).
HTML je nejjednodušší, ale metodu musí popsat prompt. Remotion se hodí pro React produkty a launch videa (pozor na licenci). HyperFrames = HTML s data atributy a GSAP, Apache 2.0.
three.js jen pro skutečné 3D, Manim pro matematiku. **Nástroj vždy jmenovat v promptu.**

**Blog: Proč AI motion grafika vypadá jako AI**: viz oddíl 4. Nejlepší pravidlo: „motion that isn't connected to an element already on screen“ je zakázaný.
Prolínačku nahradit nápadem (jeden prvek, který spojuje scény), pružiny omezit, ne zakázat. Mrtvý čas je v pořádku jen tehdy, když je co číst. `Math.random` je chyba stavby, ne vzhledu.

**Blog: Co ukazuje 230 promptů**: 33 běhů stejného promptu skončilo 0–17 023 lajky a medián je 5. Effort Max výsledek nezachránil.
Rozhoduje 5 částí: koncept, zakázané efekty, doby, metoda, kontrola. Délka promptu není cíl, každá věta v něm má rozhodovat.

**Blog: Launch video (92 promptů)**: čtvrtina launch promptů jen recykluje showreel prompt (medián 8 lajků), takže produkt je kulisa.
Dobrý launch prompt obsahuje produkt + slib jednou větou, **3–5 konkrétních momentů** v pořadí, vzhled (HEX, font, světlé/tmavé), načasování (délka, tempo, změna na každou dobu), zakázané efekty a konec (logo, URL, věta).
Blok `<inputs>` dělá prompt opakovaně použitelný. **Formát napsat výslovně: „9:16 vertical“ + px.**

**Blog: Explainer (27 promptů)**: nejkratší prompty v galerii (medián 15 slov). Funguje **proces se začátkem a koncem** nebo **seznam scén**.
Chybí v nich publikum (2 z 27), zvuk (6) a **kontrola faktů (0)**. Doporučená věta: „Research it first and keep every fact right; never invent numbers or quotes.“
Na jednu myšlenku počítat ~5 s.

---

## 9. Rozpory s našimi pravidly a návrhy úprav

| pravidlo | dnes | co říká prompt-motion | návrh nového znění |
|---|---|---|---|
| **G2** | tmavé pozadí + neonový akcent + **záře = prémiový tech dojem** [R2, R4, R5] | záře je nejčastější AI znak (zakázaná v 9 promptech a v obou šablonách). Prémiovost dělá zdrženlivost („NOT: neon“, Taxtello) | **G2** Tmavé pozadí + jeden akcent působí prémiově. **Záře jen tam, kde je sama konceptem nebo zdrojem světla**: neonové logo / nápis (R5), jeden zvýrazněný prvek nebo wordmark na end card, „AI záře“ kolem vstupu. Nikdy na UI textu ani titulcích a nikdy jako dekorace všeho. `[R2, R4, R5, PM]` |
| **F4** | UI pružina s „malým překmitem“ [R1, R4]; `scena.html` má výchozí 8 % | „a tiny overshoot at most“, „below ~2%“, „no cartoon springiness“, kriticky tlumené usazení | **F4** UI prvky (tlačítka, karty, notifikace, pop loga) → pružina s překmitem **2–5 % (výchozí 3 %)**, jednou, bez houpání. Velké plochy, kamera, text a usazování → kriticky tlumené (bez překmitu). Výraznější překmit jen u hravých videí a postav. `[R1, R4, PM]` (+ v `scena.html` změnit výchozí `prekmit` na 0,03) |
| **B3** | statický nadpis nahoře po celou dobu videa [R1, R2, R5] | zakazuje text v rozích, „outer caption, creator watermark, decorative footer“, „headers“ | **B3** Statický nadpis nahoře patří k formátu „natočená obrazovka“ a POV/meme (R1, R2, R5): jedna věta, která nese háček, pod horní bezpečnou zónou. **Do čistých motion videí (showreel, logo, produktový film) ho nevkládat.** Vždy dodat i čistou verzi a nadpis přidávat až ve střihu jako samostatnou vrstvu. Nikdy drobné popisky, štítky ani „HUD“ v rozích. `[R1, R2, R5, PM]` |
| **C6** | end card smí být dlouhý (R3 ~10 s) | zastavení > 0,5–1 s = mrtvý čas. Ale držení end card 2 s a „final frame must have enough stillness“ jsou v pořádku | **C6** Konec = end card (logo, podpis, @jméno, CTA). Drží **1,5–3 s**, ve smyčce stačí 1–1,5 s. Během držení jemný pohyb (dotlačení 2–4 %), žádný zamrzlý obraz. Dlouhý podpis (~10 s, R3) jen u konceptů, kde end card nese text nebo manifest. `[R1, R3, R4, PM]` |
| **C7** | nová informace nebo vizuální změna každé ~1–2 s | „something happens on every beat“ (0,5 s při 120 BPM), nová myšlenka každých 1,5–2 s | **C7** Nová **myšlenka** každých ~1,5–2 s, drobná vizuální **událost** na každou dobu. V emoční pointě tempo zpomalit (jediné záměrné ticho ~0,4 s). `[R2, R3, PM]` |
| **D2** | přechody pohybem, mimo jiné „diagonální světelná šmouha“ [R1–R3] | další scéna vzniká z předchozí. Zakázány prolínačky, odlesky, záblesky, glitch, náhodné wipy, whip každé 2 s | **D2** Přechody tak, že **další scéna vzniká z předchozí**: sdílený prvek (tlačítko se rozroste do stránky, tečka se změní v logo), morf tvaru, zaplavení barvou z objektu (přes všechny rohy, ~0,3 s), match cut, souvislá kamera nebo zoom skrz objekt. **Whip a světelná šmouha nanejvýš 1× za video** jako akcent. Nikdy prolínačka celých scén, náhodný wipe, spin ani glitch. `[R1, R2, R3, PM]` |
| **D5** | rozmazání u každého rychlého pohybu [R2, R3] | podsnímky vystředěné. 4 nestačí („ghost copies“), u rychlých pohybů 8. Směrová šmouha. Statický text ostrý | **D5** Rozmazání pohybem: (1) v kódu podle rychlosti a směru (svislý švih = svislá šmouha), (2) render s podsnímky: **3–4 u běžného pohybu, 6–8 u rychlých přechodů** (méně dělá „duchy“, C003). Statický text a UI zůstávají ostré a rozmazání nesmí tvar úplně smazat. `[R2, R3, PM]` |
| **E1** | kinetický text slovo po slově synchronně s hlasem [R2, R4] | s hlasem ano, slova psaná přesně podle hlasu (časy z Whisperu po úsecích). U nadpisů „avoid … every word animates independently“ | **E1** Slovo po slově **jen tam, kde text čte hlas** (titulky, háček). Slovo naskočí přesně s hlasem (`prepis.py --slova`, při nepřesnosti zarovnat po frázích). **Nadpisy a hesla bez hlasu se hýbou jako jeden navržený objekt** (maska, roztažení, morf). `[R2, R4, PM]` |
| **E2** | klíčové slovo: **barevný štítek pod slovem** [R4] | „A highlight box behind a word looks like a Windows text selection.“ Zakázané „selection-box highlights“. Povolený tah zvýrazňovače | **E2** Klíčové slovo zvýraznit barvou, řezem nebo velikostí. Štítek jen jako **navržený** prvek: zaoblená pilulka s vnitřním okrajem, která přijede pružinou, nebo tah zvýrazňovače přes frázi. **Nikdy ostrý obdélník přesně za písmeny.** `[R2, R3, R4, PM]` |
| **A1** | 30 fps, 60 fps jen pro UI a rychlý pohyb [R1–R5, R4] | téměř všechny animace z kódu jsou 60 fps | **A1** Výchozí 1080×1920 (9:16). **Animace z kódu 60 fps**, natočený materiál v nativních fps (obvykle 30). 30 fps u animace jen tam, kde to šetří čas renderu a pohyb je pomalý. `[R1–R5, PM]` |
| **I2** | hudba cca 15–20 dB pod hlasem [obecné] | hlas ~**9 dB** nad hudbou v pásmu 300 Hz–4 kHz, třípásmový ducking (`rossaxbt-3085b7`) | **I2** Hudba pod hlasem s duckingem (ztlumení jen během řeči). Cíl: hlas **≈ 9–12 dB nad hudbou v pásmu řeči 300 Hz–4 kHz**, zkontrolovat po frázích. Paušálních 15–20 dB jen u husté, hlasité hudby. `[PM, obecné]`, ověřit na prvním videu s hlasem |
| **I3** | SFX jemně, ne na každý pohyb [obecné] | SFX na **každou událost** („one soft sound effect for every element that appears and silence otherwise“), umístěné podle změřeného vrcholu, tiše pod hudbou. U prémiových značek zdrženlivě | **I3** SFX na každou **událost** v obraze (klik, dopad, pop, otevření, logo), ne na každý pohyb. Umístit tak, aby **změřený vrchol** zvuku padl na událost, dlouhé risery zkrátit kolem vrcholu. Pod hudbou tiše, jinak ticho. U prémiových značek jemné kliky, tónový „tick“ a měkký dopad na logo, žádné hlasité whooshe všude. `[PM]` |
| **F6** | text pro animace v kódu: „Entrances: ease out. Exits: ease in. Interface: spring, slight overshoot. Nothing linear.“ [R4] | doplňuje uzavřené pružiny, čistou funkci času a rozmazání podle rychlosti | **F6** … + „Springs are closed-form, tiny overshoot. Every frame is a pure function of time. Blur follows speed and direction.“ `[R4, PM]` |
| **K** | kontrolní seznam | snímek na každou dobu, skoky o 1 snímek, zamrznutí, hranice smyčky, AI znaky, fakta, LUFS po AAC | **K** přidat: ☐ snímek na každou dobu nebo 4 klíčové snímky před plným renderem · ☐ žádný jednosnímkový skok (YDIF) ani zamrzlý úsek · ☐ hranice smyčky snímek po snímku · ☐ žádný AI znak z `prompt-motion/poznatky.md` oddíl 4 bez důvodu v zadání · ☐ čísla a fakta ověřená · ☐ LUFS a true peak změřené po zakódování do AAC `[PM]` |

**Nová pravidla (návrh)**
- **A7** Předlohu 16:9 nebo 1:1 pro 9:16 **přeskládat, ne oříznout**: řady pod sebe, kamera svisle, souřadnice přepočítat. `[PM]`
- **B6** **Snímek 0 je hotový, silný obraz** (slouží jako náhled): žádné zatmívání z černé ani logo intro. První obsahový nebo produktový moment do ~2 s. `[PM]`
- **C8** **Fakta a čísla nevymýšlet** (procenta, jména zákazníků, výsledky). Čísla jen ověřená od uživatele, jinak zjevně ukázková. Texty značky citovat doslova. `[PM]`
- **D6** **Žádný pohyb bez příčiny**: každá animace vychází z prvku, který už je na obrazovce, nebo do něj vede. Objekty se nepřesouvají skokem a cesta každého předání je vidět. Odcházející text zmizí dřív, než příchozí obsadí jeho místo. `[PM]`
- **E8** Krátká hesla a titulky **bez tečky na konci**. Tečka jen jako záměrná pointa. `[PM]`
- **F7** **Jeden jazyk kamery**: jeden svět, jedna kamera (posun + zoom v logaritmické škále). Nikdy dva pohyby kamery naráz, nikdy zoom tam a hned zpátky. Kamera se mezi scénami neresetuje (další scéna začíná na zoomu, kde skončila předchozí). Pomalé dotlačení během scény (1,00 → 1,04) drží obraz živý. `[PM]`
- **G6** **AI poznávací znaky** (oddíl 4 tohoto souboru) jsou ve výchozím stavu zakázané. Výjimku musí zdůvodnit koncept a zapisuje se do zadání. `[PM]`
- **I5** Hudba a SFX jen s **licencí pro komerční použití**, zdroje zapsat do zadání. Když bezpečná hudba není, dodat video bez hudby + seznam míst pro údery. `[PM]`

---

## 10. Náš hlavní prompt (kostra zadání pro animátora, 9:16)

Vlastní šablona. Strukturu má z nejlepších promptů katalogu, obsah tvoří naše pravidla. Režisér vyplní `{…}` a pošle animátorovi spolu s `zadani.md`.
Když prompt půjde do externího modelu, přeložit ho do angličtiny a značky ponechat.

```
<vstupy>
Před prací ověř, že máš (co chybí, nahlas režisérovi, nehádej):
- typ videa a cíl jednou větou: {např. „promo aplikace X: divák pochopí, že objednávku vyřídí za 10 s“}
- značka: název {…}, logo {cesta k SVG}, barvy s rolemi {pozadí #…, text #…, akcent #…}, font {…} (latin-ext)
- obsah v pořadí: {3–5 momentů / obrazovek / kroků} | text hlasu doslova: {…}
- zvuk: {hudba: soubor + licence + BPM + čas dropu} | {zvuk z kódu} | {bez hudby, verze pro trend zvuk}
- jazyk na obrazovce: čeština s diakritikou {+ EN verze ano/ne}
- konec: {logo + CTA „Napiš do komentáře …“ / @jméno / web}
Když něco chybí a režisér to dovolí, použij: {výchozí hodnoty}.
</vstupy>

<smer>
Koncept: {jedna věta} se spojovacím prvkem {např. akcentní tečka / jeden tvar / jedna karta}, který projde všemi scénami.
Každá scéna vzniká z té předchozí (sdílený prvek, morf, zaplavení barvou, match cut). Prolínačky ne.
Formát: 1080×1920, 9:16, {60} fps, {délka} s. Komponováno na výšku od prvního snímku, žádný ořez 16:9.
Bezpečné zóny: důležitý text ne do horních 250 px, spodních 400 px a pravých 120 px.
Vzhled: max 3 barvy + černá/bílá. {font}, max 2 řezy {+ ruční písmo na anotace}. Hlavní nadpis ≥ {110} px, titulky ≥ {56} px.
Kamera: jeden svět a jedna kamera, nikdy dva pohyby naráz, žádný zoom tam a zpět, mezi scénami žádný reset. Během scény pomalé dotlačení 1,00 → 1,04.
Pohyb: příchod ease-out, odchod ease-in, UI pružina s překmitem max 3 %. Velké plochy, kamera a text bez překmitu. Nic lineárně.
Prvky se rozjíždějí s mírným zpožděním. Odcházející text zmizí dřív, než příchozí obsadí jeho místo.
Text: krátký, doslova {…}, hesla bez tečky. Žádná vymyšlená čísla, jména ani výsledky.
Zakázáno: záře, výbuchy částic, odlesky, třes kamery, RGB split, prolínačky scén, generické gradienty,
skákavý easing, text a popisky v rozích, zastavení > 1 s bez textu ke čtení, pohyb, který nevychází
z prvku na obrazovce, cokoli, co vypadá jako šablona. {Výjimka podle konceptu, např. „záře jen na neonovém logu“.}
</smer>

<struktura>
Rytmus: {BPM} BPM (doba {60/BPM} s, takt {240/BPM} s), drop v {čas} | řízeno hlasem po frázích (změny na začátcích frází, drop na klíčovou větu).
Snímek 0: hotový silný obraz (bude náhledem). Háček do 1 s: {obraz + text}.
Takt 1 ({0–…} s): háček {…}
Takty 2–{n}: jedna myšlenka na takt, každá vzniká z předchozí, drobná událost na každou dobu:
  {takt 2: …}
  {takt 3: …}
Drop / pointa ({takt}): nejsilnější moment {…}
End card ({čas–konec}): {logo + CTA}, drží {1,5–3} s s jemným dotlačením. Smyčka: poslední snímek = první {ano/ne}.
</struktura>

<stavba>
1. Kopie `nastroje/vzory/scena.html`, 1080×1920. Vše se počítá z času ve `window.seek(t)`: žádné CSS animace
   ani přechody, časovače, requestAnimationFrame ani stav mezi snímky, náhoda jen se seedem. Hodnoty spojité v čase.
2. Nahoře jeden objekt s časy všech událostí (v dobách) a jeden se všemi texty. Ve scénách žádná magická čísla.
3. Pružiny v uzavřeném tvaru. Hodnota s více cíli = součet pružin. Kamera = jedna transformace (x, y, log zoom).
4. Rychlé pohyby: rozmazání v kódu podle rychlosti a směru + podsnímky při renderu.
5. Fonty a obrázky měřit až po načtení. Video vložit jako sekvenci JPEG, seek čeká na dekódování.
6. Zvuk: {window.renderAudio() z Web Audio: kick na dobu, riser do posledního taktu, úder na změnu scény}
   | {hudba + SFX na každou událost, umístěné podle změřeného vrcholu, tiše pod hudbou}.
   Mix −14 LUFS integrated, true peak ≤ −1 dBTP, změřit znovu po zakódování do AAC.
7. Render: node nastroje/render_html.cjs --html … --out … --dur {N} --fps {60} --sub {4|8} {--audio-z-kodu | --audio …}
</stavba>

<pasti>
- will-change nikdy na prvky, které kamera škáluje (rozmazaný text).
- Plocha, která zaplaví obraz, přesáhne všechny 4 rohy a trvá ~0,3 s, jinak to vypadá jako záblesk.
- Text měněný uvnitř měnícího se tvaru má vlastní masku a časování, jinak se překryje.
- Česká slova jsou delší: rozvržení podle nejdelšího řádku, nezalamovat během pohybu, blok případně zmenšit celý.
- Bílý prvek na bílém pozadí zmizí: přidat 1px okraj nebo jemný stín.
- Smyčka: poslední snímek totožný s prvním včetně polohy a rychlosti prvků.
- {pasti specifické pro projekt z vybraného promptu prompt-motion}
</pasti>

<kontrola>
Před kódem: koncept jednou větou + storyboard po taktech (čas, obraz, text, zvuk) → schválí režisér.
Před plným renderem: snímek na každou dobu (nebo --nahled 0.5) + 4 klíčové snímky v plném rozlišení
({háček, drop, pointa, end card}). Opravit nepořádek, překryvy, text v bezpečných zónách, nečitelnost a cokoli mimo dobu.
Po renderu: arch z dekódovaného MP4, jednosnímkové skoky, zamrzlé úseky, rychlé pohyby snímek
po snímku, hranice smyčky, délka, fps, LUFS a true peak. Pak nezávislý kritik.
Odmítni vlastní výsledek, když působí jako šablona, PowerPoint, záznam obrazovky nebo přehlídka efektů.
Raději 3 výjimečné momenty než 10 průměrných.
</kontrola>

<vystup>
MP4 1080×1920 {+ verze bez hudby} {+ verze bez statického nadpisu}, zdrojový HTML, plakátový snímek, kontrolní arch,
přesná délka, seznam zdrojů obrazu a zvuku s licencí, příkaz k reprodukci renderu, známé kompromisy.
</vystup>

<start>
Nejdřív koncept jednou větou a storyboard po taktech. Po schválení stav bez dalších otázek.
</start>
```

**Rychlá verze** (když je zadání malé, podle blogu o launch videích), 6 řádků:
produkt a slib jednou větou · 3–5 momentů v pořadí · vzhled (HEX, font, světlé/tmavé) · načasování (délka, BPM, změna na každou dobu) ·
zakázané efekty (záře, částice, prolínačky, skákavý easing, text v rozích, „anything that looks like a template“) · konec (logo, CTA). K tomu vždy řádek „1080×1920 9:16“ a odkaz na `<stavba>` a `<kontrola>` výše.

---

## 11. SaaS motion [V003]

Uživatel (V002 → V003): „SaaS motion, který je velice populární“ + realistický produkt. Rozbor 2026-11-01 pro BMW řady 7 (`projekty/003-bmw-rada7/zadani.md`,
oddíl Zvolené motiony). Ukázková videa vybraných položek prohlédnutá po 12 snímcích (lokálně `media/prompt-motion/videa_v003/arch_*.jpg`).

**Co to je**: styl launch videí softwarových firem (Apple keynote, Linear, Stripe, Screen Studio). Produkt je hrdina, kolem něj čisté UI prvky
(karty, pilulky, přepínače, posuvníky, kurzor), které se **mění jeden v druhý**, kamera plynule přibližuje a typografie je krátká a sebevědomá.
V katalogu je to největší skupina: štítek product-ui má 105 položek, launch / promo 94. Ve „Most liked“ jsou 3 ze 6 SaaS položky
(Shape morphing 12 103 lajků, Photo print app, Landing page 3D scroll).

**Lajky**: web je u položek neukazuje, blog cituje jen pár čísel. Nejpopulárnější SaaS vzory podle blogu a „Most liked“:
`twoclipping-5cba86` (12 103) · `twoclipping-221cab` (nejlajkovanější launch video) · `twoclipping-d89be5` (6. v „Most liked“) · `twoclipping-6dd14e` (607).

**Nejlepší položky pro SaaS motion s realistickým produktem** (podrobně v zadání V003, M1–M7):
| položka | role | hlavní technika |
|---|---|---|
| [Shape morphing through UI states](https://prompt-motion.com/twoclipping-5cba86) | přechody | jeden prvek se mění přes stavy UI, dvě hrany ukazatele na dvou pružinách, kurzor řídí změny |
| [Spotify product film](https://prompt-motion.com/brainextends-e19ac3) | ukázka produktu | zaoblená scéna, trvalá lišta jako spojka záběrů, identita hrdinského obrazu přes všechna předání, sbíhání do loga |
| [Photo print app launch film](https://prompt-motion.com/twoclipping-221cab) | luxus, přechody | přesvícení posuvníkem mezi dvěma zarovnanými snímky, zaplavení tvarem přes rohy, clona ze 6 lamel, skutečné fotky + UI |
| [White ball UI motion loop](https://prompt-motion.com/rossaxbt-94583b) | výkon, čísla | posuvník s bublinou, číslo z polohy knobu, karty na doby, jeden svět a jedna kamera |
| [Frame by Frame launch video](https://prompt-motion.com/notdwd-7de38a) | UI řemeslo | záběry přijíždějí už v pohybu, kurzor jako postava (natočení, hover, stisk), skleněná karta vyskočí z prvku |
| [Taxtello bookkeeping app film](https://prompt-motion.com/daniel-haida-8691d4) | prémiovost | kamera jako makro produktové natáčení, překmit < 2 %, glint jako drahý akcent, zdrženlivost |
| [TypingMind logo reveal](https://prompt-motion.com/tdinh-me-815acb) | end card | logo se nejdřív poskládá (kontura → díly), teprve pak odhalí |
| [Landing page 3D scroll](https://prompt-motion.com/twoclipping-d89be5) | (záloha) | 2,5D: díly stránky se zvednou a postaví k objektivu, mělká hloubka ostrosti; chce WebGL a GPU, u nás jen zjednodušeně |

### 11.1 Průvodce stylem SaaS motion
1. **Pozadí**: světlé, teplé nebo neutrální, jednolité (`#F6F6F6`, studio z rendrů `#E7E2DC`), případně velmi jemná vinětace. Tmavé jen jako záměrná
   část (noc, výkon). Žádné tečkové mřížky, „AI fialová“ ani generické gradienty (`twoclipping-5cba86`, `brainextends-e19ac3`).
2. **Karty**: bílé nebo světle šedé, rádius 16–32 px, okraj 1 px `#E6E6E6`, uvnitř velkorysé odsazení (24–40 px). Jedna karta = jedna informace.
   Karta vzniká z prvku na obrazovce (klik, ukazatel, hrana produktu), nikdy z ničeho.
3. **Sklo**: max. 1–2 skleněné prvky (lišta, posuvník), jako rozmazaný klon scény za kartou + 1 px světlý okraj nahoře. Žádné duhové hrany,
   žádné sklo všude („no fake glassmorphism everywhere“, `daniel-haida-8691d4`), nikdy sklo přes produkt.
4. **Stíny**: měkké a nízké (dvouvrstvé: kontaktní ostrý 0–2 px + široký 24–60 px, krytí 6–12 %). Stín se mění s výškou karty. Tvrdé stíny = PowerPoint.
5. **Kurzor**: macOS šipka (černá s bílým okrajem), pohybuje se po oblouku, zpomaluje do cíle, natočí se ke směru, hover = zvětšení ×1,2–1,3,
   stisk = −15 % na 2–3 snímky + kroužek akcentu. Kurzor **způsobuje** změny (klik, tažení, dlouhý stisk), nikdy jen nepluje (`notdwd-7de38a`, `twoclipping-221cab`).
6. **Pružiny**: UI prvky překmit 2–3 % jednou, kamera, velké plochy a text kriticky tlumené. Ukazatele a knoflíky mají **dvě hrany na dvou pružinách**
   (náběžná předběhne, prvek se natáhne). Pružiny v uzavřeném tvaru, hodnota s více cíli = součet pružin.
7. **Rytmus**: 120 BPM, událost na každou dobu, nová myšlenka ~1 s, předání na úder. Drop = největší změna měřítka (karta → celý obraz).
   Nikdy dvě vrstvy textu v jednom místě, odcházející zmizí dřív.
8. **Kamera**: jeden svět, jedna kamera (posun + log zoom), přiblížení „screen studio“ na moment, který se právě děje, kurzor se škáluje s ní.
   Záběry **přijíždějí už v pohybu** a odjíždějí zrychlením.
9. **Typografie**: jedna geometrická groteska (u BMW Manrope místo BMW Type Next), čísla Light 300 velká, jednotky menší a šedé, popisky Medium 500,
   nadpisy 2–4 slova, bez tečky. Text se odkrývá maskou zdola nebo roztažením **jako celek**, ne slovo po slově.
10. **Barvy**: neutrály + **jeden akcent jen na akci** (aktivní ukazatel, výplň posuvníku, klik). Akcent nikdy jako plocha pozadí ani záplava.
11. **Přechody**: jeden prvek nese děj (pilulka, ukazatel, hrdinský obraz), další scéna vzniká z předchozí: morf tvaru, match-position,
    zaplavení tvarem přes rohy ~0,3 s, clona. Prolínačka celého obrazu nikdy.
12. **Čísla**: rolující číslice (každá číslice ve vlastním sloupci 0–9), cílová hodnota přesně ověřená (C8), číslo vázané na fyzický prvek (knob, ukazatel).
13. **Co dělá „wow“**: skutečný produkt v nečekaném měřítku (karta se rozroste přes celý obraz na drop), přímá manipulace (tažení mění skutečný obraz:
    noc se odkryje pod knobem), dokonalé předání bez střihu, ticho a prostor před úderem, jeden drahý detail (glint, rozsvícení světel).
14. **Co dělá „levnou šablonu“**: plovoucí karty bez důvodu, kurzor, který nic nedělá, sklo a záře všude, každé slovo zvlášť, skákavé pružiny,
    stock ikony s různou tloušťkou čar, text v rozích, tečkové mřížky, vymyšlená čísla a „dashboard“ bez obsahu, stejný pohyb pro všechny prvky.

### 11.2 Spojení s fotorealistickým produktem (G7)
- **Produkt je fotka / render výrobce, UI je kód.** Prompty z katalogu pracují se skutečnými snímky (Photo print app: fotky i natočená stěna),
  takže jejich techniky jdou použít beze změny, když se render jen maskuje, posouvá, škáluje a odkrývá. Nikdy ho nedeformovat ani nepřekreslovat.
- **Přesvícení mezi dvěma zarovnanými snímky** (den / noc, světla vyp / zap) je nejsilnější „realistický“ efekt: vypadá jako skutečná změna
  světla, protože to skutečné světlo je (render výrobce). Hranice odkrytí měkká a vázaná na ovládací prvek.
- **UI k produktu linkou**: popisek s tenkou linkou (1 px `#BBBBBB`) a bodem na detailu vozu, linka se kreslí od bodu ke kartě.
- **Stín pod produktem** z renderu (kontaktní stín je v rendru), UI karty mají vlastní stín, ale nikdy nevrhají stín na render.
- **Měřítko**: render jen zmenšovat nebo zvětšovat do své nativní kvality (2560 px galerie = max ~1,3× v 1080p bez měkkosti).
- **Otočka po 10° (36 snímků)** je při pomalém pohybu trhavá: buď rychle s rozmazáním mezi sousedními snímky, nebo jen krátký oblouk
  synchronizovaný s úderem, nikdy pomalý plynulý turntable.
- **AI znaky na produktu zakázané**: plastový lesk, duhy, glitch, chromatický posun, natažené okraje masky, „vystřižený“ lem (G7).
