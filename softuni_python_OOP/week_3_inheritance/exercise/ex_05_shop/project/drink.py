from project.product import Product


class Drink(Product):
    DEFAULT_QUANTITY = 10
    # def __init__(self, name:str, quantity: int=10):
    #     super().__init__(name, quantity)

    def __init__(self, name: str):
        super().__init__(name, self.DEFAULT_QUANTITY)