#!/usr/bin/env python3
"""Editor chain self-checks (tools/ script style, no framework).

- view synthesis matches the engine on every committed config
- decompile round-trip is exact on every committed config; sprites added
  later join automatically
- apply() refuses bad payloads (unknown slug, too tall, bad mask, view
  that disagrees with the mask rules) and writes nothing when refusing
- a save whose post-save rebuild fails is rolled back: previous config
  text restored, newly added config removed
"""

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import apply_grid
import decompile
import spritekit as sk
from build_sprites import load_configs
from decompile import DecompileError


def payload_for(cfg, docstring=""):
    state = decompile.editor_state(cfg)
    w, h = cfg["size"]
    mask = decompile.unpack_rows(state["mask"], w, h)
    explicit = {
        tuple(int(x) for x in k.split(",")): v for k, v in state["explicit"].items()
    }
    return {
        "slug": cfg["name"],
        "size": [w, h],
        "base": cfg["base"],
        "palette": {ch: list(rgba) for ch, rgba in cfg["palette"].items()},
        "mask": state["mask"],
        "explicit": state["explicit"],
        "docstring": docstring or f"{cfg['name']} editor round trip",
        "compare_to": cfg.get("compare_to", ""),
        "view": decompile.synthesize(mask, explicit, w, h, cfg["base"]),
    }


def synth_matches_engine():
    for cfg in load_configs():
        p = payload_for(cfg)
        mask = decompile.unpack_rows(p["mask"], *cfg["size"])
        explicit = {
            tuple(int(x) for x in k.split(",")): v
            for k, v in p["explicit"].items()
        }
        view = decompile.synthesize(mask, explicit, *cfg["size"], cfg["base"])
        assert view == ["".join(r) for r in sk.build_grid(cfg)], cfg["name"]


def round_trip_exact():
    for cfg in load_configs():
        cfg2, _ = decompile.decompile(payload_for(cfg))
        assert sk.build_grid(cfg2) == sk.build_grid(cfg), cfg["name"]


def save_refusals():
    cfg = {"name": "rathalos", "size": (4, 2), "base": "R",
           "spans": {0: [(1, 2)]}, "fills": [],
           "palette": {".": (0, 0, 0, 0), "K": (0, 0, 0, 255), "R": (1, 2, 3, 255)}}

    tmp = Path(tempfile.mkdtemp())
    try:
        # unknown slug
        bad = dict(payload_for(cfg), slug="not-a-monster")
        try:
            apply_grid.apply(bad, sprites_dir=tmp)
        except SystemExit:
            pass
        else:
            raise AssertionError("unknown slug accepted")
        assert not list(tmp.glob("*.py"))

        # too tall; refusal must come from the height rule, after decompile
        tall = dict(cfg, size=(4, 28), spans={i: [(0, 3)] for i in range(28)})
        p = payload_for(tall)
        p["size"] = [4, 28]
        try:
            apply_grid.apply(p, sprites_dir=tmp)
        except SystemExit:
            pass
        else:
            raise AssertionError("28px height accepted")
        assert not list(tmp.glob("*.py"))

        # mask wider than size
        p = payload_for(cfg)
        p["mask"] = ["ff", "0"]
        try:
            apply_grid.apply(p, sprites_dir=tmp)
        except DecompileError:
            pass
        else:
            raise AssertionError("oversized mask accepted")

        # view that disagrees with the mask rules
        p = payload_for(cfg)
        p["view"] = ["R...", "..K."]
        try:
            apply_grid.apply(p, sprites_dir=tmp)
        except DecompileError:
            pass
        else:
            raise AssertionError("drifted view accepted")
        assert not list(tmp.glob("*.py"))
    finally:
        shutil.rmtree(tmp)


def save_writes_and_skips():
    cfgs = load_configs()
    cfg = next(c for c in cfgs if c["name"] == "rathalos")
    tmp = Path(tempfile.mkdtemp())
    try:
        r1 = apply_grid.apply(payload_for(cfg), sprites_dir=tmp)
        assert r1["changed"] and (tmp / "rathalos.py").exists()
        r2 = apply_grid.apply(payload_for(cfg), sprites_dir=tmp)
        assert not r2["changed"], "identical view rewrote the file"

        # hand-authored file with comments/run splits: same view, different
        # text; saving must not normalize it away
        src = (HERE / "sprites" / "rathalos.py").read_text()
        (tmp / "rathalos.py").write_text(src)
        r3 = apply_grid.apply(payload_for(cfg), sprites_dir=tmp)
        assert not r3["changed"], "unchanged view rewrote hand-authored file"
        assert (tmp / "rathalos.py").read_text() == src

        new = dict(cfg)
        new["name"] = "purple-gypceros"  # any real slug without a config
        p = payload_for(new)
        r4 = apply_grid.apply(p, sprites_dir=tmp)
        assert (tmp / "purple_gypceros.py").exists()
    finally:
        shutil.rmtree(tmp)


def save_rollback():
    cfg = next(c for c in load_configs() if c["name"] == "rathalos")
    tmp = Path(tempfile.mkdtemp())
    # a real config tweak so the save counts as changed: recolor one cell
    recolored = dict(cfg, fills=[("runs", [(0, 1, 1)], "K")])
    failed = subprocess.CompletedProcess([], 1, stdout="", stderr="boom")
    real_run = apply_grid.subprocess.run
    apply_grid.subprocess.run = lambda *a, **k: failed
    try:
        apply_grid.apply(payload_for(cfg), sprites_dir=tmp)
        src = (tmp / "rathalos.py").read_text()
        try:
            apply_grid.apply(payload_for(recolored), sprites_dir=tmp,
                             rebuild=True)
        except RuntimeError:
            pass
        else:
            raise AssertionError("failed rebuild did not raise")
        assert (tmp / "rathalos.py").read_text() == src, "rollback lost the old text"

        new = dict(next(c for c in load_configs() if c["name"] == "rathian"),
                   name="purple-gypceros")
        try:
            apply_grid.apply(payload_for(new), sprites_dir=tmp, rebuild=True)
        except RuntimeError:
            pass
        else:
            raise AssertionError("failed rebuild did not raise")
        assert not (tmp / "purple_gypceros.py").exists(), "new sprite not removed"
    finally:
        apply_grid.subprocess.run = real_run
        shutil.rmtree(tmp)


def main():
    n = len(load_configs())
    synth_matches_engine()
    print(f"synth_matches_engine: OK ({n} sprites)")
    round_trip_exact()
    print(f"round_trip_exact: OK ({n} sprites)")
    save_refusals()
    print("save_refusals: OK")
    save_writes_and_skips()
    print("save_writes_and_skips: OK")
    save_rollback()
    print("save_rollback: OK")
    print("editor checks passed")


if __name__ == "__main__":
    main()
