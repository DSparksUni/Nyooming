"""
    Holder for the simple settings class,
that just wraps the settings detailed in the
'settings.json' file
"""

from typing import Any
from json import load

class Settings:
    """ Holds all the settings for the game """
    def __init__(self, filepath):
        with open(filepath, 'r', encoding="UTF-8") as file:
            self.settings = load(file)

        for name, value in self.settings["default"].items():
            setattr(self, name, value)

    def __getattr__(self, __name: str) -> Any:
        if __name in self.settings:
            return self.settings[__name]
        raise AttributeError("Unknown setting provided")
