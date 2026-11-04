import sys, time, os
from rembg import new_session, remove
from PIL import Image
model = sys.argv[1]; out = sys.argv[2]; files = sys.argv[3:]
s = new_session(model)
os.makedirs(out, exist_ok=True)
for f in files:
    t0 = time.time()
    im = Image.open(f).convert('RGB')
    a = remove(im, session=s, only_mask=True)
    a.save(os.path.join(out, os.path.basename(f)))
    print(f, round(time.time()-t0, 1), 's', flush=True)
