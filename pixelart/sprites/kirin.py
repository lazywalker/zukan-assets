"""Kirin, elder dragon. The white unicorn horse: slender arched neck rising
to a small head crowned by a tall GOLD lightning horn sweeping back, a
SOLID horizontal horse torso, gray-blue mane running from the crown along
the neck and back into the tail tuft, four long thin legs with dark
hooves, bright blue lightning bolts on the flank. The gold horn and the
torso block are what make it read as kirin."""

CONFIG = {
    "name": "kirin",
    "size": (30, 24),
    "compare_to": "../icons/mh4u/kirin.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "W": (228, 228, 235, 255),  # white coat
        "M": (140, 150, 175, 255),  # gray-blue mane and tail
        "Y": (226, 178, 70, 255),   # gold lightning horn
        "V": (70, 70, 85, 255),     # dark hooves
        "L": (110, 145, 230, 255),  # blue lightning bolts
    },
    "base": "W",
    "spans": {
        1:  [(6, 9)],                         # horn tip
        2:  [(5, 9)],                         # horn
        3:  [(4, 9), (9, 11)],                # horn base + mane
        4:  [(4, 8), (9, 11)],                # head + mane
        5:  [(4, 9), (9, 11)],                # head + mane
        6:  [(4, 10), (9, 12)],               # eye row
        7:  [(4, 10), (9, 12)],               # jaw + mane
        8:  [(4, 10), (9, 13)],               # jaw + neck
        9:  [(5, 11), (9, 14)],               # neck
        10: [(6, 23)],                        # torso + tail (mane edge)
        11: [(7, 22)],
        12: [(8, 21)],
        13: [(8, 20)],
        14: [(8, 20)],
        15: [(9, 20)],
        16: [(9, 19)],
        17: [(10, 11), (14, 15), (17, 18), (19, 20)],
        18: [(10, 11), (14, 15), (17, 18), (19, 20)],
        19: [(11, 12), (14, 15), (17, 18)],
        20: [(11, 12), (17, 20)],
        21: [(11, 12), (17, 20)],
        22: [(11, 12), (17, 18)],
        23: [(12, 12), (14, 14), (18, 18), (20, 20)],
    },
    "fills": [
        # tall gold lightning horn sweeping back
        ("runs", [(1, 6, 9), (2, 5, 9), (3, 4, 8)], "Y"),
        # dark eye
        ("put", 6, 5, "K"),
        # gray-blue mane from the crown along the neck
        ("runs", [(3, 9, 11), (4, 9, 11), (5, 9, 10), (6, 9, 11),
                  (7, 9, 11), (8, 9, 12), (9, 9, 12)], "M"),
        # mane continuing along the back into the tail tuft
        ("runs", [(10, 18, 22), (11, 18, 22), (12, 18, 20)], "M"),
        # chest shade
        ("runs", [(11, 8, 10), (12, 9, 11)], "L"),
        # blue lightning bolts on the flank
        ("runs", [(12, 12, 14), (13, 14, 16), (14, 12, 13), (14, 16, 17)],
         "L"),
        # dark hooves
        ("runs", [(23, 11, 12), (23, 14, 15), (23, 17, 18), (23, 19, 20)],
         "V"),
    ],
}
