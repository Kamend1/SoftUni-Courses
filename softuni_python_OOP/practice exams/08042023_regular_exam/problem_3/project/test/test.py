from project.tennis_player import TennisPlayer
from unittest import TestCase, main

class TestTennisPlayer(TestCase):

    def setUp(self):
        self.tp = TennisPlayer("Test", 20, 110.5)

    def test_correct_init(self):
        self.assertEqual("Test", self.tp.name)
        self.assertEqual(20, self.tp.age)
        self.assertEqual(110.5, self.tp.points)
        self.assertEqual([], self.tp.wins)

    def test_name_setter_raises_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.tp.name = "Te"

        expected = "Name should be more than 2 symbols!"
        self.assertEqual(expected, str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.tp.name = "T"

        expected = "Name should be more than 2 symbols!"
        self.assertEqual(expected, str(ve.exception))

    def test_name_setter_success(self):
        self.tp.name = "Grigor"
        self.assertEqual("Grigor", self.tp.name)

    def test_age_setter_raises_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.tp.age = 17

        expected = "Players must be at least 18 years of age!"
        self.assertEqual(expected, str(ve.exception))

    def test_add_new_win_failure(self):
        self.tp.wins = ["Sofia ATP"]
        result = self.tp.add_new_win("Sofia ATP")
        expected = "Sofia ATP has been already added to the list of wins!"
        self.assertEqual(expected, result)
        self.assertEqual(["Sofia ATP"], self.tp.wins)

    def test_add_new_win_success(self):
        self.tp.add_new_win("Sofia ATP")
        self.assertEqual(["Sofia ATP"], self.tp.wins)

    def test_less_than_dunder_method(self):
        other = TennisPlayer("Test 1", 35, 200)
        result = self.tp < other
        expected = 'Test 1 is a top seeded player and he/she is better than Test'
        self.assertEqual(expected, result)
        other.points = 110.5
        result = self.tp < other
        expected = 'Test is a better player than Test 1'
        self.assertEqual(expected, result)
        other.points = 50
        result = self.tp < other
        expected = 'Test is a better player than Test 1'
        self.assertEqual(expected, result)

    def test_string_dunder_method(self):
        self.tp.add_new_win("Sofia ATP")
        self.tp.add_new_win("Plovdiv ATP")
        result = str(self.tp)
        expected = (f"Tennis Player: Test\n"
                    f"Age: 20\n"
                    f"Points: 110.5\n"
                    f"Tournaments won: Sofia ATP, Plovdiv ATP")
        self.assertEqual(expected, result)

if __name__ == '__main__':
    main()