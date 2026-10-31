export const meta = {
  name: 'v002-vyroba',
  description: 'V002 Mercedes: SFX a mix ∥ klíčové snímky → schválení → pohyb a render → střih → 3 kritici → opravy (max 3 kola, wow ≥ 8, energie ≥ 8,5)',
  phases: [
    { title: 'Výroba', detail: 'zvukař (SFX podle storyboardu, automatika hudby, mix) ∥ animátor (klíčové snímky → schválení → pohyb → render)' },
    { title: 'Střih', detail: 'spojení obrazu a zvuku, mastering, plakát, popisek' },
    { title: 'Kontrola', detail: 'kritik technika · kreativní ředitel wow a energie · kritik zadání a storyboard' },
    { title: 'Opravy', detail: 'nálezy kritiků → animátor / zvukař → nový render' },
  ],
}

const P = 'projekty/002-mercedes-racing/zadani.md'
const M = 'media/projekty/002-mercedes-racing'
const KD = 'media/kontrola/002-mercedes-racing'
const CTX = `Projekt V002 Mercedes-Benz závodní spot, repozitář /home/user/strihyontop (pracuj relativně k němu). Úkol ti zadává režisér (hlavní agent).
Uživatele se nikdy neptáš. Když si nevíš rady, rozhodni rozumně sám, rozhodnutí zapiš a otázku vrať režisérovi v poli otazky_pro_rezisera. Necommituj.
ZÁVAZNÉ PODKLADY: ${P} (zadání uživatele doslova, jeho pravidla 1–6, rozhodnutí režiséra, Režijní list se Vzhledem, STORYBOARD po taktech
včetně „Změn po oponentuře“, kontrolní snímky s kritérii odmítnutí, pasti a pořadí stavby, akceptační kritéria), znalosti/pravidla-strihu.md
(nahoře VKUS UŽIVATELE: energie, rychlost, živost, efekty; o V001 řekl „není to ono, bez duše“), znalosti/chyby.md, znalosti/prompt-motion/poznatky.md.
Značka: ${M}/znacka/ (znacka.css = paleta jako CSS proměnné, PŘEDBĚŽNÁ, barvy jen přes proměnné; mercedes-hvezda-plocha.svg, -fazety.svg,
chrom jen jako PNG; vzornik-znacky.jpg). Hvězdu nikdy nedeformovat (jen jednotné měřítko a otočení).
Hudba: ${M}/hudba.wav + ${M}/hudba.json (128 BPM, doba 0,46875 s, takt 1,875 s, drop 1 = 3,75 s, zlom 15,0 s, stoupání 16,875 s,
drop 2 = 18,75 s, end card 26,25–30,0 s; pole udalosti_nastroju = přesné časy kopáku, úderů, činelů, motoru…).
Formát: 1920×1080, 60 fps, 30,0 s, texty anglicky, bez voiceoveru. Weby Mercedes-Benz vracejí 403: NENAČÍTEJ je a neobcházej.
PRACUJ PO ČÁSTECH (C018): žádný obří výstup najednou, velké soubory stav postupně (kostra + menší Edit), přemýšlej věcně a rozhodnutí rovnou zapisuj.`

const S_ARR = { type: 'array', items: { type: 'string' } }
const ANIM = {
  type: 'object',
  properties: { stav: { type: 'string', enum: ['HOTOVO', 'BLOKOVÁNO'] }, vystup: { type: 'string' }, snimky: S_ARR, co_jsem_udelal: S_ARR,
    rozhodnuti: S_ARR, zname_nedostatky: S_ARR, chyby: S_ARR, otazky_pro_rezisera: S_ARR },
  required: ['stav', 'vystup', 'snimky', 'co_jsem_udelal', 'rozhodnuti', 'zname_nedostatky', 'chyby', 'otazky_pro_rezisera'],
}
const ZVUK = {
  type: 'object',
  properties: { stav: { type: 'string', enum: ['HOTOVO', 'BLOKOVÁNO'] }, vystup_zvuk: { type: 'string' }, vystup_zvuk_bez_hudby: { type: 'string' },
    mereni: { type: 'string', description: 'LUFS, TP, pásma, oktávy, odchylka vrcholů SFX v ms' }, co_jsem_udelal: S_ARR, chyby: S_ARR, otazky_pro_rezisera: S_ARR },
  required: ['stav', 'vystup_zvuk', 'vystup_zvuk_bez_hudby', 'mereni', 'co_jsem_udelal', 'chyby', 'otazky_pro_rezisera'],
}
const REVIEW = {
  type: 'object',
  properties: { schvaleno: { type: 'boolean' }, skore: { type: 'number' }, skore_energie: { type: 'number' }, opravy: S_ARR, co_nechat: S_ARR, otazky_pro_rezisera: S_ARR },
  required: ['schvaleno', 'skore', 'skore_energie', 'opravy', 'co_nechat', 'otazky_pro_rezisera'],
}
const STRIH = {
  type: 'object',
  properties: { stav: { type: 'string', enum: ['HOTOVO', 'BLOKOVÁNO'] }, video: { type: 'string' }, video_bez_hudby: { type: 'string' },
    plakat: { type: 'string' }, popisek: { type: 'string' }, mereni: { type: 'string' }, chyby: S_ARR, otazky_pro_rezisera: S_ARR },
  required: ['stav', 'video', 'video_bez_hudby', 'plakat', 'popisek', 'mereni', 'chyby', 'otazky_pro_rezisera'],
}
const KONTROLA = {
  type: 'object',
  properties: {
    verdikt: { type: 'string', enum: ['SCHVÁLENO', 'OPRAVIT', 'BLOKUJÍCÍ'] },
    skore_wow: { type: 'number', description: 'jen kreativní ředitel 1–10 (vážený průměr), ostatní 0' },
    skore_energie: { type: 'number', description: 'jen kreativní ředitel 1–10, ostatní 0' },
    nalezy: { type: 'array', items: { type: 'object', properties: {
      zavaznost: { type: 'string', enum: ['blokující', 'závažná', 'drobná'] }, oblast: { type: 'string', enum: ['obraz', 'zvuk', 'střih'] },
      cas: { type: 'string' }, problem: { type: 'string' }, dukaz: { type: 'string' }, oprava: { type: 'string' } },
      required: ['zavaznost', 'oblast', 'cas', 'problem', 'dukaz', 'oprava'] } },
    pravidla_uzivatele: { type: 'array', items: { type: 'object', properties: { pravidlo: { type: 'string' }, splneno: { type: 'boolean' }, dukaz: { type: 'string' } },
      required: ['pravidlo', 'splneno', 'dukaz'] } },
    co_je_dobre: S_ARR, otazky_pro_rezisera: S_ARR,
  },
  required: ['verdikt', 'skore_wow', 'skore_energie', 'nalezy', 'pravidla_uzivatele', 'co_je_dobre', 'otazky_pro_rezisera'],
}

const otazky = []
const sber = (kdo, r) => { if (r && r.otazky_pro_rezisera) for (const q of r.otazky_pro_rezisera) otazky.push(`${kdo}: ${q}`); return r }
// Rychlé úseky (švihy, dropy, průlety) dostanou 8 podsnímků, zbytek 4; renderuje se ve 3 prohlížečích (C027). Úseky převzít ze storyboardu.
const RYCHLE = '3.7-4.25,5.6-5.85,7.0-7.55,8.88-9.1,10.78-11.25,16.875-17.34,17.45-17.5,18.1-18.15,18.72-19.0,20.6-20.85,26.2-26.3'
const RENDER = (v) => `node nastroje/render_html.cjs --html ${M}/scena/index.html --out ${M}/render/V002_obraz_v${v}.mp4 --dur 30 --fps 60 --sub 4 --sub-rychle 8 --rychle ${RYCHLE} --audio ${M}/hudba.wav`

// ---------- VÝROBA: zvuk ∥ obraz ----------
phase('Výroba')
const zvukar = () => agent(`${CTX}

## Tvůj úkol: SFX, AUTOMATIKA HUDBY A MIX
Hudba je hotová a schválená režisérem (${M}/hudba.wav, −14 LUFS, bez varování), časování se NESMÍ měnit.
1. SFX přesně podle storyboardu S2 v ${P} (sloupec „zvuk / událost“ + seznam nových a posunutých SFX ve „Změnách po oponentuře“; S1 neplatí):
   nastroje/sfx.py (syntéza, změřený vrchol na čas události ±5 ms).
   Závodní zvuky: průjezd (doppler), švih vzduchu, náraz / úder, záblesk, řazení, pneumatiky, elektrický glitch na glitch akcentech.
   Klíčové momenty (drop 1, drop 2, finální úder 26,25 s) musí být SLYŠET (I3), jinak SFX pod hudbou podle sfx.py.
2. Automatika hudby (sfx.py --automatika) jen tam, kde to storyboard chce (např. ztlumení těsně před dropem pro kontrast). Neměň takty ani časy.
3. Ulož ${M}/zvuk/sfx.wav + sfx.json, mix ${M}/zvuk/zvuk_v1.wav (hudba + SFX, 48 kHz stereo) a ${M}/zvuk/zvuk_bez_hudby_v1.wav.
4. Ověř, že nastroje/master_zvuk.sh z mixu udělá −14 LUFS / ≤ −1 dBTP po AAC, změř pásma, oktávy a odchylky vrcholů. Prohlédni spektrogram (Read).`,
  { label: 'zvukař · SFX, automatika, mix', phase: 'Výroba', agentType: 'zvukar', schema: ZVUK, effort: 'high' },
).then((r) => sber('zvukař', r))

const KLIC_CASY = '18.9,19.1,3.767,0,19.5,27.8'
const BLOKY = [
  { id: 'A', od: 0, do: 9.375, popis: 'T1–T5 (start, LIGHTS OUT, drop 1, FULL THROTTLE, průjezd z boku)', pasy: '3,75 / 4,05–4,22 / 5,625 / 8,906' },
  { id: 'B', od: 9.375, do: 18.75, popis: 'T6–T10 (tiker BUILT TO RACE, vracečka, mapa → prstenec, zlom, stoupání 2D → 3D)', pasy: '10,78–11,25 / 15,0 / 16,875–17,34 / 17,475 / 18,125' },
  { id: 'C', od: 18.75, do: 30, popis: 'T11–T16 (drop 2 hvězda ze světla, revolver, tři stopy, sběh do hvězdy, end card)', pasy: '18,75–18,91 / 19,22–19,55 / 20,625 / 22,5 / 24,61 / 26,25' },
]

const obraz = async () => {
  const klic = sber('animátor (klíčové snímky)', await agent(`${CTX}

## Tvůj úkol: KNIHOVNA VOZŮ, HVĚZDA A KLÍČOVÉ SNÍMKY (statické)
Postav scénu ve složce ${M}/scena/: index.html + klasické skripty přes <script src> (ES moduly přes file:// nefungují), rozděl je
(např. zaklad.js, znacka.js, vozy.js, efekty.js, texty.js, blokA.js, blokB.js, blokC.js, scena.js). Vyjdi z nastroje/vzory/scena.html (FONTY +
document.fonts.load, easing, pruzina, usazeni, kf, nahoda, kamera, rozmazani, #mrizka). Paletu vlož ze ${M}/znacka/znacka.css (barvy jen přes proměnné).
Podle „Pořadí stavby“ a „Pastí stavby“ v ${P}:
1. **Knihovna 4 vozů ve variantách A a B** (F1-předek, F1-shora, GT-bok, F1-záď; A podle storyboardu, B silueta z okrajového světla),
   helma s hledím, odznak Ø 110 a **hvězda ze světla** (polygony ramen s fazetami z ${M}/znacka/hvezda_generator.py, i rozpracovaná v 18,83
   a 18,90) na jednom testovacím listu 1920×1080 (${M}/scena/vozy_test.html → ${M}/render/vozy_test.png + zmenšenina 480 px). Prémiově,
   žádný klipart, žádná čísla ani sponzoři. Každý vůz si prohlédni (Read) na 480 px: je to formule / závodní GT? Hvězda = hvězda Mercedes?
2. **Statické klíčové snímky** ${KLIC_CASY} s (drop 2 hvězda z polygonů, plakát, drop 1, náhled, 3 kamery, end card s mercedes-benz.cz) podle storyboardu S2,
   s variantou vozů, kterou na 480 px považuješ za lepší (kreativní ředitel ji potvrdí):
   node nastroje/render_html.cjs --html ${M}/scena/index.html --out ${M}/render/klic.mp4 --dur 30 --nahled casy --casy ${KLIC_CASY}
   + zmenšenina každého snímku na šířku 480 px. Bezpečné zóny ověř s ?mrizka.
Snímky si PROHLÉDNI (Read), sám je zkritizuj podle kritérií odmítnutí v ${P} a opravuj, dokud nejsou na úrovni špičkového motion designu.
Pohyb ještě nestav. Vrať cesty ke všem snímkům (vystup = složka náhledu).`,
    { label: 'animátor · vozy, hvězda, klíčové snímky', phase: 'Výroba', agentType: 'animator', schema: ANIM, effort: 'high' }))
  if (!klic) return null
  const rev = sber('kreativní ředitel (klíčové snímky)', await agent(`${CTX}

## Tvůj úkol: SCHVÁLENÍ KNIHOVNY VOZŮ A KLÍČOVÝCH SNÍMKŮ
Animátor postavil testovací list vozů a hvězdy a statické klíčové snímky ${KLIC_CASY} s. Soubory: ${JSON.stringify(klic.snimky)} (složka ${klic.vystup}).
Prohlédni je (Read) a posuď proti storyboardu S2, Vzhledu, Pastem a kritériím odmítnutí v ${P}. U každého vozu VYBER variantu A nebo B (napiš do opravy).
Test zmenšeniny 480 px: čte se formule a závodní GT?
čte se Mercedes (hvězda věrná logu)? Je ze snímků drop 1 a drop 2 cítit energie? Nevypadá to jako klipart, hračka nebo „AI render“?
schvaleno = true jen při úrovni špičkového motion designu (skore ≥ 8 a skore_energie ≥ 8). Dej konkrétní opravy (co přesně, kde, o kolik)
seřazené podle dopadu na wow a co nechat beze změny. Nic neměň.`,
    { label: 'kreativní ředitel · schválení vozů a klíčových snímků', phase: 'Výroba', agentType: 'kreativni-reditel', schema: REVIEW, effort: 'high' }))
  let poznamky = rev ? rev.opravy : []
  log(`Klíčové snímky: ${rev ? (rev.schvaleno ? 'schváleno' : 'k opravě') + ', skóre ' + rev.skore + ', energie ' + rev.skore_energie : 'bez posudku'}`)
  if (rev && !rev.schvaleno) {
    const oprava = sber('animátor (oprava klíčových snímků)', await agent(`${CTX}

## Tvůj úkol: OPRAVA VOZŮ A KLÍČOVÝCH SNÍMKŮ
Kreativní ředitel NESCHVÁLIL (skóre ${rev.skore}, energie ${rev.skore_energie}). Opravy: ${JSON.stringify(rev.opravy)}
Nech beze změny: ${JSON.stringify(rev.co_nechat)}. Scéna je v ${M}/scena/. Oprav, znovu vyrenderuj testovací list a klíčové snímky ${KLIC_CASY}
+ zmenšeniny 480 px, prohlédni a vrať cesty.`,
      { label: 'animátor · oprava vozů a klíčových snímků', phase: 'Výroba', agentType: 'animator', schema: ANIM, effort: 'high' }))
    poznamky = oprava ? oprava.zname_nedostatky : poznamky
  }
  // Pohyb po třech blocích, každý blok vlastní agent (menší kontext, C018). Bloky jdou po sobě, protože sdílejí scénu.
  let posledni = null
  for (const b of BLOKY) {
    posledni = sber(`animátor (pohyb ${b.id})`, await agent(`${CTX}

## Tvůj úkol: POHYB, BLOK ${b.id}: ${b.od}–${b.do} s, ${b.popis}
Scéna je v ${M}/scena/, knihovna vozů a klíčové snímky jsou schválené. Připomínky, které ještě platí: ${JSON.stringify(poznamky)}.
${b.id !== 'A' ? 'Předchozí bloky jsou hotové: NEROZBIJ je (na konci zkontroluj 2 snímky z každého předchozího bloku a návaznost na hranici ' + b.od + ' s).' : ''}
Postav pohyb podle storyboardu TAKT PO TAKTU (po částech!), jen v tomto bloku. Časy hudby z ${M}/hudba.json (udalosti_nastroju: kopák, malý buben,
stab, úder, činel, motor, řazení, vír), ne odhadem. Energie: událost na každou dobu, žádná mrtvá pasáž > ~1 s, efekty synchronní s hudbou.
Dodrž Pasti stavby. Po každém taktu kontrolní snímky (--nahled casy) a oprav. Pak kontrolní snímky z tabulky v ${P} pro tento blok
a pásy sousedních snímků (--sub 8, krátký výřez kolem času) u ${b.pasy}. Prohlédni je a oprav vše, co odporuje kritériím odmítnutí.
Výkon: změř, kolik sekund výpočtu stojí 1 s videa v tomto bloku (render krátkého výřezu); když je to víc než ~40 s, zjednoduš (Pasti: výkon).
Plný render nedělej. vystup = složka s kontrolními snímky, snimky = cesty k nim.`,
      { label: `animátor · pohyb blok ${b.id}`, phase: 'Výroba', agentType: 'animator', schema: ANIM, effort: 'high' }))
    if (!posledni || posledni.stav !== 'HOTOVO') { log(`Pohyb blok ${b.id}: ${posledni ? posledni.stav : 'bez výsledku'}`); break }
  }
  return sber('animátor (render)', await agent(`${CTX}

## Tvůj úkol: CELKOVÁ KONTROLA POHYBU A PLNÝ RENDER v1
Scéna ${M}/scena/ má hotový pohyb všech tří bloků. Nejdřív node nastroje/render_html.cjs --html ${M}/scena/index.html --out ${M}/render/doby.mp4
--dur 30 --nahled doby --bpm 128 a prohlédni snímky na doby (návaznost bloků 9,375 a 18,75, nic nezamrzlé, jedna vrstva textu).
Oprav, co nesedí. Pak plný render (dlouhý, spusť a počkej): ${RENDER(1)}
Pak nastroje/kontrola.sh ${M}/render/V002_obraz_v1.mp4 ${KD}/animator-v1, projdi arch.jpg a pásy snímků, oprav případné chyby a vyrenderuj znovu.
vystup = cesta k finálnímu MP4.`,
    { label: 'animátor · plný render v1', phase: 'Výroba', agentType: 'animator', schema: ANIM, effort: 'high' }))
}

const [zv, an] = await parallel([zvukar, obraz])
if (!an || !an.vystup) return { chyba: 'animátor nedodal render', zvuk: zv, otazky }
if (!zv || !zv.vystup_zvuk) return { chyba: 'zvukař nedodal zvuk', obraz: an, otazky }
log(`Výroba hotová: obraz ${an.vystup}, zvuk ${zv.vystup_zvuk}`)

// ---------- STŘIH → KONTROLA → OPRAVY ----------
const KRITICI = [
  { id: 'technika', typ: 'kritik', pohled: `TECHNIKA A KONTROLNÍ SEZNAM K: spusť nastroje/kontrola.sh VIDEO ${KD}/kolo{n}-technika, projdi arch.jpg, každý pás snímků
a detailní snímky v časech z tabulky kontrolních snímků v ${P} (kritéria odmítnutí!). Ověř akceptační kritéria 1–8, bezpečné zóny 16:9,
texty a překlepy, AI znaky, lineární pohyb, duchy u švihů, a hvězdu (překrytím s ${M}/znacka/mercedes-hvezda-plocha-bila_1024.png nebo měřením
poměru stran: nedeformovaná). skore_wow = 0, skore_energie = 0.` },
  { id: 'wow', typ: 'kreativni-reditel', pohled: `WOW A ENERGIE: prohlédni video jako celek (arch po 0,5 s, detailní snímky, sousední snímky u dropů a přechodů).
Hodnoť 1–10 podle své role: energie a živost (3×), nápad (2×), řemeslo pohybu (2×), značka a nálada, čitelnost 16:9, bez šablonovitého vzhledu.
skore_wow = vážený průměr, skore_energie zvlášť. Pojmenuj s časy, kde jsou ve videu poznat 4 zvolené motiony (akceptační kritérium 9).
Nálezy = konkrétní opravy s největším dopadem na wow a energii (čas, co, o kolik).` },
  { id: 'zadani', typ: 'kritik', pohled: `ZADÁNÍ, ZNAČKA A STORYBOARD: pravidla uživatele 1–6 a rozhodnutí režiséra (každé zvlášť s důkazem). Porovnej video se storyboardem
řádek po řádku (snímky v časech řádků, odchylka max ±1 snímek). Barvy změř v pixelech proti ${M}/znacka/znacka.css (±4), font, logo, texty jen
z hesel a obecné (C8, žádná fakta, čísla, jména, sponzoři), end card + disclaimer „Concept ad · not affiliated with Mercedes-Benz“, a jestli
SFX a efekty sedí na dobách a úderech (porovnej obálku zvuku s časy z hudba.json). skore_wow = 0, skore_energie = 0.` },
]

let kolo = 1
let videoObraz = an.vystup
let zvuk = zv.vystup_zvuk
let zvukBez = zv.vystup_zvuk_bez_hudby
let strihNalezy = []
let posledniStrih = null
let posledniKontroly = []
const historie = []
let schvaleno = false

while (kolo <= 3) {
  phase('Střih')
  const st = sber(`střihač (kolo ${kolo})`, await agent(`${CTX}

## Tvůj úkol: STŘIH v${kolo}
Vstupy: obraz ${videoObraz} (60 fps, pracovní zvuk se nahradí), zvuk ${zvuk} (hudba + SFX), zvuk bez hudby ${zvukBez}.
${strihNalezy.length ? 'Nálezy kritiků k opravě ve střihu: ' + JSON.stringify(strihNalezy) : ''}
1. ${M}/vystup/V002_v${kolo}.mp4: obraz bez původní zvukové stopy + zvuk; video stopu nepřekódovávej, když to jde; pak nastroje/master_zvuk.sh
   (−14 LUFS, ≤ −1 dBTP po AAC). Výsledek přesně 30,0 s, 1920×1080, 60 fps, H.264 High yuv420p, BT.709, AAC 48 kHz, faststart.
2. ${M}/vystup/V002_v${kolo}_bez_hudby.mp4 (jen SFX), také masterovaný.
3. Plakát: nejsilnější snímek (drop 2 nebo end card, ne černý) → ${M}/vystup/V002_v${kolo}_plakat.jpg.
4. ${M}/vystup/popisek.txt anglicky: háček, otázka pro komentáře (J3), disclaimer „Concept ad · not affiliated with Mercedes-Benz“ (J5),
   uvedení zdroje loga „Mercedes star: Khaled / Wikimedia Commons, CC BY-SA 4.0“, 3–5 hashtagů (J4). Žádný @handle značky, žádná fakta.
5. nastroje/kontrola.sh na hlavní výstup → ${KD}/strih-v${kolo}, projdi arch.jpg. Vrať cesty a měření.`,
    { label: `střihač · v${kolo}`, phase: 'Střih', agentType: 'strihac', schema: STRIH, effort: 'high' }))
  if (!st || !st.video) { log('střih selhal'); break }
  posledniStrih = st

  phase('Kontrola')
  const kontroly = (await parallel(KRITICI.map((k) => () => agent(`${CTX}

## Tvůj úkol: KONTROLA KOLO ${kolo}, pohled ${k.id.toUpperCase()}
Video: ${st.video} (verze bez hudby ${st.video_bez_hudby}, plakát ${st.plakat}). Posuzuj jen výstup, ne tvrzení autorů.
${k.pohled.replace('{n}', String(kolo)).replace('VIDEO', st.video)}
Závažnost: blokující = porušené pravidlo uživatele, chybný formát nebo text, technická vada, deformované logo; závažná = viditelně snižuje kvalitu
(AI znaky, rytmus, nečitelnost, mimo storyboard, mrtvá pasáž bez energie); drobná = vylepšení. Oblast nálezu: obraz / zvuk / střih.
Každý nález musí mít důkaz (snímek, čas, měření).`,
    { label: `kontrola ${kolo} · ${k.id}`, phase: 'Kontrola', agentType: k.typ, schema: KONTROLA, effort: 'high' },
  ).then((r) => sber(`kritik ${k.id} (kolo ${kolo})`, r))))).filter(Boolean)
  posledniKontroly = kontroly

  const nalezy = kontroly.flatMap((k) => k.nalezy || [])
  const vazne = nalezy.filter((n) => n.zavaznost !== 'drobná')
  const wowK = kontroly.find((k) => k.skore_wow > 0)
  const wow = wowK ? wowK.skore_wow : 0
  const energie = wowK ? wowK.skore_energie : 0
  historie.push({ kolo, wow, energie, verdikty: kontroly.map((k) => k.verdikt), vazne: vazne.length, drobne: nalezy.length - vazne.length, video: st.video })
  log(`Kolo ${kolo}: wow ${wow}, energie ${energie}, blokujících a závažných ${vazne.length}, drobných ${nalezy.length - vazne.length}`)
  if (vazne.length === 0 && wow >= 8 && energie >= 8.5) { schvaleno = true; break }
  if (kolo === 3) break

  phase('Opravy')
  const chvala = kontroly.flatMap((k) => k.co_je_dobre || [])
  const proObraz = nalezy.filter((n) => n.oblast === 'obraz')
  const proZvuk = nalezy.filter((n) => n.oblast === 'zvuk')
  strihNalezy = nalezy.filter((n) => n.oblast === 'střih')
  const dalsi = kolo + 1
  const [o, z] = await parallel([
    () => (proObraz.length ? agent(`${CTX}

## Tvůj úkol: OPRAVY OBRAZU, KOLO ${kolo} → v${dalsi}
Scéna je v ${M}/scena/. Nálezy kritiků k obrazu: ${JSON.stringify(proObraz)}
Co kritici chválí a nesmí se rozbít: ${JSON.stringify(chvala)}
Oprav všechny blokující a závažné nálezy, drobné tam, kde je to rychlé. Kontrolní snímky upravených míst (prohlédni), pak plný render:
${RENDER(dalsi)}
a nastroje/kontrola.sh na výsledek → ${KD}/animator-v${dalsi}. vystup = cesta k novému MP4.`,
      { label: `animátor · opravy v${dalsi}`, phase: 'Opravy', agentType: 'animator', schema: ANIM, effort: 'high' }).then((r) => sber(`animátor (opravy v${dalsi})`, r)) : Promise.resolve(null)),
    () => (proZvuk.length ? agent(`${CTX}

## Tvůj úkol: OPRAVY ZVUKU, KOLO ${kolo} → v${dalsi}
Současný mix: ${zvuk}. Nálezy kritiků ke zvuku: ${JSON.stringify(proZvuk)}
Oprav je, časování hudby neměň. Ulož ${M}/zvuk/zvuk_v${dalsi}.wav a ${M}/zvuk/zvuk_bez_hudby_v${dalsi}.wav a změř.`,
      { label: `zvukař · opravy v${dalsi}`, phase: 'Opravy', agentType: 'zvukar', schema: ZVUK, effort: 'high' }).then((r) => sber(`zvukař (opravy v${dalsi})`, r)) : Promise.resolve(null)),
  ])
  if (o && o.vystup) videoObraz = o.vystup
  if (z && z.vystup_zvuk) { zvuk = z.vystup_zvuk; zvukBez = z.vystup_zvuk_bez_hudby || zvukBez }
  kolo++
}

return {
  schvaleno,
  kol: historie.length,
  historie,
  vystup: posledniStrih,
  zvuk: zv ? { mereni: zv.mereni, co: zv.co_jsem_udelal, chyby: zv.chyby } : null,
  animator: an ? { co: an.co_jsem_udelal, rozhodnuti: an.rozhodnuti, nedostatky: an.zname_nedostatky, chyby: an.chyby } : null,
  posledni_kontrola: posledniKontroly.map((k) => ({ verdikt: k.verdikt, wow: k.skore_wow, energie: k.skore_energie, nalezy: k.nalezy, pravidla: k.pravidla_uzivatele, dobre: k.co_je_dobre })),
  otazky,
}
