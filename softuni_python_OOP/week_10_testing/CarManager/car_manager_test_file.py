from unittest import TestCase, main
# from CarManager.car_manager import Car


class TestCarManager(TestCase):

    def setUp(self):
        self.car = Car("Mazda", "CX5", 10, 55)

    def test_correct_init(self):
        self.assertEqual("Mazda", self.car.make)
        self.assertEqual("CX5", self.car.model)
        self.assertEqual(10, self.car.fuel_consumption)
        self.assertEqual(55, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_setter_raises_exception_for_empty_string(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_setter_raises_exception_for_empty_string(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_cannot_be_zero_or_negative_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -5

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_cannot_be_negative_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -5

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_cannot_be_negative_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -5

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_with_more_fuel_than_capacity_fills_capacity(self):
        self.car.refuel(100)

        self.assertEqual(55, self.car.fuel_amount)

    def test_refuel_with_negative_amount_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-5)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_with_less_fuel_than_capacity(self):
        self.car.refuel(10)

        self.assertEqual(10, self.car.fuel_amount)

    def test_drive_distance_enough_fuel(self):
        self.car.refuel(10)
        self.car.drive(100)

        self.assertEqual(0, self.car.fuel_amount)

    def test_try_to_drive_longer_distance_than_fuel_amount(self):
        self.car.refuel(10)

        with self.assertRaises(Exception) as ex:
            self.car.drive(110)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))


if __name__ == '__main__':
    main()
