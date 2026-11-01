# Vzory workflow (orchestrace agentů)

Ověřené scénáře pro nástroj Workflow. Pro nový projekt zkopírovat do scratchpadu, přepsat `P`, `M`, `KD`, `CTX` (formát, délka, hudba)
a úkoly podle zadání, zkontrolovat syntaxi a spustit `Workflow({ scriptPath })`. Hlídač: `nastroje/hlidac.py <run_dir>` přes Monitor.

- `priprava.js` (V002): analytik (značka) ∥ zvukař (hudba) → kreativní ředitel (koncept + storyboard) → oponent (energie 3×) → revize. ~36 min, ~0,5 mil. tokenů.
- `vyroba.js` (V002): zvukař (SFX, automatika, mix) ∥ animátor (vozy a klíčové snímky → schválení → pohyb ve 3 blocích → plný render)
  → střihač → 3 kritici (technika, wow + energie, zadání) → opravy, max. 3 kola. Schváleno = žádné blokující ani závažné nálezy, wow ≥ 8, energie ≥ 8,5.

Zásady (C018, C021): agenti `effort: 'high'`, velké výstupy po částech, souběžně nanejvýš 2 agenti (4 CPU), u kontroly hashů dát agentovi konkrétní commit.

**Optimalizace (pokyn uživatele 2026-11-01, „ať každý plní svou práci a není jich hodně“)**: viz CLAUDE.md, Režie. Vzory `priprava.js` a `vyroba.js`
jsou z V002 (víc agentů); pro nová videa je slučovat podle toho pravidla: rozbor předloh dělá kreativní ředitel v konceptu, oponent rovnou reviduje,
kritik technika + zadání je jeden agent, střih a spojení zvuku dělá animátor v posledním bloku nebo režisér, kontrola dalších kol jen opravených míst.
