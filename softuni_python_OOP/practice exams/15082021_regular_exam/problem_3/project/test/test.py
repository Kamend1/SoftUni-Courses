from project.pet_shop import PetShop
from unittest import TestCase, main


class TestPetShop(TestCase):

    def setUp(self):
        self.ps = PetShop("Kamen")

    def test_correct_init(self):
        self.assertEqual("Kamen", self.ps.name)
        self.assertEqual({}, self.ps.food)
        self.assertEqual([], self.ps.pets)

    def test_add_food_quantity_negative(self):
        with self.assertRaises(ValueError) as ve:
            self.ps.add_food("Test", -10)

        expected = 'Quantity cannot be equal to or less than 0'

        self.assertEqual(expected, str(ve.exception))

    def test_add_food_new_food(self):
        self.ps.add_food("Test", 10.3)
        expected = {"Test": 10.3}

        self.assertEqual(expected, self.ps.food)
        result = self.ps.add_food("Test2", 1000)
        expected_result = "Successfully added 1000.00 grams of Test2."

    def test_add_food_add_to_quantity(self):
        self.ps.add_food("Test", 10.3)
        result = self.ps.add_food("Test", 10.3)
        expected_result = "Successfully added 10.30 grams of Test."
        expected = {"Test": 20.6}

        self.assertEqual(expected, self.ps.food)
        self.assertEqual(expected_result, result)

    def test_add_pet_name_exists_exception(self):
        self.ps.add_pet("Test")

        with self.assertRaises(Exception) as ex:
            self.ps.add_pet("Test")

        expected = "Cannot add a pet with the same name"
        self.assertEqual(expected, str(ex.exception))

    def test_add_pet_name_success(self):
        result = self.ps.add_pet("Test")
        expected = "Successfully added Test."
        self.assertEqual(expected, result)
        self.assertEqual(["Test"], self.ps.pets)

    def test_feed_pet_invalid_name(self):
        with self.assertRaises(Exception) as ex:
            self.ps.feed_pet("TestFood", "Test")

        expected = "Please insert a valid pet name"
        self.assertEqual(expected, str(ex.exception))

    def test_feed_pet_food_not_in_dictionary(self):
        self.ps.add_pet("Test")

        expected = 'You do not have TestFood'
        result = self.ps.feed_pet("TestFood", "Test")

        self.assertEqual(expected, result)

    def test_feed_pet_not_enough_food(self):
        self.ps.add_pet("Test")
        self.ps.add_food("TestFood", 10)
        expected = "Adding food..."
        result = self.ps.feed_pet("TestFood", "Test")
        self.assertEqual(expected, result)
        self.assertEqual({"TestFood": 1010}, self.ps.food)

    def test_feed_pet_correct(self):
        self.ps.add_pet("Test")
        self.ps.add_food("TestFood", 1000)
        expected = "Test was successfully fed"
        result = self.ps.feed_pet("TestFood", "Test")
        self.assertEqual(expected, result)
        self.assertEqual({"TestFood": 900}, self.ps.food)

    def test_repr_method(self):
        self.ps.add_pet("Test")
        self.ps.add_pet("Test1")
        self.ps.add_food("TestFood", 1000)
        expected = (f'Shop {self.ps.name}:\n'
                    f'Pets: {", ".join(self.ps.pets)}')
        result = str(self.ps)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    main()
