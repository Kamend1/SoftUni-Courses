
from softuni_python_OOP.week_10_testing.test_worker.test_worker import Worker

from unittest import TestCase, main




class TestWorker(TestCase):
    def setUp(self):
        self.worker = Worker("TestGuy", 25000, 100)


    def test_if_init_is_correct(self):
        self.assertEqual("TestGuy", self.worker.name)
        self.assertEqual(25000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_if_worker_works_twice_when_energy_and_money_increases_and_energy_decreases(self):
        expected_money = self.worker.money + self.worker.salary * 2
        expected_energy = self.worker.energy - 2

        self.worker.work()
        self.worker.work()

        self.assertEqual(expected_money, self.worker.money)
        self.assertEqual(expected_energy, self.worker.energy)

    def test_if_worker_works_when_no_energy_expect_raise_exception(self):
        self.worker.energy = 0 #arrange

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_check_if_rest_increases_energy_as_expected(self):
        expected_energy = self.worker.energy + 2

        self.worker.rest()
        self.worker.rest()

        self.assertEqual(expected_energy, self.worker.energy)

    def test_check_get_info_returns_correct_string(self):
        self.assertEqual('TestGuy has saved 0 money.', self.worker.get_info())

if __name__ == '__main__':
    main()