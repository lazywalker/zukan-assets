"""Frostfang Barioth, barioth deviant. The ice fang: colder white-blue
hide over the sabertooth frame, the saberteeth grown into long ice fangs
reaching the underjaw with a frost glow."""
from barioth import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "frostfang-barioth"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["W"] = (214, 226, 240, 255)  # colder white-blue coat
CONFIG["palette"]["C"] = (170, 195, 225, 255)  # ice fur shade
CONFIG["palette"]["O"] = (120, 160, 210, 255)  # ice-blue mane
CONFIG["palette"]["D"] = (80, 105, 150, 255)   # darker ice shade
CONFIG["palette"]["E"] = (40, 55, 80, 255)     # dark icy mouth

CONFIG["fills"] = list(_base["fills"]) + [
    # ice fangs extended down to the underjaw
    ("runs", [(13, 10, 11), (13, 24, 25), (14, 10, 11), (14, 24, 25)],
     "W", "C"),
    # frost glow on the fang tips
    ("runs", [(12, 10, 10), (12, 25, 25), (14, 10, 10), (14, 25, 25)],
     "V", "W"),
]
CONFIG["palette"]["V"] = (170, 210, 240, 255)  # frost glow
