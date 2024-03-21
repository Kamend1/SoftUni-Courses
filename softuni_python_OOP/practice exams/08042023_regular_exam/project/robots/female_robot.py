from project.robots.base_robot import BaseRobot


class FemaleRobot(BaseRobot):
    DEFAULT_WEIGHT = 7
    WEIGHT_INCREMENT = 1

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, weight=self.DEFAULT_WEIGHT)

    def eating(self):
        self.weight += self.WEIGHT_INCREMENT
