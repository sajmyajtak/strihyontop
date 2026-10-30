"""Zvukové efekty syntézou v kódu (naše vlastní, bez licencí, I5): papír, chleba, jemné kliky. Vrchol přesně na událost (I3).

Použití:
  python3 -I nastroje/sfx.py --udalosti udalosti.json --delka 25 --out sfx.wav
        [--hudba hudba.wav --mix zvuk.wav --bez-hudby zvuk_bez_hudby.wav] [--ticho 18.75-19.375]
udalosti.json: [{"cas": 0.625, "typ": "glp", "uroven": -26, "pan": 0.0, "popis": "…"}, …]
  cas     = kdy má padnout ZMĚŘENÝ vrchol (obálka RMS 2 ms), ne začátek zvuku
  uroven  = špička zvuku v dBFS (před mixem), pan −1 … 1, volitelně "ton" (násobek výšky) a "seed"
Výstup: sfx.wav (48 kHz stereo) + sfx.json (čas, typ, změřený vrchol samotného zvuku i v hotové stopě, odchylka v ms,
úroveň, hlasitost efektu proti hudbě v okně 400 ms). Typy zvuků: viz ZVUKY.
"""
import argparse
import json
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
    c = np.zeros(n)
    k = int(0.03 * SR)
    c[k:] = cvak(rng, 1.1, suchy=True)[: n - k] * 0.7
    return b + c


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


ZVUKY = {
    "cvak": cvak, "cvak_suchy": lambda r, v: cvak(r, v, suchy=True), "klap": klap, "tuk": tuk, "glp": glp,
    "klouznuti": klouznuti, "posunuti": lambda r, v: klouznuti(r, 0.7 * v, 0.3), "sustnuti": sustnuti,
    "sustnuti_tiche": lambda r, v: sustnuti(r, 1.2 * v, 0.18), "plink": plink, "pumf": pumf, "tup": tup, "bum": bum,
    "tsk": tsk, "nuz": nuz, "krupnuti": krupnuti, "trhnuti": trhnuti, "pop": pop_papir, "zip": zip_, "sss": sss,
    "sk": sk, "dopad": dopad,
}
