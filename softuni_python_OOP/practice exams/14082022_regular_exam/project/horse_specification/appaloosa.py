from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    MAX_SPEED = 120
    SPEED_INCREMENT = 2

    def train(self):
        if self.speed + self.SPEED_INCREMENT > self.MAX_SPEED:
            self.speed = self.MAX_SPEED
        else:
            self.speed += self.SPEED_INCREMENT
