"""Najde skoky v obraze z výstupu ffmpeg signalstats (YDIF = průměrný rozdíl jasu proti předchozímu snímku).

Použití: python3 -I nastroje/skoky.py ydif.txt [podezrele.txt]
Skok = snímek s YDIF nad 4× medián okolí a nad 8. Dva skoky hned po sobě = probliknutí na 1 snímek, nebo velmi rychlý
dvousnímkový přechod. Z rozdílů jasu to rozlišit nejde, proto se čísla snímků zapíšou do podezrele.txt k vizuální kontrole.
"""
import re
import statistics
import sys

body = []
cas = None
for radek in open(sys.argv[1]):
    m = re.search(r"pts_time:([0-9.]+)", radek)
    if m:
        cas = float(m.group(1))
    m = re.search(r"YDIF=([0-9.]+)", radek)
    if m and cas is not None:
        body.append((cas, float(m.group(1))))

skoky = []
for i, (t, y) in enumerate(body[1:], 1):
    okoli = [v for _, v in body[max(1, i - 15):i] + body[i + 1:i + 16]] or [0]
    if y > 8 and y > 4 * max(statistics.median(okoli), 0.5):
        skoky.append((i, t, y))

if not skoky:
    print("žádné")
# Série po sobě jdoucích skoků: 1 = střih, 2 = probliknutí (tam a zpět), 3+ = rychlý přechod.
serie = []
for sk in skoky:
    if serie and sk[0] == serie[-1][-1][0] + 1:
        serie[-1].append(sk)
    else:
        serie.append([sk])
podezrele = []
for s in serie:
    t, i = s[0][1], s[0][0]
    if len(s) == 1:
        druh = "střih nebo prudká změna"
    elif len(s) == 2:
        druh = "probliknutí NEBO 2snímkový přechod – prohlédnout pás snímků"
        podezrele.append(i)
    else:
        druh = f"rychlý přechod přes {len(s)} snímků (do {s[-1][1]:.3f} s)"
    print(f"{t:7.3f} s  snímek {i:5d}  YDIF max {max(y for *_, y in s):6.1f}  {druh}")
if len(sys.argv) > 2:
    open(sys.argv[2], "w").write("".join(f"{i}\n" for i in podezrele))
