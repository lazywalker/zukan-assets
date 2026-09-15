"""Bishaten, fanged beast. The fruit-tossing monkey: kecha-wacha's
big-eared frame in blue-grey with a pointed purple pinecone crest, an
orange-ringed pale face, and one hand holding an orange fruit."""
from kecha_wacha import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "bishaten"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["O"] = (108, 122, 148, 255)  # blue-grey fur
CONFIG["palette"]["D"] = (80, 92, 118, 255)    # darker blue
CONFIG["palette"]["C"] = (222, 206, 178, 255)  # pale face / hands
CONFIG["palette"]["P"] = (94, 68, 110, 255)    # pinecone crest purple
CONFIG["palette"]["R"] = (232, 158, 66, 255)   # orange face rings / fruit

# pointed pinecone crest over the head, fruit in the left hand
CONFIG["spans"] = {
    **_base["spans"],
    1:  [(14, 15)],
    2:  [(13, 16)],
    3:  [(1, 7), (13, 16), (22, 28)],
    4:  [(1, 8), (13, 16), (21, 28)],
    5:  [(1, 8), (13, 16), (21, 28)],
    16: [(6, 8), (21, 23), (24, 25)],
    17: [(6, 7), (22, 23), (24, 26)],
}

CONFIG["fills"] = [
    # purple pinecone crest
    ("runs", [(1, 14, 15), (2, 13, 16), (3, 13, 16), (4, 13, 16),
              (5, 13, 16)], "P"),
    ("runs", [(3, 14, 15), (5, 14, 15)], "D", "P"),
    # pink ear inner discs, darker ear rims
    ("runs", [(2, 3, 5), (3, 2, 6), (4, 2, 6), (5, 2, 6), (6, 3, 6),
              (7, 3, 6), (2, 24, 26), (3, 23, 27), (4, 23, 27),
              (5, 23, 27), (6, 23, 26), (7, 23, 26)], "D", "O"),
    # pale face mask with orange rings and dark eyes
    ("runs", [(8, 11, 18), (9, 10, 19), (10, 10, 19), (11, 11, 18)],
     "C", "O"),
    ("runs", [(8, 11, 11), (8, 18, 18), (9, 10, 10), (9, 19, 19),
              (10, 10, 10), (10, 19, 19), (11, 11, 11), (11, 18, 18)],
     "R", "C"),
    ("put", 9, 12, "K"),
    ("put", 9, 17, "K"),
    # dark trunk nose
    ("runs", [(10, 14, 15), (11, 14, 15)], "D", "C"),
    # long dark arms with pale hands
    ("runs", [(12, 5, 8), (13, 5, 8), (14, 6, 8), (15, 6, 8),
              (16, 6, 8), (12, 21, 24), (13, 21, 24), (14, 21, 23),
              (15, 21, 23), (16, 21, 23)], "D", "O"),
    ("runs", [(16, 6, 8), (16, 21, 23)], "C", "D"),
    # orange fruit in the lower hand
    ("runs", [(16, 24, 25), (17, 24, 26)], "R"),
    ("put", 17, 25, "C"),
    # pale belly with shading
    ("runs", [(14, 10, 19), (15, 10, 19), (16, 11, 18), (17, 11, 18),
              (18, 11, 18)], "C"),
    ("runs", [(16, 13, 14), (16, 16, 16), (17, 13, 14), (17, 16, 16)],
     "D", "C"),
    # dark legs with pale claws
    ("runs", [(19, 8, 12), (19, 17, 21), (20, 8, 12), (20, 17, 21),
              (19, 14, 15), (20, 14, 15)], "D", "O"),
    ("put", 20, 9, "C"),
    ("put", 20, 20, "C"),
]
