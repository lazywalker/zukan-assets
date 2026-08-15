"""Oroshi Kirin, kirin subspecies. The frost unicorn: ice-white coat over
the kirin frame with a glacial blue horn and frost hooves."""
from kirin import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "oroshi-kirin"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["W"] = (234, 240, 248, 255)  # ice-white coat
CONFIG["palette"]["D"] = (196, 210, 228, 255)  # colder shade
CONFIG["palette"]["Y"] = (120, 168, 216, 255)  # glacial blue horn
CONFIG["palette"]["V"] = (150, 196, 232, 255)  # frost hooves

# the frost horn forks at the tip
CONFIG["spans"] = {
    **_base["spans"],
    1:  [(5, 7), (9, 10)],
}
