from project.product import Product


class Drink(Product):

    def __init__(self, name:str, quantity: int=10):
        super().__init__(name, quantity)