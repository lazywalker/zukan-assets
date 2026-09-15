"""Jade Barroth, barroth subspecies. Snow-clay crown: the hammerhead
frame in pale ice-blue clay with a white snow crown and darker icy
grooves, two snow spikes breaking off the crown top."""
from barroth import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "jade-barroth"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["Y"] = (128, 148, 152, 255)  # ice-blue clay body
CONFIG["palette"]["B"] = (210, 220, 224, 255)  # white snow crown
CONFIG["palette"]["D"] = (96, 114, 120, 255)   # darker icy shade

# snow spikes breaking off the crown top
CONFIG["spans"] = {
    **_base["spans"],
    1:  [(13, 14), (21, 22)],
}
CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(1, 13, 14), (1, 21, 22)], "D", "Y"),
]
