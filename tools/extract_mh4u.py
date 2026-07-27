#!/usr/bin/env python3
"""Extract monster data from the vendored MH4U SQLite database to JSON.

kamegami13/MonsterHunter4UDatabase ships `mh4u.db` (SQLite) built from the
official MH4U bestiary. Reads it with stdlib `sqlite3` (no new dep) and emits
source/api_cache/mh4u_monsters.json, one record per monster keyed by `name`
so merge_numeric can join by exact name like the other numeric sources.

Covers 106 monsters (83 Boss + 23 Minion). The schema diverges from MHGU's
extractor in three places preserved here: weakness has per-state rows
(Normal/Enraged/Charged), habitats join to a locations table for the site
name, and monsters carry signature_move + name_jp.

Idempotent: overwrites the output each run.
"""

from __future__ import annotations

import hashlib
import json
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB = ROOT / "source" / "MH4UDatabase" / "mh4u.db"
# Vendored at fetch time (see source/README.md). Read, not hardcoded, so a
# re-vendor is visible without editing this script.
SOURCE_COMMIT = ROOT / "source" / "MH4UDatabase" / ".source-commit"
OUT = ROOT / "source" / "api_cache" / "mh4u_monsters.json"
# Provenance for the db this run read; parallel to the records array so
# merge_numeric's `load_json(...) or []` contract is unchanged.
META_OUT = ROOT / "source" / "api_cache" / "mh4u_monsters.meta.json"

# monster_weakness element + status columns → field names. MH4U rates 0-3
# (MHGU rates 0-5); the scale is source-specific and not normalized here.
WEAKNESS_ELEMENTS = ["fire", "water", "thunder", "ice", "dragon"]
WEAKNESS_STATUS = ["poison", "paralysis", "sleep"]
WEAKNESS_TRAPS = ["pitfall_trap", "shock_trap", "flash_bomb", "sonic_bomb", "dung_bomb", "meat"]
# monster_damage columns (per body part). Identical column set to MHGU.
DAMAGE_COLS = ["cut", "impact", "shot", "fire", "water", "ice", "thunder", "dragon", "ko"]

# class text → Large/Small. MHGU encodes this as '0'/'1'/'2'; MH4U spells it.
CLASS_MAP = {"Boss": "Large", "Minion": "Small"}


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
        "source": "kamegami13/MonsterHunter4UDatabase",
        "upstream_commit": SOURCE_COMMIT.read_text().strip() if SOURCE_COMMIT.exists() else None,
        "db_path": str(DB.relative_to(ROOT)),
        "db_sha256": hashlib.sha256(DB.read_bytes()).hexdigest(),
        "db_size": DB.stat().st_size,
        "monster_count": record_count,
    }
    META_OUT.parent.mkdir(parents=True, exist_ok=True)
    META_OUT.write_text(json.dumps(meta, ensure_ascii=False, indent=2))
    return meta


def _weakness_block(w: dict) -> dict:
    """Turn one monster_weakness row into a structured {elements, status, traps} block."""
    return {
        "elements": [{"element": e, "rating": w[e]} for e in WEAKNESS_ELEMENTS],
        "status": [{"element": s, "rating": w[s]} for s in WEAKNESS_STATUS],
        "traps": {t.replace("_bomb", "").replace("_trap", ""): bool(w[t]) for t in WEAKNESS_TRAPS},
    }


def extract() -> list[dict]:
    if not DB.exists():
        print(f"mh4u.db not found at {DB}")
        return []
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    # Eager-load the locations table: habitats reference it by id and we want
    # the name in each row without a join per monster.
    locations = {r["_id"]: r["name"] for r in _rows(cur, "SELECT _id, name FROM locations")}

    monsters = _rows(cur, "SELECT * FROM monsters ORDER BY name")
    out = []
    for m in monsters:
        mid = m["_id"]
        record = {
            "name": m["name"],
            "name_jp": m.get("name_jp") or None,
            "class": CLASS_MAP.get(m["class"], m["class"]),
            "signature_move": m.get("signature_move") or None,
            "trait": m.get("trait") or None,
        }

        # Weaknesses, grouped by state. MHGU exposes only Normal; MH4U also
        # carries Enraged (Deviljho line) and Charged. Keep every state present.
        wk_rows = _rows(cur, "SELECT * FROM monster_weakness WHERE monster_id=?", (mid,))
        if wk_rows:
            record["weakness"] = {w["state"].lower(): _weakness_block(w) for w in wk_rows}

        # Hitzones (per body part). MH4U lists a "(Break Part)" twin for each
        # part with post-break values; keep body_part verbatim to preserve it.
        # Two sentinel quirks normalized here:
        #  - ko = -1 means "part can't be KO'd"; MHGU stores 0 for the same
        #    meaning. Coerce to 0 so the two sub-structures stay comparable.
        #  - A few bosses ship all-(-1) rows for states the db has no data for
        #    (Crimson/White Fatalis entirely; Gogmazios's Enraged parts). Drop
        #    those rows rather than emit nonsense values; MHGU's hitzones are
        #    the real source for them. If every row would be dropped, omit the
        #    hitzones field entirely.
        dmg = _rows(cur, "SELECT * FROM monster_damage WHERE monster_id=?", (mid,))
        if dmg:
            kept = []
            for d in dmg:
                if all(d[c] == -1 for c in DAMAGE_COLS):
                    continue
                kept.append({
                    "part": d["body_part"],
                    **{c: (0 if c == "ko" and d[c] == -1 else d[c]) for c in DAMAGE_COLS},
                })
            if kept:
                record["hitzones"] = kept

        # Ailments the monster inflicts on the hunter (roar, blights, bleeding...).
        ail = _rows(cur, "SELECT ailment FROM monster_ailment WHERE monster_id=?", (mid,))
        if ail:
            record["ailments"] = [a["ailment"] for a in ail]

        # Status thresholds (poison/sleep/paralysis/KO/exhaust/blast/mount buildup).
        sts = _rows(
            cur,
            "SELECT status, initial, increase, max, duration, damage FROM monster_status WHERE monster_id=?",
            (mid,),
        )
        if sts:
            record["status"] = sts

        # Habitats. MH4U's start/move/rest areas are game-specific and only
        # meaningful alongside the site name, so join that in here.
        hab = _rows(cur, "SELECT * FROM monster_habitat WHERE monster_id=?", (mid,))
        if hab:
            record["habitats"] = [
                {
                    "location": locations.get(h["location_id"]),
                    "start": h["start_area"],
                    "move": h["move_area"],
                    "rest": h["rest_area"],
                }
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
