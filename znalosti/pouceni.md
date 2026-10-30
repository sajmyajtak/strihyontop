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
- Prostředí: 4 CPU, bez GPU. Render 1080×1920 krátkých videí je v pohodě, dlouhé 3D scény budou pomalé.
- `render_html.cjs`: ~8 s výpočtu na 1 s videa 1080×1920 při 30 fps a 3 podsnímcích (15s video ≈ 2 min). Při 60 fps nebo `--sub 6` počítat 2× déle.
- prompt-motion.com: data jsou ve stránce (Next.js RSC payload), stahuje se bez přihlášení. robots.txt: `use=reference`, `ai-train=no`, `/api/` zakázáno.
  Odkazy na zdroj: holý profil x.com/p4nthera_ je autor webu, ne tvůrce videa.
