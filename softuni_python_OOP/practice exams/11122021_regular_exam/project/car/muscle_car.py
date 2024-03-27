from project.car.car import Car


class MuscleCar(Car):

    @property
    def min_speed_limit(self):
        return 250

    @property
    def max_speed_limit(self):
        return 450

    @property
    def car_type(self):
        return "MuscleCar"
