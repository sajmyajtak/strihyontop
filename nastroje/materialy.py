"""Připraví stažené materiály k práci a udělá z nich přehled.

Použití: python3 -I nastroje/materialy.py SLOZKA
  - fotky: srovná otočení podle EXIF, HEIC/HEIF/WEBP převede na JPG → SLOZKA/_pripraveno/
  - videa: rozlišení, fps (i proměnlivé z iPhonu), délka, otočení, HDR, zvuk; 6 náhledů z každého
  - SLOZKA/_katalog.md (tabulka s varováními) + SLOZKA/_prehled.jpg (všechny materiály na jednom obrázku)
Vše zůstává v media/ (necommituje se). Názvy a odkazy na materiály klientů do gitu nepatří (repozitář je veřejný).
"""
import json
import subprocess
import sys
from fractions import Fraction
from pathlib import Path

from PIL import Image, ImageDraw, ImageOps

try:
    import pillow_heif
    pillow_heif.register_heif_opener()
except ImportError:
    pillow_heif = None

FOTKY = {".jpg", ".jpeg", ".png", ".heic", ".heif", ".webp", ".avif", ".tif", ".tiff"}
VIDEA = {".mp4", ".mov", ".m4v", ".mkv", ".webm", ".avi", ".mts"}
HDR = {"smpte2084": "HDR10/PQ", "arib-std-b67": "HLG (iPhone)"}
DLAZDICE = 300


def probe(f):
    out = subprocess.run(["ffprobe", "-v", "error", "-print_format", "json", "-show_streams", "-show_format", str(f)],
                         capture_output=True, text=True)
    return json.loads(out.stdout or "{}")


def zlomek(s):
    try:
        return float(Fraction(s))
    except (ValueError, ZeroDivisionError, TypeError):
        return 0.0


def video(f, nahledy):
    d = probe(f)
    v = next((s for s in d.get("streams", []) if s.get("codec_type") == "video"), None)
    if not v:
        return None, ["nečitelné video"]
    a = any(s.get("codec_type") == "audio" for s in d["streams"])
    dur = float(d.get("format", {}).get("duration", 0))
    w, h = v.get("width"), v.get("height")
    rot = 0
    for sd in v.get("side_data_list", []):
        if "rotation" in sd:
            rot = int(sd["rotation"])
    rot = rot or int(v.get("tags", {}).get("rotate", 0))
    if abs(rot) in (90, 270):
        w, h = h, w
    r, avg = zlomek(v.get("r_frame_rate")), zlomek(v.get("avg_frame_rate"))
    var = []
    if v.get("color_transfer") in HDR:
        var.append(f"HDR {HDR[v['color_transfer']]} → převést do SDR (tonemap)")
    if r and avg and abs(r - avg) > 0.5:
        var.append(f"proměnlivé fps ({avg:.2f} průměr) → sjednotit")
    if rot:
        var.append(f"otočení {rot}° v metadatech")
    if min(w, h) < 1080:
        var.append(f"nízké rozlišení {w}×{h}")
    # 6 náhledů rovnoměrně přes celé video (ffmpeg aplikuje otočení sám)
    for i in range(6):
        t = dur * (i + 0.5) / 6
        cil = nahledy / f"{f.stem}_{i}.jpg"
        subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-ss", f"{t:.2f}", "-i", str(f), "-frames:v", "1",
                        "-vf", f"scale={DLAZDICE}:{DLAZDICE}:force_original_aspect_ratio=decrease", str(cil)])
    info = dict(typ="video", soubor=f.name, rozliseni=f"{w}×{h}", fps=round(avg or r, 2), delka=round(dur, 1),
                kodek=v.get("codec_name"), bitova_hloubka=v.get("bits_per_raw_sample") or v.get("pix_fmt"), zvuk=a)
    return info, var


def fotka(f, pripraveno, nahledy):
    im = Image.open(f)
    im = ImageOps.exif_transpose(im)               # telefon ukládá otočení jen do EXIF
    var = []
    cil = f
    if f.suffix.lower() not in {".jpg", ".jpeg", ".png"} or im.mode not in ("RGB", "RGBA", "L"):
        cil = pripraveno / (f.stem + ".jpg")
        im.convert("RGB").save(cil, quality=95)
        var.append(f"převedeno na {cil.name}")
    elif ImageOps.exif_transpose(Image.open(f)).size != Image.open(f).size:
        cil = pripraveno / f.name
        im.save(cil, quality=95)
        var.append("otočeno podle EXIF")
    if min(im.size) < 1080:
        var.append(f"nízké rozlišení {im.size[0]}×{im.size[1]}")
    n = im.copy()
    n.thumbnail((DLAZDICE, DLAZDICE))
    n.convert("RGB").save(nahledy / f"{f.stem}_0.jpg")
    return dict(typ="fotka", soubor=f.name, rozliseni=f"{im.size[0]}×{im.size[1]}", pouzit=str(cil.name)), var


def prehled(polozky, nahledy, cil):
    """Jeden obrázek: řádek na soubor (video 6 náhledů, fotka 1), nad ním název."""
    radky = []
    for p in polozky:
        snimky = sorted(nahledy.glob(f"{Path(p['soubor']).stem}_*.jpg"))
        if not snimky:
            continue
        radek = Image.new("RGB", (DLAZDICE * 6, DLAZDICE + 34), (18, 18, 20))
        for i, s in enumerate(snimky[:6]):
            im = Image.open(s)
            radek.paste(im, (i * DLAZDICE + (DLAZDICE - im.width) // 2, 34 + (DLAZDICE - im.height) // 2))
        popis = f"{p['soubor']}  |  {p['rozliseni']}" + (f"  |  {p['fps']} fps  |  {p['delka']} s" if p["typ"] == "video" else "")
        ImageDraw.Draw(radek).text((8, 8), popis, fill=(235, 235, 235))
        radky.append(radek)
    if not radky:
        return
    out = Image.new("RGB", (DLAZDICE * 6, sum(r.height for r in radky)), (0, 0, 0))
    y = 0
    for r in radky:
        out.paste(r, (0, y))
        y += r.height
    out.save(cil, quality=85)


def main():
    slozka = Path(sys.argv[1])
    pripraveno, nahledy = slozka / "_pripraveno", slozka / "_nahledy"
    pripraveno.mkdir(exist_ok=True)
    nahledy.mkdir(exist_ok=True)
    polozky, radky = [], []
    for f in sorted(p for p in slozka.rglob("*") if p.is_file() and not any(c.startswith("_") for c in p.relative_to(slozka).parts)):
        pr = f.suffix.lower()
        try:
            if pr in VIDEA:
                info, var = video(f, nahledy)
            elif pr in FOTKY:
                info, var = fotka(f, pripraveno, nahledy)
            else:
                continue
        except Exception as e:                      # jeden vadný soubor nesmí zastavit celý katalog
            info, var = dict(typ="?", soubor=f.name, rozliseni="?"), [f"chyba čtení: {e}"]
        if info:
            info["varovani"] = var
            polozky.append(info)
            dalsi = f"{info.get('fps', '')} fps, {info.get('delka', '')} s, {'zvuk' if info.get('zvuk') else 'bez zvuku'}" if info["typ"] == "video" else ""
            radky.append(f"| {info['typ']} | {info['soubor']} | {info['rozliseni']} | {dalsi} | {'; '.join(var) or 'OK'} |")
    fps = {p["fps"] for p in polozky if p["typ"] == "video"}
    souhrn = f"{sum(p['typ'] == 'video' for p in polozky)} videí, {sum(p['typ'] == 'fotka' for p in polozky)} fotek"
    if len(fps) > 1:
        souhrn += f". **Různé fps {sorted(fps)} → sjednotit na výstupní fps**"
    (slozka / "_katalog.md").write_text("# Materiály\n\n" + souhrn + "\n\n| typ | soubor | rozlišení | parametry | varování |\n|---|---|---|---|---|\n"
                                       + "\n".join(radky) + "\n")
    (slozka / "_katalog.json").write_text(json.dumps(polozky, ensure_ascii=False, indent=1))
    prehled(polozky, nahledy, slozka / "_prehled.jpg")
    print(souhrn)
    print("\n".join(radky))
    print(f"přehled: {slozka / '_prehled.jpg'}")


if __name__ == "__main__":
    main()
