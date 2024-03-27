from unittest import TestCase, main

# from List.extended_list import IntegerList


class TestIntegerList(TestCase):

    def setUp(self):
        self.n_list = IntegerList(1, 2, 3, 4, 5, 6, 7, 8, 9)

    def test_init_correctness(self):
        n_list = IntegerList(1, 2, 3, 4, 5, 6, 7)

        self.assertEqual([1, 2, 3, 4, 5, 6, 7], n_list.get_data())

    def test_add_argument_not_an_integer(self):

        with self.assertRaises(ValueError) as ve:
            self.n_list.add(4.5)

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_add_argument(self):
        expected_result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        self.n_list.add(10)

        self.assertEqual(expected_result, self.n_list.get_data())

    def test_remove_index_when_out_of_range(self):
        with self.assertRaises(IndexError) as ie:
            self.n_list.remove_index(15)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_remove_correct_index(self):
        expected_result = [1, 2, 3, 4, 6, 7, 8, 9]

        self.n_list.remove_index(4)

        self.assertEqual(expected_result, self.n_list.get_data())

    def test_get_incorrect_index(self):
        with self.assertRaises(IndexError) as ie:
            self.n_list.get(15)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_incorrect_index(self):
        with self.assertRaises(IndexError) as ie:
            self.n_list.insert(15, 1000)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_correct_index(self):
        expected_result = 1

        self.assertEqual(expected_result, self.n_list.get_data()[0])

    def test_insert_correct_index(self):
        expected_result = [1, 1000, 2, 3, 4, 5, 6, 7, 8, 9]

        self.n_list.insert(1, 1000)

        self.assertEqual(expected_result, self.n_list.get_data())

    def test_get_biggest_element(self):

        expected_result = 9

        self.assertEqual(expected_result, self.n_list.get_biggest())

    def test_get_index(self):
        result = self.n_list.get_index(1)

        self.assertEqual(0, result)

if __name__ == '__main__':
    main()