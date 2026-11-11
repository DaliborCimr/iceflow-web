"""Builds the Ice Flow trailer from trailer.json.

The timeline is data: a list of segments played in order. Each is joined to the one before by a
crossfade - the global "transition", or the segment's own "transition" (0 = a straight cut).

  - "title"     a text card drawn here: dark background with soft light rays, the text revealed
                left to right in the brand blue.
                  text, duration, reveal (seconds the reveal takes)
  - "clip"      a video file, scaled into the frame (letterboxed when its shape differs).
                  path, start / end (seconds of the source), speed (2 = twice as fast),
                  hold (seconds the last frame stays),
                  taps (a .taps.json written while recording: where and when the screen was
                  touched - drawn as a touch marker, since a screen recording shows no finger)
  - "logo_zoom" the camera flies into the logo in a clip's background while the clip keeps
                playing; the sharp logo artwork fades in exactly over it and the room behind
                darkens away. With "transition": 0 and "from" where the clip before it ended, the
                footage runs on without a seam.
                  path, from (seconds of the source), speed, box (the logo in the source's
                  pixels: [x0, y0, x1, y1]), logo (transparent PNG), duration, zoom (seconds the
                  camera moves), margin (room left around the logo at the end)

The trailer is silent. Adding to it means adding a segment to trailer.json and running the
script again; the same inputs always give the same video (the light rays come from a fixed seed).

Source clips live in assets/ and the result in out/ - both stay out of git (see .gitignore);
only this script and the timeline are versioned.

Usage:
    pip install -r requirements.txt
    python build_trailer.py [trailer.json]
"""

from __future__ import annotations

import json
import random
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator

from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont

HERE = Path(__file__).resolve().parent

# Brand blues of the app: the text runs from the deeper to the lighter one.
BLUE_DEEP = (8, 104, 168)
BLUE_LIGHT = (24, 176, 245)
BACKGROUND = (3, 6, 12)
RAY_COLOR = (20, 60, 120)
LETTERBOX = (5, 10, 15)  # the app's own background behind a phone-shaped recording


def ffmpeg_exe() -> str:
    """ffmpeg from PATH, else the binary bundled with imageio-ffmpeg."""
    found = shutil.which("ffmpeg")
    if found:
        return found
    import imageio_ffmpeg

    return imageio_ffmpeg.get_ffmpeg_exe()


def run(args: list[str]) -> None:
    subprocess.run(args, check=True)


def probe(ffmpeg: str, path: Path) -> tuple[float, int, int]:
    """Duration in seconds and the video's width and height."""
    out = subprocess.run([ffmpeg, "-hide_banner", "-i", str(path)], capture_output=True, text=True).stderr
    duration, size = None, None
    for line in out.splitlines():
        line = line.strip()
        if line.startswith("Duration:"):
            h, m, s = line.split(",")[0].split()[1].split(":")
            duration = int(h) * 3600 + int(m) * 60 + float(s)
        if "Video:" in line and size is None:
            for token in line.replace(",", " ").split():
                if "x" in token and token.split("x")[0].isdigit() and token.split("x")[1].isdigit():
                    size = tuple(int(v) for v in token.split("x"))
                    break
    if duration is None or size is None:
        raise RuntimeError(f"Cannot read {path}")
    return duration, size[0], size[1]


@dataclass
class Settings:
    width: int
    height: int
    fps: int
    font: Path


def pick_font(candidates: list[str]) -> Path:
    for candidate in candidates:
        path = Path(candidate)
        if not path.is_absolute():
            path = HERE / path
        if path.exists():
            return path
    raise FileNotFoundError("None of the fonts in trailer.json exists: " + ", ".join(candidates))


def ease(t: float) -> float:
    t = min(1.0, max(0.0, t))
    return 1 - (1 - t) ** 3


def ease_in_out(t: float) -> float:
    t = min(1.0, max(0.0, t))
    return t * t * (3 - 2 * t)


class Encoder:
    """Frames in, an mp4 out (silent, constant frame rate)."""

    def __init__(self, ffmpeg: str, settings: Settings, out: Path):
        self.proc = subprocess.Popen(
            [ffmpeg, "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
             "-s", f"{settings.width}x{settings.height}", "-r", str(settings.fps), "-i", "-",
             "-c:v", "libx264", "-crf", "16", "-preset", "slow", "-pix_fmt", "yuv420p", str(out)],
            stdin=subprocess.PIPE,
        )

    def write(self, frame: Image.Image) -> None:
        self.proc.stdin.write(frame.tobytes())

    def close(self) -> None:
        self.proc.stdin.close()
        if self.proc.wait() != 0:
            raise RuntimeError("ffmpeg failed while encoding")


def source_frames(ffmpeg: str, src: Path, fps: int, start: float, end: float | None, speed: float) -> Iterator[Image.Image]:
    """The source's frames at its own size, cut and sped up, at the output frame rate.

    ffmpeg only cuts (-ss / -t) and makes the frame rate constant; speeding up is done here by
    taking every speed-th frame. Piped out as raw frames, ffmpeg 4.2 filled both a trim filter's
    cut-off start and a setpts speed-up back in with copies.
    """
    _, w, h = probe(ffmpeg, src)
    args = [ffmpeg, "-loglevel", "error", "-ss", f"{start:.3f}", "-i", str(src)]
    if end is not None:
        args += ["-t", f"{float(end) - start:.3f}"]
    args += ["-vf", f"fps={fps},format=rgb24", "-f", "rawvideo", "-"]
    proc = subprocess.Popen(args, stdout=subprocess.PIPE)
    size = w * h * 3
    index, wanted = 0, 0.0
    while True:
        data = proc.stdout.read(size)
        if len(data) < size:
            break
        while index >= round(wanted):
            yield Image.frombytes("RGB", (w, h), data)
            wanted += speed
        index += 1
    proc.wait()


# ---- Title card ---------------------------------------------------------------------------------


def light_rays(width: int, height: int, seed: int = 7) -> Image.Image:
    """Soft vertical light falling from above - drawn once, blurred, slowly drifted per frame."""
    rng = random.Random(seed)
    layer = Image.new("RGB", (width * 2, height), BACKGROUND)
    draw = ImageDraw.Draw(layer)
    for _ in range(60):
        x = rng.uniform(0, width * 2)
        w = rng.uniform(width * 0.01, width * 0.05)
        tilt = rng.uniform(-0.15, 0.15) * height
        strength = rng.uniform(0.25, 1.0)
        color = tuple(int(BACKGROUND[i] + (RAY_COLOR[i] - BACKGROUND[i]) * strength) for i in range(3))
        draw.polygon([(x - w, 0), (x + w, 0), (x + w + tilt, height), (x - w + tilt, height)], fill=color)
    layer = layer.filter(ImageFilter.GaussianBlur(width * 0.012))
    # Fade the rays out towards the bottom, the way the light falls off.
    fade = Image.linear_gradient("L").resize((width * 2, height))
    fade = ImageChops.invert(fade).point(lambda v: int(v * 0.85))
    return Image.composite(layer, Image.new("RGB", layer.size, BACKGROUND), fade)


def text_layers(text: str, settings: Settings) -> tuple[Image.Image, Image.Image, Image.Image, tuple[int, int, int, int]]:
    """The gradient-filled text, its glow and its bounding box - sized to sit inside the frame."""
    width, height = settings.width, settings.height
    # Largest size that keeps the text within 84 % of the width.
    size = int(height * 0.16)
    while True:
        font = ImageFont.truetype(str(settings.font), size)
        left, top, right, bottom = font.getbbox(text)
        if right - left <= width * 0.84 or size < 10:
            break
        size -= 2
    mask = Image.new("L", (width, height), 0)
    x = (width - (right - left)) // 2 - left
    y = int(height * 0.38) - (bottom - top) // 2 - top
    ImageDraw.Draw(mask).text((x, y), text, font=font, fill=255)
    box = mask.getbbox() or (0, 0, width, height)

    span = max(1, box[2] - box[0])
    column = Image.new("RGB", (width, 1))
    for cx in range(width):
        t = min(1.0, max(0.0, (cx - box[0]) / span))
        column.putpixel((cx, 0), tuple(int(BLUE_DEEP[i] + (BLUE_LIGHT[i] - BLUE_DEEP[i]) * t) for i in range(3)))
    gradient = column.resize((width, height))
    glow = mask.filter(ImageFilter.GaussianBlur(height * 0.02)).point(lambda v: int(v * 0.55))
    return Image.composite(gradient, Image.new("RGB", (width, height)), mask), mask, glow, box


def render_title(segment: dict, settings: Settings, ffmpeg: str, out: Path) -> None:
    width, height, fps = settings.width, settings.height, settings.fps
    duration = float(segment.get("duration", 3.0))
    reveal = float(segment.get("reveal", 1.4))
    rays = light_rays(width, height)
    filled, mask, glow, box = text_layers(segment["text"], settings)
    glow_rgb = Image.new("RGB", (width, height), BLUE_LIGHT)
    soft = max(4, int(width * 0.04))
    wipe = ImageChops.invert(Image.linear_gradient("L").rotate(90, expand=True).resize((soft, height)))
    encoder = Encoder(ffmpeg, settings, out)
    for i in range(int(round(duration * fps))):
        t = i / fps
        # Background drifts slowly sideways and fades in over the first half second.
        drift = int((width * 0.08) * t / duration)
        frame = rays.crop((drift, 0, drift + width, height))
        frame = Image.blend(Image.new("RGB", (width, height), BACKGROUND), frame, ease(t / 0.5))
        # Left-to-right wipe with a soft edge over the reveal time.
        edge = box[0] + (box[2] - box[0] + soft) * ease(t / reveal)
        wipe_mask = Image.new("L", (width, height), 0)
        wipe_mask.paste(255, (0, 0, max(0, int(edge - soft)), height))
        wipe_mask.paste(wipe, (int(edge - soft), 0))
        frame = Image.composite(glow_rgb, frame, ImageChops.multiply(glow, wipe_mask))
        frame = Image.composite(filled, frame, ImageChops.multiply(mask, wipe_mask))
        encoder.write(frame)
    encoder.close()


# ---- Clip ---------------------------------------------------------------------------------------


def load_taps(segment: dict) -> list[dict]:
    taps = segment.get("taps", [])
    if isinstance(taps, str):
        taps = json.loads((HERE / taps).read_text(encoding="utf-8"))
    return taps


def draw_touch(frame: Image.Image, x: float, y: float, age: float, scale: float) -> None:
    """A finger's touch: a filled dot that appears at once and a ring that widens and fades."""
    if age < 0 or age > 0.6:
        return
    overlay = Image.new("RGBA", frame.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    dot = 22 * scale
    dot_alpha = int(200 * (1 - ease_in_out(max(0.0, age - 0.25) / 0.35)))
    draw.ellipse((x - dot, y - dot, x + dot, y + dot), fill=(255, 255, 255, dot_alpha))
    ring = (22 + 70 * ease(age / 0.6)) * scale
    ring_alpha = int(220 * (1 - age / 0.6))
    draw.ellipse((x - ring, y - ring, x + ring, y + ring), outline=(255, 255, 255, ring_alpha), width=max(2, int(4 * scale)))
    frame.paste(Image.alpha_composite(frame.convert("RGBA"), overlay).convert("RGB"))


def fit(frame: Image.Image, settings: Settings) -> tuple[Image.Image, float, float, float]:
    """The source frame scaled into the output, letterboxed; also the scale and offsets used."""
    w, h = settings.width, settings.height
    scale = min(w / frame.width, h / frame.height)
    size = (round(frame.width * scale), round(frame.height * scale))
    canvas = Image.new("RGB", (w, h), LETTERBOX)
    ox, oy = (w - size[0]) // 2, (h - size[1]) // 2
    canvas.paste(frame.resize(size, Image.LANCZOS), (ox, oy))
    return canvas, scale, ox, oy


def render_clip(segment: dict, settings: Settings, ffmpeg: str, out: Path) -> None:
    src = (HERE / segment["path"]).resolve()
    if not src.exists():
        raise FileNotFoundError(f"Clip not found: {src} (source clips go to trailer/assets/)")
    start = float(segment.get("start", 0))
    end = segment.get("end")
    speed = float(segment.get("speed", 1.0))
    taps = load_taps(segment)
    encoder = Encoder(ffmpeg, settings, out)
    frame = None
    for i, raw in enumerate(source_frames(ffmpeg, src, settings.fps, start, end, speed)):
        frame, scale, ox, oy = fit(raw, settings)
        t_source = start + i / settings.fps * speed
        for tap in taps:
            draw_touch(frame, ox + tap["x"] * scale, oy + tap["y"] * scale, (t_source - tap["t"]) / speed, scale * settings.height / 1080)
        encoder.write(frame)
    # A screen recording stops when the screen stops changing; "hold" keeps its last picture.
    for _ in range(int(round(float(segment.get("hold", 0)) * settings.fps))):
        encoder.write(frame)
    encoder.close()


# ---- Logo zoom ----------------------------------------------------------------------------------


def render_logo_zoom(segment: dict, settings: Settings, ffmpeg: str, out: Path) -> None:
    w, h, fps = settings.width, settings.height, settings.fps
    src = (HERE / segment["path"]).resolve()
    duration = float(segment.get("duration", 3.0))
    zoom_time = float(segment.get("zoom", duration * 0.75))
    margin = float(segment.get("margin", 1.6))
    x0, y0, x1, y1 = segment["box"]
    logo = Image.open(HERE / segment["logo"]).convert("RGBA")
    logo = logo.crop(logo.getbbox())
    footage = list(source_frames(ffmpeg, src, fps, float(segment.get("from", 0)), None, float(segment.get("speed", 1.0))))
    if not footage:
        raise RuntimeError(f"No footage left in {src} after {segment.get('from', 0)} s")
    bw, bh = footage[0].size

    # Camera rectangles in the source's pixels, both of the output's aspect ratio. The first one
    # is the whole frame as the clip before showed it, so a straight cut into this has no seam.
    aspect = w / h
    first_h = bh if bw / bh >= aspect else bw / aspect
    first = ((bw - first_h * aspect) / 2, (bh - first_h) / 2, (bw + first_h * aspect) / 2, (bh + first_h) / 2)
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    end_h = max((y1 - y0), (x1 - x0) / aspect) * margin
    last = (cx - end_h * aspect / 2, cy - end_h / 2, cx + end_h * aspect / 2, cy + end_h / 2)
    dark = Image.new("RGB", (w, h), BACKGROUND)

    encoder = Encoder(ffmpeg, settings, out)
    for i in range(int(round(duration * fps))):
        base = footage[min(i, len(footage) - 1)]  # the footage plays on, then holds its last frame
        p = ease_in_out(i / fps / zoom_time)
        cam = tuple(first[k] + (last[k] - first[k]) * p for k in range(4))
        frame = base.transform((w, h), Image.EXTENT, cam, resample=Image.BICUBIC)
        # The room fades to the trailer's dark as the camera arrives.
        frame = Image.blend(frame, dark, ease_in_out((p - 0.5) / 0.5) * 0.92)
        # The sharp logo, placed where the frame's own logo is, fading in over the second half.
        alpha = ease_in_out((p - 0.3) / 0.6)
        if alpha > 0:
            sx, sy = w / (cam[2] - cam[0]), h / (cam[3] - cam[1])
            lx0, ly0 = (x0 - cam[0]) * sx, (y0 - cam[1]) * sy
            lw, lh = (x1 - x0) * sx, (y1 - y0) * sy
            scale = min(lw / logo.width, lh / logo.height)
            size = (max(1, int(logo.width * scale)), max(1, int(logo.height * scale)))
            sharp = logo.resize(size, Image.LANCZOS)
            layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
            layer.paste(sharp, (int(lx0 + (lw - size[0]) / 2), int(ly0 + (lh - size[1]) / 2)), sharp)
            layer.putalpha(layer.getchannel("A").point(lambda v: int(v * alpha)))
            frame = Image.alpha_composite(frame.convert("RGBA"), layer).convert("RGB")
        encoder.write(frame)
    encoder.close()


# ---- Assembly -----------------------------------------------------------------------------------


def join(parts: list[Path], transitions: list[float], settings: Settings, ffmpeg: str, out: Path) -> None:
    """Lays every part over a black canvas at its start; each fades in over the one before it
    for its transition (0 = a cut). Overlay + an alpha fade rather than xfade, so ffmpeg older
    than 4.3 (the one bundled with imageio-ffmpeg for Python 3.8) works too."""
    durations = [probe(ffmpeg, p)[0] for p in parts]
    starts = [0.0]
    for i in range(1, len(parts)):
        starts.append(starts[-1] + durations[i - 1] - transitions[i])
    total = starts[-1] + durations[-1]
    args = [ffmpeg, "-y", "-loglevel", "error"]
    for p in parts:
        args += ["-i", str(p)]
    chains = [f"color=c=black:s={settings.width}x{settings.height}:r={settings.fps}:d={total:.3f}[c0]"]
    for i, start in enumerate(starts):
        fade = f",fade=t=in:st=0:d={transitions[i]}:alpha=1" if i > 0 and transitions[i] > 0 else ""
        chains.append(f"[{i}:v]format=yuva420p{fade},setpts=PTS-STARTPTS+{start:.3f}/TB[p{i}]")
        chains.append(f"[c{i}][p{i}]overlay=eof_action=pass:format=auto[c{i + 1}]")
    args += ["-filter_complex", ";".join(chains), "-map", f"[c{len(parts)}]", "-an",
             "-c:v", "libx264", "-crf", "18", "-preset", "slow", "-pix_fmt", "yuv420p",
             "-movflags", "+faststart", str(out)]
    run(args)


def main() -> None:
    config_path = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "trailer.json"
    config = json.loads(config_path.read_text(encoding="utf-8"))
    settings = Settings(
        width=int(config.get("width", 1920)),
        height=int(config.get("height", 1080)),
        fps=int(config.get("fps", 30)),
        font=pick_font(config.get("fonts", [])),
    )
    ffmpeg = ffmpeg_exe()
    out = HERE / config.get("output", "out/trailer.mp4")
    out.parent.mkdir(parents=True, exist_ok=True)
    renderers = {"title": render_title, "clip": render_clip, "logo_zoom": render_logo_zoom}
    default_transition = float(config.get("transition", 0.5))
    with tempfile.TemporaryDirectory() as tmp:
        parts, transitions = [], []
        for index, segment in enumerate(config["segments"]):
            part = Path(tmp) / f"part{index:02d}.mp4"
            kind = segment["type"]
            print(f"[{index + 1}/{len(config['segments'])}] {kind}: {segment.get('text') or segment.get('path')}")
            if kind not in renderers:
                raise ValueError(f"Unknown segment type {kind!r}")
            renderers[kind](segment, settings, ffmpeg, part)
            parts.append(part)
            transitions.append(float(segment.get("transition", default_transition)) if index > 0 else 0.0)
        join(parts, transitions, settings, ffmpeg, out)
    print(f"Done: {out}")


if __name__ == "__main__":
    main()
