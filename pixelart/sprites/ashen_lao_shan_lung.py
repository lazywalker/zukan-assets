"""Ashen Lao-Shan Lung, lao-shan-lung variant. Ash-grey carapace over the
walking mountain frame with cooled gold ridges."""
from lao_shan_lung import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "ashen-lao-shan-lung"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (128, 124, 116, 255)  # ash-grey carapace
CONFIG["palette"]["D"] = (98, 94, 88, 255)     # darker ash
CONFIG["palette"]["Y"] = (176, 170, 158, 255)  # cooled gold ridges

# the aged mountain: far horn worn down to a stump
CONFIG["spans"] = {
    **_base["spans"],
    3:  [(8, 11)],
    4:  [(6, 11), (16, 17)],
    5:  [(5, 11), (15, 18)],
}

# the base tip put would land on the now-missing horn tip; restump it
CONFIG["fills"] = [
    op for op in _base["fills"] if not (op[0] == "put" and op[1:3] == (2, 11))
] + [
    ("put", 5, 18, "C"),
]
