"""Yian Garuga, bird wyvern. The black wolf-bird: kut-ku's aggressive
cousin; black-green scales, silver spikes on the back and tail, red-tinged
eye, scarred look. Same frillbird pose, meaner palette + spikes."""

CONFIG = {
    "name": "yian-garuga",
    "size": (34, 24),
    "compare_to": "../icons/mh4u/yian-garuga.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "G": (65, 75, 55, 255),     # black-green scales
        "D": (45, 52, 40, 255),     # darker shade
        "S": (205, 210, 220, 255),  # silver spikes
        "F": (65, 75, 55, 255),     # inherited frill color (matches body)
        "C": (160, 165, 150, 255),  # gray belly
        "W": (246, 242, 230, 255),
    },
    "base": "G",
    "spans": {**__import__("great_jaggi").CONFIG["spans"],
        2:  [(6, 12)],
        3:  [(4, 13)],
        4:  [(3, 13)],
    },
    "fills": list(__import__("great_jaggi").CONFIG["fills"]) + [
        # silver spikes on the back and tail
        ("runs", [(5, 10, 12), (6, 13, 15), (7, 16, 18), (8, 19, 21),
                  (9, 22, 24), (10, 25, 27), (11, 27, 29)], "S"),
        # red-tinged brow
        ("put", 6, 5, "D"),
        ("put", 7, 5, "W"),
    ],
}
