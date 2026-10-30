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
