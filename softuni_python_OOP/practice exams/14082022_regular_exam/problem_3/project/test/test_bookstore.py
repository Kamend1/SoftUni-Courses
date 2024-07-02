from project.bookstore import Bookstore
from unittest import TestCase, main

class TestBookstore(TestCase):

    def setUp(self):
        self.bs = Bookstore(100)

    def test_correct_init(self):
        self.assertEqual(100, self.bs.books_limit)
        self.assertEqual({}, self.bs.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bs.total_sold_books)

    def test_total_sold_books(self):
        self.bs._Bookstore__total_sold_books = 50
        self.assertEqual(50, self.bs.total_sold_books)

    def test_property(self):
        self.bs._Bookstore__books_limit = 50
        self.assertEqual(50, self.bs.books_limit)

    def test_books_limit_setter_value_zero_raises_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.bs.books_limit = 0

        expected = "Books limit of 0 is not valid"

        self.assertEqual(expected, str(ve.exception))
        self.assertEqual(100, self.bs.books_limit)

    def test_books_limit_value_negative_raises_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.bs.books_limit = -1

        expected = "Books limit of -1 is not valid"

        self.assertEqual(expected, str(ve.exception))
        self.assertEqual(100, self.bs.books_limit)

    def test_book_limit_setter_success(self):
        self.bs.books_limit = 10
        self.assertEqual(10, self.bs.books_limit)

    def test_len_dunder_value(self):
        self.bs.availability_in_store_by_book_titles = {"Test": 10, "Test 1": 5}
        result = len(self.bs)
        self.assertEqual(15, result)

    def test_receive_book_not_enough_capacity_raises_exception(self):
        self.bs.books_limit = 1
        with self.assertRaises(Exception) as ex:
            self.bs.receive_book("Test", 10)

        expected = "Books limit is reached. Cannot receive more books!"
        self.assertEqual(expected, str(ex.exception))
        self.assertEqual({}, self.bs.availability_in_store_by_book_titles)
        self.bs.receive_book("Test1", 1)
        with self.assertRaises(Exception) as ex:
            self.bs.receive_book("Test", 10)

        expected = "Books limit is reached. Cannot receive more books!"
        self.assertEqual(expected, str(ex.exception))
        self.assertEqual({"Test1": 1}, self.bs.availability_in_store_by_book_titles)


    def test_receive_book_when_empty(self):
        result = self.bs.receive_book("Test", 10)
        expected = "10 copies of Test are available in the bookstore."
        self.assertEqual(expected, result)
        self.assertEqual({"Test": 10}, self.bs.availability_in_store_by_book_titles)

    def test_receive_book_two_times_in_a_row(self):
        self.bs.receive_book("Test", 10)
        result = self.bs.receive_book("Test", 10)
        expected = "20 copies of Test are available in the bookstore."
        self.assertEqual(expected, result)
        self.assertEqual({"Test": 20}, self.bs.availability_in_store_by_book_titles)
        result = self.bs.receive_book("Test1", 10)
        expected = "10 copies of Test1 are available in the bookstore."
        self.assertEqual(expected, result)
        self.assertEqual({"Test": 20, "Test1": 10}, self.bs.availability_in_store_by_book_titles)

    def test_sell_book_not_available_title_raises(self):
        self.bs.receive_book("Test", 10)
        with self.assertRaises(Exception) as ex:
            self.bs.sell_book("Test1", 1)

        expected = "Book Test1 doesn't exist!"
        self.assertEqual(expected, str(ex.exception))
        self.assertEqual({"Test": 10}, self.bs.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bs.total_sold_books)

    def test_sell_book_title_available_not_enough_quantity(self):
        self.bs.receive_book("Test", 10)
        with self.assertRaises(Exception) as ex:
            self.bs.sell_book("Test", 11)

        expected = "Test has not enough copies to sell. Left: 10"
        self.assertEqual(expected, str(ex.exception))
        self.assertEqual({"Test": 10}, self.bs.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bs.total_sold_books)

    def test_sell_book_title_available_quantity_available(self):
        self.bs.receive_book("Test", 10)
        result = self.bs.sell_book("Test", 5)
        expected = "Sold 5 copies of Test"
        self.assertEqual(expected, result)
        self.assertEqual({"Test": 5}, self.bs.availability_in_store_by_book_titles)
        self.assertEqual(5, self.bs.total_sold_books)
        self.bs.receive_book("Test1", 10)
        result = self.bs.sell_book("Test1", 5)
        expected = "Sold 5 copies of Test1"
        self.assertEqual(expected, result)
        self.assertEqual({"Test": 5, "Test1": 5}, self.bs.availability_in_store_by_book_titles)
        self.assertEqual(10, self.bs.total_sold_books)

    def test_sell_book_equal_quantity(self):
        self.bs.receive_book("Test", 10)
        result = self.bs.sell_book("Test", 10)
        expected = "Sold 10 copies of Test"
        self.assertEqual(expected, result)
        self.assertEqual(10, self.bs.total_sold_books)
        self.assertEqual({"Test": 0}, self.bs.availability_in_store_by_book_titles)

    def test_string_dunder_method(self):
        self.bs.receive_book("Test", 10)
        self.bs.receive_book("Test1", 10)
        self.bs.sell_book("Test", 5)
        self.bs.sell_book("Test1", 5)
        expected = (f"Total sold books: 10\n"
                    f"Current availability: 10\n"
                    f" - Test: 5 copies\n"
                    f" - Test1: 5 copies")
        result = str(self.bs)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()
