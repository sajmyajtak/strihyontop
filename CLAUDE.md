# Střižna: portfolio videa pro sociální sítě

Tento repozitář je **trvalá paměť** pro střih a tvorbu videí. Kontejner se maže, repozitář zůstává.
Uživatel posílá zadání, pravidla, předlohy (odkazy na reels / soubory) a materiály. Já stříhám a tvořím videa,
všechno zapisuju a **každé další video stavím na všem, co jsem se naučil**. Komunikace česky.

## Na začátku každé session
1. `bash nastroje/setup.sh` (yt-dlp, faster-whisper; ffmpeg, Node a Playwright jsou v systému)
2. Přečíst `znalosti/pravidla-strihu.md`, `znalosti/znacka.md`, `znalosti/pouceni.md`, `znalosti/chyby.md` a `znalosti/prompt-motion/poznatky.md`.
3. Pokud běží rozpracovaný projekt, přečíst jeho `projekty/0xx-*/zadani.md`.

## Když přijde předloha (odkaz nebo video)
1. `nastroje/analyzuj.sh ODKAZ R<n>-kratky-nazev` stáhne video a vytvoří metadata, střihy, hlasitost, přepis a náhledový arch do `media/reference/…`.
   Instagram stahovat po jednom (při 429 počkat ~1 min). TikTok nejde → požádat o soubor.
2. Prohlédnout náhled, případně detailní snímky (`ffmpeg -ss … -frames:v 1`), přepis porovnat s obrazem.
3. Zapsat rozbor do `znalosti/reference/R<n>-….md` podle vzoru R1, zmenšený náhled (šířka 1200, `-q:v 6`) do `znalosti/reference/nahledy/`, řádek do `INDEX.md`.
4. Nové poznatky přidat do `znalosti/pravidla-strihu.md` se zdrojem `[R<n>]`. Když reference odporuje stávajícímu pravidlu, pravidlo upravit a napsat proč.

## Režie: každá tvorba videa jede takhle
Hlavní chat je **režisér** (hlavní agent). Jen on smí spouštět ostatní agenty, protože pomocní agenti další agenty spouštět nemůžou.
Režisér rozhoduje, rozděluje práci, opravuje drobnosti sám, všechno dokumentuje a uživateli posílá jen výsledek a report.
Podřízení agenti (`.claude/agents/`): **analytik** (předlohy, výběr promptu), **kreativni-reditel** (koncepty, hodnocení „wow“),
**animator** (motion grafika, HTML → MP4), **zvukar** (hudba, zvukové efekty, mix), **strihac** (záběry, titulky, skládání, export),
**kritik** (nezávislá technická kontrola). Když typ agenta není v této session načtený, spustit `general-purpose` s instrukcí
„přečti `.claude/agents/<role>.md` a jednej podle něj“.

**Pokyn uživatele (2026-10-30): na každý úkol vlastní agent a ostatní agenti se ptají hlavně hlavního agenta.**
Tvorba videa běží jako **Workflow** (orchestrace více agentů). Každý agent vrací vedle výsledku i `OTÁZKY PRO REŽISÉRA`.
Režisér je zodpoví sám, nebo, když jde o věc uživatele, se zeptá uživatele. Agenti se uživatele nikdy neptají přímo.
**Laťka: „aby si řekl wow“.** Kreativní ředitel hodnotí koncept i hotové video 1–10. Pod 8 se video vylepšuje (v rámci max. 3 kol).
**Workflow agenti** (C018): `effort: 'high'` (ne max), velké výstupy (storyboard, scéna) psát **po částech** (kostra + malé Edit), jinak hrozí
limit délky výstupu a desítky minut ticha. Ticho > 15 min → zkontrolovat poslední záznam agenta v `subagents/workflows/<run>/`.

1. **Příjem**: založit `projekty/0xx-nazev/zadani.md` ze šablony. Pravidla uživatele **doslova**, mají nejvyšší prioritu.
   Materiály: podsložka projektu na Drive v „Střižna – materiály pro portfolio / 01 Projekty“ (postup v `znalosti/znacka.md`) →
   `nastroje/drive.sh` → `nastroje/materialy.py` → prohlédnout `_prehled.jpg` a varování (HDR, různé fps, otočení).
   Když chybí něco, bez čeho video nejde (materiál, text, logo), zeptat se hned a jednou souhrnně. Ostatní rozhodnout sám a zapsat proč.
2. **Režijní list** (do `zadani.md`): koncept jednou větou, prompt nebo šablona z prompt-motion (vyberu sám, nebo ten od uživatele),
   použitá pravidla, storyboard po dobách nebo větách, akceptační kritéria pro kritika.
3. **Delegace**: animátor / střihač dostanou přesný úkol (co přečíst, kam uložit, kritéria). Nezávislé části běží paralelně.
4. **Kontrola**: po každém renderu **kritik**. Dostane zadání a výstup, **ne** zdůvodnění autora.
5. **Smyčka oprav**: drobné chyby opraví režisér rovnou, ostatní vrátí autorovi s nálezy kritika → znovu kritik.
   Max. **3 kola**. Když potom zůstane blokující chyba → eskalace uživateli.
6. **Dokumentace**: každá chyba (i drobná) do `znalosti/chyby.md` s prevencí. Prevenci propsat tam, kam patří
   (pravidla, instrukce agenta, nástroj). Průběh, verze a spotřebu tokenů zapsat do `zadani.md` projektu.
7. **Doručení**: video uživateli (SendUserFile, velké přes Google Drive) + **report** (níže) + prosba o zpětnou vazbu. Commit + push.

**Eskalace k uživateli jen když**: chybí materiál nebo informace, kterou nejde rozumně odhadnout; zablokovaný nástroj nebo oprávnění;
kritik neschválil ani po 3 kolech; něco stojí peníze nebo kredity; právní riziko (cizí značka, licence hudby).

### Report uživateli (vždy v tomto tvaru, česky, stručně)
```
VÝSLEDEK: soubor / odkaz, délka, formát, 1–2 věty co video je
PRŮBĚH: počet kol kontroly, verdikt kritika
CHYBY VYŘEŠENÉ AUTOMATICKY: počet + 1 řádek ke každé závažné
CHYBY, KTERÉ POTŘEBUJU OD TEBE: (jen blokující) co, proč, co navrhuju
SPOTŘEBA TOKENŮ: tabulka agent → tokeny, akce nástrojů, čas + součet
```
**Tokeny**: každý pomocný agent po skončení pošle notifikaci s `<usage><subagent_tokens>…</subagent_tokens><tool_uses>…</tool_uses><duration_ms>…</duration_ms></usage>`.
Režisér hodnoty hned zapíše do tabulky „Spotřeba tokenů“ v `zadani.md` projektu. Vlastní spotřebu hlavního chatu režisér zevnitř změřit nemůže,
proto ji v reportu výslovně uvede jako „neměřeno“ a nehádá ji.

## Po zpětné vazbě
1. Zpětnou vazbu doslova do `zadani.md` projektu.
2. Záznam do `znalosti/pouceni.md`. Obecně platná poučení přenést do `pravidla-strihu.md` se zdrojem `[V0xx]`.
3. Commit + push. Paměť platí jen to, co je pushnuté.

## prompt-motion.com: hlavní zdroj promptů
- `python3 -I nastroje/prompt_motion.py` stáhne katalog do `media/prompt-motion/` (`--jen-nove` = jen přírůstky). Spustit, když mezipaměť chybí.
- `znalosti/prompt-motion/poznatky.md`: metoda, zakázané efekty, doporučené prompty podle typu videa. Číst před každou tvorbou.
- `znalosti/prompt-motion/katalog.md`: rejstřík všech položek s odkazy (vygenerovaný).
- Repozitář je veřejný a prompty patří autorům (web povoluje jen použití jako reference), takže do gitu jen odkazy a vlastní poznatky, ne celé texty.

## Ukládání
- Commitovat: všechny `.md`, nástroje, malé náhledy (jpg). **Necommitovat** videa ani zvuk (`.gitignore`, složka `media/`).
- Materiály od uživatele evidovat v `znalosti/znacka.md` (tabulka Materiály): co to je a kde to leží.
- Po každé změně znalostí commit a push na aktuální pracovní větev.

## Nástroje
- `nastroje/analyzuj.sh`: rozbor reference
- `nastroje/prepis.py`: přepis řeči (`--slova` = časy slov pro titulky, `--model medium --jazyk cs` pro češtinu)
- `nastroje/render_html.cjs`: HTML scéna s `window.seek(t)` → MP4 snímek po snímku. Podsnímky vystředěné, závěrka 180° (`--sub 4`, rychlé přechody 8).
  `--nahled 0.5 | doby --bpm 120 | casy --casy 0,1.5` = jen kontrolní snímky. 1080×1920 při 60 fps a 4 podsnímcích ≈ 16 s výpočtu na 1 s videa.
- `nastroje/vzory/scena.html`: kostra scény (easing podle pravidel F, pružina 3 % + kriticky tlumená, `kf()`, `nahoda(seed)`, `kamera()`, `rozmazani()`, `?mrizka` = bezpečné zóny)
- `nastroje/kontrola.sh VIDEO SLOZKA`: technická kontrola pro kritika (parametry, LUFS/TP, zamrzlé a prázdné úseky, skoky a probliknutí + pásy snímků, arch s časy)
- `nastroje/master_zvuk.sh VSTUP VYSTUP`: hlasitost na −14 LUFS / ≤ −1 dBTP, měřeno po AAC (při přetečení ubere hlasitost v toleranci, pak jemný limiter)
- `nastroje/prompt_motion.py`: katalog prompt-motion.com
- `nastroje/hlidac.py RUN_DIR [--jen-nove]`: hlídač běžícího workflow (spouštět přes Monitor): START / HOTOVO / TICHO > 15 min / LIMIT VÝSTUPU u každého agenta; `--jen-nove` při opětovném zapnutí nepřehrává historii
- ffmpeg: střih, barvy, titulky
- Remotion (React → video) jako alternativa, pokud ho zadání nebo prompt vyžaduje. Plugin Remotion / IT Reelsmaker si uživatel může zapnout.
- `nastroje/hudba.py --nalada vazna|drza|luxusni --delka N --out x.wav [--bpm --drop --konec]`: vlastní hudba do pozadí (syntéza, bez licencí),
  + `x.json` s dobami, takty, dropem a koncem pro synchronizaci animace. Sám kontroluje pásma (telefon pod ~100 Hz nehraje).
- `nastroje/sfx.py`: zvukové efekty syntézou ze seznamu událostí (JSON) → sfx.wav + sfx.json + mix; změřený vrchol přesně na čas události,
  hlasitost `lu` pod hudbou (okno 100 ms, K-vážení). `hudba.json` obsahuje i `udalosti_nastroju` (časy kopáku, marimby… pro synchronizaci obrazu).
- `nastroje/drive.sh ID_NEBO_ODKAZ [cíl]`: stažení souboru nebo celé složky z Google Drive (konektor jen k hledání a malým souborům).
- `nastroje/materialy.py SLOZKA`: příprava materiálů (HEIC → JPG, otočení podle EXIF, HDR / proměnlivé fps / otočení videa), katalog + `_prehled.jpg`.
- **Higgsfield NEPOUŽÍVAT** (rozhodnutí uživatele 2026-10-30). Hlas a případně hudba později přes ElevenLabs (`ELEVENLABS_API_KEY`).
