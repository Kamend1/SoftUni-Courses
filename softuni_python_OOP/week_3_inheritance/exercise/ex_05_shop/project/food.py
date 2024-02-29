from project.product import Product


class Food(Product):
    DEFAULT_QUANTITY = 10

    def __init__(self, name: str):
        super().__init__(name, self.DEFAULT_QUANTITY)
    # def __init__(self, name:str, quantity: int=15):
    #     super().__init__(name, quantity)