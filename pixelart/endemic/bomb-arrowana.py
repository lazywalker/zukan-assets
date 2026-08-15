"""Arowana archetype (bomb / burst): a long slender fish with a straight
back, a tail fin, and a rounded tail-light (the bomb)."""
def _arowana(name, body, dark, belly, tail_glow):
    return {
        "name": name,
        "size": (38, 24),
        "compare_to": "",
        "palette": {
            ".": (0, 0, 0, 0),
            "K": (24, 20, 22, 255),
            "B": body,
            "D": dark,
            "C": belly,
            "G": tail_glow,
            "W": (246, 242, 230, 255),
        },
        "base": "B",
        "spans": {
            7:  [(10, 17)],
            8:  [(7, 19)],
            9:  [(4, 21), (23, 30)],
            10: [(3, 24), (22, 33)],
            11: [(3, 27), (23, 35)],
            12: [(3, 29), (24, 36)],
            13: [(4, 30), (25, 36)],
            14: [(5, 30), (26, 35)],
            15: [(6, 29), (27, 34)],
            16: [(8, 27), (29, 33)],
            17: [(11, 25)],
            18: [(12, 21)],
        },
        "fills": [
            # straight back band darker
            ("runs", [(9, 5, 21), (10, 4, 23), (11, 4, 26)], "D"),
            # belly band
            ("runs", [(13, 6, 26), (14, 7, 27), (15, 8, 26)], "C"),
            # tail fin darker with a glowing bomb tip
            ("runs", [(10, 23, 33), (11, 24, 35), (12, 24, 36),
                      (13, 25, 36), (14, 26, 35), (15, 27, 34)], "D"),
            ("runs", [(12, 33, 36), (13, 34, 36)], "G"),
            # gill + mouth + eye
            ("put", 10, 8, "K"),
            ("put", 11, 8, "K"),
            ("put", 10, 3, "K"),
            ("put", 10, 5, "KW"),
        ],
    }


CONFIG = _arowana("bomb-arrowana", (110, 150, 100, 255), (78, 116, 70, 255),
                  (196, 216, 176, 255), (230, 130, 70, 255))
