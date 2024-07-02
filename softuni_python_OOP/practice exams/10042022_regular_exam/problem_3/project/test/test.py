from project.movie import Movie
from unittest import TestCase, main

class TestMovie(TestCase):

    def setUp(self):
        self.m = Movie("Test", 2019, 5.5)

    def test_init_correct(self):
        self.assertEqual("Test", self.m.name)
        self.assertEqual(2019, self.m.year)
        self.assertEqual(5.5, self.m.rating)
        self.assertEqual([], self.m.actors)

    def test_name_setter_raises_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.m.name = ""

        expected =  "Name cannot be an empty string!"
        self.assertEqual(expected, str(ve.exception))

    def test_name_setter_correct(self):
        self.m.name = " "
        self.assertEqual(" ", self.m.name)
        self.m.name = "Kamen"
        self.assertEqual("Kamen", self.m.name)

    def test_year_setter_raises_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.m.year = 1886

        expected = "Year is not valid!"
        self.assertEqual(expected, str(ve.exception))

    def test_year_setter_correct(self):
        self.m.year = 1887
        self.assertEqual(1887, self.m.year)
        self.m.year = 2019
        self.assertEqual(2019, self.m.year)

    def test_add_actor_success(self):
        expected = None
        result = self.m.add_actor("Pesho")
        self.assertEqual(expected, result)
        self.assertEqual(1, len(self.m.actors))
        self.assertEqual(["Pesho"], self.m.actors)
        expected = None
        result = self.m.add_actor("Gosho")
        self.assertEqual(expected, result)
        self.assertEqual(2, len(self.m.actors))
        self.assertEqual(["Pesho", "Gosho"], self.m.actors)

    def test_add_actor_failure(self):
        expected = None
        result = self.m.add_actor("Pesho")
        self.assertEqual(expected, result)
        self.assertEqual(1, len(self.m.actors))
        self.assertEqual(["Pesho"], self.m.actors)
        expected = "Pesho is already added in the list of actors!"
        result = self.m.add_actor("Pesho")
        self.assertEqual(expected, result)
        self.assertEqual(1, len(self.m.actors))
        self.assertEqual(["Pesho"], self.m.actors)

    def test_gt_dunder_all_scenarios(self):
        other = Movie("Test1", 2019, 5.6)
        result = self.m > other
        expected = '"Test1" is better than "Test"'
        self.assertEqual(expected, result)
        other.rating = 5.5
        result = self.m > other
        expected = '"Test1" is better than "Test"'
        self.assertEqual(expected, result)
        other.rating = 5.4
        result = self.m > other
        expected = '"Test" is better than "Test1"'
        self.assertEqual(expected, result)

    def test_repr_dunder_method(self):
        self.m.add_actor("Pesho")
        self.m.add_actor("Gosho")

        expected = (f"Name: Test\n"
                    f"Year of Release: 2019\n"
                    f"Rating: 5.50\n"
                    f"Cast: Pesho, Gosho")

        result = repr(self.m)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    main()
