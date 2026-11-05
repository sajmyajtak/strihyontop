# Deník chyb

Každá chyba, která se při tvorbě objeví (i drobná a hned opravená), sem patří. Zapisuje režisér.
Cíl: **žádná chyba dvakrát**. Každý záznam končí prevencí, která se propíše do pravidel, protokolu, nástroje nebo instrukcí agenta.

```
### C0xx – krátký název (datum, projekt V0xx, kdo: režisér/animátor/střihač/kritik/nástroj)
- Příznak: co se stalo / co kritik našel
- Příčina:
- Oprava:
- Prevence: co se změnilo a kde (soubor), aby se to neopakovalo
```

---

### C051: Dvě masky BiRefNet souběžně = nedostatek paměti (2026-11-05, V005, režisér)
- Příznak: úloha masek režiséra skončila `Killed` (rc 137); dmesg: „Memory cgroup out of memory“ u dvou procesů python3 (7,4 GB a 6,5 GB RSS).
- Příčina: BiRefNet (rembg, CPU) bere 6,5–7,4 GB RAM na proces; kontejner má 16 GB, animátor si souběžně pustil vlastní BiRefNet na fotku F1.
- Oprava: úloha masek se spouští ve smyčce, která počká, až neběží jiný BiRefNet, a po zabití naváže (hotové masky přeskakuje, zápis atomicky).
- Prevence: v jednu chvíli jen jeden BiRefNet; v zadání agentů uvést, kdo masky počítá; skripty masek obnovitelné (přeskočit hotové, atomický zápis).

### C050: Na střihu ve stopáži vznikl prolnutý snímek obou záběrů (2026-11-05, V005 test, našel animátor)
- Příznak: v testu T8 byl na hranici dvou záběrů stopáže jeden snímek, kde se prolínaly oba záběry (dvojexpozice).
- Příčina: výměna desky 30 fps padala přesně na čas výstupního snímku; podsnímky závěrky (vystředěné kolem času snímku) tak zprůměrovaly snímky obou záběrů.
- Oprava: deska i úsek se vybírají z času zaokrouhleného na výstupní snímek (`casDesky` / `snimekDesky` v `nastroje/vzory/scena.html`).
- Prevence: ve vzoru scény; animátor používá `snimekDesky` pro každou stopáž; kritik kontroluje snímky kolem každého střihu ve stopáži.

### C049: `materialy.py` spadl na přehledu při 220 souborech (2026-11-04, V005, opravil analytik)
- Příznak: `_prehled.jpg` se neuložil, výška archu přesáhla limit formátu JPEG (65 535 px).
- Příčina: všechny řádky náhledů se lepily do jednoho obrázku bez ohledu na počet souborů.
- Oprava: přehled se dělí na `_prehled.jpg`, `_prehled_2.jpg`, … po max. 60 000 px.
- Prevence: v nástroji; u velkých složek prohlédnout všechny díly přehledu.

### C048: Lokální retuš stopáže udělala viditelnou skvrnu (2026-11-01, V004 v4b, režisér, našli kritik i kreativní ředitel)
- Příznak: ztlumení hvězdy odlesku v B_1280 (kruhová maska −1,3 EV, r 190 px) přesahovalo ze skla na světlý písek: tmavá kulatá skvrna ~200–250 px
  jela s hranou střechy 22,10–22,27, působila jako špína na objektivu. Druhý pokus (ztlumit jen světlé tóny) udělal z hvězdy tmavou díru s prstencem,
  třetí (razítko ze skla vedle) tmavší kotouč a zub na hraně střechy.
- Příčina: zásah do skutečného záběru maskou, která nesleduje tvar objektu ani jas okolí; kontrolní snímky režisér prošel jen zmenšené.
- Oprava (v4c): hvězdu jen měkce rozostřit (blur 14 px, měkký kruh r 70) a jen ve snímcích, kde leží uvnitř skla (22,0–22,2), u hrany nic. Výsledek: rozptýlený odlesk bez hvězdy.
- Prevence: retuš stopáže jen tam, kde zásah nemůže přetéct na jiný povrch (nebo v masce objektu), přednost má rozostření / změkčení před ztmavením a razítkem;
  kontrolovat výřez v plném rozlišení po snímcích a porovnat s verzí bez zásahu (`animator.md`).

### C047: Ding posunutý z dosednutí kvůli souběhu s jiným zvukem (2026-11-01, V004 v4, režisér, našli kritik a kreativní ředitel)
- Příznak: ding karty 250 km/h zněl 22,60, číslo ale dosedlo 22,38; ding 500 kW 19,58 proti dosednutí 19,45.
- Příčina: režisér posunul ding 250 za vrchol průjezdu 22,52, aby ho průjezd nezakryl; ding 500 zůstal z odhadu zvukaře (konec rolování místo ostrého snímku).
- Oprava (v4b): rolování zkráceno (G9), dingy na první ostrý snímek (500 19,21 · 3.8 21,35 · 250 22,17), průjezd zůstal 22,52 jako samostatný úder.
- Prevence: G9 doplněno („ding na první ostrý snímek, při kolizi se posouvá druhý zvuk“), `zvukar.md`.

### C046: Karta faktu stála krátce a při odchodu zůstal prázdný obdélník 3 snímky (2026-11-01, V004 kola 1–3, našli kritik a kreativní ředitel, opravil režisér)
- Příznak: hotové „686 km“ bylo čitelné jen ~0,38 s (karta na dronu 6,0–7,0); u karty „21″ / 909 M“ stál po zmizení textu plně krycí prázdný obdélník 3 snímky.
- Příčina: karta se vešla mezi dva střihy jen proto, že rolování začalo až po pomalém růstu tvaru (0,3 s); u větší karty delší odchod (`odK` 0,15) než u ostatních.
- Oprava (v4): růst 0,22 s, rolování 6,26–6,44, odchod 6,91 → klidná hodnota ~0,5 s; `odK` karty kola 0,10.
- Prevence: pravidlo G9 doplněno: hotová hodnota stojí čitelně ≥ 0,5 s, prázdný tvar při odchodu nejvýš 2 snímky. Když se karta mezi střihy nevejde, zkrátit růst a rolování, ne klid.
- Doplněk (kolo 4, kritik): režisér ve v4 opravil jen kartu 686, ostatní karty (500 kW 0,30 s, 3.8 s 0,25 s, 250 km/h 0,40 s) pravidlo porušovaly dál. Ve v4b
  všechny karty: rolování 0,22–0,3 s a dřív, klid ≥ 0,5 s. **Nové pravidlo se hned uplatní na všechna místa, kterých se týká**, ne jen na to, kde vzniklo.

### C045: Zvuk nesledoval změny obrazu v opravném kole (2026-11-01, V004 kolo 3, našel kritik)
- Příznak: v `V004_v3` zněl silný průjezd vozu 22,05 nad záběrem, kde nic neprojíždí, a skutečný průjezd 22,5 byl bez zvuku; tikání „3.8 s“
  odpovídalo starému rolování zdola (4 tiky), ne novému shora (6 přenosů); tiky karty 686 byly z časů v2.
- Příčina: zvukař a animátor běželi v opravném kole souběžně; animátor změnil záběr a časy karet, zvukař pracoval s předchozím obrazem. Nikdo nedostal seznam změn.
- Oprava (v4, režisér): tiky přepočítané přímo z funkce `polohySloupcu` (přenosy nejvyššího řádu), průjezd na skutečný průjezd D_3008 (vrchol 22,52), ding 250 na 22,6.
- Prevence: v opravném kole jde zvuk **až po obrazu** (nebo posuny SFX dělá režisér po posledním renderu); animátor v hlášení vypisuje „změny časů“ (čas, co se změnilo);
  zvukař počítá tikání z funkce rolování ve scéně, ne odhadem (`animator.md`, `zvukar.md`, `nastroje/workflow/README.md`).

### C044: Náhradní záběr ze zakázaného úseku zdroje (2026-11-01, V004 kolo 3, našel kritik, opravil režisér)
- Příznak: animátor nahradil opakovaný záběr W_900 (22,0–22,5) záběrem L_0816 = tisk 8,16–8,76, tedy z úseků, které storyboard výslovně zakazuje
  (7,08–8,25 čelní pohledy, A 8,30–9,20 leštěné aero kolo i7 60 a lamely chromových ledvinek). Přes detail kola jiného vozu stála karta „Top speed 250 km/h“.
- Příčina: seznam zakázaných úseků byl jen v textu storyboardu, skript záběrů ani zadání opravy ho nehlídaly; „čistý“ úsek se hledal podle pohledu na pár snímků.
- Oprava (v4): L_0816 vyřazen (zapsán do `vyrazene` v `seznam.json`), nový B_1280 = konec průletu nad střechou (tisk 12,80–13,40, silnice v rozmazání), zrcadlený,
  aby karta ležela nad silnicí, ne nad vozem; ověřeno po snímcích.
- Prevence: náhradní záběr jen z „Čistých úseků“ / „Rozpisu“ v zadání a s výslovnou kontrolou proti „Zakázaným“ (čas zdroje v hlášení); zapsáno do `animator.md` a `strihac.md`.
  Kritik dál kontroluje každý nový záběr proti zakázaným úsekům.

### C043: Animátor nedodržel výslovný pokyn režiséra (2026-11-01, V004 kola 1–2, našel kritik)
- Příznak: v1 opakovala záběr X_0448 (zakázané opakování úseku), v2 rolovala zrychlení zdola 0,0 → 3,8 (ukazovala lepší časy než fakt) přes rozhodnutí režiséra.
- Příčina: pokyny byly v dlouhém textu zadání opravy mezi nálezy, ne jako kontrolovatelná kritéria; animátor je přepsal vlastním řešením.
- Oprava: v dalších kolech opraveno, pravidlo G9 (rolující čísla jen přes horší hodnoty) přidáno do pravidel.
- Prevence: rozhodnutí režiséra jdou do zadání opravy jako číslovaná **závazná kritéria** (kritik je kontroluje jednotlivě); obecná pravidla rovnou do `pravidla-strihu.md` (G9).

### C042: Hudba elektromobilu měla motiv V8 (2026-11-01, V004, našel režisér)
- Příznak: nálada `luxsport` obsahuje syntetický „V8“ motor; u i7 (elektromobil) by to byla faktická chyba zvuku.
- Příčina: nálada vznikla pro spalovací vozy, přepínač pohonu neexistoval.
- Oprava: `hudba.py --motor elektricky` (tón střídače místo V8, časování beze změny), hudba i mix přegenerovány, staré soubory do `zvuk/zastarale_v8/`.
- Prevence: u vozů vždy zkontrolovat pohon a zvolit `--motor` (CLAUDE.md, Nástroje). Ostatní nálady ověřeny bit po bitu beze změny.

### C041: Barva tenkého textu se po kódování posunula (2026-11-01, V003 v4, našel kritik zadání, opravil animátor)
- Příznak: disclaimer #666666 (18 px) na teplém studiu #E7E2DC vycházel v MP4 jako (103, 99, 96); zdrojové PNG přesně 102/102/102.
- Příčina: YUV 4:2:0 sdílí barevnou složku pro 2×2 pixely, tenké písmo převezme chromu z okolního teplého pozadí.
- Oprava: mírně studenější zdrojová barva (rgb 98,105,110), v MP4 pak token ±2. Kompenzace se ladí na plném renderu, ne na výřezu (kodér má jiný kontext).
- Prevence: v `animator.md`: barvy tenkého textu (≤ 20 px) na barevném pozadí měřit v hotovém MP4 a případně kompenzovat ve zdroji.

### C040: Schodovité ozvěny čísla při dopadu ze špatně změřeného výchozího bodu (2026-11-01, V003 kola 1–3, opravil animátor v4)
- Příznak: velké „250“ při letu z bubliny 17,93–17,95 ve dvou oddělených kopiích, kritici to brali jako laciný / AI znak.
- Příčina: výchozí bod letu se počítal z rozměru DOM bubliny, která se v 17,935 skryje (offsetWidth 0), takže bod skočil o ~45 px. Nebyla to jen závěrka.
- Oprava: výchozí bod změřen jednou při zobrazené bublině; rozmazání pohybem v kódu souvisle (SVG blur podle rychlosti), ne kopiemi.
- Prevence: v `animator.md`: rozměry pro výpočet pohybu měřit jednou nebo z pevného stavu, nikdy z prvku, který se během pohybu skrývá.

### C039: Verze bez hudby vznikla ze zastaralého odvozeného souboru (2026-11-01, V003 kolo 2, našel kritik zadání)
- Příznak: `V003_v2_bez_hudby.mp4` měla efekty z doby před posunem na skutečné časy obrazu (švih 20,95 místo 20,875, chybí 24,0 / 5,875 / 15,5).
  Hlavní verze byla v pořádku (ověřeno korelací s novým mixem, 0,998–0,9996).
- Příčina: režisér přegeneroval WAV (`zvuk_v1.wav`, `zvuk_bez_hudby_v1.wav`), ale nechal ve složce starší odvozené soubory
  (`zvuk_bez_hudby_v1_stejny_zisk.m4a`, `zvuk_v1_master.m4a` ze 4:36), a střihač pro verzi bez hudby sáhl po odvozeném m4a.
- Oprava: zvukař v kole 3 přegeneruje verzi bez hudby z aktuálního WAV.
- Prevence: při přegenerování zvuku smazat nebo přegenerovat všechny odvozené soubory (m4a, spektrogramy) ve stejné složce; střihač vždy
  masteruje ze souboru WAV, který dostal v úkolu, nikdy z jiného souboru ve složce (`strihac.md`).

### C038: Do commitu se dostal dočasný soubor místo nástroje (2026-11-01, V003, režisér)
- Příznak: commit „render_html.cjs CRF 14…“ obsahoval jen `nastroje/.r.tmp`; nástroj se nevyměnil.
- Příčina: `node --check` odmítl příponu `.tmp` a zastavil řetěz `&&`, ale `git add -A && git commit` byl na samostatném řádku, takže proběhl.
- Oprava: dočasný soubor odstraněn z gitu, nástroj vyměněn a ověřen, nový commit.
- Prevence: dočasné soubory psát do scratchpadu (ne do repozitáře) se správnou příponou (`.cjs`), commit spouštět jen na konci jednoho řetězu `&&`
  a před commitem zkontrolovat `git status`.

### C037: Skvrnité bloky na světlé stěně studia (2026-11-01, V003 kolo 1, našel kritik zadání, opravil režisér + animátor)
- Příznak: na světlé stěně a v jemných přechodech kompresní bloky, ve 100 % ubírají dojmu drahé reklamy; video jen 3,7 Mbit/s.
- Příčina: (1) zdrojové snímky otočky 360° z konfigurátoru jsou silně komprimované (~60 kB WebP), (2) CRF 16 s výchozím aq-mode na velkých
  plochých plochách šetří bity. Měření na výřezu stěny: CRF 12 + aq-mode 3 = o ~37 % menší průměrná chyba než CRF 16.
- Oprava: `render_html.cjs` CRF 14 + `aq-mode=3`; animátor jemně vyhladí pozadí ve zdrojích otočky a přidá velmi jemné zrno.
- Prevence: u fotorealistických podkladů vždy zkontrolovat kvalitu zdroje ve 100 % (ne jen rozlišení) a plochy s jemným přechodem ve výsledném MP4.

### C036: Kolize klíčů časové osy mezi moduly scény (2026-11-01, V003, našel a opravil animátor)
- Příznak: lišta se na 16,000 objevila skokem i s textem, protože blok B3 přes `Object.assign(CASY, …)` přepsal klíč `listaZpet` z jádra (16,05 → 7,0).
  Regresní kontrola to nechytila, protože porovnávala jen čas po skončení přechodu.
- Oprava: přejmenování klíčů (`listaPrycB3`, `listaZpetB3`).
- Prevence: v `animator.md`: moduly, které rozšiřují společný objekt časů, používají prefix bloku a kontrolu kolize (klíč ještě nesmí existovat);
  regrese hotových bloků se měří i **uvnitř** přechodů (např. 16,0 / 16,017 / 16,05), ne jen na jejich konci.

### C035: Vrchol nízkých úderů padal 7–12 ms za náběh zvuku (2026-11-01, V003, našel a opravil zvukař)
- Příznak: změřený vrchol úderů dropů a loga 7–12 ms po náběhu; úder dropu 2 s `drive` měl vrchol rozmazaný o 10–70 ms a byl jen −9 LU pod hudbou.
- Příčina: harmonické těla v sinové fázi dají první puls obálky až po periodě základu (1/110 Hz = 9 ms); nasycený průběh má špičky obálky na hranách.
- Oprava: `sfx.py` funkce `ton_c` (kosinová fáze, puls na konci náběhu) a úder jako nasycené tělo s omezenou obálkou + krátký transient navrch.
  Teď 1,4–2,0 ms, drop 2 −3,0 LU proti hudbě.
- Prevence: u klíčových úderů kontrolovat změřený vrchol proti náběhu zvuku, ne jen proti času události (zvukař).

### C034: Duhový lem na logu v dropu 2 a ztmavená barva značky na end card (2026-10-31, V002 kolo 3, našli všichni 3 kritici, opravil animátor v4)
- Příznak: (a) prstenec a ramena hvězdy v 18,78–18,93 s v zelených a žlutých pásech (~40–50 px místo 6 px), přímo na logu v nejsilnějším momentu;
  (b) „STAR“ na end card #0072CC místo #0078D6.
- Příčina: (a) radiální chromatický posun přes R/G/B kanály na celé světelné vrstvě: G se posouval s R, z bílé vznikla žlutá, z modré záře
  zelenožlutá, posun rostl se vzdáleností od středu a prstenec se zároveň zvětšoval; (b) vinětace se kreslila až po textu.
- Oprava: na logu žádné RGB kanály, jen tečné duchy tónované barvou palety přes `screen` (RGB posun jen na rychlostních čarách); vinětace pod texty.
  Ověřeno pixely: zelenožluté body kolem hvězdy 21 165 → 0, STAR odchylka ≤ 2.
- Prevence: v `animator.md`: chromatický posun na logu a barvách značky nikdy přes R/G/B kanály; barvy značky kreslit nad vinětaci a zrno
  a změřit v hotovém MP4. Kritik zadání měří barvy loga a akcentů v pixelech (už to dělá, chytil to).

### C033: Tyrkysové lemy ze sčítání světla a couvající vůz při „chytání“ kamerou (2026-10-31, V002 kola 1–2, našli kritici, opravil animátor)
- Příznak: (a) bílé jádro na modré záři mělo tyrkysový lem (140,241,255), mimo paletu a blízko barvy sponzora (C8); (b) GT při přechodu
  do T5 zastavil a jel zpět proti směru přídě (7,13–7,5 s).
- Příčina: (a) režim `lighter` sčítá kanály, B se ořízne na 255 a přebytek dorovná G, takže odstín sjede k tyrkysové; (b) Hermitova křivka
  s počáteční rychlostí vozu a nulovou koncovou rychlostí přestřelí, vůz na obrazovce couvá.
- Oprava: světlo na modrou plochu skládat překrytím (`source-over`) nebo `screen` (volba `op` ve `FX.zare`); přechod přes schovaný střih.
- Prevence: v `animator.md`. Polohu vozu na obrazovce kontrolovat na monotónnost (pás po 1 snímku), přes úmyslný skok počítat rychlost jednostranně.

### C032: Stoupání před dropem 2 sláblo a drop 2 byl nejtišší úder (2026-10-31, V002, našel kreativní ředitel, opravil zvukař)
- Příznak: RMS v okně 50 ms ve stoupání 16,5–18,0 klesalo (−17 → −15,9 dB, pod úrovní jízdy) a drop 2 (−11,9) byl tišší než drop 1 i finále,
  i když má být nejsilnějším momentem.
- Příčina: hudba je mezi údery stoupání řidší, bez automatiky proto zní slaběji. Rezerva na úderu jen ~0,5 dB (poměr špičky a průměru 9–11 dB),
  takže samotné zesílení by limiter zmáčkl.
- Oprava: `sfx.py --zisk-hudby` (stoupání 0 → +4 dB, vysoké pásmo +2 dB navíc, jízda T3–T8 −1 dB, drop 2 +3 dB) a `--saturace` na úderu dropu 2.
  Výsledek: stoupání roste až nad úroveň jízdy, drop 2 je nejhlasitější místo videa (−9,2 dB v okně 50 ms), mimo upravené úseky bit po bitu stejné.
- Prevence: zvukař u každého stoupání a dropu měří RMS v okně 50 ms: stoupání musí růst a hlavní úder být nejhlasitější místo videa (o ≥ 1 dB).
  Pravidlo do instrukcí zvukaře.

### C031: Časy v archu `kontrola.sh` neseděly o ~0,25 s (2026-10-31, V002, našel kritik technika, opravil režisér)
- Příznak: dlaždice „26.500“ ukazovala obsah ze ~26,75 s (rozevírající se CTA, které začíná v 26,72).
- Příčina: filtr `fps=2` vybírá snímky se zaokrouhlením k nejbližšímu výstupnímu času, ne snímek přesně v čase popisku.
- Oprava: arch vybírá snímky podle čísla (`select=not(mod(n,KROK))`, KROK = fps / 2). Ověřeno: dlaždice 26,5 = snímek 1590.
  Skript se vyměnil atomicky (`mv`), protože ho souběžně používal jiný kritik (bash čte běžící skript průběžně).
- Prevence: časy kritiků ověřovat přesným snímkem (`select=eq(n,N)`), arch je jen přehled.

### C030: Verze bez hudby (jen SFX) nešla namasterovat, smyčka s limiterem nezkonvergovala (2026-10-31, V002, našel střihač, opravil režisér)
- Příznak: `master_zvuk.sh` na samotných SFX (−24 LUFS, velký poměr špičky a hlasitosti) skončil ve všech 4 pokusech na +0,1 až +0,6 dBTP.
- Příčina: ostré transienty (švihy, kovové údery) mají energii nad 19 kHz, kodér AAC ji ořízne a vznikne překmit +2–3 dB nad true peak změřený ve WAV.
  Limiter to před kódováním nevidí.
- Oprava: ve větvi limiteru `master_zvuk.sh` dolní propust 19 kHz (2× 2 póly) před limiterem. Ověřeno na stejném souboru: 2. pokus −15,0 LUFS / −1,8 dBTP.
  Hlavní mix s hudbou jde cestou bez limiteru, ta se nemění.
- Prevence: komentář ve skriptu. Syntetické SFX zbytečně nad 18 kHz netlačit (zvukař).

### C029: `kontrola.sh` nedělal pásy snímků u dropů a švihů (2026-10-31, V002, našel animátor, opravil režisér)
- Příznak: u videa s 10 skoky (dropy, švihy, tiker) nevznikl žádný pás snímků, animátor je musel vyřezávat ručně.
- Příčina: pásy se dělaly jen z `podezrele.txt`, kam `skoky.py` zapisuje jen dvousnímková probliknutí.
- Oprava: `skoky.py` zapisuje začátek každé série do `skoky.txt` a `kontrola.sh` dělá pás 6 snímků u každého skoku i probliknutí (nejvýš 30).
  Ověřeno na V002 v1: 10 pásů.
- Prevence: nástroj pro kritika testovat i na videu s rychlými přechody, ne jen s probliknutím.

### C028: Krátký záblesk na dropu byl kvůli závěrce skoro neviditelný (2026-10-31, V002, našel a opravil animátor)
- Příznak: drop 1 v plném renderu vizuálně slabý, kontrola skoků ho ani neoznačila. Záblesk 0,05 s byl vidět asi z 30 %.
- Příčina: závěrka 180° vycentrovaná na čas snímku: snímek přesně v čase události je napůl „před“ událostí a krátký záblesk se rozprůměruje.
  Klíčové snímky (statické, bez podsnímků) to neukážou.
- Oprava: záblesk 0,08 s (3 viditelné snímky), krytí 70 %, dosah přes vůz, nový render.
- Prevence: v `animator.md`: krátké záblesky a dopady navrhovat s ohledem na závěrku a jejich sílu ověřovat na snímku čas + 1/60 s
  v pásu z plného renderu (nebo `--od/--dur` výřezu s podsnímky), ne na statickém klíčovém snímku.

### C027: Plný render složité scény by trval 80 min až 2,7 h (2026-10-31, V002, našel animátor, opravil režisér)
- Příznak: ~160–190 s výpočtu na 1 s videa (1920×1080, 60 fps, `--sub 4`). Video 30 s by se renderovalo ~80 min, s `--sub 8` ~2,7 h,
  a každé kolo oprav znovu.
- Příčina: hlavní náklad nebyla scéna (~31 s na 1 s), ale kódování PNG v `page.screenshot` (550–650 ms na podsnímek, zrno se špatně komprimuje).
  Renderer navíc běžel v jednom prohlížeči, i když jsou 4 CPU. Odhad „16 s na 1 s“ v CLAUDE.md byl změřený na jednoduché scéně.
- Oprava: `render_html.cjs` snímá přes CDP `Page.captureScreenshot` s `optimizeForSpeed` (pixely ověřeně totožné, ~2,5× rychlejší),
  renderuje úseky ve 3 prohlížečích najednou a spojí je bez překódování (bezeztrátově ověřeno: totožné snímky), umí 8 podsnímků jen
  v rychlých úsecích (`--sub-rychle 8 --rychle …`) a výřez (`--od`). Změřeno: 1 s videa 189 s → 75 s (CDP) → 36 s (3 vlákna).
- Prevence: v instrukcích animátora „změř 1 s výřezu a vynásob“ místo pevného odhadu, výkonová pravidla scény (žádný blur filtr na mnoho prvků,
  záře jako sprity), workflow šablona renderuje `--sub 4` + rychlé úseky 8. Před dlouhým renderem vždy změřit výřez.

### C026: Jednoprůchodový loudnorm v `hudba.py` zploštil stavbu skladby (2026-10-31, V002, našel zvukař)
- Příznak: úvod sportovní hudby byl stejně hlasitý jako jízda a drop 2 skoro nevynikl, i když aranžmá bylo správně
  (před normalizací úvod −21,2 a drop 2 −14,5 dB, po ní −16 a −15,9 dB).
- Příčina: `loudnorm` v jednom průchodu běží v dynamickém režimu: tiché části zesílí, hlasité ztlumí. Kontrast dropu zmizí.
- Oprava: nálada `sportovni` se normalizuje lineárním ziskem a jemným limiterem. Ostatní nálady zatím beze změny (bit po bitu),
  protože by se změnil jejich zvuk.
- Prevence: dluh zapsán v `pouceni.md` (vazna, drza, luxusni, pohodova přepnout na lineární normalizaci při prvním dalším použití,
  s poslechovou ukázkou pro uživatele). Pravidlo pro nástroje: hlasitost celé skladby jen lineárním ziskem (a limiterem), nikdy dynamickým loudnorm.

### C025: Limiter `alimiter` posunul zvuk o 5 ms (2026-10-31, V002, našel zvukař, opravil režisér)
- Příznak: celá hudba po limiteru zpožděná o 240 vzorků (5,00 ms při 48 kHz), změřeno křížovou korelací se syntézou.
- Příčina: `alimiter` má look-ahead a bez `latency=1` latenci nevyrovná.
- Oprava: `latency=1` v `hudba.py` (zvukař) i ve větvi limiteru v `nastroje/master_zvuk.sh` (režisér). Ověřeno šumem: bez volby posun 240 vzorků, s ní 0.
- Prevence: každý `alimiter` v nástrojích vždy s `latency=1`. Synchronizaci zvuku po každém novém filtru ověřit křížovou korelací, ne poslechem.

### C024: Prompt pro analytika obsahoval obcházení ochrany webu (2026-10-31, V002, zastavila bezpečnostní pravidla)
- Příznak: spuštění workflow zamítnuto („Bot Check Circumvention“). V úkolu stálo „kdyby web blokoval přístup, zkus jiný User-Agent“.
- Příčina: web mercedes-benz.cz vrací automatickým požadavkům 403 (ochrana proti robotům) a já jsem to navrhl obejít.
- Oprava: pokyn odstraněn. Weby, které blokují automatický přístup, se nenačítají ani neobcházejí. Logo z veřejného oficiálního zdroje
  (Wikimedia Commons), paleta předběžně a k ověření se požádá uživatel (screenshot / soubory na Drive).
- Prevence: **nikdy neobcházet ochranu webů** (User-Agent, headless prohlížeč na blokovanou stránku…). Při 403 to oznámit uživateli
  a požádat o podklady. Zapsáno v CLAUDE.md (Příjem).

### C023: master_zvuk.sh pustil true peak −0,96 dBTP (2026-10-31, V001, našel střihač)
- Příznak: s cílem ≤ −1 dBTP skončil mix na −0,96 dBTP a skript ho přijal.
- Příčina: tolerance +0,05 dB v podmínce ukončení.
- Oprava: tolerance zrušena (podmínka ≤ cíl), ověřeno na V001_v3 (−14,0 LUFS / −1,0 dBTP).
- Prevence: limity bez tolerance, rezervu řeší cíl, ne podmínka.

### C022: Mezikrok přes MKV zkrátil video na 24,999 s (2026-10-31, V001 střih, našel a opravil střihač)
- Příčina: MKV ukládá časy v milisekundách, 1500 snímků při 60 fps se zaokrouhlilo.
- Oprava: mezikrok přes MOV, délka 25,000 s, video stopa bit po bitu stejná (MD5).
- Prevence: při kopírování stop mezi kontejnery nepoužívat MKV jako mezikrok, používat MOV nebo MP4. Délku vždy ověřit ffprobe.

### C021: Průběžné commity režiséra zmátly zvukaři základ pro porovnání (2026-10-31, V001 výroba, našel zvukař)
- Příznak: zvukař porovnával hashe pohodové nálady „proti HEAD“, jenže HEAD už obsahoval jeho vlastní rozpracovanou verzi
  (režisér ji kvůli stop hooku průběžně commitoval). Porovnával tedy verzi samu se sebou.
- Oprava: zvukař sám přešel na základ 0af1765 (poslední stav před ním). Režisér nezávisle ověřil: drzá a luxusní jsou stejné bit po bitu.
- Prevence: v zadání pro agenta, který mění nástroje, **uvádět pevný základní commit** (hash), ne HEAD. Režisér během práce agentů
  commituje průběžné snímky, takže HEAD se pod rukama mění.

### C020: Výrobu přerušil 5hodinový limit účtu (2026-10-30, V001 výroba, workflow vrátil chybu)
- Příznak: zvukař i animátor po ~7 min skončili s „You've hit your 5-hour limit · resets 11:40pm (UTC)“. Workflow vrátil „animátor nedodal render“.
  Hlídač ukazoval jen TICHO, protože skutečnou příčinu hlásí až výsledek workflow (pole failures).
- Příčina: limit využití účtu za 5 h. Předchozí fáze (fáze 1 ~0,4 mil., porota ~0,5 mil. + zaseknutý agent ~0,7 mil. tokenů) ho vyčerpaly.
- Oprava: po resetu (23:40 UTC) ověřen rozpracovaný stav (hudba.py se přeloží, ostatní nálady bit po bitu stejné jako HEAD, scéna
  má 10 rozpracovaných souborů), do skriptu doplněna informace „navazuješ na přerušený pokus“ a workflow obnoven.
- Prevence: dlouhé workflow neplánovat těsně po velké spotřebě. Při „hit your limit“ počkat na reset a obnovit (resumeFromRunId).
  Rozpracované soubory před obnovou vždy zkontrolovat (překlad, hashe, git diff). **Úspora tokenů = víc práce do limitu**: effort high,
  psaní po částech a hlídač (C018) nejsou jen rychlost, ale i rozpočet.

### C019: Hlídač hlásil falešný „limit výstupu“ hned na startu agentů (2026-10-30, nastroje/hlidac.py, našel režisér ověřením)
- Příznak: ve 22:33 hlášení LIMIT VÝSTUPU ×1 u zvukaře i animátora, oba přitom teprve začínali.
- Příčina: hlídač hledal větu „Output token limit hit“ kdekoli v transkriptu. Agenti si na startu přečetli `znalosti/chyby.md`,
  kde ta věta je v popisu C018.
- Oprava: počítá se jen systémová zpráva typu user, jejímž celým obsahem je ta věta. Ověřeno: starý agent C = 3, noví agenti = 0.
- Prevence: **každé automatické hlášení nejdřív ověřit, než se podle něj jedná** (restart agenta by stál čas i tokeny).
  Detektory testovat i na případu, kdy hledaný text jen citujeme.

### C018: Agenti workflow „stalled“ 16–23 min, narazili na limit délky výstupu (2026-10-30, V001 porota konceptů, našel režisér)
- Příznak: návrhy B a C bez zápisu 16+ minut. Uživatel to viděl v přehledu workflow jako „stalled“.
- Příčina: agenti zdědili **maximální úroveň přemýšlení** a celý návrh (storyboard na 10 taktů) psali **jednou obří odpovědí**.
  Po 23 min přišlo „Output token limit hit… Break remaining work into smaller pieces“. Nevisel žádný příkaz, generování běží na serveru
  a deník se zapíše až po dokončení odpovědi.
- Oprava: návrhy jsem nechal doběhnout (práce se neztratila), porotě a syntéze jsem upravil skript na `effort: 'high'` + psaní po částech
  a obnovil ho z deníku (hotové kroky z mezipaměti).
- Prevence: ve workflow tvůrčí a hodnotící agenti **`effort: 'high'`** (max jen pro výjimečně těžké úlohy) a v každém promptu s velkým výstupem
  **„piš po částech: kostra + malé Edit“**. Diagnostika: poslední záznam v `subagents/workflows/<run>/agent-*.jsonl`,
  ticho > 15 min bez běžícího procesu = dlouhé generování / limit výstupu.

### C017: Pohodová hudba v1 měla propad v horních středech, kontrola pásem ho neodhalila (2026-10-30, V001, našel animátor a pak režisér)
- Příznak: animátor našel propad 16 dB mezi oktávami 0,5–1 kHz a 1–2 kHz a hi-hat kolem −80 dB. Po jeho opravě režisér nezávisle naměřil
  ještě ~13 dB mezi 1 kHz a 2 kHz.
- Příčina: `kontrola_pasem` měří jen široká pásma (středy 250–2000 Hz). Propad uvnitř pásma se schová.
- Oprava: animátor přidal jas Rhodes, hlasitější hi-hat a tleskání a `vysky_db`. Zbytek vyhladí zvukař ve fázi 2.
- Prevence: `kontrola_pasem` doplnit o **spektrum po oktávách** a varování při skoku sousedních oktáv (250 Hz–8 kHz) nad ~8–10 dB (úkol pro zvukaře).

### C016: Fonty z Google Fonts nebyly stažené při měření (2026-10-30, V001, našel animátor)
- Příznak: canvas změřil všechny kandidátní fonty stejně.
- Příčina: prohlížeč stahuje font, až když ho použije prvek ve stránce. `document.fonts.ready` na nepoužité fonty nečeká.
- Oprava: fonty nejdřív vynutit, pak měřit.
- Prevence: `nastroje/vzory/scena.html` má seznam `FONTY` a před `seek(0)` volá `document.fonts.load()` pro každý řez (ověřeno testem).

### C015: setup.sh neinstaloval nástroje přidané později (2026-10-30, nástroj, našel režisér na začátku nové session)
- Příznak: v novém kontejneru chyběly `gdown` a `scipy` (stahování z Drive, generátor hudby).
- Příčina: knihovny jsem nainstaloval ručně, ale nepřidal do `nastroje/setup.sh`.
- Oprava: setup instaluje `yt-dlp faster-whisper gdown scipy pillow-heif`.
- Prevence: **každá nová závislost hned do `setup.sh`**, jinak ji příští session nemá.

### C014: Drobné chyby při psaní hudba.py (2026-10-30, nástroj, našel režisér testem)
- Příznak: (1) `butter()` nepřijal jednoprvkové pole jako mezní frekvenci, (2) náhodné „lidské“ posunutí noty před čas 0 rozbilo vkládání do mixu,
  (3) při úpravách zůstal v kódu nesmyslný řádek.
- Oprava: skalár pro lowpass/highpass, oříznutí signálu před 0, řádek přepsán na pomocnou funkci `swing()`.
- Prevence: nový nástroj vždy hned spustit ve všech režimech (všechny nálady), ne jen přeložit.

### C013: drive.sh nenašel právě stažený soubor (2026-10-30, nástroj, našel režisér testem)
- Příznak: stažení proběhlo, ověření nic nevypsalo.
- Příčina: gdown zachová původní datum souboru z Drive, hledání „novějších souborů“ ho minulo.
- Oprava: porovnání obsahu složky před a po stažení.
- Prevence: nové soubory poznávat podle seznamu, ne podle data změny.

### C012: Hudba měla 2–3× víc hlubokých basů než profesionální mix (2026-10-30, hudba.py v1, našel režisér měřením pásem)
- Příznak: sub 42–58 % energie (reference R5: 20 %), u drzé nálady jen 4 % středů. Z telefonu by hudba zněla skoro prázdně.
- Příčina: basa o oktávu níž (F1 44 Hz), dlouhý dojezd kopáku, taiko a úderu, melodické nástroje potichu. Poslech nemám, kontrola chyběla.
- Oprava: basové tóny v rozsahu 55–104 Hz s vyššími harmonickými, kratší a tišší bicí a úder, víc středů, highpass 38 Hz.
  Výsledek: sub 11–18 %, středy 31–64 %.
- Prevence: `hudba.py` po každém renderu měří pásma a varuje (pravidlo I7). **Hudbu posoudí uživatel poslechem**: zpětná vazba → pravidla.

### C011: Mastering nezkonvergoval na true peak ≤ −1 dBTP (2026-10-30, master_zvuk.sh, našel režisér na ukázce hudby)
- Příznak: po 3 pokusech −0,7 dBTP. Limiter s rychlým uvolněním (60 ms) výsledek zhoršil až na +0,6 dBTP.
- Příčina: lineární loudnorm nic neomezuje a snížení jeho cíle TP na výsledek nemá vliv. Rychlý limiter zkresluje basy a AAC pak přidá další špičky.
- Oprava: při přetečení nejdřív ubrat hlasitost o přesah (v toleranci −14 ±1), teprve potom jemný limiter (192 kHz, attack 5 ms, release 300 ms).
  Ověřeno na 3 různých vstupech: −14,0 až −14,3 LUFS, −1,0 až −1,4 dBTP.
- Prevence: zvukové nástroje testovat na více typech vstupu (tichý, hlasitý, profesionální mix).

### C010: `ffmpeg` ve smyčce `while read` sní zbytek vstupu (2026-10-30, nástroj kontrola.sh, našel režisér testem)
- Příznak: ze 2 podezřelých míst vznikl jen 1 pás snímků.
- Příčina: ffmpeg čte stdin a spotřeboval zbývající řádky smyčky.
- Oprava: `ffmpeg -nostdin`.
- Prevence: **každý ffmpeg ve smyčce `while read` má `-nostdin`**.

### C009: Rychlý přechod hlášen jako probliknutí (2026-10-30, nástroj skoky.py, našel režisér testem na R2)
- Příznak: 5snímkový přechod a 2snímkové prolnutí v R2 označené jako „probliknutí“.
- Příčina: z rozdílů jasu sousedních snímků nejde poznat, jestli se obraz vrátil.
- Oprava: série 1 = střih, 3+ = rychlý přechod, 2 = podezřelé → `kontrola.sh` vyřízne pás 6 snímků a kritik ho musí prohlédnout.
- Prevence: automatický nález je jen podezření, rozhoduje pohled na snímky (instrukce kritika).

### C008: Tmavé pozadí hlášeno jako černý úsek (2026-10-30, nástroj kontrola.sh, našel režisér testem)
- Příznak: blackdetect hlásil 0–2,8 s jako černé, i když byl na obrazovce text.
- Příčina: výchozí prahy blackdetect berou téměř černé pozadí (#0b0b0c) s malým textem jako černý snímek.
- Oprava: `pic_th=0.999:pix_th=0.06`, hlásí se jen opravdu prázdné snímky.
- Prevence: nástroje testovat i na tmavém designu, ne jen na fotkách.

### C007: True peak po AAC překročil limit (2026-10-30, nástroj master, našel režisér testem)
- Příznak: loudnorm s cílem −1 dBTP, po zakódování do AAC naměřeno −0,2 dBTP.
- Příčina: kodek AAC přidává mezivzorkové špičky.
- Oprava: `nastroje/master_zvuk.sh` měří po AAC a až 3× sníží vnitřní cíl true peak (výsledek −14,2 LUFS / −1,3 dBTP).
- Prevence: hlasitost se vždy měří **po** finálním zakódování (pravidlo A2, kontrolní seznam K).

### C006: Podsnímky nebyly vystředěné (2026-10-30, nástroj render_html.cjs, našel analytik)
- Příznak: rozmazání přes celý snímek jen dopředu (závěrka 360°), obraz posunutý o ~⅓ snímku, silná šmouha.
- Příčina: časy podsnímků `(f + s/SUB)/FPS`.
- Oprava: vystředěno kolem času snímku, `--zaverka 0.5` (180°), výchozí `--sub 4`.
- Prevence: nástroje porovnávat s metodou nejlepších promptů prompt-motion (`poznatky.md` 2.7).

### C005: Pružina měla výchozí překmit 8 % (2026-10-30, kostra scena.html, našel analytik)
- Příznak: UI prvky by „houpaly“ jako kreslený film.
- Příčina: výchozí hodnota zvolená odhadem.
- Oprava: výchozí 3 %, přidána kriticky tlumená `usazeni()`. Pravidlo F4 upraveno na 2–5 %.
- Prevence: číselné výchozí hodnoty brát z ověřených zdrojů a zapsat zdroj.

### C004: `will-change` v kostře scény (2026-10-30, kostra scena.html, našel analytik)
- Příznak: (potenciální) rozmazaný text, když ho kamera zvětší.
- Příčina: `will-change: transform` rasterizuje prvek v původní velikosti.
- Oprava: odstraněno, scéna se navíc staví až po `document.fonts.ready`.
- Prevence: past je zapsaná v oddílu `<pasti>` hlavní kostry promptu (`poznatky.md` 10) a v kontrolách kritika.

### C003: Render s 3 podsnímky dělá u rychlého pohybu „schodovité duchy“ (2026-10-30, test, nástroj)
- Příznak: při testu `render_html.cjs` byl text v rychlém příjezdu 3× zdvojený místo plynulého rozmazání.
- Příčina: 3 podsnímky na snímek nestačí na velký posun mezi snímky.
- Oprava: žádná (test).
- Prevence: v instrukcích animátora je pro rychlé přechody `--sub 6` + rozmazání v CSS podle rychlosti a směru. Kritik porovnává sousední snímky.

### C002: `analyzuj.sh` spadl u videa bez střihů (2026-10-30, nástroj)
- Příznak: skript skončil po řádku „Střihy“ a nevytvořil náhled.
- Příčina: `grep` bez shody vrací chybový kód a `set -o pipefail` ukončí skript.
- Oprava: `|| true` a hláška „žádné tvrdé střihy“.
- Prevence: v bash skriptech s `pipefail` u grep/filtrů vždy počítat s prázdným výsledkem.

### C001: Whisper nepřečetl video přímo (2026-10-30, nástroj)
- Příznak: `TypeError: open() got an unexpected keyword argument 'metadata_errors'`.
- Příčina: faster-whisper volá novější PyAV, než je nainstalované.
- Oprava: zvuk dekóduje ffmpeg a do Whisperu jde pole vzorků (`nastroje/prepis.py`).
- Prevence: používat jen `nastroje/prepis.py`, nevolat faster-whisper přímo se souborem.
