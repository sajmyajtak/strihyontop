export const meta = {
  name: 'v004-vyroba',
  description: 'V004 BMW jízda (úsporně): zvukař ∥ střihač záběry → animátor klíčové snímky → schválení → pohyb 2 bloky + render + zvuk → 2 kontroly na kolo → opravy',
  phases: [
    { title: 'Výroba', detail: 'zvukař (SFX + mix) ∥ střihač (záběry jízdy: výběr, grade, 1,2×, snímky 30 fps) → animátor (klíčové snímky → schválení → 2 bloky + render + zvuk)' },
    { title: 'Kontrola', detail: 'kritik (technika + zadání) · kreativní ředitel (jízda, realismus, energie, wow)' },
    { title: 'Opravy', detail: 'animátor (+ zvukař jen při nálezech ke zvuku)' },
  ],
}

const P = 'projekty/004-bmw-jizda/zadani.md'
const M = 'media/projekty/004-bmw-jizda'
const KD = 'media/kontrola/004-bmw-jizda'
const CTX = `Projekt V004 BMW i7 M70 s jízdou, repozitář /home/user/strihyontop (pracuj relativně k němu). Úkol ti zadává režisér (hlavní agent).
Uživatele se nikdy neptáš. Když si nevíš rady, rozhodni rozumně sám, zapiš to a otázku vrať režisérovi v poli otazky_pro_rezisera. Necommituj.
ZÁVAZNÉ: ${P} (zadání doslova, pravidla, ROZHODNUTÍ UŽIVATELE = varianta 1, odpovědi režiséra, Materiál jízdy, Test realistické jízdy, Předlohy
od uživatele, Režijní list, STORYBOARD včetně „Změn po oponentuře“, kontrolní snímky, pasti, pořadí stavby, kritéria), znalosti/pravidla-strihu.md
(VKUS UŽIVATELE: energie, nic kresleného, VŮZ MUSÍ JET; G7, G8, D7), znalosti/chyby.md (C027, C028, C033, C034, C036, C037, C039, C040, C041).
Materiály ${M}/materialy/ (katalog.md, videa/, fotky/, konfigurator/), test ${M}/test/ (skripty/test_a.sh = grade a 1,2× pro záběry, t_c_saas.html
= SaaS karta přes jízdu), značka ${M}/znacka/ (znacka.css, Manrope, logo/vrstvy). Hudba ${M}/hudba.wav + hudba.json (120 BPM, drop 1 4,0, zlom 12,0,
stoupání 16,0, drop 2 18,0, end card 26,0–30,0). Formát 1920×1080, 60 fps, 30,0 s, bez voiceoveru, anglicky.
PRACUJ PO ČÁSTECH (C018), věcně. Agentů je málo: svou část udělej celou a ověř ji sám.`

const S = { type: 'array', items: { type: 'string' } }
const ANIM = { type: 'object', properties: { stav: { type: 'string', enum: ['HOTOVO', 'BLOKOVÁNO'] }, vystup: { type: 'string' }, snimky: S,
  co_jsem_udelal: S, zname_nedostatky: S, chyby: S, otazky_pro_rezisera: S },
  required: ['stav', 'vystup', 'snimky', 'co_jsem_udelal', 'zname_nedostatky', 'chyby', 'otazky_pro_rezisera'] }
const ZVUK = { type: 'object', properties: { stav: { type: 'string', enum: ['HOTOVO', 'BLOKOVÁNO'] }, vystup_zvuk: { type: 'string' },
  vystup_zvuk_bez_hudby: { type: 'string' }, mereni: { type: 'string' }, chyby: S, otazky_pro_rezisera: S },
  required: ['stav', 'vystup_zvuk', 'vystup_zvuk_bez_hudby', 'mereni', 'chyby', 'otazky_pro_rezisera'] }
const REVIEW = { type: 'object', properties: { schvaleno: { type: 'boolean' }, skore: { type: 'number' }, skore_jizda: { type: 'number' },
  skore_realismus: { type: 'number' }, skore_energie: { type: 'number' }, opravy: S, co_nechat: S, otazky_pro_rezisera: S },
  required: ['schvaleno', 'skore', 'skore_jizda', 'skore_realismus', 'skore_energie', 'opravy', 'co_nechat', 'otazky_pro_rezisera'] }
const KONTROLA = { type: 'object', properties: {
  verdikt: { type: 'string', enum: ['SCHVÁLENO', 'OPRAVIT', 'BLOKUJÍCÍ'] },
  skore_wow: { type: 'number' }, skore_jizda: { type: 'number' }, skore_realismus: { type: 'number' }, skore_energie: { type: 'number' },
  nalezy: { type: 'array', items: { type: 'object', properties: {
    zavaznost: { type: 'string', enum: ['blokující', 'závažná', 'drobná'] }, oblast: { type: 'string', enum: ['obraz', 'zvuk', 'střih'] },
    cas: { type: 'string' }, problem: { type: 'string' }, dukaz: { type: 'string' }, oprava: { type: 'string' } },
    required: ['zavaznost', 'oblast', 'cas', 'problem', 'dukaz', 'oprava'] } },
  pravidla_uzivatele: { type: 'array', items: { type: 'object', properties: { pravidlo: { type: 'string' }, splneno: { type: 'boolean' }, dukaz: { type: 'string' } },
    required: ['pravidlo', 'splneno', 'dukaz'] } },
  co_je_dobre: S, otazky_pro_rezisera: S },
  required: ['verdikt', 'skore_wow', 'skore_jizda', 'skore_realismus', 'skore_energie', 'nalezy', 'pravidla_uzivatele', 'co_je_dobre', 'otazky_pro_rezisera'] }

const otazky = []
const sber = (kdo, r) => { if (r && r.otazky_pro_rezisera) for (const q of r.otazky_pro_rezisera) otazky.push(`${kdo}: ${q}`); return r }
const RYCHLE = '3.9-4.5,11.9-12.3,17.9-18.6,25.9-26.4'

phase('Výroba')
const zvukP = agent(`${CTX}

## Tvůj úkol: SFX A MIX (zvukař)
Podle storyboardu v ${P} (sloupec zvuku): nastroje/sfx.py (syntéza, změřený vrchol na čas události ±5 ms). Zvuky: průjezdy (doppler), vzduch
a pneumatiky při rychlosti, elektrický motor i7 (vysoký tón, žádný spalovací motor), švihy přechodů, prémiové UI (klik, karta, číslice), úder
dropů a loga. Klíčové momenty slyšet (I3), stoupání roste a drop 2 nejhlasitější (C032), nádech před dropy. Seznam událostí do
projekty/004-bmw-jizda/sfx_udalosti.json. Výstupy ${M}/zvuk/zvuk_v1.wav a zvuk_bez_hudby_v1.wav (C039: odvozené soubory přegenerovat nebo smazat).
Master z mixu −14 LUFS / ≤ −1 dBTP po AAC ověř, změř pásma a RMS po 0,5 s. Krátce zapiš „Zvuk v1“ do ${P}.`,
  { label: 'zvukař · SFX a mix', phase: 'Výroba', agentType: 'zvukar', schema: ZVUK, effort: 'high' }).then((r) => sber('zvukař', r))

const obrazP = (async () => {
  const st = sber('střihač', await agent(`${CTX}

## Tvůj úkol: ZÁBĚRY JÍZDY PRO SCÉNU (střihač)
Podle storyboardu v ${P} připrav všechny skutečné záběry (jízda, salon z videí bmw.cz): přesný výřez ze zdroje (čas ve zdroji ze storyboardu,
uprav, když najdeš lepší místo se stejným obsahem), ořez do 16:9 bez textů a vodoznaků, **high-key grade** z testu (skripty/test_a.sh), rychlost
**1,2×** a převod na **30 fps** (kadence 2:2 pro 60 fps, C027 a zjištění testu, žádná interpolace), barevné sjednocení s rendry konfigurace.
Výstup každého záběru jako sekvence JPG (kvalita 2–3) v ${M}/zabery/<id>/ + malý náhled; seznam ${M}/zabery/seznam.json
(id, zdroj, čas ve zdroji, délka, počet snímků, poznámka). Prohlédni každý záběr (pás snímků) a vyřaď ty, kde je vidět čelní pohled s chromovými
ledvinkami, text, vodoznak nebo artefakt. Zapiš do ${P} oddíl „Záběry pro scénu“.`,
    { label: 'střihač · záběry jízdy', phase: 'Výroba', agentType: 'strihac', schema: {
      type: 'object', properties: { stav: { type: 'string', enum: ['HOTOVO', 'BLOKOVÁNO'] }, zabery: S, chyby: S, otazky_pro_rezisera: S },
      required: ['stav', 'zabery', 'chyby', 'otazky_pro_rezisera'] }, effort: 'high' }))
  if (!st || st.stav !== 'HOTOVO') return { chyba: 'záběry nedodány', st }
  const klic = sber('animátor (klíčové snímky)', await agent(`${CTX}

## Tvůj úkol: KOSTRA SCÉNY A KLÍČOVÉ SNÍMKY (animátor)
Záběry jízdy jsou v ${M}/zabery/ (seznam.json). Postav scénu ${M}/scena/ (index.html + skripty přes <script src>) z nastroje/vzory/scena.html:
skutečné záběry jako sekvence snímků (výběr snímku podle času, hranice posunutá o 1/120 s, aby podsnímky nemíchaly dva zdrojové snímky),
rendry konfigurace (masky, světla zap / vyp jako ve V003), SaaS grafika podle předloh a G8, barvy ze znacka.css. Klíčové snímky podle „Pořadí stavby“
v ${P} (drop 1, drop 2, salon, logo 26,0, snímek 0) z výřezu s podsnímky (--od/--dur, C028) + zmenšeniny 480 px. Prohlédni, zkritizuj podle kritérií
odmítnutí a oprav. vystup = složka náhledu, snimky = cesty.`,
    { label: 'animátor · kostra a klíčové snímky', phase: 'Výroba', agentType: 'animator', schema: ANIM, effort: 'high' }))
  if (!klic) return null
  const rev = sber('kreativní ředitel (klíčové snímky)', await agent(`${CTX}

## Tvůj úkol: SCHVÁLENÍ KLÍČOVÝCH SNÍMKŮ (kreativní ředitel)
Soubory: ${JSON.stringify(klic.snimky)} (složka ${klic.vystup}). Posuď proti storyboardu a kritériím v ${P}: vypadá to jako skutečná reklama BMW?
Je vidět jízda a rychlost? Sedí přechod skutečný záběr ↔ render (barva, světlo)? Pozná se koláž nebo AI? SaaS grafika podle předloh?
schvaleno = true jen při skore ≥ 8,5, skore_jizda ≥ 8,5, skore_realismus ≥ 8,5, skore_energie ≥ 8. Konkrétní opravy seřazené podle dopadu. Nic neměň.`,
    { label: 'kreativní ředitel · schválení klíčových snímků', phase: 'Výroba', agentType: 'kreativni-reditel', schema: REVIEW, effort: 'high' }))
  const opravy = rev && !rev.schvaleno ? rev.opravy : []
  log(`Klíčové snímky: ${rev ? (rev.schvaleno ? 'schváleno' : 'k opravě') + ' ' + rev.skore + ' / jízda ' + rev.skore_jizda + ' / realismus ' + rev.skore_realismus : 'bez posudku'}`)
  const b1 = sber('animátor (blok 1)', await agent(`${CTX}

## Tvůj úkol: ${opravy.length ? 'OPRAVY KLÍČOVÝCH SNÍMKŮ + ' : ''}POHYB BLOK 1: 0,0–16,0 s (animátor)
${opravy.length ? 'Nejdřív oprav klíčové snímky podle kreativního ředitele: ' + JSON.stringify(opravy) + '. Nech beze změny: ' + JSON.stringify(rev.co_nechat) + '.' : 'Klíčové snímky schválené.'}
Pak postav pohyb 0,0–16,0 podle storyboardu TAKT PO TAKTU (po částech), časy z hudba.json. Energie: událost na každou dobu, střih na doby v jízdě,
žádná mrtvá pasáž. Kontrolní snímky z tabulky v ${P} a pásy u přechodů (výřez s podsnímky). Změř výkon 1 s výřezu (C027). Plný render nedělej.`,
    { label: 'animátor · blok 1 (0–16)', phase: 'Výroba', agentType: 'animator', schema: ANIM, effort: 'high' }))
  if (!b1 || b1.stav !== 'HOTOVO') return null
  const zv = await zvukP
  return sber('animátor (blok 2 + render)', await agent(`${CTX}

## Tvůj úkol: POHYB BLOK 2: 16,0–30,0 s + PLNÝ RENDER + ZVUK (animátor)
Blok 1 (0–16) je hotový, nerozbij ho (zkontroluj 3 snímky a návaznost na 16,0). Postav 16,0–30,0 podle storyboardu (stoupání, drop 2 rychlost a výkon,
logo 26,0, end card s disclaimerem „Concept ad · not affiliated with BMW“). Kontrolní snímky a pásy. Pak --nahled doby --bpm 120 celého videa
a plný render: node nastroje/render_html.cjs --html ${M}/scena/index.html --out ${M}/render/V004_obraz_v1.mp4 --dur 30 --fps 60 --sub 4 --sub-rychle 8
--rychle ${RYCHLE} (doplň rychlé úseky ze storyboardu). Spoj se zvukem ${zv && zv.vystup_zvuk ? zv.vystup_zvuk : M + '/zvuk/zvuk_v1.wav'} (video stopu nepřekódovávej)
a nastroje/master_zvuk.sh → ${M}/vystup/V004_v1.mp4. nastroje/kontrola.sh → ${KD}/v1, projdi arch a pásy, oprav a případně renderuj znovu.
vystup = cesta k V004_v1.mp4.`,
    { label: 'animátor · blok 2 + render + zvuk', phase: 'Výroba', agentType: 'animator', schema: ANIM, effort: 'high' }))
})()

const [zv, an] = await Promise.all([zvukP, obrazP])
if (!an || !an.vystup) return { chyba: 'obraz nedodán', zvuk: zv, animator: an, otazky }

const KRITICI = [
  { id: 'kritik', typ: 'kritik', pohled: (n, v) => `TECHNIKA + ZADÁNÍ: nastroje/kontrola.sh ${v} ${KD}/kolo${n}-kritik, arch, pásy, kontrolní snímky z tabulky v ${P}.
Akceptační kritéria 1–8, pravidla uživatele (každé zvlášť s důkazem), rozhodnutí uživatele (varianta 1), fakta doslova, barvy UI proti znacka.css,
bezpečné zóny, texty, AI znaky a koláž (lem masky, nesedící světlo nebo barva mezi záběrem a rendrem, duchové, trhaná kadence 25→60 fps),
logo, SFX na událostech. skore_* = 0.` },
  { id: 'wow', typ: 'kreativni-reditel', pohled: (n, v) => `JÍZDA, REALISMUS, ENERGIE, WOW: prohlédni video jako celek (arch po 0,5 s, sousední snímky u dropů a přechodů).
skore_jizda (je vidět jízda a rychlost?), skore_realismus (pozná se AI nebo koláž?), skore_energie, skore_wow = vážený průměr (jízda 3×, realismus 3×,
energie 3×, nápad a řemeslo 2×). Které 4 předlohy uživatele jsou poznat a kde. Nálezy = konkrétní opravy s největším dopadem.` },
]

let kolo = 1
let video = an.vystup
let zvuk = zv ? zv.vystup_zvuk : null
const historie = []
let posledni = []
let schvaleno = false
let opravenaMista = ''
while (kolo <= 3) {
  phase('Kontrola')
  const kontroly = (await parallel(KRITICI.map((k) => () => agent(`${CTX}

## Tvůj úkol: KONTROLA KOLO ${kolo}, pohled ${k.id.toUpperCase()}
Video: ${video}. Posuzuj jen výstup, ne tvrzení autorů. ${opravenaMista ? 'V tomto kole se opravovalo hlavně: ' + opravenaMista + '. Ty místa zkontroluj podrobně, zbytek přehledově.' : ''}
${k.pohled(kolo, video)}
Závažnost: blokující = porušené pravidlo uživatele, chybný fakt nebo formát, vůz nejede, kreslený vůz, deformované logo; závažná = viditelně snižuje
kvalitu (koláž, AI znaky, rytmus, mrtvá pasáž); drobná = vylepšení. Každý nález s důkazem.`,
    { label: `kontrola ${kolo} · ${k.id}`, phase: 'Kontrola', agentType: k.typ, schema: KONTROLA, effort: 'high' },
  ).then((r) => sber(`${k.id} (kolo ${kolo})`, r))))).filter(Boolean)
  posledni = kontroly
  const nalezy = kontroly.flatMap((k) => k.nalezy || [])
  const vazne = nalezy.filter((n) => n.zavaznost !== 'drobná')
  const w = kontroly.find((k) => k.skore_wow > 0) || {}
  historie.push({ kolo, wow: w.skore_wow, jizda: w.skore_jizda, realismus: w.skore_realismus, energie: w.skore_energie,
    verdikty: kontroly.map((k) => k.verdikt), vazne: vazne.length, drobne: nalezy.length - vazne.length, video })
  log(`Kolo ${kolo}: wow ${w.skore_wow}, jízda ${w.skore_jizda}, realismus ${w.skore_realismus}, energie ${w.skore_energie}, závažných ${vazne.length}`)
  if (vazne.length === 0 && (w.skore_wow || 0) >= 8.5 && (w.skore_jizda || 0) >= 8.5 && (w.skore_realismus || 0) >= 8.5) { schvaleno = true; break }
  if (kolo === 3 || (kolo === 2 && vazne.length === 0)) break
  phase('Opravy')
  const proZvuk = nalezy.filter((n) => n.oblast === 'zvuk' && n.zavaznost !== 'drobná')
  const proObraz = nalezy.filter((n) => n.oblast !== 'zvuk')
  const dalsi = kolo + 1
  const [o, z] = await parallel([
    () => agent(`${CTX}

## Tvůj úkol: OPRAVY OBRAZU, KOLO ${kolo} → v${dalsi} (animátor)
Scéna ${M}/scena/. Nálezy: ${JSON.stringify(proObraz)}. Co je dobré a nesmí se rozbít: ${JSON.stringify(kontroly.flatMap((k) => k.co_je_dobre || []))}.
Oprav blokující a závažné, drobné jen když jsou rychlé. Výřezy s podsnímky upravených míst prohlédni. Plný render stejným příkazem jako v1 do
${M}/render/V004_obraz_v${dalsi}.mp4, spoj se zvukem (${M}/zvuk/zvuk_v${dalsi}.wav když existuje, jinak ${zvuk}), master → ${M}/vystup/V004_v${dalsi}.mp4,
kontrola.sh → ${KD}/v${dalsi}. vystup = cesta k V004_v${dalsi}.mp4. Do co_jsem_udelal napiš stručně opravená místa s časy.`,
      { label: `animátor · opravy v${dalsi}`, phase: 'Opravy', agentType: 'animator', schema: ANIM, effort: 'high' }).then((r) => sber(`animátor (v${dalsi})`, r)),
    () => (proZvuk.length ? agent(`${CTX}

## Tvůj úkol: OPRAVY ZVUKU, KOLO ${kolo} → v${dalsi} (zvukař)
Mix ${zvuk}. Nálezy: ${JSON.stringify(proZvuk)}. Časování hudby neměň. Ulož ${M}/zvuk/zvuk_v${dalsi}.wav a zvuk_bez_hudby_v${dalsi}.wav, změř.`,
      { label: `zvukař · opravy v${dalsi}`, phase: 'Opravy', agentType: 'zvukar', schema: ZVUK, effort: 'high' }).then((r) => sber(`zvukař (v${dalsi})`, r)) : Promise.resolve(null)),
  ])
  if (z && z.vystup_zvuk) zvuk = z.vystup_zvuk
  if (o && o.vystup) { video = o.vystup; opravenaMista = (o.co_jsem_udelal || []).join(' | ').slice(0, 1500) }
  kolo++
}

return { schvaleno, kol: historie.length, historie, video, zvuk,
  posledni_kontrola: posledni.map((k) => ({ verdikt: k.verdikt, wow: k.skore_wow, jizda: k.skore_jizda, realismus: k.skore_realismus, energie: k.skore_energie, nalezy: k.nalezy, pravidla: k.pravidla_uzivatele, dobre: k.co_je_dobre })),
  otazky }
