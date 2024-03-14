from abc import ABC


class BaseFish(ABC):

    def __init__(self, name: str, points: float, time_to_catch: int):
        self.name = name
        self.points = round(points, 1)
        self.time_to_catch = time_to_catch

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value or value.isspace():
            raise ValueError("Fish name should be determined!")

        self.__name = value

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, value):
        if not 1 <= value <= 10:
            raise ValueError("Points should be a value ranging from 1 to 10!")

        self.__points = round(value, 1)

    def fish_details(self):
        return (f"{self.__class__.__name__}: {self.name} [Points: {self.points}, "
                f"Time to Catch: {self.time_to_catch} seconds]")
