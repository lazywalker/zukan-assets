"""Arkveld, flying wyvern. The chain wyvern: a lean pale-grey body, dark
brow horns sweeping back, a pale fanged jaw, the signature chain-blade
wing rising from the shoulder as a dark link arc that hooks down into a
blade tip, a chain tail ending in a blade, thick legs with dark claws."""

CONFIG = {
    "name": "arkveld",
    "size": (36, 24),
    "compare_to": "../icons/mhwilds/arkveld.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "G": (176, 176, 186, 255),  # pale grey hide
        "D": (134, 134, 146, 255),  # darker grey
        "N": (72, 72, 84, 255),     # dark horns / chain blades
        "C": (216, 214, 220, 255),  # pale chest
        "W": (246, 242, 230, 255),
    },
    "base": "G",
    "spans": {
        2:  [(15, 16)],                     # wing arc tip
        3:  [(14, 17)],
        4:  [(3, 4), (13, 18)],             # horn tip + wing arc
        5:  [(2, 5), (12, 20)],             # horn + wing arc
        6:  [(1, 6), (11, 22), (24, 25)],   # head top + wing + hook tip
        7:  [(0, 7), (10, 23), (24, 26)],   # head + wing + hook
        8:  [(0, 8), (10, 26)],             # neck + wing underside
        9:  [(0, 18)],                      # neck into body
        10: [(0, 20)],
        11: [(0, 22)],
        12: [(0, 23)],
        13: [(0, 24)],                      # body + tail chain
        14: [(0, 25)],
        15: [(0, 26)],                      # tail blade tip
        16: [(1, 25)],
        17: [(7, 10), (15, 18)],            # legs
        18: [(7, 10), (15, 18)],
        19: [(6, 9), (15, 18)],             # feet
        20: [(6, 6), (8, 8), (15, 15), (17, 17)],
    },
    "fills": [
        # dark horns sweeping back over the skull
        ("runs", [(4, 3, 4), (5, 2, 5), (6, 2, 3)], "N"),
        # pale jaw with fangs
        ("runs", [(7, 0, 3), (8, 0, 3)], "C"),
        ("put", 7, 1, "W"),
        ("put", 8, 1, "W"),
        # dark eye
        ("put", 6, 4, "K"),
        # chain-blade wing: dark arc with link notches
        ("runs", [(2, 15, 16), (3, 14, 17), (4, 13, 18), (5, 12, 20),
                  (6, 11, 22), (7, 10, 23), (8, 10, 20)], "N"),
        ("runs", [(4, 16, 16), (5, 17, 18), (6, 18, 19), (7, 19, 20)],
         "D", "N"),
        # the hook blade tip stays dark
        ("runs", [(6, 24, 25), (7, 24, 26), (8, 21, 26)], "N"),
        # pale chest along the front
        ("runs", [(10, 0, 5), (11, 0, 5), (12, 0, 5), (13, 0, 5)], "C"),
        # belly shade along the bottom
        ("runs", [(14, 2, 24), (15, 3, 25), (16, 4, 24)], "D"),
        # chain tail links
        ("runs", [(13, 20, 22), (14, 22, 24), (15, 24, 26)], "N"),
        # dark claws
        ("runs", [(20, 6, 6), (20, 8, 8), (20, 15, 15), (20, 17, 17)],
         "N"),
    ],
}
