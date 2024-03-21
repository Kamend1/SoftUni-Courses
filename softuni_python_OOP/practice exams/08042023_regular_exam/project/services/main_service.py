from project.services.base_service import BaseService


class MainService(BaseService):
    DEFAULT_CAPACITY = 30

    def __init__(self, name: str):
        super().__init__(name, capacity=self.DEFAULT_CAPACITY)

    def details(self):
        result = [self.name + " Main Service:" + "\n" + "Robots: "]

        if self.robots:
            result.append(' '.join(robot.name for robot in self.robots))
        else:
            result.append("none")

        return ''.join(result)
