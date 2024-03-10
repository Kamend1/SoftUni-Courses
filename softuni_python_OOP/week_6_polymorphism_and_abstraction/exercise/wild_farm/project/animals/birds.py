from project.animals.animal import Bird


class Owl(Bird):

    @staticmethod
    def make_sound():
        return "Hoot Hoot"

    def allowed_foods(self):
        return ['Meat']

    def weight_gain_per_food(self):
        return 0.25


class Hen(Bird):

    @staticmethod
    def make_sound():
        return "Cluck"

    def allowed_foods(self):
        return ['Meat', 'Vegetable', 'Fruit', 'Seed']

    def weight_gain_per_food(self):
        return 0.35
