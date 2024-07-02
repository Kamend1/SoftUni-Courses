from project.plantation import Plantation
from unittest import TestCase, main

class TestPlantation(TestCase):

    def setUp(self):
        self.p = Plantation(100)

    def test_correct_init(self):
        self.assertEqual(100, self.p.size)
        self.assertEqual({}, self.p.plants)
        self.assertEqual([], self.p.workers)

    def test_setter_size_negative_raises_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.p.size = -1

        expected = "Size must be positive number!"
        self.assertEqual(expected, str(ve.exception))

    def test_setter_size_zero_does_not_raise_exception(self):
        self.p.size = 0
        self.assertEqual(0, self.p.size)

    def test_setter_size_positive_value(self):
        self.p.size = 1
        self.assertEqual(1, self.p.size)

    def test_hire_worker_worker_already_hired_raise_valueerror(self):
        self.p.hire_worker("Ivan")
        self.assertEqual(["Ivan"], self.p.workers)
        self.assertEqual(1, len(self.p.workers))
        with self.assertRaises(ValueError) as ve:
            self.p.hire_worker("Ivan")

        expected = "Worker already hired!"
        self.assertEqual(expected, str(ve.exception))
        self.assertEqual(["Ivan"], self.p.workers)
        self.assertEqual(1, len(self.p.workers))

    def test_hire_worker_worker_success(self):
        result = self.p.hire_worker("Ivan")
        expected = "Ivan successfully hired."
        self.assertEqual(expected, result)
        self.assertEqual(["Ivan"], self.p.workers)
        self.assertEqual(1, len(self.p.workers))
        result = self.p.hire_worker("Pesho")
        expected = "Pesho successfully hired."
        self.assertEqual(expected, result)
        self.assertEqual(["Ivan", "Pesho"], self.p.workers)
        self.assertEqual(2, len(self.p.workers))

    def test_len_dunder_method_plants(self):
        result = len(self.p)
        self.assertEqual(0, result)
        self.p.plants = {"Test": ["plant1", "plant2"], "Test1": ["plant3"]}
        self.assertEqual(3, len(self.p))

    def test_planting_worker_not_in_workers_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.p.planting("Ivan", "plant1")

        expected = "Worker with name Ivan is not hired!"
        self.assertEqual(expected, str(ve.exception))

    def test_planting_worker_no_capacity_raises(self):
        self.p.size = 1
        self.p.hire_worker("Ivan")
        self.p.planting("Ivan", "plant1")
        with self.assertRaises(ValueError) as ve:
            self.p.planting("Ivan", "plant2")

        expected = "The plantation is full!"
        self.assertEqual(expected, str(ve.exception))

    def test_planting_success(self):
        self.p.hire_worker("Ivan")
        self.p.hire_worker("Pesho")
        result = self.p.planting("Ivan", "plant1")
        expected = "Ivan planted it's first plant1."
        self.assertEqual({"Ivan": ["plant1"]}, self.p.plants)
        self.assertEqual(1, len(self.p))
        self.assertEqual(expected, result)
        result = self.p.planting("Ivan", "plant2")
        expected = "Ivan planted plant2."
        self.assertEqual({"Ivan": ["plant1", "plant2"]}, self.p.plants)
        self.assertEqual(2, len(self.p))
        self.assertEqual(expected, result)
        result = self.p.planting("Pesho", "plant3")
        expected = "Pesho planted it's first plant3."
        self.assertEqual({"Ivan": ["plant1", "plant2"], "Pesho": ["plant3"]}, self.p.plants)
        self.assertEqual(3, len(self.p))
        self.assertEqual(expected, result)

    def test_string_dunder(self):
        self.p.hire_worker("Ivan")
        self.p.hire_worker("Pesho")
        self.p.planting("Ivan", "plant1")
        self.p.planting("Ivan", "plant2")
        self.p.planting("Pesho", "plant3")

        result = str(self.p)
        expected = (f"Plantation size: 100\n"
                    f"Ivan, Pesho\n"
                    f"Ivan planted: plant1, plant2\n"
                    f"Pesho planted: plant3")
        self.assertEqual(expected, result)

    def test_represent_dunder(self):
        self.p.hire_worker("Ivan")
        self.p.hire_worker("Pesho")
        expected = (f"Size: 100\n"
                    f"Workers: Ivan, Pesho")
        result = repr(self.p)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()
