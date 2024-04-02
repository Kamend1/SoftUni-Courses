from project.truck_driver import TruckDriver
from unittest import TestCase, main

class TestTruckDriver(TestCase):

    def setUp(self):
        self.td = TruckDriver("Ivan", 0.50)

    def test_correct_init(self):
        self.assertEqual("Ivan", self.td.name)
        self.assertEqual(0.50, self.td.money_per_mile)
        self.assertEqual({}, self.td.available_cargos)
        self.assertEqual(0, self.td.earned_money)
        self.assertEqual(0, self.td.miles)

    def test_earned_money_setter_raises_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.td.earned_money = -1

        expected = "Ivan went bankrupt."
        self.assertEqual(expected, str(ve.exception))

    def test_earned_money_setter_correct(self):
        self.td.earned_money = 1
        self.assertEqual(1, self.td.earned_money)

    def test_add_cargo_offer_exception(self):
        self.td.available_cargos = {"Burgas": 350}
        with self.assertRaises(Exception) as ex:
            self.td.add_cargo_offer("Burgas", 350)

        expected = "Cargo offer is already added."
        self.assertEqual(expected, str(ex.exception))
        self.assertEqual({"Burgas": 350}, self.td.available_cargos)

    def test_add_cargo_offer_success(self):
        result = self.td.add_cargo_offer("Burgas", 350)
        expected = "Cargo for 350 to Burgas was added as an offer."
        self.assertEqual(expected, result)
        self.assertEqual({"Burgas": 350}, self.td.available_cargos)

    def test_drive_best_cargo_offer_returns_failure(self):
        result = self.td.drive_best_cargo_offer()
        expected = "There are no offers available."
        self.assertEqual(expected, result)

    def test_drive_best_cargo_offer_success(self):
        self.td.add_cargo_offer("Burgas", 350)
        self.td.add_cargo_offer("Plovdiv", 150)
        result = self.td.drive_best_cargo_offer()
        expected = "Ivan is driving 350 to Burgas."
        self.assertEqual(expected, result)
        self.assertEqual({"Burgas": 350, "Plovdiv": 150}, self.td.available_cargos)
        self.assertEqual(155, self.td.earned_money)
        self.assertEqual(350, self.td.miles)

    def test_check_for_activities(self):
        self.td.earned_money = 11750
        self.td.check_for_activities(10000)
        self.assertEqual(0, self.td.earned_money)

    def test_eat(self):
        self.td.earned_money = 20
        self.td.eat(250)
        self.assertEqual(0, self.td.earned_money)

    def test_sleep(self):
        self.td.earned_money = 45
        self.td.sleep(1000)
        self.assertEqual(0, self.td.earned_money)

    def test_pump_gas(self):
        self.td.earned_money = 500
        self.td.pump_gas(1500)
        self.assertEqual(0, self.td.earned_money)

    def test_repair_truck(self):
        self.td.earned_money = 7500
        self.td.repair_truck(10000)
        self.assertEqual(0, self.td.earned_money)

    def test_string_representation(self):
        result = str(self.td)
        expected = "Ivan has 0 miles behind his back."
        self.assertEqual(expected, result)

if __name__ == '__main__':
    main()