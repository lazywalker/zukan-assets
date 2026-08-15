"""Mernos, wingdrake. The tan glider: a long-crested pterosaur side view
with one big swept wing, a hooked head crest, dangling legs, and a short
tail. The wingdrake archetype the others derive from."""

CONFIG = {
    "name": "mernos",
    "size": (28, 24),
    "compare_to": "../icons/mhw/mernos.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "T": (198, 176, 132, 255),  # tan body
        "D": (158, 138, 98, 255),   # darker tan
        "B": (108, 132, 160, 255),  # blue wing
        "R": (216, 130, 70, 255),   # crest
        "W": (246, 242, 230, 255),
    },
    "base": "T",
    "spans": {
        2:  [(5, 6)],                         # crest hook tip
        3:  [(4, 7), (8, 9)],
        4:  [(3, 8), (8, 13)],                # head + wing top
        5:  [(2, 9), (7, 16)],
        6:  [(2, 10), (6, 18)],               # head + wing
        7:  [(1, 11), (5, 20)],
        8:  [(1, 12), (5, 21)],               # body + wing
        9:  [(1, 13), (5, 22)],
        10: [(2, 20)],
        11: [(3, 19)],                        # body + legs
        12: [(4, 18)],
        13: [(5, 12), (14, 16)],              # dangling legs
        14: [(5, 11), (15, 15)],
        15: [(5, 10), (16, 16)],
    },
    "fills": [
        # hooked crest
        ("runs", [(2, 5, 6), (3, 4, 6)], "R"),
        # big blue wing with rib lines
        ("runs", [(4, 8, 13), (5, 7, 16), (6, 6, 18), (7, 5, 20),
                  (8, 5, 21), (9, 5, 22)], "B"),
        ("runs", [(6, 10, 10), (7, 10, 11), (8, 11, 12), (9, 12, 13)],
         "D", "B"),
        # dark eye + beak tip
        ("put", 4, 3, "K"),
        ("put", 5, 2, "D"),
        # body shade
        ("runs", [(8, 5, 11), (9, 5, 12), (10, 6, 18), (11, 7, 17)], "D"),
        # legs
        ("runs", [(13, 5, 12), (13, 14, 16)], "D"),
        # claws
        ("put", 15, 5, "W"),
        ("put", 15, 10, "W"),
        ("put", 15, 16, "W"),
    ],
}
