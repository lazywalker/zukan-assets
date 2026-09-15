"""Barioth, flying wyvern. The white sabertooth, drawn in the fanged front
of its icon: an orange mane cap over a broad white head with grey eyes,
a huge dark mouth gap crossed by two long white fangs, a pale underjaw,
and a fur body with clawed paws."""

CONFIG = {
    "name": "barioth",
    "size": (36, 24),
    "compare_to": "../icons/mh3u/barioth.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "W": (246, 242, 232, 255),   # white fur
        "C": (210, 205, 200, 255),   # fur shade
        "O": (190, 110, 50, 255),    # orange mane
        "D": (140, 75, 35, 255),     # dark mane shade
        "E": (55, 30, 30, 255),      # dark mouth
    },
    "base": "W",
    "spans": {
        1:  [(12, 13), (22, 23)],                # mane tips
        2:  [(10, 15), (20, 25)],
        3:  [(8, 17), (18, 27)],
        4:  [(7, 28)],
        5:  [(6, 29)],                           # head top
        6:  [(6, 29)],
        7:  [(5, 30)],
        8:  [(5, 30)],
        9:  [(5, 30)],                           # mouth row
        10: [(5, 30)],
        11: [(5, 30)],
        12: [(5, 30)],
        13: [(6, 29)],                           # underjaw
        14: [(7, 28)],
        15: [(8, 27)],                           # chest
        16: [(8, 27)],
        17: [(9, 26)],
        18: [(9, 12), (14, 21), (23, 26)],       # paws
        19: [(9, 12), (14, 21), (23, 26)],
    },
    "fills": [
        # orange mane cap with dark spikes
        ("runs", [(1, 12, 13), (1, 22, 23), (2, 10, 11), (2, 14, 15),
                  (2, 20, 21), (2, 24, 25), (3, 8, 9), (3, 13, 14),
                  (3, 16, 17), (3, 18, 19), (3, 21, 22), (3, 26, 27),
                  (4, 7, 9), (4, 12, 13), (4, 15, 16), (4, 19, 20),
                  (4, 22, 23), (4, 26, 28)], "O"),
        ("runs", [(2, 10, 11), (2, 24, 25), (3, 8, 9), (3, 26, 27),
                  (4, 7, 9), (4, 26, 28)], "D", "O"),
        # grey eyes with dark pupils
        ("runs", [(7, 10, 12), (7, 23, 25), (8, 10, 12), (8, 23, 25)],
         "C", "W"),
        ("put", 7, 11, "K"),
        ("put", 7, 24, "K"),
        # huge dark mouth gap
        ("runs", [(9, 9, 26), (10, 9, 26), (11, 9, 26), (12, 9, 26)],
         "E"),
        # two long white fangs crossing the gap
        ("runs", [(9, 10, 12), (10, 10, 11), (11, 10, 11), (12, 10, 10),
                  (9, 23, 25), (10, 24, 25), (11, 24, 25), (12, 25, 25)],
         "W", "E"),
        # pale underjaw with dark shade
        ("runs", [(13, 8, 27), (14, 9, 26)], "C", "W"),
        ("runs", [(13, 12, 23)], "W", "C"),
        # fur chest shading and paws
        ("runs", [(15, 8, 12), (15, 23, 27), (16, 8, 11), (16, 24, 27),
                  (17, 9, 12), (17, 23, 26)], "C", "W"),
        ("runs", [(18, 9, 12), (18, 23, 26), (19, 9, 12), (19, 23, 26),
                  (18, 14, 21), (19, 14, 21)], "C", "W"),
        ("put", 19, 10, "K"),
        ("put", 19, 25, "K"),
    ],
}
