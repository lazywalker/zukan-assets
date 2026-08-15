"""Nargacuga, flying wyvern. Stealth panther: near-black fur, hunched
prowling stance, folded wing-blades lying along the back with a silver
edge line, single visible red eye, open jaw with a white fang, long thick
tail tapering to an upturned spiked tip, four pawed legs.

Palette: near-black fur (42,44,52), darker shade (28,30,36) for the far
legs and underside, folded wing-blades (55,57,68) with a silver edge
(200,206,218), red eye (215,50,45), white fang. Recognition: the silver
blade line along the black back is the signature at terminal size.
"""

CONFIG = {
    "name": "nargacuga",
    "size": (36, 24),
    "compare_to": "../icons/mh3u/nargacuga.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),     # near-black outline
        "F": (42, 44, 52, 255),     # black fur
        "D": (28, 30, 36, 255),     # darker fur: far legs, underside
        "B": (55, 57, 68, 255),     # folded wing-blades
        "S": (200, 206, 218, 255),  # silver blade edge
        "R": (215, 50, 45, 255),    # red eye
        "W": (245, 242, 230, 255),  # fang
    },
    "base": "F",
    "spans": {
        4:  [(5, 6), (9, 10)],                # ears
        5:  [(3, 10), (13, 22)],
        6:  [(2, 11), (12, 24)],
        7:  [(1, 12), (11, 25)],
        8:  [(1, 9), (10, 26)],
        9:  [(2, 8), (9, 27)],
        10: [(4, 8), (9, 28), (33, 35)],
        11: [(5, 8), (9, 28), (31, 34)],
        12: [(6, 8), (10, 28), (29, 33)],
        13: [(6, 7), (10, 27), (27, 32)],
        14: [(7, 12), (15, 26), (26, 31)],
        15: [(8, 13), (17, 25), (25, 29)],
        16: [(9, 12), (19, 23), (25, 27)],
        17: [(9, 12), (20, 23)],
        18: [(9, 11), (20, 22)],
        19: [(9, 12), (20, 23)],
        20: [(8, 8), (10, 10), (20, 20), (22, 22)],
    },
    "fills": [
        # ear inner shade
        ("runs", [(4, 5, 5), (4, 9, 9)], "D"),
        # red eye
        ("put", 6, 4, "R"),
        # brow
        ("put", 5, 4, "D"),
        # fang from the open jaw
        ("put", 8, 2, "W"),
        # folded wing-blades along the back, silver edge on the bottom
        ("runs", [(5, 14, 22), (6, 13, 24), (7, 12, 25), (8, 12, 26),
                  (9, 13, 27)], "B"),
        ("runs", [(9, 15, 27), (10, 16, 28), (11, 16, 28)], "S"),
        # tail: dark shade under, spiked tip
        ("runs", [(11, 30, 33), (12, 30, 32), (13, 28, 31)], "D"),
        ("put", 10, 34, "S"),
        ("put", 11, 33, "S"),
        # far legs darker
        ("runs", [(17, 20, 23), (18, 20, 22), (19, 20, 23)], "D"),
        # claws
        ("put", 20, 8, "W"),
        ("put", 20, 10, "W"),
        ("put", 20, 20, "W"),
        ("put", 20, 22, "W"),
    ],
}
