from collections import deque
from unittest import TestCase, main

from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):

    def setUp(self):
        self.rs = RailwayStation("Sofia")

    def test_initialization(self):
        new_rs = RailwayStation("Plovidiv")

        self.assertEqual("Plovidiv", new_rs.name)
        self.assertEqual(deque(), new_rs.arrival_trains)
        self.assertEqual(deque(), new_rs.departure_trains)

    def test_has_attributes(self):
        self.assertTrue(hasattr(self.rs, "name"))
        self.assertTrue(hasattr(self.rs, "arrival_trains"))
        self.assertTrue(hasattr(self.rs, "departure_trains"))

    def test_name_corect(self):
        self.rs.name = "Plovdiv"

        self.assertEqual("Plovdiv", self.rs.name)

    def test_name_raises_valueerror_length_equal_three(self):
        with self.assertRaises(ValueError) as ve:
            self.rs.name = "Plo"

        expected = "Name should be more than 3 symbols!"
        self.assertEqual(expected, str(ve.exception))

    def test_name_raises_valueerror_length_less_than_three(self):
        with self.assertRaises(ValueError) as ve:
            self.rs.name = "Pl"

        expected = "Name should be more than 3 symbols!"
        self.assertEqual(expected, str(ve.exception))

    def test_new_arrival_info_added(self):
        test_info = "Test Test"

        self.rs.new_arrival_on_board(test_info)
        expected_result = deque([test_info])

        self.assertEqual(expected_result, self.rs.arrival_trains)

    def test_train_has_arrived_wrong_train_message(self):
        test_train_1 = "Test Test"
        test_train_2 = "Test Test 2"
        self.rs.new_arrival_on_board(test_train_1)
        self.rs.new_arrival_on_board(test_train_2)
        result = self.rs.train_has_arrived(test_train_2)
        expected = "There are other trains to arrive before Test Test 2."
        self.assertEqual(expected, result)

    def test_train_has_arrived_correct_train(self):
        test_train_1 = "Test Test"
        test_train_2 = "Test Test 2"
        self.rs.new_arrival_on_board(test_train_1)
        self.rs.new_arrival_on_board(test_train_2)
        result = self.rs.train_has_arrived(test_train_1)
        expected = "Test Test is on the platform and will leave in 5 minutes."
        self.assertEqual(deque([test_train_2]), self.rs.arrival_trains)
        self.assertEqual(deque([test_train_1]), self.rs.departure_trains)
        self.assertEqual(expected, result)

    def test_train_has_left_false(self):
        test_train_1 = "Test Test"
        test_train_2 = "Test Test 2"
        self.rs.new_arrival_on_board(test_train_1)
        self.rs.new_arrival_on_board(test_train_2)
        self.rs.train_has_arrived(test_train_1)
        self.rs.train_has_arrived(test_train_2)
        self.assertFalse(self.rs.train_has_left(test_train_2))

    def test_train_has_left_true(self):
        test_train_1 = "Test Test"
        test_train_2 = "Test Test 2"
        self.rs.new_arrival_on_board(test_train_1)
        self.rs.new_arrival_on_board(test_train_2)
        self.rs.train_has_arrived(test_train_1)
        self.rs.train_has_arrived(test_train_2)
        self.assertTrue(self.rs.train_has_left(test_train_1))



if __name__ == '__main__':
    main()