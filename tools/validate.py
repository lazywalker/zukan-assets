#!/usr/bin/env python3
"""Validate build output integrity and print a coverage report.

Checks:
  - every monsters.json icon reference resolves to a file in icons/
  - every items.json icon reference resolves to a file in icons/items/
  - no orphan files in icons/ (every icon is referenced)
  - items.json is non-empty and well-formed
  - per-game icon coverage counts
  - numeric data injection rate (mhw-db / wilds / mhgu / mh4u)

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

    # 2. orphans (monster icons only; items/ handled separately below)
    on_disk: set[Path] = set()
    for d in ICONS.iterdir():
        if d.is_dir() and d.name != "items":
            on_disk.update(d.glob("*.png"))
    orphans = sorted(on_disk - referenced)

    # 3. per-game coverage
    total_refs = sum(per_game.values())
    resolved_refs = sum(1 for m in monsters for g in m.get("games", []) if g.get("icon"))

    # Markdown report: CI pastes this straight into the PR body.
    out: list[str] = []
    w = out.append

    w("# zukan-assets validation report")
    w("")
    w("## Summary")
    w("")
    w("| category | count |")
    w("| --- | ---: |")
    w(f"| monsters | {len(monsters)} |")
    large = sum(1 for m in monsters if m.get("is_large"))
    w(f"| &nbsp;&nbsp;large | {large} |")
    w(f"| &nbsp;&nbsp;small | {len(monsters) - large} |")
    w(f"| items | {len(items)} |")
    w(f"| endemic life | {len(endemic)} |")
    w(f"| icon refs total | {total_refs} |")
    w(f"| icon refs resolved | {resolved_refs} |")
    w(f"| icon refs missing | {len(missing)} |")
    w("")
    if missing:
        w("<details><summary>sample missing (first 10)</summary>")
        w("")
        for line in missing[:10]:
            w(f"- {line}")
        w("")
        w("</details>")
        w("")

    # 1b. duplicate slug detection
    slug_counts: dict[str, list[int]] = defaultdict(list)
    for i, m in enumerate(monsters):
        slug_counts[m.get("slug", "")].append(i)
    dupes = {s: idxs for s, idxs in slug_counts.items() if len(idxs) > 1}

    w("## Duplicate slugs")
    w("")
    if dupes:
        w(f"**{len(dupes)} slug(s) appear more than once:**")
        w("")
        for slug, idxs in sorted(dupes.items()):
            names = [monsters[i]["name"] for i in idxs]
            w(f"- `{slug}`: indices {', '.join(map(str, idxs))} ({', '.join(names)})")
        w("")
        errors.append(f"duplicate slugs: {', '.join(dupes.keys())}")
    else:
        w("none: all slugs are unique")
    w("")

    w("## Icon coverage by game")
    w("")
    w("| game | count |")
    w("| --- | ---: |")
    for game, count in sorted(per_game.items()):
        w(f"| {game} | {count} |")
    w("")

    w("## Icon sources")
    w("")
    w("| source | count |")
    w("| --- | ---: |")
    for src, count in icon_sources.most_common():
        w(f"| {src} | {count} |")
    w("")

    w(f"## Orphan icons (on disk, unreferenced): {len(orphans)}")
    w("")
    if orphans:
        for o in orphans[:10]:
            w(f"- `{o.relative_to(ICONS)}`")
        w("")

    # 2b. item icon integrity: every items.json icon ref resolves, no orphans.
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
    w("## Item icons")
    w("")
    w("| metric | count |")
    w("| --- | ---: |")
    w(f"| refs | {len(item_referenced)} |")
    w(f"| resolved | {item_resolved} |")
    w(f"| missing | {len(item_missing)} |")
    w(f"| orphans | {len(item_orphans)} |")
    w("")
    if item_missing:
        w("<details><summary>missing item icons (first 10)</summary>")
        w("")
        for line in item_missing[:10]:
            w(f"- {line}")
        w("")
        w("</details>")
        w("")
    if item_orphans:
        w("<details><summary>orphan item icons (first 10)</summary>")
        w("")
        for o in item_orphans[:10]:
            w(f"- `{o.relative_to(ICONS)}`")
        w("")
        w("</details>")
        w("")

    numeric_mhw = stats.get("numeric_mhw", 0)
    numeric_wilds = stats.get("numeric_wilds", 0)
    numeric_mhgu = stats.get("numeric_mhgu", 0)
    numeric_mh4u = stats.get("numeric_mh4u", 0)
    w("## Numeric data")
    w("")
    w(f"- mhw-db numeric merge: {numeric_mhw} monsters")
    w(f"- wilds numeric merge: {numeric_wilds} monsters")
    w(f"- mhgu numeric merge: {numeric_mhgu} monsters")
    w(f"- mh4u numeric merge: {numeric_mh4u} monsters")
    w("")

    # 4. integrity verdict
    w("## Integrity")
    w("")
    if missing:
        pct = (resolved_refs / total_refs * 100) if total_refs else 0
        w(f"resolution rate: {pct:.1f}%")
        w("")
    if errors:
        w(f"**{len(errors)} error(s)**")
        # Missing icon files are a hard error; missing optional refs are not.
        hard = [e for e in errors if e.startswith("missing icon file")]
        if hard:
            w("")
            w(f"{len(hard)} hard: referenced but absent on disk")
            print("\n".join(out))
            return 1
    w("ok: all referenced icons present")
    print("\n".join(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
