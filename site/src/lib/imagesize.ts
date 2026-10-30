import fs from 'node:fs';
import path from 'node:path';

export interface Size { width: number; height: number }

/** Read the pixel size of a PNG, JPEG or SVG that lives in public/, at build time. */
export function imageSize(publicPath: string): Size {
  const file = path.join(process.cwd(), 'public', publicPath.replace(/^\//, ''));
  if (!fs.existsSync(file)) {
    throw new Error(`Image not found in public/: ${publicPath}`);
  }
  const buf = fs.readFileSync(file);
  if (file.endsWith('.png')) {
    return { width: buf.readUInt32BE(16), height: buf.readUInt32BE(20) };
  }
  if (/\.jpe?g$/i.test(file)) {
    // Walk the JPEG markers until a start-of-frame segment (SOF0..SOF15, not DHT/JPG/DAC).
    let i = 2;
    while (i + 9 < buf.length) {
      if (buf[i] !== 0xff) { i++; continue; }
      const m = buf[i + 1];
      if (m >= 0xc0 && m <= 0xcf && m !== 0xc4 && m !== 0xc8 && m !== 0xcc) {
        return { width: buf.readUInt16BE(i + 7), height: buf.readUInt16BE(i + 5) };
      }
      i += 2 + buf.readUInt16BE(i + 2);
    }
  }
  if (file.endsWith('.svg')) {
    const head = buf.toString('utf8', 0, 2000);
    const vb = head.match(/viewBox="([\d.\s-]+)"/);
    if (vb) {
      const [, , w, h] = vb[1].trim().split(/\s+/).map(Number);
      return { width: w, height: h };
    }
    const w = head.match(/width="([\d.]+)/);
    const h = head.match(/height="([\d.]+)/);
    if (w && h) return { width: Number(w[1]), height: Number(h[1]) };
  }
  throw new Error(`Cannot read size of ${publicPath}`);
}
