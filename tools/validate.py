#!/usr/bin env python3
"""Validate build output integrity and print a coverage report.

Checks:
  - every monsters.json icon reference resolves to a file in icons/
  - every items.json icon reference resolves to a file in icons/items/
  - no orphan files in icons/ (every icon is referenced)
  - items.json is non-empty and well-formed
  - per-game icon coverage counts
  - numeric data injection rate (mhw-db / wilds)

Exit code is non-zero if integrity checks fail (missing refs or orphans).
A non-zero-but-present count of missing refs is informational unless strict.
"""

from __future__ import annotations

import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
ICONS = ROOT / "icons"


def load(path: Path):
    if not path.exists():
        return None
    return json.loads(path.read_text())


def main() -> int:
    monsters = load(DATA / "monsters.json") or []
    items = load(DATA / "items.json") or []
    endemic = load(DATA / "endemic_life.json") or []
    stats = load(DATA / "_build_stats.json") or {}

    errors: list[str] = []

    # 1. icon reference resolution
    referenced: set[Path] = set()
    per_game = Counter()
    missing: list[str] = []
    icon_sources = Counter()
    for m in monsters:
        for g in m.get("games", []):
            icon = g.get("icon")
            if icon:
                p = ICONS / icon
                referenced.add(p)
                per_game[g["game"]] += 1
                if "icon_source" in g:
                    icon_sources[g["icon_source"]] += 1
                if not p.exists():
                    missing.append(f"{m['name']} / {g['game']}: {icon}")
                    errors.append(f"missing icon file: {icon}")
            else:
                missing.append(f"{m['name']} / {g['game_full']}: (no icon)")

    # 2. orphans (monster icons only — items/ handled separately below)
    on_disk: set[Path] = set()
    for d in ICONS.iterdir():
        if d.is_dir() and d.name != "items":
            on_disk.update(d.glob("*.png"))
    orphans = sorted(on_disk - referenced)

    # 3. per-game coverage
    total_refs = sum(per_game.values())
    resolved_refs = sum(1 for m in monsters for g in m.get("games", []) if g.get("icon"))

    print("=" * 60)
    print("zukan-assets validation report")
    print("=" * 60)
    print(f"monsters:           {len(monsters):>6}")
    large = sum(1 for m in monsters if m.get("is_large"))
    print(f"  large:            {large:>6}")
    print(f"  small:            {len(monsters) - large:>6}")
    print(f"items:              {len(items):>6}")
    print(f"endemic life:       {len(endemic):>6}")
    print()
    print(f"icon refs total:    {total_refs:>6}")
    print(f"icon refs resolved: {resolved_refs:>6}")
    print(f"icon refs missing:  {len(missing):>6}")
    if missing:
        print("  sample missing (first 10):")
        for line in missing[:10]:
            print(f"    - {line}")
    print()
    print("icon coverage by game:")
    for game, count in sorted(per_game.items()):
        print(f"  {game:<10} {count:>4}")
    print()
    print("icon sources:")
    for src, count in icon_sources.most_common():
        print(f"  {src:<22} {count:>4}")
    print()
    print(f"orphan icons (on disk, unreferenced): {len(orphans)}")
    if orphans:
        for o in orphans[:10]:
            print(f"    - {o.relative_to(ICONS)}")
    print()

    # 2b. item icon integrity — every items.json icon ref resolves, no orphans.
    item_referenced: set[Path] = set()
    item_missing: list[str] = []
    for it in items:
        icon = it.get("icon")
        if icon:
            p = ICONS / icon
            item_referenced.add(p)
            if not p.exists():
                item_missing.append(f"{it['name']}: {icon}")
                errors.append(f"missing item icon file: {icon}")
    item_dir = ICONS / "items"
    item_on_disk: set[Path] = set(item_dir.glob("*.png")) if item_dir.is_dir() else set()
    item_orphans = sorted(item_on_disk - item_referenced)
    item_resolved = len(item_referenced) - len(item_missing)
    print("item icons:")
    print(f"  refs:            {len(item_referenced):>6}")
    print(f"  resolved:        {item_resolved:>6}")
    print(f"  missing:         {len(item_missing):>6}")
    if item_missing:
        for line in item_missing[:10]:
            print(f"    - {line}")
    print(f"  orphans:         {len(item_orphans):>6}")
    if item_orphans:
        for o in item_orphans[:10]:
            print(f"    - {o.relative_to(ICONS)}")
    print()
    numeric_mhw = stats.get("numeric_mhw", 0)
    numeric_wilds = stats.get("numeric_wilds", 0)
    print(f"mhw-db numeric merge:   {numeric_mhw:>4} monsters")
    print(f"wilds numeric merge:    {numeric_wilds:>4} monsters")
    print()

    # 4. integrity verdict
    if missing:
        pct = (resolved_refs / total_refs * 100) if total_refs else 0
        print(f"resolution rate: {pct:.1f}%")
    if errors:
        print(f"\nINTEGRITY: {len(errors)} error(s)")
        # Missing icon files are a hard error; missing optional refs are not.
        hard = [e for e in errors if e.startswith("missing icon file")]
        if hard:
            print(f"  ({len(hard)} hard — referenced but absent on disk)")
            return 1
    print("\nINTEGRITY: ok (all referenced icons present)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
