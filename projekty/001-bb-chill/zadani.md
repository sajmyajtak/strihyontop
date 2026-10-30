# V001: Bageterie Boulevard: pohodový chill spot

| | |
|---|---|
| Datum zadání | 2026-10-30 |
| Platforma / formát | IG Reels / TikTok / Shorts, 1080×1920 (9:16), 60 fps |
| Délka | **25 s** |
| Termín | co nejdřív |
| Stav | výroba |

## Zadání (doslova od uživatele)
> hele vem si od tehle stranky barvu na vide logo hudbu takovou když jdeš jíst například od mekače což znamená pohodová chill. https://www.bb.cz
>
> a motion nechám na tebe pohraj si to stím zadej to hlavně agentovi at vybere fákt dobry motion a i hudbu at uděla a vše řešil pokud bude něco potřeba. Hlavní mozek to bude a když si nebude moc radit at se mě zeptá. delká vide 25 vteřin

## Pravidla pro toto video
Pravidla od uživatele (mají přednost před vším ostatním):
1. Barvy a logo **z webu bb.cz** (Bageterie Boulevard).
2. Hudba **pohodová, chill**, „jako když jdeš jíst do McDonald's“: feel-good, uvolněná, příjemná.
3. Motion necháno na nás: **„fakt dobrý motion“**, pohrát si s tím.
4. Délka **25 s**.
5. Když si agent nebude vědět rady → zeptat se uživatele (přes režiséra).

Výchozí nastavení (`znalosti/znacka.md`): angličtina na obrazovce, bez voiceoveru, CTA podle zadání (není zadáno → rozhodl režisér, viz níže).

Obecná pravidla, která se tu hlavně uplatní: A1, A2, A5, A7, B1, B6, C1, C6, C7, C8, D2, D4, D5, D6, E1–E8, F1–F7, G1–G6, I3, I5–I8, J5, K.

## Rozhodnutí režiséra (uživatel je nechal na nás)
- **Typ videa**: spec / konceptová reklama pro portfolio (jako R1 Waze). Značku nezastupujeme → **disclaimer** malým písmem na end card
  „Concept ad · not affiliated with Bageterie Boulevard“ + v popisku příspěvku (pravidlo J5).
- **Jazyk**: angličtina (I8). Slogan značky přeložen věrně: „Not fast food. Express gourmet.“ (originál: „Nejsme fastfood. Jsme exprès gourmet!“).
  Žádná vymyšlená čísla, ceny ani tvrzení (C8).
- **CTA**: není zadané → end card = logo BB + slogan + „bb.cz“.
- **Vizuál**: přednostně motion design postavený v kódu (tvary, typografie, ilustrace surovin a bagety z tvarů), logo z oficiálního SVG.
  Produktové fotky z webu jen tehdy, když jsou kvalitní a slouží konceptu.
- **Hudba**: vlastní z `nastroje/hudba.py`. Chybí nálada „pohodová“ (chill feel-good) → agent ji doplní jako nový preset.

## Reference
| ID | odkaz | co z ní převzít |
|---|---|---|
| R1 | znalosti/reference/R1-waze-koncept.md | spec reklama na značku, příběh za 25 s, přechody bez střihů, end card s logem |
| PM | znalosti/prompt-motion/poznatky.md | metoda, kostra zadání (oddíl 10), zakázané AI znaky, výběr promptu (oddíl 6) |

## Materiály
| soubor | kde je | použití |
|---|---|---|
| logo SVG | https://www.bb.cz/assets/cs/images/bb_logo_full.svg | end card, značka |
| barvy, fonty | CSS webu bb.cz | paleta, typografie |

## Režijní list
- **Koncept jednou větou**: (doplní animátor v 1. fázi, schvaluje režisér)
- **Prompt / šablona z prompt-motion**: (vybere animátor, zdůvodní)
- **Vzhled**: barvy a font podle webu bb.cz, max 3 barvy + černá/bílá
- **Rytmus**: hudba „pohodová“ ~95–105 BPM, drop ~25–35 % délky, end card ~22–25 s
- **Akceptační kritéria pro kritika**:
  1. 1080×1920, 60 fps, 25,0 s ± 0,1 s, H.264 + AAC
  2. −14 LUFS ±1, true peak ≤ −1 dBTP (po AAC)
  3. Barvy a logo odpovídají bb.cz (logo nezdeformované, barvy z CSS webu)
  4. Snímek 0 je hotový obraz, háček do 1 s, žádný text v bezpečných zónách
  5. Žádné AI poznávací znaky (G6), žádný lineární pohyb, žádné zamrznutí > 1 s bez textu
  6. Hudba je pohodová (≈ 95–105 BPM, durová / feel-good), pásma v mezích (I7), obraz sedí na doby a drop
  7. End card: logo + slogan + bb.cz + disclaimer, drží 1,5–3 s
  8. Texty anglicky, bez překlepů, bez vymyšlených tvrzení

## Storyboard / časová osa
(doplní animátor v 1. fázi)

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
