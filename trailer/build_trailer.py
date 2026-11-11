"""Builds the Ice Flow trailer from trailer.json.

The timeline is data: a list of segments played in order, joined by a short crossfade.
  - "title": a text card drawn here (dark background with soft light rays, the text revealed
    left to right in the brand blue), silent.
  - "clip":  a video file, scaled and padded to the output size.
The trailer is silent unless trailer.json sets "audio": true (then the clips keep their sound).

Adding to the trailer means adding a segment to trailer.json and running the script again; the
same inputs always give the same video (the light rays come from a fixed seed).

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

from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont

HERE = Path(__file__).resolve().parent

# Brand blues of the app: the text runs from the deeper to the lighter one.
BLUE_DEEP = (8, 104, 168)
BLUE_LIGHT = (24, 176, 245)
BACKGROUND = (3, 6, 12)
RAY_COLOR = (20, 60, 120)


def ffmpeg_exe() -> str:
    """ffmpeg from PATH, else the binary bundled with imageio-ffmpeg."""
    found = shutil.which("ffmpeg")
    if found:
        return found
    import imageio_ffmpeg

    return imageio_ffmpeg.get_ffmpeg_exe()


def run(args: list[str]) -> None:
    subprocess.run(args, check=True)


def probe_has_audio(ffmpeg: str, path: Path) -> bool:
    out = subprocess.run([ffmpeg, "-hide_banner", "-i", str(path)], capture_output=True, text=True).stderr
    return "Audio:" in out


def probe_duration(ffmpeg: str, path: Path) -> float:
    out = subprocess.run([ffmpeg, "-hide_banner", "-i", str(path)], capture_output=True, text=True).stderr
    for line in out.splitlines():
        line = line.strip()
        if line.startswith("Duration:"):
            h, m, s = line.split(",")[0].split()[1].split(":")
            return int(h) * 3600 + int(m) * 60 + float(s)
    raise RuntimeError(f"No duration for {path}")


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


def ease(t: float) -> float:
    t = min(1.0, max(0.0, t))
    return 1 - (1 - t) ** 3


def render_title(segment: dict, settings: Settings, ffmpeg: str, out: Path) -> None:
    width, height, fps = settings.width, settings.height, settings.fps
    duration = float(segment.get("duration", 3.0))
    reveal = float(segment.get("reveal", 1.4))
    rays = light_rays(width, height)
    filled, mask, glow, box = text_layers(segment["text"], settings)
    glow_rgb = Image.new("RGB", (width, height), BLUE_LIGHT)
    frames = int(round(duration * fps))
    soft = max(4, int(width * 0.04))

    proc = subprocess.Popen(
        [ffmpeg, "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{width}x{height}",
         "-r", str(fps), "-i", "-", "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo", "-shortest",
         "-c:v", "libx264", "-crf", "16", "-preset", "slow", "-pix_fmt", "yuv420p",
         "-c:a", "aac", "-b:a", "192k", str(out)],
        stdin=subprocess.PIPE,
    )
    for i in range(frames):
        t = i / fps
        # Background drifts slowly sideways and fades in over the first half second.
        drift = int((width * 0.08) * t / duration)
        frame = rays.crop((drift, 0, drift + width, height))
        frame = Image.blend(Image.new("RGB", (width, height), BACKGROUND), frame, ease(t / 0.5))
        # Left-to-right wipe with a soft edge over the reveal time.
        edge = box[0] + (box[2] - box[0] + soft) * ease(t / reveal)
        wipe = Image.linear_gradient("L").rotate(90, expand=True).resize((soft, height))
        wipe_mask = Image.new("L", (width, height), 0)
        wipe_mask.paste(255, (0, 0, max(0, int(edge - soft)), height))
        wipe_mask.paste(ImageChops.invert(wipe), (int(edge - soft), 0))
        text_mask = ImageChops.multiply(mask, wipe_mask)
        glow_mask = ImageChops.multiply(glow, wipe_mask)
        frame = Image.composite(glow_rgb, frame, glow_mask)
        frame = Image.composite(filled, frame, text_mask)
        proc.stdin.write(frame.tobytes())
    proc.stdin.close()
    if proc.wait() != 0:
        raise RuntimeError("ffmpeg failed while encoding the title")


# ---- Clip ---------------------------------------------------------------------------------------


def render_clip(segment: dict, settings: Settings, ffmpeg: str, out: Path) -> None:
    src = (HERE / segment["path"]).resolve()
    if not src.exists():
        raise FileNotFoundError(f"Clip not found: {src} (source clips go to trailer/assets/)")
    w, h, fps = settings.width, settings.height, settings.fps
    vf = f"scale={w}:{h}:force_original_aspect_ratio=decrease:flags=lanczos,pad={w}:{h}:(ow-iw)/2:(oh-ih)/2,fps={fps},format=yuv420p"
    if "start" in segment or "end" in segment:
        vf = f"trim={segment.get('start', 0)}:{segment.get('end', 1e9)},setpts=PTS-STARTPTS," + vf
    args = [ffmpeg, "-y", "-loglevel", "error", "-i", str(src)]
    if probe_has_audio(ffmpeg, src):
        af = "aresample=48000,aformat=channel_layouts=stereo"
        if "start" in segment or "end" in segment:
            af = f"atrim={segment.get('start', 0)}:{segment.get('end', 1e9)},asetpts=PTS-STARTPTS," + af
        args += ["-vf", vf, "-af", af]
    else:
        args += ["-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo", "-vf", vf, "-shortest"]
    args += ["-c:v", "libx264", "-crf", "16", "-preset", "slow", "-c:a", "aac", "-b:a", "192k", str(out)]
    run(args)


# ---- Assembly -----------------------------------------------------------------------------------


def join(parts: list[Path], transition: float, settings: Settings, ffmpeg: str, out: Path, audio: bool) -> None:
    """Crossfades every part into the next - the picture, and the sound too when `audio` is on."""
    durations = [probe_duration(ffmpeg, p) for p in parts]
    width, height, fps = settings.width, settings.height, settings.fps
    starts = [0.0]
    for d in durations[:-1]:
        starts.append(starts[-1] + d - transition)
    total = starts[-1] + durations[-1]
    args = [ffmpeg, "-y", "-loglevel", "error"]
    for p in parts:
        args += ["-i", str(p)]
    # Picture: every part laid over a black canvas at its start time, each after the first fading
    # in over the one before it. Built from overlay + an alpha fade rather than xfade, so ffmpeg
    # older than 4.3 (the one bundled with imageio-ffmpeg for Python 3.8) works too.
    chains = [f"color=c=black:s={width}x{height}:r={fps}:d={total:.3f}[c0]"]
    v_prev = "c0"
    for i, start in enumerate(starts):
        fade = f",fade=t=in:st=0:d={transition}:alpha=1" if i > 0 else ""
        chains.append(f"[{i}:v]format=yuva420p{fade},setpts=PTS-STARTPTS+{start:.3f}/TB[p{i}]")
        chains.append(f"[{v_prev}][p{i}]overlay=eof_action=pass:format=auto[c{i + 1}]")
        v_prev = f"c{i + 1}"
    sound = ["-an"]
    if audio:
        a_prev = "0:a"
        for i in range(1, len(parts)):
            chains.append(f"[{a_prev}][{i}:a]acrossfade=d={transition}[a{i}]")
            a_prev = f"a{i}"
        sound = ["-map", f"[{a_prev}]", "-c:a", "aac", "-b:a", "192k"]
    args += ["-filter_complex", ";".join(chains), "-map", f"[{v_prev}]", *sound,
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
    with tempfile.TemporaryDirectory() as tmp:
        parts = []
        for index, segment in enumerate(config["segments"]):
            part = Path(tmp) / f"part{index:02d}.mp4"
            kind = segment["type"]
            print(f"[{index + 1}/{len(config['segments'])}] {kind}: {segment.get('text') or segment.get('path')}")
            if kind == "title":
                render_title(segment, settings, ffmpeg, part)
            elif kind == "clip":
                render_clip(segment, settings, ffmpeg, part)
            else:
                raise ValueError(f"Unknown segment type {kind!r}")
            parts.append(part)
        join(parts, float(config.get("transition", 0.6)), settings, ffmpeg, out, bool(config.get("audio", False)))
    print(f"Done: {out}")


if __name__ == "__main__":
    main()
