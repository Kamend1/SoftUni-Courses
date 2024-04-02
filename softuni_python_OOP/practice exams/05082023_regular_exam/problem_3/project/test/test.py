from project.second_hand_car import SecondHandCar
from unittest import TestCase, main

class TestSecondHandCar(TestCase):

    def setUp(self):
        self.sh = SecondHandCar("Mustang", "Sports", 100000, 15000.00)

    def test_correct_init(self):
        self.assertEqual("Mustang", self.sh.model)
        self.assertEqual("Sports", self.sh.car_type)
        self.assertEqual(100000, self.sh.mileage)
        self.assertEqual(15000.00, self.sh.price)
        self.assertEqual([], self.sh.repairs)

    def test_price_setter_raises_border(self):
        with self.assertRaises(ValueError) as ve:
            self.sh.price = 1.0

        expected = 'Price should be greater than 1.0!'

        self.assertEqual(expected, str(ve.exception))

    def test_price_setter_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.sh.price = 0.9

        expected = 'Price should be greater than 1.0!'

        self.assertEqual(expected, str(ve.exception))

    def test_price_setter_success(self):
        self.sh.price = 12000

        self.assertEqual(12000, self.sh.price)

    def test_mileage_setter_raises_border(self):
        with self.assertRaises(ValueError) as ve:
            self.sh.mileage = 100

        expected = 'Please, second-hand cars only! Mileage must be greater than 100!'
        self.assertEqual(expected, str(ve.exception))

    def test_mileage_setter_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.sh.mileage = 98

        expected = 'Please, second-hand cars only! Mileage must be greater than 100!'
        self.assertEqual(expected, str(ve.exception))

    def test_set_promotional_price_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.sh.set_promotional_price(15000)

        expected = 'You are supposed to decrease the price!'
        self.assertEqual(expected, str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.sh.set_promotional_price(25000.00)

        expected = 'You are supposed to decrease the price!'
        self.assertEqual(expected, str(ve.exception))

    def test_set_promotional_price_success(self):
        result = self.sh.set_promotional_price(10000)
        expected = 'The promotional price has been successfully set.'
        self.assertEqual(expected, result)
        self.assertEqual(10000, self.sh.price)

    def test_need_repair_impossible(self):
        result = self.sh.need_repair(7501, "New Engine")
        expected = 'Repair is impossible!'
        self.assertEqual(expected, result)

    def test_need_repair_success(self):
        result = self.sh.need_repair(7400, "New Engine")
        expected = 'Price has been increased due to repair charges.'
        self.assertEqual(expected, result)
        self.assertEqual(22400, self.sh.price)
        self.assertEqual(["New Engine"], self.sh.repairs)

    def test_greater_than_dunder_method(self):
        other = SecondHandCar("Lambo", "Sports", 25000, 25000)
        other_1 = SecondHandCar("Focus", "Sedan", 50000, 5000)
        other_2 = SecondHandCar("Nissan GTR", "Sports", 300000, 3000)

        result = self.sh > other_1
        expected = 'Cars cannot be compared. Type mismatch!'
        self.assertEqual(result, expected)

        self.assertTrue(self.sh > other_2)
        self.assertFalse(self.sh > other)

    def test_string_dunder_method(self):
        result = str(self.sh)
        expected = f"""Model Mustang | Type Sports | Milage 100000km
Current price: 15000.00 | Number of Repairs: 0"""

        self.assertEqual(result, expected)


if __name__ == '__main__':
    main()
