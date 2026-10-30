"""Stáhne katalog prompt-motion.com (prompty, skilly, šablony, blog) do lokální mezipaměti.

Použití: python3 -I nastroje/prompt_motion.py [--jen-nove]
  media/prompt-motion/   plné texty (necommituje se, licence webu povoluje jen použití jako reference)
  znalosti/prompt-motion/katalog.md   rejstřík s odkazy a metadaty (commituje se, bez textů promptů)
Šetrně: 1 dotaz za ~0,7 s, nečte /api/ (zakázáno v robots.txt).
"""
import argparse
import json
import re
import sys
import time
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

WEB = "https://prompt-motion.com"
KOREN = Path(__file__).resolve().parent.parent
CACHE = KOREN / "media" / "prompt-motion"
KATALOG = KOREN / "znalosti" / "prompt-motion" / "katalog.md"
ENTRY = re.compile(r"^[a-z0-9_-]+-[0-9a-f]{6,7}$")


def stahni(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (strihyontop; reference use)"})
    for pokus in range(4):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.read().decode("utf-8")
        except Exception as e:
            if pokus == 3:
                raise
            print(f"  chyba {e}, zkouším znovu", file=sys.stderr)
            time.sleep(2 ** (pokus + 1))


def rsc(html):
    """Složí React Server Components payload, který Next.js vkládá do stránky."""
    chunks = re.findall(r'self\.__next_f\.push\(\[1,"(.*?)"\]\)</script>', html, re.S)
    return "".join(json.loads('"' + c + '"') for c in chunks)


def rsc_text(payload, ref):
    """Dlouhé texty jsou v payloadu jako odkaz "$<id>" na blok "<id>:T<délka hex>,<text>"."""
    m = re.search(r"(?:^|\n)" + re.escape(ref) + r":T([0-9a-f]+),", payload)
    if not m:
        return None
    n = int(m.group(1), 16)
    return payload[m.end():].encode("utf-8")[:n].decode("utf-8", "ignore")


class Text(HTMLParser):
    BLOK = ("p", "h1", "h2", "h3", "h4", "li", "pre", "br", "tr", "div", "section", "dd", "dt")

    def __init__(self):
        super().__init__()
        self.skip = self.main = 0
        self.out = []

    def handle_starttag(self, t, a):
        if t in ("script", "style", "svg", "noscript"):
            self.skip += 1
        if t in ("main", "article"):
            self.main += 1
        if t in self.BLOK:
            self.out.append("\n")
        if t in ("h1", "h2", "h3"):
            self.out.append("#" * int(t[1]) + " ")
        if t == "li":
            self.out.append("- ")

    def handle_endtag(self, t):
        if t in ("script", "style", "svg", "noscript"):
            self.skip -= 1
        if t in ("main", "article"):
            self.main -= 1

    def handle_data(self, d):
        if not self.skip and self.main:
            self.out.append(d)


def text(html):
    p = Text()
    p.feed(html)
    return re.sub(r"\n\s*\n+", "\n\n", "".join(p.out)).strip()


def pole(payload, nazev):
    m = re.search(r'"children":"' + nazev + r'"\}\],\["\$","dd",null,\{"className":"[^"]*","children":(".*?"|\[.*?\])\}', payload)
    if not m:
        return None
    v = m.group(1)
    d = re.search(r'"children":"([^"]+)"', v)
    return d.group(1) if d else v.strip('"')


def rozeber(slug, html, karta):
    p = rsc(html)
    prompt = None
    m = re.search(r'"prompt":("(?:[^"\\]|\\.)*")', p)
    if m:
        prompt = json.loads(m.group(1))
        if re.fullmatch(r"\$[0-9a-f]+", prompt):
            prompt = rsc_text(p, prompt[1:])
    t = text(html)
    skill = None
    if "\n## Skill" in t:
        skill = t.split("\n## Skill", 1)[1].split("\nModel", 1)[0].replace("CopiedCopy", "\n").replace("View repo (opens in a new tab)", "").strip()
    # Přednost má odkaz na konkrétní příspěvek tvůrce; holý profil x.com/p4nthera_ je autor webu v patičce.
    odkazy = re.findall(r'"href":"(https://(?:x\.com|twitter\.com|www\.instagram\.com|www\.linkedin\.com|www\.threads\.net|bsky\.app)/[^"]+)"', p)
    odkazy = [o for o in odkazy if not o.rstrip("/").endswith("/p4nthera_")]
    zdroj = next((o for o in odkazy if re.search(r"/(status|p|reel|posts|post)/", o)), odkazy[0] if odkazy else None)
    repo = re.search(r'"href":"(https://github\.com/[^"]+)"', p)
    sablona = re.search(r'"href":"/templates/([a-z0-9-]+)"', p)
    return {
        **karta,
        "url": f"{WEB}/{slug}",
        "model": pole(p, "Model"),
        "effort": pole(p, "Effort"),
        "zdroj": zdroj,
        "repo": repo.group(1) if repo else None,
        "sablona": sablona.group(1) if sablona else None,
        "prompt": prompt,
        "skill": skill,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--jen-nove", action="store_true", help="stáhnout jen položky, které ještě nejsou v mezipaměti")
    a = ap.parse_args()
    (CACHE / "stranky").mkdir(parents=True, exist_ok=True)

    print("hlavní stránka a sitemap…")
    home = rsc(stahni(WEB + "/"))
    i = home.find('{"cards":[')
    karty = {c["slug"]: {k: v for k, v in c.items() if k != "blur"} for c in json.JSONDecoder().raw_decode(home[i:])[0]["cards"]}
    urls = re.findall(r"<loc>([^<]+)</loc>", stahni(WEB + "/sitemap.xml"))
    cesty = [u.replace(WEB, "").strip("/") for u in urls]
    slugy = sorted({c for c in cesty if ENTRY.match(c)} | set(karty))
    ostatni = [c for c in cesty if c and not ENTRY.match(c) and not c.startswith("tags/")]

    soubor = CACHE / "polozky.json"
    polozky = {x["slug"]: x for x in json.loads(soubor.read_text())} if soubor.exists() else {}
    for n, slug in enumerate(slugy, 1):
        if a.jen_nove and slug in polozky:
            continue
        print(f"[{n}/{len(slugy)}] {slug}")
        polozky[slug] = rozeber(slug, stahni(f"{WEB}/{slug}"), karty.get(slug, {"slug": slug}))
        time.sleep(0.7)
    seznam = sorted(polozky.values(), key=lambda x: (x.get("date") or "", x["slug"]), reverse=True)
    soubor.write_text(json.dumps(seznam, ensure_ascii=False, indent=1))

    for cesta in ostatni:
        print("stránka", cesta)
        cil = CACHE / "stranky" / (cesta.replace("/", "__") + ".md")
        cil.write_text(f"<!-- {WEB}/{cesta} -->\n" + text(stahni(f"{WEB}/{cesta}")))
        time.sleep(0.7)

    KATALOG.parent.mkdir(parents=True, exist_ok=True)
    radky = [
        "# Katalog prompt-motion.com",
        "",
        f"Vygenerováno `nastroje/prompt_motion.py`, {len(seznam)} položek. Plné texty promptů jsou v `media/prompt-motion/polozky.json`",
        "(necommituje se, videa a prompty patří autorům, web povoluje jen použití jako reference). Vlastní poznatky jsou v `poznatky.md`.",
        "",
        "| datum | název | autor | typ | štítky | formát | effort | délka promptu | šablona |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for x in seznam:
        delka = len(x["prompt"] or "")
        radky.append(
            f"| {x.get('date', '')} | [{x.get('title', x['slug'])}]({x['url']}) | @{x.get('handle', '')} | {'+'.join(x.get('tags', []))} "
            f"| {', '.join(x.get('contentTags', []))} | {x.get('width', '')}×{x.get('height', '')} | {x.get('effort') or ''} "
            f"| {delka} | {x.get('sablona') or ''} |"
        )
    KATALOG.write_text("\n".join(radky) + "\n")
    print(f"hotovo: {len(seznam)} položek, {len(ostatni)} dalších stránek")


if __name__ == "__main__":
    main()
