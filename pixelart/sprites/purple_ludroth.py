"""Purple Ludroth, royal-ludroth subspecies. Pink sponge with darker pink
spots over the same ball frame, purple-gray face, and the olive tail
raised level with the ball instead of drooping behind it."""
from royal_ludroth import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "purple-ludroth"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["Y"] = (215, 120, 150, 255)  # pink sponge
CONFIG["palette"]["D"] = (168, 80, 112, 255)   # dark pink spots
CONFIG["palette"]["G"] = (145, 120, 140, 255)  # purple-gray face

# raised tail: carried level behind the ball, droop removed
CONFIG["spans"] = {
    **_base["spans"],
    10: [(2, 29), (32, 33)],
    11: [(2, 29), (32, 34)],
    12: [(2, 32), (33, 36)],
    13: [(2, 34), (34, 37)],
    14: [(2, 36), (35, 38)],
    15: [(2, 37), (36, 38)],
    16: [(3, 38)],
    17: [(4, 38)],
    18: [(5, 27)],
}

CONFIG["fills"] = [
    # blue crown spikes with olive bases, fanning above the face
    ("runs", [(0, 11, 12), (0, 15, 16), (0, 19, 20), (1, 10, 13),
              (1, 14, 17), (1, 18, 21), (2, 9, 13), (2, 14, 17),
              (2, 18, 22)], "B"),
    ("runs", [(2, 11, 12), (2, 15, 16), (2, 19, 20)], "G", "B"),
    # purple-gray shield-shaped face window
    ("runs", [(8, 12, 20), (9, 11, 21), (10, 10, 22), (11, 10, 22),
              (12, 10, 22), (13, 11, 21), (14, 12, 20)], "G"),
    # heavy-lidded eyes with pale pupils
    ("runs", [(9, 12, 14), (9, 18, 20), (10, 12, 14),
              (10, 18, 20)], "N"),
    ("put", 10, 13, "T"),
    ("put", 10, 19, "T"),
    # thick walrus mustache frown
    ("runs", [(12, 11, 13), (12, 19, 21), (13, 11, 21),
              (14, 14, 19)], "N"),
    # pink spots over the sponge
    ("runs", [(5, 9, 10), (5, 19, 20), (7, 6, 7), (7, 24, 25),
              (9, 5, 6), (10, 25, 26), (13, 4, 5), (15, 25, 26),
              (16, 6, 7), (18, 10, 11)], "D"),
    # raised olive tail, level with the ball
    ("runs", [(10, 32, 33), (11, 32, 34), (12, 33, 36), (13, 34, 37),
              (14, 35, 38), (15, 36, 38), (16, 37, 38)], "G"),
    ("runs", [(11, 33, 33), (12, 34, 34), (13, 35, 35), (14, 36, 36),
              (15, 37, 37)], "D", "G"),
    # splayed olive legs
    ("runs", [(21, 6, 9), (21, 23, 26)], "G"),
    # blue claws
    ("put", 22, 6, "B"),
    ("put", 22, 8, "B"),
    ("put", 22, 23, "B"),
    ("put", 22, 25, "B"),
]
