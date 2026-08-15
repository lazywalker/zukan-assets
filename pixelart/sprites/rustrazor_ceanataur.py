"""Rustrazor Ceanataur, ceanataur deviant. The rust saw: rust-red shell
over the shogun frame, the blade edge turned into a sawtooth with pale
teeth."""
from shogun_ceanataur import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "rustrazor-ceanataur"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (150, 84, 54, 255)    # rust-red shell
CONFIG["palette"]["D"] = (112, 60, 38, 255)    # darker rust
CONFIG["palette"]["G"] = (172, 148, 118, 255)  # tan body

# sawtooth teeth along the blade top edge
CONFIG["spans"] = {
    **_base["spans"],
    15: [(2, 2), (5, 5), (8, 8), (1, 11), (11, 31)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(15, 2, 2), (15, 5, 5), (15, 8, 8)], "W", "B"),
]
