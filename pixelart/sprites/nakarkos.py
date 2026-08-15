"""Nakarkos, elder dragon. The cuttlebone: a pale bone-shell dome with a
dark twin-tentacled body coiling beneath it, a single big eye between the
arms, and bone flecks stuck to the shell."""

CONFIG = {
    "name": "nakarkos",
    "size": (32, 24),
    "compare_to": "",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "C": (222, 210, 188, 255),  # bone shell
        "D": (182, 168, 144, 255),  # bone shade
        "N": (52, 48, 62, 255),     # dark tentacle body
        "d": (38, 34, 48, 255),     # darker tentacles
        "O": (226, 120, 60, 255),   # orange glow
        "W": (246, 242, 230, 255),
    },
    "base": "N",
    "spans": {
        3:  [(8, 15), (19, 20)],              # shell dome + tentacle
        4:  [(6, 17), (18, 22)],
        5:  [(5, 18), (17, 24)],
        6:  [(4, 19), (16, 26)],
        7:  [(3, 20), (15, 28)],
        8:  [(3, 20), (14, 29)],              # shell + arms
        9:  [(2, 20), (14, 30)],
        10: [(2, 20), (13, 31)],
        11: [(2, 20), (13, 31)],
        12: [(2, 20), (13, 31)],
        13: [(2, 20), (13, 31)],
        14: [(2, 20), (13, 31)],
        15: [(2, 20), (13, 31)],
        16: [(2, 20), (13, 31)],
        17: [(2, 20), (13, 31)],
        18: [(2, 20), (13, 31)],
        19: [(2, 20), (13, 31)],
        20: [(2, 20), (13, 30)],
        21: [(3, 19), (14, 29)],
    },
    "fills": [
        # pale bone-shell dome with flecks
        ("runs", [(3, 8, 20), (4, 6, 22), (5, 5, 24), (6, 4, 26),
                  (7, 3, 20)], "C"),
        ("runs", [(5, 8, 9), (5, 13, 14), (6, 11, 12), (6, 17, 17),
                  (7, 6, 6), (7, 14, 15)], "D", "C"),
        # big glowing eye between the arms
        ("runs", [(8, 21, 22), (9, 20, 23), (10, 20, 23)], "O"),
        ("put", 9, 21, "W"),
        # dark twin tentacles coiling right
        ("runs", [(4, 19, 20), (5, 18, 21), (6, 17, 22)], "D", "N"),
        ("runs", [(14, 14, 31), (15, 14, 31), (16, 14, 31)], "d", "N"),
        # shell shade along the bottom
        ("runs", [(17, 2, 20), (18, 2, 20), (19, 2, 20)], "D", "C"),
        # arm tips orange
        ("runs", [(19, 27, 31), (20, 26, 30)], "O", "N"),
    ],
}
