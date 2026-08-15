"""Great Baggi, bird wyvern leader. Sleep-dog variant of the great-jaggi
pose: dark navy scales, a tall single crest fin instead of a frill, droopy
half-lidded eyes, pale spots. Sleeps its prey, so the look is sleepy."""

CONFIG = {
    "name": "great-baggi",
    "size": (34, 24),
    "compare_to": "../icons/mh3u/great-baggi.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "N": (95, 105, 145, 255),   # navy scales
        "C": (175, 185, 210, 255),  # pale blue underbelly
        "F": (60, 70, 110, 255),    # dark navy crest fin
        "S": (50, 55, 85, 255),     # spots / shade
        "W": (246, 242, 230, 255),  # half-lid eye
    },
    "base": "N",
    "spans": {
        2:  [(8, 11)],
        3:  [(7, 12)],
        4:  [(6, 12)],
        5:  [(5, 12)],
        6:  [(1, 12), (31, 32)],
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
        # tall crest fin, dark navy
        ("runs", [(2, 8, 11), (3, 7, 12), (4, 6, 12)], "F"),
        # beak
        ("runs", [(6, 1, 3), (7, 1, 3)], "C"),
        ("runs", [(8, 2, 3)], "S"),
        # droopy half-lid eye
        ("put", 7, 5, "W"),
        ("put", 7, 6, "F"),
        # pale spots
        ("runs", [(11, 17, 18), (12, 19, 20), (13, 21, 22)], "W"),
        # underbelly along the bottom edge
        ("runs", [(14, 8, 12), (15, 8, 12), (16, 9, 12)], "C"),
        # tail fin spikes
        ("runs", [(9, 24, 25), (10, 26, 27), (11, 27, 28)], "F"),
        # tail underside shade
        ("runs", [(13, 24, 29), (14, 24, 29), (15, 25, 28), (16, 24, 26)],
         "S"),
        ("put", 21, 10, "W"),
        ("put", 21, 12, "W"),
        ("put", 21, 18, "W"),
        ("put", 21, 20, "W"),
    ],
}
