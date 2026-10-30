"""Generátor hudby do pozadí: syntéza v kódu, naše vlastní (bez licencí), přesně na doby pro animaci.

Použití:
  python3 -I nastroje/hudba.py --nalada vazna|drza|luxusni|pohodova --delka 20 --out hudba.wav
        [--bpm 120] [--drop 4.0] [--konec 17.5] [--seed 1]
  --drop   čas nástupu plné části (zaokrouhlí se na celý takt), předtím úvod a stoupání
  --konec  čas finálního úderu (end card), zaokrouhlí se na dobu; potom už jen doznívá
Výstup: WAV 48 kHz stereo na −14 LUFS (true peak ≤ −1,5 dBTP) + JSON se všemi dobami, takty a událostmi
pro synchronizaci animace (hudba.json vedle WAV).
"""
import argparse
import json
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


# ---------- harmonie ----------
def basovy(m, nejniz=33):
    """Basový tón v rozsahu nejniz … nejniz+11 (výchozí A1–G#2, 55–104 Hz)."""
    while m < nejniz:
        m += 12
    while m >= nejniz + 12:
        m -= 12
    return m


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
                    mx.pridej("melodie", t0 + d * doba + jit(), klavir(m, doba * 1.2, vel(0.7)), 0.5, pan=0.15 * (i - 1))
            for s in range(8):                                                     # ostinato osminy
                tt = t0 + s * doba / 2
                if tt < konec:
                    mx.pridej("basa", tt, ostinato(basovy(koren, 38) + (12 if s % 2 else 0), doba / 2 * 0.8, vel(0.9 if hlavni else 0.5)), 0.55 if hlavni else 0.3)
            mx.pridej("bici", t0, taiko(), 0.5 if hlavni else 0.3)
            if hlavni:
                for d in (0, 2.5):
                    mx.pridej("bici", t0 + d * doba, kick(90, 48, 0.5, 0.18, 0.15), 0.6)
                    kicky.append(t0 + d * doba)
                if t0 + 2 * doba < konec:
                    mx.pridej("bici", t0 + 2 * doba, snare(0.5, 0.16, 180), 0.6)
                    mx.pridej("fx", t0 + 2 * doba, snare(0.5, 0.16, 180), 0.35)
                for s in range(8):
                    if t0 + s * doba / 2 < konec:
                        mx.pridej("bici", t0 + s * doba / 2 + jit(), hat(), 0.18 * vel(), pan=0.3)
            if posledni_pred:                                                      # vír na snare + stoupání
                for s in range(16):
                    mx.pridej("bici", t0 + s * doba / 4, snare(0.2, 0.05), 0.08 + 0.35 * (s / 15) ** 2)
                mx.pridej("fx", t0, stoupani(takt), 0.5)
                mx.pridej("fx", drop - doba, reverse_cinel(doba), 0.6)

        elif nalada == "drza":
            swing = lambda d: d + (0.08 if (d * 2) % 2 == 1 else 0)               # noqa: E731  lichá osmina o kousek později
            for i, d in enumerate([0, 0.75, 1.5, 2.5, 3.0]):
                tt = t0 + swing(d) * doba
                if tt < konec and not (posledni_pred and d >= 3):
                    mx.pridej("melodie", tt + jit(), pizz(noty[i % len(noty)] + 12, vel(0.8)), 0.85, pan=(-0.3, 0.3)[i % 2])
            if not hlavni:
                for d in (1, 3):
                    if not (posledni_pred and d == 3):
                        mx.pridej("bici", t0 + d * doba, snap(), 0.5, pan=0.2)
            else:
                for d in (0, 1.75, 2.0 + 0.5):
                    tt = t0 + d * doba
                    if tt < konec:
                        mx.pridej("bici", tt, kick(120, 52, 0.35, 0.12, 0.35), 0.6)
                        kicky.append(tt)
                for d in (1, 3):
                    if t0 + d * doba < konec:
                        mx.pridej("bici", t0 + d * doba, clap(), 0.7)
                        mx.pridej("fx", t0 + d * doba, clap(), 0.25)
                for s in range(8):
                    tt = t0 + swing(s / 2) * doba
                    if tt < konec:
                        mx.pridej("bici", tt + jit(), hat(), (0.22 if s % 2 else 0.14) * vel(), pan=-0.25)
                for d, o in [(0, 0), (0.5, 12), (1.5, 0), (2.5, 7), (3.5, 12)]:
                    tt = t0 + swing(d) * doba
                    if tt < konec:
                        mx.pridej("basa", tt, basa_pluck(basovy(koren, 36) + o, doba * 0.4, vel(0.9)), 0.6)
                if b % 2 == 0:
                    mx.pridej("melodie", t0 + 3.5 * doba, pop(), 0.35, pan=0.4)
                mx.pridej("harmonie", t0, plocha(noty, delka_taktu, 2600, 0.3, 0.2))   # výplň středů pod drnkáním
            if posledni_pred:                                                      # drzá pauza: poslední doba ticho, jen „pop“
                mx.pridej("fx", t0, stoupani(takt * 0.75, 0.6), 0.35)
                mx.pridej("melodie", drop - doba * 0.5, pop(700, 1800, 0.15), 0.5)

        elif nalada == "luxusni":
            mx.pridej("harmonie", t0, plocha([m + 12 for m in noty[1:4]], delka_taktu, 3200, 0.22, 1.0))
            if not hlavni:
                for m in noty:
                    mx.pridej("klavesy", t0 + jit(), rhodes(m, delka_taktu * 0.95, vel(0.6)), 0.45)
                for s in range(16):
                    if t0 + s * doba / 4 < konec:
                        mx.pridej("bici", t0 + s * doba / 4 + jit(), shaker(), 0.12 * (1.4 if s % 4 == 2 else 1) * vel(), pan=0.35)
            else:
                for d, dl in [(0, 1.4), (2.5, 0.9)]:                                # akord + synkopa
                    if t0 + d * doba < konec:
                        for m in noty:
                            mx.pridej("klavesy", t0 + d * doba + jit(), rhodes(m, dl * doba, vel(0.7)), 0.4)
                for d in range(4):
                    tt = t0 + d * doba
                    if tt < konec:
                        mx.pridej("bici", tt, kick(85, 48, 0.4, 0.13, 0.18), 0.55)
                        kicky.append(tt)
                        mx.pridej("bici", tt + doba / 2, hat(True), 0.32 * vel(), pan=0.25)
                for d in (1, 3):
                    if t0 + d * doba < konec:
                        mx.pridej("bici", t0 + d * doba, clap(), 0.3)
                        mx.pridej("fx", t0 + d * doba, clap(), 0.3)
                for s in range(16):
                    if t0 + s * doba / 4 < konec:
                        mx.pridej("bici", t0 + s * doba / 4 + jit(), shaker(), 0.16 * (1.4 if s % 4 == 2 else 1) * vel(), pan=0.35)
                for d, dl, o in [(0, 1.2, 0), (1.75, 0.5, 0), (2.5, 0.9, 0), (3.5, 0.4, 12)]:
                    if t0 + d * doba < konec:
                        mx.pridej("basa", t0 + d * doba, sub(basovy(koren) + o, dl * doba, vel(0.9)), 0.6)
            if posledni_pred:
                mx.pridej("fx", drop - 2 * doba, reverse_cinel(2 * doba), 0.45)

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
                    for m in hlasy:
                        mx.pridej("klavesy", t0 + sw(d) * doba + jit(), rhodes(m, dd * doba, vel(v), JAS_RHODES), 0.5)
                mx.pridej("harmonie", t0, plocha([m + 12 for m in hlasy[1:]], (2.75 if posledni_pred else 4.0) * doba, 2800, 0.16, 0.5))   # vzdušná plocha
                for d in (1, 3):
                    if not (posledni_pred and d == 3):
                        mx.pridej("bici", t0 + d * doba + jit(), snap(), 0.4, pan=0.2)
                for s in range(12 if posledni_pred else 16):
                    mx.pridej("bici", t0 + sw(s / 4) * doba + jit(), shaker(), 0.13 * (1.5 if s % 2 else 1) * vel(), pan=-0.3)
                mx.pridej("melodie", t0 + jit(), marimba(hlasy[-1] + 12, vel(0.55)), 0.45, pan=-0.15)
                mx.pridej("melodie", t0 + sw(1.5) * doba + jit(), marimba(hlasy[1] + 12, vel(0.4)), 0.4, pan=-0.15)
                if posledni_pred:
                    for d in (0, 2):                                            # jemný kopák ohlásí drop
                        mx.pridej("bici", t0 + d * doba, kick(95, 50, 0.45, 0.15, 0.12), 0.35)
                    mx.pridej("fx", drop - 2 * doba, reverse_cinel(2 * doba), 0.32)
                    for d, m in POHODA_MOTIV[3][3:]:                            # předtakt A5 G5 do prvního tónu dropu
                        mx.pridej("melodie", t0 + sw(d) * doba + jit(), marimba(m, vel(0.7)), 0.5, pan=-0.15)
            else:
                if t0 < drop + 1e-6:
                    mx.pridej("bici", drop, cinel(), 0.22)                     # jemný činel na drop
                # Bicí: kopák 1, „a“ po 1, 3&; malý buben + tleskání na 2 a 4 o kousek později (uvolněně); hi-hat šestnáctiny se swingem.
                for d in [0, 0.75, 2.5] + ([3.75] if b % 2 else []):
                    tt = t0 + sw(d) * doba
                    if tt < konec:
                        mx.pridej("bici", tt, kick(95, 50, 0.45, 0.15, 0.12), 0.55)
                        kicky.append(tt)
                for d in (1, 3):
                    tt = t0 + d * doba
                    if tt < konec:
                        mx.pridej("bici", tt + 0.008, snare(0.3, 0.09, 190), 0.4)
                        mx.pridej("bici", tt + 0.012, clap(), 0.65)
                        mx.pridej("fx", tt + 0.012, clap(), 0.16)
                for s in range(16):
                    tt = t0 + sw(s / 4) * doba
                    if tt < konec:
                        mx.pridej("bici", tt + jit(), hat(), (0.36 if s % 4 == 2 else 0.24 if s % 2 == 0 else 0.15) * vel(), pan=0.25)
                        mx.pridej("bici", tt + jit(), shaker(), 0.12 * vel(), pan=-0.35)
                if b % 2 == 1 and t0 + 3.5 * doba < konec:
                    mx.pridej("bici", t0 + 3.5 * doba, hat(True), 0.3, pan=0.25)
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
                            mx.pridej("basa", tt + jit(), basa_prsty(m, dd * doba, vel(0.9)), 0.6)
                # Kytara: tlumené brnknutí na 2& a 4& (vesele „poskakuje“).
                for d in (1.5, 3.5):
                    tt = t0 + d * doba
                    if tt < konec:
                        ia = useky[-1][2] if d >= useky[-1][0] else useky[0][2]
                        mx.pridej("kytara", tt + jit(), kytara([m + 12 for m in akord(*akordy[ia], 62)[1:]], vel(0.6)), 0.5, pan=0.35)
                # Marimba: motiv podle akordu, v obratu sestup do toniky (zvukové logo ho dokončí na konci).
                for d, m in (POHODA_OBRAT if obrat else POHODA_MOTIV[useky[0][2]]):
                    tt = t0 + sw(d) * doba
                    if tt < konec:
                        mx.pridej("melodie", tt + jit(), marimba(m, vel(0.75)), 0.55, pan=-0.15)

    # Finále na end card: úder + závěrečný akord, který dozní do konce.
    _, noty = akord_v(0)
    koren0 = akordy[0][0]
    zbyva = max(delka - konec, 1.0)
    if nalada != "pohodova":                                            # pohodová nálada končí bez hlubokého úderu (nic agresivního)
        mx.pridej("fx", konec, uder(jemny=nalada == "luxusni"), 0.45)
        mx.pridej("bici", konec, uder(jemny=nalada == "luxusni"), 0.3)
    if nalada == "vazna":
        mx.pridej("harmonie", konec, plocha(noty + [noty[0] - 12], zbyva, 1200, 0.6, 0.05))
        mx.pridej("melodie", konec, klavir(noty[-1] + 12, zbyva, 0.8), 0.6)
        mx.pridej("basa", konec, sub(basovy(koren0, 38), zbyva, 0.9), 0.45)
    elif nalada == "drza":
        for i, m in enumerate(noty):
            mx.pridej("melodie", konec + i * 0.03, pizz(m + 12, 0.9), 0.6)
        mx.pridej("bici", konec, clap(), 0.8)
        mx.pridej("melodie", konec + 0.12, pop(600, 2000, 0.2), 0.4)
        mx.pridej("basa", konec, basa_pluck(basovy(koren0, 36), 0.6, 1.0), 0.6)
    elif nalada == "luxusni":
        for m in noty:
            mx.pridej("klavesy", konec, rhodes(m, zbyva, 0.75), 0.45)
        mx.pridej("harmonie", konec, plocha([m + 12 for m in noty[1:4]], zbyva, 3200, 0.25, 0.3))
        mx.pridej("basa", konec, sub(basovy(koren0), zbyva * 0.6, 0.9), 0.5)
    elif nalada == "pohodova":
        # Tónika (Fmaj9) s kořenem v base, kytara nechá doznít, jemný kopák + tleskání + činel.
        # Zvukové logo: marimba C5 F5 A5 v šestnáctinách, poslední tón přesně na konec (end card).
        tonika = akord(*akordy[0], 62)
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
    kicky.append(konec)

    doby = [round(i * doba, 4) for i in range(int(delka / doba) + 1)]
    takty = [round(i * takt, 4) for i in range(int(delka / takt) + 1)]
    return mx, kicky, dict(bpm=bpm, doba=round(doba, 5), takt=round(takt, 5), drop=round(drop, 4), konec=round(konec, 4),
                           delka=delka, doby=doby, takty=takty, udalosti=udalosti)


NASTAVENI_MIXU = {
    # bus: (hlasitost, dozvuk-send, sidechain)
    "vazna": dict(bici=(0.8, 0.12, False), basa=(0.7, 0.0, True), harmonie=(1.1, 0.35, True), melodie=(1.1, 0.45, False), fx=(0.5, 0.8, False), rt60=3.2),
    "drza": dict(bici=(0.8, 0.06, False), basa=(0.45, 0.0, True), harmonie=(1.3, 0.3, True), melodie=(1.5, 0.18, False), fx=(0.45, 0.5, False), rt60=1.2),
    "luxusni": dict(bici=(0.7, 0.08, False), basa=(0.65, 0.0, True), klavesy=(1.2, 0.3, True), harmonie=(0.9, 0.5, True), fx=(0.45, 0.7, False), rt60=2.6),
    # pohodová: jen lehké „pumpování“ od kopáku (sidechain 0,3), Rhodes s pomalým stereo tremolem v osminách (96 BPM → 3,2 Hz)
    "pohodova": dict(bici=(0.75, 0.07, False), basa=(0.75, 0.0, True), klavesy=(1.0, 0.28, True), kytara=(0.85, 0.22, False),
                     melodie=(0.85, 0.3, False), harmonie=(0.45, 0.35, True), fx=(0.4, 0.6, False), rt60=1.6,
                     sidechain=0.3, tremolo=3.2, vysky_db=4),
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
    out = np.tanh(1.2 * out / (np.max(np.abs(out)) + 1e-9)) / np.tanh(1.2)    # jemné „slepení“
    return out


def uloz(out, delka, cesta):
    n = int(delka * SR)
    out = out[:, :n]
    fade = int(0.25 * SR)
    out[:, -fade:] *= np.linspace(1, 0, fade) ** 2
    out *= 0.9 / (np.max(np.abs(out)) + 1e-9)
    tmp = cesta.with_suffix(".raw.wav")
    from scipy.io import wavfile
    wavfile.write(tmp, SR, (out.T * 32767).astype(np.int16))
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-af", "loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000",
                    "-c:a", "pcm_s16le", str(cesta)], check=True)
    tmp.unlink()


PASMA = [("sub", 20, 60), ("basy", 60, 250), ("stredy", 250, 2000), ("horni_stredy", 2000, 6000), ("vysky", 6000, 20000)]
# Rozumné meze podílu energie (%). Odvozeno z profesionální hudby (R5: sub 20, basy 22, středy 57). Telefon pod ~100 Hz nehraje.
MEZE = {"sub": (0, 30), "stredy": (30, 75)}


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
    return pasma


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
    a = ap.parse_args()
    rng = np.random.default_rng(a.seed)
    bpm = a.bpm or NALADY[a.nalada]["bpm"]
    drop = a.drop if a.drop is not None else a.delka * 0.22
    konec = a.konec if a.konec is not None else a.delka - 2.5
    mx, kicky, info = aranzuj(a.nalada, a.delka, bpm, drop, konec)
    cesta = Path(a.out)
    cesta.parent.mkdir(parents=True, exist_ok=True)
    uloz(mixuj(mx, kicky, a.nalada), a.delka, cesta)
    info["pasma"] = kontrola_pasem(cesta)
    cesta.with_suffix(".json").write_text(json.dumps(info, ensure_ascii=False, indent=1))
    print(f"{cesta}: {a.nalada}, {bpm} BPM, drop {info['drop']} s, konec {info['konec']} s, délka {a.delka} s")


if __name__ == "__main__":
    main()
