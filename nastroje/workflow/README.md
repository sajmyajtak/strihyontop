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

- `vyroba-v004.js` (V004, 16 agentů, 3,25 mil. tokenů, 224 min): střihač záběrů ∥ zvukař → animátor klíčové snímky → kreativní ředitel schválí →
  animátor blok 1 → blok 2 + render + zvuk → kolo kontroly (kritik ∥ kreativní ředitel) → opravy animátor ∥ zvukař, max. 3 kola.
  **Pozor (C045)**: v opravném kole zvukař souběžně s animátorem pracoval se starým obrazem. Příště: opravy obrazu → posuny SFX režisér (nebo zvukař
  až po obrazu, se seznamem změn časů od animátora). Rozhodnutí režiséra dávat do úkolu opravy jako číslovaná závazná kritéria (C043).

**Střihový vzor (2026-11-04, `znalosti/strih-vzor.md`)**: do přípravy patří fáze **partitura** (kreativní ředitel: stavy hrdiny, věta na scénu, příchod /
klid / odchod / spojka), oponent ji reviduje podle kontrolního seznamu střihu. Výroba: partitura → obraz → zvuk (zvukař až k hotovému obrazu, D12).
Kontrola: kritik dostává partituru a porovnává ji po snímcích; kreativní ředitel hodnotí střih 3×. Střihač navíc skládá 9:16 prezentaci (A9).

**Pokyny režiséra během běhu (C053, 2026-11-07)**: agentům uvnitř workflow **neposílat SendMessage**, protože vznikne jejich druhá souběžná instance.
Rozhodnutí ke kolu kontroly psát do `zadani.md` („Rozhodnutí režiséra ke kolu kontroly N“) a odkaz do STAV_VYROBY.md. Opravný agent startuje hned po kontrole,
proto ve skriptu oprav dávat do promptu výslovně „nejdřív přečti nejnovější oddíl Rozhodnutí režiséra ke kolu kontroly“; v dalším videu zvážit krátkou pauzu
(např. agent „režisér-brána“ nebo dva workflow: kontrola → režisér rozhodne → opravy).
