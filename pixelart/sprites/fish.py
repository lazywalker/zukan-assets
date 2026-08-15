"""Fish, fish. The generic catch: a simple silver-blue pond fish with a
forked tail, a round fin, and a wide eye. The endemic-catch icon."""

CONFIG = {
    "name": "fish",
    "size": (24, 24),
    "compare_to": "",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (152, 168, 190, 255),  # silver-blue scales
        "D": (116, 132, 156, 255),  # darker shade
        "C": (210, 218, 228, 255),  # pale belly
        "W": (246, 242, 230, 255),
    },
    "base": "B",
    "spans": {
        8:  [(4, 6), (18, 20)],               # head + tail tip
        9:  [(3, 8), (17, 21)],
        10: [(2, 9), (16, 22)],
        11: [(1, 10), (15, 23)],
        12: [(1, 16), (15, 23)],              # body + tail
        13: [(1, 17), (16, 22)],
        14: [(2, 16), (17, 21)],
        15: [(4, 15), (19, 20)],
    },
    "fills": [
        # wide round eye
        ("put", 10, 3, "W"),
        ("put", 10, 4, "K"),
        # small mouth
        ("put", 12, 1, "K"),
        # side fin
        ("runs", [(12, 6, 9), (13, 6, 9)], "D", "B"),
        # back shade + pale belly
        ("runs", [(9, 4, 15), (10, 5, 15)], "D"),
        ("runs", [(13, 2, 14), (14, 3, 14), (15, 5, 13)], "C"),
        # tail fin darker
        ("runs", [(11, 18, 22), (12, 18, 22), (13, 18, 21)], "D"),
    ],
}
