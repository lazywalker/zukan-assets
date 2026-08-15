"""Great Girros, fanged wyvern leader. The hooded pack leader: grey-olive
body over the great-jagras frame, and a tall orange-yellow spike ridge
standing proud along the whole back."""
from great_jagras import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "great-girros"
CONFIG["compare_to"] = "../icons/mhw/great-girros.png"
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["G"] = (110, 112, 100, 255)  # grey-olive body
CONFIG["palette"]["D"] = (80, 82, 72, 255)     # darker shade
CONFIG["palette"]["O"] = (160, 158, 135, 255)  # pale belly
CONFIG["palette"]["S"] = (232, 165, 50, 255)   # orange-yellow spikes

# taller spike ridge: extra tips above the jagras spike row
CONFIG["spans"] = {
    **_base["spans"],
    3:  [(15, 15), (20, 20)],
    4:  [(1, 6), (15, 15), (20, 20), (24, 24), (27, 27)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # spike color over the new ridge tips
    ("runs", [(3, 15, 15), (3, 20, 20), (4, 15, 15), (4, 20, 20),
              (4, 24, 24), (4, 27, 27)], "S"),
]
