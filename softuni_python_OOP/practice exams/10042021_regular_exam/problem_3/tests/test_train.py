from unittest import TestCase, main

from project.train.train import Train


class TestTrain(TestCase):

    def setUp(self):
        self.train = Train("Test Train", 100)

    def test_init_correct(self):
        self.assertEqual("Test Train", self.train.name)
        self.assertEqual(100, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_add_train_full_error(self):
        self.train.capacity = 1
        self.train.add("Test Passenger")
        with self.assertRaises(ValueError) as ve:
            self.train.add("Test Passenger 1")

        expected = "Train is full"
        self.assertEqual(expected, str(ve.exception))

    def test_add_train_passenger_name_exists(self):
        self.train.add("Test Passenger")
        with self.assertRaises(ValueError) as ve:
            self.train.add("Test Passenger")

        expected = "Passenger Test Passenger Exists"
        self.assertEqual(expected, str(ve.exception))

    def test_add_success(self):
        result = self.train.add("Test Passenger")
        self.assertEqual(1, len(self.train.passengers))
        self.assertEqual(["Test Passenger"], self.train.passengers)
        expected = "Added passenger Test Passenger"
        self.assertEqual(expected, result)

    def test_remove_passenger_not_in_list(self):
        with self.assertRaises(ValueError) as ve:
            self.train.remove("Test Passenger")

        expected = "Passenger Not Found"
        self.assertEqual(expected, str(ve.exception))

    def test_remove_passenger_success(self):
        self.train.add("Test Passenger")
        result = self.train.remove("Test Passenger")
        expected = "Removed Test Passenger"
        self.assertEqual(expected,result)
        self.assertEqual([], self.train.passengers)
        self.assertEqual(0, len(self.train.passengers))

if __name__ == '__main__':
    main()