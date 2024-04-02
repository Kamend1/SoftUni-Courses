from project.toy_store import ToyStore
from unittest import TestCase, main

class TestToyStore(TestCase):

    def setUp(self):
        self.ts = ToyStore()

    def test_correct_init(self):
        self.assertEqual({"A": None,
                          "B": None,
                          "C": None,
                          "D": None,
                          "E": None,
                          "F": None,
                          "G": None,}, self.ts.toy_shelf)

    def test_add_toy_wrong_shelf_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.ts.add_toy("H", "train")

        expected = "Shelf doesn't exist!"
        self.assertEqual(expected, str(ex.exception))

    def test_add_toy_when_toy_already_on_shelf_raises_exception(self):
        self.ts.add_toy("A", "train")
        with self.assertRaises(Exception) as ex:
            self.ts.add_toy("A", "train")

        expected = "Toy is already in shelf!"
        self.assertEqual(expected, str(ex.exception))

    def test_add_toy_shelf_already_occupied_by_another_toy_raises_exception(self):
        self.ts.add_toy("A", "train")
        with self.assertRaises(Exception) as ex:
            self.ts.add_toy("A", "doll")

        expected = "Shelf is already taken!"
        self.assertEqual(expected, str(ex.exception))

    def test_add_toy_successfully(self):
        result = self.ts.add_toy("A", "train")
        expected = "Toy:train placed successfully!"
        self.assertEqual(expected, result)
        self.assertEqual("train", self.ts.toy_shelf["A"])

    def test_remove_toy_shelf_does_not_exist(self):
        with self.assertRaises(Exception) as ex:
            self.ts.remove_toy("K","train")

        expected = "Shelf doesn't exist!"
        self.assertEqual(expected, str(ex.exception))

    def test_remove_toy_when_toy_is_not_shelf(self):
        self.ts.add_toy("A", "train")
        with self.assertRaises(Exception) as ex:
            self.ts.remove_toy("A", "doll")

        expected = "Toy in that shelf doesn't exists!"
        self.assertEqual(expected, str(ex.exception))

    def test_remove_toy_successfully(self):
        self.ts.add_toy("A", "train")
        self.assertEqual("train", self.ts.toy_shelf["A"])
        result = self.ts.remove_toy("A", "train")
        expected = "Remove toy:train successfully!"
        self.assertEqual(expected, result)
        self.assertEqual({"A": None,
                          "B": None,
                          "C": None,
                          "D": None,
                          "E": None,
                          "F": None,
                          "G": None, }, self.ts.toy_shelf)

if __name__ == '__main__':
    main()
