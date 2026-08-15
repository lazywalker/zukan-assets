"""Ivory Lagiacrus, lagiacrus subspecies. The rearing variant: pale
blue-white scales, and the whole head and neck lifted one row above the
lagiacrus frame for a taller, alert posture. Cream bands and orange
spikes unchanged."""
from lagiacrus import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "ivory-lagiacrus"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (196, 204, 220, 255)  # pale blue-white scales
CONFIG["palette"]["D"] = (152, 160, 178, 255)  # pale shade

# rearing posture: head and neck lifted one row
CONFIG["spans"] = {
    **_base["spans"],
    0: [(3, 9)],
    1: [(2, 10)],
    2: [(1, 11)],
    3: [(0, 11)],
    4: [(0, 11), (12, 12)],
    5: [(3, 4), (6, 7), (9, 12), (13, 13)],
    6: [(1, 15)],
    7: [(2, 31)],
}

CONFIG["fills"] = [
    # angry brow over a big orange eye, one row up
    ("put", 2, 4, "K"),
    ("put", 2, 5, "K"),
    ("put", 3, 4, "W"),
    ("put", 3, 5, "O"),
    ("put", 4, 4, "O"),
    # nostril on the snout tip
    ("put", 4, 0, "K"),
    # gaping mouth: 2x2 fangs over a pale lower jaw
    ("runs", [(5, 3, 4), (5, 6, 7)], "W"),
    ("runs", [(6, 1, 12)], "C"),
    ("put", 6, 3, "W"),
    ("put", 6, 6, "W"),
    # cream band on the neck
    ("runs", [(7, 13, 15)], "C"),
    # sawtooth dorsal ridge following the arched back
    ("runs", [(4, 12, 12), (5, 14, 14), (6, 17, 17), (6, 20, 20),
              (6, 24, 24), (6, 28, 28), (9, 33, 33), (10, 35, 35),
              (11, 40, 40), (12, 43, 43), (13, 46, 46), (13, 48, 48),
              (14, 50, 50)], "O"),
    # cream belly along the bottom edge
    ("runs", [(13, 12, 40), (14, 13, 45), (15, 14, 48)], "C"),
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
