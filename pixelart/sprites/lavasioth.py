"""Lavasioth, piscine wyvern subspecies. The magma fish: dark obsidian
coat over the jyuratodus frame, fins glowing lava-orange, and the grin
lit from inside."""
from jyuratodus import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "lavasioth"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (76, 66, 72, 255)     # obsidian coat
CONFIG["palette"]["D"] = (54, 46, 52, 255)     # darker rock
CONFIG["palette"]["R"] = (238, 118, 48, 255)   # lava fins
CONFIG["palette"]["C"] = (238, 160, 70, 255)   # lava-glow belly

CONFIG["fills"] = list(_base["fills"]) + [
    # lava glow seeping over the back
    ("runs", [(10, 18, 20), (11, 23, 25), (12, 19, 21)], "R", "D"),
]
