"""Bazelgeuse, flying wyvern. Flying bomber: bulky khaki body, small crested
head, huge wings, pinecone scale clusters (dark navy lumps) studding the
back and thick tail, orange glow on some clusters. Colors: khaki
(190,168,88), scale clusters (62,64,92), glow orange (228,118,48)."""

CONFIG = {
    "name": "bazelgeuse",
    "size": (36, 24),
    "compare_to": "../icons/mhw/bazelgeuse.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (190, 168, 88, 255),   # khaki body
        "D": (145, 125, 62, 255),   # darker khaki: wings, shade
        "N": (62, 64, 92, 255),     # navy pinecone clusters
        "O": (228, 118, 48, 255),   # orange glow
        "W": (246, 242, 230, 255),  # eye
    },
    "base": "B",
    "spans": {
        4:  [(1, 5), (16, 27)],
        5:  [(1, 6), (15, 29)],
        6:  [(1, 7), (14, 30)],
        7:  [(1, 8), (13, 31)],
        8:  [(1, 31)],
        9:  [(1, 31)],
        10: [(1, 31)],
        11: [(1, 30)],
        12: [(1, 30)],
        13: [(2, 29)],
        14: [(3, 11), (15, 28)],
        15: [(4, 11), (17, 27)],
        16: [(5, 11), (19, 27)],
        17: [(6, 10), (20, 26)],
        18: [(7, 10), (21, 26)],
        19: [(7, 10), (22, 25)],
        20: [(7, 10), (22, 24)],
        21: [(7, 7), (9, 9), (22, 22), (24, 24)],
    },
    "fills": [
        # crested head: dark crest ridge
        ("runs", [(4, 1, 3), (5, 1, 2)], "D"),
        # white eye
        ("put", 6, 3, "W"),
        # huge wings: darker khaki
        ("runs", [(4, 16, 27), (5, 16, 29), (6, 15, 30), (7, 14, 31),
                  (8, 13, 31), (9, 13, 31), (10, 13, 31), (11, 13, 30),
                  (12, 14, 30), (13, 15, 29)], "D"),
        # pinecone scale clusters: big navy lumps across the folded wings,
        # back and tail (all sit on the dark wing fill, so frm=D)
        ("runs", [(4, 16, 18), (4, 21, 23), (4, 25, 26), (5, 14, 15),
                  (5, 18, 20), (5, 23, 25), (5, 27, 29), (6, 15, 17),
                  (6, 20, 21), (6, 25, 27), (7, 14, 16), (7, 19, 21),
                  (7, 24, 26), (8, 15, 16), (8, 20, 22),
                  (6, 28, 30), (7, 29, 31), (8, 28, 30), (9, 27, 29),
                  (9, 25, 28), (10, 26, 29), (11, 28, 30), (12, 29, 30)],
         "N", "D"),
        ("runs", [(5, 27, 29), (6, 26, 27), (7, 25, 26), (10, 28, 29),
                  (12, 29, 30)], "O", "D"),
        # lighter khaki belly band along the bottom edge
        ("runs", [(13, 15, 27), (14, 16, 27), (15, 18, 27), (16, 19, 27)],
         "B"),
        # claws
        ("put", 21, 7, "W"),
        ("put", 21, 9, "W"),
        ("put", 21, 22, "W"),
        ("put", 21, 24, "W"),
    ],
}
