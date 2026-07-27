#!/usr/bin/env python3
"""Extract monster data from the vendored MHGU SQLite database to JSON.

GatheringHallStudios' MHGenDatabase ships a compiled `mhgu.db` (SQLite) with
detailed monster stats for Monster Hunter Generations Ultimate. This reads it
with the stdlib `sqlite3` (no new dependency) and emits a normalized JSON array
at source/api_cache/mhgu_monsters.json, one record per monster keyed by `name`
so build.py's merge_numeric can join by exact name (same as mhw-db/wilds).

The MHGU db covers 129 monsters (mostly returning roster from MHFU/MH3U/MH4U),
filling the numeric-data gap for older games that no JSON API serves.

Idempotent: overwrites the output each run.
"""

from __future__ import annotations

import hashlib
import json
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB = ROOT / "source" / "MHGenDatabase" / "mhgu.db"
# Vendored at fetch time (see source/README.md). Read, not hardcoded, so a
# re-vendor is visible without editing this script.
SOURCE_COMMIT = ROOT / "source" / "MHGenDatabase" / ".source-commit"
OUT = ROOT / "source" / "api_cache" / "mhgu_monsters.json"
# Provenance for the db this run read; parallel to the records array so
# merge_numeric's `load_json(...) or []` contract is unchanged.
META_OUT = ROOT / "source" / "api_cache" / "mhgu_monsters.meta.json"

# monster_weakness element columns → element names.
ELEMENT_COLS = ["fire", "water", "thunder", "ice", "dragon", "poison", "paralysis", "sleep"]
# monster_damage columns (per body part).
DAMAGE_COLS = ["cut", "impact", "shot", "fire", "water", "ice", "thunder", "dragon", "ko"]
# monster_weakness trap/item columns.
TRAP_COLS = ["pitfall_trap", "shock_trap", "flash_bomb", "sonic_bomb", "dung_bomb", "meat"]


def _rows(cur, sql, params=()):
    cur.execute(sql, params)
    cols = [d[0] for d in cur.description]
    return [dict(zip(cols, r)) for r in cur.fetchall()]


def write_meta(record_count: int) -> dict:
    """Record which db this extraction read, so a silent re-vendor is detectable.

    upstream_commit comes from the .source-commit file written at vendor time;
    db_sha256/size are computed from the actual file. sha256 is the definitive
    fingerprint: if it changes, the db content changed.
    """
    meta = {
        "source": "gatheringhallstudios/MHGenDatabase",
        "upstream_commit": SOURCE_COMMIT.read_text().strip() if SOURCE_COMMIT.exists() else None,
        "db_path": str(DB.relative_to(ROOT)),
        "db_sha256": hashlib.sha256(DB.read_bytes()).hexdigest(),
        "db_size": DB.stat().st_size,
        "monster_count": record_count,
    }
    META_OUT.parent.mkdir(parents=True, exist_ok=True)
    META_OUT.write_text(json.dumps(meta, ensure_ascii=False, indent=2))
    return meta


def extract() -> list[dict]:
    if not DB.exists():
        print(f"mhgu.db not found at {DB}")
        return []
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    monsters = _rows(cur, "SELECT _id, class, name, base_hp FROM monsters ORDER BY name")
    out = []
    for m in monsters:
        mid = m["_id"]
        record = {
            "name": m["name"],
            # db class (text): '0'=Large (huntable), '1'/'2'=Small.
            "class": "Large" if str(m["class"]) == "0" else "Small",
            "base_hp": m["base_hp"],
        }

        # Weaknesses (1-5 ratings), Normal state.
        wk = _rows(cur, "SELECT * FROM monster_weakness WHERE monster_id=? AND state='Normal'", (mid,))
        if wk:
            w = wk[0]
            record["weakness"] = [
                {"element": e, "rating": w[e]} for e in ELEMENT_COLS if w.get(e)
            ]
            record["traps"] = {t.replace("_bomb", "").replace("_trap", ""): bool(w[t]) for t in TRAP_COLS}

        # Hitzones (per body part).
        dmg = _rows(cur, "SELECT * FROM monster_damage WHERE monster_id=?", (mid,))
        if dmg:
            record["hitzones"] = [
                {"part": d["body_part"], **{c: d[c] for c in DAMAGE_COLS}} for d in dmg
            ]

        # Ailments (roar, wind, and the like).
        ail = _rows(cur, "SELECT ailment FROM monster_ailment WHERE monster_id=?", (mid,))
        if ail:
            record["ailments"] = [a["ailment"] for a in ail]

        # Status thresholds (poison/sleep/paralysis buildup).
        sts = _rows(cur, "SELECT status, initial, increase, max, duration, damage FROM monster_status WHERE monster_id=?", (mid,))
        if sts:
            record["status"] = sts

        # Habitats.
        hab = _rows(cur, "SELECT * FROM monster_habitat WHERE monster_id=?", (mid,))
        if hab:
            record["habitats"] = [
                {"location_id": h["location_id"], "start": h["start_area"], "move": h["move_area"], "rest": h["rest_area"]}
                for h in hab
            ]

        out.append(record)

    conn.close()
    return out


def main() -> int:
    records = extract()
    if not records:
        return 1
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(records, ensure_ascii=False, indent=2))
    meta = write_meta(len(records))
    print(f"extracted {len(records)} monsters -> {OUT.relative_to(ROOT)}")
    print(f"  db: {meta['upstream_commit']} sha256={meta['db_sha256'][:12]}… "
          f"({meta['db_size']} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
