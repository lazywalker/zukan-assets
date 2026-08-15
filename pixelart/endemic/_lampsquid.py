"""Lampsquid archetype: round mantle with a wavy fin ridge, a glowing lamp
patch on the forehead, one big eye, and short curled tentacles below.
The lamp color is the species identity (gold/green/red/yellow)."""

CONFIG = {
    "name": "_lampsquid",
    "size": (28, 24),
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (86, 130, 96, 255),    # mantle
        "D": (62, 98, 72, 255),     # darker underside
        "L": (240, 208, 90, 255),   # lamp glow
        "W": (246, 242, 230, 255),
    },
    "base": "B",
    "spans": {
        5:  [(9, 19)],
        6:  [(7, 21)],
        7:  [(5, 22)],
        8:  [(4, 22)],
        9:  [(4, 23)],
        10: [(4, 23)],
        11: [(4, 23)],
        12: [(5, 22)],
        13: [(6, 20)],
        14: [(7, 19)],
        15: [(8, 9), (12, 13), (16, 17)],
        16: [(8, 8), (12, 12), (16, 16)],
        17: [(12, 12)],
    },
    "fills": [
        # lamp glow patch on the forehead
        ("runs", [(7, 8, 12), (8, 7, 13), (9, 7, 13)], "L"),
        ("put", 8, 10, "W"),
        # big eye below the lamp
        ("put", 11, 7, "W"),
        ("put", 11, 8, "K"),
        # wavy fin ridge on the mantle top
        ("runs", [(5, 9, 12), (6, 7, 9), (6, 19, 21), (7, 5, 7),
                  (7, 21, 22)], "D"),
        # mantle underside shade
        ("runs", [(12, 7, 20), (13, 8, 18), (14, 9, 17)], "D"),
    ],
}
