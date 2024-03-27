from project.car.car import Car


class SportsCar(Car):

    @property
    def min_speed_limit(self):
        return 400

    @property
    def max_speed_limit(self):
        return 600

    @property
    def car_type(self):
        return "SportsCar"
