"""Přebarvení laku jedoucího vozu ve skutečné stopáži (cesta A, V005; ověřeno testem techniky 2026-11-05).

Princip: 1D LUT z pixelově zarovnaných rendrů konfigurátoru (výchozí lak → cílový lak, stejná kamera) v Lab:
64 binů L zdroje → medián (L, a, b) cíle. Přenese skutečnou odezvu laku (odlesky, stíny), ne plochou barvu.
Aplikuje se jen uvnitř masky karoserie (BiRefNet po snímcích), mimo masku se nemění nic.

Příkazy:
  sleduj DESKA kotvy.json KLÍČ OD DO vyluky.json
       polygony zadané na kotevních snímcích (kotvy.json: {KLÍČ: {"index": [{"nazev", "body": [x, y, …]}]}}) se sledují optickým
       tokem (OpenCV LK + podobnostní transformace RANSAC) po snímcích; mezi kotvami se oba směry prolnou → vyluky.json[KLÍČ] (poly_abs)
  propaguj DESKA DOBRY OD DO   maska z dobrého snímku přenesená homografií na OD–DO (když BiRefNet selže u uříznutého vozu)
  nahled DESKA OUT_DIR vyluky.json KLÍČ i1,i2,… [x0,y0,x1,y1]   kontrolní snímky s obrysy výluk
  lut  RENDER_ZDROJ RENDER_CIL lut.json
       maska laku = kde se rendry liší; uloží i lut_maska.png (kontrola).
  sekvence --deska DIR --lut lut.json --out DIR [volby]
       DIR/src/NNNNN.png (snímky zdroje, název = index snímku) + DIR/maska/NNNNN.png (maska vozu 0–255)
       → OUT/NNNNN.png (kompozit, mimo masku bitově shodný se src) + OUT/_log.json + souhrn měření na stdout.
       --od N --do N           rozsah indexů snímků (včetně); medián masky bere i sousedy mimo rozsah
       --chroma-s 0.8          sytost výsledku × (0,65 rozmazaný průjezd … 0,8 ostrý vůz; dorovnání na medián rendru)
       --chroma-k 0.6          kolik původní odchylky chromy (odlesky krajiny) zůstane
       --lmax 93               horní mez L laku (80 u průjezdů přes nebe: směs s nebem v rozmazu se nemění)
       --l-hladke 0           σ px: posun jasu z rozostřeného L (světlé laky se strmou LUT nezesílí šum zdroje; GT Silver 3)
       --detail 1.0           s --l-hladke / --l-guided: kolik jemné textury jasu zůstane (0,6 = ztlumit šum na světlém laku)
       --l-guided 6,0.01      hladký L hranu zachovávajícím guided filtrem (r px, eps) místo Gausse (GT Silver: šum zdroje se nezesílí)
       --l-baze 14            báze L jen z pixelů laku (σ px), LUT posune bázi, textura projde se sklonem --detail (nezesílí odrazy silnice)
       --l-strop 82           měkké koleno výstupního L (světlý lak nesplyne s nebem)
       --tma 12,26             černé díly / karbon / pneu (L < 12 beze změny, plná váha od 26)
       --uzavreni 5            morfologické uzavření masky v px (díry a „písek“ v masce rozmazu)
       --peri-k 0.5            peří = max(2, k × posun těžiště masky mezi snímky) (sledovací záběr: auto stojí v obraze → menší k)
       --peri-min 2           nejmenší peří hrany masky (px)
       --cerna 12,6           černé díly: kde L < 12 a C < 6 v originále, beze změny (M8 sání)
       --vnitrni 0             eroze masky o (vnitrni × peří) px před rozostřením = peří uvnitř karoserie (bez barevné záře za hranou)
       --peri-hrany            peří měřit i z hran bboxu, když vůz naráží na okraj obrazu (těžiště pak stojí)
       --spz auto              výluka SPZ prahováním po snímcích (světlý obdélník s nízkou chromou, poměr stran 2,5–6,5)
       --vyluky vyluky.json --klic KÓD   výluky (světla, ráfky…): ellipse / rect v souřadnicích bboxu masky 0–1,
                               nebo ellipse_abs / rect_abs / poly_abs v px s klíčovými snímky {"index": hodnoty}
       --jen-v kolo.json       naopak: měnit JEN uvnitř těchto oblastí (např. ráfek kola), formát jako výluky
Chování (z testu): časový medián masky 3 snímky (proti blikání), eroze 1 px, peří hrany = max(2 px, 0,5 × posun
vozu mezi snímky) = délka pohybového rozmazání; výpočet jen ve výřezu bboxu masky (+ okraj), zbytek snímku se kopíruje.
Měření: blikání = změna průměrného L v masce mezi sousedními snímky výstupu MINUS změna zdroje (%), ΔE76 mediánu laku proti
mediánu rendru cíle, peří. Kritéria V005: blikání < 2 % (mimo rozmaz), ΔE < 12.
"""
import sys, json, os, argparse, numpy as np
from PIL import Image, ImageFilter, ImageDraw
from skimage import color
from scipy.ndimage import gaussian_filter1d, gaussian_filter, label, find_objects

def lab(a):
    return color.rgb2lab(np.asarray(a, dtype=np.float32) / 255.0)

# ---------- LUT ----------
def postav_lut(src, dst, out):
    a, b = lab(Image.open(src).convert('RGB')), lab(Image.open(dst).convert('RGB'))
    m = np.abs(a - b).sum(axis=2) > 6                        # lak = kde se rendry liší (pneu, sklo, světla, pozadí jsou shodné)
    mi = Image.fromarray((m * 255).astype(np.uint8)).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.MaxFilter(3))
    m = np.asarray(mi) > 127
    L, A, B = (a[..., i][m] for i in range(3)); L2, A2, B2 = (b[..., i][m] for i in range(3))
    bins = 64; idx = np.clip((L / 100 * bins).astype(int), 0, bins - 1); tab = []
    for i in range(bins):
        sel = idx == i
        tab.append(None if sel.sum() < 30 else [float(np.median(v[sel])) for v in (L, A, B, L2, A2, B2)] + [int(sel.sum())])
    known = [i for i, t in enumerate(tab) if t]
    for i in range(bins):
        if tab[i] is None:
            tab[i] = tab[min(known, key=lambda k: abs(k - i))][:6] + [0]
    json.dump({'bins': bins, 'tab': tab, 'n': int(m.sum()), 'src': os.path.basename(src), 'dst': os.path.basename(dst),
               'cil_median': [float(np.median(v)) for v in (L2, A2, B2)]}, open(out, 'w'))
    Image.fromarray((m * 255).astype(np.uint8)).save(out.replace('.json', '_maska.png'))
    print('lut', out, 'pixelů laku', int(m.sum()), 'binů s daty', len(known), 'medián cíle Lab', [round(float(np.median(v)), 1) for v in (L2, A2, B2)])

def nacti_lut(lutf):
    lut = json.load(open(lutf)); tab = np.array([t[:6] for t in lut['tab']], dtype=np.float32)
    tab = gaussian_filter1d(tab, 1.5, axis=0, mode='nearest')          # hladké biny (proti posterizaci)
    c = (np.arange(len(tab)) + 0.5) * 100 / len(tab)
    tab[:, 3] = tab[:, 0] + np.maximum.accumulate(tab[:, 3] - tab[:, 0] + c) - c   # monotónní L
    return tab, c, lut

def vaha_laku(L, A, B, tma=(12, 26), Lmax=93):
    chroma = np.sqrt(A * A + B * B)   # černé díly (L < tma[0]) a sytě barevné (světla, třmeny, pruh) zůstávají; Lmax = směs s nebem
    return np.clip((L - tma[0]) / (tma[1] - tma[0]), 0, 1) * np.clip((Lmax - L) / 5, 0, 1) * np.clip((22 - chroma) / 8, 0, 1)

def guided(I, r, eps):
    """Guided filter (He 2010) s vodítkem = vstup, box r px; I v 0–1. Hladí plochy, drží hrany (odlesky, spáry karoserie)."""
    from scipy.ndimage import uniform_filter
    k = 2 * int(r) + 1
    m = uniform_filter(I, k); v = uniform_filter(I * I, k) - m * m
    a = v / (v + eps); b = m - a * m
    return uniform_filter(a, k) * I + uniform_filter(b, k)

def koleno(L, strop, sirka=8.0):
    """Měkké koleno: pod (strop − šířka) beze změny, nad ním se L plynule blíží stropu (víko světlého laku nesplyne s nebem)."""
    k0 = strop - sirka
    return np.where(L <= k0, L, k0 + sirka * (1 - np.exp(-(L - k0) / sirka)))

def aplikuj(x, tab, c, w, chroma_k=0.6, chroma_blur=2.5, chroma_s=1.0, l_hladke=0.0, detail=1.0, l_guided=None, l_strop=None, l_baze=0.0):
    L, A, B = x[..., 0], x[..., 1], x[..., 2]
    # l_hladke > 0: posun L i barva se čtou z rozostřeného L (σ px), jemná textura projde se sklonem 1 → LUT se strmou křivkou (světlé laky)
    # nezesílí šum a kompresní bloky zdroje (V005: GT Silver vypadal „špinavě“)
    # l_guided (r, eps): místo Gausse hranu zachovávající guided filter (V005 oprava KŘ: GT Silver „otlučený plech“ = zesílený šum zdroje)
    # l_baze σ: báze jen z pixelů laku (normalizovaný Gauss vážený w, bez halo u černých dílů); textura L − báze projde se sklonem `detail`
    # → strmá LUT světlého laku posune jas plochy, ale nezesílí skvrny odrazů silnice (V005 GT Silver, oprava KŘ 1)
    if l_baze > 0:
        ww = np.clip(w, 1e-3, 1); Lr = gaussian_filter(L * ww, l_baze) / np.maximum(gaussian_filter(ww, l_baze), 1e-3)
    elif l_guided: Lr = guided(L / 100.0, l_guided[0], l_guided[1]) * 100.0
    else: Lr = gaussian_filter(L, l_hladke) if l_hladke > 0 else L
    outL = np.clip(Lr + (L - Lr) * detail + np.interp(Lr, c, tab[:, 3] - tab[:, 0]), 0, 100)   # detail < 1 ztlumí jemnou texturu (šum zdroje) uvnitř laku
    if l_strop: outL = koleno(outL, l_strop)
    outA = np.interp(Lr, c, tab[:, 4]) + (A - np.interp(Lr, c, tab[:, 1])) * chroma_k
    outB = np.interp(Lr, c, tab[:, 5]) + (B - np.interp(Lr, c, tab[:, 2])) * chroma_k
    if chroma_blur > 0:
        outA = gaussian_filter(outA, chroma_blur); outB = gaussian_filter(outB, chroma_blur)
    outA = outA * chroma_s; outB = outB * chroma_s
    y = np.stack([L + (outL - L) * w, A + (outA - A) * w, B + (outB - B) * w], axis=2)
    return y

# ---------- oblasti (výluky / jen-v) ----------
def kf_abs(kfs, i):
    ks = sorted((int(k), v) for k, v in kfs.items())
    if i <= ks[0][0]: return ks[0][1]
    for (k0, v0), (k1, v1) in zip(ks, ks[1:]):
        if i <= k1:
            u = (i - k0) / (k1 - k0); return [p + (q - p) * u for p, q in zip(v0, v1)]
    return ks[-1][1]

def oblasti(shape, bbox, regiony, i, rozmaz=3):
    im = Image.new('L', (shape[1], shape[0]), 0); d = ImageDraw.Draw(im)
    x0, y0, x1, y1 = bbox; W, H = x1 - x0, y1 - y0
    for r in regiony:
        t = r['typ']
        if t == 'ellipse_abs':
            cx, cy, rx, ry = kf_abs(r['kf'], i); d.ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill=255)
        elif t == 'poly_abs':
            p = kf_abs(r['kf'], i)
            for dy in range(0, int(r.get('nahoru', 0)) + 1, 2):                      # 'nahoru': N = polygon protažený o N px nahoru (rám nad sklem)
                d.polygon([(p[k], p[k + 1] - dy) for k in range(0, len(p), 2)], fill=255)
        elif t == 'rect_abs':
            d.rectangle(kf_abs(r['kf'], i), fill=255)
        elif t == 'rect':
            a, b, c, e = r['xy']; d.rectangle([x0 + a * W, y0 + b * H, x0 + c * W, y0 + e * H], fill=255)
        else:
            cx, cy, rx, ry = r['xy']; d.ellipse([x0 + (cx - rx) * W, y0 + (cy - ry) * H, x0 + (cx + rx) * W, y0 + (cy + ry) * H], fill=255)
    return np.asarray(im.filter(ImageFilter.GaussianBlur(rozmaz)), dtype=np.float32) / 255.0

def najdi_spz(x, mb):
    """SPZ po snímcích: světlý (L > 62) a nebarevný (chroma < 12) obdélník uvnitř masky, poměr stran 2,5–6,5, vyplnění > 0,5.
    Vrací [x0, y0, x1, y1] nebo None (pak se použije soused)."""
    L, A, B = x[..., 0], x[..., 1], x[..., 2]
    sv = (L > 62) & (np.hypot(A, B) < 12) & mb
    sv = np.asarray(Image.fromarray((sv * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.MinFilter(5))) > 127   # spojit písmena
    lab_, n = label(sv); nej = None
    for k, sl in enumerate(find_objects(lab_)):
        h, w = sl[0].stop - sl[0].start, sl[1].stop - sl[1].start
        if w < 24 or h < 6: continue
        fill = (lab_[sl] == k + 1).mean(); pomer = w / h
        if 2.5 <= pomer <= 6.5 and fill > 0.5:
            sk = w * h * fill
            if nej is None or sk > nej[0]: nej = (sk, [sl[1].start, sl[0].start, sl[1].stop, sl[0].stop])
    return None if nej is None else nej[1]

# ---------- sekvence ----------
def sekvence(a):
    tab, cen, lut = nacti_lut(a.lut)
    srcd, mskd = os.path.join(a.deska, 'src'), os.path.join(a.deska, 'maska')
    os.makedirs(a.out, exist_ok=True)
    idx = sorted(int(f[:5]) for f in os.listdir(mskd) if f.endswith('.png') and os.path.exists(os.path.join(srcd, f)))
    if not idx: sys.exit('žádné masky v ' + mskd)
    od = a.od if a.od is not None else idx[0]; do_ = a.do if a.do is not None else idx[-1]
    tma = tuple(float(v) for v in a.tma.split(','))
    reg = json.load(open(a.vyluky)).get(a.klic, []) if a.vyluky else []
    jen = json.load(open(a.jen_v)).get(a.klic, []) if a.jen_v else []
    cache = {}
    def maska(n):
        if n not in cache: cache[n] = np.asarray(Image.open(os.path.join(mskd, f'{n:05d}.png')).convert('L'))
        return cache[n]
    log = []; prev = None; spz_prev = None
    for n in [i for i in idx if od - 1 <= i <= do_]:
        trojice = [maska(k) for k in (n - 1, n, n + 1) if k in idx]
        m = np.median(np.stack(trojice), axis=0) if len(trojice) == 3 else maska(n).astype(np.float32)
        mi = Image.fromarray(m.astype(np.uint8))
        if a.uzavreni: mi = mi.filter(ImageFilter.MaxFilter(a.uzavreni)).filter(ImageFilter.MinFilter(a.uzavreni))
        mi = mi.filter(ImageFilter.MinFilter(3))                                                       # eroze 1 px
        mb = np.asarray(mi) > 127
        if mb.sum() < 300:
            log.append({'n': n, 'prazdne': True}); prev = None; continue
        ys, xs = np.where(mb); bbox = (int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max())); c = (xs.mean(), ys.mean())
        posun = 0.0 if prev is None else float(np.hypot(c[0] - prev[0][0], c[1] - prev[0][1]))
        Hh, Ww = mb.shape
        if prev is not None and a.peri_hrany and (bbox[0] <= 2 or bbox[1] <= 2 or bbox[2] >= Ww - 3 or bbox[3] >= Hh - 3):
            lim = (Ww, Hh, Ww, Hh)
            hr = [abs(bbox[k] - prev[1][k]) for k in range(4) if 2 < bbox[k] < lim[k] - 3 and 2 < prev[1][k] < lim[k] - 3]
            posun = max([posun] + hr)
        if prev is None and log and 'posun' in log[-1]: posun = log[-1]['posun']
        prev = (c, bbox)
        if n < od or n > do_: continue
        peri = max(a.peri_min, a.peri_k * posun)
        # výřez = bbox + okraj (peří, chroma blur)
        okr = int(3 * peri + 16)
        X0, Y0, X1, Y1 = max(0, bbox[0] - okr), max(0, bbox[1] - okr), min(Ww, bbox[2] + okr + 1), min(Hh, bbox[3] + okr + 1)
        mc = mi.crop((X0, Y0, X1, Y1))
        ero = int(round(a.vnitrni * peri))
        if ero >= 1: mc = mc.filter(ImageFilter.MinFilter(2 * ero + 1))                                # vnitřní peří: 50 % hrany o ero px dovnitř (proti „záři“ za hranou)
        mk = np.asarray(mc.filter(ImageFilter.GaussianBlur(peri)), dtype=np.float32) / 255.0
        src = Image.open(os.path.join(srcd, f'{n:05d}.png')).convert('RGB'); S = np.asarray(src)
        x = lab(S[Y0:Y1, X0:X1])
        w = vaha_laku(x[..., 0], x[..., 1], x[..., 2], tma, a.lmax) * mk
        if a.cerna:                                                                                   # černé díly (sání, mřížky): L < L0 a C < C0 beze změny
            l0, c0 = (float(v) for v in a.cerna.split(','))
            cer = ((x[..., 0] < l0) & (np.hypot(x[..., 1], x[..., 2]) < c0)).astype(np.float32)
            w = w * (1 - np.clip(gaussian_filter(cer, 1.0) * 1.5, 0, 1))
        bb_rel = (bbox[0] - X0, bbox[1] - Y0, bbox[2] - X0, bbox[3] - Y0)
        rel = lambda rr: [dict(r, kf={k: posun_kf(v, X0, Y0, r['typ']) for k, v in r['kf'].items()}) if 'kf' in r else r for r in rr]
        reg_n = [r for r in reg if 'tmave' not in r]; reg_t = [r for r in reg if 'tmave' in r]
        if reg_n: w = w * (1 - oblasti(mk.shape, bb_rel, rel(reg_n), n))
        for r in reg_t:                                                                           # 'tmave': dL = v oblasti vyloučit jen pixely tmavší než okolní lak − dL
            R = oblasti(mk.shape, bb_rel, rel([r]), n, rozmaz=1)                               # (odhalený karbon kapoty; lakované okraje víka se přebarví)
            Rb = R > 0.5
            okoli = np.asarray(Image.fromarray((Rb * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(51)), dtype=bool) & ~Rb & (w > 0.5)
            if okoli.sum() < 50: w = w * (1 - R); continue
            Lref = float(np.median(x[..., 0][okoli]))
            cond = gaussian_filter(np.clip((Lref - r['tmave'] - x[..., 0]) / 6 + 0.5, 0, 1), 1.5)
            w = w * (1 - R * cond)
        if jen: w = w * oblasti(mk.shape, bb_rel, [dict(r, kf={k: posun_kf(v, X0, Y0, r['typ']) for k, v in r['kf'].items()}) if 'kf' in r else r for r in jen], n, rozmaz=a.jen_rozmaz)
        spz = None
        if a.spz == 'auto':
            spz = najdi_spz(x, mb[Y0:Y1, X0:X1])
            if spz is None and spz_prev is not None: spz = spz_prev
            if spz is not None:
                spz_prev = spz
                d = 4; z = np.zeros_like(w); z[max(0, spz[1] - d):spz[3] + d, max(0, spz[0] - d):spz[2] + d] = 1
                w = w * (1 - gaussian_filter(z, 1.5))
        y = aplikuj(x, tab, cen, w, a.chroma_k, chroma_s=a.chroma_s, l_hladke=a.l_hladke, detail=a.detail,
                    l_guided=[float(v) for v in a.l_guided.split(',')] if a.l_guided else None, l_strop=a.l_strop, l_baze=a.l_baze)
        out = S.copy(); out[Y0:Y1, X0:X1] = np.clip(color.lab2rgb(y) * 255 + 0.5, 0, 255).astype(np.uint8)
        Image.fromarray(out).save(os.path.join(a.out, f'{n:05d}.png'))
        sel = w > 0.5
        if sel.sum() < 50: log.append({'n': n, 'malo_laku': int(sel.sum())}); continue
        log.append({'n': n, 'posun': round(posun, 1), 'peri': round(peri, 1), 'bbox': list(bbox), 'px_laku': int(sel.sum()),
                    'spz': None if spz is None else [spz[0] + X0, spz[1] + Y0, spz[2] + X0, spz[3] + Y0],
                    'L_in': round(float(x[..., 0][sel].mean()), 2), 'L_out': round(float(y[..., 0][sel].mean()), 2),
                    'lab_out': [round(float(np.median(y[..., k][sel])), 1) for k in range(3)]})
    cil = lut['cil_median']; r = [q for q in log if 'L_out' in q]
    bl = []
    for p, q in zip(r, r[1:]):
        if q['n'] != p['n'] + 1: continue
        bl.append(abs((q['L_out'] - p['L_out']) / max(p['L_out'], 1) - (q['L_in'] - p['L_in']) / max(p['L_in'], 1)) * 100)
    de = [float(np.linalg.norm(np.array(q['lab_out']) - np.array(cil))) for q in r]
    souhrn = {'lut': os.path.basename(a.lut), 'snimku': len(r), 'od': od, 'do': do_, 'blikani_max_pct': round(max(bl), 2) if bl else 0,
              'blikani_median_pct': round(float(np.median(bl)), 2) if bl else 0, 'dE_median': round(float(np.median(de)), 1) if de else None,
              'dE_max': round(max(de), 1) if de else None, 'peri': [min(q['peri'] for q in r), max(q['peri'] for q in r)] if r else None,
              'cil_render_lab': [round(v, 1) for v in cil], 'parametry': {k: v for k, v in vars(a).items() if k not in ('cmd',)}}
    json.dump({'souhrn': souhrn, 'snimky': log}, open(os.path.join(a.out, '_log.json'), 'w'), indent=0, ensure_ascii=False)
    print(json.dumps(souhrn, ensure_ascii=False))

def posun_kf(v, X0, Y0, typ):
    v = list(v)
    if typ == 'ellipse_abs': return [v[0] - X0, v[1] - Y0, v[2], v[3]]
    if typ == 'rect_abs': return [v[0] - X0, v[1] - Y0, v[2] - X0, v[3] - Y0]
    return [p - (X0 if k % 2 == 0 else Y0) for k, p in enumerate(v)]          # poly_abs

# ---------- sledování oblastí (výluky SPZ, světel, skla…) optickým tokem ----------
def sleduj(deska, kotvy_f, klic, od, do_, out_f):
    """Oblasti (polygony v px) zadané na jednom nebo více kotevních snímcích se po snímcích posouvají podobnostní transformací
    odhadnutou z optického toku (LK) bodů uvnitř oblasti rozšířené o 40 px a omezené maskou vozu. Mezi dvěma kotvami se
    výsledky obou směrů prolnou lineárně (drift se nesčítá). Zápis: out_f[klic] = [{typ: poly_abs, nazev, kf: {index: body}}]."""
    import cv2
    kotvy = json.load(open(kotvy_f))[klic]          # {"index": [{"nazev":…, "body":[x,y,…]}, …], …}
    ks = sorted(int(k) for k in kotvy); idx = list(range(od, do_ + 1))
    sed = {}
    def nacti(n):
        if n not in sed:
            g = cv2.cvtColor(cv2.imread(os.path.join(deska, 'src', f'{n:05d}.png')), cv2.COLOR_BGR2GRAY)
            mp = os.path.join(deska, 'maska', f'{n:05d}.png')
            m = cv2.imread(mp, 0) if os.path.exists(mp) else np.full(g.shape, 255, np.uint8)
            sed[n] = (g, m)
        return sed[n]
    def krok(pts, a, b):
        ga, ma = nacti(a); gb, _ = nacti(b)
        P = np.array(pts, np.float32).reshape(-1, 2)
        x0, y0 = P.min(0) - 40; x1, y1 = P.max(0) + 40
        roi = np.zeros_like(ga); roi[int(max(0, y0)):int(y1), int(max(0, x0)):int(x1)] = 255
        roi = cv2.bitwise_and(roi, cv2.erode(ma, np.ones((5, 5), np.uint8)) if ma is not None else roi)
        f = cv2.goodFeaturesToTrack(ga, 200, 0.01, 5, mask=roi)
        if f is None or len(f) < 6: return pts
        f2, st, _ = cv2.calcOpticalFlowPyrLK(ga, gb, f, None, winSize=(21, 21), maxLevel=3)
        ok = st.ravel() == 1
        if ok.sum() < 6: return pts
        M, inl = cv2.estimateAffinePartial2D(f[ok], f2[ok], method=cv2.RANSAC, ransacReprojThreshold=2.0)
        if M is None: return pts
        Q = (np.hstack([P, np.ones((len(P), 1), np.float32)]) @ M.T)
        return Q.ravel().tolist()
    globalni = os.environ.get('SLEDUJ', 'H') == 'H'     # H = jedna homografie z bodů celé karoserie (stabilnější: sklo a řidič se hýbou jinak), jinak po oblastech
    Hcache = {}
    def krokH(pts, a, b):
        if (a, b) not in Hcache:
            ga, ma = nacti(a); gb, _ = nacti(b)
            roi = cv2.erode(ma, np.ones((9, 9), np.uint8))
            f = cv2.goodFeaturesToTrack(ga, 600, 0.005, 6, mask=roi)
            M = None
            if f is not None and len(f) >= 12:
                f2, st, _ = cv2.calcOpticalFlowPyrLK(ga, gb, f, None, winSize=(25, 25), maxLevel=4)
                ok = st.ravel() == 1
                if ok.sum() >= 12: M, _ = cv2.findHomography(f[ok], f2[ok], cv2.RANSAC, 2.5)
            Hcache[(a, b)] = M
        M = Hcache[(a, b)]
        if M is None: return pts
        P = np.array(pts, np.float32).reshape(-1, 1, 2)
        return cv2.perspectiveTransform(P, M).ravel().tolist()
    if globalni: krok = krokH
    vysl = {}                                          # nazev → {n: [směr_od_kotvy, body]}
    for k in ks:
        for obl in kotvy[str(k)]:
            nm = obl['nazev']; vysl.setdefault(nm, {})
            for smer in (1, -1):
                pts = obl['body']; n = k
                while True:
                    vysl[nm].setdefault(n, []).append((k, pts))
                    m = n + smer
                    if m < od or m > do_: break
                    if smer == 1 and any(kk > k and m > kk for kk in ks): break
                    if smer == -1 and any(kk < k and m < kk for kk in ks): break
                    pts = krok(pts, n, m); n = m
                print(nm, 'kotva', k, 'směr', smer, 'hotovo', flush=True)
    res = []
    for nm, d in vysl.items():
        kf = {}
        for n, lst in d.items():
            if len(lst) == 1: kf[str(n)] = [round(v, 1) for v in lst[0][1]]; continue
            (ka, pa), (kb, pb) = sorted(lst)[:2]
            u = (n - ka) / (kb - ka) if kb != ka else 0
            kf[str(n)] = [round(p + (q - p) * u, 1) for p, q in zip(pa, pb)]
        res.append({'typ': 'poly_abs', 'nazev': nm, 'kf': kf})
    vse = json.load(open(out_f)) if os.path.exists(out_f) else {}
    vse[klic] = res; json.dump(vse, open(out_f, 'w'), indent=0)
    print('sledováno', klic, len(res), 'oblastí', od, '–', do_, '→', out_f)

def propaguj(deska, dobry, cil_od, cil_do):
    """Oprava masky tam, kde BiRefNet selže (vůz uříznutý okrajem obrazu): maska dobrého snímku se po snímcích přenese
    homografií z optického toku bodů uvnitř masky (vůz je tuhý). Původní masky se zálohují do maska_birefnet/."""
    import cv2, shutil
    zal = os.path.join(deska, 'maska_birefnet'); os.makedirs(zal, exist_ok=True)
    smer = -1 if cil_do < dobry else 1
    rng = range(dobry + smer, (cil_od if smer < 0 else cil_do) + smer, smer)
    m = cv2.imread(os.path.join(deska, 'maska', f'{dobry:05d}.png'), 0); n0 = dobry
    for n in rng:
        ga = cv2.cvtColor(cv2.imread(os.path.join(deska, 'src', f'{n0:05d}.png')), cv2.COLOR_BGR2GRAY)
        gb = cv2.cvtColor(cv2.imread(os.path.join(deska, 'src', f'{n:05d}.png')), cv2.COLOR_BGR2GRAY)
        f = cv2.goodFeaturesToTrack(ga, 600, 0.005, 6, mask=cv2.erode(m, np.ones((9, 9), np.uint8)))
        f2, st, _ = cv2.calcOpticalFlowPyrLK(ga, gb, f, None, winSize=(25, 25), maxLevel=4)
        ok = st.ravel() == 1
        M, _ = cv2.findHomography(f[ok], f2[ok], cv2.RANSAC, 2.5)
        m = cv2.warpPerspective(m, M, (m.shape[1], m.shape[0]), flags=cv2.INTER_LINEAR)
        dst = os.path.join(deska, 'maska', f'{n:05d}.png')
        if os.path.exists(dst) and not os.path.exists(os.path.join(zal, f'{n:05d}.png')): shutil.copy(dst, zal)
        cv2.imwrite(dst, m); n0 = n
        print('maska', n, 'z', dobry, 'bodů', int(ok.sum()), flush=True)

def nahled(deska, out_dir, vyluky_f, klic, indexy, krop=None):
    """Kontrolní obrázek: výluky (zeleně) přes snímek zdroje."""
    reg = json.load(open(vyluky_f)).get(klic, [])
    for n in indexy:
        im = Image.open(os.path.join(deska, 'src', f'{n:05d}.png')).convert('RGB'); d = ImageDraw.Draw(im)
        for r in reg:
            p = kf_abs(r['kf'], n); d.polygon([(p[k], p[k + 1]) for k in range(0, len(p), 2)], outline=(0, 255, 0))
        if krop: im = im.crop(krop)
        im.save(os.path.join(out_dir, f'{klic}_{n:05d}.jpg'), quality=85)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'sleduj':
        sleduj(sys.argv[2], sys.argv[3], sys.argv[4], int(sys.argv[5]), int(sys.argv[6]), sys.argv[7]); sys.exit()
    if len(sys.argv) > 1 and sys.argv[1] == 'propaguj':
        propaguj(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])); sys.exit()
    if len(sys.argv) > 1 and sys.argv[1] == 'nahled':
        nahled(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], [int(v) for v in sys.argv[6].split(',')],
               tuple(int(v) for v in sys.argv[7].split(',')) if len(sys.argv) > 7 else None); sys.exit()
    if len(sys.argv) > 1 and sys.argv[1] == 'lut':
        postav_lut(*sys.argv[2:5]); sys.exit()
    p = argparse.ArgumentParser(description='sekvence: přebarvení laku v masce')
    p.add_argument('cmd', choices=['sekvence'])
    p.add_argument('--deska', required=True); p.add_argument('--lut', required=True); p.add_argument('--out', required=True)
    p.add_argument('--od', type=int); p.add_argument('--do', type=int)
    p.add_argument('--chroma-s', type=float, default=0.8); p.add_argument('--chroma-k', type=float, default=0.6)
    p.add_argument('--lmax', type=float, default=93); p.add_argument('--tma', default='12,26')
    p.add_argument('--l-hladke', type=float, default=0.0); p.add_argument('--detail', type=float, default=1.0)
    p.add_argument('--l-guided', help='r,eps: guided filter L (r px, eps pro L 0–1), např. 6,0.01'); p.add_argument('--l-strop', type=float, help='měkké koleno výstupního L (např. 82)')
    p.add_argument('--l-baze', type=float, default=0.0, help='σ px: báze L jen z laku (normalizovaný Gauss), textura se sklonem --detail')
    p.add_argument('--peri-min', type=float, default=2.0); p.add_argument('--cerna', help='L0,C0: černé díly (L < L0 a C < C0) beze změny')
    p.add_argument('--peri-k', type=float, default=0.5); p.add_argument('--vnitrni', type=float, default=0.0)
    p.add_argument('--uzavreni', type=int, default=5); p.add_argument('--peri-hrany', action='store_true')
    p.add_argument('--spz', default='auto', choices=['auto', 'ne'])
    p.add_argument('--vyluky'); p.add_argument('--jen-v'); p.add_argument('--jen-rozmaz', type=float, default=3); p.add_argument('--klic', default='')
    sekvence(p.parse_args())
