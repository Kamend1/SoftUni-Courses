from typing import List

from project.product import Product


class ProductRepository:

    def __init__(self):
        self.products: List = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        try:
            return next(filter(lambda x: x.name == product_name, self.products))
        except StopIteration:
            pass

    def remove(self, product_name: str):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)

    def __repr__(self):
        if self.products:
            result = f"{self.products[0].name}: {self.products[0].quantity}"
            for index in range(1, len(self.products)):
                result += f"\n{self.products[index].name}: {self.products[index].quantity}"
            return result
