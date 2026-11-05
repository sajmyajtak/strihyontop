export const meta = {
  name: 'v005-priprava',
  description: 'V005 Porsche (3–4 agenti): analytik (web, konfigurátor 982890, interiér, výbava, fakta, stopáž jízdy) → kreativní ředitel (koncept + střihová partitura) → oponent, který rovnou zapracuje → případný test techniky',
  phases: [
    { title: 'Podklady', detail: 'analytik: porsche.cz barvy a písmo, konfigurátor 982890 (exteriér, interiér, úpravy), fakta, videa jízdy, podmínky' },
    { title: 'Koncept', detail: 'kreativní ředitel: koncept + střihová partitura podle strih-vzor.md' },
    { title: 'Oponentura', detail: 'druhý kreativní ředitel: posoudí střih, realismus, pohodu a rovnou zapracuje' },
    { title: 'Test', detail: 'animátor: test nové techniky (jen když ji koncept vyžaduje)' },
  ],
}

const P = 'projekty/005-porsche/zadani.md'
const M = 'media/projekty/005-porsche'
const CTX = `Projekt V005 Porsche, repozitář /home/user/strihyontop (pracuj relativně k němu). Úkol ti zadává režisér (hlavní agent). Uživatele se nikdy
neptáš; když si nevíš rady, rozhodni rozumně sám, zapiš to a otázku vrať režisérovi v poli otazky_pro_rezisera. Necommituj.
ZÁVAZNÉ: ${P} (zadání uživatele doslova, pravidla 1–8), **znalosti/strih-vzor.md** (závazný vzor střihu od uživatele: jeden hrdina + jeden doplněk,
stavy místo záběrů, proměny místo střihů, semínko, partitura, klid jen na přečtení, věta na scénu, zvuk podle obrazu, kotva, kaskáda, podpis tvůrce),
znalosti/pravidla-strihu.md (vkus uživatele nahoře; D8–D15, G7 realismus, G8 SaaS motion, G9 čísla, H5, I9), znalosti/pouceni.md (V003, V004, 2026-11-04),
znalosti/chyby.md (C024 web se neobchází, C044 zakázané úseky stopáže, C045 zvuk až po obrazu, C046–C048).
Weby Porsche načítej jen normálně (curl / yt-dlp / Playwright jako běžný prohlížeč, bez změny User-Agenta, bez obcházení). 403, captcha, přihlášení
nebo DRM = NIC NEOBCHÁZEJ (C024): zapiš a pokračuj s tím, co máš. Formát 16:9 1920×1080, 60 fps, 30,0 s, bez voiceoveru (věty na obrazovce), anglicky.
PRACUJ PO ČÁSTECH (C018): velké soubory po částech (kostra + menší Edit), věcně, čísla, bez vaty.`
const S = { type: 'array', items: { type: 'string' } }
const otazky = []
const sber = (kdo, r) => { if (r && r.otazky_pro_rezisera) for (const q of r.otazky_pro_rezisera) otazky.push(`${kdo}: ${q}`); return r }

phase('Podklady')
const ma = sber('analytik', await agent(`${CTX}

## Tvůj úkol: VŮZ, ZNAČKA A MATERIÁL (analytik)
1. **Model**: otevři https://configurator.porsche.com/cs-CZ/mode/model/982890 v Playwright (1920×1080, cookie lištu zavři běžným tlačítkem). Zjisti a zapiš doslova:
   název modelu (982890 = ?), karoserie, **technické údaje** (výkon kW/PS, 0–100 km/h, max. rychlost, motor; u výchozí konfigurace) s URL. Projdi konfigurátor:
   **exteriér** (všechny úhly, které ukazuje, nejlépe otočka; uložit v nejvyšším rozlišení, které stránka sama načte), **interiér** (všechny pohledy),
   a **úpravy**: barvy laku (seznam + rendry téhož úhlu v několika barvách, aspoň 4), kola (aspoň 3), barvy interiéru / kůže (aspoň 3), sedadla, výrazné
   doplňky (pakety, pruhy, spoilery). Cíl videa je „během jízdy si vůz upravuješ“, proto potřebujeme **stejný úhel ve více variantách** (pixelově zarovnané
   rendry = přechod maskou, D7). Ulož do ${M}/materialy/konfigurator/<kategorie>/ s čitelnými názvy + katalog.md (co, úhel, varianta, rozlišení, URL).
2. **Web porsche.cz**: stránky tohoto modelu: fotky exteriéru a interiéru v nejvyšším rozlišení, které stránka sama načte (do ${M}/materialy/fotky/),
   texty o modelu (claimy, popisy interiéru a jízdních vlastností doslova, s URL) do katalog.md. **Barvy a písmo**: z CSS webu (tokeny, hlavní barvy,
   akcent, pozadí, text; písmo Porsche Next a jeho náhrada z Google Fonts s latin-ext) → ${M}/znacka/znacka.css + zápis do ${P} oddíl „Značka“.
   Logo / znak: jen to, co web sám zobrazuje (SVG/PNG), zapsat zdroj; použití = spec reklama do portfolia s disclaimerem, vše © Porsche AG.
3. **Skutečné záběry jízdy** (hlavní materiál podle vkusu uživatele: vůz musí jet): videa, která stránky porsche.cz tohoto modelu normálně přehrávají
   (HLS/MP4 načtené stránkou), a Porsche Newsroom (newsroom.porsche.com, bez přihlášení; podmínky použití zapsat doslova). Stáhni jen běžnou cestou do
   ${M}/materialy/videa/, ke každému: arch (ffmpeg snímek každé 2 s), délka, rozlišení, fps, co je v záběrech, **barva a provedení vozu**, text/vodoznak,
   licence. Tabulka shody: které záběry jsou tentýž model (982890) a v jaké barvě → při konceptu „úpravy za jízdy“ je barva stopáže jedna z konfigurací.
   Hledej hlavně **pohodové** záběry (krajina, hory, serpentiny, pobřeží, interiér za jízdy, ruce na volantu, výhled), ne závodní.
4. Spusť python3 -I nastroje/materialy.py ${M}/materialy (katalog, varování, _prehled.jpg) a prohlédni _prehled.jpg.
5. Zapiš do ${P}: tabulka Materiály, oddíl „Vůz a fakta“, „Značka“, „Materiál jízdy“ (co máme, barvy, kvalita, podmínky, doporučení pro koncept:
   které varianty konfigurace jdou skutečně ukázat za jízdy a jak).`,
  { label: 'analytik · Porsche web, konfigurátor, stopáž', phase: 'Podklady', agentType: 'analytik', effort: 'high', schema: {
    type: 'object', properties: { stav: { type: 'string', enum: ['HOTOVO', 'BLOKOVÁNO'] }, model: S, fakta: S, znacka: S, konfigurator: S, videa: S,
      podminky: S, doporuceni: S, otazky_pro_rezisera: S },
    required: ['stav', 'model', 'fakta', 'znacka', 'konfigurator', 'videa', 'podminky', 'doporuceni', 'otazky_pro_rezisera'] } }))
log(`Podklady: ${ma ? ma.stav : 'nic'}`)
if (!ma || ma.stav === 'BLOKOVÁNO') return { material: ma, otazky }

phase('Koncept')
const ko = sber('kreativní ředitel', await agent(`${CTX}

## Tvůj úkol: KONCEPT A STŘIHOVÁ PARTITURA (kreativní ředitel)
Materiál: ${M}/materialy/ (katalog.md, konfigurator/, fotky/, videa/ + archy, _prehled.jpg), oddíly „Vůz a fakta“, „Značka“, „Materiál jízdy“ v ${P}.
Zadání uživatele: 30 s, 16:9, **pohodová jízda** tímto Porsche, během které si **vůz upravuješ, jak se ti zalíbí** (konfigurace se mění za jízdy:
barva, kola, interiér…), hudba velmi drahá a odpočinková (hora, výhled do rozmanité krajiny), barvy z porsche.cz, realisticky (vůz musí jet, nic kresleného),
anglicky, bez voiceoveru → **jedna věta na scénu na obrazovce** v tempu řeči.
1. **Koncept jednou větou** + **semínko** (tvar v barvě značky na snímku 0, z něj logo / UI, vrací se, na konci zpět do loga; D10).
2. **Hrdina a stavy**: hrdina = vůz v jízdě; „úpravy za jízdy“ řeš jako **stavy hrdiny** (D8) přechodem přímou manipulací (D7: maska vázaná na ovládací
   prvek konfigurátoru, pixelově zarovnané rendry) nebo jinou proměnou bez střihu. Skutečná stopáž je základ jízdy; rendry konfigurátoru = úpravy.
   Realismus: přechod stopáž ↔ render věrohodný (barva, světlo, směr), žádná koláž. Posuď, jestli je potřeba **test nové techniky** (např. změna barvy
   laku na jedoucím voze ve stopáži maskou / přebarvením v kódu, nebo úprava na rendru, který „jede“ 2,5D) → pole nova_technika (co přesně otestovat).
3. **Střihová partitura** (strih-vzor.md 2, závazná tabulka: # / prvek / příchod / typ / klid / odchod / typ / spojka / věta): max. 1 hrdina + 1 doplněk,
   0 tvrdých střihů v grafické vrstvě, kotva (D13), kaskáda (D14), příchody z rozostření a odchody kratší (D2), klid jen na přečtení (D9), jedno skutečné
   číslo (G9), přechody mezi světy každý jiný (D11), obraz předbíhá větu o 0,1–0,35 s (D1), předveď → zopakuj pomaleji (D15) u klíčové úpravy, konec =
   logo klienta → ticho → boom + záblesk → podpis tvůrce 2 s + disclaimer (C9; jméno tvůrce zatím „strihyontop“, režisér vymění).
4. **Hudba** (pro zvukaře, skládá se až k partituře, D12): nálada, tempo (pomalé, široké), klíčové momenty (začátek jízdy, největší výhled = vrchol,
   první úprava, konec), bez tvrdých dropů; řekni, které z existujících nálad hudba.py (luxusni, pohodova…) jsou blízko a co by chybělo.
5. Kontrolní snímky s kritérii odmítnutí, pasti stavby (realismus, kadence stopáže, grade, C044 zakázané úseky stopáže, C046–C048), pořadí stavby.
   Zapiš vše do ${P} (Režijní list, Storyboard / střihová partitura) po částech.`,
  { label: 'kreativní ředitel · koncept + partitura', phase: 'Koncept', agentType: 'kreativni-reditel', effort: 'high', schema: {
    type: 'object', properties: { koncept_veta: { type: 'string' }, seminko: { type: 'string' }, stavy_hrdiny: S, wow_momenty: S, hudba: S,
      nova_technika: { type: 'string' }, rizika: S, otazky_pro_rezisera: S },
    required: ['koncept_veta', 'seminko', 'stavy_hrdiny', 'wow_momenty', 'hudba', 'nova_technika', 'rizika', 'otazky_pro_rezisera'] } }))
if (!ko) return { material: ma, otazky }

phase('Oponentura')
const op = sber('oponent', await agent(`${CTX}

## Tvůj úkol: OPONENTURA A REVIZE V JEDNOM (nezávislý kreativní ředitel)
Přečti koncept a partituru v ${P} a podklady (archy, katalog, znacka.css). Posuď přísně podle **strih-vzor.md 6** (kontrolní seznam střihu) a vkusu
uživatele: **střih podle vzoru** (3×: jeden hrdina, proměny místo střihů, kotva, kaskáda, klid jen na přečtení, obraz předbíhá větu, podpis tvůrce),
**realismus** (3×: vůz jede, přechod stopáž ↔ render nepozná se, nic kresleného), **pohoda a luxus** (2×: hora, výhled, drahá značka; žádná závodní
energie), nápad a řemeslo (2×). Je „úprava za jízdy“ srozumitelná a věrohodná? Je hrdina pořád jeden? Nejsou mrtvé pasáže ani přetížené snímky?
Pak **opravy rovnou zapracuj** do Režijního listu a partitury v ${P} (cíl 9+ ve střihu, realismu a pohodě) a na konec partitury připiš „Změny po oponentuře“.`,
  { label: 'oponent · posudek a revize partitury', phase: 'Oponentura', agentType: 'kreativni-reditel', effort: 'high', schema: {
    type: 'object', properties: { skore_strih: { type: 'number' }, skore_realismus: { type: 'number' }, skore_pohoda: { type: 'number' },
      skore_celkem: { type: 'number' }, zmeny: S, nova_technika: { type: 'string' }, otazky_pro_rezisera: S },
    required: ['skore_strih', 'skore_realismus', 'skore_pohoda', 'skore_celkem', 'zmeny', 'nova_technika', 'otazky_pro_rezisera'] } }))

const neni = (s) => !s || !s.trim() || /^(ne|žádn|zadn|none|no)/i.test(s.trim())
const technika = (op && !neni(op.nova_technika)) ? op.nova_technika : (!neni(ko.nova_technika) ? ko.nova_technika : '')
let te = null
if (technika) {
  phase('Test')
  te = sber('animátor test', await agent(`${CTX}

## Tvůj úkol: TEST NOVÉ TECHNIKY (animátor), nic víc
**POKRAČOVÁNÍ PO RESTARTU KONTEJNERU (2026-11-05)**: tentýž test už jednou běžel a uprostřed se přerušil restartem kontejneru. V ${M}/test/ už leží:
src/ (209 zdrojových snímků W4, W6, W7, W11, M7…), maska_birefnet/ (58 masek: W11 14, W4 1, W6 24, W7 19), maska_isnet/ (2), lut/ (24), lut_out/ (171 přebarvených),
desky/ (75), kontrola/ (mřížky _grid_*, _lut_*), nahled_nahled/, maska_log.txt, render_log.txt a skripty nastroje/skripty_test_maska.py, nastroje/skripty_test_lut.py.
Nejdřív si je prohlédni a NAVAŽ: hotové masky a LUTy nepřepočítávej, dopočítej jen chybějící. Dlouhé výpočty pouštěj po částech (kontejner se může znovu
restartovat): po každé dávce zapiš stav do ${M}/test/STAV.md (co je hotové, co zbývá). Model BiRefNet je v /root/.rembg/models/birefnet-general/.
Pomocné skripty patří do ${M}/test/_skript/ (ne do nastroje/, C038); na konci přesuň nastroje/skripty_test_*.py tam, nebo z nich udělej čistý nástroj
nastroje/prebarvi.py (jen když je ověřený) a ohlas režisérovi.
Partitura v ${P} vyžaduje techniku, kterou jsme ještě nedělali: „${technika}“. Otestuj ji na 2–4 s výřezu (1920×1080, 60 fps) do ${M}/test/:
skutečný materiál z ${M}/materialy/, kostra nastroje/vzory/scena.html + nastroje/render_html.cjs, pás snímků + 3 klíčové snímky v plném rozlišení,
čas výpočtu na 1 s. Posuď poctivě: působí to realisticky (nepozná se zásah), nebo jako koláž / AI? Co funguje, co ne, doporučení (parametry, masky, grade).
Zapiš do ${P} oddíl „Test techniky“. Nový helper, který se osvědčí, přidej do nastroje/vzory/scena.html (jen ověřený, ohlas režisérovi).`,
    { label: 'animátor · test techniky', phase: 'Test', agentType: 'animator', effort: 'high', schema: {
      type: 'object', properties: { funguje: S, nefunguje: S, doporuceni: S, vykon: { type: 'string' }, otazky_pro_rezisera: S },
      required: ['funguje', 'nefunguje', 'doporuceni', 'vykon', 'otazky_pro_rezisera'] } }))
}
return { material: ma, koncept: ko, oponentura: op, test: te, technika, otazky }
