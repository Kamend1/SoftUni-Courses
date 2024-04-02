import unittest

from project.factory.factory import Factory
from project.factory.paint_factory import PaintFactory


class TestPaintFactory(unittest.TestCase):

    def setUp(self):
        self.pf = PaintFactory("Test Paint", 100)

    def test_inheritance(self):
        self.assertTrue(issubclass(PaintFactory, Factory), msg="PaintFactory does not inherit from Factory")

    def test_correct_init(self):
        self.assertEqual("Test Paint", self.pf.name)
        self.assertEqual(100, self.pf.capacity)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], self.pf.valid_ingredients)
        self.assertEqual({}, self.pf.ingredients)

    def test_can_add_return_true(self):
        self.assertTrue(self.pf.can_add(99))
        self.assertTrue(self.pf.can_add(100))

    def test_can_add_return_false(self):
        self.assertFalse(self.pf.can_add(101))

    def test_add_more_than_capacity_valueerror(self):
        with self.assertRaises(ValueError) as ve:
            self.pf.add_ingredient("white", 101)

        expected = "Not enough space in factory"
        self.assertEqual(expected, str(ve.exception))

    def test_add_not_valid_type(self):
        with self.assertRaises(TypeError) as te:
            self.pf.add_ingredient("orange", 100)

        expected = "Ingredient of type orange not allowed in PaintFactory"
        self.assertEqual(expected, str(te.exception))

    def test_add_ingredient_correctly(self):
        self.pf.add_ingredient("white", 100)
        self.assertEqual({"white": 100}, self.pf.ingredients)
        self.assertFalse(self.pf.can_add(1))

    def test_remove_ingredient_wrong_quantity(self):
        self.pf.add_ingredient("white", 100)
        with self.assertRaises(ValueError) as ve:
            self.pf.remove_ingredient("white", 200)

        expected = "Ingredients quantity cannot be less than zero"
        self.assertEqual(expected, str(ve.exception))

    def test_remove_ingredient_not_in_list(self):
        with self.assertRaises(KeyError) as ke:
            self.pf.remove_ingredient("white", 200)

        expected = "No such ingredient in the factory"
        self.assertEqual(expected, str(ke.exception))

    def test_remove_ingredient_correct(self):
        self.pf.add_ingredient("white", 100)
        self.pf.remove_ingredient("white", 50)
        self.assertEqual({"white": 50}, self.pf.ingredients)
        self.pf.remove_ingredient("white", 50)
        self.assertEqual({"white": 0}, self.pf.ingredients)

    def test_products(self):
        result = self.pf.products
        expected = {}
        self.assertEqual(expected, result)
        self.pf.add_ingredient("white", 100)
        result = self.pf.products
        expected = {"white": 100}
        self.assertEqual(expected, result)





if __name__ == '__main__':
    unittest.main()