# Trailer

`build_trailer.py` renders the Ice Flow trailer from `trailer.json`: a list of segments played in
order and joined by a short crossfade.

- `title` - a text card drawn by the script (light rays, the text revealed left to right in the
  brand blue). Fields: `text`, `duration`, `reveal`.
- `clip` - a video from `assets/`. Optional `start`/`end` (seconds), `speed` (2 = twice as fast),
  `hold` (seconds the last frame stays) and `taps` - a `.taps.json` with where and when the screen
  was touched, drawn as a touch marker (a screen recording shows no finger).
- `logo_zoom` - the camera flies into the logo in a clip's background while the clip plays on;
  the sharp logo artwork fades in over it. With `"transition": 0` and `from` where the clip before
  ended, the footage runs on without a seam.

Each segment fades in over the one before for `transition` seconds (its own or the global one).

The trailer is silent.

To extend the trailer, put the new clip into `assets/`, add a segment to `trailer.json` and run:

```bash
pip install -r requirements.txt
python build_trailer.py
```

The result is `out/trailer.mp4`. `assets/` and `out/` are not in git - keep the source clips
elsewhere too. The light rays come from a fixed seed, so the same inputs give the same video.

New app footage: `tools/record_with_taps.py` records the Android emulator while it taps, and
writes the `.taps.json` beside the video (needs adb from the Android SDK).
