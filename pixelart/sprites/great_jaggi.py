"""Great Jaggi, bird wyvern leader. The archetype for the bird-wyvern
leader family: biped, beaked head with a frill flare behind the jaw, long
counterbalancing tail with frill spikes, two bird legs with clawed toes.

Great Jaggi specifics: orange scales with dark spots, rose frill, cream
underbelly. Siblings (baggi/wroggi/velocidrome/gendrome/iodrome/izuchi/
maccau/kut-ku/garuga) derive from this pose with crest and palette patches.
"""

CONFIG = {
    "name": "great-jaggi",
    "size": (34, 24),
    "compare_to": "../icons/mh4u/great-jaggi.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "O": (200, 120, 60, 255),   # orange scales
        "C": (230, 200, 160, 255),  # cream underbelly
        "F": (225, 135, 145, 255),  # rose frill
        "S": (150, 80, 55, 255),    # dark spots / shade
        "W": (246, 242, 230, 255),  # eye
    },
    "base": "O",
    "spans": {
        3:  [(8, 10)],                        # frill tip
        4:  [(7, 11)],                        # frill
        5:  [(5, 12)],                        # head top + frill base
        6:  [(1, 12), (31, 32)],              # beak + head; tail tip
        7:  [(1, 12), (30, 33)],
        8:  [(2, 11), (29, 33)],
        9:  [(3, 12), (13, 25), (29, 32)],
        10: [(5, 13), (14, 26), (28, 31)],
        11: [(6, 14), (15, 27), (30, 30)],
        12: [(6, 14), (16, 28)],
        13: [(7, 14), (17, 29)],
        14: [(7, 29)],
        15: [(8, 28)],
        16: [(9, 25)],
        17: [(10, 13), (14, 17), (18, 24)],
        18: [(10, 13), (18, 24)],
        19: [(10, 13), (18, 23)],
        20: [(10, 13), (18, 22)],
        21: [(10, 10), (12, 12), (18, 18), (20, 20)],
    },
    "fills": [
        # rose frill behind the jaw
        ("runs", [(3, 8, 10), (4, 7, 11), (5, 10, 12)], "F"),
        # beak: cream, dark mouth line
        ("runs", [(6, 1, 3), (7, 1, 3)], "C"),
        ("runs", [(8, 2, 3)], "S"),
        # eye
        ("put", 7, 5, "W"),
        # dark spots on the body
        ("runs", [(11, 17, 18), (12, 19, 20), (13, 21, 22), (14, 12, 13),
                  (14, 23, 24)], "S"),
        # cream underbelly
        ("runs", [(13, 8, 12), (14, 8, 12), (15, 9, 12), (16, 10, 12)],
         "C"),
        # frill spikes on the tail top
        ("runs", [(9, 24, 25), (10, 26, 27), (11, 27, 28)], "F"),
        # tail underside shade
        ("runs", [(13, 24, 29), (14, 24, 29), (15, 25, 28), (16, 24, 26)],
         "S"),
        # claws
        ("put", 21, 10, "W"),
        ("put", 21, 12, "W"),
        ("put", 21, 18, "W"),
        ("put", 21, 20, "W"),
    ],
}
