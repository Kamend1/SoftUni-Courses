from project.services.base_service import BaseService


class SecondaryService(BaseService):
    DEFAULT_CAPACITY = 15

    def __init__(self, name: str):
        super().__init__(name, capacity=self.DEFAULT_CAPACITY)

    def details(self):
        result = [self.name + " Secondary Service:" + '\n' + "Robots: "]

        if self.robots:
            result.append(' '.join(robot.name for robot in self.robots))
        else:
            result.append("none")

        return ''.join(result)
