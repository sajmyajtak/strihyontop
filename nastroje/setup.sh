#!/usr/bin/env bash
# Připraví nástroje pro analýzu a střih. Kontejner se po čase maže, takže spouštět na začátku každé session.
set -euo pipefail
command -v ffmpeg >/dev/null || { echo "Chybí ffmpeg"; exit 1; }
pip install -q --root-user-action=ignore --upgrade yt-dlp faster-whisper gdown scipy pillow-heif
echo "yt-dlp $(yt-dlp --version), ffmpeg $(ffmpeg -version | head -1 | cut -d' ' -f3), faster-whisper OK"
