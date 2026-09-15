"""Deadeye Yian Garuga, garuga deviant. Battle-scarred veteran: a notched
broken crest, red-tipped spikes, a screeching open beak with bared fangs,
and one clouded dead eye."""
from yian_garuga import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "deadeye-yian-garuga"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["S"] = (202, 108, 88, 255)
CONFIG["palette"]["B"] = (65, 75, 55, 255)
CONFIG["palette"]["O"] = (140, 50, 45, 255)   # red-tipped spikes

# broken crest: bite notch out of the top edge
CONFIG["spans"] = {
    **_base["spans"],
    3:  [(4, 9), (11, 13)],
}
CONFIG["fills"] = list(_base["fills"]) + [
    # screeching: mouth line stretched wide with bared fangs
    ("runs", [(8, 4, 6)], "S"),
    ("put", 8, 3, "W"),
    ("put", 8, 5, "W"),
    # clouded dead eye: pale ball, dark pupil
    ("put", 7, 4, "C"),
    ("put", 7, 5, "K"),
    # pale scar lines across the face and neck
    ("runs", [(5, 6, 6), (6, 7, 7), (7, 6, 6)], "C"),
    # second scar on the flank
    ("runs", [(12, 17, 18), (13, 19, 20)], "C"),
]
