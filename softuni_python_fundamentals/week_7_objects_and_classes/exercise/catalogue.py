class Catalogue:
    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        product_by_letter = []
        for product in self.products:
            if product[0] == first_letter:
                product_by_letter.append(product)
        return product_by_letter

    def __repr__(self):
        self.products = sorted(self.products)
        result = ""
        result += f"Items in the {self.name} catalogue:"
        if len(self.products) > 0:
            for product in self.products:
                result += f"\n{product}"
        return result


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
