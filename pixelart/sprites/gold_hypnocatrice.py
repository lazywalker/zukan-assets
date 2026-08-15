"""Gold Hypnocatrice, hypnocatrice variant (Frontier). Gold-yellow plumage
under a tall fanned crest, one row taller and wider than the base bird's.
No game icon exists, so compare_to is empty."""
from hypnocatrice import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "gold-hypnocatrice"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["G"] = (216, 180, 90, 255)   # gold plumage
CONFIG["palette"]["Y"] = (238, 228, 172, 255)  # pale face and belly
CONFIG["palette"]["F"] = (180, 140, 60, 255)   # crest / shade
CONFIG["palette"]["S"] = (160, 120, 50, 255)   # spots

# tall fan crest: one row higher and wider than the base
CONFIG["spans"] = {
    **_base["spans"],
    2:  [(6, 12)],
    3:  [(5, 13)],
    4:  [(4, 13)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # crest color over the enlarged fan
    ("runs", [(2, 6, 12), (3, 5, 13), (4, 4, 13)], "F"),
]
