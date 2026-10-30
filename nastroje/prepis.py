"""Přepis mluveného slova z videa (Whisper).

Použití: python3 -I nastroje/prepis.py VIDEO [--model small|medium|large-v3] [--jazyk cs] [--slova]
  --slova  vypíše časy jednotlivých slov (podklad pro titulky slovo po slově)
Pro češtinu používat --model medium nebo large-v3, "small" na ni nestačí.
"""
import argparse
import subprocess

import numpy as np
from faster_whisper import WhisperModel

p = argparse.ArgumentParser()
p.add_argument("video")
p.add_argument("--model", default="small")
p.add_argument("--jazyk", default=None)
p.add_argument("--slova", action="store_true")
a = p.parse_args()

# Zvuk dekóduje ffmpeg: vestavěné dekódování faster-whisper padá na nekompatibilní verzi PyAV.
raw = subprocess.run(
    ["ffmpeg", "-v", "error", "-i", a.video, "-ac", "1", "-ar", "16000", "-f", "f32le", "-"],
    capture_output=True, check=True,
).stdout
audio = np.frombuffer(raw, np.float32)

model = WhisperModel(a.model, device="cpu", compute_type="int8")
segs, info = model.transcribe(audio, language=a.jazyk, vad_filter=True, word_timestamps=a.slova)
print(f"# jazyk={info.language} jistota={info.language_probability:.2f}")
for s in segs:
    print(f"[{s.start:6.2f}-{s.end:6.2f}] {s.text.strip()}")
    if a.slova:
        for w in s.words:
            print(f"    {w.start:6.2f}-{w.end:6.2f} {w.word.strip()}")
