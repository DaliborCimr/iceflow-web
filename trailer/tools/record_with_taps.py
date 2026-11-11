# -*- coding: utf-8 -*-
# Records the emulator screen while performing taps, and writes the taps (seconds from the first
# frame, x/y in the recording's pixels) next to the video as <name>.taps.json, for the trailer's
# touch markers.
# Usage: python rec_taps.py <out.mp4> <seconds> "tap X Y" "wait S" ...   (X/Y in device pixels)
import json
import os
import subprocess
import sys
import time

ADB = os.path.join(os.environ["LOCALAPPDATA"], "Android", "Sdk", "platform-tools", "adb.exe")
DEVICE_W, DEVICE_H = 2400, 1080
REC_W, REC_H = 1600, 720
LATENCY = 0.45  # screenrecord's first frame comes about this long after it is started

out, seconds, actions = sys.argv[1], float(sys.argv[2]), sys.argv[3:]
subprocess.run([ADB, "shell", "rm", "-f", "/data/local/tmp/rt.mp4"])
rec = subprocess.Popen([ADB, "shell", "screenrecord", "--time-limit", str(int(seconds)), "--bit-rate", "12000000",
                        "--size", f"{REC_W}x{REC_H}", "/data/local/tmp/rt.mp4"])
t0 = time.time() + LATENCY
taps = []
time.sleep(1.0)
for action in actions:
    kind, *args = action.split()
    if kind == "wait":
        time.sleep(float(args[0]))
    elif kind == "tap":
        x, y = int(args[0]), int(args[1])
        taps.append({"t": round(time.time() - t0, 3), "x": round(x * REC_W / DEVICE_W), "y": round(y * REC_H / DEVICE_H)})
        subprocess.run([ADB, "shell", "input", "tap", str(x), str(y)])
rec.wait()
subprocess.run([ADB, "pull", "/data/local/tmp/rt.mp4", out], stdout=subprocess.DEVNULL)
with open(os.path.splitext(out)[0] + ".taps.json", "w", encoding="utf-8") as f:
    json.dump(taps, f, indent=1)
print(out, taps)
