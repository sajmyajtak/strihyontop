#!/usr/bin/env bash
# Mastering hlasitosti pro sociální sítě: dvouprůchodový loudnorm, pak kontrolní měření po zakódování do AAC.
# Použití: nastroje/master_zvuk.sh VSTUP VYSTUP [cil_LUFS=-14] [true_peak=-1]
# Video stopa se kopíruje beze změny, zvuk → AAC 256k 48 kHz.
set -euo pipefail
IN=$1; OUT=$2; I=${3:--14}; TP=${4:--1}

# 1. průchod: změřit
MER=$(ffmpeg -hide_banner -nostats -i "$IN" -af "loudnorm=I=$I:TP=$TP:LRA=11:print_format=json" -f null - 2>&1 | sed -n '/^{/,/^}/p')
hodnota() { python3 -I -c "import json,sys; print(json.loads(sys.stdin.read())[sys.argv[1]])" "$1" <<<"$MER"; }

# 2. průchod: lineární normalizace podle změřených hodnot, pak měření po zakódování do AAC (kodek přidá mezivzorkové špičky).
# Když true peak přeteče: nejdřív ubrat hlasitost o přesah (nejvýš do tolerance cíl −1 LU), teprve pak jemný limiter
# s převzorkováním a pomalým uvolněním (rychlé uvolnění zkresluje basy a AAC pak špičky ještě zvětší, viz C011).
CIL_I=$I; LIMITER=""
for pokus in 1 2 3 4; do
  AF="loudnorm=I=$CIL_I:TP=$TP:LRA=11:measured_I=$(hodnota input_i):measured_TP=$(hodnota input_tp):measured_LRA=$(hodnota input_lra):measured_thresh=$(hodnota input_thresh):offset=$(hodnota target_offset):linear=true$LIMITER,aresample=48000"
  if ffprobe -v error -select_streams v -show_entries stream=index -of csv=p=0 "$IN" | grep -q .; then
    ffmpeg -hide_banner -loglevel error -y -i "$IN" -af "$AF" -c:v copy -c:a aac -b:a 256k -movflags +faststart "$OUT"
  else
    ffmpeg -hide_banner -loglevel error -y -i "$IN" -af "$AF" -c:a aac -b:a 256k "$OUT"
  fi
  PO=$(ffmpeg -hide_banner -nostats -i "$OUT" -af ebur128=peak=true:framelog=quiet -f null - 2>&1)
  PO_I=$(grep -E "^\s+I:" <<<"$PO" | tail -1 | awk '{print $2}')
  PO_TP=$(grep -E "^\s+Peak:" <<<"$PO" | tail -1 | awk '{print $2}')
  echo "pokus $pokus (cíl $CIL_I LUFS${LIMITER:+, limiter}): po AAC I=$PO_I LUFS, TP=$PO_TP dBTP"
  if python3 -c "import sys; sys.exit(0 if float('$PO_TP') <= float('$TP') else 1)"; then break; fi
  NOVY=$(python3 -c "print(round(float('$CIL_I') - (float('$PO_TP') - float('$TP')) - 0.1, 2))")
  if python3 -c "import sys; sys.exit(0 if float('$NOVY') >= float('$I') - 1 else 1)"; then
    CIL_I=$NOVY
  else
    CIL_I=$I
    LIMITER=",aresample=192000,alimiter=limit=$(python3 -c "print(round(10 ** ((float('$TP') - 1.2) / 20), 4))"):attack=5:release=300:level=false:latency=1"
  fi
done

echo "před: I=$(hodnota input_i) LUFS, TP=$(hodnota input_tp) dBTP"
echo "po:   I=$PO_I LUFS, TP=$PO_TP dBTP (cíl $I LUFS, ≤ $TP dBTP)"
