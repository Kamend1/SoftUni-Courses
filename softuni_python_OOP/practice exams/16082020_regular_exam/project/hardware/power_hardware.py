from project.hardware.hardware import Hardware
from math import floor


class PowerHardware(Hardware):
    _TYPE = "Power"

    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, self._TYPE, floor(capacity * 0.25), floor(1.75 * memory))
