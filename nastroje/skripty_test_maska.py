import sys, time, os
import onnxruntime as ort
from rembg import remove
from rembg.sessions import sessions_class
from PIL import Image
model = sys.argv[1]; out = sys.argv[2]; files = sys.argv[3:]
so = ort.SessionOptions(); so.enable_cpu_mem_arena = False; so.enable_mem_pattern = False
cls = [c for c in sessions_class if c.name() == model][0]
s = cls(model, so, ['CPUExecutionProvider'])
os.makedirs(out, exist_ok=True)
for f in files:
    dst = os.path.join(out, os.path.basename(f))
    if os.path.exists(dst): continue
    t0 = time.time()
    im = Image.open(f).convert('RGB')
    a = remove(im, session=s, only_mask=True)
    a.save(dst)
    print(f, round(time.time()-t0, 1), 's', flush=True)
