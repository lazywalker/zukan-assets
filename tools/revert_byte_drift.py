#!/usr/bin/env python3
"""Revert working-tree source changes that are byte drift, not real edits.

The weekly check re-downloads every Fandom icon into a fresh fandom-raw/,
and the CDN re-encodes WebP responses over time. split_sprites.py copies
those bytes into committed source/*-processed files: pixel-identical images
with slightly different bytes, enough for git to open an empty update PR.

This script walks git-modified files under source/, decodes each against
its HEAD version and restores the HEAD bytes when the decoded pixels match.
JSON manifests get an order-insensitive compare instead: record order
follows the wiki crawl, and a reorder alone is not a change. Files that are
new, deleted, or genuinely different are left for the PR step.

CI hygiene only; run it before committing pipeline output.
"""

from __future__ import annotations

import io
import json
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageChops

ROOT = Path(__file__).resolve().parent.parent


def git(*args: str) -> bytes:
    r = subprocess.run(["git", *args], cwd=ROOT, capture_output=True)
    if r.returncode != 0:
        sys.exit(f"git {' '.join(args)} failed: {r.stderr.decode().strip()}")
    return r.stdout


def canon(node) -> str:
    """Canonical string for parsed JSON, lists compared as multisets."""
    if isinstance(node, list):
        return "[" + ",".join(sorted(canon(x) for x in node)) + "]"
    if isinstance(node, dict):
        return "{" + ",".join(sorted(f"{k}:{canon(v)}" for k, v in node.items())) + "}"
    return json.dumps(node, ensure_ascii=False, sort_keys=True)


def same_json(old: bytes, new: bytes) -> bool:
    try:
        return canon(json.loads(old)) == canon(json.loads(new))
    except ValueError:  # bad utf8 or malformed json: not comparable
        return False


def same_pixels(old: bytes, new: bytes) -> bool:
    try:
        a = Image.open(io.BytesIO(old)).convert("RGBA")
        b = Image.open(io.BytesIO(new)).convert("RGBA")
    except Exception:  # not decodable as an image (svg, text): not comparable
        return False
    if a.size != b.size:
        return False
    return ImageChops.difference(a, b).getbbox() is None


def main() -> int:
    dry_run = "--dry-run" in sys.argv[1:]
    status = git("status", "--porcelain", "-z").decode().split("\0")
    reverted = kept = 0
    for entry in status:
        if len(entry) < 4 or "M" not in entry[:2]:
            continue
        path = entry[3:]
        if not path.startswith("source/"):
            continue
        r = subprocess.run(["git", "show", f"HEAD:{path}"], cwd=ROOT, capture_output=True)
        if r.returncode != 0:
            continue  # not in HEAD: a new file, always a real change
        head, cur = r.stdout, (ROOT / path).read_bytes()
        if head == cur:
            continue
        same = same_json(head, cur) if path.endswith(".json") else same_pixels(head, cur)
        if same:
            reverted += 1
            print(f"  revert (byte drift only): {path}")
            if not dry_run:
                git("checkout", "HEAD", "--", path)
        else:
            kept += 1
            print(f"  keep (real change): {path}")
    print(f"  {reverted} reverted, {kept} real changes kept" + (" (dry run)" if dry_run else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
