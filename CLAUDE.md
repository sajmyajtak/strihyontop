# Střižna: portfolio videa pro sociální sítě

Tento repozitář je **trvalá paměť** pro střih a tvorbu videí. Kontejner se maže, repozitář zůstává.
Uživatel posílá zadání, pravidla, předlohy (odkazy na reels / soubory) a materiály. Já stříhám a tvořím videa,
všechno zapisuju a **každé další video stavím na všem, co jsem se naučil**. Komunikace česky.

## Na začátku každé session
1. `bash nastroje/setup.sh` (yt-dlp, faster-whisper; ffmpeg je v systému)
2. Přečíst `znalosti/pravidla-strihu.md`, `znalosti/znacka.md` a `znalosti/pouceni.md`.
3. Pokud běží rozpracovaný projekt, přečíst jeho `projekty/0xx-*/zadani.md`.

## Když přijde předloha (odkaz nebo video)
1. `nastroje/analyzuj.sh ODKAZ R<n>-kratky-nazev` stáhne video a vytvoří metadata, střihy, hlasitost, přepis a náhledový arch do `media/reference/…`.
   Instagram stahovat po jednom (při 429 počkat ~1 min). TikTok nejde → požádat o soubor.
2. Prohlédnout náhled, případně detailní snímky (`ffmpeg -ss … -frames:v 1`), přepis porovnat s obrazem.
3. Zapsat rozbor do `znalosti/reference/R<n>-….md` podle vzoru R1, zmenšený náhled (šířka 1200, `-q:v 6`) do `znalosti/reference/nahledy/`, řádek do `INDEX.md`.
4. Nové poznatky přidat do `znalosti/pravidla-strihu.md` se zdrojem `[R<n>]`. Když reference odporuje stávajícímu pravidlu, pravidlo upravit a napsat proč.

## Když přijde zadání videa
1. Založit `projekty/0xx-nazev/zadani.md` ze `projekty/_sablona/`. Pravidla uživatele zapsat **doslova**, ta mají nejvyšší prioritu.
2. Vypsat, která pravidla z `pravidla-strihu.md` se uplatní, a sestavit časovou osu. Když něco zásadního chybí (materiál, text, CTA), zeptat se.
3. Stříhat / animovat. Pracovní soubory patří do `media/` (necommituje se).
4. Projít kontrolní seznam K, prohlédnout náhledový arch výsledku a změřit hlasitost.
5. Doručit uživateli (SendUserFile, velké soubory přes Google Drive) a **zeptat se na zpětnou vazbu**.

## Po zpětné vazbě
1. Zpětnou vazbu doslova do `zadani.md` projektu.
2. Záznam do `znalosti/pouceni.md`. Obecně platná poučení přenést do `pravidla-strihu.md` se zdrojem `[V0xx]`.
3. Commit + push. Paměť platí jen to, co je pushnuté.

## Ukládání
- Commitovat: všechny `.md`, nástroje, malé náhledy (jpg). **Necommitovat** videa ani zvuk (`.gitignore`, složka `media/`).
- Materiály od uživatele evidovat v `znalosti/znacka.md` (tabulka Materiály): co to je a kde to leží.
- Po každé změně znalostí commit a push na aktuální pracovní větev.

## Nástroje
- `nastroje/analyzuj.sh`: rozbor reference
- `nastroje/prepis.py`: přepis řeči (`--slova` = časy slov pro titulky, `--model medium --jazyk cs` pro češtinu)
- ffmpeg: střih, barvy, titulky, hlasitost (`loudnorm` na −14 LUFS)
- Pro motion design a logo animace: Remotion (React → video), pokud je k dispozici. Plugin Remotion / IT Reelsmaker si uživatel může zapnout.
- Higgsfield MCP (AI generování obrazu a videa) stojí kredity. Používat **jen po odsouhlasení** uživatelem.
