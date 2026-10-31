# V002: Mercedes-Benz: závodní spot (energický)

| | |
|---|---|
| Datum zadání | 2026-10-31 |
| Platforma / formát | **16:9, 1920×1080, 60 fps** |
| Délka | **30,0 s** (rozsah uživatele 25–35 s, zvoleno podle motionu a hudby) |
| Stav | příprava |

## Zadání (doslova od uživatele)
> okey hele není to špatný ale není to ono. potřebuju víc energetické at to není tak bez duši to video. tím myslím že at je to rychlejší a více zaživnější at má to více efektů. videa budeš dělat 16:9 a kolem 25-35 vteřin podle toho jaký si vybereš motion z strýnky. udělej jen vždy jedno video ale ted zkus s hudbou ale bez voiceover. udělej mi reklamu na https://www.mercedes-benz.cz/ maš tam i logo použij tam i barvy keteré jsou na stránkach a hudba bude sportovní a auto nebo ta reklama bude hlavně o závodění aut který má mercedes. motion at vybere hlavní agent a at jsou tam minimálně 3 ale můžeš použít i víc

## Pravidla pro toto video (od uživatele, mají přednost před vším ostatním)
1. **Víc energie než V001**: rychlejší, živější, **víc efektů**, „ať to není bez duše“.
2. **16:9**, délka **25–35 s** podle zvoleného motionu.
3. **Jedno video.** S **hudbou**, **bez voiceoveru**.
4. Reklama na **mercedes-benz.cz**: použít **logo** a **barvy z jejich webu**.
5. Hudba **sportovní**. Reklama je hlavně o **závodění aut, která Mercedes má**.
6. Motion vybere **hlavní agent**, **minimálně 3 motiony** z prompt-motion (víc je povoleno).

## Rozhodnutí režiséra
- **Spec reklama do portfolia**, Mercedes-Benz nezastupujeme → disclaimer na end card „Concept ad · not affiliated with Mercedes-Benz“
  + v popisku (J5), v popisku žádný @handle značky.
- **Závodění**: Mercedes-AMG motorsport (formule a závodní AMG GT) jako **stylizované vozy postavené v kódu** (siluety, lak, světla, stopy),
  žádné fotky, žádná loga sponzorů (např. Petronas), žádná jména jezdců ani čísla titulů, pokud nejsou doslova na mercedes-benz.cz (C8).
- **Texty anglicky**, krátké, jen ze značky nebo obecné závodní výrazy (např. „0 → 100“ jen pokud je to na webu; jinak bez čísel).
- **Hudba** (pevná struktura, aby zvukař a koncept mohli běžet souběžně): **128 BPM**, takt 1,875 s, **16 taktů = 30,0 s**.
  Úvod a nádech v taktech 1–2, **drop 1 = 3,75 s** (takt 3), plná jízda takty 3–8, **zlom (breakdown) 15,0 s** (takt 9),
  stoupání takt 10, **drop 2 = 18,75 s** (takt 11, nejsilnější moment), finále takty 11–14, **end card 26,25–30,0 s** (takty 15–16)
  s finálním úderem v 26,25 s. Nová nálada `sportovni` v `nastroje/hudba.py` (driving electro / racing: tvrdý kopák, distorzovaná basa,
  risery, údery, syntetický „motor“ jako zvukový motiv).
- **Zvolené motiony z prompt-motion (4)**:
  1. **Šablona showreel** (prompt-motion.com/templates/showreel): kostra na doby, **jedna technika na takt**, poslední celý takt nejsilnější,
     2D → 3D moment, end title, kontrola 1 snímku na dobu.
  2. **Taxtello app film** ([`daniel-haida-8691d4`](https://prompt-motion.com/daniel-haida-8691d4)): **agresivní kinetická typografie**,
     údery, švihy a glitch akcenty na doby.
  3. **UGC ad generator promo** ([`twoclipping-6dd14e`](https://prompt-motion.com/twoclipping-6dd14e)): **třes kamery na údery**, rozmazání
     pohybem, švihy, mřížka dob zkalibrovaná na skutečné údery kopáku.
  4. **Food craving launch film** ([`ultimaxbt-2ddf1e`](https://prompt-motion.com/ultimaxbt-2ddf1e)): souvislý záběr, **přechody zaplavením
     barvou z objektu**, zvuk na každou událost, 8 podsnímků u rychlých pohybů.

- **Web Mercedesu blokuje automatický přístup (403)** na mercedes-benz.cz, .com, group i amg. Obcházet ochranu nebudeme (pokus o to
  zastavila bezpečnostní pravidla prostředí a je to správně). Proto: **logo z Wikimedia Commons** (oficiální hvězda) a **předběžná paleta**
  (černá, bílá, stříbrná, modrý akcent #0078D6) jako CSS proměnné. Uživatel byl požádán o screenshot webu, podle něj se paleta ověří a případně
  vymění před finálním renderem. Texty jen obecné nebo vlastní claimy reklamy, žádná fakta (C8).

## Akceptační kritéria pro kritika
1. 1920×1080, 60 fps, 30,0 s ± 0,1 s, H.264 + AAC, BT.709
2. −14 LUFS ±1, true peak ≤ −1 dBTP (po AAC)
3. **Energie**: událost na každou dobu, úder každý takt, žádná „mrtvá“ pasáž > ~1 s, aspoň 6 různých energických efektů
   (rychlostní čáry, světelné stopy, záblesk/otřes na úderu, švih, zoom, glitch akcent…) synchronních s hudbou
4. Logo Mercedes-Benz z oficiálního zdroje, nedeformované. Barvy odpovídají webu mercedes-benz.cz
5. Je poznat, že jde o **závodění** (vozy, trať, rychlost) a o **Mercedes**
6. Hudba sportovní, drop 1 v 3,75 s a drop 2 v 18,75 s jsou vizuálně nejsilnější momenty, klíčové SFX slyšet (I3)
7. End card: logo + text + disclaimer, drží ~3,75 s, nezamrzlý
8. Texty anglicky, bez překlepů, bez vymyšlených faktů. Text v bezpečné zóně 16:9 (A5)
9. Aspoň 3 zvolené motiony jsou ve videu poznat (kreativní ředitel je pojmenuje s časy)

## Materiály
| soubor | kde je | použití |
|---|---|---|

## Režijní list
- **Koncept jednou větou**: (doplní kreativní ředitel)
- **Vzhled**: (barvy a font z webu doplní analytik)

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
