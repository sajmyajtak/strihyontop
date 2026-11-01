"""Generátor hudby do pozadí: syntéza v kódu, naše vlastní (bez licencí), přesně na doby pro animaci.

Použití:
  python3 -I nastroje/hudba.py --nalada vazna|drza|luxusni|pohodova|sportovni|luxsport --delka 20 --out hudba.wav
        [--bpm 120] [--drop 4.0] [--konec 17.5] [--seed 1] [--zlom 15.0 --drop2 18.75 (jen sportovni a luxsport)]
  --drop   čas nástupu plné části (zaokrouhlí se na celý takt), předtím úvod a stoupání
  --konec  čas finálního úderu (end card), zaokrouhlí se na dobu; potom už jen doznívá
  --zlom / --drop2  (sportovni) zlom = jen pad + filtr + průjezd motoru, poslední takt před drop2 = stoupání; v JSON i „zlom“, „stoupani“, „drop2“
                    (luxsport, V003) luxusní sportovní: zlom = klavír, Rhodes, smyčce, tlumený kopák; stoupání = riser, vír, nájezd
                    motoru s řazením; drop 2 = výkon (nejsilnější), konec = úder na logo a doznění
Výstup: WAV 48 kHz stereo, přibližně −13 až −14 LUFS (jednoprůchodový loudnorm; sportovni a luxsport lineárně: zisk na −14 LUFS + limiter
−1,5 dBFS s kompenzací zpoždění, aby zůstala stavba úvod < jízda < drop 2; přesnou hlasitost řeší nastroje/master_zvuk.sh)
pro synchronizaci animace (hudba.json vedle WAV). `udalosti_nastroju`: časy po swingu pro každý nástroj
(kopák, malý buben / tlesknutí, hi-hat, marimba s notou, kytara, basa, Rhodes…), `nastup` = skutečný začátek zvuku.
Bez `nastup` = posun zvuku je náhodný (±4 ms), bere se `cas`. Shaker, plochy a stoupání se nezapisují (nejsou to údery).
"""
import argparse
import json
import re
import subprocess
from pathlib import Path

import numpy as np
from scipy import signal

SR = 48000
rng = np.random.default_rng(1)


# ---------- základní stavebnice ----------
def cas(n):
    return np.arange(n) / SR


def mtof(m):
    return 440.0 * 2 ** ((m - 69) / 12)


def obalka(n, utok=0.005, doznivani=None, drzeni=None, uvolneni=0.08):
    """Náběh, exponenciální doznívání (None = drží), volitelně konec po `drzeni` s s uvolněním."""
    t = cas(n)
    e = np.clip(t / max(utok, 1e-4), 0, 1) ** 0.7
    if doznivani:
        e = e * np.exp(-np.maximum(t - utok, 0) / doznivani)
    if drzeni is not None:
        e = e * np.clip(1 - (t - drzeni) / uvolneni, 0, 1)
    return e


def filtr(x, druh, f, rad=2):
    f = np.clip(np.asarray(f, dtype=float) / (SR / 2), 1e-4, 0.99)
    sos = signal.butter(rad, f.tolist() if f.ndim else float(f), btype=druh, output="sos")
    return signal.sosfilt(sos, x, axis=-1)


def pila(f, n, faze0=0.0):
    """Pila s PolyBLEP (bez aliasingu i u vyšších tónů)."""
    dt = f / SR
    p = (faze0 + dt * np.arange(n)) % 1.0
    y = 2 * p - 1
    m = p < dt
    x = p[m] / dt
    y[m] -= x + x - x * x - 1
    m = p > 1 - dt
    x = (p[m] - 1) / dt
    y[m] -= x * x + x + x + 1
    return y


def sum_(n, sila=1.0):
    return rng.standard_normal(n) * sila


# ---------- bicí ----------
def kick(f0=110, f1=44, delka=0.5, ton=0.2, klik=0.25):
    n = int(delka * SR)
    t = cas(n)
    f = f1 + (f0 - f1) * np.exp(-t / 0.032)
    y = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / ton)
    k = filtr(sum_(n) * np.exp(-t / 0.0025), "highpass", 1800) * klik
    return np.tanh(1.6 * (y + k)) / np.tanh(1.6)


def snare(delka=0.35, ton=0.11, telo=200):
    n = int(delka * SR)
    t = cas(n)
    s = filtr(sum_(n), "bandpass", [900, 9000]) * np.exp(-t / ton)
    b = np.sin(2 * np.pi * telo * t) * np.exp(-t / 0.05) * 0.6
    return np.tanh(1.3 * (s + b))


def clap(delka=0.4):
    n = int(delka * SR)
    t = cas(n)
    e = np.zeros(n)
    for i, d in enumerate([0, 0.011, 0.022]):
        e += np.exp(-np.maximum(t - d, 0) / (0.006 if i < 2 else 0.09)) * (t >= d)
    return filtr(sum_(n), "bandpass", [800, 4500]) * e * 0.8


def hat(otevreny=False):
    n = int((0.3 if otevreny else 0.06) * SR)
    t = cas(n)
    return filtr(sum_(n), "highpass", 7000) * np.exp(-t / (0.11 if otevreny else 0.018)) * 0.5


def shaker():
    n = int(0.09 * SR)
    t = cas(n)
    return filtr(sum_(n), "bandpass", [4500, 11000]) * obalka(n, 0.012, 0.03) * 0.35


def snap():
    n = int(0.12 * SR)
    t = cas(n)
    return filtr(sum_(n), "bandpass", [1800, 6500]) * np.exp(-t / 0.012) + np.sin(2 * np.pi * 2200 * t) * np.exp(-t / 0.004) * 0.3


def taiko(f0=95, f1=58):
    n = int(1.1 * SR)
    t = cas(n)
    f = f1 + (f0 - f1) * np.exp(-t / 0.08)
    y = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.35)
    k = filtr(sum_(n), "lowpass", 900) * np.exp(-t / 0.05) * 0.5
    return np.tanh(1.4 * (y + k))


def cinel(delka=1.6, dozneni=0.55):
    """Jemný činel (crash) na drop a konec: jen vysoký šum s dlouhým dozněním, žádná rána."""
    n = int(delka * SR)
    t = cas(n)
    return filtr(sum_(n), "highpass", 5500) * np.exp(-t / dozneni) * obalka(n, 0.002) * 0.6


# ---------- nástroje ----------
def sub(m, dur, vel=1.0):
    n = int((dur + 0.15) * SR)
    t = cas(n)
    f = mtof(m)
    # 2. a 3. harmonická + saturace: basa je slyšet i z telefonu, který pod ~100 Hz nehraje
    y = np.sin(2 * np.pi * f * t) + 0.4 * np.sin(4 * np.pi * f * t) + 0.22 * np.sin(6 * np.pi * f * t)
    return np.tanh(2.0 * y * obalka(n, 0.006, None, dur, 0.12)) / np.tanh(2.0) * vel


def basa_pluck(m, dur, vel=1.0, jas=2600):
    n = int((dur + 0.1) * SR)
    t = cas(n)
    f = mtof(m)
    s = pila(f, n, rng.random()) * 0.6 + np.sin(2 * np.pi * f * t) * 0.6
    tmavy, svetly = filtr(s, "lowpass", 350), filtr(s, "lowpass", jas)
    e = np.exp(-t / 0.07)
    return np.tanh(1.5 * (tmavy + (svetly - tmavy) * e)) * obalka(n, 0.003, 0.35, dur, 0.06) * vel


def ostinato(m, dur, vel=1.0):
    """Smyčcové spiccato: krátká pila, filtr se otevře a zavře."""
    n = int((dur + 0.12) * SR)
    t = cas(n)
    f = mtof(m)
    s = sum(pila(f * 2 ** (d / 1200), n, rng.random()) for d in (-7, 0, 7)) / 3
    tmavy, svetly = filtr(s, "lowpass", 500), filtr(s, "lowpass", 2400)
    e = np.exp(-t / 0.06)
    return (tmavy + (svetly - tmavy) * e) * obalka(n, 0.004, 0.16, dur, 0.06) * vel


def plocha(noty, dur, jas=1800, vel=1.0, utok=0.6):
    """Pad: rozladěné pily, každý kanál jiné fáze = šířka. Vrací stereo."""
    n = int((dur + 1.2) * SR)
    out = np.zeros((2, n))
    for ch in range(2):
        s = np.zeros(n)
        for m in noty:
            for d in (-11, -4, 3, 10):
                s += pila(mtof(m) * 2 ** ((d + rng.normal(0, 1.5)) / 1200), n, rng.random())
        out[ch] = filtr(s / (len(noty) * 4), "lowpass", jas, 2)
    return out * obalka(n, utok, None, dur, 1.0) * vel


def rhodes(m, dur, vel=0.8, jas=1.0):
    """Elektrické piano FM syntézou (nosná 1:1, zvonivý „tine“ 14:1). `jas` > 1 = víc harmonických a déle (výchozí 1 = původní zvuk)."""
    f = mtof(m)
    n = int((dur + 1.5) * SR)
    t = cas(n)
    index = (0.8 + 1.6 * vel) * jas * np.exp(-t / (0.45 * jas))
    y = np.sin(2 * np.pi * f * t + index * np.sin(2 * np.pi * f * t))
    if f * 14 < SR / 2.2:
        y += np.sin(2 * np.pi * f * 14 * t) * np.exp(-t / 0.025) * 0.18 * vel * jas
    return y * obalka(n, 0.003, 2.2, dur, 0.45) * vel


def klavir(m, dur, vel=0.8):
    """Klavír aditivně: lehce neharmonické alikvoty, vyšší doznívají rychleji."""
    f = mtof(m)
    n = int((dur + 2.5) * SR)
    t = cas(n)
    y = np.zeros(n)
    for k in range(1, 11):
        fk = k * f * np.sqrt(1 + 0.00035 * k * k)
        if fk > SR / 2.3:
            break
        y += np.sin(2 * np.pi * fk * t + rng.random() * 6.28) * (1 / k ** 1.35) * np.exp(-t * (0.5 + 0.38 * k))
    y += filtr(sum_(n) * np.exp(-t / 0.004), "bandpass", [1000, 5000]) * 0.05
    return y * obalka(n, 0.002, None, dur + 1.6, 0.6) * vel


def pizz(m, vel=0.8, dozneni=0.994):
    """Drnknutí Karplus-Strong (rychle přes lfilter)."""
    f = mtof(m)
    N = int(SR / f)
    n = int(0.9 * SR)
    x = np.zeros(n)
    x[:N] = filtr(rng.uniform(-1, 1, N), "lowpass", 4000, 1)
    a = np.zeros(N + 2)
    a[0], a[N], a[N + 1] = 1, -0.5 * dozneni, -0.5 * dozneni
    y = signal.lfilter([1], a, x)
    return y / (np.max(np.abs(y)) + 1e-9) * vel * obalka(n, 0.001, 0.35)


def marimba(m, vel=0.8):
    """Marimba (palička na dřevěném kameni): základ + alikvot ~4× (kámen je laděný na dvě oktávy výš)
    + slabý ~10×, vyšší alikvoty doznějí rychleji, krátký měkký úder paličky."""
    f = mtof(m)
    n = int(1.3 * SR)
    t = cas(n)
    dozneni = 0.5 * (440 / f) ** 0.4                                     # nižší kameny znějí déle
    y = np.sin(2 * np.pi * f * t) * np.exp(-t / dozneni)
    if f * 4 < SR / 2.2:
        y += 0.45 * np.sin(2 * np.pi * f * 3.98 * t) * np.exp(-t / (dozneni * 0.22))
    if f * 10 < SR / 2.2:
        y += 0.05 * np.sin(2 * np.pi * f * 9.9 * t) * np.exp(-t / 0.025)
    y += filtr(sum_(n) * np.exp(-t / 0.0015), "bandpass", [700, 3500]) * 0.1
    return y * obalka(n, 0.0015) * vel


def basa_prsty(m, dur, vel=1.0):
    """Prstová basa: kulatý základ + 2.–4. harmonická, které po brnknutí rychle ztmavnou.
    Harmonické nesou basu i z telefonu, který pod ~100 Hz nehraje (I7)."""
    f = mtof(m)
    n = int((dur + 0.12) * SR)
    t = cas(n)
    jas = np.exp(-t / 0.09)
    y = (np.sin(2 * np.pi * f * t) + (0.45 + 0.35 * jas) * np.sin(4 * np.pi * f * t)
         + (0.18 + 0.3 * jas) * np.sin(6 * np.pi * f * t) + 0.12 * jas * np.sin(8 * np.pi * f * t))
    return np.tanh(1.4 * y * obalka(n, 0.008, 0.9, dur, 0.07)) / np.tanh(1.4) * vel


def kytara(noty, vel=0.7, tlumena=True):
    """Brnknutí akordu na kytaru (Karplus-Strong), struny po 12 ms; tlumená = krátký „chop“ na dobu."""
    out = np.zeros(int(1.0 * SR))
    for i, m in enumerate(noty):
        s = pizz(m, vel * (0.85 + 0.15 * rng.random()), 0.982 if tlumena else 0.996)
        if tlumena:
            s = s * np.exp(-cas(len(s)) / 0.07)
        k = int(i * 0.012 * SR)
        d = min(len(s), len(out) - k)
        out[k:k + d] += s[:d]
    return filtr(out, "highpass", 180) / np.sqrt(max(1, len(noty)))


def pop(f0=500, f1=1400, delka=0.12):
    n = int(delka * SR)
    t = cas(n)
    f = f0 * (f1 / f0) ** (t / delka)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.05) * 0.5


def stoupani(delka, jas=1.0):
    """Riser: šum, jehož pásmo stoupá, a tón stoupající o oktávu; hlasitost roste."""
    n = int(delka * SR)
    t = cas(n) / delka
    s = sum_(n)
    pasma = [300, 600, 1200, 2400, 4800, 9000]
    y = np.zeros(n)
    for i, fc in enumerate(pasma):
        w = np.exp(-((t * (len(pasma) - 1) - i) ** 2) / 0.8)
        y += filtr(s, "bandpass", [fc / 1.5, min(fc * 1.5, 20000)]) * w
    ton = np.sin(2 * np.pi * np.cumsum(220 * 2 ** (t * 1.5)) / SR) * 0.25
    return (y * 0.6 + ton * jas) * t ** 2.2


def reverse_cinel(delka):
    n = int(delka * SR)
    t = cas(n) / delka
    return filtr(sum_(n), "highpass", 5000) * t ** 3.5 * 0.7


def uder(jemny=False):
    """Impact na drop / end card: hluboký pokles + (u nejemného) šumová rána."""
    n = int(2.4 * SR)
    t = cas(n)
    f = 28 + 52 * np.exp(-t / 0.25)
    y = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.9)
    if not jemny:
        y += filtr(sum_(n), "lowpass", 2500) * np.exp(-t / 0.18) * 0.6
    return np.tanh(1.5 * y)


# ---------- sportovní nálada (racing / driving electro) ----------
def filtr_prubeh(x, f_od, f_do, druh="lowpass", blok=256):
    """Filtr s mezním kmitočtem, který se plynule (exponenciálně) mění od f_od do f_do po celé délce x (mono i stereo)."""
    n = x.shape[-1]
    out = np.zeros_like(x)
    zi = None
    for i in range(0, n, blok):
        fc = f_od * (f_do / f_od) ** (i / max(n, 1))
        sos = signal.butter(2, min(fc / (SR / 2), 0.99), btype=druh, output="sos")
        if zi is None:
            zi = np.zeros((sos.shape[0],) + x.shape[:-1] + (2,))
        out[..., i:i + blok], zi = signal.sosfilt(sos, x[..., i:i + blok], axis=-1, zi=zi)
    return out


def kick_tvrdy(vel=1.0):
    """Tvrdý kopák: rychlý pokles 180 → 52 Hz, krátké tělo, výrazný klik, saturace (harmonické 150–300 Hz nesou kopák i z telefonu)."""
    n = int(0.38 * SR)
    t = cas(n)
    f = 52 + 130 * np.exp(-t / 0.022)
    y = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.1)
    k = filtr(sum_(n) * np.exp(-t / 0.003), "bandpass", [1500, 8000]) * 0.55
    return np.tanh(2.4 * (y + k)) / np.tanh(2.4) * obalka(n, 0.0005) * vel


def basa_dist(m, dur, vel=1.0, jas=1800):
    """Distorzovaná pulzující basa: dvě rozladěné pily + sinus, filtr se při úderu otevře, silná saturace (harmonické do středů)."""
    f = mtof(m)
    n = int((dur + 0.04) * SR)
    t = cas(n)
    s = pila(f, n, rng.random()) * 0.6 + pila(f * 2 ** (11 / 1200), n, rng.random()) * 0.45 + np.sin(2 * np.pi * f * t) * 0.9
    tmavy, svetly = filtr(s, "lowpass", 260), filtr(s, "lowpass", jas)
    y = np.tanh(3.0 * (tmavy + (svetly - tmavy) * np.exp(-t / 0.05)))
    return filtr(y, "lowpass", 5000) * obalka(n, 0.002, None, dur, 0.025) * vel


def arp_synth(m, dur, vel=1.0, jas=3500):
    """Pluck arpeggia: dvě rozladěné pily a pulz o oktávu výš, filtr se po úderu rychle zavře. `jas` = nejvyšší otevření filtru."""
    f = mtof(m)
    n = int((dur + 0.08) * SR)
    t = cas(n)
    s = pila(f * 2 ** (-6 / 1200), n, rng.random()) * 0.5 + pila(f * 2 ** (6 / 1200), n, rng.random()) * 0.5
    s += np.sign(np.sin(2 * np.pi * 2 * f * t)) * 0.18
    tmavy, svetly = filtr(s, "lowpass", min(jas, 600)), filtr(s, "lowpass", jas)
    return (tmavy + (svetly - tmavy) * np.exp(-t / 0.045)) * obalka(n, 0.002, 0.18, dur, 0.04) * vel


def supersaw(noty, dur, vel=1.0, jas=4500, utok=0.003):
    """Akordový „stab“ ze sedmi rozladěných pil na tón (široký trance / racing zvuk). Vrací stereo."""
    n = int((dur + 0.12) * SR)
    out = np.zeros((2, n))
    for ch in range(2):
        s = np.zeros(n)
        for m in noty:
            for d in (-24, -15, -7, 0, 7, 15, 24):
                s += pila(mtof(m) * 2 ** ((d + rng.normal(0, 2)) / 1200), n, rng.random())
        out[ch] = filtr(s / (len(noty) * 7) * 2.2, "lowpass", jas, 2)
    return out * obalka(n, utok, None, dur, 0.1) * vel


def impact(sila=1.0):
    """Úder na drop / end card: boom s poklesem 135 → 45 Hz, tělo jako tom (230 → 110 Hz) a šumová rána ve středech, krátký závoj výšek."""
    n = int(2.0 * SR)
    t = cas(n)
    boom = np.sin(2 * np.pi * np.cumsum(45 + 90 * np.exp(-t / 0.07)) / SR) * np.exp(-t / 0.4)
    telo = np.sin(2 * np.pi * np.cumsum(110 + 120 * np.exp(-t / 0.03)) / SR) * np.exp(-t / 0.14) * 0.7
    rana = filtr(sum_(n), "bandpass", [300, 6000]) * np.exp(-t / 0.09) * 0.8
    zavoj = filtr(sum_(n), "highpass", 3500) * np.exp(-t / 0.7) * 0.12
    return np.tanh(1.8 * (boom + telo + rana + zavoj)) * obalka(n, 0.0008) * sila


def motor(body, delka, pan_od=0.0, pan_do=0.0, hlasitost=None):
    """Syntetický motor (zvukový motiv): základní tón otáček s harmonickými, chrapot zapalování a sání.
    `body` = [(čas od začátku, Hz), …]: mezi body glissando (exponenciálně), dva body se stejným časem = skok (řazení).
    `hlasitost` = [(čas, 0–1), …] obálka (výchozí: plynule roste). Pan se posouvá od pan_od do pan_do (průjezd). Vrací stereo."""
    n = int(delka * SR)
    t = cas(n)
    tb = np.array([b[0] for b in body])
    fb = np.log(np.array([b[1] for b in body], dtype=float))
    f = np.exp(np.interp(t, tb + np.arange(len(tb)) * 1e-6, fb))     # stejný čas = skok
    faze = 2 * np.pi * np.cumsum(f) / SR
    y = np.zeros(n)
    for k in range(1, 18):
        a = (1 / k ** 0.9) * (1.25 if k in (2, 4) else 1.0)          # sudé harmonické = „V8“ barva
        y += np.where(k * f < SR / 2.3, a * np.sin(k * faze + k * 0.7), 0)
    y *= 1 + 0.35 * np.sin(faze / 2)                                  # chrapot zapalování (polovina otáček)
    y += filtr(sum_(n), "bandpass", [700, 3000]) * 0.25 * (f / f.max())  # sání a výfuk
    y = np.tanh(1.6 * filtr(y, "lowpass", 4500)) * 0.7
    if hlasitost is None:
        hlasitost = [(0, 0.15), (delka, 1.0)]
    e = np.interp(t, [h[0] for h in hlasitost], [h[1] for h in hlasitost]) * obalka(n, 0.02)
    uhel = (np.linspace(pan_od, pan_do, n) + 1) * np.pi / 4
    return np.stack([y * e * np.cos(uhel), y * e * np.sin(uhel)]) * np.sqrt(2)


# ---------- harmonie ----------
def basovy(m, nejniz=33):
    """Basový tón v rozsahu nejniz … nejniz+11 (výchozí A1–G#2, 55–104 Hz)."""
    while m < nejniz:
        m += 12
    while m >= nejniz + 12:
        m -= 12
    return m


NAZVY_NOT = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]     # Bb = české b (B♭)


def nota(m):
    return f"{NAZVY_NOT[m % 12]}{m // 12 - 1}"


def akord(koren, intervaly, stred=60):
    """Noty akordu poskládané kolem `stred` (nejbližší obraty = plynulé vedení hlasů)."""
    noty = []
    for i in intervaly:
        m = koren + i
        while m < stred - 6:
            m += 12
        while m > stred + 7:
            m -= 12
        noty.append(m)
    return sorted(noty)


NALADY = {
    # tónina a průběh: (kořen MIDI, intervaly)
    "vazna": dict(bpm=90, akordy=[(50, [0, 3, 7]), (46, [0, 4, 7]), (53, [0, 4, 7]), (48, [0, 4, 7])]),           # Dm Bb F C
    "drza": dict(bpm=116, akordy=[(53, [0, 4, 7]), (50, [0, 3, 7]), (46, [0, 4, 7]), (48, [0, 4, 7, 10])]),      # F Dm Bb C7
    "luxusni": dict(bpm=120, akordy=[(57, [0, 3, 7, 10, 14]), (53, [0, 4, 7, 11]), (50, [0, 3, 7, 10, 14]), (52, [0, 3, 7, 10])]),  # Am9 Fmaj7 Dm9 Em7
    # Chill feel-good (reklama na jídlo): F dur, I–vi–ii–V v barvách maj9/m7/m9/9, Rhodes bez kořene (kořen hraje basa).
    # Akordy se počítají OD DROPU: drop vždy přistane na tónice, takty před ním jsou obrat vi–ii–V (napětí → uvolnění).
    "pohodova": dict(bpm=96, tonina=5, akordy=[(53, [4, 7, 11, 14]), (50, [0, 3, 7, 10]), (55, [3, 7, 10, 14]), (48, [4, 7, 10, 14])]),  # Fmaj9 Dm7 Gm9 C9
    # Závodní driving electro (V002): a moll, i–VI–III–VII, počítáno OD DROPU (drop, zlom → drop 2 i konec přistanou na Am),
    # takty před dropem C–G = „nádech“ do toniky. Struktura: úvod, drop, plná jízda, zlom (pad + filtr + motor), stoupání, drop 2, finále.
    "sportovni": dict(bpm=128, akordy=[(57, [0, 3, 7]), (53, [0, 4, 7]), (48, [0, 4, 7]), (55, [0, 4, 7])]),  # Am F C G
    # Luxusní sportovní (V003, reklama na prémiový vůz): d moll, jízda i–VI–iv–III v barvách m9/maj9 (Dm9 Bbmaj9 Gm9 Fmaj9),
    # počítáno OD DROPU. Takt před dropem, dropem 2 a koncem = dominanta A7sus4 → A7(b9) (napětí → tónika). Zlom Fmaj9 Bbmaj9 (teplo).
    "luxsport": dict(bpm=120, akordy=[(50, [0, 3, 7, 10, 14]), (46, [0, 4, 7, 11, 14]), (43, [0, 3, 7, 10, 14]), (41, [0, 4, 7, 11, 14])]),
}

# Marimbový motiv nálady „pohodova“ pro každý akord: (doba v taktu, MIDI). Tři tóny po třech šestnáctinách (0; 0,75; 1,5 doby),
# pauza a dvě osminy jako předtakt do dalšího taktu. Těžké doby jen tóny akordu, stoupající rozklad (C–E–G, D–F–A, D–F–B, E–G–B)
# zní vesele a dá se zazpívat. (B = české b, tj. B♭.)
POHODA_MOTIV = [
    [(0, 72), (0.75, 76), (1.5, 79), (3.0, 77), (3.5, 76)],    # Fmaj9: C5 E5 G5 | F5 E5
    [(0, 74), (0.75, 77), (1.5, 81), (3.0, 79), (3.5, 77)],    # Dm7:   D5 F5 A5 | G5 F5
    [(0, 74), (0.75, 77), (1.5, 82), (3.0, 81), (3.5, 79)],    # Gm9:   D5 F5 B5 | A5 G5
    [(0, 76), (0.75, 79), (1.5, 82), (3.0, 81), (3.5, 79)],    # C9:    E5 G5 B5 | A5 G5
]
POHODA_OBRAT = [(0, 82), (0.75, 81), (1.5, 79), (2.0, 76), (2.75, 79)]     # poslední takt ii–V: B5 A5 G5 | E5 G5
POHODA_LOGO = [72, 77, 81]                                                 # zvukové logo na konec: C5 F5 A5 nahoru do toniky
JAS_RHODES = 1.5                                                           # Rhodes v pohodové náladě jasnější (harmonické 1–3 kHz)


# ---------- mix ----------
class Mix:
    def __init__(self, delka):
        self.n = int((delka + 4) * SR)
        self.busy = {}

    def pridej(self, bus, kdy, sig, hlasitost=1.0, pan=0.0):
        if bus not in self.busy:
            self.busy[bus] = np.zeros((2, self.n))
        if sig.ndim == 1:
            uhel = (pan + 1) * np.pi / 4
            sig = np.stack([sig * np.cos(uhel), sig * np.sin(uhel)]) * np.sqrt(2)
        i = int(round(kdy * SR))
        if i < 0:                       # náhodné posunutí těsně před začátek: uříznout
            sig, i = sig[:, -i:], 0
        if i >= self.n:
            return
        k = min(sig.shape[1], self.n - i)
        self.busy[bus][:, i:i + k] += sig[:, :k] * hlasitost


def dozvuk(x, rt60=2.0, predelay=0.02, tlumeni=6500):
    n = int(rt60 * SR)
    t = cas(n)
    ir = rng.standard_normal((2, n)) * np.exp(-6.9 * t / rt60)
    ir = filtr(ir, "lowpass", tlumeni, 1)
    ir[:, : int(predelay * SR)] = 0
    ir /= np.sqrt(np.sum(ir ** 2, axis=1, keepdims=True))
    return np.stack([signal.fftconvolve(x[c], ir[c])[: x.shape[1]] for c in range(2)])


def sidechain(n, kicky, hloubka=0.55, navrat=0.16):
    g = np.ones(n)
    t = cas(int(0.5 * SR))
    tvar = 1 - hloubka * np.exp(-t / navrat) * np.clip(t / 0.004, 0, 1) ** 0.5
    for k in kicky:
        i = int(k * SR)
        j = min(n, i + len(tvar))
        if i < n:
            g[i:j] = np.minimum(g[i:j], tvar[: j - i])
    return g


def autopan(n, f=4.5, hloubka=0.22):
    t = cas(n)
    return np.stack([1 + hloubka * np.sin(2 * np.pi * f * t), 1 - hloubka * np.sin(2 * np.pi * f * t)])


# ---------- aranžmá ----------
def aranzuj(nalada, delka, bpm, drop, konec):
    doba = 60 / bpm
    takt = 4 * doba
    drop = max(takt, round(drop / takt) * takt)
    konec = max(drop + takt, round(konec / doba) * doba)
    akordy = NALADY[nalada]["akordy"]
    mx = Mix(delka)
    kicky = []
    udalosti = [{"cas": round(drop, 4), "typ": "drop"}, {"cas": round(konec, 4), "typ": "konec"}]
    vel = lambda z=0.85: float(np.clip(rng.normal(z, 0.06), 0.4, 1))   # noqa: E731
    jit = lambda: rng.normal(0, 0.004)                                   # noqa: E731
    takt_dropu = int(round(drop / takt))
    ak_od_dropu = lambda b: (b - takt_dropu) % len(akordy)              # noqa: E731  index akordu počítaný od dropu (pohodova)
    stupnice = {(NALADY[nalada].get("tonina", 0) + i) % 12 for i in (0, 2, 4, 5, 7, 9, 11)}   # durová stupnice tóniny
    hraje = []

    def zapis(nastroj, kdy, nastup=None, **info):
        """Událost nástroje pro animaci a SFX: `kdy` = čas po swingu (na mřížce), `nastup` = skutečný začátek zvuku (+ posun, rozptyl)."""
        u = dict(cas=round(kdy, 5), **info)
        if nastup is not None:
            u["nastup"] = round(nastup, 5)
        hraje.append((nastroj, u))

    def akord_v(t, stred=60):
        k, iv = akordy[int(t // takt) % len(akordy)]
        return k, akord(k, iv, stred)

    pocet_taktu = int(np.ceil(konec / takt))
    for b in range(pocet_taktu):
        t0 = b * takt
        hlavni = t0 >= drop - 1e-6
        posledni_pred = abs(t0 + takt - drop) < 1e-6
        if t0 >= konec - 1e-6:
            break
        koren, noty = akord_v(t0)
        delka_taktu = min(takt, konec - t0)

        if nalada == "vazna":
            mx.pridej("harmonie", t0, plocha(noty + [noty[0] - 12], delka_taktu, 1500 if hlavni else 900, 0.55 if hlavni else 0.4))
            for i, d in enumerate([0, 1.5, 3]):                                      # klavírní motiv z tónů akordu
                m = (noty[-1] if i == 0 else noty[i % len(noty)]) + 12
                if t0 + d * doba < konec:
                    zapis("klavir", t0 + d * doba, nota=nota(m))
                    mx.pridej("melodie", t0 + d * doba + jit(), klavir(m, doba * 1.2, vel(0.7)), 0.5, pan=0.15 * (i - 1))
            for s in range(8):                                                     # ostinato osminy
                tt = t0 + s * doba / 2
                if tt < konec:
                    zapis("basa", tt, tt, nota=nota(basovy(koren, 38) + (12 if s % 2 else 0)))
                    mx.pridej("basa", tt, ostinato(basovy(koren, 38) + (12 if s % 2 else 0), doba / 2 * 0.8, vel(0.9 if hlavni else 0.5)), 0.55 if hlavni else 0.3)
            zapis("taiko", t0, t0)
            mx.pridej("bici", t0, taiko(), 0.5 if hlavni else 0.3)
            if hlavni:
                for d in (0, 2.5):
                    zapis("kopak", t0 + d * doba, t0 + d * doba)
                    mx.pridej("bici", t0 + d * doba, kick(90, 48, 0.5, 0.18, 0.15), 0.6)
                    kicky.append(t0 + d * doba)
                if t0 + 2 * doba < konec:
                    zapis("maly_buben_tlesknuti", t0 + 2 * doba, t0 + 2 * doba)
                    mx.pridej("bici", t0 + 2 * doba, snare(0.5, 0.16, 180), 0.6)
                    mx.pridej("fx", t0 + 2 * doba, snare(0.5, 0.16, 180), 0.35)
                for s in range(8):
                    if t0 + s * doba / 2 < konec:
                        zapis("hihat", t0 + s * doba / 2)
                        mx.pridej("bici", t0 + s * doba / 2 + jit(), hat(), 0.18 * vel(), pan=0.3)
            if posledni_pred:                                                      # vír na snare + stoupání
                for s in range(16):
                    mx.pridej("bici", t0 + s * doba / 4, snare(0.2, 0.05), 0.08 + 0.35 * (s / 15) ** 2)
                mx.pridej("fx", t0, stoupani(takt), 0.5)
                mx.pridej("fx", drop - doba, reverse_cinel(doba), 0.6)
                zapis("obraceny_cinel", drop - doba, drop - doba, vrchol=round(drop, 5))

        elif nalada == "drza":
            swing = lambda d: d + (0.08 if (d * 2) % 2 == 1 else 0)               # noqa: E731  lichá osmina o kousek později
            for i, d in enumerate([0, 0.75, 1.5, 2.5, 3.0]):
                tt = t0 + swing(d) * doba
                if tt < konec and not (posledni_pred and d >= 3):
                    zapis("pizzicato", tt, nota=nota(noty[i % len(noty)] + 12))
                    mx.pridej("melodie", tt + jit(), pizz(noty[i % len(noty)] + 12, vel(0.8)), 0.85, pan=(-0.3, 0.3)[i % 2])
            if not hlavni:
                for d in (1, 3):
                    if not (posledni_pred and d == 3):
                        zapis("lusknuti", t0 + d * doba, t0 + d * doba)
                        mx.pridej("bici", t0 + d * doba, snap(), 0.5, pan=0.2)
            else:
                for d in (0, 1.75, 2.0 + 0.5):
                    tt = t0 + d * doba
                    if tt < konec:
                        zapis("kopak", tt, tt)
                        mx.pridej("bici", tt, kick(120, 52, 0.35, 0.12, 0.35), 0.6)
                        kicky.append(tt)
                for d in (1, 3):
                    if t0 + d * doba < konec:
                        zapis("maly_buben_tlesknuti", t0 + d * doba, t0 + d * doba, jen_tlesknuti=True)
                        mx.pridej("bici", t0 + d * doba, clap(), 0.7)
                        mx.pridej("fx", t0 + d * doba, clap(), 0.25)
                for s in range(8):
                    tt = t0 + swing(s / 2) * doba
                    if tt < konec:
                        zapis("hihat", tt)
                        mx.pridej("bici", tt + jit(), hat(), (0.22 if s % 2 else 0.14) * vel(), pan=-0.25)
                for d, o in [(0, 0), (0.5, 12), (1.5, 0), (2.5, 7), (3.5, 12)]:
                    tt = t0 + swing(d) * doba
                    if tt < konec:
                        zapis("basa", tt, tt, nota=nota(basovy(koren, 36) + o))
                        mx.pridej("basa", tt, basa_pluck(basovy(koren, 36) + o, doba * 0.4, vel(0.9)), 0.6)
                if b % 2 == 0:
                    zapis("pop", t0 + 3.5 * doba, t0 + 3.5 * doba)
                    mx.pridej("melodie", t0 + 3.5 * doba, pop(), 0.35, pan=0.4)
                mx.pridej("harmonie", t0, plocha(noty, delka_taktu, 2600, 0.3, 0.2))   # výplň středů pod drnkáním
            if posledni_pred:                                                      # drzá pauza: poslední doba ticho, jen „pop“
                mx.pridej("fx", t0, stoupani(takt * 0.75, 0.6), 0.35)
                mx.pridej("melodie", drop - doba * 0.5, pop(700, 1800, 0.15), 0.5)
                zapis("pop", drop - doba * 0.5, drop - doba * 0.5)

        elif nalada == "luxusni":
            mx.pridej("harmonie", t0, plocha([m + 12 for m in noty[1:4]], delka_taktu, 3200, 0.22, 1.0))
            if not hlavni:
                zapis("rhodes", t0, akord=[nota(m) for m in noty])
                for m in noty:
                    mx.pridej("klavesy", t0 + jit(), rhodes(m, delka_taktu * 0.95, vel(0.6)), 0.45)
                for s in range(16):
                    if t0 + s * doba / 4 < konec:
                        mx.pridej("bici", t0 + s * doba / 4 + jit(), shaker(), 0.12 * (1.4 if s % 4 == 2 else 1) * vel(), pan=0.35)
            else:
                for d, dl in [(0, 1.4), (2.5, 0.9)]:                                # akord + synkopa
                    if t0 + d * doba < konec:
                        zapis("rhodes", t0 + d * doba, akord=[nota(m) for m in noty])
                        for m in noty:
                            mx.pridej("klavesy", t0 + d * doba + jit(), rhodes(m, dl * doba, vel(0.7)), 0.4)
                for d in range(4):
                    tt = t0 + d * doba
                    if tt < konec:
                        zapis("kopak", tt, tt)
                        mx.pridej("bici", tt, kick(85, 48, 0.4, 0.13, 0.18), 0.55)
                        kicky.append(tt)
                        zapis("hihat", tt + doba / 2, tt + doba / 2, otevreny=True)
                        mx.pridej("bici", tt + doba / 2, hat(True), 0.32 * vel(), pan=0.25)
                for d in (1, 3):
                    if t0 + d * doba < konec:
                        zapis("maly_buben_tlesknuti", t0 + d * doba, t0 + d * doba, jen_tlesknuti=True)
                        mx.pridej("bici", t0 + d * doba, clap(), 0.3)
                        mx.pridej("fx", t0 + d * doba, clap(), 0.3)
                for s in range(16):
                    if t0 + s * doba / 4 < konec:
                        mx.pridej("bici", t0 + s * doba / 4 + jit(), shaker(), 0.16 * (1.4 if s % 4 == 2 else 1) * vel(), pan=0.35)
                for d, dl, o in [(0, 1.2, 0), (1.75, 0.5, 0), (2.5, 0.9, 0), (3.5, 0.4, 12)]:
                    if t0 + d * doba < konec:
                        zapis("basa", t0 + d * doba, t0 + d * doba, nota=nota(basovy(koren) + o))
                        mx.pridej("basa", t0 + d * doba, sub(basovy(koren) + o, dl * doba, vel(0.9)), 0.6)
            if posledni_pred:
                mx.pridej("fx", drop - 2 * doba, reverse_cinel(2 * doba), 0.45)
                zapis("obraceny_cinel", drop - 2 * doba, drop - 2 * doba, vrchol=round(drop, 5))

        elif nalada == "pohodova":
            sw = lambda d: d + (0.06 if round(d * 4) % 2 == 1 else 0)          # noqa: E731  šestnáctinový swing: lichá šestnáctina o kousek později
            obrat = hlavni and t0 + takt >= konec - 1e-6                        # poslední takt před koncem: ii–V do toniky
            useky = [(0.0, 2.0, 2), (2.0, 2.0, 3)] if obrat else [(0.0, 4.0, ak_od_dropu(b))]   # (od doby, délka v dobách, index akordu)
            if not hlavni:
                # Úvod (v obraze „fine dining“): jen Rhodes, lusknutí a shaker, na každou změnu akordu jemné cinknutí marimby.
                # Poslední doba před dropem je nádech: ticho, jen stoupající šum a předtakt marimby do dropu.
                _, _, ia = useky[0]
                hlasy = akord(*akordy[ia], 62)
                for d, dd, v in ([(0, 1.75, 0.55), (2.0, 0.5, 0.45)] if posledni_pred else [(0, 1.75, 0.55), (2.5, 0.75, 0.45)]):
                    zapis("rhodes", t0 + sw(d) * doba, akord=[nota(m) for m in hlasy])
                    for m in hlasy:
                        mx.pridej("klavesy", t0 + sw(d) * doba + jit(), rhodes(m, dd * doba, vel(v), JAS_RHODES), 0.5)
                mx.pridej("harmonie", t0, plocha([m + 12 for m in hlasy[1:]], (2.75 if posledni_pred else 4.0) * doba, 2800, 0.16, 0.5))   # vzdušná plocha
                for d in (1, 3):
                    if not (posledni_pred and d == 3):
                        j = jit()
                        mx.pridej("bici", t0 + d * doba + j, snap(), 0.4, pan=0.2)
                        zapis("lusknuti", t0 + d * doba, t0 + d * doba + j)
                for s in range(12 if posledni_pred else 16):
                    mx.pridej("bici", t0 + sw(s / 4) * doba + jit(), shaker(), 0.13 * (1.5 if s % 2 else 1) * vel(), pan=-0.3)
                for d, m, v, h in [(0, hlasy[-1] + 12, 0.55, 0.45), (1.5, hlasy[1] + 12, 0.4, 0.4)]:
                    j = jit()
                    mx.pridej("melodie", t0 + sw(d) * doba + j, marimba(m, vel(v)), h, pan=-0.15)
                    zapis("marimba", t0 + sw(d) * doba, t0 + sw(d) * doba + j, nota=nota(m))
                if posledni_pred:
                    for d in (0, 2):                                            # jemný kopák ohlásí drop
                        mx.pridej("bici", t0 + d * doba, kick(95, 50, 0.45, 0.15, 0.12), 0.35)
                        zapis("kopak", t0 + d * doba, t0 + d * doba)
                    mx.pridej("fx", drop - 2 * doba, reverse_cinel(2 * doba), 0.32)
                    zapis("obraceny_cinel", drop - 2 * doba, drop - 2 * doba, vrchol=round(drop, 5))
                    for d, m in POHODA_MOTIV[3][3:]:                            # předtakt A5 G5 do prvního tónu dropu
                        j = jit()
                        mx.pridej("melodie", t0 + sw(d) * doba + j, marimba(m, vel(0.7)), 0.5, pan=-0.15)
                        zapis("marimba", t0 + sw(d) * doba, t0 + sw(d) * doba + j, nota=nota(m))
            else:
                if t0 < drop + 1e-6:
                    mx.pridej("bici", drop, cinel(), 0.22)                     # jemný činel na drop
                    zapis("cinel", drop, drop)
                # Bicí: kopák 1, „a“ po 1, 3&; malý buben + tleskání na 2 a 4 o kousek později (uvolněně); hi-hat šestnáctiny se swingem.
                for d in [0, 0.75, 2.5] + ([3.75] if b % 2 else []):
                    tt = t0 + sw(d) * doba
                    if tt < konec:
                        mx.pridej("bici", tt, kick(95, 50, 0.45, 0.15, 0.12), 0.55)
                        kicky.append(tt)
                        zapis("kopak", tt, tt)
                for d in (1, 3):
                    tt = t0 + d * doba
                    if tt < konec:
                        zapis("maly_buben_tlesknuti", tt, tt + 0.008)            # malý buben +8 ms, tlesknutí +12 ms
                        mx.pridej("bici", tt + 0.008, snare(0.3, 0.09, 190), 0.4)
                        mx.pridej("bici", tt + 0.012, clap(), 0.65)
                        mx.pridej("fx", tt + 0.012, clap(), 0.16)
                for s in range(16):
                    tt = t0 + sw(s / 4) * doba
                    if tt < konec:
                        j = jit()
                        mx.pridej("bici", tt + j, hat(), (0.36 if s % 4 == 2 else 0.24 if s % 2 == 0 else 0.15) * vel(), pan=0.25)
                        zapis("hihat", tt, tt + j)
                        mx.pridej("bici", tt + jit(), shaker(), 0.12 * vel(), pan=-0.35)
                if b % 2 == 1 and t0 + 3.5 * doba < konec:
                    mx.pridej("bici", t0 + 3.5 * doba, hat(True), 0.3, pan=0.25)
                    zapis("hihat", t0 + 3.5 * doba, t0 + 3.5 * doba, otevreny=True)
                for j, (od, dl, ia) in enumerate(useky):
                    k, iv = akordy[ia]
                    hlasy = akord(k, iv, 62)
                    posledni_usek = j == len(useky) - 1
                    mx.pridej("harmonie", t0 + od * doba, plocha([m + 12 for m in hlasy[1:]], dl * doba, 2800, 0.2, 0.3))
                    # Rhodes: synkopované údery (v obratu dva kratší).
                    vzor = [(0, 0.9, 0.7), (1.5, 0.4, 0.5), (2.5, 0.9, 0.65), (3.75, 0.2, 0.4)] if dl == 4 else [(0, 0.9, 0.7), (1.5, 0.4, 0.5)]
                    for d, dd, v in vzor:
                        tt = t0 + (od + sw(d)) * doba
                        if tt < konec:
                            zapis("rhodes", tt, akord=[nota(m) for m in hlasy])
                            for m in hlasy:
                                mx.pridej("klavesy", tt + jit(), rhodes(m, dd * doba, vel(v), JAS_RHODES), 0.45)
                    # Basa: kořen, „skok“, kvinta a přiblížení ke kořeni dalšího akordu (o tón shora nebo půltón zdola, ve stupnici).
                    kb = basovy(k, 36)
                    if posledni_usek:
                        if obrat:                                               # po obratu přijde tónika finále
                            dalsi = akordy[0][0]
                        elif t0 + 2 * takt >= konec - 1e-6:                     # další takt je obrat, začíná ii
                            dalsi = akordy[2][0]
                        else:
                            dalsi = akordy[ak_od_dropu(b + 1)][0]
                        nb = basovy(dalsi, 36)
                        pribl = nb - 1 if (nb - 1) % 12 in stupnice else nb + 2
                    if dl == 4:
                        tony = [(0, kb, 1.25), (1.75, kb, 0.25), (2.5, kb + 7, 0.75), (3.5, pribl, 0.45)]
                    else:
                        tony = [(0, kb, 1.0), (1.5, pribl if posledni_usek else kb + 7, 0.45)]
                    for d, m, dd in tony:
                        tt = t0 + (od + sw(d)) * doba
                        if tt < konec:
                            j = jit()
                            mx.pridej("basa", tt + j, basa_prsty(m, dd * doba, vel(0.9)), 0.6)
                            zapis("basa", tt, tt + j, nota=nota(m))
                # Kytara: tlumené brnknutí na 2& a 4& (vesele „poskakuje“).
                for d in (1.5, 3.5):
                    tt = t0 + d * doba
                    if tt < konec:
                        ia = useky[-1][2] if d >= useky[-1][0] else useky[0][2]
                        noty_k = [m + 12 for m in akord(*akordy[ia], 62)[1:]]
                        j = jit()
                        mx.pridej("kytara", tt + j, kytara(noty_k, vel(0.6)), 0.5, pan=0.35)
                        zapis("kytara", tt, tt + j, akord=[nota(m) for m in noty_k])
                # Marimba: motiv podle akordu, v obratu sestup do toniky (zvukové logo ho dokončí na konci).
                for d, m in (POHODA_OBRAT if obrat else POHODA_MOTIV[useky[0][2]]):
                    tt = t0 + sw(d) * doba
                    if tt < konec:
                        j = jit()
                        mx.pridej("melodie", tt + j, marimba(m, vel(0.75)), 0.55, pan=-0.15)
                        zapis("marimba", tt, tt + j, nota=nota(m))

    # Finále na end card: úder + závěrečný akord, který dozní do konce.
    _, noty = akord_v(0)
    koren0 = akordy[0][0]
    zbyva = max(delka - konec, 1.0)
    if nalada != "pohodova":                                            # pohodová nálada končí bez hlubokého úderu (nic agresivního)
        mx.pridej("fx", konec, uder(jemny=nalada == "luxusni"), 0.45)
        mx.pridej("bici", konec, uder(jemny=nalada == "luxusni"), 0.3)
        zapis("uder", konec, konec)
    if nalada == "vazna":
        mx.pridej("harmonie", konec, plocha(noty + [noty[0] - 12], zbyva, 1200, 0.6, 0.05))
        mx.pridej("melodie", konec, klavir(noty[-1] + 12, zbyva, 0.8), 0.6)
        mx.pridej("basa", konec, sub(basovy(koren0, 38), zbyva, 0.9), 0.45)
        zapis("klavir", konec, konec, nota=nota(noty[-1] + 12))
        zapis("basa", konec, konec, nota=nota(basovy(koren0, 38)))
    elif nalada == "drza":
        for i, m in enumerate(noty):
            mx.pridej("melodie", konec + i * 0.03, pizz(m + 12, 0.9), 0.6)
        mx.pridej("bici", konec, clap(), 0.8)
        mx.pridej("melodie", konec + 0.12, pop(600, 2000, 0.2), 0.4)
        mx.pridej("basa", konec, basa_pluck(basovy(koren0, 36), 0.6, 1.0), 0.6)
        zapis("pizzicato", konec, konec, akord=[nota(m + 12) for m in noty])
        zapis("maly_buben_tlesknuti", konec, konec, jen_tlesknuti=True)
        zapis("pop", konec + 0.12, konec + 0.12)
        zapis("basa", konec, konec, nota=nota(basovy(koren0, 36)))
    elif nalada == "luxusni":
        for m in noty:
            mx.pridej("klavesy", konec, rhodes(m, zbyva, 0.75), 0.45)
        mx.pridej("harmonie", konec, plocha([m + 12 for m in noty[1:4]], zbyva, 3200, 0.25, 0.3))
        mx.pridej("basa", konec, sub(basovy(koren0), zbyva * 0.6, 0.9), 0.5)
        zapis("rhodes", konec, konec, akord=[nota(m) for m in noty])
        zapis("basa", konec, konec, nota=nota(basovy(koren0)))
    elif nalada == "pohodova":
        # Tónika (Fmaj9) s kořenem v base, kytara nechá doznít, jemný kopák + tleskání + činel.
        # Zvukové logo: marimba C5 F5 A5 v šestnáctinách, poslední tón přesně na konec (end card).
        tonika = akord(*akordy[0], 62)
        zapis("rhodes", konec, akord=[nota(m) for m in tonika])
        zapis("kytara", konec, konec, akord=[nota(m + 12) for m in tonika], tlumena=False)
        zapis("basa", konec, konec, nota=nota(basovy(koren0, 36)))
        zapis("kopak", konec, konec)
        zapis("maly_buben_tlesknuti", konec, konec + 0.012, jen_tlesknuti=True)
        zapis("cinel", konec, konec)
        for m in tonika:
            mx.pridej("klavesy", konec + jit(), rhodes(m, zbyva, 0.7, JAS_RHODES), 0.5)
        mx.pridej("kytara", konec, kytara([m + 12 for m in tonika], 0.75, tlumena=False), 0.5, pan=0.35)
        mx.pridej("harmonie", konec, plocha([m + 12 for m in tonika[1:]], zbyva, 2800, 0.2, 0.3))
        mx.pridej("basa", konec, basa_prsty(basovy(koren0, 36), min(zbyva, 2.0), 0.95), 0.65)
        mx.pridej("bici", konec, kick(95, 50, 0.45, 0.15, 0.12), 0.55)
        mx.pridej("bici", konec + 0.012, clap(), 0.45)
        mx.pridej("bici", konec, cinel(2.4, 0.8), 0.22)
        for i, m in enumerate(POHODA_LOGO):
            mx.pridej("melodie", konec - (len(POHODA_LOGO) - 1 - i) * doba / 4, marimba(m, 0.75 if i < 2 else 0.9), 0.6, pan=-0.15)
            zapis("marimba", konec - (len(POHODA_LOGO) - 1 - i) * doba / 4, konec - (len(POHODA_LOGO) - 1 - i) * doba / 4,
                  nota=nota(m), zvukove_logo=True)
    kicky.append(konec)
    udalosti_nastroju = {}
    for n, u in sorted(hraje, key=lambda x: x[1]["cas"]):
        udalosti_nastroju.setdefault(n, []).append(u)

    doby = [round(i * doba, 4) for i in range(int(delka / doba) + 1)]
    takty = [round(i * takt, 4) for i in range(int(delka / takt) + 1)]
    return mx, kicky, dict(bpm=bpm, doba=round(doba, 5), takt=round(takt, 5), drop=round(drop, 4), konec=round(konec, 4),
                           delka=delka, doby=doby, takty=takty, udalosti=udalosti, udalosti_nastroju=udalosti_nastroju)


SPORT_ARP = [0, 1, 2, 3, 4, 5, 3, 4, 0, 1, 2, 3, 5, 4, 3, 2]            # pořadí tónů arpeggia v šestnáctinách (6 tónů = akord ve 2 oktávách)


def aranzuj_sportovni(delka, bpm, drop, konec, zlom=None, drop2=None):
    """Závodní driving electro (V002). Části (časy se zaokrouhlí na takty, konec na dobu):
    ÚVOD (filtrované arpeggio, tlumená basa, hi-hat; poslední takt: kopák, vír, riser, motor s řazením, obrácený činel),
    DROP (úder + činel), PLNÁ JÍZDA, ZLOM (jen pad s otevírajícím se filtrem a průjezd motoru), STOUPÁNÍ (kopák, vír, riser,
    motor s řazením, arpeggio se otevírá), DROP 2 (nejsilnější: + akordové staby a arpeggio o oktávu výš), FINÁLE,
    KONEC (úder, činel, akord a odjezd motoru doznívají). Výchozí zlom = takt nejblíž středu mezi dropem a koncem, drop 2 = zlom + 2 takty."""
    doba = 60 / bpm
    takt = 4 * doba
    drop = max(takt, round(drop / takt) * takt)
    konec = max(drop + takt, round(konec / doba) * doba)
    zlom = round(((drop + konec) / 2 if zlom is None else zlom) / takt) * takt
    drop2 = zlom + 2 * takt if drop2 is None else round(drop2 / takt) * takt
    if not (drop + takt <= zlom < drop2 and drop2 + takt <= konec + 1e-6):
        raise SystemExit(f"sportovni: musí platit drop + takt ≤ zlom < drop2 ≤ konec − takt (drop {drop}, zlom {zlom}, drop2 {drop2}, konec {konec})")
    stoupani_od = max(zlom, drop2 - takt)
    akordy = NALADY["sportovni"]["akordy"]
    takt_dropu = int(round(drop / takt))
    mx = Mix(delka)
    kicky = []
    hraje = []
    vel = lambda z=0.85: float(np.clip(rng.normal(z, 0.05), 0.4, 1))   # noqa: E731
    udalosti = [{"cas": round(drop, 4), "typ": "drop"}, {"cas": round(zlom, 4), "typ": "zlom"},
                {"cas": round(stoupani_od, 4), "typ": "stoupani"}, {"cas": round(drop2, 4), "typ": "drop2"},
                {"cas": round(konec, 4), "typ": "konec"}]

    def zapis(nastroj, kdy, nastup=None, **info):
        u = dict(cas=round(kdy, 5), **info)
        if nastup is not None:
            u["nastup"] = round(nastup, 5)
        hraje.append((nastroj, u))

    def kopak(tt, v=1.0, h=0.36):
        mx.pridej("bici", tt, kick_tvrdy(v), h)
        kicky.append(tt)
        zapis("kopak", tt, tt)

    def uder_na(tt, sila):
        mx.pridej("fx", tt, impact(sila), 0.5)
        mx.pridej("bici", tt, cinel(2.0, 0.6), 0.35)
        zapis("uder", tt, tt)
        zapis("cinel", tt, tt)

    def motor_na(tt, body, dl, h, **info):
        mx.pridej("motor", tt, motor(body, dl, info.pop("pan_od", 0.0), info.pop("pan_do", 0.0), info.pop("obalka", None)), h)
        zapis("motor", tt, tt, **info)
        for (a, f1), (b_, f2) in zip(body, body[1:]):
            if abs(a - b_) < 1e-9 and f2 < f1:                         # skok dolů = přeřazení
                zapis("motor_radeni", tt + a, tt + a)

    def arpeggio(t0, noty, jas_od, jas_do, h, oktava=0, ozvena=True):
        tony = sorted(noty + [m + 12 for m in noty])
        for s, i in enumerate(SPORT_ARP):
            tt = t0 + s * doba / 4
            if tt >= konec - 1e-6:
                break
            m = tony[i] + oktava
            jas = jas_od * (jas_do / jas_od) ** (s / 15)
            v = vel(0.9 if s % 4 == 0 else 0.7)
            mx.pridej("arp", tt, arp_synth(m, doba / 4 * 0.85, v, jas), h, pan=(-0.2, 0.2)[s % 2])
            if ozvena:                                                  # ozvěna o 3 šestnáctiny na druhé straně
                mx.pridej("arp", tt + 0.75 * doba, arp_synth(m, doba / 4 * 0.85, v * 0.8, jas * 0.6), h * 0.3, pan=(0.6, -0.6)[s % 2])
            zapis("arp", tt, tt, nota=nota(m))

    def basa_osminy(t0, koren, jas, h):
        for s in range(8):
            tt = t0 + s * doba / 2
            if tt < konec - 1e-6:
                m = basovy(koren, 33) + (12 if s in (3, 7) else 0)
                mx.pridej("basa", tt, basa_dist(m, doba / 2 * 0.8, vel(0.95 if s % 2 else 0.85), jas), h)
                zapis("basa", tt, tt, nota=nota(m))

    def vir(od, do, h_od, h_do, deleni=4):
        """Vír malého bubnu: od–do v šestnáctinách (deleni=4) nebo dvaatřicetinách (8), hlasitost roste."""
        k = int(round((do - od) / (doba / deleni)))
        for i in range(k):
            tt = od + i * doba / deleni
            mx.pridej("bici", tt, snare(0.2, 0.05), h_od + (h_do - h_od) * (i / max(k - 1, 1)) ** 2)
            zapis("vir", tt, tt)

    for b in range(int(np.ceil(konec / takt))):
        t0 = b * takt
        if t0 >= konec - 1e-6:
            break
        k, iv = akordy[(b - takt_dropu) % len(akordy)]
        noty = akord(k, iv, 69)
        pad = akord(k, iv, 60)
        uvod, jizda = t0 < drop - 1e-6, drop - 1e-6 <= t0 < zlom - 1e-6
        zlomu, stoupani_ = zlom - 1e-6 <= t0 < stoupani_od - 1e-6, stoupani_od - 1e-6 <= t0 < drop2 - 1e-6
        finale = t0 >= drop2 - 1e-6

        if uvod:
            posledni = abs(t0 + takt - drop) < 1e-6
            podil = (b + 1) / takt_dropu
            arpeggio(t0, noty, 500 + 900 * podil, 900 + (2600 if posledni else 1200) * podil, 0.3)
            basa_osminy(t0, k, 450 + 500 * podil, 0.3)
            for s in range(8):
                if s % 2 or posledni:
                    mx.pridej("bici", t0 + s * doba / 2, hat(), 0.28 if s % 2 else 0.16, pan=0.25)
                    zapis("hihat", t0 + s * doba / 2, t0 + s * doba / 2)
            for d in (1, 3):
                if not (posledni and d == 3):
                    mx.pridej("bici", t0 + d * doba, clap(), 0.4)
                    zapis("maly_buben_tlesknuti", t0 + d * doba, t0 + d * doba, jen_tlesknuti=True)
            if posledni:                                                # nádech před dropem
                for d in range(3):
                    kopak(t0 + d * doba, 0.85, 0.3)
                vir(t0 + 2 * doba, drop, 0.06, 0.42)
                mx.pridej("fx", t0, stoupani(takt), 0.45)
                mx.pridej("fx", drop - 2 * doba, reverse_cinel(2 * doba), 0.5)
                zapis("obraceny_cinel", drop - 2 * doba, drop - 2 * doba, vrchol=round(drop, 5))
                motor_na(t0, [(0, 75), (0.75, 175), (0.75, 125), (takt, 250)], takt, 0.32, druh="rev", vrchol=round(drop, 5))

        elif jizda or finale:
            if abs(t0 - drop) < 1e-6:
                uder_na(drop, 0.85)
            if abs(t0 - drop2) < 1e-6:
                uder_na(drop2, 1.0)
            pred_koncem = lambda tt: tt < konec - 1e-6                # noqa: E731  takt může končit uprostřed (konec na dobu)
            for d in range(4):
                if pred_koncem(t0 + d * doba):
                    kopak(t0 + d * doba)
            for d in (1, 3):
                tt = t0 + d * doba
                if not pred_koncem(tt):
                    continue
                mx.pridej("bici", tt, clap(), 0.75)
                mx.pridej("bici", tt, snare(0.3, 0.09, 190), 0.4)
                zapis("maly_buben_tlesknuti", tt, tt)
            for s in range(16):
                tt = t0 + s * doba / 4
                if not pred_koncem(tt):
                    break
                mx.pridej("bici", tt, hat(s % 4 == 2), (0.3 if s % 4 == 2 else 0.2 if s % 2 == 0 else 0.13) * vel(), pan=0.25)
                zapis("hihat", tt, tt, **({"otevreny": True} if s % 4 == 2 else {}))
            basa_osminy(t0, k, 1900 if finale else 1600, 0.6 if finale else 0.52)
            arpeggio(t0, noty, 3200, 3200, 0.75 if finale else 0.62)
            mx.pridej("harmonie", t0, plocha(pad, min(takt, konec - t0), 2200, 0.3, 0.05))
            if finale:                                                  # drop 2: + staby na „a“ a arpeggio o oktávu výš
                arpeggio(t0, noty, 4500, 4500, 0.5, oktava=12, ozvena=False)
                for d in (0.5, 1.5, 2.5, 3.5):
                    tt = t0 + d * doba
                    if not pred_koncem(tt):
                        break
                    mx.pridej("lead", tt, supersaw(pad, doba * 0.3, vel(0.9)), 1.1)
                    zapis("stab", tt, tt, akord=[nota(m) for m in pad])
            if abs(t0 + takt - zlom) < 1e-6:                            # přechod do zlomu: vír na poslední dobu
                vir(t0 + 3 * doba, zlom, 0.1, 0.4)
            if konec <= t0 + takt + 1e-6 and konec - t0 >= 2 * doba - 1e-6:
                vir(konec - doba, konec, 0.1, 0.45)                     # přechod do konce: vír + obrácený činel
                mx.pridej("fx", konec - 2 * doba, reverse_cinel(2 * doba), 0.45)
                zapis("obraceny_cinel", konec - 2 * doba, konec - 2 * doba, vrchol=round(konec, 5))

        elif zlomu:                                                     # jen pad (filtr se otevírá) + průjezd motoru
            dl = stoupani_od - t0
            mx.pridej("harmonie", t0, filtr_prubeh(plocha(pad + [pad[0] - 12], dl, 9000, 0.7, 0.08), 280, 1100), 0.75)
            if abs(t0 - zlom) < 1e-6:
                mx.pridej("fx", zlom, cinel(2.4, 0.9), 0.25)
                zapis("cinel", zlom, zlom)
                motor_na(zlom, [(0, 135), (0.9, 200), (1.05, 150), (takt, 135)], takt, 0.55, druh="prujezd",
                         pan_od=-0.9, pan_do=0.9, obalka=[(0, 0.15), (0.95, 1.0), (takt, 0.12)], vrchol=round(zlom + 0.95, 5))

        elif stoupani_:                                                 # stoupání do dropu 2
            mx.pridej("harmonie", t0, filtr_prubeh(plocha(pad + [pad[0] - 12], takt, 9000, 0.7, 0.02), 1100, 6000), 0.8)
            for d in range(4):
                kopak(t0 + d * doba, 0.7 + 0.1 * d, 0.26 + 0.03 * d)
            vir(t0, t0 + 2 * doba, 0.04, 0.16, 2)
            vir(t0 + 2 * doba, t0 + 3 * doba, 0.18, 0.3, 4)
            vir(t0 + 3 * doba, drop2, 0.3, 0.5, 8)
            arpeggio(t0, noty, 600, 4200, 0.6)
            mx.pridej("fx", t0, stoupani(takt), 0.55)
            mx.pridej("fx", drop2 - 2 * doba, reverse_cinel(2 * doba), 0.55)
            zapis("obraceny_cinel", drop2 - 2 * doba, drop2 - 2 * doba, vrchol=round(drop2, 5))
            motor_na(t0, [(0, 70), (0.6, 170), (0.6, 120), (1.25, 225), (1.25, 165), (takt, 300)], takt, 0.36,
                     druh="rev", vrchol=round(drop2, 5))

    # Konec (end card): úder, činel, akord (staby + pad + basa) a odjezd motoru doznívají do konce.
    zbyva = max(delka - konec, 1.0)
    k0, iv0 = akordy[0]
    pad0 = akord(k0, iv0, 60)
    uder_na(konec, 1.0)
    kopak(konec)
    mx.pridej("bici", konec, clap(), 0.7)
    mx.pridej("lead", konec, supersaw(pad0, zbyva * 0.7, 0.9, 3500), 0.45)
    mx.pridej("harmonie", konec, plocha(pad0 + [pad0[0] - 12], zbyva, 2000, 0.45, 0.02))
    mx.pridej("basa", konec, basa_dist(basovy(k0, 33), 1.2, 1.0, 1200), 0.55)
    mx.pridej("basa", konec, sub(basovy(k0, 33), zbyva * 0.5, 0.8), 0.35)
    zapis("stab", konec, konec, akord=[nota(m) for m in pad0])
    zapis("basa", konec, konec, nota=nota(basovy(k0, 33)))
    motor_na(konec, [(0, 210), (0.35, 270), (0.35, 190), (zbyva, 150)], zbyva, 0.35, druh="odjezd",
             pan_od=0.0, pan_do=0.85, obalka=[(0, 0.6), (0.4, 0.75), (zbyva, 0.0)])

    udalosti_nastroju = {}
    for n_, u in sorted(hraje, key=lambda x: x[1]["cas"]):
        udalosti_nastroju.setdefault(n_, []).append(u)
    doby = [round(i * doba, 4) for i in range(int(delka / doba) + 1)]
    takty = [round(i * takt, 4) for i in range(int(delka / takt) + 1)]
    return mx, kicky, dict(bpm=bpm, doba=round(doba, 5), takt=round(takt, 5), drop=round(drop, 4), zlom=round(zlom, 4),
                           stoupani=round(stoupani_od, 4), drop2=round(drop2, 4), konec=round(konec, 4), delka=delka,
                           doby=doby, takty=takty, udalosti=udalosti, udalosti_nastroju=udalosti_nastroju)


# ---------- luxusní sportovní nálada (prémiový vůz: elegance + tah, V003) ----------
def kick_hluboky(vel=1.0, tlumeny=False):
    """Hluboký čistý kopák: pokles 150 → 46 Hz, kulaté tělo, jemný klik 2–6 kHz, mírná saturace (harmonické 90–250 Hz nesou
    kopák i z telefonu). `tlumeny` = kratší a měkčí, bez kliku (zlom)."""
    n = int(0.5 * SR)
    t = cas(n)
    f = 46 + 104 * np.exp(-t / 0.03)
    y = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / (0.12 if tlumeny else 0.2))
    k = filtr(sum_(n) * np.exp(-t / 0.002), "bandpass", [2000, 6000]) * (0.04 if tlumeny else 0.22)
    y = np.tanh(1.9 * (y + k)) / np.tanh(1.9)
    if tlumeny:
        y = filtr(y, "lowpass", 900)
    return y * obalka(n, 0.0006) * vel


def pila_v(f, faze0=0.0):
    """Pila s PolyBLEP pro proměnnou frekvenci (pole Hz po vzorcích, vibrato)."""
    dt = f / SR
    p = (faze0 + np.cumsum(dt)) % 1.0
    y = 2 * p - 1
    m = p < dt
    x = p[m] / dt[m]
    y[m] -= x + x - x * x - 1
    m = p > 1 - dt
    x = (p[m] - 1) / dt[m]
    y[m] -= x * x + x + x + 1
    return y


def smycce(noty, dur, jas=2600, vel=1.0, utok=0.35):
    """Smyčcová plocha legato: tři rozladěné pily na tón, vibrato 5,3 Hz (±6 centů, nastupuje během 0,6 s), každý kanál jiné
    fáze = šířka. Highpass 140 Hz (dno patří base). Vrací stereo."""
    n = int((dur + 1.0) * SR)
    t = cas(n)
    vib = 1 + 0.0035 * np.sin(2 * np.pi * 5.3 * t + rng.random() * 6.28) * np.clip(t / 0.6, 0, 1)
    out = np.zeros((2, n))
    for ch in range(2):
        s = np.zeros(n)
        for m in noty:
            for d in (-9, 0, 8):
                s += pila_v(mtof(m) * 2 ** ((d + rng.normal(0, 2)) / 1200) * vib, rng.random())
        out[ch] = filtr(filtr(s / (len(noty) * 3), "lowpass", jas, 2), "highpass", 140, 2)
    return out * obalka(n, utok, None, dur, 0.8) * vel


def sklo(noty, dur=0.2, vel=1.0, dozneni=0.35):
    """Sklenitý stab: FM zvon (modulátor 2:1, index rychle klesá = jasný úder, pak čistý tón) + neharmonický „skleněný“
    alikvot 4,07×. Kanály rozladěné ±4 centy = šířka. Nic nad ~12 kHz (C030). Vrací stereo."""
    n = int((dur + dozneni * 4) * SR)
    t = cas(n)
    out = np.zeros((2, n))
    for ch, cent in enumerate((-4, 4)):
        for m in noty:
            f = mtof(m) * 2 ** (cent / 1200)
            y = np.sin(2 * np.pi * f * t + 2.0 * np.exp(-t / 0.07) * np.sin(4 * np.pi * f * t))
            if f * 4.07 < 12000:
                y += 0.22 * np.sin(2 * np.pi * f * 4.07 * t + rng.random() * 6.28) * np.exp(-t / 0.09)
            out[ch] += y
    return out / len(noty) * obalka(n, 0.001, dozneni, dur + dozneni, 0.3) * vel


LUX_DOM = [(45, [0, 5, 7, 10]), (45, [0, 4, 7, 10, 13])]                # A7sus4 (doby 1–2) → A7(b9) (doby 3–4)
LUX_UVOD = [(46, [0, 4, 7, 11, 14]), (43, [0, 3, 7, 10, 14])]          # úvod: Bbmaj9 Gm9 (pak dominanta)
LUX_ZLOM = [(41, [0, 4, 7, 11, 14]), (46, [0, 4, 7, 11, 14])]          # zlom (luxus a pohodlí): Fmaj9 Bbmaj9
LUX_TONIKA = (50, [0, 3, 7, 14])                                       # konec: Dm(add9)
# Klavírní melodie podle akordu: {kořen: [(doba, MIDI, délka v dobách)]}. Psaná ručně: „nejvyšší tón akordu“ je ve všech akordech
# A5 (společný tón), melodie by stála na jednom tónu (spektrogram V003: bordun 879 Hz). Úvod živější, zlom zpěvný.
LUX_KLAVIR_UVOD = {46: [(0, 77, 1.0), (1, 69, 0.5), (1.5, 72, 0.5), (2, 74, 1.0), (3, 72, 0.5), (3.5, 69, 0.5)],    # Bbmaj9: F5 A4 C5 D5 C5 A4
                   43: [(0, 74, 1.0), (1, 70, 0.5), (1.5, 74, 0.5), (2, 77, 1.0), (3, 74, 0.5), (3.5, 70, 0.5)]}    # Gm9: D5 B4 D5 F5 D5 B4
LUX_KLAVIR_ZLOM = {41: [(0, 76, 1.5), (1.5, 79, 0.5), (2, 81, 1.0), (3, 79, 0.5), (3.5, 76, 0.5)],                  # Fmaj9: E5 G5 A5 G5 E5
                   46: [(0, 74, 1.5), (1.5, 77, 0.5), (2, 72, 1.0), (3, 74, 0.5), (3.5, 69, 0.5)]}                  # Bbmaj9: D5 F5 C5 D5 A4
LUX_KLAVIR_DOM = [(0, 76, 1.0), (1, 74, 0.5), (1.5, 69, 0.5), (2, 73, 1.0), (3, 76, 0.5), (3.5, 79, 0.5)]           # A7sus4 → A7b9: E5 D5 A4 | C#5 E5 G5


def aranzuj_luxsport(delka, bpm, drop, konec, zlom=None, drop2=None):
    """Luxusní sportovní hudba (V003, prémiový vůz). Části (časy na takty, konec na dobu):
    ÚVOD (klavírní motiv, smyčce, shaker; poslední takt: tlumený kopák, vír, riser, obrácený činel), DROP 1 (úder + činel),
    JÍZDA (hluboký kopák, tlesknutí + malý buben na 2 a 4, sub basa, Rhodes, smyčcové spiccato, sklenité staby),
    ZLOM (luxus a pohodlí: klavír, Rhodes, smyčce s otevíráním filtru, jen tlumený kopák), STOUPÁNÍ (riser, vír, kopák
    na každou dobu, nájezd motoru s řazením), DROP 2 (nejsilnější: výkon, motor, basa se zrnem, staby na každé „a“),
    KONEC (úder na logo, tónika smyčce + klavír + sklo, doznění). Výchozí zlom a drop 2 jako u `sportovni`."""
    doba = 60 / bpm
    takt = 4 * doba
    drop = max(takt, round(drop / takt) * takt)
    konec = max(drop + takt, round(konec / doba) * doba)
    zlom = round(((drop + konec) / 2 if zlom is None else zlom) / takt) * takt
    drop2 = zlom + 2 * takt if drop2 is None else round(drop2 / takt) * takt
    if not (drop + takt <= zlom < drop2 and drop2 + takt <= konec + 1e-6):
        raise SystemExit(f"luxsport: musí platit drop + takt ≤ zlom < drop2 ≤ konec − takt (drop {drop}, zlom {zlom}, drop2 {drop2}, konec {konec})")
    stoupani_od = max(zlom, drop2 - takt)
    akordy = NALADY["luxsport"]["akordy"]
    mx = Mix(delka)
    kicky = []
    hraje = []
    vel = lambda z=0.85: float(np.clip(rng.normal(z, 0.05), 0.4, 1))   # noqa: E731
    jit = lambda: rng.normal(0, 0.003)                                   # noqa: E731
    udalosti = [{"cas": round(drop, 4), "typ": "drop"}, {"cas": round(zlom, 4), "typ": "zlom"},
                {"cas": round(stoupani_od, 4), "typ": "stoupani"}, {"cas": round(drop2, 4), "typ": "drop2"},
                {"cas": round(konec, 4), "typ": "konec"}]

    def zapis(nastroj, kdy, nastup=None, **info):
        u = dict(cas=round(kdy, 5), **info)
        if nastup is not None:
            u["nastup"] = round(nastup, 5)
        hraje.append((nastroj, u))

    def cast(tt):
        if tt < drop - 1e-6:
            return "uvod"
        if tt < zlom - 1e-6:
            return "jizda"
        if tt < stoupani_od - 1e-6:
            return "zlom"
        if tt < drop2 - 1e-6:
            return "stoupani"
        return "finale" if tt < konec - 1e-6 else "konec"

    def akord_v(tt):
        """(kořen, intervaly) akordu v čase tt podle části; takt před dropem, dropem 2 a koncem = dominanta."""
        b = int(np.floor(tt / takt + 1e-9))
        t0 = b * takt
        if any(abs(t0 + takt - x) < 1e-6 for x in (drop, drop2)) or (t0 + takt >= konec - 1e-6 and t0 < konec - 1e-6):
            return LUX_DOM[0 if tt - t0 < 2 * doba - 1e-6 else 1]
        c = cast(tt)
        if c == "uvod":
            return LUX_UVOD[b % len(LUX_UVOD)]
        if c == "zlom":
            return LUX_ZLOM[(b - int(round(zlom / takt))) % len(LUX_ZLOM)]
        if c == "konec":
            return LUX_TONIKA
        return akordy[(b - int(round(drop / takt))) % len(akordy)]

    pred_koncem = lambda tt: tt < konec - 1e-6                         # noqa: E731

    def kopak(tt, v=1.0, h=0.5, tlumeny=False):
        mx.pridej("bici", tt, kick_hluboky(v, tlumeny), h)
        kicky.append(tt)
        zapis("kopak", tt, tt, **({"tlumeny": True} if tlumeny else {}))

    def tlesk(tt, h=1.0):
        mx.pridej("bici", tt, clap(), 0.6 * h)
        mx.pridej("bici", tt, snare(0.3, 0.1, 185), 0.3 * h)
        mx.pridej("fx", tt, clap(), 0.2 * h)                           # do dozvuku (šířka, „drahý“ prostor)
        zapis("maly_buben_tlesknuti", tt, tt)

    def uder_na(tt, sila, h=0.5):
        mx.pridej("fx", tt, impact(sila), h)
        mx.pridej("bici", tt, cinel(2.4, 0.8), 0.3)
        zapis("uder", tt, tt)
        zapis("cinel", tt, tt)

    def motor_na(tt, body, dl, h, **info):
        mx.pridej("motor", tt, motor(body, dl, info.pop("pan_od", 0.0), info.pop("pan_do", 0.0), info.pop("obalka", None)), h)
        zapis("motor", tt, tt, **info)
        for (a, f1), (b_, f2) in zip(body, body[1:]):
            if abs(a - b_) < 1e-9 and f2 < f1:                         # skok dolů = přeřazení
                zapis("motor_radeni", tt + a, tt + a)

    def vir(od, do, h_od, h_do, deleni=4):
        k = int(round((do - od) / (doba / deleni)))
        for i in range(k):
            tt = od + i * doba / deleni
            mx.pridej("bici", tt, snare(0.2, 0.05), h_od + (h_do - h_od) * (i / max(k - 1, 1)) ** 2)
            zapis("vir", tt, tt)

    def klavir_motiv(t0, vzor, h, levou=True):
        if levou:                                                       # levá ruka: akord (bez kvinty nahoře) na těžkou dobu
            k, iv = akord_v(t0)
            lh = akord(k, iv, 55)[:3]
            for m in lh:
                mx.pridej("melodie", t0 + jit(), klavir(m, 3 * doba, vel(0.5)), h * 0.5, pan=-0.15)
        k0_ = akord_v(t0)[0]
        melodie = LUX_KLAVIR_DOM if akord_v(t0) == LUX_DOM[0] else vzor.get(k0_, [(0, akord(*akord_v(t0), 74)[-1], 2.0)])
        for d, m, dl in melodie:
            tt = t0 + d * doba
            if not pred_koncem(tt):
                break
            mx.pridej("melodie", tt + jit(), klavir(m, dl * doba, vel(0.75 if d % 1 == 0 else 0.6)), h, pan=0.1)
            zapis("klavir", tt, nota=nota(m))

    def rhodes_na(tt, dl, h, v=0.65):
        k, iv = akord_v(tt)
        noty = akord(k, iv, 64)
        for m in noty:
            mx.pridej("klavesy", tt + jit(), rhodes(m, dl * doba, vel(v)), h)
        zapis("rhodes", tt, akord=[nota(m) for m in noty])

    def smycce_na(t0, dl, jas, h, utok=0.35, f_od=None, f_do=None):
        k, iv = akord_v(t0)
        noty = akord(k, iv, 62)
        x = smycce(noty + [basovy(k, 72)], dl, jas, 1.0, utok)        # horní hlas = kořen v C5–B5 (D5 Bb5 G5 F5 A5), ne bordun A5
        if f_od:
            x = filtr_prubeh(x, f_od, f_do)
        mx.pridej("harmonie", t0, x, h)

    def spiccato(t0, deleni, h, oktava=0, jas_od=2400, jas_do=2400):
        """Smyčcové spiccato (tah): osminy (deleni=2) nebo šestnáctiny (4) z kořene, kvinty a oktávy akordu v rozsahu D3–D4."""
        kroky = int(4 * deleni)
        for s in range(kroky):
            tt = t0 + s * doba / deleni
            if not pred_koncem(tt):
                break
            k, iv = akord_v(tt)
            kor = basovy(k, 50)
            m = kor + (0, 12, 7, 12)[s % 4] + oktava
            mx.pridej("smycce", tt, ostinato(m, doba / deleni * 0.8, vel(0.9 if s % deleni == 0 else 0.7)), h, pan=(-0.35, 0.35)[s % 2])
            zapis("spiccato", tt, tt, nota=nota(m))

    def basa_na(tt, m, dl, h, zrno=0.0):
        mx.pridej("basa", tt, sub(m, dl * doba, vel(0.92)), h)
        if zrno:                                                        # výkon: distorzovaná vrstva (harmonické do středů)
            mx.pridej("basa", tt, basa_dist(m, dl * doba, vel(0.9), 1400), h * zrno)
        zapis("basa", tt, tt, nota=nota(m))

    def staby(t0, doby_, h):
        for d in doby_:
            tt = t0 + d * doba
            if not pred_koncem(tt):
                break
            k, iv = akord_v(tt)
            noty = akord(k, iv, 74)[-3:]                                 # poloha kolem D5: horní tón se mění (F5 G5 E5…), ne stále A5
            mx.pridej("lead", tt, sklo(noty, 0.15, vel(0.85)), h, pan=0.0)
            zapis("sklo", tt, tt, akord=[nota(m) for m in noty])

    for b in range(int(np.ceil(konec / takt))):
        t0 = b * takt
        if t0 >= konec - 1e-6:
            break
        c = cast(t0)
        k, _ = akord_v(t0)
        kb = basovy(k, 33)
        dl_t = min(takt, konec - t0)
        posledni_pred_dropem = abs(t0 + takt - drop) < 1e-6

        dvoji = akord_v(t0) != akord_v(t0 + 2 * doba)                   # takt se dvěma akordy (dominanta sus4 → b9)
        pulky = [(t0, 2 * doba), (t0 + 2 * doba, dl_t - 2 * doba)] if dvoji and dl_t > 2 * doba + 1e-6 else [(t0, dl_t)]

        if c == "uvod":                                                 # luxusní odhalení: klavír, smyčce, shaker, lusknutí
            podil = (b + 1) / max(int(round(drop / takt)), 1)
            klavir_motiv(t0, LUX_KLAVIR_UVOD, 0.55)
            if b == 0:                                                  # háček v 0,0 s: sklenitý akord + měkký kopák (B6)
                sk = akord(*akord_v(0), 74)[-3:]
                mx.pridej("lead", 0, sklo(sk, 0.3, 0.9, 0.7), 0.45)
                zapis("sklo", 0, 0, akord=[nota(m) for m in sk])
                kopak(0, 0.7, 0.3, tlumeny=True)
            for od, dl in pulky:
                smycce_na(od, dl, 1200 + 1600 * podil, 0.42, 0.25 if b == 0 else 0.15)
            basa_na(t0, kb, 1.75, 0.3)
            basa_na(t0 + 2 * doba, basovy(akord_v(t0 + 2 * doba)[0], 33), 1.75, 0.3)
            for s in range(16):
                mx.pridej("bici", t0 + s * doba / 4 + jit(), shaker(), 0.1 * (1.5 if s % 4 == 2 else 1) * vel(), pan=0.35)
            for d in (1, 3):
                if not (posledni_pred_dropem and d == 3):
                    mx.pridej("bici", t0 + d * doba, snap(), 0.3, pan=-0.2)
                    zapis("lusknuti", t0 + d * doba, t0 + d * doba)
            if posledni_pred_dropem:                                    # nádech do dropu 1
                for d in range(4):
                    kopak(t0 + d * doba, 0.6 + 0.1 * d, 0.22 + 0.06 * d, tlumeny=d < 2)
                vir(t0 + 2 * doba, t0 + 3 * doba, 0.05, 0.16, 4)
                vir(t0 + 3 * doba, drop, 0.18, 0.36, 8)
                mx.pridej("fx", t0, stoupani(takt, 0.6), 0.4)
                mx.pridej("fx", drop - 2 * doba, reverse_cinel(2 * doba), 0.5)
                zapis("obraceny_cinel", drop - 2 * doba, drop - 2 * doba, vrchol=round(drop, 5))

        elif c in ("jizda", "finale"):                                  # jízda (drop 1) a výkon (drop 2, nejsilnější)
            fin = c == "finale"
            if abs(t0 - drop) < 1e-6:
                uder_na(drop, 0.7, 0.4)
            if abs(t0 - drop2) < 1e-6:
                uder_na(drop2, 1.0, 1.15)
                mx.pridej("bici", drop2, kick_hluboky(1.0), 0.3)          # zdvojený kopák = nejsilnější úder
                dj = min(4 * doba * 2, konec - drop2)                   # motor v plné jízdě: dvě přeřazení nahoru, pak ustoupí
                motor_na(drop2, [(0, 230), (2 * doba, 300), (2 * doba, 215), (5 * doba, 290), (5 * doba, 210), (dj, 260)], dj, 0.3, druh="jizda",
                         pan_od=-0.3, pan_do=0.3, obalka=[(0, 1.0), (0.6, 0.75), (2.5, 0.5), (dj, 0.0)])
            for d in range(4):
                if pred_koncem(t0 + d * doba):
                    kopak(t0 + d * doba, 1.0, 0.55 if fin else 0.5)
            for d in (1, 3):
                if pred_koncem(t0 + d * doba):
                    tlesk(t0 + d * doba, 1.15 if fin else 1.0)
            for s in range(16):
                tt = t0 + s * doba / 4
                if not pred_koncem(tt):
                    break
                if s % 4 == 2:
                    mx.pridej("bici", tt, hat(True), 0.4 * vel(), pan=0.25)
                    zapis("hihat", tt, tt, otevreny=True)
                elif s % 2 == 0 or fin:
                    mx.pridej("bici", tt + jit(), hat(), (0.28 if s % 2 == 0 else 0.18) * vel(), pan=0.25)
                    zapis("hihat", tt)
            for d, m, dl in [(0, kb, 1.25), (1.5, kb, 0.4), (2.5, basovy(akord_v(t0 + 2.5 * doba)[0], 33) + 7, 0.75), (3.5, kb + 12, 0.4)]:
                if pred_koncem(t0 + d * doba):
                    basa_na(t0 + d * doba, m, dl, 0.55, 0.35 if fin else 0.0)
            for d, dl, v in [(0, 1.4, 0.7), (2.5, 0.9, 0.6)]:
                if pred_koncem(t0 + d * doba):
                    rhodes_na(t0 + d * doba, dl, 0.32, v)
            for od, dl in pulky:
                smycce_na(od, dl, 3400 if fin else 2600, 0.42 if fin else 0.36, 0.08)
            spiccato(t0, 4 if fin else 2, 0.32 if fin else 0.28, oktava=12 if fin else 0)
            staby(t0, (0.5, 1.5, 2.5, 3.5) if fin else (1.5, 3.5), 0.45 if fin else 0.35)
            if abs(t0 + takt - zlom) < 1e-6:                            # do zlomu: obrácený činel (bez víru, klidně)
                mx.pridej("fx", zlom - 2 * doba, reverse_cinel(2 * doba), 0.32)
                zapis("obraceny_cinel", zlom - 2 * doba, zlom - 2 * doba, vrchol=round(zlom, 5))
            if konec <= t0 + takt + 1e-6 and konec - t0 >= 2 * doba - 1e-6:
                vir(konec - doba, konec, 0.12, 0.42, 8)                 # do konce (logo): vír + obrácený činel
                mx.pridej("fx", konec - 2 * doba, reverse_cinel(2 * doba), 0.45)
                zapis("obraceny_cinel", konec - 2 * doba, konec - 2 * doba, vrchol=round(konec, 5))

        elif c == "zlom":                                               # luxus a pohodlí: klavír, Rhodes, smyčce, tlumený kopák
            if abs(t0 - zlom) < 1e-6:
                mx.pridej("bici", zlom, cinel(2.4, 0.9), 0.18)
                zapis("cinel", zlom, zlom)
            celkem = stoupani_od - zlom
            p0, p1 = (t0 - zlom) / celkem, (t0 + dl_t - zlom) / celkem
            klavir_motiv(t0, LUX_KLAVIR_ZLOM, 0.6)
            rhodes_na(t0, 3.8, 0.26, 0.55)
            smycce_na(t0, dl_t, 6000, 0.5, 0.4 if p0 == 0 else 0.1, 700 * 3 ** p0, 700 * 3 ** p1)   # filtr se otevírá 700 → 2100 Hz
            kopak(t0, 0.8, 0.32, tlumeny=True)
            kopak(t0 + 2.5 * doba, 0.65, 0.24, tlumeny=True)
            for d in (1, 3):
                mx.pridej("bici", t0 + d * doba, snap(), 0.22, pan=-0.2)
                zapis("lusknuti", t0 + d * doba, t0 + d * doba)
            for s in range(16):
                mx.pridej("bici", t0 + s * doba / 4 + jit(), shaker(), 0.09 * (1.5 if s % 4 == 2 else 1) * vel(), pan=0.35)
            basa_na(t0, kb, 3.4, 0.42)
            basa_na(t0 + 3.5 * doba, kb + 12, 0.45, 0.25)

        elif c == "stoupani":                                           # stoupání do dropu 2: riser, vír, nájezd motoru s řazením
            for d in range(4):                                          # každá doba hlasitější než předchozí (C032)
                kopak(t0 + d * doba, 0.75 + 0.08 * d, 0.3 + 0.09 * d)
            for d in (1, 3):
                tlesk(t0 + d * doba, 0.45 + 0.2 * d)
            vir(t0, t0 + 2 * doba, 0.04, 0.14, 2)
            vir(t0 + 2 * doba, t0 + 3 * doba, 0.16, 0.28, 4)
            vir(t0 + 3 * doba, drop2, 0.3, 0.5, 8)
            for i, (od, dl) in enumerate(pulky):
                smycce_na(od, dl, 6000, 0.38 + 0.08 * i, 0.05, 900 * 2.5 ** i, 900 * 2.5 ** (i + 1))
            spiccato(t0, 4, 0.3)
            for s in range(8):                                          # pedál dominanty v osminách, sílí
                basa_na(t0 + s * doba / 2, kb + (12 if s % 2 else 0), 0.4, 0.3 + 0.035 * s)
            mx.pridej("fx", t0, stoupani(takt), 0.5)
            mx.pridej("fx", drop2 - 2 * doba, reverse_cinel(2 * doba), 0.55)
            zapis("obraceny_cinel", drop2 - 2 * doba, drop2 - 2 * doba, vrchol=round(drop2, 5))
            motor_na(t0, [(0, 90), (doba, 180), (doba, 130), (2 * doba, 230), (2 * doba, 170), (takt, 310)], takt, 0.34,   # řazení na doby
                     druh="najezd", obalka=[(0, 0.25), (takt, 1.0)], vrchol=round(drop2, 5))

    # Konec (skládací logo): úder, kopák, tlesknutí, tónika Dm(add9) ve smyčcích, klavíru, Rhodes a skle, sub basa; doznívá.
    zbyva = max(delka - konec, 1.0)
    k0, iv0 = LUX_TONIKA
    uder_na(konec, 0.75, 0.4)
    kopak(konec, 0.9, 0.5)
    mx.pridej("bici", konec, clap(), 0.5)
    zapis("maly_buben_tlesknuti", konec, konec, jen_tlesknuti=True)
    ton = akord(k0, iv0, 62)
    mx.pridej("harmonie", konec, smycce(ton + [basovy(k0, 72)], zbyva, 2600, 1.0, 0.03), 0.45)
    for m in akord(k0, iv0, 76) + [basovy(k0, 33) + 12]:
        mx.pridej("melodie", konec + jit(), klavir(m, zbyva, 0.75), 0.45, pan=0.1)
    zapis("klavir", konec, konec, akord=[nota(m) for m in akord(k0, iv0, 76)])
    for m in akord(k0, iv0, 64):
        mx.pridej("klavesy", konec + jit(), rhodes(m, zbyva, 0.6), 0.25)
    sk = akord(k0, iv0, 74)[-3:]
    mx.pridej("lead", konec, sklo(sk, 0.3, 0.95, 0.8), 0.5)
    zapis("sklo", konec, konec, akord=[nota(m) for m in sk])
    basa_na(konec, basovy(k0, 33), zbyva * 0.5 / doba, 0.5)

    udalosti_nastroju = {}
    for n_, u in sorted(hraje, key=lambda x: x[1]["cas"]):
        udalosti_nastroju.setdefault(n_, []).append(u)
    doby = [round(i * doba, 4) for i in range(int(delka / doba) + 1)]
    takty = [round(i * takt, 4) for i in range(int(delka / takt) + 1)]
    return mx, kicky, dict(bpm=bpm, doba=round(doba, 5), takt=round(takt, 5), drop=round(drop, 4), zlom=round(zlom, 4),
                           stoupani=round(stoupani_od, 4), drop2=round(drop2, 4), konec=round(konec, 4), delka=delka,
                           doby=doby, takty=takty, udalosti=udalosti, udalosti_nastroju=udalosti_nastroju)


NASTAVENI_MIXU = {
    # bus: (hlasitost, dozvuk-send, sidechain)
    "vazna": dict(bici=(0.8, 0.12, False), basa=(0.7, 0.0, True), harmonie=(1.1, 0.35, True), melodie=(1.1, 0.45, False), fx=(0.5, 0.8, False), rt60=3.2),
    "drza": dict(bici=(0.8, 0.06, False), basa=(0.45, 0.0, True), harmonie=(1.3, 0.3, True), melodie=(1.5, 0.18, False), fx=(0.45, 0.5, False), rt60=1.2),
    "luxusni": dict(bici=(0.7, 0.08, False), basa=(0.65, 0.0, True), klavesy=(1.2, 0.3, True), harmonie=(0.9, 0.5, True), fx=(0.45, 0.7, False), rt60=2.6),
    # pohodová: jen lehké „pumpování“ od kopáku (sidechain 0,3), Rhodes s pomalým stereo tremolem v osminách (96 BPM → 3,2 Hz)
    "pohodova": dict(bici=(0.75, 0.07, False), basa=(0.75, 0.0, True), klavesy=(1.0, 0.28, True), kytara=(0.85, 0.22, False),
                     melodie=(0.85, 0.3, False), harmonie=(0.45, 0.35, True), fx=(0.4, 0.6, False), rt60=1.6,
                     sidechain=0.3, tremolo=3.2, vysky_db=4, prezence=(1400, 3000, 10)),
    # sportovní: výrazné „pumpování“ basy, arpeggia a stabů od kopáku (sidechain 0,6), suché bicí, motor bez dozvuku skoro nasucho
    "sportovni": dict(bici=(0.85, 0.04, False), basa=(0.3, 0.0, True), arp=(1.6, 0.22, True), lead=(1.4, 0.25, True),
                      harmonie=(1.4, 0.35, True), motor=(0.9, 0.12, False), fx=(0.5, 0.45, False), rt60=1.4, sidechain=0.6),
    # luxusní sportovní: delší „drahý“ prostor (rt60 2,2), mírné pumpování (0,4) basy, smyčců a Rhodes, Rhodes s tremolem v osminách (4 Hz)
    # (klavír je aditivní bez normalizace, proto melodie jen 0,3)
    "luxsport": dict(bici=(0.85, 0.06, False), basa=(0.5, 0.0, True), klavesy=(0.6, 0.3, True), melodie=(0.3, 0.35, False),
                     harmonie=(2.5, 0.4, True), smycce=(2.0, 0.25, True), lead=(1.8, 0.45, False), motor=(0.85, 0.12, False),
                     fx=(0.7, 0.5, False), rt60=2.2, sidechain=0.4, tremolo=4.0, vysky_db=3, prezence=(1500, 4500, 5)),
}


def mixuj(mx, kicky, nalada):
    nast = NASTAVENI_MIXU[nalada]
    sc = sidechain(mx.n, kicky, nast.get("sidechain", 0.55))
    suchy = np.zeros((2, mx.n))
    send = np.zeros((2, mx.n))
    for bus, x in mx.busy.items():
        g, s, duck = nast.get(bus, (0.7, 0.2, False))
        if bus == "klavesy":
            x = x * autopan(mx.n, nast.get("tremolo", 4.5))
        if duck:
            x = x * sc
        suchy += x * g
        send += x * g * s
    out = suchy + dozvuk(send, nast["rt60"]) * 0.9
    out = filtr(out, "highpass", 38, 2)
    if nast.get("vysky_db"):                                            # jemné zvýšení výšek nad ~2,5 kHz (jas z telefonu)
        out = out + (10 ** (nast["vysky_db"] / 20) - 1) * filtr(out, "highpass", 2500, 2)
    # Zvednutí pásma od–do Hz o dB: díra 1–2 kHz (C017). Pohodová: +7 dB stačí na celek, ale úvod (jen Rhodes a marimba) měl
    # pořád 1 → 2 kHz −10,9 dB, +10 dB ho stáhne na −8,5 a po dropu dá plynulý sklon −4 až −5 dB na oktávu.
    if nast.get("prezence"):
        od, do, db = nast["prezence"]
        sos = signal.butter(2, [od / (SR / 2), do / (SR / 2)], btype="bandpass", output="sos")
        out = out + (10 ** (db / 20) - 1) * signal.sosfiltfilt(sos, out, axis=-1)   # nulová fáze: sečte se bez hřebenového filtru
    out = np.tanh(1.2 * out / (np.max(np.abs(out)) + 1e-9)) / np.tanh(1.2)    # jemné „slepení“
    return out


def uloz(out, delka, cesta, linearni=False):
    """`linearni` = jen zisk na −14 LUFS + jemný limiter (zachová stavbu úvod < jízda < drop 2). Jednoprůchodový loudnorm
    je dynamický: tiché části zesílí a dropy srovná (sportovní úvod −21 → −16 dB, stejně hlasitý jako jízda)."""
    n = int(delka * SR)
    out = out[:, :n]
    fade = int(0.25 * SR)
    out[:, -fade:] *= np.linspace(1, 0, fade) ** 2
    out *= 0.9 / (np.max(np.abs(out)) + 1e-9)
    tmp = cesta.with_suffix(".raw.wav")
    from scipy.io import wavfile
    wavfile.write(tmp, SR, (out.T * 32767).astype(np.int16))
    af = "loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000"
    if linearni:
        mer = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(tmp), "-af", "ebur128", "-f", "null", "-"],
                             capture_output=True, text=True, check=True).stderr
        hlasitost = float(re.findall(r"^\s+I:\s+(-?[\d.]+) LUFS", mer, re.M)[-1])
        af = (f"volume={-14 - hlasitost:.2f}dB,aresample=192000,alimiter=limit={10 ** (-1.5 / 20):.4f}:attack=5:release=300:level=false:latency=1,"
              "aresample=48000")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-af", af, "-c:a", "pcm_s16le", str(cesta)], check=True)
    tmp.unlink()


PASMA = [("sub", 20, 60), ("basy", 60, 250), ("stredy", 250, 2000), ("horni_stredy", 2000, 6000), ("vysky", 6000, 20000)]
# Rozumné meze podílu energie (%). Odvozeno z profesionální hudby (R5: sub 20, basy 22, středy 57). Telefon pod ~100 Hz nehraje.
MEZE = {"sub": (0, 30), "stredy": (30, 75)}
# Spektrum po oktávách (středy pásem v Hz). Široká pásma schovají díru uvnitř (C017: středy v pořádku, a přitom 1 → 2 kHz −13 dB).
# Vyvážený mix klesá k výškám plynule, mezi sousedními oktávami 250 Hz–8 kHz o pár dB. Práh 9 dB (měřeno 25 s, drop 7,5, konec 22,5):
# drzá nejvýš 5,9 dB a pohodová po vyrovnání 5,6 dB projdou, pohodová před vyrovnáním (C017) 12,9 dB varuje. Varují i vážná
# (250 → 500 Hz +16 dB, středy 85 %) a luxusní (1 → 2 kHz −12,7 dB, nad 2 kHz skoro nic): ty vyvážené nejsou, oprava změní jejich zvuk.
OKTAVY = [63, 125, 250, 500, 1000, 2000, 4000, 8000, 16000]
SKOK_OKTAV = (250, 8000, 9.0)                                           # od, do (Hz), největší rozdíl sousedních oktáv (dB)


def kontrola_pasem(cesta):
    from scipy.io import wavfile
    _, x = wavfile.read(cesta)
    x = x.astype(float).mean(axis=1)
    X = np.abs(np.fft.rfft(x)) ** 2
    fr = np.fft.rfftfreq(len(x), 1 / SR)
    pasma = {k: round(float(X[(fr >= a) & (fr < b)].sum() / X.sum() * 100), 1) for k, a, b in PASMA}
    print("pásma %:", "  ".join(f"{k} {v}" for k, v in pasma.items()))
    for k, (lo, hi) in MEZE.items():
        if not lo <= pasma[k] <= hi:
            print(f"VAROVÁNÍ: {k} {pasma[k]} % mimo {lo}–{hi} % (mix nevyvážený, z telefonu bude znít špatně)")
    e = np.array([X[(fr >= f / np.sqrt(2)) & (fr < f * np.sqrt(2))].sum() for f in OKTAVY])
    db = 10 * np.log10(e / e.max() + 1e-12)
    oktavy = {str(f): round(float(d), 1) for f, d in zip(OKTAVY, db)}
    print("oktávy dB:", "  ".join(f"{f} {d}" for f, d in oktavy.items()))
    od, do, prah = SKOK_OKTAV
    for i in range(len(OKTAVY) - 1):
        if od <= OKTAVY[i] and OKTAVY[i + 1] <= do and abs(db[i + 1] - db[i]) > prah:
            print(f"VAROVÁNÍ: oktávy {OKTAVY[i]} → {OKTAVY[i + 1]} Hz se liší o {db[i + 1] - db[i]:+.1f} dB (víc než {prah:g} dB: "
                  "díra nebo schod ve spektru, z telefonu bude znít nevyrovnaně, C017)")
    return pasma, oktavy


def main():
    global rng
    ap = argparse.ArgumentParser()
    ap.add_argument("--nalada", required=True, choices=list(NALADY))
    ap.add_argument("--delka", type=float, required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--bpm", type=float)
    ap.add_argument("--drop", type=float)
    ap.add_argument("--konec", type=float)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--zlom", type=float, help="jen sportovni a luxsport: začátek zlomu (breakdown), výchozí takt nejblíž středu mezi dropem a koncem")
    ap.add_argument("--drop2", type=float, help="jen sportovni a luxsport: druhý drop, výchozí zlom + 2 takty (poslední takt před ním = stoupání)")
    a = ap.parse_args()
    rng = np.random.default_rng(a.seed)
    bpm = a.bpm or NALADY[a.nalada]["bpm"]
    drop = a.drop if a.drop is not None else a.delka * 0.22
    konec = a.konec if a.konec is not None else a.delka - 2.5
    if a.nalada == "sportovni":
        mx, kicky, info = aranzuj_sportovni(a.delka, bpm, drop, konec, a.zlom, a.drop2)
    elif a.nalada == "luxsport":
        mx, kicky, info = aranzuj_luxsport(a.delka, bpm, drop, konec, a.zlom, a.drop2)
    else:
        mx, kicky, info = aranzuj(a.nalada, a.delka, bpm, drop, konec)
    cesta = Path(a.out)
    cesta.parent.mkdir(parents=True, exist_ok=True)
    uloz(mixuj(mx, kicky, a.nalada), a.delka, cesta, linearni=a.nalada in ("sportovni", "luxsport"))
    info["pasma"], info["oktavy_db"] = kontrola_pasem(cesta)
    cesta.with_suffix(".json").write_text(json.dumps(info, ensure_ascii=False, indent=1))
    print(f"{cesta}: {a.nalada}, {bpm} BPM, drop {info['drop']} s, konec {info['konec']} s, délka {a.delka} s")


if __name__ == "__main__":
    main()
