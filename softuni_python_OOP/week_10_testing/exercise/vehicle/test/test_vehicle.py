from unittest import TestCase, main
from project.vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self):
        self.vehicle = Vehicle(50.0, 125.5)

    def test_correct_init(self):
        self.assertEqual(50.0, self.vehicle.fuel)
        self.assertEqual(50.0, self.vehicle.capacity)
        self.assertEqual(125.5, self.vehicle.horse_power)
        self.assertEqual(self.vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_drive_not_enough_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(1000)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_successful(self):
        kilometers = 10
        expected_result = self.vehicle.fuel - (kilometers * self.vehicle.fuel_consumption)
        self.vehicle.drive(kilometers)
        self.assertEqual(expected_result, self.vehicle.fuel)

    def test_refuel_more_than_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1000)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_success(self):
        self.vehicle.fuel -= 10
        fuel_added = 10
        expected_result = self.vehicle.fuel + fuel_added
        self.vehicle.refuel(fuel_added)
        self.assertEqual(expected_result, self.vehicle.fuel)

    def test_returns_correct_string(self):
        expected_result = "The vehicle has " + str(self.vehicle.horse_power) + " horse power with " + \
                          str(self.vehicle.fuel) + " fuel left and " + str(self.vehicle.fuel_consumption) +\
                          " fuel consumption"

        self.assertEqual(expected_result, str(self.vehicle))


if __name__ == '__main__':
    main()