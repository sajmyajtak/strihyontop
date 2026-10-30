#!/usr/bin/env bash
# Stáhne materiál z Google Drive do media/materialy/ (necommituje se) a ověří ho.
# Použití: nastroje/drive.sh ID_NEBO_ODKAZ [CILOVA_SLOZKA]
#   ID a názvy souborů ve složce najde Google Drive konektor (search_files: parentId = 'ID_SLOZKY').
#   Konektor se na stahování videí nehodí (vrací base64 do konverzace), proto se stahuje přímo.
#   Funguje pro soubory sdílené „kdokoli s odkazem“. Soukromý soubor vrátí HTML stránku místo dat → požádat uživatele o sdílení.
set -euo pipefail
ZDROJ=$1
KOREN=$(cd "$(dirname "$0")/.." && pwd)
CIL=${2:-$KOREN/media/materialy}
mkdir -p "$CIL"
# Původní datum souborů z Drive zůstává, proto se nové soubory poznají porovnáním obsahu složky před a po.
PRED=$(find "$CIL" -type f | sort)
ID=$(python3 -c "import re,sys; s=sys.argv[1]; m=re.search(r'(?:/d/|id=|folders/)([A-Za-z0-9_-]{20,})', s); print(m.group(1) if m else s)" "$ZDROJ")

if [[ "$ZDROJ" == *folders/* ]]; then
  gdown --folder --quiet "https://drive.google.com/drive/folders/$ID" -O "$CIL"
else
  # gdown si poradí s potvrzením „soubor je moc velký na antivirovou kontrolu“
  (cd "$CIL" && gdown --quiet "$ID")
fi

# Ověření: HTML místo dat = soubor není sdílený
comm -13 <(echo "$PRED") <(find "$CIL" -type f | sort) | while read -r F; do
  [ -n "$F" ] || continue
  if file -b --mime-type "$F" | grep -q "text/html"; then
    echo "CHYBA: $F je HTML stránka, soubor asi není sdílený odkazem" >&2; continue
  fi
  INFO=$(ffprobe -v error -show_entries stream=codec_type,width,height,r_frame_rate -show_entries format=duration -of compact "$F" 2>/dev/null | paste -sd' ' || true)
  echo "OK $(du -h "$F" | cut -f1) $F ${INFO:+| $INFO}"
done
