# Střihový vzor: jak uživatel chce, aby jeho videa byla stříhaná

Vzniklo 2026-11-04 po zpětné vazbě k V004 („není to špatný, ale zaměř se víc na ten střih a editaci… adaptuj se na tyhle střihy“)
a po rozboru tří předloh, které uživatel poslal jako vzor svých videí a jejich prezentace: **R6** (Packeta Z-BOX, @davidxsipos),
**R7** (After Effects vs. Gemini, @shhradddhaa.ai), **R4** (easing, @ugoki.ai, poslal podruhé). Platí k tomu i **R1** (Waze).
Podrobné partitury jsou v `reference/R4…`, `R6…`, `R7…`. Tenhle dokument je **závazný pro všechny agenty** (čte se na začátku každé session
a před každým konceptem, storyboardem, stavbou i kontrolou). Při rozporu s `pravidla-strihu.md` platí tento dokument (je novější a je to vkus uživatele).

## 0. Co uživatel myslí „střihem a editací“
Ne víc střihů, ale **kvalitu přechodů a vedení pozornosti**. V004 dělalo energii kvantitou (25 tvrdých střihů za 30 s, 4 karty faktů za 8 s,
mřížka 3×3, 3–5 prvků naráz, efekty na doby). Všechny jeho předlohy mají **0 tvrdých střihů**, na obrazovce **jednu věc**, a každá změna
má **příčinu** (slovo hlasu, nebo předchozí prvek, který se v tu další proměňuje). Energie vzniká z **pohybu a proměn**, ne z množství.

## 1. Deset zásad střihu (co musí každé video splnit)
1. **Jeden hrdina + nejvýš jeden doplněk.** Na obrazovce je v každém okamžiku jeden hlavní objekt (logo, telefon, mapa, produkt, karta) a nejvýš
   jedna doplňková věc (číslo, notifikace, popisek). Nikdy mřížka, koláž ani „všechno najednou“. `[R6: 36 prvků, nikdy víc než 2 naráz; R7: 1 řádek textu]`
2. **Stavy místo záběrů.** Hrdina drží **2–5 s** a prochází stavy (telefon: pole → výsledky → karty → souhrn → potvrzení = 5 s, 5 stavů).
   Změna stavu každých **~0,6 s**. Divák neztratí orientaci, protože objekt zůstává. `[R6]`
3. **Žádný tvrdý střih bez důvodu.** Scény spojují **proměny**: další prvek vzniká z předchozího (tah → logo → pole → rámeček → logo).
   Tvrdý střih jen u skutečné stopáže (jízda vozu) a i tam přes střih přežívá spojovací prvek (bod, linka). `[R1, R4, R6, R7: všechny 0 střihů]`
4. **Spojovací hmota značky („semínko“).** Jeden tvar v barvě značky (tah, tečka, kruh, plocha) je v obraze **od snímku 0**, kreslí z něj logo,
   vrací se během videa (kreslí UI, rámeček klíčového slova, explozí dělá pozadí) a na konci se **přemorfuje zpět do loga**. Nikdy nezmizí, jen se mění. `[R6, R7]`
5. **Příchod z rozostření, odchod do rozostření.** Výchozí příchod textu, karty, loga = z Gaussova rozostření do ostrosti **0,1–0,25 s**;
   odchod do rozostření + zblednutí **0,05–0,2 s**. Směrové rozmazání u letů, odometrické u číslic. Ostré naskočení maskou jen s důvodem.
   **Odchod je vždy kratší než příchod** a nejlépe proměnou (natáhne se do pilulky, smrští do tečky, zešedne), ne prolínačkou. `[R6: nic nenaskočí ostře; R7: odchody 1–3 snímky]`
6. **Klid jen na přečtení.** Slovo 0,2–0,33 s, řádek 0,4 s + 0,1–0,2 s, karta 0,5–1,2 s, hrdina 2–5 s. Nic nestojí déle, než je potřeba to přečíst.
   Výjimka: **číslo stojí ≥ 0,5 s** (G9) a jedno video má **jedno skutečné číslo** (R6: 2 912, rolování zdola 0,7 s, klid 1 s). `[R6, R7]`
7. **Hlas (nebo věta) řídí střih, obraz předbíhá slovo.** Každá scéna má jednu větu (3–7 slov). Prvek naskočí **0,1–0,35 s před** slovem, které ho
   pojmenuje; nikdy po něm. Pauzy hlasu vyplňuje souvislý pohyb (let kamery), ne klid. Bez voiceoveru platí totéž pro **větu na obrazovce**
   (claim / titulek: slova naskakují z rozostření v rytmu řeči). `[R6: Z-BOX −0,1 s, notifikace −0,35 s, logo −0,3 s; R4]`
8. **Přechody mezi světy: každý jiný, žádný dvakrát.** Zásobník: let (prvek odjede nahoru, další přijede zdola), wipe pruhy v barvách značky
   (0,35 s plné barvy = nádech, konec wipe = konec věty), zoom skrz objekt + rozostření (mapa → špendlík → Z-BOX), exploze tečky do plochy (1 snímek),
   kruhová clona ze středu (nový prvek roste ze středu), inverze barvy plochy mezi kartami, morf rámečku do loga, záblesk + boom před end card. `[R6, R7]`
9. **Zvuk až podle hotového obrazu.** Rytmus určuje animace (proměny), ne metronom. SFX tiché, jen na stavové změny (~1 za sekundu), hudba
   u videí s hlasem **≤ −25 LUFS nebo žádná**; jediný hlasitý úder (boom + záblesk) až na podpis tvůrce. U videí bez hlasu smí hudba vést,
   ale střih se nestaví „na doby“, nýbrž na proměny, a hudba se k nim doladí. `[R6: pauzy −25 až −42 LUFS; R7: 19 z 34 událostí mimo mřížku BPM]`
10. **Prezentace = natočená obrazovka nebo mockup, konec = podpis tvůrce.** Animace 16:9 / 16:10 se ukazuje na notebooku natočeném telefonem
    na výšku (R6) nebo v mockupu s panelem, štítkem a CTA v obraze (R7). Po logu klienta: logo do rozostření → 0,2 s ticho → boom + bílý záblesk →
    **end card tvůrce 2 s** + disclaimer v obraze („Spec ad · not affiliated with …“). `[R6, R7, R1]`

## 2. Střihová partitura (povinná součást storyboardu)
Storyboard se píše jako **stavy hrdiny**, ne jako seznam záběrů. Ke každému prvku tabulka (časy na 2 desetinná místa):

| # | prvek | příchod | typ příchodu | klid (s) | odchod | typ odchodu | co ho spojuje s dalším | slovo / věta hlasu |
|---|---|---|---|---|---|---|---|---|

Typy: TAH (tvar nakreslí tah), PIS (psaní maskou s měkkou hranou), ROZ-IN / ROZ-OUT (rozostření), LET (průlet se směrovým rozmazáním),
WIPE (pruhy), ZOOM (nájezd kamery, ease-out ≥ 0,2 s), MORF (tvar → jiný tvar), EXPL (tečka → plocha), CLONA (kruh ze středu), INV (inverze plochy), ZÁBLESK.
**Prvek bez spojky s předchozím nebo následujícím do videa nepatří.** Kritik partituru kontroluje proti hotovému videu po snímcích.

Orientační čísla (R6 / R7): scéna 3,2 s / 0,9 s · událost každých 0,62 s / 0,2 s · nejdelší klid 1,65 s / 0,45 s · příchod 0,1–0,25 s · odchod 0,05–0,2 s ·
rolování čísla 0,7 s · nájezd kamery 0,2–0,85 s · wipe 0,9 s (z toho 0,35 s plné barvy) · end card tvůrce 2,0 s.

## 3. Kamera a prezentace
- **Natočená obrazovka (R6, R1)**: animace běží v okně na notebooku (Dock a menu bar vidět = „opravdu to hraje“), telefon z ruky na výšku.
  Snímek 0 = ruka na klávese (právě spustila), první obsah do 0,6 s. Kamera: 0–2,5 s natočení, 0–7 s nájezd ~+30 %, dál **dýchání ±8 %** s periodou ~8 s,
  nikdy zamrzlý snímek (ani na end card). Místnost **plynule zhasne během 3.–5. s** (jas stěny 67 → 11), barevný wipe obarví místnost.
  Displej 68–89 % šířky snímku. Řeší 16:9 ↔ 9:16 bez přeskládání.
- **Mockup (R7)**: šedé pozadí s měkkými stíny listů, panel 16:9 se stínem (85 % šířky), štítek nad panelem, CTA pod ním (2 řádky, klíčové slovo tučně
  a podtržené). Dvojice panelů (originál / replika, před / po, reference / naše verze) drží pozornost a sbírá komentáře (R7: 3 600 komentářů, poměr k lajkům 0,88).
- **Kamera uvnitř animace**: jen ease-out nájezdy s důvodem (na telefon, na dvířka), žádné tvrdé punch-iny; hloubku dělají prvky (3D telefon, zoom karty z 3×).
- Dokud uživatel netočí sám, natočenou obrazovku **digitálně nasimulovat** s těmito parametry (H4): maketa notebooku, perspektiva, odraz displeje na klávesnici
  a stěně, dýchání kamery, zhasnutí místnosti.

## 4. Typografie a čísla
- Jedno písmo, 2 řezy, na obrazovce **nikdy víc než 1 řádek** textu naráz (kromě end card). Velikosti z R6: číslo 21 % výšky displeje, claim 16 %, logo 12 %.
- Claim bez hlasu: **slova naskakují z rozostření** (ne po písmenech kurzorem); názvy a tvrzení v barvě značky smí **po znacích s pádem na linku**
  (0,4 s na řádek). Klíčové slovo zvýraznit **rámečkem, který nakreslí tah** (podtržení → hrana → uzavření ~0,35 s), nikdy obdélníkem za písmeny.
- Titulky slovo po slově s hlasem (R4): aktivní slovo má podklad v barvě značky, ostatní bílá, spodní třetina (podrobnosti v `reference/R4-easing-edukace.md`,
  oddíl „Střihová partitura“).
- **Jedno číslo na video**: skutečné, roluje zdola 0,7 s jen horšími hodnotami, odometrické rozmazání, klid ≥ 1 s, odchod zblednutím.

## 5. Co se změnilo proti dosavadní praxi (V001–V004)
| dřív | teď |
|---|---|
| storyboard po taktech, událost na každou dobu | storyboard po **stavech hrdiny**, událost = změna stavu každých ~0,6 s, bez metronomu |
| 3–5 prvků naráz, mřížky, 4 fakta za 8 s | 1 hrdina + 1 doplněk, jedno číslo |
| karty a UI naskakují ostře maskou, odchod „do bodu“ ~0,25 s | příchod z rozostření, odchod do rozostření kratší než příchod |
| tvrdé střihy na čtvrtdoby, švihy | proměny; tvrdý střih jen ve skutečné stopáži a i přes něj přežívá spojovací prvek |
| hudba vede, drop nejhlasitější, SFX na každé události | hlas / věta vede; zvuk až podle obrazu; hudba pod hlasem až k tichu; jeden úder na podpis |
| end card klienta 2–4 s | logo klienta → ticho → boom + záblesk → **podpis tvůrce** 2 s + disclaimer |
| 16:9 „nahé“ video | 16:9 animace + prezentace (natočená obrazovka 9:16 nebo mockup s CTA) |

## 6. Kontrolní seznam střihu (kritik, kreativní ředitel)
- [ ] v každém snímku nejvýš 1 hrdina + 1 doplněk (spočítat na archu po 0,25 s)
- [ ] 0 tvrdých střihů v grafické vrstvě; střihy ve stopáži mají přežívající spojovací prvek
- [ ] partitura: každý prvek má příchod / klid / odchod / spojku; žádný prvek „navíc“
- [ ] příchody z rozostření 0,1–0,25 s, odchody kratší (0,05–0,2 s) a proměnou; žádná prolínačka scén
- [ ] klid: slovo ≤ 0,33 s, řádek ≤ 0,6 s, karta ≤ 1,2 s, hrdina 2–5 s; číslo ≥ 0,5 s a jen jedno ve videu
- [ ] obraz předbíhá slovo / větu o 0,1–0,35 s, nikdy nezaostává; pauzy vyplněné pohybem
- [ ] přechody mezi světy: každý jiný, žádný dvakrát; semínko na snímku 0 a návrat do loga na konci
- [ ] zvuk podle obrazu: SFX jen na proměny, hudba pod hlasem (≤ −25 LUFS) nebo doladěná k proměnám; boom + záblesk jen na podpis
- [ ] prezentace: natočená obrazovka nebo mockup; end card tvůrce 2 s s disclaimerem, kamera dýchá i na end card

## 7. Nástroje k doplnění při příštím videu (animátor, na pokyn režiséra)
`nastroje/vzory/scena.html`: `rozIn(t, t0, d)` / `rozOut(t, t0, d)` (Gauss + zblednutí), `odometr()` se svislým rozmazáním (vyšší řády se ustálí první),
`tah()` kreslení rámečku a loga, `wipePruhy()` v barvách značky, `clonaKruh()`, `explozeTecky()`, maketa natočené obrazovky (dýchání, zhasnutí, odraz).
Workflow: fáze **partitura** (kreativní ředitel) před klíčovými snímky; kritik dostává partituru a kontroluje ji po snímcích.
