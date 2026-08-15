"""Frostfang Barioth, barioth deviant. The ice fang: colder white-blue
hide over the sabertooth frame, the saberteeth grown into ice fangs with
a frost glow."""
from barioth import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "frostfang-barioth"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["W"] = (214, 226, 240, 255)  # colder white-blue coat
CONFIG["palette"]["S"] = (132, 158, 192, 255)  # ice-blue stripes
CONFIG["palette"]["D"] = (96, 122, 156, 255)   # darker ice
CONFIG["palette"]["L"] = (198, 216, 234, 255)  # pale ice belly
CONFIG["palette"]["V"] = (170, 210, 240, 255)  # frost glow claws

# ice fangs grown longer
CONFIG["spans"] = {
    **_base["spans"],
    6:  [(1, 9), (10, 16), (16, 19)],
    7:  [(1, 10), (11, 18), (17, 20)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(6, 2, 2), (6, 5, 5), (7, 2, 2), (7, 5, 5)], "V", "W"),
]
