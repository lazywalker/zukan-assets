"""White Monoblos, monoblos variant. Ivory-white hide over the single-horn
drill frame."""
from monoblos import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "white-monoblos"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["O"] = (222, 216, 204, 255)  # ivory hide
CONFIG["palette"]["o"] = (180, 174, 162, 255)  # darker ivory

# ivory sabre: horn hooks further forward than the parent drill
CONFIG["spans"] = {
    **_base["spans"],
    1:  [(1, 2), (32, 32)],
    2:  [(1, 2), (31, 33)],
    3:  [(1, 3), (31, 33)],
    4:  [(2, 4), (30, 34)],
}
