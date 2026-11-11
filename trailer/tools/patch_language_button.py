# -*- coding: utf-8 -*-
# Replaces the flag in the app's language button with "EN" in every frame of an app recording.
# A frame is patched only where the button is really there (a fit of the old button, dimmed or
# not, explains the pixels); fullscreen animations and title cards stay untouched.
# Usage: python patch_video.py <ffmpeg> <old_full.png> <new_full.png> <in.mp4> <out.mp4>
import subprocess
import sys

import numpy as np
from PIL import Image

ff, old_png, new_png, src, dst = sys.argv[1:6]
BOX = (2188, 30, 2271, 76)  # inside the button, in 2400x1080 device pixels

info = subprocess.run([ff, "-hide_banner", "-i", src], capture_output=True, text=True).stderr
size = next(t for line in info.splitlines() if "Video:" in line for t in line.replace(",", " ").split()
            if "x" in t and t.split("x")[0].isdigit() and t.split("x")[1].isdigit())
w, h = (int(v) for v in size.split("x"))
scale = w / 2400
box = [round(v * scale) for v in BOX]
bw, bh = box[2] - box[0], box[3] - box[1]
old = np.asarray(Image.open(old_png).convert("RGB").resize((w, h), Image.LANCZOS), dtype=float)[box[1]:box[3], box[0]:box[2]]
new = np.asarray(Image.open(new_png).convert("RGB").resize((w, h), Image.LANCZOS), dtype=float)[box[1]:box[3], box[0]:box[2]]
design = [np.vstack([old[..., c].ravel(), np.ones(bw * bh)]).T for c in range(3)]

dec = subprocess.Popen([ff, "-loglevel", "error", "-i", src, "-vf", "fps=30,format=rgb24", "-f", "rawvideo", "-"],
                       stdout=subprocess.PIPE)
enc = subprocess.Popen([ff, "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{w}x{h}",
                        "-r", "30", "-i", "-", "-c:v", "libx264", "-crf", "16", "-preset", "slow",
                        "-pix_fmt", "yuv420p", "-movflags", "+faststart", dst], stdin=subprocess.PIPE)
frames = patched = 0
while True:
    data = dec.stdout.read(w * h * 3)
    if len(data) < w * h * 3:
        break
    frame = np.frombuffer(data, dtype=np.uint8).reshape(h, w, 3).copy()
    cur = frame[box[1]:box[3], box[0]:box[2]].astype(float)
    out, residual, slopes = np.empty_like(cur), 0.0, []
    for c in range(3):
        (a, b), *_ = np.linalg.lstsq(design[c], cur[..., c].ravel(), rcond=None)
        residual += np.abs(design[c] @ [a, b] - cur[..., c].ravel()).mean() / 3
        slopes.append(a)
        out[..., c] = a * new[..., c] + b
    if residual < 9 and min(slopes) > 0.15:
        frame[box[1]:box[3], box[0]:box[2]] = np.clip(out, 0, 255).astype(np.uint8)
        patched += 1
    frames += 1
    enc.stdin.write(frame.tobytes())
enc.stdin.close()
enc.wait()
dec.wait()
print(f"{src}: {patched}/{frames} frames patched")
