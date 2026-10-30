#!/usr/bin/env bash
# Technická kontrola videa pro kritika: parametry, hlasitost, zamrzlé a černé úseky, skoky a probliknutí, kontrolní arch.
# Použití: nastroje/kontrola.sh VIDEO VYSTUPNI_SLOZKA
# Výstup: VYSTUPNI_SLOZKA/zprava.txt + arch.jpg (snímek každých 0,5 s)
set -euo pipefail
V=$1; OUT=$2
mkdir -p "$OUT"
KOREN=$(cd "$(dirname "$0")/.." && pwd)

{
  echo "== Soubor: $V"
  ffprobe -v error -show_entries stream=codec_type,codec_name,profile,width,height,r_frame_rate,pix_fmt,sample_rate,channels \
    -show_entries format=duration,bit_rate -of compact "$V"

  echo; echo "== Hlasitost (cíl −14 LUFS ±1, true peak ≤ −1 dBTP)"
  if ffprobe -v error -select_streams a -show_entries stream=index -of csv=p=0 "$V" | grep -q .; then
    ffmpeg -hide_banner -nostats -i "$V" -af ebur128=peak=true:framelog=quiet -f null - 2>&1 | grep -E "^\s+(I|LRA|Peak):" || true
  else
    echo "BEZ ZVUKU"
  fi

  echo; echo "== Zamrzlé úseky > 1 s (mrtvý čas)"
  F=$(ffmpeg -hide_banner -nostats -i "$V" -vf freezedetect=n=-60dB:d=1 -map 0:v -f null - 2>&1 | grep -oE "freeze_(start|duration): [0-9.]+" | paste -sd' ' || true)
  echo "${F:-žádné}"

  echo; echo "== Prázdné (černé) úseky > 0,2 s"
  # pic_th 0.999: jen opravdu prázdné snímky, tmavé pozadí s obsahem se nehlásí
  B=$(ffmpeg -hide_banner -nostats -i "$V" -vf blackdetect=d=0.2:pic_th=0.999:pix_th=0.06 -map 0:v -f null - 2>&1 | grep -oE "black_start:[0-9.]+ black_end:[0-9.]+" | paste -sd' ' || true)
  echo "${B:-žádné}"

  echo; echo "== Skoky v obraze (YDIF výrazně nad okolím): střihy, probliknutí, skoky o snímek"
  ffmpeg -hide_banner -nostats -v error -i "$V" -vf "signalstats,metadata=print:key=lavfi.signalstats.YDIF:file=$OUT/ydif.txt" -map 0:v -f null -
  python3 -I "$KOREN/nastroje/skoky.py" "$OUT/ydif.txt" "$OUT/podezrele.txt"
} | tee "$OUT/zprava.txt"

# Pás 6 snímků kolem každého podezřelého místa: kritik ho musí prohlédnout (probliknutí vs. rychlý přechod).
while read -r N; do
  [ -n "$N" ] || continue
  ffmpeg -nostdin -hide_banner -loglevel error -y -i "$V" -vf "select='between(n\,$((N-2))\,$((N+3)))',scale=300:-1,tile=6x1" -fps_mode vfr -frames:v 1 "$OUT/pas_snimek_$N.jpg"
  echo "pás snímků k prohlédnutí: $OUT/pas_snimek_$N.jpg"
done < "$OUT/podezrele.txt"

D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$V")
W=$(ffprobe -v error -select_streams v -show_entries stream=width -of csv=p=0 "$V")
H=$(ffprobe -v error -select_streams v -show_entries stream=height -of csv=p=0 "$V")
N=$(python3 -c "import math; print(max(1, math.ceil(float('$D') * 2)))")
if [ "$H" -gt "$W" ]; then COLS=8; SW=240; else COLS=4; SW=480; fi
ROWS=$(( (N + COLS - 1) / COLS ))
ffmpeg -hide_banner -loglevel error -y -i "$V" -vf "fps=2,scale=$SW:-1,drawtext=text='%{pts\:hms}':x=6:y=6:fontsize=18:fontcolor=white:box=1:boxcolor=black@0.6,tile=${COLS}x${ROWS}" -frames:v 1 "$OUT/arch.jpg"
echo "arch: $OUT/arch.jpg"
