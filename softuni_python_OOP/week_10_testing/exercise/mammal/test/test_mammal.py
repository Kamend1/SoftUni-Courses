from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self):
        self.mammal = Mammal("Test", "TestType", "TestSound")

    def test_correct_init(self):
        self.assertEqual("Test", self.mammal.name)
        self.assertEqual("TestType", self.mammal.type)
        self.assertEqual("TestSound", self.mammal.sound)

    def test_if_mammal_makes_correct_sound(self):
        expected_result = "Test makes TestSound"

        self.assertEqual(expected_result, self.mammal.make_sound())

    def test_if_mammal_class_gives_correct_info(self):
        expected_result = "Test is of type TestType"

        self.assertEqual(expected_result, self.mammal.info())

    def test_get_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

if __name__ == '__main__':
    main()