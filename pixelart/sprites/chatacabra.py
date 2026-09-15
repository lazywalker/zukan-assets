"""Chatacabra, amphibian. The stone-fisted frog: tetranadon's sumo frame
in grey-blue skin with a wide flat mouth, red eyes, and both forelimbs
turned into huge pale stone fists planted on the ground."""
from tetranadon import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "chatacabra"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["G"] = (118, 132, 142, 255)  # grey-blue skin
CONFIG["palette"]["M"] = (88, 100, 110, 255)   # darker shade
CONFIG["palette"]["C"] = (222, 208, 186, 255)  # pale stone fists / belly
CONFIG["palette"]["R"] = (216, 120, 70, 255)   # orange eyes / tongue

# huge stone fists replacing the hind legs at the front
CONFIG["spans"] = {
    **_base["spans"],
    18: [(6, 12), (19, 25)],
    19: [(6, 12), (14, 17), (19, 25)],
    20: [(6, 12), (14, 17), (19, 25)],
    21: [(6, 11), (14, 17), (20, 25)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # wide flat mouth line with a tongue tip
    ("runs", [(11, 13, 18)], "K", "C"),
    ("runs", [(11, 15, 16)], "R", "K"),
    # red eyes over the dark pupils
    ("put", 9, 13, "R"),
    ("put", 9, 18, "R"),
    # pale stone fists with dark knuckle seams
    ("runs", [(18, 6, 12), (19, 6, 12), (20, 6, 12), (21, 6, 11),
              (18, 19, 25), (19, 19, 25), (20, 19, 25), (21, 20, 25)],
     "C", "D"),
    ("runs", [(18, 9, 9), (19, 8, 9), (18, 22, 22), (19, 22, 23),
              (21, 8, 9), (21, 22, 23)], "M", "C"),
    # pale claws on the fists
    ("put", 21, 6, "W"),
    ("put", 21, 11, "W"),
    ("put", 21, 20, "W"),
    ("put", 21, 25, "W"),
]
