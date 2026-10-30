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
Podřízení agenti (`.claude/agents/`): **analytik** (předlohy, výběr promptu), **animator** (motion grafika, HTML → MP4),
**strihac** (záběry, titulky, zvuk, export), **kritik** (nezávislá kontrola). Když typ agenta není v této session načtený,
spustit `general-purpose` s instrukcí „přečti `.claude/agents/<role>.md` a jednej podle něj“.

1. **Příjem**: založit `projekty/0xx-nazev/zadani.md` ze šablony. Pravidla uživatele **doslova**, mají nejvyšší prioritu.
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
kritik neschválil ani po 3 kolech; něco stojí peníze nebo kredity (Higgsfield); právní riziko (cizí značka, licence hudby).

### Report uživateli (vždy v tomto tvaru, česky, stručně)
```
VÝSLEDEK: soubor / odkaz, délka, formát, 1–2 věty co video je
PRŮBĚH: počet kol kontroly, verdikt kritika
CHYBY VYŘEŠENÉ AUTOMATICKY: počet + 1 řádek ke každé závažné
CHYBY, KTERÉ POTŘEBUJU OD TEBE: (jen blokující) co, proč, co navrhuju
SPOTŘEBA TOKENŮ: tabulka agent → tokeny (z výsledků Agent nástroje) + součet; hlavní chat: viz poznámka v pouceni.md
```

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
- `nastroje/render_html.cjs`: HTML scéna s `window.seek(t)` → MP4 snímek po snímku s rozmazáním pohybem; `--nahled 0.5` = jen kontrolní snímky. ~8 s výpočtu na 1 s videa 1080×1920 (3 podsnímky).
- `nastroje/vzory/scena.html`: kostra scény (easing podle pravidel F, pružina s nastavitelným překmitem, `?mrizka` = bezpečné zóny)
- `nastroje/prompt_motion.py`: katalog prompt-motion.com
- ffmpeg: střih, barvy, titulky, hlasitost (`loudnorm` na −14 LUFS)
- Remotion (React → video) jako alternativa, pokud ho zadání nebo prompt vyžaduje. Plugin Remotion / IT Reelsmaker si uživatel může zapnout.
- Higgsfield MCP (AI generování obrazu a videa) stojí kredity. Používat **jen po odsouhlasení** uživatelem.
