"""Hlídač běžícího workflow pro režiséra: hlásí start a dokončení agentů, dlouhé ticho a zásah limitu výstupu (C018).

Použití (nejlépe přes Monitor, každý řádek = upozornění):
  python3 -I nastroje/hlidac.py RUN_DIR [--ticho 15] [--interval 30]
  RUN_DIR = ~/.claude/projects/<projekt>/<session>/subagents/workflows/<run_id>
"""
import argparse
import json
import time
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("run_dir")
ap.add_argument("--ticho", type=float, default=15, help="minuty bez zápisu, po kterých se agent nahlásí")
ap.add_argument("--interval", type=float, default=30)
ap.add_argument("--jen-nove", action="store_true", help="historii deníku načíst potichu, hlásit jen nové události (pro opětovné zapnutí)")
a = ap.parse_args()
run = Path(a.run_dir)

nazvy, hotove, nahlaseno_ticho, limity = {}, set(), set(), {}
videno_radku = 0
potichu = a.jen_nove          # první průchod jen načte stav, nic nehlásí


def posledni_zaznam(agent_id):
    f = run / f"agent-{agent_id}.jsonl"
    if not f.exists():
        return None, 0
    pocet_limitu = 0
    for r in f.read_text(errors="ignore").splitlines():
        if "Output token limit hit" not in r:
            continue
        # Skutečný limit je systémová zpráva typu user s textem jako celým obsahem. Stejná věta v přečteném
        # souboru (např. chyby.md v tool_result) se nepočítá (C019).
        try:
            d = json.loads(r)
        except json.JSONDecodeError:
            continue
        obsah = (d.get("message") or {}).get("content")
        if d.get("type") == "user" and isinstance(obsah, str) and obsah.startswith("Output token limit hit"):
            pocet_limitu += 1
    return f.stat().st_mtime, pocet_limitu


while True:
    j = run / "journal.jsonl"
    if j.exists():
        radky = j.read_text(errors="ignore").splitlines()
        for r in radky[videno_radku:]:
            try:
                d = json.loads(r)
            except json.JSONDecodeError:
                continue
            aid = d.get("agentId")
            if d.get("type") == "started" and aid:
                nazev = d.get("label", aid)
                for stary, n in nazvy.items():          # restart po obnovení workflow: starý agent se stejným názvem je nahrazený
                    if n == nazev and stary not in hotove:
                        hotove.add(stary)
                nazvy[aid] = nazev
                if not potichu:
                    print(f"{time.strftime('%H:%M')} START: {nazev}", flush=True)
            elif d.get("type") == "result" and aid:
                hotove.add(aid)
                if not potichu:
                    print(f"{time.strftime('%H:%M')} HOTOVO: {nazvy.get(aid, aid)}", flush=True)
        videno_radku = len(radky)
    for aid, nazev in nazvy.items():
        if aid in hotove:
            continue
        mtime, pocet_limitu = posledni_zaznam(aid)
        if mtime is None:
            continue
        if pocet_limitu > limity.get(aid, 0):
            limity[aid] = pocet_limitu
            if not potichu:
                print(f"{time.strftime('%H:%M')} LIMIT VÝSTUPU ×{pocet_limitu}: {nazev} (přemýšlí moc dlouho najednou, zvážit restart s effort high a psaním po částech)", flush=True)
        ticho = (time.time() - mtime) / 60
        if ticho >= a.ticho and (aid, int(mtime)) not in nahlaseno_ticho:
            nahlaseno_ticho.add((aid, int(mtime)))
            print(f"{time.strftime('%H:%M')} TICHO {ticho:.0f} min: {nazev}", flush=True)
    potichu = False
    time.sleep(a.interval)
