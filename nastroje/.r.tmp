// Render HTML animace do MP4 snímek po snímku (metoda z prompt-motion.com).
// Stránka musí mít window.seek(t): nastaví celý obraz pro čas t v sekundách, bez CSS animací a časovačů.
//
// Použití:
//   node nastroje/render_html.cjs --html scena.html --out video.mp4 --dur 30 [--w 1920 --h 1080 --fps 60]   (výchozí 16:9, 9:16 = --w 1080 --h 1920)
//        [--od 3.7]           začátek výřezu v s (video pak pokryje --od až --dur; --dur je konec, ne délka)
//        [--sub 4]            podsnímky na snímek, zprůměrované = rozmazání pohybem (1 = vypnuto, rychlé přechody 8)
//        [--rychle 3.7-4.25,5.6-5.85 --sub-rychle 8]   v těchto úsecích víc podsnímků (zbytek videa --sub)
//        [--vlakna 3]         počet souběžných prohlížečů (výchozí 3) (úseky videa se renderují zvlášť a spojí bez překódování)
//        [--zaverka 0.5]      jakou část snímku podsnímky pokryjí (0.5 = filmová závěrka 180°), vystředěno na čas snímku
//        [--audio hudba.wav]  přimíchat zvuk
//        [--audio-z-kodu]     zvuk ze stránky: await window.renderAudio() vrací WAV v base64
//        [--nahled 0.5]       místo videa jen kontrolní snímky každých 0,5 s + arch nahled.jpg
//        [--nahled doby --bpm 120 [--offset 0]]   kontrolní snímek na každou dobu hudby
//        [--nahled casy --casy 0,1.6,2.5]         kontrolní snímky v daných časech
//
// Výkon (V002): nejdražší bývá kódování PNG snímku obrazovky, ne scéna. Proto snímání přes CDP s optimizeForSpeed
// (pixely totožné s page.screenshot, ~2,5× rychlejší) a volitelně víc prohlížečů najednou (--vlakna).
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
const W = +opt('w', 1920), H = +opt('h', 1080), FPS = +opt('fps', 60);
const DUR = +opt('dur');
const OD = Math.max(0, +opt('od', 0));
const SUB = Math.max(1, +opt('sub', 4));
const SUB_R = Math.max(SUB, +opt('sub-rychle', SUB));
const RYCHLE = (opt('rychle', '') || '').split(',').filter(Boolean).map((u) => u.split('-').map(Number));
const VLAKNA = Math.max(1, +opt('vlakna', 3));   // 4 CPU: 3 prohlížeče ≈ 5× rychleji než 1 (V002), víc už skoro nepřidá
const ZAVERKA = Math.min(1, Math.max(0, +opt('zaverka', 0.5)));
const NAHLED = opt('nahled');
if (!fs.existsSync(html) || !(DUR > 0) || !(DUR > OD)) {
  console.error('Chybí --html (existující soubor) nebo --dur > 0 (a > --od)');
  process.exit(1);
}
if (RYCHLE.some((u) => u.length !== 2 || !(u[1] > u[0])) || SUB_R % SUB !== 0) {
  console.error('--rychle čeká úseky OD-DO oddělené čárkou a --sub-rychle musí být násobek --sub');
  process.exit(1);
}

// Otevře prohlížeč se scénou a vrátí seek(t) a snimek() (PNG Buffer).
const otevri = async (chyby) => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 1 });
  page.on('pageerror', (e) => chyby.push(e.message));
  page.on('console', (m) => m.type() === 'error' && chyby.push(m.text()));
  await page.goto('file://' + html);
  await page.waitForFunction(() => typeof window.seek === 'function', null, { timeout: 15000 });
  await page.evaluate(() => document.fonts.ready);
  const cdp = await page.context().newCDPSession(page);
  const seek = (t) => page.evaluate((t) => window.seek(t), t);
  const snimek = async () => Buffer.from((await cdp.send('Page.captureScreenshot', { format: 'png', optimizeForSpeed: true })).data, 'base64');
  return { browser, seek, snimek };
};

const ffVideo = (vstupFps, vf, cil, audio) => {
  const ff = ['-v', 'error', '-y', '-f', 'image2pipe', '-c:v', 'png', '-framerate', String(vstupFps), '-i', '-'];
  if (audio) ff.push('-ss', String(OD), '-i', path.resolve(audio));
  // Barvy: převod RGB → YUV výslovně maticí BT.709 (omezený rozsah) a stejné tagy do streamu, aby přehrávače a sítě
  // nehádaly matici a neposunuly odstín (nález kritika V001: color_* = unknown).
  ff.push('-vf', `${vf},scale=out_color_matrix=bt709:out_range=tv,format=yuv420p`, '-r', String(FPS),
    '-c:v', 'libx264', '-preset', 'slow', '-crf', '14', '-x264-params', 'aq-mode=3', '-pix_fmt', 'yuv420p',   // CRF 14 + aq-mode 3: méně bloků na světlých plochách a v přechodech (V003, C037)
    '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709', '-color_range', 'tv', '-movflags', '+faststart');
  if (audio) ff.push('-c:a', 'aac', '-b:a', '256k', '-ar', '48000', '-shortest');
  ff.push(cil);
  return ff;
};

// Vyrenderuje snímky [f0, f1) do souboru cil (bez zvuku, pokud audio není dané).
const renderUsek = async (f0, f1, cil, audio, chyby, hlasit) => {
  const { browser, seek, snimek } = await otevri(chyby);
  // Do ffmpeg jde vždy SUB_R podsnímků na snímek; tmix je zprůměruje a select nechá poslední z každé skupiny.
  // Mimo rychlé úseky se snímá jen SUB různých podsnímků a každý se pošle SUB_R / SUB krát (průměr je stejný jako ze SUB).
  const vf = SUB_R > 1 ? `tmix=frames=${SUB_R},select='eq(mod(n\\,${SUB_R})\\,${SUB_R - 1})',setpts=N/(${FPS}*TB)` : 'null';
  const enc = spawn('ffmpeg', ffVideo(FPS * SUB_R, vf, cil, audio), { stdio: ['pipe', 'inherit', 'inherit'] });
  const hotovo = new Promise((ok, ko) => enc.on('close', (c) => (c === 0 ? ok() : ko(new Error('ffmpeg skončil kódem ' + c)))));
  const zapis = async (buf) => { if (!enc.stdin.write(buf)) await new Promise((r) => enc.stdin.once('drain', r)); };
  for (let f = f0; f < f1; f++) {
    const t = f / FPS;
    const n = RYCHLE.some(([a, b]) => t >= a && t <= b) ? SUB_R : SUB;
    for (let s = 0; s < n; s++) {
      // Podsnímky rozložené symetricky kolem času snímku přes ZAVERKA jeho délky.
      await seek(Math.max(0, (f + ((s + 0.5) / n - 0.5) * ZAVERKA) / FPS));
      const png = await snimek();
      for (let k = 0; k < SUB_R / n; k++) await zapis(png);
    }
    if (hlasit && (f - f0) % FPS === 0) process.stdout.write(`\r${((f - f0) / FPS).toFixed(0)}/${((f1 - f0) / FPS).toFixed(0)} s`);
  }
  enc.stdin.end();
  await hotovo;
  await browser.close();
};

(async () => {
  const chyby = [];
  if (NAHLED) {
    const { browser, seek, snimek } = await otevri(chyby);
    let casy = [];
    if (NAHLED === 'casy') casy = opt('casy', '0').split(',').map(Number);
    else if (NAHLED === 'doby') {
      const doba = 60 / +opt('bpm', 120);
      for (let t = +opt('offset', 0); t <= DUR + 1e-9; t += doba) casy.push(t);
    } else for (let t = OD; t <= DUR + 1e-9; t += +NAHLED) casy.push(t);
    const dir = out.replace(/\.[^.]+$/, '') + '_nahled';
    fs.rmSync(dir, { recursive: true, force: true });
    fs.mkdirSync(dir, { recursive: true });
    const n = casy.length;
    for (const [i, t] of casy.entries()) {
      await seek(t);
      fs.writeFileSync(path.join(dir, `${String(i).padStart(3, '0')}_${t.toFixed(2)}s.png`), await snimek());
    }
    await browser.close();
    const cols = Math.min(n, W > H ? 4 : 8);
    execFileSync('ffmpeg', ['-v', 'error', '-y', '-pattern_type', 'glob', '-i', path.join(dir, '*.png'),
      '-vf', `scale=${W > H ? 480 : 240}:-1,tile=${cols}x${Math.ceil(n / cols)}`, '-frames:v', '1', path.join(dir, 'nahled.jpg')]);
    console.log(`kontrolní snímky: ${n} → ${dir}/nahled.jpg`);
  } else {
    let audio = opt('audio');
    if (flag('audio-z-kodu')) {
      const { browser } = await otevri(chyby);
      const page = browser.contexts()[0].pages()[0];
      const b64 = await page.evaluate(async () => await window.renderAudio());
      await browser.close();
      audio = out.replace(/\.[^.]+$/, '') + '_zvuk.wav';
      fs.writeFileSync(audio, Buffer.from(b64, 'base64'));
    }
    const F0 = Math.round(OD * FPS), F1 = Math.round(DUR * FPS);
    const t0 = Date.now();
    if (VLAKNA === 1) {
      await renderUsek(F0, F1, out, audio, chyby, true);
    } else {
      // Úseky se renderují souběžně a spojí se bez překódování (stejné parametry kodéru). Hranice úseků nevadí:
      // každý výstupní snímek se počítá jen ze svých podsnímků.
      const dir = out.replace(/\.[^.]+$/, '') + '_useky';
      fs.rmSync(dir, { recursive: true, force: true });
      fs.mkdirSync(dir, { recursive: true });
      const hranice = [...Array(VLAKNA + 1).keys()].map((i) => F0 + Math.round(((F1 - F0) * i) / VLAKNA));
      const soubory = hranice.slice(0, -1).map((_, i) => path.join(dir, `usek${i}.mp4`));
      await Promise.all(soubory.map((s, i) => renderUsek(hranice[i], hranice[i + 1], s, null, chyby, i === 0)));
      fs.writeFileSync(path.join(dir, 'seznam.txt'), soubory.map((s) => `file '${s}'`).join('\n'));
      const ff = ['-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', path.join(dir, 'seznam.txt')];
      if (audio) ff.push('-ss', String(OD), '-i', path.resolve(audio));
      ff.push('-map', '0:v', '-c:v', 'copy');
      if (audio) ff.push('-map', '1:a', '-c:a', 'aac', '-b:a', '256k', '-ar', '48000', '-shortest');
      ff.push('-movflags', '+faststart', out);
      execFileSync('ffmpeg', ff);
      fs.rmSync(dir, { recursive: true, force: true });
    }
    console.log(`\rvideo: ${out} (${((Date.now() - t0) / 1000).toFixed(0)} s výpočtu)`);
  }
  if (chyby.length) {
    console.error('CHYBY ZE STRÁNKY:\n' + [...new Set(chyby)].join('\n'));
    process.exit(2);
  }
})().catch((e) => {
  console.error(e);
  process.exit(1);
});
