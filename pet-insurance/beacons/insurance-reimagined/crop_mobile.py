#!/usr/bin/env python3
"""
Crop all _mobile.png files in a folder tree to 1284x2915 (from top-left).
Usage: python3 crop_mobile.py /path/to/your/folder
"""

import sys
from pathlib import Path
from PIL import Image

def crop_mobile_screenshots(root_dir):
    root = Path(root_dir)
    files = list(root.rglob("*_mobile.png"))
    
    if not files:
        print("No _mobile.png files found.")
        return

    print(f"Found {len(files)} file(s). Cropping to 1284x2915...")
    
    skipped = []
    for f in files:
        img = Image.open(f)
        w, h = img.size
        if h < 2915:
            print(f"  SKIP  {f.name} — only {h}px tall")
            skipped.append(f)
            continue
        cropped = img.crop((0, 0, 1284, 2915))
        cropped.save(f)
        print(f"  OK    {f.name}")
    
    done = len(files) - len(skipped)
    print(f"\nDone. {done} cropped, {len(skipped)} skipped (too short).")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 crop_mobile.py /path/to/folder")
        sys.exit(1)
    crop_mobile_screenshots(sys.argv[1])
