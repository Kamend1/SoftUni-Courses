from project.fish.base_fish import BaseFish


class PredatoryFish(BaseFish):

    def __init__(self, name: str, points: float):
        super().__init__(name, points, 90)
