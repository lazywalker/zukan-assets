"""Daltyhdon, herbivore. The slate grazer: ceratonoth's frame in a cool
grey coat, horns kept but shortened blunt stubs."""
from ceratonoth import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "daltyhdon"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["T"] = (150, 148, 142, 255)  # slate hide
CONFIG["palette"]["D"] = (116, 114, 108, 255)  # darker slate
CONFIG["palette"]["S"] = (196, 194, 186, 255)  # pale horn stubs

# horns shortened to blunt stubs
CONFIG["spans"] = {
    **_base["spans"],
    1:  [(8, 9), (12, 13), (16, 17)],
    2:  [(8, 9), (12, 13), (16, 17)],
    3:  [(7, 10), (11, 14), (15, 18)],
}
