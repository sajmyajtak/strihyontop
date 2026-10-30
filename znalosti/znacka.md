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
**Jediný zdroj materiálů pro nová videa je složka „Střižna – materiály pro portfolio“** (kořen Disku, založena 2026-10-30).
Staré složky (Zlatnictví, Mossaic aj.) **nepoužívat**, rozhodnutí uživatele.

```
Střižna – materiály pro portfolio/
  01 Projekty – každé video vlastní složka/   ← materiály k videu (uživatel v zadání řekne název podsložky)
  02 Logo a značka/                           ← logo, fonty, barvy
  03 Hotová videa/                            ← sem si uživatel ukládá výsledky (já doručuji do chatu)
  JAK SEM NAHRÁVAT                            ← návod pro uživatele
```
- **ID složek nepatří do gitu** (repozitář je veřejný a složka je sdílená odkazem). Najít konektorem podle názvu:
  `search_files: title = 'Střižna – materiály pro portfolio' and mimeType = 'application/vnd.google-apps.folder'`, pak `parentId = '<ID>'`.
- Stažení celé podsložky projektu: `nastroje/drive.sh "https://drive.google.com/drive/folders/<ID>" media/materialy/<projekt>`
  (gdown, max. 50 souborů na složku), pak `python3 -I nastroje/materialy.py media/materialy/<projekt>` → katalog, varování, `_prehled.jpg`.
- Konektor na stahování nepoužívat (base64 do konverzace). Sdílení musí být „Kdokoli s odkazem: Čtenář“. Nastavuje uživatel,
  konektor umí sdílet jen s konkrétními e-maily. Když stažení vrátí HTML místo dat, sdílení chybí.
