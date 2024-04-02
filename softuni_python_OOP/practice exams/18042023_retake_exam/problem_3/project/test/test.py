from project.robot import Robot
from unittest import TestCase, main

class TestRobot(TestCase):

    def setUp(self):
        self.r = Robot("Robo", "Military", 10, 1000.00)

    def test_correct_init(self):
        self.assertEqual("Robo", self.r.robot_id)
        self.assertEqual("Military", self.r.category)
        self.assertEqual(10, self.r.available_capacity)
        self.assertEqual(1000, self.r.price)
        self.assertEqual([], self.r.hardware_upgrades)
        self.assertEqual([], self.r.software_updates)

    def test_category_setter_raises_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.r.category = "Police"

        expected = "Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'"

        self.assertEqual(expected, str(ve.exception))

    def test_category_setter_success(self):
        self.r.category = "Humanoids"
        self.assertEqual("Humanoids", self.r.category)

    def test_price_setter_raises_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.r.price = -1

        expected = "Price cannot be negative!"
        self.assertEqual(expected, str(ve.exception))

    def test_price_setter_success(self):
        self.r.price = 100000

        self.assertEqual(100000, self.r.price)

    def test_upgrade_not_success(self):
        self.r.hardware_upgrades = ["VGI"]
        result = self.r.upgrade("VGI", 200)
        expected = "Robot Robo was not upgraded."
        self.assertEqual(result, expected)

    def test_upgrade_success(self):
        result = self.r.upgrade("VGI", 200)
        expected = 'Robot Robo was upgraded with VGI.'
        self.assertEqual(result, expected)
        self.assertEqual(["VGI"], self.r.hardware_upgrades)
        self.assertEqual(1300.00, self.r.price)

    def test_update_version_lower_failures(self):
        self.r.software_updates = [1.0, 1.1, 1.2]
        result = self.r.update(1.2, 5)
        expected = "Robot Robo was not updated."
        self.assertEqual(result, expected)
        result = self.r.update(1.0, 5)
        expected = "Robot Robo was not updated."
        self.assertEqual(result, expected)

    def test_update_capacity_not_enough(self):
        result = self.r.update(1.4, 300)
        expected = "Robot Robo was not updated."
        self.assertEqual(result, expected)

    def test_update_successful(self):
        result = self.r.update(1.4, 5)
        expected = 'Robot Robo was updated to version 1.4.'
        self.assertEqual(expected, result)
        self.assertEqual([1.4], self.r.software_updates)
        self.assertEqual(5, self.r.available_capacity)

    def test_greater_dunder_method(self):
        other = Robot("Test Robot", "Humanoids", 30, 3000)
        result = self.r > other
        expected = 'Robot with ID Robo is cheaper than Robot with ID Test Robot.'
        self.assertEqual(expected, result)
        other.price = 1000.00
        result = self.r > other
        expected = 'Robot with ID Robo costs equal to Robot with ID Test Robot.'
        self.assertEqual(expected, result)
        other.price = 900
        result = self.r > other
        expected = 'Robot with ID Robo is more expensive than Robot with ID Test Robot.'
        self.assertEqual(expected, result)

if __name__ == '__main__':
    main()
