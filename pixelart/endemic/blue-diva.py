"""Blue diva: a vivid blue songbird with a pale crest and a long tail."""
from _songbird import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "blue-diva"
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (90, 130, 200, 255)   # blue plumage
CONFIG["palette"]["D"] = (60, 94, 152, 255)    # darker wings
CONFIG["palette"]["C"] = (200, 220, 244, 255)  # pale crest / belly

CONFIG["fills"] = list(_base["fills"]) + [
    # pale crest over the crown
    ("runs", [(5, 9, 13), (6, 8, 9), (6, 13, 14)], "C", "B"),
]
