"""Fish archetype: side view facing left, oval body, fan tail, dorsal and
pectoral fins, gill line, belly band, notch mouth. Species override the
palette and may patch spans for bill/crest/fang variants."""

CONFIG = {
    "name": "_fish",
    "size": (32, 24),
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (110, 140, 170, 255),  # body
        "D": (80, 106, 136, 255),   # darker fins / back
        "C": (222, 226, 224, 255),  # belly
        "W": (246, 242, 230, 255),
    },
    "base": "B",
    "spans": {
        6:  [(10, 17)],
        7:  [(7, 19)],
        8:  [(4, 20), (21, 27)],
        9:  [(3, 21), (20, 29)],
        10: [(3, 21), (20, 29)],
        11: [(3, 22), (21, 30)],
        12: [(3, 22), (21, 30)],
        13: [(4, 22), (21, 30)],
        14: [(4, 21), (22, 29)],
        15: [(5, 20), (23, 28)],
        16: [(7, 18), (25, 27)],
        17: [(10, 16)],
        18: [(10, 13)],
    },
    "fills": [
        # dorsal + tail fins darker with ray lines
        ("runs", [(6, 10, 17), (7, 7, 9)], "D"),
        ("runs", [(8, 21, 27), (9, 20, 29), (10, 20, 29), (11, 21, 30),
                  (12, 21, 30), (13, 21, 30), (14, 22, 29), (15, 23, 28),
                  (16, 25, 27)], "D"),
        ("runs", [(9, 24, 25), (11, 25, 26), (13, 25, 26), (15, 26, 27)],
         "B", "D"),
        # pectoral fin darker
        ("runs", [(17, 11, 15), (18, 10, 13)], "D"),
        # belly band
        ("runs", [(13, 6, 19), (14, 6, 18), (15, 7, 17), (16, 9, 16)], "C"),
        # gill line + mouth
        ("put", 10, 8, "K"),
        ("put", 11, 8, "K"),
        ("put", 9, 3, "K"),
        # eye
        ("put", 9, 5, "KW"),
    ],
}
