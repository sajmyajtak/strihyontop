# Značka a výchozí nastavení

Výchozí hodnoty pro každé video. Konkrétní zadání je vždy přebíjí.

| | |
|---|---|
| Jazyk videí | **angličtina** (texty na obrazovce, titulky, CTA) |
| Voiceover | **zatím žádný.** Později hlas přes **ElevenLabs** (API klíč v prostředí jako `ELEVENLABS_API_KEY`, zatím nenastaveno) |
| Hudba | **vytvářet ke každému videu podle tónu** (vážný / drzý / luxusní …): „fakt dobrou hudbu do pozadí“. Nástroj `nastroje/hudba.py`; až bude ElevenLabs, zvážit Eleven Music |
| Barvy | **podle typu videa**, uživatel je pošle v zadání |
| Fonty | podle zadání. Jinak výrazné bezpatkové z Google Fonts (ověřeno: Anton, Inter) |
| Tón | podle zadání (vážný / drzý / luxusní …) |
| CTA na konci | **podle zadání** |
| Materiály | **Google Drive** (viz níže) |
| Platformy | IG Reels / TikTok / Shorts, 9:16 (pokud zadání neříká jinak) |
| Logo, podpis na end card | ? (zatím nedodáno) |
| Zakázané nástroje | **Higgsfield nepoužívat** (rozhodnutí uživatele 2026-10-30) |

## Materiály na Google Drive
- Konektor Google Drive najde soubory a složky (`search_files`, `parentId = 'ID_SLOZKY'`). Stahovat přes něj jen malé soubory (logo, texty):
  vrací je jako base64 do konverzace.
- Videa a velké soubory: `nastroje/drive.sh ID_NEBO_ODKAZ [cíl]` → `media/materialy/`. Funguje pro soubory sdílené „kdokoli s odkazem“.
  Když nástroj ohlásí HTML místo dat, požádat uživatele o sdílení odkazem.

| datum | soubor | kde je uložen | poznámka |
|---|---|---|---|
| 2026-10-30 | složky „Mossaic“, „Zlatnictví“ (videa 13–35 MB, 9:16, 25 fps) | Google Drive uživatele | jen zjištěno při testu přístupu, zatím bez zadání |
