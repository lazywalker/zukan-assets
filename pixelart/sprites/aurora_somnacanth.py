"""Aurora Somnacanth, somnacanth subspecies. Ice-white body, steel-navy
mane, and the tail fan split into two lobes by a deep notch on the right,
with pale ice ray lines. Palette-plus-structure derive."""
from somnacanth import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "aurora-somnacanth"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["L"] = (222, 226, 234, 255)  # icy white body
CONFIG["palette"]["D"] = (178, 190, 206, 255)  # colder shade
CONFIG["palette"]["C"] = (200, 218, 230, 255)  # pale ice face / belly
CONFIG["palette"]["M"] = (72, 86, 116, 255)    # steel navy mane / tail
CONFIG["palette"]["O"] = (120, 176, 214, 255)  # ice blue shells

# tail fan split into two lobes by a notch on the trailing edge
CONFIG["spans"] = {
    **_base["spans"],
    12: [(3, 32), (33, 39), (43, 48)],
    13: [(4, 33), (33, 40), (44, 49)],
    14: [(5, 34), (33, 40), (45, 49)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # pale rays on the lower lobe
    ("runs", [(13, 45, 45), (14, 46, 46), (15, 47, 47)], "L"),
]
