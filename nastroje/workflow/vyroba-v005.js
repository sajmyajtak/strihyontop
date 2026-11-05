export const meta = {
  name: 'v005-vyroba',
  description: 'V005 Porsche (úsporně, ~10 agentů): zvukař (nálada hora + SFX) ∥ animátor (desky, přebarvení, blok A) → KŘ schválí klíčové snímky → animátor (blok B, render, zvuk) → kritik ∥ KŘ, max. 3 kola oprav',
  phases: [
    { title: 'Výroba', detail: 'zvukař ∥ animátor A (desky, přebarvení, blok A 0–13,87) → KŘ klíčové snímky → animátor B (blok B, plný render, spojení se zvukem)' },
    { title: 'Kontrola', detail: 'kritik (technika + zadání + partitura) ∥ kreativní ředitel (wow, střih, realismus, pohoda)' },
    { title: 'Opravy', detail: 'animátor (+ zvukař jen při nálezech ke zvuku, až po obrazu)' },
  ],
}

const P = 'projekty/005-porsche/zadani.md'
const M = 'media/projekty/005-porsche'
const KD = 'media/kontrola/005-porsche'
const CTX = `Projekt V005 Porsche 718 Spyder RS, repozitář /home/user/strihyontop (pracuj relativně k němu). Úkol ti zadává režisér (hlavní agent).
Uživatele se nikdy neptáš. Když si nevíš rady, rozhodni rozumně sám, zapiš to a otázku vrať režisérovi v poli otazky_pro_rezisera. Necommituj.
ZÁVAZNÉ: ${P} (zadání doslova, pravidla 1–8, ROZHODNUTÍ REŽISÉRA včetně „Rozhodnutí režiséra po testu techniky“, Vůz a fakta, Značka, Materiál jízdy,
Režijní list, STŘIHOVÁ PARTITURA + Změny po oponentuře, Rozpis úseků stopáže, Proměny na stopáži, Hudba, Kontrolní snímky, Pasti stavby, Pořadí stavby,
Test techniky), **znalosti/strih-vzor.md** (závazný vzor střihu uživatele), znalosti/pravidla-strihu.md (vkus uživatele; D1–D15, F, G7–G9, I9),
znalosti/chyby.md (C027, C028, C036, C040, C041, C044–C050). Materiály ${M}/materialy/, značka ${M}/znacka/ (znacka.css, Barlow, erb SVG),
test ${M}/test/ (test_technika_v2.html = ověřená scéna: pilulka, vzorky, linka, LUT, MORF, nájezd skrz erb; _skript/test_lut.py, test_maska.py; STAV.md),
vzor nastroje/vzory/scena.html (helpery snimekDesky / casDesky / kresliRozostreni). **Masky vozu počítá režisér na pozadí**: ${M}/desky/<kód>/src/NNNNN.png
(název = index snímku zdroje 25 fps) a ${M}/desky/<kód>/maska/NNNNN.png pro W4 5225–5270, W7 7085–7174, M8 216–246, X1 37–63, W11 9075–9135, W6 6952–7035;
průběh v ${M}/desky_masky.log (pořadí W4 → W7 → M8 → X1 → W11 → W6, ~28 s na snímek). Když maska ještě chybí, dělej mezitím jinou část a vrať se;
masky nepočítej sám (CPU má 4 jádra). Formát 1920×1080, 60 fps, 30,00 s, bez voiceoveru (věty na obrazovce), anglicky.
Kontejner se může restartovat: po každé větší části zapiš stav do ${M}/STAV_VYROBY.md (co je hotové, kde, co zbývá) a při startu ho nejdřív přečti a navaž.
PRACUJ PO ČÁSTECH (C018), věcně. Agentů je málo: svou část udělej celou a ověř ji sám.`

const S = { type: 'array', items: { type: 'string' } }
const ANIM = { type: 'object', properties: { stav: { type: 'string', enum: ['HOTOVO', 'BLOKOVÁNO'] }, vystup: { type: 'string' }, snimky: S,
  co_jsem_udelal: S, zmeny_casu: S, zname_nedostatky: S, chyby: S, otazky_pro_rezisera: S },
  required: ['stav', 'vystup', 'snimky', 'co_jsem_udelal', 'zmeny_casu', 'zname_nedostatky', 'chyby', 'otazky_pro_rezisera'] }
const ZVUK = { type: 'object', properties: { stav: { type: 'string', enum: ['HOTOVO', 'BLOKOVÁNO'] }, vystup_hudba: { type: 'string' }, vystup_zvuk: { type: 'string' },
  vystup_zvuk_bez_hudby: { type: 'string' }, mereni: { type: 'string' }, chyby: S, otazky_pro_rezisera: S },
  required: ['stav', 'vystup_hudba', 'vystup_zvuk', 'vystup_zvuk_bez_hudby', 'mereni', 'chyby', 'otazky_pro_rezisera'] }
const REVIEW = { type: 'object', properties: { schvaleno: { type: 'boolean' }, skore_wow: { type: 'number' }, skore_strih: { type: 'number' },
  skore_realismus: { type: 'number' }, skore_pohoda: { type: 'number' }, prebarveni_A_projde: S, opravy: S, co_nechat: S, otazky_pro_rezisera: S },
  required: ['schvaleno', 'skore_wow', 'skore_strih', 'skore_realismus', 'skore_pohoda', 'prebarveni_A_projde', 'opravy', 'co_nechat', 'otazky_pro_rezisera'] }
const KONTROLA = { type: 'object', properties: {
  verdikt: { type: 'string', enum: ['SCHVÁLENO', 'OPRAVIT', 'BLOKUJÍCÍ'] },
  skore_wow: { type: 'number' }, skore_strih: { type: 'number' }, skore_realismus: { type: 'number' }, skore_pohoda: { type: 'number' },
  nalezy: { type: 'array', items: { type: 'object', properties: {
    zavaznost: { type: 'string', enum: ['blokující', 'závažná', 'drobná'] }, oblast: { type: 'string', enum: ['obraz', 'zvuk', 'střih'] },
    cas: { type: 'string' }, problem: { type: 'string' }, dukaz: { type: 'string' }, oprava: { type: 'string' } },
    required: ['zavaznost', 'oblast', 'cas', 'problem', 'dukaz', 'oprava'] } },
  pravidla_uzivatele: { type: 'array', items: { type: 'object', properties: { pravidlo: { type: 'string' }, splneno: { type: 'boolean' }, dukaz: { type: 'string' } },
    required: ['pravidlo', 'splneno', 'dukaz'] } },
  co_je_dobre: S, otazky_pro_rezisera: S },
  required: ['verdikt', 'skore_wow', 'skore_strih', 'skore_realismus', 'skore_pohoda', 'nalezy', 'pravidla_uzivatele', 'co_je_dobre', 'otazky_pro_rezisera'] }

const otazky = []
const sber = (kdo, r) => { if (r && r.otazky_pro_rezisera) for (const q of r.otazky_pro_rezisera) otazky.push(`${kdo}: ${q}`); return r }

phase('Výroba')
const zvukP = agent(`${CTX}

## Tvůj úkol: HUDBA „HORA“, SFX A MIX v1 (zvukař)
1. **Nová nálada \`hora\` v nastroje/hudba.py** podle oddílu „Hudba“ v ${P}: velmi drahá a klidná („sedíš na velké hoře a koukáš dolů, jak je krajina rozmanitá“),
   72 BPM (nebo volně), dur (F / D), akordy maj9 / m9 / add9 odvozené z \`luxusni\`, **bez bicích a bez dropu**: jediný tón piana na 0,00, plocha od 2,60, swell +2 dB 9,86–10,76,
   nádech −6 dB 13,62, **vrchol 13,87–14,15 (plocha o oktávu výš, melodie piana) → −16 LUFS do 17,60**, kadence do tóniky na 20,78, 20,72–21,02 low-pass na 2 kHz (uvnitř skla), 22,44 zpět,
   decrescendo, fade 27,40–27,65, **ticho 27,65–27,85**, dozvuk pod podpisem 28,0–30,0. Nové parametry (např. \`--vrchol\`) přidej tak, aby **ostatní nálady zůstaly bit po bitu stejné**
   (vyrenderuj všechny staré nálady před a po změně a porovnej hash; C012, I7 pásma). Výstup ${M}/hudba.wav + hudba.json (30,0 s), spektrogram si prohlédni.
2. **SFX** (nastroje/sfx.py) podle sloupce SFX v oddílu Hudba v ${P}, ALE s časy podle „Rozhodnutí režiséra po testu techniky“ (T8 = střih v pohybu na 18,00, žádný průjezd-wipe;
   věta 8 od 20,72). SFX tiché a jen na stavy (~1/s), **jediný hlasitý úder = boom 27,85** (0 až −3 LU v okně 100 ms, hudba ztichlá; I9). Seznam do projekty/005-porsche/sfx_udalosti.json.
   Časy SFX po obrazu ještě posune režisér (C045), proto piš ke každé události, na co v obraze sedí.
3. Mix ${M}/zvuk/zvuk_v1.wav a zvuk_bez_hudby_v1.wav (C039: staré odvozené soubory smazat), kontrolní master −14 LUFS / ≤ −1 dBTP po AAC, pásma, RMS po 0,5 s (stavba k vrcholu,
   boom nejhlasitější místo). Zapiš „Zvuk v1“ do ${P} (nálada, parametry, měření).`,
  { label: 'zvukař · nálada hora, SFX, mix', phase: 'Výroba', agentType: 'zvukar', schema: ZVUK, effort: 'high' }).then((r) => sber('zvukař', r))

const a1 = sber('animátor A', await agent(`${CTX}

## Tvůj úkol: DESKY, PŘEBARVENÍ A BLOK A 0–13,87 (animátor)
1. **Nástroj přebarvení**: z test/_skript/test_lut.py udělej čistý ověřený \`nastroje/prebarvi.py\` (LUT z pixelově zarovnaných rendrů 1H → cíl v Lab, v masce karoserie z ${M}/desky/<kód>/maska,
   výluky SPZ / světel / skla / pneu / černých dílů, peří = délka pohybového rozmazání, časový medián 3 snímky, parametry CHROMA_S / LMAX / UZAVRENI / PERI_HRANY jako v testu). Krátká nápověda v hlavičce.
2. **Desky stopáže** podle „Rozpisu úseků“ (s rozhodnutím režiséra: W11 do 365,40, W6 od 278,08): 1,2× (kadence 2:2), jednotný grade (Past 4), 30fps sekvence v ${M}/desky/<kód>/;
   přebarvené varianty podle tabulky stavů (W4 Guards Red od 209,57; W7 Guards Red → Black · Shark Blue · Ruby Star Neo · GT Silver → Gentian Blue; M8 Gentian Blue + ráfek Satin Neodyme;
   F1 fotka 3 vrstvy, karoserie modrá, kolo bronz, karmín → Arctic). Pro X1, W11, W6 připrav totéž, až budou masky (blok B to použije).
   **Kritéria realismu (podmínka režiséra)**: W4, W7, M8, X1 musí projít stejně jako test (žádný lem, žádné blikání > 2 % mimo rozmaz, odlesky drží, SPZ / světla / sklo / pneu beze změny,
   ΔE proti rendru < 12). Když záběr neprojde, pro něj **cesta B** (rendry konfigurátoru, oddíl Proměny B) a napiš to do zmeny_casu / zname_nedostatky.
3. **Scéna** ${M}/scena/ (kostra nastroje/vzory/scena.html + ověřené části z test_technika_v2.html; moduly A_ / B_, C036): semínko, pilulka (kotva), věty po slovech z rozostření, vzorky, linky,
   EXPL, CLONA, LET, WIPE, F1 2,5D, vše přesně podle partitury (časy, typy, kaskády). Změř skutečnou šířku textů v Barlow a zapiš levou hranu pilulky (Past 8).
4. **Kontrolní snímky bloku A** (\`render_html.cjs --nahled casy\`) ve všech časech z tabulky Kontrolní snímky do 13,87 + výřez 1 s nejtěžšího úseku s podsnímky (změř čas výpočtu).
   Ulož do ${KD}/blokA/, opravdu je prohlédni (Read) a oprav, co nesedí, než odevzdáš. Plný render zatím NE.
5. Do ${P} oddíl „Výroba: blok A“ (co, kde, měření, odchylky od partitury a proč). Změny časů proti partituře vypiš v poli zmeny_casu (C045).`,
  { label: 'animátor A · desky, přebarvení, blok A', phase: 'Výroba', agentType: 'animator', schema: ANIM, effort: 'high' }))
if (!a1 || a1.stav === 'BLOKOVÁNO') { const z = await zvukP; return { animator_a: a1, zvuk: z, otazky } }

const kr0 = sber('kreativní ředitel (blok A)', await agent(`${CTX}

## Tvůj úkol: SCHVÁLENÍ KLÍČOVÝCH SNÍMKŮ BLOKU A (kreativní ředitel)
Kontrolní snímky bloku A jsou v ${KD}/blokA/ (hlášení animátora: ${JSON.stringify(a1.snimky).slice(0, 1500)}), scéna ${M}/scena/. Posuď **přísně na 100 % výřezech**:
(1) realismus přebarvení jedoucího vozu (W4 Guards Red, W7 scroll 4 laků + pomalá Gentian Blue, M8 ráfek Satin Neodyme, F1 interiér): nepozná se zásah? lem, blikání, odlesky, SPZ, sklo, pneu;
pro každý záběr napiš do prebarveni_A_projde „W4: ano/ne – důvod“ atd.; (2) střih podle strih-vzor.md (1 hrdina + pilulka, proměny, kaskády, věty z rozostření, obraz předbíhá větu,
kotva, nic přes lak); (3) pohoda a luxus (žádná závodní energie, výhled, ticho mezi větami); (4) wow. Skóre 1–10: wow, střih, realismus, pohoda.
Schváleno = střih ≥ 8, realismus ≥ 8 a žádná vada, která se při stavbě bloku B nedá opravit. Opravy piš konkrétně (čas, co, jak).`,
  { label: 'kreativní ředitel · klíčové snímky bloku A', phase: 'Výroba', agentType: 'kreativni-reditel', schema: REVIEW, effort: 'high' }))

const zvuk = await zvukP
const a2 = sber('animátor B', await agent(`${CTX}

## Tvůj úkol: OPRAVY BLOKU A + BLOK B 13,87–30 + PLNÝ RENDER + ZVUK (animátor)
Navazuješ na scénu ${M}/scena/ (hlášení animátora A: ${JSON.stringify({ co: a1.co_jsem_udelal, zmeny: a1.zmeny_casu, nedostatky: a1.zname_nedostatky }).slice(0, 2500)}).
1. **Opravy bloku A** od kreativního ředitele (číslované, závazné, C043): ${JSON.stringify(kr0 ? kr0.opravy : []).slice(0, 3000)}
   Ponechat beze změny: ${JSON.stringify(kr0 ? kr0.co_nechat : []).slice(0, 1000)}. Verdikt přebarvení po záběrech: ${JSON.stringify(kr0 ? kr0.prebarveni_A_projde : []).slice(0, 800)}
   (záběr s „ne“ → cesta B pro ten záběr).
2. **Blok B** podle partitury a rozhodnutí režiséra: dron X1 + nádech + věta 6 + karta 500 PS (ODOMETR přes střih 16,00, G9, C046, C047), W11 (přebarvení, do 365,40) → **T8 střih v pohybu 18,00** →
   W6 (přebarvení, návrat linkou zprava 19,98–20,78, pak 1:1 originál), **MORF rámce se sklem** (věta 8 od 20,72) + průjezd za sklem, logo: název, TAH erbu (SVG porsche.cz), claim, WLTP, ticho,
   záblesk, podpis tvůrce „strihyontop“ + disclaimer „Concept ad · not affiliated with Porsche · Footage and renders © Porsche AG“. Masky X1 / W11 / W6 z ${M}/desky (počkej na ně, viz log).
3. **Plný render** ${M}/render/V005_obraz_v1.mp4 (\`--sub 4 --sub-rychle 16\` v úsecích MORF / ZOOM / LET / EXPL / CLONA / WIPE / záblesk), \`nastroje/kontrola.sh\` do ${KD}/v1-animator/, prohlédni arch a pásy.
4. **Spojení se zvukem**: zvuk ${zvuk ? zvuk.vystup_zvuk : M + '/zvuk/zvuk_v1.wav'} → \`nastroje/master_zvuk.sh\` → ${M}/vystup/V005_v1.mp4; verze bez hudby z ${zvuk ? zvuk.vystup_zvuk_bez_hudby : M + '/zvuk/zvuk_bez_hudby_v1.wav'}
   → ${M}/vystup/V005_v1_bez_hudby.mp4 (C039: jen z těchto WAV). Plakát ${M}/vystup/V005_v1_plakat.jpg (nejsilnější snímek s naším vozem v jízdě).
5. Do ${P} oddíl „Výroba: blok B a render v1“; **všechny změny časů proti partituře vypiš v poli zmeny_casu** (zvuk se posune podle nich, C045).`,
  { label: 'animátor B · blok B, render, zvuk', phase: 'Výroba', agentType: 'animator', schema: ANIM, effort: 'high' }))
if (!a2 || a2.stav === 'BLOKOVÁNO') return { animator_a: a1, kr_blokA: kr0, zvuk, animator_b: a2, otazky }

const kola = []
let verze = 1, posledni = a2, oprZvuk = null
for (let kolo = 1; kolo <= 3; kolo++) {
  phase('Kontrola')
  const video = `${M}/vystup/V005_v${verze}.mp4`
  const jenOpravene = kolo === 1 ? '' : `Toto je kolo ${kolo}: kontroluj hlavně místa opravená od minulého kola (hlášení animátora: ${JSON.stringify(posledni.co_jsem_udelal).slice(0, 2000)}) a regresi rozdílem snímků proti V005_v${verze - 1}.mp4.`
  const [kr, kd] = await parallel([
    () => agent(`${CTX}

## Tvůj úkol: NEZÁVISLÁ KONTROLA (kritik), kolo ${kolo}
Video ${video} (+ ${M}/vystup/V005_v${verze}_bez_hudby.mp4). Nevěř autorovi, posuzuj jen výstup. ${jenOpravene}
Skóre wow / střih / realismus / pohoda dej 0 (hodnotí kreativní ředitel). Projdi: technika (\`nastroje/kontrola.sh\` do ${KD}/kolo${kolo}-kritik/, 1920×1080 60 fps 30,00 s, −14 LUFS ±1, TP ≤ −1 dBTP),
**pravidla uživatele 1–8 jednotlivě**, akceptační kritéria z Režijního listu, **partitura po snímcích** (strih-vzor.md 6: 1 hrdina + pilulka, 0 střihů v grafice, střihy ve stopáži jen T1–T8 s přežívající
pilulkou, příchody z rozostření / odchody kratší, klid, věta předbíhá, kaskády, jedno číslo 500 PS ≥ 1 s klidu, ding na ustálený snímek, semínko → erb, podpis tvůrce 2 s), **stav vozu v každém záběru**
podle tabulky stavů (barva, kola, interiér; po 13,47 žádný čitelný karmín; po 20,78 rozdíl proti originálu stopáže 0 mimo UI), **realismus přebarvení na 100 % výřezech** (lem, blikání, odlesky, SPZ, sklo, pneu),
**pilulka nikdy na laku** (pás po 0,25 s), zakázané úseky stopáže (C044), kadence 2:2, C050 (žádný prolnutý snímek na střihu stopáže), texty bez překlepů, fakta doslova, disclaimer a WLTP doslova, zvuk proti obrazu
(SFX na stavy, boom 27,85 nejhlasitější, ticho 27,65–27,85). SCHVÁLENO = žádný blokující ani závažný nález.`,
      { label: `kolo ${kolo} · kritik`, phase: 'Kontrola', agentType: 'kritik', schema: KONTROLA, effort: 'high' }),
    () => agent(`${CTX}

## Tvůj úkol: HODNOCENÍ (kreativní ředitel), kolo ${kolo}
Video ${video}. ${jenOpravene} Hodnoť 1–10: **wow**, **střih podle vzoru uživatele** (strih-vzor.md: jeden hrdina, proměny, kotva, kaskády, věty, podpis tvůrce), **realismus**
(vůz jede, přebarvení se nepozná, nic kresleného), **pohoda a luxus** (výhled, ticho mezi větami, drahá značka, žádná závodní energie). Pusť si celé video (arch po 0,25 s) a projdi klíčové momenty
po snímcích. Je tam něco, co by uživatel nazval „není to ono“? Nálezy s konkrétní opravou (čas, co, jak), nutné odliš od drobných. SCHVÁLENO = wow ≥ 8, střih ≥ 8, realismus ≥ 8 a žádný blokující nález.`,
      { label: `kolo ${kolo} · kreativní ředitel`, phase: 'Kontrola', agentType: 'kreativni-reditel', schema: KONTROLA, effort: 'high' }),
  ])
  sber(`kritik ${kolo}`, kr); sber(`KŘ ${kolo}`, kd)
  kola.push({ kolo, verze, kritik: kr, kreativni_reditel: kd })
  const vazne = [...((kr && kr.nalezy) || []), ...((kd && kd.nalezy) || [])].filter((n) => n.zavaznost !== 'drobná')
  const ok = kr && kd && kr.verdikt === 'SCHVÁLENO' && kd.skore_wow >= 8 && kd.skore_strih >= 8 && kd.skore_realismus >= 8 && !vazne.length
  log(`Kolo ${kolo}: kritik ${kr ? kr.verdikt : '?'} · KŘ wow ${kd ? kd.skore_wow : '?'} / střih ${kd ? kd.skore_strih : '?'} / realismus ${kd ? kd.skore_realismus : '?'} / pohoda ${kd ? kd.skore_pohoda : '?'}`)
  if (ok || kolo === 3) break

  phase('Opravy')
  const nalezy = [...((kr && kr.nalezy) || []).map((n) => ({ ...n, od: 'kritik' })), ...((kd && kd.nalezy) || []).map((n) => ({ ...n, od: 'KŘ' }))]
  const obraz = nalezy.filter((n) => n.oblast !== 'zvuk'), zvukN = nalezy.filter((n) => n.oblast === 'zvuk')
  verze += 1
  posledni = sber(`animátor opravy ${kolo}`, await agent(`${CTX}

## Tvůj úkol: OPRAVY PO KOLE ${kolo} (animátor) → V005_v${verze}
Nálezy (číslované, závazné; drobné oprav, když to nic nerozbije): ${JSON.stringify(obraz).slice(0, 9000)}
Ponechat beze změny (co je dobře): ${JSON.stringify([...((kr && kr.co_je_dobre) || []), ...((kd && kd.co_je_dobre) || [])]).slice(0, 1500)}
Oprav ve scéně ${M}/scena/, ověř kontrolními snímky na opravených místech (100 % výřez), plný render ${M}/render/V005_obraz_v${verze}.mp4, kontrola.sh do ${KD}/v${verze}-animator/,
spoj se stejným zvukem jako minule (nebo novějším, pokud ho zvukař mezitím dodal: ${M}/zvuk/zvuk_v${verze}.wav) přes master_zvuk.sh → ${M}/vystup/V005_v${verze}.mp4 + _bez_hudby.
Všechny změny časů vypiš v poli zmeny_casu (C045). Zapiš „Opravy v${verze}“ do ${P}.`,
    { label: `animátor · opravy v${verze}`, phase: 'Opravy', agentType: 'animator', schema: ANIM, effort: 'high' }))
  if (!posledni || posledni.stav === 'BLOKOVÁNO') break
  if (zvukN.length || (posledni.zmeny_casu && posledni.zmeny_casu.length)) {
    oprZvuk = sber(`zvukař opravy ${kolo}`, await agent(`${CTX}

## Tvůj úkol: ZVUK PODLE OPRAVENÉHO OBRAZU (zvukař) → zvuk_v${verze}
Obraz je hotový (${M}/render/V005_obraz_v${verze}.mp4). Změny časů od animátora: ${JSON.stringify(posledni.zmeny_casu).slice(0, 3000)}
Nálezy ke zvuku: ${JSON.stringify(zvukN).slice(0, 3000)}
Posuň SFX na skutečné časy obrazu (projdi snímky kolem každé události), oprav nálezy, mix ${M}/zvuk/zvuk_v${verze}.wav + zvuk_bez_hudby_v${verze}.wav (C039), pak sám spoj
s obrazem přes master_zvuk.sh → přepiš ${M}/vystup/V005_v${verze}.mp4 a _bez_hudby (−14 LUFS / ≤ −1 dBTP po AAC). Zapiš „Zvuk v${verze}“ do ${P}.`,
      { label: `zvukař · zvuk v${verze}`, phase: 'Opravy', agentType: 'zvukar', schema: ZVUK, effort: 'high' }))
  }
}
return { animator_a: a1, kr_blokA: kr0, zvuk, animator_b: a2, kola, posledni, oprZvuk, verze, otazky }
