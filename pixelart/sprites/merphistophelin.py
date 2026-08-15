"""Merphistophelin, elder dragon. The elemental wraith: a green-black
serpentine dragon with prismatic crystal spikes rising off the spine."""
from fatalis import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "merphistophelin"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (74, 104, 82, 255)    # green-black scales
CONFIG["palette"]["D"] = (52, 76, 60, 255)     # darker green
CONFIG["palette"]["C"] = (168, 214, 152, 255)  # prismatic glow

# prismatic crystal crest: a tall spike crown on head and wing shoulder
CONFIG["spans"] = {
    **_base["spans"],
    1:  [(4, 4), (16, 16), (20, 20)],
    2:  [(3, 5), (15, 17), (19, 21)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # the crystal crown glowing
    ("runs", [(2, 3, 5), (2, 15, 17), (2, 19, 21)], "C", "B"),
    ("runs", [(1, 4, 4), (1, 16, 16), (1, 20, 20)], "C", "B"),
    ("runs", [(5, 14, 14), (5, 18, 18), (6, 14, 14), (6, 17, 17),
              (6, 20, 20), (7, 16, 16), (7, 19, 19), (7, 22, 22)], "C"),
]
