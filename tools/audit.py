#!/usr/bin/env python3
"""Audit monster coverage completeness against external baselines.

This answers "is the database complete?" — a different question from
validate.py's "is the build internally consistent?". It reconciles:

  1. monster-hunter-DB's per-game large-monster count vs the franchise's
     recognized totals (tools/official_counts.json). A gap means monsters the
     game shipped but monster-hunter-DB doesn't list.
  2. the MHW/Wilds rosters against the two JSON APIs (mhw-db.com,
     wilds.mhdb.io) as an independent cross-check of names.

Exit code is non-zero if any game's large-monster coverage falls below the
SHRINK_TOLERANCE threshold, so CI can flag regressions when monster-hunter-DB
is re-vendored.
"""

from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / "tools"
DATA = ROOT / "data"
SOURCE = ROOT / "source"

# A game's coverage is "ok" if its count is within this many of official.
# Tolerates small catalog drift (e.g. whether a contested variant counts).
SHRINK_TOLERANCE = 2


def load(path: Path):
    if not path.exists():
        return None
    return json.loads(path.read_text())


def reconcile_official(monsters: list[dict], official: dict) -> int:
    """Compare MHDB large-monster counts per game vs official totals."""
    print("=" * 70)
    print("1. Large-monster coverage vs official counts")
    print("=" * 70)
    mhdb = defaultdict(set)
    for mon in monsters:
        if not mon.get("is_large"):
            continue
        for g in mon.get("games", []):
            mhdb[g.get("game_full")].add(mon["name"])

    counts = official["counts"]
    regressions = 0
    print(f"{'game':<38}{'official':>9}{'mhdb':>6}{'gap':>6}")
    print("-" * 70)
    for game, official_n in counts.items():
        mhdb_n = len(mhdb.get(game, set()))
        gap = official_n - mhdb_n
        marker = ""
        if gap > SHRINK_TOLERANCE:
            marker = f"  REGRESSION (>{SHRINK_TOLERANCE} short)"
            regressions += 1
        elif gap > 0:
            marker = f"  short by {gap}"
        elif gap < 0:
            marker = f"  +{-gap} (more than official; expansions rolled in?)"
        print(f"{game:<38}{official_n:>9}{mhdb_n:>6}{gap:>6}{marker}")
    print()
    return regressions


def reconcile_api(monsters: list[dict]) -> None:
    """Cross-check MHW/Wilds rosters against the JSON API caches.

    Only large monsters are compared, to match the official-count section's
    scope (the APIs list both, but completeness claims are about large monsters;
    small/endemic rosters are noisier and not a coverage target).
    """
    print("=" * 70)
    print("2. Cross-source name check — large monsters (MHDB vs JSON APIs)")
    print("=" * 70)
    mhdb_mhw = set()
    mhdb_wilds = set()
    for mon in monsters:
        if not mon.get("is_large"):
            continue
        for g in mon.get("games", []):
            gf = g.get("game_full")
            if gf == "Monster Hunter World":
                mhdb_mhw.add(mon["name"])
            elif gf == "Monster Hunter Wilds":
                mhdb_wilds.add(mon["name"])

    mhw_api = set()
    m = load(SOURCE / "api_cache" / "mhw_monsters.json")
    if m:
        mhw_api = {x["name"] for x in m if x.get("type") == "large"}
        _diff("MHW", "MHDB", mhdb_mhw, "mhw-db.com API", mhw_api)
    else:
        print("  (mhw-db.com cache missing — run fetch_external.py --only api)")

    wilds_api = set()
    w = load(SOURCE / "api_cache" / "wilds_monsters.json")
    if w:
        wilds_api = {x["name"] for x in w if x.get("kind") == "large"}
        _diff("Wilds", "MHDB", mhdb_wilds, "wilds.mhdb.io API", wilds_api)
    else:
        print("  (wilds.mhdb.io cache missing — run fetch_external.py --only api)")
    print()


def _diff(game: str, a_label: str, a: set, b_label: str, b: set) -> None:
    print(f"\n  {game}: {a_label} ({len(a)}) vs {b_label} ({len(b)})")
    only_b = sorted(b - a)
    only_a = sorted(a - b)
    print(f"    in {b_label} but not {a_label}: {len(only_b)}")
    for n in only_b:
        print(f"      + {n}")
    print(f"    in {a_label} but not {b_label}: {len(only_a)}")
    for n in only_a:
        print(f"      - {n}")


def check_transparency_quality() -> int:
    """Detect RGB residue on fully-transparent pixels.

    A correctly transparent sprite has RGB=(0,0,0) wherever alpha=0. Any
    non-zero RGB at alpha=0 is leftover background color (e.g. an incompletely
    removed frame) that can leak as a faint halo in premultiplied compositing.

    This is the one transparency defect that is unambiguously real — unlike
    'is this dark pixel a frame or the monster', which no heuristic reliably
    separates. Residue is a strict correctness bug worth flagging per game.
    """
    from PIL import Image

    print("=" * 70)
    print("3. Transparency quality — RGB residue on alpha=0 pixels")
    print("=" * 70)
    icons = ROOT / "icons"
    defect_games = 0
    print(f"{'game':<10}{'icons':>7}{'w/ residue':>12}{'worst %':>9}")
    print("-" * 70)
    for game_dir in sorted(p for p in icons.iterdir() if p.is_dir()):
        files = sorted(game_dir.glob("*.png"))
        if not files:
            continue
        with_residue = 0
        worst = 0.0
        for f in files:
            im = Image.open(f).convert("RGBA")
            w, h = im.size
            px = im.load()
            transparent = 0
            residue = 0
            for y in range(h):
                for x in range(w):
                    r, g, b, a = px[x, y]
                    if a == 0:
                        transparent += 1
                        if r or g or b:
                            residue += 1
            if transparent and residue:
                pct = 100 * residue / transparent
                if pct > 0.1:
                    with_residue += 1
                    worst = max(worst, pct)
        flag = ""
        if with_residue:
            flag = "  RESIDUE"
            defect_games += 1
        print(f"{game_dir.name:<10}{len(files):>7}{with_residue:>12}{worst:>8.1f}%{flag}")
    print()
    return defect_games


def item_icon_coverage() -> None:
    """Report item-type icon coverage: how many items have an icon, and which
    inferred kinds are missing one (so the gap is actionable)."""
    print("=" * 70)
    print("4. Item icon coverage")
    print("=" * 70)
    items = load(DATA / "items.json") or []
    if not items:
        print("  (items.json missing)")
        return
    with_icon = sum(1 for it in items if it.get("icon"))
    total = len(items)
    pct = 100 * with_icon // total if total else 0
    print(f"  {with_icon}/{total} items have an icon ({pct}%)")

    # Break down the unmapped by inferred kind (only meaningful for MHW items
    # without a wilds_icon; Wilds items nearly all map via their kind field).
    sys.path.insert(0, str(TOOLS))
    try:
        from item_kind import infer_kind
    except ImportError:
        return
    from collections import Counter
    unmapped_kind = Counter()
    unmapped_no_kind = 0
    for it in items:
        if it.get("icon"):
            continue
        k = infer_kind(it["name"])
        if k:
            unmapped_kind[k] += 1
        else:
            unmapped_no_kind += 1
    gap = total - with_icon
    if gap:
        print(f"  {gap} unmapped:")
        if unmapped_no_kind:
            print(f"    {unmapped_no_kind} no kind inferred (unique names)")
        for k, n in unmapped_kind.most_common(10):
            print(f"    {n:>3} inferred as {k} (no icon for that kind)")
    print()


def main() -> int:
    monsters = load(DATA / "monsters.json") or []
    official = load(TOOLS / "official_counts.json")
    if not official:
        print("official_counts.json missing; cannot run coverage audit")
        return 1

    print(f"zukan-assets coverage audit — {len(monsters)} monsters in build\n")
    regressions = reconcile_official(monsters, official)
    reconcile_api(monsters)
    defects = check_transparency_quality()
    item_icon_coverage()

    print("=" * 70)
    if regressions or defects:
        parts = []
        if regressions:
            parts.append(f"{regressions} game(s) below count tolerance ({SHRINK_TOLERANCE})")
        if defects:
            parts.append(f"{defects} game(s) with RGB residue on transparent pixels")
        print("RESULT: " + "; ".join(parts))
        return 1
    print(f"RESULT: all games within tolerance (±{SHRINK_TOLERANCE}), no residue")
    return 0


if __name__ == "__main__":
    sys.exit(main())
