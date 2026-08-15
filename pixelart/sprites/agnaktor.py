"""Agnaktor, leviathan. The lava armor croc: lagiacrus's long serpentine
frame carrying dark red skin, but with a closed armored beak instead of
the fanged gape, a glowing yellow magma spine from neck to tail, and
cooled gray ash bands over the back."""
from lagiacrus import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "agnaktor"
CONFIG["compare_to"] = "../icons/mh3u/agnaktor.png"
CONFIG["palette"] = {
    ".": (0, 0, 0, 0),
    "K": (24, 20, 22, 255),
    "B": (140, 45, 40, 255),     # dark red body
    "D": (100, 30, 28, 255),     # darker red shade
    "C": (222, 188, 148, 255),   # pale lower jaw
    "G": (148, 138, 124, 255),   # cooled gray ash bands
    "Y": (245, 205, 80, 255),    # glowing yellow magma ridge
    "O": (100, 190, 190, 255),   # teal eye
    "W": (246, 242, 230, 255),
}

# armored head: no fanged gape, jaw fused into a blunt beak
CONFIG["spans"] = {
    **_base["spans"],
    6:  [(1, 12)],
    7:  [(0, 15)],
}

CONFIG["fills"] = [
    # angry brow over a teal eye
    ("put", 3, 4, "K"),
    ("put", 3, 5, "K"),
    ("put", 4, 4, "W"),
    ("put", 4, 5, "O"),
    ("put", 5, 4, "O"),
    # beak seam across the fused jaw
    ("runs", [(6, 2, 5)], "D"),
    # pale jaw plate under the seam
    ("runs", [(7, 0, 6)], "C"),
    # glowing magma ridge following the arched back
    ("runs", [(5, 12, 12), (6, 14, 14), (7, 17, 17), (7, 20, 20),
              (7, 24, 24), (7, 28, 28), (9, 33, 33), (10, 35, 35),
              (11, 40, 40), (12, 43, 43), (13, 46, 46), (13, 48, 48),
              (14, 50, 50)], "Y"),
    # cooled gray ash bands over the back
    ("runs", [(11, 14, 26), (12, 14, 27), (13, 28, 42), (14, 28, 43)],
     "G"),
    # dark belly shade
    ("runs", [(13, 12, 40), (14, 13, 45), (15, 14, 48)], "D"),
    # tail underside shade
    ("runs", [(14, 46, 52), (15, 49, 54), (16, 34, 55)], "D"),
    # rear leg darker
    ("runs", [(16, 27, 30), (17, 27, 30)], "D"),
    # claws
    ("put", 18, 13, "W"),
    ("put", 18, 15, "W"),
    ("put", 18, 27, "W"),
    ("put", 18, 29, "W"),
]
