export const meta = {
  name: 'v002-priprava',
  description: 'V002 Mercedes: značka (logo Wikimedia, předběžná paleta) ∥ sportovní hudba → koncept a storyboard (4 motiony) → oponentura na energii → revize',
  phases: [
    { title: 'Podklady', detail: 'analytik: logo a předběžná paleta ∥ zvukař: nálada sportovni 128 BPM / 30 s' },
    { title: 'Koncept', detail: 'kreativní ředitel: koncept + storyboard po taktech' },
    { title: 'Oponentura', detail: 'druhý kreativní ředitel: energie a wow, konkrétní opravy' },
    { title: 'Revize', detail: 'zapracování oponentury do storyboardu' },
  ],
}

const P = 'projekty/002-mercedes-racing/zadani.md'
const M = 'media/projekty/002-mercedes-racing'
const CTX = `Projekt V002 Mercedes-Benz závodní spot, repozitář /home/user/strihyontop (pracuj relativně k němu). Úkol ti zadává režisér (hlavní agent).
Uživatele se nikdy neptáš. Když si nevíš rady, rozhodni rozumně sám, zapiš to a otázku vrať režisérovi v poli otazky_pro_rezisera. Necommituj.
ZÁVAZNÉ: ${P} (zadání uživatele doslova, jeho pravidla, rozhodnutí režiséra, pevná struktura hudby, 4 zvolené motiony, akceptační kritéria),
znalosti/pravidla-strihu.md (nahoře VKUS UŽIVATELE: víc energie, rychlejší, živější, víc efektů; o V001 řekl „není to ono, bez duše“),
znalosti/chyby.md, znalosti/prompt-motion/poznatky.md. Plné texty promptů z prompt-motion jsou v media/prompt-motion/polozky.json (podle slugu)
a šablona showreel v media/prompt-motion/stranky/templates__showreel.md.
Weby Mercedes-Benz (mercedes-benz.cz, .com, group, amg) vracejí automatickým požadavkům 403. NEPOKOUŠEJ SE je načíst ani obcházet, nepoužívej je.
Formát 16:9 1920×1080, 60 fps, 30,0 s, hudba 128 BPM (doba 0,46875 s, takt 1,875 s), drop 1 = 3,75 s, zlom 15,0 s, drop 2 = 18,75 s, end card 26,25–30 s.
PRACUJ PO ČÁSTECH (C018): žádný obří výstup najednou, velké soubory po částech (kostra + menší Edit), přemýšlej věcně a rozhodnutí rovnou zapisuj.`

const S = { type: 'array', items: { type: 'string' } }
const otazky = []
const sber = (kdo, r) => { if (r && r.otazky_pro_rezisera) for (const q of r.otazky_pro_rezisera) otazky.push(`${kdo}: ${q}`); return r }

phase('Podklady')
const [zn, hu] = await parallel([
  () => agent(`${CTX}

## Tvůj úkol: ZNAČKA MERCEDES-BENZ (analytik), bez přístupu na jejich web
1. Logo: stáhni SVG hvězdy z Wikimedia Commons (https://upload.wikimedia.org/wikipedia/commons/9/90/Mercedes-Logo.svg) do ${M}/znacka/,
   zjednoduš ho na čistou, lehkou verzi pro scénu (stejný tvar, jen méně uzlů), vyrenderuj obě do PNG a PROHLÉDNI (Read), že tvar sedí.
   Zapiš zdroj a licenci ze stránky souboru na Commons (https://commons.wikimedia.org/wiki/File:Mercedes-Logo.svg).
2. **Předběžná paleta** (ověření z webu čeká na screenshot od uživatele): digitální paleta Mercedes-Benz černá #000000, bílá #FFFFFF,
   stříbrné / šedé tóny a modrý akcent webu #0078D6. Navrhni role (pozadí, text, akcent, světla) a závodní doplněk v rámci značky.
   Vše jako CSS proměnné, ať jdou později vyměnit. Výslovně označ „předběžné, neověřeno z webu“.
3. Font: Mercedes používá proprietární MB Corpo. Navrhni nejbližší náhrady z Google Fonts (nadpisy a text, latin-ext) a zdůvodni je.
4. Texty: z webu je nemáme, proto jen „Mercedes-Benz“, obecné závodní výrazy a krátké vlastní claimy reklamy. Žádná fakta, čísla, jména
   jezdců, týmy ani sponzoři (C8). Navrhni 5–8 krátkých anglických hesel.
5. Souhrn zapiš do ${P}: tabulka Materiály + odrážka „Vzhled“ v Režijním listu (barvy HEX s rolemi a poznámkou „předběžné“, font, logo).`,
    { label: 'analytik · značka (logo, předběžná paleta)', phase: 'Podklady', agentType: 'analytik', effort: 'high', schema: {
      type: 'object', properties: { stav: { type: 'string', enum: ['HOTOVO', 'BLOKOVÁNO'] }, barvy: S, font: { type: 'string' }, logo: S,
        hesla: S, poznamky: S, otazky_pro_rezisera: S },
      required: ['stav', 'barvy', 'font', 'logo', 'hesla', 'poznamky', 'otazky_pro_rezisera'] } },
  ).then((r) => sber('analytik', r)),
  () => agent(`${CTX}

## Tvůj úkol: SPORTOVNÍ HUDBA (zvukař)
Přidej do nastroje/hudba.py náladu **sportovni** (racing / driving electro): 128 BPM, mollová, tvrdý kopák four-on-the-floor, clap / snare na 2 a 4,
distorzovaná pulzující basa (osminy), arpeggio syntezátoru, risery a reverse před dropy, údery (impact) na drop 1 (3,75 s) a drop 2 (18,75 s),
zlom 15,0–16,875 s (jen pad + filtr + motor), stoupání 16,875–18,75 s, finální úder 26,25 s a doznění do 30,0 s. Zvukový motiv „motor“:
syntetický stoupající tón řazení / průjezdu (glissando s harmonickými), na zlomu a před dropy. Energie, ať to „táhne“.
Struktura je pevná (viz zadání). Když hudba.py potřebuje nový parametr pro zlom, přidej ho čistě. ZÁKLAD pro kontrolu ostatních nálad je commit
217b355 (git show 217b355:nastroje/hudba.py): vazna, drza, luxusni, pohodova musí zůstat bit po bitu stejné (hash).
Vyrenderuj: python3 -I nastroje/hudba.py --nalada sportovni --delka 30 --drop 3.75 --konec 26.25 --out ${M}/hudba.wav (+ hudba.json s udalosti_nastroju).
Bez varování pásem a oktáv (I7). Prohlédni spektrogram. Změř a vrať BPM, časy dropů, zlomu a konce, LUFS, pásma, oktávy.`,
    { label: 'zvukař · nálada sportovni', phase: 'Podklady', agentType: 'zvukar', effort: 'high', schema: {
      type: 'object', properties: { stav: { type: 'string', enum: ['HOTOVO', 'BLOKOVÁNO'] }, vystup: { type: 'string' }, mereni: { type: 'string' },
        co_jsem_udelal: S, chyby: S, otazky_pro_rezisera: S },
      required: ['stav', 'vystup', 'mereni', 'co_jsem_udelal', 'chyby', 'otazky_pro_rezisera'] } },
  ).then((r) => sber('zvukař', r)),
])
log(`Podklady: značka ${zn ? zn.stav : 'nic'}, hudba ${hu ? hu.stav : 'nic'}`)
if (!zn || zn.stav !== 'HOTOVO') return { chyba: 'značka nedodána', znacka: zn, hudba: hu, otazky }

const KONCEPT_SCHEMA = { type: 'object', properties: {
  koncept_veta: { type: 'string' }, motiony: S, efekty: S, wow_momenty: S, rizika: S, otazky_pro_rezisera: S },
  required: ['koncept_veta', 'motiony', 'efekty', 'wow_momenty', 'rizika', 'otazky_pro_rezisera'] }

phase('Koncept')
const ko = sber('kreativní ředitel (koncept)', await agent(`${CTX}

## Tvůj úkol: KONCEPT A STORYBOARD
Podklady: značka v ${M}/znacka/ a v ${P} (Materiály, Vzhled; paleta je předběžná, používej CSS proměnné), hudba ${M}/hudba.wav + hudba.json.
Navrhni **energický** 30s závodní spot pro Mercedes-Benz (spec reklama). Laťka: uživatel chce, ať si řekne „wow“, ať to má duši a energii.
- Jedna silná myšlenka a spojovací prvek přes celé video (např. hvězda, závodní linie, světla), závodění musí být jasné od 1. sekundy.
- Použij **všechny 4 zvolené motiony** (šablona showreel, Taxtello, UGC promo, Food craving) a u každého napiš, kde a jak je ve videu (časy).
- Energie (C7, D2, G2, G6): událost na **každou dobu**, nová scéna každé 1–2 takty, aspoň 6 různých efektů synchronních s hudbou (rychlostní čáry,
  světelné stopy, záblesk a otřes kamery na úderu, švih s rozmazáním, zoom skrz objekt, zaplavení barvou, glitch akcent…). Drop 1 a drop 2 =
  nejsilnější momenty, zlom = krátký kontrast. Hrdina velký (A8), text v bezpečné zóně 16:9 (A5), texty jen obecné nebo z hesel analytika (C8).
- Vozy, trať a svět stav v kódu (SVG / canvas / CSS 3D), stylizovaně, prémiově, žádné fotky. Musí to jít vyrenderovat na 4 CPU bez GPU.
- Přechody textu vždy přísně po sobě, nikdy dvě vrstvy textu v jednom snímku (poučení V001).
Zapiš do ${P}: odrážku „Koncept jednou větou“ v Režijním listu a celý oddíl „Storyboard / časová osa“: tabulka všech 16 taktů
(| čas (takt · doba) | obraz | text | efekt | zvuk / událost (SFX s vrcholem na čase) |), seznam efektů, kontrolní snímky s kritérii odmítnutí,
pasti stavby a pořadí stavby (nejdřív klíčové snímky drop 1 a drop 2).`,
  { label: 'kreativní ředitel · koncept + storyboard', phase: 'Koncept', agentType: 'kreativni-reditel', effort: 'high', schema: KONCEPT_SCHEMA }))
if (!ko) return { chyba: 'koncept nedodán', znacka: zn, hudba: hu, otazky }

phase('Oponentura')
const op = sber('oponent', await agent(`${CTX}

## Tvůj úkol: OPONENTURA KONCEPTU (nezávislý kreativní ředitel)
Přečti koncept a storyboard v ${P} (Režijní list + Storyboard) a podklady značky. Ohodnoť ho přísně podle své role (energie 3×).
Hlavní otázky: bude to mít energii a „duši“, ne jako V001? Je závodění a Mercedes poznat v 1. sekundě? Jsou drop 1 a drop 2 opravdu wow?
Jsou všechny 4 motiony poznat? Nejsou někde mrtvé pasáže? Dá se to postavit prémiově (ne jako klipart) na CPU?
Vrať skóre a KONKRÉTNÍ opravy (takt, čas, co přesně) seřazené podle dopadu. Nic neměň.`,
  { label: 'oponent · energie a wow', phase: 'Oponentura', agentType: 'kreativni-reditel', effort: 'high', schema: {
    type: 'object', properties: { skore_energie: { type: 'number' }, skore_celkem: { type: 'number' }, opravy: S, co_nechat: S, otazky_pro_rezisera: S },
    required: ['skore_energie', 'skore_celkem', 'opravy', 'co_nechat', 'otazky_pro_rezisera'] } }))

phase('Revize')
const rev = op ? sber('revize', await agent(`${CTX}

## Tvůj úkol: REVIZE STORYBOARDU PODLE OPONENTURY
Oponent dal konceptu energii ${op.skore_energie}/10, celkem ${op.skore_celkem}/10.
Opravy: ${JSON.stringify(op.opravy)}
Nech beze změny: ${JSON.stringify(op.co_nechat)}
Zapracuj opravy přímo do ${P} (Režijní list a Storyboard), ať je cíl energie i celkem 9+. Na konec oddílu Storyboard připiš krátký seznam
„Změny po oponentuře“. Pevné časy hudby neměň.`,
  { label: 'kreativní ředitel · revize', phase: 'Revize', agentType: 'kreativni-reditel', effort: 'high', schema: {
    type: 'object', properties: { zmeny: S, otazky_pro_rezisera: S }, required: ['zmeny', 'otazky_pro_rezisera'] } })) : null

return { znacka: zn, hudba: hu, koncept: ko, oponentura: op, revize: rev, otazky }
