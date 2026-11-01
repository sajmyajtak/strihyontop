# V003: BMW řada 7: realistická reklama ve stylu SaaS motion

| | |
|---|---|
| Datum zadání | 2026-11-01 |
| Platforma / formát | **16:9, 1920×1080, 60 fps** |
| Délka | **25,0 s** (pokyn uživatele 2026-11-01) |
| Stav | příprava |

## Zadání (doslova od uživatele)
> není to špatný ale pted použij realný modely 3D od bmw který mají na stránkách a zkus udělat tu reklamu víc realičtnější tím co myslím je že at není to tak moc kreslený ale saas motion který je velice populárny ale použij realisticke modely aut který fakt vypadají jak v realitě
>
> https://www.bmw.cz/cs/index.html (+ parametry kampaně)
>
> https://configure.bmw.cz/cs_CZ/configure/G70/21HZ/FKVSW,P0300,S01CB,S01CE,S01DG,S01DH,S01F4,S0230,S0248,S02TB,S02VB,S02VD,S02VH,S0302,S0319,S03CK,S03DN,S0416,S0428,S0465,S04A2,S04D7,S04FL,S04FM,S04HA,S04HC,S0548,S05AT,S05AV,S05DN,S0617,S061B,S0654,S06AE,S06AF,S06D5,S06NY,S06WF,S0851,S0879,S08KA,S08R3,S08R9,S08TF,S09QX
>
> a udělej s fakt dobrou realisticko ureklamu kterou jen tak člověk nerozwezná že to je dělany přes ai claude a aby byl wow efekt
>
> (+ 5 obrázků z konfigurátoru: předek, záď, 3/4 zepředu, detail kola 2×)

Upřesnění (2026-11-01, doslova):
> reklama 16:9, 25 s video bude trvat, luxusní sportovní hudba, video bude a luxusu a pohodlí a ukázka výkonu na konci kolik to muže jet, bez voice over, 5 motion na přechody, ukazku, auta, výlonu, luxusu a muže být i více motion templetu

Další upřesnění (2026-11-01, doslova):
> na konci bude simpl skládací logo bmw

## Pravidla pro toto video (od uživatele, mají přednost před vším ostatním)
1. **Reálné vozy BMW** z jejich webu / konfigurátoru („reálné 3D modely od BMW, které mají na stránkách“), **nic kresleného**.
2. **Realistická** reklama: vozy „fakt vypadají jak v realitě“, **nepoznat, že to dělala AI**.
3. Styl **SaaS motion** („velice populární“).
4. **Wow efekt.**
5. **16:9, 25 s.** **Luxusní sportovní hudba**, **bez voiceoveru**.
6. Obsah: **luxus a pohodlí**, **na konci ukázka výkonu** („kolik to může jet“).
7. **Aspoň 5 motionů** z prompt-motion (na přechody, ukázku auta, výkonu a luxusu), může jich být víc.
8. **Na konci jednoduché skládací logo BMW** (logo se složí z částí: prstenec, čtvrtiny, písmena; čistě, bez efektů navíc).
9. Dál platí: jedno video, anglicky, energie (V001), barvy podle značky.

## Rozhodnutí režiséra
- **Vůz**: BMW řady 7 (G70, 740d) přesně v konfiguraci z odkazu uživatele (bílá, černá střecha, kola z detailu). Jiné modely ne.
- **3D modely z konfigurátoru stáhnout nejde** (jsou v něm jen jako obrázky, které vyrábí server BMW). Proto stavíme z **jejich rendrů**:
  4 obrázky od uživatele + další pohledy, které konfigurátor ukáže v běžném prohlížeči (360° exteriér, interiér). Web bmw.cz odpovídá (200),
  načítat **normálně** (Playwright jako běžný prohlížeč). Když se objeví blokace, captcha nebo 403, **nic neobcházet** (C024) a říct režisérovi.
- **Realismus**: produkt = jen skutečné rendry BMW, animace 2,5D (maska vozu, paralaxa, pomalá kamera, odlesk jen v masce karoserie, rotace kola
  z detailu, rozsvícení světel, kontaktní stín), pravidlo G7. UI prvky SaaS motion (karty, přepínače, kurzor, typografie) jsou grafika, ta smí být v kódu.
- **Spec reklama do portfolia**: BMW nezastupujeme → end card „Concept ad · not affiliated with BMW“, v popisku bez @handle. Obrázky jsou © BMW AG
  (rendry z konfigurátoru dodal uživatel). Jen portfolio, ne placená kampaň (upozornit uživatele).
- **Texty anglicky**, krátké. Fakta (výkon, rozměry, výbava) **jen doslova z bmw.cz** s odkazem na stránku v zadání (C8), jinak bez čísel.
- **Hudba** (pevná struktura, aby zvukař a koncept běželi souběžně): **120 BPM**, takt 2,0 s, **25,0 s = 12,5 taktu**.
  Úvod takty 1–2 (0–4, luxusní odhalení), **drop 1 = 4,0 s** (takt 3), design a exteriér takty 3–5 (4–10),
  **zlom 10,0 s** (takty 6–7: luxus a pohodlí, interiér, klidnější), stoupání 14,0–16,0 (takt 8),
  **drop 2 = 16,0 s** (takt 9, nejsilnější: **výkon**), výkon takty 9–11 (16–22, vrchol „kolik to může jet“),
  **end card 22,0–25,0 s** s finálním úderem v 22,0. Nová nálada `luxsport` (**luxusní sportovní**: elegantní a drahá, ale s tahem:
  hluboký čistý kopák, sub basa, smyčce / pad, klavír nebo Rhodes, sklenité staby, motor jako motiv před výkonem, risery, údery).
- **Výkon**: čísla (maximální rychlost, zrychlení 0–100, výkon) **jen doslova z bmw.cz / technických údajů konfigurátoru** pro tuto konfiguraci (740d),
  s odkazem. Když je nenajdeme, ukážeme výkon bez čísel.
- **Styl**: SaaS motion jako jazyk rozhraní (karty, čísla, popisky), produkt realisticky (G7).
- **Motiony z prompt-motion**: vybere analytik (**aspoň 5**: přechody, ukázka auta, luxus, výkon), zapíše sem.

## Akceptační kritéria pro kritika
1. 1920×1080, 60 fps, 25,0 s ± 0,1 s, H.264 + AAC, BT.709; −14 LUFS ±1, true peak ≤ −1 dBTP (po AAC)
2. **Realismus**: vůz je ve všech záběrech skutečný render BMW (ne kresba), bez artefaktů masky (lem, schody, „vystřižený“ okraj), bez natažených
   nebo deformovaných částí, odlesky a stíny fyzikálně věrohodné. Divák nepozná, že video dělala AI.
3. **SaaS motion**: čisté UI prvky (karty, přepínače, kurzor, popisky s linkou k detailu vozu), plynulé pružné pohyby, kinetická typografie, produkt hrdina
4. **Energie a wow**: událost na každou dobu, žádná mrtvá pasáž > ~1 s, drop 1 a drop 2 nejsilnější momenty.
   **Obsah**: luxus a pohodlí (interiér, detaily) a na konci výkon (maximální rychlost; čísla jen z bmw.cz)
5. Logo BMW nedeformované, barvy podle bmw.cz, texty anglicky bez překlepů, fakta jen z bmw.cz, text v bezpečné zóně (A5)
6. End card: **jednoduché skládací logo BMW** (složí se z částí na finální úder 22,0, logo nedeformované, přesně podle oficiálního tvaru) + CTA + disclaimer
   „Concept ad · not affiliated with BMW“, drží ~3 s, nezamrzlý
7. Aspoň **5** zvolených motionů je ve videu poznat (kreativní ředitel je pojmenuje s časy)
8. Hudba luxusní sportovní, bez voiceoveru

## Materiály
| soubor | kde je | použití |
|---|---|---|
| `bmw7_predek.png`, `bmw7_zad.png`, `bmw7_tri-ctvrte-predek.png`, `bmw7_kolo-detail.png` (2000×1286, od uživatele, z konfigurátoru) | `media/projekty/003-bmw-rada7/materialy/` | hlavní záběry vozu (5. obrázek byl duplikát detailu kola) |

## Režijní list
- **Koncept jednou větou**: (doplní kreativní ředitel)

## Storyboard / časová osa
(doplní kreativní ředitel)

## Průběh výroby
| kolo | kdo | co se dělalo | verdikt kritika | hlavní nálezy |
|---|---|---|---|---|

## Chyby během výroby

## Spotřeba tokenů
| agent / úkol | tokeny | akce nástrojů | čas |
|---|---|---|---|

## Verze
| verze | datum | soubor / kam doručeno | změny |
|---|---|---|---|

## Zpětná vazba (doslova)

## Poučení
