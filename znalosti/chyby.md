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
