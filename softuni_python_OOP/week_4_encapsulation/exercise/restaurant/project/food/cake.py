from project.food.dessert import Dessert

class Cake(Dessert):
    GRAMS = 250
    CALORIES = 1000
    PRICE = 5

    def __init__(self, name: str, price: float=PRICE, grams: float=GRAMS, calories: float=CALORIES):
        super().__init__(name, price, grams, calories)
