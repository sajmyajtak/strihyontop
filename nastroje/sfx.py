"""Zvukové efekty syntézou v kódu (naše vlastní, bez licencí, I5): papír, chleba, jemné kliky. Vrchol přesně na událost (I3).

Použití:
  python3 -I nastroje/sfx.py --udalosti udalosti.json --delka 25 --out sfx.wav
        [--hudba hudba.wav --mix zvuk.wav --bez-hudby zvuk_bez_hudby.wav] [--ticho 18.75-19.375]
        [--automatika 7.215-7.49:-14:25:8 …]
  --automatika OD-DO:DB[:DOLU_MS[:NAHORU_MS]] = automatika hlasitosti HUDBY jen v mixu (hudba.wav ani její časování se nemění):
          v úseku OD–DO je hudba o DB tišší, náběh dolů končí v OD, návrat nahoru začíná v DO (výchozí 20 / 10 ms, kosinově).
          Víc úseků se kombinuje minimem (platí nejhlubší ztlumení). Hlasitost efektů proti hudbě se počítá už proti ztlumené hudbě.
  --zisk-hudby T:DB,T:DB,…[@HZ] = obálka zisku HUDBY v mixu po bodech (dB lineárně mezi body, před prvním a za posledním bodem
          0 dB; úseků víc, násobí se), např. stoupání do dropu nebo ztišení jízdy (V002). S `@HZ` jen pásmo nad HZ (komplementární
          dělení s nulovou fází: při stejném zisku se hudba složí zpět bit po bitu, časování se nemění). Uplatní se před --automatika.
  --saturace OD-DO:KOLENO_DB = měkké nasycení špiček MIXU v úseku (4× převzorkování, náběh/doběh 20 ms) před limiterem: sníží poměr
          špička / tělo úderu, takže úder může být hlasitější, aniž by ho limiter dlouho mačkal (V002 drop 2). Pod kolenem
          (KOLENO_DB pod stropem limiteru, výchozí strop −1,5) se signál nemění, nad ním tanh do stropu.
udalosti.json: [{"cas": 0.625, "typ": "glp", "lu": -9, "pan": 0.0, "popis": "…"}, …]
  cas     = kdy má padnout ZMĚŘENÝ vrchol (obálka analytického signálu vyhlazená 2 ms), ne začátek zvuku
  lu      = o kolik LU je efekt tišší než hudba v okně 100 ms (potřebuje --hudba), jinak uroven = špička v dBFS
  pan −1 … 1, volitelně "ton" (násobek výšky), "seed" (stejný seed = stejný zvuk), "strop" (max. špička v dBFS, výchozí −6),
          "drive" (dB, jemné tanh nasycení zvuku: sníží poměr špička / tělo, takže hlavní efekt je slyšet a strop ho neusekne),
          "pan_do" (+ "pan_tau" s, výchozí 0,12): průjezd, panorama se kolem vrcholu přelije z `pan` do `pan_do`
  PODKLAD (typy v PODKLADY, např. "volnobeh"): {"cas": OD, "do": DO, "typ": "volnobeh", "lu": -8} = souvislý zvuk od–do,
          `lu` platí proti hudbě v celém úseku, vrchol se nezarovnává ani nekontroluje (V002 kolo 2: tělo háčku pod klonky).
          Jen výjimečně: I3 chce zvuk na událost, ne koberec. Doběh podkladu nechat skončit před nádechem / tichem.
  --limiter DBFS = místo lineárního ztlumení celého mixu sběrnicový limiter jen na špičkách (192 kHz, latency=1). Pro hudbu s malou
          rezervou (sportovní: −14 LUFS při špičce −1,5 dBFS), kde se efekt sečte s úderem; bez volby se chová jako dřív (V001 bit po bitu).
Závodní zvuky (V002): rele, ting, odpal, doppler(_tichy/_dvojity), prujezd_gt, prujezd_daleko, vzduch, svih(_rotace), prulet,
  nasati(_dlouhe), pneu(_svist), kov_uder(_suchy), cink_el, fup, brzdy, jiskry, skrt, zatah, vzum(_trisk), tik, radeni, glitch,
  svetelny_uder, sssink, vuff, klap_kov, fump, dopad_logo. Šum má srovnanou obálku (`rovny_sum`), průjezdy „svist“ v nejbližším bodě:
  změřený vrchol = navržený vrchol (rozptyl mezi seedy ≤ ~10 ms, zarovnání na událost pak přesně).
Výstup: sfx.wav (48 kHz stereo) + sfx.json (čas, typ, změřený vrchol samotného zvuku i v hotové stopě, odchylka v ms,
úroveň, hlasitost efektu proti hudbě v okně 400 ms). Typy zvuků: viz ZVUKY.
"""
import argparse
import json
import subprocess
from pathlib import Path

import numpy as np
from scipy import signal
from scipy.io import wavfile

SR = 48000


def cas(n):
    return np.arange(n) / SR


def pasmo(x, lo, hi, rad=2):
    sos = signal.butter(rad, [lo / (SR / 2), min(hi, SR / 2.05) / (SR / 2)], btype="bandpass", output="sos")
    return signal.sosfilt(sos, x)


def dolni(x, f, rad=2):
    return signal.sosfilt(signal.butter(rad, f / (SR / 2), output="sos"), x)


def horni(x, f, rad=2):
    return signal.sosfilt(signal.butter(rad, f / (SR / 2), btype="highpass", output="sos"), x)


def obalka(n, utok, dozneni):
    """Náběh (s) a exponenciální doznění (s): vrchol přesně v `utok`."""
    t = cas(n)
    return np.where(t < utok, (t / max(utok, 1e-5)) ** 1.5, np.exp(-(t - utok) / dozneni))


def ton(f0, f1, n, tau):
    """Sinus s exponenciálním posunem výšky f0 → f1 (časová konstanta tau)."""
    f = f1 + (f0 - f1) * np.exp(-cas(n) / tau)
    return np.sin(2 * np.pi * np.cumsum(f) / SR)


def zrna(rng, n, hustota, delka_zrna=0.0015, lo=1500, hi=7000, rozptyl=0.6):
    """Praskání: krátké šumové impulzy v náhodných časech (papír, kůrka, list). hustota = impulzů za sekundu."""
    x = np.zeros(n)
    m = int(delka_zrna * SR) + 1
    tvar = np.exp(-np.arange(m) / (m / 4))
    for i in np.flatnonzero(rng.random(n) < hustota / SR):
        k = min(m, n - i)
        x[i:i + k] += rng.standard_normal(k) * tvar[:k] * np.exp(rng.normal(0, rozptyl))
    return pasmo(x, lo, hi)


# ---------- zvuky (mono, normalizuje se až při umístění) ----------
def cvak(rng, v=1.0, suchy=False):
    """Papírové cvaknutí: krátký šum 2–7 kHz + tělo kartonu ~450 Hz. `suchy` = kratší, bez těla."""
    n = int(0.06 * SR)
    x = pasmo(rng.standard_normal(n), 2000 * v, 7000) * obalka(n, 0.0008, 0.006 if suchy else 0.009)
    if not suchy:
        x += 0.5 * ton(520 * v, 380 * v, n, 0.01) * obalka(n, 0.001, 0.012)
    return x


def klap(rng, v=1.0):
    """Poklička: dřevitý klepot ze dvou rezonancí (kartonové víčko), měkčí než cvak."""
    n = int(0.08 * SR)
    x = 0.6 * np.sin(2 * np.pi * 820 * v * cas(n)) * obalka(n, 0.001, 0.018)
    x += 0.3 * np.sin(2 * np.pi * 2150 * v * cas(n)) * obalka(n, 0.0008, 0.008)
    return x + 0.5 * pasmo(rng.standard_normal(n), 1500, 5000) * obalka(n, 0.0006, 0.004)


def tuk(rng, v=1.0):
    """Drobný ťuk (pesto, lístek): 3 ms šumu + ťuknutí ~1,2 kHz."""
    n = int(0.03 * SR)
    x = pasmo(rng.standard_normal(n), 1800 * v, 6000) * obalka(n, 0.0005, 0.003)
    return x + 0.6 * np.sin(2 * np.pi * 1150 * v * cas(n)) * obalka(n, 0.0008, 0.006)


def glp(rng, v=1.0):
    """Měkké polknutí: bublina (tón rychle stoupá 180 → 520 Hz) + papírové cvaknutí ve stejném vrcholu."""
    n = int(0.16 * SR)
    t = cas(n)
    f = 180 * v + 340 * v * (1 - np.exp(-t / 0.035))
    b = np.sin(2 * np.pi * np.cumsum(f) / SR) * obalka(n, 0.03, 0.035)
    b += 0.35 * np.sin(2 * np.pi * np.cumsum(2 * f) / SR) * obalka(n, 0.03, 0.02)   # 2. harmonická: slyšet i z telefonu
    c = cvak(rng, 1.1, suchy=True) * 0.7
    k = int(0.03 * SR)
    b[k:k + len(c)] += c
    return b


def klouznuti(rng, v=1.0, delka=0.22):
    """Papír klouže po papíru: šum, jehož pásmo klesá, ease-out (vrchol 20 ms po začátku pohybu)."""
    n = int(delka * SR)
    t = cas(n) / delka
    s = rng.standard_normal(n)
    x = 0.6 * pasmo(s, 2500 * v, 7000) * (1 - t) + 0.4 * pasmo(s, 900 * v, 2600) * t
    x += 0.25 * zrna(rng, n, 220, 0.001, 2000, 7000)
    return x * obalka(n, 0.02, delka / 4.5)


def sustnuti(rng, v=1.0, delka=0.25):
    """Šustnutí lístků rukoly: hustá zrna 2–9 kHz + jemný šum, rychlý náběh."""
    n = int(delka * SR)
    x = zrna(rng, n, 900, 0.002, 2200 * v, 9000) + 0.25 * pasmo(rng.standard_normal(n), 3000, 9000)
    return x * obalka(n, 0.025, delka / 4)


def plink(rng, v=1.0):
    """Kapka: tón stoupající 900 → 1700 Hz, krátký."""
    n = int(0.08 * SR)
    t = cas(n)
    f = 900 * v + 800 * v * (1 - np.exp(-t / 0.012))
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * obalka(n, 0.003, 0.018)


def pumf(rng, v=1.0):
    """Tupé nafouknutí: měkký tón 160 → 90 Hz s harmonickými (telefon pod ~100 Hz nehraje) + závan šumu 200–900 Hz."""
    n = int(0.25 * SR)
    x = ton(160 * v, 90 * v, n, 0.05) + 0.45 * ton(320 * v, 180 * v, n, 0.05) + 0.2 * ton(480 * v, 270 * v, n, 0.05)
    x = x * obalka(n, 0.012, 0.06)
    return x + 0.5 * pasmo(rng.standard_normal(n), 200, 900) * obalka(n, 0.01, 0.04)


def tup(rng, v=1.0):
    """Měkký dopad plátku: kulatý tón ~230 Hz + 2. harmonická + krátký šum 300–1500 Hz."""
    n = int(0.12 * SR)
    x = (ton(260 * v, 210 * v, n, 0.02) + 0.4 * ton(520 * v, 420 * v, n, 0.02)) * obalka(n, 0.004, 0.03)
    return x + 0.4 * pasmo(rng.standard_normal(n), 300, 1500) * obalka(n, 0.002, 0.01)


def bum(rng, v=1.0):
    """Měkké „bum“ chleba (zaklapnutí): tón 130 → 75 Hz s harmonickými + tlumený šum střídy + papírový lem."""
    n = int(0.35 * SR)
    x = ton(130 * v, 75 * v, n, 0.06) + 0.5 * ton(260 * v, 150 * v, n, 0.06) + 0.25 * ton(390 * v, 225 * v, n, 0.06)
    x = x * obalka(n, 0.008, 0.09)
    x += 0.6 * dolni(rng.standard_normal(n), 1200) * obalka(n, 0.004, 0.03)
    k = int(0.007 * SR)                                                  # papírový lem ve stejném vrcholu jako tón
    x[k:k + int(0.06 * SR)] += 0.25 * cvak(rng, 0.8)
    return x


def tsk(rng, v=1.0):
    """Suchý řez papíru: krátký vysoký šum 4–11 kHz se zrnem, vrchol po 6 ms."""
    n = int(0.07 * SR)
    x = pasmo(rng.standard_normal(n), 4000 * v, 11000) + 0.5 * zrna(rng, n, 1500, 0.0008, 3000, 10000)
    return x * obalka(n, 0.006, 0.014)


def nuz(rng, v=1.0, delka=0.31):
    """Nůž po kůrce („sssk“): šum se stoupajícím pásmem a houstnoucím škrábáním, crescendo do konce (vrchol 2 ms před koncem)."""
    n = int(delka * SR)
    t = cas(n) / delka
    s = rng.standard_normal(n)
    x = (1 - t) * pasmo(s, 1800 * v, 4500) + t * pasmo(s, 3500 * v, 10000)
    x += 0.6 * zrna(rng, n, 400, 0.001, 1500, 6000) * t
    e = t ** 2.5 * np.clip((n - np.arange(n)) / (0.002 * SR), 0, 1)
    return x * e


def krupnuti(rng, v=1.0):
    """Křupnutí kůrky: jeden ostrý lom (vrchol 2 ms) + tělo bagety ~170 Hz + hustě praskající drobky, které rychle utichnou."""
    n = int(0.22 * SR)
    lom = pasmo(rng.standard_normal(n), 900 * v, 7000) * obalka(n, 0.002, 0.005)
    telo = (ton(220 * v, 150 * v, n, 0.03) + 0.4 * ton(440 * v, 300 * v, n, 0.03)) * obalka(n, 0.003, 0.035) * 0.5
    drobky = zrna(rng, n, 1400, 0.0012, 1200, 7000) * obalka(n, 0.004, 0.045) * 0.7
    return lom + telo + drobky


def trhnuti(rng, v=1.0):
    """Trhnutí papíru: hustá zrna 1–5 kHz s náběhem 15 ms."""
    n = int(0.2 * SR)
    x = zrna(rng, n, 2500, 0.0015, 1000 * v, 5000) + 0.3 * pasmo(rng.standard_normal(n), 1500, 4500)
    return x * obalka(n, 0.015, 0.05)


def pop_papir(rng, v=1.0):
    """Tiché papírové „pop“ (vrstva se sklopí z roviny): tón 450 → 900 Hz 25 ms + ťuknutí."""
    n = int(0.05 * SR)
    t = cas(n)
    f = 450 * v + 450 * v * (1 - np.exp(-t / 0.01))
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * obalka(n, 0.003, 0.008)
    return x + 0.4 * pasmo(rng.standard_normal(n), 2000, 6000) * obalka(n, 0.003, 0.002)


def zip_(rng, v=1.0):
    """Krátký „zip“ 150 ms (jediný švih ve videu): pásmo šumu stoupá 1 → 6 kHz, zoubky 110 Hz, vrchol 25 ms po začátku."""
    n = int(0.15 * SR)
    t = cas(n) / 0.15
    s = rng.standard_normal(n)
    x = sum(pasmo(s, f / 1.4, f * 1.4) * np.exp(-((t * 4 - i) ** 2) / 0.6) for i, f in enumerate([1000, 1800, 3200, 5000, 6500]))
    zoubky = 0.55 + 0.45 * np.sign(np.sin(2 * np.pi * 110 * v * cas(n))) * 0.5 + 0.225
    return x * zoubky * obalka(n, 0.025, 0.035)


def sss(rng, v=1.0):
    """Tenký tah balsamica („sss“): úzký vysoký šum, ease-out 0,35 s."""
    n = int(0.4 * SR)
    return pasmo(rng.standard_normal(n), 5500 * v, 11000) * obalka(n, 0.012, 0.1)


def sk(rng, v=1.0):
    """Papírové „šk“: krátký šum 1,5–6 kHz se zrnem, náběh 12 ms."""
    n = int(0.09 * SR)
    x = pasmo(rng.standard_normal(n), 1500 * v, 6000) + 0.4 * zrna(rng, n, 600, 0.001, 1500, 6000)
    return x * obalka(n, 0.012, 0.02)


def dopad(rng, v=1.0):
    """Měkký dopad loga: tlumené tup + papírový lem (lehčí než bum)."""
    n = int(0.2 * SR)
    x = (ton(200 * v, 130 * v, n, 0.03) + 0.45 * ton(400 * v, 260 * v, n, 0.03)) * obalka(n, 0.006, 0.05)
    k = int(0.005 * SR)
    x[k:k + int(0.06 * SR)] += 0.3 * cvak(rng, 0.9)
    return x


# ---------- závodní zvuky (V002): motor, doppler, švihy, kov, elektřina ----------
# Šum má sám o sobě náhodně kolísající obálku, takže změřený vrchol by „bloudil“ ±desítky ms od navrženého místa.
# `rovny_sum` obálku šumu srovná (vydělí vyhlazenou obálkou) a teprve pak se násobí navrženou obálkou s ostrým vrcholem:
# změřený vrchol = navržený vrchol, zvuk se dá zarovnat na událost přesně.
def rovny_sum(x, vyhlazeni=0.004):
    e = np.abs(signal.hilbert(x))
    m = max(1, int(vyhlazeni * SR))
    e = np.convolve(e, np.ones(m) / m, mode="same")
    return x / (e + 1e-3 * (e.max() + 1e-12))


def sum_pasmo(rng, n, lo, hi):
    return rovny_sum(pasmo(rng.standard_normal(n), lo, hi))


def spicka(n, vrchol_s, nahoru_s, dolu_s):
    """Obálka s ostrým vrcholem v `vrchol_s`: exponenciální náběh i doznění (tvar ∧), změřený vrchol na místě."""
    t = cas(n)
    return np.where(t < vrchol_s, np.exp(-(vrchol_s - t) / max(nahoru_s, 1e-4)), np.exp(-(t - vrchol_s) / max(dolu_s, 1e-4)))


def motor_ton(f, rng, harm=14, hrubost=0.35):
    """Řev motoru ze zadané okamžité výšky f (Hz, pole): pulzní vlna s harmonickými ~1/k^0,8, mírné kolísání (válce
    nejsou stejné), tanh nasycení. Základ 150–600 Hz: na telefonu slyšet (pod ~100 Hz nehraje)."""
    n = len(f)
    jitter = 1 + 0.012 * dolni(rng.standard_normal(n), 40) / 0.1
    faze = 2 * np.pi * np.cumsum(f * jitter) / SR
    x = sum(np.sin(k * faze + rng.uniform(0, 2 * np.pi)) / k ** 0.8 for k in range(1, harm + 1) if k * np.max(f) < SR / 2.2)
    x = x + hrubost * pasmo(rng.standard_normal(n), 300, 3000) * (0.6 + 0.4 * np.sin(faze / 2))
    return np.tanh(1.8 * x / (np.max(np.abs(x)) + 1e-12))


def doppler_jizda(rng, n, vrchol_s, f0, rychlost=70.0, vzdalenost=6.0, sum_lo=500, sum_hi=4000, sum_podil=0.5, svist=0.6):
    """Průjezd kolem kamery: výška motoru podle Dopplera (blíží se výš, vzdaluje se níž), hlasitost ~1/vzdálenost,
    vrchol hlasitosti přesně v okamžiku nejmenší vzdálenosti (`vrchol_s`). Vítr a pneumatiky = šum se stejnou obálkou."""
    t = cas(n) - vrchol_s
    x = rychlost * t
    r = np.sqrt(x ** 2 + vzdalenost ** 2)
    v_rad = rychlost * x / r                                             # + = vzdaluje se
    f = f0 / (1 + v_rad / 343.0)
    ob = (vzdalenost / r) ** 1.3
    m = motor_ton(f, rng) * (1 - sum_podil) + sum_podil * sum_pasmo(rng, n, sum_lo, sum_hi)
    m = rovny_sum(m, 0.003) * ob                                        # srovnat zvlnění harmonických: vrchol = nejbližší bod
    # „svist“ vzduchu v nejbližším bodě (krátký šum 1–6 kHz): u širokého vrcholu jinak měření bloudí ±20 ms
    return m + svist * sum_pasmo(rng, n, 1000, 6000) * spicka(n, vrchol_s, 0.006, 0.012)


def vrstva_v(x, y, k):
    """Přičte zvuk y do x od vzorku k (oříznutý na délku x)."""
    x = x.copy()
    m = min(len(y), len(x) - k)
    x[k:k + m] += y[:m]
    return x


def kov(rng, n, f0, doba=0.08, partialy=(1.0, 2.76, 5.40, 8.93)):
    """Kovová rezonance: neharmonické částečné tóny (tyč / plech), vyšší doznívají rychleji."""
    t = cas(n)
    return sum(np.sin(2 * np.pi * f0 * p * t + rng.uniform(0, 6.28)) * np.exp(-t * p ** 0.7 / doba) / (1 + 0.4 * i)
               for i, p in enumerate(partialy) if f0 * p < SR / 2.2)


def rele(rng, v=1.0):
    """Elektrické „klonk“ relé startovní lampy: cvak kontaktu + tělo 210 → 150 Hz + krátký brum 100 Hz (proud do lampy)."""
    n = int(0.3 * SR)
    t = cas(n)
    telo = (ton(210 * v, 150 * v, n, 0.02) + 0.5 * ton(420 * v, 300 * v, n, 0.02)) * obalka(n, 0.003, 0.035)
    cvak_ = sum_pasmo(rng, n, 2000, 8000) * obalka(n, 0.0008, 0.004) * 0.8
    brum = pasmo(np.sign(np.sin(2 * np.pi * 100 * t)), 200, 2500) * obalka(n, 0.006, 0.07) * 0.35
    return telo + cvak_ + brum


def ting(rng, v=1.0):
    """Drobné kovové „ting“ (blýsknutí hvězdy, odlesk na logu, uzavření kruhu): krátký zvonivý kov ~2,1 kHz."""
    n = int(0.6 * SR)
    return kov(rng, n, 2100 * v, 0.22) * obalka(n, 0.001, 1.0) + 0.15 * sum_pasmo(rng, n, 5000, 11000) * obalka(n, 0.0008, 0.003)


def odpal(rng, v=1.0):
    """Drop 1 „LIGHTS OUT“: prásk (široký šum + tupý úder) a hned za ním řev motoru, který vytáčí 190 → 330 Hz."""
    n = int(1.1 * SR)
    t = cas(n)
    prask = sum_pasmo(rng, n, 400, 10000) * obalka(n, 0.0015, 0.03)
    uder = (ton(170 * v, 85 * v, n, 0.04) + 0.6 * ton(340 * v, 170 * v, n, 0.04) + 0.3 * ton(510 * v, 255 * v, n, 0.04)) * obalka(n, 0.002, 0.12)
    f = 190 * v + 140 * v * (1 - np.exp(-t / 0.35))
    rev = motor_ton(f, rng) * np.where(t < 0.04, (t / 0.04) ** 2, np.exp(-(t - 0.04) / 0.45)) * 0.45
    return prask + 0.9 * uder + rev


def doppler(rng, v=1.0, delka=1.2, f0=260, rychlost=70.0, vzdalenost=6.0, sum_podil=0.45, lo=500, hi=4000, svist=0.6):
    """Průjezd s Dopplerem, vrchol hlasitosti uprostřed (v nejbližším bodě)."""
    n = int(delka * SR)
    return doppler_jizda(rng, n, delka / 2, f0 * v, rychlost, vzdalenost, lo, hi, sum_podil, svist)


def doppler_dvojity(rng, v=1.0):
    """Příjezd dvou soupeřů: dva průjezdy 110 ms po sobě (druhý o tón výš), první hlasitější (ten dává změřený vrchol)."""
    a = doppler(rng, v, 1.0, 240, 75, 5.0)
    return vrstva_v(a, 0.42 * doppler(rng, 1.12 * v, 1.0, 240, 75, 6.5, svist=0.2)[:len(a)], int(0.11 * SR))


def prujezd_daleko(rng, v=1.0):
    """Vzdálený průjezd (end card): měkký, ztlumené výšky, široký vrchol."""
    return dolni(doppler(rng, v, 1.6, 230, 55, 12.0, 0.35, 300, 1800, svist=1.6), 2200)


def vzduch(rng, v=1.0):
    """Zpomalený průjezd ve zlomu: jen tichý vzduch (šum 250–2500 Hz), široký měkký vrchol, žádný motor."""
    n = int(1.4 * SR)
    s = sum_pasmo(rng, n, 250 * v, 2500 * v) * 0.7 + 0.3 * sum_pasmo(rng, n, 2500, 6000)
    return dolni(s, 3500) * spicka(n, 0.7, 0.22, 0.26)


def svih(rng, v=1.0, delka=0.3, vrchol_podil=0.45):
    """Švih „vuš“: pásmo šumu stoupá a zase klesá (600 → 3 kHz → 1 kHz), ostrý vrchol obálky."""
    n = int(delka * SR)
    p = delka * vrchol_podil
    t = cas(n)
    s = rng.standard_normal(n)
    nizko = sum_pasmo(rng, n, 500 * v, 1500 * v)
    vysoko = rovny_sum(pasmo(s, 1800 * v, 6000 * v))
    w = np.exp(-((t - p) / (delka / 4)) ** 2)                            # výšky jen kolem vrcholu = „otočení“ vzduchu
    return (nizko * (1 - 0.6 * w) + vysoko * w) * spicka(n, p, delka / 6, delka / 5)


def nasati(rng, v=1.0, delka=0.45):
    """Nasátí / „vššš“ do bodu: šum houstne a stoupá (700 Hz → 7 kHz), crescendo, vrchol 3 ms před koncem, pak utne."""
    n = int(delka * SR)
    t = cas(n) / delka
    s = rng.standard_normal(n)
    x = rovny_sum((1 - t) * pasmo(s, 700 * v, 2500 * v) + t * pasmo(s, 2500 * v, 7500 * v))
    e = t ** 3 * np.clip((n - np.arange(n)) / (0.003 * SR), 0, 1)
    return x * e


def pneu(rng, v=1.0, delka=0.2, f0=1350):
    """Cvrknutí / svištění pneumatiky: tón s rychlým vibratem (gumový „chirp“) + šum asfaltu, vrchol po 15 ms."""
    n = int(delka * SR)
    t = cas(n)
    f = f0 * v * (1 - 0.06 * t / delka) + 70 * np.sin(2 * np.pi * 47 * t)
    faze = 2 * np.pi * np.cumsum(f) / SR
    x = np.sin(faze) + 0.35 * np.sin(2 * faze) + 0.15 * np.sin(3 * faze)
    x = x + 0.5 * sum_pasmo(rng, n, 1500, 6000)
    return x * spicka(n, 0.015, 0.006, delka / 4)


def kov_uder(rng, v=1.0, doba=0.07):
    """Tupý kovový úder (dopad textu, slovo tikeru): tělo 170 → 110 Hz + kovové částečné tóny ~620 Hz + cvak."""
    n = int(0.35 * SR)
    telo = (ton(170 * v, 110 * v, n, 0.03) + 0.6 * ton(340 * v, 220 * v, n, 0.03) + 0.3 * ton(510 * v, 330 * v, n, 0.03)) * obalka(n, 0.002, doba)
    plech = kov(rng, n, 620 * v, doba * 0.8, (1.0, 2.32, 4.25, 6.63)) * obalka(n, 0.001, 1.0) * 0.5
    return telo + plech + 0.5 * sum_pasmo(rng, n, 1500, 8000) * obalka(n, 0.0008, 0.004)


def cink_el(rng, v=1.0):
    """Elektrické „cink“ (světelný impuls po linii): FM tón ~3,2 kHz + 3 ms digitálního šumu."""
    n = int(0.25 * SR)
    t = cas(n)
    x = np.sin(2 * np.pi * 3200 * v * t + 1.5 * np.exp(-t / 0.03) * np.sin(2 * np.pi * 4510 * v * t)) * obalka(n, 0.001, 0.07)
    bity = np.round(rng.standard_normal(n) * 2) / 2
    return x + 0.4 * horni(bity, 3000) * obalka(n, 0.0008, 0.003)


def fup(rng, v=1.0):
    """Průlet sloupu těsně u kamery „fup“: krátký závan 250–1500 Hz, vrchol po 50 ms."""
    n = int(0.16 * SR)
    return sum_pasmo(rng, n, 250 * v, 1500 * v) * spicka(n, 0.05, 0.018, 0.03)


def brzdy(rng, v=1.0):
    """Kvílení brzd: vysoký tón ~2,4 kHz s chvěním a klesající výškou, náběh 0,12 s, + tření."""
    n = int(0.5 * SR)
    t = cas(n)
    f = 2400 * v * (1 - 0.05 * t) * (1 + 0.006 * np.sin(2 * np.pi * 9 * t)) + 25 * dolni(rng.standard_normal(n), 30) / 0.05
    faze = 2 * np.pi * np.cumsum(f) / SR
    x = np.sin(faze) + 0.3 * np.sin(2 * faze) + 0.5 * sum_pasmo(rng, n, 1200, 5000)
    return x * spicka(n, 0.12, 0.05, 0.12)


def jiskry(rng, v=1.0, praskani=1.0):
    """Škrtnutí podlahy o obrubník + praskání jisker: ostrý škrab 2–8 kHz, tupé „tk“ 220 Hz a dohasínající zrna (0,4 s)."""
    n = int(0.5 * SR)
    skrab = sum_pasmo(rng, n, 2000 * v, 8000) * (0.7 + 0.3 * np.sign(np.sin(2 * np.pi * 190 * cas(n)))) * obalka(n, 0.003, 0.06)
    tk = ton(260 * v, 200 * v, n, 0.02) * obalka(n, 0.002, 0.025) * 0.5
    zr = zrna(rng, n, 900 * praskani, 0.0008, 2500, 9000) * obalka(n, 0.01, 0.16)
    return skrab + tk + 1.2 * praskani * zr / (np.max(np.abs(zr)) + 1e-12) * 0.6


def zatah(rng, v=1.0):
    """Zátah motoru na výjezdu: výška 230 → 430 Hz, hlasitost stoupá do 0,25 s a pak ujíždí."""
    n = int(0.7 * SR)
    t = cas(n)
    f = 230 * v + 200 * v * np.clip(t / 0.5, 0, 1) ** 0.7
    return motor_ton(f, rng) * spicka(n, 0.25, 0.1, 0.18)


def vzum(rng, v=1.0, trisk=0.0):
    """„Vžum“: rychlý blízký průjezd (krátký doppler) a volitelně krátký třesk ve vrcholu (vyletění vozu se zábleskem)."""
    x = doppler(rng, v, 0.7, 300, 85, 3.5, 0.5, 700, 5000)
    if trisk:
        n = len(x)
        k = n // 2 - int(0.0015 * SR)
        tr = sum_pasmo(rng, n, 800, 10000) * obalka(n, 0.0015, 0.018) * trisk
        x = vrstva_v(x, tr[:n - k], k)
    return x


def tik(rng, v=1.0):
    """Tiché elektronické „tik“ sektorové brány: 1 ms cvak + sinus 2,4 kHz 25 ms."""
    n = int(0.08 * SR)
    t = cas(n)
    return np.sin(2 * np.pi * 2400 * v * t) * obalka(n, 0.0008, 0.012) + 0.5 * sum_pasmo(rng, n, 3000, 9000) * obalka(n, 0.0005, 0.0015)


def zap(rng, n, v=1.0, delka=0.05):
    """Digitální „zap“: pravoúhlá vlna, výška skáče 150 → 1 300 Hz za `delka`, hrubě kvantovaná (bitcrush)."""
    t = cas(n)
    f = 150 * v + 1150 * v * np.clip(t / delka, 0, 1) ** 0.5
    x = np.sign(np.sin(2 * np.pi * np.cumsum(f) / SR))
    return np.round(pasmo(x, 200, 7000) * 3) / 3


def radeni(rng, v=1.0):
    """Řazení: kovové cvaknutí převodovky + krátký digitální „zap“ (glitch akcent v obraze), vrchol v cvaknutí."""
    n = int(0.25 * SR)
    cv = (kov(rng, n, 1450 * v, 0.03) + 0.8 * sum_pasmo(rng, n, 2000, 9000) * obalka(n, 0.0006, 0.003)) * obalka(n, 0.0008, 1.0)
    z = zap(rng, n, v) * obalka(n, 0.004, 0.035) * 0.45
    return cv + z


def glitch(rng, v=1.0):
    """Elektrický glitch „zap“: bzučení 180 Hz sekané na 8ms kousky s náhodnou výškou, bitcrush, 0,14 s."""
    n = int(0.14 * SR)
    t = cas(n)
    kus = int(0.008 * SR)
    f = np.repeat(rng.choice([180, 360, 720, 1440], size=n // kus + 1) * v, kus)[:n]
    x = np.sign(np.sin(2 * np.pi * np.cumsum(f) / SR)) * (rng.random(n // kus + 1).repeat(kus)[:n] > 0.25)
    x = np.round(pasmo(x, 150, 8000) * 2.5) / 2.5
    return x * spicka(n, 0.006, 0.002, 0.05)


def svetelny_uder(rng, v=1.0):
    """Drop 2 „hvězda ze světla“: elektrický třesk (šum + praskání výboje) + hluboký dopad 120 → 60 Hz s harmonickými
    (telefon slyší 2.–4. harmonickou) + třpytivý dozvuk (FM ~4 kHz, 0,6 s)."""
    n = int(1.2 * SR)
    t = cas(n)
    tresk = sum_pasmo(rng, n, 600, 11000) * obalka(n, 0.0015, 0.035)
    vyboj = zrna(rng, n, 2500, 0.0006, 2000, 10000) * obalka(n, 0.002, 0.08)
    vyboj = vyboj / (np.max(np.abs(vyboj)) + 1e-12)
    dopad_ = sum(ton(k * 120 * v, k * 60 * v, n, 0.06) / k ** 0.7 for k in (1, 2, 3, 4)) * obalka(n, 0.003, 0.2)
    dopad_ = np.tanh(1.5 * dopad_) / np.tanh(1.5)
    trpyt = np.sin(2 * np.pi * 4100 * v * t + 2 * np.sin(2 * np.pi * 5800 * v * t)) * obalka(n, 0.01, 0.25) * 0.18
    return tresk + 0.5 * vyboj + 0.9 * dopad_ + trpyt


def sssink(rng, v=1.0):
    """Běh světla „šššink“: jasný šum 5–11 kHz + třpyt (3 vysoké tóny), roste 80 ms a doznívá."""
    n = int(0.35 * SR)
    t = cas(n)
    tony = sum(np.sin(2 * np.pi * f * v * t) for f in (4200, 5300, 6650)) / 3
    return (0.7 * sum_pasmo(rng, n, 5000 * v, 11000) + 0.5 * tony) * spicka(n, 0.08, 0.018, 0.07)


def vuff(rng, v=1.0):
    """Vlna zaplavení „vuff“: hluboký závan 150–900 Hz + měkký tón 150 → 100 Hz, vrchol po 80 ms."""
    n = int(0.45 * SR)
    s = sum_pasmo(rng, n, 150 * v, 900 * v) + 0.4 * ton(150 * v, 100 * v, n, 0.1)
    return s * spicka(n, 0.08, 0.035, 0.1)


def klap_kov(rng, v=1.0):
    """Kovový „klap“ (odkrytí výsečí, zámek): dva kovové údery 9 ms po sobě, druhý (hlavní) silnější, + tělo 300 Hz."""
    n = int(0.2 * SR)
    a = kov(rng, n, 950 * v, 0.03, (1.0, 2.7, 5.1)) * obalka(n, 0.0008, 1.0)
    a += 0.6 * ton(320 * v, 260 * v, n, 0.02) * obalka(n, 0.002, 0.03) + 0.6 * sum_pasmo(rng, n, 2000, 9000) * obalka(n, 0.0006, 0.003)
    k = int(0.009 * SR)
    return vrstva_v(0.45 * a, a[:n - k], k)


def fump(rng, v=1.0):
    """Průlet portálem „fump“: tupý závan 200–1 200 Hz + tón 180 → 120 Hz, vrchol po 15 ms."""
    n = int(0.3 * SR)
    return (sum_pasmo(rng, n, 200 * v, 1200 * v) + 0.6 * ton(180 * v, 120 * v, n, 0.04)) * spicka(n, 0.015, 0.006, 0.07)


def dopad_logo(rng, v=1.0):
    """Měkký kovový dopad loga + „cink“: tělo 165 → 110 Hz s harmonickými, zvonivý kov 1,8 kHz (doznívá 0,8 s), jemný cvak."""
    n = int(1.2 * SR)
    telo = (ton(165 * v, 110 * v, n, 0.04) + 0.6 * ton(330 * v, 220 * v, n, 0.04) + 0.35 * ton(495 * v, 330 * v, n, 0.04)) * obalka(n, 0.004, 0.11)
    zvon = kov(rng, n, 1800 * v, 0.45, (1.0, 2.76, 5.40)) * obalka(n, 0.002, 1.0) * 0.45
    return np.tanh(1.3 * telo) + zvon + 0.3 * sum_pasmo(rng, n, 2500, 9000) * obalka(n, 0.0008, 0.004)


def volnobeh(rng, v=1.0, delka=3.0):
    """PODKLAD (V002 kolo 2): volnoběh závodního V8, ~900 ot/min. Zážehy 60 Hz s nerovnoměrným „lope“ (klikový hřídel 15 Hz),
    harmonické do ~1,8 kHz, aby byl slyšet i z telefonu; pod 90 Hz oříznuto (sub ≤ 30 %). Náběh 40 ms, doběh 0,25 s."""
    n = int(delka * SR)
    t = cas(n)
    kolisani = 1 + 0.015 * dolni(rng.standard_normal(n), 4) / 0.05      # pomalé kolísání otáček (±1–2 %)
    f = 60 * v * kolisani
    x = motor_ton(f, rng, harm=30, hrubost=0.2)
    klika = 2 * np.pi * np.cumsum(f / 4) / SR
    lope = 1 + 0.35 * np.sin(klika) + 0.15 * np.sin(2 * klika + 1.3)    # nerovnoměrný chod (vačka)
    x = horni(x * lope, 90, 4)
    return x * np.clip(t / 0.04, 0, 1) * np.clip((delka - t) / 0.25, 0, 1) ** 1.5


PODKLADY = {"volnobeh": volnobeh}                                        # souvislé zvuky (od–do), vrchol se nezarovnává


ZVUKY = {
    "cvak": cvak, "cvak_suchy": lambda r, v: cvak(r, v, suchy=True), "klap": klap, "tuk": tuk, "glp": glp,
    "klouznuti": klouznuti, "posunuti": lambda r, v: klouznuti(r, 0.7 * v, 0.3), "sustnuti": sustnuti,
    "sustnuti_tiche": lambda r, v: sustnuti(r, 1.2 * v, 0.18), "plink": plink, "pumf": pumf, "tup": tup, "bum": bum,
    "tsk": tsk, "nuz": nuz, "krupnuti": krupnuti, "trhnuti": trhnuti, "pop": pop_papir, "zip": zip_, "sss": sss,
    "sk": sk, "dopad": dopad,
    # závodní (V002)
    "rele": rele, "ting": ting, "odpal": odpal, "doppler": doppler, "doppler_tichy": lambda r, v: doppler(r, v, 1.0, 250, 60, 8.0),
    "prujezd_gt": lambda r, v: doppler(r, v, 1.3, 175, 75, 4.0, 0.4, 400, 3500), "doppler_dvojity": doppler_dvojity,
    "prujezd_daleko": prujezd_daleko, "vzduch": vzduch, "svih": svih, "svih_rotace": lambda r, v: svih(r, v, 0.32, 0.5),
    "prulet": lambda r, v: svih(r, 0.85 * v, 0.4, 0.55), "nasati": nasati, "nasati_dlouhe": lambda r, v: nasati(r, v, 0.6),
    "pneu": pneu, "pneu_svist": lambda r, v: pneu(r, v, 0.26, 950), "kov_uder": kov_uder,
    "kov_uder_suchy": lambda r, v: kov_uder(r, v, 0.035), "cink_el": cink_el, "fup": fup, "brzdy": brzdy, "jiskry": jiskry,
    "skrt": lambda r, v: jiskry(r, v, 0.35), "zatah": zatah, "vzum": vzum, "vzum_trisk": lambda r, v: vzum(r, v, 1.4),
    "tik": tik, "radeni": radeni, "glitch": glitch, "svetelny_uder": svetelny_uder, "sssink": sssink, "vuff": vuff,
    "klap_kov": klap_kov, "fump": fump, "dopad_logo": dopad_logo,
}


# ---------- měření ----------
def k_vazeni(x):
    """K-vážení podle ITU-R BS.1770 (48 kHz): stejné ucho jako LUFS."""
    x = signal.lfilter([1.53512485958697, -2.69169618940638, 1.19839281085285], [1, -1.69065929318241, 0.73248077421585], x, axis=-1)
    return signal.lfilter([1, -2, 1], [1, -1.99004745483398, 0.99007225036621], x, axis=-1)


def hlasitost(xk, t, okno=0.4):
    """Okamžitá hlasitost (LUFS) K-váženého sterea v okně `okno` s se středem v čase t."""
    a, b = max(0, int((t - okno / 2) * SR)), int((t + okno / 2) * SR)
    ms = np.sum(np.mean(xk[:, a:b] ** 2, axis=1))
    return -0.691 + 10 * np.log10(ms + 1e-12)


def obalka_vrcholu(x):
    """Obálka pro hledání vrcholu: |analytický signál| vyhlazený 2 ms (u tónu nekolísá s periodou jako špička vzorku)."""
    if x.ndim > 1:
        x = x.sum(axis=0)
    e = np.abs(signal.hilbert(x))
    m = int(0.002 * SR)
    return np.convolve(e, np.ones(m) / m, mode="same")


def vrchol(x, od=0, do=None):
    """Index změřeného vrcholu v úseku od–do (vzorky)."""
    e = obalka_vrcholu(x[..., od:do])
    return od + int(np.argmax(e))


# ---------- skládání stopy ----------
SUMOVE = {"klouznuti", "posunuti", "sustnuti", "sustnuti_tiche", "sss", "sk", "tsk", "zip", "trhnuti"}   # plochý šumový vrchol


def akcent(x, rng, sila=1.2):
    """Krátký dotek (2 ms šumu 1–6 kHz) přesně ve vrcholu. Šumové zvuky (klouznutí, šustnutí) mají plochý vrchol a obálka
    RMS 2 ms ho pak najde kdekoli v rozmezí ±15 ms. S dotekem padne vrchol na stejné místo při každém způsobu měření.
    Tónové a měkké zvuky (tup, bum, glp) ho nedostanou: cvakl by v nich a zvedl špičku."""
    p = vrchol(x)
    m = int(0.002 * SR)
    if p - m < 0 or p + m > len(x):
        return x
    okno = np.hanning(2 * m)
    d = pasmo(rng.standard_normal(2 * m + 200), 1000, 6000)[100:-100] * okno
    uroven = obalka_vrcholu(x)[p]
    x = x.copy()
    x[p - m:p + m] += d / (np.sqrt(np.mean(d ** 2)) + 1e-12) * uroven * sila
    return x


# Hlasitost efektu se cílí v okně 100 ms (ucho sčítá krátké zvuky zhruba tak dlouho). V okně 400 ms (EBU momentary)
# by se 5ms cvaknutí „rozředilo“ a pro stejný údaj by muselo mít špičku nad hudbou. Kontrola se hlásí v obou oknech.
OKNO_CIL = 0.1
MAX_SPICKA = -6.0                                                       # dBFS: žádný efekt nesmí mít špičku nad touto mezí


def nasyceni(x, drive_db):
    """Měkké nasycení tanh (x normalizované na špičku 1): špičky se zakulatí, tělo zvuku zesílí o až `drive_db`."""
    g = 10 ** (drive_db / 20)
    return np.tanh(g * x) / np.tanh(g)


def automatika_hudby(n, useky):
    """Křivka zisku hudby (n vzorků) z úseků (od, do, dB, dolu_s, nahoru_s): kosinové rampy, kombinace minimem v dB."""
    t = cas(n)
    db = np.zeros(n)
    for od, do, zisk, dolu, nahoru in useky:
        k = np.zeros(n)                                                  # 0 = plná hudba, 1 = plné ztlumení
        k[(t >= od) & (t <= do)] = 1
        m = (t >= od - dolu) & (t < od)
        k[m] = 0.5 - 0.5 * np.cos(np.pi * (t[m] - (od - dolu)) / dolu)
        m = (t > do) & (t <= do + nahoru)
        k[m] = 0.5 + 0.5 * np.cos(np.pi * (t[m] - do) / nahoru)
        db = np.minimum(db, k * zisk)
    return 10 ** (db / 20)


def zisk_hudby(hudba, spec):
    """Obálka zisku hudby po bodech „T:DB,T:DB,…[@HZ]“ (dB lineárně mezi body, mimo body 0 dB). S @HZ jen pásmo nad HZ."""
    spec, _, hz = spec.partition("@")
    body = sorted(tuple(map(float, b.split(":"))) for b in spec.split(","))
    t = cas(hudba.shape[1])
    db = np.interp(t, [b[0] for b in body], [b[1] for b in body], left=0.0, right=0.0)
    g = 10 ** (db / 20)
    if not hz:
        return hudba * g
    nizke = signal.sosfiltfilt(signal.butter(4, float(hz) / (SR / 2), output="sos"), hudba, axis=1)   # nulová fáze
    return nizke + (hudba - nizke) * g


def stopa(udalosti, delka, hk=None):
    """Vyrobí stereo stopu SFX a seznam samostatně umístěných zvuků (mono, pro kontrolu vrcholů).
    Každý zvuk se posune tak, aby jeho změřený vrchol padl na `cas`. Hlasitost: `lu` = o kolik LU je efekt tišší než hudba
    v okně OKNO_CIL (potřebuje K-váženou hudbu `hk`), jinak `uroven` = špička v dBFS. Do `uroven` se zapíše výsledná špička."""
    n = int(round(delka * SR))
    out = np.zeros((2, n))
    samotne = []
    for u in udalosti:
        rng = np.random.default_rng(u.get("seed", int(u["cas"] * 1000)))
        if u["typ"] in PODKLADY:                                         # podklad: od `cas` do `do`, hlasitost proti hudbě v celém úseku
            i, k = int(round(u["cas"] * SR)), int(round((u["do"] - u["cas"]) * SR))
            x = PODKLADY[u["typ"]](rng, u.get("ton", 1.0), k / SR)
            x = x / (np.max(np.abs(x)) + 1e-12)
            uhel = (u.get("pan", 0.0) + 1) * np.pi / 4
            st = np.zeros((2, n))
            st[:, i:i + k] = np.stack([x * np.cos(uhel), x * np.sin(uhel)]) * np.sqrt(2)
            stred, okno = (u["cas"] + u["do"]) / 2, u["do"] - u["cas"]
            zisk = 10 ** ((hlasitost(hk, stred, okno) + u["lu"] - hlasitost(k_vazeni(st), stred, okno)) / 20)
            zisk = min(zisk, 10 ** (u.get("strop", MAX_SPICKA) / 20) / np.max(np.abs(st)))
            u["uroven"] = round(20 * np.log10(zisk * np.max(np.abs(st))), 1)
            out += st * zisk
            samotne.append(None)
            u["vrchol_samotny"] = u["cas"]
            continue
        x = horni(ZVUKY[u["typ"]](rng, u.get("ton", 1.0)), 60)
        if u["typ"] in SUMOVE:
            x = akcent(x, rng)
        x = x / (np.max(np.abs(x)) + 1e-12)
        if u.get("drive"):
            x = nasyceni(x, u["drive"])
        vx = vrchol(x)
        i = int(round(u["cas"] * SR)) - vx
        if i < 0:                                                        # zvuk by začal před 0 s: uříznout začátek
            x, i, vx = x[-i:], 0, vx + i
        k = min(len(x), n - i)
        uhel = (u.get("pan", 0.0) + 1) * np.pi / 4
        if "pan_do" in u:                                                # průjezd: panorama se přelije z `pan` do `pan_do` kolem vrcholu
            tt = (np.arange(k) - vx) / SR
            p = u.get("pan", 0.0) + (u["pan_do"] - u.get("pan", 0.0)) * (0.5 + 0.5 * np.tanh(tt / u.get("pan_tau", 0.12)))
            uhel = (p + 1) * np.pi / 4
        st = np.zeros((2, n))
        st[:, i:i + k] = np.stack([x[:k] * np.cos(uhel), x[:k] * np.sin(uhel)]) * np.sqrt(2)
        if "lu" in u and hk is not None:
            zisk = 10 ** ((hlasitost(hk, u["cas"], OKNO_CIL) + u["lu"] - hlasitost(k_vazeni(st), u["cas"], OKNO_CIL)) / 20)
            zisk = min(zisk, 10 ** (u.get("strop", MAX_SPICKA) / 20) / np.max(np.abs(st)))
        else:
            zisk = 10 ** (u["uroven"] / 20) / np.max(np.abs(st))
        u["uroven"] = round(20 * np.log10(zisk * np.max(np.abs(st))), 1)
        out += st * zisk
        mono = np.zeros(n)
        mono[i:i + k] = x[:k] * zisk
        samotne.append(mono)
        u["vrchol_samotny"] = round(vrchol(mono, i, i + k) / SR, 4)
    return out, samotne


def zapis_wav(cesta, x, af=None):
    """Stereo float → WAV 48 kHz 24 bit (přes ffmpeg, ať se nic neořízne na 16 bitech), volitelně přes filtr `af`."""
    tmp = Path(str(cesta) + ".f32.wav")
    wavfile.write(tmp, SR, x.T.astype(np.float32))
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp)] + (["-af", af] if af else []) + ["-c:a", "pcm_s24le", str(cesta)],
                   check=True)
    tmp.unlink()


def saturace(mix, od, do, koleno_db, strop_db=-1.5, nabeh=0.02):
    """Měkké nasycení špiček mixu v úseku od–do: pod kolenem beze změny, nad ním tanh ke stropu. 4× převzorkování, bez posunu."""
    a, b = max(0, int((od - nabeh) * SR)), min(mix.shape[1], int((do + nabeh) * SR))
    L = 10 ** (strop_db / 20)
    k = L * 10 ** (-koleno_db / 20)
    x = signal.resample_poly(mix[:, a:b], 4, 1, axis=1)
    ax = np.abs(x)
    y = np.where(ax > k, np.sign(x) * (k + (L - k) * np.tanh((ax - k) / (L - k))), x)
    y = signal.resample_poly(y, 1, 4, axis=1)[:, :b - a]
    t = cas(b - a) + a / SR
    w = np.clip(np.minimum((t - (od - nabeh)) / nabeh, ((do + nabeh) - t) / nabeh), 0, 1)
    w = 0.5 - 0.5 * np.cos(np.pi * w)                                   # kosinový náběh a doběh
    out = mix.copy()
    out[:, a:b] = mix[:, a:b] * (1 - w) + y * w
    return out


def limiter_af(strop_db):
    """Sběrnicový limiter mixu: 192 kHz (mezivzorkové špičky), rychlý náběh na transienty efektů, `latency=1` (bez posunu, C025)."""
    return (f"aresample=192000,alimiter=limit={10 ** (strop_db / 20):.4f}:attack=1:release=80:level=false:latency=1,"
            "aresample=48000")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--udalosti", required=True)
    ap.add_argument("--delka", type=float, required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--hudba")
    ap.add_argument("--mix")
    ap.add_argument("--bez-hudby")
    ap.add_argument("--ticho", action="append", default=[], help="úsek od-do (s), kde nesmí znít žádný efekt")
    ap.add_argument("--automatika", action="append", default=[], help="OD-DO:DB[:DOLU_MS[:NAHORU_MS]] ztlumení hudby v mixu")
    ap.add_argument("--zisk-hudby", action="append", default=[], help="T:DB,T:DB,…[@HZ] obálka zisku hudby v mixu (viz docstring)")
    ap.add_argument("--saturace", action="append", default=[], help="OD-DO:KOLENO_DB měkké nasycení špiček mixu v úseku")
    ap.add_argument("--limiter", type=float, help="strop mixu v dBFS (např. -1.5): místo lineárního ztlumení celého mixu jemný "
                    "limiter jen na špičkách, kde se efekt sečte s úderem hudby (hudba s malou rezervou, V002)")
    a = ap.parse_args()
    udalosti = sorted(json.loads(Path(a.udalosti).read_text()), key=lambda u: u["cas"])
    n = int(round(a.delka * SR))
    hudba = hk = None
    if a.hudba:
        sr, h = wavfile.read(a.hudba)
        h = h.T.astype(float) / (32768.0 if h.dtype == np.int16 else 1.0)
        assert sr == SR and h.shape[0] == 2, f"{a.hudba}: čekám 48 kHz stereo"
        hudba = np.zeros((2, n))
        hudba[:, :min(h.shape[1], n)] = h[:, :n]
        for spec in a.zisk_hudby:
            hudba = zisk_hudby(hudba, spec)
        useky = []
        for spec in a.automatika:
            casti = spec.split(":")
            od, do = map(float, casti[0].split("-"))
            dolu = float(casti[2]) / 1000 if len(casti) > 2 else 0.02
            nahoru = float(casti[3]) / 1000 if len(casti) > 3 else 0.01
            useky.append((od, do, float(casti[1]), dolu, nahoru))
        if useky:
            hudba *= automatika_hudby(n, useky)
        hk = k_vazeni(hudba)
    sfx, samotne = stopa(udalosti, a.delka, hk)
    zapis_wav(a.out, sfx)
    sk_ = k_vazeni(sfx)

    # Vrchol v hotové stopě (všechny efekty dohromady) má smysl jen tam, kde zvuk v okně ±30 ms převládá.
    # Kde ho překryje delší soused (pesto po „pumf“, popy po křupnutí), platí vrchol samotného zvuku a `prekryto`.
    problemy = []
    ob_stopy = obalka_vrcholu(np.sum([m for m in samotne if m is not None], axis=0))   # mono součet bez podkladů
    for u, mono in zip(udalosti, samotne):
        if mono is None:                                                 # podklad: žádný vrchol, hlasitost v celém úseku od–do
            stred, okno = (u["cas"] + u["do"]) / 2, u["do"] - u["cas"]
            u.update(prekryto=False, vrchol_ve_stope=u["cas"], odchylka_ms=0.0, odchylka_ve_stope_ms=0.0,
                     lufs_400ms=round(hlasitost(sk_, stred, okno), 1))
            if hk is not None:
                u["hudba_lufs_400ms"] = round(hlasitost(hk, stred, okno), 1)
                u["efekt_proti_hudbe_lu"] = round(u["lufs_400ms"] - u["hudba_lufs_400ms"], 1)
                u["efekt_proti_hudbe_100ms_lu"] = u["efekt_proti_hudbe_lu"]
            continue
        c = int(round(u["cas"] * SR))
        sousede = [abs(v["cas"] - u["cas"]) for v in udalosti if abs(v["cas"] - u["cas"]) > 1e-6 and v["typ"] not in PODKLADY]
        polo = int(min([0.03] + [d / 2 for d in sousede]) * SR)
        od, do = c - polo, c + polo
        ob = obalka_vrcholu(mono[od:do])
        u["prekryto"] = bool(ob.max() < 0.5 * ob_stopy[od:do].max())
        u["vrchol_ve_stope"] = round((od + int(np.argmax(ob_stopy[od:do]))) / SR, 4)
        u["odchylka_ms"] = round((u["vrchol_samotny"] - u["cas"]) * 1000, 2)
        u["odchylka_ve_stope_ms"] = round((u["vrchol_ve_stope"] - u["cas"]) * 1000, 2)
        u["lufs_400ms"] = round(hlasitost(sk_, u["cas"]), 1)
        if hk is not None:
            u["hudba_lufs_400ms"] = round(hlasitost(hk, u["cas"]), 1)
            u["efekt_proti_hudbe_lu"] = round(u["lufs_400ms"] - u["hudba_lufs_400ms"], 1)
            u["efekt_proti_hudbe_100ms_lu"] = round(hlasitost(sk_, u["cas"], 0.1) - hlasitost(hk, u["cas"], 0.1), 1)
            if max(u["efekt_proti_hudbe_lu"], u["efekt_proti_hudbe_100ms_lu"]) > 0:
                problemy.append(f"{u['cas']} {u['typ']}: efekty jsou v tu chvíli hlasitější než hudba (I3: pod hudbou tiše)")
        if abs(u["odchylka_ms"]) > 5:
            problemy.append(f"{u['cas']} {u['typ']}: vrchol o {u['odchylka_ms']} ms mimo událost (tolerance ±5 ms)")
    for t in a.ticho:
        t0, t1 = map(float, t.split("-"))
        uroven = 20 * np.log10(np.max(np.abs(sfx[:, int(t0 * SR):int(t1 * SR)])) + 1e-12)
        print(f"ticho {t0}–{t1} s: špička SFX {uroven:.1f} dBFS")
        if uroven > -70:
            problemy.append(f"v tichu {t0}–{t1} s zní efekt ({uroven:.1f} dBFS)")

    souhrn = dict(delka=a.delka, pocet=len(udalosti),
                  max_odchylka_ms=max(abs(u["odchylka_ms"]) for u in udalosti),
                  max_odchylka_ve_stope_ms=max(abs(u["odchylka_ve_stope_ms"]) for u in udalosti if not u["prekryto"]),
                  prekryte=[u["cas"] for u in udalosti if u["prekryto"]],
                  spicka_sfx_dbfs=round(20 * np.log10(np.max(np.abs(sfx)) + 1e-12), 1), problemy=problemy,
                  automatika_hudby=a.automatika, zisk_hudby=a.zisk_hudby,
                  saturace=a.saturace)
    if hudba is not None:
        souhrn["nejhlasitejsi_efekt_proti_hudbe_lu"] = max(u["efekt_proti_hudbe_lu"] for u in udalosti)
        souhrn["nejhlasitejsi_efekt_proti_hudbe_100ms_lu"] = max(u["efekt_proti_hudbe_100ms_lu"] for u in udalosti)
        mix = hudba + sfx
        for spec in a.saturace:
            useky_, koleno = spec.split(":")
            od, do = map(float, useky_.split("-"))
            mix = saturace(mix, od, do, float(koleno), a.limiter if a.limiter is not None else -1.5)
        spicka = np.max(np.abs(mix))
        souhrn["spicka_mixu_dbfs"] = round(20 * np.log10(spicka + 1e-12), 1)
        rezerva = 10 ** (-1.5 / 20)                                       # jako hudba.py: špička vzorku ≤ −1,5 dBFS, true peak pak ≤ 0
        souhrn["zisk_mixu_db"] = round(min(0.0, 20 * np.log10(rezerva / spicka)), 2)   # hlasitost pak dorovná master_zvuk.sh
        af = None
        if a.limiter is not None:                                        # celý mix zůstane hlasitý, ubere se jen na špičkách
            souhrn["zisk_mixu_db"], af = 0.0, limiter_af(a.limiter)
        elif spicka > rezerva:
            mix *= rezerva / spicka
        if a.mix:
            zapis_wav(a.mix, mix, af)
            if af:
                _, lim = wavfile.read(a.mix)
                lim = lim.T.astype(float) / 2 ** 31
                m = int(0.005 * SR)
                e0, e1 = (np.sqrt(np.convolve(np.sum(y, axis=0) ** 2, np.ones(m) / m, mode="same")) for y in (mix, lim))
                gr = 20 * np.log10((e1 + 1e-9) / (e0 + 1e-9))
                gr[e0 < 1e-3] = 0
                souhrn["limiter"] = dict(strop_dbfs=a.limiter, max_ztlumeni_db=round(float(-gr.min()), 2),
                                         ms_nad_1db=round(float((gr < -1).sum() / SR * 1000), 1),
                                         spicka_po_dbfs=round(float(20 * np.log10(np.max(np.abs(lim)) + 1e-12)), 2))
        if a.bez_hudby:
            zapis_wav(a.bez_hudby, sfx)
    for u in udalosti:
        u.pop("_vrchol_zvuku_ms", None)
    Path(a.out).with_suffix(".json").write_text(json.dumps(dict(souhrn=souhrn, udalosti=udalosti), ensure_ascii=False, indent=1))
    for u in udalosti:
        print(f"{u['cas']:8.4f} {u['typ']:15s} vrchol {u['vrchol_samotny']:.4f} ({u['odchylka_ms']:+.1f} ms, ve stopě {u['odchylka_ve_stope_ms']:+.1f})"
              f"{' překryto' if u['prekryto'] else ''}  {u['uroven']:6} dBFS  proti hudbě {u.get('efekt_proti_hudbe_100ms_lu', '')} LU"
              f" (100 ms) / {u.get('efekt_proti_hudbe_lu', '')} LU (400 ms)")
    print(json.dumps(souhrn, ensure_ascii=False))
    for p in problemy:
        print("VAROVÁNÍ:", p)


if __name__ == "__main__":
    main()
