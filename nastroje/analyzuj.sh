#!/usr/bin/env bash
# Stáhne referenční video a připraví podklady k rozboru.
# Použití: nastroje/analyzuj.sh ODKAZ_NEBO_SOUBOR NAZEV
# Výstup: media/reference/NAZEV/ (video, metadata, nahled.jpg, analyza.txt) – složka media/ se necommituje.
set -euo pipefail
ZDROJ=$1; NAZEV=$2
KOREN=$(cd "$(dirname "$0")/.." && pwd)
OUT="$KOREN/media/reference/$NAZEV"
mkdir -p "$OUT"

if [ -f "$ZDROJ" ]; then
  cp "$ZDROJ" "$OUT/video.mp4"
else
  # Instagram při rychlém stahování vrací 429 – pak počkat ~1 min a zkusit znovu.
  yt-dlp --no-warnings -o "$OUT/video.%(ext)s" --merge-output-format mp4 --write-info-json "$ZDROJ"
fi
V="$OUT/video.mp4"

{
  echo "== Zdroj: $ZDROJ"
  if [ -f "$OUT/video.info.json" ]; then
    python3 -I -c '
import json, sys
d = json.load(open(sys.argv[1]))
for k in ["channel", "uploader", "upload_date", "like_count", "comment_count", "view_count"]:
    print(f"{k}: {d.get(k)}")
print("popis:", d.get("description"))
' "$OUT/video.info.json"
  fi
  echo; echo "== Technika"
  ffprobe -v error -show_entries stream=codec_type,width,height,r_frame_rate -show_entries format=duration -of compact "$V"
  echo; echo -n "== Střihy (s): "
  STRIHY=$(ffmpeg -hide_banner -i "$V" -vf "select='gt(scene,0.3)',showinfo" -f null - 2>&1 | grep -o 'pts_time:[0-9.]*' | cut -d: -f2 | tr '\n' ' ' || true)
  echo "${STRIHY:-žádné tvrdé střihy}"
  echo; echo "== Hlasitost"
  ffmpeg -hide_banner -i "$V" -af ebur128=framelog=quiet -f null - 2>&1 | grep -E " I:| LRA:" || true
  echo; echo "== Přepis"
  python3 -I "$KOREN/nastroje/prepis.py" "$V" 2>/dev/null || echo "(přepis selhal)"
} > "$OUT/analyza.txt"

# Náhledový arch: ~80 snímků rovnoměrně přes celé video.
D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$V")
FPS=$(python3 -c "print(min(4, 80 / float('$D')))")
ffmpeg -hide_banner -loglevel error -y -i "$V" -vf "fps=$FPS,scale=240:-1,tile=10x8" -frames:v 1 "$OUT/nahled.jpg"

cat "$OUT/analyza.txt"
echo; echo "Náhled: $OUT/nahled.jpg"
