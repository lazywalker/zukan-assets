"""Bishaten, fanged beast. The fruit-tossing monkey: a blue-grey acrobat
with a pointed pinecone crest, an orange-ringed face, a long curling
tail, and one arm holding a fruit."""
from kecha_wacha import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "bishaten"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["O"] = (108, 122, 148, 255)  # blue-grey fur
CONFIG["palette"]["D"] = (80, 92, 118, 255)    # darker blue
CONFIG["palette"]["C"] = (222, 206, 178, 255)  # pale face / hands
CONFIG["palette"]["E"] = (232, 158, 66, 255)   # orange face rings
CONFIG["palette"]["P"] = (94, 68, 110, 255)    # pinecone crest purple

# pointed crest over the head + fruit in the lower hand
CONFIG["spans"] = {
    **_base["spans"],
    1:  [(13, 16)],
    2:  [(12, 17), (18, 19)],
}

CONFIG["fills"] = [
    # purple pinecone crest
    ("runs", [(1, 13, 16), (2, 12, 17), (3, 12, 17), (4, 12, 16)], "P"),
    # round pale face with orange rings
    ("runs", [(7, 8, 15), (8, 7, 14), (9, 6, 14), (10, 6, 14)], "C"),
    ("runs", [(8, 9, 10), (8, 12, 13), (9, 9, 13)], "E", "C"),
    ("put", 9, 10, "K"),
    ("put", 9, 12, "K"),
    # upper hand
    ("runs", [(3, 18, 19), (4, 18, 20), (5, 18, 21), (6, 18, 21),
              (7, 18, 21), (8, 18, 20)], "C"),
    # lower hand holding the fruit
    ("runs", [(15, 17, 19), (16, 17, 20), (17, 18, 21)], "C"),
    ("runs", [(17, 19, 20)], "E"),
    # tail hook dark blue
    ("runs", [(17, 19, 21), (18, 20, 21), (19, 20, 21)], "D"),
    # belly shade
    ("runs", [(13, 6, 14), (14, 6, 14), (15, 7, 14)], "D"),
    ("runs", [(20, 10, 11), (21, 10, 11)], "D"),
]
