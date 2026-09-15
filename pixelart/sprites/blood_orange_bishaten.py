"""Blood Orange Bishaten, bishaten subspecies. Ember-orange fur over the
fruit monkey frame with a red crest."""
from bishaten import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "blood-orange-bishaten"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["O"] = (198, 100, 58, 255)   # ember-orange fur
CONFIG["palette"]["D"] = (152, 72, 44, 255)    # darker ember
CONFIG["palette"]["P"] = (138, 52, 46, 255)    # red crest
CONFIG["palette"]["E"] = (240, 190, 92, 255)   # yellow face rings
