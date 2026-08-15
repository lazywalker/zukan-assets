"""Chatacabra, amphibian. The stone-fisted frog: grey-blue skin over the
sumo frame, both forelimbs swollen into huge stone-pale clubs, a wide
flat mouth, and a low crouch."""
from tetranadon import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "chatacabra"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["G"] = (118, 132, 142, 255)  # grey-blue skin
CONFIG["palette"]["D"] = (88, 100, 110, 255)   # darker shade
CONFIG["palette"]["C"] = (222, 208, 186, 255)  # pale stone fists
CONFIG["palette"]["R"] = (216, 120, 70, 255)   # orange tongue

# stone fists: forelimb clubs bulging down at the front
CONFIG["spans"] = {
    **_base["spans"],
    12: [(0, 16), (8, 26), (18, 18)],
    13: [(0, 16), (8, 26), (17, 17)],
}

CONFIG["fills"] = [
    # wide flat mouth line with a tongue tip
    ("runs", [(9, 0, 8)], "K"),
    ("runs", [(9, 3, 5)], "R"),
    # pale beak-less face
    ("runs", [(7, 1, 8), (8, 0, 8)], "C"),
    # red eye
    ("put", 6, 5, "R"),
    # huge pale stone fists
    ("runs", [(12, 0, 7), (13, 0, 7)], "C"),
    ("runs", [(12, 2, 2), (12, 5, 5), (13, 3, 3)], "D", "C"),
    # shell plate on the back
    ("runs", [(10, 20, 24), (11, 19, 25), (12, 19, 26)], "D"),
    # belly shade
    ("runs", [(14, 2, 14), (15, 2, 13), (16, 3, 12)], "D"),
    # claws
    ("put", 21, 10, "W"),
    ("put", 21, 16, "W"),
    ("put", 21, 18, "W"),
]
