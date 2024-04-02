from project.shopping_cart import ShoppingCart
from unittest import TestCase, main

class testShoppingCart(TestCase):

    def setUp(self):
        self.cart = ShoppingCart("Ivan", 300)
        self.other = ShoppingCart("Pesho", 400)

    def test_correct_init(self):
        self.assertEqual("Ivan", self.cart.shop_name)
        self.assertEqual(300, self.cart.budget)
        self.assertEqual({}, self.cart.products)

    def test_shop_name_setter_not_with_capital_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.shop_name = "ivan"

        expected = "Shop must contain only letters and must start with capital letter!"
        self.assertEqual(expected, str(ve.exception))

    def test_shop_name_contain_other_symbols_not_letters(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.shop_name = "Ivan11"

        expected = "Shop must contain only letters and must start with capital letter!"
        self.assertEqual(expected, str(ve.exception))

    def test_shop_name_sets_correct(self):
        self.cart.shop_name = "Kamen"
        self.assertEqual("Kamen", self.cart.shop_name)

    def test_add_to_cart_equal_amount_raises_valueerror(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.add_to_cart("Scotch", 100)

        expected = "Product Scotch cost too much!"
        self.assertEqual(expected, str(ve.exception))

    def test_add_to_cart_greater_than_amount_raises_valueerror(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.add_to_cart("Scotch", 101)

        expected = "Product Scotch cost too much!"
        self.assertEqual(expected, str(ve.exception))

    def test_add_to_cart_correct(self):
        result = self.cart.add_to_cart("Scotch", 99)
        expected = "Scotch product was successfully added to the cart!"
        self.assertEqual(expected, result)
        self.assertEqual({"Scotch": 99}, self.cart.products)
        self.assertEqual(99, self.cart.products["Scotch"])

    def test_add_to_cart_second_product_same_name(self):
        self.cart.add_to_cart("Scotch", 88)
        self.assertEqual({"Scotch": 88}, self.cart.products)
        self.assertEqual(88, self.cart.products["Scotch"])

        result = self.cart.add_to_cart("Scotch", 99)
        expected = "Scotch product was successfully added to the cart!"
        self.assertEqual(expected, result)
        self.assertEqual({"Scotch": 99}, self.cart.products)
        self.assertEqual(99, self.cart.products["Scotch"])

    def test_remove_from_cart_raises_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.remove_from_cart("Scotch")
        expected = "No product with name Scotch in the cart!"
        self.assertEqual(expected, str(ve.exception))

    def test_remove_from_cart_success(self):
        self.cart.add_to_cart("Scotch", 99)
        self.cart.add_to_cart("Bread", 1.05)
        self.assertEqual({"Scotch": 99, "Bread": 1.05}, self.cart.products)
        result = self.cart.remove_from_cart("Scotch")
        expected = "Product Scotch was successfully removed from the cart!"
        self.assertEqual(expected, result)
        self.assertEqual({"Bread": 1.05}, self.cart.products)

    def test_add_two_carts_dunder_add_methods(self):
        self.cart.add_to_cart("Scotch", 99)
        self.other.add_to_cart("Salami", 20)
        result = self.cart + self.other
        self.assertIsInstance(result, ShoppingCart)
        self.assertIsNot(self.cart, result)
        self.assertIsNot(self.other, result)
        self.assertEqual("IvanPesho", result.shop_name)
        self.assertEqual(700, result.budget)
        self.assertEqual({"Scotch": 99, "Salami": 20}, result.products)

    def test_add_two_carts_dunder_add_method_empty_carts(self):
        result = self.cart + self.other
        self.assertIsInstance(result, ShoppingCart)
        self.assertIsNot(self.cart, result)
        self.assertIsNot(self.other, result)
        self.assertEqual("IvanPesho", result.shop_name)
        self.assertEqual(700, result.budget)
        self.assertEqual({}, result.products)

    def test_buy_products_budget_not_enough(self):
        self.cart.budget = 10
        self.cart.add_to_cart("Scotch", 99)
        with self.assertRaises(ValueError) as ve:
            self.cart.buy_products()
        expected = "Not enough money to buy the products! Over budget with 89.00lv!"
        self.assertEqual(expected, str(ve.exception))

    def test_buy_products_equal_budget(self):
        self.cart.budget = 99
        self.cart.add_to_cart("Scotch", 99)
        result = self.cart.buy_products()
        expected = 'Products were successfully bought! Total cost: 99.00lv.'
        self.assertEqual(expected, result)

    def test_buy_products_success(self):
        self.cart.add_to_cart("Scotch", 99)
        result = self.cart.buy_products()
        expected = 'Products were successfully bought! Total cost: 99.00lv.'
        self.assertEqual(expected, result)

    def test_buy_products_empty(self):
        result = self.cart.buy_products()
        expected = 'Products were successfully bought! Total cost: 0.00lv.'
        self.assertEqual(expected, result)

if __name__ == '__main__':
    main()