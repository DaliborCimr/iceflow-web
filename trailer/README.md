# Trailer

`build_trailer.py` renders the Ice Flow trailer from `trailer.json`: a list of segments played in
order and joined by a short crossfade.

- `title` - a text card drawn by the script (light rays, the text revealed left to right in the
  brand blue). Fields: `text`, `duration`, `reveal` (seconds the reveal takes).
- `clip` - a video from `assets/`, scaled to the output size. Optional `start`
  and `end` (seconds) cut a part of it.

The trailer is silent; `"audio": true` in `trailer.json` keeps the clips' sound.

To extend the trailer, put the new clip into `assets/`, add a segment to `trailer.json` and run:

```bash
pip install -r requirements.txt
python build_trailer.py
```

The result is `out/trailer.mp4`. `assets/` and `out/` are not in git - keep the source clips
elsewhere too. The light rays come from a fixed seed, so the same inputs give the same video.
