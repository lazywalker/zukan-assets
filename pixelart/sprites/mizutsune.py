"""Mizutsune, leviathan. Long low bubble-fox: fox head with a magenta fin
crest swept back at the left, slender pale-pink body with deep pink flank
streaks, big magenta fan tail rising at the right, stubby legs, cyan
bubbles drifting above the back."""

CONFIG = {
    "name": "mizutsune",
    "size": (44, 24),
    "compare_to": "../icons/mhrise/mizutsune.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "W": (238, 214, 214, 255),  # pale pink-white body
        "P": (216, 132, 150, 255),  # deep pink streaks, crest, legs
        "F": (200, 150, 190, 255),  # fin magenta fan
        "C": (150, 210, 220, 255),  # bubble cyan
    },
    "base": "W",
    "spans": {
        # big crest swept back + drifting bubbles
        2:  [(3, 6), (14, 15)],
        3:  [(2, 7), (14, 15)],
        4:  [(1, 7), (17, 18)],
        5:  [(1, 7), (10, 26)],
        6:  [(0, 7), (9, 28), (32, 33)],
        7:  [(0, 36)],
        8:  [(0, 39)],
        9:  [(0, 41)],
        10: [(0, 42)],
        11: [(1, 43)],
        12: [(2, 43)],
        13: [(3, 43)],
        14: [(4, 42)],
        15: [(5, 41)],
        16: [(6, 39)],
        17: [(8, 37)],
        # stubby legs
        18: [(9, 11), (16, 18), (23, 25), (29, 31)],
        19: [(9, 11), (16, 18), (23, 25), (29, 31)],
        20: [(9, 9), (11, 11), (16, 16), (18, 18), (23, 23), (25, 25),
             (29, 29), (31, 31)],
    },
    "fills": [
        # big magenta crest swept back over the head
        ("runs", [(2, 3, 6), (3, 2, 7), (4, 1, 7), (5, 1, 6)], "P"),
        # cyan bubbles above the back
        ("runs", [(2, 14, 15), (3, 14, 15), (4, 17, 18)], "C"),
        # dark eye
        ("put", 8, 2, "K"),
        # deep pink zigzag streaks along the flank
        ("runs", [(10, 12, 13), (11, 14, 15), (12, 16, 17), (13, 17, 18)],
         "P"),
        ("runs", [(12, 21, 22), (13, 23, 24), (14, 24, 25)], "P"),
        # magenta fan tail
        ("runs", [(6, 32, 33), (7, 30, 36), (8, 31, 39), (9, 31, 41),
                  (10, 31, 42), (11, 31, 43), (12, 31, 43), (13, 31, 43),
                  (14, 31, 42), (15, 31, 41), (16, 31, 39)], "F"),
        # rays through the fan
        ("runs", [(8, 33, 34), (9, 34, 35), (10, 35, 36)], "P", "F"),
        ("runs", [(10, 38, 39), (11, 39, 40), (12, 40, 41)], "P", "F"),
        ("runs", [(13, 37, 38), (14, 36, 37)], "P", "F"),
        # deep pink legs
        ("runs", [(18, 9, 11), (18, 16, 18), (18, 23, 25), (18, 29, 31),
                  (19, 9, 11), (19, 16, 18), (19, 23, 25), (19, 29, 31),
                  (20, 9, 9), (20, 11, 11), (20, 16, 16), (20, 18, 18),
                  (20, 23, 23), (20, 25, 25), (20, 29, 29), (20, 31, 31)],
         "P"),
    ],
}
