// Render HTML animace do MP4 snímek po snímku (metoda z prompt-motion.com).
// Stránka musí mít window.seek(t): nastaví celý obraz pro čas t v sekundách, bez CSS animací a časovačů.
//
// Použití:
//   node nastroje/render_html.cjs --html scena.html --out video.mp4 --dur 15 [--w 1080 --h 1920 --fps 30]
//        [--sub 3]            podsnímky na snímek, zprůměrované = rozmazání pohybem (1 = vypnuto)
//        [--audio hudba.wav]  přimíchat zvuk
//        [--audio-z-kodu]     zvuk ze stránky: await window.renderAudio() vrací WAV v base64
//        [--nahled 0.5]       místo videa jen kontrolní snímky každých 0,5 s + arch nahled.jpg
const { chromium } = require('playwright');
const { spawn, execFileSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const args = process.argv.slice(2);
const opt = (name, def) => {
  const i = args.indexOf('--' + name);
  return i < 0 ? def : args[i + 1];
};
const flag = (name) => args.includes('--' + name);

const html = path.resolve(opt('html'));
const out = path.resolve(opt('out', 'video.mp4'));
const W = +opt('w', 1080), H = +opt('h', 1920), FPS = +opt('fps', 30);
const DUR = +opt('dur');
const SUB = Math.max(1, +opt('sub', 3));
const NAHLED = opt('nahled');
if (!fs.existsSync(html) || !(DUR > 0)) {
  console.error('Chybí --html (existující soubor) nebo --dur > 0');
  process.exit(1);
}

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 1 });
  const chyby = [];
  page.on('pageerror', (e) => chyby.push(e.message));
  page.on('console', (m) => m.type() === 'error' && chyby.push(m.text()));
  await page.goto('file://' + html);
  await page.waitForFunction(() => typeof window.seek === 'function', null, { timeout: 15000 });
  await page.evaluate(() => document.fonts.ready);
  const seek = (t) => page.evaluate((t) => window.seek(t), t);

  if (NAHLED) {
    const krok = +NAHLED;
    const dir = out.replace(/\.[^.]+$/, '') + '_nahled';
    fs.mkdirSync(dir, { recursive: true });
    let n = 0;
    for (let t = 0; t <= DUR + 1e-9; t += krok, n++) {
      await seek(t);
      await page.screenshot({ path: path.join(dir, `${String(n).padStart(3, '0')}_${t.toFixed(2)}s.png`) });
    }
    const cols = Math.min(n, W > H ? 4 : 8);
    execFileSync('ffmpeg', ['-v', 'error', '-y', '-pattern_type', 'glob', '-i', path.join(dir, '*.png'),
      '-vf', `scale=${W > H ? 480 : 240}:-1,tile=${cols}x${Math.ceil(n / cols)}`, '-frames:v', '1', path.join(dir, 'nahled.jpg')]);
    console.log(`kontrolní snímky: ${n} → ${dir}/nahled.jpg`);
  } else {
    let audio = opt('audio');
    if (flag('audio-z-kodu')) {
      const b64 = await page.evaluate(async () => await window.renderAudio());
      audio = out.replace(/\.[^.]+$/, '') + '_zvuk.wav';
      fs.writeFileSync(audio, Buffer.from(b64, 'base64'));
    }
    // Podsnímky jdou do ffmpeg rychlostí FPS*SUB; tmix zprůměruje SUB po sobě jdoucích a select nechá poslední z každé skupiny.
    const vf = SUB > 1 ? `tmix=frames=${SUB},select='eq(mod(n\\,${SUB})\\,${SUB - 1})',setpts=N/(${FPS}*TB)` : 'null';
    const ff = ['-v', 'error', '-y', '-f', 'image2pipe', '-c:v', 'png', '-framerate', String(FPS * SUB), '-i', '-'];
    if (audio) ff.push('-i', path.resolve(audio));
    ff.push('-vf', vf, '-r', String(FPS), '-c:v', 'libx264', '-preset', 'slow', '-crf', '16', '-pix_fmt', 'yuv420p', '-movflags', '+faststart');
    if (audio) ff.push('-c:a', 'aac', '-b:a', '256k', '-ar', '48000', '-shortest');
    ff.push(out);
    const enc = spawn('ffmpeg', ff, { stdio: ['pipe', 'inherit', 'inherit'] });
    const hotovo = new Promise((ok, ko) => enc.on('close', (c) => (c === 0 ? ok() : ko(new Error('ffmpeg skončil kódem ' + c)))));
    const celkem = Math.round(DUR * FPS);
    for (let f = 0; f < celkem; f++) {
      for (let s = 0; s < SUB; s++) {
        await seek((f + (s + 1) / SUB - 1 / SUB) / FPS);
        const png = await page.screenshot({ type: 'png' });
        if (!enc.stdin.write(png)) await new Promise((r) => enc.stdin.once('drain', r));
      }
      if (f % FPS === 0) process.stdout.write(`\r${(f / FPS).toFixed(0)}/${DUR} s`);
    }
    enc.stdin.end();
    await hotovo;
    console.log(`\rvideo: ${out}`);
  }
  await browser.close();
  if (chyby.length) {
    console.error('CHYBY ZE STRÁNKY:\n' + [...new Set(chyby)].join('\n'));
    process.exit(2);
  }
})().catch((e) => {
  console.error(e);
  process.exit(1);
});
