#!/usr/bin/env python3
"""Generate or update the i18n overlay files (source/i18n/*.json).

Three modes:
  --fetch-wilds-ja   Pull official Japanese names+descriptions from the
                     wilds.mhdb.io /ja/ API (34 Wilds monsters). Merges
                     into monsters.json with source="official".
  --ai-translate     Call an external AI API to translate remaining names
                     and descriptions. Requires an API key in the environment
                     (OPENAI_API_KEY or similar). Left as a stub; the initial
                     i18n data was generated offline and committed.
  --status           Print coverage stats (how many monsters/items have ja/zh).

The generated files are committed static data; they do NOT run in CI.
build.py reads them at build time via apply_i18n() as an overlay layer.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
I18N_DIR = ROOT / "source" / "i18n"
WILDS_API = "https://wilds.mhdb.io"

LANGS = ("ja", "zh")


def load_i18n(name: str) -> dict:
    p = I18N_DIR / f"{name}.json"
    if p.exists():
        return json.loads(p.read_text())
    return {}


def save_i18n(name: str, data: dict) -> None:
    I18N_DIR.mkdir(parents=True, exist_ok=True)
    (I18N_DIR / f"{name}.json").write_text(
        json.dumps(data, ensure_ascii=False, indent=2)
    )


def fetch_wilds_ja() -> None:
    """Pull official Japanese names+descriptions from wilds /ja/ endpoint.

    Only fills entries that are missing or marked source="ai"; entries with
    source="official" or "manual" are preserved (the latter protects hand-edited
    translations from being overwritten).
    """
    print("== fetch wilds /ja/ ==")
    en = requests.get(f"{WILDS_API}/en/monsters", timeout=30).json()
    time.sleep(1)
    ja = requests.get(f"{WILDS_API}/ja/monsters", timeout=30).json()

    en_by_id = {m["id"]: m for m in en}
    i18n = load_i18n("monsters")
    monsters = json.loads((DATA / "monsters.json").read_text())
    updated = 0
    skipped = 0
    for jm in ja:
        em = en_by_id.get(jm["id"])
        if not em or not jm.get("name"):
            continue
        # Find the slug in our monsters.json by English name
        slug = None
        for m in monsters:
            if m["name"] == em["name"]:
                slug = m["slug"]
                break
        if not slug:
            continue
        entry = i18n.setdefault(slug, {})
        existing = entry.get("ja", {})
        # Skip entries that are official or manually verified.
        if existing.get("source") in ("official", "manual"):
            skipped += 1
            continue
        entry["ja"] = {
            "name": jm["name"],
            "desc": jm.get("description", ""),
            "source": "official",
        }
        updated += 1

    save_i18n("monsters", i18n)
    print(f"  updated {updated}, skipped {skipped} (official/manual preserved)")


def ai_translate() -> None:
    """Translate remaining names+descriptions via an external AI API.

    Stub: the initial i18n data was generated offline and committed. When
    implemented, only overwrite source="ai" or missing entries (official and
    manual are preserved); see fetch_wilds_ja() for the pattern.
    """
    print("== ai-translate (stub) ==")
    print("  This mode requires an AI API key and is not implemented yet.")
    print("  The initial i18n data was generated offline.")
    print("  To regenerate, edit this function to call your preferred API.")


def status() -> None:
    """Print i18n coverage stats."""
    for name in ("monsters", "items"):
        records = json.loads((DATA / f"{name}.json").read_text())
        i18n = load_i18n(name)
        total = len(records)
        for lang in LANGS:
            have = sum(
                1 for r in records
                if i18n.get(r.get("slug", ""), {}).get(lang)
            )
            official = sum(
                1 for r in records
                if i18n.get(r.get("slug", ""), {}).get(lang, {}).get("source") == "official"
            )
            pct = 100 * have // total if total else 0
            print(f"{name} {lang}: {have}/{total} ({pct}%)  [official: {official}]")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--fetch-wilds-ja", action="store_true",
                    help="Pull official Japanese from wilds API")
    ap.add_argument("--ai-translate", action="store_true",
                    help="Translate remaining via AI API (stub)")
    ap.add_argument("--status", action="store_true",
                    help="Print coverage stats")
    args = ap.parse_args()

    if args.status:
        status()
    elif args.fetch_wilds_ja:
        fetch_wilds_ja()
    elif args.ai_translate:
        ai_translate()
    else:
        ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
