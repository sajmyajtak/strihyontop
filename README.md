# strihyontop

Střižna a paměť pro portfolio videa na sociální sítě.

- `CLAUDE.md`: pracovní postup a protokol režiséra (načítá se automaticky)
- `.claude/agents/`: role agentů (analytik, animator, strihac, kritik)
- `znalosti/pravidla-strihu.md`: pravidla, podle kterých se stříhá (rostou s každým videem)
- `znalosti/prompt-motion/`: poznatky a katalog z prompt-motion.com (hlavní zdroj promptů)
- `znalosti/reference/`: rozbory předloh (INDEX.md = přehled)
- `znalosti/chyby.md`: deník chyb a jejich prevence
- `znalosti/pouceni.md`: deník poučení po každém videu
- `znalosti/znacka.md`: logo, barvy, fonty, tón
- `projekty/`: zadání, režijní list, průběh a report jednotlivých videí
- `nastroje/`: rozbor předloh, přepis řeči, render HTML animací, katalog prompt-motion

Jak to funguje: zadání + pravidla + předlohy → režisér naplánuje → animátor / střihač tvoří → kritik kontroluje (max 3 kola)
→ video + report (chyby, tokeny) → zpětná vazba → zapíše se do pravidel → další video je lepší.
