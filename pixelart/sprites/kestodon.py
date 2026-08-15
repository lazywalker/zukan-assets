"""Kestodon, herbivore. The crested puncher: ceratonoth's frame in a hot
orange coat with a blue belly, and the three horns fused into one big
broad fan crest sweeping back over the body."""
from ceratonoth import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "kestodon"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["T"] = (222, 122, 60, 255)   # hot orange hide
CONFIG["palette"]["D"] = (176, 92, 44, 255)    # darker orange
CONFIG["palette"]["S"] = (140, 96, 60, 255)    # brown crest fan
CONFIG["palette"]["C"] = (140, 180, 212, 255)  # blue belly

# one broad fan crest instead of three horns
CONFIG["spans"] = {
    **_base["spans"],
    1:  [(9, 16)],
    2:  [(7, 18)],
    3:  [(6, 18)],
}

CONFIG["fills"] = [
    # brown fan crest with pale ribs
    ("runs", [(1, 9, 16), (2, 7, 18), (3, 6, 18)], "S"),
    ("runs", [(2, 10, 10), (2, 14, 14), (3, 12, 12)], "C", "S"),
    # eye
    ("put", 5, 5, "K"),
    # spiked ridge along the back
    ("runs", [(6, 12, 13), (7, 11, 12), (8, 12, 13), (9, 11, 12),
              (10, 13, 14), (11, 12, 13)], "D"),
    # blue belly
    ("runs", [(12, 4, 16), (13, 4, 16), (14, 5, 15), (15, 6, 14),
              (16, 7, 13)], "C"),
    # back shade
    ("runs", [(10, 19, 26), (11, 20, 27), (12, 20, 27)], "D"),
    # hooves
    ("put", 19, 7, "D"),
    ("put", 19, 9, "D"),
    ("put", 19, 21, "D"),
    ("put", 19, 23, "D"),
]
