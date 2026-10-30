# Deník chyb

Každá chyba, která se při tvorbě objeví (i drobná a hned opravená), sem patří. Zapisuje režisér.
Cíl: **žádná chyba dvakrát**. Každý záznam končí prevencí, která se propíše do pravidel, protokolu, nástroje nebo instrukcí agenta.

```
### C0xx – krátký název (datum, projekt V0xx, kdo: režisér/animátor/střihač/kritik/nástroj)
- Příznak: co se stalo / co kritik našel
- Příčina:
- Oprava:
- Prevence: co se změnilo a kde (soubor), aby se to neopakovalo
```

---

### C017: Pohodová hudba v1 měla propad v horních středech, kontrola pásem ho neodhalila (2026-10-30, V001, našel animátor a pak režisér)
- Příznak: animátor našel propad 16 dB mezi oktávami 0,5–1 kHz a 1–2 kHz a hi-hat kolem −80 dB. Po jeho opravě režisér nezávisle naměřil
  ještě ~13 dB mezi 1 kHz a 2 kHz.
- Příčina: `kontrola_pasem` měří jen široká pásma (středy 250–2000 Hz). Propad uvnitř pásma se schová.
- Oprava: animátor přidal jas Rhodes, hlasitější hi-hat a tleskání a `vysky_db`. Zbytek vyhladí zvukař ve fázi 2.
- Prevence: `kontrola_pasem` doplnit o **spektrum po oktávách** a varování při skoku sousedních oktáv (250 Hz–8 kHz) nad ~8–10 dB (úkol pro zvukaře).

### C016: Fonty z Google Fonts nebyly stažené při měření (2026-10-30, V001, našel animátor)
- Příznak: canvas změřil všechny kandidátní fonty stejně.
- Příčina: prohlížeč stahuje font, až když ho použije prvek ve stránce. `document.fonts.ready` na nepoužité fonty nečeká.
- Oprava: fonty nejdřív vynutit, pak měřit.
- Prevence: `nastroje/vzory/scena.html` má seznam `FONTY` a před `seek(0)` volá `document.fonts.load()` pro každý řez (ověřeno testem).

### C015: setup.sh neinstaloval nástroje přidané později (2026-10-30, nástroj, našel režisér na začátku nové session)
- Příznak: v novém kontejneru chyběly `gdown` a `scipy` (stahování z Drive, generátor hudby).
- Příčina: knihovny jsem nainstaloval ručně, ale nepřidal do `nastroje/setup.sh`.
- Oprava: setup instaluje `yt-dlp faster-whisper gdown scipy pillow-heif`.
- Prevence: **každá nová závislost hned do `setup.sh`**, jinak ji příští session nemá.

### C014: Drobné chyby při psaní hudba.py (2026-10-30, nástroj, našel režisér testem)
- Příznak: (1) `butter()` nepřijal jednoprvkové pole jako mezní frekvenci, (2) náhodné „lidské“ posunutí noty před čas 0 rozbilo vkládání do mixu,
  (3) při úpravách zůstal v kódu nesmyslný řádek.
- Oprava: skalár pro lowpass/highpass, oříznutí signálu před 0, řádek přepsán na pomocnou funkci `swing()`.
- Prevence: nový nástroj vždy hned spustit ve všech režimech (všechny nálady), ne jen přeložit.

### C013: drive.sh nenašel právě stažený soubor (2026-10-30, nástroj, našel režisér testem)
- Příznak: stažení proběhlo, ověření nic nevypsalo.
- Příčina: gdown zachová původní datum souboru z Drive, hledání „novějších souborů“ ho minulo.
- Oprava: porovnání obsahu složky před a po stažení.
- Prevence: nové soubory poznávat podle seznamu, ne podle data změny.

### C012: Hudba měla 2–3× víc hlubokých basů než profesionální mix (2026-10-30, hudba.py v1, našel režisér měřením pásem)
- Příznak: sub 42–58 % energie (reference R5: 20 %), u drzé nálady jen 4 % středů. Z telefonu by hudba zněla skoro prázdně.
- Příčina: basa o oktávu níž (F1 44 Hz), dlouhý dojezd kopáku, taiko a úderu, melodické nástroje potichu. Poslech nemám, kontrola chyběla.
- Oprava: basové tóny v rozsahu 55–104 Hz s vyššími harmonickými, kratší a tišší bicí a úder, víc středů, highpass 38 Hz.
  Výsledek: sub 11–18 %, středy 31–64 %.
- Prevence: `hudba.py` po každém renderu měří pásma a varuje (pravidlo I7). **Hudbu posoudí uživatel poslechem**: zpětná vazba → pravidla.

### C011: Mastering nezkonvergoval na true peak ≤ −1 dBTP (2026-10-30, master_zvuk.sh, našel režisér na ukázce hudby)
- Příznak: po 3 pokusech −0,7 dBTP. Limiter s rychlým uvolněním (60 ms) výsledek zhoršil až na +0,6 dBTP.
- Příčina: lineární loudnorm nic neomezuje a snížení jeho cíle TP na výsledek nemá vliv. Rychlý limiter zkresluje basy a AAC pak přidá další špičky.
- Oprava: při přetečení nejdřív ubrat hlasitost o přesah (v toleranci −14 ±1), teprve potom jemný limiter (192 kHz, attack 5 ms, release 300 ms).
  Ověřeno na 3 různých vstupech: −14,0 až −14,3 LUFS, −1,0 až −1,4 dBTP.
- Prevence: zvukové nástroje testovat na více typech vstupu (tichý, hlasitý, profesionální mix).

### C010: `ffmpeg` ve smyčce `while read` sní zbytek vstupu (2026-10-30, nástroj kontrola.sh, našel režisér testem)
- Příznak: ze 2 podezřelých míst vznikl jen 1 pás snímků.
- Příčina: ffmpeg čte stdin a spotřeboval zbývající řádky smyčky.
- Oprava: `ffmpeg -nostdin`.
- Prevence: **každý ffmpeg ve smyčce `while read` má `-nostdin`**.

### C009: Rychlý přechod hlášen jako probliknutí (2026-10-30, nástroj skoky.py, našel režisér testem na R2)
- Příznak: 5snímkový přechod a 2snímkové prolnutí v R2 označené jako „probliknutí“.
- Příčina: z rozdílů jasu sousedních snímků nejde poznat, jestli se obraz vrátil.
- Oprava: série 1 = střih, 3+ = rychlý přechod, 2 = podezřelé → `kontrola.sh` vyřízne pás 6 snímků a kritik ho musí prohlédnout.
- Prevence: automatický nález je jen podezření, rozhoduje pohled na snímky (instrukce kritika).

### C008: Tmavé pozadí hlášeno jako černý úsek (2026-10-30, nástroj kontrola.sh, našel režisér testem)
- Příznak: blackdetect hlásil 0–2,8 s jako černé, i když byl na obrazovce text.
- Příčina: výchozí prahy blackdetect berou téměř černé pozadí (#0b0b0c) s malým textem jako černý snímek.
- Oprava: `pic_th=0.999:pix_th=0.06`, hlásí se jen opravdu prázdné snímky.
- Prevence: nástroje testovat i na tmavém designu, ne jen na fotkách.

### C007: True peak po AAC překročil limit (2026-10-30, nástroj master, našel režisér testem)
- Příznak: loudnorm s cílem −1 dBTP, po zakódování do AAC naměřeno −0,2 dBTP.
- Příčina: kodek AAC přidává mezivzorkové špičky.
- Oprava: `nastroje/master_zvuk.sh` měří po AAC a až 3× sníží vnitřní cíl true peak (výsledek −14,2 LUFS / −1,3 dBTP).
- Prevence: hlasitost se vždy měří **po** finálním zakódování (pravidlo A2, kontrolní seznam K).

### C006: Podsnímky nebyly vystředěné (2026-10-30, nástroj render_html.cjs, našel analytik)
- Příznak: rozmazání přes celý snímek jen dopředu (závěrka 360°), obraz posunutý o ~⅓ snímku, silná šmouha.
- Příčina: časy podsnímků `(f + s/SUB)/FPS`.
- Oprava: vystředěno kolem času snímku, `--zaverka 0.5` (180°), výchozí `--sub 4`.
- Prevence: nástroje porovnávat s metodou nejlepších promptů prompt-motion (`poznatky.md` 2.7).

### C005: Pružina měla výchozí překmit 8 % (2026-10-30, kostra scena.html, našel analytik)
- Příznak: UI prvky by „houpaly“ jako kreslený film.
- Příčina: výchozí hodnota zvolená odhadem.
- Oprava: výchozí 3 %, přidána kriticky tlumená `usazeni()`. Pravidlo F4 upraveno na 2–5 %.
- Prevence: číselné výchozí hodnoty brát z ověřených zdrojů a zapsat zdroj.

### C004: `will-change` v kostře scény (2026-10-30, kostra scena.html, našel analytik)
- Příznak: (potenciální) rozmazaný text, když ho kamera zvětší.
- Příčina: `will-change: transform` rasterizuje prvek v původní velikosti.
- Oprava: odstraněno, scéna se navíc staví až po `document.fonts.ready`.
- Prevence: past je zapsaná v oddílu `<pasti>` hlavní kostry promptu (`poznatky.md` 10) a v kontrolách kritika.

### C003: Render s 3 podsnímky dělá u rychlého pohybu „schodovité duchy“ (2026-10-30, test, nástroj)
- Příznak: při testu `render_html.cjs` byl text v rychlém příjezdu 3× zdvojený místo plynulého rozmazání.
- Příčina: 3 podsnímky na snímek nestačí na velký posun mezi snímky.
- Oprava: žádná (test).
- Prevence: v instrukcích animátora je pro rychlé přechody `--sub 6` + rozmazání v CSS podle rychlosti a směru. Kritik porovnává sousední snímky.

### C002: `analyzuj.sh` spadl u videa bez střihů (2026-10-30, nástroj)
- Příznak: skript skončil po řádku „Střihy“ a nevytvořil náhled.
- Příčina: `grep` bez shody vrací chybový kód a `set -o pipefail` ukončí skript.
- Oprava: `|| true` a hláška „žádné tvrdé střihy“.
- Prevence: v bash skriptech s `pipefail` u grep/filtrů vždy počítat s prázdným výsledkem.

### C001: Whisper nepřečetl video přímo (2026-10-30, nástroj)
- Příznak: `TypeError: open() got an unexpected keyword argument 'metadata_errors'`.
- Příčina: faster-whisper volá novější PyAV, než je nainstalované.
- Oprava: zvuk dekóduje ffmpeg a do Whisperu jde pole vzorků (`nastroje/prepis.py`).
- Prevence: používat jen `nastroje/prepis.py`, nevolat faster-whisper přímo se souborem.
