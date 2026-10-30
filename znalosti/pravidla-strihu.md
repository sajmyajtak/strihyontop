# Pravidla střihu a tvorby videí

Živý dokument. Platí pro **každé** video, pokud zadání konkrétního videa neříká jinak.
Po každé referenci a po každém hotovém videu se doplňuje nebo upravuje.

**Priorita při konfliktu:** pravidla ze zadání konkrétního videa > `znacka.md` > tento dokument.

**Zdroje:** `[R1]`–`[R5]` = rozbory v `reference/`, `[V001]…` = poučení z našich videí (`pouceni.md`),
`[obecné]` = běžná profesní praxe, kterou zatím nepotvrdila žádná reference ani zpětná vazba.

---

## A. Formát a technika
- **A1** Výchozí formát 9:16, **1080×1920**, 30 fps. Pro UI animace a rychlý pohyb 60 fps. `[R1–R5, R4]`
- **A2** Hlasitost **−14 LUFS integrated**, true peak ≤ −1 dBTP. Všech 5 referencí mělo −14,1 až −14,3 LUFS. `[R1–R5]`
- **A3** Export H.264 (High), yuv420p, AAC 48 kHz, `+faststart`. `[obecné]`
- **A4** Délka podle obsahu: logo/showreel smyčka **8–15 s**, příběh/reklama **25–40 s**, vzdělávací/návod **45–75 s**. `[R1–R5]`
- **A5** Bezpečné zóny 9:16: důležitý text ne do horních ~250 px (nadpis/UI), ne do spodních ~400 px (popisek, tlačítka) a ne k pravému okraji ~120 px (ikony). `[obecné]`
- **A6** 4:3 (1080×810) jde použít pro „čistou“ designovou ukázku. R3 v něm měla nejvíc dosahu, ale výchozí zůstává 9:16. `[R3]`

## B. Háček (první 1–3 s)
- **B1** Háček **v první sekundě**: obrazem i textem, ne až po úvodu. `[R2, R3, R4]`
- **B2** Osvědčené typy háčků:
  - šok / emoce: „Holy sh\*t, you are not ready for this“ `[R2]`
  - otázka na bolest diváka: „Does your animation look robotic?“ `[R4]`
  - rychlá sekvence slov: „See it, like it, save it, scroll…“ `[R3]`
  - POV situace z praxe: „POV: Client asked for "cool" logo animation 👀“ `[R5]`
  - provokativní tvrzení: „… just kil\*ed motion designers 🤯“ `[R1]`
- **B3** **Statický nadpis nahoře po celou dobu videa**: bílá zaoblená bublina, černé tučné písmo a emoji na konci, nebo bílý text se stínem. Funguje i bez zvuku. `[R1, R2, R5]`
- **B4** Sporná slova cenzurovat hvězdičkou (kil\*ed, sh\*t), aby je algoritmus neomezil. `[R1, R2]`
- **B5** Video musí dávat smysl **bez zvuku** (titulky a text na obrazovce). `[R2, R4]`

## C. Struktura
- **C1** Reklama / koncept produktu: problém → řešení → komplikace → emoce → slogan → logo. `[R1]`
- **C2** Vzdělávací: háček-otázka → proč to tak je → 2–3 pravidla s vizualizací → hned použitelný tip → CTA. `[R4]`
- **C3** Promo nástroje / služby: háček → tvrzení → důkaz → **před/po srovnání** → kroky návodu → CTA. `[R2]`
- **C4** Koncept / case study: běžná situace → „But what if…“ → řešení → **emoční zvrat** → podpis. `[R3]`
- **C5** Logo / showreel: krátká smyčka, kterou ve videu zopakovat 2–3×. `[R5]`
- **C6** Konec = **end card** (logo, podpis, @jméno), který drží dost dlouho na přečtení. Smí být i dlouhý (R3 ~10 s), protože pomáhá smyčce. `[R1, R3, R4]`
- **C7** Nová informace nebo vizuální změna každé ~1–2 s, v emoční pointě tempo naopak zpomalit. `[R2, R3]`

## D. Střih, rytmus, přechody
- **D1** **Hlas řídí střih**: každá vizuální změna sedí na slovo nebo přízvuk, bez hlasu na dobu hudby. `[R2, R4]`
- **D2** Přechody přednostně **pohybem**, ne tvrdým střihem: souvislá kamera (2D → 3D), match cut, švihový přechod (whip) s rozmazáním, diagonální světelná šmouha, zoom skrz objekt. `[R1, R2, R3]`
- **D3** Tvrdé střihy jen tam, kde dávají rytmus: kroky návodu (~4 s na krok), výčty. `[R2]`
- **D4** Krátké video stavět jako **smyčku**: konec plynule navazuje na začátek. `[R3, R5]`
- **D5** Rozmazání pohybem (motion blur) u každého rychlého pohybu textu, kamery i přechodu. `[R2, R3]`

## E. Typografie a titulky
- **E1** **Kinetický text slovo po slově** synchronně s hlasem. `[R2, R4]`
- **E2** Aktivní / klíčové slovo zvýraznit: barevný štítek pod slovem `[R4]`, akcentní barva `[R2]`, větší velikost `[R2, R3]`.
- **E3** Tučné, výrazné bezpatkové písmo, VERZÁLKY pro důraz („COLLECTION“, „HELL YES.“). `[R2, R3]`
- **E4** Jedna rodina písma, max. 2 řezy + případně ruční písmo. `[R2, R4]`
- **E5** **Ručně psané anotace** (šipky, kroužky, „like it“, „Forever“) dodají lidský dojem. `[R3]`
- **E6** Animace písma: roztažení (stretch), maska, rozmazání, změna prostrkání. `[R2]`
- **E7** Titulky ve spodní třetině uprostřed, ale nad bezpečnou zónou (A5). `[R4, obecné]`

## F. Pohyb (easing): platí pro každou animaci
- **F1** **Nic se nehýbe lineárně.** `[R4]`
- **F2** **Co přichází → ease-out** (přijede rychle, dlouho dobržďuje). `[R4]`
- **F3** **Co odchází → ease-in** (pomalu se rozjede, pak zmizí). `[R4]`
- **F4** **UI prvky (tlačítka, karty, notifikace, logo „pop“) → pružina s malým překmitem.** `[R1, R4]`
- **F5** Kamera se hýbe plynule, s paralaxou a s přechodem z 2D do 3D, kde to dává smysl. `[R1]`
- **F6** Zadání pro animace v kódu vždy obsahuje: *„Entrances: ease out. Exits: ease in. Interface: spring, slight overshoot. Nothing linear.“* `[R4]`

## G. Barvy a vzhled
- **G1** Omezená paleta: **neutrální pozadí + 1–2 akcenty**. `[R2, R4, R5]`
  - černá + limetkově žlutá + růžová `[R2]`
  - téměř černá + červená `[R4]`
  - tmavě fialová + neonově růžová `[R5]`
- **G2** Tmavé pozadí + neonový akcent + záře (glow) = prémiový tech dojem. `[R2, R4, R5]`
- **G3** Emoční momenty: teplé světlo, vinětace, zrnitost. `[R3]`
- **G4** Jednotný UI systém: karty se zaoblenými rohy, jemné okraje, malé štítky, monospace popisky. `[R4]`
- **G5** Barvy značky (`znacka.md`) mají přednost před paletami z referencí.

## H. Formát „natočená obrazovka“
- **H1** Animaci přehrát na notebooku nebo monitoru a natočit telefonem v tmavé místnosti, barevné ambientní světlo ladí s paletou. Působí opravdově a „ne jako AI“. `[R1, R2, R5]`
- **H2** Pomalý ruční nájezd kamery, na začátku ruka zmáčkne klávesu (start). `[R1]`
- **H3** Ukázat software / časovou osu / prompt = důkaz řemesla. `[R2, R5]`
- **H4** Já sám natáčet neumím: buď natočí uživatel podle těchto pravidel, nebo to digitálně nasimuluju (maketa notebooku, perspektiva, odlesky, ambient). `[obecné]`

## I. Zvuk
- **I1** Hlas: krátké věty, sebevědomý, rychlý; pauzy a přeřeky vystřihnout. `[R2, R4]`
- **I2** Hudba pod hlasem nesmí přehlušit řeč (hudba cca 15–20 dB pod hlasem). `[obecné]`
- **I3** Zvukové efekty k přechodům (whoosh), textu (pop) a UI (klik) jemně, ne na každý pohyb. `[obecné]`
- **I4** Trendy zvuky z IG/TikTok knihovny se přidávají až v aplikaci při publikaci → dodat i verzi **bez hudby**. `[obecné]`

## J. CTA, popisek, publikace
- **J1** CTA s **klíčovým slovem**: „Comment PROMPT“, „comment KATANA“, „DM me UGOKI“ (automatická DM). `[R1, R2, R4]`
- **J2** Pro služby: „Need one? Open for commissions“. `[R5]`
- **J3** Popisek končí **otázkou** pro komentáře („What do you think?“). `[R3]`
- **J4** 3–5 relevantních hashtagů, ne desítky. `[R1, R4, R5]`
- **J5** Práce s cizí značkou (koncepty, spec reklamy) **vždy** s disclaimerem: „Spec ad, not affiliated with X“ / „Unofficial concept“. `[R1, R3]`
- **J6** Názor a postoj (např. „vyrobeno člověkem“) přináší komentáře a sdílení. `[R3]`

## K. Kontrola před odevzdáním
- [ ] Háček v 1. sekundě, funguje bez zvuku
- [ ] Rozlišení, fps a délka podle zadání (A1, A4)
- [ ] −14 LUFS ±1, true peak ≤ −1 dBTP (změřit `ebur128`)
- [ ] Žádný text v bezpečných zónách (A5)
- [ ] Žádný lineární pohyb (F1–F4)
- [ ] Titulky bez překlepů a správně načasované
- [ ] End card + CTA
- [ ] Splněna všechna pravidla ze zadání videa
- [ ] Náhledový arch prohlédnutý snímek po snímku
