"""Lagiacrus, leviathan. The sea serpent, drawn long and low: a compact
crocodilian head with an open toothy jaw and orange eye, a thin neck
bands sweeping into a very elongated body, a continuous sawtooth ridge of
orange dorsal tips from neck to tail, cream belly, and a tail that tapers
over a third of the total length. Legs are short stubs."""

CONFIG = {
    "name": "lagiacrus",
    "size": (24, 24),
    "compare_to": "../icons/mhwilds/lagiacrus.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (126, 64, 49, 255),
        "C": (52, 169, 210, 255),
        "D": (170, 160, 137, 255),
        "E": (248, 241, 205, 255),
    },
    "base": "C",
    "spans": {
         1: [(15, 15)],
         2: [(10, 10), (13, 15)],
         3: [(6, 10), (12, 14)],
         4: [(1, 16)],
         5: [(1, 16)],
         6: [(1, 18)],
         7: [(2, 18)],
         8: [(1, 19)],
         9: [(2, 5), (8, 9), (12, 20)],
        10: [(7, 10), (13, 19)],
        11: [(7, 11), (14, 20)],
        12: [(2, 3), (7, 11), (14, 19)],
        13: [(1, 4), (6, 12), (14, 20)],
        14: [(1, 4), (6, 21)],
        15: [(1, 20)],
        16: [(1, 21)],
        17: [(2, 21)],
        18: [(1, 21)],
        19: [(2, 22)],
        20: [(2, 21)],
        21: [(3, 22)],
        22: [(5, 6), (21, 22)],
    },
    "fills": [
        ("runs", [(7, 2, 15), (8, 1, 15), (9, 2, 5), (9, 12, 15), (10, 13, 15),
                  (11, 14, 15), (12, 14, 15), (13, 14, 15), (14, 13, 15), (15, 13, 16),
                  (16, 12, 15), (17, 13, 15), (18, 12, 15), (19, 11, 15), (20, 11, 15),
                  (21, 11, 13)], "E"),
        ("runs", [(9, 8, 9), (10, 7, 10), (11, 7, 11), (12, 3, 3)], "B"),
        ("runs", [(17, 12, 12)], "D"),
    ],
}
