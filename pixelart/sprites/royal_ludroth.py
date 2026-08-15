"""Royal Ludroth, leviathan. The sponge ball, drawn in the front pose of
its original icon: a gold ball speckled with brown spots and a tapered
chin, five blue crown spikes fanning above an olive shield-shaped face
with heavy-lidded eyes (cyan pupils under dark lids) and a thick walrus
mustache frown, splayed olive legs with blue claws, and a long green tail
drooping behind the right side."""

CONFIG = {
    "name": "royal-ludroth",
    "size": (39, 24),
    "compare_to": "../icons/mhst2/royal-ludroth.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "Y": (222, 168, 66, 255),    # gold sponge
        "D": (182, 124, 52, 255),    # brown spots / shade
        "B": (58, 76, 158, 255),     # blue crown / claws
        "G": (136, 146, 88, 255),    # olive face / legs / tail
        "N": (40, 45, 70, 255),      # dark navy eye lids / mustache
        "T": (150, 210, 225, 255),   # cyan eye pupils
        "W": (246, 242, 230, 255),
    },
    "base": "Y",
    "spans": {
        0:  [(11, 12), (15, 16), (19, 20)],    # crown tips
        1:  [(10, 13), (14, 17), (18, 21)],
        2:  [(9, 22)],
        3:  [(8, 22)],                         # ball top
        4:  [(6, 24)],
        5:  [(5, 25)],
        6:  [(4, 26)],
        7:  [(3, 27)],
        8:  [(3, 28)],
        9:  [(2, 28)],
        10: [(2, 29)],
        11: [(2, 29)],
        12: [(2, 32)],
        13: [(2, 34)],
        14: [(2, 36)],
        15: [(2, 37)],
        16: [(3, 38)],
        17: [(4, 38)],
        18: [(5, 27), (34, 38)],               # ball + tail tip
        19: [(5, 26)],
        20: [(7, 24)],
        21: [(6, 9), (12, 21), (23, 26)],      # legs + chin
        22: [(6, 6), (8, 8), (23, 23), (25, 25)],
    },
    "fills": [
        # blue crown spikes with olive bases, fanning above the face
        ("runs", [(0, 11, 12), (0, 15, 16), (0, 19, 20), (1, 10, 13),
                  (1, 14, 17), (1, 18, 21), (2, 9, 13), (2, 14, 17),
                  (2, 18, 22)], "B"),
        ("runs", [(2, 11, 12), (2, 15, 16), (2, 19, 20)], "G", "B"),
        # olive shield-shaped face window
        ("runs", [(8, 12, 20), (9, 11, 21), (10, 10, 22), (11, 10, 22),
                  (12, 10, 22), (13, 11, 21), (14, 12, 20)], "G"),
        # heavy-lidded eyes with cyan pupils
        ("runs", [(9, 12, 14), (9, 18, 20), (10, 12, 14),
                  (10, 18, 20)], "N"),
        ("put", 10, 13, "T"),
        ("put", 10, 19, "T"),
        # thick walrus mustache frown, dipping in the middle
        ("runs", [(12, 11, 13), (12, 19, 21), (13, 11, 21),
                  (14, 14, 19)], "N"),
        # brown spots over the sponge, around the face
        ("runs", [(5, 9, 10), (5, 19, 20), (7, 6, 7), (7, 24, 25),
                  (9, 5, 6), (10, 25, 26), (13, 4, 5), (15, 25, 26),
                  (16, 6, 7), (18, 10, 11)], "D"),
        # long green tail drooping behind the ball's right side
        ("runs", [(12, 30, 32), (13, 30, 34), (14, 30, 36),
                  (15, 30, 37), (16, 30, 38), (17, 30, 38),
                  (18, 34, 38)], "G"),
        # segment notches on the tail, like the icon
        ("runs", [(13, 32, 32), (14, 33, 33), (15, 34, 34),
                  (16, 35, 35), (17, 36, 36)], "D", "G"),
        # splayed olive legs
        ("runs", [(21, 6, 9), (21, 23, 26)], "G"),
        # blue claws
        ("put", 22, 6, "B"),
        ("put", 22, 8, "B"),
        ("put", 22, 23, "B"),
        ("put", 22, 25, "B"),
    ],
}
