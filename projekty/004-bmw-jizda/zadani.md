# V004: BMW řady 7: realistická reklama s jízdou (sport luxus, SaaS motion graphics)

| | |
|---|---|
| Datum zadání | 2026-11-01 |
| Platforma / formát | **16:9, 1920×1080, 60 fps** |
| Délka | **30,0 s** |
| Stav | příprava |

## Zadání (doslova od uživatele)
> není to ono ja jsem chtěl asi vybereš realistické auto jak vypada že animuješ aby to vypadalo realstické při ukázce auta i rychlosti výkonu a ty obrazky byly jen dopnění materialu. Udělej to na bmw : https://www.bmw.cz/cs/index.html (+ parametry kampaně)
>
> udělej to na tenhle vůz poslal jsem ti odkaz:
> https://configure.bmw.cz/cs_CZ/configure/G70/81HY/FVCSW,P0300,S01FE,S0230,S0248,S02PA,S02VB,S02VD,S02VH,S02Z4,S0302,S0319,S03CK,S03DM,S03DN,S03M3,S03MF,S0416,S0420,S0428,S043B,S0465,S04A2,S04FL,S04FM,S04HA,S04HC,S04T2,S04U6,S04U9,S04V1,S0548,S05AT,S05AV,S05DN,S0617,S061B,S0654,S06AE,S06AF,S06D5,S06NY,S06WF,S0710,S0760,S0775,S07M9,S0851,S0879,S08R3,S08R9,S08TF,S09QX,S09T1,S09T2,S09TB/SE000001
>
> a chci aby si z toho webu vybral fotky auta a máš tam i přístup 360 kameře kterou můžeš použit. Udělej fakt realistickou reklamu kde auto se bude pohybovat a ejt rychle i ukazka nového modelu a jeho salonu. 30s video dlouhé, hudba sport luxus, 16:9, bez voice over,dynamické, k tomu realistické záběry a saas motion graphics zaběry:
> https://prompt-motion.com/motiondsgnr-9dcfa6
> https://prompt-motion.com/lukasersil-0ed38e
> https://prompt-motion.com/souravbhar871-61f424
> https://prompt-motion.com/adamdesgns-478d6d

Upřesnění (2026-11-01, doslova):
> barvy použij jaký mají na stránkách a auto co jsem ti poslal.

Dotaz a rozhodnutí (2026-11-01): uživatel se zeptal, proč nemůžu generovat AI video. Vysvětleno: Higgsfield je v prostředí (umí video i z obrázku),
ale uživatel ho 2026-10-30 zakázal; jiný generátor není. Nabídnuto povolení pro V004 (cena předem). Odpověď uživatele (doslova):
> tak zkus sám a potom uvidíme

→ **V004 bez Higgsfieldu**, jen skutečný materiál BMW + vlastní animace. Po zpětné vazbě případně zvážit AI záběry.

## Pravidla pro toto video (od uživatele, mají přednost před vším ostatním)
1. **Vůz z odkazu uživatele** (konfigurace G70 / 81HY, přesně tato výbava a barva). **Barvy grafiky z webu bmw.cz.**
2. **Realistická reklama, kde vůz jede a jede rychle** (pohyb, rychlost, výkon). Fotky a rendry jsou **jen doplněk** materiálu.
3. Ukázka **nového modelu** a jeho **salonu** (interiér).
4. Fotky auta vybrat z webu BMW, smí se použít **360° kamera** konfigurátoru.
5. **30 s**, **16:9**, hudba **sport luxus**, **bez voiceoveru**, **dynamické**.
6. Kombinace **realistických záběrů** a **SaaS motion graphics záběrů** podle 4 předloh z prompt-motion (výše).
7. Dál platí: anglicky, energie (V001), nic kresleného na voze (V002), vůz musí jet (V003).

## Rozhodnutí režiséra
- **Generovat video AI nemůžeme** (Higgsfield zakázaný uživatelem, jiný generátor nemáme) a 3D model vozu od BMW stáhnout nejde.
  Realistickou jízdu proto stavíme ze **skutečného materiálu BMW**, který web načítá běžně (videa a fotky na bmw.cz a v konfigurátoru, případně
  tiskové materiály BMW Group, pokud jsou volně přístupné), a z **2,5D animace rendrů konfigurátoru** (vůz v uživatelově konfiguraci).
  Načítat jen normálně, nic neobcházet (C024). Videa chráněná DRM nestahovat.
- **Klíčová otázka pro přípravu**: existují záběry jízdy **v barvě a provedení vozu z odkazu**? Když ne, režisér rozhodne mezi:
  (a) jízdní záběry BMW v jiné barvě + konfigurace uživatele v rendrech (riziko: nesoulad s pravidlem 1), (b) „jízda“ z rendrů konfigurace
  (2,5D sledovací záběr: vyříznutý vůz, rotace kol, rozmazané pozadí, otřes), (c) dotaz na uživatele. Rozhodnutí zapsat sem.
- **Spec reklama do portfolia**: disclaimer „Concept ad · not affiliated with BMW“, materiály © BMW AG, jen portfolio (upozornit uživatele).
- **Hudba** (pevná struktura): nálada `luxsport` (V003), **120 BPM**, takt 2,0 s, **15 taktů = 30,0 s**: úvod / odhalení 0–4, **drop 1 = 4,0**
  (jízda), jízda a nový model 4–12, **zlom 12,0** (salon, klidnější), stoupání 16,0–18,0, **drop 2 = 18,0** (rychlost, výkon, nejsilnější),
  rychlost 18–26, **end card 26,0–30,0** (logo na finální úder 26,0).
- **Fakta** (výkon, zrychlení, max. rychlost, dojezd…) jen doslova z bmw.cz / konfigurátoru pro tuto konfiguraci.

## Akceptační kritéria pro kritika
1. 1920×1080, 60 fps, 30,0 s ± 0,1 s, H.264 + AAC, BT.709; −14 LUFS ±1, true peak ≤ −1 dBTP (po AAC)
2. **Vůz jede**: aspoň 40 % délky videa je vůz v pohybu (jízda, průjezd, rychlost) a divák to na první pohled pozná. Rychlost je cítit.
3. **Realismus**: žádný kreslený vůz, žádná koláž (lem masky, plovoucí vůz bez stínu, nesedící světlo nebo perspektiva). Divák nepozná AI.
4. **Vůz = konfigurace uživatele** (barva, kola, provedení) všude, kde je ve videu „náš“ vůz; výjimky jen podle rozhodnutí režiséra výše.
5. Nový model + **salon** (interiér) jsou poznat. Na konci výkon / rychlost (fakta jen z bmw.cz).
6. **SaaS motion graphics** záběry podle 4 předloh (kritik / kreativní ředitel je pojmenuje s časy), barvy z bmw.cz
7. Energie: dynamické, událost na každou dobu, drop 1 a drop 2 nejsilnější, žádná mrtvá pasáž > ~1 s
8. Logo BMW nedeformované, end card + disclaimer, texty anglicky bez překlepů, v bezpečné zóně (A5)

## Materiály
| soubor | kde je | použití |
|---|---|---|

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
