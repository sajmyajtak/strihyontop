# Deník poučení

Po každém videu sem zapsat: co fungovalo, co ne, zpětnou vazbu uživatele (doslova) a co se změnilo v pravidlech.
Nejnovější záznam nahoře. Každé poučení, které platí obecně, přenést do `pravidla-strihu.md` se zdrojem `[V0xx]`.

## Šablona záznamu
```
### V0xx – název videa (datum)
- Zadání: projekty/0xx-nazev/zadani.md
- Fungovalo:
- Nefungovalo / opravy:
- Zpětná vazba uživatele (doslova):
- Změny v pravidlech: (např. „E2 upraveno: …“)
```

---

### 2026-11-04: Zpětná vazba k V004 a střihový vzor uživatele (R6, R7, R4 znovu)
- **Zpětná vazba (doslova)**: „noooo hele takhle není to špatný ale zkus se zaměřít víc na ten střih a editaci videa pošlu ti další reels jak bych si
  představoval moje videa a celkově jejich prezentaci. Nic negeneruj jen si je přečti a adaptuj se n atokýhle střihy.“ → „okey tak to jsem rád. nauč agenty ať to umí“.
- **Předlohy**: R6 Packeta Z-BOX (@davidxsipos, 22 s, 0 střihů, hlas, natočená obrazovka, end card tvůrce), R7 AE vs. Gemini (@shhradddhaa.ai, 9,5 s, mockup
  se dvěma panely, CTA v obraze, 3 600 komentářů), R4 Ugoki easing (poslal podruhé: titulky slovo po slově, jeden souvislý svět, hlas řídí střih).
- **Hlavní poučení**: „střihem a editací“ uživatel myslí **kvalitu přechodů a vedení pozornosti**, ne počet střihů. V004 dělalo energii kvantitou
  (25 střihů, 4 karty, mřížka, 3–5 prvků naráz); všechny jeho předlohy mají 0 tvrdých střihů, jednoho hrdinu na obrazovce, každou změnu s příčinou
  (slovo hlasu nebo předchozí prvek) a prezentaci jako natočenou obrazovku / mockup s podpisem tvůrce.
- **Co se změnilo**: nový závazný dokument `znalosti/strih-vzor.md` (10 zásad, partitura, kamera, typografie, kontrolní seznam); pravidla D8–D12
  (rozpočet prvků, partitura, semínko, zásobník přechodů, zvuk podle obrazu), C9 (podpis tvůrce), A9 (prezentace), H5 (parametry natočené obrazovky),
  I9 (zvuk u videí s hlasem), upřesnění C7, D1, D2, D3, E1, E2, G9, J1, K; instrukce všech šesti agentů a CLAUDE.md (storyboard = partitura,
  kreativní ředitel hodnotí střih 3×). Rozbory jsou v `reference/R6…`, `R7…`, `R4…` (doplněk).
- **Otevřené otázky pro uživatele** (nerozhodnuto, zapsáno v reportu): voiceover (předlohy ho mají, zadání dosud ne), formát doručení (16:9 + 9:16 prezentace?),
  jméno a logo na podpisu tvůrce, kdo točí natočenou obrazovku (uživatel, nebo digitální maketa).

### V004: BMW i7 M70 „Bod, který nepustí vůz“ (2026-11-02, doručeno v4d, čeká na zpětnou vazbu)
- Zadání: projekty/004-bmw-jizda/zadani.md. 30 s, 16:9, 60 fps, `luxsport` s `--motor elektricky`, bez VO, vůz musí jet, 4 předlohy prompt-motion.
  Varianta 1 (rozhodnutí uživatele): jízda = skutečná stopáž BMW (stříbrná i7 60, bez čelních pohledů s chromovými ledvinkami), vůz uživatele
  (bílý M70) v rendrech konfigurátoru. Kola: v1 7,3 / jízda 7,5 / realismus 7,5 / energie 7 → v2 7,9 / 8 / 8 / 7,5 → v3 **8,2 / 8,5 / 8 / 8** (KŘ schválil,
  kritik blokující) → opravy režiséra v4 → v4d s kontrolou jen opravených míst (kola 4–7, 7 agentů): konečně **wow 8,4 / jízda 8,8 / realismus 8,3 /
  energie 8,5**, kritik SCHVÁLENO. 27 pomocných agentů, 5,15 mil. tokenů, 370 min.
- **Fungovalo**: skutečná stopáž výrobce jako hlavní materiál jízdy (1,2×, kadence 2:2 na 60 fps, jednotný high-key grade se rendry), každý úsek zdroje jen
  jednou (rozpis úseků), SaaS vrstva bod → linka → karta přes jízdu mimo vůz, drop 2 „bod → svazek stop → průlet“, písmena modelu v pásech s jízdou,
  clona z bodu → logo. Vlastní hudba s motivem elektromobilu. Režisér opravil poslední blokující nález sám (bez dalšího kola agentů).
- **Nefungovalo / zdrželo**: opravné kolo animátora si samo vybralo záběr ze zakázaného úseku (C044); zvuk souběžně s obrazem nesledoval změny (C045);
  pokyny režiséra mezi nálezy se ztrácely (C043); karta mezi dvěma střihy byla krátká (C046). Agentů bylo 20 místo cílových 10–12 (3 kola × 2 kontroly
  + 3 opravy se zvukařem).
- **Pro příště**: (1) zakázané úseky stopáže hlídat u každé náhrady (kritik i autor); (2) v opravném kole obraz → potom zvuk (posuny SFX režisér);
  (3) rozhodnutí režiséra jako číslovaná kritéria; (4) karty faktů plánovat se ≥ 0,5 s klidu už ve storyboardu; (5) zrcadlení stopáže je v pořádku jen
  bez textu, SPZ a log.
- **Kola 4–7 (režisér opravuje, 2 kontroloři ověřují jen opravená místa)**: levné (0,18–0,31 mil. tokenů na kolo) a přesné; regrese hlídal rozdíl snímků
  proti předchozí verzi. Poučení: (6) nové pravidlo hned uplatnit na všechna místa (G9 u všech karet, C046); (7) retuš stopáže kontrolovat výřezem 1:1 a raději
  rozostřit než ztmavit (C048); (8) ding až na ustálený snímek, při kolizi posunout druhý zvuk (C047); (9) definice měření předem („ustálený“ = pohyb < 0,5 px),
  jinak kritik a autor měří každý jinak.
- **Zpětná vazba uživatele**: (čeká)

### V003: BMW řada 7 „ONE CONTROL“ (2026-11-01, doručeno v4, zpětná vazba „není to ono“)
- Zadání: projekty/003-bmw-rada7/zadani.md. 25 s, 16:9, 60 fps, luxusní sportovní hudba (nová nálada `luxsport`), bez VO, 7 motionů, skládací logo.
  Kola: v1 7,5 / realismus 8 / energie 6,5 (blokující 259 km/h) → v2 8 / 8 / 7,5 → v3 8,3 / 8,5 / 8 (schváleno všemi) → režisérská oprava v4
  **8,5 / 8,6 / 8,3**. ~6,24 mil. tokenů, ~7,4 h práce agentů.
- **Fungovalo**: **skutečné rendry výrobce** místo kresby (konfigurátor v běžném prohlížeči: 14 pohledů, otočka 360° se světly zap/vyp
  pixelově zarovnaná, interiér 360°). Realistické efekty jen ze skutečných stavů (rozsvícení světel = rozdíl zap − vyp, den → noc pod knobem,
  krokování otočky jako klikání v konfigurátoru). Technický test realismu **před** konceptem (co funguje, co prozradí AI). SaaS UI (lišta, pilulka,
  posuvník, karty, kurzor) jako spojovací jazyk jednoho konceptu. Drop 2 „tma → světla → karoserie“ = nejsilnější moment. Fakta doslova z bmw.cz.
- **Nefungovalo / zdrželo**: noční rendry BMW jsou šedé („hliněný model“), lak musel dostat grade v masce; vymyšlené číslo z rolujících číslic
  (259 km/h, blokující); duchové z podsnímků u rychlých UI prvků; koláž dvou perspektiv v interiéru (vyřešeno tvrdým střihem); zastaralé odvozené
  zvukové soubory (C039); přesah textu a barvy tenkého textu po kódování (C041). Zvuk se musel po stavbě obrazu přesunout na skutečné časy.
- **Pro příště**: (1) u produktů vždy nejdřív zdroj výrobce a test realismu; (2) čísla na obrazovce omezit cílem (nikdy nad fakt); (3) rychlé UI
  rozmazávat v kódu podle rychlosti, ne kopiemi; (4) zvuk dolaďovat až podle skutečných časů obrazu (režisér přesune SFX); (5) energii u realistického
  produktu nesou tvrdé střihy na doby, dotlačení a stavy světla, ne efekty přes vůz.
- Nové nástroje a pravidla: `hudba.py` nálada `luxsport`, `sfx.py` (`ton_c`, prémiové UI zvuky), `render_html.cjs` CRF 14 + aq-mode 3, `setup.sh` + rembg,
  pravidla G7 (realismus), G8 (SaaS motion), D7 (přímá manipulace), vkus uživatele V002. Chyby C035–C041.
- **Zpětná vazba uživatele** (2026-11-01): „není to ono… realistické auto… že animuješ, aby to vypadalo realisticky při ukázce auta i rychlosti, výkonu,
  a ty obrázky byly jen doplnění materiálu… auto se bude pohybovat a jet rychle.“
- **Hlavní poučení**: kritici hodnotili realismus *obrazu* (8,6), ale uživatel chtěl realismus *pohybu*: **jedoucí auto**. Statický render
  posouvaný kamerou je pro něj „prezentace“. U aut (a produktů v pohybu) je hlavní materiál **pohyb** (skutečné záběry jízdy), rendry jen doplněk.
  Kritici musí mít v zadání výslovně „vůz jede“ a hodnotit, jestli divák vidí jízdu. Zapsáno do vkusu uživatele a G7.

### V002: Mercedes-Benz „FOLLOW THE STAR“ (2026-10-31, doručeno v4, zpětná vazba 2026-11-01)
- Zadání: projekty/002-mercedes-racing/zadani.md. 30 s, 1920×1080, 60 fps, sportovní hudba (nová nálada `sportovni`), bez VO, 4 motiony z prompt-motion.
  Kola: v1 wow 7,8 / energie 7,5 → v2 8,4 / 7,5 → v3 8,25 / 8 → režisérská oprava v4 **8,4 / 8,1**. ~4,93 mil. tokenů, ~7,6 h práce agentů.
- **Fungovalo**: koncept stojí na geometrii loga (linie → prstenec → hvězda ze světla), opět nejsilnější typ nápadu (stejně jako V001).
  Oponentura konceptu na energii před stavbou (7,6 → revize 13 oprav). Zkušební list vozů ve variantách A/B schválený na 480 px dřív, než se stavěl pohyb
  (chytil „Supru“ místo AMG GT, hranatou helmu, UI portál). Stavba pohybu po 3 blocích = žádný agent nenarazil na limit. Měření místo dojmů
  (YDIF dropů, RMS stoupání, pixely barev, framemd5 při sestřihu).
- **Nefungovalo / zdrželo**: renderer byl 5× pomalejší, než se myslelo (C027, opraveno za běhu); energie se zvedala pomalu, protože storyboard měl
  „klidná“ místa (statický celek úvodu, stojící text, stojící hvězda), která se poznala až v pohybu. Chromatický posun přes RGB kanály na logu (C034)
  prošel 2 koly, než ho chytili všichni kritici. Weby značky blokují roboty (403), paleta zůstala předběžná.
- **Pro příště**: (1) energii hlídat už ve storyboardu: u každého taktu napsat, co se hýbe **nepřetržitě** (ne jen na dobu), text nikdy nestojí bez pohybu;
  (2) úvod 0–0,5 s a end card mají mít pohyb od prvního snímku; (3) efekty „na logo“ jen v barvách palety; (4) kontrolní snímky klíčových úderů dělat
  z výřezu s podsnímky, ne staticky (C028); (5) před dlouhým renderem změřit 1 s výřezu.
- Nové nástroje a pravidla: `render_html.cjs` (CDP, 3 vlákna, `--rychle`, `--od`), `sfx.py` (`--zisk-hudby`, `--saturace`, `--limiter`, PODKLADY),
  `hudba.py` nálada `sportovni`, `kontrola.sh` (pásy u všech skoků, přesný arch), `master_zvuk.sh` (latency, dolní propust), vzory workflow
  v `nastroje/workflow/`. Chyby C025–C034. Pravidla I3 (podklad, stavba hlasitosti).
- **Zpětná vazba uživatele** (2026-11-01): „není to špatný, ale… ať to není tak moc kreslený… SaaS motion… realistické modely aut, který fakt vypadají
  jak v realitě… realistickou reklamu, kterou člověk nerozezná, že je dělaná přes AI, a aby byl wow efekt.“
- **Hlavní poučení**: energie už sedí („není to špatný“), ale **vozy kreslené v kódu působí kresleně**. U produktů (auta, zařízení) stavět na
  **skutečných fotografiích / CGI rendrech výrobce**, ne na kresbě. Styl, který uživatel chce: **SaaS motion** (čisté UI karty, plynulá kamera,
  kinetická typografie, produkt jako hrdina). Zapsáno do pravidel (vkus uživatele, G7).

### V001: Bageterie Boulevard „Logo byla celou dobu bageta“ (2026-10-31, doručeno, čeká na zpětnou vazbu)
- Zadání: projekty/001-bb-chill/zadani.md. Výsledek: 25 s, 1080×1920, 60 fps, wow 6,9 → 7,3 → **8,1**, schváleno všemi 3 kritiky ve 3. kole.
- **Fungovalo**: porota konceptů (vítěz stál na geometrii loga), schválení klíčových snímků před stavbou pohybu (chytilo „rajče jako kámen“,
  „chleba jako prkénko“ a „rukolu jako javor“ dřív, než se drahé renderovalo), nezávislí kritici s důkazy po snímcích, automatika hudby
  (ztlumení před dropem dá +17 dB kontrast), **závazný pokyn režiséra**, když se stejná chyba opakuje (řezy nadpisů selhaly 2×, po pokynu napoprvé).
- **Nefungovalo / zdržení**: maximální úroveň přemýšlení a obří výstupy (C018), limit účtu (C020), pravidlo „SFX tiše pod hudbou“ utopilo pointy (I3 upraveno),
  chybělo pravidlo o velikosti hrdiny (A8). Celkem ~3,7 mil. tokenů změřeno, ~5,3 h práce agentů.
- **Pro příště**: (1) vztahovat výtky „neviditelné na telefonu“ k zmenšenině 270 px už v klíčových snímcích; (2) přechody textu stavět vždy přísně
  po sobě (nikdy dvě vrstvy textu v jednom snímku), to je teď v pokynu V001 a patří to do pravidel D/E po zpětné vazbě; (3) u spec reklam
  v popisku neoznačovat značku @handle.
- **Zpětná vazba uživatele**: „není to špatný ale není to ono… víc energetické, ať to není tak bez duši… rychlejší, živější, víc efektů.“
- **Hlavní poučení**: kritici dali 8,1, a přesto to uživatele nenadchlo. **Laťku jsme kalibrovali na střídmost (prompt-motion: žádná záře,
  žádné efekty, jeden švih za video), ale uživatel chce energii.** Zapsáno do pravidel (C7, D2, G2, G6, vkus uživatele nahoře v pravidlech).
  Kreativní ředitel a kritici teď hodnotí energii a živost jako hlavní kritérium.
- Nová výchozí nastavení: 16:9, 25–35 s, jedno video naráz, hudba bez voiceoveru.

### 2026-10-30: V001 porota konceptů (první workflow s více agenty)
- Uživatel: **na každý úkol vlastní agent, ostatní agenti se ptají hlavního, video má být „wow“**. Zavedeny role zvukař a kreativní ředitel,
  koncept přes porotu: 3 návrhy (A animátor, B a C kreativní ředitelé z jiných úhlů) → 3 porotci s různými pohledy naslepo → syntéza.
- Výsledek: B „Logo byla celou dobu bageta“ 7,05 · A „Ubrus“ 6,98 · C „Groove“ 6,38. Těsný výsledek: porotce za značku chtěl A,
  porotci za nápad a řemeslo B. Syntéza vzala B a převzala nejlepší z A a C (sdílená slova, klidná kamera na dropu, servírování na marimbu).
  Postřeh: **nejsilnější nápady stojí na geometrii samotného loga** (jako šipka ve FedEx), nejde je přenést na jinou značku.
- Výkon: na 4 CPU pouští workflow **najednou jen 2 agenty** (strop = CPU − 2). Plánovat s tím paralelní fáze.
- Chyba C018: agenti s maximální úrovní přemýšlení a jedním obřím výstupem narazili na limit výstupu (C 3×, ~694 tis. tokenů bez výsledku).
  Po restartu s `effort: 'high'` a psaním po částech byl C hotový za 8 min a porota za 4 min. Hlídač `nastroje/hlidac.py` to teď pozná sám.

### 2026-10-30: Nová složka na Google Drive jen pro materiály
- Uživatel: **„vytvoříme úplně novou složku, kde si budeš brát materiál“** pro nová videa, staré složky nepoužívat. Soustředit se jen na tvorbu videí pro portfolio.
- Založeno: „Střižna – materiály pro portfolio“ (01 Projekty / 02 Logo a značka / 03 Hotová videa + návod). Uživatel musí nastavit sdílení odkazem (Čtenář).
- Ověřeno: stažení celé složky (6 videí, 126 MB, 21 s), příprava materiálů včetně HEIC. Nástroj `materialy.py`.
- Pozor na bezpečnost: starší složka byla sdílená „kdokoli s odkazem = Editor“. Pro materiály stačí Čtenář.

### 2026-10-30: Nastavení od uživatele, vlastní hudba v1, Google Drive
- Uživatel: videa **anglicky**, **zatím bez voiceoveru** (později ElevenLabs), **hudbu vytvářet** podle tónu (vážný / drzý / luxusní),
  barvy a CTA podle zadání, materiály na **Google Drive**, **Higgsfield nepoužívat**. Zapsáno do `znacka.md`, pravidla I6–I8.
- Higgsfield stejně nemá hudební model pro naše použití (jen pro hry, Suno v katalogu není). Ověřeno bez útraty kreditů.
- Postaven `nastroje/hudba.py` (syntéza: kopák, snare, clap, hi-hat, shaker, taiko, sub/pluck basa, smyčcové ostinato, pad, Rhodes FM,
  klavír, drnkání Karplus-Strong, riser, úder, dozvuk konvolucí, sidechain). 20 s se vyrenderuje za 3–5 s.
- **Poslouchat neumím.** Kvalitu hlídám měřením (pásma, hlasitost, spektrogram) a o „znění“ rozhoduje uživatel poslechem ukázky
  `ukazka-hudby-v1.mp4`. Jeho zpětná vazba = první pravidla pro hudbu.
- Google Drive: konektor funguje (účet s materiály), videa se stahují přímo (`drive.sh`), soubory jsou sdílené odkazem.

### 2026-10-30: Nastudován celý prompt-motion.com (první běh systému agentů)
- Analytik přečetl všech 236 položek, 2 šablony a 5 článků → `prompt-motion/poznatky.md` (metoda, anatomie promptu, AI znaky, doporučené prompty podle typu, naše kostra zadání).
- **Spotřeba: analytik 302 588 tokenů, 30 akcí nástrojů, 15,6 min.** Hlavní chat neměřeno.
- Režisér výstup zkontroloval: čísla ověřena proti datům a blogu (17 023 lajků, 16 položek 9:16, existence doporučených položek).
  Přijato 14 úprav a 8 nových pravidel (`[PM]`). Výjimka u D2/G2: předloha od uživatele smí zákaz přebít.
- Analytik našel 3 chyby v nástrojích (C004–C006). Režisér je opravil a při testech oprav našel další 4 (C007–C010).
  **Smyčka „tvůrce → nezávislá kontrola → oprava → zápis prevence“ funguje i na nástrojích.**
- Hlavní poučení z katalogu: krátký prompt je loterie (stejný prompt: 0 až 17 023 lajků). Kvalitu dělá jeden koncept, seznam zákazů,
  mřížka dob, metoda renderu a kontrola snímků. Formát 9:16 je v katalogu vzácný (7 %), skoro vždy se musí přeskládat (A7).

### 2026-10-30: prompt-motion.com jako hlavní zdroj promptů, systém agentů, kontrola kvality
- Uživatel určil **prompt-motion.com** jako hlavní zdroj promptů. Prompty vybírám já, nebo je pošle uživatel.
- Zavedena **režie**: hlavní chat = režisér, podřízení agenti analytik / animator / strihac / kritik (`.claude/agents/`).
  Kritik kontroluje každý render (max 3 kola), chyby se zapisují do `chyby.md`, uživatel dostává jen výsledek + report (chyby, tokeny).
- Postaven a otestován `nastroje/render_html.cjs` (metoda prompt-motion: HTML + `window.seek(t)` → Playwright → ffmpeg).
  Ověřeno: rozmazání podsnímky, kontrolní snímky, zvuk generovaný ve stránce (Web Audio → WAV) sedí přesně na doby.
- Repozitář je **veřejný**. Plné prompty z prompt-motion proto jen v lokální mezipaměti, do gitu odkazy a vlastní poznatky.

### 2026-10-30: Založení, rozbor prvních 5 referencí (R1–R5)
- Rozebráno 5 IG reels, výsledky v `reference/R1–R5`, pravidla A–K v `pravidla-strihu.md`.
- Uživatel chce: portfolio videa pro sociální sítě, každé video podle vlastních pravidel a předloh, **logo animace** jsou v nabídce (R5).
- Postřeh: nejvíc dosahu (148 tis. lajků) měla R3: vlastní koncept + názor („made by a human“) + emoční zvrat. Ne efekty, ale **nápad a příběh**.

## Technické poznámky
- **Instagram**: yt-dlp funguje bez přihlášení, ale při rychlém stahování vrací HTTP 429. Stahovat po jednom s pauzou ~40–60 s.
- **YouTube**: yt-dlp funguje.
- **TikTok**: yt-dlp v tomto prostředí selhává („Unexpected response from webpage request“). Obejití imitací prohlížeče zablokovala bezpečnostní pravidla prostředí. TikToky si nechat **poslat jako soubor**.
- **Přepis**: faster-whisper (`nastroje/prepis.py`). Zvuk se musí předávat přes ffmpeg, vestavěné dekódování padá na verzi PyAV. Model `small` stačí na angličtinu, pro češtinu `medium` / `large-v3`.
- Whisper občas zkomolí jména a značky („Higgs Field“, „Enmi Ogoki“ = „DM me UGOKI“). Přepis vždy porovnat s obrazem.
- **Známý dluh hudby**: nové kontrole po oktávách neprojdou nálady **vážná** (250→500 Hz +16 dB, středy 85 %) a **luxusní** (1→2 kHz −12,7 dB,
  nad 2 kHz skoro nic). Vyrovnat je v projektu, který je poprvé použije. Změní se tím jejich zvuk, proto ne naslepo. Drzá a pohodová jsou v pořádku.
  Navíc (C026): vazna, drza, luxusni a pohodova se normalizují dynamickým loudnorm, který zploští kontrast dropu. Při dalším použití přepnout
  na lineární zisk + limiter jako `sportovni` a poslat uživateli poslechovou ukázku. `sportovni` (V002) je už v pořádku.
- Spektrogram z `ffmpeg showspectrumpic` s logaritmickou osou kreslí vodorovnou čáru kolem 1,44 kHz. Je to chyba vykreslení, ne díra ve zvuku
  (ověřeno Welchovou metodou, V002). Díry v pásmu posuzovat podle `oktavy_db`, ne podle obrázku.
- Prostředí: 4 CPU, bez GPU. Render 1080×1920 krátkých videí je v pohodě, dlouhé 3D scény budou pomalé.
- `render_html.cjs` (V002, 1920×1080, 60 fps, `--sub 4`, složitá canvas scéna se zrnem): původně ~190 s výpočtu na 1 s videa, z toho většina
  kódování PNG v `page.screenshot`. Po C027 (CDP `optimizeForSpeed`, 3 prohlížeče): ~35 s na 1 s. Prázdná scéna je řádově rychlejší, vždy změřit výřez.
- prompt-motion.com: data jsou ve stránce (Next.js RSC payload), stahuje se bez přihlášení. robots.txt: `use=reference`, `ai-train=no`, `/api/` zakázáno.
  Odkazy na zdroj: holý profil x.com/p4nthera_ je autor webu, ne tvůrce videa.
- Google Fonts v rendereru fungují (ověřeno: Anton, Inter 800 s plnou českou diakritikou). Kontrola: `document.fonts.check('800 96px Inter', 'ď')`.
