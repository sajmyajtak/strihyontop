# Pravidla střihu a tvorby videí

Živý dokument. Platí pro **každé** video, pokud zadání konkrétního videa neříká jinak.
Po každé referenci a po každém hotovém videu se doplňuje nebo upravuje.

**Priorita při konfliktu:** pravidla ze zadání konkrétního videa > `znacka.md` > tento dokument.
Předloha, kterou uživatel výslovně pošle k danému videu, smí přebít i výchozí zákazy (např. šmouhy v D2, záři v G2). Výjimku zapsat do zadání.

**Zdroje:** `[R1]`–`[R5]` = rozbory v `reference/`, `[PM]` = prompt-motion.com (`prompt-motion/poznatky.md`),
`[V001]…` = poučení z našich videí (`pouceni.md`), `[obecné]` = profesní praxe, kterou zatím nepotvrdila reference ani zpětná vazba.

---

## A. Formát a technika
- **A1** Výchozí formát 9:16, **1080×1920**. **Animace z kódu 60 fps**, natočený materiál v nativních fps (obvykle 30).
  30 fps u animace jen tam, kde je pohyb pomalý a šetří se čas renderu. `[R1–R5, PM]`
- **A2** Hlasitost **−14 LUFS integrated**, true peak ≤ −1 dBTP, **měřeno po zakódování do AAC** (`nastroje/master_zvuk.sh`). Všech 5 referencí mělo −14,1 až −14,3 LUFS. `[R1–R5, PM]`
- **A3** Export H.264 (High), yuv420p, AAC 48 kHz, `+faststart`. `[obecné]`
- **A4** Délka podle obsahu: logo/showreel smyčka **8–15 s**, příběh/reklama **25–40 s**, vzdělávací/návod **45–75 s**. `[R1–R5]`
- **A5** Bezpečné zóny 9:16: důležitý text ne do horních ~250 px, spodních ~400 px ani k pravému okraji ~120 px. `[obecné]`
- **A6** 4:3 (1080×810) jde použít pro „čistou“ designovou ukázku. R3 v něm měla nejvíc dosahu, ale výchozí zůstává 9:16. `[R3]`
- **A8** **Hrdina musí být na telefonu velký**: hlavní objekt zabírá zhruba ≥ 75 % šířky obrazu nebo ≥ 45 % výšky v klíčových momentech
  a obraz je svisle vyvážený, bez prázdné poloviny (spodních ~400 px pro UI se nepočítá). Drobné změny (mezera 2 px, posun 4 px) na telefonu
  nikdo nevidí: stupňování musí být vidět na zmenšenině 270 px. `[V001 kontrola 1]`
- **A7** Předlohu 16:9 nebo 1:1 pro 9:16 **přeskládat, ne oříznout**: řady pod sebe, kamera svisle, souřadnice přepočítat. 81 % katalogu prompt-motion je 16:9. `[PM]`

## B. Háček (první 1–3 s)
- **B1** Háček **v první sekundě**, obrazem i textem, ne až po úvodu. `[R2, R3, R4]`
- **B2** Osvědčené typy háčků:
  - šok / emoce: „Holy sh\*t, you are not ready for this“ `[R2]`
  - otázka na bolest diváka: „Does your animation look robotic?“ `[R4]`
  - rychlá sekvence slov: „See it, like it, save it, scroll…“ `[R3]`
  - POV situace z praxe: „POV: Client asked for "cool" logo animation 👀“ `[R5]`
  - provokativní tvrzení: „… just kil\*ed motion designers 🤯“ `[R1]`
- **B3** **Statický nadpis nahoře** patří k formátu „natočená obrazovka“ a POV/meme: jedna věta nesoucí háček, pod horní bezpečnou zónou.
  Styl: bílá zaoblená bublina, černé tučné písmo, emoji na konci, nebo bílý text se stínem.
  **Do čistých motion videí (showreel, logo, produktový film) ho nevkládat.** Nadpis dávat až ve střihu jako samostatnou vrstvu a vždy dodat i čistou verzi. Žádné drobné popisky, štítky ani „HUD“ v rozích. `[R1, R2, R5, PM]`
- **B4** Sporná slova cenzurovat hvězdičkou (kil\*ed, sh\*t), aby je algoritmus neomezil. `[R1, R2]`
- **B5** Video musí dávat smysl **bez zvuku** (titulky a text na obrazovce). `[R2, R4]`
- **B6** **Snímek 0 je hotový, silný obraz** (slouží jako náhled): žádné zatmívání z černé ani úvodní logo. První obsahový moment do ~2 s. `[PM]`

## C. Struktura
- **C1** Reklama / koncept produktu: problém → řešení → komplikace → emoce → slogan → logo. `[R1]`
- **C2** Vzdělávací: háček-otázka → proč to tak je → 2–3 pravidla s vizualizací → hned použitelný tip → CTA. `[R4]`
- **C3** Promo nástroje / služby: háček → tvrzení → důkaz → **před/po srovnání** → kroky návodu → CTA. `[R2]`
- **C4** Koncept / case study: běžná situace → „But what if…“ → řešení → **emoční zvrat** → podpis. `[R3]`
- **C5** Logo / showreel: krátká smyčka, ve videu zopakovaná 2–3×. `[R5]`
- **C6** Konec = **end card** (logo, podpis, @jméno, CTA). Drží **1,5–3 s**, ve smyčce stačí 1–1,5 s, s jemným pohybem (dotlačení 2–4 %), nikdy zamrzlý obraz.
  Dlouhý podpis (~10 s, R3) jen u konceptů, kde end card nese text nebo manifest. `[R1, R3, R4, PM]`
- **C7** Nová **myšlenka** každých ~1,5–2 s, drobná vizuální **událost** na každou dobu hudby. V emoční pointě tempo zpomalit (jediné záměrné ticho ~0,4 s).
  Uvnitř videa žádné zastavení > 1 s bez textu ke čtení. `[R2, R3, PM]`
- **C8** **Fakta a čísla nevymýšlet** (procenta, jména zákazníků, výsledky). Čísla jen ověřená od uživatele, jinak zjevně ukázková. Texty značky citovat doslova. `[PM]`

## D. Střih, rytmus, přechody
- **D1** **Hlas řídí střih**: každá vizuální změna sedí na slovo nebo přízvuk, bez hlasu na dobu hudby. `[R2, R4, PM]`
- **D2** Přechody tak, že **další scéna vzniká z předchozí**: sdílený prvek (tlačítko se rozroste do stránky, tečka se změní v logo), morf tvaru,
  zaplavení barvou z objektu (přes všechny 4 rohy, ~0,3 s), match cut, souvislá kamera, zoom skrz objekt.
  **Whip a světelná šmouha nanejvýš 1× za video** jako akcent. Nikdy prolínačka celých scén, náhodný wipe, spin ani glitch. `[R1, R2, R3, PM]`
- **D3** Tvrdé střihy jen tam, kde dávají rytmus: kroky návodu (~4 s na krok), výčty. `[R2]`
- **D4** Krátké video stavět jako **smyčku**: poslední snímek navazuje na první včetně polohy a rychlosti prvků. `[R3, R5, PM]`
- **D5** Rozmazání pohybem: (1) v kódu podle rychlosti a směru (svislý švih = svislá šmouha), (2) render s podsnímky **4 u běžného pohybu, 6–8 u rychlých přechodů**
  (méně dělá „duchy“, C003). Statický text a UI zůstávají ostré a rozmazání nesmí tvar úplně smazat. `[R2, R3, PM]`
- **D6** **Žádný pohyb bez příčiny**: každá animace vychází z prvku, který už je na obrazovce, nebo do něj vede. Nic se nepřesouvá skokem.
  Odcházející text zmizí dřív, než příchozí obsadí jeho místo. `[PM]`

## E. Typografie a titulky
- **E1** Slovo po slově **jen tam, kde text čte hlas** (titulky, háček). Slovo naskočí přesně s hlasem (`prepis.py --slova`, při nepřesnosti zarovnat po frázích).
  **Nadpisy a hesla bez hlasu se hýbou jako jeden navržený objekt** (maska, roztažení, morf). `[R2, R4, PM]`
- **E2** Klíčové slovo zvýraznit barvou, řezem nebo velikostí. Štítek jen jako **navržený** prvek: zaoblená pilulka, která přijede pružinou (R4),
  nebo tah zvýrazňovače přes frázi. **Nikdy ostrý obdélník přesně za písmeny** (vypadá jako označený text). `[R2, R3, R4, PM]`
- **E3** Tučné, výrazné bezpatkové písmo, VERZÁLKY pro důraz („COLLECTION“, „HELL YES“). `[R2, R3]`
- **E4** Jedna rodina písma, max. 2 řezy + případně ruční písmo. Font musí mít českou diakritiku (latin-ext). `[R2, R4, PM]`
- **E5** **Ručně psané anotace** (šipky, kroužky, „like it“, „Forever“) dodají lidský dojem. `[R3]`
- **E6** Animace písma: roztažení (stretch), maska, rozmazání, změna prostrkání. `[R2]`
- **E7** Titulky ve spodní třetině uprostřed, nad bezpečnou zónou (A5). Hlavní nadpis ≥ 110 px, titulky ≥ 56 px při šířce 1080. `[R4, PM, obecné]`
- **E8** Krátká hesla a titulky **bez tečky na konci**. Tečka jen jako záměrná pointa. `[PM]`

## F. Pohyb (easing): platí pro každou animaci
- **F1** **Nic se nehýbe lineárně.** `[R4]`
- **F2** **Co přichází → ease-out** (přijede rychle, dlouho dobržďuje). `[R4]`
- **F3** **Co odchází → ease-in** (pomalu se rozjede, pak zmizí). `[R4]`
- **F4** **UI prvky** (tlačítka, karty, notifikace, pop loga) → pružina s překmitem **2–5 % (výchozí 3 %)**, jednou, bez houpání.
  Velké plochy, kamera, text a usazování → kriticky tlumené (bez překmitu). Výraznější překmit jen u hravých videí a postav. `[R1, R4, PM]`
- **F5** Kamera se hýbe plynule, s paralaxou a s přechodem z 2D do 3D, kde to dává smysl. `[R1]`
- **F6** Zadání pro animace v kódu vždy obsahuje: *„Entrances: ease out. Exits: ease in. Interface: spring, slight overshoot. Nothing linear.
  Springs are closed-form, tiny overshoot. Every frame is a pure function of time. Blur follows speed and direction.“* `[R4, PM]`
- **F7** **Jeden jazyk kamery**: jeden svět, jedna kamera (posun + zoom v logaritmické škále). Nikdy dva pohyby kamery naráz, nikdy zoom tam a hned zpátky.
  Kamera se mezi scénami neresetuje. Pomalé dotlačení během scény (1,00 → 1,04) drží obraz živý. `[PM]`

## G. Barvy a vzhled
- **G1** Omezená paleta: **neutrální pozadí + 1–2 akcenty** (max 3 barvy + černá/bílá). `[R2, R4, R5, PM]`
  - černá + limetkově žlutá + růžová `[R2]`
  - téměř černá + červená `[R4]`
  - tmavě fialová + neonově růžová `[R5]`
- **G2** Tmavé pozadí + jeden akcent působí prémiově. **Záře jen tam, kde je sama konceptem nebo zdrojem světla**: neonové logo / nápis (R5),
  jeden zvýrazněný prvek nebo wordmark na end card. Nikdy na UI textu ani titulcích a nikdy jako dekorace všeho. Záře je nejčastější AI poznávací znak. `[R2, R4, R5, PM]`
- **G3** Emoční momenty: teplé světlo, vinětace, zrnitost. `[R3]`
- **G4** Jednotný UI systém: karty se zaoblenými rohy, jemné okraje, malé štítky, monospace popisky. `[R4]`
- **G5** Barvy značky (`znacka.md`) mají přednost před paletami z referencí.
- **G6** **AI poznávací znaky** (`prompt-motion/poznatky.md`, oddíl 4) jsou ve výchozím stavu **zakázané**: záře, výbuchy částic, odlesky, třes kamery,
  RGB split, prolínačky scén, generické gradienty, skákavý easing, text v rozích, „cokoli, co vypadá jako šablona“. Výjimku musí zdůvodnit koncept a zapisuje se do zadání. `[PM]`

## H. Formát „natočená obrazovka“
- **H1** Animaci přehrát na notebooku nebo monitoru a natočit telefonem v tmavé místnosti, barevné ambientní světlo ladí s paletou. Působí opravdově a „ne jako AI“. `[R1, R2, R5]`
- **H2** Pomalý ruční nájezd kamery, na začátku ruka zmáčkne klávesu (start). `[R1]`
- **H3** Ukázat software / časovou osu / prompt = důkaz řemesla. `[R2, R5]`
- **H4** Já sám natáčet neumím: buď natočí uživatel podle těchto pravidel, nebo to digitálně nasimuluju (maketa notebooku, perspektiva, odlesky, ambient). `[obecné]`

## I. Zvuk
- **I1** Hlas: krátké věty, sebevědomý, rychlý. Pauzy a přeřeky vystřihnout. `[R2, R4]`
- **I2** Hudba pod hlasem s **duckingem** (ztlumení jen během řeči). Cíl: hlas **≈ 9–12 dB nad hudbou v pásmu řeči 300 Hz–4 kHz**, kontrolovat po frázích.
  Paušálních 15–20 dB jen u husté, hlasité hudby. `[PM, obecné]`, ověřit na prvním videu s hlasem
- **I3** SFX na každou **událost** v obraze (klik, dopad, pop, otevření, logo), ne na každý pohyb. Umístit tak, aby **změřený vrchol** zvuku padl na událost.
  Běžné efekty tiše pod hudbou. **Klíčové momenty (drop, pointa, gag, logo) musí být slyšet**: efekt na úrovni hudby nebo nad ní
  (cca 0 až −3 LU v okně 100 ms) a hudba kolem nich ustoupí. **Nádech před dropem a „ticho jako pointa“ = hudba opravdu ztichne**
  (ne jen řidší aranžmá). U prémiových značek jemné kliky a měkký dopad na logo, žádné hlasité whooshe všude. `[PM, V001 kontrola 1]`
- **I4** Trendy zvuky z IG/TikTok knihovny se přidávají až v aplikaci při publikaci → dodat i verzi **bez hudby**. `[obecné]`
- **I5** Hudba a SFX jen s **licencí pro komerční použití**, zdroje zapsat do zadání. Hudba z `nastroje/hudba.py` je naše vlastní (syntéza v kódu). `[PM]`
- **I6** Ke každému videu **vlastní hudba podle tónu** (vážný / drzý / luxusní …), nálada a BPM do režijního listu. Animace se řídí `hudba.json`
  (doby, takty, drop, konec): drop = nejsilnější vizuální moment, konec = end card. `[uživatel 2026-10-30]`
- **I7** Mix hudby musí znít i z **telefonu**: sub (20–60 Hz) max ~30 % energie, středy (250 Hz–2 kHz) ≥ 30 %, basa s vyššími harmonickými.
  `hudba.py` to hlídá a varuje. `[R5, C012]`
- **I8** Zatím **bez voiceoveru**. Hlas později přes ElevenLabs. Jazyk videí je **angličtina**. `[uživatel 2026-10-30]`

## J. CTA, popisek, publikace
- **J1** CTA s **klíčovým slovem**: „Comment PROMPT“, „comment KATANA“, „DM me UGOKI“ (automatická DM). `[R1, R2, R4]`
- **J2** Pro služby: „Need one? Open for commissions“. `[R5]`
- **J3** Popisek končí **otázkou** pro komentáře („What do you think?“). `[R3]`
- **J4** 3–5 relevantních hashtagů, ne desítky. `[R1, R4, R5]`
- **J5** Práce s cizí značkou (koncepty, spec reklamy) **vždy** s disclaimerem: „Spec ad, not affiliated with X“ / „Unofficial concept“. `[R1, R3]`
- **J6** Názor a postoj (např. „vyrobeno člověkem“) přináší komentáře a sdílení. `[R3]`

## K. Kontrola před odevzdáním
Technický podklad: `nastroje/kontrola.sh VIDEO media/kontrola/<projekt>/kolo<n>`. Pak nezávislý kritik.
- [ ] Háček v 1. sekundě, snímek 0 je hotový obraz, funguje bez zvuku (B1, B5, B6)
- [ ] Před plným renderem: snímek na každou dobu (`--nahled doby --bpm …`) nebo každých 0,5 s + 4 klíčové snímky v plném rozlišení
- [ ] Rozlišení, fps a délka podle zadání (A1, A4)
- [ ] −14 LUFS ±1, true peak ≤ −1 dBTP, změřeno **po** zakódování do AAC (A2)
- [ ] Žádný text v bezpečných zónách (A5), titulky bez překlepů a správně načasované, česká diakritika
- [ ] Žádný lineární pohyb, přehnaná pružina ani pohyb bez příčiny (F1–F4, D6)
- [ ] Žádný zamrzlý úsek > 1 s bez textu, žádné prázdné snímky, žádné probliknutí (pásy snímků z `kontrola.sh` prohlédnuté)
- [ ] Hranice smyčky snímek po snímku (D4)
- [ ] Žádný AI poznávací znak bez zdůvodnění v zadání (G6)
- [ ] Čísla a fakta ověřená (C8)
- [ ] End card + CTA (C6, J1)
- [ ] Splněna všechna pravidla ze zadání videa
