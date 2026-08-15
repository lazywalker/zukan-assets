"""Lagiacrus, leviathan. The sea serpent, drawn long and low: a compact
crocodilian head with an open toothy jaw and orange eye, a thin neck
bands sweeping into a very elongated body, a continuous sawtooth ridge of
orange dorsal tips from neck to tail, cream belly, and a tail that tapers
over a third of the total length. Legs are short stubs."""

CONFIG = {
    "name": "lagiacrus",
    "size": (56, 24),
    "compare_to": "../icons/mh3u/lagiacrus.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (95, 135, 180, 255),    # blue scales
        "D": (64, 94, 136, 255),     # darker blue shade
        "C": (232, 216, 170, 255),   # cream bands and belly
        "O": (212, 105, 55, 255),    # orange dorsal ridge / eye
        "W": (246, 242, 230, 255),
    },
    "base": "B",
    "spans": {
        1:  [(3, 9)],                          # head crown
        2:  [(2, 10)],
        3:  [(1, 11)],
        4:  [(0, 11)],
        5:  [(0, 11), (12, 12)],               # upper jaw + ridge tip
        6:  [(3, 4), (6, 7), (9, 12)],         # fangs + hinge, mouth open left
        7:  [(1, 15)],                         # pale jaw + neck
        8:  [(2, 31)],                         # jaw bottom + back arch
        9:  [(11, 33)],
        10: [(10, 37)],
        11: [(10, 41)],
        12: [(11, 45)],
        13: [(12, 49)],
        14: [(13, 52)],
        15: [(14, 54)],
        16: [(14, 17), (28, 31), (33, 55)],    # legs + tail tip
        17: [(13, 16), (27, 30)],
        18: [(13, 13), (15, 15), (27, 27), (29, 29)],
    },
    "fills": [
        # angry brow over a big orange eye
        ("put", 3, 4, "K"),
        ("put", 3, 5, "K"),
        ("put", 4, 4, "W"),
        ("put", 4, 5, "O"),
        ("put", 5, 4, "O"),
        # nostril on the snout tip
        ("put", 5, 0, "K"),
        # gaping mouth: 2x2 fangs over a pale lower jaw
        ("runs", [(6, 3, 4), (6, 6, 7)], "W"),
        ("runs", [(7, 1, 12)], "C"),
        ("put", 7, 3, "W"),
        ("put", 7, 6, "W"),
        # cream band on the neck
        ("runs", [(8, 13, 15)], "C"),
        # sawtooth dorsal ridge following the arched back
        ("runs", [(5, 12, 12), (6, 14, 14), (7, 17, 17), (7, 20, 20),
                  (7, 24, 24), (7, 28, 28), (9, 33, 33), (10, 35, 35),
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
    ],
}
