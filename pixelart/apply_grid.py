#!/usr/bin/env python3
"""Write an editor save payload back to sprites/<name>.py.

Single write path shared by editor_server.py (POST /api/save) and the
serverless flow: when no local server is running, the editor downloads
the grid JSON instead of saving, and this CLI applies that dump through
the same decompile + assert + atomic replace (rolled back if the
full-set rebuild fails):

    python3 pixelart/apply_grid.py dump.json
"""

import importlib
import json
import os
import subprocess
import sys
from pathlib import Path

import build_sprites
import decompile
import spritekit as sk
from decompile import DecompileError

HERE = Path(__file__).resolve().parent
SPRITES = HERE / "sprites"


def stem_for(slug, sprites_dir=None):
    """Existing module stem for a slug, or the underscore form for new ones."""
    sys.path.insert(0, str(sprites_dir or SPRITES))
    for p in sorted((sprites_dir or SPRITES).glob("*.py")):
        if p.stem.startswith("_"):
            continue
        try:
            mod = importlib.import_module(p.stem)
        except ImportError:
            continue
        if mod.CONFIG["name"] == slug:
            return p.stem
    return slug.replace("-", "_")


def apply(payload, sprites_dir=None, rebuild=False):
    """Validate a payload and write it as sprites/<stem>.py.

    Returns a report dict; raises DecompileError/SystemExit on refusal
    (nothing is written in that case). A failed full-set rebuild rolls
    the write back, leaving a sprite set that still builds.
    """
    cfg, text = decompile.decompile(payload)
    build_sprites.validate_slugs([cfg])
    build_sprites.validate_dimensions([cfg])

    sprites = sprites_dir or SPRITES
    stem = stem_for(cfg["name"], sprites)
    path = sprites / f"{stem}.py"
    existed = path.exists()
    old_text = path.read_text() if existed else None
    # the cached module still holds the pre-save config even after the
    # replace below; rollback needs it to restore the sprite's PNGs
    old_mod = sys.modules.get(stem)
    changed = True
    if existed:
        if old_text == text:
            changed = False
        else:
            # same view, different text (hand-authored comments/run splits):
            # rewriting would only normalize the file, skip it
            mod = sys.modules.get(stem) or importlib.import_module(stem)
            if sk.build_grid(mod.CONFIG) == sk.build_grid(cfg):
                changed = False
    if changed:
        tmp = path.with_suffix(".py.tmp")
        tmp.write_text(text)
        os.replace(tmp, path)

    log = ""
    if rebuild:
        run = subprocess.run(
            [sys.executable, str(HERE / "build_sprites.py"), cfg["name"]],
            capture_output=True,
            text=True,
        )
        log = run.stdout + run.stderr
        if run.returncode != 0:
            rollback(path, cfg, old_mod, existed, changed, old_text)
            raise RuntimeError(f"post-save rebuild failed, save rolled back:\n{log}")
    return {"file": str(path), "stem": stem, "existed": existed,
            "changed": changed, "log": log}


def rollback(path, cfg, old_mod, existed, changed, old_text):
    """Undo a save whose full-set rebuild failed: restore the previous
    config text (or drop a newly added one plus its fresh PNGs), then
    rebuild the saved sprite's own PNGs from the rolled-back config."""
    if not changed:
        return
    if existed:
        path.write_text(old_text)
        if old_mod is not None:
            build_sprites.build_dev(old_mod.CONFIG)
    else:
        path.unlink()
        for suffix in ("_sprite.png", "_sprite_preview.png",
                       "_sprite_vs_original.png"):
            png = build_sprites.HERE / f"{cfg['name']}{suffix}"
            if png.exists():
                png.unlink()


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: apply_grid.py <dump.json>")
    dump = json.loads(Path(sys.argv[1]).read_text())
    try:
        report = apply(dump, rebuild=True)
    except DecompileError as e:
        sys.exit(f"refused: {e}")
    print(f"wrote {report['file']}")
    if not report["changed"]:
        print("view unchanged since last save")
    if report["log"]:
        print(report["log"].rstrip())


if __name__ == "__main__":
    main()
