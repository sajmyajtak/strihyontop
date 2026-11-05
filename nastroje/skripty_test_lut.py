"""Test V005 (cesta A): přebarvení laku jedoucího vozu 1D LUTem z pixelově zarovnaných rendrů konfigurátoru (1H → cíl) v Lab.
  build ZDROJ.webp CIL.webp lut.json                       LUT: 64 binů L zdroje → medián (L,a,b) cíle, maska laku = kde se rendry liší
  batch KLIP lut.json SRC_DIR MASK_DIR OUT_DIR [vyluky.json] [chroma_k]   sekvence: medián masky 3 snímky, eroze 1 px, peří = max(2, 0,5×posun),
                                                           výluky (ráfky, SPZ, světla) v souřadnicích normalizovaných na bbox masky, zápis kompozitu + masky + log"""
import sys, json, glob, os, numpy as np
from PIL import Image, ImageFilter, ImageDraw
from skimage import color
from scipy.ndimage import gaussian_filter1d

def lab(im):
    return color.rgb2lab(np.asarray(im.convert('RGB'), dtype=np.float32) / 255.0)

def build(src, dst, out):
    a, b = lab(Image.open(src)), lab(Image.open(dst))
    m = np.abs(a - b).sum(axis=2) > 6                      # lak = kde se rendry liší (pneu, sklo, světla, pozadí jsou shodné)
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
    json.dump({'bins': bins, 'tab': tab, 'n': int(m.sum()), 'src': src, 'dst': dst,
               'cil_median': [float(np.median(v)) for v in (L2, A2, B2)]}, open(out, 'w'))
    Image.fromarray((m * 255).astype(np.uint8)).save(out.replace('.json', '_maska.png'))
    print('lut', out, 'pixelů laku', int(m.sum()), 'binů s daty', len(known))

def nacti_lut(lutf):
    lut = json.load(open(lutf)); tab = np.array([t[:6] for t in lut['tab']], dtype=np.float32)
    tab = gaussian_filter1d(tab, 1.5, axis=0, mode='nearest')           # hladké biny (proti posterizaci)
    dL = np.maximum.accumulate(tab[:, 3] - tab[:, 0] + (np.arange(len(tab)) + 0.5) * 100 / len(tab)) - (np.arange(len(tab)) + 0.5) * 100 / len(tab)
    tab[:, 3] = tab[:, 0] + dL                                            # monotónní L
    return tab, (np.arange(len(tab)) + 0.5) * 100 / len(tab), lut

def vaha_laku(L, A, B, tma=(12, 26)):
    chroma = np.sqrt(A * A + B * B)   # tma: černé díly a karbon (L < tma[0]) zůstávají, plná váha od tma[1]
    return np.clip((L - tma[0]) / (tma[1] - tma[0]), 0, 1) * np.clip((93 - L) / 5, 0, 1) * np.clip((22 - chroma) / 8, 0, 1)

def aplikuj(x, tab, centers, w, chroma_k=0.6, chroma_blur=2.5):
    L, A, B = x[..., 0], x[..., 1], x[..., 2]
    outL = np.clip(L + np.interp(L, centers, tab[:, 3] - tab[:, 0]), 0, 100)
    outA = np.interp(L, centers, tab[:, 4]) + (A - np.interp(L, centers, tab[:, 1])) * chroma_k
    outB = np.interp(L, centers, tab[:, 5]) + (B - np.interp(L, centers, tab[:, 2])) * chroma_k
    if chroma_blur > 0:
        from scipy.ndimage import gaussian_filter
        outA = gaussian_filter(outA, chroma_blur); outB = gaussian_filter(outB, chroma_blur)
    y = np.stack([L + (outL - L) * w, A + (outA - A) * w, B + (outB - B) * w], axis=2)
    return np.clip(color.lab2rgb(y) * 255 + 0.5, 0, 255).astype(np.uint8)

def kf_abs(kfs, i):
    ks = sorted((int(k), v) for k, v in kfs.items())
    if i <= ks[0][0]: return ks[0][1]
    for (k0, v0), (k1, v1) in zip(ks, ks[1:]):
        if i <= k1:
            u = (i - k0) / (k1 - k0); return [a + (b - a) * u for a, b in zip(v0, v1)]
    return ks[-1][1]

def vyluky_obraz(shape, bbox, regiony, i=0):
    im = Image.new('L', (shape[1], shape[0]), 0); d = ImageDraw.Draw(im)
    x0, y0, x1, y1 = bbox; W, H = x1 - x0, y1 - y0
    for r in regiony:
        if r['typ'] == 'ellipse_abs':      # absolutní px, klíčové snímky podle indexu snímku (sledovaná elipsa)
            cx, cy, rx, ry = kf_abs(r['kf'], i); d.ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill=255)
        elif r['typ'] == 'poly_abs':       # polygon v px, body klíčované po snímcích (světlomet)
            pts = kf_abs(r['kf'], i); d.polygon([(pts[k], pts[k + 1]) for k in range(0, len(pts), 2)], fill=255)
        elif r['typ'] == 'rect_abs':
            d.rectangle(kf_abs(r['kf'], i), fill=255)
        elif r['typ'] == 'rect':
            a, b, c, e = r['xy']; d.rectangle([x0 + a * W, y0 + b * H, x0 + c * W, y0 + e * H], fill=255)
        else:
            cx, cy, rx, ry = r['xy']; d.ellipse([x0 + (cx - rx) * W, y0 + (cy - ry) * H, x0 + (cx + rx) * W, y0 + (cy + ry) * H], fill=255)
    return np.asarray(im.filter(ImageFilter.GaussianBlur(3)), dtype=np.float32) / 255.0

def batch(klip, lutf, srcdir, maskdir, outdir, vylukyf=None, chroma_k=0.6, tma=(12, 26)):
    tab, centers, lut = nacti_lut(lutf); barva = os.path.basename(lutf).split('_')[0]
    os.makedirs(outdir, exist_ok=True)
    regiony = json.load(open(vylukyf)).get(klip, []) if vylukyf else []
    files = [f for f in sorted(glob.glob(os.path.join(srcdir, klip + '_*.png'))) if os.path.exists(os.path.join(maskdir, os.path.basename(f)))]
    masks = [np.asarray(Image.open(os.path.join(maskdir, os.path.basename(f))).convert('L')) for f in files]
    log = []; prev_c = None; kum = None
    for i, f in enumerate(files):
        trojice = masks[max(0, i - 1):i + 2]
        m = np.median(np.stack(trojice), axis=0) if len(trojice) == 3 else masks[i].astype(np.float32)   # časový medián 3 snímky
        mi = Image.fromarray(m.astype(np.uint8)).filter(ImageFilter.MinFilter(3))                       # eroze 1 px
        mb = np.asarray(mi) > 127
        if mb.sum() < 500:
            log.append({'i': i, 'prazdne': True}); continue
        ys, xs = np.where(mb); bbox = (xs.min(), ys.min(), xs.max(), ys.max()); c = (xs.mean(), ys.mean())
        posun = 0 if prev_c is None else float(np.hypot(c[0] - prev_c[0], c[1] - prev_c[1])); prev_c = c
        peri = max(2.0, 0.5 * posun)
        mk = np.asarray(mi.filter(ImageFilter.GaussianBlur(peri)), dtype=np.float32) / 255.0
        x = lab(Image.open(f)); w = vaha_laku(x[..., 0], x[..., 1], x[..., 2], tma) * mk
        if regiony: w = w * (1 - vyluky_obraz(mb.shape, bbox, regiony, i))
        rgb = aplikuj(x, tab, centers, w, chroma_k)
        Image.fromarray(rgb).save(os.path.join(outdir, f'{klip}_{barva}_{os.path.basename(f)[-7:-4]}.png'))
        Image.fromarray((mk * 255).astype(np.uint8)).save(os.path.join(outdir, f'{klip}_maska_{i:03d}.png'))
        kum = mk if kum is None else np.maximum(kum, mk)
        Image.fromarray((kum * 255).astype(np.uint8)).save(os.path.join(outdir, f'{klip}_kum_{i:03d}.png'))
        y = lab(Image.fromarray(rgb)); sel = w > 0.5
        log.append({'i': i, 'posun': round(posun, 1), 'peri': round(peri, 1), 'bbox': [int(v) for v in bbox],
                    'L_in': round(float(x[..., 0][sel].mean()), 2), 'L_out': round(float(y[..., 0][sel].mean()), 2),
                    'lab_out': [round(float(np.median(y[..., k][sel])), 1) for k in range(3)], 'lab_cil': [round(v, 1) for v in lut['cil_median']]})
    json.dump(log, open(os.path.join(outdir, f'{klip}_{barva}_log.json'), 'w'), indent=0)
    Ls = [r['L_out'] for r in log if 'L_out' in r]
    dl = [abs(Ls[k + 1] - Ls[k]) / max(Ls[k], 1) * 100 for k in range(len(Ls) - 1)]
    print(klip, barva, 'snímků', len(Ls), 'max ΔL mezi snímky %.2f %%' % (max(dl) if dl else 0), 'peří', [r['peri'] for r in log if 'peri' in r][:6], '…',
          'median Lab out', log[len(log)//2].get('lab_out'), 'cíl render', log[0].get('lab_cil'))

if __name__ == '__main__':
    if sys.argv[1] == 'build': build(*sys.argv[2:5])
    elif sys.argv[1] == 'batch':
        a = sys.argv[2:]; batch(a[0], a[1], a[2], a[3], a[4], a[5] if len(a) > 5 else None, float(a[6]) if len(a) > 6 else 0.6, tuple(float(q) for q in a[7].split(',')) if len(a) > 7 else (12, 26))
