from project.animals.animal import Mammal


class Mouse(Mammal):

    def make_sound(self):
        return "Squeak"

    def allowed_foods(self):
        return ['Vegetable', 'Fruit']

    def weight_gain_per_food(self):
        return 0.10


class Dog(Mammal):

    def make_sound(self):
        return "Woof!"

    def allowed_foods(self):
        return ['Meat']

    def weight_gain_per_food(self):
        return 0.40


class Cat(Mammal):

    def make_sound(self):
        return "Meow"

    def allowed_foods(self):
        return ['Vegetable', 'Meat']

    def weight_gain_per_food(self):
        return 0.30


class Tiger(Mammal):

    def make_sound(self):
        return "ROAR!!!"

    def allowed_foods(self):
        return ['Meat']

    def weight_gain_per_food(self):
        return 1.00
